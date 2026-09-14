#!/usr/bin/env python3
"""Fitness-ledger regression (2026-09-14, architecture item 4).

Two layers, mirroring wbtest_pdm_tool_cli.py conventions:
  in-process — ledger_home precedence, append/fail-open, item_hash,
    gate① snapshot, the full verdict-diff matrix (confirmed/edited/dropped/
    skip_endorsed/skip_flipped/added_at_gate/preauthorized_auto), written
    funnel, report generation on synthetic ledgers;
  subprocess — the real pdm_tool wiring (present snapshot + set-gate emit,
    transition-only idempotency), retrieve_exemplars logging + fail-open,
    log-consumption CLI, fitness_report CLI.

Hermetic: every write goes to a temp FITNESS_HOME; the real ~/.claude/fitness
is never touched. Exit: 0 all green / 1 failures. Run: py wbtest_fitness.py
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
PDM_TOOL = HERE / "pdm_tool.py"
REPORT = HERE / "fitness_report.py"
RETRIEVE = REPO / "story-blueprints" / "scripts" / "retrieve_exemplars.py"
results = []


def check(ok: bool, name: str) -> None:
    results.append((ok, name))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")


def run(script: Path, args: list, env_home, expect: int = 0):
    env = {**os.environ, "FITNESS_HOME": str(env_home)}
    r = subprocess.run([sys.executable, str(script)] + args,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, input=None, timeout=120)
    if r.returncode != expect:
        print(f"  exit={r.returncode} want {expect}: {script.name} {' '.join(args[:4])} …")
        print("  OUT:", r.stdout[-240:].replace("\n", " | "))
        print("  ERR:", r.stderr[-240:].replace("\n", " | "))
    return r


def read_events(home: Path, kind: str) -> list:
    p = home / "events" / f"{kind}.jsonl"
    if not p.is_file():
        return []
    return [json.loads(ln) for ln in
            p.read_text(encoding="utf-8").splitlines() if ln.strip()]


sys.path.insert(0, str(HERE))
from fitness_ledger import (append_event, emit_gate_verdicts,  # noqa: E402
                            emit_written, item_hash, latest_snapshot,
                            ledger_home, snapshot_gate1)


def mk_item(name, verdict, band="", text=""):
    return {"name": name, "band": band, "block_text": text,
            "dedup": {"verdict": verdict,
                      "best_match": {"heading": "H", "jaccard": 0.1}}}


with tempfile.TemporaryDirectory() as td:
    tmp = Path(td)

    # ---- 1. ledger_home 三级优先级 --------------------------------------
    saved = os.environ.pop("FITNESS_HOME", None)
    try:
        check(ledger_home(tmp / "x") == Path(tmp / "x"), "ledger_home 显式参数优先")
        os.environ["FITNESS_HOME"] = str(tmp / "y")
        check(ledger_home() == Path(tmp / "y"), "ledger_home env 次之")
        check(ledger_home(tmp / "x") == Path(tmp / "x"), "env 在场时显式仍胜")
        os.environ.pop("FITNESS_HOME")
        check(ledger_home() == Path.home() / ".claude" / "fitness",
              "ledger_home 缺省 ~/.claude/fitness")
    finally:
        if saved is not None:
            os.environ["FITNESS_HOME"] = saved

    home = tmp / "fitness"

    # ---- 2. append_event 往返 + 非法类别 + fail-open --------------------
    check(append_event("retrieval", {"section": "introduction"}, home=home),
          "append_event 正常写入")
    rec = read_events(home, "retrieval")[0]
    check(rec.get("schema_v") == 1 and "ts" in rec
          and rec.get("section") == "introduction",
          "事件带 schema_v/ts 且字段在位")
    try:
        append_event("bogus_kind", {}, home=home)
        check(False, "非法事件类别被拒")
    except ValueError:
        check(True, "非法事件类别被拒")
    blocker = tmp / "blocker.txt"
    blocker.write_text("not a dir", encoding="utf-8")
    check(append_event("retrieval", {"section": "theory"}, home=blocker) is False,
          "fail-open：台账家不可写 → False 不抛异常")

    # ---- 3. gate① 快照 + 全裁决矩阵（进程内） ---------------------------
    pdm = tmp / "fit_smoke.pdm.yaml"
    root = {"paper_id": "fit_smoke_2026"}
    plan_path = tmp / "writeback_plan.introduction.yaml"
    presented = {"introduction": (
        plan_path,
        {"items": [mk_item("变体甲", "ADD", "gap", "文本A"),
                   mk_item("变体乙", "SKIP", "", "文本B"),
                   mk_item("变体丙", "ADD", "薄弱", "文本C"),
                   mk_item("变体丁", "ADD", "quiet", "文本F"),
                   mk_item("变体庚", "SKIP", "", "文本G")]})}
    sheet = "# gate ① 写回呈审单 — fit smoke"
    snap = snapshot_gate1(pdm, root, presented, sheet, home=home)
    sdir = home / "gate1_sheets" / "fit_smoke"
    check(len(snap.get("files", [])) == 2 and snap.get("items") == 5
          and (sdir).is_dir(), "快照：md+yaml 存档且计数 5")
    latest = latest_snapshot(pdm, home=home)
    check(latest and len(latest["items"]) == 5
          and latest["run"] == "fit_smoke_2026",
          "latest_snapshot 读回最近快照")
    check(any(e.get("record") == "presented" for e in read_events(home, "acceptance")),
          "presented 事件落账")

    final = {"items": [mk_item("变体甲", "ADD", "gap", "文本A"),      # confirmed
                       mk_item("变体乙", "ADD", "", "文本D"),        # skip_flipped
                       mk_item("变体丙", "ADD", "薄弱", "文本C改"),  # edited
                       mk_item("变体戊", "SKIP", "", "文本E"),       # 未呈审 SKIP→无事件
                       mk_item("变体己", "ADD", "gap", "文本己"),    # added_at_gate
                       mk_item("变体庚", "SKIP", "", "文本G")]}      # skip_endorsed
    msg = emit_gate_verdicts(pdm, root, "introduction", final, home=home)
    got = {e["item"]: e["verdict"]
           for e in read_events(home, "acceptance")
           if e.get("record") == "verdict"}
    check(got == {"变体甲": "confirmed", "变体乙": "skip_flipped",
                  "变体丙": "edited", "变体己": "added_at_gate",
                  "变体丁": "dropped", "变体庚": "skip_endorsed"}
          and "变体戊" not in got,
          f"六类裁决 diff 全对；未呈审 SKIP 无事件（实际 {got}）")
    check("6 项" in msg and "confirmed×1" in msg, f"emit 摘要行可读（{msg[:40]}…）")

    # band 字段随事件落账（D 节结构化主源）
    bev = [e for e in read_events(home, "acceptance")
           if e.get("record") == "verdict" and e["item"] == "变体甲"]
    check(bev and bev[0].get("band") == "gap", "band 字段随裁决事件落账")

    # ---- 4. 无快照 → preauthorized_auto；written 漏斗 -------------------
    pdm2 = tmp / "auto_run.pdm.yaml"
    root2 = {"paper_id": "auto_run_2026"}
    auto_plan = {"items": [mk_item("变体甲", "ADD", "", "文本A"),
                           mk_item("变体乙", "SKIP", "", "文本B")]}
    emit_gate_verdicts(pdm2, root2, "theory", auto_plan, home=home)
    got2 = [e["verdict"] for e in read_events(home, "acceptance")
            if e.get("record") == "verdict" and e.get("run") == "auto_run_2026"]
    check(got2 == ["preauthorized_auto"],
          "无快照（auto-write）→ 仅 live 项 preauthorized_auto，SKIP 不记")
    emit_written(pdm2, root2, "theory", auto_plan, home=home)
    w = [e for e in read_events(home, "acceptance")
         if e.get("record") == "written"]
    check(w and w[-1]["items_final"] == 1, "written 事件带 items_final")

    # ---- 5. pdm_tool CLI 端到端（真实 subprocess，FITNESS_HOME 沙盒）----
    home2 = tmp / "fitness_cli"
    wd = tmp / "cli.pdm"
    wd.mkdir()
    plan2 = wd / "writeback_plan.introduction.yaml"
    plan2.write_text(yaml.safe_dump(
        {"corpus_root": str(tmp), "items": [
            mk_item("变体甲", "ADD", "gap", "CLI文本A"),
            mk_item("变体乙", "SKIP", "", "CLI文本B")]},
        allow_unicode=True), encoding="utf-8")
    rp = tmp / "cli.pdm.yaml"
    rp.write_text(yaml.safe_dump(yaml.safe_load(f"""
