# Story Learning Card — Anand & Mukherjee (2024, Organization Science)

## Metadata

```yaml
schema_version: "4.0-lite"
id: anand2024-slipups-knowledge-gaps
paper:
  citekey: anand2024learningfailures
  title: "Learning from Failures: Differentiating Between Slip-ups and Knowledge Gaps"
  outlet: "Organization Science"
  year: 2024
  publication_status: published
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A complete learning object for how a paper can split a single undifferentiated phenomenon (learning from failure) into a two-way typology, run paired hypotheses for each type, accept a differentiated pattern of support (one type learns, the other does not), and turn that asymmetry into the paper's most memorable finding through a post hoc memory-decay analysis."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "sections/introduction.md + sections/theory.md (primary story reading)"
    - "sections/results.md + sections/discussion.md (payoff checks)"
    - "sections/methods.md (story-evidence alignment audit)"
    - "sections/introduction.json / theory.yaml / theory.report.md / methods.json / results.json (verified four-section distillations)"
    - "L2 coherence flags: C1 (baseline premise in lieu of H1), C4 (no economic significance reported)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: null
classification:
  theoretical_problem_form: [incompleteness-typology-gap, contingency-reconciliation]
  narrative_dynamics: [paired-type-fork, asymmetric-support-resolution, capability-enhancement-arc, quick-decay-versus-slow-persistence]
  retrieval_signals: [learning-from-failure, failure-typology, product-recall-counts, absorptive-capacity-moderator, negative-binomial-panel, memory-decay-post-hoc]
  confidence: provisional
mechanism_evidence: "partly_probed — the attention-focusing mechanism is probed through supplementary models (litigation, serious adverse events, FDA warning letters as alternative attention triggers) and cross-learning models, but root-cause search, codification, and compliance decay are never directly observed; learning itself is inferred from reductions in subsequent same-type recall counts."
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Pair a qualitative vignette with an archival timeline as a two-example bridge placed after the theory preview and before the empirical setting: the interview narrative shows the complete failure-to-investigation-to-redesign loop (the how), while the da Vinci Figure 1 plot shows the same mechanism quantitatively over 18 years (the whether), and each example closes by naming its construct lesson."
      - "State the two-way categorization and the three-part result preview in the introduction itself, so the reader meets the typology before the theory section elaborates it."
    caveat:
      - "The paired-example bridge is expensive (an interview narrative plus an 18-year single-firm figure) and earns its place only because the two failure types are new and easily confused; do not import it as decoration for familiar constructs."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Open the hypotheses by staging the two opposing views (failure activates search vs. firms are myopic and uncertain) and reconcile them through the contingency view, which pre-positions the moderators as arbiters of when learning happens."
      - "Carry a large hypothesis tree (8 hypotheses) on one spine by arguing the main-effect fork once (attention to search to implementation) and letting each typed cell add only its type-specific repair steps, then pairing each moderator as stock (accumulated patents) and flow (lagged R&D intensity) facets of one capability lens."
    caveat:
      - "The regulator-procedure scaffolding (Figure 3 step coordinates, five practitioner interviews, a 34-year FDA expert) is high-investment phenomenon anchoring that fits FDA-regulated recalls; it is not a portable default module."
      - "Moderator arguments are single-sided (enhancing high side only) and legitimate here only because capability is argued as monotone; a non-monotone moderator in a new paper needs full bilateral argumentation."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Align measurement windows with the story's time logic: both accumulated recalls and accumulated patents use the same 10-year window so that their interaction is interpretable, and the post hoc analysis re-estimates 1-4 year windows precisely to test the decay claim the ending depends on."
    caveat:
      - "The sample funnel (firms with at least 10 years of observations and at least 30 recalls) selects high-recall, long-lived firms; the learning story is estimated on exactly the firms with the most failure experience, and robustness supplements do not erase that design-for-story choice."
      - "The process/design recall classification comes from the authors' own text analysis (95% match with firm self-classification on a subset), so the typology that drives the whole plot is a constructed measure, not an independent fact."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Report the baseline learning effect as an explicitly unhypothesized 'baseline premise in lieu of Hypothesis 1' that replicates extant work, so the hypothesis tree carries only the genuinely new forks (H1a/H1b, H2/H3 families)."
      - "Let honest nulls become the plot: H1a (process learning) and H3a are reported as unsupported in the same tables and tone as the supported hypotheses, then the post hoc window analysis converts the asymmetry into the paper's signature finding — process learning accrues quickly but decays, design learning accrues slowly but persists and is codified."
    caveat:
      - "No economic significance is reported anywhere (L2 C4): magnitudes exist only as standardized NB coefficients, so the reader cannot judge how much learning matters; this is a real gap in the exemplar, useful as a cautionary signal, not a move to copy."
      - "Positive main effects of patents and R&D intensity on subsequent recalls coexist with negative interactions; the paper reads this as innovation-pro firms issuing more recalls, a interpretive choice a writer cannot reuse without the same institutional argument."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Return to the opening question with a transformed answer: the discussion does not merely restate that firms learn, it splits the mechanism into cultural mechanisms (compliance, for slip-ups) versus structural mechanisms (codified design knowledge, for knowledge gaps) and uses the post hoc decay cycles to explain why the slip-up storyline stalled."
    caveat:
      - "The practical section generalizes the typology to unregulated software platforms and other industries beyond the evidence; the generalization is framed as implication, not demonstrated transfer."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
```

