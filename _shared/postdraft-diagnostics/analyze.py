#!/usr/bin/env python3
"""Post-draft claim–design mismatch diagnostics (SHADOW MODE).

Implements metric-contract.md v1.0.0: flags causal-language strength that
exceeds (or under-uses) what the declared design supports.

This is a diagnostic observer, NOT a gate:
- exit code is always 0 on a completed scan (1 only on usage/IO errors);
- no composite score, no pass/fail verdict, no rewriting, no writeback.

Usage:
  python analyze.py draft.md --design did_natural_experiment [--json]
  python analyze.py draft.md --design unknown     # reports design-unannotated

Sentence splitting mirrors distill-paper-exemplar/scripts/preprocess_l0.py
(2026-09-20 fixed splitter: abbreviation protection, min_chars=0).
"""

from __future__ import annotations

import argparse
import io
import json
import re
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

HERE = Path(__file__).resolve().parent
WORDLISTS = HERE / "wordlists-v1.json"

# --- sentence splitter (mirror of preprocess_l0.py, 2026-09-20 fix) ---
ABBREV_PERIODS = re.compile(
    r"\b(U\.S|U\.K|e\.g|i\.e|vs|etc|et al|Fig|Inc|Ltd|Dr|Prof|Jr|Mr|Ms|St|Vol|No|pp|p|ed|eds)\.(?=\s)"
)
SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(])")
PDOT = "\ue000"

# --- section heading classification ---
SECTION_PATTERNS = [
    ("results", re.compile(r"^#{1,4}\s*(?:(?:\d+|[IVXLC]+)[\.\d]*\s*)?(results|findings|empirical (?:results|analysis|findings)|main (?:results|analysis)|(?:empirical|econometric|regression|main|further|additional|subsample|survival|descriptive|hypothesis) analysis|estimation results|robustness|supplementary analyses|additional (?:analyses|tests)|descriptive statistics|hypotheses tests)\b", re.I)),
    ("methods", re.compile(r"^#{1,4}\s*(?:(?:\d+|[IVXLC]+)[\.\d]*\s*)?(methods?|methodology|data and (?:sample|measures|method)|sample|variables|measures|empirical (?:strategy|setting|approach|framework)|research design|econometric|identification|model (?:specification|estimation)|estimation (?:strategy|approach))\b", re.I)),
    ("discussion", re.compile(r"^#{1,4}\s*(?:(?:\d+|[IVXLC]+)[\.\d]*\s*)?(discussion|conclusion|concluding remarks|implications|general discussion)\b", re.I)),
    ("references", re.compile(r"^#{1,4}\s*(?:(?:\d+|[IVXLC]+)[\.\d]*\s*)?(references|bibliography|works cited|appendix)\b", re.I)),
]
SCANNED = ("results", "methods", "discussion")

# statistical-result markers: sentence is reporting an estimated result
RESULT_MARKERS = re.compile(
    r"(\bcoefficient\b|\bp[\s-]?value|\bβ\b|\bbeta\b|\bstandard error|\bconfidence interval|\bCI\b"
    r"|\bmodel\s+\d|\bcolumn\s*\d|\btable\s*\d|\bfigure\s*\d|\bsignificant|\bmarginally\b"
    r"|\bp\s*[<=]\s*0?\.?\d|\bpositive(ly)?\s+(?:and\s+)?significant|\bstatistically|\bwe\s+find|\bwe\s+observe|\bH\d"
    r"|\b(?:the\s+)?(?:results?|findings?)\s+(?:[\w-]+\s+){0,1}(?:shows?|indicates?|suggests?|reveals?|demonstrates?|supports?|provides?)"
    r"|\bwe\s+(?:found|observe[d]?)\b|\bstandard deviation\b|\bthis (?:indicates|suggests) that\b)"
)
STAT_HARD = re.compile(
    r"(\bcoefficient\b|\bp[\s-]?value|β|\btable\s*\d|\bmodel\s+\d|\bcolumn\s*\d|\bsignificant|\bp\s*[<=]\s*0?\.?\d|\bstandard deviations?\b)"
)
NEGATION_BEFORE_TIER = re.compile(r"\b(no|not|does not|did not|fail(?:ed|ing)? to|without)\s+(?:\w+\s+){0,2}$")