pdm_version: 1.0
paper_id: "fit_cli_2026"
title: "Fitness CLI Smoke"
status: "distilling"
distill_track:
  introduction: {{status: distilled, section_json: "sections/introduction.json",
    writeback: {{gate: awaiting_confirm}}}}
"""), allow_unicode=True, sort_keys=False), encoding="utf-8")
    P = ["--pdm", str(rp)]
    r = run(PDM_TOOL, ["present", *P, "--mode", "gate1",
                       "--sections", "introduction",
                       "--plan", f"introduction={plan2}"], home2)
    check(r.returncode == 0 and "fitness: gate① 快照已存档" in r.stdout
          and (home2 / "gate1_sheets" / "cli").is_dir(),
          "pdm_tool present 默认落快照（沙盒内）")
    n_snap = len(list((home2 / "gate1_sheets" / "cli").glob("*.gate1.items.yaml")))
    r = run(PDM_TOOL, ["present", *P, "--mode", "gate1",
                       "--sections", "introduction",
                       "--plan", f"introduction={plan2}", "--stdout-only"], home2)
    check(r.returncode == 0
          and len(list((home2 / "gate1_sheets" / "cli").glob(
              "*.gate1.items.yaml"))) == n_snap,
          "--stdout-only 不落快照")
    r = run(PDM_TOOL, ["set-gate", *P, "--section", "introduction",
                       "--gate", "confirmed", "--plan", str(plan2),
                       "--note", "全确认（中文实测）"], home2)
    verdicts = [e for e in read_events(home2, "acceptance")
                if e.get("record") == "verdict"]
    check(r.returncode == 0 and "fitness:" in r.stdout
          and {e["item"]: e["verdict"] for e in verdicts}
          == {"变体甲": "confirmed", "变体乙": "skip_endorsed"},
          "set-gate confirmed 发射逐项裁决")
    r = run(PDM_TOOL, ["set-gate", *P, "--section", "introduction",
                       "--gate", "confirmed", "--plan", str(plan2)], home2)
    verdicts2 = [e for e in read_events(home2, "acceptance")
                 if e.get("record") == "verdict"]
    check(r.returncode == 0 and len(verdicts2) == len(verdicts),
          "幂等重跑 confirmed 零新事件（只在迁移时发射）")
    r = run(PDM_TOOL, ["set-gate", *P, "--section", "introduction",
                       "--gate", "written", "--plan", str(plan2)], home2)
    wrec = [e for e in read_events(home2, "acceptance")
            if e.get("record") == "written"]
    check(r.returncode == 0 and len(wrec) == 1
          and wrec[0]["items_final"] == 1, "set-gate written 落漏斗终点事件")

    # ---- 6. retrieve_exemplars 落账 + fail-open -------------------------
    home3 = tmp / "fitness_ret"
    cat = tmp / "catalog.json"
    cat.write_text(json.dumps({"cards": [{
        "id": "fitsmoke2026-demo-card", "path": "v4/x.md",
        "paper_type": "quantitative", "publication_status": "published",
        "coverage": "complete", "theoretical_problem_form": [],
        "narrative_dynamics": ["arc-x"], "retrieval_signals": ["sig-a"],
        "section_learning": {"introduction": {
            "suitable": "yes", "requires": [], "learn": ["L"],
            "caveat": []}}}]}, ensure_ascii=False), encoding="utf-8")
    req = tmp / "request.json"
    req.write_text(json.dumps({"section": "introduction",
                               "paper_type": "quantitative",
                               "story_needs": ["arc-x"],
                               "retrieval_signals": ["sig-a"]},
                              ensure_ascii=False), encoding="utf-8")
    r = run(RETRIEVE, ["--request", str(req), "--catalog", str(cat)], home3)
    ok_json = False
    try:
        payload = json.loads(r.stdout[r.stdout.index("{"):])
        ok_json = payload["results"][0]["id"] == "fitsmoke2026-demo-card"
    except Exception:
        pass
    ev = read_events(home3, "retrieval")
    check(r.returncode == 0 and ok_json and len(ev) == 1
          and ev[0]["n_results"] == 1 and ev[0]["returned"][0]["score"] > 0
          and ev[0]["empty"] is False, "retrieve_exemplars 检索事件落账")
    r2 = run(RETRIEVE, ["--request", str(req), "--catalog", str(cat)],
             tmp / "blocker.txt")
    ok2 = False
    try:
        json.loads(r2.stdout[r2.stdout.index("{"):])
        ok2 = True
    except Exception:
        pass
    check(r2.returncode == 0 and ok2 and "WARN" in r2.stderr,
          "检索落账 fail-open：台账不可写仍出结果")

    # ---- 7. log-consumption CLI -----------------------------------------
    home4 = tmp / "fitness_cons"
    env4 = {**os.environ, "FITNESS_HOME": str(home4)}
    payload = json.dumps({"skill": "write-theory", "section": "theory",
                          "project": "smoke",
                          "variants": ["<!-- wb:fit2026:变体九 -->"],
                          "blueprint_cards": ["fitsmoke2026-demo-card"]},
                         ensure_ascii=False)
    p = subprocess.run([sys.executable, str(HERE / "fitness_ledger.py"),
                        "log-consumption"], input=payload, capture_output=True,
                       text=True, encoding="utf-8", env=env4)
    cev = read_events(home4, "consumption")
    check(p.returncode == 0 and len(cev) == 1
          and cev[0]["skill"] == "write-theory", "log-consumption stdin 入账")
    p = subprocess.run([sys.executable, str(HERE / "fitness_ledger.py"),
                        "log-consumption"], input='{"skill": ""}',
                       capture_output=True, text=True, encoding="utf-8",
                       env=env4)
    check(p.returncode == 2, "缺 skill/section → 拒绝")

    # ---- 8. fitness_report 端到端 ----------------------------------------
    r = run(REPORT, ["report", "--home", str(home)], home)
    body = r.stdout
    check(r.returncode == 0
          and all(h in body for h in ("## A. 接受率", "## B. 检索命中",
                                      "## C. 语料消耗", "## D. band×使用",
                                      "## E. 剪裁候选")),
          "报告五节齐全")
    check("preauthorized_auto" in body or "预授权" in body
          and "fit_smoke_2026" in body, "报告含裁决数据")
    out_md = tmp / "report.md"
    r = run(REPORT, ["report", "--home", str(home), "--out", str(out_md)], home)
    check(r.returncode == 0 and out_md.is_file()
          and "冷启动声明" in out_md.read_text(encoding="utf-8"),
          "--out 落盘且含冷启动声明")
    empty_home = tmp / "fitness_empty"
    r = run(REPORT, ["report", "--home", str(empty_home)], empty_home)
    check(r.returncode == 0 and "无接受事件" in r.stdout,
          "空台账冷启动不炸")

failed = [n for ok, n in results if not ok]
print("-" * 60)
print(f"{'ALL GREEN' if not failed else 'FAILURES: ' + str(failed)}"
      f"  ({len(results) - len(failed)}/{len(results)})")
sys.exit(0 if not failed else 1)
