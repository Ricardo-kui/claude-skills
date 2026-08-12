# Story Learning Card — Ridge, Hill, Ingram, Kolomeitsev & Worrell (2024, Academy of Management Journal)

## Metadata

```yaml
schema_version: "4.0-lite"
id: ridge2024-ceo-paranoia
paper:
  citekey: ridge_hill_ingram_kolomeitsev_worrell_2024_amj
  title: "Avoidance and Aggression in Stakeholder Engagement: The Impact of CEO Paranoia and Paranoia-Relevant Cues"
  outlet: "Academy of Management Journal"
  year: 2024
  publication_status: published
  paper_type: quantitative
  source_version: OvisOCR2_full_text (2026-08-10)
  inclusion_rationale: "A partial exemplar for learning honest mixed-evidence staging: a front-end dual promise (how CEO paranoia shapes stakeholder engagement + what shifts it over time), a measure built from scratch as a co-contribution, and a results section that reports a null (H2) and a significant-but-small effect (H4) in full and converts them into a stakeholder-differentiation boundary rather than hiding them."
reading_scope:
  sections_read: [abstract, introduction, theory, methods, results, additional_analyses, discussion, conclusion]
  coverage: complete
  source_records:
    - "文献笔记库/01 导入/论文导入/Ridge-2025-Avoidance and Aggression in Stakeho-OvisOCR2-20260810-173132.md (full text)"
    - "sections/introduction.json"
    - "sections/theory.report.yaml"
    - "sections/methods.json"
    - "sections/results.json"
  note: "Giant HTML/MathML table rows (Tables 1-4) and base64 figure rows were skipped; all prose, table notes, H1-H4 result paragraphs, Additional Analyses, Discussion, and Conclusion were read. Source filename reads 'Ridge-2025' but the DOI and in-text citations confirm AMJ 2024; year is registered as 2024 and the filename treated as a source-version artifact."
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Matches the default attention profile. The imperfect-paper dimensions (H2 null, H4 small-effect honesty, deferred contribution claims) received extra attention in the Results and Discussion readings because they are the card's central learning object."
classification:
  theoretical_problem_form: [trait-valence-asymmetry, stable-disposition-situation-activation]
  narrative_dynamics: [safety-behavior-continuum, cue-triggered-behavioral-switch, stakeholder-parallel-arenas, honest-mixed-evidence-staging]
  retrieval_signals: [ceo-paranoia, stakeholder-engagement, avoidance-aggression-switch, trait-activation, lobbying-breadth, competitive-actions]
  confidence: reviewed
mechanism_evidence:
  status: partly_probed
  basis: "The avoidance default is directly tested for government (H1 supported) but not for competitors (H2 null); the activation switch is directly tested in both arenas (H3 interaction flips the effect; H4 significant-but-small and the paper itself notes the interaction direction is not fully in line with the theorized mechanism); TMT risk perception and strategic attention are probed as auxiliary assumption tests (Table A8). Safety behaviors are theorized process states (B0), not measured mediators — the paper makes no formal-mediation claim."
story_track:
  fed_flags:
    - flag: "C1"
      content: "Intro carries a mild Inadequacy flavor (trait-valence selective attention: upper echelons studied self-aggrandizing traits, neglected self-deflecting ones) not independently revised in the theory; the primary Incompleteness is delivered via the mechanism extension (trait-activation switch)."
      consumption: "Introduction and Theory learning moves both flag that the valence carve-out must be cashed by the theory; the card does not treat the Inadequacy flavor as a standalone gap."
    - flag: "C4"
      content: "H4 is significant but of small practical effect, honestly de-emphasized in Results; slight tension with the intro's 'broad support' framing — the paper itself discloses this."
      consumption: "The Results learning move (significant-but-small de-emphasis) and the imperfect-paper reading rest on this flag; the intro's 'broad support' claim is read as a preview contract that the Results honors by disclosing the boundary."
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Ground a construct in practitioner discourse before the academic definition: let named CEOs speak the construct's own name, then formalize it into a measurable disposition ('As the epigraphs imply...')."
      - "Preview an honest asymmetric result: announce support for one of two parallel theorized targets and an explicit null for the other in the findings preview, so the front-end contract is honest about boundaries."
    caveat:
      - "The epigraphs must genuinely use the construct's name; do not pile more than ~4 practitioner voices, and the academic definition must follow immediately or the hook reads as journalism."
      - "The trait-valence carve-out is a mild Inadequacy flavor that the theory does not separately revise; it works here only because the primary Incompleteness is delivered by the mechanism extension. Do not copy the valence carve-out unless the theory will cash it."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Model a stable disposition as two manifestations on one continuum (avoidance and aggression on a safety-behavior continuum), with a dedicated second-act theory subsection (trait activation) carrying its own theoretical engine and generating cue-triggered moderation hypotheses."
      - "Organize hypotheses as per-stakeholder paired parallel: each stakeholder (government, competitors) receives a paired main effect and its own cue-triggered moderation, so the reader sees where the trait works and where it fails."
    caveat:
      - "The activation switch requires a concrete cue operationalization (here, regulatory ruling severity and rival attacks defined as stakeholder actions targeting the firm); without observable paranoia-relevant cues the switch reads as situationism hand-waving."
      - "Safety behaviors are B0 process states, not measured mediators; do not copy the theory into a formal-mediation claim. The mitigation-interaction form implies the moderator switches on an OPPOSITE manifestation (aggression), not mere buffering."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Build the focal measure from scratch with a full validity chain (components -> expert sort -> deductive dictionary -> student sort -> PFA -> nomological -> stability), making the measure a co-contribution that enables the whole test."
      - "Declare temporal spacing in one sentence (DV t+1, IV and controls t) and stage endogeneity as diagnose-first (RIR with N-to-overturn counts) then cure-second (2SRI), pairing naive and cured estimates."
    caveat:
      - "Reusing validation measures as 2SRI instruments (sadness/negativity) requires an independent exclusion argument; the paper only implies it. The single-sentence estimator choice (Tobit / negative binomial) with no censoring share or overdispersion test, and the undefended no-firm-FE choice, are cautionary elements, not a model to copy."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Front-load the identification defense (RIR + 2SRI naive-vs-cure pairing) before the main results, establishing credibility before revealing the evidence."
      - "Stage mixed evidence honestly: report a null in full with a sign-reversal read as an alternative mechanism rather than skipping it; explicitly de-emphasize a significant-but-small effect ('does not appear to be particularly meaningful in practice'); and synthesize the mixture into a single boundary thesis (effects differ by stakeholder) with an explicit hand-off to the Discussion."
    caveat:
      - "The small-effect de-emphasis only works when the effect truly is small and the honesty is part of the front-end contract; do not de-emphasize a meaningful effect, and do not upgrade a sensitivity-to-null (Tables A9/A10) into support — hedge it with inflation mechanics (Kalnins 2018)."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Return to the field call (Gamache et al.'s temporal-dynamics call) and the two gap layers, then convert mixed evidence into a theoretical boundary (stakeholder differentiation) instead of merely repeating findings."
      - "Reframe the trait as bright-and-dark (a balanced view) to open future directions and soften the stigma of a 'dark' disposition."
    caveat:
      - "The competitor-anomaly explanation ('it may be that government is viewed with more skepticism because of coercive political power') is explicitly speculative; route it to future research rather than turning it into a post-hoc claim of support."
story_assessment:
  overall_role: partial_exemplar
  mode: first_read_reviewed
```

