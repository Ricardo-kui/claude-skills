#!/usr/bin/env python3
"""Inspect a tabular dataset for econometrics-agent command construction."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Inspect a dataset and emit a compact JSON schema summary.")
    parser.add_argument("--data", required=True, help="Absolute or relative path to csv, dta, parquet, xlsx, or xls data.")
    parser.add_argument("--sheet-name", help="Optional Excel sheet name.")
    parser.add_argument("--preview-rows", type=int, default=5)
    parser.add_argument("--sample-values", type=int, default=5)
    parser.add_argument("--max-columns", type=int, default=200)
    return parser.parse_args()


def load_data(path: Path, sheet_name: str | None) -> pd.DataFrame:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return pd.read_csv(path)
    if suffix == ".dta":
        return pd.read_stata(path, convert_categoricals=False)
    if suffix == ".parquet":
        return pd.read_parquet(path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path, sheet_name=sheet_name or 0)
    raise ValueError(f"Unsupported file format: {suffix}")


def to_jsonable(value: Any) -> Any:
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        try:
            return value.item()
        except Exception:
            pass
    if hasattr(value, "isoformat"):
        try:
            return value.isoformat()
        except Exception:
            pass
    if isinstance(value, (str, int, float, bool)) or value is None:
        return value
    return str(value)


def is_binary_like(series: pd.Series) -> bool:
    non_null = series.dropna()
    if non_null.empty:
        return False
    unique_values = set()
    for value in non_null.unique().tolist():
        normalized = to_jsonable(value)
        if isinstance(normalized, str):
            normalized = normalized.strip().lower()
        unique_values.add(normalized)
    allowed = {0, 1, 0.0, 1.0, True, False, "0", "1", "true", "false", "yes", "no"}
    return len(unique_values) <= 2 and unique_values.issubset(allowed)


def collect_sample_values(series: pd.Series, limit: int) -> list[Any]:
    values: list[Any] = []
    for value in series.dropna().head(limit).tolist():
        values.append(to_jsonable(value))
    return values


def column_profile(name: str, series: pd.Series, sample_values: int) -> dict[str, Any]:
    non_null = int(series.notna().sum())
    missing = int(series.isna().sum())
    unique_non_null = int(series.nunique(dropna=True))
    return {
        "name": name,
        "dtype": str(series.dtype),
        "non_null": non_null,
        "missing": missing,
        "unique_non_null": unique_non_null,
        "sample_values": collect_sample_values(series, sample_values),
    }


def infer_candidates(df: pd.DataFrame) -> dict[str, list[str]]:
    id_candidates: list[str] = []
    time_candidates: list[str] = []
    binary_candidates: list[str] = []
    for name in df.columns:
        lower = str(name).lower()
        if lower == "id" or lower.endswith("_id") or lower in {"firm", "firm_id", "gvkey", "permno", "permco", "company_id", "unit", "entity"}:
            id_candidates.append(str(name))
        if any(token in lower for token in ("year", "month", "date", "quarter", "time", "period")):
            time_candidates.append(str(name))
        if is_binary_like(df[name]):
            binary_candidates.append(str(name))
    return {
        "id_candidates": id_candidates,
        "time_candidates": time_candidates,
        "binary_candidates": binary_candidates,
    }


def preview_rows(df: pd.DataFrame, rows: int) -> list[dict[str, Any]]:
    preview: list[dict[str, Any]] = []
    for _, row in df.head(rows).iterrows():
        preview.append({str(col): to_jsonable(row[col]) for col in df.columns})
    return preview


def build_payload(
    path: Path,
    df: pd.DataFrame,
    preview_rows_count: int,
    sample_values_count: int,
    max_columns: int,
) -> dict[str, Any]:
    visible_columns = [str(col) for col in df.columns[:max_columns]]
    profiles = [
        column_profile(str(name), df[name], sample_values_count)
        for name in df.columns[:max_columns]
    ]
    payload: dict[str, Any] = {
        "data_path": str(path),
        "file_format": path.suffix.lower().lstrip("."),
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "column_names": visible_columns,
        "columns_truncated": len(df.columns) > max_columns,
        "preview_rows": preview_rows(df, preview_rows_count),
        "column_profiles": profiles,
    }
    payload.update(infer_candidates(df))
    return payload


def main() -> None:
    args = parse_args()
    path = Path(args.data).expanduser().resolve()
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = load_data(path, args.sheet_name)
    payload = build_payload(path, df, args.preview_rows, args.sample_values, args.max_columns)
    print(json.dumps(payload, indent=2, ensure_ascii=True))


if __name__ == "__main__":
    main()
