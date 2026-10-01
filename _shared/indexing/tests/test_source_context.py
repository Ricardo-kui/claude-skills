"""Real archive locality and conservative handling of ambiguous source matches."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from source_context import ARCHIVE_REL, attach_contexts, compatible, normalized, excerpt_chunks
from retrieve import load_catalog


class SourceContextTests(unittest.TestCase):
    def attach(self, keys, record_key='smith2020', text='This mechanism explains the strategic choices that firms make.'):
        with tempfile.TemporaryDirectory() as home:
            root=Path(home)
            folder=root/ARCHIVE_REL
            folder.mkdir(parents=True)
            for i,(key,paragraphs) in enumerate(keys):
                body='\n'.join(f'<!-- para {j+1} -->\n{p}' for j,p in enumerate(paragraphs))
                (folder/f'{i}.sentences.md').write_text(f'---\ncitekey: "{key}"\n---\n## theory\n{body}\n',encoding='utf-8')
            rows=[{'uid':'example','kind':'verbatim','citekey':record_key,'text':text}]
            deps=attach_contexts(rows,root,lambda s:hashlib.sha256(s.encode()).hexdigest())
            json.dumps(rows)  # Context neighbours must have no reference cycles.
            self.assertEqual(len(deps),len(keys))
            return rows[0]['source_context']

    def test_real_lu_and_desjardine_have_compatible_local_archive_context(self):
        c=load_catalog()
        rows=[r for r in c['entries'] if r['kind']=='verbatim' and
              r['source_file']=='write-theory/corpus/subprotocols/hypothesis_derivation_patterns.md' and
              r['id'].split('.')[0] in ('b_variant_e_mechanism_channel_instantiation_enumeration',
                                       'dual_channel_convergence','why_not_reverse_boundary_declaration')]
        self.assertEqual(len(rows),7)
        for r in rows:
            sc=r['source_context']
            self.assertIn(sc['state'],('matched','ambiguous_paragraph'),r['id'])
            self.assertTrue(sc['citation_agreement'])
            texts=[normalized(p['text']) for p in sc['paragraphs']]
            for chunk in excerpt_chunks(r['text']):
                self.assertTrue(any(chunk in t for t in texts),r['id'])
            for p in sc['paragraphs']:
                lines=(ROOT/p['source_file']).read_text(encoding='utf-8').splitlines()
                span='\n'.join(lines[p['source_line']-1:p['source_end_line']])
                self.assertIn(normalized(p['text']),normalized(span))

    def test_aliases_can_be_title_keys_or_concatenated_authors(self):
        self.assertTrue(compatible('pontikes2012','two_sides_elizabeth_pontikes_2012'))
        self.assertTrue(compatible('westphalzajac1995','westphal1995_who_shall_govern'))
        self.assertFalse(compatible('mao2022','mao_et_al_2021_before_it'))
        self.assertIsNone(compatible('unlabelled','smith2020'))

    def test_multiple_archives_and_repeated_paragraphs_remain_visible(self):
        text='This mechanism explains the strategic choices that firms make.'
        result=self.attach([('smith2020',[text]),('smith2020',[text])])
        self.assertEqual(result['state'],'ambiguous')
        result=self.attach([('smith2020',[text,text])])
        self.assertEqual(result['state'],'ambiguous_paragraph')
        self.assertEqual(len(result['paragraphs']),2)
        self.assertTrue(result['location_ambiguous'])

    def test_wrong_source_and_missing_text_are_not_verified_identity(self):
        text='This mechanism explains the strategic choices that firms make.'
        result=self.attach([('jones2021',[text])])
        self.assertEqual(result['state'],'citation_discrepancy')
        self.assertFalse(result['citation_agreement'])
        result=self.attach([('smith2020',['A different sentence without the quoted mechanism.'])])
        self.assertEqual(result['state'],'not_found')
        self.assertNotIn('paragraphs',result)


if __name__=='__main__':
    unittest.main()
