#!/usr/bin/env python3
"""Index and retrieve write-results variants without loading whole corpus files.

The Markdown corpus remains canonical. This script builds a live, read-only index,
assigns evidence-aware menu roles, and renders exact source blocks by stable ID.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


CORPUS_DIR = Path(__file__).resolve().parents[1] / "corpus"
REGISTRY_PATH = CORPUS_DIR / "_evidence_registry.yaml"
STANDARD_HEADING = re.compile(
    r"^###\s+变体\s*(\d+)\s*[:：]\s*(.+?)\s*$", re.MULTILINE
)
EMPTY_TEMPLATE = re.compile(r"^###\s+变体\s*N\s*[:：]", re.MULTILINE)
SLOT_TOKEN = re.compile(r"(?<![A-Za-z0-9])([RF])\s*([1-9])(?!\d)", re.I)
RESULT_TYPE_ALIASES = {
    "ols/fe": "OLS-FE",
    "ols-fe": "OLS-FE",
    "ols": "OLS-FE",
    "fixed effects": "OLS-FE",
    "fixed-effects": "OLS-FE",
    "fixed effects regression": "OLS-FE",
    "logit/probit/ordered probit": "Logit-Probit-Ordered-Probit",
    "logit-probit-ordered-probit": "Logit-Probit-Ordered-Probit",
    "logit": "Logit-Probit-Ordered-Probit",
    "probit": "Logit-Probit-Ordered-Probit",
    "ordered probit": "Logit-Probit-Ordered-Probit",
    "iv/2sls": "IV-2SLS",
    "iv-2sls": "IV-2SLS",
    "2sls": "IV-2SLS",
    "instrumental variables": "IV-2SLS",
    "cox": "生存分析",
    "cox proportional hazard": "生存分析",
    "cox proportional hazards": "生存分析",
    "cox ph": "生存分析",
    "aft": "生存分析",
    "accelerated failure time": "生存分析",
    "hazard model": "生存分析",
    "survival analysis": "生存分析",
    "negative binomial": "计数模型",
    "negative binomial regression": "计数模型",
    "poisson": "计数模型",
    "poisson regression": "计数模型",
    "count model": "计数模型",
    "difference-in-differences": "DiD",
    "difference in differences": "DiD",
    "自然实验/did": "DiD",
    "同伴效应/网络效应": "同伴效应-网络效应",
    "定性过程研究/定性发现": "定性过程研究",
    "定性发现": "定性过程研究",
    "sem/调节中介": "SEM-moderated-mediation",
    "事件研究": "事件研究法",
    "blp+kalman/gmm": "BLP-状态空间",
}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys before they can silently overwrite evidence."""


def _construct_unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
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

# This legacy file predates the numbered variant convention. Keeping the small
# compatibility map here avoids rewriting or duplicating its source text.
SEM_SECTIONS = [
    (
        1,
        "SEM Moderated Mediation 基础报告模式",
        "# SEM Moderated Mediation 报告模式",
        "## 比较两条方向相反通道的持续性",
        ("R3", "R4"),
    ),
    (
        2,
        "Reverse-Code + Wald Test：比较对立通道持续性",
        "## 比较两条方向相反通道的持续性",
        "## 不一致中介",
        ("R4",),
    ),
    (
        3,
        "不一致中介 → 抑制变量报告",
        "## 不一致中介",
        "## 联立方程 SEM",
        ("R3", "R8"),
    ),
    (
        4,
        "联立方程 SEM 结果报告 + IV 诊断前置",
        "## 联立方程 SEM",
        "## 反转中介顺序",
        ("R2", "R3", "R7"),
    ),
    (
        5,
        "反转中介顺序的竞争排序敏感性检查",
        "## 反转中介顺序",
        "## 事件条件间接效应",
        ("R8",),
    ),
    (
        6,
        "事件条件间接效应：直接交互不一致时的分层报告",
        "## 事件条件间接效应",
        "## 共享中介跨异质结果分支",
        ("R4", "R8"),
    ),
    (
        7,
        "共享中介跨异质结果分支的证据账本",
        "## 共享中介跨异质结果分支",
        None,
        ("R3", "R8"),
    ),
]


