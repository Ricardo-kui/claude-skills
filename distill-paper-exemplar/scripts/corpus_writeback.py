#!/usr/bin/env python3
"""Deterministic corpus writeback executor for distill Phase 4.

Executes a HUMAN-CONFIRMED writeback plan (corpus_precheck.py output) so the
LLM never hand-edits corpus bookkeeping: variant-block insertion (with
automatic next 变体 letter/number), _evidence_registry counter bumps, and
_index.md row notes. Quality gates stay human: gate ① confirms the plan,
and --dry-run (default) prints unified diffs for review before --apply.

Usage:
  python corpus_writeback.py --plan writeback_plan.introduction.yaml \
      [--blocks blocks.yaml] --paper westphalzajac1995 --journal AMJ \
      --gap Incompleteness [--apply]

Block source precedence (blocks.yaml is OPTIONAL — 2026-08-20 merge: write the
variant once in candidates.yaml; precheck passes block_text/index_note through
into the plan, so the executor can read everything from the plan):
  1. blocks.yaml entry for the item (its file: override beats everything)
  2. plan item's own block_text / index_note / file_override fields
  gate ① anchor reassignment = set file_override in the plan item, or file:
  in blocks.yaml.

blocks.yaml:
  blocks:
    - name: hook_classic_debate_central_question   # must match plan item
      file: "hooks/17-debate-reframing.md"          # OPTIONAL override
      block_text: |                                 # {NEXT} -> assigned label
        ### 变体 {NEXT}：多文献中央问题型（westphalzajac1995 型）
        ...
      index_note: "变体 {NEXT}：多文献中央问题型，westphalzajac1995，EMERGING"

Rules:
  - SKIP items are REFUSED (double-writeback protection: precheck re-run after
    a completed writeback returns SKIP by design).
  - IDEMPOTENT (2026-08-29): each inserted block carries a
    `<!-- wb:<paper>:<item> -->` provenance marker; items whose marker or an
    identical block body is already present are skipped, so re-running
    --apply on the same plan can never duplicate blocks or re-bump registries.
  - Registry edits ACCUMULATE across items within one run (each item's bump is
    preserved; verify with scripts/verify_writeback.py after apply).
  - Variant labels recognize the file's dominant heading family
    (变体/句式/模式/框架/Pattern/Variant/技巧), not just 变体.
  - Items without an anchor and without a file override are skipped loudly.
  - Registry/index entries that cannot be located are reported, never guessed.
  - After --apply the registry is re-parsed as YAML; any parse failure rolls
    nothing back but exits non-zero so the caller inspects immediately.
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from datetime import date
from pathlib import Path

import yaml

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

CORPUS_ROOTS = {
    "introduction": SKILLS_ROOT / "write-introduction" / "academic-writing-corpus",
    "theory": SKILLS_ROOT / "write-theory" / "corpus",
    "methods": SKILLS_ROOT / "write-methods" / "econometric-models",
    "results": SKILLS_ROOT / "write-results" / "econometric-models",
}

# file stem -> (evidence section, entry key) for registry entries that are NOT
# keyed by file stem (pooled/aliased entries; extend as discovered)
REGISTRY_ALIASES = {
    "theory-lens-driven-preview": ("theory_lens", "theory-lens-templates"),
}

BLOCK_HEAD = re.compile(r"^#{2,4}\s+.+$", re.M)
BAD_ANCHOR = re.compile(r"反模式|诚实边界|anti-?pattern|boundar", re.I)
GOOD_ANCHOR = re.compile(r"变体|variant|pattern", re.I)

# Heading families that carry an incrementing variant label. The file's
# DOMINANT family (most heading matches) decides the next label — files whose
# variants use 句式/模式/框架/Pattern/技巧 previously fell through to "A" for
# every same-file item, stamping all of them with the same label
# (2026-08-29 fix; 变体 keeps priority on count ties for back-compat).
LABEL_FAMILIES = [
    ("变体", re.compile(r"^#{2,4}\s+变体\s+([A-Z]+|\d+)\b", re.M)),
    ("句式", re.compile(r"^#{2,4}\s+句式\s+([A-Z]+|\d+)\b", re.M)),
    ("模式", re.compile(r"^#{2,4}\s+模式\s+([A-Z]+|\d+)\b", re.M)),
    ("框架", re.compile(r"^#{2,4}\s+框架\s+([A-Z]+|\d+)\b", re.M)),
    ("Pattern", re.compile(r"^#{2,4}\s+Pattern\s+([A-Z]+|\d+)\b", re.M)),
    ("Variant", re.compile(r"^#{2,4}\s+Variant\s+([A-Z]+|\d+)\b", re.M)),
    ("技巧", re.compile(r"^#{2,4}\s+技巧\s+([A-Z]+|\d+)\b", re.M)),
]


def load_blocks(lines: list[str]) -> list[dict]:
    heads = [(i, ln) for i, ln in enumerate(lines) if BLOCK_HEAD.match(ln)]
    out = []
    for k, (i, ln) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        out.append({"heading": ln.strip(), "start": i, "end": end})
    return out


def next_variant_label(lines: list[str]) -> str:
    text = "\n".join(lines)
    best_labels: list[str] = []
    for _fam, rx in LABEL_FAMILIES:
        labels = rx.findall(text)
        if len(labels) > len(best_labels):
            best_labels = labels
    if best_labels:
        letters = [x for x in best_labels if x.isalpha()]
        numbers = [x for x in best_labels if x.isdigit()]
        if letters:
            def val(s: str) -> int:
                v = 0
                for ch in s:
                    v = v * 26 + (ord(ch) - ord("A") + 1)
                return v

            def name(v: int) -> str:
                s = ""
                while v:
                    v, r = divmod(v - 1, 26)
                    s = chr(ord("A") + r) + s
                return s

            return name(max(val(x) for x in letters) + 1)
        if numbers:
            return str(max(int(x) for x in numbers) + 1)
    return "A"


def body_similarity_pattern(block_text: str) -> re.Pattern:
    """Regex matching an already-inserted copy of block_text, tolerant of the
    run-varying label substituted for each {NEXT} slot (labels are short and
    never span lines). Used for idempotency hardening and post-hoc audits."""
    segs = [re.escape(s.strip("\n")) for s in block_text.split("{NEXT}")]
    return re.compile(r"[^\n]{0,40}?".join(segs), re.S)


def _norm_head(s: str) -> str:
    return re.sub(r"\s+", "", s).lower()


def insertion_index(lines: list[str], item: dict, target: Path) -> tuple[int, str]:
    """0-based line index AFTER which the block is inserted, plus an optional
    warning note.

    EXTEND -> end of the matched variant block (by anchor heading, whitespace-
    normalized); falls back to the last variant block with a warning when the
    anchor heading is not found (plan line numbers are stale by design).
    ADD    -> end of the last variant/pattern block (never a boundaries block);
              falls back to end of file.
    Recomputed at execution time — never trust stale plan line numbers.
    """
    blocks = load_blocks(lines)
    anchor = item.get("anchor") or {}
    verdict = item["dedup"]["verdict"]
    if verdict == "EXTEND" and anchor.get("after_heading"):
        want = _norm_head(anchor["after_heading"])
        for b in blocks:
            if _norm_head(b["heading"])[:80] == want[:80]:
                return b["end"], ""
        return (good[-1]["end"] if (good := [b for b in blocks
                if GOOD_ANCHOR.search(b["heading"])
                and not BAD_ANCHOR.search(b["heading"])]) else
                blocks[-1]["end"] if blocks else len(lines)), \
            f"anchor heading not found in {target.name}: {anchor['after_heading'][:60]!r}"
    good = [b for b in blocks if GOOD_ANCHOR.search(b["heading"])
            and not BAD_ANCHOR.search(b["heading"])]
    if good:
        return good[-1]["end"], ""
    if blocks:
        return blocks[-1]["end"], ""
    return len(lines), ""


def resolve_target(corpus_root: Path, item: dict, override: str | None) -> Path | None:
    if override:
        p = corpus_root / override
        if p.is_file():
            return p
        hits = list(corpus_root.rglob(override))
        if hits:
            return hits[0]
        return None
    anchor_file = (item.get("anchor") or {}).get("file")
    if anchor_file and anchor_file != "None":
        p = Path(anchor_file)
        return p if p.is_file() else None
    return None


def update_registry(registry: Path, stem: str, paper: str, journal: str,
                    gap: str, new_text: dict) -> str:
    """Surgical text edit of one entry. Returns status message."""
    # Accumulate on new_text — re-reading from disk here silently discarded
    # every earlier same-run item's edit (last item won). 2026-08-29 fix.
    text = new_text.get(str(registry)) or registry.read_text(encoding="utf-8")
    section, key, m = None, None, None
    if stem in REGISTRY_ALIASES:
        section, key = REGISTRY_ALIASES[stem]
    else:
        # entry keyed by stem under any evidence subsection
        pat = re.compile(r"^( +)%s:\n( +)paper_count: (\d+)" % re.escape(stem), re.M)
        m = pat.search(text)
        if m:
            key = stem
    if m is None and key is not None:
        pat = re.compile(r"^( +)%s:\n( +)paper_count: (\d+)" % re.escape(key), re.M)
        m = pat.search(text)
    if key is None or not m:
        return f"REGISTRY: no entry for '{stem}' — SKIPPED (update by hand)"
    ind, sub = m.group(1), m.group(2)
    count = int(m.group(3))
    # entry span: from key line to next line indented <= ind
    start = m.start()
    nxt = re.search(r"^ {1,%d}\S" % len(ind), text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    entry = text[start:end]
    # One paper = one papers-list line = one paper_count unit. When several
    # variants of the SAME paper land on one entry in a single run, the later
    # items are no-ops (accumulation fix would otherwise append duplicate
    # paper lines and double-bump the count — 2026-08-29 Anand run).
    if re.search(r"^\s*- %s \(" % re.escape(paper), entry, re.M):
        return f"REGISTRY: entry '{key}' already lists {paper} — no change"
    entry2 = entry.replace(f"paper_count: {count}", f"paper_count: {count + 1}", 1)
    # locate the papers: list and append after its last consecutive item
    lines2 = entry2.split("\n")
    papers_idx = next((i for i, l in enumerate(lines2)
                       if re.match(r"^\s*papers:\s*$", l)), None)
    if papers_idx is None:
        return f"REGISTRY: entry '{key}' has no papers list — SKIPPED papers append"
    item_re = re.compile(r"^(\s*)- .+$")
    last = papers_idx
    for j in range(papers_idx + 1, len(lines2)):
        if item_re.match(lines2[j]):
            last = j
        elif lines2[j].strip() == "":
            continue
        else:
            break
    if last == papers_idx:
        return f"REGISTRY: entry '{key}' papers list empty — SKIPPED papers append"
    ind_item = item_re.match(lines2[last]).group(1)
    lines2.insert(last + 1, f"{ind_item}- {paper} ({journal})")
    entry2 = "\n".join(lines2)
    gm = re.search(r"^(\s+)%s: (\d+)$" % re.escape(gap), entry2, re.M)
    if gm:
        entry2 = (entry2[:gm.start()]
                  + f"{gm.group(1)}{gap}: {int(gm.group(2)) + 1}"
                  + entry2[gm.end():])
    new_text[str(registry)] = text[:start] + entry2 + text[end:]
    return f"REGISTRY: {key} paper_count {count}->{count + 1}, +{paper} ({journal}), {gap}+1"


def add_index_row(corpus_root: Path, target: Path, note: str,
                  new_text: dict) -> str:
    """Append a NEW index row for a newly created module file (create_new_file).
    Unlike update_index (which edits an existing row), this adds one after the
    last table row of the directory's _index.md / INDEX.md."""
    if not note:
        return "INDEX: no index_note given — SKIPPED"
    for idx in sorted(target.parent.glob("_index.md")) + sorted(target.parent.glob("INDEX.md")):
        text = new_text.get(str(idx)) or idx.read_text(encoding="utf-8")
        if target.stem in text:
            return f"INDEX: {idx.name} already mentions {target.stem} — skipped"
        lines = text.split("\n")
        row_idxs = [i for i, l in enumerate(lines) if l.lstrip().startswith("|")]
        if not row_idxs:
            return f"INDEX: no table in {idx.name} — edit by hand: {note}"
        row = f"| `{target.stem}.md` | `{target.stem}` | {note} |"
        lines.insert(row_idxs[-1] + 1, row)
        new_text[str(idx)] = "\n".join(lines)
        return f"INDEX: {idx.name} row added"
    return f"INDEX: no index file next to {target.name} — edit by hand: {note}"