# --- v1.1 suppressions (floor-test adjudicated 2026-09-20, exemplar-backed) ---
STAT_SUBJ = r"(?:analys[ie]s|results?|findings?|evidence|tests?|data|estimation|regressions?|models?|coefficients?|study|research|estimates?|interactions|interviews|informants|respondents|conversations|discussions?|commentary|debate|table\s*\d+|table\s+[a-z]\d+|columns?|panels?\b|figures?|they)"
SUPPRESS_STAT_SUBJECT = re.compile(
    rf"\b{STAT_SUBJ}\b\s*[\])]*\s*(\([^)]*\))?\s+(?:[\w()\[\].,^#-]+\s+){{0,9}}(reveal|show|demonstrate|document|indicate|produce|cause|affect|drive)s?\b")
SUPPRESS_WHICH_REVEAL = re.compile(r"\bwhich reveals?\b", re.I)
SUPPRESS_RESULT_OBJECT = re.compile(
    r"\b(drives?|driven)\b[^.]{0,25}\bthe results?\b")
SUPPRESS_PRODUCE_OBJECT = re.compile(
    r"\b(produce|produces)\b[^.!?]{0,50}\b(coefficients?|scores?|estimates?|attenuated|consistent|misleading|biased|spurious|inflated|standard errors?|robust|similar results?|comparable results?|similar estimates?|nearly identical)\b")
PROCEDURAL_LED_TO = re.compile(
    r"\bled to\b[^;]{0,40}\b(inclusion|sample|selection|response|design|research stream|literature|overlap|agreement|attrition|constructs?|establishment of|parameter|estimat)\b")
NONSIGNIFICANT = re.compile(
    r"\b(not statistically significant|not significant|statistically insignificant|insignificant|nonsignificant|non[- ]significant|marginally significant|borderline)\b", re.I)
LIT_REVIEW = re.compile(
    r"\b(literature has (provided|shown|documented)|prior (research|studies|work) (has|have) (shown|found|documented|argued)"
    r"|studies have (shown|found|documented|argued)|papers have (argued|found|shown)"
    r"|existing studies|prior studies|previous (research|studies|work)|consistent with (the )?(findings|results) of)\b")
NOT_CONSISTENT_VIEW = re.compile(
    r"not consistent with (the )?(view|notion|idea|argument|prediction|possibility|explanation) that", re.I)
PROC_METHODS = re.compile(
    r"\b(response bias|common method|measurement error|selection (bias|concern)|sample attrition|social desirability"
    r"|reduc\w+[^.]{0,30}(dimensionality|dimension|network))\b", re.I)
STAT_ATTACHED = re.compile(
    r"\b(?:caused?|led to)\b[^;]{0,50}\b\d+(?:\.\d+)?\s*(?:%|percent)")
STAT_ATTACHED_DIR = re.compile(
    r"\b(?:raises?|increases?|reduces?|decreases?|falls?|rises?)\b[^;]{0,60}"
    r"\b\d+(?:\.\d+)?\s*(?:%|percent(?:age points?)?|trillion|billion|million|\$)|\b\w*fold\b", re.I)
MODEL_SIM = re.compile(
    r"\b(simulat\w+|equilibrium|under (?:standard )?cournot|model (?:predicts?|implies|generates?)"
    r"|assum\w+|counterfactual (?:scenario|experiment|shares)|we (?:solve|calibrate|augment) the model"
    r"|first[- ]order condition|comparative statics|predicted by our model|by our model"
    r"|in the aggregate|reallocation)\b", re.I)
DESCRIPTIVE_STATS = re.compile(
    r"\b(in (?:our|the) sample|as measured by|measured using|descriptive statistics?|average value of)\b", re.I)
PRODUCE_GOODS = re.compile(
    r"\bproduc(?:e|es|ing)\b(?:\s+[\w-]+){0,3}\s+(one|two|\d+|more|fewer|less|products?|goods?|output|units?|segments?|classifications?|categories?|types)\b", re.I)
TABLE_NOTE = re.compile(r"\*?Notes?\.?\*?:?\s|^\s*-?\s*\d*\s*Notes?\.\s", re.I)
HEDGE_BEFORE = re.compile(
    r"\b(suggests?|suggesting|indicates?|indicating|appears? to|seems? to|consistent with|plausibly|arguably)\b(?:\s+[\w()\[\],-]+){0,8}\s*$")