@dataclass(frozen=True)
class Variant:
    asset_id: str
    result_type: str
    number: int
    title: str
    slots: tuple[str, ...]
    role: str
    evidence: str
    paper_count: int | None
    promotion_basis: str | None
    registry_status: str | None
    lifecycle: str
    merged_into: str | None
    legacy_ids: tuple[str, ...]
    evidence_additions: tuple[str, ...]
    source_file: str
    start: int
    end: int


def _field(block: str, label: str) -> str | None:
    match = re.search(rf"\*\*{re.escape(label)}\*\*\s*[:：]\s*([^\n]+)", block, re.I)
    return match.group(1).strip() if match else None


def _slots(block: str, title: str) -> tuple[str, ...]:
    explicit = _field(block, "槽位")
    scan = explicit if explicit else title
    found: list[str] = []
    for match in SLOT_TOKEN.finditer(scan):
        slot = f"{match.group(1).upper()}{match.group(2)}"
        if slot not in found:
            found.append(slot)
    return tuple(found)


def _evidence(block: str, title: str) -> str:
    status = _field(block, "验证状态") or _field(block, "状态")
    if status:
        return status
    ratio = re.search(r"\((\d+)\s*/\s*(\d+)\s*复现\)", title)
    if ratio:
        return f"{ratio.group(1)}/{ratio.group(2)} 复现"
    if "1篇" in title or "单篇" in block[:700]:
        return "单篇来源"
    return "未结构化标注"


def _load_registry(registry_path: Path = REGISTRY_PATH) -> dict:
    data = yaml.load(registry_path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    if not isinstance(data, dict) or not isinstance(data.get("meta"), dict):
        raise ValueError("Evidence registry must contain a meta mapping")
    if data["meta"].get("canonical_promotion_source") != "asset_governance.overrides":
        raise ValueError("Evidence registry does not declare asset_governance.overrides as canonical")
    governance = data.get("asset_governance")
    if not isinstance(governance, dict) or governance.get("schema_version") != 1:
        raise ValueError("Evidence registry must contain asset_governance schema version 1")
    defaults = governance.get("default_record")
    inventory = governance.get("inventory")
    overrides = governance.get("overrides")
    if not isinstance(defaults, dict) or not isinstance(inventory, dict) or not isinstance(overrides, dict):
        raise ValueError("asset_governance requires default_record, inventory, and overrides mappings")
    if defaults.get("role") != "reference_exemplar" or defaults.get("lifecycle") != "active":
        raise ValueError("asset_governance defaults must be active reference exemplars")
    valid_lifecycles = {"active", "merged", "deprecated"}
    for asset_id, record in overrides.items():
        if not isinstance(record, dict):
            raise ValueError(f"Invalid asset governance record for {asset_id}")
        lifecycle = record.get("lifecycle", defaults["lifecycle"])
        role = record.get("role", defaults["role"])
        if lifecycle not in valid_lifecycles:
            raise ValueError(f"Invalid lifecycle for {asset_id}: {lifecycle}")
        if role not in {"core_operator", "optional_operator", "reference_exemplar"}:
            raise ValueError(f"Invalid asset role for {asset_id}: {role}")
        if lifecycle == "merged" and not record.get("merged_into"):
            raise ValueError(f"Merged asset lacks merged_into target: {asset_id}")
        if lifecycle != "active" and role != "reference_exemplar":
            raise ValueError(f"Inactive asset cannot remain promoted: {asset_id}")
        if role == "reference_exemplar":
            continue
        status = record.get("status")
        paper_count = record.get("paper_count")
        basis = record.get("verification_basis")
        if status not in {"VERIFIED", "ROBUST"}:
            raise ValueError(f"Invalid promotion status for {asset_id}")
        if not isinstance(paper_count, int) or paper_count < 1 or not basis:
            raise ValueError(f"Incomplete promotion evidence for {asset_id}")
        expert_override = basis == "user_expert_audit"
        if role == "optional_operator" and paper_count < 3 and not expert_override:
            raise ValueError(f"Optional operator lacks verified evidence: {asset_id}")
        if role == "core_operator":
            if status != "ROBUST" or paper_count < 5 or record.get("cross_subfields", 0) < 2:
                raise ValueError(f"Core operator lacks robust cross-subfield evidence: {asset_id}")
            if record.get("behavior_validation") != "passed":
                raise ValueError(f"Core operator lacks behavioral validation: {asset_id}")
    semantic_ids: list[str] = []

    def collect_ids(value: object) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("id"), str):
                semantic_ids.append(value["id"])
            for child in value.values():
                collect_ids(child)
        elif isinstance(value, list):
            for child in value:
                collect_ids(child)

    collect_ids(data)
    duplicates = sorted(asset_id for asset_id, count in Counter(semantic_ids).items() if count > 1)
    if duplicates:
        raise ValueError(f"Duplicate semantic IDs in evidence registry: {', '.join(duplicates)}")
    return data


