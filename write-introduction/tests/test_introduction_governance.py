from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
import json
from argparse import Namespace
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = SKILL_ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import introduction_asset_catalog as catalog
import introduction_corpus_governance as governance
import introduction_governance_benchmark as benchmark


class IntroductionGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory(prefix="intro-governance-test-")
        self.root = Path(self.tempdir.name) / "write-introduction"
        shutil.copytree(SKILL_ROOT, self.root)

    def tearDown(self):
        self.tempdir.cleanup()

    def _plan(self, rows: list[dict]) -> Path:
        path = Path(self.tempdir.name) / "plan.yaml"
        path.write_text(
            yaml.safe_dump({"actions": rows}, allow_unicode=True, sort_keys=False),
            encoding="utf-8",
        )
        return path

    def _registry(self) -> dict:
        path = self.root / "academic-writing-corpus" / "_evidence_registry.yaml"
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_inventory_and_duplicate_heading_ids_are_stable(self):
        parents, variants, _ = catalog.load_catalog()
        self.assertEqual(94, len(parents))
        self.assertEqual(345, len(variants))
        self.assertEqual(439, len({item.asset_id for item in [*parents, *variants]}))
        ids = {item.asset_id for item in variants}
        self.assertIn("literature-turns:literature-turn-templates:vD", ids)
        self.assertIn("literature-turns:literature-turn-templates:vD~2", ids)
        self.assertIn("previews:robustness-preview:vH-紧凑版", ids)

    def test_every_exact_variant_defaults_to_reference(self):
        parents, variants, _ = catalog.load_catalog()
        self.assertEqual({"reference_exemplar"}, {item.role for item in variants})
        by_id = {item.asset_id: item for item in parents}
        self.assertEqual("reference_strategy", by_id["hooks:07-cost-benefit-tension"].role)
        self.assertEqual("generative_strategy", by_id["hooks:01-cross-disciplinary-analogy"].role)

    def test_representative_menus_are_bounded_and_parent_local(self):
        parents, variants, _ = catalog.load_catalog()
        registry = catalog._load_registry()
        menus = registry["asset_governance"]["representative_reference_menus"]
        parent_ids = {item.asset_id for item in parents}
        by_id = {item.asset_id: item for item in variants}
        self.assertEqual(5, len(menus))
        for parent_id, menu in menus.items():
            self.assertIn(parent_id, parent_ids)
            self.assertLessEqual(len(menu), 5)
            self.assertEqual(len(menu), len(set(menu)))
            self.assertTrue(all(by_id[item].parent_id == parent_id for item in menu))

    def test_render_rejects_five_exact_assets(self):
        args = Namespace(
            id=[
                "hooks:03-data-shock:vA",
                "hooks:03-data-shock:vB",
                "hooks:03-data-shock:vC",
                "hooks:03-data-shock:vG",
                "hooks:03-data-shock:vK",
            ],
            allow_many=False,
            allow_reference=True,
        )
        with self.assertRaisesRegex(ValueError, "At most 4"):
            catalog.command_render(args)

    def test_parent_render_excludes_reference_blocks(self):
        output = StringIO()
        args = Namespace(
            id=["hooks:03-data-shock"],
            allow_many=False,
            allow_reference=False,
        )
        with redirect_stdout(output):
            catalog.command_render(args)
        rendered = output.getvalue()
        full = (SKILL_ROOT / "academic-writing-corpus" / "hooks" / "03-data-shock.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("### 变体", rendered)
        self.assertLess(len(rendered), len(full) / 2)

    def test_gap_and_conversation_axes_remain_independent(self):
        routing_text = (
            SKILL_ROOT / "academic-writing-corpus" / "_routing_tables.yaml"
        ).read_text(encoding="utf-8")
        routing = yaml.safe_load(routing_text)
        self.assertEqual(
            {"Incompleteness", "Inadequacy", "Incommensurability"},
            set(routing["gap_types"]),
        )
        self.assertEqual(
            {"Progressive_Coherence", "Synthesized_Coherence", "Non_Coherence"},
            set(routing["conversation_strategies"]),
        )
        self.assertNotIn("registry_status", routing_text)
        self.assertTrue(
            all("conversation_hint_only" in row for row in routing["gap_types"].values())
        )

    def test_evidence_statuses_follow_declared_threshold(self):
        registry = catalog._load_registry()
        for entries in registry["evidence"].values():
            if not isinstance(entries, dict):
                continue
            for entry in entries.values():
                if not isinstance(entry, dict) or not isinstance(entry.get("paper_count"), int):
                    continue
                papers = entry.get("papers", [])
                journals = {
                    paper.rsplit("(", 1)[-1].rstrip(")").strip()
                    for paper in papers
                    if "(" in str(paper)
                }
                count = entry["paper_count"]
                expected = "ROBUST" if count >= 5 and len(journals) >= 2 else (
                    "VERIFIED" if count >= 3 else "EMERGING"
                )
                self.assertEqual(expected, entry.get("status"))

    def test_extend_source_is_idempotent(self):
        plan = self._plan(
            [{
                "action": "EXTEND_SOURCE",
                "target_asset_id": "hooks:03-data-shock:vA",
                "source_paper": "audit_paper_2026 (AMJ)",
            }]
        )
        governance.apply_plan(self.root, plan)
        governance.apply_plan(self.root, plan)
        record = self._registry()["asset_governance"]["variant_overrides"]["hooks:03-data-shock:vA"]
        self.assertEqual(["audit_paper_2026 (AMJ)"], record["evidence_additions"])

    def test_record_validation_is_idempotent(self):
        plan = self._plan(
            [{
                "action": "RECORD_VALIDATION",
                "target_asset_id": "hooks:03-data-shock",
                "validation_id": "project:2026-08-06:hook",
                "verdict": "REVISE",
                "reason": "Evidence carrier was too generic.",
            }]
        )
        governance.apply_plan(self.root, plan)
        governance.apply_plan(self.root, plan)
        record = self._registry()["asset_governance"]["parent_overrides"]["hooks:03-data-shock"]
        self.assertEqual(1, len(record["validation_history_additions"]))
        parents, _, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        by_id = {item.asset_id: item for item in parents}
        self.assertEqual("generative_strategy", by_id["hooks:03-data-shock"].role)

    def test_validation_history_surfaces_caution_without_changing_eligibility(self):
        plan = self._plan(
            [
                {
                    "action": "RECORD_VALIDATION",
                    "target_asset_id": "hooks:03-data-shock",
                    "validation_id": "project:2026-08-06:hook-1",
                    "verdict": "REJECT",
                    "reason": "The Hook did not establish a concrete stake.",
                },
                {
                    "action": "RECORD_VALIDATION",
                    "target_asset_id": "hooks:03-data-shock",
                    "validation_id": "project:2026-08-06:hook-2",
                    "verdict": "REJECT",
                    "reason": "The Hook did not establish a concrete stake.",
                },
            ]
        )
        governance.apply_plan(self.root, plan)
        parents, _, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        asset = next(item for item in parents if item.asset_id == "hooks:03-data-shock")
        self.assertEqual("CAUTION", asset.health)
        self.assertEqual(2, asset.validation_rejects)
        self.assertEqual("generative_strategy", asset.role)
        output = StringIO()
        with redirect_stdout(output):
            catalog.command_audit(Namespace(json=True))
        # The live catalog is healthy; health calculation above verifies the staged catalog.
        self.assertIn("validation_health", json.loads(output.getvalue()))

    def test_merge_preserves_old_id_and_resolves_to_active_target(self):
        plan = self._plan(
            [{
                "action": "MERGE",
                "source_asset_id": "tensions:01-despite-progress-unaddressed:vAF",
                "target_asset_id": "tensions:01-despite-progress-unaddressed:vD",
                "capability_overlap": "Both justify why an omission matters through concrete warrants.",
            }]
        )
        governance.apply_plan(self.root, plan)
        parents, variants, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        resolved, notices = catalog._resolve_assets(
            parents, variants, ["tensions:01-despite-progress-unaddressed:vAF"]
        )
        self.assertEqual("tensions:01-despite-progress-unaddressed:vD", resolved[0].asset_id)
        self.assertIn("vAF", notices[0])

    def test_variant_merge_cannot_cross_parent_boundary(self):
        plan = self._plan(
            [{
                "action": "MERGE",
                "source_asset_id": "hooks:03-data-shock:vA",
                "target_asset_id": "tensions:01-despite-progress-unaddressed:vA",
                "capability_overlap": "test only",
            }]
        )
        with self.assertRaisesRegex(ValueError, "within one parent"):
            governance.apply_plan(self.root, plan)

    def test_variant_proposal_cannot_use_cross_parent_neighbor(self):
        plan = self._plan(
            [{
                "action": "PROPOSE_VARIANT",
                "target_parent_id": "hooks:03-data-shock",
                "nearest_neighbor_id": "tensions:01-despite-progress-unaddressed:vA",
                "capability_loss_if_merged": "Different evidence carrier.",
            }]
        )
        with self.assertRaisesRegex(ValueError, "nearest neighbor must belong"):
            governance.apply_plan(self.root, plan, dry_run=True)

    def test_promotion_requires_auditable_sources(self):
        missing_sources = self._plan(
            [{
                "action": "PROMOTE",
                "target_asset_id": "hooks:03-data-shock:vA",
                "role": "generative_variant",
                "evidence_status": "VERIFIED",
                "paper_count": 3,
                "verification_basis": "cross_paper_full_text",
            }]
        )
        with self.assertRaisesRegex(ValueError, "source_papers"):
            governance.apply_plan(self.root, missing_sources, dry_run=True)
        valid = self._plan(
            [{
                "action": "PROMOTE",
                "target_asset_id": "hooks:03-data-shock:vA",
                "role": "generative_variant",
                "evidence_status": "VERIFIED",
                "paper_count": 3,
                "verification_basis": "cross_paper_full_text",
                "source_papers": ["paper_a (AMJ)", "paper_b (SMJ)", "paper_c (OS)"],
            }]
        )
        governance.apply_plan(self.root, valid)
        record = self._registry()["asset_governance"]["variant_overrides"]["hooks:03-data-shock:vA"]
        self.assertEqual(3, len(record["source_papers"]))

    def test_batch_01_findings_preview_merge_keeps_the_legacy_alias_resolvable(self):
        parents, variants, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        resolved, notices = catalog._resolve_assets(
            parents, variants, ["previews:findings-preview:vS"]
        )
        self.assertEqual("previews:findings-preview:vM", resolved[0].asset_id)
        self.assertEqual(
            "previews:findings-preview:vS -> previews:findings-preview:vM", notices[0]
        )

    def test_representative_merge_requires_and_accepts_atomic_menu_replacement(self):
        plan = self._plan(
            [
                {
                    "action": "MERGE",
                    "source_asset_id": "hooks:03-data-shock:vB",
                    "target_asset_id": "hooks:03-data-shock:vA",
                    "capability_overlap": "Both establish observable scale before the puzzle.",
                },
                {
                    "action": "SET_REFERENCE_MENU",
                    "target_parent_id": "hooks:03-data-shock",
                    "asset_ids": [
                        "hooks:03-data-shock:vA",
                        "hooks:03-data-shock:vC",
                        "hooks:03-data-shock:vD",
                        "hooks:03-data-shock:vG",
                        "hooks:03-data-shock:vK",
                    ],
                },
            ]
        )
        governance.apply_plan(self.root, plan)
        menu = self._registry()["asset_governance"]["representative_reference_menus"][
            "hooks:03-data-shock"
        ]
        self.assertNotIn("hooks:03-data-shock:vB", menu)

    def test_add_reference_updates_markdown_and_snapshot_together(self):
        plan = self._plan(
            [{
                "action": "ADD_REFERENCE",
                "target_parent_id": "hooks:03-data-shock",
                "title": "治理测试参考型",
                "source_paper": "audit_paper_2026 (AMJ)",
                "template": "[Trend] escalates, creating [consequence].",
                "nearest_neighbor_id": "hooks:03-data-shock:vA",
                "capability_loss_if_merged": "Adds an auditable cross-level escalation carrier.",
            }]
        )
        result = governance.apply_plan(self.root, plan)
        self.assertEqual(346, result["variant_assets"])
        self.assertEqual(["hooks:03-data-shock:vL"], result["added_ids"])
        parents, variants, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        self.assertEqual(94, len(parents))
        self.assertEqual(346, len(variants))
        text = (self.root / "academic-writing-corpus" / "hooks" / "03-data-shock.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("### 变体 L：治理测试参考型", text)

    def test_invalid_promotion_does_not_mutate(self):
        registry_path = self.root / "academic-writing-corpus" / "_evidence_registry.yaml"
        before = registry_path.read_text(encoding="utf-8")
        plan = self._plan(
            [{
                "action": "PROMOTE",
                "target_asset_id": "hooks:03-data-shock:vA",
                "role": "generative_variant",
                "evidence_status": "EMERGING",
                "paper_count": 1,
                "verification_basis": "single_paper",
            }]
        )
        with self.assertRaises(ValueError):
            governance.apply_plan(self.root, plan)
        self.assertEqual(before, registry_path.read_text(encoding="utf-8"))

    def test_routed_parent_cannot_be_deprecated_without_routing_change(self):
        registry_path = self.root / "academic-writing-corpus" / "_evidence_registry.yaml"
        before = registry_path.read_text(encoding="utf-8")
        plan = self._plan(
            [{
                "action": "DEPRECATE",
                "target_asset_id": "hooks:03-data-shock",
                "reason": "test only",
            }]
        )
        with self.assertRaises(ValueError):
            governance.apply_plan(self.root, plan)
        self.assertEqual(before, registry_path.read_text(encoding="utf-8"))

    def test_dry_run_validates_without_writing(self):
        registry_path = self.root / "academic-writing-corpus" / "_evidence_registry.yaml"
        before = registry_path.read_text(encoding="utf-8")
        plan = self._plan(
            [{
                "action": "EXTEND_SOURCE",
                "target_asset_id": "hooks:03-data-shock:vA",
                "source_paper": "dry_run_2026 (SMJ)",
            }]
        )
        result = governance.apply_plan(self.root, plan, dry_run=True)
        self.assertTrue(result["validated"])
        self.assertTrue(result["dry_run"])
        self.assertEqual(before, registry_path.read_text(encoding="utf-8"))

    def test_write_and_distill_protocols_use_governed_interface(self):
        write_skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        distill_root = SKILL_ROOT.parent / "distill-introduction-exemplar"
        phase2 = (distill_root / "references" / "phase-2-extraction.md").read_text(encoding="utf-8")
        phase4 = (distill_root / "references" / "phase-4-validation-writeback.md").read_text(
            encoding="utf-8"
        )
        templates = (distill_root / "protocols" / "corpus_file_templates.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("introduction_asset_catalog.py", write_skill)
        self.assertIn("introduction_corpus_governance.py", write_skill)
        self.assertIn("capability_loss_if_merged", phase4)
        self.assertIn("ADD_REFERENCE", phase2)
        self.assertIn("--dry-run", templates)
        self.assertNotIn("append_variant", phase2)

    def test_distill_action_plan_closes_through_governance(self):
        plan = self._plan(
            [
                {
                    "action": "ADD_REFERENCE",
                    "target_parent_id": "hooks:03-data-shock",
                    "nearest_neighbor_id": "hooks:03-data-shock:vA",
                    "title": "端到端测试参考型",
                    "source_paper": "integration_test_2026 (AMJ)",
                    "template": "[Trend] creates [consequence].",
                    "capability_loss_if_merged": "Adds an auditable escalation evidence carrier.",
                },
                {
                    "action": "RECORD_VALIDATION",
                    "target_asset_id": "hooks:03-data-shock",
                    "validation_id": "integration:2026-08-06:hook",
                    "verdict": "VALIDATED",
                    "reason": "End-to-end governed writeback completed.",
                },
            ]
        )
        governance.apply_plan(self.root, plan, dry_run=True)
        governance.apply_plan(self.root, plan)
        parents, variants, _ = catalog.load_catalog(
            self.root / "academic-writing-corpus",
            self.root / "academic-writing-corpus" / "_evidence_registry.yaml",
        )
        self.assertIn("hooks:03-data-shock:vL", {item.asset_id for item in variants})
        asset = next(item for item in parents if item.asset_id == "hooks:03-data-shock")
        self.assertEqual(1, asset.validation_total)
        distill_root = SKILL_ROOT.parent / "distill-introduction-exemplar"
        output_blocks = (distill_root / "protocols" / "phase4_output_blocks.md").read_text(encoding="utf-8")
        quick_reference = (distill_root / "protocols" / "quick_reference.md").read_text(encoding="utf-8")
        self.assertIn("style_profile_enrichment` is retired", output_blocks)
        self.assertIn("不得直接创建 corpus 文件", quick_reference)

    def test_governance_benchmark_is_balanced_and_uses_active_families(self):
        data = benchmark.load_benchmark()
        snapshot = benchmark.snapshot()
        self.assertEqual(18, len(data["tasks"]))
        self.assertEqual(94, snapshot["parent_assets"])
        self.assertEqual(345, snapshot["variant_assets"])
        self.assertEqual(18, len(snapshot["task_ids"]))


if __name__ == "__main__":
    unittest.main()
