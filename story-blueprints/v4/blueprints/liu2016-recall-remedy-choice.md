# Story Learning Card — Liu, Liu & Luo (2016, Journal of Marketing)

## Metadata

```yaml
schema_version: "4.0-lite"
id: liu2016
paper:
  citekey: liuliuluo2016
  title: "What Drives a Firm's Choice of Product Recall Remedy? The Impact of Remedy Cost, Product Hazard, and the CEO"
  outlet: "Journal of Marketing"
  year: 2016
  publication_status: published
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A bounded learning object for separating recall remedy from recall timing and for organizing a response choice around a real cost–harm trade-off whose weights are conditioned by executive incentives."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "What Drives a Firm’s Choice of Product Recall.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The remedy classification and interaction results receive extra attention because the paper's payoff depends on distinguishing an after-recall compensation decision from initiation timing, and on CEO incentives changing the weight assigned to cost and harm."
classification:
  theoretical_problem_form: [underexamined-response-choice, competing-decision-criteria]
  narrative_dynamics: [cost-versus-harm-trade-off, executive-incentive-reweighting, response-choice-to-valuation]
  retrieval_signals: [remedy-cost-versus-consumer-harm, executive-incentives-in-response-choice, full-versus-partial-remediation, post-recall-decision]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Separate adjacent response decisions before theorizing: recall initiation and timing answer whether or when to act, whereas remedy asks how fully affected customers are made whole after a recall occurs."
      - "Open a response-choice question with two criteria that genuinely pull in opposite directions for the decision maker, rather than equating a more generous response with a costless best practice."
    caveat:
      - "The full-versus-partial remedy distinction belongs to CPSC consumer-product practice; a new setting needs an equivalent decision margin with meaningfully different consumer restoration and firm-cost implications."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Give each side of a response trade-off a separate causal role: product value raises the immediate cost of full remedy, while product hazard raises consumer harm, regulatory pressure, and the need for credible protection."
      - "Use executive incentives as reweighting conditions on the existing criteria, not as a detached direct-effect list; cash and equity incentives predict opposite changes in how cost and harm enter remedy choice."
    caveat:
      - "Cash compensation, equity sensitivity, and tenure are proxies for incentives, power, and temporal orientation; they do not observe a CEO's motives, private information, or direct intervention in a remedy decision."
      - "Do not infer that any compensation component is inherently ethical or unethical outside the specified short- versus long-horizon response trade-off."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Align the outcome with the proposed choice by coding full refund/replacement separately from partial repair, self-repair, or discount remedies, then estimate the criterion-by-incentive interactions on that choice."
    caveat:
      - "The 170 NYSE CPSC recalls, binary remedy aggregation, compensation measures, probit model, and instruments are setting-specific; the binary coding cannot resolve differences among partial remedies."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage a decision-trade-off result in order: establish the cost and harm main effects, reveal the direct incentive associations, then show which incentives actually reweight each criterion."
      - "Use a downstream valuation analysis as a contrastive consequence only after the remedy choice is established, and distinguish a selection-adjusted association from proof of investor interpretation."
    caveat:
      - "The event-study result that full remedy has lower CAR can reflect remedy selection or severity not fully captured by controls; it does not prove that investors infer a specific hidden crisis state."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Return to the decision criteria by explaining why governance can change the balance between immediate accounting burden and consumer protection, while retaining the operational category on which the evidence rests."
    caveat:
      - "The ethical and policy prescriptions are stronger than the observed compensation–remedy associations; do not convert proxy-based evidence into a claim of confirmed CEO self-interest."
      - "Discussion recycles cost–harm and CEO main effects but does not return to the tenure-interaction null; learn the Results spillover-null sentence, not the Discussion omission."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
  l2_flags_fed: true
  l2_notes:
    - "C2 info: main estimator is event-level probit; Results adds IV+control-function and Heckman-on-CAR as falling action, not a family mismatch."
    - "C4 info: Intro promises (cost–harm, CEO main effects, financial-interest moderation) are delivered. H7/H8 tenure interactions are a Theory subplot, reported as do not support; Discussion does not recycle that null."
```

## Story Reading

### Theme question

Once a product is recalled, what determines whether a firm provides a full rather than partial consumer remedy, and how do CEO incentives alter the balance between remedy cost and consumer harm?

### Whole-story synopsis

