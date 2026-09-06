# Story Learning Card — Gulati & Gargiulo (1999, American Journal of Sociology)

## Metadata

```yaml
schema_version: "4.0-lite"
id: gulati-ajs1999-where-networks-come-from
paper:
  citekey: gulati_1999_where_do_interorganizational_networks
  title: "Where Do Interorganizational Networks Come From?"
  outlet: "American Journal of Sociology"
  year: 1999
  publication_status: published # AJS 104(5): 1439-1493, doi:10.1086/210179 (vault frontmatter)
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "The genesis twin of Gulati's same-year SMJ alliance paper: the same data program inverted — instead of asking what network location does for firms, it asks where the network itself comes from, splitting tie formation into an exogenous whether question and an endogenous with-whom question, paying the split off with a system-level construct (structural differentiation) that redistributes explanatory weight between the two driver families (H7/H8), and metabolizing three different kinds of null in one results section. The corpus's clearest exemplar of a dual-driver incorporation story that answers its own title in the final paragraph."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records:
    - "PDM slices: gulati_1999_where_do_interorganizational_networks.pdm/sections/introduction.md, theory.md (primary story reading), then results.md, discussion.md payoff checks, methods.md alignment audit; fulltext.text-only.md not read — slices exist"
    - "PDM root: gulati_1999_where_do_interorganizational_networks.pdm.yaml (four verified distill_track identities + cross_section_identity C1-C5, coherence ok; writeback_verification PASS 90/FAIL 0). Note: the root authors field lists Ranjay Gulati only (vault frontmatter 'Gulati-1999'); the verified methods identity and the slice running header give the full authorship Ranjay Gulati & Martin Gargiulo — recorded here, not guessed"
    - "Section distillations: sections/introduction.json, theory.yaml, methods.json, results.json (all verified; central knot statement inherited from introduction.json phase_0_story_architecture)"
    - "Sentence archive: story-blueprints/v4/rhetoric-moves/sources/gulati_1999_where_do_interorganizational_networks.sentences.md"
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: null
classification:
  theoretical_problem_form: [explanatory-apparatus-reflexive-blindspot, genesis-question-whether-whom-decomposition, dual-driver-incorporation-synthesis, endogenous-network-dynamic, system-level-information-construct]
  narrative_dynamics: [answer-frontloaded-synthesis, mechanism-hypothesis-coupling-map, necessary-not-sufficient-handoff, selective-moderation-weight-redistribution, rival-adjudication-density, null-conditional-reestimation-rescoping, figure-readout-closure, footnote-carried-debates, title-question-return, monotonic-simplification-owned]
  retrieval_signals: [strategic-alliances, network-formation, embeddedness, structural-differentiation, core-periphery, structural-homophily, network-centrality, dyadic-panel-probit, random-effects, economic-sociology]
  confidence: provisional
mechanism_evidence:
  status: partly_probed
  basis: "The information-repository mechanism is warranted by 153 field interviews and tested only through positional correlates (prior tie counts, common third-party ties, centrality) plus one indirect probe — the legitimization rival (density) losing significance once structural differentiation enters — with lagged t-1 networks, MRQAP-like randomization, and a random-DV baseline ruling out artifact accounts; no information-flow variable is measured, and the recursive feedback loop itself is never fit."
section_learning:
  introduction:
    suitable: "yes"
    requires:
      - "an explanatory apparatus the field celebrates whose own origin the field never examines (a reflexive blind spot, not a missing variable)"
      - "a question decomposition whose halves map strictly onto an old and a new driver before any theory is written"
    learn:
      - "Reflexive-blindspot hook with incorporation concession: salute the embeddedness consensus, point out it has 'seldom examined the origin of those networks', carve out the few exceptions, name the exogenous default — then concede in the tension paragraph that the old view 'provides a good explanation of whether' but 'overlooks whom', so the critique hands the incumbent theory half the answer instead of overthrowing it, and the two-question RQ (where do cues come from; how do cues shape formation) is written to be answered by one synthesis sentence."
      - "AJS answer-frontloading with metatheory anchor: deliver the full dual-driver model in paragraph 3 with a recursive closure sentence ('embedded in the very same network that has shaped the organizational decisions to form those alliances'), then translate the contribution into the community's metatheoretical currency ('In theoretical terms, this is akin to specifying the mechanisms through which social structures shape organizational action and the mechanisms through which this action subsequently affects social structures')."
    caveat:
      - "Answer frontloading depends on a long introduction plus an independent multi-section theory chapter that will re-derive everything; in a short-introduction venue the same move overcommits and hollows the theory section (introduction.json risk ledger: answer-frontloading-mimicry)."
      - "The synthesis sentence reads as a theory platter unless the drivers are orthogonal — one driver answers one decomposed question; the opening also carries high citation density and no organizational face (collective academic actors instead), an AJS idiom that raises the entry cost for cross-field readers."
  theory:
    suitable: "yes"
    requires:
      - "a convergence of drivers on one dyadic outcome that can be decomposed into mechanism-sized, mutually exclusive information sources"
      - "a second theoretical life available for the same constructs once a system-level property is defined"
    learn:
      - "Mechanism-hypothesis coupling that reads as a map: each subsection names one mechanism, declares its reference frame, walks a two-step micro-mechanism (information advantage → uncertainty falls → tie probability rises), stages it with a manager quote, and closes with one hypothesis in a unified dyadic template ('The probability of a new alliance between two organizations increases with...') — the three embeddedness mechanisms have mutually exclusive criteria and ascending observation levels (dyad → triad → whole network), so H2-H5 feel like positions on a map rather than a list."
      - "Endogenous-dynamic second life via one new construct: §4 defines structural differentiation as an emergent systemic property, immediately caveats its own linearity (both extremes — undifferentiated and fully unique — are uninformative), then uses the construct twice, as a direct system-level driver (H6) and as a single moderator that redistributes explanatory weight between driver families (H7 weakens the exogenous driver, H8 amplifies positional embeddedness, with relational/structural explicitly exempted on an information-availability criterion) — closed by a figure-readout paragraph that names solid, dotted, and dashed arrows including the action-structure evolutionary link."
    caveat:
      - "The H6 linear statement sits against the section's own non-monotonic caveat — a tension the paper retains deliberately (Results footnote 14 tests polynomials only for the cohesion variables, not for structural differentiation; PDM flag C4) — copying the template means inheriting the duty to test or bound the functional form."
      - "Mechanism debates (structural equivalence rivalry, the spurious-correlation defense) are exiled to footnotes to keep one storyline — an AJS density luxury; the H5 derivation contains a mild leap (central actors refusing peripherals → homophily) backstopped by the homophily literature, not by the mechanism itself."
  methods:
    suitable: "partial"
    requires:
      - "a design whose promised dynamic can be carried structurally (lagged, updating network panels) and visualized before estimation"
      - "a named rival mechanism that can be operationalized as a control with a predeclared decision criterion"
    learn:
      - "Structural preanalysis as theory loopback: before any estimate, role-equivalence partitions and MDS maps of the 1988 networks visualize the very differentiation process the theory promised (four positions, core-periphery in all three industries), then feed construct operationalization (structural differentiation measured as centralization, trend .12→.34) — the descriptive figure does argumentative work for the endogenous story instead of decorating it."
      - "Named-rival-as-control with falsification apparatus: density-dependence legitimization is given its own paragraphs and a predeclared criterion ('If this were the case... the inclusion of alliance density should make the effect of structural differentiation insignificant'), backed by a random-DV baseline and MRQAP-like randomization for dyadic dependence — the rival enters the design as a character with lines, not as an unnamed omnibus control."
    caveat:
      - "Random effects are assumed without a sensitivity test (era flag; RE's strict assumptions acknowledged only in the appendix), the broad risk set is asserted 'essential' with the three-step robustness ladder reported only verbally, and dyad-year N never appears — a modern version must audit these."
      - "The preanalysis double-runs: it validates the theory by design and measures the moderator, so a writer without genuinely distinct constructs risks circularity between descriptive pattern and test variable."
  results:
    suitable: "yes"
    requires:
      - "hypotheses that produce at least two different kinds of null (a rival mechanism and a failed component) whose handling can differ in kind"
      - "interactions tested in separate models for a stated reason"
    learn:
      - "Three null architectures metabolized in one section: (a) rival adjudication — density, significant and theoretically read in the baseline, attenuates to non-significance once structural differentiation enters, with the candor line 'Although hypothesis 6 was not formulated as an alternative...'; (b) conditional re-estimation with construct-domain rescope — H5 'less conclusive', the ratio re-estimated separately, then the homophily claim rescored as applying only among central organizations (Mizruchi's central/peripheral role equivalence); (c) null-component candor — Model 10 reports a significant interaction on a null main effect with an explicit evidence-boundary sentence ('not strong enough... during the period of observation'). Each null is metabolized into the plot rather than footnoted away."
      - "Interaction sign-translation with survival line: H7/H8 interactions are introduced by translating the prediction into coefficient signs ('should translate into a significant and positive/negative coefficient'), the separate-model choice is declared with its multicollinearity reason, and each verdict carries a main-effect survival sentence ('interdependence on its own has a positive impact across all models') so moderation never reads as reversal."
    caveat:
      - "No magnitude translation anywhere (no AMEs or predicted probabilities; probit coefficients never read as sizes) — 1999-era anti-pattern, do not inherit; the density mediation is narrated post hoc without a formal test, and 'separate analyses' are never labeled exploratory."
      - "H5's ratio significance appears only in the estimation that excludes joint centrality — the conditionality is disclosed honestly, but a modern reviewer would demand the joint test rather than a rescope."
  discussion:
    suitable: "yes"
    requires:
      - "a title-worded question that the final paragraph can answer explicitly with a transformed, not repeated, claim"
      - "a supported mechanism whose known dark side can be projected into a future-research line"
    learn:
      - "Title-question return with dialectic upgrade: the closing paragraph answers the title in its own words ('Seeking an answer to the question in our title, we have shown that interorganizational networks result not only from exogenous drivers... but also from an endogenous evolutionary dynamic'), converting the finding into the structure-action duality the introduction anchored to, and generalizing genesis to market formation (White's self-reproducing social structures) — the origins question becomes a general account of how social structures form."
      - "Own the simplification, project the dark side: the discussion returns to §4's non-monotonic caveat as two alternative trajectories (inverse-U versus stable self-reproduction), concedes the monotonic hypotheses are 'a simplification warranted by the nature of our data, which cover only a segment' of the evolution, and then projects the mechanism's cost — overembeddedness, path dependence, instrumental rationality subordinated to embedded action — as the future line the story earns."
    caveat:
      - "The dark side (overembeddedness, path dependence) is asserted as possibility, not demonstrated; the core-periphery generalization rests on the descriptive preanalysis rather than the model; and the discussion carries several parallel extensions (mathematical network models, institutional coevolution, markets) that a tighter version would prune."
story_assessment:
  overall_role: exemplar
  mode: single_read
```

