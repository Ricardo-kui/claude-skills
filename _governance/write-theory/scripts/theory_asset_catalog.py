#!/usr/bin/env python3
"""Index and retrieve governed write-theory assets.

The registry is the authority for evidence and lifecycle. Markdown remains the
authority for the prose asset itself. Historical pattern metadata that predates
the registry is retained as a reference-only legacy asset, never a default
generative recommendation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

import yaml


SKILL_ROOT = Path(__file__).resolve().parents[1]
CORPUS_DIR = SKILL_ROOT / "corpus"
REGISTRY_PATH = CORPUS_DIR / "_evidence_registry.yaml"
PATTERN_ID = re.compile(r"(?m)^pattern_id:\s*[\"']?([A-Za-z0-9_-]+)")
VALID_LIFECYCLES = {"active", "merged", "deprecated"}
VALID_ROLES = {"generative_strategy", "reference_strategy", "reference_exemplar"}
STATUS_ORDER = {"ROBUST": 0, "VERIFIED": 1, "EMERGING": 2, "UNREGISTERED": 3, "structural": -1}
MANIFEST_SCHEMA_VERSION = 1


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently overwriting them."""


def _construct_unique_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    mapping: dict = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"Duplicate YAML key in evidence registry: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping)


@dataclass(frozen=True)
class ArchitectureAsset:
    asset_id: str
    family: str
    title: str
    source_file: str
    role: str
    lifecycle: str
    evidence_status: str
    legacy_ids: tuple[str, ...]
    validation_total: int
    validation_rejects: int
    common_revise_reasons: tuple[str, ...]
    health: str
    generation_guard: dict


@dataclass(frozen=True)
class PatternAsset:
    asset_id: str
    pattern_id: str
    asset_kind: str
    family: str
    slot: str
    source_file: str
    title: str
    role: str
    lifecycle: str
    evidence_status: str
    source_papers: tuple[str, ...]
    legacy_ids: tuple[str, ...]
    merged_into: str | None
    validation_total: int
    validation_rejects: int
    common_revise_reasons: tuple[str, ...]
    health: str
    compatible_families: tuple[str, ...]


