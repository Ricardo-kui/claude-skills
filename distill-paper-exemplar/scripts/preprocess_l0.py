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

  --sweep (2026-08-29 v2, L4 final step, no source_md needed) removes the
  *cross-run* intermediates that per-paper --clean cannot reach:
    - every `__pycache__/` dir and `*.pyc` under the skills tree (bytecode
      regenerates on next import; keeps the skill tree clean)
    - leftover PDM workdirs that are fully consumed: a `<citekey>.pdm/` whose
      root yaml says `status: integrated`, or an orphan workdir (no root yaml)
      whose LOCK is older than 12h
    - pdm_tool rolling baks (`<citekey>.pdm.yaml.bak`): removed once their
      root is `integrated` or gone; a bak of a live record is the mutation
      safety net and stays (2026-09-14, quality-review P3)
  NEVER touched: `<citekey>.pdm.yaml` state records, the sentences archive,
  story-blueprints, and any workdir whose LOCK is fresh (< 12h — may be an
  active single-window run).

  --keep-sentences writes a durable sentence inventory to
    story-blueprints/v4/rhetoric-moves/sources/<citekey>.sentences.md
    (cross-source synthesis raw material for P2 move enrichment; NOT deleted
    by --clean — it is a deliberate asset, not an intermediate product).

The raw source MD is NEVER modified and must never be read by distill agents.
Section detection is heading-based and conservative: anything uncertain is
reported as "unknown" so the orchestrator can fall back to manual slicing.

SLICE-CHECK FALLBACK (2026-08-29, Layer 3): when detection comes back empty
or suspicious (any slice < 300 words, heading-level breaks), the full
`#`/`##`/`###` heading tree with 1-based line numbers and a ready-to-edit
slice_suggestions.yaml are printed/written in one pass — the orchestrator
confirms once and reruns with `--slices <suggestions.yaml>`; no per-section
sed surgery. Explicit `--slices` overrides replace auto-detection entirely.
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
    # `\bresults\b` catches mixed titles like Ball's "Empirical approach and
    # results"; `^empirical analysis`/`^empirics`/`^cross-sectional variations`
    # cover the MS/econ section-name family (Lu 2022 §4/§5 trap, 5th instance
    # of the missed-results class as of 2026-09-13).
    "results": [r"^results?\b", r"^findings?\b", r"^analys(e|i)s\b", r"\bresults\b",
                r"^empirical analysis", r"^empirics\b", r"^cross-sectional variations"],
    "discussion": [r"^discussion\b", r"^conclusions?\b", r"discussion and conclusion",
                   r"discussion\b", r"^extensions?\b", r"^concluding"],
}
BUCKET_ORDER = ["introduction", "theory", "methods", "results", "discussion"]

IMG_DATA_URI_MD = re.compile(r"!\[([^\]]*)\]\(\s*data:image/[^)\s]+[^)]*\)")
IMG_DATA_URI_HTML = re.compile(r'<img\b[^>]*\bsrc="data:image/[^"]*"[^>]*/?>', re.I)
HEADING = re.compile(r"^(#{1,3})\s+(.+?)\s*#*\s*$")
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")
MIN_SLICE_WORDS = 300

SKILLS_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_SOURCES_DIR = (
    SKILLS_ROOT / "story-blueprints" / "v4" / "rhetoric-moves" / "sources"
)

