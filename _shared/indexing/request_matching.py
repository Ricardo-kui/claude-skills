"""Check declared applicability and source-bound action order before topic ranking."""
from __future__ import annotations
import re

FACETS = ('design', 'evidence', 'claim_scope')
ALIASES = {
    'ols': 'ols_fe', 'ols-fe': 'ols_fe', 'panel_ols': 'ols_fe', '固定效应ols': 'ols_fe',
    'iv': 'iv_2sls', '2sls': 'iv_2sls', 'iv-2sls': 'iv_2sls',
    'difference-in-differences': 'did', '双重差分': 'did',
    'logit': 'logit_probit', 'probit': 'logit_probit',
    '观测性': 'observational', '观察性': 'observational', '随机实验': 'randomized',
    '准实验': 'quasi_experimental', '非显著': 'null_result', '混合发现': 'mixed_findings',
    '关联': 'association', '因果': 'causal', '条件关联': 'conditional_association',
    '依赖识别假设的因果': 'causal_with_assumptions', '预测': 'theoretical_prediction',
}
DESIGNS = {'ols_fe', 'iv_2sls', 'did', 'heckman', 'logit_probit', 'survival', 'sem', 'experimental'}


def normalized(value):
    key = value.strip().casefold()
    return ALIASES.get(key, key.replace(' ', '_'))


def validate_applicability(value):
    if not isinstance(value, dict) or set(value) - {*FACETS, 'required_facts'}:
        raise ValueError('applicability allows design/evidence/claim_scope/required_facts')
    for facet in FACETS:
        if facet in value and (not isinstance(value[facet], list) or not value[facet] or
                               any(not isinstance(v, str) or not v.strip() for v in value[facet])):
            raise ValueError(f'applicability.{facet} must be a nonempty string list')
    facts = value.get('required_facts', {})
    if not isinstance(facts, dict) or any(not isinstance(k, str) or not k.strip() or
            not isinstance(v, (str, bool)) or (isinstance(v, str) and not v.strip()) for k, v in facts.items()):
        raise ValueError('applicability.required_facts requires named string/boolean facts')
    return value


def request_conditions(value=None, design=''):
    value = {} if value is None else value
    if not isinstance(value, dict) or set(value) - {*FACETS, 'facts'}:
        raise ValueError('conditions allows design/evidence/claim_scope/facts')
    result = {}
    for facet in FACETS:
        if facet not in value:
            continue
        raw = value[facet]
        values = [raw] if isinstance(raw, str) else raw
        if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
            raise ValueError(f'conditions.{facet} must be a string or nonempty string list')
        result[facet] = [normalized(v) for v in values]
    # Only recognized whole design names become structured facts. The existing
    # free-text design filter remains available for all other inputs.
    if design and 'design' not in result and normalized(design) in DESIGNS:
        result['design'] = [normalized(design)]
    facts = value.get('facts', {})
    if not isinstance(facts, dict) or any(not isinstance(k, str) or not k.strip() or
            not isinstance(v, (str, bool)) or (isinstance(v, str) and not v.strip()) for k, v in facts.items()):
        raise ValueError('conditions.facts requires named string/boolean facts')
    result['facts'] = facts
    return result


def applicability(rows, requested):
    authored = next((r.get('retrieval_move', {}).get('applicability') for r in rows
                     if r.get('retrieval_move', {}).get('applicability') is not None), {})
    checks = []
    for facet in FACETS:
        given, allowed = requested.get(facet), authored.get(facet)
        if given is None and allowed is None:
            continue
        allowed = [normalized(v) for v in allowed] if allowed else None
        verdict = ('unknown' if given is None or allowed is None else
                   'compatible' if all(v in allowed for v in given) else 'conflict')
        checks.append({'facet': facet, 'provided': given, 'allowed': allowed,
                       'verdict': verdict, 'basis': 'authored_applicability' if allowed else 'unannotated'})
    facts = requested.get('facts', {})
    required = authored.get('required_facts', {})
    for key in sorted(set(required) | set(facts)):
        given, expected = facts.get(key), required.get(key)
        known = key in facts and key in required
        verdict = ('compatible' if type(given) is type(expected) and given == expected else 'conflict') if known else 'unknown'
        checks.append({'facet': 'facts.' + key, 'provided': given, 'required': expected,
                       'verdict': verdict, 'basis': 'authored_applicability' if key in required else 'unannotated'})
    if not checks:
        state = 'not_checked'
    elif any(c['verdict'] == 'conflict' for c in checks):
        state = 'incompatible'
    elif any(c['verdict'] == 'unknown' for c in checks):
        state = 'unknown'
    else:
        state = 'compatible'
    return {'state': state, 'checks': checks,
            'unknowns': [c['facet'] for c in checks if c['verdict'] == 'unknown'],
            'rank': (2 if state == 'compatible' else 1 if any(c['verdict'] == 'compatible' for c in checks) else 0)}


