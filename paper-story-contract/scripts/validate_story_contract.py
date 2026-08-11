#!/usr/bin/env python3
"""Validate the canonical Pollock paper story contract."""

from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml


STATUS = {"provisional", "confirmed"}
STAGES = {"preparing", "blocking", "refining", "finishing"}
EVIDENCE_STATES = {"unstable", "mixed", "stable"}
MAIN_ROLES = {"focal_predictor", "focal_outcome", "core_process"}
INTEGRITY_STATES = {"grounded", "provisional", "unsupported"}


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(document: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(document, dict):
        return ["document must be a YAML mapping"]
    story = document.get("story", document)
    if not isinstance(story, dict):
        return ["story must be a mapping"]

    if story.get("schema_version") != 1:
        errors.append("story.schema_version must equal 1")
    if story.get("status") not in STATUS:
        errors.append("story.status must be provisional or confirmed")
    if story.get("stage") not in STAGES:
        errors.append("story.stage has an invalid value")
    if story.get("evidence_state") not in EVIDENCE_STATES:
        errors.append("story.evidence_state has an invalid value")
    for field in ("theme_question", "central_knot"):
        if not nonempty(story.get(field)):
            errors.append(f"story.{field} must be a non-empty string")

    characters = story.get("characters")
    if not isinstance(characters, dict):
        errors.append("story.characters must be a mapping")
        characters = {}
    main = characters.get("main", [])
    supporting = characters.get("supporting", [])
    if not isinstance(main, list) or not main:
        errors.append("story.characters.main must contain at least one character")
        main = []
    if not isinstance(supporting, list):
        errors.append("story.characters.supporting must be a list")
        supporting = []

    character_names: set[str] = set()
    for group_name, group in (("main", main), ("supporting", supporting)):
        for index, character in enumerate(group):
            prefix = f"story.characters.{group_name}[{index}]"
            if not isinstance(character, dict):
                errors.append(f"{prefix} must be a mapping")
                continue
            name = character.get("name")
            if not nonempty(name):
                errors.append(f"{prefix}.name must be non-empty")
            elif name in character_names:
                errors.append(f"duplicate character name: {name}")
            else:
                character_names.add(name)
            if group_name == "main" and character.get("role") not in MAIN_ROLES:
                errors.append(f"{prefix}.role has an invalid main-character value")
            if not nonempty(character.get("level")):
                errors.append(f"{prefix}.level must be non-empty")

    storylines = story.get("storylines")
    if not isinstance(storylines, list) or not storylines:
        errors.append("story.storylines must contain at least one storyline")
        storylines = []
    storyline_ids: set[str] = set()
    for index, storyline in enumerate(storylines):
        prefix = f"story.storylines[{index}]"
        if not isinstance(storyline, dict):
            errors.append(f"{prefix} must be a mapping")
            continue
        storyline_id = storyline.get("id")
        if not nonempty(storyline_id):
            errors.append(f"{prefix}.id must be non-empty")
        elif storyline_id in storyline_ids:
            errors.append(f"duplicate storyline id: {storyline_id}")
        else:
            storyline_ids.add(storyline_id)
        for field in ("question", "promised_resolution"):
            if not nonempty(storyline.get(field)):
                errors.append(f"{prefix}.{field} must be non-empty")
        constructs = storyline.get("constructs")
        if not isinstance(constructs, list) or not constructs:
            errors.append(f"{prefix}.constructs must be a non-empty list")
        else:
            for construct in constructs:
                if construct not in character_names:
                    errors.append(
                        f"{prefix}.constructs references undeclared character: {construct}"
                    )

    integrity = story.get("integrity")
    if integrity is not None:
        if not isinstance(integrity, dict):
            errors.append("story.integrity must be a mapping")
        else:
            for field in (
                "theme_grounding",
                "knot_authenticity",
                "character_discipline",
                "payoff_feasibility",
            ):
                if integrity.get(field) not in INTEGRITY_STATES:
                    errors.append(f"story.integrity.{field} has an invalid value")
            unsupported_moves = integrity.get("unsupported_moves")
            if not isinstance(unsupported_moves, list) or not all(
                nonempty(move) for move in unsupported_moves
            ):
                errors.append("story.integrity.unsupported_moves must be a list of non-empty strings")
            if not nonempty(integrity.get("notes")):
                errors.append("story.integrity.notes must be a non-empty string")
    return errors


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def self_test() -> int:
    base = {
        "story": {
            "schema_version": 1,
            "status": "confirmed",
            "stage": "refining",
            "evidence_state": "stable",
            "theme_question": "Why does X affect Y?",
            "central_knot": "Prior work predicts Y, yet the mechanism remains unclear.",
            "characters": {
                "main": [
                    {"name": "X", "role": "focal_predictor", "level": "firm"},
                    {"name": "Y", "role": "focal_outcome", "level": "firm"},
                ],
                "supporting": [],
            },
            "storylines": [
                {
                    "id": "S1",
                    "question": "Does X affect Y?",
                    "constructs": ["X", "Y"],
                    "promised_resolution": "Estimate the X-Y relationship.",
                }
            ],
        }
    }
    cases: list[tuple[str, dict[str, Any], str | None]] = [
        ("valid", base, None),
        (
            "missing knot",
            {**base, "story": {**base["story"], "central_knot": ""}},
            "central_knot",
        ),
        (
            "bad enum",
            {**base, "story": {**base["story"], "stage": "drafting"}},
            "invalid value",
        ),
        (
            "duplicate storyline",
            {
                **base,
                "story": {
                    **base["story"],
                    "storylines": base["story"]["storylines"] * 2,
                },
            },
            "duplicate storyline id",
        ),
        (
            "character mismatch",
            {
                **base,
                "story": {
                    **base["story"],
                    "storylines": [
                        {
                            **base["story"]["storylines"][0],
                            "constructs": ["X", "Z"],
                        }
                    ],
                },
            },
            "undeclared character",
        ),
        (
            "unsupported version",
            {**base, "story": {**base["story"], "schema_version": 2}},
            "schema_version",
        ),
        (
            "malformed integrity ledger",
            {
                **base,
                "story": {
                    **base["story"],
                    "integrity": {"theme_grounding": "unknown"},
                },
            },
            "story.integrity.theme_grounding",
        ),
    ]
    failed = False
    with tempfile.TemporaryDirectory(prefix="story-contract-") as directory:
        for name, payload, expected in cases:
            path = Path(directory) / f"{name.replace(' ', '-')}.yaml"
            path.write_text(yaml.safe_dump(payload, sort_keys=False), encoding="utf-8")
            errors = validate(load_yaml(path))
            passed = not errors if expected is None else any(expected in item for item in errors)
            print(f"{'PASS' if passed else 'FAIL'}: {name}")
            failed = failed or not passed
    return 1 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.path is None:
        parser.error("path is required unless --self-test is used")
    try:
        errors = validate(load_yaml(args.path))
    except (OSError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: story contract is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
