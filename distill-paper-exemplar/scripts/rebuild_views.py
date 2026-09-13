#!/usr/bin/env python3
"""Derived-view rebuilder for the four write-* evidence registries (S1 skeleton).

Blocks are the truth: every `<!-- wb:<citekey>:<item> -->` marker joins a corpus
block to its registry footprint. This tool SCANS the corpus blocks, re-derives
the DERIVED sections of each `_evidence_registry.yaml` in memory, and — in
--check mode — diffs them against the on-disk registry, writing a
reconciliation_report.yaml that classifies every check as:

  match           derived value equals on-disk value
  drift           both sides available and different — a rebuild would change it
  unattributable  the on-disk value cannot be re-derived from blocks (legacy
                  blocks without wb markers, AUTHORED fields, audit counters)

plus an adjudication (`裁决单`) grouping every non-match into classes:
  expected_legacy_gap          pre-marker legacy blocks (intro: frozen by design)
  expected_dual_key            short-key registry keys vs full wb citekeys
  expected_counter_drift       audit counters documented as drifted in the plan
  expected_authored_passthrough  AUTHORED fields the scan must not own
  expected_status_override     user-designated status that beats the ladder
  expected_stale_block_status  block frontmatter status older than registry
  novel                        needs human adjudication (real drift candidate)

S1 is PURE READ-ONLY: --check never writes registries. --apply exists as the
S6 switch but refuses to run until S2 partition markers
(`# === DERIVED: ... ===` / `# === AUTHORED ===`) are present in the registry.

Usage:
  python rebuild_views.py --check [--corpus all|introduction|theory|methods|results]
      [--out reconciliation_report.yaml] [--quiet]
  python rebuild_views.py --apply ...     # S6; guarded, refuses pre-S2
  python rebuild_views.py --self-test     # built-in unit tests
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus_writeback as cw  # noqa: E402  (CORPUS_ROOTS/SKILLS_ROOT,
#                               REGISTRY_ALIASES, LABEL_FAMILIES, GOOD_ANCHOR,
#                               BAD_ANCHOR, _block_field — single source)

SKILLS_ROOT = cw.SKILLS_ROOT
MISSING = object()  # sentinel: value not present on that side

DERIVED_MARKER = "# === DERIVED: rebuilt by rebuild_views.py — do not hand-edit ==="
AUTHORED_MARKER = "# === AUTHORED ==="

CORPUS_KEYS = {
    "introduction": "write-introduction/corpus",
    "theory": "write-theory/corpus",
    "methods": "write-methods/corpus",
    "results": "write-results/corpus",
}

WB_RE = re.compile(r"<!--\s*wb:([^:>]+):([^>]+?)\s*-->")
# S4 wb-meta format (finalized in S2): one line, separate from the wb marker,
# compact space-separated KV, values optionally double-quoted, grep-able:
#   <!-- wb-meta: dim=Boundary status=EMERGING gap=Incompleteness tbt="机制推演型" -->
WB_META_RE = re.compile(r"<!--\s*wb-meta:\s*(.+?)\s*-->")
WB_META_KV_RE = re.compile(r'(\w+)=("([^"]*)"|\S+)')
HEAD_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")
FM_COMMENT_RE = re.compile(r"<!--\s*\n(.*?)\n\s*-->", re.S)
SLOT_LINE_RE = re.compile(r"\*\*槽位\**\s*[:：]\s*(.+)$", re.M)
STATUS_LINE_RE = re.compile(r"^\*\*验证状态\**\s*[:：]\s*(\S+)", re.M)
HEADER_YAML_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
YEAR_IN_TOKEN_RE = re.compile(r"(?<!\d)(\d{4})(?!\d)")

# verify_writeback's stopword list, reused for alias tokenization
STOPWORDS = {
    "smj", "amj", "asq", "os", "orsc", "jm", "msom", "poms", "jom", "jcr", "jams",
    "jme", "et", "al", "how", "does", "do", "the", "a", "an", "of", "and", "in",
    "to", "for", "on", "at", "by", "with", "from", "across", "multiple", "new",
    "what", "why", "when", "which", "their", "its", "evidence", "study", "case",
    "firm", "firms", "paper", "value", "market", "effect", "effects", "impact",
}

LADDER = ["EMERGING", "VERIFIED", "ROBUST"]


# --------------------------------------------------------------------------- #
# block scanning
# --------------------------------------------------------------------------- #

@dataclass
class Block:
    rel: str                      # posix rel path from corpus root
    heading: str
    level: str                    # '##' / '###' / '####'
    start: int
    end: int                      # exclusive line index (next heading or EOF)
    wb: list = field(default_factory=list)      # [(citekey, item)]
    fm: dict | None = None        # theory HTML-comment frontmatter fields
    slots: set = field(default_factory=set)     # {'M2','R4'}
    status: str | None = None     # from **验证状态** line or fm.status
    wb_meta: dict = field(default_factory=dict)  # S4 wb-meta KV payload

    def full_heading(self) -> str:
        return f"{self.level} {self.heading}"


@dataclass
class CorpusScan:
    root: Path
    files: dict                   # rel -> {header_yaml, blocks}
    n_markers: int = 0

    def all_blocks(self):
        for rel in sorted(self.files):
            yield from self.files[rel]["blocks"]

    def markers(self):
        for b in self.all_blocks():
            for citekey, item in b.wb:
                yield b, citekey, item

    def file_text(self, rel: str) -> str:
        return (self.root / rel).read_text(encoding="utf-8")


def _parse_fm_comment(raw: str) -> dict | None:
    """Parse a theory HTML-comment frontmatter (pattern_id/build_type/
    source_papers/confidence/status...). None when it lacks the signature
    pattern_id key (plain comments and wb markers never qualify)."""
    out = {}
    for ln in raw.split("\n"):
        if ":" not in ln:
            continue
        k, v = ln.split(":", 1)
        out[k.strip()] = v.strip()
    if "pattern_id" not in out:
        return None
    sp = out.get("source_papers", "")
    if sp:
        try:
            v = yaml.safe_load(sp)
            out["source_papers"] = [str(x) for x in v] if isinstance(v, list) else [str(v)]
        except yaml.YAMLError:
            out["source_papers"] = [s for s in re.findall(r"[A-Za-z_][\w\-]*", sp)]
    else:
        out["source_papers"] = []
    st = out.get("status", "")
    out["status_token"] = st.split()[0] if st.split() else None
    return out


def parse_wb_meta(raw: str) -> dict:
    """Parse one wb-meta comment line into a compact KV dict (S4 payload:
    tfr makadok_dimension/note and gap attribution move into blocks)."""
    out = {}
    for m in WB_META_KV_RE.finditer(raw):
        out[m.group(1)] = m.group(3) if m.group(3) is not None else m.group(2)
    return out


def _slot_tags_from_item(item: str) -> set:
    if re.match(r"^m(\d+)_", item):
        return {f"M{re.match(r'm(\d+)_', item).group(1)}"}
    if re.match(r"^r(\d+)_", item):
        return {f"R{re.match(r'r(\d+)_', item).group(1)}"}
    return set()


def scan_corpus(root: Path) -> CorpusScan:
    scan = CorpusScan(root=root, files={})
    for p in sorted(root.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        lines = text.split("\n")
        rel = p.relative_to(root).as_posix()
        header = None
        hm = HEADER_YAML_RE.match(text)
        if hm:
            try:
                header = yaml.safe_load(hm.group(1)) or {}
            except yaml.YAMLError:
                header = None
        heads = [(i, m) for i, ln in enumerate(lines) if (m := HEAD_RE.match(ln))]
        blocks = []
        wb_starts: dict[int, list[int]] = {}
        for k, (i, m) in enumerate(heads):
            end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
            blocks.append(Block(rel=rel, heading=m.group(2), level=m.group(1),
                                start=i, end=end))
        for b in blocks:
            body = "\n".join(lines[b.start:b.end])
            for wm in WB_RE.finditer(body):
                b.wb.append((wm.group(1).strip(), wm.group(2).strip()))
                wb_starts.setdefault(id(b), []).append(
                    b.start + body[:wm.start()].count("\n"))
            for sm in SLOT_LINE_RE.finditer(body):
                # recorded for provenance info; slot DERIVATION uses wb item
                # prefixes only (that is what the executor merges into the
                # registry — the **槽位** line is block-internal prose)
                b.slots |= set()
            st = STATUS_LINE_RE.search(body)
            if st:
                b.status = st.group(1)
            for wm in WB_META_RE.finditer(body):
                b.wb_meta.update(parse_wb_meta(wm.group(1)))
            for ck, item in b.wb:
                b.slots |= _slot_tags_from_item(item)

        # frontmatter attribution — three physical positions (plan §3.2):
        #   标题后 / 块尾 wb 前  -> the containing block
        #   下块标题前           -> the NEXT block, when its wb item fuzzily
        #                           matches the frontmatter pattern_id
        def block_at(idx: int) -> Block | None:
            for b in blocks:
                if b.start <= idx < b.end:
                    return b
            return blocks[0] if blocks else None  # pre-first-heading fm -> block 0

        def fuzzy_pid_item(pid: str, item: str) -> bool:
            n = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
            a, b2 = n(pid), n(item)
            if a and b2 and (a in b2 or b2 in a):
                return True
            ta = set(re.findall(r"[a-z0-9]+", pid.lower()))
            tb = set(re.findall(r"[a-z0-9]+", item.lower()))
            return bool(ta & tb) and len(ta & tb) >= max(1, min(len(ta), len(tb)) // 2)

        fm_spans = []
        for m in FM_COMMENT_RE.finditer(text):
            fm = _parse_fm_comment(m.group(1))
            if fm is None:
                continue
            fm_spans.append((text[:m.start()].count("\n"), fm, m))
        for ln, fm, m in fm_spans:
            fm_end = text[:m.end()].count("\n")
            cont = block_at(ln)
            if cont is None:
                continue
            pid = fm["pattern_id"]
            attr = None
            if any(fuzzy_pid_item(pid, item) for _ck, item in cont.wb):
                attr = cont                                    # strongest signal
            elif any(start >= ln for start in wb_starts.get(id(cont), [])):
                attr = cont                                    # 块尾 wb 前
            else:
                nxt = next((b for b in blocks if b.start > fm_end), None)
                if nxt is not None and nxt.wb and fuzzy_pid_item(pid, nxt.wb[0][1]):
                    attr = nxt                                 # 下块标题前
                else:
                    attr = cont
            attr.fm = fm
            if fm.get("status_token") and not attr.status:
                attr.status = fm["status_token"]
        scan.files[rel] = {"header_yaml": header, "blocks": blocks}
        scan.n_markers += sum(len(b.wb) for b in blocks)
    return scan


# --------------------------------------------------------------------------- #
# alias engine (short registry keys <-> full wb citekeys)
# --------------------------------------------------------------------------- #

def _tokens(key: str) -> tuple[set, set]:
    """(years, core tokens) of a citekey; years may be embedded (gulati2005)."""
    toks = [t for t in re.split(r"[^a-z0-9]+", key.lower()) if t]
    years, core = set(), set()
    for t in toks:
        for y in YEAR_IN_TOKEN_RE.findall(t):
            years.add(y)
        t2 = YEAR_IN_TOKEN_RE.sub("", t)
        if t2 and t2 not in STOPWORDS and not t2.isdigit():
            core.add(t2)
    return years, core


def alias_score(a: str, b: str) -> int | None:
    """None = incompatible (no shared year); else core-token overlap."""
    ya, _ca = _tokens(a)
    yb, _cb = _tokens(b)
    if not ya or ya != yb:
        return None
    return len(_ca & _cb)


class AliasIndex:
    """Best-match resolver between the two citekey systems. REGISTRY keys are
    the canonical side: a wb citekey resolves to its registry key, never to
    itself; a registry key resolves to itself. Ambiguous ties resolve to None
    and get reported — never guessed."""

    def __init__(self, primary: list[str], secondary: list[str] | None = None):
        self.primary = sorted(set(primary))
        self.secondary = sorted(set(secondary or []) - set(self.primary))
        self.keys = self.primary + self.secondary
        self._lower_primary = {}
        self._lower_secondary = {}
        for k in self.primary:
            self._lower_primary.setdefault(k.lower(), k)
        for k in self.secondary:
            self._lower_secondary.setdefault(k.lower(), k)
        self.resolutions: dict[str, str] = {}
        self.ambiguous: dict[str, list[str]] = {}
        self.unresolved: set[str] = set()

    def resolve(self, key: str) -> str | None:
        if key in self.resolutions:
            return self.resolutions[key]
        if key in self.ambiguous or key in self.unresolved:
            return None
        # 1. case-variant of a canonical (primary) key
        canon = self._lower_primary.get(key.lower())
        if canon is not None:
            self.resolutions[key] = canon
            return canon
        # 2. best token match within the canonical side
        best, best_s, ties = None, -1, []
        for k in self.primary:
            s = alias_score(key, k)
            if s is None:
                continue
            if s > best_s:
                best, best_s, ties = k, s, []
            elif s == best_s:
                ties.append(k)
        if best is not None and best_s > 0 and not ties:
            self.resolutions[key] = best
            return best
        if best is not None and best_s > 0 and ties:
            self.ambiguous[key] = [best] + sorted(ties)
            return None
        # 3. wb-only key: itself (no canonical counterpart exists)
        sec = self._lower_secondary.get(key.lower())
        if sec is not None:
            self.resolutions[key] = sec
            return sec
        # 4. best token match within the wb-only side
        best, best_s, ties = None, -1, []
        for k in self.secondary:
            s = alias_score(key, k)
            if s is None:
                continue
            if s > best_s:
                best, best_s, ties = k, s, []
            elif s == best_s:
                ties.append(k)
        if best is not None and best_s > 0 and not ties:
            self.resolutions[key] = best
            return best
        if best is not None and best_s > 0 and ties:
            self.ambiguous[key] = [best] + sorted(ties)
            return None
        self.unresolved.add(key)
        return None


def strip_journal(entry: str) -> str:
    """'malshe2015 (JM)' -> 'malshe2015'; plain keys pass through."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", str(entry).strip())


