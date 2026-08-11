#!/usr/bin/env python3
"""Deterministic contract tests for the Pollock story-writing workflow."""

from __future__ import annotations

import importlib.util
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = SKILL_ROOT.parent


def load_validator():
    path = SKILL_ROOT / "scripts" / "validate_story_contract.py"
    spec = importlib.util.spec_from_file_location("story_validator", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load validator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(relative: str) -> str:
    return (PACKAGE_ROOT / relative).read_text(encoding="utf-8")


def require(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    print(f"PASS: {name}")


def main() -> int:
    validator = load_validator()
    base = {
        "story": {
            "schema_version": 1,
            "status": "confirmed",
            "stage": "refining",
            "evidence_state": "stable",
            "theme_question": "Why does X affect Y?",
            "central_knot": "Prior work predicts Y, yet the mechanism remains unclear.",
            "stakes": {"theoretical": "The missing mechanism changes the explanation."},
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
                    "promised_resolution": "Estimate and interpret the X-Y relationship.",
                }
            ],
            "reader_shift": {"from": "direct effect", "to": "mechanism-aware account"},
        }
    }
    require("valid canonical contract", validator.validate(base) == [])

    integrity = {
        **base,
        "story": {
            **base["story"],
            "integrity": {
                "theme_grounding": "grounded",
                "knot_authenticity": "grounded",
                "character_discipline": "grounded",
                "payoff_feasibility": "provisional",
                "unsupported_moves": ["claim a confirmed mechanism"],
                "notes": "Evidence for the mechanism remains incomplete.",
            },
        },
    }
    require("integrity ledger validates", validator.validate(integrity) == [])

    missing_knot = {"story": {**base["story"], "central_knot": ""}}
    require(
        "full-section contract blocks a missing knot",
        any("central_knot" in error for error in validator.validate(missing_knot)),
    )

    intro = read("write-introduction/SKILL.md")
    theory = read("write-theory/SKILL.md")
    methods = read("write-methods/SKILL.md")
    results = read("write-results/SKILL.md")
    retired = read("write-discussion/SKILL.md")
    retired_agent = read("write-discussion/agents/openai.yaml")
    discussion_review = read("discussion-review/SKILL.md")

    require("Introduction exposes front-end and alignment modes", "--mode=introduction|front-end|align" in intro)
    require("Introduction permits only labelled local bypass", "local-only bypass" in intro)
    require("Introduction ignores legacy story frames", "忽略任何 legacy `story.story_frame`" in intro)
    require("Theory maps hypotheses to storylines", "storyline_id" in theory)
    require("Theory blocks silent new main characters", "不得静默引入新的主角构念" in theory or "new main characters require" in theory)
    require(
        "Methods contains story-to-model alignment",
        "storyline–hypothesis–variable mapping" in methods or "story_alignment" in methods,
    )
    require("Methods blocks untestable promised resolutions", "无法兑现的 storyline" in methods)
    require("Results has four honest resolution states", "supported | mixed | unsupported | unresolved" in results)
    require("Results identifies climax and falling action", "climax" in results and "falling action" in results)
    require("Preparing stage prevents Results prose", "`preparing` 不生成 Results" in results)
    require("Discussion writer is a non-generative boundary", "must not" in retired and "do not draft" in retired)
    require("Discussion writer cannot invoke implicitly", "allow_implicit_invocation: false" in retired_agent)
    require("Discussion review does not route to writer", "$write-discussion" not in discussion_review)

    for skill in (
        "distill-introduction-exemplar",
        "distill-theory-exemplar",
        "distill-methods-exemplar",
        "distill-results-exemplar",
    ):
        entry = read(f"{skill}/SKILL.md")
        references = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (PACKAGE_ROOT / skill / "references").glob("*.md")
        )
        require(
            f"{skill} applies story-fidelity governance",
            "story_fidelity" in entry
            or "story-fidelity" in entry.lower()
            or "Story-Fidelity" in references,
        )

    migration = read("paper-story-contract/references/schema.md")
    require("legacy paper state has an explicit migration path", "central_knot_statement" in migration)
    require("canonical schema omits story-frame output", "exemplar_blueprint:" not in migration)
    require("story-integrity gate replaces frame selection", "story-integrity-gate.md" in read("paper-story-contract/SKILL.md"))
    require("retired frame menu is absent", not (SKILL_ROOT / "references" / "story-frame-menu.md").exists())
    require("retired Introduction modulation is absent", not (PACKAGE_ROOT / "write-introduction" / "references" / "story-modulation.md").exists())
    require("retired Theory modulation is absent", not (PACKAGE_ROOT / "write-theory" / "corpus" / "storytelling" / "knot-architecture-modulation.md").exists())
    print("PASS: all workflow contract tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
