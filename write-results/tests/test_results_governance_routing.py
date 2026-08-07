import importlib.util
import sys
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "results_variant_catalog.py"
CASES = Path(__file__).with_name("governance_routing_cases.yaml")
SPEC = importlib.util.spec_from_file_location("results_variant_catalog_governance", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ResultsGovernanceRoutingTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variants, cls.texts = MODULE.load_catalog()
        cls.cases = yaml.safe_load(CASES.read_text(encoding="utf-8"))["cases"]
        cls.known_types = {Path(name).stem.casefold(): Path(name).stem for name in cls.texts}

    def test_cross_result_type_default_routes(self):
        for case in self.cases:
            with self.subTest(case=case["id"]):
                result_type = MODULE._canonical_result_type(case["result_type"], self.known_types)
                slot = MODULE._canonical_slot(case["slot"])
                self.assertIsNotNone(result_type)
                self.assertIsNotNone(slot)
                selected = MODULE._select(self.variants, result_type, slot, include_reference=False)
                self.assertEqual(case["expected_default_ids"], [item.asset_id for item in selected])

    def test_core_only_is_a_valid_route(self):
        core_only = [case for case in self.cases if not case["expected_default_ids"]]
        self.assertGreaterEqual(len(core_only), 2)
        for case in core_only:
            result_type = MODULE._canonical_result_type(case["result_type"], self.known_types)
            slot = MODULE._canonical_slot(case["slot"])
            references = MODULE._select(self.variants, result_type, slot, include_reference=True)
            self.assertTrue(references)
            self.assertTrue(all(item.role == "reference_exemplar" for item in references))

    def test_default_operators_are_functionally_sparse(self):
        pairs = {}
        for item in self.variants:
            if item.role == "reference_exemplar":
                continue
            for slot in item.slots:
                pairs.setdefault((item.result_type, slot), []).append(item)
        self.assertTrue(pairs)
        self.assertLessEqual(max(len(items) for items in pairs.values()), 4)


if __name__ == "__main__":
    unittest.main()
