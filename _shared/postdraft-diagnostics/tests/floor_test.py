# -*- coding: utf-8 -*-
"""Step 2.5 floor test: run postdraft analyzer on exemplar papers (negative control)."""
import io, sys, os, json, re, glob, subprocess, random

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
SRC_DIR = r"C:\Users\admin\.claude\skills\story-blueprints\v4\rhetoric-moves\sources"
ANALYZER = r"C:\Users\admin\.agents\skills\_shared\postdraft-diagnostics\analyze.py"

manifest = json.load(open(os.path.join(SRC_DIR, "_backfill_manifest_2026-09-20.json"), encoding="utf-8"))
entries = [e for e in manifest["entries"] if e.get("status") == "ok" and os.path.exists(e["source_md"])]

# --- selection: all house_style (gulati/westphal) + diversified field_norm fill ---
def is_house(k):
    return bool(re.search(r"gulati|westphal|uzzi|law_and_mills", k))

house = [e for e in entries if is_house(e["derived_key"])]
field = [e for e in entries if not is_house(e["derived_key"])]
random.seed(20260920)
pick_field = random.sample(field, min(24, len(field)))
sel = house + pick_field
print(f"entries ok+exists: {len(entries)}; house: {len(house)}; field sampled: {len(pick_field)}")

# --- design annotation: keyword scan over whole md (methods-heavy evidence printed) ---
DESIGN_PATTERNS = [
    ("experiment", r"\b(randomized|laboratory experiment|field experiment|we experimentally)\b"),
    ("did_natural_experiment", r"\b(difference[- ]in[- ]differences|diff[- ]in[- ]diff|event study|staggered|quasi[- ]experiment(?:al)?|natural experiment)\b"),
    ("iv_2sls", r"\b(instrumental variable|two[- ]stage least squares|2sls)\b"),
    ("survival", r"\b(cox|hazard (model|rate|ratio)|survival (analysis|model))\b"),
    ("nonlinear", r"\b(probit|logit|tobit|negative binomial)\b"),
    ("ols_fe_panel_hlm", r"\b(fixed[- ]effects|random[- ]effects|panel (data|regression)|ordinary least squares|\bOLS\b|hierarchical linear)"),
]
def annotate(md_path):
    try:
        txt = open(md_path, encoding="utf-8", errors="replace").read().lower()
    except Exception:
        return "unknown", []
    hits = []
    for fam, pat in DESIGN_PATTERNS:
        m = re.findall(pat, txt)
        if m:
            hits.append((fam, len(m), m[:3]))
    if not hits:
        return "unknown", []
    # priority order as listed; but require nontrivial evidence (>=2 mentions) for the top families
    for fam, pat in DESIGN_PATTERNS:
        for h in hits:
            if h[0] == fam and h[1] >= 2:
                return fam, hits
    return hits[0][0], hits

results = []
for e in sel:
    key = e["derived_key"]
    md = e["source_md"]
    fam, ev = annotate(md)
    r = subprocess.run([sys.executable, ANALYZER, md, "--design", fam],
                       capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    out = r.stdout or ""
    m = re.search(r"sentences:\s*(\d+) scanned", out)
    nsc = int(m.group(1)) if m else 0
    flags = re.findall(r"\[(OVERCLAIM|UNDERCLAIM|CONDITION_MISSING)\]", out)
    idm = re.search(r"identification markers found: (.+)", out)
    results.append({
        "key": key, "design": fam, "evidence": [(h[0], h[1], h[2]) for h in ev],
        "scanned": nsc, "flags": len(flags), "by_type": {t: flags.count(t) for t in set(flags)},
        "id_markers": idm.group(1).strip() if idm else "",
        "stdout": out,
    })

results.sort(key=lambda x: -(x["flags"] / max(1, x["scanned"]) * 1000))
print("\n=== FLOOR TEST RESULTS (sorted by flag density per 1000 scanned sentences) ===")
print(f"{'key':<58} {'design':<22} {'scan':>5} {'flags':>5} {'density':>7}")
for x in results:
    dens = x["flags"] / max(1, x["scanned"]) * 1000
    print(f"{x['key'][:58]:<58} {x['design']:<22} {x['scanned']:>5} {x['flags']:>5} {dens:>7.1f}")
tot_scan = sum(x["scanned"] for x in results); tot_flag = sum(x["flags"] for x in results)
print(f"\nTOTAL: {tot_scan} scanned, {tot_flag} flags, overall density {tot_flag/max(1,tot_scan)*1000:.1f}/1000")

import pathlib as _pl
_wl = json.load(open(_pl.Path(__file__).parent.parent / "wordlists-v1.json", encoding="utf-8"))
out_path = _pl.Path(__file__).parent / f"floor_test_{_wl.get('version', 'x')}_results.json"
json.dump(results, open(out_path, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("\nsaved: C:\\Users\\admin\\AppData\\Local\\Temp\\floor_test_results.json")
