# Story Learning Card — Raithel, Hock, and Mafael (2024, Journal of the Academy of Marketing Science)

## Metadata

```yaml
schema_version: "4.0-lite"
id: raithel2024
paper:
  citekey: raithel_2024_product_recall_effectiveness_and_consumers_part  # pdm paper_id; Zotero citekey unverified
  title: "Product recall effectiveness and consumers' participation in corrective actions"
  outlet: "Journal of the Academy of Marketing Science"
  year: 2024
  publication_status: published
  paper_type: "quantitative (three-study: archival field study + two experiments)"
  source_version: pdm_slices_verified  # seven verified section slices (gap-fill 2026-09-29: results-s2s3, general-discussion) + L2 section distillations
  inclusion_rationale: "A front-end-weighted learning object showing how an institutional artifact (the standardized CPSC announcement) supplies both the levers and the theory: its mandatory fields become cues to action, and an imported health-psychology model (HBM) is modified to explain why the same cue works differently by issuer reputation."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete  # gap-fill 2026-09-29: the Study 2/3 results slice and the general-discussion slice closed the multi-study tail the first round could not observe
  source_records:
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/introduction.md"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/theory.md"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/methods.md"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/results.md (Study 1 results)"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/discussion.md (Study 1 discussion)"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/results-s2s3.md (gap-fill slice, 2026-09-29: Study 2 remedy x reputation and Study 3 incident-likelihood x reputation results)"
    - "C:/Users/admin/.claude/distill-work/raithel_2024_product_recall_effectiveness_and_consumers_part.pdm/sections/general-discussion.md (gap-fill slice, 2026-09-29: general discussion, implications, limitations)"
    - "pdm/sections/{introduction,theory,methods,results}.json (verified L2 distillations)"
    - "story-blueprints/v4/rhetoric-moves/sources/raithel_2024_product_recall_effectiveness_and_consumers_part.sentences.md (sentence inventory)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default allocation kept. The first round's only constraint (multi-study tail unobserved) was removed by the 2026-09-29 gap-fill; attention stays front-end weighted per the default profile."
mechanism_evidence:
  status: directly_tested
  basis: "Study 1 tests H1-H4 (main effects and reputation interactions) with dual Heckman control functions; the two experiments then directly measure the HBM beliefs and test the moderated-mediation chain (Hayes model 7, 5,000 bootstrap samples). H7a/H7b hold in both studies, but the first-stage assignments split: remedy runs through self-efficacy (H5b) not benefits (H5a failed), and incident likelihood runs through benefits (H6a) not self-efficacy (H6b failed) — the tested mechanism is half-confirmed and crossed."
classification:
  theoretical_problem_form: [underquantified-managerial-levers, standardized-artifact-as-theory-source]
  narrative_dynamics: [model-migration-with-modification, single-moderator-multi-role, honest-null-inside-climax, reputation-as-signal-ambiguity, crossed-mediator-payoff]
  retrieval_signals: [recall-effectiveness, standardized-announcement-levers, reputation-heuristic, hbm-migration, moderated-mediation, floodlight-jn-analysis]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Open with an institutional scale contradiction — hundreds of standardized announcements versus 6% effectiveness — and cascade the consequences (deaths, litigation, trillion-dollar losses) inside the same paragraph, so the rhetorical question that closes the hook is already carrying quantified stakes instead of a separate stakes paragraph."
      - "Turn 'little research' into a counted, positioned gap by a construct-role census (17 articles split by IV/moderator/DV roles), then enumerate three gaps with an explicit priority marker and pay each off in a numbered contribution block that embeds the headline magnitude (+11.4%), one explicit null, and the moderation directions."
    caveat:
      - "The theory lens is absent from the introduction (HBM appears only in the keywords); the mechanism is previewed in consumer vernacular. This is venue-legal at JAMS but means the front end promises a process the introduction itself cannot name — do not copy this deferral into venues that expect the lens up front."
      - "The RQ matrix plus contribution block consumes roughly the second half of a short introduction; that budget works because the hook did the stake-setting, but it front-loads contribution over theory."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Run a model-modification setup: declare the adopted model's baseline structural assumption (HBM factors act in parallel), then justify each departure by a context-specific feature — the standardized announcement's mandatory fields relocate cues to action, the missing institutional factor motivates the reputation extension, and a meta-analytic weak-association result licenses selecting only two of six factors as mediators."
      - "Derive asymmetric bilateral moderation with unequal load: fully derive the high-reputation side (halo buffering flips the same signal into severity), and zero out the low side with its own independent baseline-expectations reason rather than mirroring the high side."
    caveat:
      - "H6b (higher incident likelihood raising self-efficacy) is the why-chain's weakest step, carried by a single cross-domain correlational warrant — a counterintuitive link needs a second warrant or downgrading to exploratory."
      - "The published text carries template-reuse drift (H6's tail clause still reads 'full (vs. partial) remedy'; the Figure 1 note mislabels H5b/H6b), and the adopted constructs come with no scope conditions — multi-hypothesis derivations need a hypothesis-clause consistency check."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "When the outcome itself is confidential, make its acquisition part of the design story: a FOIA request yields effectiveness data for 217 of 338 recalls, and the 121 non-disclosing firms become a first-stage sample-selection equation whose exclusion restrictions are each validated in text (strong correlation with disclosure, near-zero with the outcome)."
      - "Anticipate the second self-selection — firms choose remedy strategically — with its own control function, and embed both IMRs in the main results table so the endogeneity answer sits inside the climax rather than in an appendix."
    caveat:
      - "The moderator (reputation) is not positioned in the measurement section and surfaces only in Eq. (3); the two first-stage specifications are asymmetric without explanation; a marginal first-stage test (p = .063) is narrated as 'significantly associated'; and the merging of two survey-based controls with archival data is unexplained."
      - "The FOIA route, CPSC standardization, and Fortune reputation measure are institution-specific; they are not portable to settings without a disclosure mandate."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage the climax as hypothesis-by-hypothesis verdicts at a declared alpha, reporting the H2 null in the same voice and format as the supports (replicated directionally in Study 3), and read both interactions off floodlight/JN confidence bands so moderation becomes regions of significance rather than a single coefficient sign."
      - "Pay the delegated process promise in a symmetric experiment block: first-stage mediation, mediator-by-moderator interactions, and the index of moderated mediation each get their own verdict, with floodlight panels for the mediators that reuse Study 1's visual grammar — the mechanism reveal is staged with the same machinery as the direct-effect climax."
    caveat:
      - "Verdict bookkeeping loosens where it matters most: H1 gets 'marginal support' (p = .078, d = 0.18), Study 3's H7b-for-self-efficacy leans on a 90% CI after the declared alpha = 5%, and Study 3's low-reputation self-efficacy indirect effect is significant and negative (CI excludes zero) yet is never reconciled with the monotone halo narrative; robustness is one sentence delegated to a web appendix and JN thresholds stay in z-units without translation back to the reputation scale."
      - "Study 3's results and discussion disagree: the results section reports H6b failed, while the study discussion narrates both beliefs as confirmed channels into participation."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Convert interaction coefficients into a reputational-profile segmentation — high, medium, and low reputation firms should manage recalls differently — then cash it out twice in the general discussion: a guidelines figure that makes the boundary condition the takeaway, and a quantified moderation payoff (the +11.4% average remedy effect more than doubles to 24.1% at one SD above the reputation mean) that shows the interaction is worth money, not just sign flips."
      - "Recycle the opening's stakes honestly by turning the null into differentiated guidance (low-reputation firms rebuild trust in repair capability; high-reputation firms amplify severity and educate on usage risk), and close with limitations that name three concrete extension fronts (remedy menus, firm-issued press releases, industry splits) instead of generic hedges."
    caveat:
      - "The general discussion pools the crossed mediation into one confirmed-sounding sentence ('targeting beliefs about benefits and self-efficacy increases recall effectiveness') without registering that each lever ran through exactly one belief and the assignments crossed the theory's symmetric derivation; it also never returns to reputation's negative main effect from the climax, and the opening stakes (23,000 deaths, $1 trillion) are restated verbatim as re-stakes rather than transformed."
story_assessment:
  overall_role: exemplar  # upgraded 2026-09-29 after the gap-fill closed the multi-study tail: the arc now runs from a quantified hook through an artifact-structured HBM migration to a directly tested (half-confirmed, crossed) mechanism and a quantified reputational-playbook ending; the crossed-mediator pooling, the 90% CI verdict, and the unreconciled negative main effect are recorded as caveats, not disqualifiers
  mode: first_write_reviewed
```

