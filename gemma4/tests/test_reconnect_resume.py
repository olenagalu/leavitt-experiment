import importlib.util
import json
import socket
import threading
import time
import unittest
from pathlib import Path


SERVER_PATH = Path(__file__).resolve().parents[1] / "Site" / "dashboard_server.py"
SPEC = importlib.util.spec_from_file_location("gemma4_dashboard_server", SERVER_PATH)
dashboard_server = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dashboard_server)


class ReconnectResumeTest(unittest.TestCase):
    def setUp(self):
        self.sockets = []
        self.experiment = dashboard_server.DashboardExperiment("127.0.0.1", 0)
        self.experiment.add_event = lambda _kind, _payload: None
        self.experiment.trial_active = True
        self.experiment.active_trial_id = 7
        self.experiment.topology = "circle"
        self.experiment.num_agents = 2
        self.experiment.cards = {
            "jetson1": ["circle", "square"],
            "jetson2": ["circle", "cross"],
        }
        self.experiment.circle_neighbors_by_name = {
            "jetson1": ["jetson2"],
            "jetson2": ["jetson1"],
        }
        self.experiment.trial_routes = [
            {"sender": "Agent1", "receiver": "Agent2", "message": "circle square"},
            {"sender": "Agent2", "receiver": "Agent1", "message": "circle cross"},
        ]

    def tearDown(self):
        for sock in self.sockets:
            sock.close()

    def socket_pair(self):
        pair = socket.socketpair()
        self.sockets.extend(pair)
        return pair

    def test_reconnect_restores_same_trial_and_history(self):
        old1_server, _old1_client = self.socket_pair()
        old2_server, _old2_client = self.socket_pair()
        self.experiment.clients = {
            old1_server: {"name": "jetson1", "hostname": "jetson1"},
            old2_server: {"name": "jetson2", "hostname": "jetson2"},
        }
        previous = {"jetson1": old1_server, "jetson2": old2_server}
        self.experiment.clients.pop(old2_server)

        result = {}
        waiter = threading.Thread(
            target=lambda: result.setdefault(
                "sockets",
                self.experiment.wait_for_trial_reconnect(
                    ["jetson1", "jetson2"], previous, 7
                ),
            )
        )
        waiter.start()
        time.sleep(0.05)
        new2_server, new2_client = self.socket_pair()
        with self.experiment.lock:
            self.experiment.clients[new2_server] = {
                "name": "jetson2",
                "hostname": "jetson2",
            }

        waiter.join(timeout=3)
        self.assertFalse(waiter.is_alive())
        self.assertIs(result["sockets"]["jetson2"], new2_server)

        payloads = [
            json.loads(line)
            for line in new2_client.recv(65536).decode().strip().splitlines()
        ]
        self.assertEqual(payloads[0]["type"], "experiment_start")
        self.assertTrue(payloads[0]["resume"])
        self.assertEqual(payloads[0]["trial_id"], 7)
        self.assertEqual(
            payloads[1:],
            [
                {
                    "type": "chat",
                    "trial_id": 7,
                    "sender": "Agent1",
                    "text": "circle square",
                },
                {
                    "type": "chat",
                    "trial_id": 7,
                    "sender": "Agent2",
                    "text": "To Agent1: circle cross",
                },
            ],
        )
        self.assertEqual(
            self.experiment.trial_disconnects[0]["missing_agents"], ["Agent2"]
        )
        self.assertGreater(self.experiment.trial_pause_total_seconds, 0)

    def test_report_includes_reconnect_details(self):
        trial = {
            "success": True,
            "submitted_answer": "circle",
            "correct_answer": "circle",
            "total_messages": 4,
            "time_seconds": 12.5,
            "temperature": 0.1,
            "disconnect_count": 1,
            "disconnect_pause_seconds": 8.25,
            "disconnects": [{
                "missing_agents": ["Agent3"],
                "started_at": "2026-09-11T12:00:00+00:00",
                "resumed_at": "2026-09-11T12:00:08+00:00",
                "duration_seconds": 8.25,
            }],
            "trial_wall_time_seconds": 20.75,
            "trial_active_time_seconds": 12.5,
            "completed_generation_count": 2,
            "total_thinking_time_seconds": 7.0,
            "average_thinking_time_seconds": 3.5,
            "total_visible_response_time_seconds": 1.0,
            "average_visible_response_time_seconds": 0.5,
            "total_generation_time_seconds": 8.0,
        }
        report = dashboard_server.build_batch_report(
            "circle", "test", [trial], [], 50, 0.1
        )
        self.assertIn("Reconnect pauses: 1", report)
        self.assertIn("Agent3", report)
        self.assertIn("Paused time is excluded", report)
        self.assertIn("Gemma 4 timing by trial", report)
        self.assertIn("Average Gemma 4 thinking time per response: 3.500 seconds", report)

if __name__ == "__main__":
    unittest.main()
