#!/usr/bin/env python3
"""fitness_ledger — 策展指标事件层：append-only JSONL 台账（2026-09-14，第 4 项）。

fitness 信号分四类事件，全部追加进 <台账家>/events/：
  acceptance    gate① 裁决（record=presented|verdict|written；pdm_tool 发射）
  retrieval     蓝图卡检索命中（retrieve_exemplars.py 发射）
  corpus_query  选材 Gate 语料查询（corpus_query.py 发射）
  consumption   写作期语料消耗（write-* 成文登记，best-effort）
  exemplar_use  句段范本返回／查看／采用／真实作者评价（query_id 关联）

设计不变量（方案裁定 2026-09-14）：
  - 台账家默认 ~/.claude/fitness/，FITNESS_HOME env 可覆盖；ledger_home()
    每次调用读取（非 import 期常量），显式参数优先——测试沙盒的前提。
  - 全部写入 fail-open：失败只 WARN，绝不阻塞蒸馏/写作主管线。
  - 事件是观察不是派生态：append-only、不改写；fitness_report.py 是其上
    的派生视图，按需再生。台账目录在 distill-work 与 skills 仓库两棵树之外，
    构造性免疫 preprocess_l0 --clean/--sweep（sweep 只触上述两树）。
  - pdm_tool 仍是 PDM 根唯一写者；本模块只写台账目录（pdm-schema 单写者表）。

gate① 裁决 diff（emit_gate_verdicts：present 快照 vs set-gate confirmed 时终版
plan 逐项）：confirmed（hash 同）/ edited（hash 异）/ dropped（live→缺席）/
skip_endorsed（终版 SKIP 且曾呈审）/ skip_flipped（呈审 SKIP→终版 live，即翻
案——第 5 项 dedup 边界带仲裁的实证数据源）/ added_at_gate（呈审后新增）/
preauthorized_auto（无快照=auto-write 直写，报告单列不入人工裁决分母）。
事件只在 gate 真实迁移时发射（幂等重跑零事件，报告侧另有 exact-dup 兜底）。
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

# 中文 Windows 控制台默认 GBK；代理按 UTF-8 读工具输出，强制 UTF-8 避免乱码。
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

SCHEMA_V = 1
EVENT_KINDS = ("acceptance", "retrieval", "corpus_query", "consumption", "exemplar_use")
VERDICTS = ("confirmed", "edited", "dropped", "skip_endorsed", "skip_flipped",
            "added_at_gate", "preauthorized_auto")


def ledger_home(explicit: str | Path | None = None) -> Path:
    """台账家目录：显式参数 > FITNESS_HOME env > ~/.claude/fitness。"""
    if explicit is not None:
        return Path(explicit).expanduser()
    env = os.environ.get("FITNESS_HOME")
    if env:
        return Path(env).expanduser()
    return Path.home() / ".claude" / "fitness"


def read_json_input(path=None):
    """Read the UTF-8 JSON transport, including Chinese Windows pipe input."""
    if path not in (None, '-'):
        return json.loads(Path(path).read_text(encoding='utf-8-sig'))
    if hasattr(sys.stdin, 'reconfigure'):
        sys.stdin.reconfigure(encoding='utf-8-sig', errors='strict')
    return json.load(sys.stdin)


def _events_path(kind: str, home=None) -> Path:
    if kind not in EVENT_KINDS:
        raise ValueError(f"未知事件类别：{kind!r}（合法：{EVENT_KINDS}）")
    return ledger_home(home) / "events" / f"{kind}.jsonl"


def append_event(kind: str, payload: dict, home=None) -> bool:
    """追加一行事件。返回 False = 写入失败（已 WARN，调用方无须再处理）。"""
    rec = {"schema_v": SCHEMA_V,
           "ts": datetime.now().astimezone().isoformat(timespec="seconds")}
    rec.update(payload)
    try:
        path = _events_path(kind, home)
        path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps(rec, ensure_ascii=False, sort_keys=True)
        with open(path, "a", encoding="utf-8", newline="\n") as f:
            f.write(line + "\n")
        return True
    except OSError as e:
        print(f"WARN: fitness 台账写入失败（{kind}）——遥测不阻塞主管线：{e}",
              file=sys.stderr)
        return False


def run_key(root: dict, fallback: str = "") -> str:
    """论文级 join key：wb_citekey > paper_id > citekey > PDM 文件名。"""
    for k in ("wb_citekey", "paper_id", "citekey"):
        v = str(root.get(k) or "").strip()
        if v:
            return v
    return fallback


def pdm_stem(pdm_path: Path) -> str:
    """`<citekey>.pdm.yaml` → `<citekey>`（stem 只剥最后一个后缀，会剩
    `.pdm`——目录名与 run fallback 都用本函数）。"""
    name = pdm_path.name
    if name.endswith(".pdm.yaml"):
        return name[: -len(".pdm.yaml")]
    return pdm_path.stem


def item_hash(item: dict) -> str:
    """块内容指纹（edited 判定用）。v2 plan 应有 block_text；缺失时退化为
    name+anchor+band 的确定性 hash——同一计算在快照与终版两侧一致即可比。"""
    h = hashlib.sha256()
    bt = item.get("block_text")
    if bt is not None:
        h.update(str(bt).encode("utf-8"))
    else:
        anchor = item.get("anchor") or {}
        h.update(json.dumps({"name": item.get("name"),
                             "after_heading": anchor.get("after_heading"),
                             "band": item.get("band")},
                            ensure_ascii=False, sort_keys=True).encode("utf-8"))
    return h.hexdigest()[:16]


def _plan_counts(plan: dict) -> Counter:
    return Counter(((it.get("dedup") or {}).get("verdict") or "?")
                   for it in plan.get("items") or [])


# ------------------------------------------------------- gate① 快照与裁决 --

def snapshot_gate1(pdm_path: Path, root: dict, plans: dict, sheet_text: str,
                   home=None) -> dict:
    """gate① 呈审落账：呈审单 md + 机器快照 yaml 存档 + presented 事件。

    plans 形如 {section: (plan_path, plan_dict)}（pdm_tool cmd_present 同构）。
    快照按时间戳追加保留、不覆盖——返工再呈审的历史即完整审计链。
    返回摘要 dict；失败返回 {}（已 WARN，fail-open）。
    """
    stem = pdm_stem(pdm_path)
    run = run_key(root, stem)
    items = []
    for s in sorted(plans):
        path, plan = plans[s]
        for it in plan.get("items") or []:
            items.append({
                "section": s,
                "item": str(it.get("name") or ""),
                "verdict": (it.get("dedup") or {}).get("verdict") or "?",
                "band": str(it.get("band") or ""),
                "content_hash": item_hash(it),
                "plan": Path(path).name,
            })
    snap = {"schema_v": SCHEMA_V,
            "ts": datetime.now().astimezone().isoformat(timespec="seconds"),
            "run": run, "sections": sorted(plans), "items": items}
    tag = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = ledger_home(home) / "gate1_sheets" / stem
    written = []
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        md = out_dir / f"{tag}.gate1.md"
        md.write_text(sheet_text.rstrip() + "\n", encoding="utf-8", newline="\n")
        yml = out_dir / f"{tag}.gate1.items.yaml"
        yml.write_text(yaml.safe_dump(snap, allow_unicode=True, sort_keys=False),
                       encoding="utf-8", newline="\n")
        written = [md.name, yml.name]
    except OSError as e:
        print(f"WARN: gate① 快照存档失败——遥测不阻塞呈审：{e}", file=sys.stderr)
    append_event("acceptance", {
        "record": "presented", "run": run,
        "sections": {s: dict(_plan_counts(plans[s][1])) for s in sorted(plans)},
        "items_total": len(items), "sheets": written, "sheet_dir": str(out_dir),
    }, home=home)
    return {"dir": str(out_dir), "files": written, "items": len(items)}


def latest_snapshot(pdm_path: Path, home=None) -> dict | None:
    """该 PDM 根最近一次 gate① 快照（文件名含时间戳，字典序即时间序）。"""
    d = ledger_home(home) / "gate1_sheets" / pdm_stem(pdm_path)
    ymls = sorted(d.glob("*.gate1.items.yaml"))
    if not ymls:
        return None
    try:
        return yaml.safe_load(ymls[-1].read_text(encoding="utf-8")) or None
    except (OSError, yaml.YAMLError) as e:
        print(f"WARN: gate① 快照不可读（按无快照=preauthorized 处理）：{e}",
              file=sys.stderr)
        return None


def emit_gate_verdicts(pdm_path: Path, root: dict, section: str, plan: dict,
                       home=None) -> str:
    """set-gate → confirmed 迁移：逐项裁决事件。返回摘要行（空=无事可记）。"""
    run = run_key(root, pdm_stem(pdm_path))
    snap = latest_snapshot(pdm_path, home=home)
    events: list[dict] = []
    if snap is None:
        # auto-write 预授权直写：无呈审快照，全部 live 项单列，不入人工分母
        for it in plan.get("items") or []:
            if ((it.get("dedup") or {}).get("verdict")) == "SKIP":
                continue
            events.append({"item": str(it.get("name") or ""),
                           "band": str(it.get("band") or ""),
                           "verdict": "preauthorized_auto",
                           "content_hash": item_hash(it)})
    else:
        presented = {(e.get("section"), e.get("item")): e
                     for e in (snap.get("items") or [])}
        final_names: set[str] = set()
        for it in plan.get("items") or []:
            name = str(it.get("name") or "")
            final_names.add(name)
            verdict = ((it.get("dedup") or {}).get("verdict")) or "?"
            p = presented.get((section, name))
            if verdict == "SKIP":
                if p is None:
                    continue  # 从未呈审的 SKIP：无接受语义可记
                v = "skip_endorsed"
            elif p is None:
                v = "added_at_gate"
            elif p.get("verdict") == "SKIP":
                v = "skip_flipped"
            elif p.get("content_hash") == item_hash(it):
                v = "confirmed"
            else:
                v = "edited"
            events.append({"item": name, "band": str(it.get("band") or ""),
                           "verdict": v, "content_hash": item_hash(it)})
        for (sec, name), p in presented.items():
            # 呈审 live 项在终版 plan 中整体消失 = gate 上被裁掉
            if (sec == section and p.get("verdict") != "SKIP"
                    and name not in final_names):
                events.append({"item": str(name),
                               "band": str(p.get("band") or ""),
                               "verdict": "dropped",
                               "content_hash": p.get("content_hash")})
    for e in events:
        append_event("acceptance", {"record": "verdict", "run": run,
                                    "section": section, **e}, home=home)
    if not events:
        return ""
    c = Counter(e["verdict"] for e in events)
    return (f"{run}/{section} 接受事件 {len(events)} 项落账："
            + " ".join(f"{k}×{v}" for k, v in sorted(c.items())))


def emit_written(pdm_path: Path, root: dict, section: str, plan: dict | None,
                 home=None) -> str:
    """set-gate → written 迁移：节级完成事件（presented→confirmed→written 漏斗）。"""
    live = None
    if plan is not None:
        live = sum(1 for it in plan.get("items") or []
                   if ((it.get("dedup") or {}).get("verdict")) != "SKIP")
    append_event("acceptance", {"record": "written", "section": section,
                                "run": run_key(root, pdm_stem(pdm_path)),
                                "items_final": live}, home=home)
    return f"{run_key(root, pdm_stem(pdm_path))}/{section} written 事件落账（final {live if live is not None else '-'} 项）"


# ------------------------------------------------------------ consumption --

def cmd_log_consumption(args) -> int:
    """成文登记；新 UID 采用关联检索与草稿，历史原生登记单列。"""
    try:
        data = read_json_input(args.file)
    except (OSError, ValueError) as e:
        print(f"ERROR: consumption JSON 不可读：{e}", file=sys.stderr)
        return 2
    if not isinstance(data, dict) or not str(data.get("skill") or "").strip() \
            or not str(data.get("section") or "").strip():
        print("ERROR: consumption 事件至少需要 skill 与 section 字段", file=sys.stderr)
        return 2
    # A new UID adoption has one writer for adopted + consumption. Historical
    # unlinked lines remain untouched; no query ID is invented for native use.
    sys.path.insert(0, str(Path(__file__).resolve().parents[2] / '_shared/indexing'))
    from use_exemplar import external_path, record_adoption
    try:
        external_path(ledger_home(args.home), name='ledger')
        if not isinstance(data.get('source_uids', []), list):
            raise ValueError('source_uids must be a list')
        if data.get('source_uids') or 'uses' in data or 'query_id' in data:
            from retrieve import load_catalog
            result = record_adoption(data, load_catalog(), args.home)
            print(json.dumps(result, ensure_ascii=False))
            return 0
        allowed = {'skill', 'section', 'project', 'corpus_files', 'source_uids',
                   'variants', 'blueprint_cards', 'note'}
        if set(data) - allowed:
            raise ValueError('consumption accepts metadata only, not prose snapshots')
        if data['section'] not in ('introduction', 'theory', 'methods', 'results') or data['skill'] != f"write-{data['section']}":
            raise ValueError('skill and section must name the same active write-* section')
    except (ValueError, TypeError, OSError) as exc:
        print(f'ERROR: 消耗登记未执行：{exc}', file=sys.stderr)
        return 2
    ok = append_event("consumption", {**data, 'linkage': 'legacy_native'}, home=args.home)
    print("consumption 已落账" if ok else "consumption 写入失败（见 WARN）")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="fitness 台账事件层（append-only；报告见 fitness_report.py）")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("log-consumption",
                       help="登记一次写作的语料消耗（JSON：stdin 或 --file）")
    p.add_argument("--file", default=None,
                   help="JSON 文件路径；缺省读 stdin，'-' 显式 stdin")
    p.add_argument('--home', type=Path, help='隔离台账目录；默认 FITNESS_HOME 或 ~/.claude/fitness')
    args = ap.parse_args()
    if args.cmd == "log-consumption":
        return cmd_log_consumption(args)
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