LIMITATION_FUTURE = re.compile(
    r"\b(further research|future research|still open|open question|remains? unclear|needs? to be (?:examined|explored)"
    r"|we do recognize|we acknowledge|caveat)\b", re.I)
PROC_SAMPLE = re.compile(
    r"\b(?:reduces?|decreases?|limits?)\b[^.]{0,30}\b(data\s?set|observations?|sample)\b", re.I)
PUZZLE_OR_STRUCTURAL = re.compile(
    r"\b(puzzling|surprising|counterintuitive|unexpected|reciprocal|reverse causal|simultaneit\w*|endogene\w*"
    r"|speculation|conjecture)\b", re.I)
THEORY_MODE = re.compile(r"\b(should|can|would|may|might|could|we argue|we posit|we propose|our argument)\b")
RIVAL_EXPL = re.compile(
    r"\b(alleviate the concern|address the concern|rule out|competing explanation|rival explanation"
    r"|to account for (?:our|the) (?:findings|results|main findings)"
    r"|(?:one|a|the) (?:candidate |possible |plausible |likely )?explanation (?:for|is that))\b", re.I)
APPENDIX_REF = re.compile(r"\bappendix\b", re.I)
GIVEN_PREMISE = re.compile(r"^\s*given\b", re.I)
ROBUST_TO = re.compile(r"\brobust to\b", re.I)
CONSTRUCT_DEF = re.compile(r"\b(?:captures?|is defined as|refers to|encompasses?|constitutes?)\b", re.I)
EXAMINE_WHETHER = re.compile(r"^\s*to (?:examine|test|investigate|assess|explore) (?:whether|if)\b", re.I)
INF_INIT = "to "
QUOTE_OPEN = ('"', '“', '”')
MECH_SEARCH = re.compile(r"\bmechanisms? that may explain\b|\bto determine (?:possible )?mechanisms\b", re.I)
NOUN_SUBJECT = re.compile(
    r"^\s*(?:however|moreover|further|furthermore|in contrast|by contrast|that is|thus|therefore|hence|indeed|in turn|second|third|first|next|finally|specifically|in particular)?[,.\s]*"
    r"(?:the|a|an|this|that|its|their)\s+(?:(?:sharply|steeper|steeply|relative|continuing|overall|subsequent|\w+ly|\w+-reducing|\w+-enhancing)\s+){0,3}"
    r"(?:increase|decrease|rise|fall|reduction|decline|growth)\b", re.I)
WE_REASON = re.compile(r"\bwe reason that\b", re.I)
HEDGE_WITH_STATS = re.compile(
    r"\b(?:appears? to|seems? to)\b[^.]{0,80}?\((?:β|p\b|b\s*=|β\s*=)", re.I)
ACCORDANCE_WITH = re.compile(r"\bin accordance with\b", re.I)
MODAL_BEFORE_VERB = re.compile(
    r"\b(may|might|could|can|would|should|will|unlikely|likely|tends?|prone|possibility)\b(?:\s+\w+){0,7}\s*$")
IF_GUARD = re.compile(r"(?:even\s+)?\bif\b(?:\s+\w+){0,7}\s*$")
HEDGE_FAMILY = re.compile(r"\b(suggests?|suggesting|indicat(?:es?|ion|ing)|seems?|appears?|possible that)\b")
ECON_DIAGNOSTIC = re.compile(r"(multicollinear\w*|variance inflation|\bVIF\b|endogene\w+|autocorrelat\w*|heteroskedast\w*|mis[- ]?specif\w*)")
SLOPE_CHANGE = re.compile(
    r"\b(?:the\s+)?(?:negative|positive|\w+-reducing|\w+-enhancing)\s+effect\s+of\b.{0,100}?\b(increases?|decreases?|weakens?|strengthens?|diminishes?)\b"
    r"|\beffect\s+of\b[^.]{0,80}\b(?:increases?|decreases?|weakens?|strengthens?|diminishes?)\b\s+with\b"
    r"|\b(?:increases?|decreases?|strengthens?|weakens?)\b[^.;]{0,40}\beffect\s+of\b", re.I | re.S)


