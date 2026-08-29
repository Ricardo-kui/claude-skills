# Story Learning Card — Westphal & Bednar (2005, Administrative Science Quarterly)

## Metadata

```yaml
schema_version: "4.0-lite"
id: westphal2005
paper:
  citekey: westphal_j_d_and_bednar_m_k_2005_pluralistic_ignorance_in_co
  title: "Pluralistic Ignorance in Corporate Boards and Firms' Strategic Persistence in Response to Low Firm Performance"
  outlet: "Administrative Science Quarterly"
  year: 2005
  publication_status: published
  paper_type: quantitative (primary multi-wave survey + archival supplements)
  source_version: pdm_slices_verified
  inclusion_rationale: "Westphal's companion inversion to the 1998 symbolic-management story: the bias moves from the executives being monitored to the monitors themselves. Masterclass in importing a social-psychological construct into governance (Abilene Paradox as human face), in building a rival-construct disambiguation against groupthink, and in a design whose key measure (own concern vs. perceived others' concern on the same scale) is the construct itself operationalized."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "PDM slices: sections/introduction.md, sections/theory.md, sections/methods.md, sections/results.md, sections/discussion.md (westphal_j_d_and_bednar_m_k_2005_pluralistic_ignorance_in_co.pdm)"
    - "Verified section distillations: sections/{introduction,theory,methods,results}.json (L2 coherence=ok; one info flag C3)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default 40/25/15/15/5 profile retained. Two flag families were fed into the card as instructed: (a) the PDM cross-section info flag C3 (theory commits board-level hypotheses; the main analysis is board-level and Appendix B supplies parallel individual-level analyses — level complementarity, no conflict) informs the tie–unravel and Methods entries; (b) the introduction distillation's narrative_risk_ledger R1–R4 (generic stakes, long quoted sentences, P1 fat suit, actor-less hook) are 2005-era craft risks recorded as caveats and as a story-assessment boundary note, not as story failures."
mechanism_evidence:
  status: partly_probed
  basis: "The focal misperception is directly measured (own concern 6.80 vs. perceived others' concern 4.77 on the same scale, same board) and the hypothesized hinge — expressed concern — is measured in two survey waves with mediation tested by Baron–Kenny/Sobel plus instrumental-variable robustness. But the interior mechanism (lay dispositionism: reading others' silence as agreement) is never measured, and the premise-validation survey (social risk of dissent) is a separate sample."
class_retrieval:
  theoretical_problem_form: [individual-virtue-group-failure, rival-explanation-rebuttal, cross-discipline-construct-import, group-level-misperception]
  narrative_dynamics: [steelman-then-double-rebut, anecdote-to-construct-teaching, same-scale-gap-as-climax, cohesion-as-cure-not-villain, spiral-of-silence-payoff]
  retrieval_signals: [pluralistic-ignorance, corporate-boards, strategic-persistence, outside-directors, group-decision-making, board-diversity]
  confidence: provisional
section_learning:
  introduction:
    suitable: "yes"
    requires: ["a rival explanation that already owns part of the evidence but fails on the focal outcome"]
    learn:
      - "Steelman-then-double-rebut tension: state the rival explanation neutrally, concede its partial support in adjacent domains (compensation, golden parachutes), then rebut on the focal outcome twice — absence of supporting evidence and direct contrary survey evidence — before pivoting in one sentence ('In this study, we offer a different explanation...')."
      - "Cross-discipline construct teaching: introduce the imported construct through a four-step lesson — a vivid anecdote (the Abilene family trip), a quoted technical definition, a named consequence ('attitude-behavior disjunction'), and a trigger bridge linking the general phenomenon to the paper's specific condition (negative performance feedback)."
    caveat:
      - "Era artifacts (narrative_risk_ledger R1–R4): stakes are generic ('fills a critical gap'), P1 runs ~270 words and P4 carries 106-word quoted sentences, and the hook names no concrete actor or case. A modern imitation needs a compressed opening, a specific theoretical-cost stakes sentence, and split quotations — the tension architecture transfers, the prose budget does not."
  theory:
    suitable: "yes"
    requires: ["a source-discipline mechanism whose preconditions the focal setting demonstrably satisfies"]
    learn:
      - "Common-trunk, parallel-branch, consequence-extension architecture: build the group-dynamics engine once (social risk of minority opinions → mutual-observation decision rule → self-other attribution asymmetry → spiral of silence), then branch it into the main effect (H1–H2), two moderators (H3–H4), and one consequence extension (H5) — each hypothesis reuses the same trunk rather than a new argument."
      - "Rival-construct opposing-sign disambiguation: explicitly contrast with groupthink, where the identical moderator (social cohesion) carries the opposite sign — cohesion exacerbates groupthink but attenuates pluralistic ignorance — so the same design element adjudicates between the two failure modes."
    caveat:
      - "The trunk's attribution step rests on cited social psychology plus a personal communication for the group-level definition; the group-level aggregation claim (biases are interdependent) is argued before it is validated in Methods (rwg/ICC). A modern version should validate the level claim where it is made. The non-linear aspiration-level premise is declared as an assumption, not derived."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Premise validation inside the design: the theory's behavioral premise (directors perceive social risk in voicing unshared concerns) is tested with a separate 500-director survey (88–94% affirm the risk), so a foundational assumption becomes data rather than assertion."
      - "Construct-definition-to-aggregation alignment: because pluralistic ignorance is defined at the group level, Methods justifies aggregation exactly where the theory located the construct (rwg = .93–.94, significant ICC), making the level of analysis part of the story rather than a technical afterthought."
    caveat:
      - "Own concern and perceived others' concern come from the same respondents on the same instrument — the self–other gap is the story, but that design choice invites common-method skepticism that 2005-era presentation does not fully answer (interrater kappas and individual-level bootstrapped SEs are the only guards). Do not copy the measurement entanglement without a separation strategy."
  results:
    suitable: "yes"
    requires: ["a construct that can be operationalized as a directly measurable gap or difference"]
    learn:
      - "Stage the climax on the misperception gap itself: the headline result is not a behavioral effect but a perceptual one — directors report concern 6.80 but perceive others' concern 4.77 (dummy coefficient 1.848, p < .001) — letting the construct's defining number land before any moderator or consequence."
      - "Nested-mediation choreography: each hypothesis is confirmed twice — the interaction dies when the mediator enters (Baron–Kenny pattern), Sobel tests quantify the mediation (z = 2.15–2.43), and instrumental-variable models replicate the consequence chain — with the premise check (non-linear concern below aspiration levels, t = 8.35) placed before the main tests."
    caveat:
      - "Era presentation: one-tailed tests for hypothesized effects, no AME or economic-magnitude interpretation, and outcome sweep limited to diversification change; causal verbs outrun the survey design by modern standards. Borrow the staging logic, not the inference language."
  discussion:
    suitable: "yes"
    requires: ["findings that bear on a live policy or reform debate the reader already knows"]
    learn:
      - "Policy-inversion ending: return to the opening governance puzzle and invert the era's reform prescription — Sarbanes-Oxley and NYSE reforms push independence, but the findings imply process reform (social cohesion, devil's-advocate aids, simply informing groups about pluralistic ignorance) — so the ending changes what the reader should do, not just what to believe."
      - "Counterintuitive corollary disclosed: the celebrated value of board diversity gets a side-effect warning (homogeneity attenuates pluralistic ignorance), and the mechanism is offered for external puzzles (Enron-era boards failing to speak up), turning the discussion into new evidence for the theory."
    caveat:
      - "The insider-director comparison (insiders report less concern; denser ties) is descriptive, post hoc, and reported from a separate survey — a modern version would pre-register it or cut it. The future-research list is long by 2005 convention; keep only the branches that transform the opening question."
story_assessment:
  overall_role: exemplar
  mode: single_read
```

