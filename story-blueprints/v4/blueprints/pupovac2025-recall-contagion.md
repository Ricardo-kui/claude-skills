# Story Learning Card — Pupovac et al. (2025, Production and Operations Management)

## Metadata

```yaml
schema_version: "4.0-lite"
id: pupovac2025
paper:
  citekey: null
  title: "Product Recall Contagion in the Supply Chain"
  outlet: "Production and Operations Management"
  year: 2025
  publication_status: accepted_manuscript
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A contrastive vertical-spillover case in which a supplier's prior customer disclosure changes the market interpretation of a buyer's recall, without claiming that the supplier caused the defect."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "Pupovac 等 - 2025 - PRODUCT RECALL CONTAGION in the SUPPLY CHAIN.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The two-stage-screen claim receives extra attention because voluntary disclosure is tested in the full sample whereas revenue dependence is observed only in a selected subsample; shareholder screening and supplier demand loss are not observed directly."
classification:
  theoretical_problem_form: [vertical-spillover, information-screening-under-uncertainty]
  narrative_dynamics: [realized-shock-to-nontarget-value-loss, disclosure-paradox, two-stage-screening]
  retrieval_signals: [vertical-spillover, customer-disclosure-under-uncertainty, revenue-dependence-exposure, external-evaluation-of-supply-chain-risk]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Define an indirectly exposed actor before theorizing contagion, then state what the focal shock could change for that actor even though it did not cause the event."
      - "Turn an unavailable ideal datum into a theory question by distinguishing broad transparency from the more diagnostic information that only some firms reveal."
    caveat:
      - "A buyer's negative event alone does not establish supplier exposure; the project needs a credible contractual or revenue relationship and a reason an external evaluator would care."
  theory:
    suitable: "partial"
    requires: []
    learn:
      - "Use information asymmetry to explain why general disclosure can reduce uncertainty while a disclosed dependence measure can reveal concentrated exposure and worsen valuation."
      - "Keep the two screening stages analytically distinct: transparency is a broad cue, whereas revenue dependence is a specific exposure cue available only after disclosure."
    caveat:
      - "The paper does not observe shareholders screening sequentially, their perceived demand uncertainty, supplier demand, or future cash flow; two-stage screening is an interpretation of differential associations."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Match a vertical-contagion question to linked buyer–supplier dyads and a public shock, then make disclosure selection visible rather than treating missing dependence data as random."
    caveat:
      - "The 896 dyads, large-automobile-recall threshold, event windows, control-function instrument, and selected 223-observation dependence subsample are setting-specific and do not identify physical disruption."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Reveal the supplier loss first, then show the disclosure paradox: broad customer disclosure attenuates loss while disclosed dependence on the recalling customer aggravates it."
      - "Use contextual severity cues after the main screen results to show which event attributes external evaluators may use when firm-specific exposure is uncertain."
    caveat:
      - "The asymmetry across full-sample and selected-subsample regressions supports the conceptual distinction but cannot prove a single investor's two-step processing sequence."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Return to a disclosure dilemma by stating the condition under which transparency may relieve ambiguity versus reveal harmful concentration, rather than treating disclosure as uniformly protective."
    caveat:
      - "The post hoc 21% disclosure threshold is exploratory and cannot be used as a general managerial rule without independent confirmation."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
```

## Story Reading

### Theme question

When a manufacturer announces a large recall, why do its suppliers lose shareholder value, and how can prior customer disclosure both reduce uncertainty and expose damaging revenue dependence?

### Whole-story synopsis

The paper opens with manufacturer–supplier interdependence: a buyer's recall can reduce expected demand for a supplier's components even when the supplier is not accused of causing the defect. The supplier's market loss is framed as vertical contagion. Screening theory then gives the story its distinctive mechanism: shareholders face uncertainty about supplier demand because they usually cannot see the supplier's customer portfolio. Revenue dependence on the recalling manufacturer would be the ideal diagnostic screen, but it is often undisclosed. The paper proposes a two-stage substitute. First, shareholders use voluntary customer disclosure as a broad transparency cue; second, among suppliers revealing the relevant customer, they use revenue dependence as a precise exposure cue. The empirical arena links 896 public automotive manufacturer–supplier dyads to large recalls and finds negative supplier abnormal returns. Prior voluntary customer disclosure predicts a less punitive reaction, while disclosed revenue dependence predicts a more punitive reaction in the selected subsample. Recall size, news volume, sentiment, and software defect type further differentiate reactions. The Discussion closes with disclosure's double edge: transparency can reveal alternatives, but it can also reveal how much demand is at risk. The result is a compelling information interpretation of vertical spillover, but neither shareholder screening, supplier demand, nor cash-flow loss is observed directly.

