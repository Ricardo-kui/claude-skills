"""Generate a searchable, source-bound view from the four native adapters.

No exemplar prose is authored here. The JSON view is disposable; canonical
cards, native adapters, and source archives remain authoritative.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
_cache_home = Path(os.environ.get('LOCALAPPDATA') or (Path.home() / '.cache'))
_workspace_key = hashlib.sha256(str(ROOT.resolve()).casefold().encode('utf-8')).hexdigest()[:12]
DEFAULT_CATALOG = _cache_home / 'claude-skills' / 'corpus-index' / _workspace_key / 'catalog.json'
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.dont_write_bytecode = True
SECTIONS = ('introduction', 'theory', 'methods', 'results')
WB = re.compile(r'<!--\s*wb:([^:>]+):([^>]+?)\s*-->')

def norm(value):
    return ' '.join(str(value).split())

def digest(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()


def write_catalog(path, rendered):
    """Publish a complete disposable view; readers never see a truncated JSON."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='\n',
                                     dir=path.parent, prefix=path.name + '.', suffix='.tmp', delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(rendered)
    try:
        # Windows can briefly hold the previous view open while another query
        # reads it. The bounded retry never publishes the temporary file early.
        for attempt in range(10):
            try:
                os.replace(temporary, path)
                break
            except PermissionError:
                if attempt == 9:
                    raise
                time.sleep(0.05)
    finally:
        temporary.unlink(missing_ok=True)

