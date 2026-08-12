# Story Learning Card — Fini, Jourdan & Perkmann (2017, Academy of Management Journal)

## Metadata

```yaml
schema_version: "4.0-lite"
id: fini2017-social-valuation
paper:
  citekey: fini_jourdan_perkmann_2017_amj
  title: "Social Valuation across Multiple Audiences: The Interplay of Ability and Identity Judgments"
  outlet: "Academy of Management Journal"
  year: 2017
  publication_status: published
  paper_type: quantitative
  source_version: OvisOCR2_full_text (2026-08-11)
  inclusion_rationale: "A partial exemplar for learning the dual-channel decomposition of one evaluation signal (ability + identity conformance, with source-dependent alignment) into a derived inverted-U, with channel-matched moderators and a three-step confirmatory design (full-panel GMM -> CEM -> interviews). Its marginal learning value is the architecture, not the curve: the inverted-U narrative frame and the cross-audience dual-signal sentence template already exist in the corpus sourced from this same paper, and the L2 coordination flag reports registry drift."
reading_scope:
  sections_read: [abstract, introduction, theory, methods, results, discussion, conclusion]
  coverage: complete
  source_records:
    - "文献笔记库/01 导入/论文导入/Fini等-2017-Social Valuation across Multiple Audiences The Interplay of Ability and Identity Judgments.md (full text, 415 lines)"
    - "sections/introduction.json"
    - "sections/theory.report.yaml"
    - "sections/methods.json"
    - "sections/results.json"
  note: "Full text read in slices (abstract/intro/theory lines 25-140, methods 141-203, results 204-246, discussion/conclusion 247-284). Very long HTML table rows (Tables 1-4) were skipped; all prose and Table-1 variable ranges were read. Line references in the four section distillates were verified against the full text. The 'stale Ridge 2024 artifact' note that the theory report carried mid-pipeline is resolved: introduction.json now holds Fini content, so the C1 two-layer gap reading rests on both sections."
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Matches the default attention profile. The imperfect-paper dimensions (marginal H2a/H3b linear interactions reported as 'consistent with', CIs reported only for the main-effect Fieller turning-point interval, single-sentence descriptive-statistics navigation, findings-preview magnitude leak without a baseline) received extra attention in the Results and Discussion readings because they are part of this card's learning object."
classification:
  theoretical_problem_form: [dual-channel-index-decomposition, cross-audience-partial-criterion-overlap, socially-endogenous-inference-boundary]
  narrative_dynamics: [opposing-channels-sum-to-inverted-U, channel-matched-dual-moderation, three-step-confirmation-chain, canonical-effect-offset]
  retrieval_signals: [social-valuation, multiple-audiences, exogenous-endogenous-indices, inverted-U, identity-conformance, peer-evaluation, university-industry]
  confidence: reviewed
mechanism_evidence:
  status: partly_probed
  basis: "The two channels (positive linear ability; increasingly negative identity conformance) are theorized information-inference paths read off ONE observable signal (B0) — not measured mediators; the paper makes no formal mediation claim. The ability channel and the inverted-U sum are directly tested (Lind-Mehlum endpoint slopes, Fieller turning-point interval). The identity-conformance channel is probed indirectly: the relative-share alternative operationalization produces an honest null that discounts the time-effort rival and supports identity non-conformance, and 10 interviews independently articulate both readings. Both moderators are directly tested through curve geometry (interaction signs, plots, range-wide profile, turning-point shift, predicted counts)."
story_track:
  fed_flags:
    - flag: "C1"
      content: "Two-layer gap: the Introduction's primary gap is Incompleteness — a mechanism well documented for homogenous audiences ('While this powerful mechanism is well known and documented for homogenous audiences, we know relatively little about how it plays out when multiple audiences are present') — while the Theory carries a distinct Inadequacy: prior work treats prior evaluations as pure ABILITY signals, an assumption the paper revises into a dual ability + identity-conformance channel whose alignment is source-dependent."
      consumption: "Introduction and Theory learning moves both flag that the two-layer architecture is only legitimate when the theory separately revises the assumption the intro extends. The card reads the Incompleteness as the surface gap (context extension) and the Inadequacy as the load-bearing revision, not as a contradiction."
    - flag: "C4"
      content: "The Introduction's findings preview leaks result magnitude (9,502 scientists, 2001-2012, attenuation directions, interview corroboration) without an economic-significance baseline; the Results fully honor the preview's inverted-U + dual-moderation + CEM + interview contract."
      consumption: "The Results learning move (curve-geometry cadence, rival-mechanism adjudication) and the imperfect-paper note (preview-magnitude leak, missing CI discipline) rest on this flag. The preview is read as a contract the Results pays off; the absent baseline is flagged as a preview-craft target, not a broken promise."
    - flag: "coordination"
      content: "The paper's core narrative is already registered in the corpus sourced from this exact paper (theory mechanism_chain 'cross_audience_dual_signal_curvilinear_inference'; methods nonlinear-model variant 16; results count-model variant 13), but the evidence registry has no fini source entry — registry drift (data-integrity gap at L4)."
      consumption: "The card judges its own learning value partly non-additive: the inverted-U frame is not novel in the corpus, so the distinctive assets are the two-layer gap, the source-dependent alignment taxonomy, and the channel-matched paired-geometry moderation. The registry drift is flagged for the orchestrator as a data-integrity fix, not a story defect."
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Open with a mechanism well documented under one condition, then make its portability to a new condition (homogenous peers -> multiple audiences) the precise research question, so the gap is a context extension with a single explicit, scope-narrowed RQ rather than a generic 'little is known' list."
      - "Name the dual reading of the same observed signal early (ability + identity conformance), and let the theory-lens decomposition mechanically generate the inverted-U preview and channel-matched moderators in the preview paragraph, so the prediction is derived, not asserted."
    caveat:
      - "Transfer only when the focal audience can reasonably treat the external evaluation as some evidence of ability while applying a nonaligned identity standard; a totally irrelevant or stigmatized external audience is a different theory problem (the authors' own boundary, stated in the Conclusion)."
      - "The findings preview leaks exact magnitudes (9,502 / 2001-2012 / attenuation directions / interviews) without an economic-significance baseline; keep the preview at direction + moderation and defer numbers to Results."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Separate the two inferential components before deriving the curve — a positive linear ability channel offset by an increasingly negative identity-conformance channel, summed at every point (Haans et al. 2015) — rather than beginning from a preferred inverted-U result."
      - "Carry a second, distinct gap layer in the theory (Inadequacy: the ability-only assumption of prior work revised into a dual channel) that fulfills the Introduction's Incompleteness; then derive each moderator FROM the two-channel decomposition and emit paired geometric hypotheses (curve shape + turning-point position) with an explicit invariance declaration for the untouched channel."
    caveat:
      - "The nonlinear prediction is justified here by distinct marginal effects with different shapes; a mere trade-off or conflicting stakeholder preference does not warrant an inverted U."
      - "The paired-geometry moderator form requires a measurable geometric claim (Haans, Pieters & He 2016); without a direct inflection-point test the H[N]b half is untestable."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "State the three-step confirmatory architecture as an explicit roadmap ('We proceed in three steps': full-panel GMM -> CEM -> interviews) that previews the Results reading order and explicitly limits interviews to mechanism corroboration rather than a second causal estimate."
      - "For an inverted-U GMM, instrument the squared term alongside the linear term and include two-year-lagged endogenous variables interacted with boundary conditions (Abadie 2003), rather than treating the square as a derived term."
    caveat:
      - "The Poisson-GMM instruments require independent exclusion arguments per endogenous variable; the paper declares three instruments for the three endogenous variables jointly. The CEM confirmation reports no post-match balance statistics, and 'controlling for self-selection, unobserved heterogeneity, and autocorrelation' conflates three distinct threats — cautionary elements, not a model to copy."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Formally adjudicate a curvilinear claim — Lind-Mehlum endpoint slopes at the interval bounds, a Fieller turning-point interval, and an in-range check — rather than stopping at the significance of the squared term."
      - "Report curve geometry, not interaction signs alone: conditional plots -> range-wide significance profile (Bowen) with explicit exceptions -> turning-point shift -> predicted-count translation; and adjudicate a rival mechanism via an alternative operationalization that produces an honest null ('We interpret this finding as discounting X and further supporting Y')."
    caveat:
      - "Marginal linear interactions (p<.10) must keep the marginal label and not be merged into full support — the paper's 'consistent with hypothesis' wording for H2a/H3b linear terms is borderline; and the near-absence of CIs beyond the Fieller interval is a transparency target, not a model."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Return to the canonical mechanism named in the opening (the Matthew effect) and transform it into a bounded conditional rule — external appreciation is an asset up to the point it becomes an identity liability — rather than merely restating the findings."
      - "State the boundary condition explicitly (moderate overlap of the audiences' ability criteria) and route open questions (reputation/status, the Tribe 'sellout' example) to future research."
    caveat:
      - "The Discussion's four-literature contribution inventory (social valuation, social approval assets, institutional logics, academic science funding) is broad and delays the return to the focal cross-audience inference; a new paper should close its own loop before expanding implications."
story_assessment:
  overall_role: partial_exemplar
  mode: first_read_reviewed
```