## Story Reading

### Theme question

Do organizations actually learn from product failures — and does the answer depend on what kind of failure it was? When a failure comes from a slip-up in executing a known process versus a gap in what the firm knows about its own design, do firms reduce subsequent failures of that type, and do their innovation capabilities (accumulated patents as knowledge stock, lagged R&D intensity as knowledge flow) enhance that learning?

### Whole-story synopsis

The paper opens inside organizational learning theory's most familiar promise — failure activates search and improvement — and immediately refuses to let the promise stand unexamined: it splits "failure" into two kinds, slip-ups in executing established processes and knowledge gaps in product designs, built on the recognition that the two demand different learning mechanisms (reinforcement of compliance versus experimentation and redesign). Rather than a personified antagonist, the tension is a genuine theoretical standoff: one view holds failures are the best teachers because they seize attention; the opposite holds firms respond myopically and learn little. The paper reconciles the two through the contingency view, making the failure type itself and the firm's innovation capabilities the conditions that decide the outcome. Two paired worked examples — an interview narrative of a medical implant recalled for inverted implantations and redesigned with a defect-prevention feature, and the da Vinci surgical robot's 18-year timeline of adverse events, recalls, patents, and design approvals — make the abstract constructs visible before any hypothesis is tested. Theory then builds a paired hypothesis tree: H1a/H1b predict learning (fewer subsequent same-type recalls) for each failure type; H2/H3 families predict that innovation stocks and flows enhance that learning overall and for each type. The FDA-regulated recall context supplies count data; the design becomes a firm-year panel (108 firms, 1,728 firm-years, 2000–2016) estimated with negative binomial GLMs with firm and year fixed effects. The results stage an asymmetric resolution: overall learning is supported as an explicitly unhypothesized baseline premise; design-related (knowledge gap) learning is supported (H1b), but process-related (slip-up) learning is not (H1a) — while the capability enhancements hold for both types (H2a, H2b, H3b supported; H3a not). The discussion accepts this asymmetry rather than burying it: learning is contingent on failure source, and the post hoc analysis of 1–4 year accumulation windows gives the stall a mechanism-shaped ending — process lessons arrive fast but decay as attention and compliance erode, while design lessons accrue slowly but persist because they get codified into design documents and formulations. The opening question returns changed: the real story is not whether firms learn from failure, but that the two failure types run on different clocks.

### Characters and storylines

