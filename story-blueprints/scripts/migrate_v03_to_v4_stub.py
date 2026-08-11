"""Create a v0.4-lite review stub from one legacy blueprint without touching the legacy file."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEGACY = ROOT / "blueprints"
TARGET = ROOT / "v4" / "blueprints"


def legacy_header(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## 文件头\s+```yaml\s*(.*?)```", text, re.S)
    if not match:
        raise ValueError("legacy header is missing")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("legacy header is not a mapping")
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("legacy_id", help="legacy blueprint filename without .md")
    args = parser.parse_args()
    source = LEGACY / f"{args.legacy_id}.md"
    if not source.exists():
        raise SystemExit(f"legacy file not found: {source}")
    header = legacy_header(source)
    target = TARGET / source.name
    if target.exists():
        raise SystemExit(f"refusing to overwrite existing v0.4-lite card: {target}")
    paper = str(header.get("paper", ""))
    card = f'''# Story Learning Card — {paper}\n\n## Metadata\n\n```yaml\nschema_version: "4.0-lite"\nid: {header.get("id", source.stem)}\npaper:\n  citekey: null\n  title: {json_string(paper)}\n  outlet: null\n  year: null\n  publication_status: unverified\n  paper_type: quantitative\n  source_version: unknown\n  inclusion_rationale: "Migrated for human-reviewed v0.4-lite reading"\nreading_scope:\n  sections_read: {header.get("distilled_sections", [])}\n  coverage: partial\n  source_records: {header.get("source_records", [])}\nclassification:\n  theoretical_problem_form: []\n  narrative_dynamics: []\n  confidence: provisional\nsection_learning:\n  introduction: {{suitable: no, learn: [], caveat: []}}\n  theory: {{suitable: no, learn: [], caveat: []}}\n  methods: {{suitable: no, learn: [], caveat: []}}\n  results: {{suitable: no, learn: [], caveat: []}}\n  discussion: {{suitable: no, learn: [], caveat: []}}\nstory_assessment:\n  overall_role: descriptive_only\n  mode: single_read\n```\n\n## Story Reading\n\n### Theme question\n\nTODO: reconstruct from a new whole-paper reading.\n\n### Whole-story synopsis\n\nTODO: write a continuous whole-paper synopsis; do not copy the legacy labels as an assessment.\n\n### Characters and storylines\n\nTODO\n\n### Five acts\n\nTODO\n\n## Story Assessment\n\nTODO: assess storytelling only after completing the descriptive reading.\n\n## Learning Affordances\n\nTODO: add only section-specific moves that pass human review.\n'''
    card = card.replace("paper_type: quantitative", f"paper_type: {header.get('paper_type', 'unknown')}")
    card = card.replace("suitable: no", 'suitable: "no"')
    target.write_text(card, encoding="utf-8")
    print(f"created review stub: {target}")
    return 0


def json_string(value: str) -> str:
    import json
    return json.dumps(value, ensure_ascii=False)


if __name__ == "__main__":
    raise SystemExit(main())
