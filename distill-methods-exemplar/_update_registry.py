"""Phase 4.5 utility: update _evidence_registry.yaml from corpus_enrichment YAML.

Usage:
    python _update_registry.py <corpus_enrichment.yaml>
    # or pipe from stdin:
    cat corpus_enrichment.yaml | python _update_registry.py --stdin

Reads a corpus_enrichment YAML block (the hardened output from distill Phase 4),
applies evidence_updates to the shared evidence registry, recalculates
paper_count and status automatically.

No manual scripting needed -- this is the automated consumer of Phase 4 output.
"""

import sys
import yaml
from pathlib import Path
from collections import Counter

REGISTRY_PATH = (
    Path(__file__).parent.parent
    / "write-methods"
    / "academic-writing-corpus"
    / "_evidence_registry.yaml"
)

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


def load_enrichment(path=None):
    """Load corpus_enrichment YAML from file or stdin."""
    if path and path != '--stdin':
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    else:
        text = sys.stdin.read()
        if 'corpus_enrichment:' in text:
            text = text[text.index('corpus_enrichment:'):]
        data = yaml.safe_load(text)

    # Unwrap top-level 'corpus_enrichment' key if present
    if isinstance(data, dict) and 'corpus_enrichment' in data:
        return data['corpus_enrichment']
    return data


def load_registry():
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_registry(reg):
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        yaml.dump(reg, f, allow_unicode=True, default_flow_style=False,
                  sort_keys=False, width=120)


def get_design_type(paper_str):
    """Extract design type for a paper from its registry string."""
    paper_short = paper_str.split(' (')[0].strip()
    return PAPER_DESIGN_TYPES.get(paper_short)


def get_journal(paper_str):
    """Extract journal abbreviation from paper string like 'author_year (JOURNAL)'."""
    if '(' in paper_str:
        return paper_str.split('(')[-1].rstrip(')').strip()
    return ''


def recalc_entry(entry):
    """Recalculate paper_count and status for a design type entry."""
    papers = sorted(set(entry.get('papers', [])))
    entry['papers'] = papers
    entry['paper_count'] = len(papers)

    journals = set()
    for p in papers:
        j = get_journal(p)
        if j:
            journals.add(j)

    if entry['paper_count'] >= 5 and len(journals) >= 2:
        entry['status'] = 'ROBUST'
    elif entry['paper_count'] >= 3:
        entry['status'] = 'VERIFIED'
    else:
        entry['status'] = 'EMERGING'


def apply_enrichment(reg, enrichment):
    """Apply corpus_enrichment evidence_updates to registry."""
    updates = enrichment.get('evidence_updates', [])
    if not updates:
        print("No evidence_updates found in enrichment block.")
        return reg

    for upd in updates:
        design_type = upd.get('design_type', '')
        slot = upd.get('slot', '')
        action = upd.get('action')

        if not design_type:
            print(f"  SKIP: missing design_type in {upd}")
            continue

        section = reg['evidence'].get('by_design_type', {})
        if design_type not in section:
            if action == 'create_new':
                section[design_type] = {
                    'paper_count': 0, 'papers': [],
                    'status': 'EMERGING',
                    'slots_covered': [],
                    'common_failures': [],
                    'validation_history': {
                        'total_runs': 0, 'validated': 0,
                        'revise': 0, 'reject': 0,
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
            # Track slot coverage
            if slot and slot not in entry.get('slots_covered', []):
                entry.setdefault('slots_covered', []).append(slot)
            recalc_entry(entry)
            print(f"  {design_type}: +{added} papers -> {entry['paper_count']}p, {entry['status']}")

        elif action == 'update_status':
            new_status = upd.get('new_status')
            if new_status:
                entry['status'] = new_status
            reason = upd.get('reason', '')
            recalc_entry(entry)
            print(f"  {design_type}: status -> {entry['status']} ({reason})")

        elif action == 'create_new':
            new_papers = upd.get('new_papers', [])
            entry['papers'] = sorted(set(new_papers))
            if slot and slot not in entry.get('slots_covered', []):
                entry.setdefault('slots_covered', []).append(slot)
            recalc_entry(entry)
            print(f"  {design_type}: CREATED {entry['paper_count']}p, {entry['status']}")

    # Apply anti-pattern updates
    for ap in enrichment.get('anti_pattern_updates', []):
        target_dt = ap.get('target_design_type', '')
        pattern = ap.get('pattern', '')
        if target_dt and pattern:
            dt_entry = section.get(target_dt, {})
            if pattern not in dt_entry.get('common_failures', []):
                dt_entry.setdefault('common_failures', []).append(pattern)
                print(f"  {target_dt}: +common_failure: {pattern[:80]}...")

    # Update meta
    reg['meta']['last_updated'] = enrichment.get('last_updated', '2026-05-21')
    reg['meta']['batches_processed'] = reg['meta'].get('batches_processed', 0) + 1

    return reg


def main():
    if len(sys.argv) > 1 and sys.argv[1] not in ('--stdin', '-h', '--help'):
        enrichment = load_enrichment(sys.argv[1])
    elif '--stdin' in sys.argv or len(sys.argv) == 1:
        enrichment = load_enrichment('--stdin')
    elif sys.argv[1] in ('-h', '--help'):
        print(__doc__)
        return

    reg = load_registry()
    reg = apply_enrichment(reg, enrichment)
    save_registry(reg)
    print(f"\nRegistry updated: {REGISTRY_PATH}")
    print(f"Batches processed: {reg['meta']['batches_processed']}")


if __name__ == '__main__':
    main()
