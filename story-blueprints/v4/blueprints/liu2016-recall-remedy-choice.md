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
  source_version: "parsed_full_text (typesetting-repaired re-read 2026-09-23; OCR splicing damage fixed, citation checks run against the PDM text-only slices, not cached impressions)"
  inclusion_rationale: "A bounded learning object for separating recall remedy from recall timing and for organizing a response choice around a real cost–harm trade-off whose weights are conditioned by executive incentives."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "00 工作台/项目/Reference for Recalls/Liu等-2016-What Drives a Firm’s Choice of Product Recall Remedy The Impact of Remedy Cost, Product Hazard, and the CEO.md"
    - "C:\\Users\\admin\\.claude\\distill-work\\liuliuluo2016.pdm\\sections\\ (introduction/theory/methods/results .md slices + discussion slice; re-typeset 2026-09-23)"
mechanism_evidence:
  status: partly_probed
  basis: "The reweighting interactions (incentives x cost, incentives x hazard) are directly estimated on the observed choice, and the endogeneity of compensation is addressed; but the incentive-to-decision process itself is proxied by compensation/tenure measures and never observed."
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The remedy classification and interaction results receive extra attention because the paper's payoff depends on distinguishing an after-recall compensation decision from initiation timing, and on CEO incentives changing the weight assigned to cost and harm."
classification:
  theoretical_problem_form: [underexamined-response-choice, competing-decision-criteria]
  narrative_dynamics: [cost-versus-harm-trade-off, executive-incentive-reweighting, response-choice-to-valuation]
  retrieval_signals: [remedy-cost-versus-consumer-harm, executive-incentives-in-response-choice, full-versus-partial-remediation, post-recall-decision]
  identity:
    gap_type: Incompleteness
    theory_building_type: "moderation-type (main effects + moderation); dual-role moderator = event-level baseline criteria (cost, hazard) x actor-level incentive superposition (cash, equity, tenure)"
    coupling: "Incompleteness is realized as mechanism extension onto a brand-new outcome variable (remedy) plus actor-level superposition — not a typical fill-in extension, and with no competing-verdict adjudication structure (which is normal, not an Incommensurability miss)"
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
      - "When testing a downstream consequence of the choice, reuse the main-choice equation as the Heckman selection equation and defend the exclusion restriction empirically — the excluded variable's near-zero, nonsignificant correlation with the outcome — rather than by assertion."
    caveat:
      - "The 170 NYSE CPSC recalls, binary remedy aggregation, compensation measures, probit model, and instruments are setting-specific; the binary coding cannot resolve differences among partial remedies."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage a decision-trade-off result in order: establish the cost and harm main effects, reveal the direct incentive associations, then show which incentives actually reweight each criterion."
      - "Use a downstream valuation analysis as a contrastive consequence only after the remedy choice is established, and distinguish a selection-adjusted association from proof of investor interpretation."
    caveat:
      - "The Heckman selection-corrected CAR result that full remedy lowers announcement-window returns can still reflect severity or confounds not captured by the selection model; the inverse Mills ratio itself flips from nonsignificant (remedy-only model) to significant (fuller models), and the result does not prove investors infer a specific hidden crisis state."
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
    - "C4 info (2026-09-23 L2): the intro-promised framework checks all receive answers in Results, but two H5/H6 components sit at only p<.10 (CEOequity x Prodvalue .138; CEOcash x Hazard -.535) and are merged into 'supported' — the card's falling action reports both pairs as delivered without upgrading their evidential strength."
    - "C1 info (2026-09-23 L2): gap=Incompleteness couples with the moderation-type architecture as mechanism extension onto a brand-new outcome variable (remedy) plus actor-level incentive superposition; the absence of a competing-verdict adjudication structure is expected here."
    - "Local re-read note (2026-09-23): H7/H8 tenure interactions remain a Theory subplot reported as do-not-support with the Results spillover-null sentence ('this adverse impact does not spill over...'); the Discussion recycles cost–harm and CEO main effects (including tenure's direct effect) but never returns to the interaction null."
