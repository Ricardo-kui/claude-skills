#!/usr/bin/env python3
"""S6 switch: rebuild DERIVED registry segments from the wb-marked block truth.

`rebuild_views.py --check` only compares. This module is the --apply
implementation it guards (plan §S6): for each corpus, regenerate the DERIVED
segments of `_evidence_registry.yaml` from a fresh corpus scan, carrying every
AUTHORED/passthrough field (plan §3 contract). Guarantees:

  1. Only DERIVED segments are rewritten — AUTHORED segments are re-emitted
     byte-identical (asserted against the pre-image).
  2. Derived lists UNION on-disk legacy values with block-derived values
     (legacy entries without wb markers are history, never dropped).
  3. tfr fragment ids: carried for matched fragments; new fragments continue
     the max+1 sequence (append-only issuance, shared with the executor).
  4. status = ladder(n_sources) ⊕ status_overrides (AUTHORED overrides win).
  5. Full-file YAML round-trip validation before write; default is dry-run.

Usage:
  py rebuild_apply.py                       # dry-run, all corpora
  py rebuild_apply.py --corpus theory --apply
"""
from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_views as rv  # noqa: E402

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent

# derived-segment root keys per corpus, in S2 layout order
SEGMENT_KEYS = {
    "introduction": ["evidence", "paper_index"],
    "theory": ["meta", "source_papers", "patterns", "summary_by_dimension"],
    "methods": ["meta", "evidence"],
    "results": ["meta", "estimators"],
}


# --------------------------------------------------------------------------- #
# rendering (parse→render round-trip must be value-identical)
# --------------------------------------------------------------------------- #

def _needs_quote(s: str) -> bool:
    if s == "" or s != s.strip():
        return True
    if re.match(r"^(19|20)\d{2}([-/.]\d{2}){0,2}$", s):  # date-ish
        return True
    if re.fullmatch(r"[-+]?(\d[_./:])*?\d+", s) and any(c.isdigit() for c in s):
        return True
    if re.fullmatch(r"(?i)(true|false|null|yes|no|on|off|~)", s):
        return True
    return bool(re.search(r"""[:#\&\*\!\|>'"%@`\{\}\[\],]|(?:  |\t)|[\n\r]""", s))


