"""Phase 4.5 utility: update corpus and registry from distill output.

Usage:
    python _update_registry.py <corpus_enrichment.yaml>
    # or pipe from stdin:
    cat corpus_enrichment.yaml | python _update_registry.py --stdin

This script performs TWO automated updates:
1. **Registry update** — _evidence_registry.yaml (paper counts, statuses, failures)
2. **Corpus skeleton update** — appends validated skeletons to the "累积变体"
   section of the target design-type corpus file.

No manual editing of corpus files needed for routine distill output.
"""

import sys
import yaml
import re
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
CORPUS_DIR = (
    Path(__file__).parent.parent
    / "write-methods"
    / "econometric-models"
)
REGISTRY_PATH = CORPUS_DIR / "_evidence_registry.yaml"

# Paper-to-design-type mapping (keep in sync with corpus INDEX.md)
PAPER_DESIGN_TYPES = {
    'darby2026': '面板数据-OLS',
    'darby2025': '面板数据-OLS',
    'eilert2017': '面板数据-OLS',
    'darby2023': '面板数据-OLS',
    'darby2024': '生存分析',
    'wowak2025': 'IV-2SLS',
    'wu2025': '自然实验-DiD',
    'zhao_ding2022': '文本构念测量',
    'shi2021': '实验',
    'vadakkepatt2022': '实验',
}

SLOT_KEY = {
    'M1': 'M1', 'M2': 'M2', 'M3': 'M3', 'M4': 'M4', 'M5': 'M5',
    'M6': 'M6', 'M7': 'M7', 'M8': 'M8', 'M9': 'M9', 'M10': 'M10',
}


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------
def load_yaml(path=None, stdin_marker='--stdin'):
    """Load YAML from file or stdin."""
    if path and path != stdin_marker:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    # If the text contains a named block, extract it
    if 'corpus_enrichment:' in text:
        text = text[text.index('corpus_enrichment:'):]

    return yaml.safe_load(text)


def save_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)


def parse_frontmatter(text):
    """Extract YAML frontmatter and body from a markdown file."""
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            fm = yaml.safe_load(parts[1])
            body = parts[2]
            return fm, body
    return {}, text


def serialize_frontmatter(fm, body):
    """Reconstruct markdown with YAML frontmatter."""
    fm_text = yaml.dump(fm, allow_unicode=True, default_flow_style=False,
                        sort_keys=False, width=120)
    return f"---\n{fm_text}---\n{body}"


# ---------------------------------------------------------------------------
# Registry logic (original, preserved)
# ---------------------------------------------------------------------------
def load_registry():
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_registry(reg):
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(reg, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)


def get_journal(paper_str):
    if '(' in paper_str:
        return paper_str.split('(')[-1].rstrip(')').strip()
    return ''


def recalc_entry(entry):
    papers = sorted(set(entry.get('papers', [])))
    entry['papers'] = papers
    entry['paper_count'] = len(papers)
    journals = {get_journal(p) for p in papers if get_journal(p)}

    if entry['paper_count'] >= 5 and len(journals) >= 2:
        entry['status'] = 'ROBUST'
    elif entry['paper_count'] >= 3:
        entry['status'] = 'VERIFIED'
    else:
        entry['status'] = 'EMERGING'


def apply_registry_updates(reg, enrichment):
    updates = enrichment.get('evidence_updates', [])
    if not updates:
        print("No evidence_updates found in enrichment block.")
        return reg

    section = reg['evidence']['by_design_type']

    for upd in updates:
        design_type = upd.get('design_type', '')
        slot = upd.get('slot', '')
        action = upd.get('action')

        if not design_type:
            print(f"  SKIP: missing design_type in {upd}")
            continue

        if design_type not in section:
            if action == 'create_new':
                section[design_type] = {
                    'paper_count': 0, 'papers': [],
                    'status': 'EMERGING',
                    'slots_covered': [],
                    'common_failures': [],
                    'validation_history': {
                        'revise': 0, 'reject': 0,
                        'last_critique': None,
                        'common_revise_reasons': [],
                    },
                }
            else:
                print(f"  SKIP: design_type '{design_type}' not found in registry")
                continue

        entry = section[design_type]

        if action == 'append_papers':
            new_papers = upd.get('new_papers', [])
            existing = set(entry.get('papers', []))
            added = 0
            for p in new_papers:
                if p and p.strip() and p not in existing:
                    existing.add(p)
                    added += 1
            entry['papers'] = sorted(existing)
            if slot and slot not in entry.get('slots_covered', []):
                entry.setdefault('slots_covered', []).append(slot)
            recalc_entry(entry)
            print(f"  REGISTRY {design_type}: +{added} papers -> {entry['paper_count']}p, {entry['status']}")

        elif action == 'update_status':
            new_status = upd.get('new_status')
            if new_status:
                entry['status'] = new_status
            reason = upd.get('reason', '')
            recalc_entry(entry)
            print(f"  REGISTRY {design_type}: status -> {entry['status']} ({reason})")

        elif action == 'create_new':
            new_papers = upd.get('new_papers', [])
            entry['papers'] = sorted(set(new_papers))
            if slot and slot not in entry.get('slots_covered', []):
                entry.setdefault('slots_covered', []).append(slot)
            recalc_entry(entry)
            print(f"  REGISTRY {design_type}: CREATED {entry['paper_count']}p, {entry['status']}")

    for ap in enrichment.get('anti_pattern_updates', []):
        target_dt = ap.get('target_design_type', '')
        pattern = ap.get('pattern', '')
        if target_dt and pattern:
            dt_entry = section.get(target_dt, {})
            if pattern not in dt_entry.get('common_failures', []):
                dt_entry.setdefault('common_failures', []).append(pattern)
                print(f"  REGISTRY {target_dt}: +common_failure: {pattern[:80]}...")

    reg['meta']['last_updated'] = enrichment.get('last_updated', datetime.now().strftime('%Y-%m-%d'))
    reg['meta']['batches_processed'] = reg['meta'].get('batches_processed', 0) + 1

    return reg


