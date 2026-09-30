# Story Learning Card — Mukherjee, Ball, Wowak, Natarajan, and Miller (2022, M&SOM)

## Metadata

```yaml
schema_version: "4.0-lite"
id: mukherjee2022-recall-cluster-herding
paper:
  citekey: mukherjee_2022_hiding_in_the_herd_the_product_recall_cluster
  title: "Hiding in the Herd: The Product Recall Clustering Phenomenon"
  outlet: "Manufacturing & Service Operations Management"
  volume: "24(1), 392-410"
  year: 2022
  publication_status: published
  paper_type: quantitative (analytical formal model + archival empirical companion)
  source_version: pdm_slices_verified # five materialized slices + four verified section distillations (2026-09-29)
  inclusion_rationale: "A learning object for the phenomenon-first, analytical-model-driven paradigm: an existence question and a consequence question are fused into one motive-consequence loop, and a stopping-time game plus a Hawkes process carry the plot where a verbal mediation theory would sit."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "pdm/sections/{introduction,theory,methods,results,discussion}.md (slices)"
    - "pdm/sections/{introduction,theory,methods,results}.json (verified distillations)"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Default front-weighted allocation retained. The formal-model adaptation: the theory audit judges the analytical model as the story's plot engine (penalty assumptions, lemmas, equilibrium) rather than as verbal mediation, and the assessment evaluates the paradigm's transferability on its own terms instead of IMRaD defaults."
mechanism_evidence:
  status: partly_probed
  basis: "Uniqueness and blame are proxied entirely by recall timing; the herding motive (deliberate delay to hide) is inferred from excitation plus discretion and component-unrelatedness checks rather than observed; the attribution judgment itself is never measured."
classification:
  theoretical_problem_form: [underexamined-phenomenon, equilibrium-based-strategic-timing]
  narrative_dynamics: [failed-assumption-as-opening, model-as-plot-engine, motive-consequence-crossing, two-act-evidence, policy-as-transparency-fix]
  retrieval_signals: [recall-clustering, herding, attribution-theory, hawkes-process, event-study, recall-timing]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Open a phenomenon through a failed field assumption: state what the literature presumes (recalls are independent across firms), juxtapose an anecdote that violates it, and promote the violation to a named, explicitly uninvestigated phenomenon so that 'does it exist at all?' is legitimate as a first research question."
      - "Chain the second research question to the first as motive-consequence: preview the position-penalty differential as the reason clustering would be rational, so two empirical studies read as one story rather than a pairing."
    caveat:
      - "The introduction pre-commits the attribution reading of its 2015 market-reaction anecdote before the theory section derives it — a paper-internal order tension; a writer borrowing the opening needs the discipline to let the mechanism arrive later, and the 'no prior research' gap claim must actually hold."
  theory:
    suitable: "yes"
    requires: [mechanism expressible as payoff-structure primitives; a solvable dynamic game or equivalent formal apparatus]
    learn:
      - "Let the analytical model carry the theory: convert a verbal mechanism (uniqueness breeds blame) into sign and monotonicity assumptions on penalty functions, derive rankings as lemmas, then embed them in a stopping game whose equilibrium makes the focal behavior endogenous — clustering emerges as an optimal strategy, not an observed accident."
      - "Map each hypothesis to a formal parent explicitly (Lemma 1a to H2a, 1b to H2b, 2 to H2c) so every hypothesis has both a behavioral parent (herding, attribution) and a formal one (equilibrium, lemma)."
    caveat:
      - "Transferable only where the mechanism can be written as payoff primitives; the penalty functions are stylized and unobserved, and papers whose theory is verbal mediation cannot borrow this architecture without acquiring the formal machinery that makes it work."
  methods:
    suitable: "partial"
    requires: [event-time data with plausible self-excitation; latent role or type structure that downstream analyses consume]
    learn:
      - "Match the estimator to the claimed phenomenon rather than to convention: because the claim is self-excitation, choose a self-exciting point process; because leader and follower roles are latent, choose an EM formulation whose by-product is the role assignment the second act needs."
      - "Design consecutive analyses so the first feeds the second: Hawkes role assignments become the event study's treatment categories, making two studies one design."
    caveat:
      - "The role assignment is model-produced, not observed, so downstream penalty estimates inherit the classification's assumptions; the paradigm has almost no off-the-shelf translatability into standard management toolkits."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Answer an existence question with a parameter, then immediately translate the parameter into narrative units: the excitation coefficient is followed by 73% of recalls clustered, 266 clusters, 16-day gaps, and 34-day persistence, turning an abstract theta into counts a reader can picture."
      - "Stage the motive-consequence crossing in the results order: the penalty differential is explicitly interpreted as the incentive behind clustering, so the second act's payoff retroactively completes the first act's motivation."
    caveat:
      - "Headline figures are best-window values ('as high as 67%') and the Leading-recall coefficient is insignificant in several event windows without the text naming the pattern — a paper-internal reporting tension; writers borrowing the headline-number move must state window dependence."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Convert the mechanism into one policy lever: because hiding in the herd depends on what the regulator cannot see, the ending narrows to a single cost-neutral transparency fix (mandatory defect-awareness dates), cross-validated against another regulator's existing practice."
      - "Use an in-sample anomaly as the ending's second beat: Toyota's 31% leading share is reinterpreted as reputation-driven herd formation, turning a robustness-table detail into theoretical meaning."
    caveat:
      - "The policy claim rests on the deliberate-hiding interpretation, which the design cannot distinguish from information-driven following; and the practical assertion is stated more firmly than the flagged industry boundary (concentration, product similarity) supports."
story_assessment:
  overall_role: partial_exemplar # storytelling judgment only: a phenomenon-first opening and an equilibrium-driven middle fuse two research questions into one motive-consequence loop, paid off by a two-act design and previewed numbers that all land; held at partial because the attribution mechanism is timing-proxied and pre-committed in the introduction, and window sensitivity in the penalty tables goes unnamed — the formal-model paradigm itself is judged as the transferable center, not against IMRaD defaults
  mode: single_read
```

