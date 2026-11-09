import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch


SERVER_PATH = Path(__file__).resolve().parents[1] / "Site" / "dashboard_server.py"
SPEC = importlib.util.spec_from_file_location("gemma4_maintenance_server", SERVER_PATH)
dashboard_server = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(dashboard_server)


class OllamaMaintenanceTest(unittest.TestCase):
    def test_circle_study_uses_all_five_requested_temperatures(self):
        self.assertEqual(
            dashboard_server.CIRCLE_STUDY_TEMPERATURES,
            (0.0, 0.05, 0.1, 0.2, 1.0),
        )

    def test_single_topology_studies_match_circle_temperatures(self):
        for topology, topologies, temperatures in (
            ("y", dashboard_server.Y_STUDY_TOPOLOGIES, dashboard_server.Y_STUDY_TEMPERATURES),
            ("wheel", dashboard_server.WHEEL_STUDY_TOPOLOGIES, dashboard_server.WHEEL_STUDY_TEMPERATURES),
            ("chain", dashboard_server.CHAIN_STUDY_TOPOLOGIES, dashboard_server.CHAIN_STUDY_TEMPERATURES),
        ):
            with self.subTest(topology=topology):
                self.assertEqual(topologies, (topology,))
                self.assertEqual(temperatures, dashboard_server.CIRCLE_STUDY_TEMPERATURES)

    def test_wheel_temperature_1_study_uses_only_temperature_1(self):
        self.assertEqual(dashboard_server.WHEEL_STUDY_TOPOLOGIES, ("wheel",))
        self.assertEqual(
            dashboard_server.WHEEL_TEMPERATURE_1_STUDY_TEMPERATURES,
            (1.0,),
        )

    def test_wheel_temperature_1_study_creates_one_50_trial_batch(self):
        experiment = dashboard_server.DashboardExperiment("127.0.0.1", 0)
        experiment.clients = {
            object(): {
                "name": f"jetson{number}",
                "hostname": f"jetson{number}",
                "model_name": dashboard_server.EXPECTED_STUDY_MODEL,
            }
            for number in range(1, 6)
        }

        with (
            tempfile.TemporaryDirectory() as data_root,
            patch.object(dashboard_server, "DATA_ROOT", Path(data_root)),
            patch.object(experiment, "schedule_next_auto_trial") as schedule_trial,
            patch.object(experiment, "start_study_watchdog") as start_watchdog,
        ):
            ok, message = experiment.start_full_study(
                ollama_options={"temperature": 0.2},
                study_kind="wheel_temperature_1",
            )

        self.assertTrue(ok, message)
        self.assertEqual(experiment.full_study_kind, "wheel_temperature_1")
        self.assertEqual(experiment.full_study_topologies, ["wheel"])
        self.assertEqual(len(experiment.full_study_batches), 1)
        self.assertEqual(experiment.full_study_batches[0]["topology"], "wheel")
        self.assertEqual(experiment.full_study_batches[0]["temperature"], 1.0)
        self.assertEqual(experiment.auto_trial_target, 50)
        self.assertEqual(experiment.auto_ollama_options["temperature"], 1.0)
        schedule_trial.assert_called_once()
        start_watchdog.assert_called_once()

    def test_restart_is_due_only_at_unfinished_25_trial_intervals(self):
        self.assertFalse(dashboard_server.ollama_restart_due(0, 50))
        self.assertTrue(dashboard_server.ollama_restart_due(25, 50))
        self.assertFalse(dashboard_server.ollama_restart_due(50, 50))

    def test_warmup_uses_gemma4_without_thinking_and_keeps_model_loaded(self):
        experiment = dashboard_server.DashboardExperiment("127.0.0.1", 0)
        experiment.add_event = lambda _kind, _payload: None
        experiment.auto_trials = True
        generation = experiment.auto_trial_generation
        calls = []

        def completed_run(command, **kwargs):
            calls.append((command, kwargs))
            return subprocess.CompletedProcess(command, 0, stdout='{"done": true}', stderr="")

        with (
            patch.object(dashboard_server, "JETSON_HOSTNAMES", ("jetson1",)),
            patch.object(dashboard_server.subprocess, "run", side_effect=completed_run),
        ):
            ok, message = experiment.warm_ollama_for_study(generation, after_trial=25)

        self.assertTrue(ok, message)
        payload = json.loads(calls[0][1]["input"])
        self.assertEqual(payload["model"], "gemma4:e2b-it-qat")
        self.assertFalse(payload["think"])
        self.assertEqual(payload["keep_alive"], -1)


if __name__ == "__main__":
    unittest.main()
