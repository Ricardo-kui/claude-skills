"""Save writing needs, top-3 candidates, source checks and timing for review."""
import argparse
import hashlib
import json
import statistics
import sys
import time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from retrieve import load_catalog, search
from build_catalog import DEFAULT_CATALOG


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--cases', type=Path, default=Path(__file__).with_name('cases.json'))
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    cases = json.loads(args.cases.read_text(encoding='utf-8'))
    start = time.perf_counter()
    catalog = load_catalog()
    cold = time.perf_counter() - start
    records, durations = [], []
    for case in cases['cases']:
        start = time.perf_counter()
        result = search(case['query'], case['function'], design=case.get('design', ''),
                        require_content=case.get('require_content', False), catalog=catalog,
                        need=case.get('need', ''), actions=case.get('actions'), conditions=case.get('conditions'),
                        evidence=case.get('evidence', ''), status=case.get('status'),
                        supplement_top=case.get('supplement_top', 2))
        durations.append(time.perf_counter()-start)
        records.append({'case': case, 'elapsed_seconds': round(durations[-1], 5), 'result': result})
    refs = [item for r in records for c in r['result']['candidates'] for item in c['originals']]
    supplements = [item for r in records for c in r['result'].get('supplementary_candidates', []) for item in c['originals']]
    uid_map = {r['uid']: r for r in catalog['entries']}
    failures = []
    for r in catalog['entries']:
        if r['kind'] != 'verbatim':
            continue
        lines = (ROOT / r['source_file']).read_text(encoding='utf-8').splitlines()
        context = '\n'.join(lines[(r['source_line'] or 1)-1:r['source_end_line']])
        import re
        context = ' '.join(re.sub(r'^\s*>\s?', '', line) for line in context.splitlines())
        if ' '.join(r['text'].split()).strip('"') not in ' '.join(context.split()):
            failures.append(r['uid'])
    summary = {'cases': len(records), 'cold_catalog_load_seconds': round(cold, 3),
       'warm_query_median_seconds': round(statistics.median(durations), 5),
       'warm_query_p95_seconds': round(sorted(durations)[int(.95*(len(durations)-1))], 5),
       'returned_cases': sum(bool(r['result']['candidates']) for r in records),
       'no_fit_cases': [r['case']['id'] for r in records if not r['result']['candidates']],
       'all_catalog_verbatim_context_checks': sum(r['kind']=='verbatim' for r in catalog['entries']),
       'verbatim_context_failures': failures,
       'local_archive_context_states': catalog['summary']['archive_contexts'],
       'candidate_excerpt_references': len(refs), 'supplementary_excerpt_references': len(supplements),
       'candidate_uid_failures': [r['uid'] for r in refs + supplements if r['uid'] not in uid_map],
       'quality_and_author_acceptance': '需另行逐题审查；结构和非空率不是质量或作者采用率'}
    deps = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in
            ['_shared/indexing/retrieve.py','_shared/indexing/request_matching.py',
             '_shared/indexing/adaptation_cards.py','_shared/indexing/retrieval-functions.json']}
    deps['catalog_content'] = hashlib.sha256(DEFAULT_CATALOG.read_bytes()).hexdigest()
    output = {'origin': cases['origin'], 'cases_sha256': hashlib.sha256(args.cases.read_bytes()).hexdigest(),
              'dependency_hashes': deps, 'summary': summary, 'records': records}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(output, ensure_ascii=False, indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(summary, ensure_ascii=False))
    return 1 if failures or summary['candidate_uid_failures'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
