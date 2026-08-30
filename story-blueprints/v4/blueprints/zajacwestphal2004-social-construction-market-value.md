# Story Learning Card — Zajac & Westphal (2004, American Sociological Review)

## Metadata

```yaml
schema_version: "4.0-lite"
id: zajacwestphal2004-social-construction-market-value
paper:
  citekey: zajac_westphal_2004_social_construction
  title: "The Social Construction of Market Value: Institutionalization and Learning Perspectives on Stock Market Reactions"
  outlet: "American Sociological Review"
  year: 2004
  publication_status: published
  paper_type: quantitative (archival event study + market-level time-series regressions)
  source_version: pdm_slices_verified
  inclusion_rationale: "The Westphal-system trilogy's scale-up move: where the 1998 ASQ paper adjudicated symbolic vs. substantive readings within one event (decoupling split), this paper adjudicates two whole theories of market value — market learning vs. institutionalization — across time, using a historical sign reversal (negative buyback reactions before the mid-1980s agency-logic shift, positive after) as the discriminating evidence. Masterclass in making a construct ('market value') the protagonist by reclassifying its measure from objective to subjective data, in numbered rival-hypothesis pairing (H2/H2a, H3/H3a), and in a paradox ending ('the teaching was too successful')."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "PDM slices: sections/introduction.md, sections/theory.md, sections/methods.md, sections/results.md, sections/discussion.md (zajac_westphal_the_social_construction_of_market_value.pdm)"
    - "Identity verified from text-only front matter: ASR 2004, 69(3), 433-457 (not ASQ). Figures 1-2 were image-references in the slices; figure content reconstructed from in-text description and captions."
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default 40/25/15/15/5 profile retained, with one deliberate emphasis: the user context prioritizes narrative and prose-level craft, so the theory section's rival-pairing rhetoric and the results' falsification rhythm ('It might be suggested that...') were given full learning-move treatment rather than being compressed into story assessment. PDM structure flags carried as caveats only: Analysis/Results separation (era-typical), one-tailed tests, thin magnitude interpretation."
mechanism_evidence:
  status: partly_probed
  basis: "The downstream observable is richly probed — historical sign reversal (difference in t-statistics, p <= .01), positive coefficient on prior nonimplemented plans across three event windows, Heckman selection, alternative implementation windows, and null profitability effects that rule out efficiency-learning — but the hypothesized interior mechanism (investors referencing prior market reactions under imperfect communication; uncertainty reduction) is never measured, and no perceptual or trader-level data exist."
class_retrieval:
  theoretical_problem_form: [social-construction-of-market-value, rival-theory-adjudication, historical-sign-reversal, decoupling-institutionalization-integration, symbolic-value-borrowing]
  narrative_dynamics: [same-practice-two-readings, objective-data-reclassified-as-subjective, rival-hypotheses-numbered-as-pairs, null-narrated-as-headline, teachable-but-slow-learning-paradox]
  retrieval_signals: [stock-repurchase-plans, institutional-logics, agency-logic, decoupling, market-learning, event-study, neoinstitutional-theory]
  confidence: provisional
section_learning:
  introduction:
    suitable: "yes"
    requires: ["two mature literatures each owning half of one phenomenon, with a genuine unowned intersection between them"]
    learn:
      - "Bridge-as-gap: show each literature's home turf (neoinstitutional: adoption and decoupling in industrial markets; financial economics: market reactions in capital markets), then name the intersection nobody owns — whether institutionalization processes reach capital markets — so the gap is a missing bridge between established camps, not a missing topic. Sharpen it by deriving the rival's own corollary as a falsifiable prediction ('if firms adopt but do not implement, the market should discount the policy')."
      - "Make the dependent variable the protagonist: stage the whole intro around one contestable claim about 'market value' — a 'reliable, historically invariant indicator of efficiency' versus a 'socially constructed' aggregate — so the reader knows the adjudication axis before any hypothesis appears."
    caveat:
      - "Requires two developed literatures with real overlap territory; without them the bridge reads as forced synthesis. The prose is citation-dense and presumes neoinstitutional vocabulary (logics, decoupling, taken-for-grantedness) — a writer without that shared language must first build it, and 2004-era intros carry no explicit stakes/magnitude preview."
  theory:
    suitable: "yes"
    requires: ["a historical or contextual boundary at which the meaning of the same practice plausibly changed, and a rival perspective strong enough to generate its own numbered hypotheses"]
    learn:
      - "Sign-flip table: use a two-column institutional-logic comparison (Table 1: agency logic vs. corporate logic) to establish that the identical practice carries opposite meanings under different logics — buyback as free-cash-flow discipline vs. buyback as evidence of exhausted prospects — then cash the flip directly into H1. Historical contingency is demonstrated structurally before it is claimed rhetorically."
      - "Competing-hypothesis pairing: number rival and own predictions as adjacent pairs (H2 vs. H2a; H3 vs. H3a), state the rival first and at full strength — including its robustness clause ('this would be true even if other motives for non-implementation were sometimes also involved') — so the data adjudicate a fair fight and the rival's null lands as a finding, not a straw man."
    caveat:
      - "The mechanism (sociohistorical estimation by investors) is asserted, never measured; a modern version needs perceptual, trader-level, or heterogeneity evidence. The design also requires an observable pre-period in which the rival reading already fails — without a negative-early-reactions era, H1 has no discriminating power."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Sample-frame as story equipment: the 1980-1994 window is chosen so the pre-shift and post-shift eras are both observable; the three-year implementation window, the 2/11/31-day event-window triangulation, and Heckman selection models each answer a named rival-reading objection (slow adjustment, adoption-selection into returns) inside the design chapter rather than after results."
    caveat:
      - "Era presentation: Analysis/Results split, one-tailed tests, thin economic-magnitude interpretation. The market-level count variables (prior nonimplemented vs. implemented plans) are the theoretical operationalization but correlate at r = .53 — a modern version must defend multicollinearity and identification of the learning-vs-institutionalization contrast more explicitly; borrowing the alignment logic, not the estimator presentation."
  results:
    suitable: "yes"
    requires: ["a rival prediction that can be narrated as null, and a figure or pattern that shows the adjudication before the controls"]
    learn:
      - "Figure-first reversal: stage the climax on Figure 2 — the raw sign flip with t-statistics and the p <= .01 difference-in-t test — before any regression appears, so the reader has seen the story before the controls; the regression table then confirms rather than reveals."
      - "Falsification rhythm: (1) narrate the rival's null as the headline ('Hypothesis 2, the market-learning hypothesis... is not supported') inside the paragraph confirming your own; (2) convert the implemented-count coefficient into a symmetry argument ('predicts market reactions regardless of whether those plans were implemented'); (3) meet the reader's best remaining objection in a named paragraph ('It might be suggested that...') and close it with supplementary profitability analyses showing implementation never paid — the last rational-learning exit is sealed."
    caveat:
      - "One-tailed tests and minimal magnitude interpretation are era artifacts; the aggregate time-series design cannot show any investor actually referencing anything — claim discipline at the mechanism level is the writer's responsibility in a modern staging."
  discussion:
    suitable: "yes"
    requires: ["a rival community whose own assumptions your null finding implicates, and two classic theses your story can connect"]
    learn:
      - "Paradox ending: convert the rival's null into a paradox about the rival community itself — markets proved 'teachable' (they reversed on the agency logic), yet the teaching profession (financial economists, business schools, media) was 'too successful' at certifying buyback rationality, foreclosing the market's opportunity to learn about decoupling. The discussion thereby adds a second theoretical contribution instead of recapping results."
      - "Thesis-integration close: explicitly announce that the study 'integrates Meyer and Rowan's decoupling thesis with Zucker's institutionalization thesis,' and name the micro-process (social referencing under imperfect communication) that does the connecting — turning a single empirical setting into a bridge between two theory classics, plus boundary-setting against behavioral finance that names the difference (macro ideology vs. individual bias) while offering a bridge (confirmation bias)."
    caveat:
      - "The paradox rests on reading aggregate coefficients as market-level learning failure; the Enron/Worldcom speculative paragraph dated quickly (a caution against anchoring future-research paragraphs to current scandals); the undervaluation-signal disconfirmation is brief and would face stronger demands today."
story_assessment:
  overall_role: exemplar
  mode: single_read
```

