"""Function, applicability, ordered source support and topic ranking regressions."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
import build_catalog as bc
import request_matching as rm
from retrieve import function_specs, load_catalog, search
from log_exemplar import observations, record_observation, record_returned

RISK = 'methods.endogeneity_risk'
MITIGATION = 'methods.design_mitigation'
CONDITIONS = {'design': 'did', 'evidence': 'quasi_experimental',
              'claim_scope': 'causal_with_assumptions', 'facts': {'plausibly_exogenous_shock': True}}


class LayeredRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.specs = function_specs(cls.catalog)
        cls.original = next(r for r in cls.catalog['entries'] if r['kind'] == 'verbatim' and
                            RISK in r.get('retrieval_move', {}).get('functions', []) and
                            r['source_file'].endswith('自然实验-DiD.md'))

    def fixture(self, suffix, text=None, applicability=None, functions=None):
        row = copy.deepcopy(self.original)
        row['uid'] += suffix
        row['parent_paragraph'] += suffix
        row['source_excerpt_id'] += suffix
        if text is not None:
            row['text'] = text
        row['retrieval_move'].pop('definitions', None)
        row['retrieval_move'].pop('sequence', None)
        if applicability is None:
            row['retrieval_move'].pop('applicability', None)
        else:
            row['retrieval_move']['applicability'] = applicability
        if functions is not None:
            row['retrieval_move']['functions'] = functions
        return row

    def data(self, *rows):
        return {**self.catalog, 'entries': list(rows)}

    def test_function_accurate_different_topic_precedes_topic_only_supplement(self):
        correct = self.fixture('correct', 'A different subject still needs an endogeneity explanation.', functions=[RISK])
        wrong = self.fixture('wrong', ' '.join('topic' + str(i) for i in range(30)), functions=[])
        result = search(wrong['text'], RISK, catalog=self.data(correct, wrong))
        self.assertEqual(result['candidates'][0]['originals'][0]['uid'], correct['uid'])
        self.assertFalse(result['candidates'][0]['content_matches'])
        supplement = result['supplementary_candidates'][0]
        self.assertEqual(supplement['originals'][0]['uid'], wrong['uid'])
        self.assertEqual(supplement['candidate_role'], 'supplementary')
        self.assertTrue(supplement['function_matching']['uncertain'])

    def test_compatible_conditions_precede_more_topic_hits_with_unknown_conditions(self):
        correct = self.fixture('known', 'unrelated subject', applicability={'design': ['did']}, functions=[RISK])
        unknown = self.fixture('unknown', 'topic alpha beta gamma', functions=[RISK])
        result = search('topic alpha beta gamma', RISK, conditions={'design': 'did'}, catalog=self.data(correct, unknown))
        self.assertEqual(result['candidates'][0]['condition_check']['state'], 'compatible')
        self.assertEqual(result['candidates'][1]['condition_check']['state'], 'unknown')
        self.assertGreater(result['candidates'][1]['content_score'], result['candidates'][0]['content_score'])

    def test_known_design_evidence_scope_or_fact_conflict_is_excluded_not_supplemented(self):
        for conditions in ({**CONDITIONS, 'design': 'iv'}, {**CONDITIONS, 'evidence': 'randomized'},
                           {**CONDITIONS, 'claim_scope': 'causal'},
                           {**CONDITIONS, 'facts': {'plausibly_exogenous_shock': False}}):
            with self.subTest(conditions=conditions):
                result = search('common ownership', RISK, conditions=conditions,
                                catalog=self.data(copy.deepcopy(self.original)))
                self.assertEqual(result['reason'], 'no_fit')
                self.assertFalse(result['candidates'] + result['supplementary_candidates'])
                self.assertEqual(result['stage_counts']['condition_conflicts'], 1)

    def test_missing_facts_stay_unknown_and_negative_keyword_mention_cannot_pass(self):
        row = self.fixture('negative', 'This design is not randomized.',
                           applicability={'design': ['did'], 'required_facts': {'plausibly_exogenous_shock': True}})
        missing = search('', RISK, conditions={'design': 'did'}, catalog=self.data(row))['candidates'][0]
        self.assertEqual(missing['condition_check']['state'], 'unknown')
        self.assertIn('facts.plausibly_exogenous_shock', missing['condition_check']['unknowns'])
        conflict = search('randomized', RISK, conditions={'design': 'randomized'}, catalog=self.data(row))
        self.assertFalse(conflict['candidates'] + conflict['supplementary_candidates'])

    def test_real_need_recognizes_two_ordered_actions_with_same_source_and_context(self):
        result = search('产品召回', 'methods.identification',
                        need='承认内生性风险，然后解释设计如何缓解风险',
                        conditions=CONDITIONS, catalog=self.catalog)
        self.assertEqual(result['functions'], [RISK, MITIGATION])
        self.assertEqual(result['parsed_request']['mode'], 'sequence')
        first = result['candidates'][0]
        self.assertIn('内生性点名', first['block_title'])
        self.assertEqual(first['condition_check']['state'], 'compatible')
        sequence = first['function_matching']['sequence']
        self.assertEqual(sequence['state'], 'source_bound_order')
        self.assertEqual(sequence['archive_order']['state'], 'verified_order')
        self.assertEqual(sequence['original_contiguity'], 'one_paragraph')
        uids = {r['uid'] for r in first['originals']}
        self.assertTrue(all(set(step['source_uids']) <= uids for step in sequence['steps']))
        self.assertIn('source_context', first['originals'][0])
        self.assertTrue(first['function_matching']['uncertain'])  # aliases are inferred, not a semantic oracle

    def test_unknown_second_action_is_not_silently_dropped(self):
        result = search('ownership', 'methods.identification',
                        need='承认内生性风险，然后报告量子识别证明999', catalog=self.catalog)
        self.assertEqual(result['reason'], 'unresolved_action_sequence')
        self.assertFalse(result['candidates'])
        self.assertEqual(result['parsed_request']['unresolved_actions'], ['报告量子识别证明999'])

    def test_reversed_sequence_and_template_substitution_cannot_be_primary(self):
        reversed_result = search('common ownership', actions=[MITIGATION, RISK], catalog=self.catalog)
        self.assertFalse(reversed_result['candidates'])
        self.assertTrue(reversed_result['supplementary_candidates'])
        row = copy.deepcopy(self.original)
        row['kind'] = 'template'
        templates = search('common ownership', actions=[RISK, MITIGATION], catalog=self.data(row))
        self.assertFalse(templates['candidates'])

    def test_one_card_cannot_stitch_two_papers_into_a_sequence(self):
        first, second = copy.deepcopy(self.original), copy.deepcopy(self.original)
        steps = first['retrieval_move']['sequence']
        first['text'], second['text'] = steps[0]['cue'], steps[1]['cue']
        second['uid'] += 'second'
        second['source_excerpt_id'] += 'second'
        second['citekey'] = 'another_paper2026'
        result = search('common ownership', actions=[RISK, MITIGATION], catalog=self.data(first, second))
        self.assertFalse(result['candidates'])
        self.assertEqual(rm.action_sequence([first, second], [{'id': RISK}, {'id': MITIGATION}])['state'],
                         'unverified_source_or_order')

    def test_card_order_cannot_override_contradictory_archive_order(self):
        row = copy.deepcopy(self.original)
        steps = row['retrieval_move']['sequence']
        row['source_context'] = {'state': 'matched', 'paragraphs': [{
            'source_file': 'synthetic-source.sentences.md', 'source_line': 1, 'source_end_line': 3,
            'source_section': 'methods', 'paragraph_number': 1,
            'text': steps[1]['cue'] + '. ' + steps[0]['cue']}]}
        result = search('', actions=[RISK, MITIGATION], catalog=self.data(row))
        self.assertFalse(result['candidates'])
        self.assertEqual(rm.action_sequence([row], [{'id': RISK}, {'id': MITIGATION}])['state'], 'archive_order_conflict')

    def test_existing_compound_contract_also_requires_one_original_source(self):
        first = copy.deepcopy(next(r for r in self.catalog['entries'] if r['kind'] == 'verbatim' and
                                   '双刃限定' in r['block_title']))
        second = copy.deepcopy(first)
        first['text'] = 'Although action could carry risk, the outcome is uncertain.'
        second['text'] = 'We expect a positive outcome because the focal condition mitigates this risk.'
        second['uid'] += 'another-source'
        first['citekey'], second['citekey'] = 'synthetic_paper_a', 'synthetic_paper_b'
        first['source_key_kind'] = second['source_key_kind'] = 'single_key'
        result = search('', 'theory.concession_direction', catalog=self.data(first, second))
        self.assertFalse(result['candidates'])
        second['citekey'] = first['citekey']
        self.assertTrue(search('', 'theory.concession_direction', catalog=self.data(first, second))['candidates'])

    def test_source_support_breaks_a_tie_after_function_conditions_and_topic(self):
        bound = self.fixture('z-bound', 'topic', functions=[RISK])
        pending = self.fixture('a-pending', 'topic', functions=[RISK])
        bound['source_context'] = {'state': 'matched'}
        pending['source_context'] = {'state': 'not_found'}
        result = search('topic', RISK, catalog=self.data(pending, bound))
        self.assertEqual(result['candidates'][0]['originals'][0]['uid'], bound['uid'])
        self.assertEqual(result['candidates'][0]['source_support']['level'], 'archive_bound')
        self.assertEqual(result['candidates'][1]['condition_check']['state'], 'not_checked')

    def test_real_designs_are_distinguished_without_default_source_status_downgrade(self):
        for design, title in [('did', '内生性点名'), ('heckman', 'Heckman 选择模型'), ('iv', 'abundance of caution')]:
            with self.subTest(design=design):
                result = search('', actions=[RISK, MITIGATION], conditions={'design': design}, catalog=self.catalog)
                self.assertIn(title, result['candidates'][0]['block_title'])
                self.assertEqual(result['candidates'][0]['function_matching']['sequence']['state'], 'source_bound_order')
                self.assertEqual(result['candidates'][0]['condition_check']['state'], 'unknown')

    def test_indirect_estimate_need_cannot_be_displaced_by_archive_bound_legacy_claim(self):
        result = search('attention mediation', 'results.mediation',
                        need='说明注意力机制证据及间接效应边界', catalog=self.catalog)
        self.assertEqual(result['function'], 'results.indirect_effect_report')
        self.assertIn('indirect effect =', result['candidates'][0]['originals'][0]['text'])
        self.assertEqual(result['candidates'][0]['function_match_basis'], 'authored_metadata')
        self.assertFalse(any('legacy Kenny' in c['block_title'] for c in result['candidates']))

    def test_legacy_mediation_is_retained_for_its_declared_evidence_scope(self):
        row = next(r for r in self.catalog['entries'] if r['kind'] == 'verbatim' and 'legacy Kenny' in r['block_title'])
        modern = search('mediation', 'results.mediation', conditions={'evidence': 'indirect_effect_test'},
                        catalog=self.data(row))
        self.assertFalse(modern['candidates'] + modern['supplementary_candidates'])
        legacy = search('mediation', 'results.mediation', conditions={
            'evidence': 'legacy_mediation', 'claim_scope': 'association', 'facts': {'legacy_mediation_intended': True}},
            catalog=self.data(row))
        self.assertEqual(legacy['candidates'][0]['condition_check']['state'], 'compatible')
        self.assertEqual(legacy['candidates'][0]['originals'][0]['status'], row['status'])

    def test_dyadic_probability_form_cannot_transfer_to_confirmed_single_unit_design(self):
        row = next(r for r in self.catalog['entries'] if r['kind'] == 'verbatim' and
                   'Dyadic Event-Probability Monotonic Form' in r['block_title'])
        unknown = search('', 'theory.hypothesis_main', catalog=self.data(row))
        self.assertEqual(unknown['candidates'][0]['condition_check']['state'], 'unknown')
        self.assertIn('facts.dyadic_unit', unknown['candidates'][0]['condition_check']['unknowns'])
        conflict = search('probability', 'theory.hypothesis_main', conditions={'facts': {'dyadic_unit': False}},
                          catalog=self.data(row))
        self.assertFalse(conflict['candidates'] + conflict['supplementary_candidates'])

    def test_metadata_rejects_invalid_conditions_foreign_cues_and_wrong_order(self):
        for meta in ({'functions': [], 'applicability': {'facts': {}}},
                     {'functions': [], 'applicability': {'design': []}},
                     {'functions': [RISK], 'function_support': {MITIGATION: 'partial'}}):
            with self.subTest(meta=meta), self.assertRaises(ValueError):
                bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps(meta) + ' -->'])
        for change in ('foreign', 'reverse'):
            row = copy.deepcopy(self.original)
            row['retrieval_move'].pop('definitions')
            if change == 'foreign':
                row['retrieval_move']['sequence'][1]['cue'] = 'not-in-this-card-999'
            else:
                row['retrieval_move']['sequence'].reverse()
            with self.subTest(change=change), self.assertRaisesRegex(ValueError, 'sequence'):
                bc.collect_function_definitions([row], self.specs)
        self.assertIn('_shared/indexing/request_matching.py', self.catalog['dependencies'])

    def test_supplements_are_query_bound_with_consecutive_global_ranks(self):
        result = search('地位 声誉 status reputation', 'theory.construct_contrast', catalog=self.catalog)
        supplements = result['supplementary_candidates']
        self.assertTrue(supplements)
        all_cards = result['candidates'] + supplements
        self.assertEqual([c['rank'] for c in all_cards], list(range(1, len(all_cards) + 1)))
        with tempfile.TemporaryDirectory() as home:
            record_returned(result, self.catalog, home)
            uid = supplements[0]['originals'][0]['uid'] if supplements[0]['originals'] else supplements[0]['templates'][0]['uid']
            record_observation({'query_id': result['query_id'], 'actor': 'agent', 'state': 'opened',
                                'source_uids': [uid]}, self.catalog, home)
            events = observations(home)
            self.assertEqual(events[-1]['selected_ranks'], [supplements[0]['rank']])
            self.assertEqual(events[0]['candidates'][-1]['candidate_role'], 'supplementary')


if __name__ == '__main__':
    unittest.main()
