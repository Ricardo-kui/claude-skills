#!/usr/bin/env python3
"""Post-writeback verification for distill-paper-exemplar (L4 mandatory gate).

Audits corpus state AFTER all writeback agents have exited, against one or
more writeback_plan.*.yaml files. Deterministic — no LLM, no corpus mutation.

Checks per plan item (block_text + resolvable target required):
  V1 body-unique   the inserted block body occurs EXACTLY once in its target
                   file ({NEXT}-aware fuzzy-join match — same logic as the
                   dedup repair). 0 = missing, >1 = duplicate insertion.
  V2 marker        `<!-- wb:<paper>:<item> -->` present once. Blocks written
                   by corpus_writeback.py after 2026-08-29 carry it; older
                   blocks report 'legacy' (informational, not a failure).

Registry checks (per plan registry file):
  V4 yaml-valid    registry parses as YAML.
  V3a no-double    NO entry's papers list contains the citekey more than
                   once (double-bump from a re-applied run = FAIL).
  V3b per-stem     for each target-file stem with a located entry that has a
                   `papers:` list: citekey appears exactly once
                   (0 = lost increment -> residual; >1 -> FAIL double-bump).
                   Entries located via stem, dash->underscore, REGISTRY_ALIASES.
                   Stems with no entry -> residual registry_no_entry (expected
                   for paper-level or estimator-slot registries — the
                   residuals file routes them to one sync pass).
                   Paper-level tracking fallback: if the registry keys entries
                   by citekey (write-theory schema), a top-level
                   `<citekey>:` entry counts as tracked (no residual).

Index checks per target:
  V5 index-row     an _index.md / INDEX.md row mentioning the stem exists in
                   the target's directory. Directory without any index file
                   -> info only. Index present, row missing -> residual
                   index_no_row.

Residuals (never FAILs — they are expected outputs of known schema gaps) are
written to --residuals-out (default: writeback_residuals.yaml next to the
first plan) so a single downstream sync pass can consume them. Residual-writing
subagents must NOT run corpus_writeback.py; this file is their complete work
order.

Exit codes: 0 = all V-checks pass (residuals allowed, listed);
            1 = FAIL (missing/duplicate block, double-bumped registry,
                invalid YAML).

Usage:
  py verify_writeback.py --plan writeback_plan.theory.yaml \
      --plan writeback_plan.methods.yaml \
      --paper fang_et_al_2025_rival_recall_ad_spend \
      [--residuals-out path/to/writeback_residuals.yaml]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_writeback as cw  # noqa: E402  (REGISTRY_ALIASES, resolve_target,
#                               body_similarity_pattern — single source of truth)

# Declared registry tracking schema per corpus root (suffix match, first hit
# wins). Drives V3b expectations; runtime detection stays as fallback for
# unlisted corpora (2026-08-29 v2 plan item D).
CORPUS_SCHEMA = {
    "write-introduction/academic-writing-corpus": "papers-list",
    "write-theory/corpus": "paper-level",
    "write-methods/econometric-models": "papers-list",
    "write-results/econometric-models": "slot-schema",
}


def corpus_schema(corpus_root: Path) -> str | None:
    s = str(corpus_root).replace("\\", "/").lower()
    for suffix, schema in CORPUS_SCHEMA.items():
        if suffix in s:
            return schema
    return None


def find_registry_entry(text: str, stem: str):
    """Locate an entry for stem (read-only mirror of update_registry's lookup,
    plus dash->underscore fallback). Returns (key, paper_count, entry_text)
    where paper_count is None for slot-schema entries (estimator heads carry
    usage_stats, not paper_count), or None when no entry exists."""
    keys = [stem]
    if stem in cw.REGISTRY_ALIASES:
        keys.insert(0, cw.REGISTRY_ALIASES[stem][1])
    keys.append(stem.replace("-", "_"))
    for key in keys:
        pat = re.compile(r"^( +)%s:\n( +)paper_count: (\d+)" % re.escape(key), re.M)
        m = pat.search(text)
        if m:
            ind = m.group(1)
            start = m.start()
            nxt = re.search(r"^ {1,%d}\S" % len(ind), text[m.end():], re.M)
            end = m.end() + nxt.start() if nxt else len(text)
            return key, int(m.group(3)), text[start:end]
        # slot-schema fallback: key line followed by any subkey (usage_stats…)
        pat2 = re.compile(r"^( +)%s:\n( +)\w" % re.escape(key), re.M)
        m2 = pat2.search(text)
        if m2:
            ind = m2.group(1)
            start = m2.start()
            nxt = re.search(r"^ {1,%d}\S" % len(ind), text[m2.end():], re.M)
            end = m2.end() + nxt.start() if nxt else len(text)
            return key, None, text[start:end]
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description="Verify corpus state after writeback")
    ap.add_argument("--plan", action="append", required=True,
                    help="writeback_plan yaml; repeatable")
    ap.add_argument("--paper", required=True, help="citekey")
    ap.add_argument("--residuals-out", default=None,
                    help="default: writeback_residuals.yaml next to first plan")
    args = ap.parse_args()

    paper = args.paper
    checks: list[tuple[str, str, str]] = []   # (status, check_id, detail)
    residuals: list[dict] = []

    def add(status: str, cid: str, detail: str) -> None:
        checks.append((status, cid, detail))

    registry_texts: dict[str, str] = {}
    plans = []
    for plan_path in args.plan:
        plan = yaml.safe_load(Path(plan_path).read_text(encoding="utf-8"))
        plans.append((plan_path, plan))
        reg = plan.get("registry")
        if reg:
            rp = Path(reg)
            if str(rp) not in registry_texts:
                registry_texts[str(rp)] = rp.read_text(encoding="utf-8") if rp.is_file() else ""

    for plan_path, plan in plans:
        section = plan.get("section", Path(plan_path).stem)
        corpus_root = Path(plan["corpus_root"])
        schema = corpus_schema(corpus_root)
        for item in plan.get("items", []):
            name = item["name"]
            block_text = item.get("block_text")
            target = cw.resolve_target(corpus_root, item,
                                       item.get("file_override"))
            if target is None and item.get("new_file"):
                # create_new_file items: the module was scaffolded at apply time
                target = corpus_root / item["new_file"]
            if not block_text or target is None:
                add("SKIP", "V1", f"{section}:{name} — no block_text or no target; not verifiable")
                continue
            text = target.read_text(encoding="utf-8")
            n = len(cw.body_similarity_pattern(block_text).findall(text))
            if n == 1:
                add("PASS", "V1", f"{section}:{name} -> {target.name} body×1")
            elif n == 0:
                add("FAIL", "V1", f"{section}:{name} -> {target.name} body MISSING")
            else:
                add("FAIL", "V1", f"{section}:{name} -> {target.name} body DUPLICATED ×{n}")
            marker = f"<!-- wb:{paper}:{name} -->"
            nm = text.count(marker)
            if nm == 1:
                add("PASS", "V2", f"{section}:{name} marker×1")
            elif nm == 0:
                add("INFO", "V2", f"{section}:{name} no marker (legacy block)")
            else:
                add("FAIL", "V2", f"{section}:{name} marker×{nm}")

            # V3b per-stem registry check (schema-declared, runtime fallback)
            if str(target) and plan.get("registry"):
                rtext = registry_texts[str(Path(plan["registry"]))]
                if schema == "paper-level":
                    # paper-level schema (write-theory): stems carry no entries
                    if re.search(r"^(\s+)%s:" % re.escape(paper), rtext, re.M):
                        add("INFO", "V3b",
                            f"{section}:{target.stem} paper-level entry for {paper} present")
                    else:
                        residuals.append({
                            "type": "registry_no_entry", "section": section,
                            "stem": target.stem, "item": name,
                            "hint": "sync pass: add paper-level entry with fragments"})
                    _skip_stem_lookup = True
                else:
                    _skip_stem_lookup = False
                found = None if _skip_stem_lookup else find_registry_entry(rtext, target.stem)
                found = find_registry_entry(rtext, target.stem)
                if found is None:
                    # paper-level schema fallback (write-theory: entry keyed by citekey)
                    if re.search(r"^(\s+)%s:" % re.escape(paper), rtext, re.M):
                        add("INFO", "V3b",
                            f"{section}:{target.stem} no stem entry; paper-level entry for "
                            f"{paper} present (schema-consistent)")
                    else:
                        residuals.append({
                            "type": "registry_no_entry", "section": section,
                            "stem": target.stem, "item": name,
                            "hint": "sync pass: add entry or extend REGISTRY_ALIASES"})
                else:
                    key, _count, entry = found
                    if _count is None:
                        # slot-schema entry (estimator head): variant ids carry
                        # the paper's registration signal, not a papers list
                        if item["name"] in entry:
                            add("PASS", "V3b",
                                f"registry '{key}' slot-schema: variant {item['name']} registered")
                        else:
                            residuals.append({
                                "type": "registry_variant_missing", "section": section,
                                "stem": target.stem, "key": key, "item": name,
                                "hint": f"sync pass: add {name} under {key}'s slots"})
                    elif re.search(r"^\s*papers:\s*$", entry, re.M):
                        hits = len(re.findall(
                            r"^\s*- %s \(" % re.escape(paper), entry, re.M))
                        if hits == 0:
                            residuals.append({
                                "type": "registry_missing_paper", "section": section,
                                "stem": target.stem, "key": key, "item": name,
                                "hint": "sync pass: add paper line + bump paper_count"})
                        elif hits > 1:
                            add("FAIL", "V3a",
                                f"registry entry '{key}' papers list has citekey ×{hits} (double bump)")
                        else:
                            add("PASS", "V3b", f"registry '{key}' papers×1")
                    else:
                        add("INFO", "V3b",
                            f"registry entry '{key}' has no papers list (slot/variant schema)")

            # V5 index row
            idx_files = sorted(target.parent.glob("_index.md")) + \
                sorted(target.parent.glob("INDEX.md")) + \
                sorted(target.parent.glob("_index.yaml"))
            if not idx_files:
                add("INFO", "V5", f"{target.name}: directory has no index file")
                continue
            row_hits = sum(
                1 for idx in idx_files
                for ln in idx.read_text(encoding="utf-8").split("\n")
                if target.stem in ln)
            if row_hits >= 1:
                add("PASS", "V5", f"{target.name} index row present")
            else:
                residuals.append({
                    "type": "index_no_row", "section": section,
                    "stem": target.stem, "item": name,
                    "hint": f"sync pass: add row mentioning {target.stem} to "
                            f"{idx_files[0].name}"})

    for rp, text in registry_texts.items():
        if not text:
            add("FAIL", "V4", f"registry missing on disk: {rp}")
            continue
        try:
            yaml.safe_load(text)
            add("PASS", "V4", f"registry YAML valid: {Path(rp).name}")
        except yaml.YAMLError as e:
            add("FAIL", "V4", f"registry YAML INVALID: {rp}: {e}")

    n_pass = sum(1 for s, _, _ in checks if s == "PASS")
    n_fail = sum(1 for s, _, _ in checks if s == "FAIL")
    n_info = sum(1 for s, _, _ in checks if s == "INFO")
    n_skip = sum(1 for s, _, _ in checks if s == "SKIP")
    for s, cid, detail in checks:
        print(f"[{s:4}] {cid} {detail}")
    print("-" * 70)
    print(f"PASS {n_pass} / FAIL {n_fail} / INFO {n_info} / SKIP {n_skip}; "
          f"residuals: {len(residuals)}")

    out = args.residuals_out or str(Path(args.plan[0]).parent / "writeback_residuals.yaml")
    if residuals or Path(out).exists():
        doc = {
            "generated": datetime.now().isoformat(timespec="seconds"),
            "paper": paper,
            "residuals": residuals,
        }
        Path(out).write_text(
            yaml.safe_dump(doc, allow_unicode=True, sort_keys=False),
            encoding="utf-8")
        print(f"residuals -> {out}")

    print(json.dumps({"verdict": "FAIL" if n_fail else "PASS",
                      "fails": n_fail, "residuals": len(residuals)},
                     ensure_ascii=False))
    return 1 if n_fail else 0


if __name__ == "__main__":
    sys.exit(main())
