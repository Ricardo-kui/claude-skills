# Story Learning Card — Gulati and Higgins (2003, Strategic Management Journal)

## Metadata

```yaml
schema_version: "4.0-lite"
id: gulati2003-which-ties-matter
paper:
  citekey: gulati_higgins_2003_which_ties_matter
  title: "Which Ties Matter When? The Contingent Effects of Interorganizational Partnerships on IPO Success"
  outlet: "Strategic Management Journal"
  year: 2003
  publication_status: published
  paper_type: quantitative
  source_version: publisher_pdf
  inclusion_rationale: "A canonical whole-paper exemplar of a pure-moderation story: a monotonic embeddedness axiom conditionalized along two dimensions (which ties x when), a decision-theoretic moderator that earns independent theoretical identity before any branch is built, and three isomorphic trunk-branch hypotheses resolved by a per-hypothesis verdict chain (H1/H2 supported, H3 not). Useful for studying how a 2x3 contingency promise is staged, paid off, and partially left dangling. Held distinct from the sister-paper card higgins2003 (Higgins & Gulati, Organization Science 2003): same authors, year, and biotech-IPO arena, but an antecedent-origins story, not this contingency story. Era-typical craft (no magnitude beats anywhere, no exclusion restriction, H3 null never explained) is held as contrast, not as model."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "PDM materialized slices: gulati_higgins_2003_which_ties_matter.pdm/sections/{introduction,theory,methods,results,discussion}.md (OCR import of the published SMJ 24(2):127-144 article; Tables 1-2 present)"
    - "Verified section distillations: sections/introduction.json, sections/theory.yaml, sections/methods.json, sections/results.yaml (L2, cross_section_identity coherence=ok, no flags)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: null
mechanism_evidence:
  status: partly_probed
  basis: "What is tested is the predicted interaction geometry: the equity-index interaction is negative for VC prominence (H1), positive for underwriter prestige (H2), and null for alliances (H3). That differential sign pattern is consistent with the attention-switching engine and does discriminate against a uniform signal-premium account, but investor attention and the two error concerns are never measured, H3's failure weakens the discriminant test, and the Heckman first stage carries no exclusion-restriction argument."
classification:
  theoretical_problem_form: [boundary-gap, axiomatic-consensus-conditionalized, typology-decomposed-signaling]
  narrative_dynamics: [paired-question-reframe, moderator-first-architecture, common-trunk-parallel-branches, isomorphic-branch-hypotheses, pre-registered-criterion-beat, verdict-order-variation, unexplained-null-thread]
  retrieval_signals: [contingent-value-of-ties, embeddedness-boundary, investor-attention, endorsement-signaling, ipo-success, hot-cold-markets, heckman-selection, moderation-interactions]
  confidence: provisional
section_learning:
  introduction:
    suitable: "partial"
    requires: [monotonic-axiom-with-citable-counter-evidence]
    learn:
      - "Conditionalize a monotonic axiom instead of attacking it: quote the shared axiom (more embeddedness is 'better'), then challenge it concessively — 'the conditions under which more is indeed better' — so the contribution is a Boundary claim that keeps the baseline literature as an ally, and pair it with a dimension-specific gap sentence ('has not examined if and when') that names both the existence and the condition of the omission."
      - "Front-load a stakes paragraph before the full research question, anchored to citable counter-evidence (ties can have deleterious effects) and closed with dual beneficiaries (scholars enriched; entrepreneurs negotiating market conditions), forming a Gap(light) -> Stakes -> Gap(heavy) sandwich that justifies the undertaking before aiming it."
    caveat:
      - "The cold-start trend hook carries no actor and no number — nine sentences elapse before the puzzle lands — so a modern adapter should add one concrete anchor behind the consensus opening."
      - "The 'challenges this basic assumption' phrasing stays honest only while the concession is real (when, not no); copied without a true conditional finding it drifts into an Inadequacy claim the design cannot cash, and the 233-word paragraph carrying lens, typology, moderator, and mechanism at once is an overload to avoid."
  theory:
    suitable: "yes"
    requires: [moderator-decomposable-into-evaluator-concerns, multiple-signal-sources-sharing-one-mechanism]
    learn:
      - "Build the moderator before the branches: give it an independent theoretical identity (market conditions decomposed decision-theoretically into investors' two error concerns — gullibility in hot markets, blindness in cold — grounded in the attention-based view), so the branch section only has to map each signal-maker onto the concern it best resolves and readers learn the engine once."
      - "Run three isomorphic branches with a fixed internal rhythm — baseline literature, challenge the uniformity assumption (not the conclusion), signal-maker attention alignment, concession-wrapped 'Therefore, while ... we expect ... particularly when' convergence, hypothesis — then lock the whole framework in a 2x3 prediction matrix figure at the close."
    caveat:
      - "H2's opposite pole is argued by thin contrast inference (banks switch into hot markets) where H1/H3 receive full bilateral mechanisms — every branch needs at least one mechanism sentence per pole; the alternative explanation that all signals carry a premium in cold markets is never adjudicated."
      - "The Type I/II labels are used opposite to statistical convention and must be locally redefined if the dual-error trunk is borrowed, and the moderator is named with three interchangeably used terms (uncertainty, receptivity, favorability) — copy neither habit."
  methods:
    suitable: "partial"
    requires: [outcome-observable-only-for-a-subset]
    learn:
      - "Engineer the risk set around the estimator's first stage: because the Heckman probit needs firms that did not go public, assemble public firms (with non-survivors actively recovered so survivorship does not bias the frame) plus never-public and dead private firms into an auditable funnel (281 + 18 + 468 + 91 = 858), with a because attached to every addition."
      - "Introduce selection correction in plain language — the outcome exists only if a firm goes public, so an unmodeled factor could account for observability — then disclose first-stage covariates and first-stage quality (73 percent correct classification) and add the SE-scope honesty note (estimates over the full risk set; errors reflect the 299 observable firms)."
    caveat:
      - "The first stage carries no exclusion-restriction argument and the interaction-term construction is never declared in Methods — both era flags a modern adapter must repair, not inherit."
      - "The textbook-style procedure walkthrough and the absent Methods-to-Results transition are 2003 conventions, not moves to copy."
  results:
    suitable: "partial"
    requires: [pre-stated-sign-criterion-for-continuous-moderator, hypothesis-verdict-reporting]
    learn:
      - "Stage a per-hypothesis verdict flow with a pre-registered criterion beat before the first verdict (map the continuous moderator's endpoints onto the predicted interaction sign: a cold-to-hot index means support for H1 requires a negative interaction), and vary the verdict order across hypotheses (restatement-first for H1, verdict-first for H2 and H3) so the chain does not read mechanically."
      - "Keep nulls inside the verdict chain unsoftened (verdict, then the null interaction, then the null main effect), insert a two-sentence saturated-model survival check as a lightweight robustness beat, and close with a tandem coda that subordinates main effects to the interaction evidence and returns to the title's paired question (what types x when)."
    caveat:
      - "There is not a single magnitude beat in the section — no coefficients, intervals, or economic significance appear in the text, so 'particularly beneficial' is never shown in interpretable terms; a modern Results must repair this with simple slopes, conditional effects, or an interaction figure."
      - "Main effects are still independently interpreted despite significant interactions, rescued only by the closing tandem sentence — do not import that ordering."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Reopen the opening paired question with the differential answer, then transform it twice: into a boundary contribution for embeddedness theory (contingency established for firms pursuing organizational goals, extending an interpersonal-level turn) and into a reconceptualization of uncertainty (exogenous, multidimensional, acting through third-party stakeholders' attention rather than the focal firm's)."
      - "Convert limitations into defenses and avenues: the single-industry limit becomes a 'strong situation' argument for testing the mechanism, and the time-bound institutional contrast (banks entering private equity) becomes a named future-research target rather than an apology."
    caveat:
      - "The H3 null is restated in the opening paragraph and never explained — no candidate reasons for why alliance ties lack contingent value are offered anywhere in the ending; a modern Discussion should process its own failed hypothesis (the sister paper does, for its H1 null)."
      - "The closing 'positively affect' phrasing slightly outruns the selection-corrected, associational design."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
  writeback_gate: "confirmed_auto_write — user pre-authorized batch writeback for this distillation run (2026-09-06); card-confirmation gate passed by the distilling agent after full reading of all five slices plus the verified section distillations"
```

