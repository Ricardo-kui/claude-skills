#!/usr/bin/env python3
"""Select and render the shadow-only Results R2 OLS-FE pilot assets."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml


SKILL_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = SKILL_ROOT / "corpus" / "_pilot_r2_index.yaml"
STATUS_RANK = {"ROBUST": 3, "VERIFIED": 2, "EMERGING": 1}


class PilotIndexError(ValueError):
    """Raised when the pilot index cannot safely resolve the legacy assets."""


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise PilotIndexError(f"Expected a YAML mapping: {path}")
    return data


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_variant_headings(text: str) -> int:
    return len(re.findall(r"^### 变体\s+\d+\s*:", text, flags=re.MULTILINE))


def extract_markdown_block(path: Path, heading: str) -> str:
    text = path.read_text(encoding="utf-8")
    marker = f"{heading}\n"
    start = text.find(marker)
    if start < 0:
        raise PilotIndexError(f"Legacy heading not found in {path}: {heading}")
    next_heading = re.search(r"^### 变体\s+\d+\s*:", text[start + len(marker) :], re.MULTILINE)
    end = len(text) if next_heading is None else start + len(marker) + next_heading.start()
    return text[start:end].rstrip() + "\n"


def extract_registry_skeleton(path: Path, locator: dict[str, Any]) -> str:
    registry = load_yaml(path)
    try:
        variants = registry["estimators"][locator["estimator"]]["slots"][locator["slot"]][
            "skeleton_variants"
        ]
    except KeyError as exc:
        raise PilotIndexError(f"Invalid registry locator in {path}: {locator}") from exc
    for variant in variants:
        if variant.get("id") == locator["variant_id"]:
            skeleton = variant.get("skeleton")
            if not isinstance(skeleton, str) or not skeleton.strip():
                raise PilotIndexError(f"Registry skeleton is empty: {locator['variant_id']}")
            return skeleton.strip() + "\n"
    raise PilotIndexError(f"Registry variant not found: {locator['variant_id']}")


def render_asset(asset: dict[str, Any]) -> str:
    locator = asset["locator"]
    path = SKILL_ROOT / locator["file"]
    if locator["type"] == "markdown_heading":
        return extract_markdown_block(path, locator["heading"])
    if locator["type"] == "registry_skeleton":
        return extract_registry_skeleton(path, locator)
    raise PilotIndexError(f"Unsupported locator type: {locator.get('type')}")


def validate_index(index: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if index.get("pilot_status") != "shadow_only":
        errors.append("pilot_status must remain shadow_only")
    if index.get("decision_node") != "results.R2.OLS_FE":
        errors.append("unexpected decision_node")

    source = index.get("sources", {}).get("legacy_corpus", {})
    source_path = SKILL_ROOT / str(source.get("file", ""))
    if not source_path.is_file():
        errors.append(f"legacy corpus does not exist: {source_path}")
    else:
        actual_hash = sha256(source_path)
        if actual_hash != str(source.get("sha256", "")).lower():
            errors.append(f"legacy corpus SHA-256 changed: {actual_hash}")
        actual_count = count_variant_headings(source_path.read_text(encoding="utf-8"))
        if actual_count != source.get("expected_variant_headings"):
            errors.append(
                f"legacy variant count changed: expected {source.get('expected_variant_headings')}, got {actual_count}"
            )

    assets = index.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.append("assets must be a non-empty list")
        return errors
    ids = [asset.get("asset_id") for asset in assets]
    if len(ids) != len(set(ids)):
        errors.append("asset_id values must be unique")
    fallbacks = [asset for asset in assets if asset.get("fallback")]
    if len(fallbacks) != 1 or not fallbacks[0].get("default_eligible"):
        errors.append("exactly one default-eligible fallback is required")

    aliases = index.get("selection_policy", {}).get("feature_aliases", {})
    if not isinstance(aliases, dict):
        errors.append("feature_aliases must be a mapping")
    elif any(not isinstance(k, str) or not isinstance(v, str) or not k or not v for k, v in aliases.items()):
        errors.append("feature_aliases keys and values must be non-empty strings")

    for asset in assets:
        asset_id = asset.get("asset_id", "<missing>")
        if asset.get("asset_role") not in {"slot_core", "optional_operator", "reference_exemplar"}:
            errors.append(f"invalid asset_role for {asset_id}")
        if asset.get("evidence_status") not in STATUS_RANK:
            errors.append(f"invalid evidence_status for {asset_id}")
        if asset.get("evidence_status") == "EMERGING" and asset.get("default_eligible"):
            errors.append(f"EMERGING asset cannot be default_eligible: {asset_id}")
        try:
            render_asset(asset)
        except (KeyError, OSError, PilotIndexError) as exc:
            errors.append(f"cannot resolve {asset_id}: {exc}")
    return errors


def normalize_features(index: dict[str, Any], features: set[str]) -> set[str]:
    aliases = index.get("selection_policy", {}).get("feature_aliases", {})
    normalized_aliases = {normalize_feature_name(key): value for key, value in aliases.items()}
    normalized = {
        normalized_aliases.get(normalize_feature_name(feature), normalize_feature_name(feature))
        for feature in features
    }
    unknown = normalized - known_features(index)
    if unknown:
        raise PilotIndexError(
            "Unknown feature tags: " + ", ".join(sorted(unknown)) + ". Run --list-features first."
        )
    return normalized


def normalize_feature_name(feature: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", feature.strip().lower())).strip("_")


def known_features(index: dict[str, Any]) -> set[str]:
    features: set[str] = set()
    for asset in index.get("assets") or []:
        features.update(normalize_feature_name(item) for item in asset.get("requires_all") or [])
        features.update(normalize_feature_name(item) for item in asset.get("match_features") or [])
    aliases = index.get("selection_policy", {}).get("feature_aliases", {})
    features.update(normalize_feature_name(value) for value in aliases.values())
    return features


def feature_catalog(index: dict[str, Any]) -> dict[str, Any]:
    return {
        "canonical_features": sorted(known_features(index)),
        "aliases": dict(sorted(index.get("selection_policy", {}).get("feature_aliases", {}).items())),
        "instruction": "Use only listed canonical features or aliases. Use no features for the ROBUST standard fallback.",
    }


def select_assets(index: dict[str, Any], features: set[str], top_k: int | None = None) -> list[dict[str, Any]]:
    policy = index["selection_policy"]
    features = normalize_features(index, features)
    limit = int(top_k or policy.get("default_top_k", 3))
    if limit < 1:
        raise PilotIndexError("top_k must be at least 1")

    eligible: list[tuple[tuple[int, int, int, str], dict[str, Any]]] = []
    fallback: dict[str, Any] | None = None
    for asset in index["assets"]:
        if asset.get("fallback"):
            fallback = asset
            continue
        required = set(asset.get("requires_all") or [])
        if not required.issubset(features):
            continue
        optional = set(asset.get("match_features") or [])
        key = (
            len(required & features),
            len(optional & features),
            STATUS_RANK[asset["evidence_status"]],
            asset["asset_id"],
        )
        eligible.append((key, asset))

    eligible.sort(key=lambda item: item[0], reverse=True)
    selected = [asset for _, asset in eligible]
    if fallback is None:
        return selected[:limit]
    if not selected:
        return [fallback]
    if policy.get("include_fallback_when_top_k_allows") and limit > 1:
        return selected[: limit - 1] + [fallback]
    return selected[:limit]


def selection_report(index: dict[str, Any], features: set[str], top_k: int | None = None) -> dict[str, Any]:
    requested_features = set(features)
    normalized_features = normalize_features(index, requested_features)
    selected = select_assets(index, normalized_features, top_k)
    rendered = [(asset, render_asset(asset)) for asset in selected]
    legacy_path = SKILL_ROOT / index["sources"]["legacy_corpus"]["file"]
    legacy_chars = len(legacy_path.read_text(encoding="utf-8"))
    selected_chars = sum(len(text) for _, text in rendered)
    return {
        "pilot_status": index["pilot_status"],
        "decision_node": index["decision_node"],
        "requested_features": sorted(requested_features),
        "features": sorted(normalized_features),
        "output_contract": index["selection_policy"].get("output_contract", []),
        "selected": [
            {
                "asset_id": asset["asset_id"],
                "asset_role": asset["asset_role"],
                "evidence_status": asset["evidence_status"],
                "default_eligible": asset["default_eligible"],
                "locator": asset["locator"],
                "rendered_chars": len(text),
            }
            for asset, text in rendered
        ],
        "context": {
            "legacy_chars": legacy_chars,
            "selected_chars": selected_chars,
            "character_reduction_ratio": round(1 - selected_chars / legacy_chars, 4),
        },
    }


def render_contract(index: dict[str, Any], selected: list[dict[str, Any]]) -> str:
    lines = ["<!-- decision-node-output-contract -->"]
    for rule in index["selection_policy"].get("output_contract", []):
        lines.append(f"- {rule}")
    for asset in selected:
        for rule in asset.get("generation_guardrails", []):
            lines.append(f"- [{asset['asset_id']}] {rule}")
    return "\n".join(lines).rstrip() + "\n"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--features", nargs="*", default=[])
    parser.add_argument("--top-k", type=int)
    parser.add_argument("--validate", action="store_true")
    parser.add_argument("--list-features", action="store_true")
    parser.add_argument("--render", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    index = load_yaml(args.index)
    errors = validate_index(index)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    if args.validate and not args.features and not args.render:
        print(json.dumps({"valid": True, "assets": len(index["assets"])}, ensure_ascii=False, indent=2))
        return 0
    if args.list_features:
        print(json.dumps(feature_catalog(index), ensure_ascii=False, indent=2))
        return 0

    report = selection_report(index, set(args.features), args.top_k)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if args.render:
        selected = select_assets(index, set(args.features), args.top_k)
        print("\n" + render_contract(index, selected), end="")
        for asset in selected:
            print(f"\n<!-- asset:{asset['asset_id']} -->")
            print(render_asset(asset), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
