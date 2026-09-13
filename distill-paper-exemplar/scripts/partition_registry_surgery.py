#!/usr/bin/env python3
"""S2 partition surgery for the four evidence registries (one-shot migration).

Inserts AUTHORED/DERIVED partition marker lines at top-level section bounds
and adds a machine-readable `status_overrides:` section (AUTHORED) that
consolidates the scattered user-designation / expert-audit rulings so the
rebuild's derived status = ladder ⊕ status_overrides reproduces on-disk state.

VALUES ARE NOT CHANGED: the surgery is line-insertion only. Verification after
each file: (a) YAML deep-equal vs the original minus the added status_overrides
key, (b) CRLF preservation, (c) marker count matches the layout spec.

Layouts (top-level key -> segment kind):
  introduction: meta=A evidence=D phrasebank=A paper_index=D critique=A
  theory:       meta=D status_rules=A source_papers=D patterns=D
                summary_by_dimension=D honesty_boundaries=A
                next_batch_targets=A unattributed_corpus=A critique=A
  methods:      meta=D evidence=D (+ status_overrides appended at EOF, A)
  results:      meta=D status_rules=A global_anti_patterns=A
                global_honesty_boundaries=A estimators=D batch_history=A

status_overrides population (mechanical, verbatim values):
  results  estimators.<ek>.slots.<sk>.skeleton_variants.<id>  <- verification_basis
  theory   patterns.<pid>                                     <- carried VERIFIED@<=2
  methods  evidence.by_source_paper.<paper>                   <- verification_basis
  intro    evidence.<module>.<entry>                          <- carried status@<=2

Usage: py partition_registry_surgery.py [--dry-run]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_views as rv  # noqa: E402  (markers, corpus roots, ladder, norm)

SKILLS_ROOT = rv.SKILLS_ROOT
REGISTRIES = {k: SKILLS_ROOT / v / "_evidence_registry.yaml"
              for k, v in rv.CORPUS_KEYS.items()}

# top-level keys that start each segment kind, per corpus
LAYOUTS = {
    "introduction": [
        ("A", None),                       # meta (head, no marker needed)
        ("D", "evidence"),
        ("A", "phrasebank"),
        ("D", "paper_index"),
        ("A", "critique"),
        ("A", "status_overrides"),         # appended at EOF (inside A tail)
    ],
    "theory": [
        ("D", "meta"),
        ("A", "status_rules"),
        ("D", "source_papers"),
        ("D", "patterns"),
        ("D", "summary_by_dimension"),
        ("A", "honesty_boundaries"),
        ("A", "next_batch_targets"),
        ("A", "unattributed_corpus"),
        ("A", "critique"),
        ("A", "status_overrides"),         # appended at EOF (inside A tail)
    ],
    "methods": [
        ("D", "meta"),
        ("D", "evidence"),
        ("A", "status_overrides"),         # new section at EOF
    ],
    "results": [
        ("D", "meta"),
        ("A", "status_rules"),
        ("A", "global_anti_patterns"),
        ("A", "global_honesty_boundaries"),
        ("D", "estimators"),
        ("A", "batch_history"),
        ("A", "status_overrides"),         # appended at EOF (inside A tail)
    ],
}

OVERRIDES_NOTE = (
    "用户裁定状态，显式越过 phase-4 ladder（1–2 来源 EMERGING / 3+ VERIFIED / "
    "5+ 跨 2 子域 ROBUST；见 distill-theory-exemplar/references/"
    "phase-4-validation-writeback.md L232-238）。rebuild 派生 status = ladder ⊕ "
    "本节（本节显式优先）；键为 registry 路径，value.status 为裁定档位，"
    "value.basis 为裁定凭据原文。本节属 AUTHORED——rebuild 透传不改。"
)


def _norm(s) -> str:
    return rv.norm_status(s)


def collect_overrides(corpus: str, doc: dict) -> dict:
    """Mechanical override extraction — verbatim from the registry."""
    out: dict[str, dict] = {}

    def add(path: str, status, basis: str):
        out[path] = {"status": str(status), "basis": basis}

    if corpus == "results":
        for ek, e in (doc.get("estimators") or {}).items():
            if not isinstance(e, dict):
                continue
            for sk, s in (e.get("slots") or {}).items():
                if not isinstance(s, dict):
                    continue
                for v in (s.get("skeleton_variants") or []):
                    if isinstance(v, dict) and v.get("verification_basis"):
                        add(f"estimators.{ek}.slots.{sk}.skeleton_variants.{v['id']}",
                            v.get("status"), str(v["verification_basis"]))
    elif corpus == "theory":
        for pid, p in (doc.get("patterns") or {}).items():
            if not isinstance(p, dict):
                continue
            st = _norm(p.get("status"))
            if st in ("VERIFIED", "ROBUST") and (p.get("source_count") or 0) <= 2:
                add(f"patterns.{pid}", st,
                    "pre-partition carried status（用户裁定时代：召回域 2026-08-29 / "
                    "Westphal·Gulati 系 2026-09-05/06 等全局单源裁定；块内无字段化凭据）")
    elif corpus == "methods":
        for pk, p in ((doc.get("evidence") or {}).get("by_source_paper") or {}).items():
            if isinstance(p, dict) and p.get("verification_basis"):
                add(f"evidence.by_source_paper.{pk}", p.get("status"),
                    str(p["verification_basis"]))
    elif corpus == "introduction":
        for mod, entries in (doc.get("evidence") or {}).items():
            for k, e in entries.items():
                if not isinstance(e, dict):
                    continue
                st = _norm(e.get("status"))
                pc = e.get("paper_count")
                if st in ("VERIFIED", "ROBUST") and isinstance(pc, int) and pc <= 2:
                    add(f"evidence.{mod}.{k}", st,
                        "pre-partition carried status（单源/双源用户裁定时代）")
    return out


def render_overrides_section(overrides: dict) -> list[str]:
    lines = ["status_overrides:",
             "  schema: '1.0'",
             "  note: >-",
             "    " + OVERRIDES_NOTE,
             "  overrides:"]
    if not overrides:
        lines.append("    {}")
        return lines
    for path in sorted(overrides):
        ov = overrides[path]
        lines.append(f"    {path}:")
        lines.append(f"      status: {ov['status']}")
        basis = str(ov["basis"]).replace("\n", " ").strip()
        lines.append("      basis: >-")
        lines.append("        " + basis)
    return lines


def surgery(corpus: str, dry_run: bool = False) -> list[str]:
    reg_path = REGISTRIES[corpus]
    # read BYTES: Path.read_text() applies universal-newline translation and
    # would silently destroy the registries' CRLF convention (hard constraint)
    text = reg_path.read_bytes().decode("utf-8")
    if rv.DERIVED_MARKER in text or rv.AUTHORED_MARKER in text:
        raise RuntimeError(f"{corpus}: partition markers already present — "
                           "surgery already applied (idempotency guard)")
    eol = "\r\n" if "\r\n" in text else "\n"
    doc = yaml.safe_load(text)
    orig_doc = yaml.safe_load(text)  # deep-compare basis
    lines = text.split(eol)

    # locate top-level key lines (column 0)
    key_lines: dict[str, int] = {}
    for i, ln in enumerate(lines):
        m = re.match(r"^([A-Za-z_][\w]*):\s*(?:#.*)?$", ln)
        if m and m.group(1) not in key_lines:
            key_lines[m.group(1)] = i

    overrides = collect_overrides(corpus, doc)
    layout = LAYOUTS[corpus]

    # build insertion plan: (line_index, [marker/section lines]); a marker is
    # only inserted when the segment KIND CHANGES (no redundant same-kind runs)
    insertions: list[tuple[int, list[str]]] = []
    prev_kind: str | None = None
    for kind, key in layout:
        if key is None:                    # head segment, no marker needed
            prev_kind = kind
            continue
        if key == "status_overrides":
            extra = render_overrides_section(overrides)
            if kind != prev_kind:          # switching into AUTHORED: marker first
                extra = [rv.AUTHORED_MARKER] + extra
            insertions.append((len(lines), extra))
            continue
        if key not in key_lines:
            raise KeyError(f"{corpus}: top-level key {key!r} not found")
        i = key_lines[key]
        if i > 0 and kind != prev_kind:
            insertions.append((i, [rv.DERIVED_MARKER if kind == "D"
                                   else rv.AUTHORED_MARKER]))
        prev_kind = kind

    # insert bottom-up so indices stay valid
    for i, extra in sorted(insertions, key=lambda x: -x[0]):
        lines[i:i] = extra
    new_text = eol.join(lines)
    if not new_text.endswith(eol):
        new_text += eol

    # --- verification ---
    new_doc = yaml.safe_load(new_text)
    problems = []
    for k in ("schema_version", "registry_type"):
        pass
    # deep-equal minus status_overrides
    baseline = {k: v for k, v in new_doc.items() if k != "status_overrides"}
    if baseline != orig_doc:
        diffs = [k for k in set(baseline) | set(orig_doc)
                 if baseline.get(k) != orig_doc.get(k)]
        problems.append(f"YAML values changed: {diffs}")
    if eol == "\r\n":
        if "\r\n" not in new_text or new_text.count("\r\n") != new_text.count("\n"):
            problems.append("CRLF not preserved")
    elif "\r\n" in new_text:
        problems.append("unexpected CRLF in LF file")
    n_markers = new_text.count(rv.DERIVED_MARKER) + new_text.count(rv.AUTHORED_MARKER)
    n_expected, prev = 0, None
    for kind, key in layout:
        if key == "status_overrides":
            if kind != prev:
                n_expected += 1
            continue
        if key not in (None,) and kind != prev and key_lines.get(key, 0) > 0:
            n_expected += 1
        if key not in (None,):
            prev = kind
    if n_markers != n_expected:
        problems.append(f"markers {n_markers} != expected {n_expected}")

    msgs = [f"[{corpus}] overrides={len(overrides)} markers={n_markers}"]
    if problems:
        for p in problems:
            msgs.append(f"  FAIL {p}")
        raise RuntimeError("; ".join(problems))
    msgs.append(f"  OK yaml-equal (minus status_overrides), EOL preserved")
    if not dry_run:
        with open(reg_path, "w", encoding="utf-8", newline="") as fh:
            fh.write(new_text)
        msgs.append(f"  written {reg_path}")
    else:
        msgs.append("  DRY-RUN (not written)")
    return msgs


def main() -> int:
    dry = "--dry-run" in sys.argv
    only = None
    for a in sys.argv[1:]:
        if a not in ("--dry-run",) and not a.startswith("--"):
            only = a
    corpora = [only] if only else list(REGISTRIES)
    rc = 0
    for c in corpora:
        try:
            for m in surgery(c, dry_run=dry):
                print(m)
        except Exception as e:  # noqa: BLE001
            print(f"[{c}] ERROR {e}")
            rc = 1
    return rc


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    sys.exit(main())
