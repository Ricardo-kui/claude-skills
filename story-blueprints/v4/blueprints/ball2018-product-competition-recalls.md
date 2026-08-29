# Story Learning Card — Ball, Anastasov, Smith, and Bercovitz (2018, *Strategic Management Journal*)

## Metadata

```yaml
schema_version: "4.0-lite"
id: ball2018
paper:
  citekey: ball_2018_product_competition_managerial_discretion_and_manu
  title: "Product competition, managerial discretion, and manufacturing recalls in the U.S. pharmaceutical industry"
  outlet: "Strategic Management Journal"
  year: 2018
  publication_status: published
  paper_type: empirical
  source_version: pdm_text_only_slices
  inclusion_rationale: "A learning object for turning a policy-induced competition shock into a two-sided quality story: one main effect plus a hetero-signed, severity-split moderation in which the moderator is built into the outcome's own categories."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "ball_2018_product_competition_managerial_discretion_and_manu.pdm/sections/introduction.md"
    - "ball_2018_product_competition_managerial_discretion_and_manu.pdm/sections/theory.md"
    - "ball_2018_product_competition_managerial_discretion_and_manu.pdm/sections/methods.md"
    - "ball_2018_product_competition_managerial_discretion_and_manu.pdm/sections/results.md"
    - "ball_2018_product_competition_managerial_discretion_and_manu.pdm/sections/discussion.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default front-weighted allocation retained. Cross-section flags C4 (intro lacks an explicit contribution paragraph; thin stakes) and C5 (discussion knot closure left unjudged by the section distills) were fed into this card and are evaluated here."
mechanism_evidence:
  status: partly_probed
  basis: "The two rival mechanisms posed at H1 (deliberate cost-cutting vs inadvertent quality-attention decay) are adjudicated indirectly: ROA/Net Income and slack show no mediation, while an OAI inspection-outcome ratio does, supporting the inattention path — but neither path is observed behaviorally."
classification:
  theoretical_problem_form: [policy-induced-competition-shock, quality-opaqueness, discretion-conditioned-consequence]
  narrative_dynamics: [paradigm-challenge-hook, dual-path-convergence, bilateral-moderation-pair, placebo-by-construction, unintended-consequence-ending]
  retrieval_signals: [anda-generic-competition, manufacturing-recalls, recall-severity-class-split, managerial-discretion-moderation, cga compliance-decay]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "partial"
    requires: []
    learn:
      - "Open by challenging a widely shared common sense (competition is good) with an economic-theory nuance (the competition-quality link is contingent on price setting), then pin the abstraction to a concrete regulation (Hatch-Waxman/ANDA) so the quality question becomes unavoidable."
      - "Preview results in one compact paragraph that states both the main effect and the sign-flipping moderation, so a hetero-signed finding is promised before the reader meets any table."
    caveat:
      - "The introduction never states an explicit contribution paragraph and the stakes for consumers are asserted rather than dramatized; copying this hook without adding a contribution turn yields a quiet, under-powered opening. The gap is Incompleteness (first empirical test in this industry), which carries less narrative force than a contested-prediction gap."
  theory:
    suitable: "yes"
    requires: [moderator_is_outcome_intrinsic, outcome_cannot_improve_by_choice_or_is_excludable]
    learn:
      - "Before hypothesizing a negative main effect, run an explicit counter-prediction exclusion: explain why firms cannot or will not compete on quality here (bioequivalence makes quality indistinguishable; cost competition makes quality costly), so the negative sign is argued rather than assumed."
      - "Build a bilateral moderation pair around a single severity split: high-severity recalls are argued to be objective (low discretion, stronger positive link), low-severity recalls subjective (high discretion, weaker/offset link), yielding H2a and H2b with opposite signs from one underlying logic rather than two theories."
    caveat:
      - "The dual-path mechanism (deliberate corner-cutting vs inadvertent quality decay) is deliberately left converged at H1 and only separated in robustness; transferring this requires a setting where an observable proxy can later adjudicate the paths, otherwise the convergence reads as unfinished theory. The severity-discretion mapping is asserted from one prior paper and two interviews, not a validated discretion measure."
  methods:
    suitable: "partial"
    requires: [regulator_publishes_outcome_severity_classes, outcome_class_content_ties_to_moderator_logic]
    learn:
      - "Operationalize a continuous-sounding moderator by splitting the dependent variable along an official regulator's own severity taxonomy (FDA Class 1&2 vs Class 3), converting a measurement problem into an institutional fact."
      - "Design a by-construction placebo alongside the main test: because ANDA products cannot be redesigned, design-related recalls should show no competition link — a null result that strengthens the story's premise."
    caveat:
      - "This requires a regulator that itself classifies outcomes by the dimension of your moderator; without such official classes the DV-split collapses into arbitrary truncation. The product-competition measure depends on non-standard data (30 years of Orange Books via FOIA) that most settings will not have."
  results:
    suitable: "yes"
    requires: [count_outcome_overdispersed, parallel_estimator_family_available]
    learn:
      - "Report FE and RE versions of the same negative binomial panel in parallel columns, then use the RE model for magnitude translation (multiplicative SD-to-percent plus recall counts), so robustness and interpretability each get their own home."
      - "Stage the moderation as a cross-column DV-split comparison (H2a column vs main-effect column vs H2b column), then back it with a four-threat battery: mediation (mechanism), PSM (selection), design-recall DV placebo (premise), and reverse causality — each addressing a distinct reader objection."
    caveat:
      - "Comparing coefficients across non-nested count models is a weaker moderation test than a formal interaction term with a statistical difference test; the paper leans on footnote-reported differences. Copying the cross-column staging requires a defensible coefficient-comparison procedure."
  discussion:
    suitable: "yes"
    requires: []
    learn:
      - "Close the knot by explaining the surprising sign against prior literature: three setting-specific boundary characteristics (quality opaqueness, buyer-user separation, regulated generic competition) are offered as the reason this industry inverts the positive competition-quality findings found elsewhere."
      - "Let the mediation result do double duty in the ending: the OAI finding becomes both a theoretical verdict (inattention, not cost-cutting) and a concrete regulatory recommendation (more inspections for ANDA-heavy firms), fusing contribution and practice."
    caveat:
      - "The three boundary explanations are post hoc interpretive claims, not tested moderators; presenting them as explanations rather than hypotheses is honest but means the ending opens a new question it does not answer."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
```