## Story Reading

### Theme question

Do firms deliberately cluster product recalls in time — hiding following recalls behind a competitor's leading recall — and does the stock market price a recall by its position within a cluster, so that the pricing itself is the incentive to cluster?

### Whole-story synopsis

The paper opens on a safety puzzle with a body count: recalls arrive after inexplicable delays, and Toyota's unintended-acceleration and GM's ignition-switch catastrophes show what waiting costs. The field's explanation machinery presumes recalls are independent across firms; the popular press's "recall tidal waves" — Ford's fuel-tank recall followed within days by Honda's and Chrysler's unrelated recalls — says the presumption fails. The authors name the violation a phenomenon: recall clusters, in which a leading recall excites competitors' following recalls, and managers may delay in order to hide in the herd. Two questions split the knot into existence (do firms cluster recalls?) and consequence (does the market penalty depend on cluster position?), with the wager that the consequence is the motive. The middle is carried by an analytical model rather than verbal mediation: market costs that rise stochastically with waiting, stock prices shocked by attribution-style penalties, two lemmas that rank the penalties (leader over follower; both worsen as elapsed time grows), and a stopping game whose equilibrium makes immediate following optimal and threshold rules govern who recalls when. Clustering is thereby derived, not asserted; Hypotheses 1 and 2a–2c are the model's testable shadows fused with herding and attribution theory. The evidence then runs as two acts keyed to the two questions. A Hawkes self-exciting point process with EM assignment of leading and following roles shows that 73% of 3,117 recalls across 48 years sit in 266 clusters, with significant excitation that decays exponentially. An event study with GARCH errors, cluster-adjusted Patell tests, and GEE covariate models shows the leading penalty runs as much as 67% larger, that followers are punished more as they lag the leader, and that leaders are punished more as the gap since the last cluster grows. Robustness walls close the obvious alternative readings on both fronts: a placebo firm, a discretion proxy in units recalled, a logistic hazard alternative, and component unrelatedness for clustering; pre-event-window handling, size-matched subsamples, follower-count correction, and component similarity for the penalty. The ending folds the two acts back into one loop: the penalty differential is the incentive, so delay is individually rational — and the fix is to make delay observable, by requiring NHTSA to collect FDA-style defect-awareness dates. Toyota's outsized 31% leading share returns as the ending's second beat: competitors move when the quality stalwart moves, so reputation, not only strategic hiding, can call the herd. Limitations concede unobservables, an estimation-window tradeoff, and an industry boundary of concentration and product similarity.

