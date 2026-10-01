"""Action contracts stay source-bound, distinct and invalidated by source edits."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
import build_catalog as bc
from retrieve import function_specs, load_catalog, resolve_function, search


class FineFunctionDefinitionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.bridge = function_specs(cls.catalog)

    def test_requested_twelve_actions_have_distinct_source_bound_contracts(self):
        expected = {
            'intro.gap_unexplained', 'intro.gap_conflicting_accounts', 'intro.gap_shared_assumption',
            'theory.actor_motivation', 'theory.mechanism_link', 'theory.condition_amplification',
            'results.robustness_alternative_explanation', 'results.robustness_identification_threat',
            'results.robustness_measurement_sensitivity', 'results.hypothesis_not_supported',
            'results.null_caution', 'results.mixed_synthesis',
        }
        definitions = {d['id']: d for d in self.catalog['function_definitions']}
        self.assertTrue(expected.issubset(definitions))
        for fid in expected:
            with self.subTest(function=fid):
                definition = definitions[fid]
                result = search('', fid, catalog=self.catalog)
                self.assertEqual(result['function_contract']['source'], definition['source'])
                self.assertTrue(result['candidates'])
                self.assertEqual(result['candidates'][0]['function_match_basis'], 'authored_metadata')

    def test_need_and_alias_resolve_to_the_canonical_action(self):
        direct = resolve_function('连接两个机制环节', catalog=self.catalog)
        refined = search('高管', 'theory.mechanism', need='连接两个机制环节', catalog=self.catalog)
        self.assertEqual(direct['id'], 'theory.mechanism_link')
        self.assertEqual(refined['function'], direct['id'])
        self.assertEqual(refined['function_contract']['definition'], direct['definition'])

    def test_template_concession_definition_does_not_fabricate_original_response(self):
        data = {**self.catalog, 'entries': self.owner_rows('theory.concession_direction')}
        result = search('', 'theory.concession_direction', catalog=data)
        self.assertEqual(result['function_contract']['positive_example']['kind'], 'template')
        self.assertEqual(result['reason'], 'no_fit')
        self.assertFalse(result['candidates'])

    def test_multiline_and_existing_inline_annotations_remain_readable(self):
        self.assertEqual(bc.retrieval_metadata(['<!-- retrieval-move: {"functions":[]} -->']), {'functions': []})
        self.assertEqual(bc.retrieval_metadata(['<!-- retrieval-move:', '{"functions":[]}', '-->']), {'functions': []})
        with self.assertRaises(ValueError):
            bc.retrieval_metadata(['<!-- retrieval-move: [] -->'])

    def owner_rows(self, function='intro.gap_unexplained'):
        definition = next(d for d in self.catalog['function_definitions'] if d['id'] == function)
        return copy.deepcopy([r for r in self.catalog['entries']
                              if r['parent_paragraph'] == definition['source']['parent_paragraph']])

    def test_references_can_reuse_a_definition_but_a_second_authority_is_rejected(self):
        rows = self.owner_rows()
        reference = copy.deepcopy(rows[0])
        reference['parent_paragraph'] = 'another-source-block'
        reference['retrieval_move'].pop('definitions')
        derived = bc.collect_function_definitions(rows + [reference], self.bridge)
        self.assertEqual(len(derived), 1)
        reference['retrieval_move']['definitions'] = copy.deepcopy(rows[0]['retrieval_move']['definitions'])
        with self.assertRaisesRegex(ValueError, 'multiple authoritative'):
            bc.collect_function_definitions(rows + [reference], self.bridge)

    def test_dangling_neighbors_missing_conditions_and_foreign_positive_cues_fail(self):
        for field, value, error in [
            ('neighbors', [{'id': 'imaginary.function', 'distinction': 'unregistered'}], 'unknown'),
            ('use_when', [], 'use_when'),
            ('positive_example', {'kind': 'verbatim', 'cue': 'not-in-this-source-block-999', 'why': 'foreign'}, 'absent'),
        ]:
            with self.subTest(field=field):
                rows = self.owner_rows()
                for row in rows:
                    row['retrieval_move']['definitions'][0][field] = copy.deepcopy(value)
                with self.assertRaisesRegex(ValueError, error):
                    bc.collect_function_definitions(rows, self.bridge)

    def test_source_change_refreshes_the_cached_definition(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, cache = root / 'source.md', root / 'catalog.json'
            source.write_text('new definition', encoding='utf-8')
            old = {'schema_version': 2, 'dependencies': {'source.md': bc.digest('old definition')},
                   'entries': [], 'function_definitions': [{'definition': 'old'}]}
            new = {**old, 'dependencies': {'source.md': bc.digest('new definition')},
                   'function_definitions': [{'definition': 'new'}]}
            cache.write_text(json.dumps(old), encoding='utf-8')
            with patch.object(bc, 'ROOT', root), patch.object(bc, 'catalog_entries', return_value=new) as rebuild:
                actual = load_catalog(cache)
            rebuild.assert_called_once()
            self.assertEqual(actual['function_definitions'][0]['definition'], 'new')
            self.assertEqual(json.loads(cache.read_text(encoding='utf-8')), new)

    def test_incomplete_disposable_cache_rebuilds_instead_of_breaking_retrieval(self):
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory) / 'catalog.json'
            new = {'dependencies': {}, 'entries': [], 'function_definitions': []}
            for broken in ('', '{"entries":', '[]', '{}'):
                cache.write_text(broken, encoding='utf-8')
                with self.subTest(cache=broken), patch.object(bc, 'catalog_entries', return_value=new) as rebuild:
                    self.assertEqual(load_catalog(cache), new)
                    rebuild.assert_called_once()
                self.assertEqual(json.loads(cache.read_text(encoding='utf-8')), new)

    def test_atomic_cache_publication_keeps_previous_view_readable_until_replace(self):
        with tempfile.TemporaryDirectory() as directory:
            cache = Path(directory) / 'catalog.json'
            cache.write_text('{"version":"old"}', encoding='utf-8')
            replace = bc.os.replace
            def observe_then_replace(temporary, destination):
                self.assertEqual(json.loads(cache.read_text(encoding='utf-8')), {'version': 'old'})
                self.assertEqual(json.loads(Path(temporary).read_text(encoding='utf-8')), {'version': 'new'})
                replace(temporary, destination)
            with patch.object(bc.os, 'replace', side_effect=observe_then_replace):
                bc.write_catalog(cache, '{"version":"new"}\n')
            self.assertEqual(json.loads(cache.read_text(encoding='utf-8')), {'version': 'new'})
            self.assertFalse(list(cache.parent.glob('*.tmp')))


if __name__ == '__main__':
    unittest.main()
