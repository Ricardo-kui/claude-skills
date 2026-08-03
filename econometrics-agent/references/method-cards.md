# Method Knowledge Cards

Source: extracted from `lite_method_knowledge.py` in the Econometrics-Agent LITE
install (`C:\Users\admin\Econometrics-Agent`). Each card states when to use the
estimator, the variation its estimate leans on, what to diagnose, and where it
commonly fails. A final **Tool boundary** line marks where this CLI's
implementation stops and where the Stata stack (via `stata-code` MCP) should
take over.

These cards are **method knowledge, not execution instructions**. They are
reusable across `econometrics-agent`, `causal-analysis`, `did-analysis`,
`stata-regression`, and related skills. They describe estimators, not any one
tool's flags.

## How to read a card

- **When to use** — the design situation that points to this estimator.
- **Core routing rule** — how the auto-router picks it (full logic in `model-selection-rules.md`).
- **Required inputs** — what must be present in the data or command.
- **Identification logic** — what variation the estimate uses, and the assumption that licenses a causal reading.
- **Diagnostics to check** — inspect these before trusting the result.
- **Common failure modes** — recurring ways the estimate goes wrong.
- **Tool boundary** — what this CLI does not do; hand off to Stata here.

---

## ols — Robust OLS

- **When to use:** baseline associative models or treatment-effect regressions when endogeneity and panel structure are not the dominant design problem.
- **Core routing rule:** fallback baseline when no stronger panel, IV, or policy-shock design is clearly specified.
- **Required inputs:** outcome, treatment, optional controls.
- **Identification logic:** interpret the treatment coefficient as a conditional association unless the design gives stronger causal leverage.
- **Diagnostics to check:** treatment coefficient precision; constant or collinear regressors; omitted-variable risk.
- **Common failure modes:** using OLS despite endogeneity; overstating causal claims from descriptive models.
- **Tool boundary:** this CLI supports robust and HAC standard errors. For endogeneity use IV (single-instrument only here); for multi-instrument IV with full weak-identification diagnostics, run `ivreg2` / `ivreghdfe` in Stata.

## fe — Two-Way Fixed Effects

