# Story Learning Card — Fang et al. (2025, Production and Operations Management)

## Metadata

```yaml
schema_version: "4.0-lite"
id: fang2025
paper:
  citekey: fang_et_al_2025
  authors: "Sihan Fang, Vivek Astvansh, Siliang (Jack) Tong, Hsiao-Hui Lee, Yue Guo"
  title: "How Do Brands Change Their Advertising Spending in Response to a Rival's Product Recall?"
  outlet: "Production and Operations Management"
  year: 2025
  publication_status: published
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A bounded learning object for how a paper can make an observer's mixed opportunity-and-threat response visible by decomposing one aggregate action into strategically different components."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "fang_et_al_2025_rival_recall_ad_spend.pdm/fulltext.text-only.md"
    - "fang_et_al_2025_rival_recall_ad_spend.pdm/sections/{introduction.json, theory.yaml + theory.report.md, methods.json, results.json} (verified four-section distillations)"
  verification_note: "2026-08-29 gap-filling re-distill: all magnitudes, design facts, and robustness labels re-verified against the full text; no field relies on OCR-readback guesses"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The disaggregated advertising results and sales moderation receive extra attention because the paper's story depends on a total-spend response concealing opposed price- and quality-advertising moves."
classification:
  theoretical_problem_form: [mixed-horizontal-spillover-response, aggregate-action-hides-strategy-portfolio]
  narrative_dynamics: [opportunity-versus-threat-interpretation, decomposed-action-reversal, response-then-payoff, similarity-heterogeneity]
  retrieval_signals: [mixed-opportunity-threat, strategic-response-to-rival-event, action-decomposition, horizontal-spillover]
  confidence: reviewed
mechanism_evidence:
  status: partly_probed
  basis: "The unobservable opportunity/threat interpretation is proxied by the direction of ad-spending adjustment; the action decomposition (total −50%: price +25%, quality −71%, brand null) is estimated by RDiT, and the sales payoff (recall lifts substitute sales 35.3%; each RMB 10,000 unit of ad spending weakens that spillover by 23.1%, driven by quality advertising) is estimated via 2SLS with a New-Ad-Firms instrument (first-stage F 102.75–260.44 across columns). Managerial belief and buyer comparison are never directly observed."
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Open a competitive-response question with a real action that appears sensible, then expose the overlooked comparison risk that makes its effectiveness uncertain."
      - "State opportunity and threat as rival interpretations of the same external event before treating either a sales gain or an advertising change as the answer."
    caveat:
      - "The GM, Toyota, and Samsung episodes work because the observing brands are credible substitutes and recall makes quality comparison salient; a rival's bad news is not automatically a comparable consumer-evaluation trigger."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Use spillover theory to separate an observer's possible sales-preemption and harm-avoidance responses, then make a third quality-signaling action conditional on perceived similarity."
      - "Treat an aggregate action as a portfolio when its components can serve opposed strategic purposes; here price, quality, and brand advertising need not move together."
    caveat:
      - "Changes in advertising are behavioral proxies consistent with managers' opportunity or threat interpretations; they do not directly observe managerial belief, consumer comparison, or strategic intent."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "When a discrete rival event changes the decision environment abruptly, define the pre- and post-event windows (here 16 + 15 weeks around the Monday after the Friday announcement) and defend a no-control-group RDiT by stating the identification assumption and pre-empting local-nature objections with named reasons."
      - "Ground a vendor-algorithm construct (BERT-classified price/quality/brand ads) in a three-layer validity chain: classifier benchmark performance, double human-coder reliability, and human-machine agreement."
    caveat:
      - "The Sagitar RDiT design, Chinese prefecture-week print-advertising data (62 models from 33 manufacturers, 308 prefectures, 591,976 records), single-event timing assumption, and New-Ad-Firms instrument are setting-specific and do not establish general competitive strategy effects."
      - "The 2SLS/IV identification stack is not previewed in Methods (it first appears in Results Equations 3-4), and the standard-error clustering level is never reported."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Reveal the aggregate response first, then decompose it into components that expose the mixed strategy hidden by the net decrease; translate each coefficient into an explicit percent of the prerecall base (-50%, +25%, -71%, brand null)."
      - "Let the performance analysis close the same strategic puzzle by testing whether the action portfolio strengthens or weakens the recall's sales spillover (35.3% sales lift; each RMB 10,000 of ad spending weakens it by 23.1%, driven by quality advertising), and narrate nulls as evidence of strategy absence."
    caveat:
      - "A 50% average decline in total spending and its association with sales do not prove that lowering visibility caused consumer comparisons to change; the study's behavioral and interpretive layers remain distinct."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Return to the opening managerial action with a changed interpretation: advertising more may be counterproductive when it invites the very quality comparison a substitute seeks to avoid."
    caveat:
      - "The practical recommendation is bounded to substitutes in this market and recall context; it should not become a general rule to cut advertising after any competitor failure."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
```

