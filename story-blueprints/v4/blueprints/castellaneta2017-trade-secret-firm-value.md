# Story Learning Card — Castellaneta, Conti & Kacperczyk (2017, Strategic Management Journal)

## Metadata

```yaml
schema_version: "4.0-lite"
id: castellaneta2017-trade-secret-firm-value
paper:
  citekey: castellaneta_conti_kacperczyk_2017_smj
  title: "How Does Trade Secret Legal Protection Affect Firm Market Value? Evidence from the Uniform Trade Secret Act"
  outlet: "Strategic Management Journal"
  year: 2017
  publication_status: published
  paper_type: quantitative
  source_version: PDM_slices (2026-09-05)
  inclusion_rationale: "First whole-paper story card for this paper (no prior card exists). Enter the corpus for the whole-narrative layer only: the write-* corpus already carries two rounds of section-level distillation (2026-08-05 + 2026-09-05), so the card's distinctive asset is the integrated sign-reversal arc — a double-edged-sword paradox whose main effect is explicitly suspended by countervailing forces and whose sign is decided by industry contingencies — plus the setting-as-measurement-engine move (the PE buyout, where the same firm is sold twice) and the dedicated identification-validity block as a story act. Marginal on the generic moderation architecture itself (registered from this same paper's earlier distillation rounds)."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "sections/introduction.md"
    - "sections/theory.md"
    - "sections/methods.md"
    - "sections/results.md"
    - "sections/discussion.md"
  note: "Read from materialized PDM slices only (fulltext not opened per context discipline). One slice artifact: the H3 hypothesis sentence in theory.md is truncated ('** **pany operates in an industry characterized by a higher risk of poor investments'); the hypothesis content was reconstructed from the surrounding hindering-effect argument and the Results restatement of H3, and this card treats the reconstruction as verified by the verified theory distillation (theory.report.md)."
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Matches the default attention profile. Extra attention given to the Introduction's penultimate paragraph (endogeneity named and answered before the design is described) because the verified intro distillation scored the paper's contribution as Boundary + Question, and the causal-identification half of that promise is staged precisely there."
classification:
  theoretical_problem_form: [sign-reversing-contingency, countervailing-forces-tension, information-duality (protection-as-shield-vs-protection-as-veil)]
  narrative_dynamics: [main-effect-suspension, contingency-resolves-paradox, net-effect-revealed-then-parsed, setting-justified-by-measurement-requirement, identification-validity-as-falling-action]
  retrieval_signals: [trade-secrets, UTSA, appropriability-regime, market-for-corporate-control, PE-buyout-IRR, staggered-legal-shock, double-edged-sword, adverse-selection, knowledge-worker-mobility]
  confidence: reviewed
mechanism_evidence:
  status: partly_probed
  basis: "The two countervailing information channels — reduced leakage to rivals (value-up) and reduced buyer information driving offer discounts and bidding withdrawal (value-down) — are theoretical story engines, not measured mediators: no analysis observes information flow, buyer uncertainty, or bid dispersion directly. What is directly tested is the sign logic they jointly imply: three treatment-x-industry interactions (mobility +; resource-value uncertainty -; poor-investment risk -, p=.062) on the net holding-period IRR, under a treatment whose exogeneity is supported by enactment-hazard models, supply-demand checks, and +/-5-year placebos. The channels are read off the interaction pattern, not probed separately."
story_track:
  fed_flags:
    - flag: "C1-C4"
      content: "All four L2 cross-section flags report info-level consistency: gap type (Incompleteness) transmits from Introduction to Theory unchanged; moderation-type theory; natural-experiment DiD design; interaction-based main test — one type per link, no drift."
      consumption: "The card reads the paper as a single-type transmission case: a weak void-assertion gap is nonetheless carried faithfully through every downstream section, so the assessment judges coherence high even though the gap's own strength is thin. Coherence and gap strength are separated explicitly in the assessment."
    - flag: "theory-internal T6"
      content: "The Theory section has no T6 closing paragraph: after H3 the paper moves straight to the Research Setting and Design, leaving the suspended main effect (countervailing forces) unresolved inside the Theory section itself."
      consumption: "Assessed under plot emergence and ending quality: the suspension is actually reconciled narratively in the Results ('the positive effect is on average stronger than the negative one', ~4.5% net IRR), not in Theory. Verdict: a minor seam that works — but see the imperfect-paper note, because the reader must wait for the Results to learn how the two opposite forces net out, and the Theory never previews that a net average effect exists at all."
    - flag: "theory pseudo-tension risk"
      content: "Sub-agent flag: the countervailing-forces tension frame is not transferable to single-channel mechanism papers — if only one mechanism is spelled out, a declared 'tension' is decoration (伪张力)."
      consumption: "Hard-wired into the theory section-learning caveat and the comparison prompt: retrieval may recommend this card's tension move only when a paper genuinely holds two opposing mechanisms traceable to two distinct claim-holders (here: rivals vs buyers), not when it wants rhetorical drama."
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Stage the paradox before the hypotheses: dedicate one full paragraph to 'two opposite ways' (protection as shield against rivals vs veil from buyers), name it explicitly ('a paradox worth exploring', 'double-edged sword'), and let the research question be heterogeneity itself — so the plot promise is a sign reversal, not a level effect."
      - "Do the causal-contribution work in its own paragraph before describing the design: name the endogeneity threat concretely (legislation responding to state conditions or lobbying), declare that 'a research design that facilitates a clean causal estimate is central', and only then introduce the UTSA shock — the identification argument is delivered as part of the story, not as a Methods appendix."
    caveat:
      - "The gap is a thin void assertion ('researchers have not linked trade secret protection to firm value, even though its effect has been documented for mobility, innovation, clustering'). This survives publication here because the Boundary (sign reversal) and Question (causal identification) contributions cash it; transfer the void phrasing only when a derived contingency or a credible shock fills the void, otherwise the weak band becomes the paper's most attackable seam."
  theory:
    suitable: "partial"
    requires: ["two opposing mechanisms traceable to two distinct audiences/claim-holders must exist before the countervailing-forces framing is invoked"]
    learn:
      - "Suspend the main effect with an explicit tension frame ('countervailing forces... exposing a fundamental tension'), then resolve it through contingency: each hypothesis is a treatment-x-moderator sign prediction (more positive / more negative), so the hypotheses are the two blades of the sword rather than robustness appendices — dialectic opposition resolved by boundary conditions (Makadok Boundary contribution)."
      - "Chain a corollary into a second hypothesis: H2 (resource-value uncertainty) is argued to a close, then extended one step ('a direct corollary of our argument...') into H3 (lemons problem / poor-investment risk) so that Akerlof logic converts one information-scarcity mechanism into two distinct, separately testable moderators."
    caveat:
      - "No T6 closing paragraph: the Theory ends at H3 and hands off to the Research Setting without telling the reader how the three interactions combine into an overall pattern — the net-effect reconciliation is deferred to the Results. Acceptable in a sign-contingency paper; in a paper where readers must track magnitudes across interactions, add a one-paragraph synthesis."
      - "The tension frame is non-transferable to single-channel mechanism papers: with only one mechanism spelled out, a declared 'fundamental tension' is pseudo-tension. Here it is legitimate because each blade has its own audience (rivals vs buyers) and its own inference path."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Justify the setting by the measurement requirement, not by convenience: the Theory's ideal-data sentence ('the same company would need to be sold twice') is answered by the PE industry (buy-and-resell), so the setting itself is the plot's enabling device — the Research Setting and Design is written as the continuation of the theory argument, not as a data section."
      - "Disclose the estimator gap honestly and argue equivalence in words: the paper states plainly that a full DiD is 'difficult to implement fully' given IRR-only data, then argues the cross-sectional OLS on holding-window IRR is 'equivalent to the DiD framework' because the dependent variable already embeds the before/after first difference — a transparency move worth copying even if the equivalence claim itself is not."
    caveat:
      - "The DiD-equivalence sentence is a narrative move, not an identification audit: there are no pre-trend/event-study tests in the main text (only +/-5-year placebo treatments), state-level clustering on ~46 treated clusters, and the modern staggered-DiD literature would push back on two-way comparisons embedded in a cross-section. Learn the honesty of the disclosure; do not import the equivalence argument as a defense."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Reveal the net effect first, then parse it: Table 3 column 5 gives a net positive ~4.5% average effect and the text interprets it as 'the positive effect is on average stronger than the negative one' — the suspended main effect from the Theory is thus resolved on stage in the Results, after which each blade gets its own interaction paragraph with a one-SD magnitude translation (+18%, -29%, -16%)."
      - "Organize the entire second half of Results as an identification-validity narrative with named subsections ('Validity of the identification strategy', 'Political economy of the UTSA', 'PE supply and demand', 'Placebo tests', 'Late versus early UTSA enactment'): each subsection states a threat in plain language, then one table of evidence against it — threats as sub-plot antagonists, each defeated in turn."
    caveat:
      - "H3's interaction is marginal (p=.062) yet is folded into 'the results provide support for our hypotheses'; the marginal label does not survive into the summary sentence. Keep the calibration explicit when borrowing the net-then-parse cadence."
      - "The 'results available upon request' early/late-adoption split is asserted, not shown — a transparency target, not a model."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Rebuild the paradox in the first two sentences of the Discussion ('two countervailing effects...') before any contribution claim, so the ending visibly closes the opening knot rather than the results table."
      - "Convert the sign reversal into a policy paradox: 'regulations promoting stronger trade secret protection do not automatically translate to greater firm value... a policy that aims to... increase their value, might paradoxically reduce the value of the firm' — the boundary contribution is restated as an institutional-effectiveness claim (law effectiveness depends on factors beyond government control), which is a distinct second audience for the same finding."
    caveat:
      - "The Discussion resolves the tension verbally but never transforms it: unlike a Discussion that turns the paradox into a bounded rule with named scope conditions, this one cycles through a four-literature contribution inventory (acquisitions x appropriability, institutions, RBV) and conventional limitations. Learn the paradox-restatement opener; the contribution inventory is broad and delays closure."
story_assessment:
  overall_role: partial_exemplar
  mode: first_read_reviewed
```