def split_sentences(text: str) -> list[str]:
    out = []
    # drop comment/annotation lines individually (<!-- para 3 --> etc.) so they never poison a paragraph start
    text = "\n".join(l for l in text.split("\n") if not l.strip().startswith("<!--"))
    for para in re.split(r"\n+", text):  # \n+ : tolerate one-sentence-per-line archives
        para = para.strip()
        if not para or para.startswith(("|", "!", "#", "```", "---", "<")):
            continue
        protected = ABBREV_PERIODS.sub(lambda m: m.group(0)[:-1] + PDOT, para)
        for s in SENTENCE_SPLIT.split(protected):
            s = s.replace(PDOT, ".").strip()
            if s and len(s) > 3:
                out.append(s)
    return out


def classify_sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    """[(section_label, [paragraph lines])]; unknown-pre-frontmatter skipped."""
    sections: list[tuple[str, list[str]]] = []
    current: tuple[str, list[str]] | None = None
    in_frontmatter = bool(lines and lines[0].strip() == "---")
    fence = False
    for i, line in enumerate(lines):
        if in_frontmatter:
            if i > 0 and line.strip() == "---":
                in_frontmatter = False
            continue
        st = line.strip()
        if st.startswith(("```", "~~~")):
            fence = not fence
            continue
        if fence:
            continue
        label = None
        if st.startswith("#"):
            for name, pat in SECTION_PATTERNS:
                if pat.match(st):
                    label = name
                    break
        if label == "references":
            if current:
                sections.append(current)
            current = None
            continue
        if label:
            if current:
                sections.append(current)
            current = (label, [])
            continue
        if current:
            current[1].append(line)
    if current:
        sections.append(current)
    return sections


def find_tiers(sentence: str, tiers: dict[str, list[str]]) -> list[tuple[str, str, int]]:
    """[(tier, matched_text, start)] — all hits, case-insensitive."""
    hits = []
    low = sentence.lower()
    for tier, pats in tiers.items():
        for pat in pats:
            m = re.search(pat, low)
            if m:
                hits.append((tier, m.group(0), m.start()))
                break  # one hit per tier is enough for reporting
    return hits


