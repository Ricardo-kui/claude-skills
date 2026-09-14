#!/usr/bin/env python3
"""PDM root state operator + gate-①/audit presentation generator (2026-09-14).

Problem 1+3 of the distill-family architecture review: the PDM root
(`<citekey>.pdm.yaml`) is the sole cross-layer handoff artifact, yet every
mutation of it used to be a hand-written `py - <<EOF` YAML surgery, and the
gate-① review table was summarized by reading 30KB+ plans into the main
context. This tool makes both deterministic.

Writer table (single-writer discipline, mirrored in references/pdm-schema.md):
  <citekey>.pdm.yaml scaffold (create-if-missing)   preprocess_l0.py
  <citekey>.pdm.yaml post-L0 mutations              pdm_tool.py  (this file)
  sections/*.md, l0_manifest.json, LOCK             preprocess_l0.py
  sections/<s>.json, feedback/*                     L1 subagents
  writeback_plan.<s>.yaml                           corpus_precheck.py
  write-*/corpus + registries                       corpus_writeback.py +
                                                    rebuild_apply.py (never touched
                                                    here — hard guard below)
  ~/.claude/fitness/** (fitness ledger events +     fitness_ledger.py (called by
    gate-① sheet snapshots; outside both              present/set-gate; fail-open —
    distill-work and the skills tree)                 telemetry never blocks gates)

Commands:
  show          resume-breakpoint view of the PDM (statuses/gates/artifacts/LOCK)
  merge-section merge identity/band from sections/<s>.json into the root (L1)
  merge-cross   write cross_section_identity from an L2 summary yaml (L2)
  set-gate      writeback gate transitions awaiting_confirm→confirmed→written
  set-paper     paper status transitions (+ wb_citekey / root note / ledger note)
  set-story     story_track state machine (L3)
  fail-section  record a section failure root-cause line (protocol: 显式失败)
  present       gate-① batch review sheet / L4 post-write audit sheet
  --selftest    in-process regression over temp fixtures (no real trees)
                  (CLI-level regression: wbtest_pdm_tool_cli.py — real
                   subprocesses, CJK argv, error lifecycle, sweep coupling)

Global invariants: idempotent (same args → no-op), forward-only state machines
(--force + --note to go backward), rolling <root>.bak before every mutation,
pdm_version in files is never bumped, corpus/registry paths hard-refused.

Exit codes: 0 ok (no-op included) · 2 usage/env · 3 contract violation
(state machine, missing artifacts, guard trip, legacy comments without
--force) · 4 plan fail_fast (gate1) / audit found unverified writes or
verify FAIL. STALE anchors annotate but never gate — the review sheet is
exactly where a human looks at them, so they must not block it.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

import yaml

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
CAPABILITY_ROOT = SKILLS_ROOT  # selftest overrides to a temp tree

try:
    from corpus_writeback import wb_block_marker  # single source of the format
except ImportError:  # pragma: no cover - only if scripts/ layout is broken
    def wb_block_marker(paper: str, item: str) -> str:
        return f"<!-- wb:{paper}:{item} -->"

SECTIONS = ("introduction", "theory", "methods", "results")
SECTION_ALIASES = {"intro": "introduction", "i": "introduction",
                   "t": "theory", "m": "methods", "r": "results"}

GATE_ORDER = {"awaiting_confirm": 0, "confirmed": 1, "written": 2}
SECTION_STATUS_ORDER = {"pending": 0, "distilled": 1, "verified": 2}
PAPER_STATUS_ORDER = {"manifest": 0, "distilling": 1, "integrated": 2}
STORY_STATUS_ORDER = {"pending": 0, "card_drafted": 1,
                      "card_confirmed": 2, "validated": 3}

# Ground truth = preprocess_l0.scaffold_pdm_root (2026-09-13). Extra keys seen
# in practice (e.g. methods estimator_family in mao_dong_lee_2022_msom) are
# captured as optional, never required.
REQUIRED_IDENTITY = {
    "introduction": ("gap_type", "contribution_dimension"),
    "theory": ("theory_building_type",),
    "methods": ("design_family",),
    "results": ("estimator_family",),
}
IDENTITY_POINTERS = {  # fallback lookups into the section json, first non-empty
    "introduction": {"gap_type": ["identity.gap_type", "gap_type"],
                     "contribution_dimension": ["identity.contribution_dimension",
                                                "contribution_dimension"]},
    "theory": {"theory_building_type": ["identity.theory_building_type",
                                        "theory_building_type", "theory_build_type"]},
    "methods": {"design_family": ["identity.design_family", "design_family",
                                  "phase_0.design_type"],
                "estimator_family": ["identity.estimator_family", "estimator_family",
                                     "phase_0.estimator_family"]},
    "results": {"estimator_family": ["identity.estimator_family", "estimator_family",
                                     "phase_0.estimator_family"],
                "design_family": ["identity.design_family", "design_family"]},
}
CROSS_KEYS = ("gap_type", "theory_building_type", "design_family",
              "estimator_family", "coherence", "flags")
CANONICAL_COMMENT_PREFIXES = ("# PDM root", "# main loop owns", "# post-L0 mutations")
ROOT_HEADER = (
    "# PDM root — auto-scaffolded by preprocess_l0.py (create-if-missing;\n"
    "# main loop owns this file afterwards: identity/status/writeback merges).\n"
    "# post-L0 mutations: pdm_tool.py only, hand edits are a protocol breach.\n"
)
FORBIDDEN_PATH_RE = re.compile(
    r"write-(introduction|theory|methods|results)[/\\]corpus|_evidence_registry", re.I)


def die(code: int, msg: str) -> None:
    print(f"ERROR({code}): {msg}", file=sys.stderr)
    raise SystemExit(code)


def guard_path(p: Path | str, what: str) -> None:
    if FORBIDDEN_PATH_RE.search(str(p)):
        die(3, f"守卫 trip：{what} 落在 corpus/registry 派生领地（A 项单写者），"
               f"pdm_tool 禁止触碰：{p}")


def as_dict(v) -> dict:
    """Legacy roots sometimes hold scalar/string values where the schema wants
    a mapping — show must survive them (mutation commands still enforce)."""
    return v if isinstance(v, dict) else {}


def trunc(s: str, n: int) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def norm_section(v: str) -> str:
    s = SECTION_ALIASES.get(str(v).lower(), str(v).lower())
    if s not in SECTIONS:
        die(2, f"未知 section：{v!r}（可选 {SECTIONS} 或 intro/t/m/r 缩写）")
    return s


def parse_sections(v: str | None) -> list[str]:
    if not v:
        return list(SECTIONS)
    return [norm_section(x) for x in re.split(r"[,，\s]+", v) if x]


# ---------------------------------------------------------------- root IO --

def comment_lines(text: str) -> list[str]:
    return [ln.rstrip() for ln in text.splitlines() if ln.lstrip().startswith("#")]


def legacy_comments(text: str) -> list[str]:
    return [c for c in comment_lines(text)
            if not c.lstrip().startswith(CANONICAL_COMMENT_PREFIXES)]


def load_root(path: Path) -> tuple[dict, str]:
    if not path.is_file():
        die(2, f"PDM 根不存在（骨架由 preprocess_l0.py 创建）：{path}")
    text = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(text)
    except yaml.YAMLError as e:
        die(2, f"PDM 根 YAML 不可解析：{path}\n{e}")
    if not isinstance(data, dict):
        die(2, f"PDM 根不是 YAML 映射：{path}")
    return data, text


def workdir_of(root_path: Path) -> Path:
    return root_path.parent / root_path.stem  # <citekey>.pdm.yaml → <citekey>.pdm


def resolve_workfile(wd: Path, rel: str | None) -> Path | None:
    """Schema has two historical path bases: bare-relative ('sections/x.json',
    distill_track.*) and workdir-prefixed ('<citekey>.pdm/sections/x.md',
    source_provenance.*). Try both, return whichever exists (None if neither)."""
    if not rel:
        return None
    rel = str(rel).replace("\\", "/")
    p1 = wd / rel
    if p1.exists():
        return p1
    p2 = wd / re.sub(rf"^{re.escape(wd.name + '/')}", "", rel)
    if p2.exists():
        return p2
    return p1  # canonical spelling even when absent — caller decides severity


def save_root(root_path: Path, old_text: str, data: dict, force: bool = False) -> bool:
    """Canonical-header, flow-free re-dump of the root. Idempotent: identical
    serialization → no-op. Rolling .bak keeps the pre-mutation text."""
    guard_path(root_path, "PDM 根写路径")
    stale = legacy_comments(old_text)
    if stale and not force:
        die(3, "根文件含非脚手架行内注释（round-trip 会丢失）——确认后加 --force，"
               f"将丢失的注释行：\n  " + "\n  ".join(stale[:10]))
    new_text = ROOT_HEADER + yaml.safe_dump(data, allow_unicode=True, sort_keys=False)
    if new_text == old_text:
        print("no-op（内容未变化）")
        return False
    bak = root_path.with_name(root_path.name + ".bak")
    bak.write_text(old_text, encoding="utf-8")
    fd, tmp = tempfile.mkstemp(dir=str(root_path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(new_text)
        os.replace(tmp, root_path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    print(f"saved: {root_path}  (备份: {bak.name})")
    return True


# ------------------------------------------------------- plan discovery --

def _infer_section(stem: str) -> str | None:
    low = stem.lower()
    for s in SECTIONS:
        if s in low:
            return s
    return None


def discover_plans(wd: Path, root: dict, sections: list[str],
                   explicit: list[str] | None) -> dict[str, Path]:
    """Priority: explicit --plan (accepts 'section=path' or bare path with the
    section name in the stem) > root-registered writeback.plan > convention
    name writeback_plan.<s>.yaml > any *<s>*plan*.yaml glob in the workdir."""
    result: dict[str, Path] = {}
    for spec in explicit or []:
        if "=" in spec and spec.split("=", 1)[0] in SECTIONS:
            sec, p = spec.split("=", 1)
            result[norm_section(sec)] = Path(p)
        else:
            sec = _infer_section(Path(spec).stem)
            if sec is None:
                die(2, f"--plan 无法推断所属节（用 section=path 形式）：{spec}")
            result[sec] = Path(spec)
    for s in sections:
        if s in result:
            continue
        reg = as_dict(as_dict(as_dict(root.get("distill_track")).get(s)).get("writeback"))
        reg_path = reg.get("plan")
        if reg_path:
            cand = Path(reg_path)
            if not cand.is_file():
                cand = wd / str(reg_path)
            if cand.is_file():
                result[s] = cand
                continue
        conv = wd / f"writeback_plan.{s}.yaml"
        if conv.is_file():
            result[s] = conv
            continue
        hits = sorted(wd.glob(f"*{s}*plan*.yaml"))
        if hits:
            result[s] = hits[0]
    return result


def load_plan(path: Path) -> dict:
    try:
        plan = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        die(2, f"plan 不可读/不可解析：{path}\n{e}")
    if not isinstance(plan, dict) or not plan.get("items"):
        die(2, f"plan 无 items 列表（schema 反了？应走 corpus_precheck 生成）：{path}")
    return plan


def plan_verdicts(plan: dict) -> Counter:
    return Counter(((it.get("dedup") or {}).get("verdict") or "?")
                   for it in plan["items"])


def item_target(item: dict, corpus_root: Path | None) -> Path | None:
    for key in ("file_override",):
        v = item.get(key)
        if v:
            p = Path(v)
            if p.is_file():
                return p
            if corpus_root:
                p2 = corpus_root / v
                if p2.is_file():
                    return p2
                hits = list(corpus_root.rglob(v))
                if hits:
                    return hits[0]
    anchor = (item.get("anchor") or {}).get("file")
    if anchor and anchor != "None":
        p = Path(anchor)
        if p.is_file():
            return p
        if corpus_root:
            p2 = corpus_root / str(anchor)
            if p2.is_file():
                return p2
    return None


def anchor_stale(item: dict) -> str:
    if ((item.get("dedup") or {}).get("verdict")) == "SKIP":
        return "–"
    anchor = item.get("anchor") or {}
    f, head = anchor.get("file"), anchor.get("after_heading")
    if not f or not head or f == "None":
        return "–"
    p = Path(f)
    if not p.is_file():
        return "STALE⚠(文件缺)"
    try:
        if head not in p.read_text(encoding="utf-8", errors="replace"):
            return "STALE⚠(锚点行变)"
    except OSError:
        return "STALE⚠(不可读)"
    return "ok"


# ------------------------------------------------------------------ show --

def _lock_age_h(wd: Path) -> str:
    lock = wd / "LOCK"
    if not lock.is_file():
        return "none"
    age_h = (datetime.now().timestamp() - lock.stat().st_mtime) / 3600
    return f"{age_h:.1f}h"


def _plan_line(wd: Path, root: dict, s: str) -> str:
    found = discover_plans(wd, root, [s], None).get(s)
    if not found:
        return "plan:-"
    try:
        c = plan_verdicts(load_plan(found))
    except SystemExit:
        return f"plan:UNREADABLE({found.name})"
    return ("plan:" + found.name
            + f" ADD{c.get('ADD', 0)}/EXT{c.get('EXTEND', 0)}/SKIP{c.get('SKIP', 0)}")


def cmd_show(args) -> int:
    root, _ = load_root(Path(args.pdm))
    wd = workdir_of(Path(args.pdm))
    info = {
        "paper_id": root.get("paper_id"), "title": root.get("title"),
        "status": root.get("status"), "wb_citekey": root.get("wb_citekey", ""),
        "structure_type": as_dict(root.get("source_provenance")).get("structure_type", ""),
        "lock_age_h": _lock_age_h(wd), "sections": {},
    }
    lines = [f"PDM {root.get('paper_id')} — {trunc(root.get('title'), 60)}",
             f"paper.status={root.get('status')} · structure="
             f"{info['structure_type'] or '?'} · wb={info['wb_citekey'] or '(未设)'} · "
             f"LOCK={info['lock_age_h']}"]
    track = root.get("distill_track") or {}
    for s in SECTIONS:
        e = as_dict(as_dict(track).get(s))
        st, gate = e.get("status", "?"), as_dict(e.get("writeback")).get("gate", "-")
        legacy = " LEGACY⚠" if st == "verified" and gate != "written" else ""
        js = resolve_workfile(wd, e.get("section_json"))
        fb = resolve_workfile(wd, e.get("feedback"))
        caps = (f"json{'✓' if js and js.is_file() else '✗'}"
                f"/fb{'✓' if fb and fb.is_file() else ('缺' if e.get('feedback') else '–')}")
        err = f" ERROR:{trunc(e.get('error'), 40)}" if e.get("error") else ""
        line = (f"{s:<13} {st:<10} gate={gate:<17}{legacy} {caps} "
                f"{_plan_line(wd, root, s)} band={trunc(e.get('band'), 34) or '-'}{err}")
        lines.append(line)
        info["sections"][s] = {"status": st, "gate": gate, "legacy": bool(legacy),
                               "band": e.get("band", ""), "error": e.get("error", "")}
    text = "\n".join(lines)
    if getattr(args, "format", "text") == "json":
        print(json.dumps(info, ensure_ascii=False, indent=2))
    else:
        print(text)
    return 0


# --------------------------------------------------------- merge-section --

def _pointer_lookup(data: dict, paths: list[str]) -> str:
    for path in paths:
        cur = data
        for part in path.split("."):
            if not isinstance(cur, dict) or part not in cur:
                cur = None
                break
            cur = cur[part]
        if isinstance(cur, str) and cur.strip():
            return cur.strip()
        if cur is not None and not isinstance(cur, (dict, list)) and cur:
            return str(cur).strip()
    return ""


def feedback_capability(section: str) -> tuple[bool, str]:
    """(infra_exists, cause_label). Runtime detection — the capability table
    lives on disk, not hardcoded (known-friction ① follows infra evolution)."""
    has = (CAPABILITY_ROOT / f"distill-{section}-exemplar"
           / "_update_design_feedback.py").is_file()
    return has, ("能力缺口（该 skill 无 feedback 基建，协议已知摩擦①）" if not has
                 else "运行缺失（有基建但未落盘，需查原因）")


def _merge_ledger(root: dict, section: str, fb_rel: str | None, fb_ok: bool) -> None:
    ledger = root.setdefault("feedback_ledger", {})
    persisted = [p for p in (ledger.get("persisted") or []) if section not in str(p)]
    missing = [m for m in (ledger.get("missing") or []) if section not in str(m)]
    if fb_ok and fb_rel:
        persisted = sorted(set(persisted + [fb_rel]))
    elif fb_rel:
        missing = sorted(set(missing + [fb_rel]))
    ledger["persisted"], ledger["missing"] = persisted, missing
    causes = ledger.setdefault("causes", {})
    if fb_ok:
        causes.pop(section, None)
    else:
        causes[section] = feedback_capability(section)[1]
    ledger["note"] = "；".join(f"{s}: {c}" for s, c in sorted(causes.items()))


def cmd_merge_section(args) -> int:
    root, old = load_root(Path(args.pdm))
    wd = workdir_of(Path(args.pdm))
    section = norm_section(args.section)
    track = root.setdefault("distill_track", {})
    entry = track.setdefault(section, {"skill": f"distill-{section}-exemplar",
                                       "status": "pending"})
    json_path = (Path(args.json) if args.json
                 else resolve_workfile(wd, entry.get("section_json")))
    if not json_path or not json_path.is_file():
        die(3, f"[{section}] sections json 缺失（{json_path}）——该节未完成：走 l1 协议"
               f"的 JSON 修复/重发路径，不要在根上假装 distilled")
    try:
        data = json.loads(json_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError):
        try:
            data = yaml.safe_load(json_path.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            die(3, f"[{section}] section 文件 json/yaml 均不可解析：{json_path}\n{e}")
    if not isinstance(data, dict):
        die(3, f"[{section}] section 文件不是映射：{json_path}")

    identity = {k: v for k, v in (entry.get("identity") or {}).items()
                if str(v or "").strip()}
    for k, v in (data.get("identity") or {}).items():
        if isinstance(v, str) and v.strip():
            identity[k] = v.strip()
        elif v and not isinstance(v, (dict, list)):
            identity[k] = str(v)
    for k in REQUIRED_IDENTITY[section]:
        if not str(identity.get(k) or "").strip():
            hit = _pointer_lookup(data, IDENTITY_POINTERS[section].get(k, [k]))
            if hit:
                identity[k] = hit
    for pair in args.set or []:
        if "=" not in pair:
            die(2, f"--set 需要 k=v 形式：{pair!r}")
        k, v = pair.split("=", 1)
        identity[k.strip()] = v.strip()
    missing = [k for k in REQUIRED_IDENTITY[section]
               if not str(identity.get(k) or "").strip()]
    if missing:
        die(3, f"[{section}] identity 必需键缺失：{missing}——节 json 无 identity 契约"
               f"时从 ≤20 行摘要 --set {missing[0]}=... 补填（摘要才是协议保证的载体）")
    entry["identity"] = identity

    if args.band:
        entry["band"] = args.band
    if (wd / "sections" / f"{section}.report.md").is_file():
        entry["section_report"] = f"sections/{section}.report.md"
    fb_rel = entry.get("feedback") or f"feedback/{section}.feedback.yaml"
    entry["feedback"] = fb_rel
    fb = resolve_workfile(wd, fb_rel)
    _merge_ledger(root, section, fb_rel, bool(fb and fb.is_file()))
    if entry.get("status") == "pending":
        entry["status"] = "distilled"
    if root.get("status") == "manifest":
        root["status"] = "distilling"
    recovered = entry.pop("error", None) is not None  # 重发成功 = 恢复

    save_root(Path(args.pdm), old, root, force=args.force)
    print(f"[{section}] identity: " + json.dumps(identity, ensure_ascii=False))
    print(f"[{section}] band={entry.get('band', '-') or '-'} · "
          f"status={entry['status']} · ledger={root['feedback_ledger']['note'] or '全落盘'}")
    if recovered:
        print(f"[{section}] 先前失败记录（error）已清除——重发成功即恢复")
    return 0


# ------------------------------------------------------------ merge-cross --

def cmd_merge_cross(args) -> int:
    if not args.from_file:
        die(2, "merge-cross 需要 --from <l2.yaml>（flags 是 dict 列表，argv 装不下）")
    root, old = load_root(Path(args.pdm))
    try:
        data = yaml.safe_load(Path(args.from_file).read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        die(2, f"L2 摘要不可读/不可解析：{args.from_file}\n{e}")
    if not isinstance(data, dict):
        die(2, f"L2 摘要不是映射：{args.from_file}")
    block = {k: data.get(k, "" if k != "flags" else []) for k in CROSS_KEYS}
    if not str(block["coherence"] or "").strip():
        die(3, "L2 摘要缺 coherence——先按 cross-section-coherence.md 执行 rubric")
    if block["coherence"] not in ("ok", "flagged", "partial"):
        print(f"WARN: coherence 非枚举值（{block['coherence']!r}）——实践允许自由文本，"
              f"仅提示不阻塞")
    if not isinstance(block["flags"], list):
        die(3, "flags 必须是列表（每项 check/observation/severity/source/target）")
    root["cross_section_identity"] = block
    save_root(Path(args.pdm), old, root, force=args.force)
    print("cross_section_identity 已写入（coherence=" + str(block["coherence"])
          + f"，flags {len(block['flags'])} 条）")
    return 0


# --------------------------------------------------------------- set-gate --

def cmd_set_gate(args) -> int:
    root, old = load_root(Path(args.pdm))
    section = norm_section(args.section)
    entry = ((root.get("distill_track") or {}).get(section))
    if not isinstance(entry, dict):
        die(3, f"[{section}] distill_track 无此节（先 merge-section）")
    wb = entry.setdefault("writeback", {})
    cur = wb.get("gate") or "awaiting_confirm"
    new = args.gate
    transitioned = new != cur
    if new not in GATE_ORDER:
        die(2, f"非法 gate：{new!r}")
    if new != cur and GATE_ORDER[new] < GATE_ORDER[cur]:
        if not (args.force and args.note):
            die(3, f"[{section}] gate 回退 {cur}→{new} 须 --force 且 --note 记录理由")
    if new != cur or args.plan or args.items is not None or args.note:
        wb["gate"] = new
    plan = None
    if args.plan:
        guard_path(args.plan, "plan 登记路径")
        plan = load_plan(Path(args.plan))
        c = plan_verdicts(plan)
        wb["plan"] = str(Path(args.plan))
        wb["items"] = int(args.items) if args.items is not None else \
            c.get("ADD", 0) + c.get("EXTEND", 0)
        if plan.get("fail_fast"):
            print(f"WARN: plan 含 fail_fast {len(plan['fail_fast'])} 处——precheck exit 4 "
                  f"应已拦截，先回子代理返工")
    elif args.items is not None:
        wb["items"] = int(args.items)
    if args.note:
        wb["note"] = args.note
    if new == "written":
        if entry.get("status") == "pending":
            die(3, f"[{section}] status=pending 时不得置 gate=written——先 merge-section")
        entry["status"] = "verified"
    save_root(Path(args.pdm), old, root, force=args.force)
    items = wb.get("items")
    items = items if isinstance(items, int) else "-"
    print(f"[{section}] gate={wb.get('gate')} items={items} "
          f"status={entry.get('status')}")
    if new == "written":
        print(f"[{section}] 该节已写回——L4 须跑 verify_writeback.py（--plan … --paper …）")
    # fitness 台账（第 4 项，2026-09-14）：接受事件只在 gate 真实迁移时发射——
    # 幂等重跑零事件；遥测失败只 WARN，绝不影响 gate 状态机（fail-open）。
    if transitioned and new in ("confirmed", "written"):
        try:
            import fitness_ledger
            if new == "confirmed" and plan is not None:
                msg = fitness_ledger.emit_gate_verdicts(
                    Path(args.pdm), root, section, plan)
            elif new == "written":
                msg = fitness_ledger.emit_written(Path(args.pdm), root,
                                                  section, plan)
            else:
                msg = ""
            if msg:
                print(f"fitness: {msg}")
        except Exception as e:  # noqa: BLE001 — 遥测永不阻塞状态机
            print(f"WARN: fitness 台账落账失败（不影响 gate 状态）：{e}",
                  file=sys.stderr)
    return 0


# -------------------------------------------------------------- set-paper --

def cmd_set_paper(args) -> int:
    root, old = load_root(Path(args.pdm))
    if args.wb_citekey:
        root["wb_citekey"] = args.wb_citekey.strip()
    if args.note:
        root["note"] = args.note
    if args.ledger_note:
        root.setdefault("feedback_ledger", {})["note"] = args.ledger_note
    if args.status:
        new = args.status
        if new not in PAPER_STATUS_ORDER:
            die(2, f"非法论文状态：{new!r}")
        cur = root.get("status") or "manifest"
        if new != cur and PAPER_STATUS_ORDER[new] < PAPER_STATUS_ORDER[cur]:
            if not (args.force and args.note):
                die(3, f"论文状态回退 {cur}→{new} 须 --force 且 --note 记录理由")
        if new == "integrated":
            track = root.get("distill_track") or {}
            scope = [s for s, e in track.items()
                     if isinstance(e, dict) and e.get("status") != "pending"]
            if not scope:
                die(3, "integrated 拒绝：无 status≠pending 的节")
            unverified = [s for s in scope if track[s].get("status") != "verified"]
            csi = root.get("cross_section_identity") or {}
            csi_filled = any(str(csi.get(k) or "").strip()
                             for k in CROSS_KEYS if k != "flags")
            if unverified or not csi_filled:
                die(3, f"integrated 守卫未过：未 verified 节={unverified or '无'}；"
                       f"cross_section_identity={'未填' if not csi_filled else '已填'}")
            if (root.get("story_track") or {}).get("status", "pending") == "pending":
                print("WARN: story_track 仍 pending——integrated 不等 L3（成文语义："
                      "告警不阻塞，story 状态由 set-story 另行推进）")
        root["status"] = new
    save_root(Path(args.pdm), old, root, force=args.force)
    print(f"paper.status={root.get('status')} wb_citekey={root.get('wb_citekey', '-')}"
          + (f" note={trunc(root.get('note'), 30)}" if root.get("note") else ""))
    return 0


# -------------------------------------------------------------- set-story --

def cmd_set_story(args) -> int:
    root, old = load_root(Path(args.pdm))
    st = root.setdefault("story_track", {"skill": "distill-story-exemplar"})
    if args.status:
        if args.status not in STORY_STATUS_ORDER:
            die(2, f"非法 story 状态：{args.status!r}")
        cur = st.get("status") or "pending"
        if args.status != cur and STORY_STATUS_ORDER[args.status] < STORY_STATUS_ORDER[cur]:
            if not (args.force and args.note):
                die(3, f"story 状态回退 {cur}→{args.status} 须 --force 且 --note")
        st["status"] = args.status
    if args.card_path:
        st["card_path"] = args.card_path
    for flag in ("validated", "catalog_rebuilt", "fed_flags"):
        if getattr(args, flag):
            st[flag] = True
    save_root(Path(args.pdm), old, root, force=args.force)
    print(f"story_track: status={st.get('status')} card={trunc(st.get('card_path'), 40) or '-'} "
          f"validated={st.get('validated')} catalog_rebuilt={st.get('catalog_rebuilt')}")
    return 0


# ------------------------------------------------------------ fail-section --

def cmd_fail_section(args) -> int:
    root, old = load_root(Path(args.pdm))
    section = norm_section(args.section)
    entry = (root.setdefault("distill_track", {}).setdefault(section, {}))
    reason = args.reason
    if args.from_file:
        try:
            data = yaml.safe_load(Path(args.from_file).read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as e:
            die(2, f"--from 不可读：{args.from_file}\n{e}")
        reason = (data or {}).get("reason") or reason
    if not reason:
        die(2, "fail-section 需要 --reason 或 --from（含 reason 键）")
    entry["error"] = str(reason)
    save_root(Path(args.pdm), old, root, force=args.force)
    print(f"[{section}] 失败已记录（status 不动、不代宣布 verified）：{trunc(reason, 60)}")
    return 0


# ---------------------------------------------------------------- present --

def _block_label(item: dict) -> str:
    bt = item.get("block_text") or ""
    for ln in bt.splitlines():
        if re.match(r"^#{1,6}\s+\S", ln):
            return trunc(ln.lstrip("# "), 42)
    return trunc(item.get("name", "?"), 42)


def _rel_target(item: dict, plan: dict) -> str:
    p = item_target(item, Path(plan["corpus_root"]) if plan.get("corpus_root") else None)
    if p is None:
        return "(目标不可解析)"
    try:
        return str(p.relative_to(plan["corpus_root"]))
    except (ValueError, KeyError, OSError):
        return p.name


def _dedup_cell(item: dict) -> str:
    bm = (item.get("dedup") or {}).get("best_match") or {}
    if "jaccard" in bm or "containment" in bm:
        return f"{bm.get('jaccard', 0):.2f}/{bm.get('containment', 0):.2f}"
    return "–"


def _notes_cell(item: dict, section: str) -> str:
    notes = []
    if item.get("create_new_file") or item.get("new_file"):
        notes.append("新建 " + trunc(item.get("new_file")
                                     or (item.get("create_new_file") or {}).get("new_file", ""), 30))
    if section == "theory" and not item.get("registry_dimension") \
            and ((item.get("dedup") or {}).get("verdict")) != "SKIP":
        notes.append("⚠缺registry_dimension(残项)")
    prov = item.get("provenance") or {}
    if item.get("provenance_warning"):
        notes.append("⚠溯源缺(gate①请确认)")
    elif prov.get("complete"):
        notes.append("溯源✓")
    return "；".join(notes) or "–"


def build_gate1_report(root: dict, plans: dict[str, tuple[Path, dict]]) -> tuple[str, int]:
    title = trunc(root.get("title") or root.get("paper"), 46) or "（无标题记录）"
    pid = root.get("paper_id") or root.get("citekey") or "(未记 paper_id)"
    counts: Counter = Counter()
    ff_total = 0
    for s, (_, plan) in plans.items():
        counts.update(plan_verdicts(plan))
        ff_total += len(plan.get("fail_fast") or [])
    out = [f"# gate ① 写回呈审单 — {title} ({pid})",
           f"生成: pdm_tool present --mode gate1 · {datetime.now():%Y-%m-%d %H:%M} · "
           f"首次蒸馏批量呈审（auto-write 直写不出此单，出 audit 单）",
           f"plan {len(plans)} 节 · ADD {counts.get('ADD', 0)} / "
           f"EXTEND {counts.get('EXTEND', 0)} / SKIP {counts.get('SKIP', 0)} · "
           f"fail_fast {ff_total}" + ("　⚠ 有 fail_fast，勿确认——先回子代理返工"
                                      if ff_total else "")]
    for s in SECTIONS:
        if s not in plans:
            continue
        path, plan = plans[s]
        c = plan_verdicts(plan)
        stale_n = 0
        checked = 0
        rows, alts = [], []
        idx = 0
        for it in plan["items"]:
            verdict = (it.get("dedup") or {}).get("verdict", "?")
            if verdict == "SKIP":
                continue
            idx += 1
            anchor = (it.get("anchor") or {}).get("after_heading")
            staleness = anchor_stale(it)
            if staleness.startswith("STALE"):
                stale_n += 1
            if staleness not in ("–",):
                checked += 1
            rows.append(f"| {idx} | {verdict} | {_block_label(it)} | "
                        f"{it.get('band', '–')} | {_rel_target(it, plan)} | "
                        f"{trunc(anchor, 24) if anchor else '–'} | "
                        f"{_dedup_cell(it)} | {_notes_cell(it, s)} |")
            picks = [e for e in it.get("anchor_candidates") or []
                     if not (anchor and e.get("heading") == anchor)]
            if picks:
                alt = " · ".join(f"{Path(e['file']).name} “{trunc(e.get('heading'), 18)}”"
                                 f"({max(e.get('jaccard', 0), e.get('containment', 0)):.2f})"
                                 for e in picks[:2])
                alts.append((idx, alt))
        out.append("")
        out.append(f"## {s} — ADD {c.get('ADD', 0)} · EXTEND {c.get('EXTEND', 0)} · "
                   f"SKIP {c.get('SKIP', 0)} · plan: {path.name} · "
                   f"锚点 ok {checked - stale_n}/{checked}"
                   + (f"（STALE {stale_n}⚠ 重跑 precheck）" if stale_n else ""))
        out.append("| # | verdict | 变体 | band | 目标文件 | 锚点 after | dedup j/c | 备注 |")
        out.append("|---|---------|------|------|----------|------------|-----------|------|")
        out.extend(rows or ["| – | – | （无 ADD/EXTEND 项） | | | | | |"])
        for idx, alt in alts:
            out.append(f"　↳ #{idx} 备选锚点: {alt}")
    skips = [(s, it) for s in SECTIONS if s in plans
             for it in plans[s][1]["items"]
             if ((it.get("dedup") or {}).get("verdict")) == "SKIP"]
    if skips:
        out += ["", "## SKIP 明细（执行器硬拒 SKIP 写回；翻案=改 plan，问题 5 领域）",
                "| 节 | 变体 | 已覆盖依据 |", "|---|------|------------|"]
        for s, it in skips:
            bm = (it.get("dedup") or {}).get("best_match") or {}
            out.append(f"| {s} | {trunc(it.get('name'), 36)} | "
                       f"{trunc(bm.get('heading'), 34) or '–'} "
                       f"(j={bm.get('jaccard', 0):.2f}) |")
    text = "\n".join(out)
    return text, (4 if ff_total else 0)


def build_audit_report(root: dict, plans: dict[str, tuple[Path, dict]],
                       verify_report: str | None, residuals: list | None) -> tuple[str, int]:
    paper = root.get("wb_citekey") or root.get("paper_id") \
        or root.get("citekey") or "(未设)"
    title = trunc(root.get("title") or root.get("paper"), 46) or "（无标题记录）"
    pid = root.get("paper_id") or root.get("citekey") or "(未记 paper_id)"
    out = [f"# L4 写回事后审计单 — {title} ({pid})",
           f"生成: pdm_tool present --mode audit · {datetime.now():%Y-%m-%d %H:%M} · "
           f"wb 键={paper}"]
    fail_n = 0
    unmarked = 0
    if verify_report:
        m = re.search(r"PASS (\d+) / FAIL (\d+) / INFO (\d+) / SKIP (\d+); "
                      r"residuals: (\d+)", verify_report)
        out.append("verify: " + (m.group(0) if m else "报告无汇总行（格式变了？人工核查）"))
        if m:
            fail_n = int(m.group(2))
    else:
        out.append("verify: 未提供 --verify-report（跳过终验解析）")
    if residuals is not None:
        by_type = Counter(str(r.get("type", "?")) for r in residuals)
        out.append(f"残项 {len(residuals)} 项: "
                   + ("；".join(f"{k}×{v}" for k, v in by_type.most_common()) or "无"))
        for r in residuals[:10]:
            out.append(f"  - {r.get('type')} {r.get('item', '')}@{r.get('stem', '')}"
                       f"（{trunc(r.get('hint', ''), 40)}）")
        if len(residuals) > 10:
            out.append(f"  …其余 {len(residuals) - 10} 项见残项单")
    for s in SECTIONS:
        if s not in plans:
            continue
        _, plan = plans[s]
        live = [it for it in plan["items"]
                if ((it.get("dedup") or {}).get("verdict")) != "SKIP"]
        out += ["", f"## {s} — 计划写 {len(live)} 项 · wb 标记实见如下",
                "| # | 变体 | 目标文件 | wb 标记 |", "|---|------|----------|---------|"]
        for i, it in enumerate(live, 1):
            tgt = item_target(it, Path(plan["corpus_root"]) if plan.get("corpus_root") else None)
            n = 0
            if tgt is not None and tgt.is_file():
                try:
                    n = tgt.read_text(encoding="utf-8", errors="replace").count(
                        wb_block_marker(paper, it.get("name", "")))
                except OSError:
                    n = -1
            cell = f"✓×{n}" if n > 0 else ("⚠不可读" if n < 0 else "⚠0 未落盘")
            unmarked += 0 if n > 0 else 1
            out.append(f"| {i} | {trunc(it.get('name'), 40)} | "
                       f"{_rel_target(it, plan)} | {cell} |")
    text = "\n".join(out)
    return text, (4 if (fail_n or unmarked) else 0)


def cmd_present(args) -> int:
    root_path = Path(args.pdm)
    root, _ = load_root(root_path)
    wd = workdir_of(root_path)
    sections = parse_sections(args.sections)
    found = discover_plans(wd, root, sections, args.plan)
    missing = [s for s in sections if s not in found]
    plans = {s: (p, load_plan(p)) for s, p in found.items()}
    if not plans:
        die(3, f"无可呈审 plan（缺: {missing or sections}）——plan 由 corpus_precheck 产出")
    residuals = None
    if args.residuals:
        try:
            loaded = yaml.safe_load(Path(args.residuals).read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as e:
            die(2, f"残项单不可读：{args.residuals}\n{e}")
        residuals = loaded if isinstance(loaded, list) else (loaded or {}).get("residuals", [])
    vr = Path(args.verify_report).read_text(encoding="utf-8", errors="replace") \
        if args.verify_report else None
    if args.mode == "gate1":
        text, code = build_gate1_report(root, plans)
    else:
        text, code = build_audit_report(root, plans, vr, residuals)
    # fitness 台账（第 4 项，2026-09-14）：gate① 呈审同时存档快照+呈审单
    # （--stdout-only 逃生阀；audit 模式不落快照）。快照按时间戳追加保留，
    # 是 set-gate 逐项裁决 diff 的基准，也使呈审单不再随工作目录 --clean 蒸发。
    if args.mode == "gate1" and not getattr(args, "stdout_only", False):
        try:
            import fitness_ledger
            snap = fitness_ledger.snapshot_gate1(root_path, root, plans, text)
            if snap.get("files"):
                print(f"fitness: gate① 快照已存档 → {snap['dir']}"
                      f"（{snap['items']} 项）")
        except Exception as e:  # noqa: BLE001 — 遥测永不阻塞呈审
            print(f"WARN: fitness 快照落账失败（不影响呈审）：{e}", file=sys.stderr)
    if missing:
        text += f"\n\n（缺 plan 的节: {', '.join(missing)}——未完成，不在本次呈审/审计范围）"
    if args.out:
        guard_path(args.out, "呈审单输出路径")
        Path(args.out).write_text(text + "\n", encoding="utf-8")
        print(f"[written] {args.out}")
    print(text)
    return code


# --------------------------------------------------------------- selftest --

def selftest() -> int:
    import shutil
    results: list[tuple[bool, str]] = []

    def check(ok: bool, name: str):
        results.append((ok, name))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")

    def expect_exit(code: int, fn, *a, **kw) -> bool:
        try:
            fn(*a, **kw)
            return False
        except SystemExit as e:
            return e.code == code

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        global CAPABILITY_ROOT
        real_cap = CAPABILITY_ROOT
        # fitness 台账沙盒（第 4 项）：selftest 在进程内直跑 cmd_present/
        # cmd_set_gate，必须把 ledger 写进临时 FITNESS_HOME，不碰真实台账。
        real_fit = os.environ.get("FITNESS_HOME")
        os.environ["FITNESS_HOME"] = str(tmp / "fitness")
        try:
            (tmp / "cap" / "distill-methods-exemplar").mkdir(parents=True)
            CAPABILITY_ROOT = tmp / "cap"  # methods 有基建；其余节无 → 能力缺口

            # fixture root：scaffold 形态（flow 块 + 双基准路径样本）
            wd = tmp / "p1.pdm"
            (wd / "sections").mkdir(parents=True)
            (wd / "feedback").mkdir()
            root = yaml.safe_load(f"""