## Story Reading

### Theme question

When the law strengthens the protection of a firm's most valuable secret assets, when does the firm become more valuable and when less — specifically, does the sign of the legal appropriability regime's effect on the price a firm commands in the market for corporate control depend on the industry the target lives in: on how leaky its workforce is, how uncertain its resource values are, and how likely a buyer is to catch a lemon?

### Whole-story synopsis

The paper opens inside the resource-based story the field knows by heart: valuable, hard-to-imitate resources sustain competitive advantage, and the legal appropriability regime is what keeps imitation at bay — with one blind spot. The large IPR-and-firm-value literature has looked almost exclusively at patents, which force disclosure and are therefore easy to value; trade secrets, the "crown jewels" rewarded precisely for staying hidden for an unlimited duration, have never been linked to firm market value. The question is posed: how does legal protection of trade secrets affect firm market value? The Introduction then does something structurally important before any hypothesis exists: it stages a paradox. Stronger protection can raise value by starving rivals of knowledge, and lower it by starving buyers of the information they need to price the target — a double-edged sword made of the same legal blade. From the paradox the plot promise follows naturally: the effect must be heterogeneous, positive where knowledge-worker mobility makes leakage the dominant threat, negative where resource-value uncertainty and lemons risk make buyer ignorance the dominant threat. The Introduction then performs its second move — endogeneity is named concretely (laws responding to state conditions or lobbying), a clean causal estimate is declared central, and the answer is pre-announced: the staggered state-by-state enactment of the UTSA (46 states, 1975–2008) as a quasi-natural experiment, observed through a setting built for the question, PE buyouts, where the same firm is sold twice so that the change in market value during the holding window is directly measurable. The Theory rebuilds the paradox as "countervailing forces" and — crucially — suspends the main effect: no hypothesis predicts a level effect at all. Three pure interaction hypotheses divide the sword: H1 (mobility) carries the enhancing blade, argued through leakage constraint and the collapse of employee bargaining power; H2 (resource-value uncertainty) and H3 (poor-investment risk, derived as a corollary of H2 via Akerlof) carry the hindering blade, argued through discounted offers, bidder withdrawal, and adverse selection. There is no closing synthesis: the section hands off to the design, which is framed as the fulfillment of the theory's own ideal-data sentence — the same firm sold twice — with the UTSA's enactment timing argued exogenous to state conditions. The Results first resolve the suspension: the net average effect is positive (~4.5% IRR), "the positive effect is on average stronger than the negative one," and the sign logic then unfolds blade by blade — +18% per SD of mobility, -29% per SD of resource-value uncertainty, -16% per SD of poor-investment risk. The second half of Results is an identification narrative: enactment-hazard models showing states' economic and political conditions did not cause adoption, supply-and-demand checks showing the UTSA did not move PE deal flow, placebo treatments five years on either side, CEM matching on ex ante value and riskiness, and an early-vs-late adoption split. The Discussion rebuilds the paradox in its first two sentences, claims the bridge between the acquisitions and appropriability literatures ("surprisingly disconnected thus far"), restates the finding as a policy paradox (a protection law can destroy the value it aims to create) and an RBV correction (protection need not raise the market value of the protected resources), concedes the IRR and patent-mobility measurement limits, and ends with managerial and policy implications plus social welfare left to future research.

