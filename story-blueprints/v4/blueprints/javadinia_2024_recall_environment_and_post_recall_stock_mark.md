# Story Learning Card — Javadinia, Gill, and Jayachandran (2024, Journal of the Academy of Marketing Science)

## Metadata

```yaml
schema_version: "4.0-lite"
id: javadinia2024
paper:
  citekey: javadinia_2024_recall_environment_and_post_recall_stock_mark  # pdm paper_id; Zotero citekey unverified
  title: "Recall environment and post-recall stock market response"
  outlet: "Journal of the Academy of Marketing Science"
  year: 2024
  publication_status: published
  paper_type: "quantitative (single archival event study with construct-development interviews and survey)"
  source_version: pdm_slices_verified  # five verified section slices + L2 section distillations (introduction/theory/methods/results) + L2 cross-consistency ok, 0 flags
  inclusion_rationale: "A construct-building learning object: the paper invents its main character (recall environment intensity) from an observation prior studies left unconceptualized, validates it inside the theory section with interviews and a survey, then runs a clean three-hypothesis event-study arc. It also carries visible seams — a five-dimension concept measured with four PCA inputs plus recency as weight, a binarized treatment, and a Table 2 definition that contradicts the text — which make it useful as a partial exemplar rather than a flawless model."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete  # all five materialized PDM slices read in attention order (introduction + theory first, then results + discussion, methods as alignment audit)
  source_records:
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/introduction.md"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/theory.md"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/methods.md"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/results.md"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/discussion.md"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm.yaml (PDM root; cross_section_identity coherence=ok, flags=[])"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/introduction.json (verified L2)"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/theory.json (verified L2)"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/methods.json (verified L2)"
    - "C:/Users/admin/.claude/distill-work/javadinia_2024_recall_environment_and_post_recall_stock_mark.pdm/sections/results.json (verified L2)"
    - "C:/Users/admin/.claude/skills/story-blueprints/v4/rhetoric-moves/sources/javadinia_2024_recall_environment_and_post_recall_stock_mark.sentences.md (sentence inventory)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default allocation kept, with one architecture note: this paper splits its construct work across two sections — dimension validation (interviews, MTurk survey) lives inside the theory section while measure construction and treatment binarization live in methods. The story reading therefore treats theory as primary but audits the concept-to-measure hand-off across the theory/methods boundary, where the paper's main seams sit."
mechanism_evidence:
  status: partly_probed
  basis: "The expectation-adjustment mechanism (surprise attenuation) is never measured directly. Its salience premise is probed twice in the results' preliminary analyses — Google 'recall' search volume tracks monthly ENV, and the ENV effect appears only for recalls without incidents (attention-competition split) — but no investor-side mediator (expectancy revision) enters any model."
classification:
  theoretical_problem_form: [unconceptualized-context-construct, uncertain-event-valuation]
  narrative_dynamics: [frequency-hook-to-existence-claim, construct-built-on-page, census-by-absence, proximate-vs-distal-information-duel, single-engine-dual-moderators, effect-reversal-grid-ending]
  retrieval_signals: [recall-environment, salience-theory, investor-attention, expectation-adjustment, event-study-car, coarsened-exact-matching, product-age, reliability-reputation]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Use an epigraph as a theme-loading device: an artist's quote ('For me context is the key' — Kenneth Noland) states the paper's core idea (context determines judgment) before any citation appears, so the hook's frequency stack can land on an idea the reader has already been given."
      - "Convert a frequency-stacked trend hook into an existence claim in one sentence: the paragraph piles NHTSA/FDA counts and a 131% increase, then ends by asserting that every new recall 'occurs in a recall environment constituted by recalls of other firms' — the last sentence turns background data into the paper's main character."
    caveat:
      - "The hook carries the stakes alone; there is no separate stakes paragraph and no consequence chain (deaths, dollar losses) — the energy is moderate and depends on the reader already caring about recall penalties."
      - "The gap is positioned against only two papers (Borah & Tellis 2016; Mukherjee et al. 2022), the contribution block is a five-item flat enumeration (a-e) without prioritization, and the gap census itself is delegated to Table 1, which physically lives in the theory section."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Build the construct on the page: define recall environment intensity through salience features, then validate each proposed dimension with quoted investor-interview speech (media repetition, unit counts, hazard, recency) plus an MTurk survey before deriving any hypothesis — the reader watches the main character acquire traits from practitioners, not just from citations."
      - "Run two moderators off one engine: both boundary conditions derive from a single proximate-vs-distal information rule (Higgins 1996) — when directly relevant product information (age, reputation) already justifies or explains the recall, distal industry-level salience matters less — so H2 and H3 are two applications of one mechanism rather than two added interactions."
    caveat:
      - "The concept-measurement hand-off leaks: the construct is announced with five dimensions (publicity, hazard, size, scope, recency), but the measure PCA-combines four inputs with recency demoted to a weighting factor — the text's 'five aspects' never reconciles with the four-index equation block."
      - "Dimension validation rests on respondent agreement (face validity from 20 interviews and a small MTurk survey); no discriminant or criterion validation of the five-dimension structure is attempted before the hypotheses are built on it, and the Rivian example is asserted as 'presumably' high-intensity rather than shown."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Make the sampling funnel part of the identification story: 526 → 497 → 148 recalls, with each deletion (no announcement date, unlisted firms, confounding events, nearby recalls) given its own bias rationale, so the reader experiences sample construction as design rather than attrition."
      - "Turn a sign conflict into a design feature: spillover from nearby recalls is negative while the hypothesized environment effect is positive, so excluding recalls in a [-2,2] window of other firms' announcements is argued to make detection harder — a conservative test — not merely to shrink the sample."
    caveat:
      - "Treatment construction is under-defended where it matters: ENV is binarized at zero (composite score sign = high/low) with footnote-level justification, though the PCA score is continuous; and the CEM step's unmatchable observations are not accounted (148 recalls enter matching, 138 remain, with no report of dropped unmatchables)."
      - "Table 2's REPUT definition ('averaged over five years prior to the recall year') contradicts the methods text ('average over the three years prior') — an operationalization-table contradiction a hypothesis-critical reader will hit twice."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Stage the dependent-variable choice as a tournament: four event windows are tested and only CAR [0,0] is significant, so the DV selection is presented as an empirical fact with prior-literature backup rather than an assumption — the reader sees the market penalty exist before any hypothesis is tested."
      - "Use preliminary analyses to probe the theory's premises before the main models: Google search trends validate that ENV captures attention, an incident/no-incident split shows the effect vanishes when the focal recall itself draws attention (the salience premise under stress), and a model-free high-vs-low comparison (+0.0061) gives the H1 sign before any regression."
    caveat:
      - "Effect sizes are tiny (main effect ≈ 0.007 of the announcement-day abnormal return) and are never translated into economic significance — no dollar or percentage-of-penalty framing appears in the results."
      - "The robustness summary outruns its own table: the text concludes the moderator hypotheses 'get strong support' across R1-R15, but several displayed models (R10-R14) show insignificant ENV×REPUT estimates; the summary averages over the battery instead of reporting where the moderation wobbles."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Convert the interaction into a signed lookup grid: Eq. 9's marginal effect becomes Table 8, an age × reputation matrix of Positive/Not Sig/Negative cells anchored with named brand-year examples (Lexus 2019 positive for young vehicles; Jaguar 2011 negative beyond age 16) — managers get a decision table, not a coefficient recitation."
      - "Generalize by analogy rather than by assertion: the closing contribution moves outward through parallel clustering phenomena (IPO hot/cold markets, new-product announcement clusters) to claim the transferable point — when firm events cluster, investors price the information content of prior events, not just the focal one."
    caveat:
      - "The ending restates the introduction's contribution list in the same order rather than transforming the opening question; the incident-split complication (context stops mattering when the focal recall is itself attention-grabbing) is never revisited, and limitations are brief and generic (single industry, industry-level environment)."
      - "The practical grid's marginal-effect derivation inherits the binarized ENV, so Table 8's 'low to high' transition is a 0/1 contrast presented as if continuous — the table's polish hides the operationalization's coarseness."
story_assessment:
  overall_role: partial_exemplar  # storytelling judgment only: a clean, promise-kept three-hypothesis arc with genuinely instructive construct-building and a transformed practical ending, held back by concept-measurement seams in the middle (five-dimension vs four-input ENV, binarized treatment, REPUT table contradiction) and an ending that restates more than it transforms
  mode: first_write_reviewed
```

