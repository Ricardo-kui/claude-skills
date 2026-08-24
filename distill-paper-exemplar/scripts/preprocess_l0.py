#!/usr/bin/env python3
"""L0 preprocessing for distill-paper-exemplar.

Deterministic, no-LLM step run BEFORE any distillation:
  1. strip base64 data-URI images (44-89% of paper-import MD bytes) -> placeholder refs
  2. materialize section slice files (introduction/theory/methods/results/discussion)

Output layout (PDM workdir):
  DEFAULT: <DISTILL_WORK_ROOT or ~/.claude/distill-work>/<citekey>.pdm/
    — deliberately OUTSIDE the vault/OneDrive (2026-08-20 user ruling: 蒸馏
    不得在论文目录生成一堆中间文件). Everything in the workdir is
    deterministically rebuildable from the source MD; delete freely.
    Pass --outdir to keep the workdir next to the paper (archival runs).
    fulltext.text-only.md          # base64-stripped full text (only file agents may read)
    sections/<section>.md          # materialized slices (best effort)
    l0_manifest.json               # detection report for PDM registration

  --unlock removes the LOCK; --clean removes the whole workdir (run at L4).

  --keep-sentences writes a durable sentence inventory to
    story-blueprints/v4/rhetoric-moves/sources/<citekey>.sentences.md
    (cross-source synthesis raw material for P2 move enrichment; NOT deleted
    by --clean — it is a deliberate asset, not an intermediate product).

The raw source MD is NEVER modified and must never be read by distill agents.
Section detection is heading-based and conservative: anything uncertain is
reported as "unknown" so the orchestrator can fall back to manual slicing.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from datetime import date
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
    "discussion": [r"^discussion\b", r"^conclusions?\b", r"discussion and conclusion",
                   r"discussion\b", r"^extensions?\b", r"^concluding"],
}
BUCKET_ORDER = ["introduction", "theory", "methods", "results", "discussion"]

IMG_DATA_URI_MD = re.compile(r"!\[([^\]]*)\]\(\s*data:image/[^)\s]+[^)]*\)")
IMG_DATA_URI_HTML = re.compile(r'<img\b[^>]*\bsrc="data:image/[^"]*"[^>]*/?>', re.I)
HEADING = re.compile(r"^(#{1,3})\s+(.+?)\s*#*\s*$")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SOURCES_DIR = (
    SKILLS_ROOT / "story-blueprints" / "v4" / "rhetoric-moves" / "sources"
)


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

    # Implicit introduction (2026-08-20): AMJ-style papers often leave the intro
    # unlabeled — text between the Abstract and the first classified heading IS
    # the introduction. Skip only the abstract paragraph itself.
    if "introduction" not in spans and classified:
        first_ln = min(ln for ln, _, _, _ in classified)  # 0-based
        start = None
        for ln, _lv, ti, _b in headings:
            if ln >= first_ln:
                break
            if re.match(r"(?i)\s*abstract\b", _strip_num(ti)):
                j = ln + 1
                while j < first_ln and not lines[j].strip():
                    j += 1
                while j < first_ln and lines[j].strip():  # skip abstract paragraph
                    j += 1
                start = j
        if start is None:
            prev = [ln for ln, _, _, _ in headings if ln < first_ln]
            start = (max(prev) + 1) if prev else 0
        if len(" ".join(lines[start:first_ln]).split()) >= 50:
            spans["introduction"] = {"start": start + 1, "end": first_ln,
                                     "heading": "(implicit introduction)"}
    return spans


def _strip_num(t: str) -> str:
    return re.sub(r"^\d+(\.\d+)*[.\s]+", "", t.strip().lower())


def derive_citekey(path: Path) -> str:
    stem = re.sub(r"-(OvisOCR2|MinerU)-\d{8}-\d{6}$", "", path.stem)
    stem = re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").lower()
    return stem[:60] or "paper"


def work_root() -> Path:
    env = os.environ.get("DISTILL_WORK_ROOT")
    return Path(env) if env else Path.home() / ".claude" / "distill-work"


def extract_sentences(body: str) -> list[tuple[int, str]]:
    """Best-effort sentence split of a section slice.

    Returns [(paragraph_1based_index, sentence), ...]. Drops headings, list
    markers, table/figure captions, and fragments shorter than 40 chars.
    Provenance is paragraph-level — enough to route a sentence back to its
    context for P2 enrichment, not a citation formatter.
    """
    paragraphs = re.split(r"\n\s*\n", body.strip())
    out: list[tuple[int, str]] = []
    for idx, para in enumerate(paragraphs, start=1):
        p = para.strip()
        if not p or p.startswith("#"):
            continue
        if re.match(r"^(table|figure)\b", p, re.I):
            continue
        p = re.sub(r"^[-*+]\s+", "", p)
        p = re.sub(r"^\d+[.)]\s+", "", p)
        p = p.strip("|").strip()
        for s in SENTENCE_SPLIT.split(p):
            s = s.strip()
            if len(s) >= 40:
                out.append((idx, s))
    return out


def write_sentences_archive(citekey: str, src: Path, spans: dict,
                            lines: list[str], sources_dir: Path) -> Path:
    """Materialize a durable sentence inventory beside the PDM workdir.

    One line per sentence, grouped by section, with paragraph-level provenance
    as `<!-- para N -->` markers. This is the raw-material pool for cross-source
    synthesis (P2 move enrichment): it survives `--clean` because it is a
    deliberate asset, not an intermediate product.
    """
    sources_dir.mkdir(parents=True, exist_ok=True)
    archive = sources_dir / f"{citekey}.sentences.md"
    parts = [
        "---",
        "type: sentences-archive",
        f'citekey: "{citekey}"',
        f'source_md: "{src.resolve()}"',
        f"created: {date.today().isoformat()}",
        "note: >-",
        "  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；",
        "  任何产出必须过护栏 scripts/guard.py（单源 4-gram 重合 ≤50%）。",
        "---",
        "",
        f"# {citekey} 句子库存",
        "",
    ]
    for bucket in BUCKET_ORDER:
        sp = spans.get(bucket)
        if not sp:
            continue
        body = "\n".join(lines[sp["start"] - 1 : sp["end"]]).rstrip()
        sentences = extract_sentences(body)
        parts.append(f"## {bucket}")
        if not sentences:
            parts.append("_（本节约无 ≥40 字符句子）_")
            parts.append("")
            continue
        cur_para: int | None = None
        for para, sent in sentences:
            if para != cur_para:
                parts.append(f"<!-- para {para} -->")
                cur_para = para
            parts.append(sent)
        parts.append("")
    archive.write_text("\n".join(parts), encoding="utf-8")
    return archive


def main() -> int:
    ap = argparse.ArgumentParser(description="L0 preprocess: strip base64 + materialize section slices")
    ap.add_argument("source_md", help="path to paper-import full-text MD (read-only)")
    ap.add_argument("--citekey", default=None, help="PDM citekey (default: derived from filename)")
    ap.add_argument("--outdir", default=None,
                    help="PDM workdir (default: <DISTILL_WORK_ROOT or ~/.claude/distill-work>/<citekey>.pdm/"
                         " — outside the vault; use --outdir to keep it next to the paper)")
    ap.add_argument("--force", action="store_true", help="override a fresh PDM LOCK")
    ap.add_argument("--unlock", action="store_true", help="remove the PDM LOCK and exit")
    ap.add_argument("--clean", action="store_true",
                    help="remove the whole PDM workdir (implies --unlock) and exit")
    ap.add_argument("--keep-sentences", action="store_true",
                    help="write a durable sentence inventory to "
                         "story-blueprints/v4/rhetoric-moves/sources/<citekey>.sentences.md "
                         "(NOT deleted by --clean)")
    ap.add_argument("--sources-dir", default=None,
                    help="override the sentence-inventory root (default: "
                         "skills/story-blueprints/v4/rhetoric-moves/sources)")
    args = ap.parse_args()

    src = Path(args.source_md)
    citekey = args.citekey or (derive_citekey(src) if src.is_file() else None)
    if not citekey:
        print(f"ERROR: not a file: {src}", file=sys.stderr)
        return 2
    outdir = Path(args.outdir) if args.outdir else work_root() / f"{citekey}.pdm"

    lock = outdir / "LOCK"
    if args.clean:
        if not (outdir / "l0_manifest.json").is_file() and not lock.is_file():
            print(f"ERROR: {outdir} does not look like a PDM workdir — refusing to delete",
                  file=sys.stderr)
            return 2
        shutil.rmtree(outdir, ignore_errors=True)
        print(f"cleaned: {outdir}")
        return 0
    if args.unlock:
        lock.unlink(missing_ok=True)
        print(f"unlocked: {lock}")
        return 0
    if not src.is_file():
        print(f"ERROR: not a file: {src}", file=sys.stderr)
        return 2
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

    # structure classification (2026-08-20): not every paper is classic IMRaD.
    # econ/finance style often runs a long introduction (lit review + theory +
    # hypotheses embedded) straight into Data; flag it instead of forcing a
    # theory slice that does not exist.
    intro_words = len("\n".join(
        lines[spans["introduction"]["start"] - 1 : spans["introduction"]["end"]]
    ).split()) if "introduction" in spans else 0
    theory_heading = spans.get("theory", {}).get("heading", "")
    if "theory" in spans:
        structure_type = ("formal-model" if re.search(r"model", theory_heading, re.I)
                          else "classic-imrad")
    elif "introduction" in spans and intro_words > 1200:
        structure_type = "extended-intro"
    elif {"introduction", "methods", "results"} <= set(spans):
        structure_type = "classic-imrad"
    else:
        structure_type = "unknown"

    manifest = {
        "citekey": citekey,
        "source_md": str(src),
        "text_only_md": str(text_only),
        "raw_bytes": raw_bytes,
        "text_only_bytes": len(text.encode("utf-8")),
        "images_replaced": n_images,
        "structure_type": structure_type,
        "structure_note": (
            "long introduction without a separate theory section — theory/hypotheses "
            "likely embedded in the introduction slice; route theory distillation to "
            "sections/introduction.md with embedded=true"
            if structure_type == "extended-intro" else ""
        ),
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

    manifest["sentences_archive"] = None
    if args.keep_sentences:
        sources_dir = Path(args.sources_dir) if args.sources_dir else DEFAULT_SOURCES_DIR
        manifest["sentences_archive"] = str(
            write_sentences_archive(citekey, src, spans, lines, sources_dir)
        )

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