def _asset_record(asset_id: str, registry: dict) -> dict:
    governance = registry["asset_governance"]
    record = dict(governance["default_record"])
    record.update(governance["overrides"].get(asset_id, {}))
    record.setdefault("merged_into", None)
    record.setdefault("legacy_ids", [])
    record.setdefault("evidence_additions", [])
    return record


def _canonical_result_type(value: str, known_types: dict[str, str]) -> str | None:
    folded = value.casefold().strip()
    if folded in known_types:
        return known_types[folded]
    alias = RESULT_TYPE_ALIASES.get(folded)
    if alias and alias.casefold() in known_types:
        return known_types[alias.casefold()]
    return None


def _canonical_slot(value: str) -> str | None:
    upper = value.upper().strip()
    return upper if re.fullmatch(r"[RF][1-9]", upper) else None


def _standard_variants(path: Path, text: str, registry: dict) -> list[Variant]:
    matches = list(STANDARD_HEADING.finditer(text))
    variants: list[Variant] = []
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[start:end]
        number = int(match.group(1))
        title = match.group(2).strip()
        evidence = _evidence(block, title)
        asset_id = f"{path.stem}:v{number}"
        governance = _asset_record(asset_id, registry)
        variants.append(
            Variant(
                asset_id=asset_id,
                result_type=path.stem,
                number=number,
                title=title,
                slots=_slots(block, title),
                role=governance["role"],
                evidence=evidence,
                paper_count=governance.get("paper_count"),
                promotion_basis=governance.get("verification_basis"),
                registry_status=governance.get("status"),
                lifecycle=governance["lifecycle"],
                merged_into=governance["merged_into"],
                legacy_ids=tuple(governance["legacy_ids"]),
                evidence_additions=tuple(governance["evidence_additions"]),
                source_file=path.name,
                start=start,
                end=end,
            )
        )
    return variants


def _sem_variants(path: Path, text: str, registry: dict) -> list[Variant]:
    variants: list[Variant] = []
    for number, title, start_marker, end_marker, slots in SEM_SECTIONS:
        start = text.find(start_marker)
        if start < 0:
            raise ValueError(f"Missing SEM marker: {start_marker}")
        end = text.find(end_marker, start + len(start_marker)) if end_marker else len(text)
        if end_marker and end < 0:
            raise ValueError(f"Missing SEM marker: {end_marker}")
        block = text[start:end]
        evidence = _evidence(block, title)
        asset_id = f"{path.stem}:v{number}"
        governance = _asset_record(asset_id, registry)
        variants.append(
            Variant(
                asset_id=asset_id,
                result_type=path.stem,
                number=number,
                title=title,
                slots=slots,
                role=governance["role"],
                evidence=evidence,
                paper_count=governance.get("paper_count"),
                promotion_basis=governance.get("verification_basis"),
                registry_status=governance.get("status"),
                lifecycle=governance["lifecycle"],
                merged_into=governance["merged_into"],
                legacy_ids=tuple(governance["legacy_ids"]),
                evidence_additions=tuple(governance["evidence_additions"]),
                source_file=path.name,
                start=start,
                end=end,
            )
        )
    return variants