# files whose content defines distillation behavior; hashed into the manifest
# fingerprint so a re-distillation can tell whether prior entries were
# produced under the current protocol (T2-8, pi-prompt-diet DISTILLER_VERSION)
DISTILLER_FILES = (
    "distill-paper-exemplar/SKILL.md",
    "distill-paper-exemplar/references/l1-subagent-protocol.md",
    "distill-paper-exemplar/references/band-vocab.md",
    "distill-paper-exemplar/references/anchor-rules.md",
    "distill-paper-exemplar/scripts/corpus_query.py",
    "distill-paper-exemplar/scripts/corpus_precheck.py",
    "distill-paper-exemplar/scripts/corpus_writeback.py",
    "distill-paper-exemplar/scripts/verify_writeback.py",
    "distill-paper-exemplar/scripts/check_contract_source.py",
    "distill-paper-exemplar/scripts/preprocess_l0.py",
    "distill-agents/agents/distill-methods.md",
    "distill-agents/agents/distill-introduction.md",
    "distill-agents/agents/distill-theory.md",
    "distill-agents/agents/distill-results.md",
    "distill-introduction-exemplar/SKILL.md",
    "distill-theory-exemplar/SKILL.md",
    "distill-methods-exemplar/SKILL.md",
    "distill-results-exemplar/SKILL.md",
)


def distiller_fingerprint() -> dict:
    import hashlib

    h = hashlib.sha256()
    n = 0
    for rel in DISTILLER_FILES:
        p = SKILLS_ROOT / rel
        if not p.is_file():
            continue
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(p.read_bytes())
        h.update(b"\0")
        n += 1
    return {"version": h.hexdigest()[:12], "files": n}


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


def apply_manual_slices(path: Path, lines: list[str], auto: dict) -> dict:
    """Apply orchestrator-confirmed slice overrides: {bucket: {start, end}}
    (1-based inclusive, same convention as the manifest) or {bucket: [start, end]}.
    Replaces auto-detection wholesale; validation errors exit 2."""
    import yaml

    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict) or not spec:
        print(f"ERROR: --slices {path} 不是非空映射（bucket: {{start, end}}）", file=sys.stderr)
        sys.exit(2)
    errs = []
    spans: dict[str, dict] = {}
    for bucket, rng in spec.items():
        if bucket not in BUCKET_ORDER:
            errs.append(f"未知 bucket {bucket!r}（应为 {', '.join(BUCKET_ORDER)}）")
            continue
        if isinstance(rng, dict):
            start, end = rng.get("start"), rng.get("end")
        elif isinstance(rng, (list, tuple)) and len(rng) == 2:
            start, end = rng
        else:
            errs.append(f"{bucket}: 区间格式不识别 {rng!r}")
            continue
        if not (isinstance(start, int) and isinstance(end, int)):
            errs.append(f"{bucket}: start/end 必须是整数行号（got {start!r}, {end!r}）")
            continue
        if not (1 <= start <= end <= len(lines)):
            errs.append(f"{bucket}: 区间越界 {start}-{end}（全文共 {len(lines)} 行）")
            continue
        spans[bucket] = {"start": start, "end": end,
                         "heading": f"(manual slices {start}-{end})"}
    if errs:
        print("ERROR: --slices 校验失败:\n  " + "\n  ".join(errs), file=sys.stderr)
        sys.exit(2)
    return spans


def heading_level_breaks(lines: list[str]) -> list[str]:
    """Consecutive-heading level jumps of >=2 (e.g. `#` straight to `###`) —
    typical OCR/转换 noise that makes heading-based slicing unreliable."""
    breaks, prev = [], None
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if not m:
            continue
        lv = len(m.group(1))
        if prev is not None and lv - prev >= 2:
            breaks.append(f"L{prev}->L{lv}@行{i + 1}:{m.group(2)[:40]!r}")
        prev = lv
    return breaks


def slice_check(spans: dict, lines: list[str]) -> list[str]:
    """Suspicion reasons for the detected slices. Non-empty => print the full
    heading tree + write slice_suggestions.yaml for one-pass confirmation."""
    reasons: list[str] = []
    unknown = [b for b in BUCKET_ORDER if b not in spans]
    if unknown:
        reasons.append("未检出节: " + ", ".join(unknown))
    for bucket in BUCKET_ORDER:
        sp = spans.get(bucket)
        if not sp:
            continue
        words = len("\n".join(lines[sp["start"] - 1: sp["end"]]).split())
        if words < MIN_SLICE_WORDS:
            reasons.append(f"{bucket} 切片仅 {words} 词 (<{MIN_SLICE_WORDS})——可能误切/漏切")
    breaks = heading_level_breaks(lines)
    if breaks:
        reasons.append("标题层级断裂: " + "; ".join(breaks[:3])
                       + (f" 等{len(breaks)}处" if len(breaks) > 3 else ""))
    return reasons