# ---------------------------------------------------------------------------
# NEW: Corpus skeleton append logic
# ---------------------------------------------------------------------------
def append_skeleton_to_corpus(update):
    """
    Append a validated skeleton to the target corpus file's 累积变体 section.

    Expected update fields (in addition to registry fields):
      - target: path relative to CORPUS_DIR, e.g. "econometric-models/生存分析.md"
      - design_type: e.g. "生存分析"
      - slot: e.g. "M7"
      - action: "append_skeleton"  (distinguishes from registry-only actions)
      - skeleton: the skeleton text itself (string)
      - skeleton_meta:
          variant_name: "AFT 分布选择"
          source_papers: ["Zhou2017 (ASQ)"]
          validation_status: "VALIDATED"
          transferability: "high"
          note: "optional explanation"
    """
    target = update.get('target', '')
    skeleton_text = update.get('skeleton', '').strip()
    slot = update.get('slot', '')
    meta = update.get('skeleton_meta', {})

    if not target or not skeleton_text:
        print(f"  CORPUS SKIP: missing target or skeleton in update")
        return False

    # Resolve file path
    # target may be "econometric-models/生存分析.md" or just "生存分析.md"
    # (also tolerate the legacy "academic-writing-corpus/" prefix from older
    # enrichment blocks written before the corpus was renamed)
    target_name = target
    for prefix in ('econometric-models/', 'academic-writing-corpus/'):
        if target_name.startswith(prefix):
            target_name = target_name[len(prefix):]
            break

    target_path = CORPUS_DIR / target_name
    if not target_path.exists():
        print(f"  CORPUS SKIP: target file not found: {target_path}")
        return False

    # Read existing file
    original_text = target_path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(original_text)

    # Build variant block
    variant_name = meta.get('variant_name', f"Distilled variant ({datetime.now().strftime('%Y-%m-%d')})")
    source_papers = meta.get('source_papers', [])
    validation_status = meta.get('validation_status', 'VALIDATED')
    transferability = meta.get('transferability', 'medium')
    note = meta.get('note', '')
    # 原始句锚点（verbatim anchor）：来源论文原句，风格参照用；空则不渲染该行（兼容旧指令）
    anchor = str(update.get('verbatim_anchor', '') or meta.get('verbatim_anchor', '') or '').strip()

    anchor_line = f"**原始句锚点**: {anchor}\n" if anchor else ""
    variant_block = f"""\n### 变体: {variant_name}
**验证状态**: {validation_status}
**来源论文**: {', '.join(source_papers) if source_papers else '待补充'}
**可迁移性**: {transferability}
**写入日期**: {datetime.now().strftime('%Y-%m-%d')}
**槽位**: {slot}
{anchor_line}**骨架**:
```text
{skeleton_text}
```
"""
    if note:
        variant_block += f"**备注**: {note}\n"

    # Append to 累积变体 section, or create it if missing
    if '## 累积变体' in body:
        body = body.rstrip() + '\n' + variant_block
    else:
        body = body.rstrip() + '\n\n## 累积变体\n' + variant_block

    # Update frontmatter
    current_count = fm.get('variants_count', 0)
    if isinstance(current_count, int):
        fm['variants_count'] = current_count + 1
    fm['updated'] = datetime.now().strftime('%Y-%m-%d')
    # Merge source papers
    existing_sources = set(fm.get('source_papers', []))
    for sp in source_papers:
        if sp:
            existing_sources.add(sp)
    fm['source_papers'] = sorted(existing_sources)

    # Write back
    new_text = serialize_frontmatter(fm, body)
    target_path.write_text(new_text, encoding='utf-8')
    print(f"  CORPUS {target_name}: +1 skeleton variant (now {fm['variants_count']} total)")
    return True


