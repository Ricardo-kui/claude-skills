"""Regression cases from the September 2026 corpus audit."""
import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / '_shared/indexing'))

def adapter(section):
    spec = importlib.util.spec_from_file_location(
        f'test_adapter_{section}', ROOT / f'write-{section}/scripts/build_indices.py')
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module

class CorpusIdentityTests(unittest.TestCase):
    def test_inline_framework_metadata_keeps_its_own_source(self):
        mod = adapter('theory')
        rows, _ = mod.parse_subprotocols(
            'corpus/subprotocols/moderator_selection_frameworks.md', mod.load_status_registry(), 'moderators')
        ridge = [r for r in rows if "TMT members' participation" in r.text and r.kind == 'verbatim']
        self.assertEqual(len(ridge), 1)
        self.assertEqual(ridge[0].citekey, 'Ridge_Aime_White_2013_SMJ')
        self.assertTrue(ridge[0].id.startswith('mechanism_participation_conditions_metaframework.'))
        mallapragada = [r for r in rows if r.text.startswith('Thus, as both CMO presence')]
        self.assertEqual(len(mallapragada), 1)
        self.assertIn('mallapragada', mallapragada[0].citekey.lower())

    def test_multi_source_quotes_are_individually_attributed(self):
        mod = adapter('theory')
        rows, _ = mod.parse_variants('corpus/variants/B_mechanism_elaboration.md', {}, 'B')
        wu = [r for r in rows if 'Following the enactment of anti-SLAPP laws' in r.text]
        self.assertEqual(len(wu), 1)
        self.assertEqual(wu[0].citekey, 'wu2025activism')
        keeves = [r for r in rows if r.kind == 'verbatim' and r.text.startswith('This prediction is formally equivalent')]
        self.assertGreaterEqual(len(keeves), 1)
        self.assertTrue(all(r.citekey == 'keeves_2017_asq' for r in keeves))

    def test_legacy_collision_is_explicit_not_first_match(self):
        mod = adapter('theory')
        rows = [mod.Entry('matrix-1', 'closure', 'a', 'EMERGING', '模板',
                          'Therefore [X] changes [Y].', 'a#close', '## close', 'a'),
                mod.Entry('matrix-1', 'definition', 'b', 'EMERGING', '模板',
                          'We define [X] as [definition].', 'b#define', '## define', 'b')]
        aliases = mod.assign_unique_ids(rows)
        self.assertEqual(len({r.id for r in rows}), 2)
        self.assertEqual([a['legacy_id'] for a in aliases], ['matrix-1', 'matrix-1'])
        rerun = [mod.Entry('matrix-1', r.func, r.citekey, r.status, r.kind, r.text,
                           r.anchor, r.heading, r.file) for r in rows]
        mod.assign_unique_ids(rerun)
        self.assertEqual([r.id for r in rows], [r.id for r in rerun])

    def test_lu_coordination_and_desjardine_channels_keep_their_own_sources(self):
        mod = adapter('theory')
        rows, _ = mod.parse_subprotocols('corpus/subprotocols/hypothesis_derivation_patterns.md',
                                        mod.load_status_registry(), 'derivation')
        lu = [r for r in rows if r.kind=='verbatim' and 'coordination mechanisms by which common owners' in r.text]
        self.assertEqual(len(lu), 1)
        self.assertEqual(lu[0].citekey, 'lu_et_al_2022_frenemies_corporate_advertising')
        self.assertTrue(lu[0].id.startswith('b_variant_e_mechanism_channel_instantiation_enumeration.'))
        desjardine = [r for r in rows if r.kind=='verbatim' and r.text.startswith('Influence begins with')]
        self.assertEqual(len(desjardine), 1)
        self.assertEqual(desjardine[0].citekey, 'desjardine_li_shi_2025_amj')

    def test_results_blank_line_before_multiline_quote_does_not_hide_asset(self):
        mod = adapter('results')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / 'example.md').write_text(
                '### 变体 A：placebo\n**槽位**: R7\n**模板**:\n\n'
                '> "We tested [alternative explanation]\n> using [placebo]."\n\n'
                '**原文锚定**:\n\n> "We randomly assigned event dates to test the model."\n'
                '**来源**: example2025\n', encoding='utf-8')
            original = mod.CORPUS
            mod.CORPUS = path
            try:
                rows, unparsed, _ = mod.parse_file({'file': 'example.md', 'slug': 'example'})
            finally:
                mod.CORPUS = original
        self.assertEqual(len(rows), 2)
        self.assertFalse(unparsed)
        self.assertEqual({r.status for r in rows}, {'verbatim', '模板'})

    def test_all_four_real_results_variants_now_have_borrowable_assets(self):
        mod = adapter('results')
        for filename, vids in [('事件研究法.md', {'18', '19', '20'}), ('Hawkes过程.md', {'A'})]:
            family = next(f for f in mod.FAMILIES if f['file'] == filename)
            rows, unparsed, _ = mod.parse_file(family)
            for vid in vids:
                self.assertTrue(any(r.vid == vid and r.status == '模板' for r in rows), (filename, vid))
                self.assertTrue(any(r.vid == vid and r.status == 'verbatim' for r in rows), (filename, vid))
                self.assertFalse(any(u.card == vid for u in unparsed), (filename, vid))

if __name__ == '__main__':
    unittest.main()
