#!/usr/bin/env python3
"""Index and retrieve governed write-introduction assets.

Markdown remains the canonical source text. The evidence registry governs
roles and lifecycles; index files are deliberately excluded from inventory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = SKILL_ROOT / "academic-writing-corpus"
REGISTRY_PATH = CORPUS_DIR / "_evidence_registry.yaml"
VARIANT_HEADING = re.compile(
    r"^#{2,4}\s+(?:变体|Variant)\s+([^：:\n]+?)(?:\s*[：:]\s*(.+))?$",
    re.MULTILINE | re.IGNORECASE,
)
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
KNOWN_MODULES = {
    "hooks": "hooks",
    "tensions": "tensions",
    "stakes": "stakes",
    "literature-turns": "literature_turns",
    "previews": "previews",
    "contributions": "contributions",
    "research-questions": "research_questions",
    "theory-lens": "theory_lens",
    "transitions": "transitions",
    "differentiation": "differentiation",
}
VALID_LIFECYCLES = {"active", "merged", "deprecated"}
VALID_PARENT_ROLES = {"generative_strategy", "reference_strategy"}
VALID_VARIANT_ROLES = {"generative_variant", "reference_exemplar"}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently overwriting them."""


def _construct_unique_mapping(
    loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False
) -> dict:
    mapping: dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"Duplicate YAML key in evidence registry: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


@dataclass(frozen=True)
class ParentAsset:
    asset_id: str
    module: str
    canonical_id: str
    role: str
    evidence_status: str
    lifecycle: str
    merged_into: str | None
    legacy_ids: tuple[str, ...]
    source_file: str
    variant_count: int
    validation_total: int
    validation_rejects: int
    common_revise_reasons: tuple[str, ...]
    health: str


@dataclass(frozen=True)
class VariantAsset:
    asset_id: str
    parent_id: str
    token: str
    title: str
    role: str
    lifecycle: str
    merged_into: str | None
    legacy_ids: tuple[str, ...]
    evidence_additions: tuple[str, ...]
    source_file: str
    start: int
    end: int
    validation_total: int
    validation_rejects: int
    common_revise_reasons: tuple[str, ...]
    health: str


def _front_matter(text: str) -> dict:
    match = FRONT_MATTER.search(text)
    if not match:
        return {}
    # Several legacy files contain descriptive front-matter values that are not
    # strict YAML. The catalog only needs canonical_id, so parse that stable
    # scalar without making unrelated prose block inventory construction.
    canonical = re.search(
        r'(?m)^canonical_id:\s*["\']?([^"\'\r\n]+?)["\']?\s*$', match.group(1)
    )
    return {"canonical_id": canonical.group(1).strip()} if canonical else {}


def _variant_token(raw: str) -> str:
    token = re.sub(r"\s+", "-", raw.strip())
    if not token or not re.fullmatch(r"[\w-]+", token):
        raise ValueError(f"Unsupported variant token: {raw!r}")
    return token


def discover_assets(
    corpus_dir: Path = CORPUS_DIR,
) -> tuple[list[dict], list[dict], dict[str, str]]:
    """Discover parents and variants without consulting governance state."""
    parents: list[dict] = []
    variants: list[dict] = []
    texts: dict[str, str] = {}
    for path in sorted(corpus_dir.rglob("*.md")):
        if path.name == "_index.md":
            continue
        text = path.read_text(encoding="utf-8")
        matches = list(VARIANT_HEADING.finditer(text))
        if not matches:
            continue
        relative = path.relative_to(corpus_dir).as_posix()
        module = relative.split("/", 1)[0]
        if module not in KNOWN_MODULES:
            continue
        metadata = _front_matter(text)
        canonical_id = str(metadata.get("canonical_id") or path.stem)
        parent_id = f"{module}:{canonical_id}"
        parents.append(
            {
                "asset_id": parent_id,
                "module": module,
                "canonical_id": canonical_id,
                "source_file": relative,
                "variant_count": len(matches),
            }
        )
        texts[relative] = text
        occurrences: Counter[str] = Counter()
        for index, match in enumerate(matches):
            token = _variant_token(match.group(1))
            occurrences[token.casefold()] += 1
            occurrence = occurrences[token.casefold()]
            unique_token = token if occurrence == 1 else f"{token}~{occurrence}"
            title = (match.group(2) or token).strip()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            variants.append(
                {
                    "asset_id": f"{parent_id}:v{unique_token}",
                    "parent_id": parent_id,
                    "token": unique_token,
                    "title": title,
                    "source_file": relative,
                    "start": match.start(),
                    "end": end,
                }
            )
    parent_ids = [item["asset_id"] for item in parents]
    variant_ids = [item["asset_id"] for item in variants]
    if len(parent_ids) != len(set(parent_ids)):
        raise ValueError("Duplicate parent asset IDs detected")
    if len(variant_ids) != len(set(variant_ids)):
        raise ValueError("Duplicate variant asset IDs detected")
    return parents, variants, texts