## Story Reading

### Theme question

Where do interorganizational networks come from — when a field explains organizational behavior by network embeddedness but treats the networks themselves as exogenous, do ties form only from exogenous resource interdependence (whether organizations seek cooperation), or does the emerging network itself, accumulating into a repository of partner information, endogenously shape with whom organizations ally — and thereby its own future form?

### Whole-story synopsis

The paper opens on a reflexive blind spot: organizational sociology explains action by embeddedness yet seldom asks where networks come from, defaulting to exogenous drivers that answer whether organizations should tie but not with whom. The tension paragraph splits the question — the exogenous approach "provides a good explanation of whether... but it overlooks whom" — and the double RQ (where do the cues come from; how do cues shape formation) is immediately answered in AJS answer-frontloading style: alliances are modeled as a dynamic process driven by exogenous interdependencies and endogenous embeddedness, with new ties increasingly "embedded in the very same network that has shaped the organizational decisions to form those alliances," a claim anchored to the classic structure-action duality and warranted by 153 field interviews plus a twenty-year, three-industry panel. The theory chapter builds the engine: alliances carry two uncertainties (information about competencies and needs; behavioral reliability under moral hazard), interdependence is necessary but not sufficient (H1), and the mechanism handoff ("If interdependence alone cannot offer sufficient cues... how do they decide with whom?") admits three embeddedness mechanisms — relational, structural, positional — each with a distinct reference frame, field-quote texture, and a hypothesis in a unified dyadic probability template (H2-H5). Then §4 grants the same constructs a second life: structural differentiation, defined as an emergent systemic property, directly raises tie probability (H6, with an explicit non-monotonic caveat about both extremes being uninformative) and moderates the driver families (H7 weakens interdependence as differentiation grows; H8 amplifies positional embeddedness, with relational/structural exempted), closed by a Figure 1 readout that includes the dashed action-structure arrow. The methods make the promise testable and visible: dyad-year risk sets, t-1 lagged networks built back to 1970 against left censoring, a structural preanalysis whose density tables and MDS maps display the promised core-periphery differentiation in all three industries, density entered as the named legitimization rival with a predeclared criterion, and a falsification apparatus (random-DV baseline, MRQAP-like randomization) in the appendix. The results stage the verdict in model order: H1 confirmed; H6 confirmed with the density rival attenuated to non-significance — the growth of alliances re-read as differentiation-driven information rather than legitimization; H2-H4 confirmed; H5 less conclusive and rescored (homophily holds only among central organizations); H7's negative and H8's positive interactions confirmed with main-effect survival lines and a null-component candor passage. Falling action polices the claims: footnote 14's polynomial probes find an inverted U for repeated ties and an exponential for common ties, with linear forms retained for parsimony. The ending answers the title, translates the finding into the structure-action dialectic, concedes the monotonic simplification (the data cover only a segment of the evolution), projects the mechanism's dark side (overembeddedness, path dependence), and generalizes network genesis to market formation.

