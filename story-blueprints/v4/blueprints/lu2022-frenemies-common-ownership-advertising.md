# Story Learning Card — Lu, Shen, Wang, and Zhang (2022, Management Science)

## Metadata

```yaml
schema_version: "4.0-lite"
id: lu2022-frenemies-common-ownership-advertising
paper:
  citekey: lu_et_al_2022_frenemies_corporate_advertising
  title: "Frenemies: Corporate Advertising Under Common Ownership"
  outlet: "Management Science"
  year: 2022
  publication_status: published
  paper_type: quantitative
  source_version: publisher_pdf
  inclusion_rationale: "A bounded learning object for the econ/MS register of a natural-experiment causal story: a phenomenon-first Incompleteness front end that converts an identification obstacle into narrative credibility, a mechanism-deduction theory that pre-seeds its own boundary twist, threat-battery results staged as promise-payoff-unravel, and one teachable promise-fulfillment overreach (Table 13) plus a recap-only ending as local cautionary material."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "lu_et_al_2022_frenemies_corporate_advertising.pdm/fulltext.text-only.md"
    - "lu_et_al_2022_frenemies_corporate_advertising.pdm/sections/{introduction,theory,methods,results}.json (verified L2 distillations)"
    - "lu_et_al_2022_frenemies_corporate_advertising.pdm/sections/discussion.md (§6 Conclusion, ~683 words; the paper has no separate discussion section)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: null
mechanism_evidence:
  status: partly_probed
  basis: "Cross-sectional benefit/cost partitions and the profitability corollary fit the coordination account, but the three coordination channels (voice/incentives/vote, enforcement, information transmission) are never observed, benefit and cost of coordination are admitted unmeasurable conjectures, and one cost proxy (same-state headquarters) carries an author-acknowledged alternative reading."
classification:
  theoretical_problem_form: [ownership-structure-as-organizational-driver, coordination-benefit-cost-calculus, invisible-arrangement-visible-budget]
  narrative_dynamics: [data-shock-blind-spot-opening, identification-obstacle-to-credibility-turn, promise-payoff-unravel-staging, pre-seeded-boundary-twist, premise-reversal-ending]
  retrieval_signals: [common-ownership-product-market-coordination, advertising-as-combative-tool, institution-merger-natural-experiment, threat-battery-did, same-institution-control-construction]
  confidence: provisional
section_learning:
  introduction:
    suitable: "yes"
    requires: [third-party-event-induced-treatment, citable-institutional-drivers-of-the-event]
    learn:
      - "Run the gap in two places: declare the blind spot inside the opening paragraph, then deepen it with a dual-reason attribution (the phenomenon is new AND causal identification is hard) so the gap reads as structurally difficult to study rather than as prior scholarship failing — which pre-sells the design as the resolution."
      - "Preview identification as plot: translate treatment construction, event-exogeneity defense, parallel-trends verification, and a dual-unit effect size into introduction paragraphs, so the reader accepts causal language before reaching Methods."
    caveat:
      - "The fused ~190-word opening paragraph and a preview block near 39% of the introduction are econ/MS register; in management journals this density buries the knot. Hardcoded preview numbers create revision-sync liability, and the exogeneity passage leans on citable institutional drivers — without such literature the same sentences invite identification attacks. Stakes ride on prevalence quantification with no consequence scenario."
  theory:
    suitable: "partial"
    requires: [mechanism-deduction-register, borrowed-theory-acceptable]
    learn:
      - "Derive an opposite-signed moderation pair from one cost-benefit calculus after the baseline main effect, so the two boundary hypotheses cover both sides of a single mechanism instead of reading as two ad hoc moderators."
      - "Pre-seed the twist: register the later boundary case (a commonly owned pair that is small relative to industry leaders) in theory as a low-commitment 'worth noting, explored empirically later' move, so its Results appearance lands as a promised complication rather than a post hoc rescue."
    caveat:
      - "The engine is borrowed theory (portfolio-value internalization; combative advertising) — the section deduces rather than builds, the coordination channels are enumerated for feasibility but never tested, and benefit/cost are conceded unmeasurable. Do not import the structure when the mechanism itself is contested or the moderators lack even proxy justification."
  methods:
    suitable: "partial"
    requires: [third-party-shock-with-institutional-drivers, archival-ownership-or-equitable-data]
    learn:
      - "Open threat-first, shock-last: name endogeneity and split it into two sources (selection on prospects; unobservable firm traits) before introducing the instrument, so institutional background arrives as a solution rather than a data dump."
      - "Make group assignment reproducible: a numbered dual-condition treatment rule fixed to pre-merger information, a named real-event walkthrough (one merger, unit by unit, figure and text sharing the same units), and treatment/control counts reported inside the sample funnel."
    caveat:
      - "2022 TWFE vintage: no event-study coefficient plot, no heterogeneity-robust estimator, cluster level unstated in Methods, and the estimation-window argument is truncated mid-sentence in the source. Copy the assignment and exogeneity staging, not the estimator specification."
  results:
    suitable: "yes"
    requires: [did-family-design]
    learn:
      - "Let the reader see the effect before the coefficient: a raw treatment/control trend figure doubles as qualitative parallel-trends pre-enactment and mechanism preview, hands off to the formal estimate, and is followed by one dedicated paragraph translating economic magnitude across all outcome measures at once."
      - "Unravel by theoretical lever, not table order: organize moderation by the theory's own dials (benefit proxies, then cost proxies), pairing each significant pole against its null pole and formalizing the between-group gap, so null groups read as boundary evidence; title each robustness subsection with the threat it answers."
    caveat:
      - "One payoff overreaches its evidence: the institutional-ownership partition is narrated as 'consistent evidence' although two of three between-group tests are insignificant, a new hypothesis enters inside Results on the strength of the theory-section pre-seed rather than an explicit post-hoc flag, and one outcome measure stays weak across many tables without discussion. Copy the staging, not the summarizing license."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Close by reversing the opening premise instead of restating findings: the conclusion re-reads the front end's default (the firm advertises to maximize firm value) as challenged by the evidence, then escalates implications across audiences from private (managers, analysts, agencies) to public (antitrust)."
    caveat:
      - "The ending is recap-shaped with no limitations passage — the control construction's coverage cost goes unacknowledged — and the closing 'further research is required' carries no specific agenda. Transfer the premise-reversal move; supply your own honesty layer."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
```

