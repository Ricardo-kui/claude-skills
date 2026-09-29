# Story Learning Card — Giannetti and Srinivasan (2022, *Journal of the Academy of Marketing Science*)

## Metadata

```yaml
schema_version: "4.0-lite"
id: giannetti2022-lobbying-product-recalls
paper:
  citekey: giannetti_2022_corporate_lobbying_and_product_recalls_an_inv
  title: "Corporate lobbying and product recalls: an investigation in the U.S. medical device industry"
  outlet: "Journal of the Academy of Marketing Science"
  year: 2022
  publication_status: published
  paper_type: quantitative
  source_version: unknown
  inclusion_rationale: "A clean whole-paper instance of a two-step mechanism story (counterintuitive harm carried by a two-path mediator) whose moderated-mediation promise made in the introduction is fully redeemed in the results, including honest staging of a failed moderator hypothesis."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "giannetti_2022_corporate_lobbying_and_product_recalls_an_inv.pdm/sections/introduction.md"
    - "giannetti_2022_corporate_lobbying_and_product_recalls_an_inv.pdm/sections/theory.md"
    - "giannetti_2022_corporate_lobbying_and_product_recalls_an_inv.pdm/sections/methods.md"
    - "giannetti_2022_corporate_lobbying_and_product_recalls_an_inv.pdm/sections/results.md"
    - "giannetti_2022_corporate_lobbying_and_product_recalls_an_inv.pdm/sections/discussion.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: null
mechanism_evidence:
  status: partly_probed
  basis: "Both paths are estimated (RE probit a-path on ISO 13485 certification; RE negative binomial b-path on recall counts), the indirect effect is bootstrapped via GSEM, and the index of partial moderated mediation is significant for two moderators; but the mediator is a binary certification proxy for a theorized graded internal state, and the authors concede partial mediation, i.e., unmeasured channels remain."
classification:
  theoretical_problem_form: [counterintuitive-self-harm-from-protective-investment, two-stream-omission-crosspoint, second-stage-moderated-mediation]
  narrative_dynamics: [double-edged-sword-reversal, institutional-primer-seeds-moderator, sign-arithmetic-makes-moderated-mediation-derivable, null-converted-to-sharpened-claim, heterogeneity-reconciles-mixed-effects]
  retrieval_signals: [corporate-lobbying, product-recalls, product-safety-emphasis, iso-13485-certification, marketing-ceo, moderated-mediation, medical-device-approval-tracks]
  confidence: provisional
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Build an incompleteness gap at the cross-point of two mature streams by naming each stream's systematic omission of the other's outcome (corporate political activity studied only through financial outcomes; recall antecedents studied only at the organization level), then fix the exact unclaimed territory with a single-paper predecessor whose stated limitation — a main effect with no firm heterogeneity — is precisely what the new paper adds."
      - "Make a three-part preview promise (mechanism finding, moderated-mediation architecture, named data sources with panel dimensions) that the results section can be audited against item by item."
    caveat:
      - "The introduction states the direction of every hypothesis as a finding before the theory section argues for it; this works only because the theory can still earn each sign and the results redeem each promise. The data-source enumeration transfers only where sources are publicly nameable and stable."
  theory:
    suitable: "yes"
    requires: ["moderator variation must be grounded in an institution or an established micro-theory, not introduced for symmetry"]
    learn:
      - "Plant an institutional primer (the FDA's 510(k) vs PMA dual-track approval system) before the hypotheses so a later moderator (radical vs incremental innovation focus) reads as context-native, and let the same primer do interpretive work again in the results (the negative main effect of radical-innovation focus)."
      - "After each moderated-mediation hypothesis pair, disclose the sign arithmetic — the product of the negative a-path and the interaction's sign — so the reader can pre-compute what the later index of moderated mediation will show; this converts a statistical product into a narratively derived prediction."
    caveat:
      - "The story's engine character is theorized as a graded internal state (emphasis on product safety) but the design can only stage a binary certification; adopting this structure requires a mediator whose measure matches its narrative grain, or an explicit signal of the gap."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Let the lag structure carry the mediation story: X at t-2, M at t-1, Y at t staggers the causal clock inside the design itself, and the switch to random effects is disclosed with its reason (never-certifying and never-recalling firms) rather than made silently."
    caveat:
      - "Coefficients are never translated into recall-count magnitudes (no average marginal effects or economic significance), so the staging never shows how large the harm is; the identification defense (control function) is deferred to appendix-level robustness with the first stage available only upon request."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage the column walk to mirror the theory's build-up (base model, then add the mediator, then add the interactions) so each hypothesis owns a dedicated coefficient and the reader watches the plot assemble rather than receive a table dump."
      - "Give the failed hypothesis (R&D CEO) equal staging, then design a follow-in analysis (CMO, CSO, and TMT power) whose own null interactions convert the failure into a sharpened claim about the CEO's unique role."
    caveat:
      - "Mediation and moderated mediation are established through significance patterns and bootstrapped intervals without quantifying the indirect effect's magnitude; the column-walk staging depends on hypotheses being grouped by narrative stage, not by estimator convenience."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Return to the opening's mixed-evidence literature and convert the story into a reconciliation principle (incorporating firm heterogeneity into empirical testing), so the ending explains the field's conflicting findings rather than re-summarizing this paper's coefficients."
      - "Route the unexplained direct effect into a concrete future-mediator map (easier FDA approvals), and use the non-FDA lobbying analysis (indirect-only mediation) as evidence for where the remaining mechanism lives."
    caveat:
      - "One managerial implication leans on interpreting a null main effect (marketing CEO) through a conjecture about CEOs balancing functional priorities; generalization is explicitly bounded to a single regulated industry."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
```