## Story Reading

### Theme question

When regulation manufactures product competition in an industry where quality is invisible and product design is frozen, does that competition erode the quality of what firms make — and does managers' room to decide what counts as a quality failure determine where the damage shows up?

### Whole-story synopsis

The paper opens against a piece of capitalist common sense: competition is good — lower prices, higher quality. Economic theory complicates this immediately: when prices are regulated, competition improves quality, but when firms set prices, the sign is contested. The Hatch-Waxman Act and its ANDA pathway make this abstraction concrete — a deliberate policy machine for increasing product competition that succeeded on price while quietly leaving manufacturing decisions (suppliers, maintenance, training) to managers under broad CGMP guidelines that dictate how work is done, not what. The unstated bargain — more competition, quality untouched — has, to the authors' knowledge, never been examined on its quality side. That unexamined bargain is the knot. The theoretical middle gives the pressure a channel and a lens. Because ANDA products must be bioequivalent, design is frozen; manufacturing is one of the few places to compete, and consumers cannot perceive quality differences anyway — so the counter-prediction (compete on quality) is explicitly excluded before H1 predicts more manufacturing-related recalls. Two paths converge on that prediction: deliberate corner-cutting or inadvertent decay of quality attentiveness. The lens is managerial discretion, argued to vary inversely with recall severity: high-severity (Class 1&2) recalls are objective facts managers cannot dodge, so competition's damage should show up more strongly there (H2a); low-severity (Class 3) problems are subjective calls managers can wave through to avoid competition-magnified recall penalties, so competition should actually associate with fewer of them (H2b). The results pay this off in an unusual sign pattern: product competition raises all manufacturing recalls, more strongly raises high-severity ones, and turns significantly negative for low-severity ones — a competitive environment that both breaks quality and teaches managers to look away from small failures. The robustness battery then adjudicates the mechanism (OAI inspection outcomes mediate; ROA, Net Income, and slack do not — inattention, not strategy), rules out selection, tests the frozen-design premise via a design-recall placebo null, and checks reverse causality. The discussion closes the knot by returning to the policy bargain: the quality erosion is real, it has a behavioral face (managers exercising discretion to not recall), and three industry characteristics — quality opaqueness, buyer-user separation, and regulated generic competition — explain why pharmaceuticals invert the positive competition-quality results found in other industries, with concrete warnings for an FDA still pushing for more generic competition.

### Characters and storylines

- **Focal character:** the pharmaceutical firm under portfolio-wide product competition (ANDA share), because it is the actor whose manufacturing attention is squeezed and whose managers face the recall decision.
- **Pressure character:** the Hatch-Waxman Act / ANDA pathway, because it is competition by design — a policy that made the pressure high, legible, and plausibly exogenous to quality choices.
- **Lens character:** managerial discretion, operationalized through the FDA's severity classes, because it splits one outcome into an objective face and a subjective face and carries both H2a and H2b.
- **Institutional characters:** FDA (inspections, recall classes, CGMP) and CGMP guidelines themselves, because they set the floor that the story claims firms quietly relax beneath — and supply the OAI proxy that later adjudicates the mechanism.
- **Stake character:** the consumer, invoked through harm-and-death stakes, thin in the introduction but made concrete in the discussion's policy turn.
- **Storyline 1 (pressure → decay):** portfolio competition → frozen design pushes rivalry into manufacturing → quality attentiveness relaxes (path ambiguous at H1) → more manufacturing recalls.
- **Storyline 2 (lens → split):** recall severity fixes discretion → objective high-severity failures surface more under competition; subjective low-severity failures get suppressed → opposite-signed relationships.
- **Intersection:** the same competitive pressure produces both an operational ramification (worse quality) and a behavioral ramification (discretion exercised to not recall) — the discussion names this duality explicitly.

