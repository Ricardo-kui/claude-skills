# Story Learning Card — Antón, Ederer, Giné, and Schmalz (2025, Management Science)

## Metadata

```yaml
schema_version: "4.0-lite"
id: anton2025
paper:
  citekey: null
  title: "Innovation: The Bright Side of Common Ownership?"
  outlet: "Management Science"
  year: 2025
  publication_status: published
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A bounded learning object for converting a one-sided common-ownership debate into a conditional cross-firm-externality story, without treating an average association as the answer."
reading_scope:
  sections_read: [abstract, introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "Antón 等 - 2025 - Innovation The Bright Side of Common Ownership.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "The theory receives added attention because the paper's story depends on a pair-level ownership topology that produces two opposed portfolio payoffs; the empirical sections test the predicted pattern rather than observe how owners direct either firm."
mechanism_evidence:
  status: partly_probed
  basis: "Pair-level ownership–technology and ownership–product-market interactions, plus limited merger-shock evidence for some patent outputs, fit the predicted heterogeneous pattern; the study does not observe investor intervention, managers' portfolio-weighted objectives, realized knowledge sharing, or suppression of competitive innovation."
classification:
  theoretical_problem_form: [conditional-portfolio-externality, competing-cross-firm-externalities]
  narrative_dynamics: [one-structure-two-opposed-payoffs, ownership-topology-to-conditional-prediction, average-effect-cancellation, technology-spillover-versus-business-stealing]
  retrieval_signals: [common-ownership-cross-firm-externalities, technology-spillover-internalization, product-market-business-stealing, ownership-network-topology]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Reopen a one-sided policy debate by showing that the same structural arrangement makes two named cross-unit consequences financially relevant, rather than by declaring a generic upside to the dominant concern."
      - "Make an average effect an explicitly inadequate question when a focal firm's action has differently signed consequences for portfolio peers, then name the relational dimensions expected to sort those consequences."
    caveat:
      - "This move needs one decision whose consequences genuinely travel across units and one actor that can capture both consequences; it cannot turn any mixed empirical result into a balanced-story claim."
  theory:
    suitable: "yes"
    requires: [genuine-mechanism-paradox]
    learn:
      - "Draw the ownership topology before deriving predictions: a common owner values the focal firm's payoff and a peer's payoff, while the focal firm's innovation can either lower a technologically related peer's costs or take sales from a product-market peer."
      - "Turn opposed terms into a conditional prediction by specifying what varies across dyads, so the theory explains why an unconditional portfolio-level coefficient can cancel rather than treating heterogeneity as a post hoc moderator search."
    caveat:
      - "The model assumes firms act in their largest owners' interests and treats proximity as potential spillover; it is not a transferable claim that all shared ownership yields either collaboration or muted competition."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Align the operationalization to a dyadic theory by measuring common ownership, technological proximity, and product-market proximity across focal–peer pairs before aggregating them into firm-year prediction terms."
      - "Use innovation input and distinct output measures to ask whether the predicted conditional pattern appears at more than one stage of the innovation process."
    caveat:
      - "Kappa weights, patent-class overlap, 10-K text similarity, U.S. holdings filings, and the BlackRock–BGI merger are setting-specific proxies and do not observe the actor's actual governance conduct."
  results:
    suitable: "yes"
    requires: [genuine-mechanism-paradox]
    learn:
      - "Stage the apparently ambiguous average association as the expected cancellation point, then reveal the positive technology-proximity and negative product-market-proximity interactions as the promised resolution."
      - "Let heterogeneity plots and the later ownership shock test show the scope and evidentiary limit of the conditional account, rather than presenting either as proof that the full owner-to-manager mechanism was observed."
    caveat:
      - "The merger analyses are mixed across inputs and outputs, and the negative competitive pathway is not robustly causal; a similar sequence requires credible variation and a clear statement of what it cannot establish."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Close a conditional-policy story by changing the relevant distinction from common ownership in general to the peer relations that make shared ownership internalize a technological benefit or a competitive loss."
    caveat:
      - "The paper's efficiency model and incomplete causal evidence do not license a general welfare verdict or a policy recommendation for all horizontal or technologically related ownership links."
story_assessment:
  overall_role: partial_exemplar
  mode: second_read_reviewed
```

## Story Reading

### Theme question

When common owners hold a focal innovator and other firms, does that ownership raise or reduce the focal firm's innovation—and why does the answer depend on whether those portfolio peers receive technological benefits or lose sales?

### Whole-story synopsis

The paper opens with an antitrust-era puzzle: rising common ownership is commonly connected to softer competition and declining innovation, yet the same portfolio structure may also make an innovator's technological spillovers valuable to firms held by the same owners. It does not replace the competition concern with a generic bright side. Instead, it reconstructs the ownership network around a focal firm. A focal firm's innovation has a private return, a potential cost-reduction benefit for technologically proximate peers, and a business-stealing loss for product-market peers. A common owner that values the focal firm's and the peers' profits has reason to internalize either consequence. The central mechanism therefore turns the opening question into a conditional prediction: common ownership increases innovation when technological spillovers dominate; it reduces innovation when product-market substitution dominates; an economy-wide average can be ambiguous because these dyads differ. The model formalizes this two-payoff topology, and the empirical design mirrors it with pair-level kappa ownership weights and technology- and product-space proximity measures aggregated to focal-firm terms. The results reveal the predicted positive and negative interactions across R&D and patent measures, and show roughly split positive and negative implied effects. Robustness checks and a BlackRock–BGI ownership shock add limited support, chiefly for some innovation-output measures, while the authors explicitly keep the causal interpretation open. The conclusion returns to the policy debate with a narrower lesson: ownership links among direct horizontal rivals and links among technologically related firms need not produce the same innovation incentive or welfare implication.

