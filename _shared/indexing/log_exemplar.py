"""Append factual returned/opened/adopted/author_accepted/rejected observations.

JSON stdin; tests and benchmark runs must use an isolated --home.
"""
import argparse
import json
import re
import sys
from pathlib import Path
from retrieve import load_catalog
from build_catalog import ROOT
sys.path.insert(0, str(ROOT / 'distill-paper-exemplar/scripts'))
from fitness_ledger import append_event, ledger_home, read_json_input
from build_catalog import digest

STATES = ('returned', 'opened', 'adopted', 'author_accepted', 'rejected')
FEEDBACK_STATES = ('author_accepted', 'rejected')
REASONS = {
    'function_mismatch': '查询解析／细功能定义与标签',
    'condition_mismatch': '设计、证据与论断适用条件',
    'adaptation_difficulty': '表达骨架与段落上下文',
    'source_unclear': '句级来源治理',
    'corpus_gap': '定向补充蒸馏',
    'content_distance': '内容匹配与排序',
    'redundant': '候选去重',
    'other': '按具体说明复核',
}


def validate(data, catalog, *, returned_uids=()):
    if not isinstance(data, dict):
        raise ValueError('event must be an object')
    data = {k: v for k, v in data.items() if k not in ('event_id', 'ts', 'schema_v')}
    allowed = {'query_id', 'state', 'actor', 'source_uids', 'project', 'request',
               'retrieval_version', 'candidates', 'resolved_function', 'resolved_actions',
               'result_reason', 'feedback', 'reason_code', 'reason', 'selected_ranks',
               'repair_target', 'read_refs', 'draft', 'use_id', 'skill', 'section', 'note',
               'feedback_scope', 'adoption_event_id'}
    if set(data) - allowed:
        raise ValueError('observation accepts references and feedback, not prose or candidate snapshots')
    if not isinstance(data.get('query_id'), str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.:-]{0,127}', data['query_id']):
        raise ValueError('query_id is required; use the ID returned by retrieval')
    state = data.get('state')
    if state not in STATES:
        raise ValueError(f'state must be one of {STATES}')
    if 'feedback_scope' in data and (state not in FEEDBACK_STATES or
                                    data['feedback_scope'] not in ('query', 'candidate', 'adoption')):
        raise ValueError('feedback_scope must be query, candidate or adoption on a feedback event')
    if 'use_id' in data and (not isinstance(data['use_id'], str) or
                             not data['use_id'].strip() or len(data['use_id']) > 128):
        raise ValueError('use_id must name an actual adoption')
    if 'adoption_event_id' in data and (state not in FEEDBACK_STATES or
            not isinstance(data['adoption_event_id'], str) or
            not re.fullmatch(r'[a-f0-9]{64}', data['adoption_event_id'])):
        raise ValueError('adoption_event_id must be an actual adopted event fingerprint')
    uids = data.get('source_uids', [])
    if not isinstance(uids, list) or any(not isinstance(u, str) for u in uids) or (
            not uids and state not in ('returned', 'rejected')):
        raise ValueError('source_uids must be a list; non-returned events need a source UID')
    known = {r['uid'] for r in catalog['entries']} | set(returned_uids)
    unknown = [u for u in uids if u not in known]
    if unknown:
        raise ValueError(f'unknown source UIDs: {unknown}')
    if data.get('actor') not in ('agent', 'author'):
        raise ValueError('actor must be agent or author')
    if state == 'author_accepted' and data.get('actor') != 'author':
        raise ValueError('author_accepted requires actual author feedback, actor=author')
    if data.get('actor') == 'author' and state in ('author_accepted', 'rejected') and (
            not isinstance(data.get('feedback'), str) or not data['feedback'].strip()):
        raise ValueError('author evaluation needs the actual author feedback')
    if data.get('reason_code') is not None and data['reason_code'] not in REASONS:
        raise ValueError(f'reason_code must be one of {tuple(REASONS)}')
    if state == 'rejected' and (not isinstance(data.get('reason'), str) or not data['reason'].strip() or
                                data.get('reason_code') not in REASONS):
        raise ValueError('rejected needs reason_code and a concrete reason')
    if 'draft' in data:
        draft = data['draft']
        if (not isinstance(draft, dict) or set(draft) - {'path', 'sha256', 'location'} or
                not isinstance(draft.get('path'), str) or not draft['path'].strip() or
                not isinstance(draft.get('sha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', draft['sha256'])):
            raise ValueError('draft observation stores a locator and fingerprint, not prose')
    if 'read_refs' in data:
        refs = data['read_refs']
        fields = {'uid', 'source_file', 'sha256', 'source_line', 'source_end_line', 'role'}
        if not isinstance(refs, list) or not refs or any(
                not isinstance(r, dict) or set(r) != fields or r.get('uid') not in uids or
                not isinstance(r.get('sha256'), str) or not re.fullmatch(r'[a-f0-9]{64}', r['sha256'])
                for r in refs):
            raise ValueError('read_refs need compact file fingerprints and selected UIDs')
    if state == 'returned':
        if not isinstance(data.get('request'), dict) or not isinstance(data.get('retrieval_version'), dict):
            raise ValueError('returned needs request and retrieval_version')
        if any(not isinstance(data['retrieval_version'].get(k), str) or not re.fullmatch(
                r'[a-f0-9]{64}', data['retrieval_version'][k]) for k in ('ranker', 'functions', 'corpus')):
            raise ValueError('retrieval_version needs ranker/functions/corpus SHA256 fingerprints')
        if not isinstance(data['request'].get('query'), str):
            raise ValueError('request needs the actual query')
        refs = data.get('candidates')
        if not isinstance(refs, list) or any(not isinstance(c, dict) for c in refs):
            raise ValueError('returned needs compact candidate ranks and UIDs')
        fields = {'rank', 'source_uids', 'function_fit', 'source_file', 'source_line', 'candidate_role'}
        if any(set(c) - fields for c in refs):
            raise ValueError('returned candidates store compact references, not snapshots')
        if [c.get('rank') for c in refs] != list(range(1, len(refs) + 1)):
            raise ValueError('candidate ranks must be consecutive from 1')
        if any(not isinstance(c.get('source_uids'), list) or not c['source_uids'] or
               any(not isinstance(u, str) for u in c['source_uids']) for c in refs):
            raise ValueError('each candidate needs source_uids')
        if set(uids) != {u for c in refs for u in c['source_uids']}:
            raise ValueError('returned source_uids must equal the candidate UID union')
    return {**data, 'source_uids': sorted(set(uids))}


def observations(home=None, kind='exemplar_use'):
    if kind not in ('exemplar_use', 'consumption'):
        raise ValueError('unsupported observation kind')
    path = ledger_home(home) / 'events' / f'{kind}.jsonl'
    if not path.is_file():
        return []
    events = []
    for line in path.read_text(encoding='utf-8').splitlines():
        try:
            item = json.loads(line)
            if isinstance(item, dict):
                events.append(item)
        except json.JSONDecodeError:
            continue
    return events


def bind_feedback(data, events):
    """Bind an evaluation to its actual candidate or saved adoption, never a later revision."""
    uids = set(data['source_uids'])
    adoptions = [e for e in events if e.get('query_id') == data['query_id']
                 and e.get('state') == 'adopted' and uids
                 and uids.issubset(e.get('source_uids', []))]
    scope = data.get('feedback_scope')
    refs = any(k in data for k in ('use_id', 'adoption_event_id', 'draft'))
    if scope is None:
        scope = 'adoption' if refs or adoptions else ('candidate' if uids else 'query')
    data['feedback_scope'] = scope
    if scope != 'adoption':
        if refs or (scope == 'query') != (not uids):
            raise ValueError('query feedback needs no UID; candidate feedback needs UIDs and no adoption reference')
        return data
    if not uids:
        raise ValueError('adoption feedback needs the actually adopted UIDs')
    if 'use_id' in data:
        adoptions = [e for e in adoptions if e.get('use_id') == data['use_id']]
    if 'adoption_event_id' in data:
        adoptions = [e for e in adoptions if e.get('event_id') == data['adoption_event_id']]
    if 'draft' in data:
        supplied = data['draft']
        adoptions = [e for e in adoptions if all(
            e.get('draft', {}).get(k) == v for k, v in supplied.items())]
    matches = {e.get('event_id') or e.get('use_id'): e for e in adoptions}
    if not matches:
        raise ValueError('feedback reference does not match an adoption of these UIDs in this query_id')
    if len(matches) != 1:
        raise ValueError('feedback target is ambiguous; specify the actual use_id or adoption_event_id')
    target = next(iter(matches.values()))
    if target.get('use_id'):
        data['use_id'] = target['use_id']
    if target.get('event_id'):
        data['adoption_event_id'] = target['event_id']
    if not target.get('use_id') and not target.get('event_id'):
        raise ValueError('historical adoption has no stable reference; do not guess its draft version')
    if target.get('draft'):
        data['draft'] = target['draft']
    return data


def is_author_evaluation(event):
    return (event.get('actor') == 'author' and event.get('state') in FEEDBACK_STATES
            and isinstance(event.get('feedback'), str) and bool(event['feedback'].strip()))


def source_history(uid, events):
    """Separate candidate feedback, individual adoption versions and unbound history."""
    selected = [e for e in events if uid in e.get('source_uids', [])]
    authors = [e for e in selected if is_author_evaluation(e)]
    candidates = [e for e in authors if e.get('feedback_scope') == 'candidate']
    versions, bound, seen = [], set(), set()
    for index, adopted in enumerate(e for e in selected if e.get('state') == 'adopted'):
        key = adopted.get('event_id') or adopted.get('use_id') or ('unbound', index)
        if key in seen:
            continue
        seen.add(key)
        ratings = []
        for i, rating in enumerate(authors):
            if rating.get('feedback_scope') in ('candidate', 'query'):
                continue
            if rating.get('adoption_event_id'):
                matches = rating['adoption_event_id'] == adopted.get('event_id')
                if rating.get('use_id'):
                    matches = matches and rating['use_id'] == adopted.get('use_id')
            else:
                matches = bool(rating.get('use_id')) and rating['use_id'] == adopted.get('use_id')
            if matches:
                ratings.append(rating)
                bound.add(i)
        versions.append({'use_id': adopted.get('use_id'), 'adoption_event_id': adopted.get('event_id'),
                         'draft': adopted.get('draft'),
                         'author_status': ratings[-1]['state'] if ratings else 'unknown',
                         'author_feedback': ratings[-1]['feedback'] if ratings else None})
    unbound = [e for i, e in enumerate(authors) if i not in bound and e.get('feedback_scope') != 'candidate']
    if versions:
        current, scope = versions[-1], 'adoption'
    elif candidates:
        current = {'author_status': candidates[-1]['state'], 'author_feedback': candidates[-1]['feedback']}
        scope = 'candidate'
    else:
        # Keep old UID-level feedback visible without assigning it to a draft.
        current = {'author_status': unbound[-1]['state'] if unbound else 'unknown',
                   'author_feedback': unbound[-1]['feedback'] if unbound else None}
        scope = 'legacy_uid' if unbound else 'unknown'
    return {'adoptions': versions, 'author_status': current['author_status'],
            'author_feedback': current['author_feedback'], 'author_status_scope': scope,
            'candidate_author_status': candidates[-1]['state'] if candidates else 'unknown',
            'unbound_author_feedback': unbound}


def record_observation(data, catalog, home=None):
    if ledger_home(home).resolve().is_relative_to(ROOT.resolve()):
        raise ValueError('exemplar-use ledger must stay outside the skills repository')
    if not isinstance(data, dict):
        raise ValueError('event must be an object')
    events = observations(home)
    returned = next((e for e in events if e.get('query_id') == data.get('query_id')
                     and e.get('state') == 'returned'), None)
    data = dict(validate(data, catalog, returned_uids=(returned or {}).get('source_uids', [])
                         if data.get('state') != 'returned' else ()))
    if data['state'] == 'returned':
        if returned and any(data.get(k) != returned.get(k) for k in
                            ('request', 'retrieval_version', 'candidates', 'source_uids')):
            raise ValueError('query_id already belongs to another request/version/candidate set; use a new ID')
    else:
        if not returned:
            raise ValueError('query_id has no returned event; record the actual retrieval first')
        if not set(data['source_uids']).issubset(returned['source_uids']):
            raise ValueError('selected UIDs were not returned by this query_id')
        data['retrieval_version'] = returned['retrieval_version']
        if returned.get('project'):
            if data.get('project') and data['project'] != returned['project']:
                raise ValueError('project differs from this query_id')
            data['project'] = returned['project']
        data['selected_ranks'] = [c['rank'] for c in returned['candidates']
                                  if set(data['source_uids']) & set(c['source_uids'])]
    if data.get('reason_code'):
        data['repair_target'] = REASONS[data['reason_code']]
    if data['state'] in FEEDBACK_STATES:
        data = bind_feedback(data, events)
    # Replaying the same observation is idempotent. Different actual feedback
    # remains append-only; states are never fabricated to fill missing steps.
    data['event_id'] = digest(json.dumps(data, ensure_ascii=False, sort_keys=True))
    if any(e.get('event_id') == data['event_id'] for e in events):
        return True
    return append_event('exemplar_use', data, home=home)


def record_returned(result, catalog, home=None, project=None):
    candidates = result['candidates'] + result.get('supplementary_candidates', [])
    refs = [{'rank': c['rank'], 'source_uids': [r['uid'] for r in c['originals'] + c['templates']],
             'function_fit': c['function_fit'], 'source_file': c['source_file'],
             'source_line': c['source_line'], 'candidate_role': c.get('candidate_role', 'primary')}
            for c in candidates]
    data = {'query_id': result['query_id'], 'state': 'returned', 'actor': 'agent',
            'source_uids': sorted({u for c in refs for u in c['source_uids']}),
            'request': result['request'], 'resolved_function': result['function'],
            'resolved_actions': result.get('functions', []),
            'retrieval_version': result['retrieval_version'], 'candidates': refs,
            'result_reason': result['reason']}
    if project:
        data['project'] = project
    return record_observation(data, catalog, home=home)


def query_chain(query_id, home=None):
    """Derive the actual chain; missing observations and author views stay unknown."""
    events = [e for e in observations(home) if e.get('query_id') == query_id]
    returned = next((e for e in events if e.get('state') == 'returned'), None)
    if not returned:
        raise ValueError('query_id has no returned event')
    consumption = [e for e in observations(home, 'consumption')
                   if isinstance(e.get('uses'), list) and any(
                       isinstance(u, dict) and u.get('query_id') == query_id for u in e['uses'])]
    sources = []
    for uid in returned.get('source_uids', []):
        selected = [e for e in events if uid in e.get('source_uids', [])]
        sources.append({
            'uid': uid,
            'candidates': [{k: c.get(k) for k in ('rank', 'candidate_role', 'function_fit')}
                           for c in returned['candidates'] if uid in c['source_uids']],
            'opened': any(e.get('state') == 'opened' for e in selected),
            'opened_with_file_evidence': any(e.get('state') == 'opened' and any(
                r.get('uid') == uid and r.get('role') == 'corpus_card' for r in e.get('read_refs', []))
                for e in selected),
            'adopted': any(e.get('state') == 'adopted' for e in selected),
            'drafts': [e['draft'] for e in selected if e.get('state') == 'adopted' and e.get('draft')],
            **source_history(uid, events),
            'rejections': [{k: e.get(k) for k in ('actor', 'reason_code', 'reason', 'repair_target', 'feedback',
                                                'feedback_scope', 'use_id', 'adoption_event_id', 'draft')}
                           for e in selected if e.get('state') == 'rejected'],
        })
    return {'query_id': query_id, 'request': returned['request'],
            'retrieval_version': returned['retrieval_version'], 'project': returned.get('project'),
            'candidates': returned['candidates'], 'sources': sources,
            'query_feedback': [e for e in events if e.get('state') == 'rejected' and not e.get('source_uids')],
            'timeline': events, 'consumption': consumption}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--home', type=Path, help='isolated ledger home for tests')
    ap.add_argument('--list-reasons', action='store_true')
    ap.add_argument('--query-id', help='read the linked chain without writing an event')
    args = ap.parse_args()
    if args.list_reasons:
        print(json.dumps(REASONS, ensure_ascii=False, indent=2))
        return 0
    try:
        if args.query_id:
            print(json.dumps(query_chain(args.query_id, args.home), ensure_ascii=False, indent=2))
            return 0
        ok = record_observation(read_json_input(), load_catalog(), home=args.home)
    except (ValueError, TypeError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
