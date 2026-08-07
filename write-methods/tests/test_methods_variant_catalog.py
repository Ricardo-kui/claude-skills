import importlib.util
import copy
import os
import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "methods_variant_catalog.py"
SPEC = importlib.util.spec_from_file_location("methods_variant_catalog", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}


class MethodsVariantCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variants, cls.texts = MODULE.load_catalog()
        cls.by_id = {item.asset_id: item for item in cls.variants}

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=ENV,
        )

    def test_corpus_count_unique_ids_and_slots(self):
        self.assertEqual(192, len(self.variants))
        self.assertEqual(192, len(self.by_id))
        self.assertEqual([], [item.asset_id for item in self.variants if not item.slots])

    def test_every_asset_resolves_to_exact_nonempty_source_block(self):
        for item in self.variants:
            block = self.texts[item.source_file][item.start:item.end]
            self.assertTrue(block.strip(), item.asset_id)
            self.assertTrue(block.lstrip().startswith("### 变体"), item.asset_id)

    def test_slot_normalization_handles_ranges_qualitative_and_cross_skill_tags(self):
        self.assertEqual(
            ("M2", "M3", "M4", "M5", "M6", "M7"),
            self.by_id["实验:v1"].slots,
        )
        self.assertEqual(("Q6", "Q7"), self.by_id["定性过程研究:v4"].slots)
        self.assertEqual(("M3",), self.by_id["事件历史+事件研究:v12"].slots)
        self.assertNotIn("M15", {slot for item in self.variants for slot in item.slots})

    def test_evidence_roles_are_conservative(self):
        self.assertEqual("core_operator", self.by_id["生存分析:v1"].role)
        self.assertEqual("reference_exemplar", self.by_id["两阶段模型:v3"].role)
        self.assertEqual("reference_exemplar", self.by_id["IV-2SLS:v8"].role)
        for item in self.variants:
            if "emerging" in item.evidence.lower() or "待第二篇" in item.evidence:
                self.assertEqual("reference_exemplar", item.role, item.asset_id)

    def test_registry_is_the_only_promotion_authority(self):
        promoted = [item for item in self.variants if item.role != "reference_exemplar"]
        self.assertEqual(9, len(promoted))
        self.assertEqual(6, sum(item.role == "core_operator" for item in promoted))
        self.assertEqual(3, sum(item.role == "optional_operator" for item in promoted))
        self.assertTrue(all(item.paper_count is not None for item in promoted))
        self.assertTrue(all(item.promotion_basis for item in promoted))

    def test_reference_requires_opt_in_and_is_capped_at_two(self):
        denied = self.run_cli("render", "--id", "两阶段模型:v3")
        self.assertEqual(2, denied.returncode)
        allowed = self.run_cli("render", "--id", "两阶段模型:v3", "--allow-reference")
        self.assertEqual(0, allowed.returncode)
        self.assertIn("Heckman", allowed.stdout)
        three = self.run_cli(
            "render",
            "--id", "两阶段模型:v3",
            "--id", "两阶段模型:v4",
            "--id", "两阶段模型:v5",
            "--allow-reference",
        )
        self.assertEqual(2, three.returncode)
        self.assertIn("At most two reference exemplars", three.stderr)

    def test_render_allows_four_but_rejects_five(self):
        four_ids = ["生存分析:v1", "生存分析:v4", "面板数据-OLS:v1", "面板数据-OLS:v2"]
        four_args = sum((["--id", asset_id] for asset_id in four_ids), [])
        self.assertEqual(0, self.run_cli("render", *four_args).returncode)
        five = self.run_cli("render", *(four_args + ["--id", "非线性模型:v13"]))
        self.assertEqual(2, five.returncode)
        self.assertIn("At most four variants", five.stderr)

    def test_empty_default_menu_is_normal_but_invalid_inputs_fail(self):
        empty = self.run_cli("list", "--design-type", "两阶段模型", "--slot", "M7")
        self.assertEqual(0, empty.returncode)
        self.assertIn("No default-eligible variants", empty.stderr)
        unknown = self.run_cli("list", "--design-type", "not-a-design", "--slot", "M7")
        self.assertEqual(2, unknown.returncode)
        bad_slot = self.run_cli("list", "--design-type", "生存分析", "--slot", "M15")
        self.assertEqual(2, bad_slot.returncode)

    def test_documented_aliases_and_supplement_slot_are_accepted(self):
        alias = self.run_cli(
            "list",
            "--design-type", "IV/2SLS",
            "--slot", "M7",
            "--include-reference",
        )
        self.assertEqual(0, alias.returncode)
        self.assertIn("IV-2SLS:v8", alias.stdout)
        supplement = self.run_cli(
            "list",
            "--design-type", "面板数据/OLS",
            "--slot", "M7补充",
        )
        self.assertEqual(0, supplement.returncode)
        self.assertIn("slot-M7-supplement.md only", supplement.stderr)

    def test_duplicate_asset_ids_fail_loudly(self):
        result = self.run_cli(
            "render",
            "--id", "生存分析:v1",
            "--id", "生存分析:v1",
        )
        self.assertEqual(2, result.returncode)
        self.assertIn("Duplicate asset IDs", result.stderr)

    def test_registry_snapshot_drift_fails(self):
        registry = MODULE._load_registry()
        registry = copy.deepcopy(registry)
        registry["meta"]["total_variants"] -= 1
        with self.assertRaisesRegex(ValueError, "total_variants"):
            MODULE._validate_registry_snapshot(registry, self.variants, self.texts)

    def test_index_counts_match_live_catalog(self):
        index = (ROOT / "econometric-models" / "INDEX.md").read_text(encoding="utf-8")
        counts = [int(value) for value in re.findall(r"^\| \[[^]]+\]\([^)]+\) \|[^|]+\|\s*(\d+)\s*\|", index, re.M)]
        self.assertEqual(24, len(counts))
        self.assertEqual(len(self.variants), sum(counts))

    def test_distill_protocol_uses_consolidation_actions_and_audit(self):
        distill = (ROOT.parent / "distill-methods-exemplar" / "SKILL.md").read_text(encoding="utf-8")
        for action in ("NONE", "REUSE", "EXTEND_SOURCE", "ADD_REFERENCE", "PROMOTE"):
            self.assertIn(action, distill)
        self.assertIn("methods_variant_catalog.py audit", distill)
        self.assertNotRegex(distill, r'action:\s*"(?:ADD|EXTEND|REPLACE|SKIP)"')

    def test_targeted_listing_is_materially_smaller_than_largest_source(self):
        source = self.texts["面板数据-OLS.md"]
        items = [item for item in self.variants if item.design_type == "面板数据-OLS" and "M7" in item.slots]
        listing = "\n".join(f"{item.asset_id}\t{item.role}\t{item.title}" for item in items)
        self.assertLess(len(listing), len(source) * 0.5)

    def test_unknown_asset_id_fails_loudly(self):
        result = self.run_cli("render", "--id", "面板数据-OLS:v999")
        self.assertEqual(2, result.returncode)
        self.assertIn("Unknown asset ID", result.stderr)


if __name__ == "__main__":
    unittest.main()
