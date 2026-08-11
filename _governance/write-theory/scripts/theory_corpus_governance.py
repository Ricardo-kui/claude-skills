#!/usr/bin/env python3
"""Apply validated, reversible governance changes to the Theory corpus."""

from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from copy import deepcopy
from pathlib import Path

import yaml

import theory_asset_catalog as catalog


SKILL_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = SKILL_ROOT / "corpus"
REGISTRY_NAME = "_evidence_registry.yaml"
START = "# -- THEORY ASSET GOVERNANCE START --"
END = "# -- THEORY ASSET GOVERNANCE END --"
VALID_ACTIONS = {
    "NONE", "REUSE", "EXTEND_SOURCE", "ADD_REFERENCE", "PROPOSE_VARIANT",
    "PROMOTE", "MERGE", "DEPRECATE", "SET_REFERENCE_MENU", "RECORD_VALIDATION",
    "PROPOSE_ROUTING_CHANGE",
}


class GovernanceError(ValueError):
    pass


def _plain_registry(path: Path) -> dict:
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=catalog.UniqueKeyLoader)
    if not isinstance(data, dict) or not isinstance(data.get("patterns"), dict):
        raise GovernanceError("Evidence registry must contain patterns")
    return data


def _split_governance(text: str) -> tuple[str, str]:
    if START not in text:
        return text.rstrip() + "\n\n", ""
    if text.count(START) != 1 or text.count(END) != 1:
        raise GovernanceError("Invalid Theory asset governance markers")
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    return before.rstrip() + "\n\n", after.lstrip("\n")


def _with_governance(text: str, governance: dict) -> str:
    before, after = _split_governance(text)
    payload = yaml.safe_dump({"asset_governance": governance}, allow_unicode=True, sort_keys=False)
    return before + START + "\n" + payload + END + ("\n" + after if after else "\n")


def _metadata_ids(corpus_dir: Path) -> set[str]:
    return set(catalog._metadata_occurrences(corpus_dir))


def _bootstrap_governance(corpus_dir: Path, registry: dict) -> dict:
    occurrences = catalog._metadata_occurrences(corpus_dir)
    duplicate = {key: paths for key, paths in occurrences.items() if len(paths) > 1}
    if duplicate:
        raise GovernanceError("Duplicate corpus pattern_id: " + ", ".join(sorted(duplicate)))
    registered = {str(key).casefold() for key in registry["patterns"]}
    legacy_count = len(set(occurrences) - registered)
    governance = {
        "schema_version": 1,
        "policy": {
            "single_paper": "reference_only",
            "default_action_order": ["NONE", "REUSE", "EXTEND_SOURCE", "ADD_REFERENCE", "PROPOSE_VARIANT"],
            "cross_family_merge": "review_only",
        },
        "default_architecture_record": {
            "role": "generative_strategy", "lifecycle": "active", "evidence_status": "structural",
            "legacy_ids": [], "validation_history_additions": [],
        },
        "default_pattern_record": {
            "role": "reference_exemplar", "lifecycle": "active", "legacy_ids": [],
            "validation_history_additions": [], "source_paper_additions": [],
        },
        "default_legacy_record": {
            "role": "reference_exemplar", "lifecycle": "active", "evidence_status": "UNREGISTERED",
            "legacy_ids": [], "validation_history_additions": [], "source_paper_additions": [],
        },
        "asset_overrides": {},
        "managed_references": {},
        "representative_reference_menus": {},
        "reference_menu_cap": 5,
        "render_cap": 4,
        "section_render_cap": 8,
        "snapshot": {
            "architecture_assets": 7,
            "pattern_assets": len(registry["patterns"]) + legacy_count,
            "inventory_sha256": "PENDING",
        },
    }
    return governance


def _set_snapshot(corpus_dir: Path, registry: dict, governance: dict) -> None:
    staged = deepcopy(registry)
    staged["asset_governance"] = governance
    architectures = catalog._architecture_assets(corpus_dir, governance)
    patterns = catalog._pattern_assets(corpus_dir, staged)
    governance["snapshot"] = {
        "architecture_assets": len(architectures),
        "pattern_assets": len(patterns),
        "inventory_sha256": catalog.inventory_fingerprint(architectures, patterns),
    }


