#!/usr/bin/env python
"""Minimal executable regression for story-blueprints exemplar retrieval.

Run from anywhere:

    python story-blueprints/tests/regression_retrieval.py

It shells out to scripts/retrieve_exemplars.py (end-to-end) and asserts:

  R1. writer-side-fini-request.json's primary result is fini2017-social-valuation,
      and fini is ranked ahead of zhou2017 (zhou is not returned above fini).
  R2. writer-side-abstain-request.json conforms to the rewritten acceptance:
      results are NON-empty, every result carries validation=="unknown", and the
      script itself does not abstain (abstention is the writing skill's call).
  R3. distinct-outcomes-introduction-request.json resolves at tier 2b.
  R4. no *-request.json fixture returns an empty result set.

Exit code 0 = all assertions pass; 1 = at least one failure.
"""
from __future__ import annotations

import glob
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "retrieve_exemplars.py"
FIXTURES = ROOT / "tests" / "fixtures"

failures: list[str] = []


def retrieve(fixture: str) -> dict:
    path = FIXTURES / fixture
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--request", str(path), "--explain"],
        capture_output=True, text=True, encoding="utf-8", env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"{fixture}: retrieve_exemplars.py failed:\n{proc.stderr}")
    return json.loads(proc.stdout)


def check(condition: bool, message: str) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {message}")
    if not condition:
        failures.append(message)


def test_fini() -> None:
    print("R1 fini request -> fini2017 primary, ahead of zhou2017")
    data = retrieve("writer-side-fini-request.json")
    results = data["results"]
    ids = [r["id"] for r in results]
    check(bool(results), "fini request returns at least one result")
    check(ids and ids[0] == "fini2017-social-valuation",
          f"primary result is fini2017-social-valuation (got {ids[:1]})")
    tpf_hits = results[0]["signals_hit"]["theoretical_problem_form"] if results else []
    check("cross-audience-partial-criterion-overlap" in tpf_hits,
          f"fini tpf hit is normalized cross-audience-partial-criterion-overlap (got {tpf_hits})")
    if "zhou2017" in ids:
        check(ids.index("fini2017-social-valuation") < ids.index("zhou2017"),
              "fini2017 is ranked ahead of zhou2017")
    else:
        check(True, "zhou2017 not returned in top-2, i.e. ranked below fini2017")


def test_abstain() -> None:
    print("R2 abstain request -> non-empty, validation=unknown (script does not abstain)")
    data = retrieve("writer-side-abstain-request.json")
    results = data["results"]
    check(bool(results), "abstain request returns non-empty results")
    check(all(r["validation"] == "unknown" for r in results),
          "every abstain result carries validation=unknown")
    check("no_match" not in data, "no no_match abstention payload is emitted")


def test_distinct_outcomes() -> None:
    print("R3 distinct-outcomes request -> tier 2b")
    data = retrieve("distinct-outcomes-introduction-request.json")
    results = data["results"]
    check(bool(results), "distinct-outcomes request returns a result")
    check(results[0]["tier"] == "2b",
          f"distinct-outcomes resolves at tier 2b (got {results[0]['tier'] if results else None})")


def test_no_empty_results() -> None:
    print("R4 all fixtures -> no empty result sets")
    fixtures = sorted(glob.glob(str(FIXTURES / "*-request.json")))
    empties = []
    for fixture in fixtures:
        data = retrieve(Path(fixture).name)
        if not data["results"]:
            empties.append(Path(fixture).name)
    check(not empties, f"all {len(fixtures)} fixtures non-empty (empty: {empties})")


def main() -> int:
    for test in (test_fini, test_abstain, test_distinct_outcomes, test_no_empty_results):
        test()
    print()
    if failures:
        print(f"FAILED ({len(failures)} assertion(s)):")
        for failure in failures:
            print(f"  - {failure}")
        return 1
    print("ALL REGRESSION ASSERTIONS PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
