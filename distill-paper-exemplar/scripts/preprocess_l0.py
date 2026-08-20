#!/usr/bin/env python3
"""L0 preprocessing for distill-paper-exemplar.

Deterministic, no-LLM step run BEFORE any distillation:
  1. strip base64 data-URI images (44-89% of paper-import MD bytes) -> placeholder refs
  2. materialize section slice files (introduction/theory/methods/results/discussion)

Output layout (PDM workdir, sibling of the source MD):
  <paper_dir>/<citekey>.pdm/
    fulltext.text-only.md          # base64-stripped full text (only file agents may read)
    sections/<section>.md          # materialized slices (best effort)
    l0_manifest.json               # detection report for PDM registration

The raw source MD is NEVER modified and must never be read by distill agents.
Section detection is heading-based and conservative: anything uncertain is
reported as "unknown" so the orchestrator can fall back to manual slicing.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# bucket -> heading patterns (case-insensitive, matched against heading text)
SECTION_PATTERNS = {
    "introduction": [r"^introduction\b"],
    "theory": [
        r"^theor", r"hypothes", r"literature review", r"^background\b",
        r"conceptual (framework|development)", r"research model",
    ],
    "methods": [
        r"^methods?\b", r"^data\b", r"^data and methods\b", r"^sample\b",
        r"research design", r"empirical (setting|context|strategy|model)",
        r"^identification\b", r"materials and methods", r"^methodology\b",
    ],
    "results": [r"^results?\b", r"^findings?\b", r"^analys(e|i)s\b", r"empirical results"],
    "discussion": [r"^discussion\b", r"^conclusions?\b", r"discussion and conclusion"],
}
BUCKET_ORDER = ["introduction", "theory", "methods", "results", "discussion"]

IMG_DATA_URI_MD = re.compile(r"!\[([^\]]*)\]\(\s*data:image/[^)\s]+[^)]*\)")
IMG_DATA_URI_HTML = re.compile(r'<img\b[^>]*\bsrc="data:image/[^"]*"[^>]*/?>', re.I)
HEADING = re.compile(r"^(#{1,3})\s+(.+?)\s*#*\s*$")


def strip_base64(text: str) -> tuple[str, int]:
    """Replace data-URI images with stable placeholder refs. Returns (text, n_images)."""
    counter = {"n": 0}

    def _md_sub(m: re.Match) -> str:
        counter["n"] += 1
        return f"![fig-{counter['n']}](image-ref-{counter['n']})"

    text = IMG_DATA_URI_MD.sub(_md_sub, text)

    def _html_sub(m: re.Match) -> str:
        counter["n"] += 1
        return f"![fig-{counter['n']}](image-ref-{counter['n']})"

    text = IMG_DATA_URI_HTML.sub(_html_sub, text)
    return text, counter["n"]


def classify_heading(title: str) -> str | None:
    t = title.strip().lower()
    t = re.sub(r"^\d+(\.\d+)*[.\s]+", "", t)  # strip "1. ", "2.3 " numbering
    for bucket in BUCKET_ORDER:
        for pat in SECTION_PATTERNS[bucket]:
            if re.search(pat, t):
                return bucket
    return None


def slice_sections(lines: list[str]) -> dict:
    """Return {bucket: {start, end, heading}} using 1-based inclusive line ranges.

    A bucket spans from its heading to the line before the next *classified*
    heading. Unclassified headings (references, appendix, tables) terminate a
    span only at level 1-2 when they follow a classified bucket, so that e.g.
    'References' ends 'discussion'. First match per bucket wins.
    """
    headings = []  # (lineno_0based, level, title, bucket)
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if m:
            headings.append((i, len(m.group(1)), m.group(2), classify_heading(m.group(2))))

    spans: dict[str, dict] = {}
    classified = [(ln, lv, ti, b) for ln, lv, ti, b in headings if b]
    for idx, (ln, lv, ti, bucket) in enumerate(classified):
        if bucket in spans:
            continue  # first match wins; later same-bucket headings stay inside span
        end = len(lines)
        for ln2, lv2, _ti2, b2 in headings:
            if ln2 <= ln:
                continue
            if b2 is not None and b2 != bucket:
                end = ln2
                break
            if b2 == bucket and lv2 <= lv:
                end = ln2  # sibling heading of same bucket closes nothing, skip
                continue
            if b2 is None and lv2 <= 2 and re.match(
                r"(?i)\s*(references|bibliography|appendix|tables?\b|figures?\b|supplement)", _strip_num(_ti2)
            ):
                end = ln2
                break
        else:
            end = len(lines)
        spans[bucket] = {"start": ln + 1, "end": end, "heading": ti}
    return spans


def _strip_num(t: str) -> str:
    return re.sub(r"^\d+(\.\d+)*[.\s]+", "", t.strip().lower())


def derive_citekey(path: Path) -> str:
    stem = re.sub(r"-(OvisOCR2|MinerU)-\d{8}-\d{6}$", "", path.stem)
    stem = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").lower()
    return stem[:60] or "paper"


def main() -> int:
    ap = argparse.ArgumentParser(description="L0 preprocess: strip base64 + materialize section slices")
    ap.add_argument("source_md", help="path to paper-import full-text MD (read-only)")
    ap.add_argument("--citekey", default=None, help="PDM citekey (default: derived from filename)")
    ap.add_argument("--outdir", default=None, help="PDM workdir (default: <paper_dir>/<citekey>.pdm/)")
    ap.add_argument("--force", action="store_true", help="override a fresh PDM LOCK")
    ap.add_argument("--unlock", action="store_true", help="remove the PDM LOCK and exit")
    args = ap.parse_args()

    src = Path(args.source_md)
    if not src.is_file():
        print(f"ERROR: not a file: {src}", file=sys.stderr)
        return 2
    citekey = args.citekey or derive_citekey(src)
    outdir = Path(args.outdir) if args.outdir else src.parent / f"{citekey}.pdm"

    # Double-run guard: one PDM must never be distilled in two concurrent windows
    # (2026-08 实测：双窗口把 L1–L3 整链路跑了两遍，是单次运行最大浪费源)。
    lock = outdir / "LOCK"
    if args.unlock:
        lock.unlink(missing_ok=True)
        print(f"unlocked: {lock}")
        return 0
    if lock.exists() and not args.force:
        import time

        age_h = (time.time() - lock.stat().st_mtime) / 3600
        if age_h < 12:
            print(
                f"ERROR: {lock} exists (age {age_h:.1f}h < 12h) — another session may be "
                "distilling this PDM. If it is stale, rerun with --force.",
                file=sys.stderr,
            )
            return 3
    outdir.mkdir(parents=True, exist_ok=True)
    lock.write_text(f"pid={__import__('os').getpid()}\n", encoding="utf-8")
    sections_dir = outdir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)

    raw = src.read_text(encoding="utf-8", errors="replace")
    raw_bytes = len(raw.encode("utf-8"))
    text, n_images = strip_base64(raw)
    lines = text.split("\n")

    text_only = outdir / "fulltext.text-only.md"
    text_only.write_text(text, encoding="utf-8")

    spans = slice_sections(lines)
    manifest = {
        "citekey": citekey,
        "source_md": str(src),
        "text_only_md": str(text_only),
        "raw_bytes": raw_bytes,
        "text_only_bytes": len(text.encode("utf-8")),
        "images_replaced": n_images,
        "section_slices": {},
        "sections_unknown": [b for b in BUCKET_ORDER if b not in spans],
    }
    for bucket, sp in spans.items():
        body = "\n".join(lines[sp["start"] - 1 : sp["end"]]).rstrip() + "\n"
        out = sections_dir / f"{bucket}.md"
        out.write_text(body, encoding="utf-8")
        manifest["section_slices"][bucket] = {
            "path": str(out),
            "start_line": sp["start"],
            "end_line": sp["end"],
            "words": len(body.split()),
            "heading": sp["heading"],
        }

    (outdir / "l0_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    if manifest["sections_unknown"]:
        print(
            "WARN: undetected sections -> " + ", ".join(manifest["sections_unknown"])
            + " (orchestrator: slice manually or mark unknown)",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
