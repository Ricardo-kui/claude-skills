"""Derive adaptation cards from retrieved source blocks; never author excerpts."""
from __future__ import annotations

import re
from pathlib import Path

from source_context import excerpt_chunks, normalized

SECTIONS = (
    ('original', '原句或原段落'),
    ('function', '完成的功能'),
    ('skeleton', '关键表达骨架'),
    ('substitution', '可替换部分'),
    ('applicability', '适用条件'),
    ('source_context', '来源与上下文'),
)
CONDITION_LABELS = {'compatible': '已声明条件相容', 'unknown': '适用条件待核对',
                    'not_checked': '尚未核对适用条件', 'incompatible': '条件不符'}
ARCHIVE_LABELS = {'matched': '已定位本地原文档案', 'not_found': '原文档案未定位',
                  'ambiguous': '原文档案不唯一', 'ambiguous_paragraph': '原文段落不唯一',
                  'citation_discrepancy': '来源键与档案键有差异'}
STRUCTURAL_MARKER = re.compile(
    r'^(?:基线|建立权衡|不对称解读|理论锚定|总结收束|事件分段\d*|机制环节\d*|'
    r'论证步骤\d*|支持判断|结果报告|段落收束)$')


def clean_list(values):
    return list(dict.fromkeys(v.strip() for v in values if isinstance(v, str) and v.strip()))


def authored_original_uids(originals, meta, function):
    """Resolve the card's supporting cue to actual excerpts, including partials."""
    evidence = meta.get('function_evidence', {}).get(function, {})
    cue = evidence.get('cue', '')
    if function not in meta.get('functions', []) or evidence.get('kind') != 'verbatim' or not cue:
        return []
    return [r['uid'] for r in originals if normalized(cue) in normalized(r['text'])]


def preferred_originals(candidate, specs):
    """Prefer actual supporting cues without pairing an unrelated paper."""
    originals = candidate['originals']
    sequence = candidate['function_matching']['sequence']
    uids = {uid for step in sequence.get('steps', []) for uid in step.get('source_uids', [])}
    if uids:
        return [r['uid'] for r in originals if r['uid'] in uids], 'ordered_action_cues'
    uids = {uid for spec in specs for uid in authored_original_uids(
        originals, candidate['retrieval_move'], spec['id'])}
    if uids:
        return [r['uid'] for r in originals if r['uid'] in uids], 'authored_function_evidence'
    uids = set()
    for spec in specs:
        positive = spec.get('positive_example', {})
        cue = positive.get('cue', '')
        if positive.get('kind') == 'verbatim' and cue:
            uids.update(r['uid'] for r in originals if normalized(cue) in normalized(r['text']))
    if uids:
        return [r['uid'] for r in originals if r['uid'] in uids], 'contract_positive_cue'
    return [r['uid'] for r in originals], 'same_source_block'


def paragraph_windows(original):
    """Expose real text immediately before/after an excerpt within each paragraph.

    Separate ellipsis chunks stay separate; neither a card annotation nor an
    archive neighbour is treated as an observed rhetorical function.
    """
    context = original.get('source_context', {})
    chunks = excerpt_chunks(original['text'])
    windows = []
    for paragraph in context.get('paragraphs', []):
        text = normalized(paragraph['text'])
        spans, cursor = [], 0
        for chunk in chunks:
            offset = text.find(chunk, cursor)
            if offset >= 0:
                spans.append({'text': chunk, 'start': offset, 'end': offset + len(chunk)})
                cursor = offset + len(chunk)
        if not spans:
            continue
        windows.append({
            **{k: paragraph.get(k) for k in ('source_file', 'source_line', 'source_end_line',
                                            'source_section', 'paragraph_number')},
            'location_unique': context.get('state') != 'ambiguous_paragraph',
            'before': text[:spans[0]['start']].strip(),
            'matched_spans': spans,
            'after': text[spans[-1]['end']:].strip(),
            'excerpt_has_omissions': bool(re.search(r'\.{3,}|…+', original['text'])),
            'text_basis': 'typography_normalized_archive_text',
        })
    return windows