## Story Reading

### Theme question

When regulators already standardize every recall announcement, which managerially controllable levers inside that announcement — remedy and incident likelihood — raise the share of defective products consumers actually return, under what reputation boundary does each lever work, and through which psychological process?

### Whole-story synopsis

The paper opens on an institutional paradox: the CPSC issues hundreds of standardized announcements covering tens of millions of units, yet only 6% of recalled products are ever corrected, and the consequences cascade from a toddler's death settlement to a trillion-dollar annual cost. A counted literature census — 17 quantitative articles, sorted by whether they treat recall effectiveness as independent variable, moderator, or dependent variable — shows that the announcement's own mandatory fields have never been tested as drivers. The introduction promises four answers in a symmetric matrix: the direct effects of remedy and incident likelihood, the psychological processes behind them, and reputation's moderation of both.

The theory section then performs the paper's characteristic move: it imports the Health Belief Model and modifies it to the recall context. The original model's parallel-structure assumption is dismantled — the standardized announcement becomes the external cue to action, remedy and incident likelihood (fields printed in every CPSC notice) become the operative cues, firm reputation is added as an institutional extension that acts as a judgment heuristic, and perceived benefits and self-efficacy are retained as the two mediators that matter. Seven hypothesis groups follow, with reputation moderating both the direct paths and the mediation itself, locked by a conceptual framework figure that assigns hypothesis groups to the three studies.

