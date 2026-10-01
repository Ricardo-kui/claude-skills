"""Writing-time function-first exemplar retrieval over native corpus adapters."""
from __future__ import annotations
import argparse
import json
import math
import re
import sys
import uuid
from collections import Counter, defaultdict
from pathlib import Path
import build_catalog as bc
import request_matching as rm
import adaptation_cards as ac

FUNCTIONS = Path(__file__).with_name('retrieval-functions.json')


def load_catalog(path=bc.DEFAULT_CATALOG):
    """Refresh a disposable view when a dependency changes, including new cards."""
    try:
        data = json.loads(path.read_text(encoding='utf-8')) if path.is_file() else None
    except (json.JSONDecodeError, FileNotFoundError):
        data = None
    if data is not None and (not isinstance(data, dict) or not isinstance(data.get('dependencies'), dict) or
                             not isinstance(data.get('entries'), list)):
        data = None
    stale = data is None
    if data:
        for rel, expected in data['dependencies'].items():
            p = bc.ROOT / rel
            if not p.is_file() or bc.digest(p.read_text(encoding='utf-8')) != expected:
                stale = True
                break
        known = set(data['dependencies'])
        from source_context import ARCHIVE_REL
        archives={p.relative_to(bc.ROOT).as_posix() for p in (bc.ROOT/ARCHIVE_REL).glob('*.sentences.md')}
        if archives != {p for p in known if p.startswith(ARCHIVE_REL+'/') and p.endswith('.sentences.md')}:
            stale=True
        if not stale:
            for sec in bc.SECTIONS:
                mod = bc.adapter(sec)
                # Native parsers decide what is an asset; added/removed assets
                # also invalidate the view, even if no old file has changed.
                paths = (set(p.relative_to(bc.ROOT).as_posix()
                             for module in mod.MODULES
                             for p in (mod.CORPUS / module['dir']).glob('*.md'))
                         if sec == 'introduction' else
                         set(f'write-{sec}/corpus/{rel}' for rel in
                             ([v[0] for v in mod.VARIANT_FILES.values()] + mod.SUBPROTOCOL_FILES + mod.SENTENCE_FILES
                              if sec == 'theory' else [f['file'] for f in mod.FAMILIES])))
                if not paths.issubset(known):
                    stale = True
                    break
    if stale:
        data = bc.catalog_entries()
        bc.write_catalog(path, json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    return data


def function_specs(catalog=None):
    """Card-authored definitions supply semantics; the bridge supplies legacy rules."""
    data = catalog if catalog is not None else load_catalog()
    specs = {s['id']: dict(s) for s in json.loads(FUNCTIONS.read_text(encoding='utf-8'))['functions']}
    for definition in data.get('function_definitions', []):
        spec = specs.setdefault(definition['id'], {'id': definition['id'], 'selector': r'(?!)'})
        spec.update(definition)
        spec['description'] = definition['definition']
    for spec in specs.values():
        spec.setdefault('aliases', [])
    return list(specs.values())


CONCEPTS = {
    '共同所有权': ['common ownership', 'common owners'],
    '产品召回': ['product recall', 'recalls'],
    '董事会': ['board', 'directors', 'governance'],
    '高管': ['executive', 'ceo', 'tmt', 'top management'],
    '竞争': ['competition', 'competitive', 'rival'],
    '创新': ['innovation', 'patent'],
    '污名': ['stigma', 'stigmatized'],
    '声誉': ['reputation', 'reputational'],
    '地位': ['status', 'prestige'],
    '学习': ['learning', 'learn'],
    '风险': ['risk', 'uncertainty'],
    '制度': ['institutional', 'institution', 'regulation'],
    '激进主义': ['activism', 'activist'],
    '员工': ['employee', 'workers'],
    '女性': ['female', 'women', 'gender'],
    '网络': ['network', 'ties', 'connections'],
    '注意力': ['attention', 'attentional'],
    '稀有事件': ['rare event', 'rare outcome', 'low incidence'],
    '固定效应': ['fixed effects', 'fixed-effects', 'firm fe'],
    '工具变量': ['instrumental', 'instrument', '2sls'],
    '双重差分': ['difference-in-differences', 'did', 'diff-in-diff'],
    '事件研究': ['event study', 'event-study', 'abnormal returns'],
    '生存分析': ['survival', 'hazard', 'cox'],
    '实验': ['experiment', 'randomization', 'randomized'],
    '定性': ['qualitative', 'interview', 'ethnography'],
    '中介': ['mediation', 'mediator', 'indirect effect'],
    '调节': ['moderation', 'moderator', 'interaction'],
    '非显著': ['non-significant', 'nonsignificant', 'not significant', 'null'],
}


def terms(query):
    expanded = []
    lower = query.lower()
    for zh, en in CONCEPTS.items():
        if zh in lower or any(w in lower for w in en):
            expanded.append([zh] + en)
            lower = lower.replace(zh, ' ')
    stops = {'a', 'an', 'the', 'of', 'to', 'in', 'and', 'for', 'with', 'how', 'we',
             'write', 'sentence', 'paragraph', 'explain', 'show', 'want'}
    words = re.findall(r'[a-z][a-z0-9-]{2,}|[\u4e00-\u9fff]{2,}', lower)
    for w in dict.fromkeys(words):
        if w not in stops and not any(any(w in phrase for phrase in g) for g in expanded):
            expanded.append([w])
    return expanded


def resolve_function(value, section=None, catalog=None):
    if not value:
        return None
    candidates = []
    for spec in function_specs(catalog):
        if section and spec['section'] != section:
            continue
        if value == spec['id']:
            return spec
        matches = [a for a in spec.get('aliases', []) if a.lower() in value.lower()]
        if matches:
            candidates.append((max(map(len, matches)), spec))
    if not candidates:
        return None
    candidates.sort(key=lambda x: x[0], reverse=True)
    if len(candidates) > 1 and candidates[0][0] == candidates[1][0]:
        return None  # ambiguous function requires an explicit choice
    return candidates[0][1]


def function_match(record, spec):
    if not spec or record['section'] != spec['section']:
        return 0
    if spec['id'] in record.get('retrieval_move', {}).get('functions', []):
        return 2 if record['retrieval_move'].get('function_support', {}).get(spec['id']) == 'partial' else 4
    if not re.search(spec['selector'], record['source_file'] + ' ' + record['native_function'], re.I):
        return 0
    label = record['block_title'] if spec.get('title_only') else (
        record['block_title'] + ' ' + record['native_function'] + ' ' + ' '.join(record['use_conditions']))
    if spec.get('exclude_title') and re.search(spec['exclude_title'], record['block_title'], re.I):
        return 0
    focused = spec.get('focus') and re.search(spec['focus'], label, re.I)
    if spec.get('require_focus') and not focused:
        return 0
    if focused:
        return 3
    return 1


def resolve_request(function, query, need, section=None, catalog=None):
    """Refine an explicitly chosen family using the authored writing need."""
    spec = (resolve_function(function, section, catalog) if function else
            resolve_function(need, section, catalog) or resolve_function(query, section, catalog))
    if not spec or not need:
        return spec
    children = [s for s in function_specs(catalog) if s.get('refines') == spec['id']]
    matches = [(max(len(a) for a in s['aliases'] if a.lower() in need.lower()), s)
               for s in children if any(a.lower() in need.lower() for a in s['aliases'])]
    matches.sort(key=lambda x: x[0], reverse=True)
    if matches and (len(matches) == 1 or matches[0][0] > matches[1][0]):
        return matches[0][1]
    return spec


def parse_request(function, query, need, section, catalog, actions=None):
    """Resolve ordered actions without discarding an unrecognized second step."""
    family = resolve_function(function, section, catalog) if function else None
    if function and not family:
        return [], {'mode': 'unresolved', 'actions': [], 'certainty': 'unknown'}, 'unknown_or_ambiguous_function'
    if actions is not None and (not isinstance(actions, list) or not actions or
                               any(not isinstance(a, str) or not a.strip() for a in actions)):
        raise ValueError('actions must be a nonempty ordered string list')
    clauses = actions if actions is not None else rm.split_actions(need)
    if actions is not None or len(clauses) > 1:
        steps, specs = [], []
        for clause in clauses:
            spec = resolve_function(clause, section or (family['section'] if family else None), catalog)
            steps.append({'text': clause, 'function': spec['id'] if spec else None,
                          'basis': 'explicit_id' if spec and clause == spec['id'] else 'alias_inference',
                          'certainty': 'declared' if spec and clause == spec['id'] else 'inferred' if spec else 'unknown'})
            if spec:
                specs.append(spec)
        # An existing fine action can itself define a multi-clause move (e.g.
        # concession + direction response). Keep that contract when every
        # clause resolves to it; explicit repeated --action steps stay ordered.
        if actions is None and len(specs) == len(clauses) and len({s['id'] for s in specs}) == 1:
            specs = specs[:1]
            mode = 'single_defined_move'
        else:
            mode = 'sequence' if len(steps) > 1 else 'single_action'
        parsed = {'mode': mode, 'actions': steps, 'certainty': 'declared' if all(
            s['certainty'] == 'declared' for s in steps) else 'inferred',
            'basis': 'structured_actions' if actions is not None else 'ordered_need'}
        if len(steps) != sum(s['function'] is not None for s in steps):
            parsed['certainty'] = 'unknown'
            parsed['unresolved_actions'] = [s['text'] for s in steps if not s['function']]
            return specs, parsed, 'unresolved_action_sequence'
        if len({s['section'] for s in specs}) > 1:
            return specs, {**parsed, 'certainty': 'unknown'}, 'cross_section_action_sequence'
        return specs, parsed, None
    spec = resolve_request(function, query, need, section, catalog)
    exact = bool(spec and function == spec['id'])
    parsed = {'mode': 'single_action' if spec else 'content_only',
              'actions': [{'text': need or function or query, 'function': spec['id'],
                           'basis': 'explicit_id' if exact else 'alias_inference',
                           'certainty': 'declared' if exact else 'inferred'}] if spec else [],
              'certainty': 'declared' if exact else 'inferred' if spec else 'unknown',
              'basis': 'explicit_function' if exact else 'need_or_query_alias'}
    return [spec] if spec else [], parsed, None


def function_checks(rows, specs):
    checks = []
    for spec in specs:
        fit = max((function_match(r, spec) for r in rows), default=0)
        # Complete, card-authored original evidence establishes the action even
        # when its wording differs from the legacy connector patterns. Partial
        # tags, templates and missing cues retain the lexical/source checks.
        authored = any(r['kind'] == 'verbatim' and
                       r.get('retrieval_move', {}).get('function_support', {}).get(spec['id']) == 'complete'
                       and ac.authored_original_uids([r], r['retrieval_move'], spec['id']) for r in rows)
        text = ' '.join(r['text'] for r in rows if not spec.get('require_original') or r['kind'] == 'verbatim')
        missing = [] if authored else [p for p in spec.get('required_text', []) if not re.search(p, text, re.I)]
        same_source = True
        if spec.get('require_original') and not authored:
            sources = defaultdict(list)
            for row in rows:
                if row['kind'] == 'verbatim':
                    key = row['citekey'] if row.get('source_key_kind') == 'single_key' else row['uid']
                    sources[key].append(row['text'])
            same_source = any(all(re.search(p, ' '.join(prose), re.I) for p in spec.get('required_text', []))
                              for prose in sources.values())
        checks.append({'id': spec['id'], 'level': fit, 'complete': bool(fit and not missing and same_source),
                       'basis': 'authored_metadata' if fit in (2, 4) else 'lexical_rule',
                       'certainty': 'tagged' if fit == 4 else 'partial' if fit == 2 else 'inferred' if fit else 'unmatched',
                       'expression_check_basis': 'authored_original_evidence' if authored else 'lexical_rule',
                       'original_support': 'same_source' if same_source and spec.get('require_original') else
                                           'missing_or_split_source' if not same_source else 'not_required',
                       'missing_expression_checks': missing})
    return checks


def retrieval_version(data):
    return {'ranker': bc.digest(Path(__file__).read_text(encoding='utf-8') + '\0' +
                              Path(rm.__file__).read_text(encoding='utf-8') + '\0' +
                              Path(ac.__file__).read_text(encoding='utf-8')),
            'functions': bc.digest(FUNCTIONS.read_text(encoding='utf-8')),
            'corpus': bc.digest(json.dumps(data['dependencies'], sort_keys=True))}


def search(query='', function=None, section=None, design='', top=3, catalog=None,
           require_content=False, evidence='', status=None, need='', query_id=None,
           conditions=None, actions=None, supplement_top=2):
    data = catalog or load_catalog()
    requested = rm.request_conditions(conditions, design)
    trace = {'query_id': query_id or 'exr_' + uuid.uuid4().hex,
             'retrieval_version': retrieval_version(data),
             'request': {'query': query, 'need': need, 'function': function, 'section': section,
                         'design': design, 'evidence': evidence, 'status': status,
                         'conditions': conditions, 'actions': actions, 'supplement_top': supplement_top,
                         'require_content': require_content, 'top': top}}
    specs, parsed, error = parse_request(function, query, need, section, data, actions)
    spec = specs[0] if len(specs) == 1 else None
    if error:
        return {**trace, 'query': query, 'function': spec['id'] if spec else function,
                'functions': [s['id'] for s in specs], 'parsed_request': parsed,
                'conditions': requested, 'candidates': [], 'supplementary_candidates': [], 'reason': error,
                'available_functions': [s['id'] for s in function_specs(data) if not section or s['section'] == section]}
    if specs:
        section = specs[0]['section']
    qterms = terms(query)
    dterms = terms(design)
    eterms = terms(evidence)
    records = [r for r in data['entries'] if (not section or r['section'] == section)
               and (not status or r['status'] in status)]
    blocks = defaultdict(list)
    for r in records:
        blocks[r['parent_paragraph']].append(r)
    documents = {}
    for key, rows in blocks.items():
        r = rows[0]
        documents[key] = (' '.join([r['block_title'], r['family'], r['native_function'],
                                   *r['use_conditions'], *(x['text'] for x in rows)])).lower()
    df = [sum(any(t in doc for t in group) for doc in documents.values()) for group in qterms]
    ranked, supplementary = [], []
    counts = Counter(blocks_seen=len(blocks))
    for key, rows in blocks.items():
        checks = function_checks(rows, specs)
        fit = min((c['level'] for c in checks), default=0)
        matched = not specs or all(c['complete'] for c in checks)
        sequence = rm.action_sequence(rows, specs)
        ordered = sequence['state'] in ('single_action', 'source_bound_order', 'excerpt_order_source_pending')
        if matched and specs:
            counts['function_candidates'] += 1
        condition_check = rm.applicability(rows, requested)
        if condition_check['state'] == 'incompatible':
            if matched:
                counts['condition_conflicts'] += 1
            continue  # known conflicts cannot reappear as topic supplements
        doc = documents[key]
        # Preserve legacy free-text constraints. Structured conditions compare
        # authored assertions, never keyword mentions (including negations).
        has_design = bool(rows[0].get('retrieval_move', {}).get('applicability', {}).get('design'))
        if dterms and not ('design' in requested and has_design) and not all(any(t in doc for t in group) for group in dterms):
            continue
        if eterms and not all(any(t in doc for t in group) for group in eterms):
            continue
        hits = [i for i, group in enumerate(qterms) if any(t in doc for t in group)]
        if (require_content or not specs) and not hits:
            continue
        score = sum(math.log(1 + (len(documents) + 1) / (df[i] + 1)) for i in hits)
        title_hits = sum(any(t in rows[0]['block_title'].lower() for t in group) for group in qterms)
        item = {'fit': fit, 'score': score, 'key': key, 'rows': rows, 'hits': hits,
                'title_hits': title_hits, 'function_checks': checks, 'sequence': sequence,
                'condition_check': condition_check, 'source_support': rm.source_support(rows)}
        if matched and ordered:
            ranked.append(item)
        elif specs and hits and supplement_top > 0:
            item['supplement_reason'] = 'unverified_action_sequence' if matched and not ordered else 'function_mismatch_or_incomplete'
            supplementary.append(item)
        if matched and not ordered:
            counts['sequences_unverified'] += 1
    order = lambda x: (-x['fit'], -x['condition_check']['rank'], -x['score'],
                       -x['title_hits'], -x['source_support']['rank'], x['key'])
    ranked.sort(key=order)
    supplementary.sort(key=order)
    counts['primary_eligible'], counts['supplementary_eligible'] = len(ranked), len(supplementary)
    candidates, supplements, seen = [], [], set()
    for item in ranked + supplementary:
        is_supplement = 'supplement_reason' in item
        destination = supplements if is_supplement else candidates
        if len(destination) >= (supplement_top if is_supplement else max(1, top)):
            continue
        fit, score, key, rows, hits, title_hits = (item[k] for k in ('fit', 'score', 'key', 'rows', 'hits', 'title_hits'))
        ordered = item['sequence']['state'] in ('single_action', 'source_bound_order', 'excerpt_order_source_pending')
        originals = [r for r in rows if r['kind'] == 'verbatim']
        templates = [r for r in rows if r['kind'] == 'template']
        # Keep all excerpts in the same source block, do not fabricate a pair.
        signatures = {r['source_excerpt_id'] for r in originals or templates}
        if signatures and signatures.issubset(seen):
            continue
        seen.update(signatures)
        first = max(rows, key=lambda r: (sum(function_match(r, s) for s in specs), r['kind'] == 'verbatim')) if specs else rows[0]
        path = bc.ROOT / first['source_file']
        source_lines = path.read_text(encoding='utf-8').splitlines()
        destination.append({
            'rank': len(candidates) + len(supplements) + 1,
            'candidate_role': 'supplementary' if is_supplement else 'primary',
            'supplement_reason': item.get('supplement_reason'),
            'function_fit': 'specific_move' if fit >= 3 else 'partial_move' if fit == 2 else ('native_family' if fit else 'content_only'),
            'function_match_basis': 'authored_metadata' if fit in (2, 4) else 'lexical_rule',
            'function_matching': {'actions': item['function_checks'], 'sequence': item['sequence'],
                                  'uncertain': parsed['certainty'] != 'declared' or any(c['level'] != 4 for c in item['function_checks']) or not ordered or is_supplement},
            'condition_check': item['condition_check'], 'source_support': item['source_support'],
            'function_definition': spec.get('description', '') if spec else ' → '.join(s.get('description', s['id']) for s in specs),
            'retrieval_move': first.get('retrieval_move', {}),
            'replaceable_slots': sorted({slot for r in templates for slot in re.findall(r'\[[^\[\]\n]+\]', r['text'])}),
            'title_content_matches': title_hits,
            'content_matches': [qterms[i] for i in hits], 'content_score': round(score, 3),
            'matched_terms': [{'concept': qterms[i][0], 'matched': [t for t in qterms[i] if t in documents[key]]} for i in hits],
            'content_coverage': round(len(hits)/len(qterms), 3) if qterms else None,
            'block_title': first['block_title'], 'source_file': first['source_file'],
            'source_line': first['source_line'], 'source_end_line': first['source_end_line'],
            'use_conditions_source_line': first['use_conditions_source_line'],
            'native_function': first['native_function'], 'parent_paragraph': key,
            'native_functions': sorted({r['native_function'] for r in rows}),
            'originals': [brief(r) for r in originals], 'templates': [brief(r) for r in templates],
            'use_conditions': first['use_conditions'], 'nontransferable': first['nontransferable'],
            'learnable_move': first['learnable_move'],
            'context': '\n'.join(source_lines[(first['source_line'] or 1)-1:first['source_end_line']]),
            'preceding_context': '\n'.join(source_lines[max(0,(first['source_line'] or 1)-9):(first['source_line'] or 1)-1]),
            'following_context': '\n'.join(source_lines[first['source_end_line']:first['source_end_line']+8]),
            'limitations': ([] if originals else ['此块未抽取到原文，须查看卡片或来源档案']) +
                           (['功能由需求别名或词法规则推断，须核对当前动作'] if parsed['certainty'] != 'declared' or any(c['level'] not in (2, 4) for c in item['function_checks']) else []) +
                           (['此块仅部分支持所需动作，须阅读前文并补足论证'] if fit == 2 else []) +
                           (['适用条件尚未确认：' + '、'.join(item['condition_check']['unknowns'])] if item['condition_check']['state'] == 'unknown' else []) +
                           (['未进行结构化适用条件核验'] if item['condition_check']['state'] == 'not_checked' else []) +
                           (['仅为补充候选，未完成所需功能或未确认连续动作顺序'] if is_supplement else []) +
                           ([] if first['use_conditions'] else ['此块未结构化标注适用条件，需人工判断']) +
                           ([] if hits or not qterms else ['没有内容词命中；仅作为同功能的异主题候选']) +
                           (['此块有原句缺来源键，不称为已确认顶刊摘录'] if any(r['provenance_level']=='source_pending' for r in originals) else []) +
                           (['此块有来源字符串或多来源键，仍需消歧到单篇论文'] if any(r['source_key_kind'] in ('reference_string','multiple_keys') for r in originals) else []) +
                           (['摘录命中档案，但来源键作者/年份有差异；须核对别名、年份或归源'] if any(r['source_context']['state']=='citation_discrepancy' for r in originals) else []) +
                           (['原文档案或段落定位不唯一；须比较列出的实际位置'] if any(r['source_context']['state'] in ('ambiguous','ambiguous_paragraph') for r in originals) else []) +
                           (['有摘录尚未在本地句子档案定位；当前只能核对卡片上下文'] if any(r['source_context']['state']=='not_found' for r in originals) else []),
        })
        destination[-1]['adaptation_card'] = ac.make_card(destination[-1], specs)
    return {**trace, 'query': query, 'function': spec['id'] if spec else None, 'section': section,
            'functions': [s['id'] for s in specs], 'parsed_request': parsed, 'conditions': requested,
            'ranking_order': ['function_accuracy', 'condition_compatibility', 'content_relevance', 'source_and_context'],
            'stage_counts': dict(counts),
            'function_contract': {k: spec[k] for k in ('id', 'label', 'definition', 'use_when', 'neighbors',
                'positive_example', 'mismatch_example', 'source') if k in spec} if spec else None,
            'function_contracts': [{k: s[k] for k in ('id', 'label', 'definition', 'use_when', 'neighbors',
                'positive_example', 'mismatch_example', 'source') if k in s} for s in specs],
            'design': design, 'evidence': evidence, 'status_filter': status, 'candidates': candidates,
            'supplementary_candidates': supplements,
            'reason': 'matched' if candidates else 'no_fit',
            'limits': '动作解析使用显式ID或别名规则；适用条件只核对源卡声明与输入事实，缺失保持未知。连续动作限同一源块的同一来源原文，省略号与档案歧义保留。context为卡片上下文，originals.source_context为本地原文档案定位，不等于PDF核验。'}


def brief(r):
    result={k: r[k] for k in ('uid', 'id', 'text', 'citekey', 'source_key_kind', 'status', 'status_basis', 'native_function', 'source_anchor', 'provenance_level', 'wb_items')}
    if r['kind']=='verbatim':
        result['source_context']=r['source_context']
    return result


def main(*, record_use=False):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('query', nargs='?', default='')
    ap.add_argument('--function')
    ap.add_argument('--need', default='', help='当前句段要完成的具体动作；用于细功能识别')
    ap.add_argument('--action', action='append', help='可重复；按顺序填写功能ID或动作名称，覆盖自动解析')
    condition_args = ap.add_mutually_exclusive_group()
    condition_args.add_argument('--conditions-json', help='结构化条件：design/evidence/claim_scope/facts；只填已知事实')
    condition_args.add_argument('--conditions-file', type=Path, help='从外部 JSON 文件读取结构化条件')
    ap.add_argument('--query-id', help='复用同一次检索编号；需求或候选变化时用新编号')
    ap.add_argument('--record-use', action='store_true', help='真实写作检索：登记 returned；基准/试运行不启用')
    ap.add_argument('--home', type=Path, help='隔离台账目录（测试/试运行）')
    ap.add_argument('--project', help='真实检索所属项目；仅写入外部台账')
    ap.add_argument('--section', choices=bc.SECTIONS)
    ap.add_argument('--design', default='')
    ap.add_argument('--evidence', default='', help='证据特征词法硬筛选（例如 null/mediation）')
    ap.add_argument('--status', action='append', help='可重复；显式筛选原有验证状态，不默认排除单源范本')
    ap.add_argument('--require-content', action='store_true', help='至少命中一个内容概念；否则允许同功能异主题候选')
    ap.add_argument('--top', type=int, default=3)
    ap.add_argument('--supplement-top', type=int, default=2, help='主题相关但动作不符或顺序未核验的补充候选上限；0关闭')
    ap.add_argument('--list-functions', action='store_true')
    ap.add_argument('--out', type=Path)
    ap.add_argument('--format', choices=('json', 'cards'), default='json',
                    help='json 保留结构化接口；cards 输出六栏 Markdown 改编卡')
    ap.add_argument('--batch', type=Path, help='JSON query list, sharing one catalog load')
    args = ap.parse_args()
    if args.list_functions and args.format != 'json':
        ap.error('--list-functions 使用 JSON；--format cards 用于检索结果')
    try:
        conditions = json.loads(args.conditions_file.read_text(encoding='utf-8-sig')) if args.conditions_file else (
            json.loads(args.conditions_json) if args.conditions_json else None)
        rm.request_conditions(conditions, args.design)
    except (ValueError, OSError) as exc:
        ap.error(str(exc))
    if args.batch and args.query_id:
        ap.error('--batch 使用每项 query_id，不能整批共用 --query-id')
    if args.batch and (args.action or conditions is not None):
        ap.error('--batch 的 actions/conditions 由每项需求填写')
    if args.list_functions:
        result = function_specs()
    elif args.batch:
        batch = json.loads(args.batch.read_text(encoding='utf-8'))
        batch = batch.get('queries', batch.get('cases', [])) if isinstance(batch, dict) else batch
        catalog = load_catalog()
        result = {'results': [{'id': q.get('id'), 'result': search(
            q.get('query',''), q.get('function'), q.get('section'), q.get('design',''),
            max(1,q.get('top',args.top)), catalog=catalog, require_content=q.get('require_content',False),
            evidence=q.get('evidence',''), status=q.get('status'), need=q.get('need',''),
            query_id=q.get('query_id'), conditions=q.get('conditions'), actions=q.get('actions'),
            supplement_top=max(0,q.get('supplement_top',args.supplement_top)))} for q in batch]}
    else:
        catalog = load_catalog()
        result = search(args.query, args.function, args.section, args.design,
                 max(1, args.top), require_content=args.require_content, evidence=args.evidence, status=args.status,
                 need=args.need, query_id=args.query_id, catalog=catalog, conditions=conditions, actions=args.action,
                 supplement_top=max(0,args.supplement_top))
    if (record_use or args.record_use) and not args.list_functions:
        from log_exemplar import record_returned
        for result_item in ([r['result'] for r in result['results']] if args.batch else [result]):
            try:
                result_item['returned_recorded'] = record_returned(result_item, catalog, home=args.home, project=args.project)
            except (ValueError, OSError, TypeError) as exc:
                result_item['returned_recorded'] = False
                print(f'WARN: 检索已完成，使用登记失败：{exc}', file=sys.stderr)
    rendered = ac.render_markdown(result, bc.ROOT) if args.format == 'cards' else json.dumps(result, ensure_ascii=False, indent=2) + '\n'
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(rendered, encoding='utf-8', newline='\n')
        print(f'written: {args.out}')
    else:
        print(rendered, end='')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
