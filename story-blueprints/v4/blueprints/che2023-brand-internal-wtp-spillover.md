# Story Learning Card — Che, Katayama, and Lee (2023, Journal of Marketing Research)

## Metadata

```yaml
schema_version: "4.0-lite"
id: che2023
paper:
  citekey: chekatayamalee2023
  title: "Product-Harm Crises and Spillover Effects: A Case Study of the Volkswagen Diesel Emissions Scandal in eBay Used Car Auction Markets"
  outlet: "Journal of Marketing Research"
  year: 2023
  publication_status: published
  paper_type: quantitative
  source_version: clipped_full_text
  inclusion_rationale: "A contrastive learning object for how a paper makes a highly specific crisis reveal brand-internal damage to products known to be unaffected, using willingness to pay as the consequence that closes the information-updating story."
reading_scope:
  sections_read: [abstract, introduction, background, methods, results, discussion]
  coverage: complete
  source_records:
    - "Product-Harm Crises and Spillover Effects A Case Study of the Volkswagen Diesel Emissions Scandal in eBay Used Car Auction Markets - Xiaogang Che, Hajime Katayama, Peter Lee, 2023.md"
    - "chekatayamalee2023-product-harm-crisis-spillover-ebay.md"
analysis_focus:
  primary: [introduction, background]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The article has no discrete theory section; the introduction carries the information-updating mechanism and the background establishes why Volkswagen's known violating and known nonviolating models form a sharp contrast."
mechanism_evidence:
  status: partly_probed
  basis: "The design identifies lower auction prices for known nonviolating Volkswagen models and finds little evidence of changed supply, entry, bidding, or reserve-price strategies; it does not directly measure buyers' quality expectations, disappointment, or dissatisfaction."
classification:
  theoretical_problem_form: [unresolved-brand-internal-consequence, crisis-as-quality-signal]
  narrative_dynamics: [specific-violation-to-brand-wide-demand-shock, unaffected-product-revaluation, information-isolation-failure, revealed-willingness-to-pay]
  retrieval_signals: [brand-internal-negative-spillover, unaffected-product-revaluation, quality-signal-to-willingness-to-pay]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Make spillover concrete by defining an unaffected target whose status is unambiguous, then ask why known noninvolvement does not insulate it from a brand-level information shock."
      - "Use an outcome with theoretical meaning—in this case willingness to pay—so the study asks how a crisis changes the value consumers assign to an unaffected product, not merely whether a price moves."
    caveat:
      - "The Volkswagen scandal's regulatory announcement, deliberate deception, and sharply identified violating models create an unusually clean focal-versus-unaffected contrast that cannot be assumed in ordinary recalls."
  theory:
    suitable: "partial"
    requires: []
    learn:
      - "Keep the middle mechanism compact: consumers cannot fully isolate products from brand-level information, so a crisis revises expected quality and resale value, lowering willingness to pay for nonviolators."
      - "Let contradictory prior findings create the need for a consequential setting and outcome, without pretending that the single case resolves all sources of heterogeneity in the literature."
    caveat:
      - "The article invokes quality updating, disappointment, and dissatisfaction as closely connected routes; it does not distinguish their individual theoretical roles."
  methods:
    suitable: "yes"
    requires: []
    learn:
      - "Match a crisis-as-demand-shock claim to an arena where the outcome has behavioral meaning: second-price auction prices allow the paper to treat final bids as revealed willingness to pay."
      - "Use auxiliary outcomes to rule out rival market-side accounts—supply, bidder entry, bids, and reserve choices—after establishing the focal price effect."
    caveat:
      - "The exogenous EPA announcement, auction format, and model-year/fuel classifications are evidence assets particular to this event, not a general recipe for studying product harm."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage the reveal around the counterintuitive target: prices decline not only for violating models but also for Volkswagen models that were not implicated, including gasoline cars."
      - "Use alternative market responses to sharpen the interpretation of the main outcome rather than adding disconnected robustness volume."
    caveat:
      - "The no-change auxiliary analyses make a demand-side account more plausible; they do not themselves observe the buyer beliefs that theory places in the middle."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Return to the initial isolation failure by making clear that a crisis-management loss calculation must include products whose physical quality did not change."
    caveat:
      - "Compensation and recovery recommendations are sensible extensions of the result but are not directly tested response strategies in the paper."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
```

## Story Reading

### Theme question

When a publicly identified Volkswagen emissions violation concerns only particular diesel models, why do consumers lower what they will pay for Volkswagen cars that they know were not implicated?

### Whole-story synopsis

The paper starts from an apparent containment premise: product-harm crises should damage the defective product, yet information about products under the same brand is difficult for consumers to isolate. Prior spillover findings are mixed, so the authors choose the Volkswagen emissions scandal because the EPA announcement both sharply identifies the violating 2009–2015 diesel models and leaves other Volkswagen cars clearly nonviolating. That distinction makes the central character unusually strong: a truly unaffected product. The middle story is a brand-quality updating process. The scandal can lower expectations about the quality and resale value of products carrying the Volkswagen name; disappointment and dissatisfaction then shift consumers' willingness to pay even when the target vehicle itself did not violate the standard. eBay's second-price used-car auctions turn that otherwise latent valuation into an observable final bid. Difference-in-differences analyses show price declines for nonviolating older diesel and gasoline Volkswagen cars, while auxiliary analyses show little corresponding change in bidder participation, bidding, supply, or reserve-price choices. The ending returns to the initial containment premise: the physical noninvolvement of a product does not prevent an economic loss when consumers treat the event as negative brand-level information.