- **Main characters (a paired fork, not a single hero):** slip-up failures (process-related recalls) and knowledge-gap failures (design-related recalls). The whole plot exists because the paper insists these are different characters with different motives — one calls for restoring compliance, the other for searching and redesigning — and the plot's outcome is that only one of them delivers the promised learning.
- **Enhancing characters (the moderators):** accumulated patents (innovation stock) and lagged R&D intensity (innovation flow), jointly carrying the absorptive-capacity lens. They are what lets the paper move beyond "does learning happen" to "who learns better" — and they enhance learning for both failure types even where the main effect fails.
- **Outcome character:** subsequent same-type recall counts, the operationalization of "learning" as reduction — deliberately narrow, and the source of both the design's cleanliness and its interpretive ceiling.
- **Contextual supporting cast:** the FDA's recall-approval apparatus (Figure 3's step schematic, the 34-year FDA expert, five practitioners), which gives the learning steps institutional texture and authorizes the process/design split.
- **Storyline 1 (slip-up):** accumulated process recalls → SOP updates and compliance training → fewer subsequent process recalls. This storyline is predicted, tested, and defeated (H1a unsupported; H3a unsupported) — only to be revived in the denouement as a fast-but-decaying learning clock.
- **Storyline 2 (knowledge gap):** accumulated design recalls → internal/external search and redesign → fewer subsequent design recalls. Supported (H1b), and strengthened by both capability facets (H2b, H3b).
- **Intersection:** the capability characters cross both storylines — absorptive capacity helps firms learn from either type of failure, which is what keeps the two-way typology from collapsing into two unrelated papers.

### Five acts

- **Exposition:** Learning from failure is a canonical promise, but the literature is inconsistent, and repeated calls ask for differentiation by failure type and for conditions conducive to learning; the paper stakes its identity on a two-way failure typology and the absorptive-capacity lens.
- **Rising action:** The contingency view reconciles the do-firms-learn standoff; theory walks the FDA's recall procedure to argue paired hypotheses — learning from each failure type, enhanced by innovation stocks and flows — and the worked examples let readers see both failure types before the tests.
- **Climax:** The results reveal the asymmetry: knowledge-gap learning works (H1b) while slip-up learning does not (H1a), even though innovation capabilities enhance learning in both storylines (H2a/H2b/H3b; H3a alone fails).
- **Falling action:** Supplementary analyses probe the attention mechanism (litigation, serious adverse events, warning letters as alternative attention triggers; cross-learning models against the firm-capability alternative explanation), and IV (capital reserves and surplus) plus GEE robustness checks hold the main results in place.
- **Denouement:** The post hoc window analysis (1–4 years) transforms the defeated slip-up storyline into the paper's signature insight — process learning is quick but deteriorates while design learning is slow but persistent and codified — and the discussion recasts the question from whether firms learn from failure to which mechanisms (cultural compliance versus structural codification) each failure type demands.

### Tension

- **Source:** The tension is theoretical, not personified: organizational learning theory contains a live standoff — failures activate attention and focused search versus firms react myopically, face causal ambiguity, and do not sustain change. Neither view can be dismissed, and the paper's own data will later split the difference by failure type.
- **Construction:** The theory section stages the two views explicitly and reconciles them through the contingency view ("conditions under which failures may or may not lead to learning"), so the moderators enter as arbiters rather than afterthoughts; the epistemology sentence in the construct definition ("less ambiguity about the causes... slip-up... than knowledge gap") quietly pre-loads the asymmetry the results will deliver.

### Alternative readings

- **analyst_counterfactual:** The paper could have been read as a straight absorptive-capacity application (H2/H3 families as the real contribution, with the typology as scaffolding). The narrative weight — the worked examples, the paired fork, the post hoc decay analysis — supports the typology-first reading recorded here, but a capability-first reading is defensible and would re-center the introduction's third contribution.
- **documented_literature_alternative (L2 C1, paper-designed):** The overall learning main effect (H1) is never formally hypothesized; the paper deliberately substitutes a "Baseline Premise in Lieu of Hypothesis 1" that replicates extant work. This is a front-end design choice to keep the hypothesis tree on the new forks, not an oversight — and it is the load-bearing move that lets eight typed hypotheses stay visible.

## Story Assessment

