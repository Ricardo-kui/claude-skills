from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))
import theory_asset_catalog as catalog  # noqa: E402
import theory_corpus_governance as governance  # noqa: E402
import theory_governance_benchmark as benchmark  # noqa: E402


class TheoryGovernanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "write-theory"
        shutil.copytree(SKILL_ROOT, self.root)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def _plan(self, rows: list[dict]) -> Path:
        path = self.root / "plan.yaml"
        path.write_text(yaml.safe_dump({"actions": rows}, allow_unicode=True, sort_keys=False), encoding="utf-8")
        return path

    def _catalog(self):
        return catalog.load_catalog(self.root / "corpus", self.root / "corpus" / "_evidence_registry.yaml")

    def _registry_text(self) -> str:
        return (self.root / "corpus" / "_evidence_registry.yaml").read_text(encoding="utf-8")

    def test_catalog_has_seven_architectures_and_governed_historical_patterns(self):
        architectures, patterns = self._catalog()
        self.assertEqual(set("ABCDEFG"), {item.family for item in architectures})
        self.assertEqual(7, len(architectures))
        self.assertEqual(120, len(patterns))
        self.assertEqual(26, sum(item.evidence_status == "UNREGISTERED" for item in patterns))

    def test_architecture_family_shorthand_resolves_without_changing_identity(self):
        architectures, _ = self._catalog()
        self.assertEqual("theory:architecture:D", catalog.resolve_architecture("D", architectures).asset_id)
        self.assertEqual("theory:architecture:E", catalog.resolve_architecture("architecture:E", architectures).asset_id)
        self.assertEqual("theory:architecture:B", catalog.resolve_architecture("theory:architecture:B", architectures).asset_id)
        with self.assertRaisesRegex(ValueError, "Unknown or ambiguous"):
            catalog.resolve_architecture("process", architectures)

    def test_registry_status_thresholds_are_enforced(self):
        _, patterns = self._catalog()
        by_id = {item.pattern_id: item for item in patterns}
        self.assertEqual("EMERGING", by_id["paired_hypotheses"].evidence_status)
        self.assertEqual("EMERGING", by_id["track_level_local_closure"].evidence_status)

    def test_duplicate_metadata_id_is_removed_from_active_inventory(self):
        occurrences = catalog._metadata_occurrences(self.root / "corpus")
        self.assertTrue(all(len(paths) == 1 for paths in occurrences.values()))
        self.assertIn("simultaneously_recognize_leverage", occurrences)

    def test_reference_menu_is_bounded_and_architecture_local(self):
        plan = self._plan([{
            "action": "SET_REFERENCE_MENU",
            "target_architecture_id": "theory:architecture:A",
            "asset_ids": ["theory:pattern:construct_differentiation"],
        }])
        governance.apply_plan(self.root, plan)
        architectures, patterns = self._catalog()
        menu = catalog._load_registry(self.root / "corpus" / "_evidence_registry.yaml")["asset_governance"]["representative_reference_menus"]
        self.assertEqual(["theory:pattern:construct_differentiation"], menu["theory:architecture:A"])
        self.assertEqual(7, len(architectures))
        self.assertTrue(any(item.pattern_id == "construct_differentiation" for item in patterns))

    def test_validation_caution_does_not_change_architecture_eligibility(self):
        plan = self._plan([
            {"action": "RECORD_VALIDATION", "target_asset_id": "theory:architecture:B", "validation_id": "t1", "verdict": "REJECT", "reason": "why-chain incomplete"},
            {"action": "RECORD_VALIDATION", "target_asset_id": "theory:architecture:B", "validation_id": "t2", "verdict": "REJECT", "reason": "why-chain incomplete"},
        ])
        governance.apply_plan(self.root, plan)
        architectures, _ = self._catalog()
        asset = next(item for item in architectures if item.family == "B")
        self.assertEqual("CAUTION", asset.health)
        self.assertEqual("generative_strategy", asset.role)

    def test_generation_contracts_expose_architecture_and_story_state_guards(self):
        registry = catalog._load_registry(self.root / "corpus" / "_evidence_registry.yaml")["asset_governance"]
        moderation = catalog.generation_contract(registry, "E", "hypotheses", "complete")
        process = catalog.generation_contract(registry, "D", "propositions", "complete")
        local = catalog.generation_contract(registry, "B", "hypotheses", "local_only")
        self.assertTrue(any("both boundary states" in item for item in moderation["required"]))
        self.assertTrue(any("transition condition" in item for item in process["required"]))
        self.assertTrue(any("Numbered hypotheses" in item for item in local["prohibited"]))
        self.assertTrue(any("diagnostic observation" in item for item in moderation["required"]))
        self.assertTrue(any("no directed edge may run from X to the boundary state" in item for item in moderation["required"]))
        self.assertTrue(any("carrier/channel" in item for item in process["required"]))
        self.assertTrue(any("terminal process state" in item for item in process["required"]))

    def test_structural_process_operators_are_registered_but_not_evidence_assets(self):
        protocol = self.root / "corpus" / "subprotocols" / "process_transition_operators.md"
        text = protocol.read_text(encoding="utf-8")
        self.assertNotIn("pattern_id:", text)
        self.assertIn("pre-next-stage marker", text)
        self.assertIn("feedback source", text)
        self.assertIn("carrier or channel", text)
        self.assertIn("decision-capable recipient", text)
        registry = catalog._load_registry(self.root / "corpus" / "_evidence_registry.yaml")
        record = next(item for item in registry["unattributed_corpus"] if item["file"] == "subprotocols/process_transition_operators.md")
        self.assertEqual("structural", record["status"])

    def test_retrieval_manifest_is_hash_chained_and_detects_tampering(self):
        path = self.root / "retrieval-manifest.json"
        catalog.append_retrieval_manifest(path, {
            "command": "list-references", "candidate_ids": ["a", "b"], "returned_ids": ["a"]
        })
        catalog.append_retrieval_manifest(path, {
            "command": "render", "assets": [{"resolved_id": "a", "content_sha256": "abc"}]
        })
        data = json.loads(path.read_text(encoding="utf-8"))
        catalog.validate_retrieval_manifest(data)
        self.assertEqual(2, len(data["events"]))
        self.assertEqual(data["events"][0]["event_hash"], data["events"][1]["previous_event_hash"])
        self.assertEqual(data["events"][1]["event_hash"], data["head_hash"])
        data["events"][0]["candidate_ids"].append("tampered")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            catalog.validate_retrieval_manifest(data)

    def test_architecture_specific_reference_classification_and_fragment_rendering(self):
        _, patterns = self._catalog()
        bilateral = next(item for item in patterns if item.pattern_id == "bilateral_moderation_derivation")
        self.assertIn("E", bilateral.compatible_families)
        fragment = catalog._reference_fragment(self.root / "corpus" / bilateral.source_file, bilateral.pattern_id)
        self.assertIsNotNone(fragment)
        self.assertIn("Bilateral Moderation Derivation", fragment)
        self.assertNotIn("Cumulative Moderation Build-up", fragment)
        competitors = [item for item in patterns if item.slot == "T3" and "E" in item.compatible_families]
        ranked = sorted(competitors, key=lambda item: -catalog.reference_query_score(item, "bilateral moderation"))
        self.assertEqual("bilateral_moderation_derivation", ranked[0].pattern_id)

    def test_extend_source_is_idempotent_and_recomputes_status(self):
        plan = self._plan([{
            "action": "EXTEND_SOURCE",
            "target_asset_id": "theory:pattern:paired_hypotheses",
            "source_paper": "independent_test_2026_amj",
        }])
        governance.apply_plan(self.root, plan)
        governance.apply_plan(self.root, plan)
        _, patterns = self._catalog()
        asset = next(item for item in patterns if item.pattern_id == "paired_hypotheses")
        self.assertEqual("VERIFIED", asset.evidence_status)
        self.assertEqual(3, len(asset.source_papers))

    def test_distill_output_shape_is_accepted(self):
        path = self.root / "nested-plan.yaml"
        path.write_text(yaml.safe_dump({"governance_plan": {"actions": [{
            "action": "EXTEND_SOURCE",
            "target_asset_id": "theory:pattern:paired_hypotheses",
            "source_paper": "nested_plan_2026_amj",
        }]}}, allow_unicode=True, sort_keys=False), encoding="utf-8")
        self.assertTrue(governance.apply_plan(self.root, path, dry_run=True)["validated"])

    def test_promotion_requires_unique_auditable_sources(self):
        invalid = self._plan([{
            "action": "PROMOTE", "target_asset_id": "theory:pattern:paired_hypotheses",
            "evidence_status": "VERIFIED", "paper_count": 3,
            "verification_basis": "full_text", "source_papers": ["a", "a", "b"],
        }])
        with self.assertRaisesRegex(ValueError, "unique source"):
            governance.apply_plan(self.root, invalid, dry_run=True)
        valid = self._plan([{
            "action": "PROMOTE", "target_asset_id": "theory:pattern:paired_hypotheses",
            "evidence_status": "VERIFIED", "paper_count": 3,
            "verification_basis": "full_text", "source_papers": ["a", "b", "c"],
        }])
        governance.apply_plan(self.root, valid)
        _, patterns = self._catalog()
        self.assertEqual("generative_strategy", next(item for item in patterns if item.pattern_id == "paired_hypotheses").role)

    def test_merge_preserves_source_id_and_blocks_cross_slot_merge(self):
        merge = self._plan([{
            "action": "MERGE",
            "source_asset_id": "theory:pattern:anchor_then_mechanism_then_prediction",
            "target_asset_id": "theory:pattern:two_step_mechanism_chain",
            "capability_overlap": "Both are two-step T3 why-chain references.",
        }])
        governance.apply_plan(self.root, merge)
        architectures, patterns = self._catalog()
        resolved, notices = catalog.resolve_assets(["anchor_then_mechanism_then_prediction"], architectures, patterns)
        self.assertEqual("two_step_mechanism_chain", resolved[0].pattern_id)
        self.assertIn("two_step_mechanism_chain", notices[0])
        bad = self._plan([{
            "action": "MERGE",
            "source_asset_id": "theory:pattern:two_step_mechanism_chain",
            "target_asset_id": "theory:pattern:no_global_closure",
            "capability_overlap": "test",
        }])
        with self.assertRaisesRegex(ValueError, "family and slot"):
            governance.apply_plan(self.root, bad, dry_run=True)

    def test_proposal_requires_same_family_or_explicit_cross_family_operator(self):
        good = self._plan([{
            "action": "PROPOSE_VARIANT", "target_architecture_id": "theory:architecture:B",
            "nearest_neighbor_id": "theory:pattern:two_step_mechanism_chain",
            "capability_loss_if_merged": "Adds a distinct time-ordered mechanism operator.",
        }])
        self.assertTrue(governance.apply_plan(self.root, good, dry_run=True)["validated"])
        bad = self._plan([{
            "action": "PROPOSE_VARIANT", "target_architecture_id": "theory:architecture:B",
            "nearest_neighbor_id": "theory:pattern:construct_differentiation",
            "capability_loss_if_merged": "test",
        }])
        with self.assertRaisesRegex(ValueError, "target architecture family"):
            governance.apply_plan(self.root, bad, dry_run=True)

    def test_add_reference_is_hidden_from_default_architecture_menu(self):
        plan = self._plan([{
            "action": "ADD_REFERENCE", "pattern_id": "governance_test_temporal_operator",
            "target_architecture_id": "theory:architecture:B",
            "home_file": "subprotocols/hypothesis_derivation_patterns.md",
            "title": "Governance test temporal operator", "source_paper": "test_2026_amj",
            "template": "[X] changes [state] before [state] changes [Y].",
            "nearest_neighbor_id": "theory:pattern:two_step_mechanism_chain",
            "capability_loss_if_merged": "Retains a time-ordered mechanism capability for later validation.",
        }])
        before = self._registry_text()
        self.assertTrue(governance.apply_plan(self.root, plan, dry_run=True)["dry_run"])
        self.assertEqual(before, self._registry_text())
        governance.apply_plan(self.root, plan)
        _, patterns = self._catalog()
        asset = next(item for item in patterns if item.pattern_id == "governance_test_temporal_operator")
        self.assertEqual("reference_exemplar", asset.role)
        self.assertEqual("EMERGING", asset.evidence_status)
        self.assertIn("单篇 reference exemplar", (self.root / "corpus" / asset.source_file).read_text(encoding="utf-8"))

    def test_routing_change_is_review_only_and_invalid_plans_do_not_mutate(self):
        before = self._registry_text()
        review = self._plan([{"action": "PROPOSE_ROUTING_CHANGE"}])
        with self.assertRaisesRegex(ValueError, "review-only"):
            governance.apply_plan(self.root, review)
        self.assertEqual(before, self._registry_text())

    def test_write_and_distill_skills_reference_the_governed_interface(self):
        write_skill = (self.root / "SKILL.md").read_text(encoding="utf-8")
        distill_skill = (SKILL_ROOT.parent / "distill-theory-exemplar" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("theory_asset_catalog.py", write_skill)
        self.assertIn("theory_corpus_governance.py", write_skill)
        self.assertIn("generation-contract", write_skill)
        self.assertIn("governed-generation-guards.md", write_skill)
        self.assertIn("process_transition_operators.md", write_skill)
        self.assertIn("--manifest", write_skill)
        self.assertIn("governance_plan", distill_skill)
        self.assertIn("theory_corpus_governance.py", distill_skill)

    def test_blind_benchmark_is_balanced(self):
        data = benchmark.snapshot()
        self.assertEqual(24, data["tasks"])
        self.assertEqual(set("ABCDEFG"), set(data["architectures"]))
        self.assertEqual({"Incompleteness", "Inadequacy", "Incommensurability"}, set(data["gaps"]))

    def test_r3_guard_benchmark_has_preregistered_safety_and_quality_rules(self):
        path = SKILL_ROOT / "benchmarks" / "theory_governance" / "R3_GUARD_TASKS.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertEqual(8, len(data["tasks"]))
        self.assertEqual(0, data["decision_rule"]["primary_safety"]["governed_critical_failures_max"])
        self.assertEqual(0.5, data["decision_rule"]["comparative_quality"]["governed_mean_score_must_be_at_least_legacy_minus"])
        self.assertEqual({"D", "E", "B"}, {task["architecture"] for task in data["tasks"]})

    def test_r4_acceptance_is_preregistered_and_stratified(self):
        path = SKILL_ROOT / "benchmarks" / "theory_governance" / "R4_ACCEPTANCE_TASKS.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertEqual(12, len(data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "targeted" for task in data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "preservation" for task in data["tasks"]))
        self.assertEqual(0.25, data["decision_rule"]["comparative_superiority"]["governed_mean_score_must_exceed_legacy_by_at_least"])
        self.assertEqual(2, data["decision_rule"]["comparative_superiority"]["targeted_task_losses_max"])
        self.assertTrue(data["blinding"]["seed"])

    def test_r5_acceptance_is_preregistered_before_generation(self):
        path = SKILL_ROOT / "benchmarks" / "theory_governance" / "R5_ACCEPTANCE_TASKS.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertEqual(12, len(data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "targeted" for task in data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "preservation" for task in data["tasks"]))
        self.assertEqual({"D", "E"}, {task["architecture"] for task in data["tasks"] if task["stratum"] == "targeted"})
        self.assertEqual(12, data["decision_rule"]["primary_integrity"]["governed_manifest_task_coverage_required"])
        self.assertEqual(1, data["decision_rule"]["comparative_superiority"]["targeted_task_losses_max"])
        self.assertEqual(0.25, data["decision_rule"]["comparative_superiority"]["governed_mean_score_must_exceed_legacy_by_at_least"])

    def test_r6_acceptance_is_preregistered_before_generation(self):
        path = SKILL_ROOT / "benchmarks" / "theory_governance" / "R6_ACCEPTANCE_TASKS.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        self.assertEqual(12, len(data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "targeted" for task in data["tasks"]))
        self.assertEqual(6, sum(task["stratum"] == "preservation" for task in data["tasks"]))
        self.assertEqual({"B", "D", "E", "G"}, {task["architecture"] for task in data["tasks"] if task["stratum"] == "targeted"})
        self.assertEqual(12, data["decision_rule"]["primary_integrity"]["governed_manifest_task_coverage_required"])
        self.assertEqual(1, data["decision_rule"]["comparative_superiority"]["targeted_task_losses_max"])
        self.assertEqual(0.25, data["decision_rule"]["comparative_superiority"]["governed_mean_score_must_exceed_legacy_by_at_least"])


if __name__ == "__main__":
    unittest.main()