# --------------------------------------------------------------------------- #
# check model
# --------------------------------------------------------------------------- #

@dataclass
class Check:
    path: str
    on_disk: object = MISSING
    derived: object = MISSING
    verdict: str = "match"          # match / drift / unattributable
    cls: str | None = None
    note: str = ""


def norm_status(s) -> str:
    s = str(s or "").strip()
    return s.split()[0].upper() if s else ""


def ladder_status(n_sources: int) -> str:
    """phase-4-validation-writeback L232-238: 1-2 EMERGING / 3+ VERIFIED /
    5+ across 2 subdomains ROBUST (subdomain unknowable from a scan -> cap)."""
    return "VERIFIED" if n_sources >= 3 else "EMERGING"


def cmp_scalar(chk: Check, normalize=None) -> Check:
    a, b = chk.on_disk, chk.derived
    if normalize:
        a, b = normalize(a), normalize(b)
    if a == b:
        chk.verdict = "match"
    else:
        chk.verdict = "drift"
        chk.cls = chk.cls or "novel"
    return chk


def flowlist(v) -> list:
    """Normalize a value that may be a list, a comma string, or the legacy
    space-joined single-string form (`[M2 M7 M8]`)."""
    if v is None:
        return []
    if isinstance(v, list):
        return [str(x).strip() for x in v if str(x).strip()]
    s = str(v).strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    parts = [p.strip() for p in re.split(r"[,;]", s)] if ("," in s or ";" in s) else [s]
    return [p for p in parts if p]


def alias_failure(alias: AliasIndex, key: str) -> str | None:
    """Adjudication class when a citekey failed to resolve: None if it resolved
    fine, else the dual-key class with the ambiguity candidates in the note."""
    if key in alias.ambiguous:
        return f"ambiguous: {' | '.join(alias.ambiguous[key])}"
    if key in alias.unresolved:
        return "no year+token-compatible registry key"
    return None


def status_override_for(doc: dict, path: str) -> dict | None:
    """status_overrides lookup: the override key is the check path minus its
    trailing `.status` component (e.g. `patterns.p1` for `patterns.p1.status`)."""
    so = (doc.get("status_overrides") or {}).get("overrides") or {}
    key = path[:-len(".status")] if path.endswith(".status") else path
    ov = so.get(key)
    return ov if isinstance(ov, dict) else None


def status_cmp_check(path: str, on_disk: str, derived: str, n_sources: int,
                     doc: dict | None = None) -> Check:
    """Ladder-vs-registry status verdict with the override classes."""
    c = Check(path, on_disk=on_disk, derived=derived)
    ov = status_override_for(doc or {}, path)
    if ov is not None:
        ov_st = norm_status(ov.get("status"))
        if ov_st == on_disk:
            c.verdict = "match"
            c.note = ("status_overrides: "
                      + str(ov.get("basis", ""))[:60])
            return c
        c.verdict = "drift"
        c.cls = "novel"
        c.note = (f"registry status disagrees with its own status_overrides "
                  f"entry ({ov_st})")
        return c
    if on_disk == derived:
        c.verdict = "match"
    elif on_disk in ("VERIFIED", "ROBUST") and derived == "EMERGING":
        if n_sources <= 2:
            c.verdict = "drift"
            c.cls = "expected_status_override"
            c.note = "above ladder at 1-2 sources — status_overrides owns this"
        else:
            c.verdict = "match"
            c.note = "3+ sources VERIFIED consistent with ladder (ROBUST needs subdomain evidence)"
    elif on_disk == "ROBUST" and derived == "VERIFIED":
        c.verdict = "unattributable"
        c.cls = "expected_status_override"
        c.note = "ROBUST needs cross-subdomain evidence (not scan-derivable)"
    elif on_disk == "EMERGING" and derived == "VERIFIED":
        c.verdict = "drift"
        c.cls = "novel"
        c.note = "ladder says promote (3+ sources); registry still EMERGING"
    else:
        c.verdict = "drift"
        c.cls = "novel"
    return c