## Story Reading

### Theme question

When firm performance is low, why do boards staffed with objective, independent outside directors still fail to stop strategic persistence — if the directors privately share the same concerns about strategy, what prevents those concerns from ever being voiced?

### Whole-story synopsis

The paper opens with a division of narrative labor: the strategic-persistence literature has located the bias in top executives — attribution distortions, socialization, threat-rigidity — and corporate governance theory has nominated the corrective: outside directors, who neither formulate strategy nor absorb its culture, should make unbiased attributions and force change. Yet boards fail anyway, regardless of how many outsiders sit on them, and the leading explanation — directors' lack of independence from management — does not consistently survive its own evidence base: it works, at best, on compensation and succession, and survey evidence shows independent directors are no more likely to challenge strategy. The pivot: the problem is not that directors are biased about strategy, but that they are biased about each other. The imported engine is pluralistic ignorance — the Abilene family that drove 106 miles through a dust storm because no one said they'd rather stay home. In board form: expressing a minority opinion carries social risk; each director waits for someone else to speak; observing others' silence, directors overattribute it to confidence in the strategy (lay dispositionism); the spiral of silence ends with a board full of private skeptics and no public doubt. Theory then makes three structural claims: low performance triggers the concern (H1), failure to express concern drives the misperception (H2), social cohesion — dense friendship ties and demographic homogeneity — enables the discovery of shared concerns and so dissolves the bias (H3–H4, mediated by expressed concern), and the misperception suppresses the conversion of private concern into collective voice, blocking strategic change (H5, moderated mediation). Evidence delivers in the same order: the misperception gap is large and significant (6.80 vs. 4.77), the expression mechanism confirms, cohesion shrinks the gap to non-significance at high levels, and the concern × perceived-others'-non-concern interaction predicts strategic persistence, mediated by unvoiced concerns. A separate premise-validation survey shows directors do perceive social risk in unshared dissent (88–94%). The ending returns to the opening question with the polarity reversed: boards fail not because directors lack independence but because they misperceive each other; the reform implication inverts Sarbanes-Oxley's independence logic toward process reform; diversity itself carries an unexamined side effect; and pluralistic ignorance joins groupthink in a taxonomy of group decision failures — with the twist that the cure for one resembles the cause of the other.

