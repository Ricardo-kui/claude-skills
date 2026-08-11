#!/usr/bin/env python3
"""Prepare and score blind legacy/indexed forward tests for the R2 pilot."""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
from pathlib import Path
from typing import Any

import yaml


SKILL_ROOT = Path(__file__).resolve().parent.parent
# 治理副本位于 _governance/ 下；盲测 prompt 里注明的被测 skill 路径必须指向 live 技能本体。
# 默认推导：skills_root/_governance/write-results/scripts/x.py → parents[3]=skills_root → write-results。
# 可用环境变量 WRITE_RESULTS_ROOT 覆盖。
import os
LIVE_SKILL_ROOT = Path(os.environ.get(
    "WRITE_RESULTS_ROOT",
    Path(__file__).resolve().parents[3] / "write-results",
))
PROMPTS_PATH = SKILL_ROOT / "tests" / "r2_forward_prompts.yaml"
GOLD_PATH = SKILL_ROOT / "tests" / "r2_forward_gold.yaml"
INDEX_PATH = SKILL_ROOT / "econometric-models" / "_pilot_r2_index.yaml"
ROUTING_RE = re.compile(r"^ROUTING_JSON:\s*(\{.*\})\s*$", re.MULTILINE)
OUTPUT_MARKER = "R2_OUTPUT:"


class BenchmarkError(ValueError):
    """Raised when a benchmark artifact would compromise the blind test."""


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise BenchmarkError(f"Expected YAML mapping: {path}")
    return data


def prompt_cases() -> list[dict[str, str]]:
    data = load_yaml(PROMPTS_PATH)
    cases = data.get("cases")
    if not isinstance(cases, list):
        raise BenchmarkError("prompts cases must be a list")
    return cases


def validate_benchmark() -> list[str]:
    errors: list[str] = []
    prompts = load_yaml(PROMPTS_PATH)
    gold = load_yaml(GOLD_PATH)
    index = load_yaml(INDEX_PATH)
    cases = prompts.get("cases") or []
    prompt_ids = [case.get("case_id") for case in cases]
    if len(prompt_ids) != len(set(prompt_ids)):
        errors.append("prompt case_id values must be unique")
    if set(prompt_ids) != set((gold.get("cases") or {}).keys()):
        errors.append("prompt and gold case IDs differ")
    index_assets = {asset.get("asset_id") for asset in index.get("assets") or []}
    if set(gold.get("assets") or []) != index_assets:
        errors.append("gold asset inventory differs from pilot index")
    for case in cases:
        task = str(case.get("task") or "").strip()
        if not task:
            errors.append(f"empty task: {case.get('case_id')}")
        leaked = sorted(asset for asset in index_assets if asset and asset in task)
        if leaked:
            errors.append(f"asset IDs leaked in prompt {case.get('case_id')}: {leaked}")
    for case_id, expected in (gold.get("cases") or {}).items():
        if expected.get("expected_first_asset") not in index_assets:
            errors.append(f"unknown expected asset for {case_id}")
        unknown_forbidden = set(expected.get("forbidden_assets") or []) - index_assets
        if unknown_forbidden:
            errors.append(f"unknown forbidden assets for {case_id}: {sorted(unknown_forbidden)}")
    return errors


def opaque_run_id(case_id: str, arm: str, seed: int) -> str:
    raw = f"{seed}:{case_id}:{arm}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:12]


def indexed_instruction(task: str) -> str:
    return f"""Use the write-results skill at {LIVE_SKILL_ROOT} to complete the task below.
This is an opt-in shadow test for results.R2.OLS_FE. Do not read files under tests/.
First run `python -X utf8 scripts/select_r2_pilot.py --list-features`.
Choose the minimum listed canonical tags or aliases justified by the task; do not invent tags. Then run:
python -X utf8 scripts/select_r2_pilot.py --features <your feature tags> --render
Use only the returned pilot assets plus the task facts. Do not load the full OLS-FE.md.
Do not invent coefficients or significance. Preserve the evidence-status boundary.

Return exactly:
ROUTING_JSON: {{"features": ["..."], "selected_asset_ids": ["..."]}}
R2_OUTPUT:
<one publishable R2 navigation paragraph>

Task:
{task}
"""


def legacy_instruction(task: str) -> str:
    return f"""Use the write-results skill at {LIVE_SKILL_ROOT} to complete the task below.
Use the current legacy loading instructions. Do not read files under tests/ or the pilot sidecar index.
Load the normal R2 slot resource and legacy OLS-FE corpus as the skill currently requires.
Do not invent coefficients or significance.

Return exactly:
R2_OUTPUT:
<one publishable R2 navigation paragraph>

Task:
{task}
"""


def emit_manifest(seed: int) -> dict[str, Any]:
    runs: list[dict[str, str]] = []
    for case in prompt_cases():
        case_id = case["case_id"]
        task = case["task"]
        runs.extend(
            [
                {
                    "run_id": opaque_run_id(case_id, "indexed", seed),
                    "case_id": case_id,
                    "arm": "indexed",
                    "request": indexed_instruction(task),
                },
                {
                    "run_id": opaque_run_id(case_id, "legacy", seed),
                    "case_id": case_id,
                    "arm": "legacy",
                    "request": legacy_instruction(task),
                },
            ]
        )
    random.Random(seed).shuffle(runs)
    return {"schema_version": "0.1.0-pilot", "seed": seed, "runs": runs}