def _block_field(block_text: str, label: str) -> list[str]:
    """Extract the bullet-ish lines under a `**<label>**:` field in a block."""
    out, grab = [], False
    for ln in block_text.split("\n"):
        if re.match(r"^\*\*%s\**\s*[:：]" % re.escape(label), ln):
            grab = True
            rest = re.sub(r"^\*\*%s\**\s*[:：]\s*" % re.escape(label), "", ln).strip()
            if rest:
                out.append(rest)
            continue
        if grab:
            if not ln.strip() or ln.lstrip().startswith("**"):
                break
            out.append(re.sub(r"^[-*+]\s+", "", ln.strip()))
    return out


def build_new_module(target: Path, block_body: str, module_description: str,
                     verification_note: str, template: Path | None) -> str:
    """Scaffold a canonical module file for a create_new_file writeback item.

    Frontmatter: mirror the template's key order/values for module-class keys
    (type/status/generativity/exclusivity), fill identity keys from the item.
    Body: template's `## ` section order (or a sane default), with prose
    sections filled ONLY from content the distill agent actually supplied —
    no hollow boilerplate."""
    stem = target.stem
    fm_values: dict[str, str] = {}
    section_order: list[str] | None = None
    if template is not None and template.is_file():
        t = template.read_text(encoding="utf-8")
        fm = re.match(r"^---\n(.*?)\n---\n", t, re.S)
        if fm:
            for k, v in re.findall(r"^([A-Za-z_]+):\s*(.+)$", fm.group(1), re.M):
                fm_values[k] = v.strip().strip('"')
        secs = re.findall(r"^## .+$", t, re.M)
        if secs:
            section_order = secs

    fm_type = fm_values.get("type", "canonical_module")
    fm_status = fm_values.get("status", "✓ STANDARD")
    fm_generativity = fm_values.get("generativity", "ADAPTABLE")
    fm_exclusivity = fm_values.get("exclusivity", "MEDIUM")
    function_1st = re.split(r"(?<=[。.!?])\s+", module_description.strip())[0]

    sections: dict[str, list[str]] = {
        "## 功能描述": [module_description.strip(), ""],
        "## 适用场景": (["- " + b for b in _block_field(block_body, "适用")] or None) and
                    (["- " + b for b in _block_field(block_body, "适用")] + [""]),
        "## 验证状态": [
            "### 单源验证",
            f"- {verification_note}",
            "- 待第二篇跨论文复现后升 ROBUST",
            "",
        ],
        "## 句法模板": [block_body, ""],
        "## 组装规则": (
            ["### 互斥", ""] + ["- " + b for b in _block_field(block_body, "禁忌")] + [""]
            if _block_field(block_body, "禁忌") else []),
    }
    order = section_order or list(sections.keys())

    out = ["---",
           f"type: {fm_type}",
           f'canonical_id: "{stem}"',
           f"status: {fm_status}",
           f'function: "{function_1st}"',
           "generativity: " + fm_generativity,
           "exclusivity: " + fm_exclusivity,
           "created: " + date.today().isoformat(),
           'source: "corpus_writeback.py create_new_file（gate ① 裁决新建模块）"',
           "---",
           "",
           f"# {stem} — {function_1st}",
           ""]
    for sec in order:
        body = sections.get(sec)
        if not body:
            continue
        out.append(sec)
        out.extend(body)
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def update_index(corpus_root: Path, target: Path, note: str,
                 new_text: dict) -> str:
    """Append an index note to the row mentioning the target file stem.
    Recognized rows end with '） |' (parenthetical variant list) — insert before
    the closing paren; otherwise append '；<note>' before the trailing ' |'
    (lands in the LAST cell of multi-column tables — approximate; the dry-run
    diff is the review surface, fix placement there if it matters)."""
    if not note:
        return "INDEX: no index_note given — SKIPPED"
    for idx in sorted(target.parent.glob("_index.md")) + sorted(target.parent.glob("INDEX.md")):
        text = new_text.get(str(idx)) or idx.read_text(encoding="utf-8")
        lines = text.split("\n")
        hits = [i for i, l in enumerate(lines)
                if target.stem in l and l.lstrip().startswith("|")]
        if len(hits) != 1:
            continue
        i = hits[0]
        row = lines[i]
        if row.rstrip().endswith("） |"):
            row = row.rstrip()[:-3] + f"；{note}） |"
        elif row.rstrip().endswith("|"):
            row = row.rstrip()[:-1].rstrip() + f"；{note} |"
        else:
            return f"INDEX: row format unrecognized in {idx.name} — edit by hand: {note}"
        lines[i] = row
        new_text[str(idx)] = "\n".join(lines)
        return f"INDEX: {idx.name} row updated"
    return f"INDEX: no unique row for '{target.stem}' — edit by hand: {note}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Execute a confirmed writeback plan")
    ap.add_argument("--plan", required=True)
    ap.add_argument("--blocks", default=None,
                    help="optional; plan items may carry block_text/index_note directly")
    ap.add_argument("--paper", required=True, help="citekey")
    ap.add_argument("--journal", required=True)
    ap.add_argument("--gap", default="Incompleteness",
                    choices=["Incompleteness", "Inadequacy", "Incommensurability"])
    ap.add_argument("--apply", action="store_true", help="write files (default: dry-run diffs)")
    args = ap.parse_args()

    plan = yaml.safe_load(Path(args.plan).read_text(encoding="utf-8"))
    if args.blocks:
        blocks_spec = yaml.safe_load(Path(args.blocks).read_text(encoding="utf-8"))
        blocks = {b["name"]: b for b in (blocks_spec.get("blocks") or [])}
    else:
        blocks = {}
    corpus_root = Path(plan["corpus_root"])
    if not corpus_root.is_dir():
        print(f"ERROR: corpus root missing: {corpus_root}", file=sys.stderr)
        return 2
    registry = Path(plan["registry"]) if plan.get("registry") else None

    new_text: dict[str, str] = {}
    messages: list[str] = []
    rc = 0
    for item in plan["items"]:
        name = item["name"]
        verdict = item["dedup"]["verdict"]
        entry = blocks.get(name) or {}
        block_text = entry.get("block_text") or item.get("block_text")
        index_note = entry.get("index_note") or item.get("index_note") or ""
        file_override = entry.get("file") or item.get("file_override")
        if verdict == "SKIP":
            messages.append(f"[{name}] REFUSED: verdict SKIP（语料已覆盖，禁止写回）")
            rc = 1
            continue
        if verdict == "create_new_file":
            # 2026-08-29 (v2 plan): scaffold a NEW canonical module file —
            # kills the manual "方案 B" triple (module file + _index row +
            # registry) that gate ① used to hand off to the main loop.
            rel = item.get("new_file") or file_override
            if not rel:
                messages.append(f"[{name}] SKIPPED: create_new_file needs new_file "
                                f"(path relative to corpus_root)")
                rc = 1
                continue
            target = corpus_root / rel
            desc = entry.get("module_description") or item.get("module_description")
            if not desc:
                messages.append(f"[{name}] SKIPPED: create_new_file needs module_description")
                rc = 1
                continue
            marker = f"<!-- wb:{args.paper}:{name} -->"
            if target.exists():
                t0 = target.read_text(encoding="utf-8")
                if marker in t0 or body_similarity_pattern(block_text).search(t0):
                    messages.append(f"[{name}] ALREADY-APPLIED: new file exists "
                                    f"with marker/body — skipped")
                    continue
                messages.append(f"[{name}] REFUSED: create_new_file target already "
                                f"exists: {target}")
                rc = 1
                continue
            tpl_name = item.get("template_of")
            template = corpus_root / tpl_name if tpl_name else None
            if template is not None and not template.is_file():
                hits = list(corpus_root.rglob(tpl_name))
                template = hits[0] if hits else None
            label = "A"
            body = block_text.replace("{NEXT}", label).strip("\n")
            note = (index_note or module_description).replace("{NEXT}", label)
            content = build_new_module(target, body, desc, note, template)
            content += f"\n<!-- wb:{args.paper}:{name} -->\n"
            new_text[str(target)] = content
            messages.append(f"[{name}] CREATE -> {target.name} (module scaffold, 变体 A)")
            messages.append(f"[{name}] " + add_index_row(corpus_root, target, note, new_text))
            if registry:
                messages.append(f"[{name}] " + update_registry(
                    registry, target.stem, args.paper, args.journal, args.gap, new_text))
            continue

        target = resolve_target(corpus_root, item, file_override)
        if target is None:
            messages.append(f"[{name}] SKIPPED: no anchor file (override via blocks.yaml file:)")
            rc = 1
            continue
        if not block_text:
            messages.append(f"[{name}] SKIPPED: no block_text (blocks.yaml 与 plan 均无)")
            rc = 1
            continue

        path = str(target)
        text = new_text.get(path) or target.read_text(encoding="utf-8")
        # Idempotency (2026-08-29): re-running --apply on the same plan must
        # never duplicate blocks. Two signals, either one skips the item:
        #   1. provenance marker from a previous executor run
        #   2. an identical block body already present (pre-marker/legacy
        #      blocks; {NEXT}-aware match, same logic as the dedup repair)
        marker = f"<!-- wb:{args.paper}:{name} -->"
        if marker in text:
            messages.append(f"[{name}] ALREADY-APPLIED: marker present — skipped")
            continue
        if body_similarity_pattern(block_text).search(text):
            messages.append(f"[{name}] ALREADY-APPLIED: identical block body "
                            f"present (no marker) — skipped")
            continue
        lines = text.split("\n")
        label = next_variant_label(lines)
        body = block_text.replace("{NEXT}", label).strip("\n")
        # provenance warning (P1b, 2026-08-24): precheck flagged the plan item
        # as anchor-less; if the final body still carries no anchor marker,
        # surface it for gate ① rather than silently writing back an unanchored
        # variant. Warning only — no rc change.
        if item.get("provenance_warning") and not any(
            m in body for m in ("原文锚定", "原文锚点", "原始句锚点")
        ):
            messages.append(f"[{name}] WARN: {item['provenance_warning']}")
        at, anchor_warn = insertion_index(lines, item, target)
        if anchor_warn:
            messages.append(f"[{name}] WARN: {anchor_warn}")
        lines[at:at] = ["", body + "\n\n" + marker, ""]
        new_text[path] = "\n".join(lines)
        messages.append(f"[{name}] {verdict} -> {target.name} 变体 {label} "
                        f"(inserted after line {at})")

        note = index_note.replace("{NEXT}", label)
        messages.append(f"[{name}] " + update_index(corpus_root, target, note, new_text))
        if registry:
            messages.append(f"[{name}] " + update_registry(
                registry, target.stem, args.paper, args.journal, args.gap, new_text))

    if not args.apply:
        for path, text in new_text.items():
            old_p = Path(path)
            old = old_p.read_text(encoding="utf-8").split("\n") if old_p.is_file() else []
            diff = difflib.unified_diff(old, text.split("\n"),
                                        fromfile=path, tofile=path + " (new)",
                                        lineterm="", n=2)
            sys.stdout.writelines(d + "\n" for d in diff)
        print("\n".join(messages))
        print("\nDRY-RUN — rerun with --apply to write.")
        return rc

    for path, text in new_text.items():
        Path(path).write_text(text, encoding="utf-8")
    if registry and str(registry) in new_text:
        try:
            yaml.safe_load(new_text[str(registry)])
        except yaml.YAMLError as e:
            print(f"ERROR: registry YAML invalid after edit: {e}", file=sys.stderr)
            return 2
    print("\n".join(messages))
    print(json.dumps({"applied": sorted(new_text)}, ensure_ascii=False, indent=2))
    return rc


if __name__ == "__main__":
    sys.exit(main())