### Five acts

- **Exposition:** Common sense says competition improves quality; theory says it depends on price setting; the Hatch-Waxman Act created a real, large-scale competition-inducing experiment whose quality consequences were never examined.
- **Rising action:** ANDA bioequivalence freezes design and pushes competition into manufacturing; the quality-competing alternative is excluded on two grounds; two convergent paths (cut corners / let attentiveness decay) yield H1, and the severity-discretion logic yields the H2a/H2b opposite-sign pair.
- **Climax:** The results reveal the full sign pattern — positive overall, stronger positive for Class 1&2, significantly negative for Class 3 — in parallel FE and RE negative binomial panels, with magnitude translation on the RE models.
- **Falling action:** The four-threat battery resolves the mechanism question (OAI mediates; financial outcomes and slack do not — inattention wins), plus PSM, the design-recall placebo, and reverse-causality checks.
- **Denouement:** The ending returns to the opening policy bargain and revises it: competition regulation carried an unpriced quality and behavioral cost, explained by three industry boundary conditions, with actionable implications for an FDA still doubling down on generic competition.

### Tension

- **Source:** A shared cultural belief (competition is good) and an explicit regulatory design (Hatch-Waxman) both assume quality is unaffected — while theory offers no clear answer for firm-set-price industries, and the alternative (compete on quality) is structurally unavailable.
- **Construction:** The tension is not personified; it is a bargain no one signed. The paper sharpens it by showing the bargain's fine print — CGMP's "how, not what" — and by letting the moderator reveal that the same pressure both causes failures and shapes whether failures get admitted.

### Alternative readings

- **analyst_counterfactual:** The H2a/H2b pair can be read not as managerial discretion but as a mechanical severity composition story — competition may simply produce different mixes of defect types — since severity is a property of the recall, not a separately measured managerial choice. The paper's interview evidence (two should-have-recalled-but-didn't episodes) supports the discretion reading but does not settle it.
- **analyst_counterfactual:** The negative Class 3 coefficient could also be read through recall-detection or reporting behavior under competition rather than genuine suppression of subjective recall decisions; the paper does not distinguish reporting margins from failure margins.

## Story Assessment

- **Theme coherence:** `works` — the competition-quality question organizes the hook, the exclusion argument, the severity lens, the placebo design, and the policy ending without drift.
- **Character discipline:** `works` — pressure (ANDA competition), lens (discretion/severity), and institutional floor (FDA/CGMP) have distinct, non-overlapping narrative jobs; no distracting side storylines.
- **Knot integrity:** `works` — the unexamined half of a real policy bargain is a genuine, externally verifiable challenge the study can plausibly address.
- **Plot emergence:** `works` — the DV-split moderation follows from the severity-discretion logic rather than being bolted on; the placebo test and the mediation adjudication arise from premises the theory itself set up.
- **Tie–unravel alignment:** `works` — the results answer exactly the question the front end made salient, including the sign flip the theory promised; the caveat is that moderation is staged as cross-column comparison rather than a single interaction test.
- **Ending quality:** `works` — the discussion transforms the opening (the bargain had a hidden behavioral cost; three boundary characteristics explain the inverted sign; policy is still pushing the same lever). This resolves cross-section flag C5: the knot closure is strong even though the discussion was not separately distilled.
- **Boundary:** This evaluates storytelling only — not the validity of the discretion conceptualization, the comparability of coefficients across count models, or the paper's causal or journal standing.

## Learning Affordances

### Introduction and Theory

Use this card when a policy or institutional change manufactures variation in a familiar variable (competition, pressure, resources) and the outcome's downstream consequences were publicly assumed away; and when you can argue one moderator as two opposite-signed predictions from a single underlying logic. The hook is a paradigm-challenge move (common sense + theoretical ambiguity + concrete regulation). It is not a template for any negative-main-effect paper: the exclusion argument (quality cannot be the competing dimension here) is load-bearing, and the severity lens requires an outcome whose categories genuinely encode the moderator. The introduction itself is a cautionary partial — its missing contribution paragraph and thin stakes are why the card is a partial, not full, exemplar at the front end (flag C4 confirmed).

### Results and Discussion

The transferable staging is the pairing of parallel FE/RE replication with DV-split cross-column moderation, a magnitude translation on the inclusive model, and a four-threat battery where the mediation test also resolves the theory's own dual-path ambiguity. Its mechanism evidence is `partly_probed` — the OAI result discriminates inattention from cost-cutting, but neither path is observed directly, so writers may claim mechanism *support*, not mechanism *proof*. The discussion's lesson is to close a policy knot by (a) explaining the surprising sign with named boundary conditions and (b) converting the mediation verdict into the specific regulatory recommendation it implies.

## Comparison prompt

Compared with `bala2017` (anticipated rival recall as a modeled category-defense problem) and `thirumalai2011` (medical-device recalls without a severity-discretion lens), does your paper treat outcome severity as an intrinsic moderator that can split the dependent variable (`ball2018`), or does severity remain a context you only discuss? If your moderator is not built into your outcome's official categories, the DV-split staging here does not transfer.
