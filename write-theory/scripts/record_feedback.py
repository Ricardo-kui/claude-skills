#!/usr/bin/env python3
"""Thin wrapper: write-theory feedback recording, powered by the shared engine.

The 4th scope discriminator is ``variant`` (theory-construction variants A-G:
construct differentiation / mechanism elaboration / hypothesis tree / process
theory / moderation / competing hypotheses / dialectical opposition).
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import record_feedback  # noqa: E402

CONFIG = record_feedback.SkillConfig(
    skill_name="write-theory",
    id_prefix="wtf_",
    registry_default=SKILL_ROOT / "references" / "feedback-registry.json",
    valid_categories=frozenset(
        {
            "source_intake",
            "variant_selection",
            "construct_clarity",
            "mechanism_logic",
            "hypothesis_form",
            "moderation_logic",
            "process_theory",
            "section_order",
            "terminology",
            "language_lock",
            "voice_tone",
            "corpus_fit",
            "evidence_status",
            "interface",
        }
    ),
    scope_field="variant",
    scope_cli_flag="--variant",
    scope_cli_dest="variant",
    valid_scopes=frozenset({"skill", "project", "section", "variant"}),
)


if __name__ == "__main__":
    raise SystemExit(record_feedback.entrypoint(CONFIG))