def inventory_fingerprint(variant_ids: list[str]) -> str:
    payload = "\n".join(sorted(variant_ids)).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _load_registry(registry_path: Path = REGISTRY_PATH) -> dict:
    data = yaml.load(registry_path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    if not isinstance(data, dict) or not isinstance(data.get("evidence"), dict):
        raise ValueError("Evidence registry must contain an evidence mapping")
    governance = data.get("asset_governance")
    if governance is None:
        # 兼容 2026-08 新版 registry：asset_governance 段已随脚本化治理裁撤。
        # 治理副本（_governance/）按旧版默认值合成该段：全部资产视为 active 默认角色，
        # 无 overrides/menus/snapshot；快照一致性检查由调用方按标记跳过。
        data["asset_governance"] = {
            "schema_version": 1,
            "default_parent_record": {"role": "reference_strategy", "lifecycle": "active"},
            "default_variant_record": {"role": "reference_exemplar", "lifecycle": "active"},
            "snapshot": {},
            "parent_overrides": {},
            "variant_overrides": {},
            "representative_reference_menus": {},
        }
        data["_governance_synthesized"] = True
        return data
    if not isinstance(governance, dict) or governance.get("schema_version") != 1:
        raise ValueError("Evidence registry must contain asset_governance schema version 1")
    for key in (
        "default_parent_record",
        "default_variant_record",
        "snapshot",
        "parent_overrides",
        "variant_overrides",
        "representative_reference_menus",
    ):
        if not isinstance(governance.get(key), dict):
            raise ValueError(f"asset_governance requires a {key} mapping")
    parent_default = governance["default_parent_record"]
    variant_default = governance["default_variant_record"]
    if parent_default.get("role") != "reference_strategy" or parent_default.get("lifecycle") != "active":
        raise ValueError("Invalid default parent governance record")
    if variant_default.get("role") != "reference_exemplar" or variant_default.get("lifecycle") != "active":
        raise ValueError("Invalid default variant governance record")
    return data


def _effective_record(governance: dict, kind: str, asset_id: str) -> dict:
    default_key = f"default_{kind}_record"
    override_key = f"{kind}_overrides"
    record = dict(governance[default_key])
    record.update(governance[override_key].get(asset_id, {}))
    record.setdefault("merged_into", None)
    record.setdefault("legacy_ids", [])
    record.setdefault("evidence_additions", [])
    return record


def _validation_summary(record: dict) -> tuple[int, int, tuple[str, ...], str]:
    """Expose governed use feedback without changing asset eligibility."""
    history = record.get("validation_history_additions", [])
    if not isinstance(history, list):
        raise ValueError("validation_history_additions must be a list")
    rows = [row for row in history if isinstance(row, dict)]
    total = len(rows)
    rejects = sum(row.get("verdict") == "REJECT" for row in rows)
    reasons = tuple(
        dict.fromkeys(
            str(row.get("reason") or "").strip()
            for row in rows
            if row.get("verdict") in {"REVISE", "REJECT"} and str(row.get("reason") or "").strip()
        )
    )
    health = "CAUTION" if total >= 2 and rejects / total >= 0.5 else (
        "HEALTHY" if total >= 2 else "INSUFFICIENT_DATA"
    )
    return total, rejects, reasons, health


def _legacy_parent_evidence(registry: dict, module: str, canonical_id: str) -> dict:
    category = KNOWN_MODULES[module]
    entry = registry["evidence"].get(category, {}).get(canonical_id)
    return entry if isinstance(entry, dict) else {}


def _validate_record(kind: str, asset_id: str, record: dict) -> None:
    roles = VALID_PARENT_ROLES if kind == "parent" else VALID_VARIANT_ROLES
    if record.get("role") not in roles:
        raise ValueError(f"Invalid {kind} role for {asset_id}: {record.get('role')}")
    if record.get("lifecycle") not in VALID_LIFECYCLES:
        raise ValueError(f"Invalid lifecycle for {asset_id}: {record.get('lifecycle')}")
    if record["lifecycle"] == "merged" and not record.get("merged_into"):
        raise ValueError(f"Merged asset lacks target: {asset_id}")
    if record["lifecycle"] != "active" and record["role"] not in {
        "reference_strategy",
        "reference_exemplar",
    }:
        raise ValueError(f"Inactive asset cannot remain generative: {asset_id}")
    if record["role"] in {"generative_strategy", "generative_variant"}:
        status = record.get("evidence_status")
        paper_count = record.get("paper_count")
        basis = record.get("verification_basis")
        if status not in {"VERIFIED", "ROBUST"} or not isinstance(paper_count, int) or not basis:
            raise ValueError(f"Incomplete promotion evidence for {asset_id}")
        if paper_count < 3 and basis != "user_expert_audit":
            raise ValueError(f"Generative asset lacks verified evidence: {asset_id}")


def _validate_routing(corpus_dir: Path, parents: list[ParentAsset]) -> None:
    routing_path = corpus_dir / "_routing_tables.yaml"
    routing = yaml.load(routing_path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    known: dict[str, set[str]] = {}
    active: set[str] = set()
    for item in parents:
        known.setdefault(item.module, set()).add(item.canonical_id)
        if item.lifecycle == "active":
            active.add(item.asset_id)
    references: list[tuple[str, str]] = []
    for rows in routing["hooks"]["by_gap_strength"].values():
        references.extend(("hooks", row["canonical_id"]) for row in rows)
    for row in routing["hooks"]["contribution_micro"].values():
        references.extend(("hooks", value) for value in row.get("preferred", []))
    for rows in routing["tensions"].values():
        references.extend(("tensions", row["canonical_id"]) for row in rows)
    references.extend(("stakes", row["stakes"]) for row in routing["stakes"]["selection"])
    for rows in routing["transitions"].values():
        references.extend(("transitions", row["canonical_id"]) for row in rows)
    for row in routing["pairing_constraints"]["mandatory"]:
        references.append(("hooks", row["hook"]))
        references.extend(
            ("tensions", value)
            for value in re.findall(r"\b\d{2}-[a-z0-9-]+", row["tension"])
        )
    missing = sorted({
        f"{module}:{canonical_id}"
        for module, canonical_id in references
        if canonical_id not in known.get(module, set())
        or f"{module}:{canonical_id}" not in active
    })
    if missing:
        raise ValueError("Routing references unknown or inactive parents: " + ", ".join(missing))


def load_catalog(
    corpus_dir: Path = CORPUS_DIR,
    registry_path: Path = REGISTRY_PATH,
) -> tuple[list[ParentAsset], list[VariantAsset], dict[str, str]]:
    discovered_parents, discovered_variants, texts = discover_assets(corpus_dir)
    registry = _load_registry(registry_path)
    governance = registry["asset_governance"]
    parent_ids = {item["asset_id"] for item in discovered_parents}
    variant_ids = {item["asset_id"] for item in discovered_variants}

    unknown_parents = sorted(set(governance["parent_overrides"]) - parent_ids)
    unknown_variants = sorted(set(governance["variant_overrides"]) - variant_ids)
    if unknown_parents or unknown_variants:
        raise ValueError(
            "Governance overrides reference unknown assets: "
            + ", ".join(unknown_parents + unknown_variants)
        )

    parents: list[ParentAsset] = []
    for item in discovered_parents:
        legacy = _legacy_parent_evidence(registry, item["module"], item["canonical_id"])
        record = dict(governance["default_parent_record"])
        if legacy.get("status"):
            record.update(
                evidence_status=legacy["status"],
                paper_count=legacy.get("paper_count"),
                verification_basis="legacy_registry_migration",
            )
            if legacy["status"] in {"VERIFIED", "ROBUST"}:
                record["role"] = "generative_strategy"
        record.update(governance["parent_overrides"].get(item["asset_id"], {}))
        record.setdefault("merged_into", None)
        record.setdefault("legacy_ids", [])
        record.setdefault("evidence_additions", [])
        _validate_record("parent", item["asset_id"], record)
        validation_total, validation_rejects, reasons, health = _validation_summary(record)
        parents.append(
            ParentAsset(
                **item,
                role=record["role"],
                evidence_status=str(record.get("evidence_status") or legacy.get("status") or "UNREGISTERED"),
                lifecycle=record["lifecycle"],
                merged_into=record["merged_into"],
                legacy_ids=tuple(record["legacy_ids"]),
                validation_total=validation_total,
                validation_rejects=validation_rejects,
                common_revise_reasons=reasons,
                health=health,
            )
        )

    variants: list[VariantAsset] = []
    for item in discovered_variants:
        record = _effective_record(governance, "variant", item["asset_id"])
        _validate_record("variant", item["asset_id"], record)
        validation_total, validation_rejects, reasons, health = _validation_summary(record)
        variants.append(
            VariantAsset(
                **item,
                role=record["role"],
                lifecycle=record["lifecycle"],
                merged_into=record["merged_into"],
                legacy_ids=tuple(record["legacy_ids"]),
                evidence_additions=tuple(record["evidence_additions"]),
                validation_total=validation_total,
                validation_rejects=validation_rejects,
                common_revise_reasons=reasons,
                health=health,
            )
        )

    all_assets = {item.asset_id: item for item in [*parents, *variants]}
    legacy_ids: Counter[str] = Counter()
    canonical_folded = {key.casefold() for key in all_assets}
    for item in all_assets.values():
        for legacy_id in item.legacy_ids:
            legacy_ids[legacy_id.casefold()] += 1
            if legacy_id.casefold() in canonical_folded:
                raise ValueError(f"Legacy ID collides with canonical ID: {legacy_id}")
    duplicates = [key for key, count in legacy_ids.items() if count > 1]
    if duplicates:
        raise ValueError("Duplicate legacy asset IDs: " + ", ".join(sorted(duplicates)))
    for item in all_assets.values():
        if item.lifecycle == "merged":
            target = all_assets.get(item.merged_into or "")
            if target is None or target.lifecycle != "active" or target.asset_id == item.asset_id:
                raise ValueError(f"Invalid merge target for {item.asset_id}: {item.merged_into}")

    snapshot = governance["snapshot"]
    fingerprint = inventory_fingerprint([item.asset_id for item in variants])
    expected = {
        "total_parent_assets": len(parents),
        "total_variant_assets": len(variants),
        "inventory_sha256": fingerprint,
    }
    # 合成的 governance（新版 registry 无 asset_governance 段）没有可信快照，跳过一致性检查
    if registry.get("_governance_synthesized"):
        mismatches = []
    else:
        mismatches = [key for key, value in expected.items() if snapshot.get(key) != value]
    if mismatches:
        raise ValueError("Asset governance snapshot mismatch: " + ", ".join(mismatches))

    cap = int(governance.get("active_variant_cap_per_parent", 5))
    generative_counts = Counter(
        item.parent_id
        for item in variants
        if item.lifecycle == "active" and item.role == "generative_variant"
    )
    over_cap = [parent for parent, count in generative_counts.items() if count > cap]
    if over_cap:
        raise ValueError("Generative variant cap exceeded: " + ", ".join(sorted(over_cap)))

    variant_by_id = {item.asset_id: item for item in variants}
    for parent_id, menu in governance["representative_reference_menus"].items():
        if parent_id not in parent_ids or not isinstance(menu, list) or len(menu) > cap:
            raise ValueError(f"Invalid representative menu for {parent_id}")
        if len(menu) != len(set(menu)):
            raise ValueError(f"Duplicate representative menu entries for {parent_id}")
        for asset_id in menu:
            item = variant_by_id.get(asset_id)
            if item is None or item.parent_id != parent_id or item.lifecycle != "active":
                raise ValueError(f"Invalid representative reference {asset_id} for {parent_id}")
    _validate_routing(corpus_dir, parents)
    return parents, variants, texts


def _resolve_assets(
    parents: list[ParentAsset], variants: list[VariantAsset], requested_ids: list[str]
) -> tuple[list[ParentAsset | VariantAsset], list[str | None]]:
    assets = [*parents, *variants]
    by_id = {item.asset_id.casefold(): item for item in assets}
    legacy = {alias.casefold(): item for item in assets for alias in item.legacy_ids}
    resolved: list[ParentAsset | VariantAsset] = []
    notices: list[str | None] = []
    for requested in requested_ids:
        item = by_id.get(requested.casefold()) or legacy.get(requested.casefold())
        if item is None:
            raise ValueError(f"Unknown asset ID: {requested}")
        notice = None if requested.casefold() == item.asset_id.casefold() else f"{requested} -> {item.asset_id}"
        if item.lifecycle == "merged":
            target = by_id[item.merged_into.casefold()]
            notice = f"{item.asset_id} -> {target.asset_id}"
            item = target
        resolved.append(item)
        notices.append(notice)
    duplicate_targets = [key for key, count in Counter(item.asset_id for item in resolved).items() if count > 1]
    if duplicate_targets:
        raise ValueError("Requested IDs resolve to duplicate assets: " + ", ".join(duplicate_targets))
    return resolved, notices


def command_list_parents(args: argparse.Namespace) -> int:
    parents, _, _ = load_catalog()
    known_modules = {item.module.casefold() for item in parents}
    if args.module and args.module.casefold() not in known_modules:
        raise ValueError(f"Unknown Introduction module: {args.module}")
    selected = [item for item in parents if item.lifecycle == "active"]
    if args.module:
        selected = [item for item in selected if item.module.casefold() == args.module.casefold()]
    if not args.include_reference:
        selected = [item for item in selected if item.role == "generative_strategy"]
    for item in selected:
        health = ""
        if item.health == "CAUTION":
            health = f"\thealth=CAUTION\treasons={' | '.join(item.common_revise_reasons)}"
        print(
            f"{item.asset_id}\t{item.role}\t{item.evidence_status}\t"
            f"variants={item.variant_count}\t{item.source_file}{health}"
        )
    return 0


def command_list_variants(args: argparse.Namespace) -> int:
    parents, variants, _ = load_catalog()
    if args.parent not in {item.asset_id for item in parents}:
        raise ValueError(f"Unknown parent asset: {args.parent}")
    registry = _load_registry()
    menu = registry["asset_governance"]["representative_reference_menus"].get(args.parent, [])
    selected = [item for item in variants if item.parent_id == args.parent and item.lifecycle == "active"]
    if not args.include_all:
        selected = [item for item in selected if item.role == "generative_variant" or item.asset_id in menu]
    for item in selected:
        marker = "representative" if item.asset_id in menu else item.role
        health = "" if item.health != "CAUTION" else f"\thealth=CAUTION\treasons={' | '.join(item.common_revise_reasons)}"
        print(f"{item.asset_id}\t{marker}\t{item.title}{health}")
    return 0


def command_render(args: argparse.Namespace) -> int:
    parents, variants, texts = load_catalog()
    requested, notices = _resolve_assets(parents, variants, args.id)
    max_render = int(_load_registry()["asset_governance"].get("render_cap", 4))
    if len(requested) > max_render and not args.allow_many:
        raise ValueError(f"At most {max_render} exact assets may be rendered per call")
    if any(isinstance(item, VariantAsset) and item.role == "reference_exemplar" for item in requested):
        if not args.allow_reference:
            raise ValueError("Reference exemplars require --allow-reference")
    for index, item in enumerate(requested):
        if index:
            print("\n---\n")
        print(f"<!-- asset_id: {item.asset_id}; lifecycle: {item.lifecycle} -->")
        if item.health == "CAUTION":
            print(
                "<!-- governance_health: CAUTION; "
                f"validation_rejects={item.validation_rejects}/{item.validation_total}; "
                f"reasons={' | '.join(item.common_revise_reasons)} -->"
            )
        if notices[index]:
            print(f"<!-- lifecycle_notice: {notices[index]} -->")
        if isinstance(item, ParentAsset):
            first_variant = min(
                (variant.start for variant in variants if variant.parent_id == item.asset_id),
                default=len(texts[item.source_file]),
            )
            print(texts[item.source_file][:first_variant].rstrip())
        else:
            print(texts[item.source_file][item.start:item.end].rstrip())
    return 0


def command_audit(args: argparse.Namespace) -> int:
    parents, variants, _ = load_catalog()
    registry = _load_registry()
    menus = registry["asset_governance"]["representative_reference_menus"]
    payload = {
        "asset_record_coverage": f"{len(parents) + len(variants)}/{len(parents) + len(variants)}",
        "parent_assets": len(parents),
        "variant_assets": len(variants),
        "parent_roles": dict(sorted(Counter(item.role for item in parents).items())),
        "variant_roles": dict(sorted(Counter(item.role for item in variants).items())),
        "lifecycles": dict(sorted(Counter(item.lifecycle for item in [*parents, *variants]).items())),
        "unregistered_parents": [item.asset_id for item in parents if item.evidence_status == "UNREGISTERED"],
        "representative_menu_sizes": {key: len(value) for key, value in menus.items()},
        "largest_variant_families": [
            {"parent_id": item.asset_id, "variants": item.variant_count}
            for item in sorted(parents, key=lambda row: row.variant_count, reverse=True)[:10]
        ],
        "validation_health": {
            "caution_assets": [
                {
                    "asset_id": item.asset_id,
                    "validation_rejects": item.validation_rejects,
                    "validation_total": item.validation_total,
                    "common_revise_reasons": list(item.common_revise_reasons),
                }
                for item in [*parents, *variants]
                if item.health == "CAUTION"
            ]
        },
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(yaml.safe_dump(payload, allow_unicode=True, sort_keys=False).strip())
    return 0


def command_dump(args: argparse.Namespace) -> int:
    parents, variants, _ = load_catalog()
    print(
        json.dumps(
            {"parents": [asdict(item) for item in parents], "variants": [asdict(item) for item in variants]},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    parents = subparsers.add_parser("list-parents")
    parents.add_argument("--module")
    parents.add_argument("--include-reference", action="store_true")
    parents.set_defaults(func=command_list_parents)
    variants = subparsers.add_parser("list-variants")
    variants.add_argument("--parent", required=True)
    variants.add_argument("--include-all", action="store_true")
    variants.set_defaults(func=command_list_variants)
    render = subparsers.add_parser("render")
    render.add_argument("--id", action="append", required=True)
    render.add_argument("--allow-reference", action="store_true")
    render.add_argument("--allow-many", action="store_true")
    render.set_defaults(func=command_render)
    audit = subparsers.add_parser("audit")
    audit.add_argument("--json", action="store_true")
    audit.set_defaults(func=command_audit)
    dump = subparsers.add_parser("dump-index")
    dump.set_defaults(func=command_dump)
    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError) as error:
        print(f"Catalog error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
