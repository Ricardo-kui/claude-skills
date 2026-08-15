# Draft Revision Protocol

Use this protocol whenever the user supplies an existing Results draft, a path to one, revision notes, or asks to continue/revise/rewrite prior work.

## Contents

1. Source hierarchy
2. Revision intake
3. Section architecture
4. Analysis-unit contract
5. Paragraph and heading rules
6. Corpus use
7. Language locks
8. Completion checks

## 1. Source hierarchy

Resolve conflicts in this order:

1. Explicit decisions in the current user turn
2. Active language locks, Decision Register, and revision records in the current Results draft
3. Current Methods and verified tables/logs
4. Current `paper-state.yaml`
5. Theory only when the user or file state confirms it is current
6. Published exemplars and write-results corpus
7. Generic slot defaults

Never allow an obsolete Theory draft, an earlier plan, or a corpus default to overwrite a later user decision. Record unresolved conflicts instead of silently choosing.

## 2. Revision intake

Before planning or rewriting:

- Read the current manuscript text, not only its headings or a prior summary.
- Locate any revision log, language lock, table-number map, support-status table, and paper-state block attached to the draft.
- Read the current Methods passages that define samples, variables, estimators, and time windows used in Results.
- Verify every reported number against the designated table source when the task includes numerical revision.
- Separate manuscript prose from internal notes. Do not polish internal QC records as if they were submission text.

Produce an internal `revision_constraints` map:

```yaml
revision_constraints:
  mode: revision | local_rewrite
  hypothesis_order: [H1, H2]
  section_order: []
  current_sources: []
  stale_sources: []
  terminology_required: []
  terminology_prohibited: []
  language_locks: []
  voice_benchmarks: []
  prohibited_meta_wrappers: []
  prohibited_patterns: []
  superseded_advice: []
  mixed_findings_to_preserve: []
  table_number_source: ""
  authorized_scope: ""
```

Do not show this block unless useful to the user, but use it as a pre-generation gate.

## 3. Section architecture

Treat R1–R9 as evidence functions, not a mandatory sequence.

For an observational management paper with baseline tests plus supplementary analyses, use this default unless the current paper or target exemplars justify another order:

1. Descriptive statistics and unadjusted/model-free evidence
2. Baseline results, in hypothesis-number order
3. Sample selection and generalizability
4. Endogeneity, divided by source
5. Mechanism tests or rival explanations
6. Heterogeneity and boundary conditions
7. Other robustness checks
8. Optional evidence summary

Rules:

- A theoretical anchor may receive more interpretation without moving ahead of an earlier-numbered hypothesis.
- Keep sample selection separate from endogeneity when either contains more than one substantive analysis. Selection asks who or what enters the observed sample; endogeneity asks why the focal regressor and outcome may be jointly determined or confounded.
- Place each test under the empirical problem it can diagnose. Do not group Heckman, IPW, Lewbel, placebo, alternative estimators, and measurement checks merely because they are all “additional analyses.”
- Order endogeneity analyses by the source of bias: omitted variables, reverse temporal ordering/simultaneity, measurement error, or another design-specific source. The estimator name is secondary.
- Distinguish confirmatory hypotheses, mechanism/rival tests, exploratory heterogeneity, and robustness. Do not relabel one category to improve the story.

## 4. Analysis-unit contract

Every selection, endogeneity, rival-explanation, heterogeneity, and robustness unit must answer six questions. These are logical moves, not six mandatory sentences.

1. **Problem path** — What exactly could go wrong, through which data-generating or sampling path?
2. **Affected inference** — Which hypothesis, outcome, coefficient, or scope claim would be distorted, and in what plausible direction?
3. **Diagnostic implication** — If the concern were true, what observable pattern should appear?
4. **Test and fit** — Why can the chosen analysis detect or reduce that concern?
5. **Evidence** — What does the analysis show, including divergent or null results?
6. **Verdict and residue** — What concern is reduced, qualified, or unresolved? State what the test cannot establish.

The following openers fail because they only name a category:

- “A first concern is that the baseline associations may reflect which firm-years enter the recall record.”
- “A different selection issue concerns the composition of realized recalls.”
- “We conducted several robustness checks.”

