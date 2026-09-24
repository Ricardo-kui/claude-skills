#!/usr/bin/env python3
"""Thin wrapper: polish feedback recording, powered by the shared engine.

The 4th scope discriminator is ``action`` (rhetorical actions from
``story-blueprints/v4/rhetoric-moves/_index.md``, e.g. 双向预测先行 / 双链汇一 /
调节元框架 / 反向证伪 / 嵌入型补充分析 / 条件支付收束 / 微观打磨).
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import record_feedback  # noqa: E402

CONFIG = record_feedback.SkillConfig(
    skill_name="polish",
    id_prefix="pof_",
    registry_default=SKILL_ROOT / "references" / "feedback-registry.json",
    valid_categories=frozenset(
        {
            "routing",
            "rhetorical_action_match",
            "fluency_gate",
            "specificity_gate",
            "source_attribution",
            "terminology",
            "language_lock",
            "voice_tone",
            "corpus_fit",
            "interface",
        }
    ),
    scope_field="action",
    scope_cli_flag="--action",
    scope_cli_dest="action",
    valid_scopes=frozenset({"skill", "project", "action"}),
)


if __name__ == "__main__":
    raise SystemExit(record_feedback.entrypoint(CONFIG))