Study 1 delivers the climax in archival data: full remedy raises effectiveness by 11.4 percentage points on average; incident likelihood alone does nothing — an honestly reported null; but both effects are reshaped by reputation, with floodlight analyses locating the regions where each interaction turns positive or even reverses. Reputation itself carries a negative main effect, a complication the front end did not advertise. Control functions for sample disclosure and remedy choice sit inside the main table. The observed discussion converts the interactions into a reputational-profile playbook — high, medium, and low reputation firms need different recall management — before handing the process questions to the experiments. The two experiments then pay that hand-off, but with a twist the front end did not predict: each lever runs through exactly one belief and the assignments cross — remedy works through self-efficacy (not benefits), incident likelihood through benefits (not self-efficacy) — while reputation moderates both indirect paths in both studies. The general discussion closes the loop by converting the interactions into a guidelines figure and quantifying the moderation payoff (the +11.4% remedy effect more than doubles to 24.1% for high-reputation firms), yet it pools the crossed mediation into a single confirmed-sounding sentence and never returns to the climax's unexplained negative reputation main effect.

### Characters and storylines

- **Main character:** recall effectiveness, the 6% outcome the whole paper exists to move; the introduction makes it a character by quantifying its failure before any construct is named.
- **Co-protagonist:** the consumer deciding whether to participate — the theory section's grammatical subject, whose beliefs (benefits, self-efficacy) the HBM migration equips with motives.
- **Lever characters:** remedy and incident likelihood, two fields every standardized announcement already prints; their power is that managers control them and research has ignored them.
- **Boundary character:** firm reputation, the judgment heuristic that decides how the same cue is read — buffering, amplifying, or reversing it; notably it also carries an unadvertised negative main effect in the results.
- **Institutional supporting character:** the CPSC announcement itself, the artifact whose standardization makes the levers observable and comparable in field data.
- **Storyline 1 (cue):** what the announcement says — full versus partial remedy, many versus few prior incidents — moves participation through perceived benefits and self-efficacy.
- **Storyline 2 (heuristic):** who says it — high versus low reputation — changes what the same words mean, moderating both direct effects and the underlying beliefs.
- **Intersection:** the 6% number is not a communication failure but a design variable: participation responds to the interaction between what the announcement says and who issues it.