## Story Reading

### Theme question

Can a stable, negatively-valenced CEO disposition (paranoia) systematically shape how the firm engages the external stakeholders it depends on — producing avoidance as a default safety behavior, and flipping that avoidance into aggression when the stakeholder's own actions (regulatory rulings, rival attacks) signal that avoidance has failed?

### Whole-story synopsis

The paper opens with two CEO epigraphs (Washkewicz of Parker Hannifin, Krzanich of Intel) that speak "paranoia" as a lived managerial idiom, reinforced by Bill Gates's "paranoia principle" and Andy Grove's "only the paranoid survive." The academic definition then formalizes paranoia as a stable dispositional trait — suspicion, ill will or resentment, mistrust, and belief in external control. The front end builds a two-layer gap: paranoia has no theory of organizational action, and the upper echelons literature has studied the self-aggrandizing half of the trait space while neglecting self-deflecting traits. Gamache et al.'s (2020) call for a theory of "how and why" CEOs pursue stakeholder engagement strategies — and how those approaches shift over time — becomes the field invitation the paper answers. The theory builds a threat-processing cascade (hypervigilance → rumination → self-as-target and sinister attribution biases → jumping to conclusions / suspicion confirmation → safety behaviors) that lands on avoidance as the dominant default. Upper echelons theory conducts this into two parallel arenas — government (lobbying breadth) and competitors (competitive actions) — yielding negative main effects (H1, H2). Act 2 of the theory opens trait activation: paranoia-relevant cues — stakeholder actions that target the firm, operationalized as regulatory ruling severity and rival attacks — signal that avoidance has failed, switching the CEO toward aggression, the opposite end of the safety-behavior continuum, and thus increasing engagement in the very actions previously avoided (H3, H4 as mitigation interactions). The Methods build a content-analytic measure of CEO paranoia from scratch (six components, nine-step validation chain) on an S&P 1500 panel (2010–2017; 925 CEOs, 774 firms, 3,823 firm-years), with temporal spacing and a selection correction. Results deliver a deliberately asymmetric payoff: H1 and H3 support avoidance-then-aggression toward the government (lobbying breadth falls ~7% at +1SD, then more than doubles as regulatory rulings escalate); H2 is a reported null for competitors (the coefficient is even positive); H4 is significant but explicitly de-emphasized as not practically meaningful. The Additional Analyses probe underlying assumptions (TMT risk perceptions, strategic attention) and transparently disclose sensitivity boundaries (null→significant margins hedged with inflation mechanics). The Discussion returns to the field call, converts the mixed evidence into a stakeholder-differentiation boundary (the same trait produces avoidance toward coercive government but not toward competitors, whose attacks are read as expected economic competition), reframes paranoia as bright-and-dark, and hands the measure to the field as a methodological contribution.

