"""Bind maintainer judgements to a concrete candidate snapshot and export them."""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--benchmark', required=True, type=Path)
    ap.add_argument('--out-dir', required=True, type=Path)
    args = ap.parse_args()
    b = json.loads(args.benchmark.read_text(encoding='utf-8'))
    review = json.loads(Path(__file__).with_name('review-decisions.json').read_text(encoding='utf-8'))
    if review.get('cases_sha256') != b['cases_sha256'] or review.get('dependency_hashes') != b['dependency_hashes']:
        raise ValueError('review is stale for these requests/retrieval/corpus versions; review again before export')
    decisions = {d['id']: d for d in review['decisions']}
    if set(decisions) != {r['case']['id'] for r in b['records']}:
        raise ValueError('review case IDs differ from benchmark')
    lines = ['# 40 场景范本检索复核', '', review['reviewer'], '',
             '场景来自现有写作功能、审计反例及一个真实项目记录的扩展。它们是构造的代表性需求，不是作者已经逐题验收的40项真实请求。检索曾按本组场景调过参数；这里是开发期复核，不宣称独立泛化准确率。', '',
             'usable：当前动作有可学习的卡片原文与模板，不表示书目/PDF身份已确认；conditional：仅部分动作/模板可借，仍有条件；gap：缺满足需求的顶刊原文；expected_no_fit：负例正确拒配。原文档案定位状态单列。作者采用、实际浏览次数和改编后接受尚未测得。', '',
             '| 场景 | 写作需求 | 判断 | 复核选择的候选位置 | 理由与改编限制 |',
             '|---|---|---|---|---|']
    bound, counts, rank_counts = [], Counter(), Counter()
    for r in b['records']:
        d = dict(decisions[r['case']['id']])
        cs = r['result']['candidates']
        chosen = cs[d['rank']-1] if d.get('rank') else None
        actual_uids = sorted(x['uid'] for x in chosen['originals'] + chosen['templates']) if chosen else []
        if actual_uids != sorted(d.get('selected_source_uids', [])):
            raise ValueError(f"reviewed UIDs changed for {d['id']}; review again, do not reuse the old rank")
        d.update({'need':r['case']['need'], 'query':r['case']['query'], 'function':r['case']['function'],
                  'selected_parent_paragraph': chosen['parent_paragraph'] if chosen else None,
                  'selected_source_uids': [x['uid'] for x in (chosen['originals']+chosen['templates'])] if chosen else [],
                  'selected_source_file': chosen['source_file'] if chosen else None,
                  'selected_archive_context_states': dict(Counter(x['source_context']['state'] for x in chosen['originals'])) if chosen else {},
                  'selected_title':chosen['block_title'] if chosen else None, 'author_acceptance':None,
                  'actual_candidates_opened_by_author':None, 'actual_adoption':None})
        bound.append(d)
        counts[d['verdict']]+=1
        if d.get('rank'):
            rank_counts[d['rank']]+=1
        lines.append(f"| {d['id']} | {d['need']} | {d['verdict']} | {d.get('rank') or '—'} | {d['reason']} |")
    lines += ['', '## 已测得的范围', '',
              f'判断计数：{dict(counts)}。这些是实施者的场景判断，不是作者接受率。选择位置：{dict(rank_counts)}；位置不等于实际阅读量。',
              f"首项会误导盲目改编的场景：{[d['id'] for d in bound if d.get('first_misleading')]}。这些场景需要比较候选和约束，不能自动取第一项。", '',
              '结构、来源局部性、耗时的测量：', '',
              '```json', json.dumps(b['summary'],ensure_ascii=False,indent=2),'```','',
              '冷启动含依赖校验与模块加载；同一次 Python 进程/批量查询的耗时才能使用 warm 指标。一次 CLI 查询不会自动获得 warm 延迟。卡片内逐字命中不证明与 PDF 全文一致，也不证明范文适配。', '',
              '## 可审查的改编底本', '',
              '下面只展示所选源块已有模板（保留占位符），并列出应如何改编的限制。它们不是已填入用户事实的最终稿，未计入真实使用台账；作者接受仍为空。']
    by_id = {r['case']['id']:r for r in b['records']}
    for case_id in ('I02','I09','T01','T05','M04','M07','R04','R05','R06','R09'):
        d = next(x for x in bound if x['id']==case_id)
        c = by_id[case_id]['result']['candidates'][d['rank']-1]
        lines.extend(['', f"### {case_id} · {d['need']}", '', d['reason'], '',
                      f"源块：[{c['block_title']}]({(ROOT/c['source_file']).as_posix()}:{c['source_line']})。"])
        if c['originals']:
            original=c['originals'][0]
            lines.extend(['', f"来源键：`{original['citekey']}`；核验级别：`{original['provenance_level']}`；状态：`{original['status']}`。"])
            sc=original['source_context']
            lines.extend(['', f"本地原文档案状态：`{sc['state']}`。这不等于PDF或书目身份已核验。"])
            if sc.get('paragraphs'):
                p=sc['paragraphs'][0]
                lines.extend(['', f"档案原文：[第{p['paragraph_number']}段 · {p['source_section']}]({(ROOT/p['source_file']).as_posix()}:{p['source_line']})。"])
        if c['templates']:
            template=c['templates'][0]
            lines.extend(['', f"模板 UID：`{template['uid']}`。", '', '```text', template['text'], '```'])
    data = {'reviewer':review['reviewer'],'benchmark_dependency_hashes':b['dependency_hashes'],
            'cases_sha256':b['cases_sha256'],'counts':dict(counts),'decisions':bound,
            'author_acceptance_measured':False,'independent_blind_evaluation':False}
    args.out_dir.mkdir(parents=True,exist_ok=True)
    (args.out_dir/'review-results.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    (args.out_dir/'40场景检索复核.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'judgements':dict(counts),'first_misleading':sum(bool(d.get('first_misleading')) for d in bound)},ensure_ascii=False))
    return 0


if __name__=='__main__':
    raise SystemExit(main())