## Story Reading

### Theme question

Is the stock market's valuation of a corporate policy a reliable, historically invariant indicator of technical efficiency — or is market value socially constructed, shifting with prevailing institutional logics and self-perpetuating through institutionalization even as evidence of decoupling accumulates?

### Whole-story synopsis

The paper opens on a division of labor: neoinstitutional theory has explained how corporate policies acquire legitimacy, spread, and get decoupled in industrial markets, while financial economics owns the capital-market side, treating the stock market's reaction to a policy adoption as a "reliable, historically invariant indicator" of efficiency benefits. Neither has asked whether institutional processes shape what financial markets pay for. The latent provocation comes from the authors' own stream: firms adopted-but-did-not-implement incentive plans and repurchase plans, yet — if the efficient-markets premise held — accumulating evidence of nonimplementation should have discounted the policy's value. Instead of accepting that premise, the paper recasts the measure itself: market reactions are not objective data on efficiency but "subjective data that reflect the symbolic value of adoption, neatly quantified and aggregated." The story's engine is a historical meaning reversal: under the old corporate logic, managers were professionals with unique strategic knowledge, so a buyback signaled exhausted investment prospects (negative reading); after the mid-1980s shift to an agency logic — managers as fungible, self-interested agents, firms as nexuses of contracts — the same buyback signaled free-cash-flow discipline (positive reading). From this engine two rival theory-pairs emerge: as prior nonimplementation accumulates, does the market learn to discount (H2, H3 — market learning) or does the policy borrow ever more symbolic value from prior adoptions and from the earlier diffusion of agency-framed LTIPs (H2a, H3a — institutionalization), with investors estimating other investors' reactions through social referencing? The verdict, staged first as a raw historical reversal (Figure 2: significantly negative reactions in the early period, positive from the mid-1980s, difference significant at p <= .01, all while nonimplementation grew) and then in regressions across three event windows: the market-learning hypotheses fail outright, the institutionalization hypotheses hold, and prior LTIP decoupling actually raises buyback reactions — symbolic value borrowed across policies. Supplementary analyses show implemented buybacks never improved profitability, sealing the last rational-learning exit. The ending converts the null into a paradox (markets are "teachable" but were taught too well), integrates Meyer and Rowan's decoupling thesis with Zucker's institutionalization thesis, and stakes out a sociology of finance distinct from behavioral finance.