### Five acts

- **Exposition:** 300 recalls, 40 million units, 6% effectiveness, one $46 million settlement, 23,000 deaths, $1 trillion in costs — compressed into one paragraph that ends in the broad question; a counted census and three prioritized gaps; four numbered research questions in a {direct, moderated} × {effect, process} matrix.
- **Rising action:** the HBM is migrated and modified — cue to action relocated to the standardized announcement, reputation added as institutional extension, two of six beliefs promoted to mediators on meta-analytic grounds; seven hypothesis groups derived with asymmetric bilateral moderation logic, locked by the framework figure and closed by a three-study overview.
- **Climax:** the fractional probit with dual control functions returns verdicts at α = 5%: H1 supported with the +11.4% magnitude, H2 honestly null, H3 and H4 supported and mapped onto floodlight regions with two JN points each; reputation's negative main effect surfaces here for the first time.
- **Falling action:** the control functions are justified in place; robustness is delegated in one sentence to a web appendix; the Study 1 discussion translates the interactions into differentiated guidance by reputational profile and bridges to the experiments on endogeneity grounds.
- **Denouement:** the experiments pay the hand-off with a crossed reveal — remedy runs through self-efficacy, incident likelihood through benefits, reputation moderating both indirect paths in both studies — and the general discussion reopens the introduction's three questions verbatim, converts the interactions into a guidelines figure (Fig. 5), quantifies the moderation payoff (11.4% → 24.1% for high-reputation firms), extends the playbook to regulators, and names three concrete limitation fronts, while smoothing the crossed mediation into one pooled sentence and leaving the negative reputation main effect unmentioned.

### Tension

- **Source:** the standardized announcement system itself. Every CPSC notice already prints remedy and incident likelihood — the levers are public, mandatory, and managerially set — yet effectiveness is 6% and their impact is unknown. The paper never needs an antagonist because the artifact is both the infrastructure and the untested black box.
- **Construction:** the tension is made legible twice. First by counting: thirteen prior studies used effectiveness as a dependent variable and none tested the announcement's own fields. Second by ambiguity: reputation means the same printed cue does not carry the same meaning — the halo reading discounts a partial remedy from a high-reputation firm while the severity reading amplifies incidents from one, so the announcement's message depends on its issuer.

### Alternative readings

- **analyst_counterfactual:** The H2 null could be promoted from a supported-adjacent footnote to the paper's most interesting claim — severity signals alone do not move participation without a reputational frame — which would recast the paper from "drivers of effectiveness" to "when severity information is inert." The authors instead frame it as extending Hall and Johnson-Hall (2021); this counterfactual is the analyst's, not the authors'.
- **analyst_counterfactual:** One could read the design as remedy-endogeneity-first (Chen et al. 2009 lineage, which the methods control function honors) rather than communication-design-first; the paper's story chooses the consumer-side HBM framing and treats strategic remedy choice as a nuisance to be corrected.
- **analyst_counterfactual:** The crossed mediation pattern (remedy → self-efficacy, incident likelihood → benefits) could be promoted from pooled verdicts to the headline: the announcement's remedy field is an efficacy communication and its incident field is a benefit-severity communication — two different persuasion routes inside one form, not one mechanism with two inputs. The authors instead report the four first-stage hypotheses as separate pass/fail verdicts and pool them in the general discussion; this counterfactual is the analyst's, not the authors'.

## Story Assessment