# --------------------------------------------------------------------------- #
# partition region helpers (S2/S6 mechanics — unit-tested, unused by --check)
# --------------------------------------------------------------------------- #

class PartitionError(Exception):
    pass


def split_partitions(text: str) -> list[tuple[str, str]]:
    """Split registry text into an ordered list of (kind, text) segments where
    kind is 'authored' or 'derived'. A `# === DERIVED: ... ===` marker line
    starts a derived segment; `# === AUTHORED ===` starts an authored segment;
    text before the first marker is authored. Markers are NOT included in the
    segment texts. Raises PartitionError when no markers are present (the
    --apply refuses-to-run signal pre-S2)."""
    eol = "\r\n" if "\r\n" in text else "\n"
    lines = text.split(eol)
    segs: list[tuple[str, str]] = []
    kind = "authored"
    buf: list[str] = []
    for ln in lines:
        s = ln.strip()
        if s in (DERIVED_MARKER, AUTHORED_MARKER):
            segs.append((kind, eol.join(buf)))
            buf = []
            kind = "derived" if s == DERIVED_MARKER else "authored"
            continue
        buf.append(ln)
    segs.append((kind, eol.join(buf)))
    if not any(k == "derived" for k, _ in segs):
        raise PartitionError("registry lacks DERIVED/AUTHORED partition markers "
                             "(S2 not applied to this file)")
    return segs


def derived_regions(text: str) -> list[str]:
    """The derived-segment texts (in order)."""
    return [t for k, t in split_partitions(text) if k == "derived"]


def rebuild_registry_text(old_text: str, derived_region_texts: list[str] | str) -> str:
    """Re-emit the registry with new DERIVED segment texts (list, one per
    derived segment in order; a plain string replaces the FIRST derived
    segment and keeps the rest). Byte-preserves AUTHORED segments and the
    file's EOL convention; marker lines are re-inserted at segment bounds."""
    eol = "\r\n" if "\r\n" in old_text else "\n"
    segs = split_partitions(old_text)
    if isinstance(derived_region_texts, str):
        new_map = {next(i for i, (k, _t) in enumerate(segs) if k == "derived"):
                   derived_region_texts}
    else:
        der_idxs = [i for i, (k, _t) in enumerate(segs) if k == "derived"]
        if len(derived_region_texts) != len(der_idxs):
            raise PartitionError(f"expected {len(der_idxs)} derived segment "
                                 f"texts, got {len(derived_region_texts)}")
        new_map = dict(zip(der_idxs, derived_region_texts))
    out: list[str] = []
    for i, (kind, old_seg) in enumerate(segs):
        out.append(DERIVED_MARKER if kind == "derived" else AUTHORED_MARKER)
        seg = new_map.get(i, old_seg)
        out.append(seg.replace("\r\n", "\n").replace("\n", eol))  # eol-normalize only
    # drop a leading AUTHORED marker when the file does not start with one:
    # segment 0 is authored-with-no-marker if the original had no marker there
    first = segs[0][0]
    if first == "authored" and not old_text.lstrip().startswith(AUTHORED_MARKER):
        out = out[1:]  # omit the spurious leading AUTHORED marker
    return eol.join(out)


# --------------------------------------------------------------------------- #
# rebuilder: write-introduction (papers-list schema)
# --------------------------------------------------------------------------- #

INTRO_MODULE_DIRS = {
    "hooks": "hooks", "tensions": "tensions", "stakes": "stakes",
    "literature_turns": "literature-turns", "previews": "previews",
    "contributions": "contributions", "transitions": "transitions",
    "research_questions": "research-questions", "theory_lens": "theory-lens",
}


def _intro_files_for_entry(scan: CorpusScan, module: str, entry: str) -> list[str]:
    """Registry entry -> corpus files. REGISTRY_ALIASES mirrors the executor's
    exceptions; everything else maps module-dir/entry-stem."""
    files = []
    for stem_key, (sec, key) in cw.REGISTRY_ALIASES.items():
        if sec == module and key == entry:
            files += [rel for rel in scan.files if Path(rel).stem == stem_key]
    d = INTRO_MODULE_DIRS.get(module)
    if d:
        files += [rel for rel in scan.files
                  if rel.startswith(d + "/") and Path(rel).stem == entry]
    return sorted(set(files))


def intro_rebuild(scan: CorpusScan, doc: dict, alias: AliasIndex) -> list[Check]:
    checks: list[Check] = []
    for module, entries in (doc.get("evidence") or {}).items():
        for entry, ed in entries.items():
            if not isinstance(ed, dict):
                continue
            base = f"evidence.{module}.{entry}"
            rels = _intro_files_for_entry(scan, module, entry)
            wb_keys = {ck for rel in rels for b in scan.files[rel]["blocks"]
                       for ck, _ in b.wb}
            papers_disk = [strip_journal(p) for p in flowlist(ed.get("papers"))]
            cnt = ed.get("paper_count")
            if cnt is not None and ed.get("papers") is not None:
                checks.append(cmp_scalar(Check(
                    f"{base}.paper_count==len(papers)",
                    on_disk=cnt, derived=len(papers_disk))))
            gd = ed.get("gap_distribution")
            if isinstance(gd, dict) and cnt is not None:
                checks.append(cmp_scalar(Check(
                    f"{base}.gap_distribution.sum==paper_count",
                    on_disk=sum(gd.values()), derived=cnt)))
            if not rels:
                checks.append(Check(
                    f"{base}.papers", on_disk=papers_disk, derived=MISSING,
                    verdict="unattributable", cls="expected_legacy_gap",
                    note="entry file not located in corpus (or module exempt)"))
                continue
            for ck in sorted(wb_keys):
                tgt = alias.resolve(ck)
                if ck in papers_disk or (tgt and tgt in papers_disk):
                    checks.append(Check(
                        f"{base}.papers∋{ck}", verdict="match",
                        note=f"alias→{tgt}" if tgt and tgt != ck else ""))
                else:
                    checks.append(Check(
                        f"{base}.papers∋{ck}", on_disk=papers_disk, derived=ck,
                        verdict="drift", cls="expected_dual_key",
                        note="wb citekey not represented in registry papers list"))
            for p in papers_disk:
                if not any(p == ck or p == alias.resolve(ck) for ck in wb_keys):
                    checks.append(Check(
                        f"{base}.papers[{p}]", verdict="unattributable",
                        cls="expected_legacy_gap",
                        note="no wb marker attributes this paper (intro legacy-frozen)"))
    pi = doc.get("paper_index") or {}
    derived_pi_keys = {ck for _b, ck, _i in scan.markers()}
    for k in sorted(pi):
        if k in derived_pi_keys or any(alias.resolve(ck) == k for ck in derived_pi_keys):
            checks.append(Check(f"paper_index.{k}.key", verdict="match"))
        else:
            checks.append(Check(
                f"paper_index.{k}.key", on_disk=k, derived=MISSING,
                verdict="unattributable", cls="expected_dual_key",
                note="registry key not derivable from wb markers (short-key system)"))
    for ck in sorted(derived_pi_keys):
        if ck in pi or alias.resolve(ck) in pi:
            continue
        checks.append(Check(
            f"paper_index[{ck}]", on_disk=MISSING, derived=ck,
            verdict="drift", cls="expected_dual_key",
            note="wb citekey absent from paper_index"))
    checks.append(Check(
        "paper_index.*.gap_value", verdict="unattributable",
        cls="expected_authored_passthrough",
        note=f"{len(pi)} gap values are not recorded in blocks "
             "(--gap arg at writeback time is not block-provenanced)"))
    return checks


# --------------------------------------------------------------------------- #
# rebuilder: write-theory (paper-level fragment schema)
# --------------------------------------------------------------------------- #

def theory_block_papers(b: Block, alias: AliasIndex) -> set:
    """Papers a theory block is attributable to, normalized into the registry's
    canonical key system and deduped — a block can carry BOTH a full wb
    citekey and an already-canonical frontmatter source_papers entry for the
    SAME paper (dual-key system); counting both is the classic double-bump."""
    out = set()
    for p in ((b.fm or {}).get("source_papers") or []):
        out.add(alias.resolve(p) or p)
    for ck, _ in b.wb:
        out.add(alias.resolve(ck) or ck)
    return out


