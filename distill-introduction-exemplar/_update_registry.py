"""Phase 4.5 utility: update _evidence_registry.yaml from corpus_enrichment YAML.

Usage:
    python _update_registry.py <corpus_enrichment.yaml>
    # or pipe from stdin:
    cat corpus_enrichment.yaml | python _update_registry.py --stdin

Reads a corpus_enrichment YAML block (the hardened output from distill Phase 4),
applies evidence_updates to the shared evidence registry, recalculates
gap_distribution and status automatically.

Paper-to-gap mappings are stored in the registry's `paper_index` section
(self-maintaining).  The hardcoded PAPER_GAPS dict below serves only as
a bootstrap / fallback — it seeds the registry on first migration and catches
any paper IDs that haven't yet been written into the index.
"""

import sys
import yaml
from pathlib import Path
from collections import Counter

REGISTRY_PATH = Path(__file__).parent.parent / "write-introduction" / "corpus" / "_evidence_registry.yaml"

# Bootstrap-only paper-to-gap mapping.
# Once the registry contains a `paper_index` block this dict is *only* a fallback
# for paper IDs that predate the index migration.  New papers are added to
# `paper_index` automatically by `apply_enrichment`.
_PAPER_GAPS_BOOTSTRAP = {
    'ceo_regulatory_focus_ijrm': 'Inadequacy', 'darby2024': 'Incompleteness',
    'eilert2017': 'Incompleteness', 'han2020': 'Inadequacy', 'han2024': 'Inadequacy',
    'keeves2017': 'Inadequacy', 'kundro2023': 'Inadequacy',
    'lashley_pollock2020': 'Inadequacy', 'lovelace2021': 'Inadequacy',
    'park2013': 'Incompleteness', 'park2025': 'Inadequacy',
    'paruchuri2020': 'Inadequacy', 'pollock2015': 'Incompleteness',
    'pontikes2012': 'Incommensurability', 'shen2022': 'Inadequacy',
    'shi2021': 'Incompleteness', 'shipilov2020': 'Inadequacy',
    'singh2023': 'Inadequacy', 'toh2023': 'Incompleteness',
    'wu2025': 'Incompleteness', 'zhao_ding2022': 'Incompleteness',
    'zhou2017': 'Incommensurability', 'employee_free_speech': 'Inadequacy',
    'malshe2015': 'Incompleteness', 'gamache2020': 'Inadequacy',
    'gamache2023': 'Inadequacy', 'hahl2017': 'Inadequacy',
    'desjardine2023': 'Incompleteness', 'darby2025': 'Incompleteness',
    'darby2026': 'Incompleteness', 'desai2012': 'Incompleteness',
    'lehman2014': 'Incompleteness', 'mannor2016': 'Incompleteness',
    'mayo2021': 'Incompleteness', 'pfarrer2010': 'Inadequacy',
    'vadakkepatt2022': 'Incompleteness', 'wowak2025': 'Incompleteness',
    'gomulya2019': 'Inadequacy',
    'employee_free_speech2024': 'Inadequacy',
    'haunschild2015': 'Incompleteness',
    'darby2023': 'Incompleteness',
    'vidal_mitchell2015': 'Incommensurability',
    'jiang2026': 'Incompleteness',
}

MODULE_KEY = {
    'hooks': 'hooks', 'hook': 'hooks',
    'tensions': 'tensions', 'tension': 'tensions',
    'stakes': 'stakes', 'stake': 'stakes',
    'literature_turns': 'literature_turns', 'literature_turn': 'literature_turns',
    'previews': 'previews', 'preview': 'previews',
    'contributions': 'contributions', 'contribution': 'contributions',
    'theory_lens': 'theory_lens',
}


def load_enrichment(path=None):
    """Load corpus_enrichment YAML from file or stdin. Unwraps top-level key if present."""
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
        yaml.dump(reg, f, allow_unicode=True, default_flow_style=False, sort_keys=False, width=120)


def get_gap(paper_str, paper_index=None):
    """Extract gap type for a paper.

    Looks up the paper in:
    1. `paper_index` (registry-maintained, primary source)
    2. `_PAPER_GAPS_BOOTSTRAP` (hardcoded fallback for pre-migration papers)
    """
    paper_short = paper_str.split(' (')[0].strip()
    if paper_index and paper_short in paper_index:
        return paper_index[paper_short]
    return _PAPER_GAPS_BOOTSTRAP.get(paper_short)


def recalc_entry(entry, paper_index=None):
    """Recalculate paper_count, gap_distribution, and status for a template entry."""
    papers = sorted(set(entry.get('papers', [])))
    entry['papers'] = papers
    entry['paper_count'] = len(papers)

    dist = Counter()
    journals = set()
    missing = []
    for p in papers:
        gap = get_gap(p, paper_index)
        if gap:
            dist[gap] += 1
        else:
            missing.append(p.split(' (')[0].strip())
        j = p.split('(')[-1].rstrip(')') if '(' in p else ''
        if j:
            journals.add(j)

    entry['gap_distribution'] = {
        'Incompleteness': dist.get('Incompleteness', 0),
        'Inadequacy': dist.get('Inadequacy', 0),
        'Incommensurability': dist.get('Incommensurability', 0),
    }

    if missing:
        print(f"  WARN {entry.get('canonical_id', '?' )}: {len(missing)} paper(s) missing gap type: {missing}")

    if entry['paper_count'] >= 5 and len(journals) >= 2:
        entry['status'] = 'ROBUST'
    elif entry['paper_count'] >= 3:
        entry['status'] = 'VERIFIED'
    else:
        entry['status'] = 'EMERGING'


