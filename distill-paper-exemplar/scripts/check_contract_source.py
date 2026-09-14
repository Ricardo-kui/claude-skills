#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_contract_source.py — 蒸馏家族契约源漂移守卫（B 项，2026-09-14）

单一职责：校验「子代理输出契约」的载体结构未被破坏。契约正文唯一活载体 =
l1-subagent-protocol.md「子代理输出契约」节（由 distill-agents 四个 agent 定义
spawn 时 Read 自举加载）；分发消息只填 WHAT。本脚本不校验契约内容对错，只校验
载体结构与单一源纪律：

  C1 双路径同一性   .claude\\skills\\* 与 claude-skills\\* 五组 skill 哨兵文件一致
  C2 分发模板苗条   「分发消息」fence 不含契约正文（两档匹配：FAIL/WARN）
  C3 契约节在位     「子代理输出契约」节含必需条款（防过度瘦身误删真契约）
  C4 agent 定义同步 四份 distill-agents/agents/*.md 硬护栏行一致 + 双 Read 指针在位
  C5 四节对齐       四份 phase-4 头部「产出格式」「写回执行权」块逐字一致；
                    四节 skill 树无写回器调用模式、phase-4 无 candidates: 模板残留
  C6 源↔缓存        distill-agents 源与插件缓存 diff（WARN-only，缓存更新走 GUI）

用法：
  py check_contract_source.py                        # 全量源检查，exit 0 / 5
  py check_contract_source.py --check-dispatch <pdm根yaml或工作目录>
                                                     # 行为级：扫描 dispatch/*.prompt.txt
  py check_contract_source.py --selftest             # 篡改夹具自检（不触真树）

exit：0 通过 / 5 存在 FAIL / 2 用法错误。WARN 只提示不影响退出码。
"""
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

SKILLS = [
    "distill-paper-exemplar",
    "distill-introduction-exemplar",
    "distill-theory-exemplar",
    "distill-methods-exemplar",
    "distill-results-exemplar",
]
SECTIONS = ["introduction", "theory", "methods", "results"]
PREFIX_A = Path(r"C:\Users\huawei\.claude\skills")
PREFIX_B = Path(r"C:\Users\huawei\claude-skills")
PROTOCOL_REL = Path("distill-paper-exemplar/references/l1-subagent-protocol.md")
AGENTS_SRC = PREFIX_B / "distill-agents"
CACHE_ROOT = Path(r"C:\Users\huawei\.zcode\cli\plugins\cache\huawei-skills-local\distill-agents")
PHASE4_REL = "references/phase-4-validation-writeback.md"
GUARD_MARK = "硬护栏"

# C2/C-check-dispatch 两档匹配：硬 token / 调用模式 / 契约逐字句 = FAIL；软词 = WARN
HARD_TOKENS = ["block_text", "index_note", "dedup.verdict", "anchor.file",
               "registry_dimension", "corpus_writeback", "items:", "identity: {",
               "≤20 行紧凑摘要"]
INVOCATION_RE = re.compile(r"(py|python)\s+\S*corpus_writeback\.py\s+--")
CANDIDATES_TEMPLATE_RE = re.compile(r"^\s*>?\s*candidates:\s*$", re.M)
SOFT_TOKENS = ["identity", "≤20"]
# 退役 schema 家族（B 项核查新增）：以现行语气复现 = 形状契约残留
RETIRED_SCHEMA_TOKENS = ["skill_update_instructions", "skill_main_skeleton_update"]


def norm(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path: Path) -> str:
    return norm(path.read_text(encoding="utf-8", errors="replace"))


def findings_add(out: list, severity: str, code: str, msg: str) -> None:
    out.append((severity, code, msg))


# ---------- 纯检查函数（selftest 直接喂篡改文本） ----------

def fence_after(heading_marker: str, text: str) -> str:
    """取 heading_marker 所在行之后第一个 ``` fence 的内容；找不到返回 ''。"""
    idx = text.find(heading_marker)
    if idx < 0:
        return ""
    first = text.find("```", idx)
    if first < 0:
        return ""
    second = text.find("```", first + 3)
    if second < 0:
        return ""
    return text[first + 3:second]


def section_between(start_marker: str, text: str) -> str:
    """取 start_marker 所在行起到下一个 '## ' 标题（或文末）的内容。"""
    idx = text.find(start_marker)
    if idx < 0:
        return ""
    nxt = text.find("\n## ", idx + len(start_marker))
    return text[idx:nxt] if nxt >= 0 else text[idx:]


def check_template_slim(text: str) -> list:
    out = []
    fence = fence_after("## 分发消息", text)
    if not fence.strip():
        findings_add(out, "FAIL", "C2", "「分发消息」节无模板 fence——模板丢失或被改名")
        return out
    for tok in HARD_TOKENS:
        if tok in fence:
            findings_add(out, "FAIL", "C2", f"分发模板含契约 token「{tok}」——契约条款被回填进 WHAT 模板")
    for tok in SOFT_TOKENS:
        if tok in fence:
            findings_add(out, "WARN", "C2", f"分发模板含软词「{tok}」——确认属合法 WHAT 用途（如 identity 预填 provisional）")
    if INVOCATION_RE.search(fence):
        findings_add(out, "FAIL", "C2", "分发模板含写回器调用模式")
    return out


C3_REQUIRED = [
    ("sections/<section>.json", "clause1: section JSON 落盘要求"),
    ("identity", "clause1: identity 顶层字段"),
    ("不得运行 corpus_writeback.py", "clause2: 写回禁令"),
    ("≤20 行紧凑摘要", "clause3: 摘要格式"),
    ("plan 条目字段契约", "clause2: 指向 §plan 字段契约的指针"),
    ("禁止把条款回填进分发消息模板", "治理语"),
]


def check_contract_section(text: str) -> list:
    out = []
    sec = section_between("## 子代理输出契约", text)
    if not sec.strip():
        findings_add(out, "FAIL", "C3", "「子代理输出契约」节缺失")
        return out
    for marker, what in C3_REQUIRED:
        if marker not in sec:
            findings_add(out, "FAIL", "C3", f"契约节缺必需条款（{what}）——被过度瘦身误删")
    return out


def check_agent_defs(defs: dict) -> list:
    out = []
    if len(defs) != len(SECTIONS):
        findings_add(out, "FAIL", "C4", f"agent 定义缺文件：现有 {sorted(defs)}")
        return out
    guards = {}
    for sec, text in defs.items():
        line = next((ln for ln in text.splitlines() if GUARD_MARK in ln), "")
        if not line:
            findings_add(out, "FAIL", "C4", f"distill-{sec}.md 缺「{GUARD_MARK}」行")
        guards[sec] = line
        if "l1-subagent-protocol.md" not in text:
            findings_add(out, "FAIL", "C4", f"distill-{sec}.md 缺协议 Read 指针（自举断链）")
        if "SKILL.md" not in text:
            findings_add(out, "FAIL", "C4", f"distill-{sec}.md 缺分节 SKILL.md Read 指针")
        if f"sections/{sec}.json" not in text:
            findings_add(out, "FAIL", "C4", f"distill-{sec}.md 输出路径与节名不符")
        if "≤20" not in text:
            findings_add(out, "FAIL", "C4", f"distill-{sec}.md 缺 ≤20 行摘要约束")
    unique = set(guards.values())
    if len(unique) > 1:
        findings_add(out, "FAIL", "C4", "四份硬护栏行不再逐字一致——同步后再改契约")
    return out


def blockquote_block(marker: str, text: str) -> str:
    """取含 marker 的 '> ' 连续块；空引用行（裸 '>'，注释分隔符）即块终止。"""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if marker in ln:
            out = []
            j = i
            while j < len(lines):
                cur = lines[j]
                if not cur.lstrip().startswith(">") or cur.strip() == ">":
                    break
                out.append(cur)
                j += 1
            return "\n".join(out)
    return ""


def check_phase4_blocks(texts: dict) -> list:
    out = []
    for marker, label in [("产出格式", "产出格式块"), ("写回执行权", "写回执行权块")]:
        blocks = {sec: blockquote_block(f"{marker}（", t) for sec, t in texts.items()}
        missing = [s for s, b in blocks.items() if not b]
        if missing:
            findings_add(out, "FAIL", "C5", f"{label}缺失于：{missing}")
            continue
        unique = set(blocks.values())
        if len(unique) > 1:
            findings_add(out, "FAIL", "C5", f"四份 phase-4「{marker}」块不再逐字一致——对齐块被单方面改动")
    return out


def scan_md_texts(texts: dict, with_candidates: bool = False) -> list:
    out = []
    for path, text in texts.items():
        if INVOCATION_RE.search(text):
            findings_add(out, "FAIL", "C5", f"写回器调用模式残留：{path}")
        if with_candidates and CANDIDATES_TEMPLATE_RE.search(text):
            findings_add(out, "FAIL", "C5", f"candidates: 模板残留：{path}")
    return out


def check_retired_schema(tree: dict) -> list:
    """退役 schema 家族：phase-4 文件允许 ≤1 次（退役映射注记），
    四节 skill 树其余 md 文件 0 次——以现行语气复现即 FAIL。"""
    out = []
    for path, text in tree.items():
        n = sum(text.count(tok) for tok in RETIRED_SCHEMA_TOKENS)
        limit = 1 if path.replace("\\", "/").endswith(
            "references/phase-4-validation-writeback.md") else 0
        if n > limit:
            findings_add(out, "FAIL", "C5", f"退役 schema 家族复现（{n} 次，上限 {limit}）：{path}")
    return out


# ---------- 组装真实输入 ----------

def gather() -> int:
    out = []

    # C1 双路径哨兵
    sentinels = {SKILLS[0]: ["SKILL.md", str(PROTOCOL_REL.relative_to(SKILLS[0]))]}
    for s in SKILLS[1:]:
        sentinels[s] = ["SKILL.md", PHASE4_REL]
    for skill, files in sentinels.items():
        for f in files:
            pa, pb = PREFIX_A / skill / f, PREFIX_B / skill / f
            if not (pa.exists() and pb.exists()):
                findings_add(out, "FAIL", "C1", f"哨兵缺失：{skill}/{f}（A={pa.exists()} B={pb.exists()}）")
            elif sha(pa) != sha(pb):
                findings_add(out, "FAIL", "C1", f"双路径漂移：{skill}/{f} 两副本不一致（junction 断裂？）")

    # 协议
    proto_path = PREFIX_A / PROTOCOL_REL
    if not proto_path.exists():
        findings_add(out, "FAIL", "C0", f"协议文件缺失：{proto_path}")
        report(out)
        return 5
    proto = read(proto_path)
    out.extend(check_template_slim(proto))
    out.extend(check_contract_section(proto))

    # C4 agent 定义（源）
    defs = {}
    for sec in SECTIONS:
        p = AGENTS_SRC / "agents" / f"distill-{sec}.md"
        if p.exists():
            defs[sec] = read(p)
        else:
            findings_add(out, "FAIL", "C4", f"agent 定义缺失：{p}")
    out.extend(check_agent_defs(defs))

    # C5 四节 phase-4 + 全树调用扫描
    p4 = {}
    tree = {}
    for sec in SECTIONS:
        skill = f"distill-{sec}-exemplar"
        p4_path = PREFIX_A / skill / PHASE4_REL
        if p4_path.exists():
            p4[sec] = read(p4_path)
        else:
            findings_add(out, "FAIL", "C5", f"phase-4 缺失：{p4_path}")
        root = PREFIX_A / skill
        for p in sorted(root.rglob("*.md")):
            tree[f"{skill}/{p.relative_to(root)}"] = read(p)
    out.extend(check_phase4_blocks(p4))
    out.extend(scan_md_texts(tree))
    out.extend(scan_md_texts({f"phase4[{s}]": t for s, t in p4.items()}, with_candidates=True))
    out.extend(check_retired_schema(tree))

    # C6 源↔缓存（WARN-only）
    src_plugin = AGENTS_SRC / ".zcode-plugin" / "plugin.json"
    try:
        src_ver = json.loads(src_plugin.read_text(encoding="utf-8"))["version"]
    except Exception:
        src_ver = None
        findings_add(out, "WARN", "C6", f"无法读源版本：{src_plugin}")
    if CACHE_ROOT.exists():
        vers = sorted([d.name for d in CACHE_ROOT.iterdir() if d.is_dir()])
        if src_ver and vers and src_ver not in vers:
            findings_add(out, "WARN", "C6",
                         f"源版本 {src_ver} 不在缓存版本 {vers} 中——改 agent 定义后须 GUI 更新插件")
        cur = CACHE_ROOT / (src_ver if src_ver in vers else (vers[-1] if vers else ""))
        for sec in SECTIONS:
            sp, cp = AGENTS_SRC / "agents" / f"distill-{sec}.md", cur / "agents" / f"distill-{sec}.md"
            if sp.exists() and cp.exists():
                if norm(sp.read_text(encoding="utf-8", errors="replace")) != norm(cp.read_text(encoding="utf-8", errors="replace")):
                    findings_add(out, "WARN", "C6", f"缓存与源不一致：distill-{sec}.md（{cur.name}）")
            elif sp.exists() and not cp.exists():
                findings_add(out, "WARN", "C6", f"缓存缺文件：distill-{sec}.md（{cur.name}）")
    else:
        findings_add(out, "WARN", "C6", f"插件缓存目录不存在：{CACHE_ROOT}")

    report(out)
    return 5 if any(sev == "FAIL" for sev, _, _ in out) else 0


def resolve_dispatch_dirs(target: Path) -> list:
    """目录→自身；<x>.pdm.yaml→同名工作目录 <x>.pdm 优先，其父目录兜底。"""
    if target.is_dir():
        return [target]
    dirs = []
    sib = target.with_suffix("")  # <citekey>.pdm.yaml → <citekey>.pdm
    if sib.is_dir():
        dirs.append(sib)
    dirs.append(target.parent)
    return dirs


def check_dispatch(target: Path) -> int:
    out = []
    tees = []
    checked = []
    for d in resolve_dispatch_dirs(target):
        dispatch = d / "dispatch"
        checked.append(str(dispatch))
        if dispatch.is_dir():
            tees = sorted(dispatch.glob("*.prompt.txt"))
            if tees:
                break
    if not tees:
        print(f"[INFO] 无 dispatch tee（查过 {' ； '.join(checked)}）。"
              f"tee 是 2026-09-14 起新纪律，旧 PDM 无属正常。")
        return 0
    for t in tees:
        text = read(t)
        for tok in HARD_TOKENS:
            if tok in text:
                findings_add(out, "FAIL", "D", f"{t.name} 含契约 token「{tok}」——分发消息夹带了契约正文")
        for tok in SOFT_TOKENS:
            if tok in text:
                findings_add(out, "WARN", "D", f"{t.name} 含软词「{tok}」——人工确认属 WHAT")
        if INVOCATION_RE.search(text):
            findings_add(out, "FAIL", "D", f"{t.name} 含写回器调用模式")
    report(out)
    return 5 if any(sev == "FAIL" for sev, _, _ in out) else 0


def report(out: list) -> None:
    if not out:
        print("CONTRACT SOURCE: ALL GREEN")
        return
    for sev, code, msg in out:
        print(f"[{sev}] ({code}) {msg}")
    n_fail = sum(1 for sev, _, _ in out if sev == "FAIL")
    n_warn = sum(1 for sev, _, _ in out if sev == "WARN")
    print(f"CONTRACT SOURCE: {n_fail} FAIL / {n_warn} WARN")


# ---------- selftest：对纯函数喂篡改夹具 ----------

def selftest() -> int:
    fails = []

    def expect(name: str, cond: bool):
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        if not cond:
            fails.append(name)

    proto = read(PREFIX_A / PROTOCOL_REL)
    base_p4 = {s: read(PREFIX_A / f"distill-{s}-exemplar" / PHASE4_REL) for s in SECTIONS}
    base_defs = {s: read(AGENTS_SRC / "agents" / f"distill-{s}.md") for s in SECTIONS}

    # 1 干净基线全绿
    expect("baseline template slim", check_template_slim(proto) == [])
    expect("baseline contract section", check_contract_section(proto) == [])
    expect("baseline agent defs", check_agent_defs(base_defs) == [])
    expect("baseline phase4 blocks", check_phase4_blocks(base_p4) == [])
    expect("baseline scan", scan_md_texts(base_p4, with_candidates=True) == [])

    # 2 模板回填 block_text → FAIL
    slim = fence_after("## 分发消息", proto)
    expect("tamper template +block_text", any(c == "C2" and "FAIL" == s for s, c, _ in
           check_template_slim(proto.replace(slim, slim + "\nblock_text: x"))))

    # 3 删写回禁令 → C3 FAIL
    expect("tamper contract -prohibition", any(c == "C3" for s, c, _ in
           check_contract_section(proto.replace("不得运行 corpus_writeback.py", "不得自行写回"))))

    # 4 硬护栏行单方面改动 → C4 FAIL
    tampered = dict(base_defs)
    tampered["theory"] = tampered["theory"].replace("py", "python", 1)
    expect("tamper defs guard-line drift", check_agent_defs(tampered) != [])
    expect("tamper defs guard-line drift is C4", any(c == "C4" for s, c, _ in check_agent_defs(tampered)))

    # 5 对齐块单方面改动 → C5 FAIL
    tampered_p4 = dict(base_p4)
    tampered_p4["methods"] = tampered_p4["methods"].replace("2026-09-14 起，单一契约源", "2026-09-14 起，单一契约源 ")
    expect("tamper phase4 block drift", any(c == "C5" for s, c, _ in check_phase4_blocks(tampered_p4)))

    # 6 phase-4 注入写回器调用 → C5 FAIL；注入 candidates: 模板 → C5 FAIL
    evil = dict(base_p4)
    evil["results"] = evil["results"] + "\npy scripts/corpus_writeback.py --plan x\n"
    expect("tamper invocation", any(c == "C5" for s, c, _ in scan_md_texts(evil, with_candidates=True)))
    evil2 = dict(base_p4)
    evil2["results"] = evil2["results"] + "\n> candidates:\n"
    expect("tamper candidates template", any(c == "C5" and "candidates" in m for s, c, m in
           scan_md_texts(evil2, with_candidates=True)))

    # 7 调用模式正则不得误伤禁令句/裸提及
    expect("no false positive on prohibition", INVOCATION_RE.search("子代理一律不得运行 corpus_writeback.py，plan") is None)
    expect("no false positive on bare mention", INVOCATION_RE.search("调用写回执行器 `corpus_writeback.py`（先 dry-run") is None)
    expect("invocation pattern matches", INVOCATION_RE.search("python ../scripts/corpus_writeback.py --plan p") is not None)

    # 8 退役 schema 家族（核查修正新增检查）：phase-4 ≤1 次放行，其余文件 0 容忍
    skill_sk = {s: read(PREFIX_A / f"distill-{s}-exemplar" / "SKILL.md") for s in SECTIONS}
    base_tree = {}
    for s in SECTIONS:
        base_tree[f"distill-{s}-exemplar/SKILL.md"] = skill_sk[s]
        base_tree[f"distill-{s}-exemplar/references/phase-4-validation-writeback.md"] = base_p4[s]
    expect("baseline retired schema", check_retired_schema(base_tree) == [])
    evil_tree = dict(base_tree)
    evil_tree["distill-methods-exemplar/SKILL.md"] += "\nskill_update_instructions 复现"
    expect("tamper retired in SKILL.md", check_retired_schema(evil_tree) != [])
    evil_tree2 = dict(base_tree)
    evil_tree2["distill-theory-exemplar/references/phase-4-validation-writeback.md"] += (
        "\nskill_main_skeleton_update\nskill_update_instructions")
    expect("tamper retired >1 in phase4", check_retired_schema(evil_tree2) != [])

    print(f"SELFTEST: {'ALL GREEN' if not fails else str(len(fails)) + ' FAILED'}")
    return 0 if not fails else 5


def main() -> int:
    ap = argparse.ArgumentParser(description="蒸馏家族契约源漂移守卫")
    ap.add_argument("--check-dispatch", metavar="PDM", help="扫描 <pdm>/dispatch/*.prompt.txt")
    ap.add_argument("--selftest", action="store_true", help="篡改夹具自检（不触真树）")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if args.check_dispatch:
        return check_dispatch(Path(args.check_dispatch))
    return gather()


if __name__ == "__main__":
    sys.exit(main())
