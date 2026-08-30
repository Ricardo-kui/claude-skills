import importlib.util
import copy
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "results_variant_catalog.py"
SPEC = importlib.util.spec_from_file_location("results_variant_catalog", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class ResultsVariantCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variants, cls.texts = MODULE.load_catalog()
        cls.by_id = {item.asset_id: item for item in cls.variants}

    def test_corpus_count_and_unique_ids(self):
        self.assertEqual(163, len(self.variants))
        self.assertEqual(163, len(self.by_id))

    def test_every_asset_resolves_to_nonempty_source_text(self):
        for item in self.variants:
            block = self.texts[item.source_file][item.start:item.end]
            self.assertTrue(block.strip(), item.asset_id)
            self.assertTrue(block.lstrip().startswith("#"), item.asset_id)

    def test_all_assets_have_current_slots(self):
        unclassified = [item.asset_id for item in self.variants if not item.slots]
        self.assertEqual([], unclassified)

    def test_single_paper_asset_is_reference_only(self):
        self.assertEqual("reference_exemplar", self.by_id["OLS-FE:v24"].role)

    def test_replicated_asset_remains_in_default_menu(self):
        self.assertEqual("optional_operator", self.by_id["生存分析:v1"].role)

    def test_emerging_assets_never_enter_default_menu(self):
        for item in self.variants:
            if "emerging" in item.evidence.lower() or "待第二篇" in item.evidence:
                self.assertEqual("reference_exemplar", item.role, item.asset_id)

    def test_registry_is_the_only_promotion_authority(self):
        promoted = [item for item in self.variants if item.role != "reference_exemplar"]
        self.assertEqual(4, len(promoted))
        self.assertEqual(0, sum(item.role == "core_operator" for item in promoted))
        self.assertEqual(4, sum(item.role == "optional_operator" for item in promoted))
        self.assertTrue(all(item.paper_count is not None for item in promoted))
        self.assertTrue(all(item.promotion_basis for item in promoted))
        self.assertEqual("reference_exemplar", self.by_id["生存分析:v2"].role)

    def test_sem_legacy_sections_are_indexed(self):
        sem = [item for item in self.variants if item.result_type == "SEM-moderated-mediation"]
        self.assertEqual(7, len(sem))
        self.assertIn("R7", self.by_id["SEM-moderated-mediation:v4"].slots)

    def test_reference_render_requires_explicit_opt_in(self):
        denied = subprocess.run(
            [sys.executable, str(SCRIPT), "render", "--id", "OLS-FE:v24"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, denied.returncode)
        allowed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "render",
                "--id",
                "OLS-FE:v24",
                "--allow-reference",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(0, allowed.returncode)
        self.assertIn("Heckman 两阶段表格导航", allowed.stdout)

    def test_unknown_id_fails_loudly(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "render", "--id", "OLS-FE:v999"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("Unknown asset ID", result.stderr)

    def test_empty_default_menu_is_normal_but_unknown_type_fails(self):
        empty = subprocess.run(
            [sys.executable, str(SCRIPT), "list", "--result-type", "OLS-FE", "--slot", "R2"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(0, empty.returncode)
        self.assertIn("No default-eligible variants", empty.stderr)
        unknown = subprocess.run(
            [sys.executable, str(SCRIPT), "list", "--result-type", "not-a-model", "--slot", "R2"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, unknown.returncode)
        self.assertIn("Unknown result type", unknown.stderr)

    def test_documented_result_type_aliases_are_accepted(self):
        cases = (
            ("OLS/FE", "OLS-FE:v24", "R2"),
            ("fixed effects", "OLS-FE:v2", "R7"),
            ("Logit/Probit/Ordered Probit", "Logit-Probit-Ordered-Probit:v9", "R3"),
            ("ordered probit", "Logit-Probit-Ordered-Probit:v9", "R3"),
            ("Cox", "生存分析:v1", "R3"),
            ("AFT", "生存分析:v1", "R3"),
            ("negative binomial", "计数模型:v1", "R3"),
            ("IV/2SLS", "IV-2SLS:v3", "R2"),
            ("同伴效应/网络效应", None, "R3"),
            ("定性过程研究/定性发现", "定性过程研究:v1", "F1"),
        )
        for result_type, expected, slot in cases:
            with self.subTest(result_type=result_type):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "list", "--result-type", result_type, "--slot", slot, "--include-reference"],
                    capture_output=True,
                    text=True,
                    encoding="utf-8",
                    env={**os.environ, "PYTHONIOENCODING": "utf-8"},
                )
                self.assertEqual(0, result.returncode)
                if expected:
                    self.assertIn(expected, result.stdout)

    def test_duplicate_asset_ids_fail_loudly(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "render", "--id", "OLS-FE:v2", "--id", "OLS-FE:v2"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("Duplicate asset IDs", result.stderr)

    def test_registry_snapshot_drift_fails(self):
        registry = copy.deepcopy(MODULE._load_registry())
        registry["meta"]["total_variants"] -= 1
        with self.assertRaisesRegex(ValueError, "total_variants"):
            MODULE._validate_registry_snapshot(registry, self.variants, self.texts)

    def test_index_counts_match_live_catalog(self):
        index = (ROOT / "corpus" / "INDEX.md").read_text(encoding="utf-8")
        counts = [
            int(value)
            for value in re.findall(r"^\| \[[^]]+\]\([^)]+\) \|[^|]+\|\s*(\d+)\s*\|", index, re.M)
        ]
        self.assertEqual(20, len(counts))
        self.assertEqual(len(self.variants), sum(counts))

    def test_registry_semantic_ids_are_unique(self):
        registry = MODULE._load_registry()
        semantic_ids = []

        def collect(value):
            if isinstance(value, dict):
                if isinstance(value.get("id"), str):
                    semantic_ids.append(value["id"])
                for child in value.values():
                    collect(child)
            elif isinstance(value, list):
                for child in value:
                    collect(child)

        collect(registry)
        self.assertEqual(len(semantic_ids), len(set(semantic_ids)))

    def test_distill_protocol_defaults_to_reuse_and_consolidation(self):
        distill = (ROOT.parent / "distill-results-exemplar" / "SKILL.md").read_text(encoding="utf-8")
        for action in (
            "NONE", "REUSE", "EXTEND_SOURCE", "ADD_REFERENCE",
            "PROPOSE_OPERATOR", "PROMOTE", "MERGE", "DEPRECATE",
        ):
            self.assertIn(action, distill)
        self.assertIn("capability_loss_if_merged", distill)
        self.assertIn("results_corpus_governance.py apply-plan", distill)
        self.assertIn("catalog `audit`", distill)
        self.assertNotRegex(distill, r'action:\s*"(?:ADD|EXTEND|REPLACE|SKIP)"')

    def test_render_cap_allows_four_but_rejects_five(self):
        base = [sys.executable, str(SCRIPT), "render"]
        four_ids = [
            "生存分析:v1",
            "Logit-Probit-Ordered-Probit:v9",
            "Logit-Probit-Ordered-Probit:v12",
            "OLS-FE:v2",
        ]
        four = subprocess.run(
            base + sum((["--id", asset_id] for asset_id in four_ids), []),
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(0, four.returncode)
        five = subprocess.run(
            base
            + sum((["--id", asset_id] for asset_id in four_ids + ["OLS-FE:v1"]), []),
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, five.returncode)
        self.assertIn("At most four variants", five.stderr)

    def test_reference_cap_is_two(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "render",
                "--id",
                "OLS-FE:v16",
                "--id",
                "OLS-FE:v19",
                "--id",
                "OLS-FE:v24",
                "--allow-reference",
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("At most two reference exemplars", result.stderr)


if __name__ == "__main__":
    unittest.main()