def adapter(section):
    name = f'catalog_adapter_{section}'
    spec = importlib.util.spec_from_file_location(name, ROOT / f'write-{section}/scripts/build_indices.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module

def native_entries(section):
    mod = adapter(section)
    if section == 'introduction':
        parser = mod.CardParser(mod.build_known_citekeys())
        excluded = mod.load_exclusions()
        rows = []
        for module in mod.MODULES:
            for path in sorted((mod.CORPUS / module['dir']).glob('*.md')):
                rows.extend(e for e in parser.parse(path, module['dir'], module['kind']).entries
                            if e.id not in excluded)
        mod.apply_citekey_overrides(rows, mod.load_citekey_overrides())
        return mod, rows
    if section == 'theory':
        registry, rows = mod.load_status_registry(), []
        for _, (rel, branch) in mod.VARIANT_FILES.items():
            func = mod.parse_variants if branch == 'branch1' else mod.parse_variants_branch4
            rows.extend(func('corpus/' + rel, registry, '')[0])
        for rel in mod.SUBPROTOCOL_FILES:
            rows.extend(mod.parse_subprotocols('corpus/' + rel, registry, '')[0])
        for rel in mod.SENTENCE_FILES:
            rows.extend(mod.parse_sentences('corpus/' + rel, registry, '')[0])
        mod.assign_unique_ids(rows)
        return mod, rows
    rows = []
    for family in mod.FAMILIES:
        rows.extend(mod.parse_file(family)[0])
    return mod, rows

def headings(lines):
    result, fenced = [], False
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            fenced = not fenced
        if not fenced and re.match(r'^#{1,6}\s', line.strip()):
            result.append((i, line.strip()))
    return result

def field_values(body, labels):
    """Read authored conditions as-is, including bullet continuations."""
    found, capture = [], False
    for line in body:
        s = line.strip()
        m = re.match(r'^\*\*([^*]+)\*\*\s*[:：]?\s*(.*)', s)
        if m:
            capture = any(label in m.group(1) for label in labels)
            if capture and m.group(2):
                found.append(m.group(2))
        elif s.startswith('#') or s.startswith('<!--'):
            capture = False
        elif capture and s and not s.startswith(('```', '|')):
            found.append(s.lstrip('-* ').strip())
    return found


def retrieval_metadata(body):
    """Fine moves are authored beside the exemplar, never in a duplicate corpus."""
    matches = re.findall(r'<!--\s*retrieval-move:\s*(.*?)\s*-->', '\n'.join(body), re.S)
    if len(matches) > 1:
        raise ValueError('multiple retrieval-move annotations in one source block')
    if not matches:
        return {}
    data = json.loads(matches[0])
    if not isinstance(data, dict) or not isinstance(data.get('functions'), list) or any(not isinstance(f, str) for f in data['functions']):
        raise ValueError('retrieval-move.functions must be a list of function IDs')
    if not isinstance(data.get('definitions', []), list):
        raise ValueError('retrieval-move.definitions must be a list')
    for field in ('position', 'prerequisite', 'next', 'advances'):
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            raise ValueError(f'retrieval-move.{field} must be a nonempty string')
    if 'next_evidence' in data and (not isinstance(data['next_evidence'], list) or not data['next_evidence'] or
                                   any(not isinstance(v, str) or not v.strip() for v in data['next_evidence'])):
        raise ValueError('retrieval-move.next_evidence must contain nonempty strings')
    if 'skeleton_span' in data:
        span = data['skeleton_span']
        if not isinstance(span, dict) or set(span) - {'start', 'end_before', 'functions'}:
            raise ValueError('skeleton_span requires functions/start and optional end_before')
        if not isinstance(span.get('start'), str) or not span['start'].strip() or (
                'end_before' in span and (not isinstance(span['end_before'], str) or not span['end_before'].strip())):
            raise ValueError('skeleton_span requires nonempty start/end_before cues')
        span_functions = span.get('functions', data['functions'])
        if not isinstance(span_functions, list) or not span_functions or any(
                fid not in data['functions'] for fid in span_functions):
            raise ValueError('skeleton_span.functions must name authored functions in this block')
    from request_matching import validate_applicability
    if 'applicability' in data:
        validate_applicability(data['applicability'])
    evidence = data.get('function_evidence', {})
    if not isinstance(evidence, dict):
        raise ValueError('function_evidence must be an object')
    for fid, example in evidence.items():
        if fid not in data['functions'] or not isinstance(example, dict) or set(example) != {'kind', 'cue', 'why'} or (
                example.get('kind') not in ('verbatim', 'template')) or any(
                not isinstance(example.get(k), str) or not example[k].strip() for k in ('cue', 'why')):
            raise ValueError('function_evidence requires an authored function and kind/cue/why')
    support = data.get('function_support', {})
    if not isinstance(support, dict) or any(k not in data['functions'] or v not in ('complete', 'partial')
                                            for k, v in support.items()):
        raise ValueError('function_support must name an authored function and complete/partial')
    if 'sequence' in data:
        steps = data['sequence']
        if not isinstance(steps, list) or len(steps) < 2 or any(
                not isinstance(s, dict) or s.get('function') not in data['functions'] or
                s.get('kind') not in ('verbatim', 'template') or
                not isinstance(s.get('cue'), str) or not s['cue'].strip() for s in steps):
            raise ValueError('sequence requires at least two authored function/kind/cue steps')
    return data


def collect_function_definitions(records, bridge):
    """Derive action contracts from their sole owning card blocks."""
    definitions, owners, blocks = {}, {}, {}
    for row in records:
        blocks.setdefault(row['parent_paragraph'], []).append(row)
        for definition in row.get('retrieval_move', {}).get('definitions', []):
            if not isinstance(definition, dict):
                raise ValueError('function definition must be an object')
            for field in ('id', 'label', 'section', 'refines', 'definition'):
                if not isinstance(definition.get(field), str) or not definition[field].strip():
                    raise ValueError(f'function definition requires {field}')
            fid = definition['id']
            if definition['section'] != row['section']:
                raise ValueError(f'{fid}: definition section differs from owning card')
            for field in ('use_when', 'aliases'):
                values = definition.get(field)
                if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
                    raise ValueError(f'{fid}: {field} must contain nonempty strings')
            neighbors = definition.get('neighbors')
            if not isinstance(neighbors, list) or not neighbors:
                raise ValueError(f'{fid}: requires neighboring functions')
            for neighbor in neighbors:
                if not isinstance(neighbor, dict) or any(not isinstance(neighbor.get(k), str) or not neighbor[k].strip() for k in ('id', 'distinction')):
                    raise ValueError(f'{fid}: neighbor requires id and distinction')
            positive, mismatch = definition.get('positive_example'), definition.get('mismatch_example')
            if not isinstance(positive, dict) or positive.get('kind') not in ('verbatim', 'template') or any(not isinstance(positive.get(k), str) or not positive[k].strip() for k in ('cue', 'why')):
                raise ValueError(f'{fid}: positive example requires a card excerpt kind, cue and why')
            if not isinstance(mismatch, dict) or mismatch.get('kind') != 'illustrative' or any(not isinstance(mismatch.get(k), str) or not mismatch[k].strip() for k in ('text', 'why', 'actual_function')):
                raise ValueError(f'{fid}: mismatch must be an explicitly illustrative example')
            owner = row['parent_paragraph']
            if fid in definitions and (owners[fid] != owner or definitions[fid] != definition):
                raise ValueError(f'{fid}: multiple authoritative definition blocks')
            definitions[fid], owners[fid] = definition, owner
    known = {spec['id']: spec for spec in bridge}
    known.update(definitions)
    for fid, definition in definitions.items():
        parent = definition['refines']
        if parent not in known or known[parent]['section'] != definition['section'] or parent == fid:
            raise ValueError(f'{fid}: invalid parent function {parent}')
        trail, current = {fid}, parent
        while current in definitions:
            if current in trail:
                raise ValueError(f'{fid}: cyclic refinement')
            trail.add(current)
            current = definitions[current]['refines']
        for target in [n['id'] for n in definition['neighbors']] + [definition['mismatch_example']['actual_function']]:
            if target not in known or target == fid:
                raise ValueError(f'{fid}: unknown or self-referencing adjacent function {target}')
        rows = blocks[owners[fid]]
        positive = definition['positive_example']
        if not any(r['kind'] == positive['kind'] and norm(positive['cue']) in norm(r['text']) for r in rows):
            raise ValueError(f'{fid}: positive example cue is absent from its owning {positive["kind"]} excerpt')
    for row in records:
        for fid in row.get('retrieval_move', {}).get('functions', []):
            if fid not in known or known[fid]['section'] != row['section']:
                raise ValueError(f'{row["source_file"]}: invalid authored function {fid}')
    # Validate authored sequences against the same native source block. Runtime
    # matching additionally checks the requested order and single-paper binding.
    for rows in blocks.values():
        meta = rows[0].get('retrieval_move', {})
        for fid, example in meta.get('function_evidence', {}).items():
            if not any(r['kind'] == example['kind'] and norm(example['cue']) in norm(r['text']) for r in rows):
                raise ValueError(f'{rows[0]["source_file"]}: {fid} function_evidence cue absent from its owning {example["kind"]} excerpt')
        span = meta.get('skeleton_span')
        if span:
            matches = []
            for row in rows:
                if row['kind'] != 'template' or row['text'].count(span['start']) != 1:
                    continue
                start = row['text'].find(span['start'])
                if 'end_before' not in span or row['text'].find(span['end_before'], start + len(span['start'])) >= 0:
                    matches.append(row['uid'])
            if len(matches) != 1:
                raise ValueError(f'{rows[0]["source_file"]}: skeleton_span must select one existing template range')
        for step in meta.get('sequence', []):
            if not any(r['kind'] == step['kind'] and norm(step['cue']) in norm(r['text']) for r in rows):
                raise ValueError(f'{rows[0]["source_file"]}: sequence cue absent from its owning {step["kind"]} excerpt')
        if meta.get('sequence') and all(s['kind'] == 'verbatim' for s in meta['sequence']):
            from request_matching import action_sequence
            result = action_sequence(rows, [{'id': s['function']} for s in meta['sequence']])
            if result['state'] not in ('source_bound_order', 'excerpt_order_source_pending'):
                raise ValueError(f'{rows[0]["source_file"]}: sequence must preserve order within one source')
    result = []
    for fid, definition in sorted(definitions.items()):
        row = blocks[owners[fid]][0]
        result.append({**definition, 'source': {k: row[k] for k in
                       ('source_file', 'source_line', 'source_anchor', 'parent_paragraph')}})
    return result


def quickref_conditions(lines, vid):
    """Use an authored unique variant row; never guess among repeated ordinals."""
    found, headers = [], []
    for i, line in enumerate(lines):
        if not line.startswith('|'):
            headers = []
            continue
        cells = [s.strip() for s in line.strip('|').split('|')]
        if '适用场景' in cells:
            headers = cells
            continue
        if headers and len(cells) == len(headers) and cells[0].strip('`# ') == vid:
            found.append((cells[headers.index('适用场景')], i + 1))
    return found[0] if len(found) == 1 else ('', None)


def governed_status(section, entry, rel, markers, current, registry, rv, policy):
    """Carry explicit rulings/policy floors; never infer ratings from 1 source."""
    normalize_key = lambda s: re.sub(r'[\s_\-]+', '', str(s)).lower()
    overrides = (registry.get('status_overrides') or {}).get('overrides') or {}
    pattern = entry.id.split('.')[0].split('~')[0]
    item_ids = {m['item'] for m in markers}
    paper = normalize_key(entry.citekey)
    scopes = []
    for path, decision in overrides.items():
        if not isinstance(decision, dict) or not decision.get('status'):
            continue
        level = None
        if '.by_source_paper.' in path and normalize_key(path.split('.by_source_paper.',1)[1]) == paper:
            level = 'source_paper_override'
        elif section == 'introduction' and path == f'evidence.{Path(rel).parent.name}.{Path(rel).stem}':
            level = 'card_override'
        elif section == 'theory' and path == f'patterns.{pattern}':
            level = 'pattern_override'
        elif '.skeleton_variants.' in path and path.rsplit('.',1)[-1] in item_ids:
            level = 'pattern_override'
        if level:
            scopes.append({'scope':level, 'registry_path':path,
                           'status':rv.norm_status(str(decision['status'])), 'basis':decision.get('basis','')})
    specific = [s for s in scopes if s['scope'] != 'source_paper_override']
    authoritative = specific or scopes
    if authoritative:
        values = {s['status'] for s in authoritative}
        if len(values) == 1:
            return authoritative[0]['status'], authoritative
        # Conflicting explicit scopes are surfaced, not flattened by a ladder.
        return current, authoritative + [{'scope':'conflicting_overrides', 'status':current}]
    pstat, rule = rv.policy_status([entry.citekey], 1, policy,
                                  auxiliary=rv.source_is_auxiliary(registry,entry.citekey))
    if pstat:
        order = {'unrated':-1,'未标注':-1,'EMERGING':0,'VERIFIED':1,'ROBUST':2}
        if order.get(pstat,-1) > order.get(current,-1):
            return pstat, [{'scope':'existing_status_policy', 'status':pstat,'basis':rule}]
    return current, [{'scope':'native_or_card', 'status':current}]

def locate(section, mod, entry, lines):
    hs = headings(lines)
    if section == 'theory':
        candidates = [i for i, h in hs if h == entry.heading]
    elif section == 'introduction' and entry.anchor.startswith('标题-'):
        ordinal = int(entry.anchor.split('-')[1]) - 1
        candidates = [hs[ordinal][0]] if ordinal < len(hs) else []
    elif section in ('methods', 'results'):
        candidates = [i for i, h in hs if re.search(
            r'^#{3,4}\s+变体\s*[:：]?\s*' + re.escape(entry.vid) + r'(?:\s|[:：（(]|$)', h)]
        if not candidates and entry.vid.startswith(('unnum', 'extend')):
            candidates = [i for i, h in hs if entry.anchor.split('#')[-1] in h]
    else:
        candidates = []
    # For lexical tables and repeated headings, locate the excerpt itself.
    needle = norm(entry.text).strip('"')
    if len(candidates) != 1:
        for i, h in hs:
            end = next((j for j, _ in hs if j > i), len(lines))
            clean = norm(' '.join(re.sub(r'^\s*>\s?', '', s) for s in lines[i:end]))
            if needle in clean:
                candidates = [i]
                break
    if not candidates:
        # Honest fallback: full card context, not a fabricated line anchor.
        return 0, len(lines), '', 'card_only'
    start = candidates[0]
    level = len(lines[start]) - len(lines[start].lstrip('#'))
    # Theory/Intro adapters end a source block at the next heading. Methods/
    # Results variants include named technical/anchor subsections (####), but
    # do not inherit metadata from the following variant.
    end = next((j for j, h in hs if j > start and (section in ('theory', 'introduction')
                or len(h) - len(h.lstrip('#')) <= level)), len(lines))
    return start, end, lines[start].lstrip('#').strip(), 'block'

def catalog_entries():
    records, sources = [], {}
    import yaml
    sys.path.insert(0, str(ROOT / 'distill-paper-exemplar/scripts'))
    import rebuild_views as rv
    policy = rv.load_policy()
    for section in SECTIONS:
        mod, rows = native_entries(section)
        registry = yaml.safe_load((ROOT/f'write-{section}/corpus/_evidence_registry.yaml').read_text(encoding='utf-8'))
        for entry in rows:
            rel = entry.file if section == 'theory' else entry.path
            source = ROOT / f'write-{section}' / rel
            key = source.relative_to(ROOT).as_posix()
            if key not in sources:
                raw = source.read_text(encoding='utf-8')
                sources[key] = (raw.splitlines(), digest(raw))
            lines, source_hash = sources[key]
            start, end, title, resolution = locate(section, mod, entry, lines)
            body = lines[start:end]
            conditions = field_values(body, ('适用', '条件', '触发'))
            conditions_line = start + 1 if conditions else None
            if not conditions and section in ('methods', 'results'):
                condition, conditions_line = quickref_conditions(lines, entry.vid)
                conditions = [condition] if condition else []
            kind = entry.kind if section == 'theory' else entry.status
            kind = 'verbatim' if kind == 'verbatim' else 'template'
            uid = section + ':' + digest('\0'.join((rel, entry.anchor, kind, norm(entry.text))))[:24]
            text_hash = digest(norm(entry.text))
            markers = [{'paper': m.group(1).strip(), 'item': m.group(2).strip()}
                       for m in WB.finditer('\n'.join(body))]
            # Variant subheadings may precede a wb marker at the end of the
            # entire variant. Include that containing variant, not the file.
            if not markers and section in ('methods', 'results'):
                parents = [i for i, h in headings(lines) if i <= start and re.match(r'^###\s+变体', h)]
                if parents:
                    ps = parents[-1]
                    pe = next((i for i, h in headings(lines) if i > ps and re.match(r'^#{1,3}\s', h)), len(lines))
                    markers = [{'paper': m.group(1).strip(), 'item': m.group(2).strip()}
                               for m in WB.finditer('\n'.join(lines[ps:pe]))]
            native = entry.func if section == 'theory' else getattr(entry, 'slot', Path(rel).parent.name)
            status = entry.status if section == 'theory' else ''
            if not status:
                sm = re.search(r'(?:验证状态|状态)\*\*\s*[:：]\s*(ROBUST|VERIFIED|EMERGING)', '\n'.join(body))
                status = sm.group(1) if sm else 'unrated'
            status, status_basis = governed_status(section, entry, rel, markers, status, registry, rv, policy)
            provenance = 'card_verbatim' if kind == 'verbatim' and entry.citekey != '未标注' else (
                'source_pending' if kind == 'verbatim' else 'card_template')
            source_key_kind = ('missing' if entry.citekey == '未标注' else
                               'multiple_keys' if '/' in entry.citekey else
                               'single_key' if re.fullmatch(r'[A-Za-z0-9_.-]+',entry.citekey) else 'reference_string')
            records.append({
                'uid': uid, 'section': section, 'id': entry.id, 'kind': kind,
                'text': entry.text, 'citekey': entry.citekey, 'status': status,
                'status_basis':status_basis,
                'native_function': native, 'family': Path(rel).stem,
                'block_title': title, 'source_file': key, 'source_anchor': entry.anchor,
                'source_line': start + 1 if resolution == 'block' else None,
                'source_end_line': end, 'context_resolution': resolution,
                'source_sha256': source_hash, 'text_sha256': text_hash,
                'parent_paragraph': section + ':' + digest(key + '\0' + str(start) + '\0' + title)[:24],
                'source_excerpt_id': 'excerpt:' + digest(entry.citekey + '\0' + norm(entry.text))[:24],
                'provenance_level': provenance,
                'source_key_kind':source_key_kind,
                'use_conditions': conditions,
                'use_conditions_source_line': conditions_line,
                'nontransferable': field_values(body, ('禁忌', '反模式', '注意事项', '边界')),
                'learnable_move': field_values(body, ('功能节拍', '微观动作序列', '关键特征', '为什么有效', '与原骨架差异', '句位')),
                'retrieval_move': retrieval_metadata(body),
                'wb_items': markers,
            })
    ids = [r['uid'] for r in records]
    if len(set(ids)) != len(ids):
        raise ValueError('catalog contains duplicate UIDs')
    bridge = json.loads((ROOT / '_shared/indexing/retrieval-functions.json').read_text(encoding='utf-8'))['functions']
    function_definitions = collect_function_definitions(records, bridge)
    dependencies = {k: h for k, (_, h) in sources.items()}
    from source_context import attach_contexts
    dependencies.update(attach_contexts(records,ROOT,digest))
    for section in SECTIONS:
        for rel in ('scripts/build_indices.py', 'corpus/_evidence_registry.yaml'):
            path = ROOT / f'write-{section}' / rel
            dependencies[path.relative_to(ROOT).as_posix()] = digest(path.read_text(encoding='utf-8'))
    for rel in ('_shared/indexing/build_catalog.py', '_shared/indexing/indexing_engine.py',
                '_shared/indexing/source_context.py',
                '_shared/indexing/request_matching.py',
                '_shared/indexing/retrieval-functions.json',
                'distill-paper-exemplar/scripts/rebuild_views.py',
                'distill-paper-exemplar/scripts/status_policy.yaml',
                'write-introduction/scripts/skeleton_exclusions.txt',
                'write-introduction/scripts/citekey_overrides.yaml'):
        path = ROOT / rel
        if path.is_file():
            dependencies[rel] = digest(path.read_text(encoding='utf-8'))
    return {'schema_version': 2, 'dependencies': dependencies, 'entries': records,
            'function_definitions': function_definitions,
            'summary': {'entries': len(records), 'sections': dict(Counter(r['section'] for r in records)),
                        'fine_functions': len(function_definitions),
                        'archive_contexts':dict(Counter(r['source_context']['state'] for r in records if r['kind']=='verbatim')),
                        'card_only': sum(r['context_resolution'] == 'card_only' for r in records)}}

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, default=DEFAULT_CATALOG)
    ap.add_argument('--check', action='store_true', help='validate in memory; compare cache if present; do not write')
    args = ap.parse_args()
    data = catalog_entries()
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + '\n'
    if args.check:
        if args.out.is_file() and args.out.read_text(encoding='utf-8') != rendered:
            print('CATALOG DRIFT: regenerate build_catalog.py')
            return 1
        if not args.out.is_file():
            print('CATALOG NOT CACHED: native corpus validated in memory')
    else:
        write_catalog(args.out, rendered)
    print(json.dumps(data['summary'], ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