### Characters and storylines

- **Main character:** trade secret legal protection — a single treatment with two faces: shield against rivals, veil from buyers. It has no level effect of its own in the hypothesis set; its "character" is only revealed through the industries it passes through.
- **Audience characters:** rivals/competitors (who would love to steal the secrets — the channel the law closes, raising value) and buyers/potential acquirers (who need to read the secrets to price the firm — the channel the law closes, lowering value). The two audiences are the load-bearing cast: the tension frame is legitimate precisely because both are genuinely present in the market for corporate control.
- **Boundary characters:** knowledge-worker mobility (enhancing-side moderator); resource-value uncertainty and poor-investment risk (hindering-side moderators, the second chained off the first via the lemons corollary).
- **Enabling character:** the PE buyout holding window — the narrative clock that makes "the same firm sold twice" observable, and the UTSA's staggered enactment — the shock whose exogeneity is the paper's most repeated claim.
- **Storyline 1 (shield):** stronger protection -> constrained leakage and constrained employee mobility -> higher target value, strongest where mobility is high.
- **Storyline 2 (veil):** stronger protection -> less information for buyers -> discounted offers, bidder withdrawal, lemons pricing, strongest where uncertainty and lemons risk are high.
- **Intersection:** one legal change, two audiences with opposite stakes; the net effect is an unweighted average over which storyline dominates, which is exactly why the Theory refuses a main-effect hypothesis and why the Results must reveal the net before parsing it.

