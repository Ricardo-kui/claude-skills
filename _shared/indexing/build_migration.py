"""Build an explicit migration from a frozen pre-change index audit (read-only)."""
import argparse
import hashlib
import html
import json
from collections import defaultdict
from pathlib import Path
from retrieve import load_catalog


def normalize(text):
    return ' '.join(html.unescape(text).replace('\\|', '|').replace('<br>', ' ').split())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--baseline', required=True, type=Path)
    ap.add_argument('--out', type=Path, default=Path(__file__).with_name('legacy-id-migration.json'))
    args = ap.parse_args()
    baseline = json.loads(args.baseline.read_text(encoding='utf-8'))
    by = defaultdict(list)
    for row in load_catalog()['entries']:
        by[(row['section'], row['source_file'], normalize(row['text']))].append(row)
    migrations, unresolved, mapped = [], [], 0
    for old in baseline:
        anchor = old.get('anchor', old.get('卡片路径#锚点', ''))
        source = f"write-{old['section']}/" + anchor.split('#')[0]
        text = normalize(old.get('text') or old.get('模板') or '')
        matches = by.get((old['section'], source, text), [])
        if not matches:
            unresolved.append({'section': old['section'], 'id': old['id'], 'source_file': source})
            continue
        mapped += 1
        if any(r['id'] != old['id'] or r['citekey'] != old['citekey'] for r in matches):
            migrations.append({'section': old['section'], 'legacy_id': old['id'], 'legacy_anchor': anchor,
                'legacy_citekey': old['citekey'], 'source_file': source,
                'text_sha256': hashlib.sha256(text.encode()).hexdigest(),
                'targets': [{'id': r['id'], 'uid': r['uid'], 'citekey': r['citekey']} for r in matches]})
    data = {'schema_version': 1, 'baseline_sha256': hashlib.sha256(args.baseline.read_bytes()).hexdigest(),
            'policy': '旧 ID 需结合源文件与摘录内容；多目标显式保留，不取第一项。',
            'migrations': migrations, 'unresolved': unresolved,
            'summary': {'baseline_entries': len(baseline), 'mapped': mapped,
                        'unresolved': len(unresolved), 'changed_records': len(migrations)}}
    args.out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(data['summary']))
    return 1 if unresolved else 0


if __name__ == '__main__':
    raise SystemExit(main())