## Story Reading

### Theme question

How does a peer audience evaluate a candidate who has already been valued by an external, non-peer audience, when that external appreciation simultaneously signals the candidate's unobservable ability and a possible deviation from the identity the peer audience expects — such that prior appreciation helps a candidate only up to a point, and the identity proximity between audiences and the availability of peer-certified records decide where that point is?

### Whole-story synopsis

The paper opens from the resource-dependence premise that individuals and organizations depend on multiple audiences that control critical resources, each deploying its own evaluative "yardstick" (investors, customers, museums, galleries, industry). It then recalls the dominant mechanism: because a candidate's worth is often not directly observable, evaluators rely on socially endogenous inferences — taking the opinions of other evaluators into account via observable transactions — which produces herding and the Matthew effect, disproportionately rewarding those already appreciated. The paper then makes this well-documented mechanism unstable by moving from homogeneous peer audiences to multiple audiences: we know relatively little about how it plays out when multiple audiences are present, and a single scope-narrowed RQ is posed — how is the peer evaluation of a candidate influenced by the earlier evaluations made by external, non-peer audiences? The theory lens decomposes observable past evaluations ("indices") into two information dimensions — indices of ability and indices of identity conformance — and shows that their alignment is source-dependent: for endogenous (peer-sourced) indices the two are aligned and indistinguishable; for exogenous (external, e.g., industry) indices they diverge. The paper concretizes this with academic scientists seeking research grants, where industry contracts are the exogenous index. Read as an ability index, contracts signal competence to acquire resources, orchestrate projects, and manage collaborations — positive and linear. Read as an identity-conformance index, accumulating contracts increasingly signal deviation from the prototypical academic identity — "is the candidate one of ours?" The sum of a positive linear channel and an increasingly negative channel yields H1: an inverted U between industry evaluation and peer evaluation. A conditionalization pivot then opens two moderator acts derived from the decomposition: audience identity proximity (H2a curve flattening/steepening; H2b turning-point shift) selectively binds the identity channel and leaves the ability channel explicitly invariant; endogenous indices — publication quality (H3a) and regularity (H3b) — reduce reliance on the ambiguous external signal through uncertainty reduction and typecasting. The Methods build a unique archival dataset on the full population of 9,502 scientists at an anonymous UK research university (Minerva) 2001–2012, run through a three-step confirmatory design: full-panel iterative Poisson GMM with a Probit-to-IMR selection correction and an instrumented squared term, then CEM replication, then 10 interviews. Results deliver the promised payoff: the inverted U is formally confirmed (Lind-Mehlum slopes and a Fieller turning-point interval at 12.48 contracts), both moderators operate through the predicted curve geometry, the relative-share alternative operationalization produces a null that discounts the time-effort rival and supports identity non-conformance, system-GMM replication with individual fixed effects adds support, CEM replicates the curve and moderations, and the interviews independently articulate both ability and identity readings. The Discussion returns to the Matthew-effect opening and transforms it: external appreciation is a bounded social approval asset — an asset up to the point it becomes an identity liability. The Conclusion states the overlap boundary explicitly (moderate overlap of the audiences' ability criteria; "a successful bank robber is unlikely to apply to become a banker") and draws university-industry and management-practice implications, with junior researchers flagged as most vulnerable.

