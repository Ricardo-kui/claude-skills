#!/usr/bin/env python3
"""resolve_lineup.py — 跨模型对抗阵容解析器（lineup-protocol v1.1 的可执行实现）.

用法:
  python resolve_lineup.py --registry <models-dump.txt> \
      --slots identification,construct,theory,scope,alternative,contribution,referee \
      [--lineup balanced|cheap|max|single] \
      [--models "theory=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5"] \
      [--require-distinct-debaters] [--out lineup.json]

registry 输入 = `subagent({action:"models"})` 输出原样保存的文本（容忍截断）。
输出 JSON: {lineup, degraded, degraded_reason, slots:[{slot,role,model,family,tier,provider,fallback_chain}], notes}。
退出码: 0 正常; 2 校验错误（裁判隔离 / 手动 A-B 同族 / 未知槽位 / 发现失败）。

不变量（优先级）: ①裁判家族∉辩手家族（自动分配恒保证；手动违反→报错）
②tod A/B 异族（手动违反→报错；≤2 家族自动降级→放行+标注） ③辩手家族尽量唯一（偏好，非门禁）。
④裁判回退链 fail-closed：仅在原裁判家族内换模型，耗尽→orchestrator 自审；绝不进入辩手家族。
  session-default 仅当不属裁判家族时可入辩手链（同属裁判家族则跳过并标注，保运行时隔离）。
目录表只是候选偏好，可用性以 registry + 派发时验证为准；绝不读 auth.json / models-store.json。
"""
import argparse
import json
import re
import sys

# ── 候选目录快照（lineup-protocol §1；只是偏好，不是可用性） ─────────────────
CATALOG_ORDER = ["GLM", "DeepSeek", "GPT", "Claude", "Gemini", "Grok", "Kimi"]
REFEREE_PREF = ["Claude", "GPT"]  # 旗舰裁判偏好序，其余按目录序
TIER_RANK = {"high": 2, "mid": 1, "cheap": 0}

STEM_RULES = [  # id 词干 → 家族（未知词干返回 None：不造虚假家族、不入池）
    (r"^(glm|zai)", "GLM"),
    (r"^deepseek", "DeepSeek"),
    (r"^(gpt|codex|o[134])", "GPT"),
    (r"^(claude|fable|anthropic)", "Claude"),
    (r"^(gemini|gemma)", "Gemini"),
    (r"^grok", "Grok"),
    (r"^(kimi|moonshot|k3)", "Kimi"),
    (r"^mai", "MAI"),
]
TIER_SUFFIX = [  # 未知 id 档位启发式
    (r"(flash|luna|haiku|nano|mini|air|lite)", "cheap"),
    (r"(opus|sol|astra|fable|ultra|max|pro-max)", "high"),
]
CATALOG_TIERS = {  # 目录中明确列出 id 的档位（覆盖启发式）
    "glm-5.3": "mid", "glm-5.3-flash": "cheap",
    "deepseek-v4-pro": "mid", "deepseek-flash": "cheap",
    "gpt-5.6-terra": "mid", "gpt-5.6-luna": "cheap", "gpt-5.6-sol": "high", "gpt-5.5": "high",
    "claude-sonnet-5": "mid", "claude-haiku-4.5": "cheap", "claude-opus-5": "high",
    "gemini-3.8-flash": "cheap",
    "grok-4.6": "mid", "grok-4.5": "mid",
    "kimi-k3": "mid", "k3": "mid", "kimi-for-coding": "cheap",
}


NON_MODEL_STEMS = re.compile(r"^(auto|default|composer)")  # 占位/自动路由 id，非具体模型


def family_of(model_id):
    low = model_id.lower()
    if NON_MODEL_STEMS.match(low):
        return None
    for pat, fam in STEM_RULES:
        if re.match(pat, low):
            return fam
    return None  # 未知词干不造虚假家族（协议 §1：未知跳过）