### Characters and storylines

- **Initiating character:** the EPA's public disclosure of Volkswagen's defeat-device violation, because it is a highly salient, brand-diagnostic negative shock.
- **Counterintuitive target:** Volkswagen models not identified as violating emissions standards, because their unchanged physical quality makes brand-internal spillover visible rather than assumed.
- **Middle character:** consumers' brand-level quality and resale-value expectations, which carry information from the violating models to the nonviolating models.
- **Resolution-bearing character:** auction willingness to pay, revealed in final bids and therefore able to show whether the nonviolating target loses economic value.
- **Storyline 1:** scandal disclosure → revised expectation about Volkswagen quality/value → lower willingness to pay for nonviolating Volkswagen models.
- **Storyline 2:** if the outcome is a demand shock, price declines should not need a parallel change in seller supply, buyer entry, bidding behavior, or reserve-price setting.
- **Intersection:** the evidence changes a seemingly narrow violation into a brand-wide valuation problem while retaining a hard factual distinction between implicated and unimplicated products.

### Five acts

- **Exposition:** Product-harm crises harm affected products, but mixed prior evidence leaves unresolved whether unaffected products under the same brand also suffer.
- **Rising action:** The Volkswagen scandal supplies a rare contrast between identified violators and clearly nonviolating models; an information-isolation failure gives that contrast a demand-side mechanism.
- **Climax:** Difference-in-differences estimates show sharp price reductions for nonviolating older diesel Volkswagens and for Volkswagen gasoline cars following the scandal announcement.
- **Falling action:** Placebos, synthetic control, alternative comparison groups, and auction-side analyses make the price drop read as a lower-willingness-to-pay response rather than a supply or bidding artifact.
- **Denouement:** The conclusion recasts the loss from a product-specific scandal as a broader erosion of brand value that reaches products whose physical quality did not change.

### Tension

- **Source:** The announcement makes the violating models identifiable, so unaffected Volkswagen cars should be informationally separable; yet consumers may still treat the scandal as a signal about the brand that made them all.
- **Construction:** The paper preserves both sides by repeatedly naming the target models as nonviolators while using their subsequent auction valuation to test whether factual separation defeats brand-level inference.

### Alternative readings

- **author-signaled-alternative:** The paper considers price declines caused by supply, bidder entry, bidding strategy, and reserve-price changes, then treats their limited movement as support for a demand-side interpretation.
- **analyst_counterfactual:** The outcome could reflect a broad short-term Volkswagen stigma without a specific perceived-quality update. The design shows a brand-internal valuation loss, but does not directly separate disappointment, trust loss, and expected resale value as distinct psychological routes.

## Story Assessment

- **Theme coherence:** `works` — the same question about nonviolating products organizes the crisis, auction setting, main estimates, and closing implications.
- **Character discipline:** `works` — violating models, nonviolating targets, consumer valuation, and auction price have distinct and necessary roles.
- **Knot integrity:** `works` — the clear factual innocence of the target produces a genuine challenge to a product-specific view of harm.
- **Plot emergence:** `works` — the special event, price outcome, and auxiliary market responses all arise from the proposed brand-level demand shock.
- **Tie–unravel alignment:** `works` — the evidence directly tests the promised revaluation of known nonviolators and supplies a bounded calibration of competing market-side accounts.
- **Ending quality:** `partly_works` — the conclusion returns cleanly to brand-wide loss, though proposed compensation and recovery actions are not part of the empirical resolution.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification or research quality.

## Learning Affordances

### Introduction and Theory

Use this paper when a project has a genuinely unaffected target whose status makes an audience-level spillover surprising. The reusable action is to hold physical noninvolvement and economic vulnerability together, then supply a mechanism that connects them. It is not suitable where the supposedly unaffected object may itself share the defect or have ambiguous exposure.

### Methods and Results

The results matter because the auction price operationalizes the exact valuation shift promised at the front end, and auxiliary analyses narrow competing market responses. The empirical calibration is `partly_probed`: the paper demonstrates a brand-internal valuation loss and rules out several alternatives, but does not observe the quality-expectation mechanism directly.

### Discussion

The paper closes by broadening the managerial loss account from the implicated product to the brand portfolio. Transfer this move only when the evidence supports a shared brand signal; do not infer brand-wide spillover from a negative outcome at the focal product alone.

## Comparison prompt

Is the negative information being carried from one product to an unrelated but similar rival (Borah and Tellis), or from a product to another product that shares the very same brand identity (this paper)? Does the downstream outcome register public discussion, strategic response, or a buyer's valuation?