### Characters and storylines

- **Main character:** the exogenous index — prior appreciation conferred by an external, non-peer audience (industry contracts), which carries two opposing pieces of information for the focal peer audience.
- **Signal-decomposition characters:** the ability channel (positive, linear) and the identity-conformance channel (increasingly negative) — two information dimensions read off one observable signal whose alignment depends on the signal's source (endogenous aligned / exogenous divergent).
- **Audience characters:** the peer (academic) audience — the focal evaluator who controls the resource and interprets the external signal; the external (industry) audience — confers the exogenous index; the candidate (scientist) — evaluated across both audiences. The opening hook's broader audiences (investors, customers, artists) are a scope statement, not characters — the paper narrows to the common case of peer evaluation.
- **Boundary characters:** identity proximity (W1) — discipline-level, selectively binds the identity channel and leaves the ability channel invariant; endogenous indices (W2) — publication quality and regularity, reduce reliance on the external signal through peer certification and typecasting.
- **Storyline 1 (ability):** external evaluation read as imputed ability -> positive, linear contribution to peer valuation.
- **Storyline 2 (identity conformance):** accumulating external evaluation read as deviation from the expected peer identity -> increasingly negative contribution.
- **Intersection:** one observable external signal carries two non-reducible meanings to the focal peer audience, so prior appreciation yields a bounded benefit rather than universal reinforcement; each moderator binds a specific channel, letting the reader see exactly where the benefit and the penalty live.