def theory_rebuild(scan: CorpusScan, doc: dict, alias: AliasIndex) -> list[Check]:
    checks: list[Check] = []
    # ---- patterns.* = blocks aggregated by pattern id ----
    blocks_by_pattern: dict[str, list[Block]] = {}
    for b in scan.all_blocks():
        pid = (b.fm or {}).get("pattern_id")
        if not pid and b.wb:
            pid = b.wb[0][1]  # wb item == pattern id on theory corpora
        if pid:
            blocks_by_pattern.setdefault(pid, []).append(b)
    patterns = doc.get("patterns") or {}
    for pid, pentry in patterns.items():
        if not isinstance(pentry, dict):
            continue
        base = f"patterns.{pid}"
        grp = blocks_by_pattern.get(pid, [])
        if not grp:
            checks.append(Check(
                base, on_disk=pentry, derived=MISSING, verdict="unattributable",
                cls="expected_legacy_gap", note="no block carries this pattern id"))
            continue
        papers = sorted({p for b in grp for p in theory_block_papers(b, alias)})
        homes = sorted({b.rel for b in grp})
        checks.append(cmp_scalar(Check(
            f"{base}.source_count==len(source_papers)",
            on_disk=pentry.get("source_count"),
            derived=len(flowlist(pentry.get("source_papers"))))))
        disk_papers = [alias.resolve(x) or x for x in flowlist(pentry.get("source_papers"))]
        der_extra = [p for p in papers if p not in disk_papers]
        disk_extra = [p for p in disk_papers if p not in papers]
        if der_extra:
            checks.append(Check(
                f"{base}.source_papers∋block-attested", on_disk=disk_papers,
                derived=der_extra, verdict="drift", cls="novel",
                note="block-attested paper(s) missing from pattern source_papers"))
        if disk_extra:
            checks.append(Check(
                f"{base}.source_papers[unattributed]", on_disk=disk_extra,
                derived=MISSING, verdict="unattributable", cls="expected_legacy_gap",
                note="registry lists paper(s) no scan-attributable block carries "
                     "(legacy blocks)"))
        if not der_extra and not disk_extra:
            checks.append(Check(f"{base}.source_papers", verdict="match"))
        hf = pentry.get("home_file")
        d_hf = Check(f"{base}.home_file", on_disk=hf, derived=homes)
        if isinstance(hf, str) and homes == [hf]:
            d_hf.verdict = "match"
        elif hf == homes:
            d_hf.verdict = "match"
        else:
            d_hf.verdict = "drift"
            d_hf.cls = "novel" if len(homes) > 1 else "expected_legacy_gap"
            if len(homes) > 1:
                d_hf.note = f"pattern spans {len(homes)} files: {homes}"
        checks.append(d_hf)
        n_status = max(len(papers), int(pentry.get("source_count") or 0))
        checks.append(status_cmp_check(
            f"{base}.status", norm_status(pentry.get("status")),
            ladder_status(n_status), n_status, doc=doc))
    for pid in sorted(set(blocks_by_pattern) - set(patterns)):
        grp = blocks_by_pattern[pid]
        papers = sorted({p for b in grp for p in theory_block_papers(b, alias)})
        marked = any(b.wb for b in grp)
        checks.append(Check(
            f"patterns[{pid}]", on_disk=MISSING, derived={
                "source_count": len(papers), "source_papers": papers,
                "home_file": sorted({b.rel for b in grp})},
            verdict="drift" if marked else "unattributable",
            cls="novel" if marked else "expected_legacy_gap",
            note="wb-marked block attests this pattern but the patterns section "
                 "lacks it (incomplete derived view)"
            if marked else
            "fm-attested pattern absent from patterns section (manual-era; "
            "S3 backfill will mint its wb marker)"))
    # ---- source_papers.<paper>.fragments ----
    frag_by_paper: dict[str, list[dict]] = {}
    for b in scan.all_blocks():
        papers = theory_block_papers(b, alias)
        pid = (b.fm or {}).get("pattern_id") or (b.wb[0][1] if b.wb else None)
        if not papers or not pid:
            continue
        for p in papers:
            frag_by_paper.setdefault(p, []).append({
                "type": pid, "title": b.heading, "home_files": [b.rel],
                "status": norm_status((b.fm or {}).get("status_token") or b.status),
                "_wb": bool(b.wb)})
    sp = doc.get("source_papers") or {}
    for paper, pentry in sp.items():
        if not isinstance(pentry, dict):
            continue
        base = f"source_papers.{paper}"
        frags = pentry.get("fragments") or []
        # index disk fragments by pattern type; a derived fragment matches when
        # its home file is among the registry entry's home_files (registry
        # entries may be multi-home: one tfr registered from several files)
        disk_by_type: dict[str, list[dict]] = {}
        for f in frags:
            if isinstance(f, dict):
                disk_by_type.setdefault(str(f.get("type", "")).lower(), []).append(f)
        matched_disk: set[int] = set()
        der_unmatched: list[dict] = []
        for df in frag_by_paper.get(paper, []):
            cands = [f for f in disk_by_type.get(str(df["type"]).lower(), [])
                     if id(f) not in matched_disk]
            homes_d = set(df["home_files"])
            hit = next((f for f in cands
                        if homes_d & {str(h).replace("\\", "/")
                                      for h in flowlist(f.get("home_files"))}), None)
            if hit is None:
                der_unmatched.append(df)
                continue
            matched_disk.add(id(hit))
            reg = hit
            st_r = norm_status(reg.get("status"))
            st_d = df["status"]
            if st_d == "" or st_d not in LADDER:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}].status", on_disk=st_r,
                    derived=st_d or MISSING, verdict="unattributable"
                    if st_d == "" else "drift",
                    cls="expected_legacy_gap" if st_d == "" else
                    "expected_stale_block_status",
                    note="" if st_d == "" else
                    "non-ladder block status vocabulary (pre-ladder era; "
                    "S4 wb-meta owns status)"))
            elif st_r == st_d:
                checks.append(Check(f"{base}.fragments[{df['type']}].status",
                                    verdict="match"))
            elif st_r in LADDER and LADDER.index(st_r) > LADDER.index(st_d):
                checks.append(Check(
                    f"{base}.fragments[{df['type']}].status", on_disk=st_r,
                    derived=st_d, verdict="drift", cls="expected_stale_block_status",
                    note="registry promoted; block frontmatter stale (S4 wb-meta owns)"))
            else:
                checks.append(Check(f"{base}.fragments[{df['type']}].status",
                                    on_disk=st_r, derived=st_d, verdict="drift",
                                    cls="novel"))
            hf_disk = {str(h).replace("\\", "/") for h in flowlist(reg.get("home_files"))}
            if homes_d <= hf_disk:
                checks.append(Check(f"{base}.fragments[{df['type']}].home_files",
                                    verdict="match",
                                    note="registry entry is multi-home"
                                    if len(hf_disk) > 1 else ""))
            else:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}].home_files",
                    on_disk=sorted(hf_disk), derived=sorted(homes_d),
                    verdict="drift", cls="novel",
                    note="block home not among registry entry homes"))
            t_disk = re.sub(r"\s+", "", str(reg.get("title", "")))
            t_der = re.sub(r"\s+", "", df["title"])
            if t_disk == t_der:
                checks.append(Check(f"{base}.fragments[{df['type']}].title",
                                    verdict="match"))
            else:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}].title",
                    on_disk=str(reg.get("title", ""))[:60], derived=df["title"][:60],
                    verdict="unattributable", cls="expected_legacy_gap",
                    note="title text differs from block heading (hand-written "
                         "legacy title; rebuild standardizes to heading)"))
        for df in der_unmatched:
            marked = bool(df.get("_wb"))
            afail = alias_failure(alias, paper) if marked else None
            if not marked:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}|{df['home_files'][0]}]",
                    on_disk=MISSING, derived=df["title"][:60],
                    verdict="unattributable", cls="expected_legacy_gap",
                    note="fm-attested block not in registry (manual-era; S3 "
                         "backfill will mint its wb marker)"))
            elif afail:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}|{df['home_files'][0]}]",
                    on_disk=MISSING, derived=df["title"][:60],
                    verdict="drift", cls="expected_dual_key",
                    note=f"wb-marked block missing; citekey resolution failed "
                         f"({afail}) — may live under the canonical key"))
            else:
                checks.append(Check(
                    f"{base}.fragments[{df['type']}|{df['home_files'][0]}]",
                    on_disk=MISSING, derived=df["title"][:60],
                    verdict="drift", cls="novel",
                    note="wb-marked block missing from registry (lost increment)"))
        for f in frags:
            if isinstance(f, dict) and id(f) not in matched_disk:
                checks.append(Check(
                    f"{base}.fragments[{f.get('fragment_id', '?')}]",
                    on_disk=f.get("fragment_id"), derived=MISSING,
                    verdict="unattributable", cls="expected_legacy_gap",
                    note="registry fragment with no frontmatter/wb-attributed block"))
        ids = [str(f.get("fragment_id")) for f in frags if isinstance(f, dict)]
        dup = [i for i, n in Counter(ids).items() if n > 1]
        if dup:
            checks.append(Check(f"{base}.fragments.fragment_id.unique",
                                on_disk=dup, derived=[], verdict="drift",
                                cls="novel", note="duplicate fragment_id"))
    for paper in sorted(set(frag_by_paper) - set(sp)):
        afail = alias_failure(alias, paper)
        checks.append(Check(
            f"source_papers[{paper}]", on_disk=MISSING,
            derived=len(frag_by_paper[paper]),
            verdict="drift",
            cls="expected_dual_key" if afail else "novel",
            note=(f"{len(frag_by_paper[paper])} block-attested fragments; "
                  f"citekey resolution failed ({afail}) — entry may exist "
                  "under the canonical key")
            if afail else
            f"{len(frag_by_paper[paper])} block-attested fragments, "
            "no registry entry"))
    # ---- summary_by_dimension: pure re-aggregation of AUTHORED inputs ----
    sbd = doc.get("summary_by_dimension") or {}
    agg: dict[str, dict] = {}
    for paper, pentry in sp.items():
        if not isinstance(pentry, dict):
            continue
        for f in pentry.get("fragments") or []:
            if not isinstance(f, dict) or not f.get("makadok_dimension"):
                continue
            a = agg.setdefault(str(f["makadok_dimension"]),
                               {"frags": 0, "papers": set(), "verified": set()})
            a["frags"] += 1
            a["papers"].add(paper)
            if norm_status(f.get("status")) in ("VERIFIED", "ROBUST"):
                a["verified"].add(str(f.get("type", "")).lower())
    for dim, dent in sbd.items():
        if not isinstance(dent, dict):
            continue
        base = f"summary_by_dimension.{dim}"
        a = agg.get(dim)
        if a is None:
            checks.append(Check(base, on_disk=dent, derived=MISSING,
                                verdict="drift", cls="novel",
                                note="dimension has no fragments to aggregate"))
            continue
        checks.append(cmp_scalar(Check(f"{base}.total_fragments",
                                       on_disk=dent.get("total_fragments"),
                                       derived=a["frags"])))
        checks.append(cmp_scalar(Check(f"{base}.source_papers",
                                       on_disk=dent.get("source_papers"),
                                       derived=len(a["papers"]))))
        if dent.get("verified_patterns") is not None:
            checks.append(cmp_scalar(Check(
                f"{base}.verified_patterns",
                on_disk=dent.get("verified_patterns"),
                derived=len(a["verified"]),
                note="derived = distinct VERIFIED+ fragment types carrying "
                     "this dimension (pattern-level approximation)")))
    for dim in sorted(set(agg) - set(sbd)):
        checks.append(Check(f"summary_by_dimension[{dim}]", on_disk=MISSING,
                            derived=agg[dim]["frags"], verdict="drift", cls="novel",
                            note="aggregated dimension absent from summary section"))
    # ---- meta ----
    meta = doc.get("meta") or {}
    n_aux = sum(1 for v in sp.values() if isinstance(v, dict)
                and str(v.get("source_tier", "")).lower() == "auxiliary")
    if "total_papers_indexed" in meta:
        c = cmp_scalar(Check(
            "meta.total_papers_indexed", on_disk=meta["total_papers_indexed"],
            derived=len(sp) - n_aux,
            note=f"{len(sp)} source_papers keys - {n_aux} auxiliary"))
        if c.verdict == "drift":
            # plan §3.1 documents this exact drift (83 vs 91 keys)
            c.cls = "expected_counter_drift"
            c.note += " (plan-documented stale manual count)"
        checks.append(c)
    if "batches_processed" in meta:
        checks.append(Check(
            "meta.batches_processed", on_disk=meta["batches_processed"],
            derived=MISSING, verdict="unattributable", cls="expected_counter_drift",
            note="audit counter without a batch ledger in this registry"))
    # AUTHORED boundary made explicit (audit surface, not drift candidates)
    checks.append(Check(
        "AUTHORED[source_papers.*.makadok_dimension|note|gap_type|"
        "theory_build_type|honesty_boundaries|next_batch_targets|"
        "unattributed_corpus]", verdict="unattributable",
        cls="expected_authored_passthrough",
        note="S4 wb-meta will move tfr makadok_dimension/note into blocks"))
    return checks


