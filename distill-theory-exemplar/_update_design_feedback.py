"""Persist evidence about write-theory design defects.

This ledger script never edits core skills. The design-feedback protocol controls
whether an eligible defect may be patched.
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
    Path(__file__).parent.parent / "write-theory" / "corpus" / "_skill_design_feedback.yaml"
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
RISKS = {"low", "medium", "high"}
EVIDENCE_QUALITIES = {"full_text_verified", "functional_summary", "metadata_only"}
EVIDENCE_RANK = {"metadata_only": 0, "functional_summary": 1, "full_text_verified": 2}


def load_yaml(path: str | None, use_stdin: bool = False) -> dict:
    raw = sys.stdin.read() if use_stdin else Path(path or "").read_text(encoding="utf-8")
    data = yaml.safe_load(raw)
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
                "description": (
                    "Evidence ledger for write-theory design defects inferred from "
                    "Theory exemplar distillation."
                ),
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
        registry, allow_unicode=True, sort_keys=False, default_flow_style=False, width=120
    )
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", delete=False, dir=path.parent, suffix=".tmp"
    ) as handle:
        handle.write(rendered)
        temp_path = Path(handle.name)
    temp_path.replace(path)


def _dedupe(items: list[dict]) -> list[dict]:
    seen: set[str] = set()
    result: list[dict] = []
    for item in items:
        key = json.dumps(item, ensure_ascii=False, sort_keys=True)
        if key not in seen:
            seen.add(key)
            result.append(item)
    return result


def _stable_strings(values: object) -> list[str]:
    if not isinstance(values, list):
        return []
    return sorted({str(value).strip() for value in values if str(value).strip()})


def normalize_paper(raw: object) -> dict:
    if isinstance(raw, str):
        return {
            "id": raw.strip(),
            "journal": "",
            "build_type": "",
            "hypothesis_family": "",
            "evidence_anchor": "",
            "evidence_quality": "metadata_only",
        }
    if not isinstance(raw, dict):
        raise ValueError(f"Paper evidence must be a string or mapping: {raw!r}")
    paper_id = str(raw.get("id") or raw.get("paper_id") or "").strip()
    if not paper_id:
        raise ValueError("Paper evidence is missing id.")
    quality = str(raw.get("evidence_quality") or "functional_summary").strip()
    if quality not in EVIDENCE_QUALITIES:
        raise ValueError(f"Unknown evidence_quality {quality!r} for {paper_id!r}")
    return {
        "id": paper_id,
        "journal": str(raw.get("journal") or "").strip(),
        "build_type": str(raw.get("build_type") or "").strip(),
        "hypothesis_family": str(raw.get("hypothesis_family") or "").strip(),
        "evidence_anchor": str(raw.get("evidence_anchor") or "").strip(),
        "evidence_quality": quality,
    }


def validate_cases(observation: dict) -> None:
    if observation.get("classification") == "corpus_gap":
        return
    cases = observation.get("regression_cases")
    if not isinstance(cases, dict):
        raise ValueError("Core design observations require regression_cases.")
    for name in ("positive", "preservation"):
        case = cases.get(name)
        if not isinstance(case, dict) or not case.get("prompt"):
            raise ValueError(f"Missing regression_cases.{name}.prompt")
        invariants = case.get("expected_invariants")
        if not isinstance(invariants, list) or not invariants:
            raise ValueError(f"Missing regression_cases.{name}.expected_invariants")


def validate_observation(observation: dict) -> None:
    required = ("defect_id", "classification", "current_rule", "target", "diagnosis")
    missing = [field for field in required if not observation.get(field)]
    if missing:
        raise ValueError(f"Observation missing required fields: {missing}")
    if observation["classification"] not in CLASSIFICATIONS:
        raise ValueError(f"Unknown classification: {observation['classification']}")
    if observation.get("risk", "medium") not in RISKS:
        raise ValueError(f"Unknown risk: {observation.get('risk')}")
    if observation["classification"] != "corpus_gap" and not observation.get("rule_excerpt"):
        raise ValueError("Core design observations require an exact rule_excerpt.")
    if observation.get("decisive_falsifier") and not observation.get("absolute_rule"):
        raise ValueError("decisive_falsifier requires absolute_rule: true")
    validate_cases(observation)


def _safe_target(target: str, skills_root: Path) -> Path:
    rel = Path(target)
    if rel.is_absolute() or ".." in rel.parts or ":" in target:
        raise ValueError("target must be a relative skill path without line suffixes.")
    if not rel.parts or rel.parts[0].lower() != "write-theory":
        raise ValueError("Design feedback targets must stay inside write-theory.")
    root = skills_root.resolve()
    resolved = (root / rel).resolve()
    if root not in resolved.parents or not resolved.is_file():
        raise ValueError(f"Target file does not exist inside skills root: {target}")
    return resolved


def verify_rule_target(observation: dict, skills_root: Path) -> None:
    if observation.get("classification") == "corpus_gap":
        return
    target_path = _safe_target(str(observation["target"]), skills_root)
    excerpt = " ".join(str(observation["rule_excerpt"]).split())
    content = " ".join(target_path.read_text(encoding="utf-8").split())
    if excerpt not in content:
        raise ValueError(
            f"rule_excerpt was not found in {observation['target']}; verify the current rule first."
        )


def verify_resolution(resolution: dict, entry: dict, skills_root: Path) -> None:
    targets = resolution.get("modified_targets")
    if not isinstance(targets, list) or not targets:
        raise ValueError("resolution.modified_targets must be a non-empty list.")
    resolved_targets = {str(target): _safe_target(str(target), skills_root) for target in targets}
    validation = resolution.get("validation")
    if not isinstance(validation, dict):
        raise ValueError("resolution.validation must be a mapping.")
    for key in ("quick_validate", "regression", "forward_test"):
        if validation.get(key) is not True and resolution.get("status") == "applied":
            raise ValueError(f"Applied resolution requires validation.{key}: true")
    if resolution.get("status") != "applied":
        return
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


def evidence_status(entry: dict) -> str:
    count = int(entry.get("verified_paper_count", 0))
    journals = int(entry.get("verified_journal_count", 0))
    if entry.get("decisive_falsifier") and entry.get("absolute_rule") and count >= 1:
        return "FALSIFIER"
    if count >= 5 and journals >= 2:
        return "ROBUST"
    if count >= 3 and journals >= 2:
        return "VERIFIED"
    return "EMERGING"


def action_for(entry: dict) -> dict:
    status = entry["status"]
    classification = entry["classification"]
    risk = entry.get("risk", "medium")
    if entry.get("lifecycle") == "resolved":
        return {"eligibility": "no_action", "reason": "Validated correction already applied."}
    if classification == "corpus_gap":
        eligibility = "reference_write" if status in {"VERIFIED", "ROBUST"} else "optional_variant_only"
        return {"eligibility": eligibility, "reason": "Corpus changes do not alter core routing."}
    if classification in HIGH_RISK_CLASSES or risk == "high":
        return {"eligibility": "explicit_review", "reason": "High-risk contract change."}
    if status == "FALSIFIER":
        return {
            "eligibility": "conditionalize_candidate",
            "reason": "Counterexample may weaken an absolute rule, not establish its inverse.",
        }
    if status in {"VERIFIED", "ROBUST"}:
        return {
            "eligibility": "safe_core_patch_candidate",
            "reason": "Cross-paper evidence meets the bounded core-revision threshold.",
        }
    return {"eligibility": "log_only", "reason": "Insufficient evidence for core revision."}


def _merge_applicability(entry: dict, observation: dict) -> None:
    current = entry.setdefault("applicability", {})
    incoming = observation.get("applicability") or {}
    for key in ("build_types", "hypothesis_families", "journals"):
        old_values = current.get(key, []) if isinstance(current.get(key, []), list) else []
        new_values = incoming.get(key, []) if isinstance(incoming.get(key, []), list) else []
        current[key] = _stable_strings(old_values + new_values)
    if incoming.get("boundary"):
        current["boundary"] = str(incoming["boundary"])


def merge_observation(registry: dict, observation: dict, observed_on: str) -> None:
    validate_observation(observation)
    defect_id = str(observation["defect_id"])
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
            "applicability": {},
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
        raise ValueError(f"Classification changed for {defect_id}; use a new defect_id.")
    entry["risk"] = observation.get("risk", entry["risk"])
    entry["diagnosis"] = observation.get("diagnosis", entry["diagnosis"])
    entry["proposed_change"] = observation.get("proposed_change", entry["proposed_change"])
    entry["absolute_rule"] = bool(observation.get("absolute_rule", entry["absolute_rule"]))
    entry["decisive_falsifier"] = bool(
        observation.get("decisive_falsifier") or entry.get("decisive_falsifier")
    )
    entry["last_seen"] = observed_on
    _merge_applicability(entry, observation)

    papers = {paper["id"]: paper for paper in entry.get("papers", [])}
    for raw in (observation.get("evidence") or {}).get("papers", []):
        paper = normalize_paper(raw)
        previous = papers.get(paper["id"], {})
        quality = max(
            (paper["evidence_quality"], previous.get("evidence_quality", "metadata_only")),
            key=lambda item: EVIDENCE_RANK[item],
        )
        papers[paper["id"]] = {
            "id": paper["id"],
            "journal": paper["journal"] or previous.get("journal", ""),
            "build_type": paper["build_type"] or previous.get("build_type", ""),
            "hypothesis_family": paper["hypothesis_family"] or previous.get("hypothesis_family", ""),
            "evidence_anchor": paper["evidence_anchor"] or previous.get("evidence_anchor", ""),
            "evidence_quality": quality,
        }
    entry["papers"] = sorted(papers.values(), key=lambda item: item["id"])
    entry["paper_count"] = len(entry["papers"])
    entry["journals"] = sorted({p["journal"] for p in entry["papers"] if p["journal"]})
    entry["journal_count"] = len(entry["journals"])
    verified = [p for p in entry["papers"] if p["evidence_quality"] == "full_text_verified"]
    entry["verified_paper_count"] = len(verified)
    entry["verified_journals"] = sorted({p["journal"] for p in verified if p["journal"]})
    entry["verified_journal_count"] = len(entry["verified_journals"])

    cases = observation.get("regression_cases") or {}
    stored = entry.setdefault("regression_cases", {"positive": [], "preservation": []})
    for name in ("positive", "preservation"):
        if isinstance(cases.get(name), dict):
            stored[name] = _dedupe(stored.get(name, []) + [cases[name]])
    entry["status"] = evidence_status(entry)
    entry["auto_action"] = action_for(entry)


def merge_resolution(registry: dict, observation: dict, skills_root: Path) -> None:
    defect_id = str(observation.get("defect_id") or "")
    entry = registry.get("defects", {}).get(defect_id)
    if not entry:
        raise ValueError(f"Cannot resolve unknown defect: {defect_id}")
    resolution = observation.get("resolution")
    if not isinstance(resolution, dict):
        raise ValueError("Resolution update requires a resolution mapping.")
    if resolution.get("status") not in {"applied", "needs_revision"}:
        raise ValueError("resolution.status must be applied or needs_revision.")
    verify_resolution(resolution, entry, skills_root)
    entry["resolution_history"] = _dedupe(entry.get("resolution_history", []) + [resolution])
    entry["lifecycle"] = "resolved" if resolution["status"] == "applied" else "needs_revision"
    entry["auto_action"] = action_for(entry)


def apply_feedback(
    registry: dict, feedback: dict, skills_root: Path | None = None, verify_targets: bool = True
) -> dict:
    result = copy.deepcopy(registry)
    observations = feedback.get("observations", [])
    if not isinstance(observations, list):
        raise ValueError("skill_design_feedback.observations must be a list.")
    root = (skills_root or Path(__file__).parent.parent).resolve()
    observed_on = str(feedback.get("last_updated") or date.today())
    for observation in observations:
        if not isinstance(observation, dict):
            raise ValueError("Each observation must be a mapping.")
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
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        target = root / "write-theory" / "SKILL.md"
        target.parent.mkdir(parents=True)
        target.write_text("Every theory must use mediation.\n", encoding="utf-8")
        registry = load_registry(root / "missing.yaml")
        base = {
            "defect_id": "forced-mediation",
            "classification": "output_contract_defect",
            "current_rule": "Every theory must use mediation.",
            "rule_excerpt": "Every theory must use mediation.",
            "target": "write-theory/SKILL.md",
            "diagnosis": "B0 process explanation is legitimate without a measured mediator.",
            "risk": "medium",
            "applicability": {"build_types": ["机制推演型"], "hypothesis_families": ["main_effect_only"]},
            "regression_cases": {
                "positive": {"prompt": "Explain X to Y without measured M", "expected_invariants": ["no invented mediator"]},
                "preservation": {"prompt": "Explain measured mediation", "expected_invariants": ["retain mediation route"]},
            },
        }
        papers = [
            {"id": "p1", "journal": "AMJ", "evidence_quality": "full_text_verified"},
            {"id": "p2", "journal": "SMJ", "evidence_quality": "full_text_verified"},
            {"id": "p3", "journal": "AMJ", "evidence_quality": "full_text_verified"},
        ]
        feedback = {"last_updated": "2026-08-03", "observations": [{**base, "evidence": {"papers": papers}}]}
        result = apply_feedback(registry, feedback, skills_root=root)
        entry = result["defects"]["forced-mediation"]
        assert entry["status"] == "VERIFIED"
        assert entry["auto_action"]["eligibility"] == "safe_core_patch_candidate"

        falsifier = {
            **base,
            "defect_id": "absolute-mediation-rule",
            "absolute_rule": True,
            "decisive_falsifier": True,
            "evidence": {"papers": [{"id": "p4", "journal": "ASQ", "evidence_quality": "full_text_verified"}]},
        }
        with_falsifier = apply_feedback(
            result, {"last_updated": "2026-08-03", "observations": [falsifier]}, skills_root=root
        )
        assert with_falsifier["defects"]["absolute-mediation-rule"]["status"] == "FALSIFIER"
        assert (
            with_falsifier["defects"]["absolute-mediation-rule"]["auto_action"]["eligibility"]
            == "conditionalize_candidate"
        )

        invalid_cases = copy.deepcopy(base)
        invalid_cases["defect_id"] = "missing-preservation"
        invalid_cases["regression_cases"].pop("preservation")
        try:
            apply_feedback(
                with_falsifier,
                {"last_updated": "2026-08-03", "observations": [invalid_cases]},
                skills_root=root,
            )
            raise AssertionError("Missing preservation regression should fail.")
        except ValueError as exc:
            assert "preservation" in str(exc)

        bad_excerpt = copy.deepcopy(base)
        bad_excerpt["defect_id"] = "missing-rule"
        bad_excerpt["rule_excerpt"] = "This rule is not present."
        try:
            apply_feedback(
                with_falsifier,
                {"last_updated": "2026-08-03", "observations": [bad_excerpt]},
                skills_root=root,
            )
            raise AssertionError("Missing rule excerpt should fail.")
        except ValueError as exc:
            assert "rule_excerpt was not found" in str(exc)

        premature_resolution = {
            "defect_id": "forced-mediation",
            "resolution": {
                "status": "applied",
                "modified_targets": ["write-theory/SKILL.md"],
                "rule_excerpt_after": "Mediation is required only when M is measured.",
                "old_rule_excerpt_absent": True,
                "validation": {"quick_validate": True, "regression": True, "forward_test": True},
            },
        }
        try:
            apply_feedback(with_falsifier, {"observations": [premature_resolution]}, skills_root=root)
            raise AssertionError("Resolution without an applied rule change should fail.")
        except ValueError as exc:
            assert "rule_excerpt_after" in str(exc) or "old rule_excerpt" in str(exc)

        target.write_text("Mediation is required only when M is measured.\n", encoding="utf-8")
        resolved = apply_feedback(
            with_falsifier,
            {
                "last_updated": "2026-08-04",
                "observations": [{
                    "defect_id": "forced-mediation",
                    "resolution": {
                        "status": "applied",
                        "modified_targets": ["write-theory/SKILL.md"],
                        "rule_excerpt_after": "Mediation is required only when M is measured.",
                        "old_rule_excerpt_absent": True,
                        "validation": {"quick_validate": True, "regression": True, "forward_test": True},
                        "date": "2026-08-04",
                    },
                }],
            },
            skills_root=root,
        )
        assert resolved["defects"]["forced-mediation"]["lifecycle"] == "resolved"
        registry_path = root / "registry.yaml"
        save_registry(registry_path, resolved)
        assert load_registry(registry_path)["meta"]["observations_processed"] == 3
    print("SELF_TEST_OK")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="YAML file containing skill_design_feedback")
    parser.add_argument("--stdin", action="store_true", help="Read YAML from stdin")
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if not args.input and not args.stdin:
        parser.error("Provide an input path or --stdin.")
    feedback = load_yaml(args.input, args.stdin)
    updated = apply_feedback(load_registry(args.registry), feedback)
    if args.dry_run:
        print(yaml.safe_dump(updated, allow_unicode=True, sort_keys=False, width=120))
        return
    save_registry(args.registry, updated)
    print(f"Design-feedback registry updated: {args.registry}")
    print(f"Observations processed: {updated['meta']['observations_processed']}")


if __name__ == "__main__":
    main()
