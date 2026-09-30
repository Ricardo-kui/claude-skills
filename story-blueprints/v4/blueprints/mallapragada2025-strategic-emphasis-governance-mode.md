# Story Learning Card — Mallapragada, Bommaraju, Kumar & Pedada (2025, Journal of Marketing)

## Metadata

```yaml
schema_version: "4.0-lite"
id: mallapragada2025
paper:
  citekey: mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate
  title: "To Acquire or to Ally? The Impact of Strategic Emphasis on Governance Mode Choice"
  outlet: "Journal of Marketing"
  year: 2025
  publication_status: published
  paper_type: quantitative
  source_version: pdm_slices_v1
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate.pdm/sections/introduction.md"
    - "mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate.pdm/sections/theory.md"
    - "mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate.pdm/sections/methods.md"
    - "mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate.pdm/sections/results.md"
    - "mallapragada_2025_to_acquire_or_to_ally_the_impact_of_strate.pdm/sections/discussion.md"
    - "verified L2 section distillations: sections/{introduction,theory,methods,results}.json"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default front-weighted allocation kept. Results receive slightly more attention than the default payoff check only because fed L2 flags (H3 judged support at p<.10, untranslated probit coefficients, no simple slopes for interactions) are used as calibration input for the tie-unravel judgment."
mechanism_evidence:
  status: not_directly_tested
  basis: "The three asset attributes that drive the hazard mechanism (valuation ambiguity, modularity, adaptation frequency) are never measured; the supplemental transaction-risk mediation uses a global LIWC risk dictionary as proxy, not the named attributes."
classification:
  theoretical_problem_form: [silent-literature-import, asset-attribute-mechanism, dual-lens-convergence]
  narrative_dynamics: [absence-knot, convergence-as-confirmation, paired-actor-attenuation, corrected-headline-model]
  retrieval_signals: [governance-mode-choice, firm-level-antecedent-import, internal-external-actor-moderators, hazard-attenuation-moderation]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: [documented-but-undeveloped-allusion-in-target-literature]
    learn:
      - "Import a construct from an adjacent literature through a documented-but-undeveloped allusion: concede that the target literature has 'alluded pointedly' to the relevant factor without building it, which defends the gap against novelty objections and recasts the import as completion rather than invasion."
      - "Organize boundary conditions as a matched internal/external actor pair (a C-suite role inside, an information intermediary outside) announced in the preview, so each moderator's later entrance fills a pre-declared slot instead of reading as an afterthought."
    caveat:
      - "The allusion defense collapses if prior work already modeled the link rather than gesturing at it; the silence register also depends on the construct being genuinely absent, not merely renamed."
  theory:
    suitable: "yes"
    requires: [dual-lenses-predict-same-direction]
    learn:
      - "Specify an asset-attribute mechanism instead of asserting that asset classes differ: name the exact attributes (valuation ambiguity, modularity, adaptation frequency), let each independently generate a governance hazard, then sum the hazards into the main effect."
      - "Run dual-lens convergence as a marked result, not a ritual ('like TCE—but independent of TCE's safeguarding logic—RBV also suggests'), then apply the lenses unevenly to moderators (H2 from both lenses, H3 from TCE only) so the scope reduction displays honesty rather than symmetry."
    caveat:
      - "Convergence is an asset only while both lenses truly predict the same direction; divergence turns the same architecture into a visible contradiction. The attribute claims are argued from literature, not measured."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Stage a model-free preview (median-split contingency table with chi-square and ANOVA) before any specification so the headline hypothesis is visible in raw proportions."
      - "Present the endogeneity ledger as named threats, each with a dedicated cure and an explicit exclusion argument that strengthens as instrument granularity coarsens, rather than one shared appeal to exogeneity."
    caveat:
      - "The ledger is exemplary in form but incomplete in coverage: the declared interaction hypotheses are never operationalized in Methods (no interaction-term construction statement), and analyst coverage's own endogeneity never enters the ledger. Peer-prevalence IVs, LDA topics, and 2SRI specifics are study-bound."
  results:
    suitable: "partial"
    requires: []
    learn:
      - "Embed endogeneity corrections in the final nested model and declare it the only discussed model ('We discuss the results for M4'), converting robustness investment into main-test credibility in one sentence."
      - "Organize supplementary analyses as a threat battery—swap functional form, swap correction method, swap heterogeneity operationalization—each closed with a class-level 'inferences hold regardless of' statement; then elevate one control variable to a theorized mediator with second-link moderation for a second mechanism appearance."
    caveat:
      - "Calibration counterexample: probit coefficients are never translated into marginal effects or probability changes, and the H3 interaction is declared support at p<.10 with no simple slopes, AME, or figure—copy the staircase and threat battery, not the magnitude-reporting or support-language norms."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Close a two-literature story by naming each literature's 'atomistic' blind spot—what one lens cannot see alone—so the contribution is the amalgamation itself rather than an increment to either side."
      - "Reopen the performance loop promised by the Introduction with a compact event-study coda, letting the ending test the match payoff instead of restating coefficients."
    caveat:
      - "The event study appears only in the Discussion without its own setup, so its evidentiary weight is thin; some managerial implications (CMO retention questions) outrun what a choice model can warrant."
story_assessment:
  overall_role: partial_exemplar  # storytelling judgment only: the front end is exemplary—an allusion-hardened silence knot, an attribute-level mechanism from which moderators derivatively emerge, and dual-lens convergence staged as a finding; the results staging is the partial part—a headline moderation paid off at p<.10 with zero magnitude translation, making the card both a model and a calibration counterexample
  mode: single_read
```