### Characters and storylines

- **Main character — the emerging alliance network as a repository of partner information:** the paper's protagonist and its identity claim; introduced as an accumulating information base, given a measurable system-level expression (structural differentiation, centralization trend .12→.34), promoted to direct driver (H6) and moderator of the whole driver cast (H7/H8), and generalized at the ending into an account of social-structure genesis.
- **Second lead — exogenous interdependence:** the incumbent theory, incorporated rather than defeated; it answers the whether half of the RQ, delivers H1, then cedes explanatory weight as differentiation grows (H7) — its survival across all models is what makes the incorporation story honest.
- **Supporting cast — the three embeddedness mechanisms (relational, structural, positional):** the whom-side information channels at dyad, triad, and whole-network levels, staged with manager quotes; their observed traces (repeated ties, common ties, joint centrality, centrality ratio) carry H2-H5 and the H8 interaction.
- **Foil — density-dependent legitimization:** the named ecological rival (bandwagon legitimacy of a new cooperation form), staged respectfully as a control with its own theory paragraph and predeclared decision criterion, then attenuated to non-significance in Model 3 and re-read in the discussion as a mediated, secondary account.
- **Supporting cast — bounded-rational decision-makers under two uncertainties:** the micro-foundation (partner information; behavioral reliability) whose pain the fieldwork quotes voice; and the decision-makers' fieldworker author, whose 153 interviews double as recurring warrant.
- **Storyline 1 (exogenous whether):** resource needs → seeking cooperation → H1 → weakened but alive under H7.
- **Storyline 2 (embedded whom):** partner uncertainty → network as information repository → three mechanisms → H2-H5, with H5's homophily strand rescored as conditional.
- **Storyline 3 (differentiation):** accumulated action → structural differentiation → direct information effect (H6) → weight redistribution between driver families (H7/H8).
- **Storyline 4 (feedback loop):** action remakes the structure that guides action — promised in the introduction, carried by the lagged architecture and the preanalysis, generalized to markets in the ending.
- **Intersection:** all four storylines meet at the dyadic tie decision — the single point where whether (exogenous) and whom (endogenous) merge into one probability, and where the emerging structure both guides and is remade.