## Story Reading

### Theme question

Are the benefits of a young firm's prominent interorganizational ties uniform — or does *which* tie matters depend on *when*, that is, on the uncertainty prevailing in the equity market at the moment the firm goes public?

### Whole-story synopsis

The paper opens inside the embeddedness consensus: economic action is socially embedded, and ties to prominent actors have been generally touted as beneficial. The consensus is quietly incomplete — interpersonal-network scholars have already begun to show that tie value varies with the situation, ties can even have deleterious effects, and yet the interorganizational side has not asked if and when tie effects vary. Stakes arrive before the research question: the contingency matters for scholars (it specifies the conditions under which networks affect performance) and for entrepreneurs (who must negotiate market conditions). The question is then named as a paired question — which ties matter when — in the IPO context. The theory gives the moderator an independent identity before any tie is examined: equity market uncertainty is decomposed, decision-theoretically, into investors' two error concerns (investing in bad firms versus missing good ones), grounded in the attention-based view. Three tie-type branches then run isomorphically — each establishes the baseline signal, challenges the field's uniformity assumption, argues that the signal-maker attends most carefully to the IPO market in one regime (VCs scrutinize best in cold markets; prestigious banks engage when markets are hot; pharma partners evaluate most carefully when funding is scarce), and converges on a conditional hypothesis. Figure 1 locks the 2x3 prediction matrix. The methods assemble the empirical arena: an 858-firm risk set engineered so the Heckman first stage is estimable (281 public firms plus 18 recovered non-survivors, 468 never-public firms, 91 dead private firms), list-based prominence measures, Lerner's equity index read at event-time, a composite IPO-success measure, and a plain-language preflight of the selection correction. The results deliver the answer as a per-hypothesis verdict chain with varied verdict order and a pre-registered sign criterion: H1 supported (negative VC-by-index interaction — VC ties pay in cold markets), H2 supported (positive underwriter-by-index interaction — bank ties pay in hot markets), H3 not supported (the alliance interaction and its main effect are both null); a saturated Model V survival check confirms H1/H2, and a tandem coda folds the main effects back under the which-by-when answer. The discussion reopens the paired question, converts the differential answer into two theory extensions (a firm-level contingency turn for embeddedness; uncertainty as multidimensional and exogenous, acting through third parties), proposes follow-ups on tie content, closeness, syndicate structure, and institutional change, defends the single industry as a strong situation, and closes on the two contingency dimensions — while the alliance null, restated but never explained, remains an open thread in the weave.