## Story Reading

### Theme question

When a rival brand issues a product recall, do substitute brands treat the event as an opportunity to preempt sales or a threat of unfavorable comparison, and how does the resulting portfolio of advertising adjustments affect their sales spillover?

### Whole-story synopsis

The paper opens with GM's aggressive response to Toyota's recall and immediately makes the apparent opportunity unstable: some heavily advertised GM models used the same accelerator pedal, so visibility could invite rather than avoid quality comparison. This moves the focal actor from the recalling brand to an observing substitute brand. Spillover theory offers two opposed interpretations: a recall can free sales for substitutes or contaminate evaluations of related products. Advertising becomes the observable response, but the paper refuses to treat it as one action. Price advertising can preempt sales, quality advertising can signal superiority or trigger an unfavorable comparison, and brand advertising can manage broader image exposure. The Sagitar recall supplies a time discontinuity: Volkswagen's October 17, 2014 recall of 563,605 New Sagitar cars (China's largest auto recall of 2014, about 11.3% of all cars recalled that year) is observed through 62 substitute A-class models from 33 manufacturers across 308 Chinese prefectures over 31 weeks — 591,976 model-week-prefecture print-ad records. Total advertising falls by half, suggesting threat dominates in the aggregate, but decomposition reveals a portfolio: price advertising rises, quality advertising falls sharply, and brand advertising does not change. A sales analysis then shows positive competitive spillover from the recall (substitute sales lift of 35.3%), while more total advertising weakens that sales lift (each RMB 10,000 unit weakens the main effect by 23.1%); the weakening is driven by quality advertising. Similarity changes the response: direct substitutes cut price and quality advertising further, whereas sibling substitutes raise quality advertising. Five robustness tests (alternate prerecall window, augmented local linear, negative-binomial alternate estimator, falsification, alternate media traces) and a Cadillac SRX recall replication in the same market support the pattern. The Discussion returns to the opening irony: visible quality promotion can undermine a substitute's effort to benefit from a rival's recall.

### Characters and storylines

- **Main character:** the substitute brand manager's advertising portfolio, because it translates an unobserved spillover interpretation into differentiated actions.
- **Trigger character:** a rival product recall, which can generate positive competitive sales substitution and negative contagion through consumer comparison.
- **Action characters:** price advertising supports sales preemption; quality advertising can signal superiority or raise risky comparisons; brand advertising tests broader harm avoidance.
- **Outcome character:** substitute sales volume, which determines whether the action portfolio preserves or weakens positive spillover.
- **Similarity characters:** direct substitute status changes consideration-set closeness, while sibling status changes common-manufacturer association.
- **Storyline 1:** substitutes can capitalize on a rival's sales loss through price-oriented advertising.
- **Storyline 2:** substitutes can avoid quality-oriented visibility when comparison with a recalled model may contaminate their evaluation.
- **Intersection:** the same substitute can pursue preemption and avoidance at once, so total advertising hides a strategically mixed response.

### Five acts

- **Exposition:** GM's response to Toyota shows why a rival recall may create both an invitation to compete and a danger of shared-quality association.
- **Rising action:** Spillover theory frames opportunity, threat, and their cancellation; price, quality, and brand advertising convert the possible interpretations into separable response actions.
- **Climax:** Following Sagitar's recall, substitutes reduce total advertising by 50%, indicating a net threat-oriented response.
- **Falling action:** The aggregate decline decomposes into higher price advertising (+25%), sharply lower quality advertising (−71%), and unchanged brand advertising. Sales rise after the recall (+35.3%), but advertising weakens that positive spillover (−23.1% per RMB 10,000, driven by quality advertising); direct and sibling substitutes show different portfolios.
- **Denouement:** The paper returns to the opening practice and recasts aggressive advertising as potentially counterproductive when it makes a substitute more visibly comparable to the recalled product.