### Characters and storylines

- **Main character:** the supplier exposed to its manufacturer's recall, because the supplier is the indirect victim whose market value is evaluated.
- **Shock character:** a large manufacturer recall, which creates a realized buyer-side event rather than a threat of future monitoring.
- **Screen characters:** voluntary customer disclosure as a broad transparency cue and revenue dependence as a specific exposure cue.
- **Hidden-state character:** future demand uncertainty for the supplier, proposed as the reason shareholders revalue the supplier but not measured.
- **Storyline 1:** a buyer recall creates expected supplier demand risk and negative supplier CAR.
- **Storyline 2:** broad disclosure can reduce ambiguity by signaling an observable customer portfolio, while specific dependence identifies concentrated risk and aggravates the reaction.
- **Intersection:** the same disclosure domain produces opposing implications because general transparency and dependence answer different uncertainty questions.

### Five acts

- **Exposition:** Buyer recalls may spread value loss to linked suppliers, a vertical exposure distinct from competitor spillover.
- **Rising action:** Information asymmetry makes revenue dependence the ideal but often unavailable screen; two-stage screening organizes broad disclosure and specific dependence.
- **Climax:** Event studies show significant supplier value loss around large manufacturer recalls.
- **Falling action:** Disclosure attenuates loss in the full sample; dependence aggravates it in the disclosure-selected subsample; contextual recall cues refine the result.
- **Denouement:** The Discussion makes customer disclosure a conditional risk-management dilemma while acknowledging evidence is limited to US automotive market reactions.

### Tension

- **Source:** The same information practice can reassure outsiders that a supplier has alternatives or reveal that the supplier is highly exposed to a failing customer.
- **Construction:** The paper does not treat disclosure as uniformly good or bad; it separates general portfolio visibility from customer-specific revenue concentration.

### Alternative readings

- **analyst_counterfactual:** The observed supplier CAR could reflect a common reassessment of automobile-industry demand or unobserved supplier quality exposure rather than shareholders' demand-uncertainty screening. The study's controls and selection adjustments narrow, but do not observe, this alternative.

## Story Assessment

- **Theme coherence:** `works` — vertical loss, information asymmetry, disclosure, dependence, and the ending's transparency dilemma remain connected.
- **Character discipline:** `works` — broad disclosure and specific dependence have distinct informational roles rather than acting as interchangeable transparency measures.
- **Knot integrity:** `works` — vertical supply-chain exposure plus unavailable customer information creates a genuine uncertainty problem.
- **Plot emergence:** `works` — the dyad event study and selected dependence analysis follow from the stated availability of the two screens.
- **Tie–unravel alignment:** `partly_works` — supplier CAR and disclosure/dependence associations are tested, but the proposed sequential screening and demand uncertainty are not directly observed.
- **Ending quality:** `partly_works` — it returns well to disclosure's double edge, though the prescriptive threshold and mitigation claims go beyond the observed associations.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, disclosure law, or research quality.

## Learning Affordances

### Introduction and Theory

Use this card when an indirect shock exposes an actor through a relationship and a missing information problem gives a public cue its meaning. The transferable move is the distinction between broad transparency and a diagnostic exposure measure—not the claim that every disclosure generates two-stage screening.

### Methods and Results

The card illustrates how sample availability itself can be theory-relevant: the ideal dependence measure is available only for disclosing suppliers. Selection correction does not transform the two samples into direct evidence of investor cognition, so report the mechanism as a bounded interpretation.

### Discussion

The ending is useful when a policy or disclosure lever has genuine opposing implications. It should not turn a post hoc cut point into an operational rule.

## Comparison prompt

Compared with Li 2026, is supplier loss theorized through network pipes and prisms or through shareholder screening of customer information? What is actually observed—cash-flow and impression traces, or disclosure and dependence cues—and what remains an explanation of investor interpretation?