def load_responses(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("responses") if isinstance(data, dict) else None
    if not isinstance(rows, list):
        raise BenchmarkError("responses JSON must contain a responses list")
    result: dict[str, str] = {}
    for row in rows:
        run_id = row.get("run_id")
        response = row.get("response")
        if not isinstance(run_id, str) or not isinstance(response, str):
            raise BenchmarkError("each response requires string run_id and response")
        if run_id in result:
            raise BenchmarkError(f"duplicate response run_id: {run_id}")
        result[run_id] = response
    return result


def output_body(response: str) -> str:
    if OUTPUT_MARKER not in response:
        raise BenchmarkError("response is missing R2_OUTPUT marker")
    return response.split(OUTPUT_MARKER, 1)[1].strip()


def routing_metadata(response: str) -> dict[str, Any]:
    match = ROUTING_RE.search(response)
    if not match:
        raise BenchmarkError("indexed response is missing ROUTING_JSON")
    data = json.loads(match.group(1))
    if not isinstance(data.get("features"), list) or not isinstance(data.get("selected_asset_ids"), list):
        raise BenchmarkError("ROUTING_JSON requires features and selected_asset_ids lists")
    return data


def evaluate_routes(manifest: dict[str, Any], responses: dict[str, str]) -> dict[str, Any]:
    gold = load_yaml(GOLD_PATH)["cases"]
    rows: list[dict[str, Any]] = []
    for run in manifest["runs"]:
        if run["arm"] != "indexed":
            continue
        response = responses.get(run["run_id"])
        if response is None:
            rows.append({"case_id": run["case_id"], "passed": False, "error": "missing response"})
            continue
        try:
            route = routing_metadata(response)
            selected = route["selected_asset_ids"]
            expected = gold[run["case_id"]]
            first_ok = bool(selected) and selected[0] == expected["expected_first_asset"]
            forbidden_ok = not (set(selected) & set(expected.get("forbidden_assets") or []))
            rows.append(
                {
                    "case_id": run["case_id"],
                    "passed": first_ok and forbidden_ok,
                    "expected_first_asset": expected["expected_first_asset"],
                    "selected_asset_ids": selected,
                    "forbidden_assets_present": sorted(
                        set(selected) & set(expected.get("forbidden_assets") or [])
                    ),
                }
            )
        except (BenchmarkError, json.JSONDecodeError) as exc:
            rows.append({"case_id": run["case_id"], "passed": False, "error": str(exc)})
    passed = sum(bool(row["passed"]) for row in rows)
    return {"passed": passed, "total": len(rows), "accuracy": passed / len(rows) if rows else 0, "cases": rows}


def blind_eval_bundle(manifest: dict[str, Any], responses: dict[str, str], seed: int) -> dict[str, Any]:
    by_case: dict[str, dict[str, dict[str, str]]] = {}
    for run in manifest["runs"]:
        response = responses.get(run["run_id"])
        if response is None:
            raise BenchmarkError(f"missing response for run {run['run_id']}")
        by_case.setdefault(run["case_id"], {})[run["arm"]] = {
            "run_id": run["run_id"],
            "body": output_body(response),
        }
    pairs: list[dict[str, Any]] = []
    rng = random.Random(seed)
    for case_id in sorted(by_case):
        arms = by_case[case_id]
        if set(arms) != {"legacy", "indexed"}:
            raise BenchmarkError(f"incomplete pair: {case_id}")
        ordered = [arms["legacy"], arms["indexed"]]
        rng.shuffle(ordered)
        pairs.append(
            {
                "case_id": case_id,
                "candidate_a": ordered[0]["body"],
                "candidate_b": ordered[1]["body"],
                "rubric": {
                    "routing_and_task_fit": "0-2",
                    "audit_genre_navigation": "0-2",
                    "no_premature_results_interpretation": "0-2",
                    "methodological_honesty": "0-2",
                    "clarity_and_concision": "0-2",
                    "critical_error": "true/false",
                    "preference": "A/B/tie",
                },
            }
        )
    return {"schema_version": "0.1.0-pilot", "pairs": pairs}


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    emit = sub.add_parser("emit")
    emit.add_argument("--seed", type=int, default=20260806)
    routes = sub.add_parser("score-routes")
    routes.add_argument("responses", type=Path)
    routes.add_argument("--seed", type=int, default=20260806)
    blind = sub.add_parser("blind-bundle")
    blind.add_argument("responses", type=Path)
    blind.add_argument("--seed", type=int, default=20260806)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_benchmark()
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    if args.command == "validate":
        print(json.dumps({"valid": True, "cases": len(prompt_cases())}, ensure_ascii=False, indent=2))
        return 0
    manifest = emit_manifest(args.seed)
    if args.command == "emit":
        print(json.dumps(manifest, ensure_ascii=False, indent=2))
        return 0
    responses = load_responses(args.responses)
    if args.command == "score-routes":
        print(json.dumps(evaluate_routes(manifest, responses), ensure_ascii=False, indent=2))
        return 0
    if args.command == "blind-bundle":
        print(json.dumps(blind_eval_bundle(manifest, responses, args.seed), ensure_ascii=False, indent=2))
        return 0
    raise BenchmarkError(f"unsupported command: {args.command}")


if __name__ == "__main__":
    sys.exit(main())