## Story Reading

### Theme question

When product recalls are frequent and each announcement's market penalty is uncertain at the moment it lands, does the salience of the industry's prior recalls — the recall environment's intensity — make investors discount a new announcement's surprise, attenuating its stock-market penalty, and under what product-level conditions (vehicle age, reliability reputation) does that attenuation strengthen or dissolve?

### Whole-story synopsis

The paper opens with an artist's epigraph — "For me context is the key" — that names the theme before any evidence appears, then stacks three regulators' frequency counts (tens of millions of vehicles, 300 FDA products, a 131% rise since 1999) into a single claim: a new recall announcement never arrives alone; it arrives into a recall environment made of other firms' recalls. The knot is set in the next breath: recalls reliably extract a stock-price penalty, yet the size of any specific penalty is uncertain when announced — so decision-makers must evaluate it against context. The introduction's research question and its five-part contribution list follow, with the gap located by absence in a census table and sharpened against two neighbours (Borah and Tellis studied rival effects, not the environment; Mukherjee et al. studied the recall's position in a cluster, not the information content of what precedes it).

The theory section builds the main character in public. Salience theory supplies the engine — investors with limited attention and uncertain cash-flow impacts reach for the most noticeable contextual information — and recall environment intensity is defined as the noticeability of prior industry recalls along five dimensions: publicity, hazard, size, scope, and recency. Unusually for a theory section, the construct is then validated before use: twenty investor interviews, quoted at length, confirm each dimension ("if a recall is shown on media repeatedly, she will pay attention to it even if it does not involve any serious issue"), and an MTurk survey corroborates both the dimensions and the premise that investors consult the environment. On that foundation H1 derives the expectation-adjustment effect — a salient environment makes the new recall less surprising, so the penalty shrinks — and both moderators derive from one proximate-information rule: when product age or reliability reputation already explains the recall, the distal industry context loses leverage; when they do not (new product, strong reliability reputation), the environment does more work, giving H2 (age weakens the mitigation) and H3 (reputation strengthens it).

The methods section converts the character into a number — recency-weighted daily sums of other firms' recall size, scope, publicity, and hazard between the focal firm's own consecutive recalls, PCA-reduced to one index and binarized at zero — while the sampling funnel (526 to 497 to 148 recalls) and the spillover-aware clean window are argued as identification, and CEM matching on five timing-related covariates assembles 138 comparable high- and low-intensity announcements. The results pay the promise almost verbatim: the event-window tournament shows the penalty exists only on the announcement day; three preliminary analyses probe the theory's premises (Google "recall" search volume tracks ENV; the effect lives only in recalls without incidents; the model-free high-low gap is positive); and the main models return H1 (+0.0074, p<.01), H2 (−0.0040, p<.05), and H3 (+0.0041, p<.05) in the promised directions, defended by a fifteen-model robustness battery. The discussion converts the interactions into a signed age × reputation lookup grid with named brands, claims a transferable principle through the IPO-clustering analogy — and then mostly restates the opening's contribution list, leaving the incident boundary and the concept-measure seams unaddressed.

### Characters and storylines

- **Main character:** recall environment intensity — created, not imported; the introduction's hook asserts its existence, the theory section gives it five traits and practitioner-quoted validation, methods gives it a formula, and results give it a sign. The paper's whole arc is this character's biography.
- **Theoretical protagonist:** the investor under uncertainty — limited attention, uncertain cash-flow impacts, reaching for whatever is most noticeable; heard from directly in the interviews, then present only as an assumption in the event-study models.
- **Foil characters:** product age and reliability reputation, the proximate-information pair whose presence crowds out the environment's influence; they do not attack the main character, they make it unnecessary.
- **Institutional supporting cast:** NHTSA and CRSP databases, Consumer Reports trouble indexes, and Google Trends — data infrastructures that make an abstract "environment" observable and checkable.
- **Shadow comparison:** Mukherjee et al. (2022)'s cluster position — never an antagonist, but the adjacent account the paper must differentiate itself from, and does so twice (introduction and robustness model R3).
- **Storyline 1 (existence):** the recall environment is real, salient, and measurable — established by frequencies, interviews, survey, and Google Trends before any hypothesis is tested.
- **Storyline 2 (attenuation):** because salient prior recalls lower surprise, a new announcement in a high-intensity environment is penalized less — H1 — and the attenuation's strength is traded off against the proximate information each product carries (H2, H3).
- **Intersection:** the two storylines meet in the claim that the same objective recall can be priced differently depending on the information content of what preceded it — the False Similarity puzzle the introduction sets up.

### Five acts

- **Exposition:** epigraph plus stacked regulator frequencies (tens of millions of vehicles, 131% increase, 914 recalls in 2018) compressed into an existence claim for the recall environment; the uncertain-penalty knot; the research question; a five-part contribution enumeration and two-paper positioning against Borah-Tellis and Mukherjee.
- **Rising action:** salience theory imported as the engine (attention scarcity + event uncertainty → context reliance); the construct defined in five dimensions and validated on the page through investor interviews and an MTurk survey; H1 derived from expectation adjustment, H2 and H3 derived from a single proximate-vs-distal information rule; Fig. 1 locks the three-path model.
- **Climax:** after the funnel narrows 526→148→138 and CEM assembles matched high/low environments, the results deliver the premise probes (Google Trends co-movement; incident split; model-free comparison) and then the three verdicts in the promised directions — +0.0074, −0.0040, +0.0041 — with the main effect surviving a fifteen-model robustness battery.
- **Falling action:** the robustness narrative asserts moderator strength beyond what several table cells show; the incident-split's theoretical meaning (context influence is conditional on the focal event not hogging attention) is reported but not elevated.
- **Denouement:** the discussion restates the contributions, adds the IPO/new-product-announcement clustering analogy as a generalization claim, and transforms the interactions into Table 8 — a manager-facing signed grid over age × reputation with named brand-years — before closing with brief, generic limitations.

### Tension

- **Source:** the uncertainty of valuation at the announcement moment. The penalty is a near-certainty in the aggregate but unknown in the particular, and investors have limited attention — so the same recall can be priced differently, and the paper's puzzle is why.
- **Construction:** the tension is built from similarity without sameness — identical-looking announcements, divergent penalties (the Davis False Similarity register) — and then made tractable by giving the invisible context a name, five dimensions, and a measure. The absence of a personified antagonist is deliberate: the opponent is the field's own habit of treating recall announcements as if they arrived alone, embodied in the census table's column of "No"s.

### Alternative readings

- **analyst_counterfactual:** The incident-split result could be promoted from a robustness-flavored preliminary analysis to the paper's most interesting claim — the environment effect is an attention-budget phenomenon that disappears whenever the focal event itself is attention-grabbing — recasting the story from "context attenuates penalties" to "context attenuates penalties only when nothing closer grabs the eye." The authors report it as premise support and never return to it in the discussion; this counterfactual is the analyst's.
- **analyst_counterfactual:** One could read the paper as a measurement contribution wearing an event-study coat — the durable artifact is the ENV index (recency-weighted, PCA-combined, portable to any clustered-event setting), while the three hypotheses are its demonstration. The authors order the contributions concept-first; the measure-first reading is the analyst's.
- **documented_in_literature (authors' own framing):** the paper invites reading as a complement to Mukherjee et al. (2022) — position-in-cluster and information-content-of-preceding-recalls as two orthogonal summaries of the same environment — a reading the authors themselves state and defend with robustness model R3.

## Story Assessment

- **Theme coherence:** `works` — every section organizes around making the recall environment observable and pricing it; the epigraph, the census, the interviews, the index, and the grid all point at the same question.
- **Character discipline:** `partly_works` — the main character leads a double life the text never reconciles: conceptualized in five dimensions, measured with four PCA inputs plus recency-as-weight, and binarized into a dummy; reliability reputation also carries three jobs at once (matching covariate, control, moderator) while Table 2 mis-describes its construction window (five years vs the text's three). The investor-protagonist disappears after the interviews.
- **Knot integrity:** `works` — uncertain penalties under limited attention, and an unconceptualized context that prior findings already implied mattered, form a genuine, addressable challenge.
- **Plot emergence:** `works` — the hypotheses follow from the salience engine and the single proximate-information rule rather than from added-predictor logic; the moderators are derived, not harvested.
- **Tie–unravel alignment:** `works` — all three promised verdicts arrive in the promised directions, the cluster-position rival is controlled (R3), and the premise probes precede the verdicts; the caveat is calibration, not direction (tiny magnitudes, several insignificant moderation cells summarized as strong).
- **Ending quality:** `partly_works` — Table 8 is a real transformation of the interaction coefficients into a decision artifact, and the clustering analogy genuinely generalizes the construct; but the contribution paragraphs restate the introduction nearly in order, the incident boundary is dropped, and limitations are generic hedges.
- **Boundary:** This evaluates storytelling only; it is not a judgment about the paper's causal identification, the validity of the ENV index, or the study's research quality.

## Learning Affordances

### Introduction and Theory

The transferable core: when your main character is a context construct the literature has used but never named, (1) assert its existence in one sentence at the end of a frequency-stacked hook, (2) build it on the page — define features, then validate each with practitioner speech and a survey before deriving hypotheses — and (3) derive every moderator from one information-selection rule so the boundary conditions read as a system rather than a list. The epigraph-as-theme-loader is portable to any paper whose core idea can be stated in one borrowed sentence. Not copyable: the recall setting's abundant regulator data and the convenient existence of Consumer Reports trouble indexes. Do not copy the concept-measure drift (five dimensions announced, four measured, recency silently demoted to a weight) or respondent-agreement-only dimension validation into a construct paper — these are the seams a hypothesis-critical reviewer will find.

### Methods and Results

Use this card when the treatment is an environment the firm only partially controls: the funnel-as-identification narration (each sample deletion given a bias rationale), the sign-conflict-into-conservative-test argument for excluding nearby events, the event-window tournament for DV selection, and the three-probe preliminary battery (premise → premise → model-free sign) that stages the mechanism's assumptions before the main verdicts. Also transferable: CEM with weights when treatment is a threshold crossing. Cautionary: the binarized treatment with a one-line defense, the unreported unmatchable-observation count, the table-vs-text operationalization contradiction, and a robustness summary that claims strong moderator support beyond what several cells show are recorded weakness, not rhythm to imitate; and tiny coefficients with no economic-significance translation leave the reader convinced of direction but not of size.

### Discussion

The discussion's one genuinely instructive move: cash the interactions into a signed lookup grid anchored with named brand-year examples, so managers receive a decision table rather than a coefficient recitation — and derive that grid explicitly (Eq. 9) so the table is auditable. Copyable too: generalizing by analogy to adjacent clustering phenomena (IPO cycles, announcement clusters) to claim the construct travels beyond recalls. Not copyable: restating the introduction's contribution enumeration as the spine of the discussion — transform the opening question instead — and dropping the paper's own most theoretically suggestive complication (the incident split) from the ending.

## Comparison prompt

Compared with Pupovac et al. (2025) on recall contagion in this corpus, ask whether "environment as attenuator" and "contagion as amplifier" are the same environment construct with opposite signs — and what feature of the environment (aggregate salience versus firm-proximity of the source recall) selects the sign. Read against Eilert et al. (2017) and Gao et al. (2015), ask whether product age and reputation play the same dual role there (proximate information crowding out context here, cost/severity signals there) or whether this paper has quietly re-derived their moderators under a new engine.
