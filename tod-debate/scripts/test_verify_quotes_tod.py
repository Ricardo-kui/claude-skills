#!/usr/bin/env python3
"""Regression tests for verify_quotes_tod.py.

Run directly:  python test_verify_quotes_tod.py
Subprocesses are forced to UTF-8 (PYTHONUTF8=1 + explicit capture encoding),
so the suite passes on a stock Windows console without env setup.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("verify_quotes_tod.py")

PAPER_A = (
    "Our staggered adoption design follows Callaway and Sant'Anna. "
    "Identification comes from variation in tariff exposure across regions."
)
PAPER_B = (
    "We study CEO turnover after product recalls. "
    "Hazard models show dismissal risk rises sharply."
)

QUOTE_A1 = "Our staggered adoption design follows Callaway and Sant'Anna."
QUOTE_A2 = "Identification comes from variation in tariff exposure across regions."
QUOTE_B1 = "We study CEO turnover after product recalls."
QUOTE_B2 = "Hazard models show dismissal risk rises sharply."
FABRICATED = "This sentence appears in neither paper at all."


def run_verifier(records, papers, *extra_args):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        args = [sys.executable, str(SCRIPT)]
        for key, text in papers.items():
            p = td / f"paper_{key}.md"
            p.write_text(text, encoding="utf-8")
            args += ["--paper", f"{key}={p}"]
        rec = td / "records.json"
        rec.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
        args.append(str(rec))
        args += list(extra_args)
        env = dict(os.environ, PYTHONUTF8="1")
        proc = subprocess.run(
            args, capture_output=True, text=True, encoding="utf-8", env=env
        )
        out = json.loads(proc.stdout) if proc.stdout.strip() else None
        return proc, out


def full_debate_records(quote_overrides=None):
    """Protocol-shaped records: root claims + rounds.{present,revise}.{A,B}
    + leaf verdicts with evidence_A/evidence_B plain strings."""
    qo = quote_overrides or {}
    return {
        "root_claims": [
            {"paper": "A", "claims": [
                {"claim_id": "A1", "title": "design", "evidence_quotes": [
                    {"quote": qo.get("root_A", QUOTE_A1), "section": "Design"}]}]},
            {"paper": "B", "claims": [
                {"claim_id": "B1", "title": "setting", "evidence_quotes": [
                    {"quote": qo.get("root_B", QUOTE_B1), "section": "Intro"}]}]},
        ],
        "nodes": [{
            "node_id": "s1", "topic": "identification",
            "rounds": [{
                "present": {
                    "A": {"argument": "ours is cleaner",
                          "evidence_quotes": [{"quote": qo.get("present_A", QUOTE_A2), "section": "ID"}]},
                    "B": {"argument": "ours is sharper",
                          "evidence_quotes": [{"quote": qo.get("present_B", QUOTE_B2), "section": "Results"}]},
                },
                "respond": {
                    "A": {"critique": "their hazard window is short"},
                    "B": {"critique": "their tariffs are aggregated"},
                },
                "revise": {
                    "A": {"revised_argument": "still distinct", "verdict_on_overlap": "distinct",
                          "evidence_quotes": [{"quote": qo.get("revise_A", QUOTE_A1), "section": "Design"}]},
                    "B": {"revised_argument": "still distinct", "verdict_on_overlap": "distinct",
                          "evidence_quotes": [{"quote": qo.get("revise_B", QUOTE_B1), "section": "Intro"}]},
                },
            }],
            "leaf_verdicts": [
                {"claims": ["A1", "B1"], "verdict": "distinct",
                 "evidence_A": [qo.get("leaf_A", QUOTE_A1)],
                 "evidence_B": [qo.get("leaf_B", QUOTE_B2)]}
            ],
        }],
    }


class TestProtocolShapes(unittest.TestCase):
    def test_rounds_structure_fully_verified(self):
        """Regression: rounds.present/revise.{A,B} + evidence_A/B must be found
        (previously reported 'verified 0/0 quotes' with exit 0)."""
        proc, out = run_verifier(full_debate_records(), {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("paper A: verified 4/4", proc.stderr)
        self.assertIn("paper B: verified 4/4", proc.stderr)
        present_a = out["nodes"][0]["rounds"][0]["present"]["A"]
        self.assertTrue(present_a["quotes_verified"])
        leaf = out["nodes"][0]["leaf_verdicts"][0]
        self.assertTrue(leaf["evidence_A_all_verified"])
        self.assertTrue(leaf["evidence_B_all_verified"])
        self.assertEqual(leaf["evidence_A_verified"], [True])

    def test_fabricated_quote_exit_1(self):
        proc, out = run_verifier(
            full_debate_records({"present_A": FABRICATED}), {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 1, proc.stderr)
        present_a = out["nodes"][0]["rounds"][0]["present"]["A"]
        self.assertFalse(present_a["quotes_verified"])
        self.assertFalse(present_a["evidence_quotes"][0]["verified"])

    def test_fabricated_leaf_string_exit_1(self):
        proc, out = run_verifier(
            full_debate_records({"leaf_B": FABRICATED}), {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 1, proc.stderr)
        leaf = out["nodes"][0]["leaf_verdicts"][0]
        self.assertEqual(leaf["evidence_B_verified"], [False])

    def test_ellipsis_fails(self):
        proc, _ = run_verifier(
            full_debate_records({"present_B": "Hazard models show ... sharply."}),
            {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 1)
        self.assertIn("ellipsis", proc.stdout)

    def test_zero_quotes_fail_closed(self):
        proc, _ = run_verifier({"nodes": []}, {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 2)
        self.assertIn("no evidence quotes", proc.stderr)

    def test_unknown_paper_key_fails(self):
        records = full_debate_records()
        records["root_claims"][0]["paper"] = "C"
        proc, _ = run_verifier(records, {"A": PAPER_A, "B": PAPER_B})
        self.assertEqual(proc.returncode, 1)
        self.assertIn("unknown paper key", proc.stdout)


class TestCliShapes(unittest.TestCase):
    def test_deprecated_papers_alias_still_works(self):
        """records.json precedes --papers (nargs='+' would swallow it)."""
        with tempfile.TemporaryDirectory() as td:
            td = Path(td)
            pa, pb = td / "a.md", td / "b.md"
            pa.write_text(PAPER_A, encoding="utf-8")
            pb.write_text(PAPER_B, encoding="utf-8")
            rec = td / "records.json"
            rec.write_text(json.dumps(full_debate_records(), ensure_ascii=False), encoding="utf-8")
            env = dict(os.environ, PYTHONUTF8="1")
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), str(rec),
                 "--papers", f"A={pa}", f"B={pb}"],
                capture_output=True, text=True, encoding="utf-8", env=env)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("paper A: verified 4/4", proc.stderr)

    def test_missing_paper_spec_is_usage_error(self):
        with tempfile.TemporaryDirectory() as td:
            rec = Path(td) / "records.json"
            rec.write_text("{}", encoding="utf-8")
            env = dict(os.environ, PYTHONUTF8="1")
            proc = subprocess.run(
                [sys.executable, str(SCRIPT), str(rec)],
                capture_output=True, text=True, encoding="utf-8", env=env)
            self.assertEqual(proc.returncode, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