def heading_tree(lines: list[str], spans: dict) -> list[str]:
    """Every #-level heading with 1-based line number, annotated with its
    auto-detected bucket — the confirmation surface for manual slicing."""
    out = []
    for i, ln in enumerate(lines):
        m = HEADING.match(ln)
        if m:
            b = classify_heading(m.group(2))
            out.append(f"  {i + 1:>5}: {'#' * len(m.group(1))} {m.group(2)}"
                       + (f"  [->{b}]" if b else ""))
    return out


def slice_suggestions_yaml(spans: dict) -> str:
    """Ready-to-edit --slices input: detected spans as defaults, undetected
    buckets as TODO comments."""
    parts = [
        "# L0 slice suggestions — 编辑 start/end（1-based 闭区间），删掉不需要的 bucket，",
        "# 然后重跑: python preprocess_l0.py <全文MD> --citekey <ck> --slices <本文件>",
        "# 各标题所在行号见运行时打印的 heading tree。",
        "",
    ]
    for bucket in BUCKET_ORDER:
        sp = spans.get(bucket)
        if sp:
            parts.append(f'{bucket}: {{start: {sp["start"]}, end: {sp["end"]}}}'
                         f'  # {sp["heading"][:60]}')
        else:
            parts.append(f"# {bucket}: 未检出——从标题树选定起止行后取消本行注释并填行号")
    return "\n".join(parts) + "\n"


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
        "  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。",
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


def sweep(work_root_dir: Path, skills_root: Path) -> int:
    """Cross-run intermediate cleanup (L4 final step). Deterministic, no LLM.

    Returns process exit code. Never touches state records, the sentences
    archive, story-blueprints, or workdirs with a fresh (<12h) LOCK.
    Rolling pdm_tool `<root>.pdm.yaml.bak` files are removed once their root
    is integrated or gone; a bak of a live (un-integrated) record stays — it
    is the mutation safety net."""
    import time
    import yaml

    removed = kept = 0
    # 1. bytecode caches anywhere in the skills tree
    for cache in skills_root.rglob("__pycache__"):
        shutil.rmtree(cache, ignore_errors=True)
        removed += 1
    for pyc in skills_root.rglob("*.pyc"):
        pyc.unlink(missing_ok=True)
        removed += 1

    # 2. fully-consumed / orphaned PDM workdirs
    for wd in sorted(work_root_dir.glob("*.pdm")):
        if not wd.is_dir():
            continue
        root_yaml = work_root_dir / (wd.name + ".yaml")
        lock = wd / "LOCK"
        fresh_lock = lock.is_file() and (time.time() - lock.stat().st_mtime) / 3600 < 12
        if fresh_lock:
            kept += 1
            print(f"KEEP (fresh LOCK, active run?): {wd.name}")
            continue
        status = None
        if root_yaml.is_file():
            try:
                status = (yaml.safe_load(root_yaml.read_text(encoding="utf-8"))
                          or {}).get("status")
            except yaml.YAMLError:
                status = None
        if status == "integrated" or not root_yaml.is_file():
            age_h = ((time.time() - lock.stat().st_mtime) / 3600) if lock.is_file() else None
            tag = "integrated" if status == "integrated" else f"orphan (no root yaml, lock {age_h:.1f}h)" if age_h else "orphan (no root yaml, no lock)"
            shutil.rmtree(wd, ignore_errors=True)
            removed += 1
            print(f"RM ({tag}): {wd.name}")
        else:
            kept += 1
            print(f"KEEP (status: {status}): {wd.name}")

    # 3. rolling pdm_tool baks: delete when the run is over (integrated) or
    #    the root is gone; keep while the record can still be mutated
    for bak in sorted(work_root_dir.glob("*.pdm.yaml.bak")):
        root_yaml = work_root_dir / bak.name[:-len(".bak")]
        try:
            status = ((yaml.safe_load(root_yaml.read_text(encoding="utf-8"))
                       or {}).get("status")) if root_yaml.is_file() else None
        except yaml.YAMLError:
            status = None
        if status == "integrated" or not root_yaml.is_file():
            tag = "integrated bak" if status == "integrated" else "orphan bak (no root yaml)"
            bak.unlink(missing_ok=True)
            removed += 1
            print(f"RM ({tag}): {bak.name}")
        else:
            print(f"KEEP (bak of live record, status: {status}): {bak.name}")

    print(f"sweep done: {removed} item(s) removed, {kept} workdir(s) kept, "
          f"state records & sentences archive untouched")
    return 0


