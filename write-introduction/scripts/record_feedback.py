#!/usr/bin/env python3
"""Thin wrapper: write-introduction feedback recording, powered by the shared engine.

The registry starts with empty records (truthful state); revision rules are added
via this script. Meta-language word locks are a separate executable channel in
``references/prohibited_patterns.json`` (scanned by ``lint_introduction_language.py``).
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import record_feedback  # noqa: E402

CONFIG = record_feedback.SkillConfig(
    skill_name="write-introduction",
    id_prefix="wif_",
    registry_default=SKILL_ROOT / "references" / "feedback-registry.json",
    valid_categories=frozenset(
        {
            "source_intake",
            "gap_framing",
            "contribution_positioning",
            "section_order",
            "meta_language",
            "terminology",
            "language_lock",
            "voice_tone",
            "corpus_fit",
            "interface",
        }
    ),
    valid_scopes=frozenset({"skill", "project", "section"}),
    scope_cli_flag=None,
)


if __name__ == "__main__":
    raise SystemExit(record_feedback.entrypoint(CONFIG))
