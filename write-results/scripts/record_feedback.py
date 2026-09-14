#!/usr/bin/env python3
"""Thin wrapper: write-results feedback recording, powered by the shared engine."""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import record_feedback  # noqa: E402

CONFIG = record_feedback.SkillConfig(
    skill_name="write-results",
    id_prefix="wrf_",
    registry_default=SKILL_ROOT / "references" / "feedback-registry.json",
    valid_categories=frozenset(
        {
            "source_intake",
            "section_order",
            "hypothesis_order",
            "analysis_logic",
            "heading_navigation",
            "paragraph_cohesion",
            "terminology",
            "language_lock",
            "voice_tone",
            "evidence_interpretation",
            "mixed_evidence",
            "corpus_fit",
            "interface",
        }
    ),
)


if __name__ == "__main__":
    raise SystemExit(record_feedback.entrypoint(CONFIG))