### Characters and storylines

- **Main character:** the tie type — the young firm's portfolio of prominent partnerships, decomposed into endorsement ties (prominent VCs, prestigious investment banks) versus strategic alliances with major pharmaceutical/health-care firms — because its value is the contested object the whole story is organized to re-specify.
- **Co-protagonist:** equity market uncertainty (hot versus cold) — unusual in that the moderator earns its own theoretical identity (the dual-error decomposition) before any branch is built, so it can plausibly re-sort the other characters' value.
- **Supporting characters:** investors' two error concerns, the decision-theoretic engine that turns abstract market conditions into a switching attentional lens; the signal-makers' attention (VCs overloaded in hot markets, banks migrating into hot markets, pharma partners courted hardest in cold markets), which aligns each signal with one regime; and IPO success, the composite financial stake that makes tie choice consequential.
- **Storyline 1 (which):** tie types carry different signals because their makers evaluate young firms under different conditions; **Storyline 2 (when):** the market regime switches which error dominates investors, re-weighting every signal at once. The storylines intersect cell by cell in the 2x3 matrix — two cells confirm the design, and the third (alliances in cold markets) fails without a repair scene.

### Five acts

- **Exposition:** the embeddedness axiom is established and quietly cracked — interpersonal contingency findings and documented deleterious tie effects against interorganizational silence; stakes are front-loaded with cited counter-evidence; the paired question lands as an appositive ("which ties matter when").
- **Rising action:** the moderator is built first (market uncertainty into two error concerns, under the attention-based view); three isomorphic branches each run baseline-uniformity-challenge-attention-alignment-concession to a conditional hypothesis; Figure 1 locks the 2x3 matrix; the methods raise the arena — survivorship-repaired risk set, prominence lists, event-time Lerner index, composite DV, Heckman preflight.
- **Climax:** the Table 2 verdict chain — H1 supported through a pre-registered sign criterion, H2 supported (with the underwriter main effect robust across models), H3 not supported with a double null; verdict order varies paragraph to paragraph; Model V's saturated survival check closes the family.
- **Falling action:** thin by design — controls and main effects are summarized after the verdicts (underwriter prestige consistently positive; VC prominence marginal), then the tandem coda subordinates that material to the interaction evidence and returns to the title's paired question.
- **Denouement:** the discussion restates the differential answer, transforms it into boundary contributions and a multidimensional view of uncertainty, sets future-research avenues, reframes the single-industry limit as a strong situation, and ends on the two contingency dimensions — leaving the alliance null explained nowhere.

### Tension

