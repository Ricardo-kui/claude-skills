"""Source-locality and writing-need regressions, including misleading matches."""
import json
import re
import sys
import unittest
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from retrieve import load_catalog, search
from consumption_join import resolve_event
from log_exemplar import validate


class RetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()

    def test_every_verbatim_has_its_own_context_not_a_neighbour(self):
        for row in self.catalog['entries']:
            if row['kind'] != 'verbatim':
                continue
            lines = (ROOT / row['source_file']).read_text(encoding='utf-8').splitlines()
            lines = lines[(row['source_line'] or 1)-1:row['source_end_line']]
            context = ' '.join(re.sub(r'^\s*>\s?', '', line) for line in lines)
            self.assertIn(' '.join(row['text'].split()).strip('"'), ' '.join(context.split()), row['uid'])

    def test_unique_section_ids_and_excerpt_uids(self):
        rows = self.catalog['entries']
        self.assertEqual(len(rows), len({r['uid'] for r in rows}))
        collisions = [key for key, count in Counter((r['section'],r['id']) for r in rows).items() if count > 1]
        self.assertFalse(collisions, collisions)

    def test_ridge_is_retrieved_with_ridge_source(self):
        result = search('高管 participation succession tournament', 'theory.moderator_selection', catalog=self.catalog)
        original = result['candidates'][0]['originals']
        self.assertTrue(any(r['citekey'] == 'Ridge_Aime_White_2013_SMJ'
                            and "TMT members' participation" in r['text'] for r in original))

    def test_rare_binary_outcome_is_not_tobit_or_random_effects(self):
        result = search('产品召回 稀有事件 binary', 'methods.dv', catalog=self.catalog)
        first = result['candidates'][0]
        self.assertTrue(any('extensive margin' in r['text'] for r in first['originals']))
        self.assertTrue(first['templates'])

    def test_null_and_mixed_are_different_moves_for_same_topic(self):
        a = search('产品召回 interaction', 'results.null', catalog=self.catalog)
        b = search('产品召回 interaction', 'results.mixed', catalog=self.catalog)
        self.assertNotEqual(a['candidates'][0]['parent_paragraph'], b['candidates'][0]['parent_paragraph'])
        self.assertTrue(any('mixed' in r['text'].lower() or 'partial' in r['text'].lower()
                            for c in b['candidates'] for r in c['originals']))

    def test_unknown_function_and_impossible_design_are_explicit(self):
        unknown = search('产品召回', 'imaginary_function', catalog=self.catalog)
        self.assertFalse(unknown['candidates'])
        result = search('共同所有权 产品召回', 'methods.identification',
                        design='quantum-causal-inference-999', catalog=self.catalog)
        self.assertEqual(result['reason'], 'no_fit')
        self.assertFalse(result['candidates'])
        unmatched = search('zzzzabsentconcept98765', 'intro.hook', require_content=True, catalog=self.catalog)
        self.assertFalse(unmatched['candidates'])

    def test_real_legacy_aliases_join_all_five_without_editing_the_ledger(self):
        event = {'section':'methods', 'variants':[
            '<!-- wb:lun_zurbruegg_mount_2026_etp:rare-outcome-2 -->',
            '<!-- wb:zorn_shropshire_martin_combs_ketchen_2017_smj:rare-outcome-1 -->',
            '<!-- wb:pfarrer_pollock_and_rindova_2010:construct-object-10 -->',
            '<!-- wb:pollock_2015_asq:construct-object-4 -->',
            '<!-- wb:mao_dong_lee_2022_msom:construct-object-13 -->']}
        original = json.dumps(event)
        joined = resolve_event(event, self.catalog)
        self.assertEqual(len(joined['resolved']), 5)
        self.assertFalse(joined['unresolved'])
        self.assertEqual(json.dumps(event), original)
        bad = resolve_event({'section':'methods','variants':['<!-- wb:wrong_source:construct-object-4 -->']}, self.catalog)
        self.assertFalse(bad['resolved'])
        self.assertTrue(bad['unresolved'])

    def test_author_acceptance_cannot_be_inferred_from_agent_opening(self):
        uid = self.catalog['entries'][0]['uid']
        with self.assertRaises(ValueError):
            validate({'state':'author_accepted', 'actor':'agent', 'source_uids':[uid]}, self.catalog)
        with self.assertRaises(ValueError):
            validate({'state':'opened', 'actor':'agent', 'source_uids':['invalid']}, self.catalog)

    def test_template_and_paper_verbatim_provenance_are_distinct(self):
        row = next(r for r in self.catalog['entries'] if r['kind']=='template')
        self.assertEqual(row['provenance_level'], 'card_template')
        self.assertTrue(any(r['provenance_level']=='source_pending' for r in self.catalog['entries']))

    def test_author_override_wins_without_a_three_source_requirement(self):
        import rebuild_views as rv
        from build_catalog import governed_status
        from types import SimpleNamespace
        entry = SimpleNamespace(id='single.a',citekey='one_paper2025')
        registry={'status_overrides':{'overrides':{'patterns.single':{'status':'VERIFIED','basis':'explicit author ruling'}}}}
        status,basis = governed_status('theory',entry,'corpus/sentences/example.md',[],
                                       'EMERGING',registry,rv,rv.load_policy())
        self.assertEqual(status,'VERIFIED')
        self.assertEqual(basis[0]['scope'],'pattern_override')


if __name__ == '__main__':
    unittest.main()