def main() -> int:
    ap = argparse.ArgumentParser(description="postdraft-diagnostics v1.0.0 (shadow mode)")
    ap.add_argument("draft", help="Markdown draft path")
    ap.add_argument("--design", required=True,
                    choices=["ols_fe_panel_hlm", "did_natural_experiment", "iv_2sls",
                             "nonlinear", "survival", "experiment", "unknown"],
                    help="design family (from Design Packet / Analysis Manifest)")
    ap.add_argument("--wordlists", type=Path, default=WORDLISTS)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args()

    wl = json.loads(args.wordlists.read_text(encoding="utf-8"))
    allowance = wl["design_allowance"][args.design]
    tiers = wl["verb_tiers"]
    tentative = wl["tentative"]
    hyp_markers = wl["hypothesis_markers"]
    id_markers = wl["identification_markers"]

    text = Path(args.draft).read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    sections = classify_sections(lines)

    # identification markers: searched across the whole draft (results+methods primarily)
    low_all = text.lower()
    id_found = sorted({m for m in id_markers if re.search(m, low_all)})
    wl_tentative = wl["tentative"] + [r"\b(may|might|could)\b"]  # core modals: hedging-strength 极弱档

    flags: list[dict] = []
    stats = {"sentences_scanned": 0, "by_section": {}, "hypothesis_exempt": 0}

    for label, sec_lines in sections:
        if label not in SCANNED:
            continue
        sentences = split_sentences("\n".join(sec_lines))
        stats["by_section"][label] = len(sentences)
        for si, sent in enumerate(sentences, 1):
            stats["sentences_scanned"] += 1
            low = sent.lower()
            if any(re.search(h, low) for h in hyp_markers):
                stats["hypothesis_exempt"] += 1
                continue
            hits = find_tiers(sent, tiers)
            tent_hit = next((p for p in wl_tentative if re.search(p, low)), None)
            stat_subj = SUPPRESS_STAT_SUBJECT.search(low) or SUPPRESS_RESULT_OBJECT.search(low) or SUPPRESS_WHICH_REVEAL.search(low)
            prod_obj = SUPPRESS_PRODUCE_OBJECT.search(low) or PRODUCE_GOODS.search(low)
            proc_led = PROCEDURAL_LED_TO.search(low)
            nonsig = NONSIGNIFICANT.search(low)
            lit_rev = LIT_REVIEW.search(low)
            view_neg = NOT_CONSISTENT_VIEW.search(low)
            proc_meth = PROC_METHODS.search(low)
            stat_att = STAT_ATTACHED.search(low)
            model_sim = MODEL_SIM.search(low)
            table_note = TABLE_NOTE.search(low)
            limitation = LIMITATION_FUTURE.search(low)
            proc_sample = PROC_SAMPLE.search(low)
            descriptive = DESCRIPTIVE_STATS.search(low)
            stat_dir = STAT_ATTACHED_DIR.search(low)
            noun_subj = NOUN_SUBJECT.match(low)
            rival = RIVAL_EXPL.search(low)
            appendix = APPENDIX_REF.search(low)
            hedge_stats = HEDGE_WITH_STATS.search(low)
            accordance = ACCORDANCE_WITH.search(low)
            given_premise = GIVEN_PREMISE.search(low)
            robust_to = ROBUST_TO.search(low)
            construct_def = CONSTRUCT_DEF.search(low)
            examine_whether = EXAMINE_WHETHER.search(low)
            mech_search = MECH_SEARCH.search(low)
            econ_diag = ECON_DIAGNOSTIC.search(low)
            we_argue = re.match(r"\s*(?:we argue|we posit|we propose|our argument)\b", low)
            in_quote = (low.count('"') + low.count('\u201c') + low.count('\u201d')) % 2 == 1
            def _quote_ctx(prefix: str) -> bool:
                opens = prefix.count('\u201c') + (prefix.count('"') % 2)
                return opens > prefix.count('\u201d')
            question = "?" in sent
            if_prefix = re.match(r"\s*[Ii]f\b", sent)
            # conditional tier satisfied by: draft-level id markers OR sentence-level result reporting
            cond_ok = id_found or RESULT_MARKERS.search(low)
            theory_mode = THEORY_MODE.search(low) and not RESULT_MARKERS.search(low)
            slope = SLOPE_CHANGE.search(sent)

            if label == "results":
                for tier, matched, start in hits:
                    modal_guard = MODAL_BEFORE_VERB.search(low[:start]) or IF_GUARD.search(low[:start]) or HEDGE_BEFORE.search(low[:start])
                    neg_guard = NEGATION_BEFORE_TIER.search(low[:start])
                    italic_ctx = low[:start].count('*') % 2 == 1
                    infinitive = low[:start].rstrip().endswith("to")
                    quote_ctx = _quote_ctx(low[:start])
                    if tier in allowance["forbidden"]:
                        if stat_subj or prod_obj or question or if_prefix or modal_guard or neg_guard or proc_led or view_neg or lit_rev or stat_att or table_note or limitation or rival or appendix or given_premise or robust_to or construct_def or examine_whether or italic_ctx or infinitive or in_quote or quote_ctx or we_argue:
                            continue
                        flags.append({
                            "type": "OVERCLAIM", "section": label, "sentence_no": si,
                            "tier": tier, "match": matched, "sentence": sent,
                            "rule": f"{args.design}.forbidden includes {tier}",
                        })
                    elif tier in allowance.get("conditional", {}) and not cond_ok:
                        if theory_mode or slope or question or nonsig or lit_rev or model_sim or proc_sample or descriptive or stat_dir or noun_subj or accordance or modal_guard or proc_meth or econ_diag or examine_whether:
                            continue
                        flags.append({
                            "type": "CONDITION_MISSING", "section": label, "sentence_no": si,
                            "tier": tier, "match": matched, "sentence": sent,
                            "rule": f"{args.design}.conditional[{tier}] requires identification markers or result-reporting context; none found",
                        })
                # under-claim: tentative + hard-stat context in Results (non-sig/structural-uncertainty/puzzle-exempt)
                if tent_hit and hits and STAT_HARD.search(low) and not econ_diag and not nonsig and not PUZZLE_OR_STRUCTURAL.search(low) and not hedge_stats and not mech_search and not proc_sample and not proc_meth and not WE_REASON.search(low):
                    flags.append({
                        "type": "UNDERCLAIM", "section": label, "sentence_no": si,
                        "tier": "tentative", "match": tent_hit, "sentence": sent,
                        "rule": "results_main_effect: verified effect weakened by tentative (claim-calibration 勿过度回缩)",
                    })
            elif label == "methods":
                for tier, matched, start in hits:
                    modal_guard = MODAL_BEFORE_VERB.search(low[:start]) or IF_GUARD.search(low[:start]) or HEDGE_BEFORE.search(low[:start])
                    neg_guard = NEGATION_BEFORE_TIER.search(low[:start])
                    italic_ctx = low[:start].count('*') % 2 == 1
                    infinitive = low[:start].rstrip().endswith("to")
                    quote_ctx = _quote_ctx(low[:start])
                    if tier in allowance["forbidden"]:
                        if stat_subj or prod_obj or question or if_prefix or modal_guard or neg_guard or proc_led or view_neg or lit_rev or stat_att or table_note or limitation or model_sim or rival or given_premise or robust_to or construct_def or examine_whether or italic_ctx or infinitive or in_quote or quote_ctx or we_argue:
                            continue
                        flags.append({
                            "type": "OVERCLAIM", "section": label, "sentence_no": si,
                            "tier": tier, "match": matched, "sentence": sent,
                            "rule": f"methods_m7: {args.design}.forbidden includes {tier}",
                        })
                    elif tier in allowance.get("conditional", {}) and not cond_ok:
                        if theory_mode or slope or question or nonsig or lit_rev or proc_meth or model_sim or descriptive or stat_dir or noun_subj or modal_guard or econ_diag or examine_whether:
                            continue
                        flags.append({
                            "type": "CONDITION_MISSING", "section": label, "sentence_no": si,
                            "tier": tier, "match": matched, "sentence": sent,
                            "rule": f"methods_m8: {tier} preview requires identification markers or result-reporting context; none found",
                        })
            elif label == "discussion":
                strong = [h for h in hits if h[0] in ("T_MECHANISM", "T_DEFINITIVE")]
                disc_tent = tent_hit or HEDGE_FAMILY.search(low)
                reporting = re.search(
                    r"\b(we found|we find|our finding|our results?|consistent with|this effect (?:was|is) mediated|the effect (?:was|is) mediated|was partially mediated)\b", low)
                if strong and not disc_tent and not stat_subj and not question and not reporting and not lit_rev and not view_neg:
                    tier, matched, start = strong[0]
                    if MODAL_BEFORE_VERB.search(low[:start]):
                        continue
                    flags.append({
                        "type": "OVERCLAIM", "section": label, "sentence_no": si,
                        "tier": tier, "match": matched, "sentence": sent,
                        "rule": "discussion_mechanism: extrapolation without tentative framing",
                    })

    report = {
        "tool": "postdraft-diagnostics", "version": wl["version"], "mode": "shadow",
        "draft": str(args.draft), "design": args.design,
        "sections_scanned": {k: v for k, v in stats["by_section"].items()},
        "identification_markers_found": id_found,
        "sentences_scanned": stats["sentences_scanned"],
        "hypothesis_exempt": stats["hypothesis_exempt"],
        "flag_count": len(flags),
        "flags": flags,
        "disclaimer": "diagnostic observer only — no score, no gate, no rewrite; human adjudication required",
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=1))
    else:
        print(f"postdraft-diagnostics v{wl['version']} (SHADOW MODE — no pass/fail)")
        print(f"draft: {args.draft}")
        print(f"design: {args.design}" + ("  [design-unannotated: supply metadata and rerun]" if args.design == "unknown" else ""))
        print(f"sections scanned: {', '.join(f'{k} ({v} sentences)' for k, v in stats['by_section'].items())}")
        print(f"identification markers found: {', '.join(id_found) if id_found else 'NONE'}")
        print(f"sentences: {stats['sentences_scanned']} scanned | {stats['hypothesis_exempt']} hypothesis-exempt")
        print(f"flags: {len(flags)}")
        for f in flags:
            print(f"\n[{f['type']}] {f['section']} s{f['sentence_no']}  tier={f['tier']} ({f['match']!r})")
            print(f"  > {f['sentence'][:160]}")
            print(f"  rule: {f['rule']}")
        print("\n(diagnostic observer only — no score, no gate; human adjudication required)")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, json.JSONDecodeError, re.error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