- **Theme coherence:** `works` — the differentiation question organizes everything downstream: the typology, the paired hypotheses, the typed dependent variables, and the ending's two-clock conclusion all answer the same question.
- **Character discipline:** `works` — the two failure types, the two capability facets, and the recall-count outcome each hold one role; the regulator apparatus supports without hijacking. The only near-distraction is the capability main effect's positive sign, which the paper manages rather than pursues.
- **Knot integrity:** `works` — the inconsistency in prior learning-from-failure findings is a genuine challenge the typology plausibly addresses, and the contingency reconciliation makes the resolution available to the study by design.
- **Plot emergence:** `works` — the FDA procedure walkthrough generates the repair-step differences that generate the hypotheses; the design (typed counts, matched 10-year windows) arises from the constructs rather than being forced onto them.
- **Tie–unravel alignment:** `partly_works` — the evidence answers the differentiated question and honors the null (H1a, H3a) visibly, but learning is only ever recall-count reduction: no root-cause analysis, codification, or compliance behavior is observed, so the mechanism the theory promised is probed (attention triggers) rather than shown, and no economic magnitude is ever reported (L2 C4).
- **Ending quality:** `works` — the post hoc decay analysis and the cultural-versus-structural mechanism split genuinely transform the opening: the reader leaves understanding why the slip-up storyline failed, not just that it did.
- **Boundary:** This evaluates storytelling only; it is not a judgment about identification quality, the IV's validity, or the paper's scientific contribution.

## Learning Affordances

### Introduction

- **Suitable:** `yes`
- **Learn:** Use a paired worked example (qualitative vignette + archival figure) as a construct-operationalization bridge after the theory preview; state the typology and the result asymmetry preview in the introduction so the theory section elaborates rather than introduces.
- **Do not copy:** The implant/da Vinci examples and the two-example cost are justified only by genuinely new, confusable constructs; the examples must point at one mechanism from two sides, never become a case-pair anthology.

### Theory

- **Suitable:** `yes`
- **Learn:** Open hypotheses with an explicit two-view standoff reconciled by the contingency view so moderators arrive as arbiters; carry a large paired hypothesis tree on one argued spine (fork once, per-cell type-specific steps) with moderators decomposed as stock/flow facets of a single lens.
- **Do not copy:** The Figure 3 step-coordinate citation system, the expert/practitioner testimony inside theory, and the single-sided enhancement arguments are phenomenon- and monotonicity-specific; the slip-up/knowledge-gap labels and their repair steps belong to this paper.

### Methods

- **Suitable:** `partial`
- **Learn:** Match accumulation windows across interacting variables so interactions are interpretable, and design the accumulation window itself as a testable parameter (the post hoc re-estimation) when the story's claim is about time.
- **Do not copy:** The ≥10-year/≥30-recall sample funnel and the authors' own text classification of recalls are story-serving design choices with real selection and construct-dependency costs; a new paper must re-derive, not inherit, them.

### Results

- **Suitable:** `yes`
- **Learn:** Handle an expected-but-not-novel main effect as a labeled baseline premise instead of a fake hypothesis; report typed nulls in the same voice as supports and then spend a post hoc analysis converting the null asymmetry into the paper's most transferable finding.
- **Do not copy:** The absence of economic-significance reporting (L2 C4) is a weakness to avoid, not a convention to follow; and the positive capability main effects' interpretive rescue (innovation-pro firms attract more recalls) depends on institutional arguments specific to FDA recall data.

### Discussion

- **Suitable:** `yes`
- **Learn:** Close by splitting the theoretical mechanism into the mechanisms each character demands (cultural compliance vs. structural codification) and use a time-window analysis to explain — not excuse — the failed storyline.
- **Do not copy:** The generalization to software platforms and unregulated industries outruns the two-industry evidence; bounded generalization must be earned by the reader's own setting.

## Comparison prompt

Compared with kalaignanam2013-recall-learning, which treats learning from recalls as a single undifferentiated experience curve with a mediating reliability mechanism, what does Anand & Mukherjee gain — and what does it give up — by forking failure into two types and losing a single mediating mechanism? And compared with mukherjee2018-medical-device-recall-bias, where recall experience carries a bias lesson, does the same FDA recall panel support a learning story, a bias story, or a type-dependent mixture of both?
