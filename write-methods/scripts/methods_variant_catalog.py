#!/usr/bin/env python3
"""Build a live evidence-aware catalog for write-methods corpus variants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


CORPUS_DIR = Path(__file__).resolve().parents[1] / "econometric-models"
REGISTRY_PATH = CORPUS_DIR / "_evidence_registry.yaml"
HEADING = re.compile(r"^###\s+变体\s*(\d+)\s*[:：]\s*(.+?)\s*$", re.MULTILINE)
EMPTY_TEMPLATE = re.compile(r"^###\s+变体\s*N\s*[:：]", re.MULTILINE)
METHOD_SLOT = re.compile(r"(?<![A-Za-z0-9])([MQ])\s*(10|[1-9])(?:\.(5))?(?!\d)", re.I)
METHOD_RANGE = re.compile(r"M\s*([1-9])\s*[–—-]\s*M?\s*([1-9])", re.I)
DESIGN_ALIASES = {
    "iv/2sls": "IV-2SLS",
    "面板数据/ols": "面板数据-OLS",
    "自然实验/did": "自然实验-DiD",
    "动态面板/gmm": "动态面板-GMM",
    "匹配did/广义did": "匹配DiD-广义DiD",
    "事件历史/事件研究": "事件历史+事件研究",
}
SLOT_ALIASES = {
    "m7补充": "M7SUP",
    "m7-supplement": "M7SUP",
    "m7 supplement": "M7SUP",
    "m2_5": "M2.5",
}


@dataclass(frozen=True)
class Variant:
    asset_id: str
    design_type: str
    number: int
    title: str
    slots: tuple[str, ...]
    role: str
    evidence: str
    paper_count: int | None
    promotion_basis: str | None
    source_file: str
    start: int
    end: int


def _field(block: str, label: str) -> str | None:
    match = re.search(rf"\*\*{re.escape(label)}\*\*\s*[:：]\s*([^\n]+)", block, re.I)
    return match.group(1).strip() if match else None


def _slots(block: str) -> tuple[str, ...]:
    raw = _field(block, "槽位") or ""
    found: list[str] = []
    for match in METHOD_RANGE.finditer(raw):
        first, last = int(match.group(1)), int(match.group(2))
        if first <= last:
            for number in range(first, last + 1):
                slot = f"M{number}"
                if slot not in found:
                    found.append(slot)
    for match in METHOD_SLOT.finditer(raw):
        decimal = ".5" if match.group(3) else ""
        slot = f"{match.group(1).upper()}{match.group(2)}{decimal}"
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
    data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("meta"), dict):
        raise ValueError("Evidence registry must contain a meta mapping")
    if data["meta"].get("canonical_promotion_source") != "variant_evidence":
        raise ValueError("Evidence registry does not declare variant_evidence as canonical")
    promotions = data.get("variant_evidence")
    if not isinstance(promotions, dict):
        raise ValueError("Evidence registry must contain a variant_evidence mapping")
    valid_roles = {"core_operator", "optional_operator", "reference_exemplar"}
    for asset_id, record in promotions.items():
        if not isinstance(record, dict) or record.get("role") not in valid_roles:
            raise ValueError(f"Invalid promotion record for {asset_id}")
        paper_count = record.get("paper_count")
        basis = record.get("verification_basis")
        if not isinstance(paper_count, int) or paper_count < 1 or not basis:
            raise ValueError(f"Incomplete promotion evidence for {asset_id}")
        if record["role"] == "optional_operator" and paper_count < 2:
            raise ValueError(f"Optional operator lacks cross-source evidence: {asset_id}")
        if record["role"] == "core_operator" and paper_count < 3 and record.get("status") not in {"VERIFIED", "ROBUST"}:
            raise ValueError(f"Core operator lacks verified evidence: {asset_id}")
    return data


def _promotion(asset_id: str, registry: dict) -> tuple[str, int | None, str | None]:
    record = registry["variant_evidence"].get(asset_id)
    if record is None:
        return "reference_exemplar", None, None
    return record["role"], record["paper_count"], record["verification_basis"]


def _canonical_design_type(value: str, known_types: dict[str, str]) -> str | None:
    folded = value.casefold().strip()
    if folded in known_types:
        return known_types[folded]
    alias = DESIGN_ALIASES.get(folded)
    if alias and alias.casefold() in known_types:
        return known_types[alias.casefold()]
    return None


def _canonical_slot(value: str) -> str | None:
    folded = value.casefold().strip()
    if folded in SLOT_ALIASES:
        return SLOT_ALIASES[folded]
    upper = value.upper().strip()
    if re.fullmatch(r"(?:M(?:10|[1-9])(?:\.5)?|Q(?:10|[1-9]))", upper):
        return upper
    return None


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
        matches = list(HEADING.finditer(text))
        for index, match in enumerate(matches):
            start = match.start()
            end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            block = text[start:end]
            number = int(match.group(1))
            title = match.group(2).strip()
            evidence = _evidence(block, title)
            asset_id = f"{path.stem}:v{number}"
            role, paper_count, promotion_basis = _promotion(asset_id, registry)
            variants.append(
                Variant(
                    asset_id=asset_id,
                    design_type=path.stem,
                    number=number,
                    title=title,
                    slots=_slots(block),
                    role=role,
                    evidence=evidence,
                    paper_count=paper_count,
                    promotion_basis=promotion_basis,
                    source_file=path.name,
                    start=start,
                    end=end,
                )
            )
    ids = [item.asset_id for item in variants]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate asset IDs detected")
    missing_assets = sorted(set(registry["variant_evidence"]) - set(ids))
    if missing_assets:
        raise ValueError(f"Registry contains unknown asset IDs: {', '.join(missing_assets)}")
    _validate_registry_snapshot(registry, variants, texts)
    return variants, texts


def _validate_registry_snapshot(registry: dict, variants: list[Variant], texts: dict[str, str]) -> None:
    meta = registry["meta"]
    filled = len({item.design_type for item in variants})
    total_types = len(texts)
    empty = sorted(Path(name).stem for name in texts if not any(item.source_file == name for item in variants))
    role_counts = {role: 0 for role in ("core_operator", "optional_operator", "reference_exemplar")}
    for item in variants:
        role_counts[item.role] += 1
    expected = {
        "total_design_types": total_types,
        "filled_design_types": filled,
        "total_variants": len(variants),
        "empty_design_types": empty,
        "menu_roles": role_counts,
    }
    mismatches = [key for key, value in expected.items() if meta.get(key) != value]
    summaries = registry.get("evidence", {}).get("by_design_type", {})
    known_types = {Path(name).stem for name in texts}
    if not isinstance(summaries, dict) or set(summaries) != known_types:
        mismatches.append("evidence.by_design_type")
    else:
        for design_type, record in summaries.items():
            slots = record.get("slots_covered", []) if isinstance(record, dict) else []
            if any(_canonical_slot(str(slot)) is None for slot in slots):
                mismatches.append(f"evidence.by_design_type.{design_type}.slots_covered")
    if mismatches:
        raise ValueError("Evidence registry snapshot mismatch: " + ", ".join(mismatches))


def _select(
    variants: list[Variant], design_type: str | None, slot: str | None, include_reference: bool
) -> list[Variant]:
    selected = variants
    if design_type:
        selected = [item for item in selected if item.design_type.casefold() == design_type.casefold()]
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
    if args.design_type:
        canonical_type = _canonical_design_type(args.design_type, known_types)
    if args.design_type and canonical_type is None:
        print(f"Unknown design type: {args.design_type}", file=sys.stderr)
        return 2
    canonical_slot = _canonical_slot(args.slot) if args.slot else None
    if args.slot and canonical_slot is None:
        print(f"Invalid slot: {args.slot}; expected M1-M10, M2.5, or Q1-Q10", file=sys.stderr)
        return 2
    if canonical_slot == "M7SUP":
        print("M7 supplement uses references/slot-M7-supplement.md only; no corpus variants are indexed.", file=sys.stderr)
        return 0
    selected = _select(variants, canonical_type, canonical_slot, args.include_reference)
    for item in selected:
        slots = ",".join(item.slots) if item.slots else "UNCLASSIFIED"
        promotion = f"papers={item.paper_count};basis={item.promotion_basis}" if item.paper_count else "unpromoted"
        print(f"{item.asset_id}\t{slots}\t{item.role}\t{promotion}\t{item.evidence}\t{item.title}")
    if not selected:
        print(
            "No default-eligible variants matched. Re-run with --include-reference "
            "to inspect single-paper exemplars, or use the slot core only.",
            file=sys.stderr,
        )
    return 0


def command_render(args: argparse.Namespace) -> int:
    variants, texts = load_catalog()
    by_id = {item.asset_id.casefold(): item for item in variants}
    requested: list[Variant] = []
    missing: list[str] = []
    folded_ids = [asset_id.casefold() for asset_id in args.id]
    if len(folded_ids) != len(set(folded_ids)):
        print("Duplicate asset IDs are not allowed.", file=sys.stderr)
        return 2
    for asset_id in args.id:
        item = by_id.get(asset_id.casefold())
        if item is None:
            missing.append(asset_id)
        else:
            requested.append(item)
    if missing:
        print(f"Unknown asset ID(s): {', '.join(missing)}", file=sys.stderr)
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
        print(
            f"<!-- menu_role: {item.role}; papers: {item.paper_count}; "
            f"promotion_basis: {item.promotion_basis}; evidence: {item.evidence} -->"
        )
        print(texts[item.source_file][item.start:item.end].rstrip())
    return 0


def command_audit(args: argparse.Namespace) -> int:
    variants, texts = load_catalog()
    by_type: dict[str, int] = {}
    by_role: dict[str, int] = {}
    by_slot: dict[str, int] = {}
    for item in variants:
        by_type[item.design_type] = by_type.get(item.design_type, 0) + 1
        by_role[item.role] = by_role.get(item.role, 0) + 1
        for slot in item.slots or ("UNCLASSIFIED",):
            by_slot[slot] = by_slot.get(slot, 0) + 1
    empty_templates = sorted(
        name for name, text in texts.items() if EMPTY_TEMPLATE.search(text) and not HEADING.search(text)
    )
    payload = {
        "promotion_authority": "_evidence_registry.yaml:variant_evidence",
        "total_variants": len(variants),
        "design_types_with_variants": len(by_type),
        "by_design_type": dict(sorted(by_type.items())),
        "by_role": dict(sorted(by_role.items())),
        "by_slot": dict(sorted(by_slot.items())),
        "unclassified_ids": [item.asset_id for item in variants if not item.slots],
        "promoted_ids": [item.asset_id for item in variants if item.role != "reference_exemplar"],
        "empty_template_files": empty_templates,
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"variants={payload['total_variants']}")
        print(f"design_types_with_variants={payload['design_types_with_variants']}")
        print("roles=" + ", ".join(f"{key}:{value}" for key, value in by_role.items()))
        print("unclassified=" + ", ".join(payload["unclassified_ids"]))
        print("empty_templates=" + ", ".join(empty_templates))
    return 0


def command_dump(_: argparse.Namespace) -> int:
    variants, _ = load_catalog()
    print(json.dumps([asdict(item) for item in variants], ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    list_parser = subparsers.add_parser("list", help="List compact candidates")
    list_parser.add_argument("--design-type")
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
