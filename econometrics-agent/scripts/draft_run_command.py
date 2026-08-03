#!/usr/bin/env python3
"""Generate a draft econometrics-agent run command from inspection JSON or data."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from inspect_dataset import build_payload, load_data

MODELS = [
    "auto",
    "ols",
    "fe",
    "iv",
    "did",
    "event-study",
    "psm",
    "ipw",
    "aipw",
    "ipwra",
    "rdd",
    "fuzzy-rdd",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a draft econometrics-agent run command from inspection JSON or directly from a data file.")
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument("--inspection", help="Path to inspection JSON emitted by inspect_dataset.py or inspect_dataset.ps1.")
    source_group.add_argument("--data", help="Path to csv, dta, parquet, xlsx, or xls data for one-step inspection plus draft generation.")
    parser.add_argument("--sheet-name", help="Optional Excel sheet name when --data is used.")
    parser.add_argument("--preview-rows", type=int, default=5)
    parser.add_argument("--sample-values", type=int, default=5)
    parser.add_argument("--max-columns", type=int, default=200)
    parser.add_argument("--model", choices=MODELS, default="auto")
    parser.add_argument("--query")
    parser.add_argument("--outcome")
    parser.add_argument("--treatment")
    parser.add_argument("--controls", nargs="*")
    parser.add_argument("--entity-id")
    parser.add_argument("--time-id")
    parser.add_argument("--instrument")
    parser.add_argument("--weights")
    parser.add_argument("--cluster")
    parser.add_argument("--cov-type")
    parser.add_argument("--treat-group")
    parser.add_argument("--post")
    parser.add_argument("--running-variable")
    parser.add_argument("--cutoff")
    parser.add_argument("--bandwidth")
    parser.add_argument("--kernel")
    parser.add_argument("--rdd-mode")
    parser.add_argument("--poly-order")
    parser.add_argument("--estimand")
    parser.add_argument("--lead-window")
    parser.add_argument("--lag-window")
    parser.add_argument("--format", choices=["powershell", "json"], default="powershell")
    return parser.parse_args()


def load_inspection(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def load_payload(args: argparse.Namespace) -> tuple[dict[str, Any], list[str]]:
    if args.inspection:
        inspection_path = Path(args.inspection).expanduser().resolve()
        return load_inspection(inspection_path), []
    data_path = Path(args.data).expanduser().resolve()
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")
    dataframe = load_data(data_path, args.sheet_name)
    payload = build_payload(
        data_path,
        dataframe,
        args.preview_rows,
        args.sample_values,
        args.max_columns,
    )
    return payload, ["Inspection payload was generated directly from the data file."]


def is_numeric_dtype(dtype: str) -> bool:
    lower = dtype.lower()
    return any(token in lower for token in ("int", "float", "double", "decimal"))


def quote_ps(value: str) -> str:
    return '"' + value.replace("`", "``").replace('"', '`"') + '"'


def default_query(model: str) -> str:
    mapping = {
        "auto": "estimate the main effect",
        "ols": "estimate the baseline effect",
        "fe": "estimate the effect with entity and time fixed effects",
        "iv": "estimate the endogenous treatment effect with IV-2SLS",
        "did": "estimate the policy effect with difference in differences",
        "event-study": "run an event study and inspect pre-trends",
        "psm": "estimate the treatment effect with propensity score matching",
        "ipw": "estimate the treatment effect with inverse probability weighting",
        "aipw": "estimate the treatment effect with doubly robust augmented IPW",
        "ipwra": "estimate the treatment effect with IPW regression adjustment",
        "rdd": "run a sharp RDD around the score cutoff",
        "fuzzy-rdd": "run a fuzzy RDD around the score cutoff",
    }
    return mapping[model]


def choose_first(candidates: list[str], exclude: set[str]) -> str | None:
    for candidate in candidates:
        if candidate not in exclude:
            return candidate
    return None


def choose_named(columns: list[str], exclude: set[str], exact: list[str], contains: list[str]) -> str | None:
    lower_map = {column.lower(): column for column in columns if column not in exclude}
    for key in exact:
        if key in lower_map:
            return lower_map[key]
    for column in columns:
        if column in exclude:
            continue
        lower = column.lower()
        if any(token in lower for token in contains):
            return column
    return None


def choose_outcome(columns: list[str], profiles: dict[str, dict[str, Any]], exclude: set[str]) -> str | None:
    numeric = [
        column
        for column in columns
        if column not in exclude
        and is_numeric_dtype(profiles.get(column, {}).get("dtype", ""))
        and int(profiles.get(column, {}).get("unique_non_null", 0)) > 2
    ]
    return choose_first(numeric, set())


def choose_controls(columns: list[str], profiles: dict[str, dict[str, Any]], exclude: set[str]) -> list[str]:
    controls: list[str] = []
    for column in columns:
        if column in exclude:
            continue
        if not is_numeric_dtype(profiles.get(column, {}).get("dtype", "")):
            continue
        if int(profiles.get(column, {}).get("unique_non_null", 0)) <= 2:
            continue
        controls.append(column)
        if len(controls) == 3:
            break
    return controls


def placeholder(name: str) -> str:
    return f"<{name}>"


def infer_spec(payload: dict[str, Any], args: argparse.Namespace) -> tuple[dict[str, Any], list[str]]:
    columns = [str(column) for column in payload.get("column_names", [])]
    profiles = {
        str(profile["name"]): profile
        for profile in payload.get("column_profiles", [])
        if isinstance(profile, dict) and "name" in profile
    }
    id_candidates = [str(value) for value in payload.get("id_candidates", [])]
    time_candidates = [str(value) for value in payload.get("time_candidates", [])]
    binary_candidates = [str(value) for value in payload.get("binary_candidates", [])]
    notes: list[str] = []

    spec: dict[str, Any] = {
        "data": str(payload.get("data_path", "")),
        "model": args.model,
        "query": args.query or default_query(args.model),
    }

    excluded = set(id_candidates) | set(time_candidates)

    outcome = args.outcome or choose_outcome(columns, profiles, excluded | set(binary_candidates))
    if outcome is None:
        outcome = placeholder("outcome")
        notes.append("Outcome could not be inferred; replace <outcome> before running.")
    elif args.outcome is None:
        notes.append(f"Outcome was auto-filled from inspection data: {outcome}")
    spec["outcome"] = outcome

    treatment_exclude = excluded | {outcome}
    treatment = args.treatment or choose_first(binary_candidates, treatment_exclude)
    if treatment is None:
        treatment = placeholder("treatment")
        notes.append("Treatment could not be inferred; replace <treatment> before running.")
    elif args.treatment is None:
        notes.append(f"Treatment was auto-filled from binary candidates: {treatment}")
    spec["treatment"] = treatment

    control_exclude = excluded | {outcome, treatment}
    controls = args.controls if args.controls is not None else choose_controls(columns, profiles, control_exclude)
    if args.controls is None and controls:
        notes.append(f"Controls were auto-filled as a first-pass numeric set: {', '.join(controls)}")
    spec["controls"] = controls

    if args.model in {"fe", "did", "event-study"}:
        entity_id = args.entity_id or choose_first(id_candidates, {outcome, treatment})
        time_id = args.time_id or choose_first(time_candidates, {outcome, treatment, entity_id or ""})
        if entity_id is None:
            entity_id = placeholder("entity_id")
            notes.append("Entity id could not be inferred for the selected panel-style model.")
        elif args.entity_id is None:
            notes.append(f"Entity id was auto-filled from id candidates: {entity_id}")
        if time_id is None:
            time_id = placeholder("time_id")
            notes.append("Time id could not be inferred for the selected panel-style model.")
        elif args.time_id is None:
            notes.append(f"Time id was auto-filled from time candidates: {time_id}")
        spec["entity_id"] = entity_id
        spec["time_id"] = time_id

    if args.model == "did":
        did_exclude = {outcome, treatment, spec.get("entity_id", ""), spec.get("time_id", "")}
        treat_group = args.treat_group or choose_named(columns, did_exclude, ["treat_group", "treated_group", "treated_firm", "ever_treated"], ["treat_group", "treated_group", "ever_treated"])
        post = args.post or choose_named(columns, did_exclude | {treat_group or ""}, ["post", "post_policy", "post_treatment"], ["post", "after"])
        if treat_group is None:
            treat_group = placeholder("treat_group")
            notes.append("Treat-group could not be inferred for DID.")
        elif args.treat_group is None:
            notes.append(f"Treat-group was auto-filled from named candidates: {treat_group}")
        if post is None:
            post = placeholder("post")
            notes.append("Post-period indicator could not be inferred for DID.")
        elif args.post is None:
            notes.append(f"Post indicator was auto-filled from named candidates: {post}")
        if treatment in {treat_group, post}:
            spec["treatment"] = placeholder("treatment")
            notes.append("Treatment overlapped with DID helper columns; replace <treatment> with the actual interaction or treatment indicator.")
        spec["treat_group"] = treat_group
        spec["post"] = post

    if args.model == "iv":
        instrument = args.instrument or choose_named(columns, {outcome, treatment}, ["z", "instrument", "instr", "iv"], ["instrument", "instr"])
        if instrument is None:
            instrument = placeholder("instrument")
            notes.append("Instrument could not be inferred for IV.")
        elif args.instrument is None:
            notes.append(f"Instrument was auto-filled from named candidates: {instrument}")
        spec["instrument"] = instrument

    if args.model in {"rdd", "fuzzy-rdd"}:
        running_variable = args.running_variable or choose_named(columns, {outcome, treatment}, ["score", "running_variable", "running", "forcing"], ["score", "running", "forcing", "assignment"])
        if running_variable is None:
            running_variable = placeholder("running_variable")
            notes.append("Running variable could not be inferred for the selected RDD model.")
        elif args.running_variable is None:
            notes.append(f"Running variable was auto-filled from named candidates: {running_variable}")
        spec["running_variable"] = running_variable
        spec["cutoff"] = args.cutoff or placeholder("cutoff")
        if args.cutoff is None:
            notes.append("Cutoff was not inferred; replace <cutoff> with the actual threshold.")
        if args.bandwidth:
            spec["bandwidth"] = args.bandwidth
        if args.kernel:
            spec["kernel"] = args.kernel
        if args.rdd_mode:
            spec["rdd_mode"] = args.rdd_mode
        if args.poly_order:
            spec["poly_order"] = args.poly_order

    if args.model in {"psm", "ipw", "aipw", "ipwra"} and args.estimand:
        spec["estimand"] = args.estimand

    if args.model == "event-study":
        if args.lead_window:
            spec["lead_window"] = args.lead_window
        if args.lag_window:
            spec["lag_window"] = args.lag_window

    for key in ["weights", "cluster", "cov_type"]:
        value = getattr(args, key)
        if value:
            spec[key] = value

    if args.model == "auto" and id_candidates and time_candidates:
        notes.append(f"Panel-style candidates are available if needed later: entity-id={id_candidates[0]}, time-id={time_candidates[0]}")

    return spec, notes


def command_pairs(spec: dict[str, Any]) -> list[tuple[str, list[str]]]:
    pairs: list[tuple[str, list[str]]] = [
        ("--data", [spec["data"]]),
        ("--query", [spec["query"]]),
        ("--outcome", [spec["outcome"]]),
        ("--treatment", [spec["treatment"]]),
    ]
    if spec.get("controls"):
        pairs.append(("--controls", list(spec["controls"])))
    if spec.get("model") and spec["model"] != "auto":
        pairs.append(("--model", [spec["model"]]))
    for key, flag in [
        ("entity_id", "--entity-id"),
        ("time_id", "--time-id"),
        ("instrument", "--instrument"),
        ("weights", "--weights"),
        ("cluster", "--cluster"),
        ("cov_type", "--cov-type"),
        ("treat_group", "--treat-group"),
        ("post", "--post"),
        ("running_variable", "--running-variable"),
        ("cutoff", "--cutoff"),
        ("bandwidth", "--bandwidth"),
        ("kernel", "--kernel"),
        ("rdd_mode", "--rdd-mode"),
        ("poly_order", "--poly-order"),
        ("estimand", "--estimand"),
        ("lead_window", "--lead-window"),
        ("lag_window", "--lag-window"),
    ]:
        value = spec.get(key)
        if value is not None:
            pairs.append((flag, [str(value)]))
    return pairs


def render_powershell(spec: dict[str, Any], notes: list[str]) -> str:
    lines: list[str] = [
        "# Draft econometrics-agent command generated from inspection JSON.",
        "# Review auto-filled fields and placeholders before running.",
    ]
    for note in notes:
        lines.append(f"# {note}")
    pairs = command_pairs(spec)
    lines.append("econometrics-agent run `")
    for index, (flag, values) in enumerate(pairs):
        rendered = " ".join([flag] + [quote_ps(value) for value in values])
        suffix = " `" if index < len(pairs) - 1 else ""
        lines.append(f"  {rendered}{suffix}")
    return "\n".join(lines)


def render_json(spec: dict[str, Any], notes: list[str]) -> str:
    payload = {
        "spec": spec,
        "notes": notes,
        "powershell_command": render_powershell(spec, notes),
    }
    return json.dumps(payload, indent=2, ensure_ascii=True)


def main() -> None:
    args = parse_args()
    payload, source_notes = load_payload(args)
    spec, notes = infer_spec(payload, args)
    notes = source_notes + notes
    if args.format == "json":
        print(render_json(spec, notes))
    else:
        print(render_powershell(spec, notes))


if __name__ == "__main__":
    main()
