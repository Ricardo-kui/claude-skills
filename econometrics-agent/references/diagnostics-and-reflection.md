# Diagnostics and Reflection

Source: extracted from the reflection log and per-estimator diagnostic assembly
in `lite_econometrics_agent.py`. This documents what the CLI **automatically
detects and reports**, so you know what is checked for you and what you still
owe yourself.

The reflection mechanism is **rule-based, not open-ended LLM self-repair**. It
records deterministic, citable events. That is a feature: the log is auditable.
The cost is that it will not catch design flaws the rules do not encode — those
remain the researcher's responsibility (and where the method cards' failure-mode
lists matter).

## Reflection log categories

The log (`reflection_log`) accumulates entries in four groups.

### 1. Routing upgrades
Recorded when the router adjusts the plan beyond a plain match:

- query suggests a global-polynomial RDD → `rdd_mode` upgraded to `global-poly`;
- event-study selected because the task asks for dynamic treatment effects in panel data;
- any other auto-routing decision the router wants to make visible.

### 2. Data cleaning (always inspect these)
Recorded before estimation, so dropped observations are never silent:

- trimmed whitespace from column names before matching variables;
- coerced a column to numeric and report how many new NaNs that introduced;
- dropped N rows with missing values in required variables;
- removed constant controls (zero-variance regressors).

### 3. Per-estimator diagnostics
Appended to the `diagnostics` list in the summary:

- **RDD / fuzzy-RDD**: global polynomial order; bandwidth or polynomial sensitivity comparison; support counts left/right of the cutoff; bandwidth used.
- **Fuzzy-RDD**: cutoff first-stage F statistic parsed from the first-stage diagnostics (the cutoff-as-instrument relevance check).
- **PScore estimators (psm / ipw / aipw / ipwra)**: balance summary built from `_balance_diagnostics`, comparing standardized mean differences before and after weighting/matching; propensity-range overlap.

### 4. Export notes
Recorded when artifacts are written:

- exported balance table / coefficient table / narrative to a path;
- requested a balance-table export from a method that does not produce one;
- failed to parse `label_map`, fell back to raw term names.

## Cross-cutting diagnostics you still owe yourself

The reflection rules cover mechanical failures. They do **not** discharge these
judgments, which belong to the researcher and should appear in any write-up:

- **Parallel trends** (DID / event study): needs a figure plus a placebo/falsification test, not just an insignificant lead. The CLI flags always-treated and non-monotone adoption; it does not adjudicate whether the control group is credible.
- **Weak instruments** (IV / fuzzy-RDD): the CLI reports a first-stage F, but Stock-Yogo critical values and Anderson-Rubin robust inference are Stata-side (`ivreg2`, `weakiv`).
- **Overlap / positivity** (pscore estimators): the CLI reports balance SMD and propensity range; the call on whether overlap is adequate is yours.
- **Bandwidth / functional form** (RDD): the CLI gives sensitivity across local-linear and global-poly; optimal bandwidth with bias correction is `rdrobust` in Stata.
- **Heterogeneous treatment effects** (staggered DID / event study): the CLI's TWFE estimates can be negative-weighted under staggered adoption. This is the single most important gap — see the `did` and `event-study` tool boundaries in `method-cards.md`.

## How to read a result

The decision-useful fields in a run summary are:

- `selected_model` and `selection_reasons` — what ran and why.
- `knowledge_card` — the method's identification logic and failure modes.
- `main_result` — coefficient, SE, significance, R² where defined.
- `diagnostics` — estimator-specific checks the CLI ran.
- `reflection` — the auditable log of cleaning, routing, and export events.

Treat `reflection` as a receipt: if rows were dropped or controls removed, the
log says so, and you should be able to justify each item in a methods footnote.