## Story Reading

### Theme question

Does a firm's relative emphasis on value appropriation versus value creation—rooted in marketing versus R&D assets—push it toward acquiring rather than allying, and do an internal actor (CMO presence) and an external actor (analyst coverage) weaken that pull?

### Whole-story synopsis

The paper opens on a routine executive dilemma: growth comes through acquiring or allying, and CEOs use both at comparable rates, yet no account says when a firm's own strategic posture should favor one. The governance literature locates the choice in transaction-level trade-offs, but one prominent firm-level factor is missing—strategic emphasis, the relative reliance on harvesting value through marketing assets versus creating value through R&D assets. Evidence ties this emphasis to firm performance, while the governance modes through which the emphasis must travel to reach performance remain uncharted; the Introduction converts that absence into two questions and hardens it by noting that interfirm scholarship has pointedly alluded to firm-specific assets without building the link. The Theory then supplies the engine in two layers. An attribute layer turns the asset asymmetry into three governance hazards—brand equity is subjective and hard to value, holistic rather than modular, and demands frequent front-end adaptation—each of which makes alliances dangerous for appropriation-heavy firms. A lens layer runs the prediction twice: TCE derives internalization from safeguarding logic, RBV independently derives it from the tacit, sticky character of marketing know-how, and their convergence is staged as a finding. Two actors are then positioned to dissolve the hazards: a CMO inside the firm can tangibilize brand worth, screen partners, and broker tacit knowledge, while analysts outside can validate intangible assets and stifle partner opportunism. Random-effects probit estimates on 6,581 U.S. transactions, with endogeneity corrections embedded in the headline model, confirm the pull toward acquisitions and its CMO attenuation; the analyst attenuation is confirmed only marginally. Supplementary batteries swap specifications without moving the inferences, and transaction risk is elevated to a mediator that gives the CMO a second role as risk shield. The Discussion returns to the opening with the landscape changed: each literature's blind spot is named and repaired, the first attribute-level differentiation of marketing versus R&D assets is claimed, and an event study closes the performance loop the Introduction opened.

### Characters and storylines

- **Main character:** strategic emphasis, the firm-level orientation toward value appropriation versus value creation, whose governance consequence is the story's unknown.
- **Decision character:** governance mode choice, the acquire-or-ally binary into which the whole plot resolves.
- **Mechanism characters:** marketing versus R&D assets, specified through three attributes—valuation ambiguity, modularity, adaptation frequency—that generate the hazards doing the causal work.
- **Supporting characters:** CMO presence, the internal actor who tangibilizes, screens, and brokers; analyst coverage, the external actor who validates, legitimizes, and deters opportunism. They are introduced as a matched pair and attenuate rather than reverse the main pull.
- **Narrator characters:** TCE and RBV, twin lenses whose independently derived agreement is itself a plot point, and whose uneven application to the moderators (both for H2, TCE only for H3) marks the theory's honesty.
- **Storyline 1 (hazard):** appropriation emphasis means marketing assets; marketing assets carry ambiguity, low modularity, and frequent adaptation; the hazards make alliances unsafe and internalization rational.
- **Storyline 2 (recombination):** marketing know-how is tacit and sticky; it transfers poorly across firm boundaries, so an appropriation emphasis is exploited more effectively inside the firm.
- **Intersection:** the two storylines converge on the same prediction from different premises, and both are subject to the same attenuation—when actors dissolve the hazards or broker the tacit knowledge, the pull toward acquisition weakens.

### Five acts

- **Exposition:** growth requires acquiring or allying; the governance literature is mature but blind to the firm's value-management orientation, and practitioner surveys make both modes live alternatives.
- **Rising action:** strategic emphasis enters the governance conversation through a documented allusion; asset attributes are named and converted into hazards; two lenses converge on the same prediction; two actors are staged as internal and external attenuators.
- **Climax:** the corrected headline probit model confirms the appropriation-to-acquisition pull (H1) and the CMO attenuation (H2); the analyst attenuation (H3) clears only at p<.10.
- **Falling action:** a threat battery swaps functional form, correction method, and heterogeneity operationalization with inferences holding regardless; transaction risk is elevated to a theorized mediator and the CMO reappears as a risk shield.
- **Denouement:** the Discussion names the "atomistic" blind spot each literature carried, claims the first attribute-level differentiation of marketing versus R&D assets, extends the CMO's repertoire to inorganic growth, and closes the performance loop with an event-study coda.