### Characters and storylines

- **Main character — the stock repurchase plan:** a policy whose *meaning* is the protagonist; the story tracks a single practice through two institutional eras, and the plot question is what the market is paying for when it pays for it.
- **Protagonist theory — institutionalization via social referencing:** the process character that carries the positive predictions; investors estimate other investors' responses from prior reactions, so value accumulates through reciprocated interpretation rather than efficiency evidence.
- **Counter-reader — the market-learning perspective (financial economics):** the dignified rival; it owns the conventional wisdom and the event-study evidence, generates the paired negative hypotheses, and its core assumption (that markets learn) is exposed as "curiously not" empirically examined.
- **Supporting character — the agency logic of governance:** the macro ideological shift of the mid-1980s (Table 1's six-row contrast with the corporate logic); it supplies the positive interpretation that makes institutionalization possible and later becomes a character in its own right as the thing LTIPs legitimated.
- **Supporting character — decoupling / nonimplementation:** the accumulating counter-evidence that should deflate value; its paradoxical role is that growth in decoupling is the very variable the institutionalization story converts into rising symbolic worth.
- **Supporting character — LTIPs with agency explanations:** the predecessor policy from which buybacks "borrow symbolic value"; extends the story from one policy to the logic itself.
- **Judge — the stock market as aggregate audience:** measured by excess returns; passive as a person but the final arbiter whose verdict reverses over time.
- **Offstage anchor — the authors' own research stream:** Zajac & Westphal (1995) on logics and explanation language, Westphal & Zajac (1998, 2001) on decoupling; the paper is positioned as the arc's capital-market completion.
- **Storyline 1 (historical reversal):** corporate logic era → negative reactions; agency logic era → positive reactions; same practice, opposite verdicts (H1).
- **Storyline 2 (within-logic adjudication):** accumulating nonimplementation → discount (H2) or appreciation (H2a); the paper's central collision.
- **Storyline 3 (cross-policy generalization):** LTIP decoupling → skepticism spreads (H3) or symbolic value transfers (H3a); the storyline that makes the claim about logics, not just policies.
- **Intersection:** all three storylines are the same phenomenon at three scopes (one practice, one practice over time, one logic across practices); the social-referencing mechanism is the single hinge on which every turn of the plot swings.

### Five acts

- **Exposition:** Two literatures, two markets — neoinstitutional theory explains adoption and decoupling in industrial markets; financial economics certifies market reactions as historically invariant efficiency readings. The intersection is unowned. Sociology of markets (imitation, social referencing, Keynes, Merton, Zuckerman) supplies the raw material for an alternative.
- **Rising action:** The agency-logic shift is documented (Useem's discourse evidence, Davis et al.'s document analyses, the authors' own proxy-statement content analyses); Table 1 fixes the two readings of a buyback; H1 predicts the reversal. Figure 1 shows adoption and nonimplementation both rising; the paper poses the question the efficient-markets view cannot survive — does value fall with accumulated decoupling? — and builds the numbered rival pairs H2/H2a and H3/H3a.
- **Climax:** Figure 2 — the market's aggregate verdict on buybacks is significantly negative in the early period and positive from the mid-1980s, the shift significant at p <= .01, occurring precisely as nonimplementation accelerates. Table 3 confirms across all three event windows: prior nonimplemented plans predict *more* positive reactions (H2a); the market-learning hypothesis is not supported.
- **Falling action:** H3a holds — prior LTIP decoupling raises buyback reactions, symbolic value borrowed from the diffusion of the agency logic itself (H3 null). Robustness sweep: alternative implementation windows, Heckman selection, interaction models, moving three-year windows, crash-week inclusion. The "It might be suggested that..." paragraph delivers the closing argument: implemented repurchase plans show no effect on ROA/ROE in any lag structure — efficiency-learning cannot rescue the rival.
- **Denouement:** The Discussion converts the null into the "teachable but slow-learning" paradox, disconfirms the undervaluation-signal reading, supplies the inputs to the sociology-of-markets social-estimation process, explicitly integrates the decoupling and institutionalization theses, and maps the research frontier (tipping points between logics, the Enron-era reinterpretation of stock options) while fencing off behavioral finance with a named bridge.

### Tension

- **Source:** One observable — the market's reaction to a buyback announcement — is claimed by two theories that agree it is positive today but disagree on what it means and on what must happen as decoupling accumulates: a learned discount (market learning) or an appreciating symbolic value (institutionalization). The tension is sharpened because the rival's assumption (that markets learn) is foundational to an entire literature yet empirically unexamined.
- **Construction:** The paper never argues the rival down rhetorically; it builds the fork into history and into hypothesis numbering. The pre-agency-logic era gives the rival a fact it cannot own (negative reactions to the same practice); the paired hypotheses (H2/H2a, H3/H3a) make the data the referee; and the robustness-plus-profitability sequence removes each escape route in turn. The rival is quoted generously throughout — Buffett and Jensen speak for the agency-logic reading — before being turned.

### Alternative readings

- **author_signaled_alternative:** Investors react to buybacks as undervaluation signals (Ikenberry et al. 2000); the authors answer that this reading cannot explain negative reactions in the early period nor the gradual increase over time — an explicitly historical disconfirmation.
- **author_signaled_alternative:** Rising reactions might reflect rising real efficiency benefits from implemented plans or learning about them; answered with the supplementary ROA/ROE analyses (null effects, robust to lags and estimators).
- **analyst_counterfactual:** The count of prior adoptions (implemented and nonimplemented) is highly collinear (r = .53) and trend-driven; a skeptic could read the Table 3 coefficients as a general familiarity/attention effect (any prior adoption raises salience) rather than institutionalization — the paper's own symmetry finding ("regardless of whether those plans were implemented") is offered as institutionalization evidence but is also consistent with salience. The year-effect controls make this partially testable but the card records it as an analyst-generated alternative.

## Story Assessment

- **Theme coherence:** `works` — one question (is market value socially constructed) organizes the logic-shift history, both rival pairs, the robustness sequence, and the ending; every hypothesis is a face of the same claim at a different scope.
- **Character discipline:** `works` — the repurchase plan, the agency logic, and social referencing have structurally distinct roles; the market-learning perspective is a genuine counter-reader rather than a straw man; the authors' own prior studies stay offstage as the stream's arc rather than hijacking the plot.
- **Knot integrity:** `works` — a head-on collision between two theories that make opposite signed predictions on the same observable, with the rival owning the conventional wisdom and the adjudicating evidence (a historical reversal the rival literature never looked for) genuinely capable of deciding.
- **Plot emergence:** `works` — Figure 1 (adoption and nonimplementation both rising) is the phenomenon generating the plot; hypotheses fall out of the logic contrast and the decoupling record rather than being reverse-engineered from the results.
- **Tie–unravel alignment:** `works` — every hypothesis is adjudicated in the promised order; H1 is tested with a pre-announced difference-in-t criterion; the strongest promised test (value rising despite decoupling) is literally delivered in Table 3 and reinforced by the profitability null. The one looseness — the unmeasured social-referencing mechanism — is calibrated as `partly_probed`, not as a story failure.
- **Ending quality:** `works` — the ending does not repeat findings: it upgrades the null into a paradox about the rival community, names the two theory classics the study connects, answers the micro-foundations question raised by the sociology-of-markets literature, and sets a disciplined boundary against behavioral finance while extending a bridge to it.
- **Boundary:** This evaluates storytelling only — not causal identification, research quality, or journal value. Era flags (Analysis/Results separation, one-tailed tests, thin magnitude reporting, dated scandal paragraph) are craft-boundary notes carried in section caveats, not story failures.

## Learning Affordances

### Introduction

- **Suitable:** `yes`
- **Learn:** (1) The bridge-as-gap opening — give each of two literatures its home turf, name the unowned intersection, and derive the dominant perspective's own corollary ("adopt-but-don't-implement → the market should discount") as the falsifiable prediction your study will stress. (2) Dependent variable as protagonist — build the intro around one contestable characterization of your DV ("historically invariant indicator" vs. "socially constructed"), so the entire paper reads as an adjudication of what the measure *is*.
- **Do not copy:** The move needs two mature literatures whose intersection is genuinely unclaimed; the citation-dense, jargon-presuming neoinstitutional prose style is native to the 2004 ASR register, and the intro carries no stakes or magnitude preview — modern versions should add both.

### Theory

- **Suitable:** `yes`
- **Learn:** (1) The sign-flip comparison table — demonstrate historical contingency structurally (same practice, opposite meanings under two logics, in one table) before asserting it in prose, then cash the flip into the first hypothesis. (2) Fair-fight hypothesis pairing — number the rival's prediction and yours as adjacent pairs (H2/H2a, H3/H3a), rival first, stated at full strength including its own robustness clause, so the data adjudicate rather than the adjectives.
- **Do not copy:** Requires an observable pre-period in which the rival reading already fails (a negative-reactions era) — without an era boundary the pairing collapses into difference-of-degree; the social-referencing mechanism is asserted, so a modern version needs perceptual, trader-level, or heterogeneity evidence before claiming the interior of the process.

### Methods

- **Suitable:** `partial`
- **Learn:** Design-to-story alignment — the sample window spans the logic shift so both readings of the practice are observable; implementation-window, event-window, and selection-model choices each answer a named rival objection inside the design chapter; the first-three-years exclusion and its robustness checks are narrated as consequences of the coding rule, not buried.
- **Do not copy:** Era presentation (Analysis/Results split, one-tailed tests, no AME/magnitude beat); the market-level count operationalization with r = .53 collinearity would need explicit defense today — borrow the alignment logic, not the estimator or coding presentation.

### Results

- **Suitable:** `yes`
- **Learn:** (1) Figure-first climax — show the raw historical reversal (with t-statistics and the pre-announced difference test) before the regression table, so controls confirm a story the reader has already seen. (2) The falsification rhythm — narrate the rival's null as a headline finding, convert the symmetrical coefficient ("regardless of whether those plans were implemented") into a mechanism argument, then meet the reader's best objection in an explicit "It might be suggested that..." paragraph and seal the last exit with the profitability nulls. This is the paper's most transferable prose rhythm.
- **Do not copy:** One-tailed testing and minimal economic-magnitude interpretation are era artifacts; the aggregate design licenses no claims about any investor actually referencing prior reactions — the writer must keep mechanism claims at the pattern level unless perceptual data exist.

### Discussion

- **Suitable:** `yes`
- **Learn:** (1) The paradox ending — turn the rival's null into a paradox implicating the rival community itself ("the effort... to emphasize the rationality of stock buybacks may have been too successful, paradoxically limiting the market's subsequent opportunity to learn"); a paradox recomputes the whole story in one sentence and adds a contribution instead of a recap. (2) The named-integration close — explicitly state which two theory classics your story connects (Meyer & Rowan's decoupling + Zucker's institutionalization) and name the micro-process that does the connecting, so the contribution is a bridge, not a finding.
- **Do not copy:** The paradox rests on reading aggregate time-series coefficients as market-level learning failure; the future-research paragraph anchored to Enron/Worldcom dated within years — anchor speculative extensions to mechanisms, not to current scandals.

## Comparison prompt

Against the other two Westphal-system cards already in the corpus: all three stories conclude that appearance is rewarded over substance, but each stages the adjudication differently — westphal1998 splits a single event (adopted vs. implemented, explained vs. not) and asks *who is fooled* (audience construction); this 2004 card splits history (pre- vs. post-agency-logic) and asks *when fooling becomes collective self-deception* (institutionalization); westphal2005 measures a perception gap on the same scale and asks *why the actors themselves cannot see it* (pluralistic ignorance). Concrete reading question: when you have a symbolic-vs-substantive puzzle, what does each staging — within-event split, over-time reversal, same-scale perception gap — allow your ending to claim about the *locus* of the irrationality (audience, market, actors), and which locus does your design actually license?

## Notes

- Venue verified from the source front matter: *American Sociological Review*, 2004, 69(3), 433–457 (DOI 10.1177/000312240406900306) — the intake assumption "ASQ" was wrong for this paper; recorded as ASR.
- PDM slice artifacts: stray OCR fragments ("Thu, 08 Dec") inside theory.md and Table 2; Figures 1–2 present as image references only — figure content reconstructed from in-text narration and captions, which the paper itself narrates densely enough for story reading.
