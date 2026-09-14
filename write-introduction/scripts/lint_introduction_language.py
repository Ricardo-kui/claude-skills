#!/usr/bin/env python3
"""Thin wrapper: write-introduction meta-language lint, powered by the shared engine.

Scans the intro prose against ``references/prohibited_patterns.json`` (meta-language
word list, same source as the water-level gate's meta_language field) plus any active
records in ``references/feedback-registry.json``. Stops at the first ``### 提醒``
heading so the prose skeleton is linted but the reminder/GBL appendix is not.
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import lint_language  # noqa: E402
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
    end_heading=r"^###\s+提醒",
    standalone_patterns_path=SKILL_ROOT / "references" / "prohibited_patterns.json",
)


if __name__ == "__main__":
    raise SystemExit(lint_language.entrypoint(CONFIG))