- **Source:** a genuine crack inside a consensus rather than a personified opponent — the field's own axiom (more ties are better) is contradicted by cited deleterious-effects evidence and by an adjacent interpersonal-network literature that had already begun conditionalizing tie value, while the interorganizational side had not asked the question at all.
- **Construction:** the paper makes the crack legible by decision-theoretic personification of the audience — investors worry about either gullibility or blindness — so "market conditions" becomes two concrete error concerns; the 2x3 matrix then converts the tension into cell-level predictions whose mixed confirmation (two cells supported, one failed) keeps the outcome genuinely in doubt rather than rhetorical.

### Alternative readings

- **author_signaled_alternative:** the discussion itself warns that institutional change — banks entering the private equity market with VC-like due diligence — "dilute[s] the contrast set forth in the present research"; under that reading the H1/H2 timing contrast is period-bound (1979-96) rather than a stable feature of endorsement markets.
- **analyst_counterfactual:** sorting rather than signaling could carry the story — prominent partners select better firms in ways the Heckman correction (which handles selection into going public, not partners into firms) does not remove; and because a uniform cold-market signal premium was never explicitly adjudicated, the alliance null cannot cleanly separate "no contingency" from "the attention-alignment mechanism does not describe alliance partners." Analyst-generated; asserted by neither author.

## Story Assessment

- **Theme coherence:** `works` — the paired question organizes the introduction's relay, the trunk-branch theory, the matrix figure, the verdict chain, and the discussion's extensions; every section serves either the which-by-when question or the apparatus that answers it.
- **Character discipline:** `works` — tie type and market regime stay distinct, the dual-error concerns serve the moderator, and no stray storyline appears; the alliance branch is a legitimate character that fails on stage, not a distraction.
- **Knot integrity:** `works` — the challenge is the field's own axiom plus documented counter-evidence, and the 2x3 design makes it plausibly addressable within one study.
- **Plot emergence:** `works` — the dual-error trunk generates the branch mapping, the measures follow the constructs (list-based prominence, event-time index), and the verdict chain reads directly off the promised matrix; no section forces a plot the constructs do not generate.
- **Tie–unravel alignment:** `partly_works` — two of three promised cells are answered with a pre-registered criterion and a survival check, but the third (H3) unravels with no explanation offered in Results or Discussion; the evidence carries no magnitude or conditional-effect display, so "particularly beneficial" is never shown in interpretable terms; and the attention mechanism is inferred from the interaction pattern, not observed.
- **Ending quality:** `works` — the ending returns to the paired question with changed understanding (contingency as a boundary contribution; uncertainty as multidimensional and third-party), converts limitations into defenses and avenues; its blemish is processing the null by restatement only, never by explanation.
- **Boundary:** This evaluates storytelling only — not research quality, identification, or journal value.

## Learning Affordances

### Introduction

Use this card when a writer must conditionalize a mature, monotonic consensus rather than refute it. The transferable moves are the concessive axiom-conditionalization contribution (challenge the *when*, keep the baseline as ally, paired with a dimension-specific "if and when" gap sentence) and the counter-evidence-anchored stakes paragraph front-loaded before the full research question. Do not copy the actor-free trend hook, the unconceded use of "challenges this basic assumption," or the four-job mega-paragraph.

### Theory

Use this card when a study has one moderator that can be decomposed into a decision-maker's distinct concerns and several signal sources that share one alignment mechanism. The transferable moves are moderator-first architecture (earn the moderator's independent theoretical identity so branches only map) and isomorphic branch rhythm with concession-wrapped convergence and a closing matrix figure. Do not copy the thin opposite pole in H2, the inverted error-type labels, the three-way naming drift of the moderator, or the unadjudicated uniform-premium alternative.

### Methods, Results, and Discussion

The paper is useful for structural staging: a risk set engineered around the estimator's first stage with a plain-language observability-selection preflight; a verdict flow with a pre-registered sign criterion, varied verdict order, unsoftened nulls, and a saturated-model survival check; and an ending that transforms the answer into boundary contributions while converting limitations into avenues. Its mechanism calibration is `partly_probed`: the interaction geometry fits attention-switching, but attention is unmeasured and the first stage lacks an exclusion argument — borrow the staging, not the evidentiary confidence. The Results' total absence of magnitude beats and the never-explained H3 null are era-era contrast material, not moves.

## Comparison prompt

Read this card with `higgins2003` (Higgins & Gulati, Organization Science 2003) — same authors, same year, same biotech-IPO arena, opposite story grammars: an antecedent-origins relay there, an axiom-conditionalization contingency here. Ask: what does each gap type demand of the rest of the paper, and which grammar survives a partial result better — the origins story that explains its null on the spot, or the contingency story that leaves one promised cell unexplained?