### Characters and storylines

- **Main character:** CEO paranoia — the stable dispositional trait whose cognitive processing (hypervigilance, rumination, self-as-target and sinister attribution biases) gives it motive.
- **Response-space character (mechanism):** the safety-behavior continuum — avoidance and aggression as opposite ends, giving the theory an internal comparison and the two DVs their interpretation.
- **Switch character:** trait activation, triggered by paranoia-relevant cues — stakeholder actions that target the firm — which flips the trait's dominant manifestation.
- **Parallel arenas (not antagonists):** government (lobbying breadth) and competitors (competitive actions) — two external stakeholders, each with a paired main effect plus cue-triggered moderation branch.
- **Supporting characters:** TMT risk perceptions (auxiliary evidence of the premise); the named CEO exemplars (Washkewicz, Krzanich, Gates, Grove) in the hook and McMillon in the theory.
- **Storyline 1 (avoidance):** paranoia → threat-processing → safety behavior of avoidance → reduced engagement (H1 supported for government; H2 null for competitors).
- **Storyline 2 (activation):** stakeholder actions cue failure of avoidance → trait activation → shift to aggression → increased engagement in the same action categories (H3 supported with a flip; H4 significant-but-small).
- **Intersection:** the same trait yields opposite behaviors across time and contexts depending on whether cues say avoidance is working; and yields asymmetric effects across stakeholders, which the paper converts into a boundary.

### Five acts

- **Exposition:** practitioner chorus grounds paranoia; academic definition; two-layer gap (no theory of paranoia→action; trait-valence asymmetry); field call.
- **Rising action:** threat-processing cascade builds the avoidance default; upper echelons conducts it; two parallel stakeholder branches; H1/H2.
- **Climax:** trait-activation act (cue-triggered switch, H3/H4) and the results reveal the asymmetric payoff — H1/H3 support, H2 null, H4 small.
- **Falling action:** front-loaded identification defense, Additional Analyses (assumption tests, sensitivity with inflation hedging), and R9 synthesis into stakeholder differentiation.
- **Denouement:** Discussion returns to the field call and the two gap layers, converts mixed evidence into a boundary, reframes paranoia as bright-and-dark, contributes the measure, and routes the competitor anomaly to future research.

### Tension

- **Source:** the same disposition culturally celebrated as vigilance ("only the paranoid survive") is theorized to systematically distort engagement with the external actors firms depend on — suppressing engagement by default and, under threat cues, escalating into aggressive direct engagement. The central challenge is a stable trait with two opposite behavioral manifestations switched by the very stakeholders it engages.
- **Construction:** the safety-behavior continuum supplies an internal comparison (avoidance ↔ aggression) so the shift is observable in the same DV; the parallel two-stakeholder design lets the reader see exactly where the trait works (government) and where it does not (competitors), which is how the paper's honesty becomes visible.