def initialize(root: Path = SKILL_ROOT, *, dry_run: bool = False) -> dict:
    corpus_dir = root / "corpus"
    registry_path = corpus_dir / REGISTRY_NAME
    original = registry_path.read_text(encoding="utf-8")
    registry = _plain_registry(registry_path)
    if "asset_governance" in registry:
        architectures, patterns = catalog.load_catalog(corpus_dir, registry_path)
        return {
            "validated": True,
            "dry_run": dry_run,
            "already_initialized": True,
            "architecture_assets": len(architectures),
            "pattern_assets": len(patterns),
            "inventory_sha256": registry["asset_governance"]["snapshot"]["inventory_sha256"],
        }
    governance = _bootstrap_governance(corpus_dir, registry)
    _set_snapshot(corpus_dir, registry, governance)
    updated = _with_governance(original, governance)
    if not dry_run:
        _atomic_write(registry_path, updated)
        catalog.load_catalog(corpus_dir, registry_path)
    return {"validated": True, "dry_run": dry_run, **governance["snapshot"]}


def _atomic_write(path: Path, text: str) -> None:
    fd, name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def _read_plan(path: Path) -> list[dict]:
    data = yaml.load(path.read_text(encoding="utf-8"), Loader=catalog.UniqueKeyLoader)
    rows = data.get("actions") if isinstance(data, dict) else None
    if rows is None and isinstance(data, dict) and isinstance(data.get("governance_plan"), dict):
        rows = data["governance_plan"].get("actions")
    if not isinstance(rows, list):
        raise GovernanceError("Governance plan requires an actions list")
    for row in rows:
        if not isinstance(row, dict) or row.get("action") not in VALID_ACTIONS:
            raise GovernanceError("Every action requires a supported action type")
    return rows


def _record(governance: dict, asset_id: str) -> dict:
    return governance["asset_overrides"].setdefault(asset_id, {})


def _require(row: dict, *keys: str) -> None:
    missing = [key for key in keys if not row.get(key)]
    if missing:
        raise GovernanceError("Missing required fields: " + ", ".join(missing))


def _sources_for(asset: catalog.PatternAsset, governance: dict) -> list[str]:
    override = governance["asset_overrides"].get(asset.asset_id, {})
    base = override.get("source_papers_override", asset.source_papers)
    return list(dict.fromkeys([*base, *override.get("source_paper_additions", [])]))


def _status_for(sources: list[str], registry: dict) -> str:
    return catalog._status_for_sources(sources, registry.get("source_papers", {}))


def _append_reference(text: str, action: dict) -> str:
    entry = (
        "\n\n---\n\n<!--\n"
        f"pattern_id: {action['pattern_id']}\n"
        f"build_type: {action['family']}\n"
        f"source_papers: [{json.dumps(action['source_paper'], ensure_ascii=False)}]\n"
        "confidence: low\n"
        "governance_role: reference_exemplar\n"
        "-->\n\n"
        f"### {action['title']}\n\n"
        f"**适用场景**: {action.get('applicability', '待跨论文验证的精确参考。')}\n\n"
        "**骨架**:\n```text\n"
        f"{action['template']}\n"
        "```\n\n"
        f"**来源**: {action['source_paper']}\n\n"
        "**治理边界**: 单篇 reference exemplar；不进入默认生成菜单。\n"
    )
    return text.rstrip() + entry


def _staged_catalog(root: Path, registry_text: str) -> tuple[list[catalog.ArchitectureAsset], list[catalog.PatternAsset]]:
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", encoding="utf-8", delete=False) as handle:
        handle.write(registry_text)
        temporary = Path(handle.name)
    try:
        return catalog.load_catalog(root / "corpus", temporary)
    finally:
        temporary.unlink(missing_ok=True)


