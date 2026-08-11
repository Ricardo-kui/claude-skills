"""Validate and freeze the paired Introduction-governance benchmark."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

import introduction_asset_catalog as catalog


SKILL_ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_PATH = SKILL_ROOT / "tests" / "fixtures" / "introduction_governance_benchmark.yaml"


def load_benchmark(path: Path = BENCHMARK_PATH) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Benchmark requires schema_version: 1")
    tasks = data.get("tasks")
    if not isinstance(tasks, list) or len(tasks) != 18:
        raise ValueError("Benchmark requires exactly 18 tasks")
    required = {"task_id", "gap_type", "conversation_strategy", "paper_type", "length", "focus_parent", "brief"}
    if any(not isinstance(row, dict) or required - set(row) for row in tasks):
        raise ValueError("Every benchmark task must contain the required fields")
    if len({row["task_id"] for row in tasks}) != len(tasks):
        raise ValueError("Benchmark task IDs must be unique")
    if {row["gap_type"] for row in tasks} != {"Incompleteness", "Inadequacy", "Incommensurability"}:
        raise ValueError("Benchmark must cover all Gap types")
    if {row["conversation_strategy"] for row in tasks} != {"Progressive_Coherence", "Synthesized_Coherence", "Non_Coherence"}:
        raise ValueError("Benchmark must cover all Conversation strategies")
    if {row["paper_type"] for row in tasks} != {"quantitative", "qualitative", "theory"}:
        raise ValueError("Benchmark must cover all paper types")
    focus = Counter(row["focus_parent"] for row in tasks)
    if any(focus[parent] < 3 for parent in set(focus)) or len(focus) != 5:
        raise ValueError("Benchmark must trigger each of five dense families at least three times")
    parents, _, _ = catalog.load_catalog()
    active = {item.asset_id for item in parents if item.lifecycle == "active"}
    missing = sorted(set(focus) - active)
    if missing:
        raise ValueError("Benchmark refers to inactive or unknown parents: " + ", ".join(missing))
    return data


def snapshot(path: Path = BENCHMARK_PATH) -> dict:
    data = load_benchmark(path)
    corpus = SKILL_ROOT / "academic-writing-corpus"
    digest = hashlib.sha256()
    for item in sorted(corpus.rglob("*")):
        if item.is_file() and item.suffix in {".md", ".yaml"}:
            digest.update(item.relative_to(corpus).as_posix().encode("utf-8"))
            digest.update(item.read_bytes())
    parents, variants, _ = catalog.load_catalog()
    return {
        "seed": data["seed"],
        "benchmark_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "corpus_sha256": digest.hexdigest(),
        "parent_assets": len(parents),
        "variant_assets": len(variants),
        "task_ids": [row["task_id"] for row in data["tasks"]],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot", action="store_true")
    args = parser.parse_args()
    payload = snapshot() if args.snapshot else {"validated": True, "tasks": len(load_benchmark()["tasks"])}
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