def prior_traces(citekey: str, source_text: str) -> dict:
    """Gap-fill detection (2026-09-12). A pre-existing story card or registry
    trace means the paper enters gap-fill semantics (auto-write default),
    not first-time batch review. Matching is case-insensitive with hyphen /
    no-separator citekey variants plus the frontmatter title prefix — the
    ridge2013 card was missed by a case-sensitive grep (2026-09-12)."""
    ck = citekey.lower()
    variants = {ck, ck.replace("_", "-"), ck.replace("_", "")}
    m = re.search(r'^title:\s*"?(.+?)"?\s*$', source_text, re.M | re.I)
    title_norm = re.sub(r"[^a-z0-9 ]", "", m.group(1).lower())[:60] if m else None
    out = {"story_cards": [], "registries": [], "corpus_wb_markers": 0}
    bp = SKILLS_ROOT / "story-blueprints" / "v4" / "blueprints"
    if bp.is_dir():
        for f in bp.glob("*.md"):
            t = f.read_text(encoding="utf-8", errors="ignore").lower()
            if any(v in t for v in variants) or (title_norm and title_norm in t):
                out["story_cards"].append(f.name)
    for reg in ("write-introduction/corpus/_evidence_registry.yaml",
                "write-theory/corpus/_evidence_registry.yaml",
                "write-methods/corpus/_evidence_registry.yaml",
                "write-results/corpus/_evidence_registry.yaml"):
        p = SKILLS_ROOT / reg
        if p.is_file():
            t = p.read_text(encoding="utf-8", errors="ignore").lower()
            flat = t.replace("_", "").replace("-", "")
            if any(v.replace("_", "").replace("-", "") in flat for v in variants):
                out["registries"].append(reg)
    # Marker format is `<!-- wb:<paper>:<item> -->` — anchor at the paper:item
    # colon. The old pattern (wb: + citekey first segment anywhere) matched
    # "lu" INSIDE other papers' citekeys (fai**lu**re / inf**lu**ence /
    # va**l**ue) and reported 74 bogus traces on the 2026-09-13 Lu run, which
    # would have misrouted a first-time distill into gap-fill auto-write.
    # Precision-over-recall ruling (2026-09-13): legacy short-key markers
    # (e.g. `wb:gulati2005-adaptation-vertical:` for an underscore citekey)
    # are NOT matched — a false NEGATIVE merely routes a re-distill through
    # batch review (safe; story-card/registry checks still cover it), while a
    # false POSITIVE silently skips gate ① (dangerous).
    ck_variants = sorted({ck, ck.replace("_", "-"), ck.replace("_", "")},
                         key=len, reverse=True)
    pat = re.compile("wb:(?:" + "|".join(re.escape(v) for v in ck_variants) + "):",
                     re.I)
    for cdir in ("write-introduction/corpus", "write-theory/corpus",
                 "write-methods/corpus", "write-results/corpus"):
        d = SKILLS_ROOT / cdir
        if d.is_dir():
            for f in d.rglob("*.md"):
                out["corpus_wb_markers"] += len(pat.findall(
                    f.read_text(encoding="utf-8", errors="ignore")))
    return out


