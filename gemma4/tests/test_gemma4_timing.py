import importlib.util
import json
from pathlib import Path
import sys
import time
import unittest
from unittest.mock import patch


MAIN_DIR = Path(__file__).resolve().parents[1] / "Main"
sys.path.insert(0, str(MAIN_DIR))
SPEC = importlib.util.spec_from_file_location("gemma4_client", MAIN_DIR / "client.py")
client = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(client)


class StreamingResponse:
    status_code = 200

    def raise_for_status(self):
        return None

    def iter_lines(self, decode_unicode=True):
        chunks = [
            {"thinking": "private thought one"},
            {"thinking": "private thought two"},
            {"response": "MESSAGE Agent2: circle square"},
            {
                "done": True,
                "done_reason": "stop",
                "eval_count": 12,
                "total_duration": 100,
                "load_duration": 10,
                "prompt_eval_count": 5,
                "prompt_eval_duration": 20,
                "eval_duration": 70,
            },
        ]
        for chunk in chunks:
            time.sleep(0.002)
            yield json.dumps(chunk)


class OverLimitResponse(StreamingResponse):
    def iter_lines(self, decode_unicode=True):
        visible = " ".join(f"word{index}" for index in range(81))
        yield json.dumps({"thinking": "private"})
        yield json.dumps({"response": visible})
        yield json.dumps({"done": True, "done_reason": "stop", "eval_count": 82})


class Gemma4TimingTest(unittest.TestCase):
    def test_thinking_is_timed_but_not_retained(self):
        with (
            patch.object(client.requests, "post", return_value=StreamingResponse()),
            patch.object(client, "append_diagnostic"),
        ):
            decision = client.generate_agent_reply(
                "Agent1",
                ["circle", "square", "cross"],
                [],
                5,
                0,
                False,
                topology="circle",
                circle_neighbors=["Agent2", "Agent5"],
                preferred_neighbor="Agent2",
                diagnostic_context={"trial_id": 1},
            )

        self.assertEqual(decision["ollama_response"], "MESSAGE Agent2: circle square")
        self.assertEqual(decision["extracted_response"], "MESSAGE Agent2: circle square")
        self.assertGreater(decision["thinking_chars"], 0)
        self.assertGreater(decision["thinking_time_seconds"], 0)
        self.assertGreater(decision["response_time_seconds"], 0)
        self.assertNotIn("ollama_thinking", decision)
        metadata = client.model_response_diagnostics(decision)
        self.assertNotIn("private thought", json.dumps(metadata))

    def test_over_limit_response_is_preserved_and_marked_invalid(self):
        with (
            patch.object(client.requests, "post", return_value=OverLimitResponse()),
            patch.object(client, "append_diagnostic"),
        ):
            decision = client.generate_agent_reply(
                "Agent1",
                ["circle", "square", "cross"],
                [],
                5,
                0,
                False,
                topology="circle",
                circle_neighbors=["Agent2", "Agent5"],
                preferred_neighbor="Agent2",
            )
        self.assertEqual(decision["action"], "invalid")
        self.assertEqual(decision["ollama_response"], decision["extracted_response"])
        self.assertEqual(decision["visible_response_tokens"], 81)
        self.assertIn("exceeded", decision["validation_error"])


if __name__ == "__main__":
    unittest.main()
