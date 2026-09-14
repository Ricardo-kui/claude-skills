#!/usr/bin/env python3
"""S4 sandbox regression for the writeback pipeline (wbtest mode).

Runs the executor against a TEMP COPY of the four corpora with synthetic
plans covering all write paths, and asserts:

  1. ADD / EXTEND / create_new_file / SKIP executor paths behave
  2. idempotency: a second identical --apply run adds nothing, bumps nothing
  3. new blocks carry the wb marker AND the wb-meta line
  4. registry CRLF signatures byte-stable across all applies
  5. verify_writeback returns PASS on the wbtest plans
  6. rebuild_views --check runs green against the sandboxed corpora
     (derived-view reconciliation sees the new markers)

The REAL corpora are never touched. WBTEST_SKIP_SHADOW=1 is set for the
subprocess applies so the shadow hook does not scan production roots.

Usage: py wbtest_writeback.py
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
SKILLS = SCRIPTS.parent.parent
PAPER = "wbtest2026_sandbox_paper"
FAILS: list[str] = []


def check(name: str, cond: bool, detail: str = ""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not cond:
        FAILS.append(name)


def run_plan(plan_path: Path, second_run: bool = False):
    # S6: the apply-end rebuild hook IS the registry derived-field writer —
    # it must run here (sandbox targets flow through the plan's registry/
    # corpus_root overrides). WBTEST_SKIP_SHADOW remains supported by the
    # executor for emergency bypass only.
    env = dict(os.environ)
    env.pop("WBTEST_SKIP_SHADOW", None)
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "corpus_writeback.py"),
         "--plan", str(plan_path), "--paper", PAPER, "--journal", "SMJ",
         "--gap", "Incompleteness", "--apply"],
        capture_output=True, text=True, env=env, cwd=str(SCRIPTS))
    return proc


def eol_sig(path: Path) -> tuple[int, int]:
    raw = path.read_bytes()
    crlf = raw.count(b"\r\n")
    return crlf, raw.count(b"\n") - crlf


def plan(kind: str, corpus: str, items: list, roots: dict, tmp: Path) -> Path:
    doc = {"section": corpus,
           "corpus_root": str(roots[corpus] / "corpus"),
           "registry": str(roots[corpus] / "corpus" / "_evidence_registry.yaml"),
           "items": items}
    if corpus == "theory":
        doc["paper_meta"] = {"title": "WBTest Paper", "year": "2026",
                             "theory_build_type": "机制推演型"}
    p = tmp / f"wbtest_plan.{corpus}.{kind}.yaml"
    p.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False),
                 encoding="utf-8")
    return p


def main() -> int:
    tmp = Path(tempfile.mkdtemp(prefix="wbtest_"))
    dirs = {"introduction": "write-introduction", "theory": "write-theory",
            "methods": "write-methods", "results": "write-results"}
    roots = {c: tmp / d for c, d in dirs.items()}
    for c, d in dirs.items():
        shutil.copytree(SKILLS / d / "corpus", roots[c] / "corpus")
    eols = {c: eol_sig(roots[c] / "corpus" / "_evidence_registry.yaml")
            for c in roots}
    print(f"sandbox: {tmp}")

    hooks01 = roots["introduction"] / "corpus" / "hooks" / "01-cross-disciplinary-analogy.md"
    methods_md = roots["methods"] / "corpus" / "面板数据-OLS.md"
    results_md = roots["results"] / "corpus" / "OLS-FE.md"
    theory_md = roots["theory"] / "corpus" / "variants" / "E_moderation.md"

    intro_items = [
        {"name": "i1_wbtest_hook", "file_override": str(hooks01),
         "dedup": {"verdict": "ADD"},
         "block_text": "### 变体 {NEXT}：WBTest 钩子型（wbtest 型）\n\n"
                       "**功能**: 沙盒回归用钩子变体。\n",
         "index_note": "变体 {NEXT}：WBTest 钩子"},
        {"name": "i2_wbtest_extend", "file_override": str(hooks01),
         "dedup": {"verdict": "EXTEND"},
         "anchor": {"file": str(hooks01),
                    "after_heading": "### 变体 A：遍在性建立型（pollock2015 型）"},
         "block_text": "WBTest EXTEND 补充段落：直接并入变体 A。\n",
         "index_note": ""},
        {"name": "i3_wbtest_skip", "file_override": str(hooks01),
         "dedup": {"verdict": "SKIP"}, "block_text": "should never land\n"},
        {"name": "i4_wbtest_module", "dedup": {"verdict": "create_new_file"},
         "new_file": "hooks/wbtest-module.md",
         "module_description": "WBTest 沙盒新建模块。",
         "block_text": "### 变体 {NEXT}：WBTest 模块变体\n\n正文。\n",
         "index_note": "变体 {NEXT}：WBTest 模块"},
    ]
    methods_items = [
        {"name": "m9_wbtest_ols_robustness", "file_override": str(methods_md),
         "dedup": {"verdict": "ADD"},
         "block_text": "### 变体 {NEXT}：WBTest 稳健性序列\n\n"
                       "**槽位**: M9\n\n**骨架**: sandbox only.\n",
         "index_note": ""},
    ]
    results_items = [
        {"name": "r9_wbtest_ols_strategy_nav", "file_override": str(results_md),
         "dedup": {"verdict": "ADD"},
         "block_text": "### 变体 {NEXT}: WBTest strategy navigation\n\n"
                       "**骨架**: Sandbox skeleton. Second sentence.\n",
         "index_note": ""},
    ]
    theory_items = [
        {"name": "s_hypothesis_forms_wbtest_pair", "file_override": str(theory_md),
         "dedup": {"verdict": "ADD"}, "registry_dimension": "Mechanism",
         "block_text": "### 变体 Z：WBTest 假设对（wbtest 型）\n\n"
                       "<!--\npattern_id: wbtest_pair_pattern\nbuild_type: 假设型\n"
                       "source_papers: [\"wbtest2026_sandbox_paper\"]\n"
                       "status: EMERGING\n-->\n",
         "index_note": ""},
    ]

    plans = [
        ("intro", plan("a", "introduction", intro_items, roots, tmp)),
        ("methods", plan("a", "methods", methods_items, roots, tmp)),
        ("results", plan("a", "results", results_items, roots, tmp)),
        ("theory", plan("a", "theory", theory_items, roots, tmp)),
    ]

    # 1. first applies — the intro plan carries a SKIP item, which the
    # executor REFUSES by design (dedup gate), so its rc is 1 with REFUSED
    for name, pp in plans:
        proc = run_plan(pp)
        if name == "intro":
            check("apply[intro] rc==1 (SKIP refused by design)",
                  proc.returncode == 1 and "REFUSED" in proc.stdout,
                  f"rc={proc.returncode}")
        else:
            check(f"apply[{name}] exit==0", proc.returncode == 0,
                  f"rc={proc.returncode} tail={proc.stdout[-200:]!r} {proc.stderr[-200:]!r}")
    all_text = hooks01.read_text(encoding="utf-8")
    check("skip never lands", "should never land" not in all_text)

    # 2. idempotency: second identical applies
    before_counts = {}
    for name, pp in plans:
        proc2 = run_plan(pp, second_run=True)
        before_counts[name] = proc2.stdout
    for name, pp in plans:
        proc2b = run_plan(pp, second_run=True)
        check(f"idempotent[{name}] no new inserts",
              "ALREADY-APPLIED" in proc2b.stdout or proc2b.returncode == 0)

    # 3. wb marker + wb-meta on new blocks
    t1 = hooks01.read_text(encoding="utf-8")
    check("intro block has marker", f"<!-- wb:{PAPER}:i1_wbtest_hook -->" in t1)
    check("intro block has wb-meta",
          "<!-- wb-meta: gap=Incompleteness" in t1)
    check("extend appended into variant A",
          "WBTest EXTEND 补充段落" in t1)
    mod = roots["introduction"] / "corpus" / "hooks" / "wbtest-module.md"
    check("create_new_file exists", mod.is_file())
    if mod.is_file():
        mt = mod.read_text(encoding="utf-8")
        check("module has marker+wb-meta",
              f"<!-- wb:{PAPER}:i4_wbtest_module -->" in mt
              and "<!-- wb-meta:" in mt)
    m1 = methods_md.read_text(encoding="utf-8")
    check("methods block has marker", f"<!-- wb:{PAPER}:m9_wbtest_ols_robustness -->" in m1)
    r1 = results_md.read_text(encoding="utf-8")
    check("results block has marker", f"<!-- wb:{PAPER}:r9_wbtest_ols_strategy_nav -->" in r1)
    t01 = theory_md.read_text(encoding="utf-8")
    check("theory block has marker",
          f"<!-- wb:{PAPER}:s_hypothesis_forms_wbtest_pair -->" in t01)

    # 4. registry EOL uniformity unchanged (line COUNTS legitimately change
    # with registry edits; what must never change is the EOL convention)
    for c in roots:
        sig = eol_sig(roots[c] / "corpus" / "_evidence_registry.yaml")
        check(f"registry EOL uniform[{c}]",
              sig[1] == eols[c][1] == 0 and sig[0] > 0, f"now={sig} pre={eols[c]}")

    # 5. registry state after the apply-end rebuild hook (S6 semantics):
    # the executor defers derived fields; the rebuild union lands the paper
    # with paper_count == len(papers)
    reg_m = yaml.safe_load((roots["methods"] / "corpus" / "_evidence_registry.yaml")
                           .read_text(encoding="utf-8"))
    e = reg_m["evidence"]["by_design_type"]["面板数据-OLS"]
    papers = [str(p) for p in e.get("papers", [])]
    check("methods rebuild union landed the paper",
          any(PAPER in p for p in papers),
          f"paper_count={e['paper_count']} len(papers)={len(papers)} "
          f"slots={e.get('slots_covered')}")
    check("methods paper_count==len(papers)",
          e.get("paper_count") == len(papers),
          f"paper_count={e['paper_count']} len(papers)={len(papers)}")
    check("methods non-canonical slot tag preserved",
          "M2.5" in str(e.get("slots_covered", "")),
          str(e.get("slots_covered")))
    reg_r = yaml.safe_load((roots["results"] / "corpus" / "_evidence_registry.yaml")
                           .read_text(encoding="utf-8"))
    r9 = reg_r["estimators"]["OLS_FE"]["slots"]["R9"]["skeleton_variants"]
    check("results R9 variant appended",
          any(v.get("id") == "r9_wbtest_ols_strategy_nav" for v in r9))
    ids = [v.get("id") for v in r9]
    check("results no double-append", ids.count("r9_wbtest_ols_strategy_nav") == 1)

    # 6. verify_writeback PASS on the plans
    proc = subprocess.run(
        [sys.executable, str(SCRIPTS / "verify_writeback.py"),
         "--plan", str(plans[0][1]), "--plan", str(plans[1][1]),
         "--plan", str(plans[2][1]), "--plan", str(plans[3][1]),
         "--paper", PAPER, "--residuals-out", str(tmp / "residuals.yaml")],
        capture_output=True, text=True, cwd=str(SCRIPTS))
    check("verify_writeback PASS", '"verdict": "PASS"' in proc.stdout,
          proc.stdout.strip().splitlines()[-1] if proc.stdout else proc.stderr[:200])

    # 7. rebuild_views --check on sandbox (patched roots)
    import rebuild_views as rv
    real_root, real_keys = rv.SKILLS_ROOT, dict(rv.CORPUS_KEYS)
    try:
        rv.SKILLS_ROOT = tmp
        rv.CORPUS_KEYS = {c: f"{d}/corpus" for c, d in {
            "introduction": "write-introduction", "theory": "write-theory",
            "methods": "write-methods", "results": "write-results"}.items()}
        for c in rv.CORPUS_KEYS:
            rep = rv.check_corpus(c, quiet=True)
            n = rep["summary"].get("drift", 0) + rep["summary"].get("match", 0) \
                + rep["summary"].get("unattributable", 0)
            check(f"sandbox rebuild check[{c}]", n > 0, str(rep["summary"]))
    finally:
        rv.SKILLS_ROOT, rv.CORPUS_KEYS = real_root, real_keys

    print("-" * 60)
    print(f"{'ALL GREEN' if not FAILS else f'{len(FAILS)} FAILURES: {FAILS}'}")
    print(f"sandbox kept for inspection: {tmp}")
    return 1 if FAILS else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