# --------------------------------------------------------------------------- #
# rebuilder: write-methods (papers-list + slots schema)
# --------------------------------------------------------------------------- #

def _file_for_stem(scan: CorpusScan, stem: str) -> list[str]:
    want = {stem, stem.replace("-", "_"), stem.replace("_", "-")}
    return sorted(rel for rel in scan.files
                  if "/" not in rel and Path(rel).stem in want)


def methods_rebuild(scan: CorpusScan, doc: dict, alias: AliasIndex) -> list[Check]:
    checks: list[Check] = []
    ev = doc.get("evidence") or {}
    bdt = ev.get("by_design_type") or {}
    paper_to_files: dict[str, set] = {}
    for key, dent in bdt.items():
        if not isinstance(dent, dict):
            continue
        base = f"evidence.by_design_type.{key}"
        rels = _file_for_stem(scan, key)
        if not rels:
            checks.append(Check(base, on_disk=dent, derived=MISSING,
                                verdict="unattributable", cls="expected_legacy_gap",
                                note="design-type file not found in corpus"))
            continue
        blocks = [b for rel in rels for b in scan.files[rel]["blocks"]]
        wb_keys = {ck for b in blocks for ck, _ in b.wb}
        block_slots = {s for b in blocks for s in b.slots}
        papers_disk = [strip_journal(p) for p in flowlist(dent.get("papers"))]
        cnt = dent.get("paper_count")
        if cnt is not None and dent.get("papers") is not None:
            checks.append(cmp_scalar(Check(f"{base}.paper_count==len(papers)",
                                           on_disk=cnt, derived=len(papers_disk))))
        for ck in sorted(wb_keys):
            tgt = alias.resolve(ck)
            for p in {ck, tgt} - {None}:
                paper_to_files.setdefault(p, set()).update(rels)
            if ck in papers_disk or (tgt and tgt in papers_disk):
                checks.append(Check(
                    f"{base}.papers∋{ck}", verdict="match",
                    note=f"alias→{tgt}" if tgt and tgt != ck else ""))
            else:
                checks.append(Check(
                    f"{base}.papers∋{ck}", on_disk=papers_disk, derived=ck,
                    verdict="drift", cls="expected_dual_key",
                    note="wb citekey not represented in papers list"))
        for p in papers_disk:
            if not any(p == ck or p == alias.resolve(ck) for ck in wb_keys):
                paper_to_files.setdefault(p, set()).update(rels)
                checks.append(Check(
                    f"{base}.papers[{p}]", verdict="unattributable",
                    cls="expected_legacy_gap",
                    note="no wb marker attributes this paper"))
        sc = dent.get("slots_covered")
        if sc is not None:
            disk_slots = set(re.findall(r"[MR]\d+", str(sc)))
            der_extra = block_slots - disk_slots
            disk_extra = disk_slots - block_slots
            if der_extra:
                checks.append(Check(
                    f"{base}.slots_covered∋blocks", on_disk=sorted(disk_slots),
                    derived=sorted(der_extra), verdict="drift", cls="novel",
                    note="block-attested slot(s) missing from slots_covered"))
            if disk_extra:
                checks.append(Check(
                    f"{base}.slots_covered[unattributed]", on_disk=sorted(disk_extra),
                    derived=MISSING, verdict="unattributable",
                    cls="expected_legacy_gap",
                    note="registry slot(s) no wb-marked block attests (hand-sync "
                         "era or block moved)"))
            if not der_extra and not disk_extra:
                checks.append(Check(f"{base}.slots_covered", verdict="match"))
    bsp = ev.get("by_source_paper") or {}
    for paper, pent in bsp.items():
        if not isinstance(pent, dict) or pent.get("design_types") is None:
            continue
        rev = alias.resolve(paper)
        derived_files = set(paper_to_files.get(paper, set()))
        if rev:
            derived_files |= set(paper_to_files.get(rev, set()))
        derived_dt = sorted(Path(r).stem for r in derived_files)
        disk_dt = [Path(str(x)).stem.replace("_", "-").replace(".md", "")
                   for x in flowlist(pent["design_types"])]
        der_extra = [d for d in derived_dt
                     if d.replace("_", "-") not in {x.replace("_", "-") for x in disk_dt}]
        if der_extra:
            checks.append(Check(
                f"evidence.by_source_paper.{paper}.design_types∋blocks",
                on_disk=disk_dt, derived=der_extra, verdict="drift", cls="novel",
                note="wb-marked block design type(s) missing from reverse lookup"))
        elif disk_dt:
            checks.append(Check(
                f"evidence.by_source_paper.{paper}.design_types[unattributed]",
                on_disk=disk_dt, derived=MISSING, verdict="unattributable",
                cls="expected_legacy_gap",
                note="registry design types not re-derivable (paper has no "
                     "wb-marked blocks)"))
        else:
            checks.append(Check(
                f"evidence.by_source_paper.{paper}.design_types", verdict="match"))
    meta = doc.get("meta") or {}
    if "total_design_types" in meta:
        checks.append(cmp_scalar(Check("meta.total_design_types",
                                       on_disk=meta["total_design_types"],
                                       derived=len(bdt))))
    if "batches_processed" in meta:
        checks.append(Check(
            "meta.batches_processed", on_disk=meta["batches_processed"],
            derived=MISSING, verdict="unattributable", cls="expected_counter_drift",
            note="audit counter; append-only ledger semantics kept"))
    checks.append(Check(
        "AUTHORED[common_failures|validation_history|verification_basis|note]",
        verdict="unattributable", cls="expected_authored_passthrough",
        note="the corpus's only real critique ledger — rebuild must never touch"))
    return checks