def tier_of(model_id):
    low = model_id.lower()
    base = re.sub(r"@.*$", "", low)
    if base in CATALOG_TIERS:
        return CATALOG_TIERS[base]
    for pat, tier in TIER_SUFFIX:
        if re.search(pat, low):
            return tier
    return "mid"


def parse_registry(text):
    """解析 action:models 输出 → (models, session_model, truncated)。容忍噪声与截断。"""
    session_model = None
    m = re.search(r"Current session model:\s*\n\s+(\S+/\S+)", text)
    if m:
        session_model = m.group(1)
    truncated = bool(re.search(r"\.\.\. and \d+ more", text))
    body = text
    hdr = re.search(r"Available models[^\n]*:", text)
    if hdr:
        body = text[hdr.end():]
    models, seen = [], set()
    for line in body.splitlines():
        mm = re.match(r"^\s*[`'\"]?([A-Za-z0-9][\w.-]*)/([\w][\w.*-]*)[`'\"]?\s*$", line)
        if mm:
            pid = f"{mm.group(1)}/{mm.group(2)}"
            if pid not in seen:
                seen.add(pid)
                models.append(pid)
    return models, session_model, truncated


def prefer(pid):
    """provider 偏好: 非 cursor(0) 优先于 cursor(1)。"""
    return 1 if pid.split("/", 1)[0].startswith("cursor") else 0


def build_family_pool(models, session_model):
    """→ {family: [entry]}，每家族按 (档位降序, provider 偏好) 排好。会话模型入池兜底。"""
    pool = {}
    for pid in models:
        provider, mid = pid.split("/", 1)
        fam = family_of(mid)
        if fam:
            pool.setdefault(fam, []).append(
                {"model": pid, "tier": tier_of(mid), "provider": provider, "source": "registry"})
    if session_model:
        sp, sid = session_model.split("/", 1)
        fam = family_of(sid)
        if fam and not any(e["model"] == session_model for e in pool.get(fam, [])):
            pool.setdefault(fam, []).append(
                {"model": session_model, "tier": tier_of(sid), "provider": sp, "source": "session"})
    for fam in pool:
        pool[fam].sort(key=lambda e: (-TIER_RANK[e["tier"]], prefer(e["model"])))
    return pool


def family_sort_key(fam):
    return ((REFEREE_PREF.index(fam) if fam in REFEREE_PREF else len(REFEREE_PREF)),
            CATALOG_ORDER.index(fam) if fam in CATALOG_ORDER else len(CATALOG_ORDER),
            fam)


def pick_model(family_entries, tier):
    """家族内选目标档位；缺失时 balanced/max 取最高可用，cheap 取最低可用。"""
    for e in family_entries:
        if e["tier"] == tier:
            return e
    best_rank = (min if tier == "cheap" else max)(TIER_RANK[e["tier"]] for e in family_entries)
    return next(e for e in family_entries if TIER_RANK[e["tier"]] == best_rank)


def find_debater_candidate(pool, avail_fams, used_fams, used_models, tier):
    """辩手四轮检索: 未用家族同档 → 未用家族异档(取最高) → 已用家族同档异模 → 已用家族异档异模。
    返回 (family, entry, reused)；四轮皆空返回 (None, None, False)。"""
    for f in avail_fams:  # R1: 未用家族 + 目标档
        if f not in used_fams:
            for e in pool[f]:
                if e["tier"] == tier:
                    return f, e, False
    for f in avail_fams:  # R2: 未用家族 + 异档（最高可用）
        if f not in used_fams:
            for e in pool[f]:
                if e["tier"] != tier:
                    return f, e, False
    for f in avail_fams:  # R3: 已用家族 + 同档异模
        if f in used_fams:
            for e in pool[f]:
                if e["tier"] == tier and e["model"] not in used_models:
                    return f, e, True
    for f in avail_fams:  # R4: 已用家族 + 异档异模
        if f in used_fams:
            for e in sorted(pool[f], key=lambda x: -TIER_RANK[x["tier"]]):
                if e["model"] not in used_models:
                    return f, e, True
    return None, None, False