def _load_registry(registry_path: Path = REGISTRY_PATH) -> dict:
    data = yaml.load(registry_path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
    if not isinstance(data, dict) or not isinstance(data.get("patterns"), dict):
        raise ValueError("Evidence registry must contain a patterns mapping")
    governance = data.get("asset_governance")
    required = {
        "schema_version",
        "default_architecture_record",
        "default_pattern_record",
        "default_legacy_record",
        "asset_overrides",
        "managed_references",
        "representative_reference_menus",
        "generation_guards",
        "snapshot",
    }
    if not isinstance(governance, dict) or governance.get("schema_version") != 1:
        raise ValueError("Evidence registry must contain asset_governance schema version 1")
    missing = sorted(required - set(governance))
    if missing:
        raise ValueError("asset_governance missing: " + ", ".join(missing))
    if not all(isinstance(governance[key], dict) for key in required - {"schema_version"}):
        raise ValueError("asset_governance records must be mappings")
    if "default" not in governance["generation_guards"]:
        raise ValueError("generation_guards must define default")
    return data


def _family_from_path(path: str) -> str:
    match = re.search(r"(?:^|/)variants/([A-G])_", path)
    return match.group(1) if match else "cross_family"


def _slot_from_path(path: str) -> str:
    name = Path(path).name
    if name == "construct_definition.md" or "construct_differentiation" in name:
        return "T1"
    if name in {"mechanism_chain.md", "hypothesis_derivation_patterns.md", "argumentation_patterns.md"}:
        return "T3"
    if name in {"hypothesis_forms.md", "hypothesis_organization_patterns.md", "arrangement_patterns.md"}:
        return "T4"
    if name in {"moderation.md", "bilateral_argumentation_templates.md", "moderator_selection_frameworks.md"}:
        return "T5"
    if name in {"closure.md", "leitmotif-section-opener.md"}:
        return "transition"
    return "cross_slot"


def _metadata_occurrences(corpus_dir: Path) -> dict[str, list[str]]:
    occurrences: dict[str, list[str]] = {}
    for path in sorted(corpus_dir.rglob("*.md")):
        if path.name == "_index.md":
            continue
        relative = path.relative_to(corpus_dir).as_posix()
        for pattern_id in PATTERN_ID.findall(path.read_text(encoding="utf-8")):
            occurrences.setdefault(pattern_id.casefold(), []).append(relative)
    return occurrences


def _compatible_families(corpus_dir: Path, pattern_id: str, source_file: str, family: str) -> tuple[str, ...]:
    if family in set("ABCDEFG"):
        return (family,)
    text = (corpus_dir / source_file).read_text(encoding="utf-8")
    marker = re.search(rf"(?mi)^pattern_id:\s*[\"']?{re.escape(pattern_id)}[\"']?\s*$", text)
    nearby = ""
    if marker:
        block_end = text.find("-->", marker.end())
        nearby = text[marker.start():block_end if block_end >= 0 else marker.end() + 500]
    build_type = re.search(r"(?mi)^build_type:\s*(.+)$", nearby)
    signal = (build_type.group(1) if build_type else "") + " " + pattern_id.replace("_", " ")
    mapping = {
        "A": ("构念辨析", "construct differentiation", "construct definition"),
        "B": ("机制推演", "mechanism elaboration", "why chain", "mechanism chain"),
        "C": ("假设树", "hypothesis tree", "shared trunk"),
        "D": ("过程理论", "质性", "process theory", "stage process"),
        "E": ("调节效应", "边界条件", "moderation", "moderator", "boundary condition"),
        "F": ("竞争假设", "competing hypotheses", "horse race"),
        "G": ("辩证对立", "dialectical", "opposing mechanisms"),
    }
    folded = signal.casefold()
    matched = tuple(key for key, terms in mapping.items() if any(term.casefold() in folded for term in terms))
    return matched or tuple("ABCDEFG")


def _reference_fragment(source: Path, pattern_id: str, max_chars: int = 6000) -> str | None:
    """Extract one metadata-anchored pattern section without loading its whole file."""
    text = source.read_text(encoding="utf-8")
    marker = re.search(rf"(?mi)^pattern_id:\s*[\"']?{re.escape(pattern_id)}[\"']?\s*$", text)
    if not marker:
        return None
    comment_end = text.find("-->", marker.end())
    search_start = comment_end + 3 if comment_end >= 0 else marker.end()
    heading = re.search(r"(?m)^#{2,4}\s+.+$", text[search_start:])
    if not heading:
        return None
    start = search_start + heading.start()
    candidates: list[int] = []
    for boundary in (
        re.search(r"(?m)^---\s*$", text[start + 1:]),
        re.search(r"(?m)^<!--\s*\r?\npattern_id:\s*", text[start + 1:]),
    ):
        if boundary:
            candidates.append(start + 1 + boundary.start())
    end = min(candidates) if candidates else len(text)
    fragment = text[start:end].strip()
    if len(fragment) > max_chars:
        fragment = fragment[:max_chars].rsplit("\n", 1)[0].rstrip() + "\n\n[fragment truncated]"
    return fragment


def _canonical_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def validate_retrieval_manifest(data: dict) -> None:
    """Validate a deterministic, hash-chained evaluation retrieval manifest."""
    if data.get("schema_version") != MANIFEST_SCHEMA_VERSION or not isinstance(data.get("events"), list):
        raise ValueError("Invalid retrieval manifest schema")
    previous = None
    for index, event in enumerate(data["events"]):
        if not isinstance(event, dict) or event.get("sequence") != index + 1:
            raise ValueError("Invalid retrieval manifest event sequence")
        if event.get("previous_event_hash") != previous:
            raise ValueError("Broken retrieval manifest hash chain")
        supplied = event.get("event_hash")
        unsigned = {key: value for key, value in event.items() if key != "event_hash"}
        expected = hashlib.sha256(_canonical_json(unsigned).encode("utf-8")).hexdigest()
        if supplied != expected:
            raise ValueError("Retrieval manifest event hash mismatch")
        previous = supplied
    if data.get("head_hash") != previous:
        raise ValueError("Retrieval manifest head hash mismatch")


def append_retrieval_manifest(path: Path, event: dict) -> None:
    """Append one event after validating the existing chain; write atomically."""
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        validate_retrieval_manifest(data)
    else:
        data = {"schema_version": MANIFEST_SCHEMA_VERSION, "events": [], "head_hash": None}
    unsigned = {
        **event,
        "sequence": len(data["events"]) + 1,
        "previous_event_hash": data["head_hash"],
    }
    signed = {**unsigned, "event_hash": hashlib.sha256(_canonical_json(unsigned).encode("utf-8")).hexdigest()}
    data["events"].append(signed)
    data["head_hash"] = signed["event_hash"]
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def generation_contract(governance: dict, family: str, mode: str | None = None,
                        story_state: str | None = None) -> dict:
    """Return the non-negotiable generation checks for a chosen route."""
    guards = governance["generation_guards"]
    keys = ["default", family]
    if mode:
        keys.append(mode)
    if story_state:
        keys.append(story_state)
    required: list[str] = []
    prohibited: list[str] = []
    for key in keys:
        record = guards.get(key, {})
        if not isinstance(record, dict):
            raise ValueError(f"generation guard must be a mapping: {key}")
        required.extend(str(item) for item in record.get("required", []))
        prohibited.extend(str(item) for item in record.get("prohibited", []))
    return {
        "architecture": family,
        "mode": mode,
        "story_state": story_state,
        "required": list(dict.fromkeys(required)),
        "prohibited": list(dict.fromkeys(prohibited)),
    }


def _architecture_assets(corpus_dir: Path, governance: dict) -> list[ArchitectureAsset]:
    assets: list[ArchitectureAsset] = []
    for path in sorted((corpus_dir / "variants").glob("[A-G]_*.md")):
        family = path.name[0]
        record = dict(governance["default_architecture_record"])
        record.update(governance["asset_overrides"].get(f"theory:architecture:{family}", {}))
        _validate_record(f"theory:architecture:{family}", record, is_architecture=True)
        total, rejects, reasons, health = _validation_summary(record)
        assets.append(ArchitectureAsset(
            asset_id=f"theory:architecture:{family}", family=family,
            title=path.stem.split("_", 1)[1].replace("_", " "),
            source_file=path.relative_to(corpus_dir).as_posix(), role=record["role"],
            lifecycle=record["lifecycle"], evidence_status=record.get("evidence_status", "structural"),
            legacy_ids=tuple(record.get("legacy_ids", [])), validation_total=total,
            validation_rejects=rejects, common_revise_reasons=reasons, health=health,
            generation_guard=generation_contract(governance, family),
        ))
    if {item.family for item in assets} != set("ABCDEFG"):
        raise ValueError("Theory architecture inventory must contain A-G exactly once")
    return assets


def _status_for_sources(source_papers: list[str], source_records: dict) -> str:
    eligible = [
        source for source in dict.fromkeys(source_papers)
        if str(source_records.get(source, {}).get("source_tier", "")).casefold() != "auxiliary"
    ]
    count = len(eligible)
    if count < 3:
        return "EMERGING"
    subfields = {
        str(source_records.get(source, {}).get("subfield", "")).strip()
        for source in eligible
        if str(source_records.get(source, {}).get("subfield", "")).strip()
    }
    return "ROBUST" if count >= 5 and len(subfields) >= 2 else "VERIFIED"


def _effective_pattern_record(governance: dict, asset_id: str, base: dict, legacy: bool) -> dict:
    default = governance["default_legacy_record" if legacy else "default_pattern_record"]
    record = dict(default)
    record.update(governance["asset_overrides"].get(asset_id, {}))
    record.setdefault("legacy_ids", [])
    record.setdefault("merged_into", None)
    record.setdefault("validation_history_additions", [])
    record.setdefault("source_paper_additions", [])
    sources = list(record.get("source_papers_override", base.get("source_papers", [])))
    sources += list(record["source_paper_additions"])
    record["effective_sources"] = tuple(dict.fromkeys(str(value) for value in sources))
    if not legacy and not record.get("evidence_status"):
        record["evidence_status"] = str(base.get("status", "UNREGISTERED"))
    return record


def _pattern_assets(corpus_dir: Path, registry: dict) -> list[PatternAsset]:
    governance = registry["asset_governance"]
    source_records = registry.get("source_papers", {})
    occurrences = _metadata_occurrences(corpus_dir)
    assets: list[PatternAsset] = []
    registered_ids: set[str] = set()
    for pattern_id, base in registry["patterns"].items():
        if not isinstance(base, dict):
            raise ValueError(f"Pattern must be a mapping: {pattern_id}")
        home = str(base.get("home_file", ""))
        if not home or not (corpus_dir / home).is_file():
            raise ValueError(f"Pattern {pattern_id} has a missing home_file: {home}")
        asset_id = f"theory:pattern:{pattern_id}"
        record = _effective_pattern_record(governance, asset_id, base, legacy=False)
        _validate_record(asset_id, record, is_architecture=False)
        sources = record["effective_sources"]
        expected = _status_for_sources(list(sources), source_records)
        if record["evidence_status"] != expected:
            raise ValueError(
                f"Evidence status mismatch for {pattern_id}: {record['evidence_status']} != {expected}"
            )
        total, rejects, reasons, health = _validation_summary(record)
        family = str(record.get("family") or _family_from_path(home))
        assets.append(PatternAsset(
            asset_id=asset_id, pattern_id=str(pattern_id), asset_kind="pattern",
            family=family,
            slot=str(record.get("slot") or _slot_from_path(home)), source_file=home,
            title=str(base.get("description") or pattern_id), role=record["role"],
            lifecycle=record["lifecycle"], evidence_status=record["evidence_status"],
            source_papers=sources, legacy_ids=tuple(record["legacy_ids"]),
            merged_into=record["merged_into"], validation_total=total,
            validation_rejects=rejects, common_revise_reasons=reasons, health=health,
            compatible_families=_compatible_families(corpus_dir, str(pattern_id), home, family),
        ))
        registered_ids.add(str(pattern_id).casefold())
    managed_ids = {str(key).casefold() for key in governance["managed_references"]}
    for pattern_id, paths in sorted(occurrences.items()):
        if len(paths) > 1:
            raise ValueError("Duplicate corpus pattern_id: " + pattern_id + " in " + ", ".join(paths))
        if pattern_id in registered_ids or pattern_id in managed_ids:
            continue
        asset_id = f"theory:legacy:{pattern_id}"
        base = {"source_papers": []}
        record = _effective_pattern_record(governance, asset_id, base, legacy=True)
        _validate_record(asset_id, record, is_architecture=False)
        total, rejects, reasons, health = _validation_summary(record)
        family = str(record.get("family") or _family_from_path(paths[0]))
        assets.append(PatternAsset(
            asset_id=asset_id, pattern_id=pattern_id, asset_kind="legacy_reference",
            family=family,
            slot=str(record.get("slot") or _slot_from_path(paths[0])), source_file=paths[0],
            title=pattern_id.replace("_", " "), role=record["role"], lifecycle=record["lifecycle"],
            evidence_status=str(record.get("evidence_status", "UNREGISTERED")), source_papers=(),
            legacy_ids=tuple(record["legacy_ids"]), merged_into=record["merged_into"],
            validation_total=total, validation_rejects=rejects,
            common_revise_reasons=reasons, health=health,
            compatible_families=_compatible_families(corpus_dir, pattern_id, paths[0], family),
        ))
    for pattern_id, entry in governance["managed_references"].items():
        if not isinstance(entry, dict):
            raise ValueError(f"Managed reference must be a mapping: {pattern_id}")
        home = str(entry.get("source_file", ""))
        if not home or not (corpus_dir / home).is_file():
            raise ValueError(f"Managed reference {pattern_id} has a missing source_file")
        asset_id = f"theory:managed:{pattern_id}"
        record = _effective_pattern_record(governance, asset_id, entry, legacy=False)
        record.setdefault("evidence_status", "EMERGING")
        _validate_record(asset_id, record, is_architecture=False)
        total, rejects, reasons, health = _validation_summary(record)
        assets.append(PatternAsset(
            asset_id=asset_id, pattern_id=pattern_id, asset_kind="managed_reference",
            family=str(entry["family"]), slot=str(entry["slot"]), source_file=home,
            title=str(entry["title"]), role=record["role"], lifecycle=record["lifecycle"],
            evidence_status=record["evidence_status"], source_papers=record["effective_sources"],
            legacy_ids=tuple(record["legacy_ids"]), merged_into=record["merged_into"],
            validation_total=total, validation_rejects=rejects,
            common_revise_reasons=reasons, health=health,
            compatible_families=_compatible_families(corpus_dir, pattern_id, home, str(entry["family"])),
        ))
    ids = [item.asset_id for item in assets]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate catalog asset IDs")
    return assets


def _validation_summary(record: dict) -> tuple[int, int, tuple[str, ...], str]:
    history = record.get("validation_history_additions", [])
    if not isinstance(history, list):
        raise ValueError("validation_history_additions must be a list")
    rows = [row for row in history if isinstance(row, dict)]
    total = len(rows)
    rejects = sum(row.get("verdict") == "REJECT" for row in rows)
    reasons = tuple(dict.fromkeys(
        str(row.get("reason") or "").strip() for row in rows
        if row.get("verdict") in {"REVISE", "REJECT"} and str(row.get("reason") or "").strip()
    ))
    health = "CAUTION" if total >= 2 and rejects / total >= 0.5 else (
        "HEALTHY" if total >= 2 else "INSUFFICIENT_DATA"
    )
    return total, rejects, reasons, health


def _validate_record(asset_id: str, record: dict, *, is_architecture: bool) -> None:
    if record.get("role") not in VALID_ROLES:
        raise ValueError(f"Invalid role for {asset_id}: {record.get('role')}")
    if record.get("lifecycle") not in VALID_LIFECYCLES:
        raise ValueError(f"Invalid lifecycle for {asset_id}: {record.get('lifecycle')}")
    if record["lifecycle"] == "merged" and not record.get("merged_into"):
        raise ValueError(f"Merged asset lacks target: {asset_id}")
    if record["lifecycle"] != "active" and record["role"] == "generative_strategy":
        raise ValueError(f"Inactive asset cannot remain generative: {asset_id}")
    if is_architecture and record["role"] != "generative_strategy":
        raise ValueError(f"Theory architecture must remain generative: {asset_id}")
    if record["role"] == "generative_strategy" and not is_architecture:
        sources = record.get("effective_sources", ())
        if record.get("evidence_status") not in {"VERIFIED", "ROBUST", "structural"} or len(sources) < 3:
            raise ValueError(f"Generative pattern lacks verified evidence: {asset_id}")


def inventory_fingerprint(architectures: list[ArchitectureAsset], patterns: list[PatternAsset]) -> str:
    payload = "\n".join(sorted([item.asset_id for item in [*architectures, *patterns]])).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_catalog(corpus_dir: Path = CORPUS_DIR, registry_path: Path = REGISTRY_PATH) -> tuple[list[ArchitectureAsset], list[PatternAsset]]:
    registry = _load_registry(registry_path)
    architectures = _architecture_assets(corpus_dir, registry["asset_governance"])
    patterns = _pattern_assets(corpus_dir, registry)
    assets = [*architectures, *patterns]
    by_id = {item.asset_id: item for item in assets}
    aliases: dict[str, str] = {}
    for item in assets:
        for legacy_id in item.legacy_ids:
            folded = legacy_id.casefold()
            if folded in aliases or folded in {key.casefold() for key in by_id}:
                raise ValueError(f"Duplicate or colliding legacy ID: {legacy_id}")
            aliases[folded] = item.asset_id
        if isinstance(item, PatternAsset) and item.lifecycle == "merged":
            target = by_id.get(item.merged_into or "")
            if target is None or target.lifecycle != "active" or target.asset_id == item.asset_id:
                raise ValueError(f"Invalid merge target for {item.asset_id}")
    governance = registry["asset_governance"]
    snapshot = governance["snapshot"]
    expected = {
        "architecture_assets": len(architectures),
        "pattern_assets": len(patterns),
        "inventory_sha256": inventory_fingerprint(architectures, patterns),
    }
    mismatch = [key for key, value in expected.items() if snapshot.get(key) != value]
    if mismatch:
        raise ValueError("Asset governance snapshot mismatch: " + ", ".join(mismatch))
    cap = int(governance.get("reference_menu_cap", 5))
    for architecture_id, menu in governance["representative_reference_menus"].items():
        architecture = by_id.get(architecture_id)
        if not isinstance(architecture, ArchitectureAsset) or not isinstance(menu, list) or len(menu) > cap:
            raise ValueError(f"Invalid representative menu for {architecture_id}")
        if len(menu) != len(set(menu)):
            raise ValueError(f"Duplicate menu asset for {architecture_id}")
        for asset_id in menu:
            item = by_id.get(asset_id)
            if not isinstance(item, PatternAsset) or item.lifecycle != "active" or architecture.family not in item.compatible_families:
                raise ValueError(f"Invalid reference menu asset {asset_id} for {architecture_id}")
    return architectures, patterns


def resolve_assets(requested_ids: list[str], architectures: list[ArchitectureAsset] | None = None,
                   patterns: list[PatternAsset] | None = None) -> tuple[list[ArchitectureAsset | PatternAsset], list[str | None]]:
    architectures, patterns = (architectures, patterns) if architectures is not None and patterns is not None else load_catalog()
    assets = [*architectures, *patterns]
    by_id = {item.asset_id.casefold(): item for item in assets}
    shorthand = {item.asset_id.rsplit(":", 1)[-1].casefold(): item for item in assets if isinstance(item, PatternAsset)}
    aliases = {alias.casefold(): item for item in assets for alias in item.legacy_ids}
    resolved: list[ArchitectureAsset | PatternAsset] = []
    notices: list[str | None] = []
    for requested in requested_ids:
        item = by_id.get(requested.casefold()) or shorthand.get(requested.casefold()) or aliases.get(requested.casefold())
        if item is None:
            raise ValueError(f"Unknown asset ID: {requested}")
        notice = None if requested.casefold() == item.asset_id.casefold() else f"{requested} -> {item.asset_id}"
        if isinstance(item, PatternAsset) and item.lifecycle == "merged":
            item = by_id[item.merged_into.casefold()]
            notice = f"{requested} -> {item.asset_id}"
        resolved.append(item)
        notices.append(notice)
    if len({item.asset_id for item in resolved}) != len(resolved):
        raise ValueError("Requested IDs resolve to duplicate assets")
    return resolved, notices


def resolve_architecture(requested: str, architectures: list[ArchitectureAsset]) -> ArchitectureAsset:
    """Accept a canonical ID or an unambiguous A-G family shorthand."""
    folded = requested.casefold()
    matches = [
        item for item in architectures
        if folded in {item.asset_id.casefold(), item.family.casefold(), f"architecture:{item.family}".casefold()}
    ]
    if len(matches) != 1:
        raise ValueError(f"Unknown or ambiguous architecture ID: {requested}")
    return matches[0]


def command_list_architectures(args: argparse.Namespace) -> int:
    architectures, _ = load_catalog()
    rows = [asdict(item) for item in architectures if item.lifecycle == "active" and item.role == "generative_strategy"]
    print(json.dumps(rows, ensure_ascii=False, indent=2) if args.json else "\n".join(
        f"{row['asset_id']}\t{row['title']}\t{row['health']}" for row in rows
    ))
    return 0


def reference_query_score(item: PatternAsset, query: str | None) -> int:
    if not query:
        return 0
    terms = {term.casefold() for term in re.findall(r"[A-Za-z0-9_]+", query) if len(term) >= 3}
    haystack = f"{item.pattern_id} {item.title} {item.source_file}".casefold()
    return sum(term in haystack for term in terms)


def command_list_references(args: argparse.Namespace) -> int:
    architectures, patterns = load_catalog()
    architecture = resolve_architecture(args.architecture, architectures)
    registry = _load_registry()["asset_governance"]
    menu = registry["representative_reference_menus"].get(architecture.asset_id)
    if menu:
        by_id = {item.asset_id: item for item in patterns}
        selected = [by_id[item] for item in menu if not args.slot or by_id[item].slot == args.slot]
    else:
        eligible = [
            item for item in patterns
            if item.lifecycle == "active" and architecture.family in item.compatible_families
            and (not args.slot or item.slot == args.slot)
        ]
        ranking = lambda item: (
            -reference_query_score(item, args.query),
            STATUS_ORDER.get(item.evidence_status, 9),
            -len(item.source_papers),
            item.pattern_id,
        )
        if args.query:
            eligible.sort(key=ranking)
            selected = eligible
        else:
            specific = [item for item in eligible if len(item.compatible_families) < 7]
            generic = [item for item in eligible if len(item.compatible_families) == 7]
            specific.sort(key=ranking)
            generic.sort(key=ranking)
            selected = specific[:2] + generic
    candidates = list(selected)
    cap = int(registry.get("reference_menu_cap", 5))
    if not args.include_all:
        selected = selected[:cap]
    rows = [asdict(item) for item in selected]
    if args.manifest:
        append_retrieval_manifest(Path(args.manifest), {
            "command": "list-references",
            "architecture": architecture.asset_id,
            "slot": args.slot,
            "query": args.query,
            "candidate_ids": [item.asset_id for item in candidates],
            "returned_ids": [item.asset_id for item in selected],
            "cap_applied": None if args.include_all else cap,
        })
    print(json.dumps(rows, ensure_ascii=False, indent=2) if args.json else "\n".join(
        f"{row['asset_id']}\t{row['evidence_status']}\t{row['slot']}\t{row['title']}" for row in rows
    ))
    return 0


def command_generation_contract(args: argparse.Namespace) -> int:
    architectures, _ = load_catalog()
    architecture = resolve_architecture(args.architecture, architectures)
    governance = _load_registry()["asset_governance"]
    contract = generation_contract(governance, architecture.family, args.mode, args.story_state)
    if args.json:
        print(json.dumps(contract, ensure_ascii=False, indent=2))
    else:
        print(f"architecture: {architecture.asset_id}")
        print(f"mode: {args.mode or 'unspecified'}")
        print(f"story_state: {args.story_state or 'unspecified'}")
        print("required:")
        print("\n".join(f"- {item}" for item in contract["required"]))
        print("prohibited:")
        print("\n".join(f"- {item}" for item in contract["prohibited"]) or "- none")
    return 0


def command_render(args: argparse.Namespace) -> int:
    architectures, patterns = load_catalog()
    selected, notices = resolve_assets(args.id, architectures, patterns)
    cap = int(_load_registry()["asset_governance"].get("render_cap", 4))
    exact_count = sum(isinstance(item, PatternAsset) for item in selected)
    if exact_count and not args.allow_reference:
        raise ValueError("Exact reference assets require --allow-reference")
    if exact_count > cap and not args.allow_many:
        raise ValueError(f"At most {cap} exact reference assets may be rendered per call")
    manifest_assets = []
    for item, notice in zip(selected, notices):
        if notice:
            print(f"<!-- alias: {notice} -->")
        print(f"<!-- asset_id: {item.asset_id}; role: {item.role}; status: {item.evidence_status} -->")
        if getattr(item, "health", "") == "CAUTION":
            print("<!-- governance_health: CAUTION; reasons: " + " | ".join(item.common_revise_reasons) + " -->")
        source = CORPUS_DIR / item.source_file
        if isinstance(item, ArchitectureAsset):
            payload = source.read_text(encoding="utf-8")
        else:
            fragment = _reference_fragment(source, item.pattern_id)
            payload = fragment or f"Reference asset: {item.title}\nSource file: {item.source_file}\n[No metadata-anchored fragment available]"
        print(payload)
        manifest_assets.append({
            "requested_id": args.id[len(manifest_assets)],
            "resolved_id": item.asset_id,
            "role": item.role,
            "evidence_status": item.evidence_status,
            "source_file": item.source_file,
            "content_sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
        })
    if args.manifest:
        append_retrieval_manifest(Path(args.manifest), {
            "command": "render",
            "allow_reference": bool(args.allow_reference),
            "assets": manifest_assets,
        })
    return 0


def command_audit(args: argparse.Namespace) -> int:
    architectures, patterns = load_catalog()
    data = {
        "architecture_assets": len(architectures),
        "pattern_assets": len(patterns),
        "generative_architectures": sum(item.role == "generative_strategy" for item in architectures),
        "reference_assets": sum(item.role == "reference_exemplar" for item in patterns),
        "status_counts": dict(Counter(item.evidence_status for item in patterns)),
        "validation_health": dict(Counter(item.health for item in [*architectures, *patterns])),
    }
    print(json.dumps(data, ensure_ascii=False, indent=2) if args.json else "\n".join(f"{key}: {value}" for key, value in data.items()))
    return 0


def command_verify_manifest(args: argparse.Namespace) -> int:
    path = Path(args.manifest)
    data = json.loads(path.read_text(encoding="utf-8"))
    validate_retrieval_manifest(data)
    print(json.dumps({
        "valid": True,
        "events": len(data["events"]),
        "head_hash": data["head_hash"],
    }, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    architectures = sub.add_parser("list-architectures")
    architectures.add_argument("--json", action="store_true")
    architectures.set_defaults(func=command_list_architectures)
    references = sub.add_parser("list-references")
    references.add_argument("--architecture", required=True)
    references.add_argument("--slot")
    references.add_argument("--query")
    references.add_argument("--include-all", action="store_true")
    references.add_argument("--json", action="store_true")
    references.add_argument("--manifest", help="Append a hash-chained evaluation retrieval trace")
    references.set_defaults(func=command_list_references)
    contract = sub.add_parser("generation-contract")
    contract.add_argument("--architecture", required=True)
    contract.add_argument("--mode", choices=["hypotheses", "propositions", "no_numbered_hypotheses"])
    contract.add_argument("--story-state", choices=["complete", "ambiguous", "local_only"], default="complete")
    contract.add_argument("--json", action="store_true")
    contract.set_defaults(func=command_generation_contract)
    render = sub.add_parser("render")
    render.add_argument("--id", action="append", required=True)
    render.add_argument("--allow-reference", action="store_true")
    render.add_argument("--allow-many", action="store_true")
    render.add_argument("--manifest", help="Append a hash-chained evaluation retrieval trace")
    render.set_defaults(func=command_render)
    audit = sub.add_parser("audit")
    audit.add_argument("--json", action="store_true")
    audit.set_defaults(func=command_audit)
    verify = sub.add_parser("verify-manifest")
    verify.add_argument("--manifest", required=True)
    verify.set_defaults(func=command_verify_manifest)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