pdm_version: 1.0
paper_id: "fix_paper_2026"
title: "Fixture Paper"
authors: ["A Author"]
year: 2026
journal: "AMJ"
source_provenance:
  fulltext_md: "D:/x/fp.md"
  text_only_md: "p1.pdm/fulltext.text-only.md"
  zotero_ref: ""
  ingestion: "paper-import (OvisOCR2)"
  structure_type: "classic-imrad"
  section_slices: {{}}
status: "manifest"
distill_track:
  introduction:
    skill: distill-introduction-exemplar
    status: "pending"
    section_json: "sections/introduction.json"
    feedback: "feedback/introduction.feedback.yaml"
    identity: {{gap_type: "", contribution_dimension: ""}}
    writeback: {{target: "write-introduction/corpus/", gate: awaiting_confirm, items: []}}
  theory:
    skill: distill-theory-exemplar
    status: "pending"
    section_json: "sections/theory.json"
    feedback: "feedback/theory.feedback.yaml"
    identity: {{theory_building_type: ""}}
    writeback: {{target: "write-theory/corpus/", gate: awaiting_confirm, items: []}}
  methods:
    skill: distill-methods-exemplar
    status: "pending"
    section_json: "sections/methods.json"
    feedback: "feedback/methods.feedback.yaml"
    identity: {{design_family: ""}}
    writeback: {{target: "write-methods/corpus/", gate: awaiting_confirm, items: []}}
  results:
    skill: distill-results-exemplar
    status: "pending"
    section_json: "sections/results.json"
    feedback: "feedback/results.feedback.yaml"
    identity: {{estimator_family: ""}}
    writeback: {{target: "write-results/corpus/", gate: awaiting_confirm, items: []}}