```

## Story Reading

### Theme question

Once a product is recalled, what determines whether a firm provides a full rather than partial consumer remedy, and how do CEO incentives alter the balance between remedy cost and consumer harm?

### Whole-story synopsis

The paper begins by separating a neglected response decision from the better-known question of recall timing. A recall remedy is what the firm offers affected consumers after the event: full refund or replacement versus repair, self-repair kit, or a future-purchase discount. Before defining the margin, it legitimizes the dichotomy by aligning it with precedent strategy dichotomies (unambiguous support versus stonewalling, proactive versus passive, supereffort versus denial), declaring full versus partial the fundamental distinction and the differences among partial remedies matters of degree. This gives the paper a concrete choice whose two criteria conflict. Full remedy is more costly in immediate expense and uptake, especially when the recalled product value is high; it is also more responsive to consumer harm, regulatory scrutiny, trust restoration, and long-run value. CEO compensation and tenure enter not as a separate collection of correlates but as conditions that can change how those two criteria are weighted. Higher cash compensation and longer tenure are theorized to favor short-term earnings or entrenchment; equity incentive should privilege long-run value. A sample of 170 CPSC recalls (1996–2007) by NYSE-listed companies finds lower full-remedy likelihood for higher product value, higher likelihood for greater hazard, lower likelihood with CEO cash pay and tenure, and higher likelihood with equity incentive. Cash and equity also change the cost and hazard effects in opposite directions (two of the four interaction components at p<.10), whereas tenure does not moderate them. A Heckman selection-corrected CAR regression over the [0,+1] announcement window — the main probit reused as the selection equation — then finds lower short-window market returns for full remedy, reintroducing the consumer–investor contrast. The Discussion returns to remedy as a consumer-welfare and governance decision, but the data observe compensation, remedy category, and CAR—not CEO intent, consumer trust, or the presumed long-run benefit of full remedy.

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
- **Rising action:** Full versus partial remedy is introduced through precedent dichotomies and establishes the cost–harm trade-off; CEO incentives and tenure are introduced as potential reweighting conditions, with the six interactions handed off as "based on similar theoretical reasoning."
- **Climax:** Probit results show the predicted product-value, hazard, cash, equity, and tenure associations with full remedy.
- **Falling action:** Cash and equity incentives moderate both decision criteria in opposite directions (H5/H6 judged as joint verdicts, two components at p<.10); tenure interactions fail; a Heckman selection-corrected CAR regression (main probit reused for selection, Reputation excluded on empirical grounds) shows lower announcement-window returns for full remedy.
- **Denouement:** The Discussion reframes consumer remedy as a governance and welfare choice, while acknowledging the coarse partial-remedy category.

### Tension

- **Source:** A full remedy creates an immediate firm expense but better protects customers and may support longer-run trust; executive incentives may make the same cost and harm information carry different weight.
- **Construction:** The paper makes the tension operational through an explicit remedy choice and tests interactions that attach incentives to the two decision criteria.

### Alternative readings

- **author-signaled-alternative:** The paper acknowledges that partial remedies are heterogeneous: an ordered logit over all remedy categories keeps the key effects (product value, hazard, CEO cash, CEOequity x Hazard) similar but drops others below conventional significance, so the strongest claims concern full versus partial remedy, not a fine-grained remedy continuum.
- **analyst_counterfactual:** The CEO-pay associations could reflect unobserved firm governance, crisis severity, or consumer composition rather than CEOs acting from private self-interest. The design addresses compensation endogeneity with instruments (CLR strength test, Hansen J, Wald, control function) but does not observe deliberation or motive.

## Story Assessment

- **Theme coherence:** `works` — remedy choice, cost, harm, CEO conditions, interactions, and the policy ending address the same post-recall decision.
- **Character discipline:** `works` — the paper clearly distinguishes response criteria, incentive conditions, and downstream valuation.
- **Knot integrity:** `works` — full remedy's immediate cost and consumer-protection value form a real decision conflict, not merely a neglected variable.
- **Plot emergence:** `works` — the interaction tests follow naturally from the claim that incentives reweight cost and harm.
- **Tie–unravel alignment:** `partly_works` — the remedy and interaction predictions are directly tested, but CEO motives, customer trust, and long-run value are inferred from proxies and prior literature.
- **Ending quality:** `partly_works` — it returns to welfare and governance but casts proxy-based associations too readily as CEO private-interest behavior and policy prescriptions.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, remedy regulation, CEO ethics, or research quality.

### L1 re-distillation increments (writeback 2026-09-23, 8 blocks)

Structural moves extracted by the section-level re-distillation; cited here as reference, not duplicated into `section_learning` (two-move cap).

- **Introduction** — `contribution_cross_literature_escalation_ladder_liuliuluo2016` (variant N of the three-layer-contribution corpus): a three-rung cross-literature escalation ladder — phenomenon gap (almost no research on remedy) → framework first claim (first study to test the remedy-cost versus consumer-harm trade-off) → actor bridge ("people" factors: CEO financial interests). Each rung runs a two-beat rhythm (literature-state sentence, then declaration sentence); the second rung anchors the framework-level first claim; the third merges direct effect plus moderation via "not only... but also" and embeds a findings preview.
- **Theory** — `precedent_dichotomy_legitimacy_alignment`: the new full/partial margin is legitimized before definition by aligning with precedent strategy dichotomies (support/stonewalling, proactive/passive, supereffort/denial). `component_split_opposite_sign_ab_pair`: H3 is split into H3a (cash, negative) and H3b (equity, positive) — an opposite-sign component pair on the same theoretical axis, not one composite pay hypothesis. `analogous_moderator_handoff`: the six moderation hypotheses are handed off with "based on similar theoretical reasoning," and the tenure interactions (H7/H8) are derived by declared resemblance to the cash-compensation logic.
- **Methods** — `m8_heckman_main_equation_reuse_empirical_exclusion` (variant in the two-stage-model corpus): the firm-value analysis reuses the main Equation 1 probit as the Heckman selection equation, and the exclusion of Reputation is defended empirically (correlation with CAR .017, nonsignificant). `m6_archival_field_measurement_construction_rules` (variant in variable-operationalization): archival-field measurement construction — logged CPSC/Execucomp/CRSP fields, reputation residualized on firm size, mean-centering for interaction interpretation.
- **Results** — `r3_construct_subsection_verdict_mapping` (variant AS): results are organized into construct-named subsections (Product Value and Product Hazard; CEO Compensation and Tenure; Interactions) that each close with explicit hypothesis verdicts. `r6_multipart_hypothesis_joint_verdict` (variant AT): multi-part hypotheses H5/H6 receive joint verdicts ("these results support H5"; "the two parts of H6 are both supported") — with the two p<.10 components merged into "supported" (see l2_notes, C4).

## Learning Affordances

### Introduction and Theory

This is useful when a project has a real post-event response choice with opposing criteria and a theoretically justified actor condition that changes their weighting. It is not a generic way to add executive moderators after a cost-benefit prediction.

### Methods and Results

The card's main value is the interaction architecture: measure the actual choice, establish the two criteria, then test whether an incentive changes each criterion's effect — with results staged in construct-named subsections whose multi-part hypotheses receive joint verdicts. Downstream CAR is a separate evaluative arena handled by reusing the main-choice probit in a Heckman selection correction, not a substitute for observing customer restoration or CEO mechanism.

### Discussion

Use the ending as a reminder that consumer welfare, short-term firm cost, and market reaction need not align. Do not label managers unethical or incentives corrective without direct evidence of their decision process and longer-run effects.

## Comparison prompt

Compared with Chen 2009, does a study ask how a recall is announced and signaled, or how consumers are remedied after it? Compared with Darby 2024 and Malik 2025, do executive incentives change post-awareness timing, public handling, or the cost–harm weighting of a concrete remediation choice?