## Story Reading

### Theme question

Does corporate lobbying — the tool firms buy to protect themselves in their regulatory environment — quietly endanger the firms that use it: does lobbying increase the number of a firm's product recalls, and does a lowered emphasis on product safety carry that harm?

### Whole-story synopsis

The paper opens at the junction of two mature literatures that each omit the other's object: corporate political activity research follows lobbying into shareholder value and risk but not into marketing-relevant outcomes, while the product-recall antecedents literature catalogs organization-level drivers — learning, R&D intensity, CEO traits, CMO presence — but not political ones. A single predecessor found a lobbying–recall main effect and left firm heterogeneity unexamined; that stated limitation becomes this paper's exact territory. The story then turns counterintuitive: lobbying, purchased as protection, builds privileged relationships with regulators, breeds complacency, lowers the firm's emphasis on product safety in new product development, and thereby raises recalls — a double-edged sword in which the harm travels through an internal character the firm itself controls. Three heterogeneity characters then enter at the second stage of the mediated path: a marketing CEO, who treats brands and customers as assets to be safeguarded and so amplifies the protective power of safety emphasis; an R&D CEO, hypothesized to prioritize technological sophistication and so attenuate it; and the firm's focus on radical versus incremental innovation, grounded in the industry's dual approval tracks, under which incremental products face no rigorous pre-market testing and safety emphasis matters most. The design stages the story in time — lobbying at t−2, safety emphasis at t−1, recalls at t — across 86 U.S. medical device firms and 696 firm-years, 2005–2018. The results assemble in step with the theory: lobbying raises recalls, safety emphasis lowers them, the marketing CEO interaction and the radical-innovation interaction are significant, and GSEM bootstrapping with the index of partial moderated mediation confirms both indirect effects — while the R&D CEO fails its test. The falling action isolates the CEO's uniqueness through null CMO/CSO analyses and fortifies the story with endogeneity and reverse-causality checks. The ending converts the whole plot into a reconciliation principle: the lobbying–performance literature's positive, negative, and null findings may coexist once heterogeneity is modeled, and the unexplained direct effect is handed to future work as a mapped, testable mechanism.

### Characters and storylines

- **Main character:** corporate lobbying (X) — the paradoxical protagonist, an expenditure undertaken for protection that the story argues becomes a self-inflicted hazard.
- **Engine character:** emphasis on product safety (M, staged as ISO 13485 certification) — the internal character whose erosion transmits lobbying's harm into recalls; the hinge of the double-edged sword and the locus of both moderators' work.
- **Supporting characters:** the marketing CEO, an amplifier of safety emphasis's protective power; the R&D CEO, a hypothesized attenuator that fails its test; the focus on radical versus incremental innovation, an institutionally grounded attenuator.
- **Setting character:** the FDA — simultaneously regulator, designer of the 510(k)/PMA dual-track stage, lobbying target, and the relationship whose privilege the mechanism presupposes.
- **Predecessor character:** Rayfield and Unsal (2019), the edge of the known plot whose main-effect-only finding defines what remains to be told.
- **Storyline 1 (harm transmission):** lobbying → privileged regulator relationships → complacency → lower safety emphasis → more recalls.
- **Storyline 2 (heterogeneity):** upper-echelons characters (CEO functional backgrounds) enter the b-path's second stage and determine where the harm concentrates.
- **Storyline 3 (institution):** the 510(k) vs PMA tracks motivate the industry setting, underwrite the innovation-focus moderator, and return in the results as an explanation of the moderator's own negative main effect.
- **Intersection:** storylines 2 and 3 meet inside storyline 1's second stage — the multiplication of the negative a-path and each interaction's sign is the point where character, institution, and plot become one number.

### Five acts

- **Exposition:** lobbying is pervasive and its performance effects are mixed (positive, negative, null); each of the two literatures systematically omits the other's outcome, and the lone predecessor stopped at a main effect.
- **Rising action:** the two-step mechanism is built (H1a/H1b); three heterogeneity characters enter at the second stage (H2, H3, H4), with the institutional primer making the third context-native.
- **Climax:** the Table 3 column walk — lobbying raises recalls, safety emphasis lowers them, the marketing CEO strengthens and the radical-innovation focus weakens the safety–recall link; GSEM bootstrap and the index of partial moderated mediation confirm both indirect effects; the R&D CEO is null.
- **Falling action:** CMO/CSO and TMT-power analyses return null interactions, sharpening the CEO's unique role; robustness checks (control function, Granger tests, recall class and root cause, decay alternatives) hold the plot in place; non-FDA lobbying shows indirect-only mediation.
- **Denouement:** heterogeneity reconciles the mixed lobbying–performance evidence; the marketing CEO reframed as "bringing customers into the boardroom"; a cautionary note for incremental innovators; the residual direct effect mapped to a future FDA-approval mechanism.

