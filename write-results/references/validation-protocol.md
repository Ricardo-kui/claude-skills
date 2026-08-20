# Validation Protocol

Run these gates after generating or revising Results. A failed gate requires another revision before delivery.

## Gate 1 — Source fidelity

- Current Results and revision records were read in revision mode.
- Stale or obsolete files did not govern the rewrite.
- Samples, years, variable definitions, estimators, table numbers, and numerical values match current sources.

## Gate 2 — Hypothesis reporting

- Baseline results follow the locked hypothesis order.
- Each hypothesis reports direction, uncertainty/significance, substantive magnitude, and baseline verdict.
- Baseline verdict is separated from overall evidence stability.
- Null, reversed, and mixed findings remain visible.

## Gate 3 — Section architecture

- The section order follows the paper’s evidence logic, not the numeric order of R1–R9.
- Sample selection and endogeneity are separated when they address distinct problems.
- Endogeneity tests are ordered by source of bias.
- Mechanism/rival tests, heterogeneity, and robustness are not conflated.

## Gate 4 — Analysis-unit logic

For every supplementary analysis, verify:

- the exact problem path is stated;
- the affected inference is named;
- the test’s diagnostic implication is explained;
- the method fits that implication;
- the result includes divergent evidence;
- the verdict is no broader than the test permits.

Generic `One concern is ...` language without a path and affected inference fails this gate.

## Gate 5 — Navigation and prose

- Sections with multiple analyses use informative subheadings.
- Each paragraph performs one evidence function.
- Sentences form a problem→evidence→implication chain rather than a list.
- Table navigation does not crowd out interpretation.
- Repeated `First/Second/Finally`, repeated support judgments, and boilerplate transitions are removed.
- Prose follows the active voice benchmark: empirical fact first, no more explanation than the evidence needs, and a verdict tied to the hypothesis/theory rather than to the authors' reporting conduct.

## Gate 6 — Language and terminology

- Current Methods terminology is preserved.
- Project language locks are satisfied.
- `model/modeled/modelled/modeling/modelling` is not used as a verb unless explicitly permitted.
- Self-evaluative wrappers (`we report honestly`, `we disclose`, `rather than papering over`, `we do not present this as`, and equivalents) are absent; limitations are stated directly.
- No unsupported umbrella construct or uniform-robustness claim appears.
- Causal language matches design strength.

## Gate 7 — Feedback regression

- Active skill, project, section, and estimator feedback rules were loaded.
- Rules and legacy advice named in an applicable `supersedes` field were excluded even if they remain in revision history or corpus notes.
- Every rule relevant to the current passage has a pass/fail result.
- The deterministic language lint passed for all applicable `prohibited_patterns`; its default boundary excluded the revision/audit log but not manuscript prose.
- Any newly exposed failure is registered after the manuscript correction.

## Evidence summary trigger

When the paper has at least two hypotheses and at least four supplementary analyses, or when evidence is materially mixed, produce or update a summary table with:

| Analysis | Problem addressed | H1 | H2 | Interpretation | Location |
|---|---|---|---|---|---|

Use `supports | qualifies | does not support | mixed | not applicable`. The table is an audit map, not a vote count. A hypothesis may be baseline-supported while its overall evidence is qualified.

## Optional independent review

After the internal gates pass, `/results-review <current Results path>` may provide a second-pass audit. Use `distill-results-exemplar` only for published exemplars and corpus maintenance; it has no draft-validation mode.
