import importlib.util
from pathlib import Path
import unittest
from unittest.mock import Mock


class IpIdentityTest(unittest.TestCase):
    def test_dashboard_requires_reserved_peer_ip(self):
        root = Path(__file__).resolve().parents[1]
        for relative, class_name in [("Site/dashboard_server.py", "DashboardExperiment")]:
            with self.subTest(server=relative):
                spec = importlib.util.spec_from_file_location("identity_server", root / relative)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                # Bypass initialization to avoid opening ports or starting services.
                import threading
                cls = getattr(module, class_name)
                server = cls.__new__(cls)
                server.lock = threading.RLock()
                server.clients = {}
                server.recv_buffers = {}
                server.turn_order = []
                server.pending_reload_agents = set()
                server.add_event = Mock()
                receive = Mock(return_value={"type": "nickname", "hostname": "wrong-host"})
                send, drop = Mock(), Mock()
                server.recv_json = server._recv = receive
                server.send_json = server._send = send
                server.drop_client = server._drop_client = drop
                for ip, name in module.IP_TO_JETSON.items():
                    sock = Mock()
                    server.handle_new_client(sock, (ip, 12345))
                    self.assertEqual(server.clients[sock]["name"], name)
                unknown = Mock()
                receive.return_value = {"type": "nickname", "hostname": "jetson1"}
                server.handle_new_client(unknown, ("192.168.0.99", 12345))
                self.assertNotIn(unknown, server.clients)
                self.assertTrue(drop.called)


if __name__ == "__main__":
    unittest.main()