### Five acts

- **Exposition:** embeddedness progress acknowledged, its genesis blind spot named, exceptions carved out, exogenous default stated; the whether/whom concession splits the question; the double RQ; the full dual-driver answer fronted with the recursive closure sentence; the metatheory anchor to structure-action; the 153-interview warrant and twenty-year panel preview.
- **Rising action:** the alliance arena with two named uncertainties and a growth puzzle ("How do they do it?"); interdependence necessary-not-sufficient (H1); the alone-cannot handoff into embeddedness; three mechanisms staged with quotes and unified dyadic hypotheses (H2-H5); §4 defines structural differentiation, caveats non-monotonicity, derives H6 and the selective moderation pair H7/H8 with exemption defenses; Figure 1 readout closes the framework.
- **Climax:** Table 3's sequential reveal — H1; H6 with the density rival defeated (legitimization re-read as differentiation-driven information); H2/H3/H4 confirmed; H5 downgraded to "less conclusive," conditionally re-estimated, and rescored as central-organization homophily; H7's negative interaction; H8's positive interactions including a significant interaction on a null main effect.
- **Falling action:** footnote 14's polynomial probes (repeated ties inverted U; common ties exponential; linear retained for parsimony) partially answering the theory's own non-monotonic caveat; null controls disclosed item by item; the appendix's falsification apparatus (random-DV baseline, MRQAP-like randomization) securing the dyadic estimates.
- **Denouement:** the title question answered explicitly; the finding translated into the structure-action dialectic and generalized to market genesis; the monotonic simplification owned (observation window covers a segment); the mechanism's dark side (overembeddedness, path dependence) opened as future research; extensions to institutions, coevolution, and other tie types.