The paper begins by separating a neglected response decision from the better-known question of recall timing. A recall remedy is what the firm offers affected consumers after the event: full refund or replacement versus repair, self-repair kit, or a future-purchase discount. This distinction gives the paper a concrete choice whose two criteria conflict. Full remedy is more costly in immediate expense and uptake, especially when the recalled product value is high; it is also more responsive to consumer harm, regulatory scrutiny, trust restoration, and long-run value. CEO compensation and tenure enter not as a separate collection of correlates but as conditions that can change how those two criteria are weighted. Higher cash compensation and longer tenure are theorized to favor short-term earnings or entrenchment; equity incentive should privilege long-run value. A CPSC/NYSE sample finds lower full-remedy likelihood for higher product value, higher likelihood for greater hazard, lower likelihood with CEO cash pay and tenure, and higher likelihood with equity incentive. Cash and equity also change the cost and hazard effects in opposite directions, whereas tenure does not moderate them. A selection-adjusted event study then finds lower short-window market returns for full remedy, reintroducing the consumer–investor contrast. The Discussion returns to remedy as a consumer-welfare and governance decision, but the data observe compensation, remedy category, and CAR—not CEO intent, consumer trust, or the presumed long-run benefit of full remedy.

### Characters and storylines

- **Main character:** full versus partial recall remedy, because it is the after-recall compensation decision that the paper distinguishes from whether or when to recall.
- **Criterion characters:** product value represents the immediate cost of full remedy; product hazard represents consumer harm and pressure for more complete protection.
- **Governance characters:** CEO cash compensation, equity incentive, and tenure, which are proposed to shift the decision weight given to cost and harm.
- **Consequence character:** announcement-window stock return, which adds a different external valuation of full remedy after the primary choice analysis.
- **Storyline 1:** high remedy cost discourages full remedy while severe hazard encourages it.
- **Storyline 2:** cash and equity incentives respectively strengthen and weaken the cost-oriented tendency, and respectively weaken and strengthen the hazard-oriented tendency.
- **Intersection:** CEO conditions reshape an existing cost–harm choice rather than creating an unrelated governance outcome; tenure's direct effect does not extend to the two criterion interactions.

### Five acts

- **Exposition:** Recall research has emphasized event effects and timing, leaving the level of consumer remedy after a recall underexamined.
- **Rising action:** Full versus partial remedy establishes the cost–harm trade-off; CEO incentives and tenure are introduced as potential reweighting conditions.
- **Climax:** Probit results show the predicted product-value, hazard, cash, equity, and tenure associations with full remedy.
- **Falling action:** Cash and equity incentives moderate both decision criteria in opposite directions; tenure interactions fail; selection-adjusted event-study evidence shows lower CAR for full remedy.
- **Denouement:** The Discussion reframes consumer remedy as a governance and welfare choice, while acknowledging the coarse partial-remedy category.

### Tension

- **Source:** A full remedy creates an immediate firm expense but better protects customers and may support longer-run trust; executive incentives may make the same cost and harm information carry different weight.
- **Construction:** The paper makes the tension operational through an explicit remedy choice and tests interactions that attach incentives to the two decision criteria.

### Alternative readings

- **author-signaled-alternative:** The paper notes that partial remedies contain heterogeneous actions and that some results weaken when they are modeled separately; its strongest claims concern full versus partial remedy, not a fine-grained remedy continuum.
- **analyst_counterfactual:** The CEO-pay associations could reflect unobserved firm governance, crisis severity, or consumer composition rather than CEOs acting from private self-interest. The design addresses compensation endogeneity with instruments but does not observe deliberation or motive.

## Story Assessment

- **Theme coherence:** `works` — remedy choice, cost, harm, CEO conditions, interactions, and the policy ending address the same post-recall decision.
- **Character discipline:** `works` — the paper clearly distinguishes response criteria, incentive conditions, and downstream valuation.
- **Knot integrity:** `works` — full remedy's immediate cost and consumer-protection value form a real decision conflict, not merely a neglected variable.
- **Plot emergence:** `works` — the interaction tests follow naturally from the claim that incentives reweight cost and harm.
- **Tie–unravel alignment:** `partly_works` — the remedy and interaction predictions are directly tested, but CEO motives, customer trust, and long-run value are inferred from proxies and prior literature.
- **Ending quality:** `partly_works` — it returns to welfare and governance but casts proxy-based associations too readily as CEO private-interest behavior and policy prescriptions.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, remedy regulation, CEO ethics, or research quality.

## Learning Affordances

### Introduction and Theory

This is useful when a project has a real post-event response choice with opposing criteria and a theoretically justified actor condition that changes their weighting. It is not a generic way to add executive moderators after a cost-benefit prediction.

### Methods and Results

The card's main value is the interaction architecture: measure the actual choice, establish the two criteria, then test whether an incentive changes each criterion's effect. Downstream CAR is a separate evaluative arena, not a substitute for observing customer restoration or CEO mechanism.

### Discussion

Use the ending as a reminder that consumer welfare, short-term firm cost, and market reaction need not align. Do not label managers unethical or incentives corrective without direct evidence of their decision process and longer-run effects.

## Comparison prompt

Compared with Chen 2009, does a study ask how a recall is announced and signaled, or how consumers are remedied after it? Compared with Darby 2024 and Malik 2025, do executive incentives change post-awareness timing, public handling, or the cost–harm weighting of a concrete remediation choice?
