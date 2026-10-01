"""Curated actions survive wording variation without filling source gaps."""
import copy
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from retrieve import function_checks, function_specs, load_catalog, search
from adaptation_cards import render_candidate

CONCESSION = 'theory.concession_direction'
SPILLOVER = 'theory:5be33f8ba4b509fb63eda86c'
SCOPING = 'theory:67e80f1745fb43b8faabb766'
CAUTION = 'results:208f6d42ee1f35a23d6c6ac8'


class CuratedFunctionEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()

    def fixture(self, uid):
        block = next(r['parent_paragraph'] for r in self.catalog['entries'] if r['uid'] == uid)
        return {**self.catalog, 'entries': [copy.deepcopy(r) for r in self.catalog['entries']
                                          if r['parent_paragraph'] == block]}

    def test_curated_originals_match_without_legacy_connectors(self):
        for uid in (SPILLOVER, SCOPING):
            with self.subTest(uid=uid):
                data = self.fixture(uid)
                result = search('', CONCESSION, catalog=data)
                candidate = result['candidates'][0]
                check = candidate['function_matching']['actions'][0]
                self.assertTrue(check['complete'])
                self.assertEqual(check['expression_check_basis'], 'authored_original_evidence')
                self.assertEqual(candidate['adaptation_card']['original']['preferred_uids'], [uid])
                # Annotation establishes fit; it does not claim archive verification.
                original = next(r for r in candidate['originals'] if r['uid'] == uid)
                self.assertEqual(original['source_context']['state'], 'not_found')
                self.assertEqual(candidate['condition_check']['state'], 'unknown')

    def test_partial_or_unsupported_tags_retain_expression_checks(self):
        for mode in ('partial', 'implicit', 'missing_cue', 'template'):
            with self.subTest(mode=mode):
                data = self.fixture(SPILLOVER)
                for row in data['entries']:
                    meta = row['retrieval_move']
                    if mode == 'partial':
                        meta['function_support'][CONCESSION] = 'partial'
                    elif mode == 'implicit':
                        meta.pop('function_support')
                    elif mode == 'missing_cue':
                        meta['function_evidence'][CONCESSION]['cue'] = 'absent supporting cue'
                    else:
                        meta['function_evidence'][CONCESSION] = {
                            'kind': 'template', 'cue': 'This follows from the idea', 'why': 'Template only.'}
                result = search('', CONCESSION, catalog=data)
                self.assertFalse(result['candidates'])
                spec = next(s for s in function_specs(data) if s['id'] == CONCESSION)
                self.assertEqual(function_checks(data['entries'], [spec])[0]['expression_check_basis'],
                                 'lexical_rule')

    def test_old_template_cannot_fill_its_incomplete_original(self):
        definition = next(d for d in self.catalog['function_definitions'] if d['id'] == CONCESSION)
        row = next(r for r in self.catalog['entries']
                   if r['parent_paragraph'] == definition['source']['parent_paragraph'])
        data = self.fixture(row['uid'])
        self.assertTrue(any(r['kind'] == 'template' for r in data['entries']))
        result = search('', CONCESSION, catalog=data)
        self.assertEqual(result['reason'], 'no_fit')
        self.assertFalse(result['candidates'])

    def test_legacy_checks_do_not_join_opposing_sources(self):
        data = self.fixture(SPILLOVER)
        originals = [r for r in data['entries'] if r['kind'] == 'verbatim']
        for row, source, text in zip(originals, ('source_one', 'source_two'), (
                'Although a contrary direction is plausible, it remains possible.',
                'We expect the focal direction because our mechanism supports it.')):
            row.update(citekey=source, source_key_kind='single_key', text=text,
                       source_file='write-theory/corpus/sentences/acknowledgment_response.md',
                       block_title='反向机制回应', retrieval_move={})
        spec = next(s for s in function_specs(data) if s['id'] == CONCESSION)
        check = function_checks(originals, [spec])[0]
        self.assertFalse(check['complete'])
        self.assertEqual(check['original_support'], 'missing_or_split_source')

    def test_curated_fit_still_requires_actual_conditions(self):
        for uid, function in ((SPILLOVER, CONCESSION), (SCOPING, CONCESSION),
                              (CAUTION, 'results.null_caution')):
            data = self.fixture(uid)
            required = data['entries'][0]['retrieval_move']['applicability']['required_facts']
            good = search('', function, catalog=data, conditions={'facts': required})
            self.assertEqual(good['candidates'][0]['condition_check']['state'], 'compatible')
            for fact in required:
                with self.subTest(uid=uid, fact=fact):
                    bad = search('', function, catalog=data,
                                 conditions={'facts': {**required, fact: False}})
                    self.assertFalse(bad['candidates'])
                    self.assertFalse(bad['supplementary_candidates'])

    def test_concession_card_shows_supporting_excerpt_and_focused_skeleton(self):
        candidate = search('', CONCESSION, catalog=self.fixture(SPILLOVER))['candidates'][0]
        card = candidate['adaptation_card']
        self.assertEqual(card['original']['selection_basis'], 'authored_function_evidence')
        self.assertEqual(card['skeleton']['selection'], 'authored_span')
        skeleton = card['skeleton']['templates'][0]['text']
        self.assertTrue(skeleton.startswith('Although rivals'))
        self.assertIn('This follows from the idea', skeleton)
        self.assertNotIn('H2a', skeleton)
        self.assertNotIn('H2b', skeleton)
        rendered = render_candidate(candidate, ROOT)
        self.assertIn('should still fare better', rendered)
        self.assertNotIn('common owners may be especially motivated', rendered)

    def test_null_caution_retains_observation_scope_and_omissions(self):
        candidate = search('', 'results.null_caution', catalog=self.fixture(CAUTION))['candidates'][0]
        original = candidate['adaptation_card']['original']['excerpts'][0]
        self.assertIn('not a significant predictor', original['text'])
        self.assertIn('during the period of observation', original['text'])
        self.assertIn('...', original['text'])
        self.assertEqual(candidate['adaptation_card']['source_context']['state'], 'local_archive_located')

    def test_power_supported_negligible_effect_is_not_absence_caution(self):
        data = self.fixture('results:ca272ed912f5b36697de2e5f')
        self.assertFalse(search('', 'results.null_caution', catalog=data)['candidates'])
        self.assertTrue(search('', 'results.null', catalog=data)['candidates'])


if __name__ == '__main__':
    unittest.main()
