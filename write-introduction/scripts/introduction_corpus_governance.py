#!/usr/bin/env python3
"""Apply validated, transactional changes to the Introduction corpus."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

import yaml

import introduction_asset_catalog as catalog


BEGIN_MARKER = "# BEGIN MANAGED ASSET GOVERNANCE"
END_MARKER = "# END MANAGED ASSET GOVERNANCE"
SUPPORTED_ACTIONS = {
    "NONE",
    "REUSE",
    "EXTEND_SOURCE",
    "ADD_REFERENCE",
    "PROPOSE_VARIANT",
    "PROMOTE",
    "MERGE",
    "DEPRECATE",
    "PROPOSE_ROUTING_CHANGE",
    "RECORD_VALIDATION",
    "SET_REFERENCE_MENU",
}
PROMOTION_FIELDS = {"role", "evidence_status", "paper_count", "verification_basis", "source_papers"}


class GovernanceError(ValueError):
    """Raised when a plan violates an asset-governance invariant."""


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


def _asset_kind(asset_id: str, parent_ids: set[str], variant_ids: set[str]) -> str:
    if asset_id in parent_ids:
        return "parent"
    if asset_id in variant_ids:
        return "variant"
    raise GovernanceError(f"Unknown asset: {asset_id}")


def _record(governance: dict, kind: str, asset_id: str) -> dict:
    effective = dict(governance[f"default_{kind}_record"])
    effective.update(governance[f"{kind}_overrides"].get(asset_id, {}))
    return effective


def _override(governance: dict, kind: str, asset_id: str) -> dict:
    return governance[f"{kind}_overrides"].setdefault(asset_id, {})


def _require_active(governance: dict, kind: str, asset_id: str) -> None:
    if _record(governance, kind, asset_id).get("lifecycle") != "active":
        raise GovernanceError(f"Governance action requires an active asset: {asset_id}")


def _remove_promotion(record: dict, kind: str) -> None:
    for field in PROMOTION_FIELDS:
        record.pop(field, None)
    record["role"] = "reference_strategy" if kind == "parent" else "reference_exemplar"


def _apply_state_action(
    row: dict,
    governance: dict,
    parent_ids: set[str],
    variant_ids: set[str],
) -> None:
    action = row["action"]
    if action in {"NONE", "REUSE"}:
        return
    if action == "PROPOSE_ROUTING_CHANGE":
        _required(row, "target", "diagnosis", "explicit_review")
        if row["explicit_review"] is not True:
            raise GovernanceError("Routing changes require explicit_review: true")
        return
    if action == "PROPOSE_VARIANT":
        _required(row, "target_parent_id", "nearest_neighbor_id", "capability_loss_if_merged")
        if row["target_parent_id"] not in parent_ids:
            raise GovernanceError(f"Unknown target parent: {row['target_parent_id']}")
        if row["nearest_neighbor_id"] not in variant_ids:
            raise GovernanceError(f"Unknown nearest neighbor: {row['nearest_neighbor_id']}")
        if not row["nearest_neighbor_id"].startswith(row["target_parent_id"] + ":v"):
            raise GovernanceError("PROPOSE_VARIANT nearest neighbor must belong to target parent")
        if str(row["capability_loss_if_merged"]).strip().upper() == "NONE":
            raise GovernanceError("PROPOSE_VARIANT requires concrete capability loss")
        return
    if action == "ADD_REFERENCE":
        return
    if action == "SET_REFERENCE_MENU":
        _required(row, "target_parent_id", "asset_ids")
        parent_id = row["target_parent_id"]
        asset_ids = row["asset_ids"]
        cap = int(governance.get("active_variant_cap_per_parent", 5))
        if parent_id not in parent_ids or not isinstance(asset_ids, list):
            raise GovernanceError(f"Invalid reference menu parent: {parent_id}")
        if len(asset_ids) > cap or len(asset_ids) != len(set(asset_ids)):
            raise GovernanceError(f"Reference menu exceeds cap or contains duplicates: {parent_id}")
        for asset_id in asset_ids:
            if asset_id not in variant_ids or not asset_id.startswith(parent_id + ":v"):
                raise GovernanceError(f"Invalid reference menu member: {asset_id}")
        governance["representative_reference_menus"][parent_id] = asset_ids
        return

    target_id = row.get("target_asset_id")
    if action == "MERGE":
        _required(row, "source_asset_id", "target_asset_id", "capability_overlap")
        source = row["source_asset_id"]
        target = row["target_asset_id"]
        source_kind = _asset_kind(source, parent_ids, variant_ids)
        target_kind = _asset_kind(target, parent_ids, variant_ids)
        if source == target or source_kind != target_kind:
            raise GovernanceError(f"Invalid merge edge: {source} -> {target}")
        if source_kind == "variant" and source.rsplit(":v", 1)[0] != target.rsplit(":v", 1)[0]:
            raise GovernanceError(f"Variant merges must remain within one parent: {source} -> {target}")
        _require_active(governance, source_kind, source)
        _require_active(governance, target_kind, target)
        record = _override(governance, source_kind, source)
        _remove_promotion(record, source_kind)
        record.update(lifecycle="merged", merged_into=target)
        return

    _required(row, "target_asset_id")
    kind = _asset_kind(target_id, parent_ids, variant_ids)
    _require_active(governance, kind, target_id)
    record = _override(governance, kind, target_id)
    if action == "RECORD_VALIDATION":
        _required(row, "validation_id", "verdict")
        if row["verdict"] not in {"VALIDATED", "REVISE", "REJECT"}:
            raise GovernanceError(f"Invalid validation verdict: {row['verdict']}")
        history = record.setdefault("validation_history_additions", [])
        if not any(item.get("validation_id") == row["validation_id"] for item in history):
            history.append(
                {
                    "validation_id": row["validation_id"],
                    "verdict": row["verdict"],
                    "reason": row.get("reason", ""),
                }
            )
        return
    if action == "EXTEND_SOURCE":
        _required(row, "source_paper")
        additions = record.setdefault("evidence_additions", [])
        if row["source_paper"] not in additions:
            additions.append(row["source_paper"])
        return
    if action == "PROMOTE":
        _required(row, "role", "evidence_status", "paper_count", "verification_basis", "source_papers")
        valid_role = "generative_strategy" if kind == "parent" else "generative_variant"
        if row["role"] != valid_role:
            raise GovernanceError(f"PROMOTE role for {kind} must be {valid_role}")
        if not isinstance(row["paper_count"], int) or row["paper_count"] < 1:
            raise GovernanceError("PROMOTE paper_count must be a positive integer")
        sources = row["source_papers"]
        if not isinstance(sources, list) or not all(isinstance(item, str) and item.strip() for item in sources):
            raise GovernanceError("PROMOTE source_papers must be a non-empty list of source identifiers")
        if len(sources) != len(set(sources)) or len(sources) < row["paper_count"]:
            raise GovernanceError("PROMOTE source_papers must provide one unique source per claimed paper")
        expected_status = "ROBUST" if row["paper_count"] >= 5 else "VERIFIED"
        if row["verification_basis"] != "user_expert_audit" and row["evidence_status"] != expected_status:
            raise GovernanceError("PROMOTE evidence_status is inconsistent with claimed paper_count")
        for field in PROMOTION_FIELDS:
            record.pop(field, None)
        record.update(
            role=row["role"],
            lifecycle="active",
            evidence_status=row["evidence_status"],
            paper_count=row["paper_count"],
            verification_basis=row["verification_basis"],
            source_papers=sources,
        )
        return
    if action == "DEPRECATE":
        _required(row, "reason")
        _remove_promotion(record, kind)
        record.update(lifecycle="deprecated", deprecation_reason=row["reason"])
        return
    raise GovernanceError(f"Unsupported state action: {action}")


def _letters_to_number(token: str) -> int:
    value = 0
    for char in token.upper():
        value = value * 26 + ord(char) - ord("A") + 1
    return value


def _number_to_letters(value: int) -> str:
    result = ""
    while value:
        value, remainder = divmod(value - 1, 26)
        result = chr(ord("A") + remainder) + result
    return result


def _next_variant_token(variants: list[dict], parent_id: str) -> str:
    values = [
        _letters_to_number(item["token"])
        for item in variants
        if item["parent_id"] == parent_id and re.fullmatch(r"[A-Za-z]+", item["token"])
    ]
    return _number_to_letters(max(values, default=0) + 1)


def _reference_block(row: dict, token: str) -> str:
    _required(
        row,
        "title",
        "source_paper",
        "template",
        "nearest_neighbor_id",
        "capability_loss_if_merged",
    )
    if str(row["capability_loss_if_merged"]).strip().upper() == "NONE":
        raise GovernanceError("ADD_REFERENCE requires concrete capability loss")
    applicability = row.get("applicability", "仅作受控类比，不自动成为通用规则")
    taboo = row.get("taboo", "不得复制来源论文的领域填充或事实")
    return (
        f"\n\n### 变体 {token}：{row['title']}\n\n"
        f"**模板**:\n> {row['template']}\n\n"
        f"**来源**: {row['source_paper']}\n\n"
        "**治理角色**: reference_exemplar（单篇资产，不进入默认生成菜单）\n\n"
        f"**最近邻**: {row['nearest_neighbor_id']}\n\n"
        f"**合并能力损失**: {row['capability_loss_if_merged']}\n\n"
        f"**适用**: {applicability}\n\n"
        f"**禁忌**: {taboo}\n"
    )


def _render_registry(original: str, governance: dict) -> str:
    block = yaml.safe_dump(
        {"asset_governance": governance},
        allow_unicode=True,
        sort_keys=False,
        width=1000,
    ).rstrip()
    replacement = f"{BEGIN_MARKER}\n{block}\n{END_MARKER}"
    pattern = re.compile(rf"{re.escape(BEGIN_MARKER)}.*?{re.escape(END_MARKER)}", re.DOTALL)
    if not pattern.search(original):
        raise GovernanceError("Managed asset governance markers are missing")
    return pattern.sub(replacement, original, count=1)


def _atomic_write(path: Path, text: str) -> None:
    temp = path.with_name(f".{path.name}.introduction-governance.tmp")
    temp.write_text(text, encoding="utf-8")
    os.replace(temp, path)


def _stage_and_validate(
    skill_root: Path,
    staged_files: dict[Path, str],
    registry: dict,
) -> tuple[dict[Path, str], int, int]:
    corpus = skill_root / "academic-writing-corpus"
    registry_path = corpus / "_evidence_registry.yaml"
    with tempfile.TemporaryDirectory(prefix="introduction-governance-") as tmp:
        staged_root = Path(tmp) / "academic-writing-corpus"
        shutil.copytree(corpus, staged_root)
        for source, text in staged_files.items():
            target = staged_root / source.relative_to(corpus)
            target.write_text(text, encoding="utf-8")
        parents, variants, _ = catalog.discover_assets(staged_root)
        registry["asset_governance"]["snapshot"].update(
            total_parent_assets=len(parents),
            total_variant_assets=len(variants),
            inventory_sha256=catalog.inventory_fingerprint([item["asset_id"] for item in variants]),
            last_validated=date.today().isoformat(),
        )
        rendered_registry = _render_registry(
            registry_path.read_text(encoding="utf-8"), registry["asset_governance"]
        )
        staged_registry = staged_root / "_evidence_registry.yaml"
        staged_registry.write_text(rendered_registry, encoding="utf-8")
        catalog.load_catalog(staged_root, staged_registry)
    staged_files[registry_path] = rendered_registry
    return staged_files, len(parents), len(variants)


def apply_plan(skill_root: Path, plan_path: Path, dry_run: bool = False) -> dict:
    corpus = skill_root / "academic-writing-corpus"
    registry_path = corpus / "_evidence_registry.yaml"
    registry = catalog._load_registry(registry_path)
    governance = registry["asset_governance"]
    discovered_parents, discovered_variants, _ = catalog.discover_assets(corpus)
    parent_by_id = {item["asset_id"]: item for item in discovered_parents}
    parent_ids = set(parent_by_id)
    variant_ids = {item["asset_id"] for item in discovered_variants}
    staged_files: dict[Path, str] = {}
    originals: dict[Path, str] = {registry_path: registry_path.read_text(encoding="utf-8")}
    added_ids: list[str] = []
    actions = _load_plan(plan_path)

    for row in actions:
        if row["action"] != "ADD_REFERENCE":
            _apply_state_action(row, governance, parent_ids, variant_ids)
            continue
        _required(row, "target_parent_id", "nearest_neighbor_id")
        parent_id = row["target_parent_id"]
        nearest = row["nearest_neighbor_id"]
        if parent_id not in parent_by_id:
            raise GovernanceError(f"Unknown target parent: {parent_id}")
        if nearest not in variant_ids or not nearest.startswith(parent_id + ":v"):
            raise GovernanceError("ADD_REFERENCE nearest neighbor must belong to target parent")
        relative = Path(parent_by_id[parent_id]["source_file"])
        target_path = corpus / relative
        if target_path not in originals:
            originals[target_path] = target_path.read_text(encoding="utf-8")
        current = staged_files.get(target_path, originals[target_path])
        token = _next_variant_token(discovered_variants, parent_id)
        asset_id = f"{parent_id}:v{token}"
        if asset_id in variant_ids:
            raise GovernanceError(f"Generated duplicate asset ID: {asset_id}")
        current += _reference_block(row, token)
        staged_files[target_path] = current
        variant_ids.add(asset_id)
        discovered_variants.append(
            {"asset_id": asset_id, "parent_id": parent_id, "token": token}
        )
        governance["variant_overrides"][asset_id] = {
            "evidence_additions": [row["source_paper"]]
        }
        added_ids.append(asset_id)

    staged_files, parent_count, variant_count = _stage_and_validate(skill_root, staged_files, registry)
    if not dry_run:
        for path in staged_files:
            expected = originals.get(path, path.read_text(encoding="utf-8"))
            if path.read_text(encoding="utf-8") != expected:
                raise GovernanceError(f"Concurrent modification detected: {path}")
        committed_originals = {path: path.read_text(encoding="utf-8") for path in staged_files}
        try:
            for path, text in staged_files.items():
                _atomic_write(path, text)
        except Exception:
            for path, text in committed_originals.items():
                _atomic_write(path, text)
            raise
    return {
        "validated": True,
        "dry_run": dry_run,
        "actions": len(actions),
        "added_ids": added_ids,
        "parent_assets": parent_count,
        "variant_assets": variant_count,
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
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    try:
        if args.command == "validate":
            parents, variants, _ = catalog.load_catalog(
                args.skill_root / "academic-writing-corpus",
                args.skill_root / "academic-writing-corpus" / "_evidence_registry.yaml",
            )
            print(
                yaml.safe_dump(
                    {"valid": True, "parent_assets": len(parents), "variant_assets": len(variants)},
                    sort_keys=False,
                ).strip()
            )
            return 0
        print(yaml.safe_dump(apply_plan(args.skill_root, args.plan, args.dry_run), sort_keys=False).strip())
        return 0
    except (OSError, GovernanceError, ValueError) as error:
        print(f"Governance error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
