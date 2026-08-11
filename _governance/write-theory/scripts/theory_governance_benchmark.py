#!/usr/bin/env python3
"""Validate the pre-registered Theory governance blind-test matrix."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml


BENCHMARK = Path(__file__).resolve().parents[1] / "benchmarks" / "theory_governance" / "tasks.yaml"


def load_benchmark(path: Path = BENCHMARK) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("tasks"), list):
        raise ValueError("Benchmark requires a tasks list")
    return data


def snapshot(path: Path = BENCHMARK) -> dict:
    tasks = load_benchmark(path)["tasks"]
    ids = [row.get("id") for row in tasks]
    if len(tasks) != 24 or len(ids) != len(set(ids)):
        raise ValueError("Benchmark requires 24 unique tasks")
    architectures = Counter(row.get("architecture") for row in tasks)
    gaps = Counter(row.get("gap") for row in tasks)
    modes = Counter(row.get("mode") for row in tasks)
    if set(architectures) != set("ABCDEFG") or any(value < 3 for value in architectures.values()):
        raise ValueError("Every A-G architecture requires at least three tasks")
    if set(gaps) != {"Incompleteness", "Inadequacy", "Incommensurability"} or any(value < 7 for value in gaps.values()):
        raise ValueError("Benchmark gaps are not balanced")
    if not {"hypotheses", "propositions", "no_numbered_hypotheses"} <= set(modes):
        raise ValueError("Benchmark must cover hypotheses, propositions, and no-H tasks")
    return {"tasks": len(tasks), "architectures": dict(architectures), "gaps": dict(gaps), "modes": dict(modes)}


if __name__ == "__main__":
    print(yaml.safe_dump(snapshot(), allow_unicode=True, sort_keys=False))