### Characters and storylines

- **Main character — pluralistic ignorance:** the protagonist construct; an invisible, group-level state (everyone privately doubts, everyone believes others approve) that must be made measurable, and is — as the gap between own reported concern and perceived others' concern on the same scale.
- **The outside director — the divided hero:** privately objective (the data confirms directors do report concern at low-performing firms) yet socially inhibited; the story's engine is the mismatch between the virtue the governance literature assigns this character and the silence the character actually keeps.
- **Hinge character — expressed concern about strategy:** the missing voice; the mediator in every branch (H2, H3b, H4b, H5b) and the only pathway through which private concern could become collective action. Its absence is the plot.
- **Paired supporting characters — friendship-tie density and demographic homogeneity:** the paradox characters; cohesion, the villain of the groupthink genre, plays the cure here, and diversity, the era's hero, plays an aggravator. Their roles are defined against the rival genre.
- **Stakes character — strategic persistence:** the outcome the whole governance literature cares about; operationalized as change (non-change) in product-market and geographic diversification.
- **Offstage character — the biased top executive:** the earlier literature's culprit, deliberately benched; the story's point is that the bias has migrated to the monitors.
- **Counter-reader — the independence explanation:** steelmanned in the introduction (partial support for compensation outcomes) and rebutted on the focal outcome; rebutted again in the discussion against Sarbanes-Oxley-style reform.
- **Rival genre — groupthink:** the disambiguation foil; same genre (group decision failure), same moderator, opposite sign.
- **Storyline 1 (formation):** low performance → private concern rises, but unexpressed concern → underestimation of others' shared concern (H1–H2).
- **Storyline 2 (moderation):** social cohesion → more willingness and more occasion to speak → discovery of shared concerns → less pluralistic ignorance (H3–H4).
- **Storyline 3 (consequence):** misperception → inhibited voice → no strategic change → persistence (H5), closing the spiral of silence loop the theory section opened.
- **Intersection:** all three storylines pass through the single hinge of expressed concern, and all three are staged on one measurement object — the own-vs-perceived concern gap.

### Five acts