def archive_sequence(originals, steps):
    """Check actual archive paragraph order where identity and location are bound."""
    from source_context import normalized as source_normalized
    paragraphs = {}
    for row in originals:
        context = row.get('source_context', {})
        if context.get('state') == 'matched':
            for paragraph in context.get('paragraphs', []):
                paragraphs[(paragraph['source_file'], paragraph['source_line'])] = paragraph
    if not paragraphs:
        return {'state': 'not_verified', 'locations': []}
    sources = {key[0] for key in paragraphs}
    if len(sources) != 1:
        return {'state': 'not_verified', 'locations': []}
    ordered = [p for _, p in sorted(paragraphs.items())]
    texts = [source_normalized(p['text']) for p in ordered]
    cues = [source_normalized(s['cue']) for s in steps]
    joined = ' '.join(texts)
    if not all(cue in joined for cue in cues):
        return {'state': 'not_verified', 'locations': []}
    cursor, locations = 0, []
    for cue in cues:
        index = joined.find(cue, cursor)
        if index < 0:
            return {'state': 'contradictory_order', 'locations': []}
        offset = 0
        for paragraph, text in zip(ordered, texts):
            if offset <= index < offset + len(text):
                locations.append({k: paragraph[k] for k in ('source_file', 'source_line', 'source_end_line',
                                                            'source_section', 'paragraph_number')})
                break
            offset += len(text) + 1
        cursor = index + len(cue)
    return {'state': 'verified_order', 'locations': locations,
            'contiguity': 'one_paragraph' if len({(p['source_file'], p['source_line']) for p in locations}) == 1 else 'multiple_paragraphs'}


def action_sequence(rows, specs):
    """A sequence needs ordered cues in one existing source block, never a collage."""
    wanted = [s['id'] for s in specs]
    if len(wanted) < 2:
        return {'state': 'single_action', 'steps': []}
    steps = next((r.get('retrieval_move', {}).get('sequence') for r in rows
                  if r.get('retrieval_move', {}).get('sequence')), [])
    cursor, selected = 0, []
    for fid in wanted:
        index = next((i for i in range(cursor, len(steps)) if steps[i]['function'] == fid), None)
        if index is None:
            return {'state': 'unverified_order', 'steps': [], 'required': wanted}
        selected.append(steps[index])
        cursor = index + 1
    if any(step['kind'] != 'verbatim' for step in selected):
        return {'state': 'template_or_unverified', 'steps': selected, 'required': wanted}
    # A card may quote several papers. Only one paper, or one still-unbound
    # excerpt containing every cue, can support the requested sequence.
    groups = {}
    for row in rows:
        if row['kind'] == 'verbatim':
            key = row['citekey'] if row.get('source_key_kind') == 'single_key' else row['uid']
            groups.setdefault(key, []).append(row)
    for originals in groups.values():
        original_text = ' '.join(' '.join(r['text'].split()) for r in originals)
        cursor, evidence = 0, []
        for step in selected:
            cue = ' '.join(step['cue'].split())
            index = original_text.find(cue, cursor)
            if index < 0:
                break
            matches = [r for r in originals if cue in ' '.join(r['text'].split())]
            evidence.append({**step, 'source_uids': [r['uid'] for r in matches],
                             'archive_states': sorted({r.get('source_context', {}).get('state', 'not_found') for r in matches})})
            cursor = index + len(cue)
        if len(evidence) == len(selected):
            bound = originals[0].get('source_key_kind') == 'single_key'
            archive = archive_sequence(originals, selected)
            if archive['state'] == 'contradictory_order':
                return {'state': 'archive_order_conflict', 'steps': evidence, 'archive_order': archive}
            return {'state': 'source_bound_order' if bound else 'excerpt_order_source_pending',
                    'basis': 'authored_cues_in_one_card_block', 'steps': evidence,
                    'citekey': originals[0]['citekey'], 'archive_order': archive,
                    'original_contiguity': archive.get('contiguity', 'read_source_context'),
                    'note': '顺序已在同一来源摘录中定位；省略号、跨段与档案歧义仍按来源状态保留。'}
    return {'state': 'unverified_source_or_order', 'steps': [], 'required': wanted}


def source_support(rows):
    originals = [r for r in rows if r['kind'] == 'verbatim']
    if not originals:
        return {'level': 'template_only', 'rank': 0, 'archive_states': []}
    states = sorted({r.get('source_context', {}).get('state', 'not_found') for r in originals})
    bound = all(r.get('source_key_kind') == 'single_key' and
                r.get('source_context', {}).get('state') == 'matched' for r in originals)
    return {'level': 'archive_bound' if bound else 'card_excerpt_pending_checks',
            'rank': 2 if bound else 1, 'archive_states': states,
            'note': '原文档案定位与检索适用性分别呈现；档案匹配不等于PDF核验。'}


def split_actions(need):
    return [v.strip(' ，,。.;；') for v in re.split(
        r'(?:然后|随后|接着|再(?=解释|说明|报告|判断)|→|->|\bthen\b|\bfollowed by\b)', need, flags=re.I)
            if v.strip(' ，,。.;；')]