def load_catalog(
    corpus_dir: Path = CORPUS_DIR, registry_path: Path = REGISTRY_PATH
) -> tuple[list[Variant], dict[str, str]]:
    registry = _load_registry(registry_path)
    variants: list[Variant] = []
    texts: dict[str, str] = {}
    for path in sorted(corpus_dir.glob("*.md")):
        if path.name == "INDEX.md":
            continue
        text = path.read_text(encoding="utf-8")
        texts[path.name] = text
        if path.name == "SEM-moderated-mediation.md":
            variants.extend(_sem_variants(path, text, registry))
        else:
            variants.extend(_standard_variants(path, text, registry))
    ids = [variant.asset_id for variant in variants]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate asset IDs detected")
    governance = registry["asset_governance"]
    missing_assets = sorted(set(governance["overrides"]) - set(ids))
    if missing_assets:
        raise ValueError(f"Registry contains unknown asset IDs: {', '.join(missing_assets)}")
    duplicate_legacy = [
        legacy_id
        for legacy_id, count in Counter(
            legacy_id.casefold() for item in variants for legacy_id in item.legacy_ids
        ).items()
        if count > 1
    ]
    collisions = sorted(
        legacy_id for item in variants for legacy_id in item.legacy_ids if legacy_id.casefold() in {x.casefold() for x in ids}
    )
    if duplicate_legacy or collisions:
        raise ValueError("Duplicate or colliding legacy asset IDs detected")
    by_id = {item.asset_id: item for item in variants}
    for item in variants:
        if item.lifecycle == "merged":
            target = by_id.get(item.merged_into or "")
            if target is None or target.lifecycle != "active" or target.asset_id == item.asset_id:
                raise ValueError(f"Invalid merge target for {item.asset_id}: {item.merged_into}")
    _validate_registry_snapshot(registry, variants, texts)
    return variants, texts


def _validate_registry_snapshot(registry: dict, variants: list[Variant], texts: dict[str, str]) -> None:
    meta = registry["meta"]
    by_type = {Path(name).stem: 0 for name in texts}
    for item in variants:
        by_type[item.result_type] += 1
    filled = sum(count > 0 for count in by_type.values())
    empty = sorted(name for name, count in by_type.items() if count == 0)
    role_counts = {role: 0 for role in ("core_operator", "optional_operator", "reference_exemplar")}
    for item in variants:
        role_counts[item.role] += 1
    expected = {
        "total_result_types": len(texts),
        "filled_result_types": filled,
        "total_variants": len(variants),
        "empty_result_types": empty,
        "menu_roles": role_counts,
        "variants_by_result_type": dict(sorted(by_type.items())),
    }
    inventory = registry["asset_governance"]["inventory"]
    if inventory != dict(sorted(by_type.items())):
        mismatches = ["asset_governance.inventory"]
    else:
        mismatches = []
    mismatches.extend(key for key, value in expected.items() if meta.get(key) != value)
    if mismatches:
        raise ValueError("Evidence registry snapshot mismatch: " + ", ".join(mismatches))


def _select(
    variants: list[Variant], result_type: str | None, slot: str | None, include_reference: bool
) -> list[Variant]:
    selected = [item for item in variants if item.lifecycle == "active"]
    if result_type:
        selected = [item for item in selected if item.result_type.casefold() == result_type.casefold()]
    if slot:
        wanted = slot.upper()
        selected = [item for item in selected if wanted in item.slots]
    if not include_reference:
        selected = [item for item in selected if item.role != "reference_exemplar"]
    return selected


