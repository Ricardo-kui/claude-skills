#!/usr/bin/env python3
"""CLI-level regression for pdm_tool.py (2026-09-14, quality-review P3).

`pdm_tool --selftest` exercises the command functions in-process; THIS script
drives the real argparse surface via subprocess — flag wiring, exit codes,
CJK argv survival (Git Bash → py → disk, adjudication ⑩), the fail/error
lifecycle (ruling ⑪), and the sweep coupling that reaps pdm_tool's rolling
.bak files (ruling ⑨ infrastructure). Hermetic: all state in a temp dir;
corpus/registries are never touched.

Exit: 0 all green / 1 failures. Run: py wbtest_pdm_tool_cli.py
"""
import io
import json
import os
import subprocess
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

import yaml

TOOL = Path(__file__).resolve().parent / "pdm_tool.py"
results = []
SUBPROC_ENV: dict = {}  # set inside the temp-dir block: FITNESS_HOME sandbox


def check(ok: bool, name: str) -> None:
    results.append((ok, name))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def run(args: list, expect: int):
    r = subprocess.run([sys.executable, str(TOOL)] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace",
                       env={**os.environ, **SUBPROC_ENV})
    if r.returncode != expect:
        print(f"  exit={r.returncode} want {expect}: pdm_tool {' '.join(args[:3])} …")
        print("  OUT:", r.stdout[-220:].replace("\n", " | "))
        print("  ERR:", r.stderr[-220:].replace("\n", " | "))
    return r


