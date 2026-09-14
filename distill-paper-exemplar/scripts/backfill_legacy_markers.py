#!/usr/bin/env python3
"""S3 legacy backfill: mint wb markers for frontmatter-attributed theory blocks.

Deterministic (zero LLM): every theory corpus block that carries an HTML-comment
frontmatter with non-empty `source_papers` but NO wb marker gets, at its block
end, one minted marker per source paper:

  <!-- wb:<citekey>:legacy_<stem>_<label> -->

(label from the heading's variant family; block-line disambiguation on collision).
Block text is otherwise untouched. Byte-level IO (CRLF hard constraint), idempotent
(marked blocks skipped), per-file YAML-free markdown edit.

Usage:  py backfill_legacy_markers.py [--dry-run] [--report out.yaml]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rebuild_views as rv  # noqa: E402  (scanner, fm parsing, WB_RE, SKILLS_ROOT)

THEORY_ROOT = rv.SKILLS_ROOT / "write-theory" / "corpus"
HEAD_RE = re.compile(r"^(#{2,4})\s+(.+?)\s*$")


def variant_label(heading: str) -> str:
    """Label token from the heading's variant family (E13 / D / 5 ...)."""
    for _fam, rx in rv.cw.LABEL_FAMILIES:
        m = rx.match(heading if heading.startswith("#") else f"### {heading}")
        if m:
            return m.group(1)
    slug = re.sub(r"[^\w]+", "", heading)[:20]
    return slug or "x"


def minted_items_for_file(rel: str, scan: rv.CorpusScan, text: str) -> list[tuple[int, list[str]]]:
    """(insert_line_index, marker_lines) per block attributed by the SCANNER
    (three-position frontmatter rule) — never per raw span, which would
    wrongly mint for a '下块标题前' comment belonging to the next block."""
    lines = text.split("\n")
    plan: list[tuple[int, list[str]]] = []
    used_items: set[str] = set()
    stem = Path(rel).stem
    for b in scan.files[rel]["blocks"]:
        if not b.wb and b.fm and b.fm.get("source_papers"):
            papers = b.fm["source_papers"]
        else:
            continue  # no attribution, or already executor-marked
        base = f"legacy_{stem}_{variant_label(b.heading)}"
        used = set()
        items = []
        for p in papers:
            item = base
            n = 2
            while (p, item) in used_items or item in used:
                item = f"{base}_{n}"
                n += 1
            used.add(item)
            used_items.add((p, item))
            items.append(f"<!-- wb:{p}:{item} -->")
        # insert after the last non-blank line of the block span
        last = b.end - 1
        while last > b.start and not lines[last].strip():
            last -= 1
        plan.append((last + 1, items))
    return plan


def backfill(dry_run: bool = False) -> dict:
    scan = rv.scan_corpus(THEORY_ROOT)
    report = {"files": {}, "minted": 0}
    for rel in sorted(scan.files):
        text = (THEORY_ROOT / rel).read_bytes().decode("utf-8")
        eol = "\r\n" if "\r\n" in text else "\n"
        blocks = scan.files[rel]["blocks"]
        n_fm = sum(1 for b in blocks if b.fm)
        n_marked = sum(1 for b in blocks if b.wb)
        plan = minted_items_for_file(rel, scan, text)
        if not plan:
            continue
        lines = text.split(eol)
        for idx, items in sorted(plan, key=lambda x: -x[0]):
            lines[idx:idx] = items
        new_text = eol.join(lines)
        if not new_text.endswith(eol):
            new_text += eol
        report["files"][rel] = {"fm_blocks": n_fm, "already_marked": n_marked,
                                "minted_markers": sum(len(v) for _i, v in plan)}
        report["minted"] += sum(len(v) for _i, v in plan)
        if not dry_run:
            with open(THEORY_ROOT / rel, "w", encoding="utf-8", newline="") as fh:
                fh.write(new_text)
    return report


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa: BLE001
        pass
    dry = "--dry-run" in sys.argv
    report = backfill(dry_run=dry)
    print(f"mode={'dry-run' if dry else 'APPLY'} minted={report['minted']} "
          f"files={len(report['files'])}")
    for rel, st in sorted(report["files"].items()):
        print(f"  {rel}: fm={st['fm_blocks']} marked={st['already_marked']} "
              f"minted={st['minted_markers']}")
    out = Path.home() / ".claude" / "distill-work" / "rebuild_views" / \
        "backfill_theory_report.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(yaml.safe_dump(report, allow_unicode=True, sort_keys=False),
                   encoding="utf-8")
    print(f"report -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