### Alternative readings

- **analyst_counterfactual:** A single-mechanism story could have predicted paranoia → avoidance across all stakeholders and treated the competitor branch as a failed hypothesis. The paper instead doubled the mechanism (avoidance default + activation switch) and used the competitor failure to build a stakeholder-differentiation boundary. An analyst reading: the H2 null and H4 small effect could equally be read as the theory over-reaching; the authors' staging turns this into a strength, but that is a judgment call, not an observed fact.
- **cross-paper comparison note:** against positively-valenced upper-echelons traits (e.g., narcissism), the presence of a cue-triggered second manifestation is what lets a null in one arena become a boundary rather than a failed study; the concrete reading question is whether a dual-manifestation design is what predicts where honest nulls get reported.

## Story Assessment

- **Theme coherence:** `works` — one construct organizes the gap, theory, measure, two DVs, and the ending; the avoidance→aggression-via-cues knot stays central through the Discussion. The mild Inadequacy flavor (C1) is a stray but does not break the theme because the mechanism extension carries the Incompleteness.
- **Character discipline:** `works` — paranoia is the protagonist; the avoidance/aggression continuum and the two cue moderators specify its manifestations; government and competitors stay parallel arenas with no crowd actors. (Minor: the generic "stakeholders" category is diffuse, but it is a scope statement, not a character.)
- **Knot integrity:** `works` — the unanswered question (a disposition celebrated as vigilance, with a default and a trigger) is genuine and the design can plausibly address it; though the gap is asserted as a void rather than an explicit "surprising because" puzzle, the safety-behavior continuum plus activation switch gives the knot real content.
- **Plot emergence:** `partly_works` — the theory genuinely generates the design (parallel branches, cues as moderators, a measure built to test it), but the payoff is asymmetric: Act 2's promise is fully cashed only for government; the competitor branch resolves as a null and a small effect, so the plot rises unevenly.
- **Tie–unravel alignment:** `works` — the results answer the front-end dual promise (how paranoia shapes engagement + what shifts it), including honest disclosure of where it fails; the preview's embedded null is honored by the Results.
- **Ending quality:** `works` — the Discussion returns to the field call, transforms the mixed evidence into a stakeholder-differentiation boundary, reframes the trait as bright-and-dark, and routes the anomaly to future research rather than merely repeating findings.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, the content-analytic measure's validity, or the research's value. The H2 null and H4 small effect are evidence facts, not story defects; their handling is what is assessed.

## Learning Affordances

### Introduction and Theory

Learn the discipline of constructing a dual-manifestation theory: name both poles of the behavioral continuum and the cue that switches between them before deriving hypotheses. The transferable action is not "add a moderation"; it is to make the moderator a trait-relevant cue that the theory itself defines, and to let a second theoretical act (trait activation) carry its own engine. The parallel-stakeholder layout is transferable when the theory predicts parallel effects across contexts; it is not a generic scaffold.

### Methods and Results

The methods move to carry is measure-as-co-contribution with a full validity chain; the results move to carry is front-loaded identification defense plus honest mixed-evidence staging (report the null in full with a sign-reversal read; de-emphasize the significant-but-small effect; synthesize into a boundary and hand off). Do not copy the single-sentence estimator choice or the implied-only exclusion of the 2SRI instruments.

### Discussion

The ending shows how to convert mixed evidence into a theoretical boundary and a balanced (bright-and-dark) view of a negatively-valenced trait, routing the anomaly to future research rather than post-hoc rationalizing it.

### Imperfect-paper learning note

This is a deliberate imperfect-paper case: H2 is null (coefficient positive), H4 is significant-but-small, and the contribution claims are deferred to the Discussion. The card's value is not that every paper should have a null; it is that a null and a small effect can be staged as evidence of a boundary rather than hidden, provided the front-end contract (preview) has already disclosed them.

## Comparison prompt

When a stable trait is the protagonist, does the paper give it one manifestation or two? Ridge gives paranoia two manifestations on a safety-behavior continuum and a cue that switches between them — which is what lets a null in one stakeholder arena become a boundary. Compare with positively-valenced upper-echelons traits (e.g., narcissism) that carry a single manifestation: where would the second manifestation have to come from, and what cue would switch it?
