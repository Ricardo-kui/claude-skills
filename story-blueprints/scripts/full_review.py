# -*- coding: utf-8 -*-
"""全量复核：输出每份 blueprint 的完整 climax 文本 + primary + fa_len。"""
import glob, os, re
d = r'C:\Users\40500\.claude\skills\story-blueprints\blueprints'
for p in sorted(glob.glob(os.path.join(d, '*.md'))):
    if p.endswith('_index.md'):
        continue
    t = open(p, encoding='utf-8').read()
    blocks = re.findall(r'```yaml\n(.*?)```', t, re.S)
    lines = []
    for b in blocks:
        lines.extend(b.splitlines())
    def fld(key, ind):
        pat = re.compile(r'^ {' + str(ind) + r'}' + re.escape(key) + r':\s*(.*)$')
        for ln in lines:
            m = pat.match(ln)
            if m:
                v = m.group(1).strip()
                return v[1:].strip() if v.startswith('-') else v
        return ''
    def falen(key, ind):
        pat = re.compile(r'^ {' + str(ind) + r'}' + re.escape(key) + r':\s*$')
        dash = re.compile(r'^ {' + str(ind+2) + r'}- ')
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
    prim = fld('primary_type', 2)
    climax = re.sub(r'\s+', ' ', fld('climax', 2)).strip()
    fa = falen('falling_action', 2)
    print(f"{os.path.basename(p)[:45]:<46} | {prim:<22} | fa={fa} | {climax}")