# --------------------------------------------------------------------------- #
# rebuilder: write-results (estimator slot-skeleton schema)
# --------------------------------------------------------------------------- #

def results_rebuild(scan: CorpusScan, doc: dict, alias: AliasIndex) -> list[Check]:
    checks: list[Check] = []
    est = doc.get("estimators") or {}
    texts: dict[str, list[str]] = {}

    def lines_of(rel: str) -> list[str]:
        if rel not in texts:
            texts[rel] = scan.file_text(rel).split("\n")
        return texts[rel]

    derived: dict[tuple, dict] = {}
    for b, ck, item in scan.markers():
        m = re.match(r"^r(\d+)_", item)
        if not m:
            continue
        est_key = Path(b.rel).stem.replace("-", "_")
        derived.setdefault((est_key, f"R{m.group(1)}"), {})[item] = {
            "sources": [ck], "corpus_path": f"corpus/{b.rel}", "block": b}
    for ekey, eentry in est.items():
        if not isinstance(eentry, dict):
            continue
        base = f"estimators.{ekey}"
        slots = eentry.get("slots") or {}
        for skey, sent in slots.items():
            if not isinstance(sent, dict):
                continue
            svs = sent.get("skeleton_variants") or []
            der = derived.get((ekey, skey), {})
            disk_ids = {str(v["id"]): v for v in svs
                        if isinstance(v, dict) and v.get("id")}
            for vid in sorted(set(der) - set(disk_ids)):
                # registry id may carry a run-specific suffix the block marker
                # lacks (r2_x vs r2_x_gulati_sytch2007) — id drift, not a loss
                sib = next((d2 for d2 in disk_ids if d2.startswith(vid + "_")), None)
                if sib:
                    checks.append(Check(
                        f"{base}.slots.{skey}.skeleton_variants[{vid}]",
                        on_disk=sib, derived=vid, verdict="drift",
                        cls="expected_dual_key",
                        note="registry id carries a run suffix absent from the "
                             "block marker (same variant)"))
                    continue
                checks.append(Check(
                    f"{base}.slots.{skey}.skeleton_variants[{vid}]",
                    on_disk=MISSING, derived=der[vid]["corpus_path"],
                    verdict="drift", cls="novel",
                    note="wb-marked block has no registry variant (lost increment)"))
            for vid, v in sorted(disk_ids.items()):
                vbase = f"{base}.slots.{skey}.skeleton_variants.{vid}"
                if vid not in der:
                    checks.append(Check(
                        vbase, on_disk=v.get("corpus_path"), derived=MISSING,
                        verdict="unattributable", cls="expected_legacy_gap",
                        note="registry variant without a wb-marked block"))
                    continue
                d = der[vid]
                src_disk = [alias.resolve(strip_journal(s)) or strip_journal(s)
                            for s in flowlist(v.get("sources"))]
                src_der = [alias.resolve(d["sources"][0]) or d["sources"][0]]
                checks.append(cmp_scalar(Check(
                    f"{vbase}.sources", on_disk=src_disk, derived=src_der),
                    normalize=lambda x: sorted(str(s).lower().replace("-", "_")
                                               for s in x) if isinstance(x, list) else x))
                if v.get("paper_count") is not None:
                    checks.append(cmp_scalar(Check(
                        f"{vbase}.paper_count==len(sources)",
                        on_disk=v["paper_count"],
                        derived=len(flowlist(v.get("sources"))))))
                if v.get("corpus_path") is not None:
                    checks.append(cmp_scalar(Check(
                        f"{vbase}.corpus_path", on_disk=str(v["corpus_path"]),
                        derived=d["corpus_path"])))
                if v.get("status") is not None:
                    n_status = max(len(src_disk),
                                   int(v.get("paper_count") or 0))
                    checks.append(status_cmp_check(
                        f"{vbase}.status", norm_status(v.get("status")),
                        ladder_status(n_status), n_status, doc=doc))
                # skeleton: re-derive from the block's **骨架** field; compare
                # whitespace-insensitively (executor wrote '. '-split + >- fold)
                if v.get("skeleton") is not None:
                    blk = d["block"]
                    body = "\n".join(lines_of(blk.rel)[blk.start:blk.end])
                    field_lines = cw._block_field(body, "骨架")
                    field = " ".join(
                        re.sub(r"^\s*>\s?", "", ln).strip().strip('"').strip()
                        for ln in field_lines).strip()                # quote strip
                    if not field:
                        checks.append(Check(
                            f"{vbase}.skeleton", on_disk="present", derived=MISSING,
                            verdict="unattributable", cls="expected_legacy_gap",
                            note="block lacks a **骨架** field"))
                    else:
                        same = re.sub(r"\s+", "", field) == \
                            re.sub(r"\s+", "", str(v["skeleton"]))
                        c = Check(f"{vbase}.skeleton",
                                  on_disk="present", derived="present")
                        c.verdict = "match" if same else "drift"
                        c.cls = None if same else "novel"
                        if not same:
                            c.note = ("text differs beyond whitespace "
                                      "(whitespace-insensitive compare)")
                        checks.append(c)
    for (ekey, skey), vs in sorted(derived.items()):
        slots = ((est.get(ekey) or {}).get("slots") or {})
        if ekey in est and skey not in slots:
            for vid in sorted(vs):
                checks.append(Check(
                    f"estimators.{ekey}.slots[{skey}].skeleton_variants[{vid}]",
                    on_disk=MISSING, derived=vs[vid]["corpus_path"],
                    verdict="drift", cls="novel",
                    note=f"slot {skey} missing under estimator "
                         "(slot-schema 误报 incident family)"))
    # INDEX variant counts vs variant-family headings in each file
    if "INDEX.md" in scan.files:
        for ln in scan.file_text("INDEX.md").split("\n"):
            m = re.match(r"^\|\s*\[([^\]]+)\]\(", ln)
            if not m:
                continue
            mm = re.search(r"\|\s*(\d+)\s*\|", ln)
            if not mm:
                continue
            stem, idx_n = m.group(1), int(mm.group(1))
            blocks = scan.files.get(f"{stem}.md", {}).get("blocks", [])
            n_var = sum(1 for b in blocks
                        if any(rx.search(b.full_heading())
                               for _f, rx in cw.LABEL_FAMILIES))
            n_wb = sum(len(b.wb) for b in blocks)
            c = Check(f"INDEX.{stem}.variant_count", on_disk=idx_n, derived=n_var)
            c.verdict = "match" if idx_n == n_var else "drift"
            c.cls = None if c.verdict == "match" else "novel"
            c.note = f"variant-family headings in {stem}.md; wb markers={n_wb}"
            checks.append(c)
    meta = doc.get("meta") or {}
    bh = doc.get("batch_history") or []
    if "batches_processed" in meta:
        c = cmp_scalar(Check(
            "meta.batches_processed==len(batch_history)",
            on_disk=meta["batches_processed"], derived=len(bh)))
        if c.verdict == "drift":
            # plan §3.1 documents this exact drift (49 vs batch_history)
            c.cls = "expected_counter_drift"
            c.note = "plan-documented stale manual count"
        checks.append(c)
    if "last_batch_id" in meta and bh:
        checks.append(cmp_scalar(Check(
            "meta.last_batch_id==batch_history[-1].batch_id",
            on_disk=str(meta["last_batch_id"]),
            derived=str(bh[-1].get("batch_id")))))
    if "total_papers_indexed" in meta:
        all_src = set()
        for eentry in est.values():
            if not isinstance(eentry, dict):
                continue
            for sent in (eentry.get("slots") or {}).values():
                if not isinstance(sent, dict):
                    continue
                for v in sent.get("skeleton_variants") or []:
                    if isinstance(v, dict):
                        all_src |= set(flowlist(v.get("sources")))
        checks.append(cmp_scalar(Check(
            "meta.total_papers_indexed==distinct sources",
            on_disk=meta["total_papers_indexed"], derived=len(all_src),
            note=f"{len(all_src)} distinct source keys across skeleton_variants")))
    checks.append(Check(
        "AUTHORED[verification_basis|paradigm_exclusivity|transferability|"
        "rhythm_tags|notes|batch_history本体|usage_stats|high_risk_missing|"
        "global_anti_patterns|honesty_boundaries]",
        verdict="unattributable", cls="expected_authored_passthrough",
        note="EXTEND-provenance and critique fields — rebuild passthrough only"))
    return checks