### Five acts

- **Exposition:** RBV + appropriability premise; the patents-only blind spot; the void gap (trade secrets never linked to market value); the double-edged-sword paradox paragraph; the heterogeneity RQ; the endogeneity paragraph with the UTSA natural experiment and PE setting previewed.
- **Rising action:** Theory defines trade secrets and misappropriation law; the countervailing-forces tension frame suspends the main effect; H1 from the shield blade, H2 from the veil blade, H3 chained from H2 via Akerlof; Research Setting and Design written as the theory's ideal-data fulfillment (sold twice; staggered exogenous shock; OLS on holding-window IRR with state clustering).
- **Climax:** Results reveal the net positive average effect (resolving the suspension), then the three sign-reversing interactions with one-SD magnitude translations — the promised sign reversal paid off in a single table read twice.
- **Falling action:** the identification-validity battery as named subsections: CEM matching, political-economy enactment models (LPM, logistic and proportional hazards), PE supply-and-demand checks, +/-5-year placebos, early/late split, alternative mobility/risk/protection measures.
- **Denouement:** Discussion restates the two countervailing effects first, bridges the acquisitions and appropriability literatures, converts the finding into a policy paradox and an RBV boundary, concedes IRR and mobility-measurement limits, and routes social-welfare questions to future research.