### Five acts

- **Exposition:** multi-audience resource dependence; the well-documented socially endogenous-inference / herding / Matthew-effect mechanism; the two-layer gap (Incompleteness: the mechanism is unexamined across audiences); the single scope-narrowed RQ.
- **Rising action:** the indices taxonomy (endogenous vs exogenous x ability vs identity conformance); the grants-vs-contracts context; the dual-channel decomposition; H1 derived from the two-channel sum (Figure 1); the conditionalization pivot; two moderator acts (W1 identity proximity, W2 endogenous indices), each with an independent engine and paired geometric hypotheses.
- **Climax:** Results formally confirm the inverted U (Lind-Mehlum endpoint slopes, Fieller turning-point interval) and both moderations through curve geometry; the relative-share null adjudicates the rival mechanism.
- **Falling action:** robustness battery (IMR bootstrap, negative binomial, three selection models, alternative specs, Gram-Schmidt, censoring/winsorizing); system-GMM replication with individual fixed effects; CEM replication; interview triangulation of the two mechanisms.
- **Denouement:** Discussion returns to the Matthew effect and converts it into a bounded social-approval rule (asset -> liability); Conclusion states the overlap boundary and draws university-industry and management implications.

### Tension

- **Source:** the dominant socially endogenous-inference account predicts self-reinforcing value from prior positive evaluation, yet it assumes peer homogeneity; what survives when the prior evaluation comes from an external audience with a different identity standard is unknown, and the same signal can be read as both competence and deviance.
- **Construction:** the Introduction first establishes why peer reinforcement is plausible, then uses the external audience to expose a signal with two meanings; the Theory does not declare one audience right and the other wrong — it specifies why the focal peer evaluator can read the same signal as both ability and identity deviation, and the two moderators specify when each reading weakens.

### Alternative readings

- **author-stated:** the authors explicitly delimit the theory to cases of moderate overlap in the audiences' ability criteria. With radically distant or stigmatized audiences, external recognition may not signal ability at all, or may be read negatively from the outset (the bank robber example).
- **analyst_counterfactual:** a generic "multiple audiences impose a trade-off" story would predict tension but not why initial external recognition helps, why the identity penalty accelerates, or why identity proximity and endogenous indices flatten the curve in the specific geometric way observed (curve flattening plus turning-point shift). An analyst reading of the evidence: the marginal H2a/H3b linear interactions (p<.10) could equally have been staged as a soft spot rather than full support; the authors' "consistent with" framing converts them into support — a judgment call, not an observed fact.
- **cross-paper comparison note:** against single-mechanism inverted-U cards (Cui cost-benefit; the existing cross-audience dual-signal curvilinear sentence template already sourced from this same paper), the distinctive asset here is the decomposition of one signal into two channels with source-dependent alignment and channel-matched moderation, not the inverted-U frame itself.

## Story Assessment

- **Theme coherence:** `works` — the portability of one signal's dual meaning across audiences stays central from the abstract, through the derived curve and channel-matched moderators, to the Discussion's bounded-asset transformation. The two moderators are derived from the two-channel decomposition, so they are not robustness appendices. The only stray is the surface Incompleteness language in P3, which is fulfilled by the Theory's Inadequacy revision rather than left dangling.
- **Character discipline:** `works` — the exogenous index is the protagonist signal; ability and identity conformance remain analytically separate; identity proximity and endogenous indices play clear boundary roles; the peer and industry audiences stay parallel evaluators with no crowd actors. The opening multi-audience list (investors, customers, artists) is a scope statement, not a cast.
- **Knot integrity:** `works` — the knot is a real, bounded challenge to the peer-homogeneity assumption of socially endogenous inference, with a precise single RQ and a mechanism (source-dependent signal alignment) that gives the knot content rather than a generic "multi-audience is complex" gap. The gap is asserted as a void ("we know relatively little") rather than an explicit "surprising because" puzzle, but the two-channel decomposition supplies the surprise.
- **Plot emergence:** `works` — the inverted-U follows from the sum of two opposing monotonic channels of different slope, not from a desire for a curve; the design (a self-built archival dataset justified by data-availability challenges, a three-step confirmation chain) is generated by the theory's measurement needs, and the Methods' "we proceed in three steps" roadmap previews the Results' reading order.
- **Tie–unravel alignment:** `works` — the Results honor the front-end contract in full: the inverted U, both moderations through curve geometry, the robustness battery, CEM replication, and interview corroboration. Honesty caveat: H2a/H3b linear interactions are marginal (p<.10) yet read as "consistent with" hypotheses, and CIs are reported only for the main-effect Fieller interval — the promise is paid, but the reporting discipline is imperfect.
- **Ending quality:** `works` — the Discussion returns to the Matthew-effect opening and transforms it into a bounded social-approval rule (external appreciation is an asset only up to the point it becomes an identity liability), states the overlap boundary explicitly, and routes open questions (reputation/status, the Tribe example) to future research. The long four-literature contribution inventory delays the return to the focal inference but does not break it.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, the Poisson-GMM instruments' exclusion validity, the CEM balance, or the research's value. The marginal interactions and the near-absence of CIs are evidence facts; their handling is what is assessed.

