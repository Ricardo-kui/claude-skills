# Story Learning Card — Zhang et al. (2025, rejected manuscript: SMJ desk/1R reject, JAMS reject)

## Metadata

```yaml
schema_version: "4.0-lite"
id: zhang-idd-advertising-rejected
paper:
  citekey: null
  title: "Beyond Employee Retention: Leveraging Brand Equity to Mitigate Knowledge Leakage Risk from Employee Mobility"
  outlet: null
  year: 2025
  publication_status: working # rejected at SMJ (first round) and JAMS; analyzed as a rejected working manuscript
  paper_type: quantitative
  source_version: working_paper
  inclusion_rationale: "A cautionary paired-comparison object against moon2026-trade-secret-protection-advertising: same IDD shock x advertising-spending design, but this manuscript was rejected twice. Its narrative defects—construct overstretch (advertising flow named 'brand equity investment'), an undiscussed main-effect sign reversal in the full model, a paradigm-shift contribution claim the evidence cannot carry, and mechanism tests that skip every intermediate link—are precisely the learning content."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "JAMS_Manuscript.md (extracted plain text, project folder, 2026-08 review session; includes Tables 1-4)"
    - "JAMS_WebAppendix.md (extracted plain text; Web Appendix A Heckman design, B data/variables, C robustness incl. event-study Tables C1-C5 and Figures C1-C3, D moderator sensitivity Tables D1-D4)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Results received above-default attention because the card's key learning signal (Table 3 full-model main-effect sign reversal, undiscussed in text) is only visible by reading the table against the prose; the Web Appendix was read in full on a second pass, which showed the same reversal replicated—and still un-narrated—across appendix Tables D1-D4."
mechanism_evidence:
  status: partly_probed
  basis: "Table 4 interacts LnADV x IDD rejection to predict downstream outcomes (market share, net income at t/t+1/t+2; Glassdoor rating at t+1), but no intermediate link of either theorized pathway—customer loyalty/switching costs/rival imitation on the external side, actual retention or turnover on the internal side—is ever measured, and the interaction design tests outcome amplification, not mediation of the H1 effect."
classification:
  theoretical_problem_form: [incompleteness]
  narrative_dynamics: [supply-side-to-demand-side-reframe, dual-mechanism-defense, paradigm-shift-claim]
  retrieval_signals: [inevitable-disclosure-doctrine, idd-rejection, advertising-spending, brand-equity, knowledge-leakage, employee-mobility, rbv, staggered-did, differentiation, cost-leadership, b2c, glassdoor, rejected-manuscript]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "partial"
    requires: []
    learn:
      - "Reframe an incumbent paradigm with a supply-side/demand-side asymmetry (retention = stopping outflow vs. brand = devaluing leaked knowledge in rival hands), and back the reframe with a literature-positioning table (Table 1) that maps every cited prior study as supply-side-only."
      - "Open with a live policy hook (FTC 2024 non-compete ban) to make a decades-old legal shock feel urgent."
    caveat:
      - "The 2024 FTC hook never returns in the evidence (identification is 1977-2023 state IDD rejections), so the opening promise and the tested setting drift apart; and the threefold contribution preview already claims paradigm status ('reconceptualize', 'pioneers', 'first to theorize and test') that the results cannot underwrite—a cautionary case of front-loading a claim the back end must then fail to pay off."
  theory:
    suitable: "partial"
    requires: []
    learn:
      - "Derive one DV prediction from two stacked mechanisms (external demand-side isolation + internal nonpecuniary retention), then derive all three moderators from a single strategic-fit logic so the contingency set reads as one argument."
    caveat:
      - "The theory's named construct is brand equity (a perceptual stock) while the only operationalization is advertising spending (a flow); the paper narrates the stock but estimates the flow, and neither intermediate link (loyalty/switching costs, actual retention) is given a measurable form—do not copy the naming-overstretch or the unmeasurable middle."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Pair staggered state-court DiD with a Heckman IMR for advertising-disclosure selection, and pre-commit to heterogeneity-robust event-study estimators (Sun-Abraham, Borusyak-Jaravel-Spiess) for staggered timing."
    caveat:
      - "The measurement section carries the entire construct claim: a three-paragraph defense that advertising = brand equity investment is doing work that belongs to the theory-evidence link, and the limitations section later contradicts it by calling the DV a 'composite measure' of brand-building activities."
      - "Disclosure-completeness gap (Web-Appendix-informed): the main text promises 'the first-stage estimation results are provided in Web Appendix A,' but Appendix A contains only the instrument construction and probit specification—no first-stage coefficient table appears anywhere—and the IMR is insignificant in most second-stage models (p roughly .055-.23), so the selection-correction storyline rests on an unshown first stage."
  results:
    suitable: "partial"
    requires: []
    learn:
      - "Negative example worth studying: once interaction terms enter (Table 3 cols. 3-4), the IDD-rejection main effect flips to -0.090/-0.101 (p=.017/.008) for the B2B baseline group—negative and significant—and the text says only 'Column (4) confirms robustness in the full model.' An un-narrated sign reversal on the focal coefficient is exactly what referees find; the learnable move is that conditional main effects must be reported and interpreted, not absorbed silently."
      - "The event-study layer is genuinely well staged (Web Appendix C): TWFE leads/lags with jointly zero pre-trends (Table C1), then Sun-Abraham and Borusyak-Jaravel-Spiess estimates on identical controls (Figure C1), then a 1,000-draw placebo distribution (Figure C3)—a validity escalation worth imitating as design sequencing."
    caveat:
      - "The baseline magnitude framing ('5.4-6.2% increase relative to the sample mean') is assembled from the coefficient and mean in a way that reads larger than the log-point estimate warrants; do not copy the economic-significance rhetoric without showing the arithmetic."
      - "Web-Appendix-informed hardening: the sign reversal is not a one-table accident—it replicates in every appendix full model (D1 UTSA control: -0.100, p=.008; D2 adjacent-state matching: -0.091, p=.030; D3 5% winsorization: -0.127, p=.005; D4 text-based strategies with B2C: -0.090/-0.101, p=.017/.006)—and D3's prose asserts 'the main effect of IDD rejection remains positive and significant' while its own column (5) shows -0.127 (p=.005), an active mis-description of the table it introduces."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Negative example: the ending claims a paradigm shift ('shifting the scholarly paradigm from internal employee retention to external, market-based defense') although the evidence shows only an advertising-spending response with a reversed main effect for B2B firms—the gap between ending altitude and evidence altitude is the rejection-relevant signal."
    caveat:
      - "The limitations subsection quietly re-describes the DV as a 'composite measure' of brand-building investment, contradicting the single-measure reality (advertising only); a discussion that re-labeled the construct to advertising response would have been more defensible."
story_assessment:
  overall_role: cautionary_case
  mode: single_read
```