with tempfile.TemporaryDirectory() as td:
    tmp = Path(td)
    # fitness 台账沙盒（第 4 项）：present/set-gate 现在会发射 ledger 事件，
    # 全部 subprocess 必须落在临时 FITNESS_HOME，绝不写真实 ~/.claude/fitness。
    SUBPROC_ENV["FITNESS_HOME"] = str(tmp / "fitness")
    wd = tmp / "smoke.pdm"
    (wd / "sections").mkdir(parents=True)
    (wd / "feedback").mkdir()
    plan_path = wd / "plan_introduction.yaml"
    plan = {"corpus_root": str(tmp), "items": [
        {"name": "v1", "band": "gap",
         "dedup": {"verdict": "ADD",
                   "best_match": {"heading": "H", "jaccard": 0.1,
                                  "containment": 0.1}},
         "anchor": {"file": str(plan_path), "after_heading": "# T"},
         "block_text": "### 变体一：CLI 冒烟",
         "provenance": {"complete": True},
         "registry_dimension": "Mechanism"},
        {"name": "v2", "dedup": {"verdict": "SKIP",
                                 "best_match": {"heading": "旧", "jaccard": 0.5}},
         "block_text": "### 变体二"}]}
    plan_path.write_text(yaml.safe_dump(plan, allow_unicode=True), encoding="utf-8")
    l2 = tmp / "l2.yaml"
    l2.write_text(yaml.safe_dump({"gap_type": "Inadequacy", "coherence": "ok",
                                  "flags": []}, allow_unicode=True), encoding="utf-8")
    root = yaml.safe_load(f"""
pdm_version: 1.0
paper_id: "cli_smoke_2026"
title: "CLI Smoke"
status: "manifest"
source_provenance: {{section_slices: {{}}}}
distill_track:
  introduction: {{status: pending, section_json: "sections/introduction.json",
    feedback: "feedback/introduction.feedback.yaml",
    identity: {{gap_type: "", contribution_dimension: ""}},
    writeback: {{gate: awaiting_confirm, items: []}}}}
  theory: {{status: pending, section_json: "sections/theory.json",
    feedback: "feedback/theory.feedback.yaml",
    identity: {{theory_building_type: ""}}, writeback: {{gate: awaiting_confirm}}}}
  methods: {{status: pending, section_json: "sections/methods.json", writeback: {{}}}}
  results: {{status: pending, section_json: "sections/results.json", writeback: {{}}}}
cross_section_identity: {{coherence: ""}}
story_track: {{status: pending}}
feedback_ledger: {{persisted: [], missing: [], note: ""}}
""")
    rp = tmp / "smoke.pdm.yaml"
    rp.write_text(yaml.safe_dump(root, allow_unicode=True, sort_keys=False),
                  encoding="utf-8")
    (wd / "sections" / "introduction.json").write_text(json.dumps(
        {"identity": {"gap_type": "Inadequacy", "contribution_dimension": "Method"}}),
        encoding="utf-8")

    def ok_exit(r, expect):
        return r.returncode == expect

    # A. 状态机与 CLI 接线（每命令至少一次真实 subprocess）
    P = ["--pdm", str(rp)]
    r = run(["show", *P, "--format", "json"], 0)
    check(ok_exit(r, 0) and '"cli_smoke_2026"' in r.stdout, "show --format json")
    r = run(["merge-section", *P, "--section", "methods"], 3)
    check(r.returncode == 3, "merge-section json 缺失 → 3")
    r = run(["merge-section", *P, "--section", "introduction"], 0)
    check(r.returncode == 0, "merge-section 正常合并")
    r = run(["merge-section", *P, "--section", "introduction",
             "--band", "gap（CLI 中文 band 实测）"], 0)
    check(r.returncode == 0, "merge-section --band CJK")
    r = run(["set-gate", *P, "--section", "introduction", "--gate", "confirmed",
             "--plan", str(plan_path), "--note", "用户确认（中文 note 实测）"], 0)
    check(r.returncode == 0, "set-gate confirmed + plan 登记 + CJK note")
    r = run(["set-gate", *P, "--section", "introduction", "--gate", "written"], 0)
    check(r.returncode == 0, "set-gate written 级联 verified")
    r = run(["fail-section", *P, "--section", "theory", "--reason", "子代理超时（中文理由实测）"], 0)
    check(r.returncode == 0, "fail-section 记录 CJK 理由")
    r = run(["set-paper", *P, "--wb-citekey", "cli_smoke_2026_amj"], 0)
    check(r.returncode == 0, "set-paper --wb-citekey")
    r = run(["merge-cross", *P, "--from", str(l2)], 0)
    check(r.returncode == 0, "merge-cross --from")

    # B. 剩余三节合并 + written；theory 的 error 应被成功 merge 清除（裁定⑪）
    for s, ident in (("theory", {"theory_building_type": "机制"}),
                     ("methods", {"design_family": "档案",
                                  "estimator_family": "logit"}),
                     ("results", {"estimator_family": "Firth logit"})):
        (wd / "sections" / f"{s}.json").write_text(
            json.dumps({"identity": ident}), encoding="utf-8")
        run(["merge-section", *P, "--section", s], 0)
        run(["set-gate", *P, "--section", s, "--gate", "written"], 0)
    d = yaml.safe_load(rp.read_text(encoding="utf-8"))
    check("error" not in d["distill_track"]["theory"],
          "error 生命周期：成功 merge 清除先前失败记录")
    r = run(["set-paper", *P, "--status", "integrated",
             "--ledger-note", "L4 汇总注记（中文）"], 0)
    check(r.returncode == 0, "set-paper integrated + ledger-note CJK")
    r = run(["set-story", *P, "--status", "validated", "--card-path", "c.md",
             "--validated", "--catalog-rebuilt", "--fed-flags"], 0)
    check(r.returncode == 0, "set-story 全旗标")

    # C. 呈审/审计双模式（内容抽查 + 退出码语义）
    r = run(["present", *P, "--mode", "gate1", "--sections", "introduction"], 0)
    check(r.returncode == 0 and "| gap |" in r.stdout and "SKIP 明细" in r.stdout
          and "ADD 1 / EXTEND 0 / SKIP 1" in r.stdout,
          "present gate1（band 列/SKIP 明细/计数）")
    check((tmp / "fitness" / "gate1_sheets" / "smoke").is_dir()
          and "fitness: gate① 快照已存档" in r.stdout,
          "present 快照落 FITNESS_HOME 沙盒（不污染真实台账）")
    r = run(["present", *P, "--mode", "audit", "--sections", "introduction"], 4)
    check(r.returncode == 4 and "⚠0 未落盘" in r.stdout,
          "present audit 未落盘 → 4")
    d = yaml.safe_load(rp.read_text(encoding="utf-8"))
    note = d["distill_track"]["introduction"]["writeback"].get("note", "")
    band = d["distill_track"]["introduction"].get("band", "")
    ledger = d["feedback_ledger"].get("note", "")
    check("用户确认" in note and "中文 band 实测" in band and "L4 汇总" in ledger,
          "CJK argv 全程无损落盘（note/band/ledger-note）")
    b = rp.read_bytes()
    check(b.count(b"\r\n") == 0 and b.count(b"\n") > 0,
          "pdm_tool 落盘为 LF（裁定⑨归一化）")

    # D. sweep 联动：.bak 回收（integrated 删 / 活跃留 / 孤儿删）
    from preprocess_l0 import sweep
    fake_skills = tmp / "skills"
    fake_skills.mkdir()
    sw = tmp / "sw"
    sw.mkdir()
    (sw / "a.pdm.yaml").write_text("status: integrated\n", encoding="utf-8")
    (sw / "a.pdm.yaml.bak").write_text("old", encoding="utf-8")
    (sw / "b.pdm.yaml").write_text("status: distilling\n", encoding="utf-8")
    (sw / "b.pdm.yaml.bak").write_text("old", encoding="utf-8")
    (sw / "c.pdm.yaml.bak").write_text("old", encoding="utf-8")
    buf = io.StringIO()
    with redirect_stdout(buf):
        sweep(sw, fake_skills)
    log = buf.getvalue()
    check(not (sw / "a.pdm.yaml.bak").exists() and (sw / "a.pdm.yaml").exists()
          and "integrated bak" in log, "sweep 删 integrated 根的 bak、留根")
    check((sw / "b.pdm.yaml.bak").exists() and "live record" in log,
          "sweep 留活跃记录的 bak")
    check(not (sw / "c.pdm.yaml.bak").exists() and "orphan bak" in log,
          "sweep 删孤儿 bak")

failed = [n for ok, n in results if not ok]
print("-" * 60)
print(f"{'ALL GREEN' if not failed else 'FAILURES: ' + str(failed)}"
      f"  ({len(results) - len(failed)}/{len(results)})")
sys.exit(0 if not failed else 1)
