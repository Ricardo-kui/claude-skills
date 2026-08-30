"""Persist design-defect evidence from Introduction exemplar distillation.

Usage:
    python _update_design_feedback.py <skill_design_feedback.yaml>
    python _update_design_feedback.py --stdin
    python _update_design_feedback.py <input.yaml> --dry-run
    python _update_design_feedback.py --self-test

The script aggregates evidence only. It never edits SKILL.md, routing tables,
validators, schemas, or stage gates; the Phase 4.7 protocol controls revisions.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
import tempfile
from datetime import date
from pathlib import Path

import yaml


DEFAULT_REGISTRY = (
    Path(__file__).parent.parent
    / "write-introduction"
    / "corpus"
    / "_skill_design_feedback.yaml"
)

CLASSIFICATIONS = {
    "corpus_gap",
    "routing_defect",
    "validator_defect",
    "output_contract_defect",
    "schema_defect",
    "stage_gate_defect",
}
HIGH_RISK_CLASSES = {"schema_defect", "stage_gate_defect"}
ALLOWED_RISKS = {"low", "medium", "high"}
EVIDENCE_QUALITIES = {"full_text_verified", "functional_summary", "metadata_only"}
EVIDENCE_RANK = {"metadata_only": 0, "functional_summary": 1, "full_text_verified": 2}


def load_yaml(path: str | None, use_stdin: bool = False) -> dict:
    if use_stdin:
        data = yaml.safe_load(sys.stdin.read())
    else:
        if not path:
            raise ValueError("Provide an input path or --stdin.")
        data = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("Input must be a YAML mapping.")
    return data.get("skill_design_feedback", data)


def load_registry(path: Path) -> dict:
    if not path.exists():
        return {
            "meta": {
                "schema_version": 1,
                "last_updated": str(date.today()),
                "observations_processed": 0,
                "description": "Evidence ledger for design defects inferred from Introduction exemplar distillation.",
            },
            "defects": {},
        }
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"Registry is not a YAML mapping: {path}")
    data.setdefault("meta", {})
    data.setdefault("defects", {})
    return data


def save_registry(path: Path, registry: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = yaml.safe_dump(
        registry,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp"
    ) as handle:
        handle.write(rendered)
        temp_path = Path(handle.name)
    temp_path.replace(path)


def normalize_paper(raw: object) -> dict:
    if isinstance(raw, str):
        return {"id": raw.strip(), "journal": "", "evidence_anchor": "", "evidence_quality": "metadata_only"}
    if not isinstance(raw, dict):
        raise ValueError(f"Paper evidence must be a string or mapping: {raw!r}")
    paper_id = str(raw.get("id") or raw.get("paper_id") or "").strip()
    if not paper_id:
        raise ValueError(f"Paper evidence is missing id: {raw!r}")
    quality = str(raw.get("evidence_quality") or "functional_summary").strip()
    if quality not in EVIDENCE_QUALITIES:
        raise ValueError(f"Unknown evidence_quality {quality!r} for paper {paper_id!r}")
    return {
        "id": paper_id,
        "journal": str(raw.get("journal") or "").strip(),
        "evidence_anchor": str(raw.get("evidence_anchor") or "").strip(),
        "evidence_quality": quality,
    }


def validate_regression_cases(observation: dict) -> None:
    if observation.get("classification") == "corpus_gap":
        return
    cases = observation.get("regression_cases")
    if not isinstance(cases, dict):
        raise ValueError("Core design observations require regression_cases.")
    for name in ("positive", "preservation"):
        case = cases.get(name)
        if not isinstance(case, dict) or not str(case.get("prompt") or "").strip():
            raise ValueError(f"Missing regression_cases.{name}.prompt")
        invariants = case.get("expected_invariants")
        if not isinstance(invariants, list) or not any(str(item).strip() for item in invariants):
            raise ValueError(f"Missing regression_cases.{name}.expected_invariants")


def validate_observation(observation: dict) -> None:
    required = ["defect_id", "classification", "current_rule", "target", "diagnosis"]
    missing = [field for field in required if not observation.get(field)]
    if missing:
        raise ValueError(f"Observation missing required fields {missing}: {observation}")
    if observation["classification"] not in CLASSIFICATIONS:
        raise ValueError(f"Unknown classification: {observation['classification']}")
    if observation["classification"] != "corpus_gap" and not observation.get("rule_excerpt"):
        raise ValueError("Core design observations require an exact rule_excerpt.")
    risk = observation.get("risk", "medium")
    if risk not in ALLOWED_RISKS:
        raise ValueError(f"Unknown risk: {risk}")
    validate_regression_cases(observation)


def evidence_status(entry: dict) -> str:
    verified_count = entry.get("verified_paper_count", 0)
    verified_journals = entry.get("verified_journal_count", 0)
    if entry.get("decisive_falsifier") and entry.get("absolute_rule") and verified_count >= 1:
        return "FALSIFIER"
    if verified_count >= 5 and verified_journals >= 2:
        return "ROBUST"
    if verified_count >= 3 and verified_journals >= 2:
        return "VERIFIED"
    return "EMERGING"


def safe_target(target: str, skills_root: Path) -> Path:
    relative = Path(target)
    if relative.is_absolute() or ".." in relative.parts or ":" in target:
        raise ValueError("target must be a relative skill path without line suffixes; use rule_locator for lines.")
    if not relative.parts or relative.parts[0] != "write-introduction":
        raise ValueError("Design feedback targets must stay inside write-introduction.")
    root = skills_root.resolve()
    target_path = (root / relative).resolve()
    if root not in target_path.parents or not target_path.is_file():
        raise ValueError(f"Target file does not exist inside skills root: {target}")
    return target_path


def verify_rule_target(observation: dict, skills_root: Path) -> None:
    if observation.get("classification") == "corpus_gap":
        return
    target = str(observation["target"])
    target_path = safe_target(target, skills_root)
    excerpt = " ".join(str(observation["rule_excerpt"]).split())
    content = " ".join(target_path.read_text(encoding="utf-8").split())
    if excerpt not in content:
        raise ValueError(
            f"rule_excerpt was not found in {target}; do not register a defect until the current rule is verified."
        )


def verify_resolution(resolution: dict, entry: dict, skills_root: Path) -> None:
    if resolution.get("status") not in {"applied", "needs_revision"}:
        raise ValueError("resolution.status must be applied or needs_revision.")
    targets = resolution.get("modified_targets")
    if not isinstance(targets, list) or not targets:
        raise ValueError("resolution.modified_targets must be a non-empty list.")
    resolved_targets = {str(target): safe_target(str(target), skills_root) for target in targets}
    if resolution.get("status") != "applied":
        return
    validation = resolution.get("validation")
    if not isinstance(validation, dict):
        raise ValueError("Applied resolution requires validation results.")
    for key in ("quick_validate", "regression", "forward_test"):
        if validation.get(key) is not True:
            raise ValueError(f"Applied resolution requires validation.{key}: true")
    target = str(entry.get("target") or "")
    if target not in resolved_targets:
        raise ValueError("Applied resolution must include the registered defect target.")
    after = " ".join(str(resolution.get("rule_excerpt_after") or "").split())
    before = " ".join(str(entry.get("rule_excerpt") or "").split())
    if not after or after == before:
        raise ValueError("Applied resolution requires a distinct rule_excerpt_after.")
    content = " ".join(resolved_targets[target].read_text(encoding="utf-8").split())
    if after not in content:
        raise ValueError("rule_excerpt_after was not found in the registered target.")
    if resolution.get("old_rule_excerpt_absent") is True and before and before in content:
        raise ValueError("The old rule_excerpt is still present despite old_rule_excerpt_absent: true.")


def action_for(entry: dict) -> dict:
    status = entry["status"]
    classification = entry["classification"]
    risk = entry.get("risk", "medium")
    if entry.get("lifecycle") == "resolved":
        eligibility = "no_action"
        reason = "A validated correction has already resolved this defect."
    elif classification == "corpus_gap":
        eligibility = "reference_write" if status in {"VERIFIED", "ROBUST"} else "optional_variant_only"
        reason = "Corpus assets do not alter core routing or story gates."
    elif classification in HIGH_RISK_CLASSES or risk == "high":
        eligibility = "explicit_review"
        reason = "Schema, stage-gate, or high-risk changes can break downstream skills."
    elif status == "FALSIFIER" and has_dual_regressions(entry):
        eligibility = "conditionalize_candidate"
        reason = "A decisive counterexample may weaken an absolute rule but cannot establish its inverse."
    elif status in {"VERIFIED", "ROBUST"} and has_dual_regressions(entry):
        eligibility = "safe_core_patch_candidate"
        reason = "Cross-paper and cross-journal evidence meets the bounded core-revision threshold."
    else:
        eligibility = "log_only"
        reason = "Evidence is insufficient for a core-skill change."
    return {"eligibility": eligibility, "reason": reason}


def has_dual_regressions(entry: dict) -> bool:
    cases = entry.get("regression_cases")
    return isinstance(cases, dict) and all(cases.get(name) for name in ("positive", "preservation"))


def _dedupe_objects(items: list[dict]) -> list[dict]:
    seen = set()
    result = []
    for item in items:
        key = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def merge_observation(registry: dict, observation: dict, observed_on: str) -> None:
    validate_observation(observation)
    defect_id = observation["defect_id"]
    defects = registry.setdefault("defects", {})
    entry = defects.setdefault(
        defect_id,
        {
            "classification": observation["classification"],
            "status": "EMERGING",
            "risk": observation.get("risk", "medium"),
            "current_rule": observation["current_rule"],
            "rule_excerpt": observation.get("rule_excerpt", ""),
            "rule_locator": observation.get("rule_locator", ""),
            "target": observation["target"],
            "diagnosis": observation["diagnosis"],
            "proposed_change": observation.get("proposed_change", {}),
            "absolute_rule": bool(observation.get("absolute_rule", False)),
            "decisive_falsifier": False,
            "papers": [],
            "paper_count": 0,
            "journals": [],
            "journal_count": 0,
            "verified_paper_count": 0,
            "verified_journals": [],
            "verified_journal_count": 0,
            "regression_cases": {"positive": [], "preservation": []},
            "resolution_history": [],
            "lifecycle": "open",
            "first_seen": observed_on,
            "last_seen": observed_on,
        },
    )
    if entry["classification"] != observation["classification"]:
        raise ValueError(
            f"Defect {defect_id!r} classification changed from {entry['classification']} "
            f"to {observation['classification']}; use a new defect_id."
        )

    entry["risk"] = observation.get("risk", entry.get("risk", "medium"))
    entry["diagnosis"] = observation.get("diagnosis", entry["diagnosis"])
    entry["proposed_change"] = observation.get("proposed_change", entry.get("proposed_change", {}))
    entry["absolute_rule"] = bool(observation.get("absolute_rule", entry.get("absolute_rule", False)))
    entry["decisive_falsifier"] = bool(
        observation.get("decisive_falsifier", False) or entry.get("decisive_falsifier", False)
    )
    entry["last_seen"] = observed_on

    papers_by_id = {paper["id"]: paper for paper in entry.get("papers", [])}
    evidence = observation.get("evidence", {}) or {}
    for raw_paper in evidence.get("papers", []):
        paper = normalize_paper(raw_paper)
        previous = papers_by_id.get(paper["id"], {})
        previous_quality = previous.get("evidence_quality", "metadata_only")
        quality = max((paper["evidence_quality"], previous_quality), key=lambda item: EVIDENCE_RANK[item])
        papers_by_id[paper["id"]] = {
            "id": paper["id"],
            "journal": paper["journal"] or previous.get("journal", ""),
            "evidence_anchor": paper["evidence_anchor"] or previous.get("evidence_anchor", ""),
            "evidence_quality": quality,
        }
    entry["papers"] = sorted(papers_by_id.values(), key=lambda item: item["id"])
    entry["paper_count"] = len(entry["papers"])
    entry["journals"] = sorted({p["journal"] for p in entry["papers"] if p["journal"]})
    entry["journal_count"] = len(entry["journals"])
    verified = [p for p in entry["papers"] if p.get("evidence_quality") == "full_text_verified"]
    entry["verified_paper_count"] = len(verified)
    entry["verified_journals"] = sorted({p["journal"] for p in verified if p["journal"]})
    entry["verified_journal_count"] = len(entry["verified_journals"])

    stored = entry.get("regression_cases")
    if not isinstance(stored, dict):
        stored = {"positive": [], "preservation": []}
    cases = observation.get("regression_cases") or {}
    for name in ("positive", "preservation"):
        case = cases.get(name)
        if isinstance(case, dict) and case:
            stored[name] = _dedupe_objects(list(stored.get(name) or []) + [case])
    entry["regression_cases"] = stored
    entry["status"] = evidence_status(entry)
    entry["auto_action"] = action_for(entry)


def merge_resolution(registry: dict, observation: dict, skills_root: Path) -> None:
    defect_id = str(observation.get("defect_id") or "").strip()
    entry = registry.get("defects", {}).get(defect_id)
    if not entry:
        raise ValueError(f"Cannot resolve unknown defect: {defect_id}")
    resolution = observation.get("resolution")
    if not isinstance(resolution, dict):
        raise ValueError("Resolution update requires a resolution mapping.")
    verify_resolution(resolution, entry, skills_root)
    entry["resolution_history"] = _dedupe_objects(entry.get("resolution_history", []) + [resolution])
    entry["lifecycle"] = "resolved" if resolution["status"] == "applied" else "needs_revision"
    entry["auto_action"] = action_for(entry)


def apply_feedback(registry: dict, feedback: dict, skills_root: Path | None = None, verify_targets: bool = True) -> dict:
    result = copy.deepcopy(registry)
    observations = feedback.get("observations", [])
    if not isinstance(observations, list):
        raise ValueError("skill_design_feedback.observations must be a list.")
    observed_on = str(feedback.get("last_updated") or date.today())
    root = skills_root or Path(__file__).parent.parent
    for observation in observations:
        if not isinstance(observation, dict):
            raise ValueError("Each design-feedback observation must be a mapping.")
        resolution_only = bool(observation.get("resolution")) and not observation.get("current_rule")
        if resolution_only:
            merge_resolution(result, observation, root)
            continue
        if verify_targets:
            verify_rule_target(observation, root)
        merge_observation(result, observation, observed_on)
        if observation.get("resolution"):
            merge_resolution(result, observation, root)
    meta = result.setdefault("meta", {})
    meta["schema_version"] = 1
    meta["last_updated"] = observed_on
    meta["observations_processed"] = int(meta.get("observations_processed", 0)) + len(observations)
    return result


def self_test() -> None:
    registry = load_registry(Path("__missing_registry_for_self_test__.yaml"))
    regressions = {
        "positive": {"prompt": "Non-diagonal combination", "expected_invariants": ["independent routing"]},
        "preservation": {"prompt": "Aligned combination", "expected_invariants": ["existing route remains available"]},
    }
    feedback = {
        "last_updated": "2026-08-03",
        "observations": [
            {
                "defect_id": "conversation-gap-coupling",
                "classification": "routing_defect",
                "current_rule": "Gap type determines Conversation.",
                "rule_excerpt": "Gap type determines Conversation.",
                "target": "write-introduction/corpus/_routing_tables.yaml",
                "diagnosis": "The axes are independent.",
                "risk": "medium",
                "regression_cases": regressions,
                "evidence": {"papers": [
                    {"id": "p1", "journal": "AMJ", "evidence_quality": "full_text_verified"},
                    {"id": "p2", "journal": "ASQ", "evidence_quality": "full_text_verified"},
                    {"id": "p3", "journal": "AMJ", "evidence_quality": "full_text_verified"},
                ]},
            },
            {
                "defect_id": "fixed-paragraph-rule",
                "classification": "output_contract_defect",
                "current_rule": "P2 must always be Literature Turn.",
                "rule_excerpt": "P2 must always be Literature Turn.",
                "target": "write-introduction/SKILL.md",
                "diagnosis": "Compact Introductions merge functions.",
                "absolute_rule": True,
                "decisive_falsifier": True,
                "risk": "low",
                "regression_cases": regressions,
                "evidence": {"papers": [{"id": "p4", "journal": "JM", "evidence_quality": "full_text_verified"}]},
            },
        ],
    }
    result = apply_feedback(registry, feedback, verify_targets=False)
    assert result["defects"]["conversation-gap-coupling"]["status"] == "VERIFIED"
    assert result["defects"]["conversation-gap-coupling"]["auto_action"]["eligibility"] == "safe_core_patch_candidate"
    assert result["defects"]["fixed-paragraph-rule"]["status"] == "FALSIFIER"
    assert result["defects"]["fixed-paragraph-rule"]["auto_action"]["eligibility"] == "conditionalize_candidate"

    missing_preservation = copy.deepcopy(feedback["observations"][0])
    missing_preservation["defect_id"] = "missing-preservation"
    missing_preservation["regression_cases"].pop("preservation")
    try:
        apply_feedback(registry, {"observations": [missing_preservation]}, verify_targets=False)
    except ValueError as exc:
        assert "preservation" in str(exc)
    else:
        raise AssertionError("Missing preservation regression should fail.")

    lower_quality = copy.deepcopy(feedback["observations"][0])
    lower_quality["evidence"] = {"papers": [{"id": "p1", "journal": "AMJ", "evidence_quality": "functional_summary"}]}
    preserved = apply_feedback(result, {"observations": [lower_quality]}, verify_targets=False)
    p1 = next(p for p in preserved["defects"]["conversation-gap-coupling"]["papers"] if p["id"] == "p1")
    assert p1["evidence_quality"] == "full_text_verified"

    with tempfile.TemporaryDirectory() as temp_dir:
        skills_root = Path(temp_dir)
        routing = skills_root / "write-introduction" / "corpus" / "_routing_tables.yaml"
        routing.parent.mkdir(parents=True)
        routing.write_text("Gap type determines Conversation.\n", encoding="utf-8")
        skill = skills_root / "write-introduction" / "SKILL.md"
        skill.write_text("P2 must always be Literature Turn.\n", encoding="utf-8")
        verify_rule_target(feedback["observations"][0], skills_root)
        routing.write_text("Conversation is routed independently from Gap type.\n", encoding="utf-8")
        resolution = {
            "defect_id": "conversation-gap-coupling",
            "resolution": {
                "status": "applied",
                "modified_targets": ["write-introduction/corpus/_routing_tables.yaml"],
                "rule_excerpt_after": "Conversation is routed independently from Gap type.",
                "old_rule_excerpt_absent": True,
                "validation": {"quick_validate": True, "regression": True, "forward_test": True},
                "date": "2026-08-04",
            },
        }
        resolved = apply_feedback(result, {"last_updated": "2026-08-04", "observations": [resolution]}, skills_root=skills_root)
        assert resolved["defects"]["conversation-gap-coupling"]["lifecycle"] == "resolved"
        registry_path = Path(temp_dir) / "registry.yaml"
        save_registry(registry_path, resolved)
        reloaded = load_registry(registry_path)
        assert reloaded["meta"]["observations_processed"] == 3
    print("SELF_TEST_OK")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="YAML file containing skill_design_feedback")
    parser.add_argument("--stdin", action="store_true", help="Read YAML from stdin")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY, help="Override registry path")
    parser.add_argument("--dry-run", action="store_true", help="Validate and print without writing")
    parser.add_argument("--self-test", action="store_true", help="Run deterministic in-memory tests")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return
    feedback = load_yaml(args.input, args.stdin)
    registry = load_registry(args.registry)
    updated = apply_feedback(registry, feedback)
    if args.dry_run:
        print(yaml.safe_dump(updated, allow_unicode=True, sort_keys=False, width=120))
        return
    save_registry(args.registry, updated)
    print(f"Design-feedback registry updated: {args.registry}")
    print(f"Observations processed: {updated['meta']['observations_processed']}")


if __name__ == "__main__":
    main()
