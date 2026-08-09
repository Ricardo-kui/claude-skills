# -*- coding: utf-8 -*-
"""提取 59 份 blueprint 的布局字段，输出紧凑汇总表。
用法: python extract_layout.py <blueprints_dir> [out.csv]
字段: id | primary_type | compound | resolution | climax(截断) | fa_len | tied_at(截断) | pacing(截断)
"""
import glob, os, re, sys, csv

def parse_field(lines, key, indent=2):
    """返回 key 的标量值或首行；处理 '- ' 数组首元素。"""
    pat = re.compile(r'^ {' + str(indent) + r'}' + re.escape(key) + r':\s*(.*)$')
    for i, ln in enumerate(lines):
        m = pat.match(ln)
        if m:
            val = m.group(1).strip()
            if val.startswith('-'):
                return val[1:].strip()
            return val
    return ''

def count_array(lines, key, indent=2):
    """统计 key 下缩进数组的项数。"""
    pat = re.compile(r'^ {' + str(indent) + r'}' + re.escape(key) + r':\s*$')
    dash = re.compile(r'^ {' + str(indent+2) + r'}- ')
    for i, ln in enumerate(lines):
        if pat.match(ln):
            n = 0
            for j in range(i+1, min(i+12, len(lines))):
                if dash.match(lines[j]):
                    n += 1
                elif lines[j].strip() and not lines[j].startswith(' '):
                    break
            return n
    return 0

def clean(s):
    s = s.strip().strip('"').strip("'")
    s = re.sub(r'\s+', ' ', s)
    return s

def extract(md_path):
    with open(md_path, encoding='utf-8') as f:
        text = f.read()
    # 所有 YAML 围栏块（文件头 + knot + characters + five_acts + ...）
    blocks = re.findall(r'```yaml\n(.*?)```', text, re.S)
    lines = []
    for b in blocks:
        lines.extend(b.splitlines())
    # resolution_logic 可能不带围栏（### 标题下直接正文）
    m_rl = re.search(r'^resolution_logic[：:]\s*(.+)$', text, re.M)
    prim = parse_field(lines, 'primary_type', 2) or parse_field(lines, 'primary_type', 0)
    comp = parse_field(lines, 'compound_types', 2)
    tied = parse_field(lines, 'tied_at', 2)
    untied = parse_field(lines, 'untied_at', 2)
    reso = parse_field(lines, 'resolution_logic', 0) or parse_field(lines, 'resolution_logic', 2)
    if (not reso) and m_rl:
        reso = clean(m_rl.group(1)).split('：')[0]
    if not reso:  # ### resolution_logic 标题 + 正文（`word` 代码格式）
        m_h = re.search(r'^### resolution_logic\s*\n+`([a-z-]+)`', text, re.M)
        if m_h:
            reso = m_h.group(1)
    climax = parse_field(lines, 'climax', 2)
    fa_len = count_array(lines, 'falling_action', 2)
    pacing = parse_field(lines, 'pacing_notes', 4) or parse_field(lines, 'pacing_notes', 2)
    return {
        'id': os.path.basename(md_path).replace('.md', ''),
        'primary': clean(prim.split('#')[0]),
        'compound': clean(comp),
        'resolution': clean(reso.split('（')[0] if reso else ''),
        'climax': clean(climax)[:90],
        'fa_len': fa_len,
        'tied': clean(tied)[:60],
        'pacing': clean(pacing)[:60],
    }

def main():
    d = sys.argv[1] if len(sys.argv) > 1 else '.'
    out = sys.argv[2] if len(sys.argv) > 2 else 'layout_extract.csv'
    rows = []
    for p in sorted(glob.glob(os.path.join(d, '*.md'))):
        if os.path.basename(p) == '_index.md':
            continue
        rows.append(extract(p))
    with open(out, 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id', 'primary', 'compound', 'resolution', 'climax', 'fa_len', 'tied', 'pacing'])
        for r in rows:
            w.writerow([r['id'], r['primary'], r['compound'], r['resolution'], r['climax'], r['fa_len'], r['tied'], r['pacing']])
    # 汇总: 每类样本数 / 缺失
    from collections import Counter, defaultdict
    cnt = Counter(r['primary'] for r in rows)
    missing = [r['id'] for r in rows if not r['primary'] or not r['climax'] or r['fa_len'] == 0]
    fa_stats = defaultdict(list)
    for r in rows:
        fa_stats[r['primary']].append(r['fa_len'])
    print(f"总份数: {len(rows)}")
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        fvals = fa_stats[k]
        mid = sorted(fvals)[len(fvals)//2]
        print(f"  {k}: {v} 份 | falling_action 项数 范围{min(fvals)}-{max(fvals)} 中位{mid}")
    print(f"缺失/解析失败: {missing if missing else '无'}")

if __name__ == '__main__':
    main()