## Story Reading

### Theme question

When the same institutional blockholder owns stakes in rival firms, do those rivals compete less fiercely — visible in their advertising budgets — and under what conditions does that quieting appear or disappear?

### Whole-story synopsis

The paper opens on advertising's visible scale — hundreds of billions of dollars, named trade sources — and locates a blind spot: advertising research explains spending by demand and competition, while organizational factors, above all ownership, go unexamined despite a recognizable anecdote (a named investor common to two airlines precedes their marketing alliance) hinting that owners can quiet rivalry. The blind spot is then quantified as a spreading phenomenon, and imported industrial-organization theory gives it a plot: common owners maximize portfolio value, so rivals sharing an owner should internalize mutual business stealing; since advertising is established as combative, the prediction is quieter ad budgets. The story names its obstacle honestly — blockholders do not invest randomly — and converts that obstacle into the engine: mergers of financial institutions create common-ownership links that no stock-picker chose, and the same institutions' other portfolio firms, untouched by new links, serve as controls. The design verifies its own stage (parallel pre-trends), reveals the effect (roughly a sixth of dollar advertising gone), and then interrogates the answer twice. A robustness battery, each subsection titled by the threat it answers, plus a profitability corollary argue the cut is a coordination payoff rather than neglect. Then the unravel re-reads the average effect through a coordination cost-benefit calculus: cuts deepen where coordination pays (product similarity, ownership magnitude, advertising intensity) and shrink where it costs (geographic distance, diffuse institutional ownership), with a pre-seeded twist — when the commonly owned pair is small relative to industry leaders, the effect vanishes. The conclusion returns to the opening and reverses its premise: the optimizer writing the ad budget may be the portfolio, not the firm, and industry power should be read through owners' portfolios.

