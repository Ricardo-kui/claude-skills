"""New Methods files cannot silently miss registration or retrieval."""
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
sys.path.insert(0, str(ROOT / 'distill-paper-exemplar/scripts'))
import check_all
import build_catalog as bc
from retrieve import search


class IncrementalGovernanceTests(unittest.TestCase):
    def registration_failures(self, files, registered):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            corpus=root/'write-methods/corpus'
            corpus.mkdir(parents=True)
            for rel in files:
                p=corpus/rel
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_text('### 变体 1: sample\n',encoding='utf-8')
            failures=[]
            mod=SimpleNamespace(FAMILIES=[{'file':rel} for rel in registered])
            with patch.object(check_all,'REPO',root), patch.object(check_all,'_load_adapter',return_value=mod):
                check_all.methods_registration_gate(failures.append)
            return failures

    def test_unregistered_root_and_nested_design_files_fail(self):
        for rel in ('new-design.md','new-designs/new-design.md'):
            failures=self.registration_failures([rel],[])
            self.assertEqual(len(failures),1)
            self.assertIn(rel,failures[0])
            self.assertIn('未登记进 FAMILIES',failures[0])

    def test_valid_registration_passes_and_deleted_registered_file_fails(self):
        self.assertFalse(self.registration_failures(['new-design.md'],['new-design.md']))
        failures=self.registration_failures([],['deleted-design.md'])
        self.assertEqual(len(failures),1)
        self.assertIn('不存在',failures[0])

    def test_derivatives_indexes_and_directly_routed_microtemplates_are_preserved(self):
        self.assertFalse(self.registration_failures(
            ['INDEX.md','_skeleton/new-design.md','_governance/note.md',
             'micro-templates/INDEX.md','micro-templates/opening.md'],[]))

    def test_registered_new_file_enters_native_catalog_and_function_retrieval(self):
        mod=bc.adapter('methods')
        family={'file':'new-design.md','slug':'new-design','name':'new design',
                'desc':'sample funnel','trigger':'sample'}
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            corpus=root/'write-methods/corpus'
            corpus.mkdir(parents=True)
            script=root/'write-methods/scripts/build_indices.py'
            script.parent.mkdir(parents=True)
            script.write_text('# isolated adapter dependency\n',encoding='utf-8')
            (corpus/'_evidence_registry.yaml').write_text('{}\n',encoding='utf-8')
            bridge=root/'_shared/indexing/retrieval-functions.json'
            bridge.parent.mkdir(parents=True, exist_ok=True)
            bridge.write_text((ROOT/'_shared/indexing/retrieval-functions.json').read_text(encoding='utf-8'),encoding='utf-8')
            (corpus/'new-design.md').write_text(
                '### 变体 1: sample funnel\n**槽位**: M2\n**适用条件**: archive sample\n'
                '**来源**: example2025\n'
                '**原始句锚点**: "We combined archival sources to construct the final sample."\n'
                '**骨架**:\n> We combined [sources] to construct [sample].\n',encoding='utf-8')
            with patch.object(bc,'ROOT',root), patch.object(bc,'SECTIONS',('methods',)), \
                 patch.object(bc,'adapter',return_value=mod), patch.object(mod,'CORPUS',corpus), \
                 patch.object(mod,'FAMILIES',[family]):
                data=bc.catalog_entries()
                result=search('archival sample','methods.sample',catalog=data)
            self.assertEqual(len(data['entries']),2)
            self.assertEqual(len(result['candidates']),1)
            candidate=result['candidates'][0]
            self.assertEqual(candidate['source_file'],'write-methods/corpus/new-design.md')
            self.assertEqual(candidate['originals'][0]['citekey'],'example2025')
            self.assertTrue(candidate['templates'])

    def test_four_single_section_entrypoints_reach_shared_completion_protocol(self):
        protocol=ROOT/'_shared/distillation-writeback-finalization.md'
        self.assertTrue(protocol.is_file())
        for section in ('introduction','theory','methods','results'):
            folder=ROOT/f'distill-{section}-exemplar'
            self.assertIn('../_shared/distillation-writeback-finalization.md',
                          (folder/'SKILL.md').read_text(encoding='utf-8'))
            reference=(folder/'references/phase-4-validation-writeback.md').read_text(encoding='utf-8')
            self.assertIn('../../_shared/distillation-writeback-finalization.md',reference)
            self.assertNotIn('corpus 同批提交',reference)

    def hygiene_failures(self, files, directories=()):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            for skill in check_all.SKILLS:
                (root/skill).mkdir()
            for rel in directories:
                (root/rel).mkdir(parents=True)
            for rel in files:
                p=root/rel
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_text('isolated fixture\n',encoding='utf-8')
            failures=[]
            with patch.object(check_all,'REPO',root):
                check_all.artifact_hygiene_gate(failures.append)
            return failures

    def test_hygiene_detects_transient_files_in_each_write_skill(self):
        files=['write-introduction/corpus/candidates.yaml',
               'write-theory/scripts/audit.tmp',
               'write-methods/corpus/example.md.bak-2026-09-30',
               'write-results/references/benchmark-results.json']
        failures=self.hygiene_failures(files)
        self.assertEqual(len(failures),4)
        for rel in files:
            self.assertTrue(any(rel.split('/',1)[1] in f for f in failures),rel)

    def test_hygiene_reports_cache_directory_once(self):
        failures=self.hygiene_failures(
            ['write-theory/scripts/__pycache__/a.pyc','write-theory/scripts/__pycache__/b.pyc'])
        self.assertEqual(len(failures),1)
        self.assertIn('__pycache__',failures[0])

    def test_hygiene_preserves_runtime_indices_and_governance_notebooks(self):
        files=['write-introduction/corpus/previews/findings-preview.md',
               'write-introduction/references/draft-revision-protocol.md',
               'write-theory/corpus/_skeleton/_id_aliases.json',
               'write-theory/corpus/_skill_design_feedback.yaml',
               'write-methods/corpus/_skeleton/_unparsed.md',
               'write-methods/corpus/_evidence_registry.yaml',
               'write-results/references/feedback-registry.json']
        self.assertFalse(self.hygiene_failures(files))


if __name__=='__main__':
    unittest.main()