def parse_frontmatter(src: Path) -> dict:
    """Light frontmatter extraction from the paper-import MD (title/Author/
    Journal/Year/parser). YAML-first, regex fallback — L0 must not fail on
    frontmatter quirks."""
    try:
        text = src.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not m:
        return {}
    block = m.group(1)
    try:
        import yaml  # PyYAML is a dependency of the corpus scripts already
        data = yaml.safe_load(block)
        if isinstance(data, dict):
            return data
    except Exception:
        pass
    out = {}
    for key in ("title", "Journal", "journal", "Year", "year", "parser"):
        km = re.search(rf"^{key}:\s*\"?([^\"\n]+)\"?\s*$", block, re.M | re.I)
        if km:
            out[key.lower()] = km.group(1).strip()
    authors = re.findall(r"^\s*-\s+(.+)$", block, re.M)
    if authors:
        out["authors"] = [a.strip() for a in authors]
    return out


def scaffold_pdm_root(citekey: str, src: Path, manifest: dict,
                      outdir: Path) -> Path:
    """Create the PDM root yaml (`<citekey>.pdm.yaml`) next to the workdir.

    The schema (pdm-schema.md) previously had to be hand-written by the main
    loop on every run — 4th repetition during the 2026-09-13 Lu run. This
    scaffolds the same skeleton deterministically from the L0 manifest +
    source frontmatter. Create-if-missing only: an existing root is NEVER
    touched (main loop owns the state record after creation; re-slice runs
    keep their merged status/identity)."""
    root = outdir.parent / f"{citekey}.pdm.yaml"
    if root.is_file():
        existing = root.read_text(encoding="utf-8", errors="replace")
        st = re.search(r"^status:\s*(\S+)", existing, re.M)
        print(f"PDM-ROOT: exists ({st.group(1) if st else 'unknown status'}) "
              f"— left untouched: {root}")
        return root
    fm = parse_frontmatter(src)
    title = fm.get("title") or ""
    journal = fm.get("journal") or fm.get("Journal") or ""
    authors = fm.get("authors") or fm.get("Author") or fm.get("Authors") or []
    year = fm.get("year") or fm.get("Year")
    ingestion = f"paper-import ({fm.get('parser') or 'parser-unrecorded'})"
    slices = manifest["section_slices"]
    slices_yaml = "\n".join(
        f'    {b}: "{citekey}.pdm/sections/{b}.md"' for b in BUCKET_ORDER
        if b in slices)
    fp = manifest["distiller_fingerprint"]

    def q(s: str) -> str:
        # JSON string escapes are valid YAML double-quoted scalars
        return json.dumps(s, ensure_ascii=False)

    content = f"""# PDM root — auto-scaffolded by preprocess_l0.py (create-if-missing;
# main loop owns this file afterwards: identity/status/writeback merges).
pdm_version: 1.0
paper_id: {q(citekey)}
title: {q(title)}
authors: {json.dumps([str(a) for a in authors], ensure_ascii=False)}
year: {year if isinstance(year, int) else q(str(year)) if year else 'null'}
journal: {q(journal)}

source_provenance:
  fulltext_md: {q(str(src))}
  text_only_md: {q(f"{citekey}.pdm/fulltext.text-only.md")}
  zotero_ref: ""
  ingestion: {q(ingestion)}
  structure_type: {q(manifest.get("structure_type", "unknown"))}
  section_slices:
{slices_yaml}

status: manifest

distill_track:
  introduction:
    skill: distill-introduction-exemplar
    status: pending
    section_json: "sections/introduction.json"
    feedback: "feedback/introduction.feedback.yaml"
    identity: {{gap_type: "", contribution_dimension: ""}}
    writeback: {{target: "write-introduction/corpus/", gate: awaiting_confirm, items: []}}
  theory:
    skill: distill-theory-exemplar
    status: pending
    section_json: "sections/theory.json"
    feedback: "feedback/theory.feedback.yaml"
    identity: {{theory_building_type: ""}}
    writeback: {{target: "write-theory/corpus/", gate: awaiting_confirm, items: []}}
  methods:
    skill: distill-methods-exemplar
    status: pending
    section_json: "sections/methods.json"
    feedback: "feedback/methods.feedback.yaml"
    identity: {{design_family: ""}}
    writeback: {{target: "write-methods/corpus/", gate: awaiting_confirm, items: []}}
  results:
    skill: distill-results-exemplar
    status: pending
    section_json: "sections/results.json"
    feedback: "feedback/results.feedback.yaml"
    identity: {{estimator_family: ""}}
    writeback: {{target: "write-results/corpus/", gate: awaiting_confirm, items: []}}

cross_section_identity:
  gap_type: ""
  theory_building_type: ""
  design_family: ""
  estimator_family: ""
  coherence: ""
  flags: []

story_track:
  skill: distill-story-exemplar
  status: pending
  card_path: ""
  validated: false
  catalog_rebuilt: false
  fed_flags: false

feedback_ledger:
  persisted: []
  missing: []
  note: ""

distiller_fingerprint:
  version: {q(fp["version"])}
  files: {fp["files"]}
"""
    root.write_text(content, encoding="utf-8")
    print(f"PDM-ROOT: scaffolded {root}")
    return root


