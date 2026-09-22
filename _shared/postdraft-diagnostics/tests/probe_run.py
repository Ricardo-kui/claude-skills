#!/usr/bin/env python3
"""Probe runner + scorer v1 — 阶段② recall measurement.

For every manifest entry: run analyze.py on the probe doc (expected flag on
the mutated target sentence) and on the control twin (expected 0 flags;
context-contamination detector). M6's control is the same doc under
ols_fe (T_CAUSAL_EFFECT not conditional there) with expected PASS.

Verdicts per probe:
  HIT            expected flag type found on target sentence
  MISS           no flag on target
  MISCLASS       flag on target but different type
  CONTAMINATED   control flagged (pair excluded from denominators)
  FALSE_POSITIVE expected PASS but target flagged

Usage: python probe_run.py [--out probe_results_v1.json]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
PKG = HERE.parent
ANALYZE = PKG / "analyze.py"
WL = json.loads((PKG / "wordlists-v1.json").read_text(encoding="utf-8"))

def run(doc: Path, design: str) -> dict:
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    p = subprocess.run([sys.executable, str(ANALYZE), str(doc), "--design", design, "--json"],
                       capture_output=True, text=True, encoding="utf-8", env=env, timeout=120)
    if p.returncode != 0:
        return {"error": p.stderr.strip()[:300], "flag_count": -1, "flags": []}
    return json.loads(p.stdout)

def on_target(flag: dict, target: str) -> bool:
    fs = flag.get("sentence", "")
    return fs == target or fs.startswith(target[:80]) or target.startswith(fs[:80])

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE / "probe_results_v1.json"))
    args = ap.parse_args()

    manifest = json.loads((HERE / "probes_v1" / "manifest.json").read_text(encoding="utf-8"))
    results = []
    for e in manifest:
        design = e["design"]
        probe = run(HERE / e["doc"], design)
        ctrl_design = e.get("control_design", design)
        ctrl = run(HERE / e["control"], ctrl_design)
        ctrl_expected = e.get("control_expected", "PASS")
        ctrl_ok = (ctrl.get("flag_count") == 0) if ctrl_expected == "PASS" else True
        target_flags = [f for f in probe.get("flags", []) if on_target(f, e["mutated"])]
        other_flags = [f for f in probe.get("flags", []) if not on_target(f, e["mutated"])]
        types = sorted({f["type"] for f in target_flags})
        reclass = e.get("reclassified_to") == "PASS"
        exp = "PASS" if reclass else e["expected"]
        if not ctrl_ok:
            verdict = "CONTAMINATED"
        elif exp == "PASS":
            verdict = "HIT" if not target_flags else ("ADJUDICATED_FP" if reclass else "FALSE_POSITIVE")
        elif exp in types:
            verdict = "HIT"
        elif target_flags:
            verdict = "MISCLASS"
        else:
            verdict = "MISS"
        results.append({
            "id": e["id"], "class": e["class"], "design": design, "expected": exp,
            "reclassified": e.get("reclassified_to") == "PASS",
            "adjudication_reason": e.get("adjudication_reason", ""),
            "verdict": verdict, "flag_types": types,
            "extra_flags_on_others": len(other_flags),
            "control_flags": ctrl.get("flag_count", -1),
            "control_detail": ctrl.get("flags", [])[:2],
            "probe_detail": [{k: f[k] for k in ("type", "tier", "match", "sentence")} for f in target_flags[:3]],
            "paper": e["paper"],
        })

    by_class = defaultdict(lambda: Counter())
    for r in results:
        if r["reclassified"]:
            by_class[r["class"]]["ADJ_CONSISTENT" if r["verdict"] == "HIT" else "ADJUDICATED_FP"] += 1
        else:
            by_class[r["class"]][r["verdict"]] += 1
    summary = {}
    for cls, c in sorted(by_class.items()):
        cls_res = [r for r in results if r["class"] == cls and not r["reclassified"] and r["expected"] != "PASS"]
        n_flagexp = sum(r["verdict"] in ("HIT", "MISS", "MISCLASS") for r in cls_res)
        n_hit_fe = sum(r["verdict"] == "HIT" for r in cls_res)
        summary[cls] = {
            "n": sum(c.values()), "n_adjudicated_nav": c.get("ADJ_CONSISTENT", 0) + c.get("ADJUDICATED_FP", 0),
            "verdicts": dict(c),
            "recall_flagexp": round(n_hit_fe / n_flagexp, 3) if n_flagexp else None,
        }
    flagexp = [r for r in results if not r["reclassified"] and r["expected"] != "PASS" and r["verdict"] in ("HIT", "MISS", "MISCLASS")]
    total_valid = len(flagexp)
    total_hit = sum(1 for r in flagexp if r["verdict"] == "HIT")
    passexp = [r for r in results if not r["reclassified"] and r["expected"] == "PASS"]
    pass_ok = sum(1 for r in passexp if r["verdict"] == "HIT")
    adj_ok = sum(1 for r in results if r["reclassified"] and r["verdict"] == "HIT")
    out = {"tool_version": WL["version"], "n_probes": len(results), "results": results,
           "by_class": summary,
           "overall_recall_flagexp": round(total_hit / total_valid, 3) if total_valid else None,
           "pass_specificity": f"{pass_ok}/{len(passexp)}",
           "adjudicated_nav_consistency": f"{adj_ok}/10",
           "note": "recall over adjudicated flag-expectation probes; 10 probes adjudicated NOT_A_VIOLATION (mutation failed to create real violation); M2b/M6-ols are PASS-expectation specificity checks"}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"{'class':5} {'n':>3} {'NAV':>3} {'HIT':>4} {'MISS':>4} {'MISC':>4} {'FP':>3} {'CONT':>4}  recall")
    for cls, s in sorted(summary.items()):
        v = s["verdicts"]
        print(f"{cls:5} {s['n']:>3} {s['n_adjudicated_nav']:>3} {v.get('HIT',0):>4} {v.get('MISS',0):>4} "
              f"{v.get('MISCLASS',0):>4} {v.get('FALSE_POSITIVE',0):>3} {v.get('CONTAMINATED',0):>4}  {s['recall_flagexp']}")
    print(f"\noverall recall (flag-expectation, adjudicated set): {out['overall_recall_flagexp']}")
    print(f"PASS specificity: {out['pass_specificity']}; adjudicated NAV consistency: {out['adjudicated_nav_consistency']}")
    for r in results:
        if r["verdict"] not in ("HIT",):
            print(f"  ! {r['id']} [{r['verdict']}] exp={r['expected']} got={r['flag_types']} "
                  f"ctrl={r['control_flags']} extra={r['extra_flags_on_others']}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
