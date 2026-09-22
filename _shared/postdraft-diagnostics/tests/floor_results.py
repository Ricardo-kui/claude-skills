# -*- coding: utf-8 -*-
"""Results-dedicated floor test: all archives, Results-bucket flags only."""
import json, re, subprocess, sys, io, collections, random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

MANIFEST = r"C:\Users\admin\.claude\skills\story-blueprints\v4\rhetoric-moves\sources\_backfill_manifest_2026-09-20.json"
ANALYZE = r"C:\Users\admin\.agents\skills\_shared\postdraft-diagnostics\analyze.py"

DESIGN_PATTERNS = [
    ("experiment", r"\brandom(ized|ly| assignment| assignment check)|\bexperiment(al)? (design|condition|group|manipulation)|\btreatment group\b"),
    ("did_natural_experiment", r"\bdifference[- ]in[- ]difference|\bdid design|\bevent study|\bstaggered\b|\bpre[- ]?trend"),
    ("iv_2sls", r"\binstrumental variable|\b2sls\b|\bfirst[- ]stage|\bexogenous (shock|variation)|\bf[- ]statistic|\bexclusion restriction"),
    ("survival", r"\bhazard (rate|model|ratio)|\bcloglog\b|\bcox\b|\bsurvival (analysis|curve|function)|\bweibull\b"),
    ("nonlinear", r"\binverted[- ]u|\bu[- ]shaped|\bcurvilinear|\bquadratic term|\binflection point|\bspline"),
    ("ols_fe_panel_hlm", r"\bfixed effects?\b|\bpanel data\b|\bclustered standard errors?\b|\bhierarchical linear"),
]

def annotate_design(text):
    hits = []
    for name, pat in DESIGN_PATTERNS:
        n = len(re.findall(pat, text, re.I))
        if n:
            hits.append((n, name))
    if not hits:
        return "unknown", []
    hits.sort(reverse=True)
    return hits[0][1], hits

def main():
    man = json.load(open(MANIFEST, encoding='utf-8'))
    import os
    for e in man['entries']:
        if e.get('status') == 'ok':
            e['path'] = e['source_md']
            e['exists'] = os.path.exists(e['path'])
    entries = [e for e in man['entries'] if e.get('exists')
               and (e.get('sections') or {}).get('results', 0) >= 5]
    out = []
    total_sent = 0
    for e in entries:
        p = e['path']
        try:
            text = open(p, encoding='utf-8').read()
        except OSError:
            continue
        design, ev = annotate_design(text)
        r = subprocess.run([sys.executable, ANALYZE, p, '--design', design, '--json'],
                           capture_output=True, text=True, encoding='utf-8', timeout=120)
        try:
            rep = json.loads(r.stdout)
        except json.JSONDecodeError:
            print('PARSE FAIL', e['derived_key'][:40], r.stdout[:100], r.stderr[:100]); continue
        rflags = [f for f in rep['flags'] if f['section'] == 'results']
        # results-bucket sentence count from stats
        sec_counts = {}
        for m in re.finditer(r"(results|methods|discussion):\s*(\d+)", r.stdout):
            pass
        nres = rep['sections_scanned'].get('results', 0)
        total_sent += nres
        out.append({'key': e['derived_key'], 'design': design, 'design_evidence': ev[:3],
                    'results_sentences': nres, 'flags': rflags,
                    'all_flag_count': rep['flag_count']})
    tc = collections.Counter(f['type'] for o in out for f in o['flags'])
    tot = sum(len(o['flags']) for o in out)
    print(f"papers={len(out)}  results_sentences={total_sent}  results_flags={tot}  "
          f"density={1000*tot/max(total_sent,1):.1f}/1000  types={dict(tc)}")
    per = sorted(out, key=lambda o: -len(o['flags']))
    for o in per[:12]:
        if o['flags']:
            print(f"  {o['key'][:44]:46s} {o['design'][:18]:19s} {len(o['flags'])} flags")
    import pathlib as _pl
    _wl = json.load(open(_pl.Path(ANALYZE).parent / "wordlists-v1.json", encoding="utf-8"))
    out_path = _pl.Path(__file__).parent / f"floor_results_{_wl.get('version', 'x')}_results.json"
    json.dump(out, open(out_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    print('saved results json')

if __name__ == '__main__':
    main()
