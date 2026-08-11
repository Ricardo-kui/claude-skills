# Story Learning Card — Mukherjee and Sinha (2018, Production and Operations Management)

## Metadata

```yaml
schema_version: "4.0-lite"
id: mukherjee2018
paper:
  citekey: null
  title: "Product Recall Decisions in Medical Device Supply Chains: A Big Data Analytic Approach to Evaluating Judgment Bias"
  outlet: "Production and Operations Management"
  year: 2018
  publication_status: published
  paper_type: quantitative
  source_version: publisher_pdf
  inclusion_rationale: "A bounded learning object for converting a vague timely-recall problem into a signal-detection account that distinguishes under-reaction from over-reaction and separates signal properties from the organizational context of attention."
reading_scope:
  sections_read: [abstract, introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "Production Oper Manag - 2017 - Mukherjee - P-OvisOCR2-20260811-151633.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The theory and design are read together because the signal-detection definition of judgment bias dictates the predictive-model construction used to create the empirical outcome."
mechanism_evidence:
  status: partly_probed
  basis: "The study constructs device-level false-alarm and miss rates from a high-performing recall-prediction model and finds the predicted associations of signal noise, severity, firm size, and portfolio scope with the resulting bias measure; it does not observe managers' thresholds, attention allocation, perceived error costs, or deliberation."
classification:
  theoretical_problem_form: [decision-calibration-under-uncertain-signals, error-type-asymmetry]
  narrative_dynamics: [adverse-event-stream-to-recall-threshold, underreaction-overreaction-map, signal-and-attention-sources-of-bias, predictive-model-to-normative-deviation]
  retrieval_signals: [signal-detection-recall-decision, user-feedback-noise, managerial-attention-allocation, underreaction-overreaction-recall-bias]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Turn a broad call for timely action into a two-error decision problem by distinguishing failure to act on a credible signal from premature action on an inadequate signal, and state the avoidable harm attached to each."
      - "Use the availability of fine-grained feedback data as an evidence opportunity only after specifying the managerial judgment it can illuminate, rather than treating data scale as the contribution itself."
    caveat:
      - "This framing requires a real action threshold and meaningful false-alarm and miss possibilities; it cannot be transferred to outcomes where a delayed or early response is merely a different preference rather than a decision error."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Use signal detection to make the theoretical middle operational: a recall threshold trades off miss and false-alarm costs, so under- and over-reaction are opposite deviations from a calibrated decision rather than opposite average outcomes."
      - "Separate the two source families before generating hypotheses: properties of the adverse-event signal shape detectability, while firm size and portfolio scope shape how much managerial attention a focal signal receives."
    caveat:
      - "Signal detection supplies a normative comparator only when the relevant error costs and a defensible reference threshold are meaningful; it does not establish that an observed recall decision was cognitively biased without such a benchmark."
  methods:
    suitable: "yes"
    requires: []
    learn:
      - "When the theoretical outcome is an unobserved decision error, first build and validate a prediction model for the underlying event, then use its false-alarm and miss implications to construct the error-type measure before estimating its sources."
      - "Keep measurement levels visible: user reports and signal characteristics sit at the device level, whereas attention context sits at the firm level, which justifies a hierarchical model rather than a single undifferentiated regression."
    caveat:
      - "MAUDE text, FDA recall labels, LDA preprocessing, random-forest predictions, train/test splits, and product-code fixed effects make the error measure contingent on data quality and model specification; predicted recall need is not an observed managerial threshold."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Reveal the empirical distribution of under- versus over-reaction before explaining its sources, so the reader sees why a single recall-rate outcome would conceal the decision problem."
      - "Use the noise-by-severity interaction to revise a simple main-effect account: noisy feedback generally accompanies under-reaction, but at high severity the same condition is associated with precautionary over-reaction."
    caveat:
      - "The reported associations show patterns in a constructed bias measure; they do not demonstrate that managers consciously changed thresholds because they perceived noise, severity, or portfolio complexity."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Close a decision-calibration story by returning to how prospective surveillance can reduce both error types, while preserving the distinct operational implications of noisy signals and highly severe signals."
    caveat:
      - "The regulatory and managerial prescription assumes that better analytics can improve threshold calibration; the study does not evaluate an intervention that changes firm decisions or patient outcomes."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
```

## Story Reading

### Theme question

When firms receive a continuous, noisy stream of user reports about adverse medical-device events, do their recall decisions systematically err through under-reaction or over-reaction, and which signal and attention conditions are associated with each direction of bias?

### Whole-story synopsis

The paper begins with an urgent operational problem: a medical-device recall can prevent serious harm, but firms and regulators often react too late or too readily to accumulating adverse-event reports. The authors refuse to equate timely recall with simply more recalls. Signal detection theory gives the story a decision threshold: a firm can miss a credible recall signal or create a false alarm, and either error can be costly. System neglect then explains why noisy feedback obscures a signal and should be associated with under-reaction, while severe adverse events raise the perceived cost of a miss and should be associated with over-reaction. Managerial-attention theory supplies the organizational middle: large firms and broad, deep portfolios distribute attention across more issues, reducing the salience of a focal device signal and thereby favoring under-reaction. The design first mines MAUDE reports and related FDA, firm, and product data to construct a recall-prediction model. It uses the model's device-level false-alarm and miss implications to form a relative judgment-bias measure, then estimates how signal and firm contexts relate to that outcome. The results show a predominance of under-reaction, more under-reaction with high noise-to-signal ratios, more over-reaction with high severity, an important interaction in which high severity changes the noisy-signal pattern, and more under-reaction in larger and less focused firms. The conclusion returns to evidence-based post-market surveillance: predictive analytics may make recall detection more calibrated, but the evidence has mapped inferred error patterns rather than observed managerial cognition or an intervention's effects.

