"""Adaptation cards retain actual source boundaries and conditional claims."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
import adaptation_cards as ac
import build_catalog as bc
from retrieve import function_specs, load_catalog, retrieval_version, search

RISK = 'methods.endogeneity_risk'
MITIGATION = 'methods.design_mitigation'
DID_CONDITIONS = {'design': 'did', 'evidence': 'quasi_experimental',
                  'claim_scope': 'causal_with_assumptions', 'facts': {'plausibly_exogenous_shock': True}}
INDIRECT_CONDITIONS = {'evidence': 'indirect_effect_test', 'claim_scope': 'association',
                       'facts': {'indirect_effect_estimated': True, 'indirect_method_appropriate': True}}


class AdaptationCardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.risk = next(r for r in cls.catalog['entries'] if r['kind'] == 'verbatim' and
                        RISK in r.get('retrieval_move', {}).get('functions', []) and
                        r['source_file'].endswith('自然实验-DiD.md'))

    def data(self, *rows):
        return {**self.catalog, 'entries': list(rows)}

    def first(self, **kwargs):
        return search(catalog=self.catalog, top=1, supplement_top=0, **kwargs)['candidates'][0]

    def contract_first(self, function, **kwargs):
        """Source-specific features are fixtures, independent of corpus growth."""
        owner = next(d['source']['parent_paragraph'] for d in self.catalog['function_definitions']
                     if d['id'] == function)
        rows = [copy.deepcopy(r) for r in self.catalog['entries'] if r['parent_paragraph'] == owner]
        return search(function=function, catalog=self.data(*rows), top=1,
                      supplement_top=0, **kwargs)['candidates'][0]

    def test_every_section_and_supplement_has_the_same_six_part_card(self):
        for function in ('intro.gap_unexplained', 'theory.mechanism_link', RISK, 'results.indirect_effect_report'):
            with self.subTest(function=function):
                candidate = self.first(function=function, design='did' if function == RISK else '')
                card = candidate['adaptation_card']
                self.assertEqual(list(card)[1:], [key for key, _ in ac.SECTIONS])
                self.assertEqual(card['original']['excerpts'], [
                    {k: original[k] for k in ('uid', 'id', 'text', 'citekey', 'provenance_level')}
                    for original in candidate['originals']])
                integration = card['function']['paragraph_integration']
                self.assertIsNotNone(integration['advances'])
                self.assertTrue(integration['next_evidence'])
        result = search('地位 声誉 status reputation', 'theory.construct_contrast', catalog=self.catalog)
        self.assertTrue(result['supplementary_candidates'])
        for candidate in result['candidates'] + result['supplementary_candidates']:
            self.assertIn('adaptation_card', candidate)

    def test_ordered_actions_return_real_full_paragraph_without_stitching_ellipsis(self):
        candidate = self.first(actions=[RISK, MITIGATION], conditions=DID_CONDITIONS)
        card = candidate['adaptation_card']
        self.assertEqual(card['applicability']['state'], 'compatible')
        self.assertEqual([a['id'] for a in card['function']['actions']], [RISK, MITIGATION])
        full = card['original']['full_paragraphs']
        self.assertEqual(len(full), 1)
        original = candidate['originals'][0]
        self.assertIn('...', original['text'])
        self.assertEqual(full, original['source_context']['paragraphs'])
        self.assertNotIn('...', full[0]['text'])
        self.assertEqual(full[0]['paragraph_number'], 2)
        self.assertTrue(card['source_context']['excerpt_sources'][0]['paragraph_windows'][0]['excerpt_has_omissions'])
        self.assertNotIn('首段', card['function']['paragraph_integration']['position'])

    def test_compatible_adaptation_does_not_confirm_a_pending_source(self):
        candidate = self.first(function='results.indirect_effect_report', conditions=INDIRECT_CONDITIONS)
        card = candidate['adaptation_card']
        self.assertEqual(card['applicability']['state'], 'compatible')
        self.assertEqual(card['source_context']['state'], 'pending_checks')
        source = card['source_context']['excerpt_sources'][0]
        self.assertEqual(source['archive_state'], 'not_found')
        self.assertEqual(source['status'], 'VERIFIED')  # existing rating is a different axis
        self.assertFalse(source['paragraph_windows'])
        text = ac.render_candidate(candidate, ROOT)
        self.assertIn('已声明条件相容', text)
        self.assertIn('原文档案未定位', text)
        self.assertIn('不等于原始 PDF', text)

    def test_archive_binding_does_not_fill_missing_project_conditions(self):
        candidate = self.first(actions=[RISK, MITIGATION], design='did')
        card = candidate['adaptation_card']
        self.assertEqual(card['applicability']['state'], 'unknown')
        self.assertEqual(card['source_context']['state'], 'local_archive_located')
        self.assertIn('facts.plausibly_exogenous_shock', card['applicability']['structured_check']['unknowns'])

    def test_template_only_card_never_labels_template_as_original(self):
        row = copy.deepcopy(next(r for r in self.catalog['entries'] if r['kind'] == 'template' and
                                 RISK in r.get('retrieval_move', {}).get('functions', []) and
                                 r['source_file'].endswith('自然实验-DiD.md')))
        result = search('', RISK, catalog=self.data(row))
        candidate = result['candidates'][0]
        card = candidate['adaptation_card']
        self.assertEqual(card['original']['state'], 'missing')
        self.assertFalse(card['original']['excerpts'] + card['original']['full_paragraphs'])
        self.assertEqual(card['source_context']['state'], 'no_original')
        self.assertTrue(card['skeleton']['templates'])
        text = ac.render_candidate(candidate, ROOT)
        self.assertIn('本块缺少原句', text)
        self.assertIn('模板的来源键不构成原文验证', text)

    def test_ambiguous_source_keeps_every_real_alternative_and_no_guessed_context(self):
        candidate = self.contract_first('intro.gap_unexplained')
        ambiguous = next(source for source in candidate['adaptation_card']['source_context']['excerpt_sources']
                         if source['archive_state'] == 'ambiguous')
        self.assertEqual(len(ambiguous['archive_context']['candidate_archives']), 2)
        self.assertFalse(ambiguous['paragraph_windows'])
        text = ac.render_candidate(candidate, ROOT)
        self.assertIn('原文档案不唯一', text)
        for path in ambiguous['archive_context']['candidate_archives']:
            self.assertIn(path, text)
        # The card's existing key is retained even when the archive needs reconciliation.
        self.assertEqual(ambiguous['citekey'], 'eilert2017')

    def test_missing_source_key_remains_pending_even_with_a_text_match(self):
        row = copy.deepcopy(self.risk)
        row.update(citekey='', source_key_kind='missing', provenance_level='source_pending')
        candidate = search('', RISK, catalog=self.data(row))['candidates'][0]
        self.assertEqual(candidate['adaptation_card']['source_context']['state'], 'pending_checks')
        text = ac.render_candidate(candidate, ROOT)
        self.assertIn('卡片键 `待确认`', text)
        self.assertIn('来源键待消歧', text)

    def test_partial_support_remains_explicit_even_when_legacy_selector_passes(self):
        row = copy.deepcopy(self.risk)
        row['retrieval_move']['function_support'] = {RISK: 'partial'}
        result = search('common ownership', RISK, catalog=self.data(row))
        candidate = result['candidates'][0]
        action = candidate['adaptation_card']['function']['actions'][0]
        self.assertEqual(action['support']['state'], 'partial')
        self.assertTrue(action['support']['selector_satisfied'])
        text = ac.render_candidate(candidate, ROOT)
        self.assertIn('部分支持', text)

    def test_missing_paragraph_annotation_cannot_be_inferred_from_archive_or_label(self):
        row = copy.deepcopy(self.risk)
        for field in ('position', 'prerequisite', 'next', 'advances', 'next_evidence'):
            row['retrieval_move'].pop(field, None)
        candidate = search('', RISK, catalog=self.data(row))['candidates'][0]
        integration = candidate['adaptation_card']['function']['paragraph_integration']
        self.assertEqual(integration['state'], 'unknown')
        self.assertIsNone(integration['position'])
        self.assertIsNone(integration['advances'])
        self.assertEqual(integration['evidence_state'], 'not_annotated')

    def test_structure_markers_and_condition_clauses_are_not_free_content_slots(self):
        theory = self.contract_first('theory.mechanism_link')['adaptation_card']['substitution']
        markers = {s['slot'] for s in theory['structural_markers']}
        self.assertEqual(markers, {'[事件分段1]'})
        self.assertFalse(markers & {s['slot'] for s in theory['slots']})
        results = self.contract_first('results.indirect_effect_report')['adaptation_card']['substitution']
        slots = {s['slot']: s for s in results['slots']}
        self.assertEqual(slots['[value]']['kind'], 'evidence_value')
        self.assertEqual(slots['[threshold]']['kind'], 'evidence_value')
        self.assertNotIn('[when mediator included]', slots)  # outside this result sentence
        full_slots, _ = ac.substitution_parts(self.contract_first('results.indirect_effect_report')['templates'])
        full_slots = {s['slot']: s for s in full_slots}
        self.assertEqual(full_slots['[when mediator included]']['kind'], 'design_or_condition')
        self.assertEqual(full_slots['[direction]']['kind'], 'claim_or_judgment')

    def test_theoretical_coefficient_is_not_mislabelled_as_an_empirical_estimate(self):
        card = self.contract_first('theory.mechanism_link')['adaptation_card']
        slot = next(s for s in card['substitution']['slots'] if s['slot'] == '[内部系数]')
        self.assertEqual(slot['kind'], 'model_quantity')
        self.assertIn('模型设定与实际检验结果分别说明', slot['guidance'])
        self.assertNotIn('使用本研究实际估计值', slot['guidance'])

    def test_fine_action_skeleton_is_a_bound_range_of_existing_template_not_a_rewrite(self):
        for function, excluded in [('theory.mechanism_link', '[事件分段2]'),
                                   ('results.indirect_effect_report', 'To examine mediation')]:
            with self.subTest(function=function):
                candidate = self.contract_first(function)
                skeleton = candidate['adaptation_card']['skeleton']
                self.assertEqual(skeleton['selection'], 'authored_span')
                self.assertEqual(len(skeleton['templates']), 1)
                focused = skeleton['templates'][0]
                source = next(t for t in candidate['templates'] if t['uid'] == focused['uid'])
                self.assertEqual(source['text'][focused['source_text_start']:focused['source_text_end']].strip(), focused['text'])
                self.assertNotIn(excluded, focused['text'])
                self.assertIn(excluded, source['text'])

    def test_skeleton_range_cannot_reference_another_block_or_a_reversed_range(self):
        owner = next(d['source']['parent_paragraph'] for d in self.catalog['function_definitions']
                     if d['id'] == 'theory.mechanism_link')
        block = [copy.deepcopy(r) for r in self.catalog['entries'] if r['parent_paragraph'] == owner]
        for span in ({'start': 'absent cue 999'}, {'start': '[事件分段2]', 'end_before': '[基线]'}):
            rows = copy.deepcopy(block)
            for row in rows:
                row['retrieval_move']['skeleton_span'] = span
            with self.subTest(span=span), self.assertRaisesRegex(ValueError, 'skeleton_span'):
                bc.collect_function_definitions(rows, function_specs(self.catalog))

    def test_fine_skeleton_range_does_not_shorten_a_different_writing_action(self):
        candidate = self.contract_first('theory.mechanism_link')
        broad_spec = next(s for s in function_specs(self.catalog) if s['id'] == 'theory.mechanism')
        templates, focused = ac.expression_skeletons(candidate, [broad_spec])
        self.assertFalse(focused)
        self.assertEqual([t['text'] for t in templates], [t['text'] for t in candidate['templates']])

    def test_existing_skeleton_range_inherits_authored_actions_without_new_scope_field(self):
        candidate = self.contract_first('theory.mechanism_link')
        candidate['retrieval_move']['skeleton_span'].pop('functions')
        meta = candidate['retrieval_move']
        self.assertEqual(bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps(meta) + ' -->']), meta)
        template, focused = ac.expression_skeletons(candidate, [{'id': 'theory.mechanism_link'}])
        self.assertTrue(focused)
        self.assertEqual(template[0]['scope'], 'authored_span')
        _, other = ac.expression_skeletons(candidate, [{'id': 'theory.mechanism'}])
        self.assertFalse(other)

    def test_same_paragraph_windows_are_actual_text_and_neighbours_stay_separate(self):
        candidate = self.contract_first('theory.mechanism_link')
        source = candidate['adaptation_card']['source_context']['excerpt_sources'][0]
        self.assertEqual(source['archive_state'], 'citation_discrepancy')
        window = source['paragraph_windows'][0]
        paragraph = source['archive_context']['paragraphs'][0]
        actual = ac.normalized(paragraph['text'])
        self.assertEqual(actual[:window['matched_spans'][0]['start']].strip(), window['before'])
        self.assertEqual(actual[window['matched_spans'][-1]['end']:].strip(), window['after'])
        self.assertIn('Bass diffusion model', window['before'])
        self.assertIn('Specifically, we assume', window['after'])
        self.assertNotEqual(source['archive_context']['preceding_paragraph']['text'], window['before'])

    def test_renderer_version_changes_are_bound_to_retrieval(self):
        baseline = retrieval_version(self.catalog)
        with tempfile.TemporaryDirectory() as home:
            path = Path(home) / 'renderer.py'
            path.write_text('# a different presentation implementation', encoding='utf-8')
            with patch.object(ac, '__file__', str(path)):
                changed = retrieval_version(self.catalog)
        self.assertNotEqual(baseline['ranker'], changed['ranker'])
        self.assertEqual(baseline['corpus'], changed['corpus'])

    def test_new_paragraph_metadata_rejects_unusable_values_but_remains_optional(self):
        for fields in ({'advances': ''}, {'position': 2}, {'next_evidence': []},
                       {'next_evidence': 'guess evidence'}, {'next_evidence': [None]},
                       {'skeleton_span': {'start': ''}}, {'skeleton_span': {'start': 'cue', 'end_before': 2}}):
            with self.subTest(fields=fields), self.assertRaises(ValueError):
                bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps({'functions': [], **fields}) + ' -->'])
        self.assertEqual(bc.retrieval_metadata(['<!-- retrieval-move: {"functions":[]} -->']), {'functions': []})

    def test_batch_cli_renders_six_sections_and_no_match_without_logging_use(self):
        with tempfile.TemporaryDirectory() as home:
            batch = Path(home) / 'requests.json'
            output = Path(home) / 'cards.md'
            batch.write_text(json.dumps([
                {'id': 'risk-handoff', 'query': '', 'actions': [RISK, MITIGATION],
                 'conditions': DID_CONDITIONS, 'top': 1, 'supplement_top': 0},
                {'id': 'unresolved', 'query': '', 'need': '承认内生性风险，然后报告量子识别证明999'},
            ], ensure_ascii=False), encoding='utf-8')
            run = subprocess.run([sys.executable, '-X', 'utf8', '-B', str(ROOT / '_shared/indexing/retrieve.py'),
                                  '--batch', str(batch), '--format', 'cards', '--out', str(output)],
                                 capture_output=True, text=True, encoding='utf-8', timeout=90)
            self.assertEqual(run.returncode, 0, run.stderr)
            text = output.read_text(encoding='utf-8')
            for _, label in ac.SECTIONS:
                self.assertEqual(text.count('**' + label + '**'), 1)
            self.assertIn('本地档案原段落', text)
            self.assertIn('未找到满足当前动作的主候选', text)
            self.assertIn('报告量子识别证明999', text)
            self.assertFalse((Path(home) / 'observations.jsonl').exists())


if __name__ == '__main__':
    unittest.main()