def apply_plan(root: Path, plan_path: Path, *, dry_run: bool = False) -> dict:
    corpus_dir = root / "corpus"
    registry_path = corpus_dir / REGISTRY_NAME
    registry_text = registry_path.read_text(encoding="utf-8")
    registry = _plain_registry(registry_path)
    if "asset_governance" not in registry:
        raise GovernanceError("Initialize asset governance before applying a plan")
    governance = deepcopy(registry["asset_governance"])
    architectures, patterns = catalog.load_catalog(corpus_dir, registry_path)
    assets: dict[str, catalog.ArchitectureAsset | catalog.PatternAsset] = {item.asset_id: item for item in [*architectures, *patterns]}
    actions = _read_plan(plan_path)
    markdown_updates: dict[Path, str] = {}
    added: list[str] = []
    for row in actions:
        action = row["action"]
        if action in {"NONE", "REUSE"}:
            continue
        if action == "PROPOSE_ROUTING_CHANGE":
            raise GovernanceError("Routing changes are review-only and cannot be auto-applied")
        if action == "PROPOSE_VARIANT":
            _require(row, "target_architecture_id", "nearest_neighbor_id", "capability_loss_if_merged")
            parent = assets.get(row["target_architecture_id"])
            neighbor = assets.get(row["nearest_neighbor_id"])
            if not isinstance(parent, catalog.ArchitectureAsset) or not isinstance(neighbor, catalog.PatternAsset):
                raise GovernanceError("PROPOSE_VARIANT requires an architecture and a reference neighbor")
            if parent.family not in neighbor.compatible_families:
                raise GovernanceError("PROPOSE_VARIANT nearest neighbor must belong to target architecture family")
            continue
        if action == "ADD_REFERENCE":
            _require(row, "pattern_id", "target_architecture_id", "home_file", "title", "source_paper", "template", "nearest_neighbor_id", "capability_loss_if_merged")
            pattern_id = str(row["pattern_id"]).casefold()
            if pattern_id in _metadata_ids(corpus_dir) or pattern_id in {key.casefold() for key in governance["managed_references"]}:
                raise GovernanceError(f"Duplicate pattern_id: {row['pattern_id']}")
            parent = assets.get(row["target_architecture_id"])
            neighbor = assets.get(row["nearest_neighbor_id"])
            if not isinstance(parent, catalog.ArchitectureAsset) or not isinstance(neighbor, catalog.PatternAsset):
                raise GovernanceError("ADD_REFERENCE requires an architecture and a reference neighbor")
            slot = str(row.get("slot") or neighbor.slot)
            if neighbor.family not in {parent.family, "cross_family"} or neighbor.slot != slot:
                raise GovernanceError("ADD_REFERENCE nearest neighbor must share target family and slot")
            home = Path(str(row["home_file"]))
            if home.is_absolute() or ".." in home.parts or not (corpus_dir / home).is_file():
                raise GovernanceError("ADD_REFERENCE home_file must be an existing corpus-relative Markdown file")
            managed = {
                "title": row["title"], "family": parent.family, "slot": slot,
                "source_file": home.as_posix(), "source_papers": [row["source_paper"]],
                "status": "EMERGING", "capability_signature": row.get("capability_signature", {}),
            }
            governance["managed_references"][pattern_id] = managed
            source_path = corpus_dir / home
            markdown_updates[source_path] = _append_reference(markdown_updates.get(source_path, source_path.read_text(encoding="utf-8")), {**row, "family": parent.family, "pattern_id": pattern_id})
            added.append(f"theory:managed:{pattern_id}")
            continue
        if action == "SET_REFERENCE_MENU":
            _require(row, "target_architecture_id", "asset_ids")
            parent = assets.get(row["target_architecture_id"])
            ids = row["asset_ids"]
            if not isinstance(parent, catalog.ArchitectureAsset) or not isinstance(ids, list):
                raise GovernanceError("SET_REFERENCE_MENU requires an architecture and an asset list")
            if len(ids) > int(governance.get("reference_menu_cap", 5)) or len(set(ids)) != len(ids):
                raise GovernanceError("Invalid reference menu size or duplicate assets")
            for asset_id in ids:
                item = assets.get(asset_id)
                if not isinstance(item, catalog.PatternAsset) or parent.family not in item.compatible_families:
                    raise GovernanceError("Reference menus must contain same-family pattern assets")
            governance["representative_reference_menus"][parent.asset_id] = ids
            continue
        target_id = row.get("target_asset_id") or row.get("source_asset_id")
        target = assets.get(target_id or "")
        if target is None:
            raise GovernanceError(f"Unknown target asset: {target_id}")
        if action == "EXTEND_SOURCE":
            if not isinstance(target, catalog.PatternAsset):
                raise GovernanceError("EXTEND_SOURCE applies only to pattern assets")
            _require(row, "source_paper")
            record = _record(governance, target.asset_id)
            additions = record.setdefault("source_paper_additions", [])
            if row["source_paper"] not in additions and row["source_paper"] not in target.source_papers:
                additions.append(row["source_paper"])
            record["evidence_status"] = _status_for(_sources_for(target, governance), registry)
        elif action == "PROMOTE":
            if not isinstance(target, catalog.PatternAsset):
                raise GovernanceError("PROMOTE applies only to pattern assets")
            _require(row, "evidence_status", "paper_count", "verification_basis", "source_papers")
            sources = row["source_papers"]
            if not isinstance(sources, list) or len(set(sources)) != len(sources) or len(sources) != int(row["paper_count"]):
                raise GovernanceError("PROMOTE source_papers must provide one unique source per claimed paper")
            if row["evidence_status"] not in {"VERIFIED", "ROBUST"} or len(sources) < 3:
                raise GovernanceError("PROMOTE requires VERIFIED/ROBUST evidence from at least three papers")
            record = _record(governance, target.asset_id)
            record.update({"role": "generative_strategy", "evidence_status": row["evidence_status"], "verification_basis": row["verification_basis"], "source_papers_override": list(sources)})
        elif action == "MERGE":
            _require(row, "source_asset_id", "target_asset_id", "capability_overlap")
            source = assets.get(row["source_asset_id"])
            destination = assets.get(row["target_asset_id"])
            if not isinstance(source, catalog.PatternAsset) or not isinstance(destination, catalog.PatternAsset):
                raise GovernanceError("MERGE applies only to pattern assets")
            if source.family != destination.family or source.slot != destination.slot:
                raise GovernanceError("MERGE must remain within one family and slot")
            record = _record(governance, source.asset_id)
            record.update({"role": "reference_exemplar", "lifecycle": "merged", "merged_into": destination.asset_id})
        elif action == "DEPRECATE":
            _require(row, "reason")
            if isinstance(target, catalog.ArchitectureAsset):
                raise GovernanceError("Architecture deprecation requires explicit routing review")
            record = _record(governance, target.asset_id)
            record.update({"role": "reference_exemplar", "lifecycle": "deprecated", "deprecation_reason": row["reason"]})
        elif action == "RECORD_VALIDATION":
            _require(row, "validation_id", "verdict", "reason")
            if row["verdict"] not in {"VALIDATED", "REVISE", "REJECT"}:
                raise GovernanceError("Unsupported validation verdict")
            record = _record(governance, target.asset_id)
            history = record.setdefault("validation_history_additions", [])
            if not any(item.get("validation_id") == row["validation_id"] for item in history if isinstance(item, dict)):
                history.append({"validation_id": row["validation_id"], "verdict": row["verdict"], "reason": row["reason"]})
        else:
            raise GovernanceError(f"Unsupported governance action: {action}")
    _set_snapshot(corpus_dir, registry, governance)
    updated_registry = _with_governance(registry_text, governance)
    _staged_catalog(root, updated_registry)
    if dry_run:
        return {"validated": True, "dry_run": True, "added_ids": added, **governance["snapshot"]}
    originals = {registry_path: registry_text, **{path: path.read_text(encoding="utf-8") for path in markdown_updates}}
    try:
        for path, text in markdown_updates.items():
            _atomic_write(path, text)
        _atomic_write(registry_path, updated_registry)
        catalog.load_catalog(corpus_dir, registry_path)
    except Exception:
        for path, text in originals.items():
            _atomic_write(path, text)
        raise
    return {"validated": True, "dry_run": False, "added_ids": added, **governance["snapshot"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    initialize_parser = sub.add_parser("initialize")
    initialize_parser.add_argument("--dry-run", action="store_true")
    apply_parser = sub.add_parser("apply-plan")
    apply_parser.add_argument("plan", type=Path)
    apply_parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    result = initialize(dry_run=args.dry_run) if args.command == "initialize" else apply_plan(SKILL_ROOT, args.plan, dry_run=args.dry_run)
    print(yaml.safe_dump(result, allow_unicode=True, sort_keys=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
