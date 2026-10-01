"""Additional labels must point to evidence in their own canonical source block."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
import build_catalog as bc

FUNCTION = 'theory.mechanism_link'
BRIDGE = [{'id': FUNCTION, 'section': 'theory'}]


class AnnotationEvidenceTests(unittest.TestCase):
    def row(self):
        return {'parent_paragraph': 'block-a', 'section': 'theory',
                'source_file': 'card.md', 'kind': 'verbatim',
                'text': 'A threat changes incentives, which leads to faster action.',
                'retrieval_move': {'functions': [FUNCTION], 'function_evidence': {
                    FUNCTION: {'kind': 'verbatim', 'cue': 'changes incentives, which leads',
                               'why': 'Connects threat, incentives and action.'}}}}

    def test_same_block_evidence_and_whitespace_normalization(self):
        row = self.row()
        row['text'] = row['text'].replace('which leads', 'which\n   leads')
        meta = row['retrieval_move']
        self.assertEqual(bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps(meta) + ' -->']), meta)
        self.assertEqual(bc.collect_function_definitions([row], BRIDGE), [])

    def test_another_block_or_template_cannot_supply_an_original_cue(self):
        original = self.row()
        for foreign in ('block', 'kind'):
            with self.subTest(foreign=foreign):
                target = copy.deepcopy(original)
                target['text'] = 'A different sentence about the same topic.'
                extra = copy.deepcopy(original)
                extra['retrieval_move'] = {}
                if foreign == 'block':
                    extra['parent_paragraph'] = 'block-b'
                else:
                    extra['kind'] = 'template'
                with self.assertRaisesRegex(ValueError, 'function_evidence cue absent'):
                    bc.collect_function_definitions([target, extra], BRIDGE)

    def test_malformed_or_foreign_function_evidence_is_rejected(self):
        good = self.row()['retrieval_move']
        for changes in ({'kind': 'generated'}, {'cue': ''}, {'why': ''}, {'why': 1},
                        {'extra': 'unvalidated'}):
            meta = copy.deepcopy(good)
            meta['function_evidence'][FUNCTION].update(changes)
            with self.subTest(changes=changes), self.assertRaisesRegex(ValueError, 'function_evidence'):
                bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps(meta) + ' -->'])
        good['function_evidence']['intro.gap_unexplained'] = good['function_evidence'][FUNCTION]
        with self.assertRaisesRegex(ValueError, 'function_evidence'):
            bc.retrieval_metadata(['<!-- retrieval-move: ' + json.dumps(good) + ' -->'])


if __name__ == '__main__':
    unittest.main()