def command_list(args: argparse.Namespace) -> int:
    variants, texts = load_catalog()
    known_types = {Path(name).stem.casefold(): Path(name).stem for name in texts}
    canonical_type = None
    if args.result_type:
        canonical_type = _canonical_result_type(args.result_type, known_types)
    if args.result_type and canonical_type is None:
        print(f"Unknown result type: {args.result_type}", file=sys.stderr)
        return 2
    canonical_slot = _canonical_slot(args.slot) if args.slot else None
    if args.slot and canonical_slot is None:
        print(f"Invalid slot: {args.slot}; expected R1-R9 or F1-F9", file=sys.stderr)
        return 2
    selected = _select(variants, canonical_type, canonical_slot, args.include_reference)
    for item in selected:
        slots = ",".join(item.slots) if item.slots else "UNCLASSIFIED"
        promotion = (
            f"status={item.registry_status};papers={item.paper_count};basis={item.promotion_basis}"
            if item.paper_count
            else "unpromoted"
        )
        print(f"{item.asset_id}\t{slots}\t{item.role}\t{promotion}\t{item.evidence}\t{item.title}")
    if not selected:
        print(
            "No default-eligible variants matched. Re-run with --include-reference "
            "to inspect single-paper exemplars, or use the slot core only.",
            file=sys.stderr,
        )
        return 0
    return 0


def _resolve_requested_assets(
    variants: list[Variant], requested_ids: list[str]
) -> tuple[list[Variant], list[str | None]]:
    by_id = {item.asset_id.casefold(): item for item in variants}
    legacy_to_item = {
        legacy_id.casefold(): item for item in variants for legacy_id in item.legacy_ids
    }
    requested: list[Variant] = []
    notices: list[str | None] = []
    missing: list[str] = []
    for asset_id in requested_ids:
        item = by_id.get(asset_id.casefold()) or legacy_to_item.get(asset_id.casefold())
        if item is None:
            missing.append(asset_id)
            continue
        notice = (
            f"legacy asset ID {asset_id} resolves to {item.asset_id}"
            if asset_id.casefold() != item.asset_id.casefold()
            else None
        )
        if item.lifecycle == "merged":
            target = by_id[item.merged_into.casefold()]
            notice = f"merged asset {item.asset_id} resolves to {target.asset_id}"
            item = target
        requested.append(item)
        notices.append(notice)
    if missing:
        raise ValueError(f"Unknown asset ID(s): {', '.join(missing)}")
    resolved_ids = [item.asset_id.casefold() for item in requested]
    if len(resolved_ids) != len(set(resolved_ids)):
        raise ValueError("Requested IDs resolve to duplicate active assets")
    return requested, notices


def command_render(args: argparse.Namespace) -> int:
    variants, texts = load_catalog()
    folded_ids = [asset_id.casefold() for asset_id in args.id]
    if len(folded_ids) != len(set(folded_ids)):
        print("Duplicate asset IDs are not allowed.", file=sys.stderr)
        return 2
    try:
        requested, notices = _resolve_requested_assets(variants, args.id)
    except ValueError as error:
        print(str(error), file=sys.stderr)
        return 2
    if len(requested) > 4 and not args.allow_many:
        print("At most four variants may be rendered per call; use --allow-many for an explicit audit.", file=sys.stderr)
        return 2
    reference_count = sum(item.role == "reference_exemplar" for item in requested)
    if reference_count and not args.allow_reference:
        print(
            "Reference exemplars require --allow-reference; they are analogies, not default rules.",
            file=sys.stderr,
        )
        return 2
    if reference_count > 2 and not args.allow_many:
        print(
            "At most two reference exemplars may be rendered per call; reserve other slots for core/optional assets.",
            file=sys.stderr,
        )
        return 2
    for index, item in enumerate(requested):
        if index:
            print("\n---\n")
        print(f"<!-- asset_id: {item.asset_id} -->")
        if notices[index]:
            print(f"<!-- lifecycle_notice: {notices[index]} -->")
        print(
            f"<!-- menu_role: {item.role}; lifecycle: {item.lifecycle}; registry_status: {item.registry_status}; "
            f"papers: {item.paper_count}; promotion_basis: {item.promotion_basis}; "
            f"source_label: {item.evidence} -->"
        )
        print(texts[item.source_file][item.start:item.end].rstrip())
    return 0


