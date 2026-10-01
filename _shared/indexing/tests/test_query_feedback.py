"""Fine-move regressions and query-bound factual feedback; isolated ledgers only."""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / '_shared/indexing'))
from retrieve import load_catalog, search, function_specs
from log_exemplar import observations, record_observation, record_returned
from fitness_report import sec_exemplar_use


class QueryFeedbackTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = load_catalog()
        cls.cases = json.loads((ROOT / '_governance/exemplar-retrieval/cases.json').read_text(encoding='utf-8'))['cases']

    def query(self, case_id):
        q = next(q for q in self.cases if q['id'] == case_id)
        return search(q['query'], q['function'], need=q['need'], catalog=self.catalog)

    def test_seven_misleading_first_results_are_corrected_or_an_explicit_gap(self):
        expected = {'I05': '注意力重定向', 'T01': '两构念四维', 'T02': 'Dual-Channel Convergence',
                    'T06': '分离编号回指竞争对', 'R06': '诚实声明'}
        for case_id, title in expected.items():
            with self.subTest(case=case_id):
                result = self.query(case_id)
                self.assertIn(title, result['candidates'][0]['block_title'])
                self.assertEqual(result['candidates'][0]['function_match_basis'], 'authored_metadata')
                self.assertTrue(result['candidates'][0]['originals'])
        # The expanded pool now has an article excerpt covering both sides.
        # Do not require an older template-only card to stay first forever.
        balance = self.query('T09')['candidates'][0]
        self.assertEqual(balance['function_match_basis'], 'authored_metadata')
        self.assertTrue(balance['originals'])
        self.assertTrue(any('cost' in r['text'].lower() and 'benefit' in r['text'].lower()
                            for r in balance['originals']))
        concession = self.query('T07')
        self.assertEqual(concession['function'], 'theory.concession_direction')
        self.assertTrue(concession['candidates'])
        self.assertTrue(all(c['function_match_basis'] == 'authored_metadata'
                            and c['originals'] for c in concession['candidates']))

    def test_template_only_balance_fixture_keeps_missing_original_explicit(self):
        definition = next(d for d in self.catalog['function_definitions']
                          if d['id'] == 'theory.cost_benefit_balance')
        rows = [copy.deepcopy(r) for r in self.catalog['entries']
                if r['parent_paragraph'] == definition['source']['parent_paragraph']]
        result = search('', definition['id'], catalog={**self.catalog, 'entries': rows})
        candidate = result['candidates'][0]
        self.assertFalse(candidate['originals'])
        self.assertEqual(candidate['adaptation_card']['original']['state'], 'missing')
        self.assertTrue(candidate['limitations'])

    def test_query_ids_are_distinct_and_versions_reproducible(self):
        a, b = self.query('I05'), self.query('I05')
        self.assertNotEqual(a['query_id'], b['query_id'])
        self.assertEqual(a['retrieval_version'], b['retrieval_version'])
        self.assertEqual(a['request'], b['request'])

    def test_existing_design_and_navigation_cases_do_not_regress(self):
        for cid, title in [('M08', '二元 rare outcome'), ('R02', '模型序列'),
                           ('R04', 'Chow'), ('R07', '混合证据'), ('R10', '管道衰减')]:
            with self.subTest(case=cid):
                self.assertIn(title, self.query(cid)['candidates'][0]['block_title'])

    def test_usage_ledger_cannot_pollute_skills_directory(self):
        with self.assertRaises(ValueError):
            record_returned(self.query('I05'), self.catalog, ROOT / '_shared')

    def test_authored_function_beats_many_content_hits(self):
        result = self.query('T01')
        wanted = result['candidates'][0]['originals'][0]['uid']
        correct = copy.deepcopy(next(r for r in self.catalog['entries'] if r['uid'] == wanted))
        wrong = copy.deepcopy(next(r for r in self.catalog['entries'] if 'Framework-Anchored 双构念区分' in r['block_title']))
        wrong['text'] += ' ' + ' '.join(f'topic{i}' for i in range(30))
        data = {**self.catalog, 'entries': [correct, wrong]}
        q = ' '.join(f'topic{i}' for i in range(30))
        actual = search(q, 'theory.construct_contrast', catalog=data)
        self.assertEqual(actual['candidates'][0]['originals'][0]['uid'], wanted)

    def test_concession_requires_original_response_in_same_block(self):
        row = copy.deepcopy(next(r for r in self.catalog['entries'] if '双刃限定' in r['block_title'] and r['kind'] == 'verbatim'))
        data = {**self.catalog, 'entries': [row]}
        self.assertFalse(search('', 'theory.concession_direction', catalog=data)['candidates'])
        row['text'] = 'Although action can carry risk, we expect a positive outcome because the focal condition mitigates this risk.'
        self.assertTrue(search('', 'theory.concession_direction', catalog=data)['candidates'])

    def test_all_authored_labels_are_registered_and_have_position(self):
        known = {s['id'] for s in function_specs()}
        for r in self.catalog['entries']:
            meta = r.get('retrieval_move', {})
            if meta:
                self.assertTrue(set(meta['functions']).issubset(known), r['source_file'])
                self.assertTrue(all(meta.get(k) for k in ('position', 'prerequisite', 'next')))

    def test_feedback_join_reason_and_idempotent_replay(self):
        result = self.query('I05')
        uid = result['candidates'][0]['originals'][0]['uid']
        with tempfile.TemporaryDirectory() as home:
            self.assertTrue(record_returned(result, self.catalog, home))
            self.assertTrue(record_returned(result, self.catalog, home))
            event = {'query_id': result['query_id'], 'state': 'rejected', 'actor': 'agent',
                     'source_uids': [uid], 'reason_code': 'condition_mismatch',
                     'reason': '当前研究没有释放旧注意力需求的制度冲击。'}
            record_observation(event, self.catalog, home)
            record_observation(event, self.catalog, home)
            events = observations(home)
            self.assertEqual(len(events), 2)
            self.assertEqual(events[-1]['selected_ranks'], [1])
            self.assertEqual(events[-1]['retrieval_version'], result['retrieval_version'])
            self.assertIn('设计', events[-1]['repair_target'])
            self.assertNotIn('originals', events[0]['candidates'][0])

    def test_feedback_rejects_unreturned_uid_and_missing_query_or_reason(self):
        result = self.query('I05')
        returned = {r['uid'] for c in result['candidates'] + result.get('supplementary_candidates', [])
                    for r in c['originals'] + c['templates']}
        outside = next(r['uid'] for r in self.catalog['entries'] if r['uid'] not in returned)
        base = {'query_id': result['query_id'], 'state': 'opened', 'actor': 'agent', 'source_uids': [outside]}
        with tempfile.TemporaryDirectory() as home:
            with self.assertRaises(ValueError):
                record_observation(base, self.catalog, home)
            record_returned(result, self.catalog, home)
            for bad in [base, {**base, 'query_id': ''},
                        {**base, 'state': 'rejected', 'reason': '不适合'},
                        {**base, 'state': 'rejected', 'reason_code': 'invented', 'reason': '不适合'}]:
                with self.assertRaises(ValueError):
                    record_observation(bad, self.catalog, home)

    def test_same_query_id_cannot_bind_changed_request(self):
        result = self.query('I05')
        changed = copy.deepcopy(result)
        changed['request']['need'] = '另一个写作动作'
        with tempfile.TemporaryDirectory() as home:
            record_returned(result, self.catalog, home)
            with self.assertRaises(ValueError):
                record_returned(changed, self.catalog, home)

    def test_adoption_is_not_author_acceptance_and_quote_is_required(self):
        result = self.query('I05')
        base = {'query_id': result['query_id'], 'source_uids': [result['candidates'][0]['originals'][0]['uid']]}
        with tempfile.TemporaryDirectory() as home:
            record_returned(result, self.catalog, home)
            record_observation({**base, 'state': 'adopted', 'actor': 'agent'}, self.catalog, home)
            for bad in [{'actor': 'agent', 'feedback': '作者认可'}, {'actor': 'author'}]:
                with self.assertRaises(ValueError):
                    record_observation({**base, 'state': 'author_accepted', **bad}, self.catalog, home)
            out = []
            sec_exemplar_use(observations(home), out)
            self.assertIn('作者评价记录：1', '\n'.join(out))
            self.assertFalse(any(e['state'] == 'author_accepted' for e in observations(home)))
            # Synthetic author feedback is confined to this temporary test ledger.
            record_observation({**base, 'state': 'author_accepted', 'actor': 'author',
                                'feedback': '测试夹具中的明确作者评价'}, self.catalog, home)

    def test_no_fit_query_can_record_a_corpus_gap_without_fake_uid(self):
        result = self.query('T07')
        with tempfile.TemporaryDirectory() as home:
            record_returned(result, self.catalog, home)
            record_observation({'query_id': result['query_id'], 'state': 'rejected', 'actor': 'agent',
                                'source_uids': [], 'reason_code': 'corpus_gap',
                                'reason': '没有同块完成方向让步与回应的文章原文。'}, self.catalog, home)
            self.assertEqual(observations(home)[-1]['selected_ranks'], [])

    def test_cli_registers_batch_ids_and_feedback_in_isolated_home(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            queries = root / 'queries.json'
            queries.write_text(json.dumps([q for q in self.cases if q['id'] in ('I05', 'T07')], ensure_ascii=False), encoding='utf-8')
            env = {**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONDONTWRITEBYTECODE': '1',
                   'FITNESS_HOME': str(root / 'ledger')}
            cmd = [sys.executable, '-B', '_shared/indexing/retrieve.py', '--batch', str(queries)]
            preview = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertFalse(observations(root / 'ledger'))
            live = subprocess.run(cmd + ['--record-use', '--project', 'isolated-test'], cwd=ROOT,
                                  env=env, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(live.returncode, 0, live.stderr)
            results = json.loads(live.stdout)['results']
            self.assertEqual(len({r['result']['query_id'] for r in results}), 2)
            self.assertEqual(len(observations(root / 'ledger')), 2)
            first = results[0]['result']
            event = {'query_id': first['query_id'], 'state': 'opened', 'actor': 'agent',
                     'source_uids': [first['candidates'][0]['originals'][0]['uid']]}
            logged = subprocess.run([sys.executable, '-B', '_shared/indexing/log_exemplar.py'],
                                    input=json.dumps(event), cwd=ROOT, env=env,
                                    capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(logged.returncode, 0, logged.stderr)
            self.assertEqual(len(observations(root / 'ledger')), 3)


if __name__ == '__main__':
    unittest.main()
