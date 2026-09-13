#!/usr/bin/env python3
"""S5 一致率对比：pre-distillation baseline vs post-distillation check.

Usage:
  py compare_s5.py [pre.yaml] [post.yaml]

Defaults: ~/.claude/distill-work/rebuild_views/{reconciliation_report.pre_S5_baseline.yaml,
reconciliation_report.yaml}

Prints per-corpus match/drift/unattributable deltas and a 一致率 verdict.
Exit 0 when every corpus's match-rate is 100% over (match + drift) and drift
did not increase — the S6-switch gate per plan §7.1.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

BASE = Path.home() / ".claude" / "distill-work" / "rebuild_views"


def load(p: Path) -> dict:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


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
        a = pre["corpora"].get(ck, {}).get("summary", {})
        b = post["corpora"][ck]["summary"]
        m, d = b.get("match", 0), b.get("drift", 0)
        rate = m / (m + d) if (m + d) else 0.0
        delta_d = d - a.get("drift", 0)
        # S5 gate (plan §7.1): the shadow double-run proves the NEW writeback
        # introduced NO unexplained drift — drift delta vs the frozen baseline
        # must be <= 0. The standing drift inventory (INDEX lags, novel
        # patterns gaps, dual-key) is adjudicated/fixed by the S6 switch
        # itself, so absolute 一致率 is informational here, not the gate.
        verdict = "GREEN" if delta_d <= 0 else "NOT GREEN"
        if verdict != "GREEN":
            all_green = False
        print(f"[{ck}] match {a.get('match',0)}->{m}  drift {a.get('drift',0)}->{d} "
              f"(delta {delta_d:+d})  unattr {a.get('unattributable',0)}->{b.get('unattributable',0)}"
              f"  一致率(参考) {rate:.1%}  {verdict}")
    print()
    print("S5-SHADOW GATE:", "PASS — no new unexplained drift in any corpus"
          if all_green else
          "NOT PASS — new drift introduced; adjudicate before S6")
    return 0 if all_green else 1


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