### Tension

- **Source:** a firm must choose a growth mode, yet the factor that should organize that choice—its own value-management orientation—is missing from the literature's account; appropriation emphasis offers harvest now but exposes the firm's most ambiguous, most holistic, most adaptation-hungry assets to a partner's opportunism.
- **Construction:** the paper manufactures no antagonist; the absence itself is the knot, hardened by the concession that prior work alluded to the link without developing it. The dual-lens convergence shows the knot has a determinate answer, and the moderators resolve the tension by calibration—every attenuation is introduced by recycling the exact hazards it dissolves, never by flipping the story.

### Alternative readings

- **author-signaled-alternative:** the Limitations concede that the expenditure-based operationalization assumes advertising and R&D outlays convert to assets at comparable efficiency (a stochastic-frontier robustness check is run in the Web Appendix), and that the modularity argument may hold differently for mono- versus multi-brand firms—so the attribute mechanism's empirical anchor is weaker than its narrative anchor.
- **analyst_counterfactual:** strategic emphasis measured as (advertising − R&D)/total assets could proxy for industry membership, intangible intensity, or selective-disclosure propensity (the paper's own inverse-Mills cure exists because disclosure is selective), and the marginal H3 interaction might reflect analyst coverage's direct negative main effect or its unmodeled endogeneity rather than hazard attenuation. This reading is analyst-generated; the paper does not entertain it.

## Story Assessment

- **Theme coherence:** `works` — the first research question organizes every section from hook to coda; the boundary-condition question stays subordinate and is delivered.
- **Character discipline:** `works` — the emphasis-to-mode decision pair carries the plot; the three attributes do mechanism work without becoming separate hypotheses; the moderator pair never spawns side plots, and the event study stays in the denouement instead of hijacking the story.
- **Knot integrity:** `works` — an absence-based gap hardened into a genuine incompleteness by the allusion concession, and plausibly addressable with archival choice data.
- **Plot emergence:** `works` — hazards derive from named attributes; moderators derive from those same hazards ("precisely for marketing vs. R&D assets the moderating effect should be most palpable"); the corrected probit staircase derives from the choice setting; nothing is forced.
- **Tie–unravel alignment:** `partly_works` — the main question is answered decisively in the corrected model, but one promised payoff beat is staged more weakly than its billing: analyst coverage received equal Introduction billing and a full theory subsection, yet its interaction is declared support at p<.10 with no simple slopes and no magnitude translation anywhere in the paper.
- **Ending quality:** `works` — the ending transforms rather than repeats: two blind spots become one amalgamation claim, the CMO's role is recast as governance, and the performance loop opened in the Introduction is closed by the event study.
- **Mechanism evidence check:** `not_directly_tested` — the three asset attributes are argued from literature and never measured; the supplemental transaction-risk mediation proxies hazards with a global LIWC risk dictionary. The choice design tests the reduced-form emphasis-to-mode link, not the hazard chain.
- **Boundary:** this evaluates storytelling only; it is not a judgment about the causal credibility of the estimates, the strategic-emphasis construct, or governance research generally.

## Learning Affordances

### Introduction and Theory

Use this card when a construct matured in one literature is genuinely absent from a target literature that has nonetheless alluded to it, and when two theoretical lenses can be shown to converge on the same prediction from independent premises. The attribute-level mechanism is the transferable core: replace "these categories differ" with named, citable attributes that each generate a distinct hazard. It is not a license to import any construct into any literature, and the dual-lens architecture becomes a liability the moment the lenses diverge in direction.

### Methods and Results

The reusable lesson is staging discipline: a model-free preview before specification, corrections embedded in the headline model that is alone discussed, and a threat battery closed with class-level invariance statements. The card doubles as a calibration counterexample: nonlinear coefficients with no marginal-effect translation and a headline moderation declared support at p<.10 show what top-venue storytelling can still omit, so writers should pair this card with a magnitude-reporting exemplar rather than imitate its reporting norms.

### Discussion

The ending earns its transformation twice—by naming what each literature could not see alone and by reopening the performance loop the Introduction promised. The move requires that the paper actually supply the missing link; an event-study coda without its own setup adds narrative closure, not evidentiary weight, and should not be presented as a second study.

## Comparison prompt

Bendig, Hensellek & Schulte (2024) also stages two external-venturing modes, but its predictor is what the firm does (activity intensity accumulating costs and learning), while this card's predictor is what the firm is (a value-management orientation imported from another literature). When the antecedent is an identity-like orientation rather than a behavior, do moderators need to be actors who dissolve specific hazards (CMO, analysts here) rather than environments that reshape curves (turbulence in the CVC card)—and what breaks if a hazard-attenuation moderator is theorized for an activity-intensity story?