def slot_kind(label):
    """Conservative substitution guidance; unknown brackets require review."""
    if STRUCTURAL_MARKER.fullmatch(label) or '→' in label or '->' in label:
        return 'structural_marker', '论证步骤提示；保留其顺序与作用，不作为研究变量替换。'
    lower = label.lower()
    if re.search(r'citation|reference|文献|引文|来源', lower):
        return 'citation', '替换为实际支持当前论断的文献；核对来源和引用范围。'
    if re.search(r'coefficient|parameter|参数|函数|系数', lower):
        return 'model_quantity', '核对该项表示模型参数、函数还是估计值，填入当前研究对应量；模型设定与实际检验结果分别说明。'
    if re.search(r'\b(?:value|threshold|estimate|ci|n)\b|数值|阈值|区间|标准误|样本量', lower):
        return 'evidence_value', '使用本研究实际估计值、检验信息或样本数，并同步核对单位和论断。'
    if re.search(r'direction|significan|support|causal|unaddressed|poorly understood|underspecified|幅度|方向|显著|支持|因果', lower):
        return 'claim_or_judgment', '依据实际理论或检验结果选择方向与判断；不沿用范文的支持结论或因果强度。'
    if re.search(r'\b(?:when|if)\b|method|model|design|hazard|estimator|shock|instrument|control|treatment|识别|估计|模型|冲击|处理|控制|条件', lower):
        return 'design_or_condition', '填入本研究实际设计、过程或条件，并重新核对该骨架的适用性。'
    if re.search(r'^(?:x|y|iv|dv|dv_count)$|actor|unit|mediator|outcome|dimension|mechanism|characteristic|variable|渠道|主体|事件|构念|变量|结果|情形|企业|采纳', lower):
        return 'research_content', '替换为本研究对应的主体、构念或关系；保持分析单位、时间顺序和逻辑角色一致。'
    return 'requires_review', '先确认该括号表示内容、措辞选项还是成立条件，再按当前研究事实改编。'


def substitution_parts(templates):
    parts = {}
    for template in templates:
        for match in re.finditer(r'\[([^\[\]\n]+)\]', template['text']):
            label = match.group(1)
            kind, guidance = slot_kind(label)
            part = parts.setdefault(label, {'slot': match.group(), 'kind': kind,
                                           'guidance': guidance, 'template_uids': []})
            if template['uid'] not in part['template_uids']:
                part['template_uids'].append(template['uid'])
    return ([p for p in parts.values() if p['kind'] != 'structural_marker'],
            [p for p in parts.values() if p['kind'] == 'structural_marker'])


def expression_skeletons(candidate, specs):
    """An authored range selects existing template text, never rewrites it."""
    span = candidate['retrieval_move'].get('skeleton_span')
    if not specs or (span and not {s['id'] for s in specs} <= set(
            span.get('functions', candidate['retrieval_move'].get('functions', [])))):
        span = None
    templates = []
    for template in candidate['templates']:
        text = template['text']
        start, end = 0, len(text)
        if span:
            start = text.find(span['start'])
            if start < 0:
                continue
            if span.get('end_before'):
                end = text.find(span['end_before'], start + len(span['start']))
                if end < 0:
                    continue
        templates.append({
            **{k: template[k] for k in ('uid', 'id', 'provenance_level')},
            'text': text[start:end].strip(),
            'scope': 'authored_span' if span else 'whole_template',
            'source_text_start': start, 'source_text_end': end,
        })
    return templates, bool(span)