- **Theme coherence:** `works` — every section organizes around raising the 6% number through announcement levers; the counted census, the HBM migration, and the floodlight results all point at the same knot.
- **Character discipline:** `partly_works` — reputation still carries three jobs at once (negative main effect, moderator of direct effects, moderator of mediation), and the front end introduces only the moderating jobs. The gap-fill re-check confirms the first round's flag: even with the full paper observed, the general discussion never returns to the negative main effect, and the moderation job's own evidence is internally uneven — Study 3's low-reputation self-efficacy indirect effect is significant and negative, contradicting the monotone halo narrative that the Study 3 discussion nevertheless narrates as confirmed.
- **Knot integrity:** `works` — managerially controllable fields with unknown impact inside a standardized system whose outcome is a measured 6% is a genuine, addressable challenge.
- **Plot emergence:** `works` — the hypotheses follow from the declared modifications of the HBM rather than from an added-predictor logic; each departure from the baseline model is justified by a context feature.
- **Tie–unravel alignment:** `partly_works` — the direct and boundary questions are answered cleanly (including the honest, directionally replicated H2 null) and the promised process is now directly tested, but the answer crosses the promise: of the four first-stage mediation hypotheses, exactly the mirrored half survive (H5b, H6a) while the other half fail (H5a, H6b), and the general discussion pools the pattern into a confirmed-sounding claim without registering the crossing.
- **Ending quality:** `works` — the general discussion reopens the introduction's three questions verbatim and returns a changed understanding: a guidelines figure that makes the reputational profile the unit of advice, a monetized moderation payoff (11.4% → 24.1%), differentiated incident-likelihood guidance that turns the null into action, and a regulator extension. Caveats: the opening stakes are restated verbatim rather than transformed, and the crossed mediation is pooled smooth.
- **Boundary:** This evaluates storytelling only; it is not a judgment about the paper's causal identification, measurement validity, or research quality.

## Learning Affordances

### Introduction and Theory

The transferable core: when a standardized institutional artifact contains the candidate levers, let the artifact structure the theory — migrate an established model, declare its baseline structural assumption, and justify each modification by one feature of the artifact. The countable literature census and the quantified-null contribution block are portable to any field where a regulatory form's fields have gone untested. Not copyable: the CPSC's standardization, the HBM's health-psychology authority, and the convenience of a regulator-published DV. Do not copy the single-warrant counterintuitive derivation (H6b) or the deferred theory lens into venues that require the lens in the introduction.

### Methods and Results

Use this card when the outcome variable itself is scarce, confidential, or selectively disclosed: the FOIA-plus-Heckman architecture makes data acquisition part of the design story and puts endogeneity answers inside the main table. Also transferable: floodlight/JN presentation of interactions, a declared-alpha verdict format with the null reported in the same voice as the supports, and the experiments' mechanism-staging sequence (first-stage mediation → moderated-mediation index → floodlight panels for the mediators). Cautionary: the falling action's pacing (one-sentence robustness, untranslated magnitudes, alpha-counting inconsistency, z-unit thresholds) and the experiments' loosening verdict bookkeeping (marginal support at p = .078, a 90% CI after a declared 5% alpha, a study discussion narrating a failed hypothesis as confirmed) are recorded weakness, not rhythm to imitate.

### Discussion

The discussion arc works because it converts the boundary character (reputation) into a segmentation the reader can act on, rather than restating coefficients — and the general discussion then cashes the segmentation into a guidelines figure and a monetized payoff. Copyable: quantifying the moderation (the +11.4% average remedy effect more than doubles to 24.1% for high-reputation firms), turning the null into differentiated guidance by reputational profile, and closing with concrete limitation fronts. Not copyable: the closing pooling that presents crossed mediation as a confirmed symmetric mechanism — register your crossed patterns instead. The Study 1→2→3 process hand-off is a bridge convention for multi-study papers, not an argument to copy wholesale.

## Comparison prompt

Compared with Chen et al. (2009) in this corpus, where remedy signals firm type to investors and markets, does the HBM migration shift the audience of the same remedy field from markets to the defective-product holder — and does that audience shift explain why reputation enters here as a consumer-side heuristic rather than a market-side signal? Read against Eilert et al. (2017), ask whether timing-based recall stories and announcement-design stories compete for the same outcome or address different stages of the same participation funnel.