## Story Reading

### Theme question

When legal tools that keep knowledge-bearing employees from leaving are dismantled, can a firm defend itself by investing outward—building brand equity so that leaked knowledge loses its value in a rival's hands—instead of investing inward in retention?

### Whole-story synopsis

The paper opens on the FTC's April 2024 non-compete ban to dramatize a long erosion of legal protection against knowledge leakage, then problematizes the incumbent paradigm: decades of strategy research answer leakage with inward retention—legal barriers and golden handcuffs—which is crumbling and, more deeply, addresses only the supply side (stopping outflow) while ignoring the demand side (making leaked knowledge worthless to the rival). A Coca-Cola executive's quote supplies the demand-side intuition: the formula without the brand is worth little. The proposed answer is brand equity as a market-based isolating mechanism with two pathways: externally, loyalty and switching costs devalue leaked knowledge; internally, brand prestige is a nonpecuniary retention incentive. H1 predicts firms raise brand equity investment when leakage risk rises; H2a/H2b and H3 derive differentiation, cost leadership, and B2C/B2B as fit-based contingencies. The design exploits staggered state-level IDD rejections (18 states, 1977-2023, 59,628 firm-years) in a DiD with Heckman correction, with LnADV standing in for brand equity investment. The baseline shows a 5.4-6.2% advertising increase after rejection; the moderators interact as theorized—except that in the full model the IDD main effect turns significantly negative for the B2B baseline, a reversal the text never mentions. Mechanism tests interact advertising with IDD to predict market share, net income, and Glassdoor satisfaction, probing downstream outcomes while leaving both theorized intermediate links (customer lock-in; actual retention) unmeasured. The Discussion closes by claiming a paradigm shift from internal prevention to external safeguarding and a strategic-substitute role for brand equity—an ending pitched well above what the evidence carries, including a limitations paragraph that re-describes the single advertising measure as a 'composite measure.'

### Characters and storylines

- **Main character(s):** Brand equity investment—the hero construct whose journey (from marketing expense to strategic defense weapon) is the paper's plot; and IDD rejection—the institutional antagonist-event whose staggered arrival drives the action. The hero has an embodiment problem: it appears on stage only as advertising spending.
- **Supporting character(s):** Differentiation, cost leadership, and B2C/B2B as fit-based contingency characters that modulate the hero's response; market share, net income, and Glassdoor satisfaction as payoff witnesses summoned to vouch for the two mechanisms; the incumbent retention paradigm (non-competes, golden handcuffs) as the declining former champion.
- **Storyline(s):** The legal-erosion storyline (protection weakening from IDD rejections to the FTC ban) and the brand-defense storyline (advertising as buildable moat) run in parallel and intersect at the DiD; the internal-retention storyline (brand prestige binds employees) branches off inside the theory and rejoins only weakly, via a satisfaction rating rather than any retention outcome; the contingency storyline is where the plot quietly breaks, because the full model shows the effect reversing sign for the B2B baseline.