# --------------------------------------------------------------------------- #
# driver
# --------------------------------------------------------------------------- #

REBUILDERS = {
    "introduction": intro_rebuild,
    "theory": theory_rebuild,
    "methods": methods_rebuild,
    "results": results_rebuild,
}


def registry_for(corpus_key: str) -> Path:
    return SKILLS_ROOT / CORPUS_KEYS[corpus_key] / "_evidence_registry.yaml"


def alias_universe(corpus_key: str, doc: dict, scan: CorpusScan) -> tuple[list, list]:
    """(primary, secondary): primary = registry-side keys (canonical),
    secondary = wb marker citekeys (resolve into primary, never to themselves)."""
    primary: set[str] = set()

    def papers_of(ed):
        if isinstance(ed, dict):
            return {strip_journal(p) for p in flowlist(ed.get("papers"))}
        return set()
    if corpus_key == "introduction":
        for entries in (doc.get("evidence") or {}).values():
            for ed in entries.values():
                primary |= papers_of(ed)
        primary |= set(doc.get("paper_index") or {})
    elif corpus_key == "theory":
        sp = doc.get("source_papers") or {}
        primary |= set(sp)
        for pentry in sp.values():
            if isinstance(pentry, dict):
                for f in pentry.get("fragments") or []:
                    if isinstance(f, dict):
                        primary |= set(flowlist(f.get("source_papers")))
        for pentry in (doc.get("patterns") or {}).values():
            if isinstance(pentry, dict):
                primary |= set(flowlist(pentry.get("source_papers")))
    elif corpus_key == "methods":
        ev = doc.get("evidence") or {}
        for ed in (ev.get("by_design_type") or {}).values():
            primary |= papers_of(ed)
        primary |= set(ev.get("by_source_paper") or {})
    elif corpus_key == "results":
        for eentry in (doc.get("estimators") or {}).values():
            if not isinstance(eentry, dict):
                continue
            for sent in (eentry.get("slots") or {}).values():
                if not isinstance(sent, dict):
                    continue
                for v in sent.get("skeleton_variants") or []:
                    if isinstance(v, dict):
                        primary |= set(flowlist(v.get("sources")))
    secondary = {ck for _b, ck, _i in scan.markers()}
    return [k for k in primary if k], [k for k in secondary if k]


def check_corpus(corpus_key: str, quiet: bool = False) -> dict:
    root = SKILLS_ROOT / CORPUS_KEYS[corpus_key]
    reg_path = registry_for(corpus_key)
    text = reg_path.read_text(encoding="utf-8")
    doc = yaml.safe_load(text)
    scan = scan_corpus(root)
    prim, sec = alias_universe(corpus_key, doc, scan)
    alias = AliasIndex(prim, sec)
    checks = REBUILDERS[corpus_key](scan, doc, alias)
    counts = Counter(c.verdict for c in checks)
    cls_counts = Counter(c.cls for c in checks if c.cls)
    if not quiet:
        n_blocks = sum(len(f["blocks"]) for f in scan.files.values())
        print(f"[{corpus_key}] blocks={n_blocks} wb_markers={scan.n_markers} "
              f"checks={len(checks)} match={counts['match']} "
              f"drift={counts['drift']} unattributable={counts['unattributable']}")
        for cls, n in cls_counts.most_common():
            print(f"    {cls}: {n}")
    return {
        "registry": str(reg_path),
        "scan_stats": {
            "files_scanned": len(scan.files),
            "blocks": sum(len(f["blocks"]) for f in scan.files.values()),
            "wb_markers": scan.n_markers,
        },
        "summary": dict(counts),
        "adjudication_classes": dict(cls_counts),
        "alias_resolutions": dict(sorted(alias.resolutions.items())),
        "alias_ambiguous": dict(sorted(alias.ambiguous.items())),
        "alias_unresolved": sorted(alias.unresolved),
        "drifts": [c for c in checks if c.verdict == "drift"],
        "unattributable": [c for c in checks if c.verdict == "unattributable"],
        "n_matches": counts["match"],
    }


def _check_to_dict(c: Check) -> dict:
    d = {"path": c.path, "verdict": c.verdict}
    if c.cls:
        d["class"] = c.cls
    if c.note:
        d["note"] = c.note
    for side in ("on_disk", "derived"):
        v = getattr(c, side)
        if v is MISSING:
            d[side] = "<missing>"
        elif isinstance(v, Block):
            d[side] = "<block>"
        elif isinstance(v, (set, tuple)):
            d[side] = sorted(v)
        else:
            try:
                yaml.safe_dump(v)
                d[side] = v
            except yaml.YAMLError:
                d[side] = str(v)[:200]
    return d


def main() -> int:
    ap = argparse.ArgumentParser(description="Registry derived-view rebuilder")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--apply", action="store_true",
                    help="S6 switch: refuses until S2 partition markers exist")
    ap.add_argument("--corpus", default="all",
                    choices=["all", "introduction", "theory", "methods", "results"])
    ap.add_argument("--out", default=None,
                    help="report path (default ~/.claude/distill-work/rebuild_views/"
                         "reconciliation_report.yaml)")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        return run_self_tests()
    if args.apply:
        print("REFUSED: --apply requires S2 partition markers in the registries "
              "(S1 is read-only). Run --check instead.", file=sys.stderr)
        return 3

    corpora = list(REBUILDERS) if args.corpus == "all" else [args.corpus]
    report = {
        "generated": datetime.now().isoformat(timespec="seconds"),
        "mode": "check",
        "tool": "rebuild_views.py S1",
        "verdict_legend": {
            "match": "derived == on-disk",
            "drift": "both sides available, different — rebuild would change it",
            "unattributable": "on-disk value not re-derivable from blocks",
            "novel": "adjudication class: real drift candidate, needs human ruling",
        },
        "corpora": {},
    }
    for ck in corpora:
        report["corpora"][ck] = check_corpus(ck, quiet=args.quiet)
    total: Counter = Counter()
    for crep in report["corpora"].values():
        total.update(crep["summary"])
        for cls, n in crep["adjudication_classes"].items():
            total[f"class:{cls}"] += n
    novel_total = sum(1 for crep in report["corpora"].values()
                      for c in crep["drifts"] if c.cls == "novel")
    report["totals"] = dict(total)
    report["novel_drift_total"] = novel_total

    out = Path(args.out) if args.out else (
        Path.home() / ".claude" / "distill-work" / "rebuild_views" /
        "reconciliation_report.yaml")
    out.parent.mkdir(parents=True, exist_ok=True)
    dumpable = {}
    for ck, crep in report["corpora"].items():
        entry = {k: v for k, v in crep.items() if k not in ("drifts", "unattributable")}
        entry["drifts"] = [_check_to_dict(c) for c in crep["drifts"]]
        entry["unattributable"] = [_check_to_dict(c) for c in crep["unattributable"]]
        by_cls: dict[str, list] = {}
        for c in crep["drifts"] + crep["unattributable"]:
            by_cls.setdefault(c.cls or "?", []).append(c.path)
        entry["adjudication_paths"] = by_cls
        dumpable[ck] = entry
    doc = {**report, "corpora": dumpable}
    out.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=110),
                   encoding="utf-8")
    if not args.quiet:
        print(f"report -> {out}")
        print(f"TOTAL match={total.get('match', 0)} drift={total.get('drift', 0)} "
              f"unattributable={total.get('unattributable', 0)} "
              f"novel_drifts={novel_total}")
    return 0


# --------------------------------------------------------------------------- #
# self tests (S1 acceptance: CRLF, yaml validity, id: keys, EOL/indent edges)
# --------------------------------------------------------------------------- #

