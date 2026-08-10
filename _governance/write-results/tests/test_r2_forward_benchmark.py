from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parent.parent
MODULE_PATH = SKILL_ROOT / "scripts" / "r2_forward_benchmark.py"
SPEC = importlib.util.spec_from_file_location("r2_forward_benchmark", MODULE_PATH)
assert SPEC and SPEC.loader
benchmark = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = benchmark
SPEC.loader.exec_module(benchmark)


class R2ForwardBenchmarkTests(unittest.TestCase):
    def test_benchmark_is_valid_and_gold_does_not_leak(self) -> None:
        self.assertEqual(benchmark.validate_benchmark(), [])

    def test_manifest_contains_blind_randomized_pairs(self) -> None:
        manifest = benchmark.emit_manifest(20260806)
        self.assertEqual(len(manifest["runs"]), 16)
        self.assertEqual(len({run["run_id"] for run in manifest["runs"]}), 16)
        for run in manifest["runs"]:
            self.assertNotIn("expected_first_asset", run["request"])
            self.assertNotIn("r2_forward_gold", run["request"])

    def test_manifest_is_deterministic_for_same_seed(self) -> None:
        self.assertEqual(benchmark.emit_manifest(11), benchmark.emit_manifest(11))
        self.assertNotEqual(benchmark.emit_manifest(11), benchmark.emit_manifest(12))

    def test_route_scoring_uses_private_gold(self) -> None:
        manifest = benchmark.emit_manifest(20260806)
        gold = benchmark.load_yaml(benchmark.GOLD_PATH)["cases"]
        responses = {}
        for run in manifest["runs"]:
            if run["arm"] == "indexed":
                expected = gold[run["case_id"]]
                responses[run["run_id"]] = (
                    "ROUTING_JSON: "
                    + json.dumps(
                        {
                            "features": expected["expected_features"],
                            "selected_asset_ids": [expected["expected_first_asset"]],
                        }
                    )
                    + "\nR2_OUTPUT:\nTest paragraph."
                )
            else:
                responses[run["run_id"]] = "R2_OUTPUT:\nLegacy paragraph."
        report = benchmark.evaluate_routes(manifest, responses)
        self.assertEqual(report["passed"], 8)
        self.assertEqual(report["accuracy"], 1.0)

    def test_blind_bundle_removes_routing_and_arm_labels(self) -> None:
        manifest = benchmark.emit_manifest(20260806)
        responses = {}
        for run in manifest["runs"]:
            routing = (
                'ROUTING_JSON: {"features": [], "selected_asset_ids": ["r2_ols_model_sequence"]}\n'
                if run["arm"] == "indexed"
                else ""
            )
            responses[run["run_id"]] = routing + f"R2_OUTPUT:\nBody {run['run_id']}"
        bundle = benchmark.blind_eval_bundle(manifest, responses, seed=99)
        self.assertEqual(len(bundle["pairs"]), 8)
        serialized = json.dumps(bundle, ensure_ascii=False)
        self.assertNotIn("ROUTING_JSON", serialized)
        self.assertNotIn('"arm"', serialized)
        self.assertNotIn('"run_id"', serialized)

    def test_response_loader_rejects_duplicate_run_ids(self) -> None:
        payload = {
            "responses": [
                {"run_id": "same", "response": "R2_OUTPUT:\nA"},
                {"run_id": "same", "response": "R2_OUTPUT:\nB"},
            ]
        }
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "responses.json"
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaises(benchmark.BenchmarkError):
                benchmark.load_responses(path)


if __name__ == "__main__":
    unittest.main()