- **Exposition:** The persistence literature blames executives' cognitive biases; governance theory nominates outside directors as the objective check; yet boards fail regardless of outsider representation, and the independence explanation lacks consistent evidence on exactly the outcome that matters.
- **Rising action:** The construct import (Abilene anecdote → quoted definition → attitude–behavior disjunction → performance-feedback trigger); the group-dynamics trunk is built (social risk → mutual-observation decision rule → lay dispositionism → spiral of silence); boards are shown to satisfy the engine's preconditions (low cohesion, high mutual observability of the boardroom); the outside-director scoping is defended on two grounds; H1–H5 follow, including two mediated-moderation hypotheses.
- **Climax:** Table 2: the misperception gap itself — directors' own concern (6.80) versus their perception of others' concern (4.77) at low-performing firms, a highly significant difference robust across four Heckman models — plus the H2 interaction showing the gap widens as prior expressed concern falls. The construct's defining delusion is now a number.
- **Falling action:** H3–H4: friendship ties and demographic homogeneity (three of four attributes) shrink the gap to non-significance, mediated by expressed concern (Sobel z = 2.15–2.39); H5: the concern × perceived-non-concern interaction predicts both diversification outcomes, dies when expressed concern enters, and survives IV robustness; the premise survey (500 directors) confirms the social-risk foundation.
- **Denouement:** The Discussion reinterprets the governance puzzle (weak boards despite independence), inverts the reform prescription (process over structure), discloses the diversity side effect, extends to Enron-era silence on wrongdoing, and elevates the finding into a two-failure taxonomy: persistence from individual bias (executives) and persistence from group misperception (boards) — with groupthink as the contrast case.

### Tension

- **Source:** The gap between individual virtue and group outcome. Every element the governance literature trusts — objectivity, independence, information — is present in the boardroom, and the paper's own data confirms directors privately hold the "right" belief; the failure is located one level up, in what they believe about each other.
- **Construction:** The tension is never argued abstractly; it is built into the rival explanation's own evidence record (works for compensation, fails for strategy) and then into the measurement design — because own concern and perceived others' concern are elicited on the same scale from the same board, the story's central delusion becomes a single testable difference. The Abilene anecdote supplies the emotional preview of the mechanism before any hypothesis is stated.

### Alternative readings

- **author_signaled_alternative:** Pluralistic ignorance might be less pronounced among inside directors (they report less concern, and their friendship networks are denser); the authors present descriptive survey evidence to this effect and speculate that it may still occur in peripheral top-management subgroups — a boundary they flag rather than resolve.
- **analyst_counterfactual:** The headline gap could partly reflect scale-use asymmetry (self-ratings versus other-perceptions) or social desirability rather than pluralistic ignorance proper; the authors partially pre-empt this with interrater agreement among directors (kappa > .75, ICC = .90), individual-level analyses with bootstrapped standard errors, and the premise-validation survey — but the attribution step (reading silence as agreement) remains unobserved, so a perceptual-measurement replication would be the modern test.

## Story Assessment

- **Theme coherence:** `works` — one question (why objective monitors fail to convert private concern into voice) organizes the hook, the imported mechanism, the measurement design, all five hypotheses, and both outcome dimensions; nothing in the paper is off-theme.
- **Character discipline:** `works` — pluralistic ignorance is a concentrated protagonist; expressed concern is a genuine hinge character rather than a generic mediator (the theory says why voice matters before the results show it); the moderators carry genre-inverting roles that are explained, not decorative; the executive stays convincingly offstage.
- **Knot integrity:** `works` — the rival independence explanation is given real evidence before being rebutted, so the knot ("why do even independent boards fail?") is a genuine unresolved challenge rather than a straw man.
- **Plot emergence:** `works` — the design arises from the construct: a group-level misperception is operationalized as the same-scale own-versus-perceived concern difference, the aspiration-level premise motivates the low-performance subsample, and the mediation structure follows from the spiral-of-silence trunk rather than being bolted on.
- **Tie–unravel alignment:** `works` — the front end promises how and why the bias occurs, when it is worse, and what it costs; every promise is cashed as H1–H5 in the promised order, with the level-of-analysis complementarity (board-level primary, individual-level Appendix B) consistent with the theory's group-level definition (PDM flag C3, no conflict). The one looseness — the interior attribution mechanism is unmeasured and the premise survey is a separate sample — is calibrated as `partly_probed` without breaking the story promise.
- **Ending quality:** `works` — the ending transforms the opening question: from "why do boards fail" to "which kind of decision failure is this," inverts a live policy prescription (SOX independence → process reform), and discloses an uncomfortable corollary about diversity. The long future-research catalogue and the post hoc insider evidence are 2005-era padding, noted as craft caveats, not story failures.
- **Boundary:** This evaluates storytelling only — not causal identification, survey validity, or journal value. The era risks from the introduction distillation's narrative_risk_ledger (R1 generic stakes; R2 sentence-stuffed quotations; R3 fat-suit opening; R4 actor-less hook) and the C3 level-complementarity info flag were fed into section caveats and this boundary note; they do not downgrade the story's architecture.

