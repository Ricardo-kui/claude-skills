# Validation Protocol

Run these gates after revising Methods.

## Gate 1 — Source truth

- The current Methods body and revision history were read.
- Sample, time window, units, severity classes, measures, and estimators agree with verified project materials.
- Stale theory or earlier drafts did not override current decisions.

## Gate 2 — Section ownership

- Baseline design and estimator information remain in Methods.
- Supplemental selection, endogeneity, sensitivity, mechanism, heterogeneity, and robustness analyses remain in Results unless they are part of the baseline design.
- Variables moved to Results have no orphaned Methods definition or preview.

## Gate 3 — Slot integrity

- Each M1–M10 paragraph performs its assigned evidence function.
- Measurement sections do not preview estimator mechanics; estimator sections do not redefine constructs.
- Sample funnel, unit of analysis, and estimand are explicit and internally consistent.

## Gate 4 — Argument and evidence

- Estimator choices are justified by the data-generating process or diagnostics.
- Controls correspond to concrete rival explanations.
- Measurement defenses identify the actual threat and the evidence addressing it.
- Methods does not report hypothesis support, coefficients, or robustness outcomes.

## Gate 5 — Voice and language

- Completed procedures use active past tense; definitions and general properties use present tense.
- Terminology matches the current paper and does not revive removed umbrella constructs.
- Limitations and scope conditions are stated directly, without defensive or self-congratulatory wrappers.
- Corpus sentence architecture may be used directly; source-specific content (proper names, numbers, coefficients, table numbers) is replaced.

## Gate 6 — Feedback regression

- Active skill, project, section, and design-type feedback rules were loaded.
- Superseded rules and legacy advice were excluded from generation.
- Every applicable rule has a pass/fail result.
- `lint_methods_language.py` passed for applicable prohibited patterns using the manuscript-body boundary.
- Any new failure was corrected before being registered.