### Five acts

- **Exposition:** FTC bans non-competes (2024); the retention-centric fortress—legal walls plus golden handcuffs—is crumbling and was always supply-side-only; the demand-side question (devalue leaked knowledge in rival hands) is unasked, with the Coca-Cola formula-vs-memory quote as its emblem.
- **Rising action:** RBV plus market-based assets yield brand equity as a dual-pathway isolating mechanism (external demand-side barrier, internal nonpecuniary incentive); H1 predicts escalation of brand investment; differentiation, cost leadership, and B2C/B2B contingencies become H2a/H2b/H3 via one strategic-fit logic.
- **Climax:** Staggered DiD on IDD rejection shows treated firms raising advertising 5.4-6.2%, robust across ten checks including heterogeneity-robust event studies, placebos, and PSM.
- **Falling action:** Moderators confirm individually, but Table 3's full model turns the IDD main effect negative and significant (-0.101, p=.008) for the B2B baseline—unremarked in the text, and replicated still unremarked across appendix Tables D1-D4 (down to -0.127, p=.005 under 5% winsorization, whose prose claims the main effect 'remains positive and significant'); Table 4's ADV x IDD interactions predict market share, net income, and Glassdoor satisfaction, probing downstream payoffs while the theorized intermediate links stay unmeasured.
- **Denouement:** The Discussion claims a paradigm shift to external, market-based defense and a strategic-substitute role for brand equity, with managerial 'market moat' advice; limitations concede the DV is a single measure while calling it composite, leaving the opening's brand-equity promise only partially kept.

### Tension (optional)

- **Source:** A real institutional trend (weakening legal protection of knowledge via employee mobility) against a real theoretical incompleteness (the retention paradigm never addresses what happens after knowledge leaks).
- **Construction:** The introduction personifies the incumbent paradigm as a 'crumbling fortress,' uses the FTC rule as a present-tense stakes device, and deploys Table 1 to display every prior study as supply-side-only—an effective construction that the evidence side (a 1977-2023 identification and an advertising-flow DV) does not fully honor.

### Alternative readings (optional)

- **analyst_counterfactual:** Read the paper as a narrower, defensible advertising-response story: 'firms raise advertising when legal protection of trade secrets weakens'—essentially Moon et al. (2026) with rejection instead of recognition. Under this reading the construct overstretch, the paradigm-shift claim, and most referee vulnerability disappear; the B2B sign reversal would still need narration. The authors instead chose the higher-altitude brand-equity-as-isolating-mechanism framing, which is where the story breaks.

## Story Assessment

- **Theme coherence:** `partly_works` — The opening question ('how to defend when legal locks fail') is clear and does organize the theory and design, but the question the evidence answers ('do firms advertise more after IDD rejection?') is narrower than the question the front end asks ('do firms build brand equity as an isolating mechanism?'), so the theme's center of gravity shifts between naming and measurement.
- **Character discipline:** `partly_works` — The shock, the hero construct, and the three moderators are distinguishable and the moderators share one fit logic, but the hero is embodied only by an advertising flow while narrated as a perceptual stock, and the internal-retention storyline is vouched for by a satisfaction rating rather than retention—two supporting witnesses testifying to something other than what they were called for.
- **Tie–unravel alignment:** `does_not_work` — The full model's focal main effect flips to a significant negative for the B2B baseline and the text declares robustness instead of narrating it; the Web Appendix hardens this from a one-table lapse into a systematic pattern—the reversal replicates in every appendix full model (D1: -0.100, p=.008; D2: -0.091, p=.030; D3: -0.127, p=.005; D4: -0.101, p=.006) and D3's prose positively mis-describes its own table ('the main effect remains positive and significant'). The promised dual mechanism is unraveled only at downstream outcomes via interaction terms, with both intermediate links (customer lock-in, actual retention) unmeasured; the evidence thus does not answer the front-end question at the altitude at which it was posed.
- **Ending quality:** `partly_works` — The Discussion does return to the opening and attempts transformation (prevention paradigm → safeguarding paradigm), but the transformation claims more than the evidence changed, and the limitations subsection quietly contradicts the measurement section ('composite measure' vs. advertising-only), so the ending re-labels rather than resolves.
- **Boundary:** This evaluates storytelling, not research quality or identification. The DiD execution itself (staggered estimators, clean pre-trends in Table C1 and Figure C1, 1,000-draw placebo in Figure C3, adjacent-state matching) is competent and, in the event-study layer, well staged; the failure points assessed here are narrative: construct naming, un-narrated conditional effects replicated across the appendix, a Heckman first stage promised in the main text but never reported in Web Appendix A (with the IMR insignificant in most models), and claim-evidence altitude mismatch.