### Tension

- **Source:** a genuine paradox — the firm buys lobbying as protection, yet the story claims it invites harm; and the harm's conduit (regulatory leniency) is invisible, so the damage must be shown traveling through an internal, observable character rather than asserted at the regulator's window.
- **Construction:** the "double-edged sword" framing; a named industry critic's quote about watered-down approval standards; the 510(k) institutional critique (most serious-hazard recalls were cleared through the less stringent track); and the moderated-mediation architecture, which lets the reader pre-compute where the harm should concentrate before the results confirm it.

### Alternative readings

- **analyst_counterfactual:** the same coefficients support a selection reading — lobbying firms are observably different (they average 10.94 recalls vs 1.63; certify at 0.32 vs 0.68; firm size correlates 0.63 with recalls), so a scale-and-capability story fits the data without the complacency narrative; the lag structure and control function constrain but do not eliminate this reading.
- **analyst_counterfactual:** the R&D CEO null may reflect sparse measurement (14% of CEO-years) as much as theory failure; the paper does not explore this, and its own follow-in analysis stays with the CEO-uniqueness storyline.

## Story Assessment

- **Theme coherence:** `works` — the question of self-inflicted harm through safety complacency organizes the two-stream opening, the mechanism middle, the moderated staging, and the reconciliation ending; the introduction's three-part preview is redeemed item by item in the results.
- **Character discipline:** `works` — the protagonist, engine, and three moderators have distinct narrative jobs; the near-duplicate characters (CMO, CSO, TMT power) are held back to the falling action and used only to sharpen the CEO's uniqueness, and the failed moderator is given honest space rather than buried.
- **Knot integrity:** `works` — the double-edged-sword paradox is a real challenge, and the predecessor's stated limitation fixes a genuine, bounded piece of unclaimed territory.
- **Plot emergence:** `works` — the moderators arise from upper echelons theory and the industry's approval-track institution rather than from symmetry; the sign arithmetic makes the moderated-mediation predictions derivable from the setup instead of imposed on it.
- **Tie–unravel alignment:** `works` — the evidence answers the whether-and-how question as staged, with partial mediation disclosed rather than hidden; the coarser unraveling (a binary certification standing in for a graded state, no magnitude translation) is an evidence-calibration limit, not a story misdirection.
- **Ending quality:** `works` — the discussion converts the plot into a reconciliation principle for a conflicting literature and routes its own residual (the direct effect) into a mapped future mechanism, changing rather than repeating the opening.
- **Boundary:** This evaluates storytelling only — not the validity of the ISO 13485 proxy, the identification strategy, or the paper's research quality or journal value.

## Learning Affordances

### Introduction

- **Suitable:** `yes`
- **Learn:** see `section_learning.introduction` — the two-stream omission cross-point with a predecessor-defined remainder, and the auditable three-part preview promise.
- **Do not copy:** the hypothesis directions are spent in the introduction before the theory earns them; and the industry-statistics and data-source enumeration paragraphs assume a regulated setting with publicly nameable sources.

### Theory

- **Suitable:** `yes`
- **Learn:** see `section_learning.theory` — the institutional primer that seeds a moderator twice, and sign-arithmetic disclosure that makes moderated mediation narratively derivable.
- **Do not copy:** the engine character's narrative grain exceeds its binary measure; do not import the mechanism story without a mediator whose operationalization matches what the prose promises.

### Methods

- **Suitable:** `partial`
- **Learn:** see `section_learning.methods` — the staggered mediation clock and the reasoned RE-instead-of-FE disclosure.
- **Do not copy:** the absence of effect-magnitude translation and the deferred identification defense are paper-specific choices a writer should not treat as the story's price.

### Results

- **Suitable:** `yes`
- **Learn:** see `section_learning.results` — the theory-mirroring column walk, and the null-then-follow-in staging that converts a failed hypothesis into a sharpened claim.
- **Do not copy:** mediation asserted from significance patterns without indirect-effect magnitudes; the staging requires hypotheses grouped by narrative stage.

### Discussion

- **Suitable:** `yes`
- **Learn:** see `section_learning.discussion` — the ending as reconciliation principle for a mixed literature, and the residual direct effect converted into a mapped, evidence-backed future mechanism.
- **Do not copy:** one managerial implication rests on interpreting a null with a conjecture; generalization is explicitly bounded to one regulated industry.

## Comparison prompt

Compared with `chen2009-recall-strategy-financial-value` — the corpus's other confirmed instance of the two-stream-omission cross-point gap with product recalls as outcome — how does each paper stage the mechanism between the political/strategic antecedent and the recall outcome (recall strategy choice vs safety-emphasis certification), and which staging matches the grain of the construct its introduction promised?
