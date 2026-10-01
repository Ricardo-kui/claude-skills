"""Actual writing operations with query-bound, metadata-only use records.

query: live retrieval (returned is automatic; retrieve.py remains read-only).
open: read selected cards and available original context, then record opened.
write: save a text draft, then record adopted and consumption together.
adopt: verify a draft saved by another writer, then use the same registration.
feedback: register an actual evaluation of candidates or a particular adoption.
show: derive a query's chain. Tests must pass an isolated --home.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from pathlib import Path

from build_catalog import ROOT, SECTIONS, digest
from retrieve import load_catalog, retrieval_version
from log_exemplar import observations, query_chain, record_observation, validate, FEEDBACK_STATES
from fitness_ledger import append_event, ledger_home, read_json_input


def file_hash(data):
    return hashlib.sha256(data).hexdigest()


def external_path(value, *, name, home=None):
    if not isinstance(value, (str, Path)) or not str(value).strip():
        raise ValueError(f'{name} needs a path')
    path = Path(value).expanduser().resolve()
    if path.is_relative_to(ROOT.resolve()):
        raise ValueError(f'{name} must stay outside the skills repository')
    if name == 'draft' and path.is_relative_to(ledger_home(home).resolve()):
        raise ValueError('draft must stay outside the use ledger')
    return path


def bound_selection(query_id, uids, catalog, events, project=None):
    selected = validate({'query_id': query_id, 'source_uids': uids,
                         'state': 'opened', 'actor': 'agent'}, catalog)
    returned = next((e for e in events if e.get('query_id') == query_id
                     and e.get('state') == 'returned'), None)
    if not returned:
        raise ValueError('query_id has no returned event; record the actual retrieval first')
    if not set(selected['source_uids']).issubset(returned['source_uids']):
        raise ValueError('selected UIDs were not returned by this query_id')
    if returned.get('project') and project and returned['project'] != project:
        raise ValueError('project differs from this query_id')
    if returned['retrieval_version']['corpus'] != retrieval_version(catalog)['corpus']:
        raise ValueError('corpus changed since retrieval; query again before reading or adopting')
    return selected['source_uids'], returned


def open_exemplars(query_id, source_uids, catalog, home=None, project=None):
    """Read files, never infer a read from a returned card or a cache hit."""
    external_path(ledger_home(home), name='ledger')
    uids, returned = bound_selection(query_id, source_uids, catalog, observations(home), project)
    rows = {r['uid']: r for r in catalog['entries']}
    files, refs, sources = {}, [], []

    def read_range(uid, rel, start, end, role):
        path = (ROOT / rel).resolve()
        if not path.is_relative_to(ROOT.resolve()):
            raise ValueError('source path escapes the corpus repository')
        if rel not in files:
            raw = path.read_bytes()
            text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
            expected = catalog['dependencies'].get(rel)
            if expected is None or digest(text) != expected:
                raise ValueError('source changed or is unregistered; refresh the retrieval')
            files[rel] = (raw, text.splitlines())
        raw, lines = files[rel]
        if not isinstance(start, int) or not isinstance(end, int) or not 1 <= start <= end <= len(lines):
            raise ValueError('source range is no longer valid; refresh the retrieval')
        refs.append({'uid': uid, 'source_file': rel, 'sha256': file_hash(raw),
                     'source_line': start, 'source_end_line': end, 'role': role})
        return '\n'.join(lines[start - 1:end])

    for uid in uids:
        row = rows[uid]
        card = read_range(uid, row['source_file'], row['source_line'], row['source_end_line'], 'corpus_card')
        context = row.get('source_context', {})
        paragraphs = []
        for role, locations in (('original_paragraph', context.get('paragraphs', [])),
                                ('preceding_paragraph', [context.get('preceding_paragraph')]),
                                ('following_paragraph', [context.get('following_paragraph')])):
            for loc in locations:
                if loc:
                    text = read_range(uid, loc['source_file'], loc['source_line'], loc['source_end_line'], role)
                    paragraphs.append({k: loc.get(k) for k in
                                       ('source_file', 'source_line', 'source_end_line', 'source_section', 'paragraph_number')} |
                                      {'role': role, 'text': text})
        sources.append({'uid': uid, 'kind': row['kind'], 'text': row['text'],
                        'citekey': row['citekey'], 'status': row['status'],
                        'source_context_state': context.get('state', 'not_applicable'),
                        'card_context': card, 'archive_context': paragraphs})
    event = {'query_id': query_id, 'state': 'opened', 'actor': 'agent',
             'source_uids': uids, 'read_refs': refs}
    if project or returned.get('project'):
        event['project'] = project or returned['project']
    ok = record_observation(event, catalog, home)
    return {'query_id': query_id, 'sources': sources, 'opened_recorded': ok,
            'limits': '实际读取的是语料卡与可定位的本地原文档案；不代表核验原始 PDF。'}


def prepare_adoption(data, catalog, home=None):
    if not isinstance(data, dict):
        raise ValueError('adoption must be an object')
    allowed = {'skill', 'section', 'project', 'query_id', 'source_uids', 'uses', 'draft',
               'corpus_files', 'variants', 'blueprint_cards', 'note'}
    if set(data) - allowed:
        raise ValueError('adoption accepts metadata only; put prose in the draft file')
    section = data.get('section')
    if section not in SECTIONS or data.get('skill') != f'write-{section}':
        raise ValueError('skill and section must name the same active write-* section')
    project = data.get('project')
    if not isinstance(project, str) or not project.strip():
        raise ValueError('adoption needs the actual project')
    external_path(ledger_home(home), name='ledger')
    uses = data.get('uses')
    if uses is None:
        uses = [{'query_id': data.get('query_id'), 'source_uids': data.get('source_uids')}]
    if not isinstance(uses, list) or not uses or any(not isinstance(u, dict) for u in uses):
        raise ValueError('adoption needs query-bound uses')
    events, grouped = observations(home), {}
    for use in uses:
        if set(use) != {'query_id', 'source_uids'}:
            raise ValueError('each use needs only query_id and source_uids')
        uids, _ = bound_selection(use['query_id'], use['source_uids'], catalog, events, project)
        for uid in uids:
            if not any(e.get('query_id') == use['query_id'] and e.get('state') == 'opened'
                       and uid in e.get('source_uids', [])
                       and any(r.get('uid') == uid and r.get('role') == 'corpus_card'
                               for r in e.get('read_refs', [])) for e in events):
                raise ValueError('adoption needs an actual file read; use the open operation first')
        grouped.setdefault(use['query_id'], set()).update(uids)
    uses = [{'query_id': q, 'source_uids': sorted(uids)} for q, uids in sorted(grouped.items())]
    uids = sorted({uid for use in uses for uid in use['source_uids']})
    if 'source_uids' in data and (not isinstance(data['source_uids'], list) or set(data['source_uids']) != set(uids)):
        raise ValueError('source_uids must equal the UID union of uses')
    if 'query_id' in data and (len(uses) != 1 or data['query_id'] != uses[0]['query_id']):
        raise ValueError('query_id differs from uses; multiple queries need the uses list')
    result = {'skill': data['skill'], 'section': section, 'project': project,
              'uses': uses, 'source_uids': uids}
    rows = {r['uid']: r for r in catalog['entries']}
    known_files = {r['source_file'] for r in catalog['entries']}
    markers = {f"<!-- wb:{w['paper']}:{w['item']} -->" for uid in uids for w in rows[uid]['wb_items']}
    for key in ('corpus_files', 'variants', 'blueprint_cards'):
        values = data.get(key, [])
        if not isinstance(values, list) or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError(f'{key} must be a list of actual identifiers')
        if key == 'corpus_files' and not set(values).issubset(known_files):
            raise ValueError('corpus_files contains an unregistered source')
        if key == 'variants' and not set(values).issubset(markers):
            raise ValueError('variants must be actual wb markers of the adopted UIDs')
        result[key] = sorted(set(values))
    result['corpus_files'] = sorted(set(result['corpus_files']) | {rows[u]['source_file'] for u in uids})
    if 'note' in data:
        if not isinstance(data['note'], str) or len(data['note']) > 512:
            raise ValueError('note must be a short observation, not a prose snapshot')
        result['note'] = data['note']
    return result


def draft_location(draft):
    if 'location' in draft and (not isinstance(draft['location'], str) or
                                not draft['location'].strip() or len(draft['location']) > 300):
        raise ValueError('draft location must be a short locator')


def draft_reference(draft, home=None):
    if not isinstance(draft, dict) or set(draft) - {'path', 'sha256', 'location'}:
        raise ValueError('draft reference needs path, sha256 and optional location; no prose')
    path = external_path(draft.get('path'), name='draft', home=home)
    expected = draft.get('sha256')
    if not isinstance(expected, str) or not re.fullmatch(r'[a-f0-9]{64}', expected):
        raise ValueError('draft needs its actual SHA256 fingerprint')
    if file_hash(path.read_bytes()) != expected:
        raise ValueError('draft fingerprint differs; register the revision actually saved')
    ref = {'path': str(path), 'sha256': expected}
    draft_location(draft)
    if 'location' in draft:
        ref['location'] = draft['location']
    return ref


def record_adoption(data, catalog, home=None):
    """One saved revision -> linked adopted observations plus one consumption.

    Both logs share use_id. A partial telemetry failure can be repaired by replay;
    the draft is never rewritten here and successful observations are not counted twice.
    """
    payload = prepare_adoption(data, catalog, home)
    payload['draft'] = draft_reference(data.get('draft'), home)
    identity = {k: payload[k] for k in ('skill', 'section', 'project', 'uses', 'draft')}
    payload['use_id'] = 'exu_' + digest(json.dumps(identity, ensure_ascii=False, sort_keys=True))
    if len(payload['uses']) == 1:
        payload['query_id'] = payload['uses'][0]['query_id']
    events, recorded = observations(home), []
    for use in payload['uses']:
        already = any(e.get('state') == 'adopted' and e.get('query_id') == use['query_id']
                      and e.get('use_id') == payload['use_id'] for e in events)
        event = {k: payload[k] for k in ('skill', 'section', 'project', 'draft', 'use_id')}
        event.update(use, state='adopted', actor='agent')
        recorded.append({'query_id': use['query_id'],
                         'recorded': already or record_observation(event, catalog, home)})
    prior = observations(home, 'consumption')
    consumed = any(e.get('use_id') == payload['use_id'] for e in prior)
    consumed = consumed or append_event('consumption', payload, home=home)
    return {'use_id': payload['use_id'], 'draft': payload['draft'],
            'adopted_recorded': recorded, 'consumption_recorded': consumed}


def write_adaptation(data, catalog, home=None):
    """Save UTF-8 text with create/guarded replace/guarded append, then register.

    Replaying an already-saved result repairs logging without appending text twice.
    Existing manuscripts require the caller's actual prior file fingerprint.
    """
    prepare_adoption(data, catalog, home)
    draft = data.get('draft')
    if not isinstance(draft, dict) or set(draft) - {'path', 'text', 'mode', 'expected_sha256', 'location'}:
        raise ValueError('write draft needs path, text, mode and optional expected_sha256/location')
    draft_location(draft)
    path = external_path(draft.get('path'), name='draft', home=home)
    if path.suffix.lower() not in ('.md', '.txt', '.tex', '.qmd', '.rmd', '.rst'):
        raise ValueError('write saves text drafts; use the native writer and adopt for other formats')
    if not isinstance(draft.get('text'), str) or not draft['text'].strip():
        raise ValueError('write needs the actual adapted text')
    incoming = draft['text'].encode('utf-8')
    mode = draft.get('mode', 'create')
    if mode not in ('create', 'replace', 'append'):
        raise ValueError('draft mode must be create, replace or append')
    expected = draft.get('expected_sha256')
    if mode != 'create' and (not isinstance(expected, str) or not re.fullmatch(r'[a-f0-9]{64}', expected)):
        raise ValueError('editing an existing draft needs its actual expected_sha256')
    if mode == 'create' and expected is not None:
        raise ValueError('create does not use expected_sha256')
    before = path.read_bytes() if path.exists() else None
    replay = before == incoming if mode in ('create', 'replace') else (
        before is not None and before.endswith(incoming) and file_hash(before[:-len(incoming)]) == expected)
    if not replay:
        if mode == 'create' and before is not None:
            raise ValueError('draft already exists; guarded replace or a new draft path is required')
        if mode != 'create' and (before is None or file_hash(before) != expected):
            raise ValueError('draft changed since reading; reread before editing')
        saved = (before + incoming) if mode == 'append' else incoming
        path.parent.mkdir(parents=True, exist_ok=True)
        if mode == 'create':
            with path.open('xb') as handle:
                handle.write(saved)
        else:
            # Publish a complete revision and check again immediately before replacing.
            with tempfile.NamedTemporaryFile(dir=path.parent, prefix=path.name + '.', suffix='.tmp', delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(saved)
            try:
                if file_hash(path.read_bytes()) != expected:
                    raise ValueError('draft changed during writing; reread before editing')
                os.replace(temporary, path)
            finally:
                temporary.unlink(missing_ok=True)
    else:
        saved = before
    ref = {'path': str(path), 'sha256': file_hash(saved)}
    if 'location' in draft:
        ref['location'] = draft['location']
    result = record_adoption({**data, 'draft': ref}, catalog, home)
    return {'written': True, 'replayed_saved_revision': replay, **result}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'query':
        import retrieve
        del sys.argv[1]
        return retrieve.main(record_use=True)
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('operation', choices=('open', 'write', 'adopt', 'feedback', 'show'))
    ap.add_argument('--home', type=Path, help='isolated ledger for tests')
    ap.add_argument('--query-id', help='query to inspect with show')
    args = ap.parse_args()
    try:
        if args.operation == 'show':
            result = query_chain(args.query_id, args.home)
        else:
            data = read_json_input()
            catalog = load_catalog()
            if args.operation == 'open':
                if not isinstance(data, dict) or set(data) - {'query_id', 'source_uids', 'project'}:
                    raise ValueError('open needs query_id, source_uids and optional project')
                result = open_exemplars(data.get('query_id'), data.get('source_uids'), catalog,
                                        args.home, data.get('project'))
            elif args.operation == 'write':
                result = write_adaptation(data, catalog, args.home)
            elif args.operation == 'feedback':
                if not isinstance(data, dict) or data.get('state') not in FEEDBACK_STATES:
                    raise ValueError('feedback records only an actual author_accepted or rejected evaluation')
                ok = record_observation(data, catalog, args.home)
                result = {'query_id': data['query_id'], 'feedback_recorded': ok,
                          'chain': query_chain(data['query_id'], args.home)}
            else:
                result = record_adoption(data, catalog, args.home)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, TypeError, OSError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
