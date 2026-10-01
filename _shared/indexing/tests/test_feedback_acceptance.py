"""Acceptance of query/adoption-bound feedback; synthetic authors in temp ledgers only."""
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
from log_exemplar import observations, record_returned, record_observation, query_chain, REASONS
from use_exemplar import open_exemplars, write_adaptation, file_hash
from fitness_report import sec_exemplar_use


class FeedbackAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='feedback-acceptance-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / 'ledger'
        self.project = '隔离反馈验收夹具'
        self.result = self.query()
        self.uid = self.result['candidates'][0]['originals'][0]['uid']
        open_exemplars(self.result['query_id'], [self.uid], self.catalog, self.home)

    def query(self):
        result = search('地位 声誉', 'theory.construct_contrast', catalog=self.catalog)
        record_returned(result, self.catalog, self.home, self.project)
        return result

    def save(self, label='A', *, result=None, uids=None, draft=None, extra_uses=()):
        result = result or self.result
        return write_adaptation({'skill': 'write-theory', 'section': 'theory', 'project': self.project,
                'uses': [{'query_id': result['query_id'], 'source_uids': uids or [self.uid]}, *extra_uses],
                'draft': {'path': str(self.root / f'{label}.md'),
                          'text': f'【隔离验收夹具】{label}；不是用户稿件。\n', **(draft or {})}},
                                self.catalog, self.home)

    def feedback(self, **overrides):
        data = {'query_id': self.result['query_id'], 'source_uids': [self.uid],
                'state': 'author_accepted', 'actor': 'author',
                'feedback': '【模拟作者夹具】这一版可以采用。', **overrides}
        return record_observation(data, self.catalog, self.home)

    def source(self, uid=None, result=None):
        return next(s for s in query_chain((result or self.result)['query_id'], self.home)['sources']
                    if s['uid'] == (uid or self.uid))

    def test_unique_actual_adoption_is_bound_without_author_supplying_ids(self):
        saved = self.save()
        self.assertTrue(self.feedback())
        event = observations(self.home)[-1]
        self.assertEqual(event['feedback_scope'], 'adoption')
        self.assertEqual(event['use_id'], saved['use_id'])
        self.assertEqual(event['draft'], saved['draft'])
        self.assertEqual(event['adoption_event_id'], observations(self.home)[-2]['event_id'])
        self.assertEqual(event['retrieval_version'], self.result['retrieval_version'])
        self.assertEqual(event['selected_ranks'], [1])
        self.assertEqual(self.source()['adoptions'][0]['author_status'], 'author_accepted')

    def test_foreign_query_use_id_is_rejected_even_for_same_uid_and_project(self):
        first = self.save()
        other = self.query()
        open_exemplars(other['query_id'], [self.uid], self.catalog, self.home)
        self.save('Other', result=other)
        before = len(observations(self.home))
        with self.assertRaisesRegex(ValueError, 'does not match an adoption'):
            self.feedback(query_id=other['query_id'], use_id=first['use_id'])
        self.assertEqual(len(observations(self.home)), before)
        self.assertEqual(self.source(result=other)['author_status'], 'unknown')

    def test_returned_but_unadopted_uid_cannot_be_rated_as_part_of_use_id(self):
        saved = self.save()
        template = self.result['candidates'][0]['templates'][0]['uid']
        with self.assertRaises(ValueError):
            self.feedback(source_uids=[template], use_id=saved['use_id'])
        self.assertEqual(self.source(template)['author_status'], 'unknown')

    def test_false_draft_fingerprint_or_wrong_event_reference_is_rejected(self):
        saved = self.save()
        for change in [{'draft': {**saved['draft'], 'sha256': '0' * 64}},
                       {'draft': {**saved['draft'], 'path': str(self.root / 'wrong.md')}},
                       {'adoption_event_id': '0' * 64}]:
            with self.assertRaises(ValueError):
                self.feedback(use_id=saved['use_id'], **change)
        self.assertEqual(self.source()['author_status'], 'unknown')

    def test_multiple_adoptions_require_an_explicit_version(self):
        self.save('A')
        self.save('B')
        before = len(observations(self.home))
        with self.assertRaisesRegex(ValueError, 'ambiguous'):
            self.feedback()
        self.assertEqual(len(observations(self.home)), before)
        self.assertEqual(self.source()['author_status'], 'unknown')

    def test_new_draft_does_not_inherit_old_author_acceptance(self):
        first = self.save('A')
        self.feedback(use_id=first['use_id'])
        second = self.save('B')
        source = self.source()
        self.assertEqual(source['author_status'], 'unknown')
        versions = {v['use_id']: v for v in source['adoptions']}
        self.assertEqual(versions[first['use_id']]['author_status'], 'author_accepted')
        self.assertEqual(versions[second['use_id']]['author_status'], 'unknown')
        out = []
        sec_exemplar_use(observations(self.home), out)
        self.assertIn('作者评价未知：1', '\n'.join(out))
        self.assertIn('作者评价未知版本：1', '\n'.join(out))

    def test_late_old_version_feedback_remains_on_the_old_version(self):
        first = self.save('A')
        self.save('B')
        self.feedback(use_id=first['use_id'])
        source = self.source()
        self.assertEqual(source['author_status'], 'unknown')
        self.assertEqual(source['adoptions'][0]['author_status'], 'author_accepted')
        self.assertEqual(source['adoptions'][1]['author_status'], 'unknown')

    def test_feedback_uses_saved_revision_not_current_disk_contents(self):
        first = self.save('A')
        path = Path(first['draft']['path'])
        before_sha = file_hash(path.read_bytes())
        second = self.save('B', draft={'path': str(path), 'mode': 'replace', 'expected_sha256': before_sha})
        self.feedback(use_id=first['use_id'])
        event = observations(self.home)[-1]
        self.assertEqual(event['draft']['sha256'], before_sha)
        self.assertNotEqual(event['draft']['sha256'], second['draft']['sha256'])
        self.assertEqual(self.source()['author_status'], 'unknown')

    def test_candidate_acceptance_does_not_accept_a_subsequent_draft(self):
        self.feedback()
        self.assertEqual(observations(self.home)[-1]['feedback_scope'], 'candidate')
        self.save()
        source = self.source()
        self.assertEqual(source['candidate_author_status'], 'author_accepted')
        self.assertEqual(source['author_status'], 'unknown')
        self.assertEqual(source['adoptions'][0]['author_status'], 'unknown')

    def test_author_rating_is_per_uid_even_when_adoption_contains_two_sources(self):
        template = self.result['candidates'][0]['templates'][0]['uid']
        open_exemplars(self.result['query_id'], [template], self.catalog, self.home)
        saved = self.save(uids=[self.uid, template])
        self.feedback(use_id=saved['use_id'])
        self.assertEqual(self.source()['author_status'], 'author_accepted')
        self.assertEqual(self.source(template)['author_status'], 'unknown')

    def test_multi_query_use_id_does_not_propagate_feedback_to_other_queries(self):
        other = self.query()
        open_exemplars(other['query_id'], [self.uid], self.catalog, self.home)
        saved = self.save(extra_uses=[{'query_id': other['query_id'], 'source_uids': [self.uid]}])
        self.feedback(use_id=saved['use_id'])
        self.assertEqual(self.source()['author_status'], 'author_accepted')
        self.assertEqual(self.source(result=other)['author_status'], 'unknown')

    def test_agent_rejection_and_missing_quote_leave_author_unknown(self):
        saved = self.save()
        for change in [{'feedback': ''}, {'actor': 'agent'},
                       {'state': 'rejected', 'reason_code': 'function_mismatch', 'reason': '夹具', 'feedback': ''}]:
            with self.assertRaises(ValueError):
                self.feedback(use_id=saved['use_id'], **change)
        self.feedback(use_id=saved['use_id'], state='rejected', actor='agent',
                      reason_code='adaptation_difficulty', reason='【夹具】接入后承接不顺。')
        self.assertEqual(self.source()['author_status'], 'unknown')

    def test_rejection_reasons_route_and_replay_without_duplicate_events(self):
        saved = self.save()
        for code in ('function_mismatch', 'condition_mismatch', 'adaptation_difficulty', 'source_unclear'):
            self.feedback(use_id=saved['use_id'], state='rejected', reason_code=code,
                          reason=f'【夹具】{code}', feedback=f'【模拟作者夹具】{code}')
            count = len(observations(self.home))
            self.feedback(use_id=saved['use_id'], state='rejected', reason_code=code,
                          reason=f'【夹具】{code}', feedback=f'【模拟作者夹具】{code}')
            self.assertEqual(len(observations(self.home)), count)
            self.assertEqual(observations(self.home)[-1]['repair_target'], REASONS[code])
        self.assertEqual(self.source()['author_status'], 'rejected')
        gap = search('', 'theory.concession_direction', catalog=self.catalog)
        record_returned(gap, self.catalog, self.home)
        self.feedback(query_id=gap['query_id'], source_uids=[], state='rejected', reason_code='corpus_gap',
                      reason='【夹具】没有合适范本。', feedback='【模拟作者夹具】没有合适范本。')
        self.assertEqual(observations(self.home)[-1]['feedback_scope'], 'query')
        self.assertEqual(observations(self.home)[-1]['repair_target'], REASONS['corpus_gap'])

    def test_unbound_legacy_feedback_is_visible_without_guessing_a_draft(self):
        self.save()
        path = self.home / 'events/exemplar_use.jsonl'
        old = {'query_id': self.result['query_id'], 'source_uids': [self.uid], 'state': 'author_accepted',
               'actor': 'author', 'feedback': '【历史模拟夹具】接受，但未登记稿件版本。', 'ts': '2026-09-30T00:00:00+08:00'}
        with path.open('a', encoding='utf-8') as handle:
            handle.write(json.dumps(old, ensure_ascii=False) + '\n')
        before = path.read_bytes()
        source = self.source()
        self.assertEqual(source['author_status'], 'unknown')
        self.assertEqual(len(source['unbound_author_feedback']), 1)
        self.assertEqual(path.read_bytes(), before)
        self.feedback()
        self.assertTrue(path.read_bytes().startswith(before))

    def test_feedback_logging_failure_leaves_recorded_author_status_unknown(self):
        saved = self.save()
        with patch('log_exemplar.append_event', return_value=False):
            self.assertFalse(self.feedback(use_id=saved['use_id']))
        self.assertEqual(self.source()['author_status'], 'unknown')
        self.assertTrue(self.feedback(use_id=saved['use_id']))
        self.assertEqual(self.source()['author_status'], 'author_accepted')

    def test_feedback_cli_preserves_chinese_and_rejects_other_operation_states(self):
        saved = self.save()
        env = {k: v for k, v in os.environ.items() if k not in ('PYTHONIOENCODING', 'PYTHONUTF8')}
        env.update(FITNESS_HOME=str(self.home), PYTHONDONTWRITEBYTECODE='1')
        command = [sys.executable, '-B', str(ROOT / '_shared/indexing/use_exemplar.py'), 'feedback']
        data = {'query_id': self.result['query_id'], 'source_uids': [self.uid], 'use_id': saved['use_id'],
                'state': 'author_accepted', 'actor': 'author', 'feedback': '【模拟作者夹具】保留这一版。'}
        run = subprocess.run(command, input=json.dumps(data, ensure_ascii=False), cwd=ROOT, env=env,
                             capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(run.returncode, 0, run.stderr)
        output = json.loads(run.stdout)
        self.assertTrue(output['feedback_recorded'])
        self.assertEqual(observations(self.home)[-1]['feedback'], data['feedback'])
        bad = subprocess.run(command, input=json.dumps({**data, 'state': 'adopted'}), cwd=ROOT, env=env,
                             capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(bad.returncode, 1)


if __name__ == '__main__':
    unittest.main()
