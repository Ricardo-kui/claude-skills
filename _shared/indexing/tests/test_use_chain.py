"""Actual read/write operations and linked use records; isolated fixtures only."""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from retrieve import load_catalog, search
from log_exemplar import observations, record_observation, record_returned, query_chain
from use_exemplar import open_exemplars, write_adaptation, record_adoption, file_hash
from fitness_report import sec_exemplar_use


class UseChainTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.requests = {
            'introduction': {'function': 'intro.attention_lens', 'query': '共同所有权 产品召回'},
            'theory': {'function': 'theory.construct_contrast', 'query': '地位 声誉'},
            'methods': {'query': '共同所有权', 'actions': ['methods.endogeneity_risk', 'methods.design_mitigation'],
                        'conditions': {'design': 'did', 'evidence': 'quasi_experimental',
                                       'claim_scope': 'causal_with_assumptions',
                                       'facts': {'plausibly_exogenous_shock': True}}},
            'results': {'function': 'results.hypothesis_not_supported', 'query': '非显著'},
        }

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / 'ledger'
        self.project = 'isolated-use-chain-fixture'

    def query(self, section='methods', *, opened=True):
        result = search(catalog=self.catalog, **self.requests[section])
        uid = result['candidates'][0]['originals'][0]['uid']
        record_returned(result, self.catalog, self.home, self.project)
        if opened:
            open_exemplars(result['query_id'], [uid], self.catalog, self.home)
        return result, uid

    def writing(self, result, uid, section='methods', **draft):
        return {'skill': f'write-{section}', 'section': section, 'project': self.project,
                'uses': [{'query_id': result['query_id'], 'source_uids': [uid]}],
                'draft': {'path': str(self.root / 'project' / f'{section}.md'),
                          'text': '【自动化联调夹具】已保存的改编文字；不代表真实研究或作者反馈。\n',
                          'location': 'test paragraph', **draft}}

    def cli(self, script, args, data=None):
        env = {**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONDONTWRITEBYTECODE': '1',
               'FITNESS_HOME': str(self.home)}
        return subprocess.run([sys.executable, '-B', str(ROOT / script), *args], cwd=ROOT, env=env,
                              input=json.dumps(data, ensure_ascii=False) if data is not None else None,
                              capture_output=True, text=True, encoding='utf-8')

    def test_four_sections_save_actual_files_and_keep_author_unknown(self):
        for section in self.requests:
            with self.subTest(section=section):
                result, uid = self.query(section)
                data = self.writing(result, uid, section)
                saved = write_adaptation(data, self.catalog, self.home)
                self.assertTrue(saved['written'])
                self.assertEqual(Path(saved['draft']['path']).read_text(encoding='utf-8'), data['draft']['text'])
                chain = query_chain(result['query_id'], self.home)
                self.assertEqual([e['state'] for e in chain['timeline']], ['returned', 'opened', 'adopted'])
                selected = next(s for s in chain['sources'] if s['uid'] == uid)
                self.assertTrue(selected['opened_with_file_evidence'])
                self.assertTrue(selected['adopted'])
                self.assertEqual(selected['author_status'], 'unknown')
                self.assertEqual(chain['consumption'][0]['use_id'], saved['use_id'])
                self.assertEqual(chain['timeline'][-1]['selected_ranks'], [1])
                self.assertEqual(chain['timeline'][-1]['retrieval_version'], result['retrieval_version'])

    def test_open_reads_real_archive_and_card_and_deduplicates_replay(self):
        result, uid = self.query(opened=False)
        opened = open_exemplars(result['query_id'], [uid], self.catalog, self.home)
        source = opened['sources'][0]
        original = next(p for p in source['archive_context'] if p['role'] == 'original_paragraph')
        lines = (ROOT / original['source_file']).read_text(encoding='utf-8').splitlines()
        self.assertEqual(original['text'], '\n'.join(lines[original['source_line'] - 1:original['source_end_line']]))
        self.assertIn('Institutions may choose to invest', original['text'])
        self.assertIn('retrieval-move', source['card_context'])
        open_exemplars(result['query_id'], [uid], self.catalog, self.home)
        self.assertEqual(len(observations(self.home)), 2)
        raw = (self.home / 'events/exemplar_use.jsonl').read_text(encoding='utf-8')
        self.assertNotIn(original['text'].splitlines()[0], raw)
        self.assertNotIn('card_context', raw)

    def test_pending_source_is_read_as_card_without_invented_archive(self):
        result = search('', 'intro.hook', catalog=self.catalog, top=30)
        rows = {r['uid']: r for r in self.catalog['entries']}
        uid = next(r['uid'] for c in result['candidates'] for r in c['originals']
                   if rows[r['uid']].get('source_context', {}).get('state') == 'not_found')
        record_returned(result, self.catalog, self.home, self.project)
        opened = open_exemplars(result['query_id'], [uid], self.catalog, self.home)
        self.assertEqual(opened['sources'][0]['source_context_state'], 'not_found')
        self.assertFalse(opened['sources'][0]['archive_context'])
        self.assertEqual({r['role'] for r in observations(self.home)[-1]['read_refs']}, {'corpus_card'})

    def test_multiple_queries_share_one_saved_revision_and_consumption(self):
        first, u1 = self.query('methods')
        second, u2 = self.query('theory')
        data = self.writing(first, u1)
        data['uses'].append({'query_id': second['query_id'], 'source_uids': [u2]})
        result = write_adaptation(data, self.catalog, self.home)
        write_adaptation(data, self.catalog, self.home)
        self.assertEqual(len(observations(self.home, 'consumption')), 1)
        adopts = [e for e in observations(self.home) if e['state'] == 'adopted']
        self.assertEqual(len(adopts), 2)
        self.assertEqual({e['use_id'] for e in adopts}, {result['use_id']})
        self.assertEqual({e['query_id'] for e in adopts}, {first['query_id'], second['query_id']})
        self.assertTrue(all(e['section'] == 'methods' for e in adopts))

    def test_unreturned_uid_missing_query_or_no_actual_open_prevent_write(self):
        result, uid = self.query(opened=False)
        data = self.writing(result, uid)
        with self.assertRaisesRegex(ValueError, 'actual file read'):
            write_adaptation(data, self.catalog, self.home)
        outside = next(r['uid'] for r in self.catalog['entries']
                       if r['uid'] not in observations(self.home)[0]['source_uids'])
        for q, u in [(result['query_id'], outside), ('missing-query', uid)]:
            with self.assertRaises(ValueError):
                open_exemplars(q, [u], self.catalog, self.home)
        self.assertFalse(Path(data['draft']['path']).exists())
        self.assertEqual(len(observations(self.home)), 1)

    def test_failed_source_read_is_not_recorded_as_opened(self):
        result, uid = self.query(opened=False)
        with patch.object(Path, 'read_bytes', side_effect=OSError('isolated read failure')):
            with self.assertRaises(OSError):
                open_exemplars(result['query_id'], [uid], self.catalog, self.home)
        self.assertEqual([e['state'] for e in observations(self.home)], ['returned'])

    def test_failed_draft_write_does_not_create_adoption(self):
        result, uid = self.query()
        data = self.writing(result, uid)
        with patch.object(Path, 'open', side_effect=OSError('isolated write failure')):
            with self.assertRaises(OSError):
                write_adaptation(data, self.catalog, self.home)
        self.assertFalse(Path(data['draft']['path']).exists())
        self.assertEqual([e['state'] for e in observations(self.home)], ['returned', 'opened'])
        self.assertFalse(observations(self.home, 'consumption'))

    def test_changed_corpus_requires_fresh_query_without_fabricating_read(self):
        result, uid = self.query(opened=False)
        stale = {**self.catalog, 'dependencies': {**self.catalog['dependencies'], 'changed': '0' * 64}}
        with self.assertRaisesRegex(ValueError, 'corpus changed'):
            open_exemplars(result['query_id'], [uid], stale, self.home)
        self.assertEqual(len(observations(self.home)), 1)

    def test_draft_guard_preserves_later_changes_and_allows_actual_revision(self):
        result, uid = self.query()
        path = self.root / 'existing.md'
        path.write_text('Existing manuscript.\n', encoding='utf-8')
        data = self.writing(result, uid, path=str(path), mode='replace', expected_sha256='0' * 64)
        with self.assertRaisesRegex(ValueError, 'changed since reading'):
            write_adaptation(data, self.catalog, self.home)
        self.assertEqual(path.read_text(encoding='utf-8'), 'Existing manuscript.\n')
        self.assertEqual(len(observations(self.home)), 2)
        data['draft']['expected_sha256'] = file_hash(path.read_bytes())
        self.assertTrue(write_adaptation(data, self.catalog, self.home)['written'])

    def test_append_retry_never_appends_text_or_counts_twice(self):
        result, uid = self.query()
        path = self.root / 'append.md'
        path.write_bytes(b'Before.\n')
        data = self.writing(result, uid, path=str(path), mode='append', expected_sha256=file_hash(path.read_bytes()))
        first = write_adaptation(data, self.catalog, self.home)
        second = write_adaptation(data, self.catalog, self.home)
        self.assertEqual(path.read_text(encoding='utf-8'), 'Before.\n' + data['draft']['text'])
        self.assertTrue(second['replayed_saved_revision'])
        self.assertEqual(first['use_id'], second['use_id'])
        self.assertEqual(len(observations(self.home)), 3)
        self.assertEqual(len(observations(self.home, 'consumption')), 1)

    def test_saved_native_artifact_requires_its_actual_fingerprint(self):
        result, uid = self.query()
        path = self.root / 'native-writer-fixture.docx'
        path.write_bytes(b'Isolated artifact fingerprint fixture; not a Word document.')
        data = self.writing(result, uid)
        data['draft'] = {'path': str(path), 'sha256': '0' * 64, 'location': 'fixture paragraph'}
        with self.assertRaisesRegex(ValueError, 'fingerprint differs'):
            record_adoption(data, self.catalog, self.home)
        data['draft']['sha256'] = file_hash(path.read_bytes())
        self.assertTrue(record_adoption(data, self.catalog, self.home)['consumption_recorded'])
        self.assertEqual(len(observations(self.home)), 3)

    def test_partial_consumption_failure_keeps_draft_and_repairs_only_missing_log(self):
        result, uid = self.query()
        data = self.writing(result, uid)
        with patch('use_exemplar.append_event', return_value=False):
            first = write_adaptation(data, self.catalog, self.home)
        self.assertTrue(first['written'])
        self.assertTrue(first['adopted_recorded'][0]['recorded'])
        self.assertFalse(first['consumption_recorded'])
        second = write_adaptation(data, self.catalog, self.home)
        self.assertTrue(second['consumption_recorded'])
        self.assertEqual(len(observations(self.home)), 3)
        self.assertEqual(len(observations(self.home, 'consumption')), 1)

    def test_partial_adoption_failure_keeps_draft_and_repairs_only_missing_log(self):
        result, uid = self.query()
        data = self.writing(result, uid)
        with patch('log_exemplar.append_event', return_value=False):
            first = write_adaptation(data, self.catalog, self.home)
        self.assertTrue(first['written'])
        self.assertFalse(first['adopted_recorded'][0]['recorded'])
        self.assertTrue(first['consumption_recorded'])
        self.assertEqual(len(query_chain(result['query_id'], self.home)['consumption']), 1)
        second = write_adaptation(data, self.catalog, self.home)
        self.assertTrue(second['adopted_recorded'][0]['recorded'])
        self.assertEqual(len(observations(self.home)), 3)
        self.assertEqual(len(observations(self.home, 'consumption')), 1)

    def test_author_evaluation_is_per_uid_and_agent_rejection_keeps_unknown(self):
        result, uid = self.query()
        other = result['candidates'][0]['templates'][0]['uid']
        base = {'query_id': result['query_id'], 'source_uids': [uid]}
        for bad in [dict(base, state='author_accepted', actor='agent', feedback='测试'),
                    dict(base, state='rejected', actor='author', reason_code='function_mismatch', reason='测试原因')]:
            with self.assertRaises(ValueError):
                record_observation(bad, self.catalog, self.home)
        # Explicit synthetic feedback exists only in this disposable test ledger.
        record_observation(dict(base, state='author_accepted', actor='author',
                                feedback='【夹具】我接受这一项。'), self.catalog, self.home)
        record_observation(dict(base, source_uids=[other], state='rejected', actor='agent',
                                reason_code='adaptation_difficulty', reason='【夹具】此骨架接入不顺。'),
                           self.catalog, self.home)
        selected = {s['uid']: s for s in query_chain(result['query_id'], self.home)['sources']}
        self.assertEqual(selected[uid]['author_status'], 'author_accepted')
        self.assertEqual(selected[other]['author_status'], 'unknown')
        self.assertIn('上下文', selected[other]['rejections'][0]['repair_target'])

    def test_feedback_can_bind_a_returned_uid_that_left_current_catalog(self):
        result, uid = self.query()
        changed = {**self.catalog, 'entries': [r for r in self.catalog['entries'] if r['uid'] != uid]}
        record_observation({'query_id': result['query_id'], 'source_uids': [uid],
                            'state': 'rejected', 'actor': 'author', 'feedback': '【夹具】来源仍待确认。',
                            'reason_code': 'source_unclear', 'reason': '【夹具】来源仍待确认。'}, changed, self.home)
        last = observations(self.home)[-1]
        self.assertEqual(last['retrieval_version'], result['retrieval_version'])
        self.assertEqual(last['selected_ranks'], [1])

    def test_prose_snapshots_and_wrong_draft_location_are_rejected_before_write(self):
        result, uid = self.query()
        data = self.writing(result, uid)
        with self.assertRaises(ValueError):
            write_adaptation({**data, 'body': 'prose snapshot'}, self.catalog, self.home)
        with self.assertRaises(ValueError):
            write_adaptation({**data, 'draft': {**data['draft'], 'location': ''}}, self.catalog, self.home)
        with self.assertRaises(ValueError):
            record_observation({'query_id': result['query_id'], 'source_uids': [uid],
                                'state': 'opened', 'actor': 'agent', 'originals': ['snapshot']},
                               self.catalog, self.home)
        self.assertFalse(Path(data['draft']['path']).exists())

    def test_skills_and_ledger_cannot_be_used_as_draft_destinations(self):
        result, uid = self.query()
        for target in [ROOT / '_shared/fixture-never-created.md', self.home / 'draft.md']:
            with self.assertRaises(ValueError):
                write_adaptation(self.writing(result, uid, path=str(target)), self.catalog, self.home)
            self.assertFalse(target.exists())

    def test_cli_executes_automatic_query_open_write_show_chain(self):
        script = '_shared/indexing/use_exemplar.py'
        found = self.cli(script, ['query', '地位 声誉', '--function', 'theory.construct_contrast',
                                  '--project', self.project])
        self.assertEqual(found.returncode, 0, found.stderr)
        result = json.loads(found.stdout)
        self.assertTrue(result['returned_recorded'])
        uid = result['candidates'][0]['originals'][0]['uid']
        opened = self.cli(script, ['open'], {'query_id': result['query_id'], 'source_uids': [uid]})
        self.assertEqual(opened.returncode, 0, opened.stderr)
        written = self.cli(script, ['write'], self.writing(result, uid, 'theory'))
        self.assertEqual(written.returncode, 0, written.stderr)
        shown = self.cli(script, ['show', '--query-id', result['query_id']])
        self.assertEqual(shown.returncode, 0, shown.stderr)
        chain = json.loads(shown.stdout)
        self.assertEqual([e['state'] for e in chain['timeline']], ['returned', 'opened', 'adopted'])
        self.assertEqual(next(s for s in chain['sources'] if s['uid'] == uid)['author_status'], 'unknown')

    def test_old_consumption_cli_requires_binding_for_new_uids_and_keeps_native_compatibility(self):
        result, uid = self.query()
        script = 'distill-paper-exemplar/scripts/fitness_ledger.py'
        anonymous = {'skill': 'write-methods', 'section': 'methods', 'project': self.project, 'source_uids': [uid]}
        bad = self.cli(script, ['log-consumption'], anonymous)
        self.assertEqual(bad.returncode, 2, bad.stderr)
        self.assertFalse(observations(self.home, 'consumption'))
        old = {'schema_v': 1, 'ts': '2026-09-01T00:00:00+08:00', **anonymous}
        path = self.home / 'events/consumption.jsonl'
        prior = (json.dumps(old) + '\n').encode('utf-8')
        path.write_bytes(prior)
        data = self.writing(result, uid)
        draft = self.root / 'from-native-writer.md'
        draft.write_bytes(b'Isolated saved draft.\n')
        data['draft'] = {'path': str(draft), 'sha256': file_hash(draft.read_bytes())}
        bridged = self.cli(script, ['log-consumption'], data)
        self.assertEqual(bridged.returncode, 0, bridged.stderr)
        self.assertEqual(len(observations(self.home, 'consumption')), 2)
        self.assertTrue(path.read_bytes().startswith(prior))
        native = self.cli(script, ['log-consumption'], {'skill': 'write-theory', 'section': 'theory',
                          'variants': ['<!-- wb:fixture2026:native_item -->'], 'project': self.project})
        self.assertEqual(native.returncode, 0, native.stderr)
        self.assertEqual(observations(self.home, 'consumption')[-1]['linkage'], 'legacy_native')
        self.assertEqual(len(query_chain(result['query_id'], self.home)['consumption']), 1)

    def test_chinese_legacy_stdin_works_without_python_encoding_override(self):
        env = {k: v for k, v in os.environ.items() if k not in ('PYTHONIOENCODING', 'PYTHONUTF8')}
        env['FITNESS_HOME'] = str(self.home)
        data = {'skill': 'write-theory', 'section': 'theory', 'project': '中文隔离夹具',
                'variants': ['<!-- wb:fixture2026:中文变体 -->']}
        run = subprocess.run([sys.executable, str(ROOT / 'distill-paper-exemplar/scripts/fitness_ledger.py'),
                              'log-consumption'], input=json.dumps(data, ensure_ascii=False),
                             cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(observations(self.home, 'consumption')[0]['project'], data['project'])
        self.assertEqual(observations(self.home, 'consumption')[0]['variants'], data['variants'])

    def test_report_exposes_missing_author_rating_without_inventing_feedback(self):
        result, uid = self.query()
        write_adaptation(self.writing(result, uid), self.catalog, self.home)
        out = []
        sec_exemplar_use(observations(self.home), out)
        self.assertIn('关联已保存草稿：1', '\n'.join(out))
        self.assertIn('作者评价未知：1', '\n'.join(out))
        self.assertFalse(any(e['actor'] == 'author' for e in observations(self.home)))


if __name__ == '__main__':
    unittest.main()