## Learning Affordances

### Introduction

- **Suitable:** `yes`
- **Learn:** (1) Steelman-then-double-rebut: concede the rival explanation's partial evidence in adjacent domains, then rebut twice on the focal outcome (missing evidence + direct contrary evidence), and pivot with a single sentence that names the new explanation — friction is minimized because the attack targets an explanation's reach, not the literature's worth. (2) The construct-teaching lens paragraph: anecdote → quoted definition → named consequence → trigger bridge, so readers who have never heard of pluralistic ignorance can follow every later hypothesis.
- **Do not copy:** The 2005 prose budget (270-word opening paragraph, 106-word quoted sentences, generic "critical gap" stakes, no concrete actor in the hook) is era-typical and would fail modern front-page standards; the tension architecture transfers, the paragraph economics do not.

### Theory

- **Suitable:** `yes`
- **Learn:** (1) Build the mechanism engine once in its home discipline (social risk → decision rule → attribution asymmetry → spiral), then show the focal setting satisfies its preconditions (low cohesion, high mutual observability) — every subsequent hypothesis becomes a branch of the same trunk, giving five hypotheses one voice. (2) Rival-construct opposing-sign disambiguation: name the neighboring failure mode (groupthink) and show the identical moderator carries the opposite sign, converting a confound into an adjudication.
- **Do not copy:** The trunk's attribution step and the group-level construct definition are imported on citations plus a personal communication; a modern version must validate the level claim (the paper defers this to Methods) and measure the interior mechanism, not just its behavioral shadow.

### Methods

- **Suitable:** `partial`
- **Learn:** Premise validation as design element — the theory's assumed foundation (directors perceive social risk in unshared dissent) is tested with a separate 500-director survey, turning an assumption into evidence. Construct-definition-to-aggregation alignment — rwg/ICC justify aggregating exactly where the theory placed the construct.
- **Do not copy:** The common-instrument measurement of own concern and perceived others' concern from the same respondents is the era's convenience; without interrater guards and individual-level replications it would not survive modern common-method scrutiny — do not import the entanglement.

### Results

- **Suitable:** `yes`
- **Learn:** (1) Stage the climax on the construct's defining number — the misperception gap (6.80 vs. 4.77) lands before any moderator or consequence, so the reader has seen the delusion before being told its causes and costs. (2) Nested-mediation choreography: interaction-dies-when-mediator-enters, Sobel quantification, IV robustness, and a premise check (non-linear concern, t = 8.35) placed ahead of the main tests — the same confirmatory pattern repeated per hypothesis so the story's rhythm is audible.
- **Do not copy:** One-tailed tests, no economic-magnitude beat, and causal verbs outrunning a survey design are era presentation; a modern staging needs AMEs/magnitudes and disciplined language.

### Discussion

- **Suitable:** `yes`
- **Learn:** (1) Policy-inversion ending: use the mechanism to overturn the reform logic the reader arrived with (independence → process), so the ending changes the action, not just the belief. (2) Corollary disclosure: volunteer the implication that hurts a favored narrative (diversity side effects) and offer the mechanism for an external puzzle (board silence on wrongdoing) — the discussion becomes new evidence for the theory.
- **Do not copy:** The post hoc insider-director descriptive comparison and the multi-paragraph future-research catalogue are 2005 conventions; a modern ending keeps the inversion and the corollary, and cuts the padding.

## Comparison prompt

Read this card against westphal1998 (Westphal & Zajac): both stories turn on a belief held about others — investors reading symbolic adoption as substance there, directors reading silence as agreement here — and both are Westphal moving the same investigative lens across the boardroom table. Ask: what does each paper need the reader to give up (the "hard numbers" reading of market reactions; the independence prescription of governance theory), and how does each design manufacture the single number (unimplemented-plan returns; the 6.80-versus-4.77 gap) that forces the surrender?