Repair them by identifying the entry mechanism and the affected estimand. For example, distinguish:

- firms excluded because they never record an event during the panel;
- potential problems that never become observed events;
- realized-event samples in which high-occurrence firm-years contribute disproportionate observations;
- attrition or matching restrictions that alter generalizability.

Do not claim that a test “addresses endogeneity” in general. Name the source it bears on and calibrate the verdict to that source.

## 5. Paragraph and heading rules

### Headings

- When a section contains two or more distinct analyses, give each analysis a short subheading.
- Prefer `Empirical problem: analysis` or an empirical-problem heading such as `Selection into the Recall Record: Heckman Correction`.
- A method-only heading such as `Heckman Test` is acceptable only when the surrounding section already states the exact problem.
- Headings must help readers distinguish analyses; do not create a heading for every table row or coefficient.

### Paragraphs

- Give each paragraph one evidence function.
- Default to fact-forward Results voice: state the empirical fact, add at most one necessary explanatory sentence, and tie the verdict to the hypothesis or theoretical prediction.
- Build a sentence chain: problem → diagnostic logic → procedure/evidence → implication. Adjacent sentences must have an explicit logical relation, not merely share a topic.
- Merge beats when natural. Four short sentences that mechanically mirror a template still count as a list.
- Use table references where they orient the reader, but do not begin every paragraph with `Table X reports`.
- End with a calibrated inference, not a repeated summary of the preceding sentence.
- When several columns answer one problem, synthesize them. When columns answer different problems, split the paragraph or analysis unit.

### Support judgments

Separate two judgments:

- `baseline_verdict`: whether the designated baseline estimate supports the hypothesis;
- `overall_evidence`: whether selection, endogeneity, measurement, subsample, and alternative-specification evidence leaves the result stable, qualified, mixed, or unresolved.

Never turn a baseline-supported but fragile result into “robust support.” Never treat robustness checks as votes; explain which inferential boundary each one changes.

## 6. Corpus use

For paragraph-level rewriting:

1. Identify the paragraph’s evidence function and estimator family.
2. Retrieve 2–4 matched variants from the relevant corpus files.
3. Compare their ordering, transitions, qualification, and evidence density.
4. Synthesize a paragraph around the current paper’s facts.
5. Check that no source-specific syntax, coefficient, table number, or distinctive phrase has been copied.

Use a published exemplar to solve a rhetorical problem, not to dictate the paper’s empirical architecture. User decisions and current evidence always outrank corpus frequency.

## 7. Language locks

Apply project-specific locks from the current draft. Unless the user requests otherwise, also enforce these defaults:

- Do not use `model`, `modeled`, `modelled`, `modeling`, or `modelling` as verbs. Use `estimate`, `re-estimate`, `analyze`, `specify`, `include`, or a direct description of the unit/estimator.
- Do not use self-evaluative reporting wrappers such as `we report honestly`, `we disclose`, `rather than papering over`, `we do not present this as`, or analogous claims of transparency. State the direction, uncertainty, magnitude, and limitation directly.
- Preserve the operational terms used in the current Methods. Do not invent umbrella constructs, “margins,” “universes,” or propensities that the paper has not defined.
- Avoid `results are uniformly robust`, `all results hold`, or equivalent language when any material test diverges.
- Avoid repeated `First/Second/Finally` sequences when the headings already supply navigation.
- Use present tense for table content and inferential judgments where journal convention supports it (`Table 4 shows`; `the coefficient is`). Do not mechanically copy Methods tense.

## 8. Completion checks

A revision is incomplete if any of the following remains:

- the current draft or its revision record was not read;
- hypothesis display order was changed only to emphasize the theoretical anchor;
- selection and endogeneity tests are pooled without source-specific logic;
- a threat opener does not explain how the problem enters the data or affects inference;
- multiple analyses lack navigable subheadings;
- paragraph sentences read as independent report entries rather than an evidence chain;
- a prior language lock reappears;
- a superseded wording suggestion or meta-reporting wrapper reappears;
- the paragraph comments on the authors' honesty/transparency instead of stating the evidentiary limitation;
- a mixed/null finding is absent from both the prose and evidence summary;
- the new wording changes a number, sample, table reference, or estimand without evidence.
