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
    "introduction": SKILLS_ROOT / "write-introduction" / "corpus",
    "theory": SKILLS_ROOT / "write-theory" / "corpus",
    "methods": SKILLS_ROOT / "write-methods" / "corpus",
    "results": SKILLS_ROOT / "write-results" / "corpus",
}

# file stem -> (evidence section, entry key) for registry entries that are NOT
# keyed by file stem (pooled/aliased entries; extend as discovered)
REGISTRY_ALIASES = {
    "theory-lens-driven-preview": ("theory_lens", "theory-lens-templates"),
    # write-introduction contributions/_index.md is itself the canonical variants file
    "_index": ("contributions", "contribution-statements"),
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
    run-varying label substituted for each {NEXT} slot. Labels are short and
    usually same-line, but plans occasionally place {NEXT} at end-of-line
    (e.g. a trailing `wb 批次 {NEXT}` frontmatter line), so the gap may span
    the substituted label PLUS the following line breaks — hence a bounded
    `.{0,80}?` with re.S instead of the old same-line-only `[^\n]{0,40}?`
    (2026-09-05 user-approved fix; segments themselves are long and
    distinctive, so the widened gap does not loosen duplicate detection in
    practice). Used for idempotency hardening and post-hoc audits."""
    segs = [re.escape(s.strip("\n")) for s in block_text.split("{NEXT}")]
    return re.compile(r".{0,80}?".join(segs), re.S)


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
                    gap: str, new_text: dict, slot_tag: str | None = None) -> str:
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
        # Empty-shell entry (paper_count present, papers list absent — e.g.
        # 动态面板-GMM 2026-09-12): create the list inline instead of skipping.
        # Kills the "registry-sync agent" class for methods corpora.
        # papers/paper_count are SIBLINGS at the same indent; respect the
        # file's EOL style (methods registry is CRLF).
        eol = "\r\n" if "\r\n" in entry else "\n"
        entry2 = entry.replace(
            f"paper_count: {count}",
            f"paper_count: {count + 1}{eol}{sub}papers:{eol}{sub}- {paper} ({journal})", 1)
        if slot_tag:
            sc = re.search(r"^(\s*)slots_covered:.*$", entry2, re.M)
            if sc:
                have = re.findall(r"M\d+", sc.group(0))
                merged = " ".join(sorted(set(have) | {slot_tag}))
                entry2 = entry2[:sc.start()] + f"{sc.group(1)}slots_covered: [{merged}]" + entry2[sc.end():]
        new_text[str(registry)] = text[:start] + entry2 + text[end:]
        return (f"REGISTRY: {key} papers list created, paper_count {count}->{count + 1}, "
                f"+{paper} ({journal})" + (f", slots_covered+{slot_tag}" if slot_tag else ""))
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
    if slot_tag:
        sc = re.search(r"^(\s*)slots_covered:.*$", entry2, re.M)
        if sc:
            have = re.findall(r"M\d+", sc.group(0))
            merged = " ".join(sorted(set(have) | {slot_tag}))
            entry2 = entry2[:sc.start()] + f"{sc.group(1)}slots_covered: [{merged}]" + entry2[sc.end():]
    gm = re.search(r"^(\s+)%s: (\d+)$" % re.escape(gap), entry2, re.M)
    if gm:
        entry2 = (entry2[:gm.start()]
                  + f"{gm.group(1)}{gap}: {int(gm.group(2)) + 1}"
                  + entry2[gm.end():])
    new_text[str(registry)] = text[:start] + entry2 + text[end:]
    return f"REGISTRY: {key} paper_count {count}->{count + 1}, +{paper} ({journal}), {gap}+1"


def _bump_last_updated(current: str, today: str) -> str:
    """Registry last_updated is date-letter style (2026-09-12a): same day
    increments the letter, a new day resets to `a`."""
    m = re.match(r"^(\d{4}-\d{2}-\d{2})([a-z]?)$", (current or "").strip())
    if m and m.group(1) == today:
        return today + chr(ord(m.group(2) or "`") + 1)
    return today + "a"


def update_theory_registry(registry: Path, paper: str, journal: str, gap: str,
                           applied: list, new_text: dict, title: str | None,
                           year: str | None, tbt: str | None,
                           timestamp: str) -> list[str]:
    """Per-paper tfr-fragment sync for section == theory (2026-09-12).

    Replaces the post-hoc registry-sync agent (~5M tokens/run): fragments are
    appended under source_papers.<paper> (entry created when missing), meta and
    summary_by_dimension counters follow. Items WITHOUT registry_dimension are
    left as residuals on purpose — a guessed makadok_dimension costs more than
    a manual sync. Both insertion paths are line-based (2026-09-13 rewrite:
    the first cut-arithmetic version split the previous fragment's fields)."""
    msgs = []
    lines = (new_text.get(str(registry)) or registry.read_text(encoding="utf-8")).split("\n")
    frags = []
    for name, target, label, item in applied:
        dim = item.get("registry_dimension")
        if not dim:
            msgs.append(f"[{name}] REGISTRY(theory): no registry_dimension — SKIPPED (manual sync)")
            continue
        heading = next((l for l in (item.get("block_text") or "").split("\n")
                        if l.startswith("#")), name).lstrip("# ").strip()
        try:
            home = str(target.relative_to(registry.parent)).replace("\\", "/")
        except ValueError:
            home = target.name
        frags.append({"type": name, "title": heading, "home_files": [home],
                      "makadok_dimension": dim, "status": "EMERGING",
                      "note": (item.get("index_note") or "").replace("{NEXT}", label)})
    if not frags:
        msgs.append("REGISTRY(theory): nothing to sync (no item carried registry_dimension)")
        new_text[str(registry)] = "\n".join(lines)
        return msgs
    sp_i = next((i for i, l in enumerate(lines) if l.strip() == "source_papers:"), None)
    if sp_i is None:
        return msgs + ["REGISTRY(theory): source_papers section not found — SKIPPED (manual sync)"]
    sp_end = next((i for i in range(sp_i + 1, len(lines))
                   if lines[i] and not lines[i][0].isspace()), len(lines))
    paper_new = not any(l.strip() == f"{paper}:" for l in lines[sp_i:sp_end])
    next_id = max([int(x) for x in re.findall(r"tfr_(\d+)", "\n".join(lines))] or [0]) + 1

    def fragment_lines():
        out = []
        for k, f in enumerate(frags):
            fid = f"tfr_{next_id + k}"
            out.append(f"      - fragment_id: {fid}")
            out.append(f"        type: {f['type']}")
            out.append(f'        title: "{f["title"]}"')
            out.append("        home_files:")
            for hf in f["home_files"]:
                out.append(f"          - {hf}")
            out.append(f"        makadok_dimension: {f['makadok_dimension']}")
            out.append(f"        status: {f['status']}")
            out.append(f'        note: "{f["note"]}"')
        return out

    if paper_new:
        entry = [f"  {paper}:", f'    display_name: "{title or paper}"',
                 f'    journal: "{journal}"']
        if year:
            entry.append(f'    year: "{year}"')
        entry.append(f"    gap_type: {gap}")
        if tbt:
            entry.append(f'    theory_build_type: "{tbt}"')
        entry.append("    fragments:")
        entry += fragment_lines()
        lines = lines[:sp_end] + entry + [""] + lines[sp_end:]
        msgs.append(f"REGISTRY(theory): paper entry {paper} created with "
                    f"{len(frags)} fragments (tfr_{next_id}-tfr_{next_id + len(frags) - 1})")
    else:
        e_i = next(i for i, l in enumerate(lines[sp_i:sp_end])
                   if l.strip() == f"{paper}:") + sp_i
        e_end = next((i for i in range(e_i + 1, sp_end)
                      if lines[i] and not lines[i][0].isspace()), sp_end)
        f_i = next((i for i in range(e_i + 1, e_end)
                    if lines[i].strip() == "fragments:"), None)
        if f_i is None:
            return msgs + [f"REGISTRY(theory): {paper} has no fragments list — SKIPPED (manual sync)"]
        item_is = [i for i in range(f_i + 1, e_end)
                   if re.match(r"^\s*- fragment_id:", lines[i])]
        if item_is:
            item_ind = re.match(r"^(\s*)- fragment_id:", lines[item_is[0]]).group(1)
            ins_at = item_is[-1] + 1
            while ins_at < e_end and (lines[ins_at].strip() == "" or
                                      len(lines[ins_at]) - len(lines[ins_at].lstrip()) > len(item_ind)):
                ins_at += 1
        else:
            item_ind = re.match(r"^(\s*)fragments:", lines[f_i]).group(1) + "  "
            ins_at = f_i + 1
        lines = lines[:ins_at] + fragment_lines() + lines[ins_at:]
        msgs.append(f"REGISTRY(theory): {len(frags)} fragments appended to {paper} "
                    f"(tfr_{next_id}-tfr_{next_id + len(frags) - 1})")
    text = "\n".join(lines)
    # summary_by_dimension 计数（行级，逐维度）
    for dim in {f["makadok_dimension"] for f in frags}:
        n = sum(1 for f in frags if f["makadok_dimension"] == dim)
        dm = next((i for i, l in enumerate(lines) if l.strip() == f"{dim}:"), None)
        if dm is None:
            msgs.append(f"REGISTRY(theory): WARN summary_by_dimension[{dim}] not found — counters not bumped")
            continue
        for j in range(dm + 1, min(dm + 5, len(lines))):
            if "total_fragments:" in lines[j]:
                v = int(re.search(r"(\d+)", lines[j].split(":", 1)[1]).group(1))
                lines[j] = re.sub(r"(\d+)", str(v + n), lines[j], count=1)
            if "source_papers:" in lines[j]:
                v = int(re.search(r"(\d+)", lines[j].split(":", 1)[1]).group(1))
                lines[j] = re.sub(r"(\d+)", str(v + (1 if paper_new else 0)), lines[j], count=1)
    text = "\n".join(lines)
    # meta 计数
    for i, l in enumerate(lines):
        if l.strip().startswith("total_papers_indexed:"):
            v = int(l.split(":", 1)[1].strip())
            lines[i] = re.sub(r"(\d+)", str(v + (1 if paper_new else 0)), l, count=1)
        if l.strip().startswith("batches_processed:"):
            v = int(l.split(":", 1)[1].strip())
            lines[i] = re.sub(r"(\d+)", str(v + 1), l, count=1)
        if l.strip().startswith("last_updated:"):
            cur = l.split(":", 1)[1].strip()
            lines[i] = re.sub(r"last_updated: \S+", f"last_updated: {_bump_last_updated(cur, timestamp)}", l, count=1)
    text = "\n".join(lines)
    new_text[str(registry)] = text
    return msgs


def update_results_registry(registry: Path, paper: str, applied: list,
                            new_text: dict, timestamp: str) -> list[str]:
    """Estimator slot-append sync for section == results (2026-09-12).

    Slot = item-name prefix r<N>_; registry key = file stem with `-` → `_`
    (registry keys are underscore-style; the executor previously missed
    hyphen stems — Gulati-1999/ridge runs). Appends skeleton_variants items
    plus batch_history and meta bumps."""
    msgs = []
    text = new_text.get(str(registry)) or registry.read_text(encoding="utf-8")
    done = 0
    for name, target, label, item in applied:
        ms = re.match(r"r(\d+)_", name)
        if not ms:
            continue
        slot, key = f"R{ms.group(1)}", target.stem.replace("-", "_")
        ke = re.search(rf"^  {re.escape(key)}:\s*$", text, re.M)
        if not ke:
            msgs.append(f"[{name}] REGISTRY(results): estimator '{key}' not found — SKIPPED (manual sync)")
            continue
        nxt_e = re.search(r"^  \S", text[ke.end():], re.M)
        e_end = ke.end() + (nxt_e.start() if nxt_e else len(text) - ke.end())
        ktext = text[ke.end():e_end]
        se = re.search(rf"^(\s+){slot}:\s*$", ktext, re.M)
        if not se:
            msgs.append(f"[{name}] REGISTRY(results): slot {slot} not found under {key} — SKIPPED (manual sync)")
            continue
        sv = re.search(r"^(\s+)skeleton_variants:.*$", ktext[se.end():], re.M)
        if not sv:
            msgs.append(f"[{name}] REGISTRY(results): skeleton_variants not found — SKIPPED (manual sync)")
            continue
        base = se.end() + sv.start()
        ind_item = sv.group(1)  # 真实风格：列表项与 skeleton_variants 键同缩进
        skeleton = " ".join(_block_field(item.get("block_text") or "", "骨架")) or "见语料块"
        notes = " ".join(_block_field(item.get("block_text") or "", "与原骨架差异")) \
            or (item.get("index_note") or "").replace("{NEXT}", label)
        block = (f"{ind_item}- id: {name}\n"
                 f"{ind_item}  skeleton: >-\n"
                 + "".join(f"{ind_item}    {ln.strip()}\n" for ln in skeleton.split(". ") if ln.strip())
                 + f"{ind_item}  notes: >-\n"
                 + "".join(f"{ind_item}    {ln.strip()}\n" for ln in f"corpus {target.stem}.md {label}：{notes}".split("；") if ln.strip()))
        ins_at = ke.end() + base + sv.end() + 1
        # append at the END of the skeleton_variants list: next line at item indent or less
        tail = ins_at
        tl = text.split("\n")
        # walk in line space for the list end
        line_no = text[:ins_at].count("\n")
        j = line_no
        while j < len(tl) - 1 and (tl[j + 1].strip() == "" or tl[j + 1].startswith(ind_item) or tl[j + 1].startswith(sv.group(1) + "- ")):
            j += 1
        ins_at_line = j + 1
        text = "\n".join(tl[:ins_at_line]) + "\n" + block.rstrip("\n") + "\n" + "\n".join(tl[ins_at_line:])
        done += 1
        msgs.append(f"[{name}] REGISTRY(results): {key}.slots.{slot}.skeleton_variants +1 (corpus {target.stem}.md {label})")
    if done:
        tl = text.split("\n")
        paper_new = not any(l.strip().startswith(f"source_paper: {paper}") for l in tl)
        n_batch = max([int(x) for x in re.findall(r"batch_(\d+)", text)] or [0]) + 1
        bid = f"batch_{n_batch}_{paper}_writeback"
        bh_i = next((i for i, l in enumerate(tl) if l.strip() == "batch_history:"), None)
        if bh_i is None:
            msgs.append("REGISTRY(results): WARN batch_history section not found — batch not recorded")
        else:
            list_indent = "  "
            if bh_i + 1 < len(tl) and re.match(r"^\s*- ", tl[bh_i + 1]):
                list_indent = re.match(r"^(\s*)- ", tl[bh_i + 1]).group(1)
            j = bh_i + 1
            while j < len(tl) and (tl[j].startswith(list_indent + "- ")
                                   or tl[j].strip() == ""
                                   or tl[j].startswith(list_indent + "  ")):
                j += 1
            entry_lines = [f"{list_indent}- batch_id: {bid}",
                           f"{list_indent}  timestamp: {timestamp}",
                           f"{list_indent}  source_paper: {paper}",
                           f"{list_indent}  slot_updates_count: {done}",
                           f"{list_indent}  novel_patterns_count: {done}"]
            tl = tl[:j] + entry_lines + tl[j:]
            text = "\n".join(tl)
        text = re.sub(r"^(  batches_processed: )(\d+)",
                      lambda mm: mm.group(1) + str(int(mm.group(2)) + 1), text, count=1, flags=re.M)
        text = re.sub(r"^(  total_papers_indexed: )(\d+)",
                      lambda mm: mm.group(1) + str(int(mm.group(2)) + (1 if paper_new else 0)),
                      text, count=1, flags=re.M)
        lb = re.search(r"^(  last_batch_id: )(\S+)", text, re.M)
        if lb:
            text = text[:lb.start()] + f"{lb.group(1)}{bid}" + text[lb.end():]
        lu = re.search(r"^(  last_updated: )(\S+)", text, re.M)
        if lu:
            text = text[:lu.start()] + f"{lu.group(1)}{_bump_last_updated(lu.group(2), timestamp)}" + text[lu.end():]
        msgs.append(f"REGISTRY(results): batch {bid} recorded ({done} slot updates)")
    new_text[str(registry)] = text
    return msgs


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
    ap.add_argument("--paper-title", default=None,
                    help="paper title (theory registry display_name; plan paper_meta overrides)")
    ap.add_argument("--paper-year", default=None,
                    help="publication year (theory registry; plan paper_meta overrides)")
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
    applied: list = []
    section = str(plan.get("section") or "")
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
        slot_tag = (f"M{re.match(r'm(\d+)_', name).group(1)}"
                    if re.match(r"m(\d+)_", name) else None)
        if registry and section not in ("theory", "results"):
            # theory/results 的 registry 同步由节级函数接管（apply 循环后统一执行）
            messages.append(f"[{name}] " + update_registry(
                registry, target.stem, args.paper, args.journal, args.gap, new_text,
                slot_tag=slot_tag))
        applied.append((name, target, label, item))

    if registry and section == "theory":
        pm = plan.get("paper_meta") or {}
        messages += update_theory_registry(
            registry, args.paper, args.journal, args.gap, applied, new_text,
            title=args.paper_title or pm.get("title"),
            year=str(args.paper_year or pm.get("year") or "") or None,
            tbt=pm.get("theory_build_type"), timestamp=date.today().isoformat())
    elif registry and section == "results":
        messages += update_results_registry(
            registry, args.paper, applied, new_text, timestamp=date.today().isoformat())

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