def main() -> int:
    ap = argparse.ArgumentParser(description="L0 preprocess: strip base64 + materialize section slices")
    ap.add_argument("source_md", nargs="?", default=None,
                    help="path to paper-import full-text MD (read-only); "
                         "optional when --sweep")
    ap.add_argument("--citekey", default=None, help="PDM citekey (default: derived from filename)")
    ap.add_argument("--outdir", default=None,
                    help="PDM workdir (default: <DISTILL_WORK_ROOT or ~/.claude/distill-work>/<citekey>.pdm/"
                         " — outside the vault; use --outdir to keep it next to the paper)")
    ap.add_argument("--force", action="store_true", help="override a fresh PDM LOCK")
    ap.add_argument("--slices", default=None, metavar="SLICES_YAML",
                    help="explicit slice overrides {bucket: {start, end}} (1-based "
                         "inclusive) — replaces auto-detection; use the generated "
                         "slice_suggestions.yaml after one-pass confirmation")
    ap.add_argument("--unlock", action="store_true", help="remove the PDM LOCK and exit")
    ap.add_argument("--clean", action="store_true",
                    help="remove the whole PDM workdir (implies --unlock) and exit")
    ap.add_argument("--keep-sentences", action="store_true",
                    help="write a durable sentence inventory to "
                         "story-blueprints/v4/rhetoric-moves/sources/<citekey>.sentences.md "
                         "(NOT deleted by --clean)")
    ap.add_argument("--sweep", action="store_true",
                    help="L4 final step: remove cross-run intermediates "
                         "(__pycache__ under the skills tree, fully-consumed/"
                         "orphaned PDM workdirs). No source_md needed; never "
                         "touches state records, sentences archive, or fresh-"
                         "LOCK workdirs")
    ap.add_argument("--sources-dir", default=None,
                    help="override the sentence-inventory root (default: "
                         "skills/story-blueprints/v4/rhetoric-moves/sources)")
    ap.add_argument("--min-compression-ratio", type=float, default=1.5,
                    help="overall raw/text-only byte ratio below which the "
                         "conversion is reported as ineffective (default 1.5)")
    args = ap.parse_args()

    if args.sweep:
        return sweep(work_root(), SKILLS_ROOT)

    src = Path(args.source_md) if args.source_md else None
    citekey = args.citekey or (derive_citekey(src) if src and src.is_file() else None)
    if not citekey or src is None:
        print("ERROR: --sweep 不需要 source_md；其他模式必须提供论文 MD 路径",
              file=sys.stderr)
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
    text_bytes_total = len(text.encode("utf-8"))
    # per-slice compression stats need the pre-strip text; line spans only
    # align when stripping removed no newlines (data URIs are single-line)
    raw_lines = raw.split("\n")
    lines_aligned = len(raw_lines) == len(lines)

    text_only = outdir / "fulltext.text-only.md"
    text_only.write_text(text, encoding="utf-8")

    spans = slice_sections(lines)
    slice_source = "auto-detect"
    if args.slices:
        spans = apply_manual_slices(Path(args.slices), lines, spans)
        slice_source = "manual-slices"

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
        "text_only_bytes": text_bytes_total,
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
        entry = {
            "path": str(out),
            "start_line": sp["start"],
            "end_line": sp["end"],
            "words": len(body.split()),
            "heading": sp["heading"],
        }
        if lines_aligned:
            raw_slice = "\n".join(raw_lines[sp["start"] - 1 : sp["end"]])
            raw_slice_bytes = len(raw_slice.encode("utf-8"))
            body_bytes = len(body.encode("utf-8"))
            entry["raw_bytes"] = raw_slice_bytes
            entry["text_bytes"] = body_bytes
            entry["compression_ratio"] = round(raw_slice_bytes / max(1, body_bytes), 2)
        manifest["section_slices"][bucket] = entry

    # compression savings observability (T2-6, 2026-09-12; pi-distill's
    # ineffective-compression spirit): surface when the text-only conversion
    # bought almost nothing instead of silently claiming savings.
    overall_ratio = round(raw_bytes / max(1, text_bytes_total), 2)
    savings_warning = overall_ratio < args.min_compression_ratio
    manifest["compression"] = {
        "ratio": overall_ratio,
        "min_ratio": args.min_compression_ratio,
        "savings_warning": savings_warning,
        "per_slice_aligned": lines_aligned,
    }
    manifest["distiller_fingerprint"] = distiller_fingerprint()
    manifest["prior_traces"] = prior_traces(citekey, raw)
    if any(manifest["prior_traces"].get(k) for k in ("story_cards", "registries")) \
            or manifest["prior_traces"]["corpus_wb_markers"]:
        print("DEDUP: prior traces found — gap-fill semantics (auto-write default) "
              "per protocol; NOT a first-time distill:")
        for card in manifest["prior_traces"]["story_cards"]:
            print(f"  story card: {card}")
        for reg in manifest["prior_traces"]["registries"]:
            print(f"  registry: {reg}")
        print(f"  corpus wb markers: {manifest['prior_traces']['corpus_wb_markers']}")
    if savings_warning:
        print(
            f"COMPRESSION: ineffective ({overall_ratio}x < "
            f"{args.min_compression_ratio}x) — source carried little base64 "
            "weight; text-only conversion bought almost nothing"
        )
    print(f"DISTILLER: {manifest['distiller_fingerprint']['version']} "
          f"({manifest['distiller_fingerprint']['files']} files)")

    manifest["sentences_archive"] = None
    if args.keep_sentences:
        sources_dir = Path(args.sources_dir) if args.sources_dir else DEFAULT_SOURCES_DIR
        manifest["sentences_archive"] = str(
            write_sentences_archive(citekey, src, spans, lines, sources_dir)
        )

    check_reasons = slice_check(spans, lines)
    manifest["slice_source"] = slice_source
    manifest["slice_check"] = {"suspicious": bool(check_reasons),
                               "min_words": MIN_SLICE_WORDS,
                               "reasons": check_reasons}
    if check_reasons and slice_source == "auto-detect":
        sug = outdir / "slice_suggestions.yaml"
        sug.write_text(slice_suggestions_yaml(spans), encoding="utf-8")
        manifest["slice_check"]["suggestions"] = str(sug)
        print("SLICE-CHECK: SUSPICIOUS — " + "; ".join(check_reasons))
        print("Heading tree（行号: 标题 [->自动判定节]）:")
        print("\n".join(heading_tree(lines, spans)))
        print(f"切片建议已写入 {sug} —— 一次确认后重跑: --slices {sug}")

    (outdir / "l0_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    scaffold_pdm_root(citekey, src, manifest, outdir)
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
