#!/usr/bin/env python3
"""S5 一致率对比：pre-distillation baseline vs post-distillation check.

Usage:
  py compare_s5.py [pre.yaml] [post.yaml]

Defaults: ~/.claude/distill-work/rebuild_views/{reconciliation_report.pre_S5_baseline.yaml,
reconciliation_report.yaml}

Prints per-corpus match/drift/unattributable deltas and a 一致率 verdict.
Exit 0 when every corpus's *unexplained* drift delta is <= 0 — the S6-switch
gate per plan §7.1. "Unexplained" = drift whose adjudication class is absent
or outside the expected_* family (novel, None, …). expected_* classes
(expected_dual_key / expected_legacy_gap / expected_status_override /
expected_counter_drift / expected_authored_passthrough / expected_derived_rebuild)
are recorded adjudications whose cleanup is the S6 switch itself.

Both snapshots are bucketed with the SAME rule set: baseline drifts predating
the expected_derived_rebuild classifier are re-bucketed by path/note shape so
the delta compares like with like (baseline frozen at S3 close is not
regenerated).
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

BASE = Path.home() / ".claude" / "distill-work" / "rebuild_views"

EXPECTED_PREFIX = "expected_"

# Baseline-era entries stored with cls="novel" that the current classifier
# buckets as expected_derived_rebuild (field DERIVED-designated per the S2
# partition contract; S6 rebuild overwrites from block truth):
#   - theory patterns entry absent despite a wb-marked block
#   - results variant skeleton text differing beyond whitespace
#   - results variant .sources lists (block-attested paper missing on disk)
def rebucket(d: dict) -> str:
    cls = str(d.get("class") or d.get("cls") or "")
    if cls == "novel":
        note = str(d.get("note") or "")
        path = str(d.get("path") or "")
        if ("incomplete derived view" in note
                or "text differs beyond whitespace" in note
                or path.endswith(".sources")
                or path.endswith("]")
                and ".skeleton_variants[" in path):
            return "expected_derived_rebuild"
    return cls


def load(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def bucket(rep: dict, ck: str) -> dict[str, int]:
    counts: dict[str, int] = {"explained": 0, "unexplained": 0}
    for d in rep["corpora"].get(ck, {}).get("drifts", []):
        cls = rebucket(d)
        if cls.startswith(EXPECTED_PREFIX):
            counts["explained"] += 1
        else:
            counts["unexplained"] += 1
    return counts


def main() -> int:
    pre_p = Path(sys.argv[1]) if len(sys.argv) > 1 else BASE / \
        "reconciliation_report.pre_S5_baseline.yaml"
    post_p = Path(sys.argv[2]) if len(sys.argv) > 2 else BASE / \
        "reconciliation_report.yaml"
    pre, post = load(pre_p), load(post_p)
    print(f"pre : {pre_p}  ({pre['generated']})")
    print(f"post: {post_p}  ({post['generated']})")
    print()
    all_green = True
    for ck in post["corpora"]:
        a, b = pre["corpora"].get(ck, {}), post["corpora"][ck]
        sa, sb = a.get("summary", {}), b.get("summary", {})
        m, d = sb.get("match", 0), sb.get("drift", 0)
        rate = m / (m + d) if (m + d) else 0.0
        ba, bb = bucket(pre, ck), bucket(post, ck)
        du = bb["unexplained"] - ba["unexplained"]
        de = bb["explained"] - ba["explained"]
        # S5 gate (plan §7.1): the shadow double-run proves the NEW writeback
        # introduced NO unexplained drift — unexplained drift delta vs the
        # frozen baseline must be <= 0. expected_* drift is the documented S6
        # cleanup queue, reported but not gating.
        verdict = "GREEN" if du <= 0 else "NOT GREEN"
        if verdict != "GREEN":
            all_green = False
        print(f"[{ck}] match {sa.get('match',0)}->{m}  drift {sa.get('drift',0)}->{d} "
              f"(delta {d - sa.get('drift',0):+d})  unattr {sa.get('unattributable',0)}->{sb.get('unattributable',0)}"
              f"  一致率(参考) {rate:.1%}  {verdict}")
        print(f"      drift buckets: unexplained {ba['unexplained']}->{bb['unexplained']} "
              f"(delta {du:+d}, gates) | explained {ba['explained']}->{bb['explained']} "
              f"(delta {de:+d}, S6 queue)")
    print()
    print("S5-SHADOW GATE:", "PASS — no new unexplained drift in any corpus"
          if all_green else
          "NOT PASS — new unexplained drift; adjudicate before S6")
    return 0 if all_green else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