### Tension

- **Source:** the challenge is not a rival finding but the field's reflexive blind spot — an entire literature using networks as its explanatory apparatus while treating network genesis as exogenous — compounded by an internal tension: the same uncertainty that makes alliances valuable makes partner selection hard, and the remedy (relying on the existing network) may itself constrain choice. A second internal tension is formal: §4's non-monotonic caveat sits against H6's linear statement, and the observation window cannot contain the mature-structure alternative.
- **Construction:** the hook turns the field's celebrated concept into its own explanandum, and the concession sentence ("a good explanation of whether... but overlooks whom") splits the question so the incumbent theory is hired as half the answer rather than fired; the two uncertainties are made audible through manager quotes; the formal tension is surfaced by the authors themselves (the caveat paragraph, footnote 14's polynomials, and the discussion's "simplification warranted" concession), so the reader watches the paper police its own strongest claim.

### Alternative readings

- **author_signaled_alternative:** the discussion itself raises that the results "do not preclude" a tension between instrumental and social drives — that embeddedness may subordinate instrumental rationality (overembeddedness, path dependence, cohesive clusters limiting partner ranges), turning the paper's own mechanism into a potential harm. Reading the supported embeddedness effects as unambiguously beneficial overshoots what the authors claim; they explicitly flag the dark side as the open question.
- **analyst_counterfactual:** the Model 3 adjudication can be read the other way — structural differentiation is itself a function of the cumulative tie distribution, so "density attenuates once differentiation enters" is a contest between two constructs computed from the same underlying alliance data, not an independent test of information against legitimization; the mediation reading of density is narrative post hoc without a formal test (results.json cross-section note). The two accounts could be descriptions of one accumulation process at different granularities.