def emit(result, out):
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            f.write(text + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--registry", help="action:models 输出保存的文本文件（可省略：此时须 --models 全量或 --lineup single）")
    ap.add_argument("--slots", required=True, help="逗号分隔槽位名（辩手槽任意名，裁判槽必须叫 referee）")
    ap.add_argument("--lineup", default="balanced", choices=["balanced", "cheap", "max", "single"])
    ap.add_argument("--models", default="", help='命名槽位覆盖，如 "theory=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5"')
    ap.add_argument("--require-distinct-debaters", action="store_true", help="tod 模式：手动指定的两个辩手槽不得同家族")
    ap.add_argument("--out", help="把 JSON 同时写入该文件")
    args = ap.parse_args()

    slots = [s.strip() for s in args.slots.split(",") if s.strip()]
    err = lambda msg: (print(json.dumps({"error": msg}, ensure_ascii=False), file=sys.stderr), sys.exit(2))
    if not slots or "referee" not in slots:
        err("slots 必须包含 referee 槽位")
    debater_slots = [s for s in slots if s != "referee"]

    manual = {}
    for part in re.split(r"[,，]", args.models):
        part = part.strip()
        if not part:
            continue
        if "=" not in part:
            err(f"--models 条目缺少 '=': {part}（命名槽位格式 slot=provider/id）")
        slot, model = part.split("=", 1)
        slot, model = slot.strip(), model.strip()
        if slot not in slots:
            err(f"未知槽位 '{slot}'；合法槽位: {', '.join(slots)}")
        if slot in manual:
            err(f"槽位 '{slot}' 重复指定")
        if "/" not in model:
            err(f"槽位 '{slot}' 的模型 '{model}' 缺 provider 前缀（须 provider/id 全称）")
        manual[slot] = model

    notes = []
    models, session_model, truncated = [], None, False
    if args.registry:
        try:
            with open(args.registry, encoding="utf-8", errors="replace") as f:
                models, session_model, truncated = parse_registry(f.read())
        except OSError as e:
            err(f"registry 文件不可读: {e}")
        if truncated:
            notes.append("registry dump 截断（'... and N more'）：不在 dump 中的候选仍保留，派发时验证兜底")
    else:
        notes.append("未提供 registry：--models 命名覆盖未经可用性验证")

    if args.lineup == "single":
        emit({"lineup": "single", "degraded": False, "degraded_reason": "single by request",
              "slots": [{"slot": s, "role": "referee" if s == "referee" else "debater",
                         "model": "session-default", "family": "-", "tier": "-",
                         "provider": "-", "fallback_chain": []} for s in slots],
              "notes": notes + ["裁判=编排者自审（single 档）"]}, args.out)
        return

    pool = build_family_pool(models, session_model) if (models or session_model) else {}
    if not pool and len(manual) < len(slots):
        err("无法发现可用模型（registry 为空/不可解析）：提供 --registry，或全量 --models，或 --lineup single")

    entries = {}
    for slot, pid in manual.items():
        provider, mid = pid.split("/", 1)
        entries[slot] = {"slot": slot, "role": "referee" if slot == "referee" else "debater",
                         "model": pid, "family": family_of(mid), "tier": tier_of(mid),
                         "provider": provider, "fallback_chain": [], "manual": True}
        if pool and not any(pid == e["model"] for es in pool.values() for e in es):
            notes.append(f"槽位 '{slot}' 手动模型 {pid} 不在 registry dump 中（可能截断），派发时验证")

    ref_fam = entries.get("referee", {}).get("family")
    auto_fams = sorted(pool, key=family_sort_key)

    if len(auto_fams) <= 1 and "referee" not in entries:
        # 单家族路径（协议 §5）：裁判回编排者，辩手用唯一家族（或会话默认）
        notes.append("可用家族 ≤1：跨模型关闭，裁判回编排者自审")
        for s in slots:
            if s == "referee":
                entries[s] = {"slot": s, "role": "referee", "model": "orchestrator",
                              "family": "-", "tier": "-", "provider": "-", "fallback_chain": []}
            elif s not in entries:
                if auto_fams:
                    e = pick_model(pool[auto_fams[0]], {"balanced": "mid", "cheap": "cheap", "max": "high"}[args.lineup])
                    entries[s] = {"slot": s, "role": "debater", "model": e["model"], "family": auto_fams[0],
                                  "tier": e["tier"], "provider": e["provider"], "fallback_chain": []}
                else:
                    entries[s] = {"slot": s, "role": "debater", "model": "session-default",
                                  "family": "-", "tier": "-", "provider": "-", "fallback_chain": []}
        emit({"lineup": "manual" if manual else args.lineup, "base_lineup": args.lineup,
              "degraded": True, "degraded_reason": "single-family fallback",
              "slots": [entries[s] for s in slots], "notes": notes, "session_model": session_model}, args.out)
        return

    if "referee" not in entries:  # 裁判优先：偏好序预留旗舰家族（隔离在分配辩手之前成立）
        with_high = [f for f in auto_fams if any(e["tier"] == "high" for e in pool[f])]
        cand = with_high or auto_fams
        ref_fam = cand[0] if cand else None
        if ref_fam is None:
            err("registry 中无可分配家族：改用 --lineup single")
        if not with_high:
            notes.append(f"无 high 档家族：裁判用 {ref_fam} 最强可用档顶替")
        e = pick_model(pool[ref_fam], "high")
        entries["referee"] = {"slot": "referee", "role": "referee", "model": e["model"],
                              "family": ref_fam, "tier": e["tier"], "provider": e["provider"],
                              "fallback_chain": []}
    elif ref_fam is None:
        notes.append("裁判模型家族未知（词干未匹配）：隔离无法静态校验，派发时验证兜底")

    # 辩手自动分配（目录序避开裁判家族与手动占用家族；耗尽后四轮复用）
    lineup_tier = {"balanced": "mid", "cheap": "cheap", "max": "high"}[args.lineup]
    used_models = {e["model"] for e in entries.values()}
    used_fams = {e["family"] for e in entries.values() if e["role"] == "debater"}
    avail_fams = [f for f in auto_fams if f != ref_fam]
    shared_instances = 0
    for s in debater_slots:
        if s in entries:
            continue
        if not avail_fams:
            entries[s] = {"slot": s, "role": "debater", "model": "session-default",
                          "family": "-", "tier": "-", "provider": "-", "fallback_chain": []}
            notes.append(f"槽位 '{s}' 无可用辩手家族：降为会话默认模型")
            continue
        fam, e, reused = find_debater_candidate(pool, avail_fams, used_fams, used_models, lineup_tier)
        if e is None:  # 家族与模型全部耗尽 → 共享实例（保槽位）
            fam = avail_fams[0]
            e = pick_model(pool[fam], lineup_tier)
            shared_instances += 1
            entries[s] = {"slot": s, "role": "debater", "model": e["model"], "family": fam,
                          "tier": e["tier"], "provider": e["provider"], "fallback_chain": []}
            continue
        entries[s] = {"slot": s, "role": "debater", "model": e["model"], "family": fam,
                      "tier": e["tier"], "provider": e["provider"], "fallback_chain": []}
        used_models.add(e["model"])
        used_fams.add(fam)
    if shared_instances:
        notes.append(f"{shared_instances} 槽共享同一模型实例（家族模型耗尽，保槽位优先）")

    # ── 不变量校验 ──
    deb_fams = {s: entries[s]["family"] for s in debater_slots}
    conflicts = []
    if ref_fam and ref_fam in deb_fams.values():
        bad = [s for s, f in deb_fams.items() if f == ref_fam]
        conflicts.append(f"裁判家族 {ref_fam} 同时用于辩手槽 {bad}（违反隔离不变量①）")
    if args.require_distinct_debaters:
        seen = {}
        for s, f in deb_fams.items():
            if f is None:
                continue
            if f in seen:
                pair_manual = entries[s].get("manual") and entries[seen[f]].get("manual")
                if pair_manual:
                    conflicts.append(f"辩手槽 {seen[f]}+{s} 手动指定同家族 {f}（违反 A/B 异族不变量②）")
                else:
                    notes.append(f"辩手槽 {seen[f]}+{s} 同家族 {f}（家族不足的自动降级；裁判仍隔离）")
            seen[f] = s
    toc_same = [f"{a}+{b}" for a in deb_fams for b in deb_fams
                if a < b and deb_fams[a] == deb_fams[b] and deb_fams[a] is not None
                and (entries[a].get("manual") or entries[b].get("manual"))]
    if toc_same and not args.require_distinct_debaters:
        notes.append(f"手动指定的辩手槽存在同家族: {toc_same}（不变量③为偏好，放行并标注）")
    if conflicts:
        err(" | ".join(conflicts) + " —— 请修正 --models 或改用 --lineup single")

    # ── 降级状态（协议 §5） ──
    fam_set = set(f for f in list(deb_fams.values()) + [ref_fam] if f)
    n_deb, uniq_deb = len(deb_fams), len(set(deb_fams.values()))
    if len(fam_set) == 2:
        degraded, reason = "partial", "2 families: referee isolated, debaters same-family"
    elif uniq_deb < n_deb or shared_instances:
        degraded, reason = "partial", f"family reuse: {n_deb - uniq_deb} 槽" + (f"；{shared_instances} 共享实例" if shared_instances else "")
    else:
        degraded, reason = False, ""

    # ── fallback 链 ──
    # 辩手：同家族 ≤2 → 跨家族每族 1 席（排除裁判家族）→ session-default（仅当不属裁判家族）。
    # 裁判 fail-closed：仅原裁判家族内换模型（会话模型同族时已经由家族池入链）→ 末位 orchestrator；
    # 绝不进入辩手家族；耗尽动作标注 fallback_exhausted_action。
    sess_fam = family_of(session_model.split("/", 1)[1]) if session_model else None
    sess_skipped = False
    for s in slots:
        me = entries[s]
        if me["model"] in ("session-default", "orchestrator"):
            continue
        same = [e["model"] for e in pool.get(me["family"], []) if e["model"] != me["model"]]
        if me["role"] == "referee":
            chain = same[:5]
            chain.append("orchestrator")
            me["fallback_chain"] = chain
            me["fallback_exhausted_action"] = "orchestrator"
            continue
        fam_order = sorted((f2 for f2 in pool if f2 != me["family"]), key=family_sort_key)
        groups = [[f2 for f2 in fam_order if f2 != ref_fam]]
        others = []
        for grp in groups:
            # 跨族每族 1 席（该族最高档），族间按档位降序、同档保家族偏好序
            picks = [(pool[f2][0]["tier"], pool[f2][0]["model"], i) for i, f2 in enumerate(grp) if pool[f2]]
            for tier, model, _ in sorted(picks, key=lambda t: (-TIER_RANK[t[0]], t[2])):
                others.append(model)
        chain = (same[:2] + others)[:5]
        if session_model and session_model != me["model"] and session_model not in chain:
            if sess_fam and sess_fam == ref_fam:
                sess_skipped = True
            else:
                chain.append("session-default:" + session_model)
        me["fallback_chain"] = chain
    if sess_skipped:
        notes.append(f"session-default 属裁判家族 {ref_fam}：未放入辩手回退链（保运行时隔离）")

    emit({"lineup": "manual" if manual else args.lineup, "base_lineup": args.lineup,
          "degraded": degraded, "degraded_reason": reason,
          "slots": [entries[s] for s in slots], "notes": notes, "session_model": session_model}, args.out)


if __name__ == "__main__":
    main()
