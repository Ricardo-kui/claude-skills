# Diagnostics — Symptom → Test → Remedy → Recheck

**When to use**: whenever a regression looks wrong — a coefficient significant in the wrong direction, SEs that collapse or explode, a test that fires, a null result you don't trust, a reviewer objection. This is the cheatsheet's "tells & smells" promoted to a procedure.

**How to use**: find your symptom in the index, then work that card: test → interpret (against its assumption rung) → remedy → recheck. Each card ends on a **recheck criterion** — done when the diagnosis is resolved or explicitly declared unresolvable. Never leave a fired diagnostic unexamined.

**Diagnosis discipline**: a fired diagnostic is a fact about your identifying assumption, not a checkbox. Interpret it before remedying. Never "fix" a diagnostic by changing the spec to make it pass — that is specification search (ch20).

## Index

| Symptom | Card |
|---|---|
| Robust ≠ usual SEs, or BP/White significant | [1. Heteroskedasticity](#1-heteroskedasticity) |
| BG test fires; OLS vs FGLS diverge | [2. Serial correlation](#2-serial-correlation) |
| SEs collapse after FE; panel | [3. Panel: clustering](#3-panel-clustering) |
| First-stage F < 10 | [4. Weak instruments](#4-weak-instruments) |
| Individual t's all ns, joint F significant | [5. Multicollinearity](#5-multicollinearity) |
| Main effect null | [6. Null results](#6-null-results) |
| Count outcome, log(1+y) used | [7. Count misspecification](#7-count-misspecification) |
| RESET fires; turning point outside range | [8. Functional form](#8-functional-form) |
| Huge R², trending series | [9. Spurious regression](#9-spurious-regression) |
| Attrition / selected sample | [10. Sample selection](#10-sample-selection) |
| FE with lagged DV | [11. Dynamic panel bias](#11-dynamic-panel-bias) |
| Policy rolls out over time | [12. Staggered DiD](#12-staggered-did) |
| Policy varies across few clusters | [13. Few-cluster inference](#13-few-cluster-inference) |

---

## 1. Heteroskedasticity

- **Symptom.** Robust SEs differ markedly from usual SEs; Breusch-Pagan or special White test significant (regress û² on ŷ, ŷ²).
- **Test.** `reg y x, robust` vs default; `estat hettest` (BP) or regress û² on ŷ, ŷ² (special White).
- **Interpret.** MLR.5 (constant variance) fails. The coefficient is unchanged; only inference is at risk — robust SEs restore valid t/F.
- **Remedy.** Report robust SEs — the default for cross-sections, not a fallback. Do NOT switch to WLS/FGLS unless you can model the variance form (e.g. group-size weights for per-capita data); WLS loses unbiasedness, and OLS–WLS divergence means the mean equation is misspecified, not that WLS wins (ch08).
- **Recheck.** Robust and usual SEs both reported; if WLS was tried, the OLS–WLS divergence is stated and resolved (usually: keep OLS + robust).

## 2. Serial correlation

- **Symptom.** Breusch-Godfrey test fires; Durbin-Watson near 0; time-series residuals wander.
- **Test.** `estat bgodfrey` after OLS ((n−q)R² from regressing û on x and q lags of û; valid with a lagged DV).
- **Interpret.** Serial correlation breaks inference but not consistency — *only if* regressors are contemporaneously exogenous (TS.3′). Under strict exogeneity (TS.3) both are fine.
- **Remedy.** Newey-West/HAC SEs (safe: needs only contemporaneous exogeneity). Reach for FGLS Cochrane-Orcutt/Prais-Winsten only under strict exogeneity; if OLS ≠ FGLS coefficients, keep OLS (ch12).
- **Recheck.** HAC SEs reported; if FGLS was tried, the coefficient divergence is stated and OLS kept unless the strict-exogeneity case is made.

## 3. Panel: clustering

- **Symptom.** Switching from pooled OLS to FE shrinks SEs ~10×; or FE/RE run without `vce(cluster id)`.
- **Test.** Compare clustered vs default SEs on pooled OLS, RE, FE.
- **Interpret.** The composite error ν_it = a_i + u_it is serially correlated by construction, Corr(ν_it, ν_is) = σ²_a/(σ²_a + σ²_u) — default SEs are systematically too small (ch14).
- **Remedy.** Cluster by the cross-sectional unit on pooled OLS, RE, and FE. Cluster at the level where the assignment/policy variation lives — never on ex-post groupings of a random sample.
- **Recheck.** Clustered SEs everywhere; the clustering level matches the assignment unit; no ex-post grouping.

## 4. Weak instruments

- **Symptom.** First-stage F < 10 (|t| < 3.2 for one endogenous regressor); 2SLS estimate implausibly large or drifting toward OLS.
- **Test.** First-stage regression; F test on the excluded instruments. Under heteroskedasticity/serial correlation, demand Montiel Olea–Pflueger F ≳ 20.
- **Interpret.** IV relevance fails — the instrument explains almost no residual variation in x. 2SLS is biased toward OLS and its SEs are unreliable (ch15).
- **Remedy.** Report the weakness honestly; seek a stronger instrument or a different design; never paper over with a large sample. Run VAT/control-function and overid tests for the rest of the story.
- **Recheck.** First-stage F reported; the weakness acknowledged in text; no overinterpretation of a weak-IV estimate.

## 5. Multicollinearity

- **Symptom.** Individual t's all insignificant while the joint F is strongly significant; large SEs on a correlated set.
- **Test.** Joint F on the suspect regressors.
- **Interpret.** The data cannot separate the individual effects; the joint hypothesis is still testable. A data limitation, not an assumption failure.
- **Remedy.** Test jointly; do not drop the collinear variable on significance grounds (that is specification search); keep it if theory says it belongs and report the joint test.
- **Recheck.** Joint F reported; the collinear variable's retention justified by theory, not by its t.

## 6. Null results

- **Symptom.** Main coefficient insignificant; or significant in one spec and dead in others.
- **Test.** Precision (SE / confidence interval of the estimate), not just p-value; the sensitivity grid; the design's identifying assumption.
- **Interpret.** Null can mean no effect, or underpowered, or a failed design — distinguish before touching the spec (ch20).
- **Remedy.** (1) Report the effect size and CI honestly. (2) Audit the design — was the identifying assumption defensible? (3) Run and report the robustness grid. (4) Never search specs for significance: t/F assumes one model estimated once.
- **Recheck.** The null is stated as evidence with its rung named, not buried; the grid is reported; no spec was changed because of a p-value.

## 7. Count misspecification

- **Symptom.** log(1+y) used for a count/corner outcome; count regression with default (not robust) SEs.
- **Test.** Distribution of y (share at zero); compare OLS-log vs Poisson QMLE coefficients.
- **Interpret.** log(1+y) is not invariant to units and has no clean interpretation; Poisson QMLE needs only the mean right, E(y|x) = exp(xβ), with robust (overdispersion-corrected) SEs (ch17).
- **Remedy.** Poisson QMLE with exp-mean and robust SEs. Tobit only if y is a true corner in a continuous variable (latent normality required).
- **Recheck.** Poisson QMLE reported with robust SEs; if Tobit is used, the latent-normality assumption is stated.

## 8. Functional form

- **Symptom.** RESET fires (add ŷ², ŷ³); quadratic turning point |β̂₁/2β̂₂| outside the data range; dummy-in-log reported as δ×100%.
- **Test.** RESET; turning point vs the variable's observed min/max; exp(δ̂)−1 for the exact percentage.
- **Interpret.** The conditional-mean form is misspecified. RESET has no power against linear omitted variables or heteroskedasticity (ch09).
- **Remedy.** Adopt the flexible form the data support; report dummy-in-log exactly as 100[exp(δ̂)−1]%; mean-center interactions so main effects read as APEs.
- **Recheck.** Functional form matches the data's shape; the dummy-in-log effect is the exact percentage, not δ̂.

## 9. Spurious regression

- **Symptom.** Huge R² between two trending series; ρ̂ > 0.9; ADF/DF fails to reject a unit root.
- **Test.** (Augmented) Dickey-Fuller on each series; Engle-Granger on the levels residuals if a long-run relation is the point.
- **Interpret.** I(1) series in levels produce meaningless high R². DF has low power — "fail to reject a unit root" ≠ "is a unit root" (ch11, ch18).
- **Remedy.** Difference or use growth rates. If a long-run levels relation is the claim, test cointegration and estimate the ECM.
- **Recheck.** Each series classified I(0)/I(1); the levels regression is either cointegrated or dropped.

## 10. Sample selection

- **Symptom.** y observed only for a selected subsample; panel attrition; a Heckman-style concern.
- **Test.** Why is the sample selected? Is there a real exclusion restriction? In Heckit, the t-test on the inverse Mills ratio λ̂.
- **Interpret.** Selection on unobservables induces endogeneity controls alone don't fix; Heckit is identified by a credible exclusion restriction, not by functional form — the IMR is nearly linear (ch17). Panel attrition: FE tolerates attrition correlated with aᵢ but not with u_it — know which (ch14).
- **Remedy.** Heckit with a named and defended exclusion restriction; for panels, state the attrition type and use FE if it's aᵢ-driven.
- **Recheck.** Exclusion restriction named and defended; attrition type (aᵢ vs u_it) stated; IMR test interpreted.

## 11. Dynamic panel bias

- **Symptom.** FE with a lagged dependent variable; small T.
- **Test.** T size; compare FE-with-lag vs an estimator built for dynamics.
- **Interpret.** Strict exogeneity (FE.4) fails with a lagged DV — the within transform induces correlation between the transformed lag and the transformed error (Nickell bias), which shrinks in T (ch14).
- **Remedy.** Small T: use estimators designed for dynamic panels (Arellano-Bond and successors — beyond the book; route to `stata` / econometrics-agent). Moderate T: report the bias direction rather than ignoring it.
- **Recheck.** The dynamic structure is handled by an estimator whose assumptions are stated; the bias direction is acknowledged.

## 12. Staggered DiD

- **Symptom.** Policy rolls out across units at different times; TWFE (xtreg, fe + i.year) used.
- **Test.** Treatment-timing variation; heterogeneity across cohorts; negative-weight diagnostics.
- **Interpret.** TWFE is a weighted average of 2×2 DiDs that can carry negative weights under heterogeneous effects — the book's general w_it framework is the starting point, but the estimator is superseded here (registered exception).
- **Remedy.** Route to `staggered-did` (Callaway–Sant'Anna, Sun–Abraham, did2s, eventstudyinteract). Show parallel-trends evidence.
- **Recheck.** A modern staggered estimator is used; pre-trends are shown; cohort heterogeneity is reported.

## 13. Few-cluster inference

- **Symptom.** Policy varies across a handful of clusters (2–10 states/units).
- **Test.** Number of treated clusters.
- **Interpret.** Cluster-robust SEs are unreliable with few clusters even when computed — the asymptotics need many clusters (beyond the book).
- **Remedy.** Wild cluster bootstrap or randomization inference; report both point estimate and the bootstrap CI.
- **Recheck.** Few-cluster inference handled by a method that does not rely on many clusters.
