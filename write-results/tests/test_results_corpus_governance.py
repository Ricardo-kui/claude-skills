import importlib.util
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "results_corpus_governance.py"
SPEC = importlib.util.spec_from_file_location("results_corpus_governance", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.path.insert(0, str(ROOT / "scripts"))
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ResultsCorpusGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.skill_root = Path(self.temp.name) / "write-results"
        shutil.copytree(ROOT / "econometric-models", self.skill_root / "econometric-models")

    def tearDown(self):
        self.temp.cleanup()

    def write_plan(self, actions):
        path = Path(self.temp.name) / "plan.yaml"
        path.write_text(yaml.safe_dump({"actions": actions}, allow_unicode=True), encoding="utf-8")
        return path

    def load_catalog(self):
        return MODULE.catalog.load_catalog(
            self.skill_root / "econometric-models",
            self.skill_root / "econometric-models" / "_evidence_registry.yaml",
        )

    def test_all_assets_materialize_lifecycle_records(self):
        variants, _ = self.load_catalog()
        self.assertEqual(163, len(variants))
        self.assertTrue(all(item.lifecycle == "active" for item in variants))
        self.assertTrue(all(item.role for item in variants))

    def test_extend_source_is_idempotent(self):
        plan = self.write_plan(
            [
                {
                    "action": "EXTEND_SOURCE",
                    "target_asset_id": "OLS-FE:v24",
                    "source_paper": "new_source_2026",
                },
                {
                    "action": "EXTEND_SOURCE",
                    "target_asset_id": "OLS-FE:v24",
                    "source_paper": "new_source_2026",
                },
            ]
        )
        MODULE.apply_plan(self.skill_root, plan)
        variants, _ = self.load_catalog()
        item = next(item for item in variants if item.asset_id == "OLS-FE:v24")
        self.assertEqual(("new_source_2026",), item.evidence_additions)
        self.assertEqual(163, len(variants))

    def test_promote_merge_and_deprecate_are_enforced(self):
        plan = self.write_plan(
            [
                {
                    "action": "PROMOTE",
                    "target_asset_id": "OLS-FE:v23",
                    "role": "optional_operator",
                    "status": "VERIFIED",
                    "paper_count": 3,
                    "cross_subfields": 2,
                    "verification_basis": "cross_paper_replication",
                },
                {
                    "action": "MERGE",
                    "source_asset_id": "OLS-FE:v24",
                    "target_asset_id": "OLS-FE:v22",
                    "capability_overlap": "Both provide R2 evidence-first navigation.",
                },
                {
                    "action": "DEPRECATE",
                    "target_asset_id": "OLS-FE:v25",
                    "reason": "Superseded by a broader falsification operator.",
                },
            ]
        )
        MODULE.apply_plan(self.skill_root, plan)
        variants, _ = self.load_catalog()
        by_id = {item.asset_id: item for item in variants}
        self.assertEqual("optional_operator", by_id["OLS-FE:v23"].role)
        self.assertEqual("merged", by_id["OLS-FE:v24"].lifecycle)
        self.assertEqual("OLS-FE:v22", by_id["OLS-FE:v24"].merged_into)
        self.assertEqual("deprecated", by_id["OLS-FE:v25"].lifecycle)
        active = MODULE.catalog._select(variants, "OLS-FE", "R2", include_reference=True)
        self.assertNotIn("OLS-FE:v24", {item.asset_id for item in active})
        resolved, notices = MODULE.catalog._resolve_requested_assets(variants, ["OLS-FE:v24"])
        self.assertEqual(["OLS-FE:v22"], [item.asset_id for item in resolved])
        self.assertIn("merged asset OLS-FE:v24", notices[0])

    def test_add_reference_updates_corpus_registry_and_index_together(self):
        plan = self.write_plan(
            [
                {
                    "action": "ADD_REFERENCE",
                    "target_file": "OLS-FE.md",
                    "target_slot": "R6",
                    "title": "Synthetic governance fixture",
                    "source_paper": "fixture_2026",
                    "skeleton": "[Report the unsupported result without upgrading the claim.]",
                    "nearest_neighbor_id": "OLS-FE:v42",
                    "capability_loss_if_merged": "Adds a distinct preregistered-null reporting obligation.",
                }
            ]
        )
        result = MODULE.apply_plan(self.skill_root, plan)
        self.assertEqual(["OLS-FE:v47"], result["added_ids"])
        variants, _ = self.load_catalog()
        self.assertEqual(164, len(variants))
        added = next(item for item in variants if item.asset_id == "OLS-FE:v47")
        self.assertEqual("reference_exemplar", added.role)
        self.assertEqual(("fixture_2026",), added.evidence_additions)
        index = (self.skill_root / "econometric-models" / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("| [OLS-FE](OLS-FE.md) | OLS-FE | 47 |", index)

    def test_invalid_plan_is_non_mutating(self):
        registry = self.skill_root / "econometric-models" / "_evidence_registry.yaml"
        before = registry.read_text(encoding="utf-8")
        plan = self.write_plan(
            [
                {
                    "action": "MERGE",
                    "source_asset_id": "OLS-FE:v24",
                    "target_asset_id": "OLS-FE:v999",
                    "capability_overlap": "fixture",
                }
            ]
        )
        with self.assertRaises(MODULE.GovernanceError):
            MODULE.apply_plan(self.skill_root, plan)
        self.assertEqual(before, registry.read_text(encoding="utf-8"))

    def test_dry_run_validates_without_writing(self):
        registry = self.skill_root / "econometric-models" / "_evidence_registry.yaml"
        before = registry.read_text(encoding="utf-8")
        plan = self.write_plan(
            [
                {
                    "action": "EXTEND_SOURCE",
                    "target_asset_id": "OLS-FE:v24",
                    "source_paper": "dry_run_source",
                }
            ]
        )
        result = MODULE.apply_plan(self.skill_root, plan, dry_run=True)
        self.assertTrue(result["validated"])
        self.assertTrue(result["dry_run"])
        self.assertEqual(before, registry.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