def make_card(candidate, specs):
    """Six ordered sections. Missing facts and source states remain explicit."""
    meta = candidate['retrieval_move']
    selected, selection_basis = preferred_originals(candidate, specs)
    matching = candidate['function_matching']
    checks = {check['id']: check for check in matching['actions']}
    actions = [{'id': spec['id'], 'label': spec.get('label', spec.get('description', spec['id'])),
                'definition': spec.get('definition', spec.get('description', '')),
                'support': {
                    'state': checks.get(spec['id'], {}).get('certainty', 'unmatched'),
                    'selector_satisfied': checks.get(spec['id'], {}).get('complete', False),
                    'basis': checks.get(spec['id'], {}).get('basis'),
                    'original_support': checks.get(spec['id'], {}).get('original_support'),
                    'expression_check_basis': checks.get(spec['id'], {}).get('expression_check_basis'),
                    'missing_expression_checks': checks.get(spec['id'], {}).get('missing_expression_checks', []),
                }} for spec in specs]
    templates, focused_skeleton = expression_skeletons(candidate, specs)
    slots, markers = substitution_parts(templates)
    sources = []
    full_paragraphs = {}
    sequence = matching['sequence']
    verified_locations = {(p['source_file'], p['source_line'])
                          for p in sequence.get('archive_order', {}).get('locations', [])
                          if sequence.get('archive_order', {}).get('state') == 'verified_order'}
    for original in candidate['originals']:
        context = original.get('source_context', {})
        sources.append({
            **{k: original[k] for k in ('uid', 'citekey', 'source_key_kind', 'status',
                                       'status_basis', 'provenance_level', 'source_anchor')},
            'archive_state': context.get('state', 'not_found'),
            'archive_context': context,
            'paragraph_windows': paragraph_windows(original),
        })
        if original['uid'] in selected and context.get('state') == 'matched':
            for paragraph in context.get('paragraphs', []):
                key = (paragraph['source_file'], paragraph['source_line'])
                if key in verified_locations:
                    full_paragraphs[key] = paragraph
    position = meta.get('position', '')
    follows = meta.get('prerequisite', '')
    next_move = meta.get('next', '')
    integration = {
        'state': 'annotated' if position and follows and next_move else ('partial' if position or follows or next_move else 'unknown'),
        'basis': 'authored_source_card',
        'position': position or None, 'follows': follows or None,
        'advances': meta.get('advances') or None,
        'next': next_move or None,
        'next_evidence': meta.get('next_evidence', []),
        'evidence_state': 'annotated' if meta.get('next_evidence') else 'not_annotated',
    }
    return {
        'schema_version': 1,
        'original': {
            'state': 'available' if candidate['originals'] else 'missing',
            'excerpts': [{k: r[k] for k in ('uid', 'id', 'text', 'citekey', 'provenance_level')}
                         for r in candidate['originals']],
            'preferred_uids': selected, 'selection_basis': selection_basis,
            'full_paragraphs': [full_paragraphs[key] for key in sorted(full_paragraphs)],
            'note': '原句保持原摘录；有省略号时查看档案段落。不同段落和不同来源分别呈现。',
        },
        'function': {
            'actions': actions, 'native_function': candidate['native_function'],
            'uncertain': matching['uncertain'], 'sequence': sequence,
            'candidate_role': candidate['candidate_role'],
            'supplement_reason': candidate['supplement_reason'],
            'paragraph_integration': integration,
        },
        'skeleton': {
            'state': 'templates_available' if templates else ('move_only' if candidate['learnable_move'] else 'missing'),
            'templates': templates, 'learnable_moves': clean_list(candidate['learnable_move']),
            'basis': 'authored_source_card',
            'selection': 'authored_span' if focused_skeleton else 'same_source_block',
            'selection_unresolved': focused_skeleton and not templates,
            'note': '骨架为同块蒸馏模板，不是论文原句；宽于当前动作的段落骨架须按条件选用相应部分。',
        },
        'substitution': {
            'state': 'slots_available' if slots else 'requires_manual_review',
            'slots': slots, 'structural_markers': markers,
            'nontransferable': clean_list(candidate['nontransferable']),
            'boundaries': ['数值、设计、制度事实、因果强度及支持判断必须来自当前研究。',
                           '改编后保留承接关系与论证顺序，并补齐该动作需要的证据。'],
        },
        'applicability': {
            'state': candidate['condition_check']['state'],
            'structured_check': candidate['condition_check'],
            'declared_conditions': meta.get('applicability', {}),
            'card_conditions': clean_list(candidate['use_conditions']),
            'function_conditions': [{'id': spec['id'], 'use_when': spec.get('use_when', [])} for spec in specs],
            'content_matches': candidate['content_matches'],
            'content_coverage': candidate['content_coverage'],
            'note': '条件状态只覆盖已声明的检查；文字条件、设计可信度和当前论断仍须核对。',
        },
        'source_context': {
            'state': 'no_original' if not sources else ('pending_checks' if any(
                s['archive_state'] != 'matched' or s['source_key_kind'] != 'single_key' or
                s['archive_context'].get('citation_agreement') is not True for s in sources) else 'local_archive_located'),
            'source_support': candidate['source_support'],
            'card_location': {k: candidate[k] for k in ('source_file', 'source_line', 'source_end_line', 'parent_paragraph')},
            'excerpt_sources': sources,
            'note': '来源状态与检索适用性分别呈现；本地档案定位不等于原始 PDF 或书目核验，原有验证状态保留。',
        },
    }