def _ensure_paper_index(reg):
    """One-time migration: seed paper_index from the bootstrap dict if missing."""
    if 'paper_index' not in reg:
        reg['paper_index'] = dict(_PAPER_GAPS_BOOTSTRAP)
        print(f"  Migrated {len(reg['paper_index'])} paper gap mappings from bootstrap to registry paper_index.")


def apply_enrichment(reg, enrichment):
    """Apply corpus_enrichment evidence_updates to registry."""
    _ensure_paper_index(reg)
    paper_index = reg['paper_index']

    # Absorb new paper gaps from the enrichment block (distill Phase 4 output)
    new_paper_gaps = enrichment.get('paper_gaps', {})
    if new_paper_gaps:
        paper_index.update(new_paper_gaps)
        print(f"  +{len(new_paper_gaps)} paper gap(s) added to paper_index: {list(new_paper_gaps.keys())}")

    updates = enrichment.get('evidence_updates', [])
    if not updates:
        print("No evidence_updates found in enrichment block.")
        return reg

    for upd in updates:
        canonical_id = upd.get('canonical_id')
        module_key = MODULE_KEY.get(upd.get('module', ''))
        action = upd.get('action')

        if not canonical_id or not module_key:
            print(f"  SKIP: missing canonical_id or module in {upd}")
            continue

        if module_key not in reg['evidence']:
            print(f"  SKIP: unknown module '{module_key}'")
            continue

        if canonical_id not in reg['evidence'][module_key]:
            if action == 'create_new':
                reg['evidence'][module_key][canonical_id] = {
                    'paper_count': 0, 'papers': [],
                    'gap_distribution': {'Incompleteness': 0, 'Inadequacy': 0, 'Incommensurability': 0},
                    'status': 'EMERGING', 'generativity': 'ADAPTABLE',
                    'exclusivity': 'MEDIUM', 'common_failures': [],
                    'validation_history': {'total_runs': 0, 'validated': 0, 'revise': 0, 'reject': 0, 'common_revise_reasons': []},
                }
            else:
                print(f"  SKIP: canonical_id '{canonical_id}' not found in {module_key}")
                continue

        entry = reg['evidence'][module_key][canonical_id]

        if action == 'append_papers':
            new_papers = upd.get('new_papers', [])
            existing = set(entry.get('papers', []))
            added = 0
            for p in new_papers:
                if p and p.strip() and p not in existing:
                    existing.add(p)
                    added += 1
            entry['papers'] = sorted(existing)
            recalc_entry(entry, paper_index)
            print(f"  {canonical_id}: +{added} papers → {entry['paper_count']}p, {entry['status']}")

        elif action == 'update_status':
            new_status = upd.get('new_status')
            if new_status:
                entry['status'] = new_status
            reason = upd.get('reason', '')
            recalc_entry(entry, paper_index)
            print(f"  {canonical_id}: status → {entry['status']} ({reason})")

        elif action == 'create_new':
            new_papers = upd.get('new_papers', [])
            entry['papers'] = sorted(set(new_papers))
            entry['gap_type'] = upd.get('gap_type', '')
            recalc_entry(entry, paper_index)
            print(f"  {canonical_id}: CREATED {entry['paper_count']}p, {entry['status']}")

        # Update common_failures if provided in anti_pattern_updates
        anti_patterns = enrichment.get('anti_pattern_updates', [])
        for ap in anti_patterns:
            target_canonical = ap.get('target_canonical_id', '')
            target_module = ap.get('target_module', '')
            # Only apply if canonical_id matches exactly, or if target_module matches the module key
            # AND target_canonical is not specified (module-level pattern)
            if target_canonical and target_canonical == canonical_id:
                pattern = ap.get('pattern', '')
                if pattern and pattern not in entry.get('common_failures', []):
                    entry.setdefault('common_failures', []).append(pattern)
                    print(f"  {canonical_id}: +common_failure: {pattern[:80]}...")
            elif not target_canonical and target_module == module_key:
                # Module-level anti-pattern — only add if no specific canonical_id is targeted
                pattern = ap.get('pattern', '')
                if pattern and pattern not in entry.get('common_failures', []):
                    entry.setdefault('common_failures', []).append(pattern)
                    print(f"  {canonical_id}: +common_failure: {pattern[:80]}...")

    # Update gap_distribution_updates
    for gdu in enrichment.get('gap_distribution_updates', []):
        cid = gdu.get('canonical_id')
        if cid:
            for mod_key in ['hooks', 'tensions', 'stakes', 'literature_turns']:
                if cid in reg['evidence'].get(mod_key, {}):
                    recalc_entry(reg['evidence'][mod_key][cid], paper_index)

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