def apply_corpus_updates(enrichment):
    """Process evidence_updates that carry skeleton payloads."""
    updates = enrichment.get('evidence_updates', [])
    if not updates:
        return 0

    appended = 0
    for upd in updates:
        action = upd.get('action', '')
        has_skeleton = bool(upd.get('skeleton', '').strip())

        # Append skeleton if:
        #   action == "append_skeleton"  (explicit)
        #   OR action == "create_new" AND skeleton text is present
        if action == 'append_skeleton' or (has_skeleton and action in ('create_new',)):
            if append_skeleton_to_corpus(upd):
                appended += 1

    return appended


# ---------------------------------------------------------------------------
# Usage recording (Skill-SP frontier curriculum port)
# ---------------------------------------------------------------------------
def apply_critique_updates(reg, critique_updates):
    """Record user critiques of write-methods output into per-design-type validation_history.

    Each update: {design_type: str, verdict: 'revise'|'reject', reason: str, date: 'YYYY-MM-DD'}
    Signals per registry meta.usage_stats_schema (critique-driven, no pruning):
      gap: slots_covered 缺口（静态，不依赖登记）
      critique_heavy: revise + reject >= 2 → 精炼优先（REPLACE/EXTEND 候选）
      quiet: 无批评 → 正常蒸馏
    """
    section = reg['evidence']['by_design_type']
    MAX_REASONS = 8
    if not critique_updates:
        print("  No critique_updates found.")
        return

    for upd in critique_updates:
        dt = str(upd.get('design_type', '')).strip()
        verdict = str(upd.get('verdict', '')).strip().lower()
        reason = str(upd.get('reason', '') or '').strip()
        date = str(upd.get('date', '') or '').strip() or datetime.now().strftime('%Y-%m-%d')
        if dt not in section:
            print(f"  SKIP: design_type '{dt}' not in registry")
            continue
        if verdict not in ('revise', 'reject'):
            print(f"  SKIP: verdict '{verdict}' invalid (revise/reject)")
            continue

        vh = section[dt].setdefault('validation_history', {
            'revise': 0, 'reject': 0, 'last_critique': None, 'common_revise_reasons': [],
        })
        vh[verdict] = int(vh.get(verdict, 0)) + 1
        vh['last_critique'] = date
        if reason:
            reasons = list(vh.get('common_revise_reasons', []))
            if reason not in reasons:
                reasons.insert(0, reason)
                vh['common_revise_reasons'] = reasons[:MAX_REASONS]

        total = vh['revise'] + vh['reject']
        signal = 'critique_heavy' if total >= 2 else 'quiet'
        print(f"  CRITIQUE {dt}: {verdict} ({date}) -> revise={vh['revise']}, reject={vh['reject']} [{signal}]")

    reg['meta']['last_updated'] = datetime.now().strftime('%Y-%m-%d')


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    if '--record-critique' in sys.argv:
        try:
            critique_path = sys.argv[sys.argv.index('--record-critique') + 1]
        except IndexError:
            print("用法: python _update_registry.py --record-critique <critiques.yaml>")
            sys.exit(1)
        print("=" * 60)
        print("Critique Recorder (critique-driven stats)")
        print("=" * 60)
        critiques = load_yaml(critique_path)
        if isinstance(critiques, dict) and 'critique_updates' in critiques:
            critiques = critiques['critique_updates']
        reg = load_registry()
        apply_critique_updates(reg, critiques)
        save_registry(reg)
        print(f"Registry updated: {REGISTRY_PATH}")
        print("Done.")
        return

    if len(sys.argv) > 1 and sys.argv[1] not in ('--stdin', '-h', '--help'):
        enrichment = load_yaml(sys.argv[1])
    elif '--stdin' in sys.argv or len(sys.argv) == 1:
        enrichment = load_yaml(stdin_marker='--stdin')
    elif sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return

    # Unwrap top-level key if present
    if isinstance(enrichment, dict) and 'corpus_enrichment' in enrichment:
        enrichment = enrichment['corpus_enrichment']

    print("=" * 60)
    print("Corpus & Registry Updater (Phase 4.5)")
    print("=" * 60)

    # 1. Update registry
    print("\n[1/2] Updating evidence registry...")
    reg = load_registry()
    reg = apply_registry_updates(reg, enrichment)
    save_registry(reg)

    # 2. Update corpus files (NEW)
    print("\n[2/2] Updating corpus skeleton files...")
    appended = apply_corpus_updates(enrichment)
    if appended == 0:
        print("  No skeleton updates to apply (only registry was updated).")
    else:
        print(f"  Appended {appended} skeleton variant(s) to corpus files.")

    print("\n" + "=" * 60)
    print(f"Registry updated: {REGISTRY_PATH}")
    print(f"Batches processed: {reg['meta']['batches_processed']}")
    print("Done.")


if __name__ == '__main__':
    main()