## Story Assessment

- **Theme coherence:** `works` — the whether/whom decomposition organizes hook, double RQ, driver synthesis, hypothesis map, interaction design, and the final title-question return; every hypothesis answers one half of the split, and the discussion closes the loop in the title's own words.
- **Character discipline:** `works` — the network-as-information-repository leads; interdependence is incorporated as a distinct second lead rather than a straw man; the three embeddedness mechanisms stay mutually exclusive with ascending observation levels; the density foil is theorized before it is defeated, and structural differentiation is explicitly distinguished from density in both theory (§4) and results (Model 3).
- **Knot integrity:** `works` — the genesis question is genuine (the field's own apparatus unexamined) and addressable: a dyad-year panel with lagged networks, a broad risk set, and a system-level measure can bear exactly the whether/whom answer the front end promises.
- **Plot emergence:** `works` — the hypotheses fall out of the mechanism decomposition rather than a template; the design's defining choices (t-1 updating networks, back-collection to 1970 against left censoring, broad risk set, centralization as the differentiation measure) arise from the endogenous-dynamic premise, and the preanalysis visualizes the promised process before any estimate.
- **Tie–unravel alignment:** `works` — both front-end questions are paid: cue source via H2-H4 plus the rescored H5, cue shaping via H6-H8, with the rival adjudication (density) upgrading the answer's distinctiveness; the two known residues are handled by the paper itself — the feedback loop is carried as architecture and descriptive trend with the mechanism honestly calibrated (`partly_probed`), and the H6 linearity tension is partially answered (footnote 14) then explicitly retained as a "simplification warranted by the nature of our data" rather than narrated away (PDM flag C4; a narrative risk the authors own, not an unpaid debt). C5 resolves here: the central knot defined at L2 is tied in the discussion — the ending returns to and transforms the opening question.
- **Ending quality:** `works` — the ending answers the title, translates the verdict into the structure-action dialectic, concedes the observation-window boundary, projects the mechanism's dark side as a earned future line, and generalizes genesis to market formation — transformation, not repetition.
- **Boundary:** This evaluates storytelling only — no inference about the validity of embeddedness theory, the probit identification, or journal value. The PDM L2 flags are digested as learning signals: C1 (intro Inadequacy ↔ theory Mechanism: the "overlooks whom" gap is exactly what the mechanism process theory answers) and C3 (theory promises ↔ dyad-level lagged design) underwrite plot emergence; C2 (estimator-family naming across methods/results) is a compatibility recorded in the methods audit; C4 (theory §4 non-monotonic caveat vs H6 linear statement) is recorded as an author-owned narrative risk in the tie-unravel rationale and the theory/results caveats — partially承接 by footnote 14, explicitly retained, not a hard flaw; C5 resolves here as `works`.

## Learning Affordances

### Introduction

- **Suitable:** `yes`
- **Learn:** (1) Reflexive-blindspot hook with incorporation concession — salute the field's consensus apparatus, name that its own origin is unexamined (with few-exceptions carve-outs), then split the question so the incumbent theory keeps the whether half and the new mechanism claims the whom half, writing the double RQ to be answerable by one synthesis sentence. (2) AJS answer-frontloading with metatheory anchor — deliver the complete dual-driver model in the introduction with a recursive closure sentence, then translate the contribution into the community's classic duality so readers across subfields can claim it.
- **Do not copy:** answer frontloading requires a long introduction plus an independent theory chapter — in a short-intro venue it overcommits; the synthesis sentence needs strictly orthogonal drivers (one per decomposed question) or it reads as a platter; the citation-dense, faceless opening is an AJS idiom, not a model for reader accessibility.

### Theory

- **Suitable:** `yes`
- **Learn:** (1) Mechanism-hypothesis coupling as a map — one mechanism per subsection with a declared reference frame, a two-step micro-mechanism, field-quote texture, and a unified dyadic probability hypothesis, the mechanism set chosen so criteria are mutually exclusive and observation levels ascend from dyad to triad to whole network. (2) Second-life dynamic via one new construct — define a system-level property, caveat its own functional form at both extremes, then reuse it as direct driver and as a single moderator that redistributes explanatory weight between driver families, exempting immune mechanisms on a stated information-availability criterion, and close with a figure readout that names every arrow type.
- **Do not copy:** the three-way embeddedness split belongs to the Granovetter lineage and cannot be rebranded; the linear H6 template imports the duty to test or bound functional form (footnote-14 duty); footnote exile of mechanism debates presumes a venue that tolerates long footnotes; the H5 leap (refusal → homophily) needed a literature backstop — do not treat it as self-sufficient derivation.

### Methods

- **Suitable:** `partial`
- **Learn:** (1) Structural preanalysis as theory loopback — visualize the promised emergent process (positions, core-periphery) descriptively before estimation and let it feed the moderator's operationalization, so the design's descriptive figure advances the claim. (2) Named rival with falsification apparatus — give the strongest alternative mechanism its own theory paragraph, operationalize it as a control with a predeclared significance criterion, and back the dyadic estimates with a random-DV baseline and randomization test.
- **Do not copy:** RE without sensitivity checks, the verbally reported risk-set ladder, and the missing dyad-year N are era tolerances to audit, not inherit; the preanalysis double-runs as validation and measurement — with less distinct constructs the same move is circular; "essential to uncovering unbiased results" is a strong claim that here leans on an untabled ladder.

### Results

- **Suitable:** `yes`
- **Learn:** (1) Three null architectures in one section — rival adjudication with an "not formulated as an alternative" candor line; conditional re-estimation plus construct-domain rescope anchored to an external distinction (central/peripheral role equivalence); null-component/significant-interaction candor with an evidence-boundary sentence — match the null's kind to its treatment instead of applying one template. (2) Interaction sign-translation with survival line — translate each predicted interaction into its coefficient sign, declare the separate-model choice with its reason, and close each verdict with a main-effect survival sentence so moderation reads as weight redistribution, not reversal.
- **Do not copy:** the total absence of magnitude translation (no AMEs or predicted probabilities) is a 1999 anti-pattern — modern probit work must add the amplitude beat; the density mediation is narrated post hoc and "separate analyses" are unlabeled exploratory — label both; H5's rescope rests on a separate estimation that excludes the co-tested variable, a conditional disclosure a modern submission must replace with a joint test.

### Discussion

- **Suitable:** `yes`
- **Learn:** (1) Title-question return with dialectic upgrade — answer the title in the final paragraph in its own words, translate the verdict into the metatheoretical duality the introduction anchored to, and generalize the genesis mechanism to adjacent structure-formation domains (markets as self-reproducing social structures). (2) Own the simplification, project the dark side — return the theory's internal caveat as named alternative trajectories, concede what the observation window cannot contain, and convert the mechanism's known cost (overembeddedness, path dependence) into the future-research line the story has earned.
- **Do not copy:** the dark side is projected, not demonstrated — a writer must mark it as possibility; the core-periphery generalization leans on the descriptive preanalysis rather than the model; the multi-front extension list (markets, institutions, mathematical models, other tie types) is an AJS-length luxury a tighter discussion would prune.

## Comparison prompt

Read this card against gulati1999-network-location-learning — same lead author, same year, the same 166-firm / three-industry / 1970-89 data program, opposite causal arrows: here the network is the explanandum (where does it come from), there it is the explanans (what does network location do for firms). Ask what adding one system-level construct (structural differentiation) buys that the firm-level construct (network resources) could not — specifically, how each paper carries the coevolution promise it makes (architecture plus explicit moderation versus lagged architecture alone), and where each puts its null (H5 rescoping plus density adjudication versus explained-away material-resource controls), given that one discussion owns its simplification while the other re-asserts the dynamic as if certified.