## Learning Affordances

### Introduction and Theory

Learn the two-layer gap architecture and the dual-channel derivation. The transferable actions are: (1) pose a context-extension Incompleteness in the Introduction (a mechanism documented for homogenous audiences, unexamined across audiences) and let the Theory carry a separate Inadequacy (the ability-only assumption revised into a dual ability + identity-conformance channel) — two layers that mutually fulfill rather than contradict; (2) decompose one observable signal into two named information dimensions whose alignment depends on the signal's source, then derive the curvilinear prediction from the sum of the two opposing channels rather than asserting a curve; (3) derive each moderator from the decomposition so that it binds a specific channel and emits paired geometric hypotheses (curve shape + turning-point position) with an explicit invariance declaration for the untouched channel. The two-layer architecture is only legitimate when the theory cashes the Inadequacy it implies; a surface Incompleteness alone would not justify the paper.

### Methods and Results

The methods move to carry is the three-step confirmatory architecture stated as an explicit roadmap (full-panel GMM -> CEM -> interviews) that previews the Results reading order and limits interviews to mechanism corroboration, not a second causal estimate; plus the instrumented-squared-term-and-boundary-interaction detail for an inverted-U GMM. The results move is the curve-geometry reporting cadence (interaction signs -> conditional plots -> range-wide significance profile -> turning-point shift -> predicted-count translation) and the rival-mechanism adjudication via an alternative operationalization that produces an honest null. Do not copy the missing post-match balance statistics, the conflated "controlling for self-selection, unobserved heterogeneity, and autocorrelation" sentence, or the single-sentence descriptive-statistics navigation.

### Discussion

The ending shows how to convert a canonical positive mechanism (the Matthew effect) into a bounded conditional rule (asset -> liability), state the overlap boundary explicitly, and route open questions to future research. Caveat: the four-literature contribution inventory is broad; a new paper should return first to its own focal cross-audience inference before expanding implications.

### Imperfect-paper learning note

This is a deliberate imperfect-paper case on honest-reporting boundaries. (1) CIs are reported only for the main-effect turning point (Fieller interval [8.31; 23.62]), with no CIs for the curve elsewhere or for the moderation geometry — readers cannot see the precision of most estimates. (2) H2a/H3b linear interactions are marginal (p<.10) yet the conclusion sentences read "consistent with hypothesis," blurring the boundary between support and marginal support; the marginal label should survive into the conclusion. (3) The descriptive-statistics opening is a single navigation sentence. (4) The Introduction's findings preview leaks exact magnitudes (9,502 scientists, 2001–2012, attenuation directions, interviews) without an economic-significance baseline. These are worth learning as reporting-discipline targets, not as defects to avoid repeating the strengths of the story: the paper's honesty shows precisely in the relative-share null it reports in full and converts into mechanism adjudication.

## Comparison prompt

When one signal carries two meanings for a focal audience, does the paper decompose it into channels with source-dependent alignment (Fini) or treat it as a single mechanism? Fini's distinctive asset is the dual-channel decomposition and channel-matched moderation, not the inverted-U frame itself — the cross-audience dual-signal curvilinear sentence is already in the corpus sourced from this exact paper, and inverted-U narrative frames exist in comparable cards. Compare with Ridge (two theories governing different ranges of one X–Y relation), Pontikes (the same attribute valued oppositely by two audiences), and Cui (an inverted-U cost-benefit preview without channel-matched moderation). The concrete reading question: what does the paper teach that the corpus does not already hold — the two-layer gap (Incompleteness in the intro cashed by an Inadequacy revision in the theory), the source-dependent alignment taxonomy, and the channel-matched paired-geometry moderation with an invariance declaration?