### Tension

- **Source:** one legal intervention serves two audiences with exactly opposite informational stakes — the same secrecy that protects value creation from rivals destroys value assessment by buyers. The tension is real, not personified: there is no antagonist, only a law whose effect cannot have a single sign.
- **Construction:** the Introduction announces the paradox as "worth exploring" before any hypothesis; the Theory formalizes it as "countervailing forces" and turns the resolution into the entire hypothesis set; the Results resolve the suspension empirically (net positive, then sign-contingent); the Discussion re-poses it as a policy paradox. The tension arc is the paper's spine.

### Alternative readings

- **analyst_counterfactual:** the same evidence supports a flatter story — "protection helps where imitation threats matter and hurts where valuation problems matter" — as a conventional hedging/insurance moderation paper with no paradox at all: the two channels are never separately measured, so the countervailing-forces frame is an interpretive commitment, not an observed mechanism. A skeptic's reading of Table 3 is three interactions around a modest positive main effect; the paradox is what the authors make of it.
- **cross-paper comparison note:** against `moon2026-trade-secret-protection-advertising` (same UTSA staggered shock, different outcome), the concrete reading question is: how does the identical legal shock get cast into two different stories — a buyer-information/valuation story here versus an advertising/attention story there — and what does each casting require the Theory to suspend or assert? Against the corpus's legal-institution cards (`hoffmann2024-legal-liability`, `chen2026-anti-slapp-*`), this paper is the case where the shock's *sign* is the unknown, rather than its magnitude or existence.

## Story Assessment

- **Theme coherence:** `works` — the double-edged-sword frame is announced in the Introduction, formalized as countervailing forces, resolved sign by sign in the Results, and restated as a policy paradox in the Discussion. The main effect stays suspended exactly where the architecture wants it, and every section speaks the same two-blade language.
- **Character discipline:** `works` — the treatment's two faces (shield/veil) map onto two real audiences (rivals/buyers), the three moderators are industry attributes rather than competing mechanisms, and the PE holding window plays its enabling role without absorbing attention. No invented antagonists.
- **Knot integrity:** `partly_works` — the knot (sign unknown, paradox real) is well-formed and single, but it hangs from a thin void-assertion gap ("researchers have not linked X to Y") whose own strength is low; the knot survives because the Boundary + Question contributions cash it. The gap and the knot are not the same quality, and readers conflate them at the paper's peril.
- **Plot emergence:** `partly_works` — the sign-reversal prediction follows from the two-audience information logic, not from a preference for moderation; but the Theory has no closing synthesis (no T6), so the reader does not learn until the Results that the two opposite forces are expected to net out to a positive average — the reconciliation of the suspended main effect happens off-stage from the Theory's perspective, even though the Results stage it explicitly.
- **Tie–unravel alignment:** `works` — the Results pay the front-end contract in full and in order: heterogeneous effects exactly as previewed, then an identification-validity narrative that answers every threat the Introduction named. Honesty caveats: H3 is marginal (p=.062) yet absorbed into blanket support language, and the early/late split is "available upon request" rather than shown.
- **Ending quality:** `partly_works` — the Discussion restates the paradox before claiming contributions (good), and the policy-paradox / RBV-correction restatements are genuine transformations for two additional audiences; but the ending resolves the tension verbally rather than converting it into a bounded conditional rule with named scope conditions, and the four-literature inventory delays closure.
- **Boundary:** This evaluates storytelling only. It is not a judgment about the validity of the DiD-equivalence argument, the exogeneity of UTSA enactment, the state-level clustering, the patent-based mobility measure, or the paper's contribution to law-and-finance. The marginal H3 and the request-only split are evidence facts; their narrative handling is what is assessed.

