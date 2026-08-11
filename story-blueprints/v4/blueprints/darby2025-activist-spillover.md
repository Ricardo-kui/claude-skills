# Story Learning Card — Darby et al. (2025, Journal of Supply Chain Management)

## Metadata

```yaml
schema_version: "4.0-lite"
id: darby2025
paper:
  citekey: DarbyEtAl2025Activists
  title: "An Agency Theory Perspective on Activist Investors and Supply Chain Failures: The Case of Product Recalls"
  outlet: "Journal of Supply Chain Management"
  year: 2025
  publication_status: published
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A contrastive case for learning how an observed threat to other organizations can be theorized as a proactive governance spillover, without equating a non-targeted actor with a directly monitored one."
reading_scope:
  sections_read: [introduction, theory, methods, results]
  coverage: partial
  source_records:
    - "4.54 Darby et al (2025) JSCM 激进投资者与召回时机.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results]
  audit: [methods]
  departure_note: "The supplied parsed text ends after results and robustness checks; no Discussion assessment or learning claim is made."
classification:
  theoretical_problem_form: [cross-domain-application, underexamined-spillover]
  narrative_dynamics: [threat-to-proactive-action, governance-spillover, boundary-by-observability]
  retrieval_signals: [anticipated-monitoring, spillover-effect, proactive-response-to-threat]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "partial"
    requires: []
    learn:
      - "Move from a high-stakes focal failure to a specific unanswered question about whether a visible threat elsewhere can change untargeted actors' preventive behavior."
      - "Distinguish the focal actor from the attacked actor early, so the spillover rather than direct treatment is the reader's question."
    caveat:
      - "The Vioxx case, the activist stereotype, and the claim that investors can observe each other's attacks are not portable substitutes for a credible transmission path."
  theory:
    suitable: "partial"
    requires: []
    learn:
      - "Use a theory of monitoring to explain why a potential future sanction can alter action before the focal organization is directly targeted."
      - "Make moderators explain the visibility or interpretability of the action for the threatened audience, not merely add contextual heterogeneity."
    caveat:
      - "The impression-management account is inferred from outcome patterns; do not write it as observed conduct without process evidence."
  methods:
    suitable: "yes"
    requires: []
    learn:
      - "Operationalize a spillover claim so the exposure explicitly excludes direct treatment; here, activists targeted other firms but not the recalling firm."
    caveat:
      - "The Schedule 13D construction, FOIA data, recurrent-event AFT models, and matching design are study-specific evidence choices."
  results:
    suitable: "partial"
    requires: []
    learn:
      - "Reveal the focal spillover result before moderators, then use moderators to test why the threatened audience should care more in some events."
    caveat:
      - "Do not let robustness volume stand in for evidence of the claimed perceptual mechanism."
  discussion:
    suitable: "no"
    requires: []
    learn: []
    caveat: []
story_assessment:
  overall_role: contrastive_case
  mode: second_read_reviewed
```

## Story Reading

### Theme question

Can activist investors speed recall initiation at firms they have not targeted by making those firms fear becoming the next target?

### Whole-story synopsis

The Introduction begins with the human cost of delayed recalls and asks what might accelerate action when firms retain discretion. It reviews known recall antecedents, then narrows from internal governance to activist investors as a distinct external force. The central move is not that activists directly intervene in the recalling firm; it is that an activist's highly visible attack on another portfolio firm may be observed by executives at an untargeted firm. Agency theory turns this observation into a threat-of-monitoring mechanism: quick recall can signal decisiveness and concern for consumers, helping managers avoid future activism. Design defects and high-severity defects become conditions under which quick action can more credibly manage an activist's impression. The design deliberately removes firms targeted in the recall year, making the evidence arena match the spillover claim. Results show faster recalls at firms owned by activists that targeted other firms, with stronger associations for design-related and high-severity defects. Because the supplied text lacks a Discussion, the available story ends with robustness rather than an observed authorial denouement.

### Characters and storylines

- **Main character:** activist investor ownership linked to attacks on other firms, because this is the unusual non-targeted exposure the paper needs to explain.
- **Resolution-bearing character:** time-to-recall, the post-awareness managerial response that can display quick action.
- **Audience/threat character:** executives at the focal firm, who observe activists and may seek to avoid becoming their next target.
- **Supporting characters:** defect type and severity govern how interpretable and consequential a quick recall appears to the potential monitor.
- **Storyline 1:** a public attack elsewhere turns otherwise distant investor activity into a latent threat at the focal firm.
- **Storyline 2:** rapid recall is treated as a signal that manages this threat by demonstrating decisive handling of a visible supply-chain failure.
- **Intersection:** the paper's claim depends on exposure being indirect; direct activist intervention would be a different causal story.

### Five acts

- **Exposition:** Vioxx illustrates the stakes of delay; discretionary recall timing becomes a governance question.
- **Rising action:** Prior work on internal governance and direct activism narrows to a potential spillover; agency theory explains why untargeted firms might act preemptively.
- **Climax:** Models restricted to non-targeted firms show that greater activist ownership associated with attacks elsewhere predicts faster recall initiation.
- **Falling action:** Design-defect and high-severity results specify where the association is stronger, followed by alternative estimators, lagged exposure, and matching checks.
- **Denouement:** Not assessable from the supplied full text because it ends before the Discussion section.

### Tension

- **Source:** An activist attack is ordinarily a direct threat to its target, yet the paper asks whether its visibility creates a governance effect before any direct attack occurs.
- **Construction:** The Introduction repeatedly distinguishes target from non-target, and the empirical sample excludes current targets so the spillover is the focal object rather than a rhetorical label.

### Alternative readings

- **analyst_counterfactual:** The paper could have treated activist ownership as ordinary external monitoring. Its stronger and riskier narrative choice is to make prior attacks at other firms the causal source of pressure; this is an analyst reading.

## Story Assessment

- **Theme coherence:** `works` — the non-targeted spillover remains the central question from introduction through design and results.
- **Character discipline:** `partly_works` — activists alternately function as owners, potential monitors, threats, and implied audiences, which makes the mechanism less sharply bounded.
- **Knot integrity:** `partly_works` — the non-targeted spillover is a meaningful unanswered question, but the paper establishes a gap more strongly than a consequential conflict in existing theory.
- **Plot emergence:** `partly_works` — excluding direct targets makes the evidence fit the claim, while the link from speed to impression management remains inferential.
- **Tie–unravel alignment:** `works` — the results directly address the promised spillover and its stated boundaries.
- **Ending quality:** `not_assessable` — the supplied text does not contain the Discussion.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification or research quality.

## Learning Affordances

### Introduction and Theory

Learn the discipline of identifying the genuinely indirect object of a study. The transferable action is not "frame every outside event as a spillover," but make clear why the focal actor observes, interprets, and can preempt the external event.

### Methods and Results

This card is especially useful for checking whether a spillover design actually removes direct exposure. It should not be used to infer a perception-management mechanism from an association alone.

## Comparison prompt

What is changing the decision: an executive's own wealth exposure (Darby 2023), routine monitoring by powerful owners (Darby 2026), or fear induced by visible attacks on other firms (this paper)? If an external actor is not directly involved, what observed transmission path makes the comparison credible?