def run_self_tests() -> int:
    tests = []

    def register(fn):
        tests.append(fn)
        return fn

    @register
    def test_scan_blocks_and_markers():
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            f = root / "A_test.md"
            f.write_text(
                "# T\r\n\r\n## 变体 1：X 型\r\n\r\nbody **槽位**: M2\r\n\r\n"
                "<!-- wb:lu2022_frenemies:a1_x -->\r\n\r\n## 反模式\r\n\r\nbad\r\n",
                encoding="utf-8", newline="")
            scan = scan_corpus(root)
            blocks = scan.files["A_test.md"]["blocks"]
            assert [b.heading for b in blocks] == ["变体 1：X 型", "反模式"], blocks
            assert blocks[0].wb == [("lu2022_frenemies", "a1_x")]
            # slots derive from wb ITEM PREFIXES only (executor-faithful);
            # the **槽位** line is block-internal prose, not registry input
            assert blocks[0].slots == set(), blocks[0].slots
            assert blocks[1].wb == []

    @register
    def test_theory_frontmatter_three_positions():
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "V.md").write_text(
                "# T\n\n"
                "<!--\npattern_id: p_head\nsource_papers: [\"a2005_x\"]\n"
                "status: EMERGING — 单源\n-->\n\n"
                "## 变体 A：头置型\n\nbody A\n\n"
                "## 变体 B：尾置型\n\nbody B\n\n"
                "<!--\npattern_id: p_tail\nsource_papers: [\"b2010_y\"]\n"
                "status: VERIFIED\n-->\n\n"
                "<!-- wb:b2010_y:item_b -->\n\n"
                "## 变体 C：下块标题前\n\nbody C\n\n"
                "<!--\npattern_id: p_next\nsource_papers: [\"c2011_z\"]\n-->\n",
                encoding="utf-8", newline="")
            scan = scan_corpus(root)
            blocks = scan.files["V.md"]["blocks"]
            assert len(blocks) == 3, [b.heading for b in blocks]
            fm = [b.fm for b in blocks]
            assert fm[0]["pattern_id"] == "p_head"
            assert fm[0]["source_papers"] == ["a2005_x"]
            assert fm[0]["status_token"] == "EMERGING"
            assert fm[1]["pattern_id"] == "p_tail"
            assert fm[1]["source_papers"] == ["b2010_y"]
            assert fm[2]["pattern_id"] == "p_next"
            assert scan.n_markers == 1

    @register
    def test_partition_split_and_rebuild_crlf():
        text = ("meta: top\r\n"
                f"{DERIVED_MARKER}\r\n"
                "paper_count: 3\r\n"
                f"{AUTHORED_MARKER}\r\n"
                "note: 手写批评账\r\n")
        segs = split_partitions(text)
        assert [k for k, _ in segs] == ["authored", "derived", "authored"]
        head, region, tail = (t for _k, t in segs)
        assert "meta: top" in head and "paper_count" in region and "手写批评账" in tail
        new = rebuild_registry_text(text, "paper_count: 5")
        assert new.count("\r\n") == new.count("\n")          # CRLF-only, no mixed EOL
        segs2 = split_partitions(new)
        assert [t for k, t in segs2 if k == "authored"] == [head, tail]  # byte-preserved
        assert "paper_count: 5" in [t for k, t in segs2 if k == "derived"][0]
        assert yaml.safe_load(new.replace(DERIVED_MARKER, "# d")
                              .replace(AUTHORED_MARKER, "# a")) is not None

    @register
    def test_partition_multi_segment():
        """Markers may alternate; rebuild replaces each derived segment by
        position and byte-preserves every authored segment."""
        text = ("meta:\n  last_updated: x\n"
                f"{DERIVED_MARKER}\n"
                "counts:\n  a: 1\n"
                f"{AUTHORED_MARKER}\n"
                "status_rules: keep1\n"
                f"{DERIVED_MARKER}\n"
                "patterns:\n  p1: 2\n"
                f"{AUTHORED_MARKER}\n"
                "batch_history: keep2\n")
        segs = split_partitions(text)
        assert [k for k, _ in segs] == ["authored", "derived", "authored",
                                        "derived", "authored"]
        new = rebuild_registry_text(text, ["counts:\n  a: 9", "patterns:\n  p1: 9"])
        assert "a: 9" in new and "p1: 9" in new
        assert "keep1" in new and "keep2" in new and "last_updated: x" in new
        assert "\r\n" not in new  # LF-only file stays LF-only
        assert yaml.safe_load(new.replace(DERIVED_MARKER, "# d")
                              .replace(AUTHORED_MARKER, "# a"))["patterns"]["p1"] == 9

    @register
    def test_partition_error_pre_s2():
        try:
            split_partitions("a: 1\nb: 2\n")
            raise AssertionError("expected PartitionError")
        except PartitionError:
            pass

    @register
    def test_id_keys_survive_rebuild():
        """corpus_precheck chunks the registry at `id:` lines — they must
        survive a DERIVED-region rebuild."""
        text = ("estimators:\r\n"
                f"  {DERIVED_MARKER}\r\n"
                "  - id: r4_ols_x\r\n    skeleton: A. B\r\n"
                f"  {AUTHORED_MARKER}\r\n"
                "  note: keep\r\n")
        new = rebuild_registry_text(text, "- id: r4_ols_x\n  skeleton: A. B")
        assert re.search(r"^\s*- id: r4_ols_x", new, re.M), new

    @register
    def test_yaml_validity_of_scanned_fields():
        fm = _parse_fm_comment(
            'pattern_id: p1\nbuild_type: 调节效应型\n'
            'source_papers: ["a_2005_x", b2010y]\nstatus: EMERGING — 单篇')
        assert fm["pattern_id"] == "p1"
        assert fm["source_papers"] == ["a_2005_x", "b2010y"]
        assert fm["status_token"] == "EMERGING"
        assert _parse_fm_comment("just a note") is None

    @register
    def test_wb_meta_format():
        d = parse_wb_meta('dim=Boundary status=EMERGING gap=Incompleteness '
                          'tbt="机制推演型"')
        assert d == {"dim": "Boundary", "status": "EMERGING",
                     "gap": "Incompleteness", "tbt": "机制推演型"}, d
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "W.md").write_text(
                "## 变体 A\n\nbody\n\n"
                "<!-- wb:lu2022_frenemies:a1_x -->\n"
                "<!-- wb-meta: dim=Boundary status=EMERGING -->\n",
                encoding="utf-8", newline="")
            scan = scan_corpus(root)
            b = scan.files["W.md"]["blocks"][0]
            assert b.wb_meta == {"dim": "Boundary", "status": "EMERGING"}
            assert len(b.wb) == 1  # wb marker unaffected by wb-meta line

    @register
    def test_alias_engine():
        idx = AliasIndex([
            "gulati_2007_dependence_asymmetry_and_joint_dependence_in_int",
            "gulati2005-adaptation-vertical", "westphal_bednar_2005_asq"])
        assert idx.resolve("gulati_sytch2007") == \
            "gulati_2007_dependence_asymmetry_and_joint_dependence_in_int"
        assert idx.resolve("gulati2005") == "gulati2005-adaptation-vertical"
        assert idx.resolve("lu2022") is None and "lu2022" in idx.unresolved
        amb = AliasIndex(["a_2007_x", "b_2007_x"])
        assert amb.resolve("x2007") is None and amb.ambiguous  # tied overlap

    @register
    def test_strip_journal_and_flowlist():
        assert strip_journal("malshe2015 (JM)") == "malshe2015"
        assert strip_journal("westphal_bednar_2005_asq") == "westphal_bednar_2005_asq"
        assert flowlist(["M2", " M7"]) == ["M2", "M7"]
        assert flowlist("M2, M7") == ["M2", "M7"]
        assert flowlist("[M2 M7 M8]") == ["M2 M7 M8"]  # legacy single-string form

    @register
    def test_ladder_and_norm():
        assert ladder_status(1) == "EMERGING"
        assert ladder_status(2) == "EMERGING"
        assert ladder_status(3) == "VERIFIED"
        assert norm_status("VERIFIED (expert_audit_override)") == "VERIFIED"
        assert norm_status(None) == ""

    @register
    def test_indentation_boundaries_in_region():
        """Nested DERIVED content keeps its indent; AUTHORED tail untouched."""
        text = ("top:\n"
                "  sub: 1\n"
                f"{DERIVED_MARKER}\n"
                "  entry:\n    papers:\n      - a2010\n"
                f"{AUTHORED_MARKER}\n"
                "  deep:\n    kept: true\n")
        segs = split_partitions(text)
        head = segs[0][1]
        region = next(t for k, t in segs if k == "derived")
        tail = segs[-1][1]
        assert "  sub: 1" in head and "kept: true" in tail
        assert "      - a2010" in region
        new = rebuild_registry_text(text, region)
        assert new == text  # identical region round-trips byte-for-byte

    failed = 0
    for fn in tests:
        try:
            fn()
            print(f"[PASS] {fn.__name__}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            import traceback
            print(f"[FAIL] {fn.__name__}: {type(e).__name__}: {e}")
            traceback.print_exc()
    print(f"{len(tests) - failed}/{len(tests)} tests passed")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