### Characters and storylines

- **Role characters:** the leading recall and the following recall — positions rather than actors, and the plot is literally an assignment of these roles, performed by the EM algorithm at model convergence.
- **The strategic firm:** a manager who, each period, chooses between recalling alone (a large, uniqueness-priced penalty) and waiting (a rising continuous market cost); the player whose equilibrium behavior the model derives.
- **The attributing market:** the judge character; its uniqueness-to-blame rule sets the payoff structure every other character responds to, and it never appears as an observed actor.
- **Toyota as reputation node:** boundary character, standing out with 31% of its recalls leading clusters and reinterpreted at the ending as the bellwether the herd follows.
- **The regulator (NHTSA):** counter-character whose inability to observe defect-awareness dates is the enabling condition of hiding; the policy endpoint targets precisely this blindness.
- **Storyline 1 (existence):** failed independence assumption → herding motive → equilibrium clustering → Hawkes excitation evidence → 73% clustered.
- **Storyline 2 (valuation):** uniqueness → blame → position-priced penalties → event-study differentials within and between clusters.
- **The crossing:** the two storylines meet in the penalty differential — consequence of position (storyline 2) and cause of clustering (storyline 1) — which is the paper's narrative engine.

### Five acts

- **Exposition:** Record-breaking recalls, deadly announcement delays, and a literature that presumes recalls to be independent across firms.
- **Rising action:** Anecdote violates the assumption; the violation is named a phenomenon; an analytical model derives clustering as an equilibrium of the penalty structure and issues hypotheses as the lemmas' empirical shadows.
- **Climax:** The Hawkes excitation parameter reveals the herd (theta-hat 0.24, 73% clustered, 266 clusters); the event study prices position (leading penalty up to 67% larger, decaying within clusters and amplifying between them).
- **Falling action:** Four-plus-four robustness walls close alternative readings one by one; firm-level texture (Toyota's 31% leading share) surfaces as an anomaly awaiting interpretation.
- **Denouement:** The motive-consequence loop closes — the differential is the incentive — and the opening's delay problem returns transformed as a single regulatory design change: make the awareness date observable so hiding loses its cover.

### Tension

- **Source:** The market punishes the firm that recalls alone more than the firm that recalls in company, so the individually rational timing rule is to wait for someone else to move first — while defective products stay on the road. Safety disclosure and self-protection point in opposite directions, and the delay is not negligence but equilibrium behavior.
- **Construction:** The tension is built by derivation rather than assertion: attribution-style assumptions yield the penalty rankings, the game converts the rankings into a clustering incentive, and the data must then confirm both that herds form and that positions are priced differently for the tension to hold.

### Alternative readings

- **author-signaled-alternative:** The limitations concede that reusing the leader's pre-event window for followers introduces its own bias, and that industry concentration and product similarity make autos a friendly case for detecting herding; the discussion additionally offers NHTSA scrutiny dilution during dense clusters as an untested extra motive for clustering.
- **analyst_counterfactual:** Observed clustering could reflect common temporal shocks to all firms' recall propensity — shared component-aging regimes, regulatory waves, industry-wide quality events — rather than strategic herding. The placebo firm rules out pure randomness and the component analysis rules out within-cluster relatedness, but neither rules out a correlated common shock; the deliberate-hiding motive itself is never observed.

## Story Assessment

- **Theme coherence:** `works` — the cluster-and-position question organizes both halves; every section, including the executive interviews on the wait-and-see file, advances it.
- **Character discipline:** `works` — leader and follower roles, the attributing market, the strategic firm, Toyota, and the regulator stay distinguishable; the eight robustness checks remain servants of the two storylines rather than a distracting third act.
- **Knot integrity:** `works` — the independence assumption is genuinely load-bearing in prior recall research, and the challenge to it is addressable with 48 years of timing data.
- **Plot emergence:** `works` — the formal model makes clustering a derived equilibrium of the penalty structure rather than a forced plot, and the Hawkes design follows from the existence claim instead of convention.
- **Tie–unravel alignment:** `partly_works` — the existence question is answered directly and the introduction's previewed numbers (73%, 266 clusters, 67%) all land in the results; but the consequence question's attribution reading is proxied by timing, is pre-committed in the introduction before the theory derives it, and rests on event windows where the key coefficient is not always significant, a sensitivity the text does not name.
- **Ending quality:** `works` — the ending returns to the opening's delay problem and transforms it into a specific, cost-neutral regulatory design change rather than repeating findings; the Toyota reinterpretation gives the close a theoretical second beat.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification, the correctness of the equilibrium model, or research quality.

**Mechanism evidence check:** `partly_probed` — uniqueness and blame are proxied entirely by recall timing; the herding motive is inferred from excitation plus discretion and component-unrelatedness checks; the attribution judgment and the decision to wait are never observed.

## Learning Affordances

### Introduction

The structural action is to open with a failed field assumption rather than a gap in attention: state what prior work presumes, show an anecdote the presumption cannot survive, and promote the violation to a named phenomenon so existence becomes a legitimate first question. It transfers only when the assumption is genuinely load-bearing in the target literature and the phenomenon is verifiably unstudied; the paper's own order tension — the attribution interpretation of the 2015 anecdote arriving before its derivation — marks the discipline the borrower must restore. Do not copy the recall setting, the press-anecdote device, or the "to our knowledge" claim without checking it.

### Theory

The theory shows how a model can be the plot engine: a verbal mechanism becomes payoff primitives, primitives become lemmas, lemmas become a game, and the game's equilibrium makes the focal behavior something the paper derived rather than presumed. This is the card's central transferable move, but its invocation conditions are real: the writer's mechanism must be expressible as payoff-structure primitives and a solvable dynamic apparatus must exist; hypotheses then inherit two parents (behavioral and formal) through explicit lemma-to-hypothesis mapping. Do not imitate the appearance of formality — stylized assumptions without a derivation give a plot that looks engineered because it is.

### Methods

The design demonstrates estimator-to-claim matching: self-excitation claims get a self-exciting point process, latent roles get an EM formulation, and the role assignment by-product becomes the second analysis's treatment variable so two studies are one design. Transfer requires event-time data with plausible self-excitation and a latent role structure downstream analyses genuinely consume; the paradigm has almost no off-the-shelf path in standard management toolkits, and model-produced role assignments propagate their assumptions into every downstream estimate.

### Results

The results architecture answers existence with a parameter and immediately translates it into narrative units, then stages the crossing: the valuation act's differential is read back as the existence act's motive. The sequence is borrowable whenever a design has one act per research question and the questions are motive-consequence linked. The calibration lesson is the paper's own tension: headline figures quoted at best window ("as high as 67%") alongside unnamed insignificant windows will carry the story only until a reader opens the table — window dependence must be stated, not suppressed.

### Discussion

The ending shows how to convert a mechanism into one policy lever: identify what the enabling institution cannot see (the awareness date), borrow the fix from a neighboring regulator that already collects it, and narrow to that single cost-neutral change. Its second beat — an in-sample anomaly reinterpreted as theory (Toyota's leading share as reputation calling the herd) — turns robustness texture into meaning. Do not extend the move into claims the design cannot carry: the deliberate-hiding reading of clustering is an interpretation, and the industry boundary the limitations flag bounds the practical assertion more tightly than the ending states.

## Comparison prompt

Mao, Dong, and Lee (2022, M&SOM) explains the same recall-delay behavior with a different clock: delay produced before the decision, through endogenous investigation effort, versus delay produced at the decision, through strategic waiting for a leading recall. When two formal models attribute one observed timing pattern to different stages of the same decision chain, what evidence architecture lets a writer claim one clock rather than the other — and can both equilibria coexist in one data-generating process, with investigation resolving some delays and herding masking others?