## Learning Affordances

### Introduction

- **Suitable:** `partial`
- **Learn:** (1) Reframe an incumbent paradigm by exposing a supply-side/demand-side asymmetry and displaying it in a literature-positioning table where every prior study lands on one side. (2) Use a live policy event (FTC non-compete ban) as a present-tense hook for an older identification setting.
- **Do not copy:** The hook-setting mismatch (2024 FTC rule vs. 1977-2023 state rejections) and the paradigm-status contribution preview; both require the back end to pay off at an altitude this design cannot reach—transfer only if the identification setting and the hook are the same institutional object.

### Theory

- **Suitable:** `partial`
- **Learn:** (1) Stack two mechanisms (external market shield + internal retention incentive) under one hero construct to produce a single DV prediction, then derive all moderators from one strategic-fit principle. (2) Use a concrete brand anecdote (Coca-Cola formula, Apple premium, Ryanair efficiency) to make each why-chain legible.
- **Do not copy:** The construct-overstretch—naming a perceptual stock (brand equity) while theorizing at an altitude the operationalized flow (advertising) cannot reach—and mechanism chains whose intermediate links are never given measurable form; this is the card's central cautionary signal.

### Methods

- **Suitable:** `partial`
- **Learn:** Combine staggered DiD with Heckman IMR for outcome-disclosure selection and pre-commit to heterogeneity-robust estimators (Sun-Abraham; Borusyak-Jaravel-Spiess) plus a placebo and PSM battery.
- **Do not copy:** Letting the measurement section carry the construct claim with a proxy-validity essay; do not let the limitations section later re-describe the measure differently than the methods defined it; and do not promise appendix evidence that is not there—the main text announces first-stage Heckman results 'provided in Web Appendix A,' yet Appendix A reports only instrument construction, no estimated first stage, while the IMR is mostly insignificant.

### Results

- **Suitable:** `partial`
- **Learn:** (1) Negative example: when interactions absorb the main effect (Table 3 cols. 3-4: IDD main effect -0.090/-0.101, significant, for the B2B baseline), the conditional main effect must be reported and interpreted—declaring 'the full model confirms robustness' is the exact move referees punish, and the appendix shows the same un-narrated reversal in every D-table full model. (2) Positive example: stage the validity battery as escalation—TWFE event study with clean pre-trends (Table C1), heterogeneity-robust estimators on identical controls (Figure C1), state-level aggregation, PSM with balance diagnostics, 1,000-draw placebo tail (Figure C3), then confound-specific sensitivity cuts.
- **Do not copy:** The magnitude rhetoric that inflates a log-point coefficient into a percent-of-mean claim without showing the arithmetic; mechanism tables that interact treatment with the DV to predict outcomes while calling it a mediation test; and D3-style prose that asserts the main effect 'remains positive and significant' while its own full-model column shows -0.127 (p=.005).

### Discussion

- **Suitable:** `partial`
- **Learn:** Negative example of ending-altitude control: the discussion claims a scholarly paradigm shift and a strategic-substitute theorem from evidence showing an advertising response with a reversed B2B baseline; the learnable skill is to pitch the denouement at the altitude the results actually reached.
- **Do not copy:** Re-describing the DV in limitations as a 'composite measure' when the design used advertising only; inconsistency between methods and limitations is a credibility leak.

## Comparison prompt (optional)

Compare with `moon2026-trade-secret-protection-advertising`: same IDD shock and same advertising DV, opposite treatment direction (recognition vs. rejection) and opposite fate (published vs. twice-rejected). What does Moon buy by naming the DV 'advertising spending' and the mechanism 'managerial attention'—constructs at the altitude of the data—versus this card's 'brand equity investment' and 'isolating mechanism' framing; and does Moon's post hoc Discussion mechanism seam differ in kind or only in degree from this card's un-narrated sign reversal and unmeasured intermediate links? A second, appendix-level contrast: both papers use the same peer-disclosure Heckman design (after Moon et al. 2023), but Moon's selection story is fully specified whereas this manuscript promises first-stage results in Web Appendix A and never reports them—does visible promise-keeping at the appendix level change how much referee trust the main text can spend?