### Tension

- **Source:** A rival's recall can release demand for substitute brands while simultaneously making product quality comparison more salient and therefore more dangerous.
- **Construction:** The paper turns that ambiguity into opposed advertising components rather than forcing a single prediction about total advertising or treating sales gains as proof that managers perceive only opportunity.

### Alternative readings

- **author-signaled-alternative:** Advertising reductions may reflect managerial threat interpretation, but they may also follow contemporaneous market conditions or a different communications strategy. The discontinuity, falsification, alternate media measures, and second recall improve the case for an event-related response without observing beliefs or buyer utility directly.

## Story Assessment

- **Theme coherence:** `works` — the hook, spillover ambiguity, advertising portfolio, sales payoff, similarity analyses, and ending all concern substitute response to a rival recall.
- **Character discipline:** `works` — price, quality, and brand advertising have distinct strategic roles, and direct versus sibling similarity changes a different comparison relationship.
- **Knot integrity:** `works` — opportunity and threat create a genuine ambiguity that a total-spending measure cannot resolve by itself.
- **Plot emergence:** `works` — the action decomposition and sales moderation arise naturally from the claim that competing interpretations can coexist in one response.
- **Tie–unravel alignment:** `partly_works` — the evidence supports the stated advertising and sales patterns, but manager interpretation, buyer comparison, and the causal effect of advertising on sales remain inferred rather than directly observed.
- **Ending quality:** `works` — the ending clearly transforms the GM opening: more advertising may weaken, not capture, competitive benefit when quality comparison is salient.
- **Imperfect-paper signals (cross-section consistency check, 2026-08-29):** learning signals from the paper's own seams, not narrative errors to delete.
    - **C1 — informal predictions:** the Theory section carries zero numbered hypotheses; the H1-H3-style predictions are three-way response directions (raise/lower/hold) produced by a proxy-bridging argument and a conceptual-framework figure. Competing predictions can be adjudicated without formal Hs, but this is a POM convention, not a transferable rule for AMJ/SMJ submissions.
    - **C2 — identification stack deferred:** the IV/2SLS endogenous-moderator identification is not previewed in Methods; it first appears in Results (Equations 3-4), with weak-instrument F-statistics (102.75-260.44) embedded per column of Table 4. The story stays readable, but the design's IV layer is revealed only mid-Results.
    - **C4 — undiscussed robustness contradiction:** the narrative treats brand advertising as unchanged (null as evidence of no harm-avoidance strategy), yet Table 8's augmented-local-linear robustness shows Brand Ad significantly positive (coefficient 0.000***, SE 4.62e-07), undiscussed. A robustness table can silently undercut a narratively load-bearing null; writers should reconcile or flag such conflicts rather than inherit them.
- **Boundary:** This evaluates storytelling only; it is not a judgment about the RDiT design, advertising causal effects, or research quality.

## Learning Affordances

### Introduction and Theory

This card is useful when one external event plausibly presents a single actor with opposed opportunity and threat interpretations and those interpretations imply different observable actions. It is not a generic way to call any mixed coefficient a strategic portfolio.

### Methods and Results

The card's strongest lesson is action decomposition: if an aggregate measure combines components with different strategic meanings, stage the aggregate result then reveal the components and test their shared payoff. It does not establish inner motives merely because component choices match a theory.

### Discussion

The ending is useful for returning to an opening practice with a conditional reversal. Its implication must remain tied to the comparison process and market context that made visibility harmful.

## Comparison prompt

Compared with Li, is the exposed firm a horizontal substitute facing consumer categorization or a vertically tied supplier facing operational and evaluative transmission? Compared with Singh, does media-related attention constrain political influence over recall decisions, or do buyers' comparisons constrain a rival's marketing response after the recall?
