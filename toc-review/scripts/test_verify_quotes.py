#!/usr/bin/env python3
"""Regression tests for verify_quotes.py (toc-review).

Run directly:  python test_verify_quotes.py
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

SCRIPT = Path(__file__).with_name("verify_quotes.py")

MANUSCRIPT = (
    "Baseline results are from Cox proportional hazard models (Table 3). "
    "The effect is concentrated in founder-led firms."
)

CLAIM_QUOTE = "Baseline results are from Cox proportional hazard models (Table 3)."
CITATION_QUOTE = "The effect is concentrated in founder-led firms."
FABRICATED = "Fabricated counterquote."


def run_verifier(records, manuscript=MANUSCRIPT):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        ms = td / "manuscript.md"
        ms.write_text(manuscript, encoding="utf-8")
        rec = td / "records.json"
        rec.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
        env = dict(os.environ, PYTHONUTF8="1")
        proc = subprocess.run(
            [sys.executable, str(SCRIPT), str(ms), str(rec)],
            capture_output=True, text=True, encoding="utf-8", env=env)
        out = json.loads(proc.stdout) if proc.stdout.strip() else None
        return proc, out


def node(claim_quote=CLAIM_QUOTE, acknowledges=False, citation=CITATION_QUOTE):
    return {
        "node_id": "root",
        "claim": {"description": "d", "evidence_quote": claim_quote, "evidence_section": "s"},
        "advocate": {"acknowledges": acknowledges, "response": "r", "citation_quote": citation},
        "revision": {"revised_description": "rd", "concedes": False},
        "moderator": {"verdict": "holds", "severity": "major"},
    }


def first_node(out):
    if isinstance(out, dict) and "nodes" in out:
        return out["nodes"][0]
    return out[0] if isinstance(out[0], dict) and "claim" in out[0] else out[0]["nodes"][0]


class TestClaimAndCitation(unittest.TestCase):
    def test_all_quotes_verified_exit_0(self):
        proc, out = run_verifier([node()])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        n = first_node(out)
        self.assertTrue(n["evidence_verified"])
        self.assertTrue(n["advocate"]["citation_verified"])
        self.assertFalse(n["panel_blocked"])
        self.assertIn("claim quotes: verified 1/1", proc.stderr)
        self.assertIn("advocate citations: verified 1/1", proc.stderr)

    def test_fabricated_citation_blocks_panel(self):
        """Regression: fabricated advocate.citation_quote previously passed
        silently while the node showed verified 1/1."""
        proc, out = run_verifier([node(citation=FABRICATED)])
        self.assertEqual(proc.returncode, 1, proc.stderr)
        n = first_node(out)
        self.assertTrue(n["evidence_verified"])
        self.assertFalse(n["advocate"]["citation_verified"])
        self.assertTrue(n["panel_blocked"])
        self.assertIn("panel_blocked: 1", proc.stderr)

    def test_deflection_without_citation_blocked(self):
        proc, out = run_verifier([node(acknowledges=False, citation="")])
        self.assertEqual(proc.returncode, 1)
        n = first_node(out)
        self.assertFalse(n["advocate"]["citation_verified"])
        self.assertIn("ungrounded deflection", n["advocate"]["citation_note"])
        self.assertTrue(n["panel_blocked"])

    def test_acknowledgement_without_citation_skipped(self):
        proc, out = run_verifier([node(acknowledges=True, citation="")])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        n = first_node(out)
        self.assertNotIn("citation_verified", n["advocate"])
        self.assertFalse(n["panel_blocked"])
        self.assertIn("1 skipped", proc.stderr)

    def test_fabricated_claim_blocks_panel(self):
        proc, out = run_verifier([node(claim_quote=FABRICATED, acknowledges=True, citation="")])
        self.assertEqual(proc.returncode, 1)
        n = first_node(out)
        self.assertFalse(n["evidence_verified"])
        self.assertTrue(n["panel_blocked"])

    def test_ellipsis_claim_fails(self):
        proc, out = run_verifier(
            [node(claim_quote="Baseline results ... (Table 3).", acknowledges=True, citation="")])
        self.assertEqual(proc.returncode, 1)
        self.assertIn("ellipsis", first_node(out)["evidence_note"])

    def test_branch_return_structure(self):
        proc, out = run_verifier({"branch": "identification", "nodes": [node()], "surviving": ["root"]})
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(first_node(out)["evidence_verified"])

    def test_zero_nodes_fail_closed(self):
        proc, _ = run_verifier([])
        self.assertEqual(proc.returncode, 2)
        self.assertIn("no nodes found", proc.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
