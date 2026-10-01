"""Read-side resolution of legacy wb aliases and current excerpt UIDs.

Never modify historical JSONL events. Ambiguous references remain unresolved.
"""
import re
from retrieve import load_catalog
from build_catalog import WB


def norm_key(value):
    return re.sub(r'[\s_\-]+', '', value or '').lower()


def resolve_event(event, catalog=None):
    data = catalog or load_catalog()
    rows = data['entries']
    section = event.get('section') or event.get('skill', '').removeprefix('write-')
    rows = [r for r in rows if r['section'] == section]
    actual = {(norm_key(m['paper']), m['item']) for r in rows for m in r['wb_items']}
    resolved, unresolved, details = set(), [], []
    for uid in event.get('source_uids', []):
        matches = [r for r in rows if r['uid'] == uid]
        if len(matches) == 1:
            keys = {(norm_key(m['paper']), m['item']) for m in matches[0]['wb_items']}
            resolved.update(keys)
            details.append({'input': uid, 'resolution': 'uid', 'keys': sorted(keys)})
        else:
            unresolved.append(uid)
    for value in event.get('variants', []):
        ms = list(WB.finditer(str(value)))
        if not ms:
            unresolved.append(value)
            continue
        for m in ms:
            paper, item = norm_key(m.group(1).strip()), m.group(2).strip()
            if (paper, item) in actual:
                resolved.add((paper, item))
                details.append({'input': m.group(0), 'resolution': 'exact_wb', 'keys': [(paper, item)]})
                continue
            # Old event used skeleton family-N instead of the authored wb item.
            # Require family+variant AND citekey AND one source block, no first match.
            family, sep, ordinal = item.rpartition('-')
            if not sep or not ordinal.isdigit():
                unresolved.append(m.group(0))
                continue
            matches = [r for r in rows if r['id'].split('#')[0] == family
                       and r['id'].split('#')[-1] in (ordinal, 'T' + ordinal)
                       and norm_key(r['citekey']) == paper]
            parents = {r['parent_paragraph'] for r in matches}
            keys = {(norm_key(w['paper']), w['item']) for r in matches for w in r['wb_items']}
            if len(parents) == 1 and keys:
                resolved.update(keys)
                details.append({'input': m.group(0), 'resolution': 'legacy_family_variant_source',
                                'source_uids': [r['uid'] for r in matches], 'keys': sorted(keys)})
            else:
                unresolved.append(m.group(0))
    return {'resolved': sorted(resolved), 'unresolved': unresolved, 'details': details}