def location_link(location, root):
    path = Path(root) / location['source_file']
    line = location.get('source_line') or 1
    return f"[{path.name}:{line}](<{path.as_posix()}:{line}>)"


def quote(text):
    return '\n'.join('> ' + line for line in text.splitlines())


def render_candidate(candidate, root):
    card = candidate['adaptation_card']
    role = '主候选' if candidate['candidate_role'] == 'primary' else '补充候选：功能或顺序尚未满足'
    lines = [f"### {candidate['rank']}. {candidate['block_title']}（{role}）", '']
    for key, label in SECTIONS:
        data = card[key]
        lines.extend([f'**{label}**', ''])
        if key == 'original':
            paragraphs = data['full_paragraphs']
            if paragraphs:
                for paragraph in paragraphs:
                    lines.extend([f"本地档案原段落（{paragraph['source_section']}，第 {paragraph['paragraph_number']} 段）：",
                                  '', quote(paragraph['text']), ''])
            else:
                preferred = set(data['preferred_uids'])
                for original in data['excerpts']:
                    if original['uid'] in preferred:
                        lines.extend([quote(original['text']), '', f"摘录：`{original['uid']}`；卡片来源键：`{original['citekey'] or '待确认'}`。", ''])
                if not data['excerpts']:
                    lines.extend(['本块缺少原句；下方仅有蒸馏骨架或动作说明。', ''])
                elif len(preferred) < len(data['excerpts']):
                    lines.extend(['其他同块摘录见卡片；其来源状态在下方逐项列出。', ''])
        elif key == 'function':
            for action in data['actions']:
                support = action['support']
                qualifier = ('部分支持' if support['state'] == 'partial' else '未满足当前动作判据'
                             if not support['selector_satisfied'] else '功能待核对'
                             if data['uncertain'] else '已标注动作')
                lines.extend([f"- {action['label']}：{action['definition']}（{qualifier}）"])
            if not data['actions']:
                lines.append('当前仅按内容检索，具体写作动作待确认。')
            integration = data['paragraph_integration']
            follows = integration['follows']
            if follows and 'definitions' in follows and 'use_when' in follows:
                follows = '见下方功能条件；源卡未单独说明具体承接内容。'
            lines.extend(['', f"- 句段位置：{integration['position'] or '未标注，须查看原文'}。",
                          f"- 承接：{follows or '未标注，须核对前文'}",
                          f"- 推进：{integration['advances'] or '按上方动作判据及原文上下文核对；本块未另作标注'}",
                          f"- 后接：{integration['next'] or '未标注，须补足后续交接'}"])
            evidence = integration['next_evidence']
            lines.append('- 后续证据：' + ('；'.join(evidence) if evidence else '未单独标注；按后接要求、文字条件和原文核对，不能由句式推定。'))
            lines.append('')
        elif key == 'skeleton':
            for template in data['templates']:
                scope = '（源卡指定部分；完整模板见卡片）' if template['scope'] == 'authored_span' else ''
                lines.extend([quote(template['text']), '', f"卡片模板：`{template['uid']}`{scope}。", ''])
            if not data['templates']:
                lines.extend(['源卡指定的骨架部分未在本次模板候选中定位，须查看完整源卡。' if data['selection_unresolved'] else '本块未抽取表达模板。', ''])
            for move in data['learnable_moves']:
                lines.append('- 可学动作：' + move)
            lines.extend(['', data['note'], ''])
        elif key == 'substitution':
            groups = {}
            for slot in data['slots']:
                groups.setdefault(slot['guidance'], []).append(slot['slot'])
            lines.extend(f"- {'、'.join(slots)}：{guidance}" for guidance, slots in groups.items())
            if not data['slots']:
                lines.append('没有已抽取的替换槽位，需结合原文手动确认。')
            if data['structural_markers']:
                lines.append('- 论证步骤提示（保留作用）：' + '、'.join(p['slot'] for p in data['structural_markers']))
            lines.extend('- 不可移植：' + item for item in data['nontransferable'])
            lines.extend(['', *data['boundaries'], ''])
        elif key == 'applicability':
            lines.extend([CONDITION_LABELS[data['state']] + '。', ''])
            if data['structured_check'].get('unknowns'):
                lines.extend(['待确认：' + '、'.join(data['structured_check']['unknowns']) + '。', ''])
            for item in data['card_conditions']:
                lines.append('- 卡片条件：' + item)
            for condition in data['function_conditions']:
                lines.extend('- 功能条件：' + item for item in condition['use_when'])
            lines.extend(['', data['note'], ''])
        else:
            lines.extend(['卡片：' + location_link(data['card_location'], root), ''])
            for source in data['excerpt_sources']:
                context = source['archive_context']
                lines.append(f"- `{source['uid']}`：卡片键 `{source['citekey'] or '待确认'}`；原有状态 `{source['status']}`；{ARCHIVE_LABELS.get(source['archive_state'], source['archive_state'])}。")
                if source['source_key_kind'] != 'single_key':
                    lines.append('  来源键待消歧到单篇论文。')
                if context.get('archive_citekey'):
                    lines.append(f"  档案键 `{context['archive_citekey']}`；书目对应关系：" + ('键字符串相容，书目仍须核验。' if context.get('citation_agreement') is True else '待核对。'))
                for path in context.get('candidate_archives', []):
                    lines.append('  可能档案：' + location_link({'source_file': path}, root))
                for window in source['paragraph_windows']:
                    lines.extend(['', f"原文位置：{location_link(window, root)}（{window['source_section']}，第 {window['paragraph_number']} 段" + ('，位置待消歧' if not window['location_unique'] else '') + '）。'])
                    if window['before']:
                        lines.extend(['', '同段前文：', '', quote(window['before'])])
                    if window['after']:
                        lines.extend(['', '同段后文：', '', quote(window['after'])])
                    if window['excerpt_has_omissions']:
                        lines.extend(['', '卡片摘录含省略；段落及省略范围须结合档案核对。'])
                for field, label in (('preceding_paragraph', '前段'), ('following_paragraph', '后段')):
                    if context.get(field):
                        lines.extend(['', f"{label}：{location_link(context[field], root)}（第 {context[field]['paragraph_number']} 段）。"])
            if not data['excerpt_sources']:
                lines.append('没有原句来源可核验；模板的来源键不构成原文验证。')
            lines.extend(['', data['note'], ''])
    return '\n'.join(lines).rstrip() + '\n'


def render_markdown(result, root):
    if 'results' in result:
        return '\n\n'.join(f"## 需求 {item.get('id') or index}\n\n" + render_markdown(item['result'], root)
                            for index, item in enumerate(result['results'], 1))
    lines = [f"检索编号：`{result['query_id']}`", '']
    cards = result['candidates'] + result.get('supplementary_candidates', [])
    if not result['candidates']:
        lines.extend([f"未找到满足当前动作的主候选（{result['reason']}）。", ''])
        unresolved = result.get('parsed_request', {}).get('unresolved_actions', [])
        if unresolved:
            lines.extend(['待明确动作：' + '；'.join(unresolved), ''])
    lines.extend(render_candidate(candidate, root) for candidate in cards)
    return '\n'.join(lines).rstrip() + '\n'
