#!/usr/bin/env python3
"""fitness_report — 策展指标聚合报告（fitness 台账之上的派生视图，按需再生）。

五节（对应架构批评第 4 项的五个空白）：
  A 接受率    gate① 存活率：run×section 漏斗 + 按节汇总 + 月度趋势。
              acceptance_rate = confirmed / (confirmed+edited+dropped+
              skip_endorsed+skip_flipped)；preauthorized_auto 单列不入分母。
              度量的是呈审存活率，不度量 present 之前的子代理返工。
  B 检索命中  蓝图卡逐卡计数、零命中卡清单（对 catalog 全集）、空结果率/节
              （目录缺口信号）、卡↔论文 join 覆盖率。
  C 语料消耗  写作期登记的 corpus 文件 / wb 变体 / 蓝图卡（best-effort 面，
              覆盖率取决于登记依从度）。
  D band×使用 事件自带 band × 实测使用矩阵。矛盾候选 v1 仅一条规则
              （quiet 带论文的卡被高频检索 → band 可能过时），只列候选
              不自动裁定——band-vocab「提升路由权重」仍是人裁的事。
  E 剪裁候选  从未被消耗的 wb 变体（排除 30 天内新建）+ 低接受率 run。
              全部是候选清单；剪与不剪走 Decision Protocol，本脚本不删任何东西。

v1 诚实边界：历史 gate① 裁决无快照不可回补，一切比率自台账首事件起算；
band 历史判定（_skill_design_feedback.yaml 散文后缀）不回填进矩阵——
事件自带的 band 字段是唯一结构化主源。

Usage:
  py fitness_report.py report [--days N] [--out PATH] [--home DIR]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

# 中文 Windows 控制台默认 GBK；代理按 UTF-8 读工具输出，强制 UTF-8 避免乱码。
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    from fitness_ledger import ledger_home  # same dir, single ledger definition
except ImportError:  # pragma: no cover — scripts/ 布局损坏时才触发
    def ledger_home(explicit=None):
        return Path(explicit) if explicit else Path.home() / ".claude" / "fitness"

try:
    from rebuild_views import CORPUS_KEYS, WB_RE  # 单源：语料根 + wb 标记正则
except ImportError:  # pragma: no cover
    SKILLS_ROOT = Path(__file__).resolve().parents[2]
    CORPUS_KEYS = {s: SKILLS_ROOT / f"write-{s}" / "corpus"
                   for s in ("introduction", "theory", "methods", "results")}
    WB_RE = re.compile(r"<!--\s*wb:([^:>]+):([^>]+?)\s*-->")

SKILLS_ROOT = Path(__file__).resolve().parents[2]
CATALOG = SKILLS_ROOT / "story-blueprints" / "v4" / "catalog.json"
DENOM_VERDICTS = ("confirmed", "edited", "dropped", "skip_endorsed",
                  "skip_flipped")
RECENT_DAYS = 30          # E 节：新建保护期
RETRIEVE_HIGH = 5         # D 节矛盾候选默认阈值（仅排序参考，非裁定）
LOW_RATE = 0.8            # E 节低接受率阈值
LOW_DENOM = 3             # E 节低接受率最小分母
CAP_TABLE = 40            # 长表行数上限


def norm_key(s: str) -> str:
    """citekey/卡 id 归一化：去空白/下划线/连字符、小写（join 前双方同法）。"""
    return re.sub(r"[\s_\-]+", "", str(s or "")).lower()


def load_events(kind: str, since: datetime | None, home=None):
    path = ledger_home(home) / "events" / f"{kind}.jsonl"
    out, bad, seen = [], 0, set()
    if not path.is_file():
        return out, bad
    for ln in path.read_text(encoding="utf-8", errors="replace").splitlines():
        ln = ln.strip()
        if not ln:
            continue
        try:
            rec = json.loads(ln)
        except json.JSONDecodeError:
            bad += 1
            continue
        # exact-dup 兜底（发射侧已按迁移去重，这里防手工补录重复）
        key = json.dumps(rec, ensure_ascii=False, sort_keys=True)
        if key in seen:
            continue
        seen.add(key)
        if since:
            try:
                if datetime.fromisoformat(str(rec.get("ts"))) < since:
                    continue
            except ValueError:
                pass
        out.append(rec)
    return out, bad


def load_catalog_ids() -> set:
    try:
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        return {str(c.get("id") or "") for c in data.get("cards", [])} - {""}
    except (OSError, json.JSONDecodeError):
        return set()


def map_cards_to_papers(runs: set) -> tuple[dict, str]:
    """card id → run citekey（归一化包含匹配）；返回 (映射, 覆盖率说明)。"""
    norm_runs = {norm_key(r): r for r in runs if r}
    all_cards = load_catalog_ids()
    mapping: dict[str, str] = {}
    for cid in all_cards:
        ncid = norm_key(cid)
        for nr, orig in norm_runs.items():
            if nr and nr in ncid:
                mapping[cid] = orig
                break
    cov = (f"卡↔论文 join：{len(mapping)}/{len(all_cards)} 张卡匹配到已知 run"
           if all_cards else "catalog 不可读，join 跳过")
    return mapping, cov


# ------------------------------------------------------------------ A 节 --

def sec_acceptance(acc: list, out: list):
    """返回 (rates, lows)：rates 供调用方复用；lows 供 E 节低接受率清单。"""
    out.append("## A. 接受率（gate① 存活率）")
    verdicts = [e for e in acc if e.get("record") == "verdict"]
    presented = [e for e in acc if e.get("record") == "presented"]
    written = [e for e in acc if e.get("record") == "written"]
    if not verdicts and not presented:
        out.append("")
        out.append("（无接受事件——gate① 尚未有呈审/裁决落账）")
        return {}, []
    per: dict[tuple, Counter] = defaultdict(Counter)
    for e in verdicts:
        per[(str(e.get("run") or "?"), str(e.get("section") or "?"))][
            str(e.get("verdict") or "?")] += 1
    wmap = {(str(e.get("run") or ""), str(e.get("section") or "")) for e in written}
    pmap: Counter = Counter()
    for e in presented:
        for s, c in (e.get("sections") or {}).items():
            pmap[(str(e.get("run") or ""), str(s))] += sum(
                int(v) for v in (c or {}).values() if str(v).isdigit())
    out.append("")
    out.append("分母定义：confirmed/(confirmed+edited+dropped+skip_endorsed+"
               "skip_flipped)；preauthorized_auto/added_at_gate 单列不入分母；"
               "本率度量呈审存活，不度量 present 之前的子代理返工。")
    out.append("")
    out.append("| run | 节 | 呈审 | confirmed | edited | dropped | skip认可 | "
               "skip翻案 | 新增 | 预授权 | 率 | written |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    rates: dict[tuple, float | None] = {}
    lows = []
    for (run, sec), c in sorted(per.items()):
        denom = sum(c[v] for v in DENOM_VERDICTS)
        rate = (c["confirmed"] / denom) if denom else None
        rates[(run, sec)] = rate
        if rate is not None and denom >= LOW_DENOM and rate < LOW_RATE:
            lows.append((run, sec, rate, denom))
        out.append(
            f"| {run} | {sec} | {pmap.get((run, sec), '–')} "
            f"| {c['confirmed']} | {c['edited']} | {c['dropped']} "
            f"| {c['skip_endorsed']} | {c['skip_flipped']} "
            f"| {c['added_at_gate']} | {c['preauthorized_auto']} "
            f"| {'–' if rate is None else f'{rate:.0%}'} "
            f"| {'✓' if (run, sec) in wmap else '–'} |")
    by_sec: dict[str, Counter] = defaultdict(Counter)
    for (_run, sec), c in per.items():
        by_sec[sec].update(c)
    out.append("")
    out.append("| 节 | 分母 | confirmed | 率 |")
    out.append("|---|---|---|---|")
    for sec, c in sorted(by_sec.items()):
        denom = sum(c[v] for v in DENOM_VERDICTS)
        r = f"{c['confirmed'] / denom:.0%}" if denom else "–"
        out.append(f"| {sec} | {denom} | {c['confirmed']} | {r} |")
    trend: dict[str, Counter] = defaultdict(Counter)
    for e in verdicts:
        trend[str(e.get("ts"))[:7]][str(e.get("verdict"))] += 1
    if trend:
        out.append("")
        out.append("| 月 | confirmed | edited | dropped | skip系 | 其他 |")
        out.append("|---|---|---|---|---|---|")
        for m in sorted(trend):
            c = trend[m]
            other = sum(n for v, n in c.items()
                        if v not in DENOM_VERDICTS
                        and v != "preauthorized_auto")
            out.append(f"| {m} | {c['confirmed']} | {c['edited']} "
                       f"| {c['dropped']} "
                       f"| {c['skip_endorsed'] + c['skip_flipped']} | {other} |")
    return rates, lows


# ------------------------------------------------------------------ B 节 --

def sec_retrieval(ret: list, out: list):
    out.append("## B. 检索命中（story-blueprints 蓝图卡）")
    if not ret:
        out.append("")
        out.append("（无检索事件——write-* 即时范文协议尚未产生调用）")
        return
    card_counts: Counter = Counter()
    sec_stats: dict[str, list] = defaultdict(lambda: [0, 0])  # req, empty
    for e in ret:
        s = str(e.get("section") or "?")
        sec_stats[s][0] += 1
        if e.get("empty"):
            sec_stats[s][1] += 1
        for r in e.get("returned") or []:
            card_counts[str(r.get("id") or "?")] += 1
    out.append("")
    out.append("| 节 | 调用 | 空结果 | 空结果率 |")
    out.append("|---|---|---|---|")
    for s, (req, empty) in sorted(sec_stats.items()):
        out.append(f"| {s} | {req} | {empty} | {empty / req:.0%} |")
    out.append("")
    if card_counts:
        out.append(f"逐卡命中（{len(card_counts)} 张卡被检索过，"
                   f"top {min(15, len(card_counts))}）：")
        out.extend(f"- {cid} ×{n}" for cid, n in card_counts.most_common(15))
    cat = load_catalog_ids()
    if cat:
        zero = sorted(cat - set(card_counts))
        out.append("")
        out.append(f"零命中卡 {len(zero)}/{len(cat)}（对 catalog 全集；"
                   f"台账窗口内零命中 ≠ 永远零命中）")
        out.extend(f"- {cid}" for cid in zero[:30])
        if len(zero) > 30:
            out.append(f"- …其余 {len(zero) - 30} 张略")


# ------------------------------------------------------------------ C 节 --

def sec_consumption(cons: list, out: list):
    """返回 (consumed_variant_keys, file_counts) 供 E 节复用。"""
    out.append("## C. 语料消耗（write-* 成文登记，best-effort）")
    consumed: set = set()
    if not cons:
        out.append("")
        out.append("（无消耗事件——write-* 的 log-consumption 登记尚未产生数据；"
                   "该面为协议级 best-effort，覆盖率取决于登记依从度）")
        return consumed, Counter()
    file_counts: Counter = Counter()
    variant_counts: Counter = Counter()
    card_counts: Counter = Counter()
    skills: Counter = Counter()
    for e in cons:
        skills[str(e.get("skill") or "?")] += 1
        for f in e.get("corpus_files") or []:
            file_counts[str(f)] += 1
        for v in e.get("variants") or []:
            ms = list(WB_RE.finditer(str(v)))
            if not ms:
                variant_counts[f"::??（非 wb 标记）{str(v)[:40]}"] += 1
            for m in ms:
                consumed.add((norm_key(m.group(1)), m.group(2)))
                variant_counts[f"{norm_key(m.group(1))}::{m.group(2)}"] += 1
        for c in e.get("blueprint_cards") or []:
            card_counts[str(c)] += 1
    out.append("")
    out.append(f"事件 {len(cons)} 次（按 skill："
               + "，".join(f"{k}×{v}" for k, v in skills.most_common()) + "）")
    if file_counts:
        out.append("")
        out.append(f"corpus 文件（{len(file_counts)} 个被登记，"
                   f"top {min(20, len(file_counts))}）：")
        out.extend(f"- {f} ×{n}" for f, n in file_counts.most_common(20))
    if variant_counts:
        out.append("")
        out.append(f"wb 变体（{len(variant_counts)} 个被消耗，"
                   f"top {min(20, len(variant_counts))}）：")
        out.extend(f"- {v} ×{n}" for v, n in variant_counts.most_common(20))
    if card_counts:
        out.append("")
        out.append(f"蓝图卡采用（{len(card_counts)} 张）：")
        out.extend(f"- {c} ×{n}" for c, n in card_counts.most_common(10))
    return consumed, file_counts


# ------------------------------------------------------------------ D 节 --

def sec_band(acc: list, ret: list, out: list):
    out.append("## D. band×使用矩阵（事件自带 band 为结构化主源）")
    verdicts = [e for e in acc if e.get("record") == "verdict"]
    if not verdicts:
        out.append("")
        out.append("（无裁决事件——band 矩阵待首批 gate① 数据）")
        return
    band_c: dict[str, Counter] = defaultdict(Counter)
    run_bands: dict[str, set] = defaultdict(set)
    for e in verdicts:
        b = str(e.get("band") or "").strip() or "（未记）"
        band_c[b][str(e.get("verdict"))] += 1
        run_bands[str(e.get("run") or "?")].add(b)
    runs = {r for r in run_bands if r not in ("", "?")}
    card_paper, cov = map_cards_to_papers(runs)
    paper_ret: Counter = Counter()
    for e in ret:
        for r in e.get("returned") or []:
            p = card_paper.get(str(r.get("id") or ""))
            if p:
                paper_ret[p] += 1
    out.append("")
    out.append(f"（{cov}）")
    out.append("")
    out.append("| band | 分母 | confirmed | 率 | 关联 run 卡检索均值 |")
    out.append("|---|---|---|---|---|")
    for b, c in sorted(band_c.items()):
        denom = sum(c[v] for v in DENOM_VERDICTS)
        rate = f"{c['confirmed'] / denom:.0%}" if denom else "–"
        rvals = [paper_ret.get(r, 0) for r, bs in run_bands.items() if b in bs]
        avg = f"{sum(rvals) / len(rvals):.1f}" if rvals else "–"
        out.append(f"| {b} | {denom} | {c['confirmed']} | {rate} | {avg} |")
    out.append("")
    out.append(f"矛盾候选（v1 唯一规则：quiet 带论文的卡被检索 ≥{RETRIEVE_HIGH} "
               "次 → band 可能过时；只列候选，不自动裁定）：")
    hits = [(r, n) for r, n in paper_ret.most_common()
            if n >= RETRIEVE_HIGH and "quiet" in run_bands.get(r, set())]
    if hits:
        out.extend(f"- {r}（卡检索 ×{n}，band 含 quiet）" for r, n in hits)
    else:
        out.append("（暂无）")
    out.append("")
    out.append("注：gap/薄弱/critique_heavy 的矛盾判据需更多数据窗口后再定；"
               "band-vocab「提升路由权重」仍是人裁事项，本报告只供数。")


# ------------------------------------------------------------------ E 节 --

def scan_corpus_markers() -> dict:
    """全集：{(norm_paper, item): {file, created}}——扫四家 corpus 的 wb 标记。"""
    markers: dict[tuple, dict] = {}
    for v in CORPUS_KEYS.values():
        root = Path(v)
        if not root.is_absolute():
            root = SKILLS_ROOT / v  # CORPUS_KEYS 存的是仓库根相对路径
        if not root.is_dir():
            continue
        for f in root.rglob("*.md"):
            try:
                text = f.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            ms = list(WB_RE.finditer(text))
            if not ms:
                continue
            created = None
            m = re.search(r"^created:\s*['\"]?(\d{4}-\d{2}-\d{2})",
                          "\n".join(text.splitlines()[:24]), re.MULTILINE)
            if m:
                created = m.group(1)
            else:
                created = time.strftime("%Y-%m-%d",
                                        time.localtime(f.stat().st_mtime))
            try:
                rel = str(f.relative_to(SKILLS_ROOT))
            except ValueError:
                rel = str(f)
            for mm in ms:
                markers.setdefault((norm_key(mm.group(1)), mm.group(2)),
                                   {"file": rel, "created": created})
    return markers


def sec_prune(cons: list, out: list, lows):
    out.append("## E. 剪裁候选（只列不剪——裁决走 Decision Protocol）")
    consumed, _ = sec_consumption(cons, [])  # 复用解析，不重复出 C 节文字
    markers = scan_corpus_markers()
    cutoff = (datetime.now() - timedelta(days=RECENT_DAYS)).strftime("%Y-%m-%d")
    never = {k: v for k, v in markers.items()
             if k not in consumed and (v["created"] or "9999") < cutoff}
    out.append("")
    out.append(f"语料 wb 变体全集 {len(markers)}；台账窗口内被消耗 "
               f"{len([k for k in markers if k in consumed])}；"
               f"从未被消耗（排除 {RECENT_DAYS} 天内新建）{len(never)}。")
    if never and not cons:
        # 冷启动保护：消耗台账为空时 never-consumed = 全部旧变体，零判别力，
        # 只报计数不出明细——防止 441 这类数字被误读成剪裁信号。
        out.append(f"（消耗台账尚无事件——明细表自首个消耗窗口起才有判别力，"
                   "暂不列出）")
    elif never:
        out.append("")
        out.append("| 文件 | 变体 | 论文(归一) | created/mtime |")
        out.append("|---|---|---|---|")
        for (np_, item), v in sorted(never.items(),
                                     key=lambda kv: kv[1]["file"])[:CAP_TABLE]:
            out.append(f"| {v['file']} | {item} | {np_} | {v['created']} |")
        if len(never) > CAP_TABLE:
            out.append(f"| …其余 {len(never) - CAP_TABLE} 项略 | | | |")
    if lows:
        out.append("")
        out.append(f"低接受率 run（率 <{LOW_RATE:.0%} 且分母 ≥{LOW_DENOM}；"
                   "系统性 edited/dropped 偏高提示子代理质量或呈审前返工不足）：")
        out.extend(f"- {run}/{sec}：{rate:.0%}（分母 {denom}）"
                   for run, sec, rate, denom in lows)
    out.append("")
    out.append("提示：报告为派生视图可随时再生；如需留档请复制本文件"
               "（台账不自动备份）——剪裁与 band 调整请走 Decision Protocol 登记。")


# ------------------------------------------------------------------ main --

def build_report(days: int, home=None) -> str:
    since = (datetime.now().astimezone()
             - timedelta(days=days)) if days else None
    acc, b1 = load_events("acceptance", since, home)
    ret, b2 = load_events("retrieval", since, home)
    cq, b3 = load_events("corpus_query", since, home)
    cons, b4 = load_events("consumption", since, home)
    bads = [f"{k}×{n}" for k, n in (("acceptance", b1), ("retrieval", b2),
                                    ("corpus_query", b3),
                                    ("consumption", b4)) if n]
    out = ["# fitness 策展报告",
           f"生成：{datetime.now():%Y-%m-%d %H:%M} · "
           + ("窗口：全部历史" if not days else f"窗口：近 {days} 天")
           + (f" · 解析失败行：{'，'.join(bads)}" if bads else ""),
           "",
           "冷启动声明：历史 gate① 裁决无快照不可回补，一切比率自台账首事件"
           "（2026-09-14 上线）起算；本报告是事件之上的派生视图，按需再生。"]
    rates, lows = sec_acceptance(acc, out)
    out.append("")
    sec_retrieval(ret, out)
    out.append("")
    sec_consumption(cons, out)
    out.append("")
    sec_band(acc, ret, out)
    out.append("")
    sec_prune(cons, out, lows)
    if cq:
        out.append("")
        out.append(f"附：选材 Gate 查询 {len(cq)} 次"
                   "（明细在 corpus_query.jsonl，此处略）。")
    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(
        description="fitness 策展报告（台账之上的派生视图，只报不改）")
    sub = ap.add_subparsers(dest="cmd")
    p = sub.add_parser("report", help="生成五节报告")
    p.add_argument("--days", type=int, default=0, help="窗口天数（0=全部）")
    p.add_argument("--out", default=None, help="写文件（默认仅 stdout）")
    p.add_argument("--home", default=None, help="台账目录覆盖（测试用）")
    args = ap.parse_args()
    if args.cmd != "report":
        ap.print_help()
        return 2
    text = build_report(args.days, args.home)
    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.out).write_text(text, encoding="utf-8", newline="\n")
        print(f"[written] {args.out}")
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
