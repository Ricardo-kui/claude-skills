#!/usr/bin/env python3
"""Apply validated lifecycle changes to the write-results corpus."""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path

import yaml

import results_variant_catalog as catalog


BEGIN_MARKER = "# BEGIN MANAGED ASSET GOVERNANCE"
END_MARKER = "# END MANAGED ASSET GOVERNANCE"
PROMOTION_FIELDS = {
    "status",
    "paper_count",
    "cross_subfields",
    "verification_basis",
    "behavior_validation",
}
SUPPORTED_ACTIONS = {
    "NONE",
    "REUSE",
    "EXTEND_SOURCE",
    "ADD_REFERENCE",
    "PROPOSE_OPERATOR",
    "PROMOTE",
    "MERGE",
    "DEPRECATE",
}


class GovernanceError(ValueError):
    pass


def _load_plan(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    actions = data.get("actions") if isinstance(data, dict) else None
    if not isinstance(actions, list) or not actions:
        raise GovernanceError("Plan must contain a non-empty actions list")
    for row in actions:
        if not isinstance(row, dict) or row.get("action") not in SUPPORTED_ACTIONS:
            raise GovernanceError(f"Unsupported governance action: {row}")
    return actions


def _required(row: dict, *keys: str) -> None:
    missing = [key for key in keys if row.get(key) in (None, "", [])]
    if missing:
        raise GovernanceError(f"{row.get('action')} lacks required fields: {', '.join(missing)}")


def _override(governance: dict, asset_id: str) -> dict:
    return governance["overrides"].setdefault(asset_id, {})


def _effective_record(governance: dict, asset_id: str) -> dict:
    record = dict(governance["default_record"])
    record.update(governance["overrides"].get(asset_id, {}))
    return record


def _require_active(governance: dict, asset_id: str) -> None:
    if _effective_record(governance, asset_id).get("lifecycle") != "active":
        raise GovernanceError(f"Governance action requires an active asset: {asset_id}")


def _remove_promotion(record: dict) -> None:
    for field in PROMOTION_FIELDS:
        record.pop(field, None)
    record["role"] = "reference_exemplar"


def _apply_state_action(row: dict, governance: dict, known_ids: set[str]) -> None:
    action = row["action"]
    if action in {"NONE", "REUSE"}:
        return
    if action == "PROPOSE_OPERATOR":
        _required(row, "target_asset_id", "capability_loss_if_merged")
        if row["target_asset_id"] not in known_ids:
            raise GovernanceError(f"Unknown target asset: {row['target_asset_id']}")
        _require_active(governance, row["target_asset_id"])
        return
    if action == "EXTEND_SOURCE":
        _required(row, "target_asset_id", "source_paper")
        asset_id = row["target_asset_id"]
        if asset_id not in known_ids:
            raise GovernanceError(f"Unknown target asset: {asset_id}")
        _require_active(governance, asset_id)
        record = _override(governance, asset_id)
        additions = record.setdefault("evidence_additions", [])
        if row["source_paper"] not in additions:
            additions.append(row["source_paper"])
        return
    if action == "PROMOTE":
        _required(
            row,
            "target_asset_id",
            "role",
            "status",
            "paper_count",
            "verification_basis",
        )
        asset_id = row["target_asset_id"]
        if asset_id not in known_ids:
            raise GovernanceError(f"Unknown target asset: {asset_id}")
        _require_active(governance, asset_id)
        record = _override(governance, asset_id)
        for field in PROMOTION_FIELDS:
            record.pop(field, None)
        record.update(
            role=row["role"],
            lifecycle="active",
            status=row["status"],
            paper_count=row["paper_count"],
            cross_subfields=row.get("cross_subfields", 1),
            verification_basis=row["verification_basis"],
        )
        if row.get("behavior_validation"):
            record["behavior_validation"] = row["behavior_validation"]
        return
    if action == "MERGE":
        _required(row, "source_asset_id", "target_asset_id", "capability_overlap")
        source = row["source_asset_id"]
        target = row["target_asset_id"]
        if source not in known_ids or target not in known_ids or source == target:
            raise GovernanceError(f"Invalid merge edge: {source} -> {target}")
        _require_active(governance, source)
        _require_active(governance, target)
        source_record = _override(governance, source)
        _remove_promotion(source_record)
        source_record.update(lifecycle="merged", merged_into=target)
        return
    if action == "DEPRECATE":
        _required(row, "target_asset_id", "reason")
        asset_id = row["target_asset_id"]
        if asset_id not in known_ids:
            raise GovernanceError(f"Unknown target asset: {asset_id}")
        _require_active(governance, asset_id)
        record = _override(governance, asset_id)
        _remove_promotion(record)
        record.update(lifecycle="deprecated", deprecation_reason=row["reason"])


def _reference_block(row: dict, number: int) -> str:
    _required(
        row,
        "target_file",
        "target_slot",
        "title",
        "source_paper",
        "skeleton",
        "capability_loss_if_merged",
        "nearest_neighbor_id",
    )
    slots = [slot.strip() for slot in re.split(r"[,/|]", str(row["target_slot"]))]
    if not slots or any(catalog._canonical_slot(slot) is None for slot in slots):
        raise GovernanceError(f"Invalid ADD_REFERENCE slot declaration: {row['target_slot']}")
    return (
        f"\n\n### 变体 {number}: {row['title']}\n"
        f"**来源论文**: {row['source_paper']}\n"
        "**验证状态**: EMERGING（单篇 reference_exemplar）\n"
        f"**写入日期**: {date.today().isoformat()}\n"
        f"**槽位**: {row['target_slot']}\n"
        "**骨架**:\n"
        f"> {row['skeleton']}\n"
        f"**最近邻**: {row['nearest_neighbor_id']}\n"
        f"**合并能力损失**: {row['capability_loss_if_merged']}\n"
    )


def _materialized_role(governance: dict, asset_id: str) -> str:
    record = dict(governance["default_record"])
    record.update(governance["overrides"].get(asset_id, {}))
    return record.get("role", "reference_exemplar")


def _render_registry(original: str, data: dict, type_counts: dict[str, int], role_counts: Counter) -> str:
    governance_yaml = yaml.safe_dump(
        {"asset_governance": data["asset_governance"]},
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).rstrip()
    replacement = f"{BEGIN_MARKER}\n{governance_yaml}\n{END_MARKER}"
    pattern = re.compile(
        rf"{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}",
        re.DOTALL,
    )
    if not pattern.search(original):
        raise GovernanceError("Managed asset governance markers are missing")
    text = pattern.sub(replacement, original, count=1)
    total = sum(type_counts.values())
    filled = sum(value > 0 for value in type_counts.values())
    scalar_updates = {
        "last_updated": f"'{date.today().isoformat()}'",
        "filled_result_types": str(filled),
        "total_variants": str(total),
    }
    for key, value in scalar_updates.items():
        text = re.sub(rf"(?m)^  {key}:.*$", f"  {key}: {value}", text, count=1)
    for role in ("core_operator", "optional_operator", "reference_exemplar"):
        text = re.sub(
            rf"(?m)^    {role}:\s*\d+\s*$",
            f"    {role}: {role_counts[role]}",
            text,
            count=1,
        )
    for result_type, count in type_counts.items():
        text = re.sub(
            rf"(?m)^    {re.escape(result_type)}:\s*\d+\s*$",
            f"    {result_type}: {count}",
            text,
            count=1,
        )
    return text


def _render_index(original: str, type_counts: dict[str, int], role_counts: Counter) -> str:
    text = re.sub(r"(?m)^updated:\s*.*$", f"updated: {date.today().isoformat()}", original, count=1)
    for result_type, count in type_counts.items():
        pattern = re.compile(
            rf"(?m)^(\| \[{re.escape(result_type)}\]\([^)]+\) \|[^|]+\|)\s*\d+(\s*\|)"
        )
        text = pattern.sub(rf"\g<1> {count}\g<2>", text, count=1)
    total = sum(type_counts.values())
    text = re.sub(r"当前共 \*\*\d+\*\* 个可解析资产", f"当前共 **{total}** 个可解析资产", text, count=1)
    text = re.sub(
        r"\d+ 个 registry 明示的 optional operators、\d+ 个单篇/EMERGING/未充分结构化的 reference exemplars",
        f"{role_counts['optional_operator']} 个 registry 明示的 optional operators、{role_counts['reference_exemplar']} 个单篇/EMERGING/未充分结构化的 reference exemplars",
        text,
        count=1,
    )
    return text


def _atomic_write(path: Path, text: str) -> None:
    temp = path.with_name(f".{path.name}.governance.tmp")
    temp.write_text(text, encoding="utf-8")
    os.replace(temp, path)


def _validate_staged(skill_root: Path, files: dict[Path, str]) -> None:
    with tempfile.TemporaryDirectory(prefix="results-governance-") as tmp:
        staged_root = Path(tmp)
        staged_corpus = staged_root / "econometric-models"
        staged_corpus.mkdir()
        for source in (skill_root / "econometric-models").glob("*.md"):
            target = staged_corpus / source.name
            target.write_text(files.get(source, source.read_text(encoding="utf-8")), encoding="utf-8")
        registry_source = skill_root / "econometric-models" / "_evidence_registry.yaml"
        staged_registry = staged_corpus / registry_source.name
        staged_registry.write_text(files.get(registry_source, registry_source.read_text(encoding="utf-8")), encoding="utf-8")
        catalog.load_catalog(staged_corpus, staged_registry)


def apply_plan(skill_root: Path, plan_path: Path, dry_run: bool = False) -> dict:
    registry_path = skill_root / "econometric-models" / "_evidence_registry.yaml"
    index_path = skill_root / "econometric-models" / "INDEX.md"
    registry_text = registry_path.read_text(encoding="utf-8")
    registry = catalog._load_registry(registry_path)
    variants, _ = catalog.load_catalog(skill_root / "econometric-models", registry_path)
    known_ids = {item.asset_id for item in variants}
    type_counts = Counter(item.result_type for item in variants)
    governance = registry["asset_governance"]
    staged_files: dict[Path, str] = {}
    added_ids: list[str] = []

    actions = _load_plan(plan_path)
    for row in actions:
        if row["action"] != "ADD_REFERENCE":
            _apply_state_action(row, governance, known_ids)
            continue
        target_name = str(row.get("target_file", ""))
        if not target_name.endswith(".md"):
            target_name += ".md"
        if Path(target_name).name != target_name:
            raise GovernanceError("ADD_REFERENCE target_file must be a corpus filename, not a path")
        target_path = skill_root / "econometric-models" / target_name
        result_type = target_path.stem
        if result_type not in type_counts or type_counts[result_type] == 0:
            raise GovernanceError("ADD_REFERENCE currently requires an already-filled result type")
        nearest = row.get("nearest_neighbor_id")
        if nearest != "NONE" and nearest not in known_ids:
            raise GovernanceError(f"ADD_REFERENCE has unknown nearest neighbor: {nearest}")
        if str(row.get("capability_loss_if_merged", "")).strip().upper() == "NONE":
            raise GovernanceError("ADD_REFERENCE requires a concrete capability loss")
        current = staged_files.get(target_path, target_path.read_text(encoding="utf-8"))
        number = type_counts[result_type] + 1
        asset_id = f"{result_type}:v{number}"
        current += _reference_block(row, number)
        staged_files[target_path] = current
        type_counts[result_type] += 1
        governance["inventory"][result_type] += 1
        record = _override(governance, asset_id)
        record["evidence_additions"] = [row["source_paper"]]
        known_ids.add(asset_id)
        added_ids.append(asset_id)

    all_ids = set(known_ids)
    role_counts = Counter(_materialized_role(governance, asset_id) for asset_id in all_ids)
    staged_files[registry_path] = _render_registry(registry_text, registry, dict(type_counts), role_counts)
    staged_files[index_path] = _render_index(
        index_path.read_text(encoding="utf-8"), dict(type_counts), role_counts
    )
    _validate_staged(skill_root, staged_files)
    if not dry_run:
        originals = {path: path.read_text(encoding="utf-8") for path in staged_files}
        try:
            for path, text in staged_files.items():
                _atomic_write(path, text)
        except Exception:
            for path, text in originals.items():
                _atomic_write(path, text)
            raise
    return {
        "validated": True,
        "dry_run": dry_run,
        "actions": len(actions),
        "added_ids": added_ids,
        "asset_count": sum(type_counts.values()),
        "roles": dict(role_counts),
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    apply_parser = subparsers.add_parser("apply-plan")
    apply_parser.add_argument("plan", type=Path)
    apply_parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    try:
        if args.command == "validate":
            variants, _ = catalog.load_catalog(
                args.skill_root / "econometric-models",
                args.skill_root / "econometric-models" / "_evidence_registry.yaml",
            )
            print(yaml.safe_dump({"valid": True, "asset_records": len(variants)}, sort_keys=False).strip())
            return 0
        print(yaml.safe_dump(apply_plan(args.skill_root, args.plan, args.dry_run), sort_keys=False).strip())
        return 0
    except (OSError, GovernanceError, ValueError) as error:
        print(f"Governance error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