### Characters and storylines

- **Main character — common ownership:** institutional blockholders holding rivals simultaneously; the invisible structure whose arrival through mergers is the inciting force, and whose presence or absence organizes every test.
- **Main character — advertising expenditure:** the visible competitive instrument through which the invisible structure becomes observable; the paper's answer is written in this budget's movement.
- **Supporting — financial institution mergers:** the exogenous matchmaker; its timing, drivers, and portfolio weights carry the causal plot's credibility.
- **Supporting — coordination benefit and coordination cost:** twin dials imported from theory that organize the unravel, translating a single coordination claim into conditional predictions.
- **Supporting (twist) — relative competitiveness of the pair vs industry leaders:** pre-seeded in the theory section, re-enters late to bound the main effect.
- **Storyline 1 (ownership):** merger → new common links → portfolio-internalization incentive.
- **Storyline 2 (advertising):** combative spending → softened rivalry incentive → measurable cut.
- **Storyline 3 (conditionality):** the benefit/cost dials and the pair's position in the industry sort when the cut appears; it intersects the first two in the cross-sectional unravel.

### Five acts

- **Exposition:** Advertising is huge, visible, and strategic; its literature explains demand and competition, not organization; common ownership is surging, theory predicts it softens competition, and one anecdote shows the pattern in the wild.
- **Rising action:** The obstacle — endogenous blockholding — is named and dismantled: mergers assign treatment by pre-merger holdings only; controls are the same institutions' other holdings; the design promises that if common ownership quiets rivalry, treated budgets should fall relative to controls after parallel pre-trends.
- **Climax:** The trend figure lets the reader see the divergence; the formal estimate confirms it — treated firms cut advertising by roughly 17% (about half a point of the ad-to-sales ratio) — and the main hypothesis is declared answered in the paper's strongest register.
- **Falling action:** The answer is stress-tested, then unpacked: a threat battery (matched controls, preshock-overlap partition, alternative windows, reconstructed controls) holds the effect; rising profitability stages the cut as a coordination payoff; the unravel re-reads the average through benefit proxies (35% cut in the high-similarity pole vs none in the low; parallel results for ownership magnitude and advertising intensity) and cost proxies (large cuts only when headquarters are close and institutions concentrated), ending on the pre-seeded boundary — small pairs relative to industry leaders do not cut.
- **Denouement:** The conclusion recaps and reverses the opening premise — advertising may serve the portfolio rather than the firm — then cascades implications from managers to analysts to advertising agencies to antitrust authorities, closing with a call for welfare research.

### Tension

- **Source:** The causal force is invisible — ownership links sit in regulatory filings, not in the ad market, and coordination itself is never directly observable; the whole story must make an unobservable arrangement legible through a public budget line.
- **Construction:** The paper makes the arrangement legible by quantifying the blind spot's prevalence, naming a recognizable anecdote before any data appear, turning the epistemic weakness (blockholders do not invest randomly) into the design's centerpiece, and staging unmeasurable coordination as benefit/cost conditions whose observable correlates move as the theory predicts.

### Alternative readings

- **author_signaled_alternative:** The authors acknowledge (crediting a referee) that same-state headquarters could proxy coordination benefit — competition intensity — rather than coordination cost; the benefit/cost mapping that organizes the falling action therefore has a seam the authors themselves concede.
- **analyst_counterfactual:** The profitability corollary is staged as coordination evidence, but the story would survive readings in which post-merger performance reflects other portfolio-firm differences; the paper's own device ("If this argument is valid, we should expect...") marks it as a consistency check, not an observation of the mechanism.

## Story Assessment

