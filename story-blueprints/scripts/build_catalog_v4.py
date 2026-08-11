"""Build the non-authoritative runtime catalog for v0.4-lite story cards."""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CARDS = ROOT / "v4" / "blueprints"
CATALOG = ROOT / "v4" / "catalog.json"


def read_metadata(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"## Metadata\s+```yaml\s*(.*?)```", text, re.S)
    if not match:
        raise ValueError(f"{path.name}: missing Metadata YAML block")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError(f"{path.name}: Metadata YAML is not a mapping")
    return data


def main() -> int:
    entries = []
    for path in sorted(CARDS.glob("*.md")):
        data = read_metadata(path)
        paper = data.get("paper", {})
        scope = data.get("reading_scope", {})
        classification = data.get("classification", {})
        assessment = data.get("story_assessment", {})
        entries.append({
            "id": data.get("id"),
            "path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "paper_type": paper.get("paper_type"),
            "outlet": paper.get("outlet"),
            "publication_status": paper.get("publication_status"),
            "coverage": scope.get("coverage"),
            "theoretical_problem_form": classification.get("theoretical_problem_form", []),
            "narrative_dynamics": classification.get("narrative_dynamics", []),
            "retrieval_signals": classification.get("retrieval_signals", []),
            "section_learning": data.get("section_learning", {}),
            "overall_role": assessment.get("overall_role"),
        })
    CATALOG.write_text(json.dumps({"schema_version": "4.0-lite-catalog", "cards": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"catalog built: {len(entries)} cards -> {CATALOG}")


if __name__ == "__main__":
    main()