def render_scalar(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    s = str(v)
    if not _needs_quote(s):
        return s
    esc = (s.replace("\\", "\\\\").replace('"', '\\"')
           .replace("\r\n", "\\n").replace("\n", "\\n").replace("\r", "\\n")
           .replace("\t", "\\t"))
    return f'"{esc}"'


def render_node(obj, indent: int, lines: list[str]) -> None:
    pad = " " * indent
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, dict) and v:
                lines.append(f"{pad}{k}:")
                render_node(v, indent + 2, lines)
            elif isinstance(v, list) and v:
                lines.append(f"{pad}{k}:")
                render_node(v, indent + 2, lines)
            elif isinstance(v, (dict, list)):
                lines.append(f"{pad}{k}: []")
            else:
                lines.append(f"{pad}{k}: {render_scalar(v)}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                items = list(item.items())
                if not items:
                    lines.append(f"{pad}- {{}}")
                    continue
                k0, v0 = items[0]
                if isinstance(v0, (dict, list)) and v0:
                    lines.append(f"{pad}- {k0}:")
                    render_node(v0, indent + 4, lines)
                else:
                    lines.append(f"{pad}- {k0}: {render_scalar(v0)}")
                render_node(dict(items[1:]), indent + 2, lines)
            elif isinstance(item, list):
                lines.append(f"{pad}-")
                render_node(item, indent + 2, lines)
            else:
                lines.append(f"{pad}- {render_scalar(item)}")
    else:
        lines.append(f"{pad}{render_scalar(obj)}")


def render_root(obj) -> str:
    lines: list[str] = []
    render_node(obj, 0, lines)
    return "\n".join(lines) + "\n"


def diff_paths(old, new, path: tuple = (), out: list | None = None) -> list:
    if out is None:
        out = []
    if isinstance(old, dict) and isinstance(new, dict):
        for k in old.keys() | new.keys():
            diff_paths(old.get(k), new.get(k), path + (str(k),), out)
    elif isinstance(old, list) and isinstance(new, list):
        for i in range(max(len(old), len(new))):
            diff_paths(old[i] if i < len(old) else None,
                       new[i] if i < len(new) else None, path + (f"[{i}]",), out)
    elif old != new:
        out.append((path, old, new))
    return out


# --------------------------------------------------------------------------- #
# shared derivation helpers
# --------------------------------------------------------------------------- #

def _block_gaps(blocks) -> dict[str, str]:
    gaps: dict[str, str] = {}
    for b in blocks:
        for ck, _ in b.wb:
            g = (b.wb_meta or {}).get("gap")
            if g:
                gaps.setdefault(ck, g)
    return gaps


_ATTRIBUTION: dict[str, int] = {}


def _status_for(doc: dict, path: str, n_sources: int, current=None,
                paper_keys=None, auxiliary: bool = False) -> str:
    """status_overrides ⊕ status_policy ⊕ ladder (C item). Never DOWNGRADES
    below an on-disk VERIFIED/ROBUST: a high status at low source count is
    either an override (which wins anyway), a policy author/domain rule hit
    (scripts/status_policy.yaml), or a pre-partition carried user ruling
    whose basis lives in the carried verification_basis/note fields — rebuild
    destroying it would silently repeal user rulings (S1 classified those
    drifts 'status_overrides owns this', i.e. resolved by adding override
    rows, never by downgrade). Decision attribution accumulates into
    _ATTRIBUTION (S5 observability; reset per apply_corpus run)."""
    ov = rv.status_override_for(doc, path)
    if ov and ov.get("status"):
        _ATTRIBUTION["override"] = _ATTRIBUTION.get("override", 0) + 1
        return str(ov["status"])
    pstat, _prule = rv.policy_status(paper_keys, n_sources, rv.cached_policy(),
                                     auxiliary=auxiliary)
    base = pstat or rv.ladder_status(n_sources)
    cur = rv.norm_status(str(current or ""))
    # never-demote: any on-disk VERIFIED/ROBUST beats a lower derived base.
    # (The ROBUST-vs-VERIFIED leg matters: ROBUST is not scan-derivable, so a
    # 5-source curated ROBUST row must not be rewritten VERIFIED just because
    # the ladder tops out there — the checker already treats that pair as
    # 'expected_status_override'.)
    if cur in ("VERIFIED", "ROBUST") and base in rv.LADDER and \
            rv.LADDER.index(base) < rv.LADDER.index(cur):
        _ATTRIBUTION["never-demote"] = _ATTRIBUTION.get("never-demote", 0) + 1
        return cur
    _ATTRIBUTION["policy" if pstat else "ladder"] = \
        _ATTRIBUTION.get("policy" if pstat else "ladder", 0) + 1
    return base


def _tfr_next(all_ids) -> int:
    nums = [int(m.group(1)) for i in all_ids if (m := re.search(r"tfr_(\d+)", str(i)))]
    return (max(nums) + 1) if nums else 1


def _merge_paper_lines(old_rendered: list[str], new_keys: list[str]) -> list[str]:
    return list(old_rendered) + [k for k in new_keys if k not in old_rendered]


# --------------------------------------------------------------------------- #
# introduction
# --------------------------------------------------------------------------- #

def plan_introduction(objs: dict, doc: dict, scan, alias) -> list[str]:
    notes: list[str] = []
    evidence = objs["evidence"].get("evidence") or {}
    for module, entries in evidence.items():
        if not isinstance(entries, dict):
            continue
        for entry, ed in entries.items():
            if not isinstance(ed, dict):
                continue
            rels = rv._intro_files_for_entry(scan, module, entry)
            blocks = [b for rel in rels for b in scan.files[rel]["blocks"]]
            wb_keys = {ck for b in blocks for ck, _ in b.wb}
            old_rendered = [str(p) for p in (ed.get("papers") or [])]
            old_keys = {rv.strip_journal(p) for p in old_rendered}
            new_keys = [t for ck in sorted(wb_keys)
                        if (t := alias.resolve(ck) or ck) not in old_keys]
            if new_keys:
                ed["papers"] = _merge_paper_lines(old_rendered, new_keys)
                gaps = _block_gaps(blocks)
                gd0 = ed.get("gap_distribution") or {}
                for k in new_keys:
                    g = gaps.get(k, "Incompleteness")
                    gd0[g] = gd0.get(g, 0) + 1
                notes.append(f"evidence.{module}.{entry}: papers +{new_keys}")
            # intra-entry consistency: sum(gap_distribution) == paper_count
            # (historical drift absorbed into the residual bucket, always)
            if ed.get("gap_distribution") is not None and \
               ed.get("paper_count") is not None:
                gd = ed["gap_distribution"]
                diff = ed["paper_count"] - sum(gd.values())
                if diff:
                    gd["Incompleteness"] = gd.get("Incompleteness", 0) + diff
                    notes.append(f"evidence.{module}.{entry}: gap_distribution "
                                 f"absorbed {diff:+d} into Incompleteness")
            # status derivation (C item S3b): overrides ⊕ policy ⊕ ladder off
            # the merged papers list — ends the intro passthrough island so
            # verify covers intro status drift. Frozen blocks untouched: n
            # comes from the registry papers list, not a block scan.
            if "status" in ed:
                keys = [rv.strip_journal(str(p)) for p in (ed.get("papers") or [])]
                new_status = _status_for(doc, f"evidence.{module}.{entry}",
                                         len(keys), current=ed.get("status"),
                                         paper_keys=keys)
                if rv.norm_status(str(ed.get("status"))) != \
                        rv.norm_status(new_status):
                    ed["status"] = new_status
                    notes.append(f"evidence.{module}.{entry}: "
                                 f"status ~{new_status}")
    paper_index = objs["paper_index"].get("paper_index") or {}
    attested: dict[str, str] = {}
    for b in scan.all_blocks():
        for ck, _ in b.wb:
            t = alias.resolve(ck) or ck
            attested.setdefault(t, (b.wb_meta or {}).get("gap") or "Incompleteness")
    added = sorted(k for k in attested if k not in paper_index)
    for k in added:
        paper_index[k] = attested[k]
    if added:
        notes.append(f"paper_index +{added}")
    return notes


# --------------------------------------------------------------------------- #
# theory
# --------------------------------------------------------------------------- #

def _theory_frag_by_paper(scan, alias) -> dict[str, list[dict]]:
    frag_by_paper: dict[str, list[dict]] = {}
    for b in scan.all_blocks():
        papers = rv.theory_block_papers(b, alias)
        pid = (b.fm or {}).get("pattern_id") or (b.wb[0][1] if b.wb else None)
        if not papers or not pid:
            continue
        for p in papers:
            frag_by_paper.setdefault(p, []).append({
                "type": pid, "title": b.heading, "home_files": [b.rel],
                "status": (b.wb_meta or {}).get("status")
                or rv.norm_status((b.fm or {}).get("status_token") or b.status),
                "dim": (b.wb_meta or {}).get("dim") or ""})
    return frag_by_paper


def plan_theory(objs: dict, doc: dict, scan, alias) -> list[str]:
    notes: list[str] = []
    meta = objs["meta"].get("meta") or {}
    source_papers = objs["source_papers"].get("source_papers") or {}
    # first-time bootstrap: a null/empty `patterns` root is falsy, so `or {}`
    # would detach the mapping and silently drop every entry plan_theory adds.
    # Attach the fresh dict back so the rendered segment keeps it (2026-09-23,
    # liuliuluo2016 run: 235 created patterns lost per apply → never converged).
    patterns = objs["patterns"].get("patterns")
    if not isinstance(patterns, dict):
        patterns = {}
        objs["patterns"]["patterns"] = patterns
    sbd = objs["summary_by_dimension"].get("summary_by_dimension") or {}
    frag_by_paper = _theory_frag_by_paper(scan, alias)
    all_ids = [f.get("fragment_id")
               for p in source_papers.values() if isinstance(p, dict)
               for f in (p.get("fragments") or []) if isinstance(f, dict)]
    next_tfr = _tfr_next(all_ids)
    # ---- fragments: merge derived into each paper's list ----
    for paper, pentry in source_papers.items():
        if not isinstance(pentry, dict):
            continue
        frags = [f for f in (pentry.get("fragments") or []) if isinstance(f, dict)]
        by_type: dict[str, list[dict]] = {}
        for f in frags:
            by_type.setdefault(str(f.get("type", "")).lower(), []).append(f)
        used: set[int] = set()
        for df in frag_by_paper.get(paper, []):
            cands = [f for f in by_type.get(str(df["type"]).lower(), [])
                     if id(f) not in used]
            homes_d = {df["home_files"][0].replace("\\", "/")}
            hit = next((f for f in cands
                        if homes_d & {str(h).replace("\\", "/")
                                      for h in rv.flowlist(f.get("home_files"))}),
                       None)
            if hit is None:
                pentry.setdefault("fragments", []).append({
                    "fragment_id": f"tfr_{next_tfr}", "type": df["type"],
                    "title": df["title"], "home_files": df["home_files"],
                    "makadok_dimension": df["dim"],
                    "status": _status_for(doc, f"source_papers.{paper}", 1,
                                          paper_keys=[paper],
                                          auxiliary=rv.source_is_auxiliary(
                                              doc, paper)),
                    "note": ""})
                notes.append(f"source_papers.{paper}: fragment +{df['type']} "
                             f"(minted tfr_{next_tfr})")
                next_tfr += 1
                continue
            used.add(id(hit))
            changed = []
            if str(hit.get("type", "")) != df["type"]:
                hit["type"] = df["type"]; changed.append("type")
            # status: never-downgrade max over three signals — on-disk row,
            # block 验证状态 surface (user rulings, e.g. 2026-09-06d sweeps),
            # and the status policy (C item: author/domain rules surface the
            # batch-flip-era debt mechanically). A block promoted above its
            # registry row means the row missed a ruling sweep; a policy hit
            # above both means the ruling was never swept here at all.
            st_r = rv.norm_status(str(hit.get("status") or ""))
            st_d = rv.norm_status(str(df.get("status") or ""))
            st_p, _prule = rv.policy_status(
                [paper], 1, rv.cached_policy(),
                auxiliary=rv.source_is_auxiliary(doc, paper))
            cand = [s for s in (st_r, st_d, st_p or "")
                    if s in rv.LADDER]
            st_new = max(cand, key=rv.LADDER.index) if cand else st_r
            if st_new != st_r:
                hit["status"] = st_new; changed.append("status")
            # title: carry-if-present. On-disk titles are curated summaries
            # written at distill time; the block heading is a cruder proxy.
            # Overwriting ~130 curated titles would destroy curation, so the
            # derive side only mints titles for NEW fragments.
            hf_old = {str(h).replace("\\", "/")
                      for h in rv.flowlist(hit.get("home_files"))}
            if not homes_d <= hf_old:
                hit["home_files"] = sorted(hf_old | homes_d)
                changed.append("home_files")
            if changed:
                notes.append(f"source_papers.{paper}.{hit.get('fragment_id')}: "
                             f"~{changed}")
    for paper in sorted(set(frag_by_paper) - set(source_papers)):
        source_papers[paper] = {
            "display_name": re.sub(r"[_]+", " ", paper).strip(),
            "journal": "", "year": None,
            "fragments": [
                {"fragment_id": f"tfr_{next_tfr + i}", "type": df["type"],
                 "title": df["title"], "home_files": df["home_files"],
                 "makadok_dimension": df["dim"],
                 "status": _status_for(doc, f"source_papers.{paper}", 1,
                                       paper_keys=[paper],
                                       auxiliary=rv.source_is_auxiliary(
                                           doc, paper)),
                 "note": ""}
                for i, df in enumerate(frag_by_paper[paper])]}
        next_tfr += len(frag_by_paper[paper])
        notes.append(f"source_papers +{paper} (minted; journal/year need "
                     f"human completion)")
    # full-coverage status synthesis (C item): the block-driven merge above
    # only visits fragments matched by block attestation — fragments of
    # unattested papers, and unmatched fragments of attested papers, would
    # silently never receive policy flips. Status depends only on the
    # registry paper key, so synthesize for EVERY fragment row; idempotent
    # max with the merge-loop signal, never-downgrade preserved.
    for paper, pentry in source_papers.items():
        if not isinstance(pentry, dict):
            continue
        st_p, _ = rv.policy_status([paper], 1, rv.cached_policy(),
                                   auxiliary=rv.source_is_auxiliary(doc, paper))
        if not st_p:
            continue
        for f in pentry.get("fragments") or []:
            if not isinstance(f, dict):
                continue
            st_r = rv.norm_status(str(f.get("status") or ""))
            if st_r in rv.LADDER and rv.LADDER.index(st_r) >= rv.LADDER.index(st_p):
                continue
            f["status"] = st_p
            notes.append(f"source_papers.{paper}.{f.get('fragment_id')}: "
                         f"~['status'] (policy)")
    if "total_papers_indexed" in meta:
        meta["total_papers_indexed"] = len(source_papers)
    # ---- patterns ----
    # attestation mirrors the checker: fm pattern_id first, wb item fallback
    blocks_by_pattern: dict[str, list] = {}
    for b in scan.all_blocks():
        pid = (b.fm or {}).get("pattern_id") or (b.wb[0][1] if b.wb else None)
        if pid:
            blocks_by_pattern.setdefault(pid, []).append(b)
    for pid in sorted(set(blocks_by_pattern) - set(patterns)):
        grp = blocks_by_pattern[pid]
        papers = sorted({p for b in grp
                         for p in rv.theory_block_papers(b, alias)})
        patterns[pid] = {
            "description": "",
            "status": _status_for(doc, f"patterns.{pid}", len(papers),
                                  paper_keys=list(papers),
                                  auxiliary=any(rv.source_is_auxiliary(doc, p)
                                                for p in papers)),
            "source_count": len(papers),
            "source_papers": papers,
            "home_file": sorted({b.rel for b in grp})}
        notes.append(f"patterns +{pid} (new; description needs human completion)")
    for pid, pent in patterns.items():
        if not isinstance(pent, dict):
            continue
        grp = blocks_by_pattern.get(pid) or []
        if not grp:
            continue
        # mirrors the checker's derivation exactly (theory_block_papers only)
        papers = {p for b in grp for p in rv.theory_block_papers(b, alias)}
        old_sp = [rv.strip_journal(x) for x in rv.flowlist(pent.get("source_papers"))]
        merged = list(dict.fromkeys(old_sp + sorted(papers - set(old_sp))))
        hf_old = rv.flowlist(pent.get("home_file"))
        hf_new = sorted(set(hf_old) | {b.rel for b in grp})
        new_status = _status_for(doc, f"patterns.{pid}", len(merged),
                                 current=pent.get("status"),
                                 paper_keys=merged,
                                 auxiliary=any(rv.source_is_auxiliary(doc, p)
                                               for p in merged))
        changed = []
        if merged != old_sp:
            pent["source_papers"] = merged; changed.append("source_papers")
        if pent.get("source_count") != len(merged):
            pent["source_count"] = len(merged); changed.append("source_count")
        if hf_new != hf_old:
            pent["home_file"] = hf_new[0] if len(hf_new) == 1 else hf_new
            changed.append("home_file")
        if rv.norm_status(str(pent.get("status") or "")) != rv.norm_status(new_status):
            pent["status"] = new_status; changed.append("status")
        if changed:
            notes.append(f"patterns.{pid}: ~{changed}")
    # full-coverage pattern status synthesis (C item): the merge loop skips
    # patterns without attesting blocks (`if not grp`), so policy flips would
    # silently never land there. Never-downgrade preserved.
    for pid, pent in patterns.items():
        if not isinstance(pent, dict) or blocks_by_pattern.get(pid):
            continue
        pkeys = [rv.strip_journal(str(p))
                 for p in rv.flowlist(pent.get("source_papers"))]
        st_p, _ = rv.policy_status(
            pkeys, max(len(pkeys), int(pent.get("source_count") or 0)),
            rv.cached_policy(),
            auxiliary=any(rv.source_is_auxiliary(doc, k) for k in pkeys))
        if not st_p:
            continue
        st_r = rv.norm_status(str(pent.get("status") or ""))
        if st_r in rv.LADDER and rv.LADDER.index(st_r) >= rv.LADDER.index(st_p):
            continue
        pent["status"] = st_p
        notes.append(f"patterns.{pid}: ~['status'] (policy)")
    # ---- summary_by_dimension: re-aggregate from merged fragments ----
    agg: dict[str, dict] = {}
    for paper, pentry in source_papers.items():
        if not isinstance(pentry, dict):
            continue
        for f in (pentry.get("fragments") or []):
            if not isinstance(f, dict) or not f.get("makadok_dimension"):
                continue
            a = agg.setdefault(str(f["makadok_dimension"]),
                               {"frags": 0, "papers": set(), "verified": set()})
            a["frags"] += 1
            a["papers"].add(paper)
            if rv.norm_status(f.get("status")) in ("VERIFIED", "ROBUST"):
                a["verified"].add(str(f.get("type", "")).lower())
    for dim in sorted(set(agg) - set(sbd)):
        sbd[dim] = {"total_fragments": agg[dim]["frags"],
                    "source_papers": len(agg[dim]["papers"])}
        notes.append(f"summary_by_dimension +{dim}")
    for dim, dent in sbd.items():
        if not isinstance(dent, dict):
            continue
        a = agg.get(dim)
        if a is None:
            continue
        changed = []
        if dent.get("total_fragments") != a["frags"]:
            dent["total_fragments"] = a["frags"]; changed.append("total_fragments")
        if dent.get("source_papers") != len(a["papers"]):
            dent["source_papers"] = len(a["papers"]); changed.append("source_papers")
        if dent.get("verified_patterns") is not None and \
           dent["verified_patterns"] != len(a["verified"]):
            dent["verified_patterns"] = len(a["verified"])
            changed.append("verified_patterns")
        if changed:
            notes.append(f"summary_by_dimension.{dim}: ~{changed}")
    return notes


# --------------------------------------------------------------------------- #
# methods
# --------------------------------------------------------------------------- #

def plan_methods(objs: dict, doc: dict, scan, alias) -> list[str]:
    notes: list[str] = []
    meta = objs["meta"].get("meta") or {}
    evidence = objs["evidence"].get("evidence") or {}
    bdt = evidence.get("by_design_type") or {}
    paper_to_files: dict[str, set] = {}
    for key, dent in bdt.items():
        if not isinstance(dent, dict):
            continue
        rels = rv._file_for_stem(scan, key)
        if not rels:
            continue
        blocks = [b for rel in rels for b in scan.files[rel]["blocks"]]
        wb_keys = {ck for b in blocks for ck, _ in b.wb}
        old_rendered = [str(p) for p in (dent.get("papers") or [])]
        old_keys = {rv.strip_journal(p) for p in old_rendered}
        new_keys = []
        for ck in sorted(wb_keys):
            tgt = alias.resolve(ck) or ck
            if tgt not in old_keys and tgt not in new_keys:
                new_keys.append(tgt)
            for p in {ck, alias.resolve(ck)} - {None}:
                paper_to_files.setdefault(p, set()).update(rels)
        if new_keys:
            dent["papers"] = _merge_paper_lines(old_rendered, new_keys)
            notes.append(f"by_design_type.{key}: papers +{new_keys}")
        if dent.get("paper_count") is not None and dent.get("papers") is not None:
            dent["paper_count"] = len(dent["papers"])
        # status derivation (C item S3b): overrides ⊕ policy ⊕ ladder; the
        # passthrough era ended — verify now covers methods status drift.
        if "status" in dent:
            keys = [rv.strip_journal(str(p)) for p in (dent.get("papers") or [])]
            new_status = _status_for(doc, f"evidence.by_design_type.{key}",
                                     len(keys), current=dent.get("status"),
                                     paper_keys=keys)
            if rv.norm_status(str(dent.get("status"))) != \
                    rv.norm_status(new_status):
                dent["status"] = new_status
                notes.append(f"by_design_type.{key}: status ~{new_status}")
        if "slots_covered" in dent:
            block_slots = {s for b in blocks for s in b.slots}
            old_slots = rv.flowlist(dent.get("slots_covered"))
            merged = list(dict.fromkeys(old_slots + sorted(block_slots)))
            if merged != old_slots:
                dent["slots_covered"] = merged
                notes.append(f"by_design_type.{key}: slots_covered ~{merged}")
    for paper, pent in (evidence.get("by_source_paper") or {}).items():
        if not isinstance(pent, dict):
            continue
        rev = alias.resolve(paper)
        files = set(paper_to_files.get(paper, set()))
        if rev:
            files |= set(paper_to_files.get(rev, set()))
        derived_dt = sorted(Path(r).stem for r in files)
        disk_dt = [Path(str(x)).stem.replace("_", "-").replace(".md", "")
                   for x in rv.flowlist(pent.get("design_types"))]
        extra = [d for d in derived_dt
                 if d.replace("_", "-") not in {x.replace("_", "-") for x in disk_dt}]
        if extra:
            pent["design_types"] = disk_dt + extra
            notes.append(f"by_source_paper.{paper}: design_types +{extra}")
        if "status" in pent:
            new_status = _status_for(doc, f"evidence.by_source_paper.{paper}",
                                     1, current=pent.get("status"),
                                     paper_keys=[paper])
            if rv.norm_status(str(pent.get("status"))) != \
                    rv.norm_status(new_status):
                pent["status"] = new_status
                notes.append(f"by_source_paper.{paper}: status ~{new_status}")
    if "total_design_types" in meta:
        meta["total_design_types"] = len(bdt)
    return notes


# --------------------------------------------------------------------------- #
# results
# --------------------------------------------------------------------------- #

def _block_skeleton(scan, rel: str, start: int, end: int, cache: dict) -> str:
    import corpus_writeback as cw
    if rel not in cache:
        cache[rel] = scan.file_text(rel).split("\n")
    body = "\n".join(cache[rel][start:end])
    folded = cw._block_field(body, "骨架")
    return " ".join(re.sub(r"^\s*>\s?", "", ln).strip().strip('"').strip()
                    for ln in folded).strip()


def plan_results(objs: dict, doc: dict, scan, alias) -> list[str]:
    notes: list[str] = []
    meta = objs["meta"].get("meta") or {}
    estimators = objs["estimators"].get("estimators") or {}
    texts: dict[str, list[str]] = {}

    derived: dict[tuple, dict] = {}
    for b, ck, item in scan.markers():
        m = re.match(r"^r(\d+)_", item)
        if not m:
            continue
        est_key = Path(b.rel).stem.replace("-", "_")
        derived.setdefault((est_key, f"R{m.group(1)}"), {})[item] = {
            "sources": [ck], "corpus_path": f"corpus/{b.rel}", "block": b}
    for ekey, eentry in estimators.items():
        if not isinstance(eentry, dict):
            continue
        slots = eentry.setdefault("slots", {})
        for (dk, dsk) in derived:
            if dk == ekey and dsk not in slots:
                slots[dsk] = {"skeleton_variants": []}
                notes.append(f"estimators.{ekey}.slots +{dsk}")
        for skey, sent in slots.items():
            if not isinstance(sent, dict):
                continue
            dvars = derived.get((ekey, skey)) or {}
            svs = sent.setdefault("skeleton_variants", [])
            disk_by_id = {}
            for v in svs:
                if isinstance(v, dict):
                    vid = str(v.get("id") or "").replace("-", "_")
                    if vid:
                        disk_by_id[vid] = v
            for vid, dv in dvars.items():
                res = alias.resolve(dv["sources"][0]) or dv["sources"][0]
                sk = _block_skeleton(scan, dv["block"].rel, dv["block"].start,
                                     dv["block"].end, texts)
                if vid not in disk_by_id:
                    new_v = {"id": vid, "corpus_path": dv["corpus_path"],
                             "sources": [res], "paper_count": 1,
                             "status": _status_for(
                                 doc, f"estimators.{ekey}.slots.{skey}"
                                      f".skeleton_variants.{vid}", 1,
                                 paper_keys=[res])}
                    if sk:
                        new_v["skeleton"] = sk
                    svs.append(new_v)
                    notes.append(f"estimators.{ekey}.{skey}.{vid}: +new variant")
                    continue
                v = disk_by_id[vid]
                old_src = [alias.resolve(rv.strip_journal(s))
                           or rv.strip_journal(s)
                           for s in rv.flowlist(v.get("sources"))]
                merged = (list(dict.fromkeys(old_src + [res]))
                          if res not in old_src else old_src)
                changed = []
                if merged != old_src:
                    v["sources"] = merged; changed.append("sources")
                if v.get("paper_count") is not None and \
                   v["paper_count"] != len(v["sources"]):
                    v["paper_count"] = len(v["sources"])
                    changed.append("paper_count")
                if v.get("corpus_path") is not None and \
                   str(v["corpus_path"]).replace("\\", "/") != dv["corpus_path"]:
                    v["corpus_path"] = dv["corpus_path"]
                    changed.append("corpus_path")
                if v.get("skeleton") is not None and sk and \
                   re.sub(r"\s+", "", str(v["skeleton"])) != \
                   re.sub(r"\s+", "", sk):
                    v["skeleton"] = sk; changed.append("skeleton")
                # status: variant-level override path (the 196 partition-
                # collected keys are variant-level; the pre-S3a estimator-
                # level path never consumed them). A missing status (executor
                # stub limbo) is filled here — same _status_for gate, never-
                # downgrade preserved.
                vpath = (f"estimators.{ekey}.slots.{skey}"
                         f".skeleton_variants.{vid}")
                st = _status_for(doc, vpath, len(v["sources"]),
                                 current=v.get("status"),
                                 paper_keys=v["sources"])
                if rv.norm_status(str(v.get("status"))) != rv.norm_status(st):
                    v["status"] = st; changed.append("status")
                if changed:
                    notes.append(f"estimators.{ekey}.{skey}.{vid}: ~{changed}")
    # full-coverage status synthesis (C item): variants whose blocks are not
    # attested in this scan are invisible to the block-driven loop above —
    # policy flips and the statusless fill must reach them too. Idempotent
    # with the in-loop synthesis (same _status_for, never-downgrade).
    for ek, ee in estimators.items():
        if not isinstance(ee, dict):
            continue
        for sk, sl in (ee.get("slots") or {}).items():
            if not isinstance(sl, dict):
                continue
            for v in sl.get("skeleton_variants") or []:
                if not isinstance(v, dict) or not v.get("id"):
                    continue
                vpath = (f"estimators.{ek}.slots.{sk}"
                         f".skeleton_variants.{v['id']}")
                keys = [rv.strip_journal(str(s))
                        for s in rv.flowlist(v.get("sources"))]
                st = _status_for(doc, vpath,
                                 max(len(keys), int(v.get("paper_count") or 0)),
                                 current=v.get("status"), paper_keys=keys)
                if rv.norm_status(str(v.get("status"))) != rv.norm_status(st):
                    v["status"] = st
                    notes.append(f"estimators.{ek}.{sk}.{v['id']}: "
                                 f"~['status'] (policy/fill)")
    if "batches_processed" in meta:
        bh = doc.get("batch_history")
        if isinstance(bh, list):
            meta["batches_processed"] = len(bh)
        # last_batch_id is carried from the append-only ledger tail (the
        # executor no longer writes meta counters; S6 plan §7.4)
        if "last_batch_id" in meta and isinstance(bh, list) and bh:
            tail = bh[-1]
            if isinstance(tail, dict) and tail.get("batch_id"):
                meta["last_batch_id"] = str(tail["batch_id"])
    if "total_papers_indexed" in meta:
        srcs = set()
        for eentry in estimators.values():
            for sent in (eentry.get("slots") or {}).values():
                for v in (sent.get("skeleton_variants") or []):
                    if isinstance(v, dict):
                        srcs.update(rv.strip_journal(s)
                                    for s in rv.flowlist(v.get("sources")))
        meta["total_papers_indexed"] = len(srcs)
    return notes


PLANNERS = {
    "introduction": plan_introduction,
    "theory": plan_theory,
    "methods": plan_methods,
    "results": plan_results,
}


# --------------------------------------------------------------------------- #
# orchestration
# --------------------------------------------------------------------------- #

def apply_corpus(corpus: str, dry_run: bool = True,
                 registry_path: str | None = None,
                 corpus_root: str | None = None) -> list[str]:
    _ATTRIBUTION.clear()        # S5: per-corpus status decision attribution
    reg = Path(registry_path) if registry_path else rv.registry_for(corpus)
    if not reg.is_file():
        raise RuntimeError(f"{corpus}: registry missing: {reg}")
    raw = reg.read_bytes().decode("utf-8")
    doc = yaml.safe_load(raw.replace("\r\n", "\n"))
    root = Path(corpus_root) if corpus_root else rv.SKILLS_ROOT / rv.CORPUS_KEYS[corpus]
    scan = rv.scan_corpus(root)
    prim, sec = rv.alias_universe(corpus, doc, scan)
    alias = rv.AliasIndex(prim, sec)
    segs = rv.split_partitions(raw)
    der_segs = [(i, t) for i, (k, t) in enumerate(segs) if k == "derived"]
    keys = SEGMENT_KEYS[corpus]
    # parse each derived segment; consecutive derived roots share one marker,
    # so a segment may hold several of the layout's roots (order = SEGMENT_KEYS)
    objs: dict[str, dict] = {}
    seg_roots: list[tuple[int, list[str]]] = []
    for i, (idx, t) in enumerate(der_segs):
        obj = yaml.safe_load(t.replace("\r\n", "\n")) or {}
        roots = [k for k in keys if k in obj]
        unknown = [k for k in obj if k not in keys]
        if unknown:
            raise RuntimeError(f"{corpus}: derived segment #{i} has unexpected "
                               f"root(s) {unknown} (expected subset of {keys})")
        if not roots:
            raise RuntimeError(f"{corpus}: derived segment #{i} matches none "
                               f"of {keys} (has {list(obj)[:6]})")
        for k in roots:
            if k in objs:
                raise RuntimeError(f"{corpus}: root {k} appears in two segments")
            objs[k] = obj
        seg_roots.append((idx, obj))
    missing = [k for k in keys if k not in objs]
    if missing:
        raise RuntimeError(f"{corpus}: layout roots absent from file: {missing}")
    notes = PLANNERS[corpus](objs, doc, scan, alias)
    # render back per segment; keep original bytes when nothing value-changed
    new_texts: dict[int, str] = {}
    for idx, obj in seg_roots:
        rendered = render_root(obj)
        reparsed = yaml.safe_load(rendered)
        if reparsed != obj:
            raise RuntimeError(f"{corpus}: render round-trip mismatch")
        old_parsed = yaml.safe_load(segs[idx][1].replace("\r\n", "\n")) or {}
        changed = diff_paths(old_parsed, reparsed)
        if not changed:
            continue  # values identical — never restyle untouched segments
        new_texts[idx] = rendered
    if dry_run:
        print(f"[{corpus}] DRY-RUN — {len(notes)} planned change(s):")
        for n in notes:
            print(f"  - {n}")
        return notes
    ordered = [new_texts.get(i, t) for i, (k, t) in enumerate(segs)
               if k == "derived"]
    assembled = rv.rebuild_registry_text(raw, ordered)
    # guards before write
    yaml.safe_load(assembled.replace("\r\n", "\n"))
    new_segs = rv.split_partitions(assembled)
    assert len(new_segs) == len(segs), "segment count changed"
    for (kind, t_old), (kind2, t_new) in zip(segs, new_segs):
        if kind == "authored":
            assert t_old == t_new, "AUTHORED segment mutated"
    if assembled.count("\r\n") != assembled.count("\n"):
        raise RuntimeError("mixed EOL after rebuild")
    reg.write_bytes(assembled.encode("utf-8"))
    print(f"[{corpus}] APPLIED — {len(notes)} change(s); AUTHORED segments "
          f"byte-identical")
    for n in notes:
        print(f"  - {n}")
    return notes


def attribution_line() -> str:
    """S5: one-line status decision attribution (override / policy / ladder /
    never-demote counts from the last apply_corpus planning pass)."""
    parts = [f"{k} {_ATTRIBUTION.get(k, 0)}"
             for k in ("override", "policy", "ladder", "never-demote")]
    return "STATUS ATTRIBUTION: " + " / ".join(parts)


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", choices=list(SEGMENT_KEYS), default="all")
    ap.add_argument("--apply", action="store_true",
                    help="write files (default: dry-run)")
    ap.add_argument("--registry", default=None,
                    help="override registry path (sandbox / non-default layouts)")
    ap.add_argument("--corpus-root", default=None,
                    help="override corpus root scanned for wb blocks")
    args = ap.parse_args()
    corpora = list(SEGMENT_KEYS) if args.corpus == "all" else [args.corpus]
    total = 0
    attr_total: dict[str, int] = {}
    for ck in corpora:
        total += len(apply_corpus(ck, dry_run=not args.apply,
                                  registry_path=args.registry,
                                  corpus_root=args.corpus_root))
        for k, v in _ATTRIBUTION.items():
            attr_total[k] = attr_total.get(k, 0) + v
    print(f"\n{'APPLIED' if args.apply else 'DRY-RUN'}: {total} change(s) across "
          f"{len(corpora)} corpus/corpora")
    print("STATUS ATTRIBUTION: "
          + " / ".join(f"{k} {attr_total.get(k, 0)}"
                       for k in ("override", "policy", "ladder", "never-demote")))
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
