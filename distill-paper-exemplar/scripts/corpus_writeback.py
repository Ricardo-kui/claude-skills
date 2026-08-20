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
VARIANT_HEAD = re.compile(r"^#{2,4}\s+变体\s+([A-Z]+|\d+)", re.M)
BAD_ANCHOR = re.compile(r"反模式|诚实边界|anti-?pattern|boundar", re.I)
GOOD_ANCHOR = re.compile(r"变体|variant|pattern", re.I)


def load_blocks(lines: list[str]) -> list[dict]:
    heads = [(i, ln) for i, ln in enumerate(lines) if BLOCK_HEAD.match(ln)]
    out = []
    for k, (i, ln) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        out.append({"heading": ln.strip(), "start": i, "end": end})
    return out


def next_variant_label(lines: list[str]) -> str:
    letters, numbers = [], []
    for ln in lines:
        m = VARIANT_HEAD.match(ln)
        if m:
            (letters if m.group(1).isalpha() else numbers).append(m.group(1))
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


def insertion_index(lines: list[str], item: dict, target: Path) -> int:
    """0-based line index AFTER which the block is inserted.

    EXTEND -> end of the matched variant block (by anchor heading).
    ADD    -> end of the last variant/pattern block (never a boundaries block);
              falls back to end of file.
    Recomputed at execution time — never trust stale plan line numbers.
    """
    blocks = load_blocks(lines)
    anchor = item.get("anchor") or {}
    verdict = item["dedup"]["verdict"]
    if verdict == "EXTEND" and anchor.get("after_heading"):
        for b in blocks:
            if b["heading"][:80] == anchor["after_heading"]:
                return b["end"]
    good = [b for b in blocks if GOOD_ANCHOR.search(b["heading"])
            and not BAD_ANCHOR.search(b["heading"])]
    if good:
        return good[-1]["end"]
    if blocks:
        return blocks[-1]["end"]
    return len(lines)


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
    text = registry.read_text(encoding="utf-8")
    section, key = None, None
    if stem in REGISTRY_ALIASES:
        section, key = REGISTRY_ALIASES[stem]
    else:
        # entry keyed by stem under any evidence subsection
        pat = re.compile(r"^( +)%s:\n( +)paper_count: (\d+)" % re.escape(stem), re.M)
        m = pat.search(text)
        if m:
            key = stem
    if key is None and section is not None:
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
    blocks_spec = yaml.safe_load(Path(args.blocks).read_text(encoding="utf-8"))
    blocks = {b["name"]: b for b in (blocks_spec.get("blocks") or [])}
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
        if verdict == "SKIP":
            messages.append(f"[{name}] REFUSED: verdict SKIP（语料已覆盖，禁止写回）")
            rc = 1
            continue
        spec = blocks.get(name)
        if spec is None:
            messages.append(f"[{name}] SKIPPED: no block in blocks.yaml")
            rc = 1
            continue
        target = resolve_target(corpus_root, item, spec.get("file"))
        if target is None:
            messages.append(f"[{name}] SKIPPED: no anchor file (override via blocks.yaml file:)")
            rc = 1
            continue

        path = str(target)
        text = new_text.get(path) or target.read_text(encoding="utf-8")
        lines = text.split("\n")
        label = next_variant_label(lines)
        body = spec["block_text"].replace("{NEXT}", label).strip("\n")
        at = insertion_index(lines, item, target)
        lines[at:at] = ["", body, ""]
        new_text[path] = "\n".join(lines)
        messages.append(f"[{name}] {verdict} -> {target.name} 变体 {label} "
                        f"(inserted after line {at})")

        note = (spec.get("index_note") or "").replace("{NEXT}", label)
        messages.append(f"[{name}] " + update_index(corpus_root, target, note, new_text))
        if registry:
            messages.append(f"[{name}] " + update_registry(
                registry, target.stem, args.paper, args.journal, args.gap, new_text))

    if not args.apply:
        for path, text in new_text.items():
            old = Path(path).read_text(encoding="utf-8")
            diff = difflib.unified_diff(old.split("\n"), text.split("\n"),
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