### Characters and storylines

- **Portfolio actor:** the common owner (or the owners represented in the focal firm's portfolio-weighted objective), because its stakes make peer-firm profits consequential to the focal firm's modeled decision.
- **Focal decision maker:** the innovating firm and its managers, whose innovation choice is modeled as serving the largest owners' weighted portfolio interests; the study does not observe this instruction or governance process.
- **Beneficiary peer:** a technologically related firm held by the same owner, because the focal firm's innovation can lower this peer's costs through a potential technological spillover.
- **Harmed peer:** a product-market-related firm held by the same owner, because focal innovation can take its sales and profits through business stealing.
- **Relational boundary characters:** technology proximity and product-market proximity, which sort the magnitude and sign of the two portfolio consequences rather than functioning as generic moderators.
- **Storyline 1:** common owner → internalizes a focal innovation's technological benefit to an owned peer → greater incentive for focal innovation.
- **Storyline 2:** common owner → internalizes an owned competitor's loss from focal innovation → weaker incentive for focal innovation.
- **Intersection:** the same focal firm, owner, and innovation choice can enter both lines through different peers; the paper's answer is the relative strength of the two cross-firm payoff paths, not a single net effect of common ownership.

### Five acts

- **Exposition:** U.S. concentration, common ownership, and declining innovation make common ownership appear primarily as a competition problem, while potentially procompetitive effects remain less examined.
- **Rising action:** The model maps owner, focal firm, and peer firms, then derives opposed technology-spillover and business-stealing effects whose relative strength predicts the direction of innovation.
- **Climax:** Once the pair-level interactions enter the empirical models, common ownership is more positively related to innovation with greater technological proximity and more negatively related with greater product-market proximity; the implied effect is positive for roughly half the firms and negative for the rest.
- **Falling action:** Alternative ownership and proximity measures, lags, and subsamples preserve the pattern; BlackRock–BGI shock designs offer selective support for technology-related innovation outputs but leave important causal claims unresolved.
- **Denouement:** The conclusion narrows the policy question from whether common ownership is categorically harmful or beneficial to which ownership-linked peer relations it internalizes.

### Tension

- **Source:** A common owner's portfolio can make the same innovation both a shared technological gain and a shared competitive loss; an average innovation association therefore obscures the theoretical object.
- **Construction:** The paper makes the tension concrete by keeping the owner, focal innovator, technology-beneficiary peer, and product-market-harmed peer distinct, and by giving each relation a different payoff implication.

### Alternative readings

- **author-signaled-alternative:** The authors say the observed patterns could arise through passive nonenforcement and quiet-life behavior or through active investor engagement and voting; their data do not distinguish those routes.
- **analyst_counterfactual:** Ownership patterns may select firms with different innovation propensities or peer configurations. The BlackRock–BGI analyses narrow this concern for some outcomes, but the authors conclude that they do not establish a strong causal interpretation of either pathway.

## Story Assessment

- **Theme coherence:** `works` — the paper consistently asks why the same ownership structure can have opposed innovation implications, and its model, measures, results, and conclusion retain that conditional question.
- **Character discipline:** `works` — the owner, focal firm, technological peer, and product-market peer have distinct payoff roles; the two proximity measures diagnose those roles rather than adding unrelated subplots.
- **Knot integrity:** `works` — the opening policy debate creates a genuine problem because neither a uniformly anticompetitive nor a uniformly beneficial account can explain the model's cross-firm payoffs.
- **Plot emergence:** `works` — the interactions follow directly from the pair-level portfolio objective and the two externalities, so the empirical heterogeneity is the theory's resolution rather than a decorative moderation exercise.
- **Tie–unravel alignment:** `partly_works` — the empirical patterns and limited shock evidence enact the promised conditional resolution, but causal leverage is incomplete and the actual owner-to-manager and spillover processes are not observed.
- **Ending quality:** `partly_works` — the conclusion effectively returns to the policy distinction, but its welfare implications necessarily remain qualified by the paper's model and unresolved causal evidence.
- **Boundary:** This evaluates storytelling, not research quality, causal identification, or journal value.

## Learning Affordances

### Introduction and Theory

Use this card when a single structural relation makes a focal actor internalize two genuinely opposed cross-unit consequences, and the paper can specify which relational condition sorts them. The transferable move is to turn the tension into a conditional prediction before data collection. It is not a template for framing any mixed sign, ownership measure, or two moderators as a paradox.

### Methods, Results, and Discussion

The paper is useful for learning how a dyadic theoretical topology can determine measurement and how a predicted average cancellation can be staged before heterogeneous results. Its empirical mechanism calibration is `partly_probed`: the evidence supports the pattern and some ownership-shock implications, not the unobserved portfolio-objective, engagement, nonenforcement, or knowledge-sharing routes.

## Comparison prompt

Does common ownership make the investor internalize a focal firm's portfolio-wide positive externality, as in `desjardine2022`, or does it make the same focal innovation simultaneously valuable to technologically related peers and costly to product-market peers? Which peer receives which payoff, and is the claimed portfolio action observed or inferred?