- **When to use:** panel data where identification relies on within-unit variation after absorbing entity and time shocks.
- **Core routing rule:** if the data are panel and the task is not clearly IV, DID, or event study, default to FE rather than pooled OLS.
- **Required inputs:** outcome, treatment, entity_id, time_id, optional controls.
- **Identification logic:** use within-entity treatment changes while differencing out unit and calendar-time confounders.
- **Diagnostics to check:** within-unit treatment variation; absorbed regressors; identification after FE.
- **Common failure modes:** no within-unit variation; assuming FE solves endogeneity automatically.
- **Tool boundary:** this CLI implements TWFE with one-way cluster, two-way cluster, and HAC covariance. Under staggered adoption with heterogeneous treatment effects, TWFE is biased; the modern estimators (Callaway-Sant'Anna `csdid`, Sun-Abraham `eventstudyinteract`, de Chaisemartin `did_multiplegt`) live in Stata.

## iv — IV-2SLS

- **When to use:** treatment is endogenous and a credible external instrument is available.
- **Core routing rule:** if an instrument is provided or the query explicitly mentions IV / endogeneity, route to IV before FE or OLS.
- **Required inputs:** outcome, treatment, instrument, optional controls.
- **Identification logic:** use only the treatment variation induced by the instrument, not the full endogenous treatment variation.
- **Diagnostics to check:** first-stage relevance; weak instrument risk; exclusion restriction plausibility.
- **Common failure modes:** weak instruments; bad instruments that directly affect the outcome.
- **Tool boundary:** this CLI supports a **single instrument** and flags weak-instrument risk. For multiple instruments, Stock-Yogo critical values, and Anderson-Rubin weak-instrument-robust inference, run `ivreg2` / `ivreghdfe` / `weakiv` in Stata.

## did — Difference-in-Differences

- **When to use:** policy shocks or treatment-timing designs where treated and control units are compared before and after adoption.
- **Core routing rule:** if the query is about a policy effect or treatment timing and the data provide group-post or staggered timing, prefer DID over generic FE.
- **Required inputs:** outcome, group-post or panel treatment indicator; entity_id + time_id recommended.
- **Identification logic:** compare changes over time for treated units against changes for control units under a parallel-trends assumption.
- **Diagnostics to check:** parallel-trends plausibility; treatment timing variation; binary treatment design.
- **Common failure modes:** no real control group; non-binary treatment timing; causal claims without design checks.
- **Tool boundary:** this CLI's staggered DID is a **TWFE implementation** and inherits the Goodman-Bacon / negative-weighting problem under heterogeneous treatment effects. For robust dynamic ATT, use `csdid`, `did_multiplegt`, or `did_imputation` in Stata. Always present parallel-trends with both a figure and a placebo test.

## event-study — Staggered DID Event Study

- **When to use:** dynamic treatment effects, pre-trend checks, or lead-lag coefficients around staggered adoption.
- **Core routing rule:** if the query asks for event-study dynamics or pre-trend diagnostics in panel data with treatment timing, route here before plain DID.
- **Required inputs:** outcome, binary treatment indicator, entity_id, time_id, optional controls.
- **Identification logic:** estimate dynamic lead and lag coefficients around first treatment adoption while absorbing entity and time effects.
- **Diagnostics to check:** significant pre-treatment leads; always-treated units; coherent treatment timing.
- **Common failure modes:** always-treated units; treatment that turns on and off repeatedly; over-interpreting noisy pre-trends.
- **Tool boundary:** this CLI assumes **monotone binary adoption**. For estimators robust to heterogeneous and dynamic treatment effects (Sun-Abraham, Borusyak-Jaravel-Spiess), use `eventstudyinteract` / `did_imputation` / `eventstudyinteract` in Stata.

## rdd — Sharp RDD

- **When to use:** treatment assignment changes discontinuously at a known cutoff in a running variable.
- **Core routing rule:** if the query mentions a cutoff / threshold / discontinuity and a running variable plus cutoff are provided, route to sharp RDD.
- **Required inputs:** outcome, treatment, running_variable, cutoff, optional controls.
- **Identification logic:** compare observations just above and below the cutoff under continuity of potential outcomes at the threshold.
- **Diagnostics to check:** support on both sides of the cutoff; bandwidth or polynomial sensitivity; whether treatment jumps sharply at the threshold.
- **Common failure modes:** cutoff outside support; fuzzy treatment despite sharp-RDD specification; too-wide bandwidth driving global functional-form bias.
- **Tool boundary:** this CLI offers local-linear and global-polynomial fits plus bandwidth/poly sensitivity. For data-driven optimal bandwidth with bias correction and valid CI, run `rdrobust` in Stata.

## psm — Propensity Score Matching

- **When to use:** binary treatment with plausible selection on observables, especially when matching is explicitly requested.
- **Core routing rule:** if the query asks for matching or PSM and the treatment is binary, route here before plain OLS.
- **Required inputs:** outcome, binary treatment, covariates for the propensity model.
- **Identification logic:** reweight the sample by matching treated and control observations with similar estimated treatment propensity.
- **Diagnostics to check:** overlap in propensity scores; balance intuition; sensitivity to matched neighbor count.
- **Common failure modes:** poor overlap; using PSM without credible observables; treating matching estimates as immune to hidden bias.
- **Tool boundary:** this CLI reports standardized mean-difference balance. For Rosenbaum sensitivity bounds to hidden bias, caliper and kernel matching, and `teffects`-based inference, use `psmatch2` / `teffects` in Stata.

## ipw — Inverse Probability Weighting

- **When to use:** binary treatment when the user wants weighting from estimated treatment probabilities rather than nearest-neighbor matching.
- **Core routing rule:** if the query asks for IPW / weighting from propensity scores and the treatment is binary, route here.
- **Required inputs:** outcome, binary treatment, covariates for the propensity model.
- **Identification logic:** estimate treatment probabilities and weight observations by the inverse of the treatment they received.
- **Diagnostics to check:** extreme propensity scores; effective weight stability; common support.
- **Common failure modes:** extreme weights; positivity violations; using IPW with a badly misspecified propensity model.
- **Tool boundary:** this CLI flags extreme weights and overlap. For stabilized weights, trimming rules, and doubly-robust SEs, use `teffects ipwra` in Stata.

## aipw — Augmented IPW (doubly robust)

- **When to use:** binary treatment when the user wants a doubly robust estimator combining an outcome model with inverse-probability weighting.
- **Core routing rule:** if the query asks for AIPW, augmented IPW, or doubly robust estimation with binary treatment, route here before plain IPW.
- **Required inputs:** outcome, binary treatment, covariates for propensity and outcome models.
- **Identification logic:** combine treatment-probability weighting with separate outcome regressions so consistency survives one model being misspecified.
- **Diagnostics to check:** common support; extreme weights; balance after weighting; dependence on outcome-model functional form.
- **Common failure modes:** poor overlap; joint misspecification of propensity and outcome models; treating doubly robust as assumption-free.
- **Tool boundary:** supports ATE and ATT. For cross-fitting / machine-learning outcome models (DML), run a separate workflow; this CLI uses parametric nuisance models.

## ipwra — IPW Regression Adjustment (doubly robust)

- **When to use:** binary treatment when the user wants a doubly robust weighted regression-adjustment estimator rather than AIPW's augmentation formula.
- **Core routing rule:** if the query asks for IPWRA or doubly robust regression adjustment with binary treatment, route here.
- **Required inputs:** outcome, binary treatment, covariates for propensity and outcome models.
- **Identification logic:** estimate treatment propensity, construct inverse-probability weights, and run a weighted regression-adjustment model for the outcome.
- **Diagnostics to check:** common support; extreme weights; balance after weighting; sensitivity to regression specification.
- **Common failure modes:** poor overlap; joint misspecification of weighting and outcome models; reading weighted regression adjustment as assumption-free.
- **Tool boundary:** supports ATE and ATT. The Stata equivalent is `teffects ipwra`, which also provides proper treatment-effect SEs.

## fuzzy-rdd — Fuzzy RDD

- **When to use:** cutoff assignment shifts treatment probability but does not deterministically assign treatment.
- **Core routing rule:** if the query explicitly mentions fuzzy RDD and running-variable / cutoff inputs are available, route here instead of sharp RDD.
- **Required inputs:** outcome, treatment, running_variable, cutoff, optional controls.
- **Identification logic:** use crossing the cutoff as an instrument for treatment within a local bandwidth around the threshold.
- **Diagnostics to check:** support near cutoff; first-stage jump in treatment probability; bandwidth or polynomial sensitivity.
- **Common failure modes:** weak first stage at the cutoff; using fuzzy RDD when treatment is actually sharp; interpreting global patterns as local treatment effects.
- **Tool boundary:** this CLI reports a cutoff first-stage F statistic. For optimal-bandwidth fuzzy estimation with bias-corrected CIs, run `rdrobust` with the fuzzy option in Stata.