- **Theme coherence:** `works` — one question (does common ownership quiet a visible competitive instrument?) organizes the intro's promise, the theory's prediction, the design, the climax, and the unravel; the conclusion restates it as a premise-reversal rather than a new topic.
- **Character discipline:** `works` — common ownership, the ad budget, the merger shock, and the benefit/cost dials each hold one narrative job; the late twist was seeded in the theory section, so no stranger enters; the profitability corollary is scoped as corroboration, not a subplot.
- **Knot integrity:** `works` — the challenge is genuine: coordination is unobservable and blockholding is endogenous; the story's plausibility rests on whether the merger device can overcome both, and the paper confronts rather than assumes away that burden.
- **Plot emergence:** `works` — the prediction, design, and moderation structure follow from the constructs (portfolio internalization → combative advertising → conditional cut) and from one cost-benefit calculus, not from a moderator shopping list; the admitted unmeasurability of benefit/cost is handled as the situation's constraint, with proxy correlates doing the narrative work.
- **Tie–unravel alignment:** `partly_works` — the front end's promise (effect, robustness, benefit/cost organization) is delivered act by act, but one cost-side promise is settled with overstated language: the institutional-ownership partition is summarized as "consistent evidence" although two of three between-group tests are insignificant, and one outcome measure stays weak across many tables without discussion; claim tightness slips exactly where the intro promised conditional precision.
- **Ending quality:** `partly_works` — the ending returns and transforms (portfolio-interests reversal; antitrust reading of industry power through owner portfolios), but it operates in recap mode with no limitations passage — the same-institution control construction's coverage cost is never acknowledged — and a generic further-research close.
- **Boundary:** This evaluates storytelling only, not research quality, identification credibility, or journal value; the estimator vintage (2022 TWFE register, no event-study plot or heterogeneity-robust re-estimation) is recorded as a narrative-era fact and a transfer caution, not as a verdict on the paper's evidence.

**Mechanism evidence check:** `partly_probed` — the benefit/cost partitions and the profitability corollary fit the coordination account, but the coordination channels are never observed, benefit/cost are conceded unmeasurable, and one cost proxy carries an author-acknowledged alternative reading.

## Learning Affordances

### Introduction

Use when a causal paper's treatment is induced by a third-party event and the event's drivers have citable institutional history. The two-place gap move converts an identification weakness into a credibility asset: the gap is not an accusation but a structural difficulty the design resolves. The identification-as-plot preview accepts causal language before Methods.

Do not copy: the fused econ-register opening paragraph or the ~39%-of-intro preview block into management journals; hardcoded preview numbers without a revision-sync discipline; the exogeneity passage without citable event drivers; prevalence-quantified stakes without any consequence scenario.

### Theory

Use when a single mechanism admits a cost-benefit reading: derive both boundary hypotheses from one calculus after the baseline effect, and pre-seed any later boundary twist as a low-commitment "worth noting" so Results can cash it without post hoc suspicion.

Do not copy: the deduction-from-borrowed-theory register when your mechanism is contested; channel enumeration for channels you will never test; moderation pairs built on proxies with no measurement story.

### Methods and Results

Use when a DiD-type story must earn causality on the page: open threat-first and shock-last; make group assignment a reproducible procedure (numbered ex-ante rules, a named-event walkthrough, counts inside the funnel); let the reader see the effect in raw trends before the coefficient, then deliver economic magnitude in one dedicated translation paragraph; unravel by the theory's own dials with significant/null poles paired and between-group gaps formalized; title robustness subsections by the threat they answer.

Do not copy: the 2022 TWFE estimator vintage (no event-study coefficient plot, no heterogeneity-robust re-estimation) — the staging transfers, the specification must meet the current standard; the summarizing license that narrates a mixed partition as "consistent evidence"; introducing a new hypothesis inside Results on the strength of a theory-section seed alone.

### Discussion

Use the premise-reversal close when the evidence genuinely contradicts the front end's default assumption, escalating implications from private to public audiences.

Do not copy: the recap-only ending without limitations; silence about the control construction's coverage cost; a further-research close with no agenda.

## Comparison prompt

Against `anton2025` (same literature, same instrument family — institution-merger-induced common ownership, opposite welfare valence): compare how the two front ends instruct the reader to feel about the identical shock — this card stages it as the device that reveals quiet coordination ("frenemies"), anton2025 as the device that can reveal technology internalization ("bright side") — and ask what each choice of dependent variable (advertising budget vs innovation output) lets the same merger shock prove, and which premise the reader must accept first in each story.