def command_audit(args: argparse.Namespace) -> int:
    variants, texts = load_catalog()
    by_type: dict[str, int] = {}
    by_role: dict[str, int] = {}
    by_slot: dict[str, int] = {}
    by_lifecycle: dict[str, int] = {}
    for item in variants:
        by_type[item.result_type] = by_type.get(item.result_type, 0) + 1
        by_role[item.role] = by_role.get(item.role, 0) + 1
        by_lifecycle[item.lifecycle] = by_lifecycle.get(item.lifecycle, 0) + 1
        for slot in item.slots or ("UNCLASSIFIED",):
            by_slot[slot] = by_slot.get(slot, 0) + 1
    empty_templates = sorted(
        name for name, text in texts.items() if EMPTY_TEMPLATE.search(text) and not STANDARD_HEADING.search(text)
    )
    payload = {
        "promotion_authority": "_evidence_registry.yaml:asset_governance.overrides",
        "asset_record_coverage": f"{len(variants)}/{len(variants)}",
        "total_variants": len(variants),
        "result_types_with_variants": len(by_type),
        "by_result_type": dict(sorted(by_type.items())),
        "by_role": dict(sorted(by_role.items())),
        "by_lifecycle": dict(sorted(by_lifecycle.items())),
        "by_slot": dict(sorted(by_slot.items())),
        "unclassified_ids": [item.asset_id for item in variants if not item.slots],
        "promoted_ids": [item.asset_id for item in variants if item.role != "reference_exemplar"],
        "empty_template_files": empty_templates,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"variants={payload['total_variants']}")
        print(f"result_types_with_variants={payload['result_types_with_variants']}")
        print("roles=" + ", ".join(f"{key}:{value}" for key, value in by_role.items()))
        print("lifecycle=" + ", ".join(f"{key}:{value}" for key, value in by_lifecycle.items()))
        print("unclassified=" + ", ".join(payload["unclassified_ids"]))
        print("empty_templates=" + ", ".join(empty_templates))
    return 0


def command_dump(args: argparse.Namespace) -> int:
    variants, _ = load_catalog()
    print(json.dumps([asdict(item) for item in variants], ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List compact candidates")
    list_parser.add_argument("--result-type")
    list_parser.add_argument("--slot")
    list_parser.add_argument("--include-reference", action="store_true")
    list_parser.set_defaults(func=command_list)

    render_parser = subparsers.add_parser("render", help="Render exact blocks by stable ID")
    render_parser.add_argument("--id", action="append", required=True)
    render_parser.add_argument("--allow-reference", action="store_true")
    render_parser.add_argument("--allow-many", action="store_true")
    render_parser.set_defaults(func=command_render)

    audit_parser = subparsers.add_parser("audit", help="Report corpus structure and menu roles")
    audit_parser.add_argument("--json", action="store_true")
    audit_parser.set_defaults(func=command_audit)

    dump_parser = subparsers.add_parser("dump-index", help="Emit the live index as JSON")
    dump_parser.set_defaults(func=command_dump)
    return parser


def main() -> int:
    # Tool runners consume UTF-8 even when the host PowerShell code page is GBK.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except (OSError, ValueError) as error:
        print(f"Catalog error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