cross_section_identity:
  gap_type: ""
  theory_building_type: ""
  design_family: ""
  estimator_family: ""
  coherence: ""
  flags: []
story_track:
  skill: distill-story-exemplar
  status: "pending"
  card_path: ""
  validated: false
  catalog_rebuilt: false
  fed_flags: false
feedback_ledger:
  persisted: []
  missing: []
  note: ""
distiller_fingerprint:
  version: "deadbeef"
  files: 3
""")
            root_path = tmp / "p1.pdm.yaml"
            old_text = ROOT_HEADER + yaml.safe_dump(root, allow_unicode=True,
                                                    sort_keys=False)
            root_path.write_text(old_text, encoding="utf-8")

            def ns(**kw):
                base = dict(pdm=str(root_path), force=False, note=None,
                            plan=None, items=None, section=None, gate=None,
                            json=None, band=None, set=None, status=None,
                            wb_citekey=None, ledger_note=None, card_path=None,
                            validated=False, catalog_rebuilt=False,
                            fed_flags=False, reason=None, from_file=None,
                            mode=None, sections=None, verify_report=None,
                            residuals=None, out=None, format="text")
                base.update(kw)
                return argparse.Namespace(**base)

            # 1 双基准 resolver
            (wd / "sections" / "introduction.json").write_text("{}", encoding="utf-8")
            check(resolve_workfile(wd, "sections/introduction.json").is_file(),
                  "resolver 裸相对路径")
            check(resolve_workfile(wd, "p1.pdm/sections/introduction.json").is_file(),
                  "resolver 带 <citekey>.pdm/ 前缀路径")

            # 2 守卫
            check(expect_exit(3, guard_path,
                              r"C:\x\skills\write-theory\corpus\a.md", "t"),
                  "守卫拒绝 corpus 写路径")

            # 3 幂等：同内容重存 → no-op 不写；真实变更 → 写 + .bak
            check(save_root(root_path, old_text, root) is False,
                  "幂等：fixture 已是规范形，重存 no-op")
            d1 = yaml.safe_load(old_text)
            d1["note"] = "trigger"
            text1 = ROOT_HEADER + yaml.safe_dump(d1, allow_unicode=True,
                                                 sort_keys=False)
            root_path.write_text(text1, encoding="utf-8")
            check(save_root(root_path, text1, d1) is False,
                  "幂等：同内容再次 no-op")
            text1 = root_path.read_text(encoding="utf-8")
            d2 = yaml.safe_load(text1)
            d2["note"] = "changed"
            check(save_root(root_path, text1, d2) is True, "真实变更写入")
            check(root_path.with_name("p1.pdm.yaml.bak").is_file(), ".bak 已生成")

            # 4 旧根行内注释须 --force
            commented = text1.replace(ROOT_HEADER.splitlines()[0],
                                      "# 用户手注：本篇是重蒸馏\n" + ROOT_HEADER.splitlines()[0], 1)
            root_path.write_text(commented, encoding="utf-8")
            data_c = yaml.safe_load(commented)
            check(expect_exit(3, save_root, root_path, commented, data_c, False),
                  "行内注释无 --force → exit 3")
            save_root(root_path, commented, data_c, True)
            check("# 用户手注" not in root_path.read_text(encoding="utf-8"),
                  "--force 后注释收口为规范头")

            # 5 merge-section：identity 缺失 → exit 3；--set 补填 → distilled
            def msec(**kw):
                return cmd_merge_section(ns(section="introduction", **kw))
            check(expect_exit(3, msec), "identity 全缺 → exit 3")
            (wd / "sections" / "introduction.json").write_text(json.dumps({
                "paper_id": "fix", "identity": {"gap_type": "Inadequacy"}}),
                encoding="utf-8")
            check(expect_exit(3, msec), "identity 缺 contribution_dimension → exit 3")
            msec(set=["contribution_dimension=Method"])
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            e = d["distill_track"]["introduction"]
            check(e["identity"] == {"gap_type": "Inadequacy",
                                    "contribution_dimension": "Method"}
                  and e["status"] == "distilled" and d["status"] == "distilling",
                  "merge-section 写入 identity/状态级联")
            check(e["feedback"].startswith("feedback/") and
                  "introduction" in "；".join(
                      f"{k}: {v}" for k, v in
                      d["feedback_ledger"]["causes"].items()),
                  "feedback 缺失记账为能力缺口（intro 无基建）")

            # 6 set-gate：跃迁守卫 + written 级联 + items 归一化
            cmd_set_gate(ns(section="introduction", gate="confirmed"))
            check(expect_exit(3, cmd_set_gate, ns(section="introduction",
                                                  gate="awaiting_confirm")),
                  "gate 回退无 --force → exit 3")
            check(expect_exit(3, cmd_set_gate, ns(section="introduction",
                                                  gate="awaiting_confirm",
                                                  force=True)),
                  "gate 回退 --force 缺 note → exit 3")
            plan = {"corpus_root": str(wd), "items": [
                {"name": "a", "dedup": {"verdict": "ADD"}, "block_text": "### 变体甲",
                 "anchor": {"file": None}},
                {"name": "b", "dedup": {"verdict": "EXTEND"}, "block_text": "### 乙",
                 "anchor": {"file": None}},
                {"name": "c", "dedup": {"verdict": "SKIP"}, "block_text": "### 丙"},
            ]}
            plan_path = wd / "writeback_plan.introduction.yaml"
            plan_path.write_text(yaml.safe_dump(plan, allow_unicode=True),
                                 encoding="utf-8")
            cmd_set_gate(ns(section="introduction", gate="written",
                            plan=str(plan_path), items=None, note=None))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            e = d["distill_track"]["introduction"]
            check(e["writeback"]["gate"] == "written"
                  and e["writeback"]["items"] == 2 and e["status"] == "verified",
                  "awaiting_confirm→written 跳跃 + items 归一化为 2")
            check(expect_exit(3, cmd_set_gate, ns(section="theory",
                                                  gate="written")),
                  "status=pending 时置 written → exit 3")

            # 7 LEGACY⚠ 识别
            d["distill_track"]["theory"]["status"] = "verified"
            d["distill_track"]["theory"]["writeback"]["gate"] = "confirmed"
            root_path.write_text(ROOT_HEADER + yaml.safe_dump(
                d, allow_unicode=True, sort_keys=False), encoding="utf-8")
            import io
            from contextlib import redirect_stdout
            buf = io.StringIO()
            with redirect_stdout(buf):
                cmd_show(ns(pdm=str(root_path), format="text"))
            check("LEGACY⚠" in buf.getvalue() and "theory" in buf.getvalue(),
                  "show 识别 confirmed+verified 为 LEGACY⚠")
            buf = io.StringIO()
            with redirect_stdout(buf):
                cmd_show(ns(pdm=str(root_path), format="json"))
            info = json.loads(buf.getvalue())
            check(info["sections"]["theory"]["legacy"] is True,
                  "show --format json 结构化 legacy/状态字段")

            # 7b fail-section：记录 error 且 status 不动
            cmd_fail_section(ns(section="methods", reason="子代理超时（自测）"))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            check(d["distill_track"]["methods"].get("error") == "子代理超时（自测）"
                  and d["distill_track"]["methods"]["status"] == "pending",
                  "fail-section 记录 error 且 status 不动")

            # 8 set-paper integrated 守卫 + wb_citekey + set-story
            check(expect_exit(3, cmd_set_paper, ns(status="integrated",
                                                   wb_citekey=None, note=None,
                                                   ledger_note=None)),
                  "integrated 守卫（identity 未填）→ exit 3")
            d["distill_track"]["theory"]["status"] = "pending"
            d["distill_track"]["methods"]["status"] = "distilled"
            (wd / "sections" / "theory.json").write_text(json.dumps({"identity": {
                "theory_building_type": "机制推演型"}}), encoding="utf-8")
            root_path.write_text(ROOT_HEADER + yaml.safe_dump(
                d, allow_unicode=True, sort_keys=False), encoding="utf-8")
            cmd_merge_section(ns(section="theory", json=None, band=None, set=None,
                                 force=False))
            l2 = tmp / "l2.yaml"
            l2.write_text(yaml.safe_dump({
                "gap_type": "Inadequacy", "theory_building_type": "机制推演型",
                "design_family": "档案", "estimator_family": "logit",
                "coherence": "ok", "flags": [
                    {"check": "gap->theory", "observation": "一致",
                     "severity": "info", "source": "introduction",
                     "target": "theory"}]}, allow_unicode=True), encoding="utf-8")
            for s in ("methods", "results"):
                jp = wd / "sections" / f"{s}.json"
                jp.write_text(json.dumps({"identity": {
                    "design_family": "档案", "estimator_family": "logit"}}),
                    encoding="utf-8")
                cmd_merge_section(ns(section=s, json=None, band=None, set=None,
                                     force=False))
                cmd_set_gate(ns(section=s, gate="written",
                                plan=None, items=0, note=None))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            check("error" not in d["distill_track"]["methods"],
                  "merge-section 成功清除先前 error（重发=恢复）")
            check(expect_exit(3, cmd_set_paper, ns(status="integrated",
                                                   wb_citekey=None, note=None,
                                                   ledger_note=None)),
                  "integrated 守卫（cross_section_identity 未填）→ exit 3")
            (wd / "sections" / "results.json").write_text(json.dumps({"identity": {
                "estimator_family": "Firth logit"}}), encoding="utf-8")
            cmd_merge_section(ns(section="results", json=None, band=None, set=None,
                                 force=False))
            cmd_set_gate(ns(section="results", gate="written",
                            plan=None, items=0, note=None))
            cmd_merge_cross(ns(from_file=str(l2), force=False))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            d["distill_track"]["results"]["status"] = "distilled"  # 伪造：范围节未 verified
            root_path.write_text(ROOT_HEADER + yaml.safe_dump(
                d, allow_unicode=True, sort_keys=False), encoding="utf-8")
            check(expect_exit(3, cmd_set_paper, ns(status="integrated",
                                                   wb_citekey=None, note=None,
                                                   ledger_note=None)),
                  "integrated 守卫（范围节 distilled 未 verified）→ exit 3")
            cmd_set_gate(ns(section="theory", gate="written",
                            plan=None, items=0, note=None))
            cmd_set_gate(ns(section="results", gate="written",
                            plan=None, items=0, note=None))
            cmd_set_paper(ns(status="integrated", wb_citekey="fix_2026_amj",
                             note="自测", ledger_note=None))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            check(d["status"] == "integrated"
                  and d["wb_citekey"] == "fix_2026_amj"
                  and d["cross_section_identity"]["coherence"] == "ok",
                  "integrated + wb_citekey + merge-cross 落盘")
            cmd_set_story(ns(status="validated", card_path="cards/x.md",
                             validated=True, catalog_rebuilt=True, fed_flags=True))
            d = yaml.safe_load(root_path.read_text(encoding="utf-8"))
            check(d["story_track"]["status"] == "validated"
                  and d["story_track"]["catalog_rebuilt"] is True, "set-story 落盘")

            # 9 present gate1（全字段 fixture）+ audit（wb 点数）
            plan2 = {"corpus_root": str(wd), "section": "theory",
                     "items": [
                         {"name": "v_one", "band": "gap",
                          "dedup": {"verdict": "ADD", "threshold": 0.33,
                                    "best_match": {"file": str(wd / "x.md"),
                                                   "heading": "H", "jaccard": 0.1,
                                                   "containment": 0.1}},
                          "anchor": {"file": str(plan_path),
                                     "insert_after_line": 1,
                                     "after_heading": "# Fixture"},
                          "anchor_candidates": [
                              {"file": str(plan_path), "heading": "Other",
                               "jaccard": 0.2, "containment": 0.1, "line": 2}],
                          "registry_dimension": "Mechanism",
                          "provenance": {"structured": True, "marker_in_block": False,
                                         "complete": True},
                          "block_text": "### 变体一：测试句式\n正文",
                          "index_note": "变体 {NEXT}"},
                         {"name": "v_two", "band": "quiet",
                          "dedup": {"verdict": "SKIP", "threshold": 0.33,
                                    "best_match": {"heading": "已覆盖旧变体",
                                                   "jaccard": 0.41}},
                          "block_text": "### 变体二"},
                         {"name": "v_three", "band": "quiet",
                          "dedup": {"verdict": "EXTEND", "threshold": 0.33,
                                    "best_match": {"heading": "旧", "jaccard": 0.25,
                                                   "containment": 0.3}},
                          "anchor": {"file": str(wd / "sections" / "methods.json"),
                                     "insert_after_line": 1,
                                     "after_heading": "# Fixture"},
                          "block_text": "### 变体三"},
                     ]}
            plan2_path = wd / "writeback_plan.theory.yaml"
            plan2_path.write_text(yaml.safe_dump(plan2, allow_unicode=True),
                                  encoding="utf-8")
            d2, _ = load_root(root_path)
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cmd_present(ns(pdm=str(root_path), mode="gate1",
                                      sections="theory", plan=None,
                                      verify_report=None, residuals=None,
                                      out=None))
            g = buf.getvalue()
            check(code == 0 and "ADD 1 / EXTEND 1 / SKIP 1" in g
                  and "| gap |" in g and "溯源✓" in g and "SKIP 明细" in g
                  and "STALE" in g,
                  "present gate1 渲染（band/溯源/STALE/SKIP 明细/计数）")
            tgt_md = plan_path  # v_one 的 anchor.file 指向该文件
            tgt_md.write_text(tgt_md.read_text(encoding="utf-8")
                              + "\n" + wb_block_marker("fix_2026_amj", "v_one"),
                              encoding="utf-8")
            vlog = tmp / "v.log"
            vlog.write_text("stuff\n[ PASS] V1 x\n"
                            "------------------------------------------------------------\n"
                            "PASS 5 / FAIL 0 / INFO 2 / SKIP 0; residuals: 1\n",
                            encoding="utf-8")
            res = tmp / "res.yaml"
            res.write_text(yaml.safe_dump([
                {"type": "registry_no_entry", "section": "theory",
                 "stem": "x.md", "item": "v_one", "hint": "sync"}],
                allow_unicode=True), encoding="utf-8")
            buf = io.StringIO()
            with redirect_stdout(buf):
                code = cmd_present(ns(pdm=str(root_path), mode="audit",
                                      sections="theory", plan=None,
                                      verify_report=str(vlog),
                                      residuals=str(res), out=None))
            a = buf.getvalue()
            check(code == 4 and "PASS 5 / FAIL 0" in a and "✓×1" in a
                  and "⚠0 未落盘" in a and "registry_no_entry×1" in a,
                  "present audit（verify 解析/wb 点数/残项/未落盘→exit 4）")

            # 10 原子写无残渣
            check(not list(tmp.glob("*.tmp*")), "原子写无临时文件残渣")
        finally:
            CAPABILITY_ROOT = real_cap
            if real_fit is None:
                os.environ.pop("FITNESS_HOME", None)
            else:
                os.environ["FITNESS_HOME"] = real_fit

    failed = [n for ok, n in results if not ok]
    print("-" * 60)
    print(f"{'ALL GREEN' if not failed else 'FAILURES: ' + str(failed)}"
          f"  ({len(results) - len(failed)}/{len(results)})")
    return 0 if not failed else 1


# ------------------------------------------------------------------ main --

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0],
                                 epilog="exit: 0 ok / 2 usage / 3 契约 / "
                                        "4 fail_fast(gate1)·未落盘或verify FAIL(audit)")
    ap.add_argument("--selftest", action="store_true", help="in-process 回归（temp 夹具）")
    sub = ap.add_subparsers(dest="cmd")

    def pdm_arg(p):
        p.add_argument("--pdm", required=True, help="PDM 根 yaml 路径")
        p.add_argument("--force", action="store_true",
                       help="允许回退/覆盖行内注释等需明示的操作")
        return p

    p = pdm_arg(sub.add_parser("show", help="续跑断点视图"))
    p.add_argument("--format", choices=("text", "json"), default="text")

    p = pdm_arg(sub.add_parser("merge-section", help="合并节 identity/band 进根"))
    p.add_argument("--section", required=True)
    p.add_argument("--json", default=None, help="覆盖 section json 路径")
    p.add_argument("--band", default=None)
    p.add_argument("--set", action="append", metavar="K=V",
                   help="identity 键值补填（可重复）")

    p = pdm_arg(sub.add_parser("merge-cross", help="写入 L2 cross_section_identity"))
    p.add_argument("--from", dest="from_file", required=True, help="L2 摘要 yaml")

    p = pdm_arg(sub.add_parser("set-gate", help="写回门禁三态"))
    p.add_argument("--section", required=True)
    p.add_argument("--gate", required=True,
                   choices=("awaiting_confirm", "confirmed", "written"))
    p.add_argument("--plan", default=None, help="登记 plan 路径并自动导出 items 计数")
    p.add_argument("--items", type=int, default=None)
    p.add_argument("--note", default=None)

    p = pdm_arg(sub.add_parser("set-paper", help="论文级状态/承载字段"))
    p.add_argument("--status", choices=tuple(PAPER_STATUS_ORDER), default=None)
    p.add_argument("--wb-citekey", dest="wb_citekey", default=None)
    p.add_argument("--note", default=None, help="根级 note（如指纹不一致注记）")
    p.add_argument("--ledger-note", dest="ledger_note", default=None)

    p = pdm_arg(sub.add_parser("set-story", help="story_track 状态机（L3）"))
    p.add_argument("--status", choices=tuple(STORY_STATUS_ORDER), default=None)
    p.add_argument("--card-path", dest="card_path", default=None)
    p.add_argument("--validated", action="store_true")
    p.add_argument("--catalog-rebuilt", dest="catalog_rebuilt", action="store_true")
    p.add_argument("--fed-flags", dest="fed_flags", action="store_true")
    p.add_argument("--note", default=None)

    p = pdm_arg(sub.add_parser("fail-section", help="记录节失败根因（status 不动）"))
    p.add_argument("--section", required=True)
    p.add_argument("--reason", default=None)
    p.add_argument("--from", dest="from_file", default=None, help="yaml: {reason}")

    p = pdm_arg(sub.add_parser("present", help="gate① 呈审单 / L4 审计单"))
    p.add_argument("--mode", choices=("gate1", "audit"), required=True)
    p.add_argument("--sections", default=None, help="逗号分隔；缺省四节")
    p.add_argument("--plan", action="append", help="section=path 或可推断的路径（可重复）")
    p.add_argument("--verify-report", dest="verify_report", default=None,
                   help="verify_writeback 的 tee 文本（非 JSON）")
    p.add_argument("--residuals", default=None, help="writeback_residuals.yaml")
    p.add_argument("--out", default=None, help="另存 markdown（默认仅 stdout）")
    p.add_argument("--stdout-only", dest="stdout_only", action="store_true",
                   help="不落 fitness 台账快照（默认 gate① 呈审同时存档）")
    return ap


def dispatch(args) -> int:
    return {
        "show": cmd_show, "merge-section": cmd_merge_section,
        "merge-cross": cmd_merge_cross, "set-gate": cmd_set_gate,
        "set-paper": cmd_set_paper, "set-story": cmd_set_story,
        "fail-section": cmd_fail_section, "present": cmd_present,
    }[args.cmd](args)


def main() -> int:
    ap = build_parser()
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not getattr(args, "cmd", None):
        ap.print_help()
        return 2
    return dispatch(args)


if __name__ == "__main__":
    sys.exit(main())