### Characters and storylines

- **Focal decision character:** the manufacturer or regulator's recall threshold, because it determines whether an adverse-event stream triggers recall action.
- **Error characters:** miss/under-reaction and false alarm/over-reaction, because the paper treats them as distinct deviations with different patient, operational, and economic costs.
- **Signal characters:** adverse-event noise-to-signal ratio and severity, because they change signal detectability and the perceived cost of missing a potentially dangerous problem.
- **Attention-context characters:** firm size and product-portfolio depth and breadth, because they distribute attention over issues and reduce a focal device signal's relative salience.
- **Measurement character:** the recall-prediction model, because it translates observed user reports and recall records into the false-alarm and miss rates required to estimate bias.
- **Storyline 1:** noisier user feedback → impaired detection → higher under-reaction likelihood.
- **Storyline 2:** severe adverse events → higher perceived miss cost and precaution → higher over-reaction likelihood.
- **Storyline 3:** larger or less focused organizations → more distributed attention → higher under-reaction likelihood.
- **Intersection:** the same adverse-event stream is not self-interpreting; signal properties and organizational attention jointly determine which of two decision errors becomes more likely.

### Five acts

- **Exposition:** Product recalls can disrupt supply chains and endanger patients, yet user feedback is often met with either avoidable delay or excessive precaution.
- **Rising action:** Signal detection defines the recall threshold and two error types; system neglect predicts the role of noise and severity, while attention theory adds firm size and portfolio scope as contextual sources of bias.
- **Climax:** The constructed bias measure shows under-reaction is more prevalent; noisy signals associate with under-reaction and severe events with over-reaction, with severity altering the noisy-signal relationship.
- **Falling action:** Larger firms and broader/deeper portfolios associate with under-reaction; device usage, age, growth activity, and competition refine the map, while categorical-bias models support the main patterns.
- **Denouement:** The paper recasts post-market surveillance as a calibration problem for firms and regulators, proposing more evidence-based and predictive recall detection without claiming to have observed or changed decision routines.

### Tension

- **Source:** The same protective recall system can fail by missing dangerous defects or by acting on insufficient evidence; a metric that counts recalls alone cannot distinguish these failures.
- **Construction:** The paper makes the trade-off concrete by locating both errors around one threshold and by pairing signal quality with the organizational attention context that shapes its practical use.

### Alternative readings

- **author-signaled-alternative:** The authors note that the situated context of recall decision makers can include temporal factors such as profitability, demand/supply conditions, and organizational changes, but retain firm size and portfolio scope as relatively stable attention contexts.
- **analyst_counterfactual:** The constructed false-alarm and miss rates may partly reflect how the prediction model, FDA labels, and reference threshold classify recall need rather than managers' actual cognitive bias. Validation supports predictive accuracy but does not observe deliberation or the counterfactual correct decision.

## Story Assessment

- **Theme coherence:** `works` — the threshold and two-error framing connects the initial stakes, hypotheses, predictive construction, source estimates, and surveillance conclusion.
- **Character discipline:** `works` — signal features, attention context, and measurement apparatus have differentiated roles in explaining a common decision-bias outcome.
- **Knot integrity:** `works` — early and late recall can create different harms, so the study has a genuine calibration problem rather than a generic call for more responsiveness.
- **Plot emergence:** `works` — the prediction model is necessary to construct the error measure specified by the theory, and the multilevel analysis follows the device- and firm-level mechanisms.
- **Tie–unravel alignment:** `partly_works` — the data support the predicted associations with a constructed bias outcome, but the counterfactual threshold, perceived costs, and managerial attention process remain inferred.
- **Ending quality:** `partly_works` — the conclusion returns effectively to evidence-based surveillance, while its implication that analytics will correct decision bias exceeds the study's nonintervention evidence.
- **Boundary:** This evaluates storytelling, not the validity of the prediction model, causal identification, medical-device regulation, or research quality.

## Learning Affordances

### Introduction and Theory

Use this card when a decision genuinely has two asymmetric errors around a defensible action threshold, and when the theoretical task is to explain which conditions move error direction rather than only the likelihood of action. It is not a generic way to label opposite signs, faster/slower behavior, or any classification error as managerial bias.

### Methods, Results, and Discussion

The card shows how an auxiliary predictive model can be a measurement bridge for an otherwise latent decision-error construct, and how the results can preserve both under- and over-reaction. Its empirical calibration is `partly_probed`: the paper estimates inferred error patterns, not decision makers' attention, thresholds, error costs, or response to an analytic intervention.

## Comparison prompt

Does the study evaluate calibration before an adverse-event signal becomes a recall decision (`mukherjee2018`), or the financial and recurrence consequences after a medical-device recall has occurred (`thirumalai2011`)? Which time point and actor make the focal outcome meaningful?
