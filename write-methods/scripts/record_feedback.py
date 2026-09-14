#!/usr/bin/env python3
"""Thin wrapper: write-methods feedback recording, powered by the shared engine.

The on-disk registry stays 1.0.0 with the ``design_type`` scope discriminator; the
shared engine migrates it to the canonical 1.1.0 shape in memory and maps it back
on write, so the legacy validator stays green and the data file is untouched.
"""

from __future__ import annotations

import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SHARED = SKILL_ROOT.parent / "_shared" / "feedback"
sys.path.insert(0, str(SHARED))

import record_feedback  # noqa: E402

CONFIG = record_feedback.SkillConfig(
    skill_name="write-methods",
    id_prefix="wmf_",
    registry_default=SKILL_ROOT / "references" / "feedback-registry.json",
    valid_categories=frozenset(
        {
            "source_intake",
            "methods_results_boundary",
            "section_order",
            "slot_assignment",
            "sample_scope",
            "estimand_definition",
            "terminology",
            "language_lock",
            "voice_tone",
            "measurement_argument",
            "estimator_justification",
            "evidence_interpretation",
            "corpus_fit",
            "interface",
        }
    ),
    scope_cli_flag="--design-type",
    scope_cli_dest="design_type",
    end_heading=r"^(?:##\s+生成后自检记录|>\s+\*\*\d{4}-\d{2}-\d{2}\s+修订记录)",
    legacy_disk_schema_version="1.0.0",
    legacy_scope_field="design_type",
)


if __name__ == "__main__":
    raise SystemExit(record_feedback.entrypoint(CONFIG))