## Learning Affordances

### Introduction and Theory

Learn the paradox-first architecture and the identification-as-story move. The transferable actions are: (1) open the paradox in its own paragraph (one mechanism, two audiences with opposite stakes), name it, and let the research question be heterogeneity, so every downstream hypothesis is a blade of the announced sword rather than an appended moderator; (2) give endogeneity its own paragraph before the design — name the threat concretely, declare the clean-estimate requirement, then let the natural experiment answer it — so that the causal half of the contribution claim is staged where the reader forms expectations. The tension frame requires two genuinely opposing mechanisms traceable to two distinct audiences; with a single channel, a declared "fundamental tension" is pseudo-tension and this card must not be retrieved as its template. The void-assertion gap survives here only because the sign reversal and the natural experiment fill it; copy the gap phrasing only with an equivalent cashing mechanism in hand.

### Methods and Results

The methods move to carry is setting-justified-by-measurement-requirement: state the ideal data the theory needs (the same firm sold twice), then show the setting that provides it — plus the honest disclosure of the estimator gap ("equivalent to the DiD framework" argued in words, with its limits stated). Do not import the equivalence argument itself as an identification defense: no pre-trend tests, ~46 treated state clusters, and the modern staggered-DiD critique are visible here. The results move is the net-then-parse cadence (reveal the average effect and interpret it as one blade outweighing the other, then translate each interaction into a one-SD magnitude) followed by the identification-validity block written as named threat-by-threat subsections. Keep the marginal label alive through the summary sentence (H3, p=.062); show rather than promise robustness splits.

### Discussion

Learn the paradox-restatement opener (rebuild the two countervailing effects in the first sentences before any contribution claim) and the double-audience transformation (same finding restated as an institutional-effectiveness claim for policy and a protection-need-not-pay correction for the RBV). Caveat: the contribution inventory spans four literatures and the tension is resolved verbally, not converted into a bounded rule — close the paper's own loop first and name scope conditions where this paper routes them to "future research."

### Imperfect-paper learning note

Three seams worth studying rather than copying. (1) The gap band is thin — a pure void assertion — yet coherent downstream; the lesson is that coherence and gap strength are independent, and reviewers attack the gap even when the transmission is clean. (2) The Theory's missing T6: the suspended main effect is reconciled in the Results instead, which works here only because the Results stage the reconciliation explicitly ("the positive effect is on average stronger than the negative one"); a one-paragraph synthesis would have removed the wait. (3) Calibration slippage at the margin: H3 (p=.062) and the request-only early/late split show a paper whose story is strong enough to absorb weaker evidence labels — the exact condition under which writers most need the discipline not to merge marginal into full support.

## Comparison prompt

When a single legal or institutional shock plausibly moves an outcome through two opposite channels, does the paper suspend the main effect and let sign-reversing moderators carry the plot (this paper), or measure the channels separately, or report only a net effect? The concrete reading question for retrieval: what does this card teach that `moon2026-trade-secret-protection-advertising` does not — the main-effect-suspension architecture, the setting-as-measurement-engine justification, and the identification-validity block as narrative falling action — versus what Moon already covers about turning the same UTSA shock into a different story? Compare also with the corpus's legal-shock cards (Hoffmann 2024; Chen 2026 anti-SLAPP pair) where the shock's existence, not its sign, is the open question.
