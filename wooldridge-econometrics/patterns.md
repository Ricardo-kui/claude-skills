# Patterns & Techniques — Wooldridge 8e

## Omitted Variable Bias Sign Analysis
**When to use**: A key regressor might be correlated with an omitted factor.
**How**: Bias(β̃₁) = β₂δ̃₁. Sign β₂ (effect of omitted on y) × sign δ̃₁ (regression of omitted on included). Use the Table 3.2 four-cell matrix.
**Trade-offs**: Signs only the bias when one omitted variable dominates; magnitude needs the full regression.

## Partialling Out (Frisch-Waugh) for Interpretation
**When to use**: To explain what "controlling for x₂" does, or to compute one slope by hand.
**How**: Regress x₁ on the other regressors → residuals r̂₁; regress y on r̂₁ → β̂₁ identical to multiple regression.
**Trade-offs**: Pedagogical/computational device; in practice just run the multiple regression.

## Heteroskedasticity-Robust Inference
**When to use**: Every cross-sectional regression by default.
**How**: Report White/Huber/Eicker SEs (Stata: `, robust`); use robust F/Wald/LM for joint tests. Optionally confirm with BP or special White test (û² on ŷ, ŷ²).
**Trade-offs**: Loses efficiency vs WLS if the variance form is truly known — rarely worth it.

## FGLS for Heteroskedasticity
**When to use**: Efficiency matters and the variance can be modeled (e.g. averaged/per-capita data: weight by group size).
**How**: 5 steps — OLS → save û → regress log(û²) on x → ĥ = exp(ĝ) → WLS with weights 1/ĥ. Always use robust SEs after WLS (h may be misspecified).
**Trade-offs**: No longer unbiased; OLS–WLS divergence signals a misspecified mean equation.

## Serial Correlation: Test then Fix
**When to use**: Any time-series regression.
**How**: Test with Breusch-Godfrey ((n−q)R² from regressing û on x and q lags of û; valid with lagged DV). Fix by Newey-West/HAC SEs (only contemporaneous exogeneity needed) or FGLS Cochrane-Orcutt/Prais-Winsten (needs strict exogeneity — strong).
**Trade-offs**: HAC keeps OLS and is safe; FGLS is efficient only under strict exogeneity — if OLS and FGLS coefficients diverge, keep OLS.

## IV / 2SLS Recipe
**When to use**: Endogenous regressor from omitted variables, simultaneity, or measurement error.
**How**: (1) Argue instrument exogeneity (Cov(z,u)=0, untestable — make the case). (2) Test relevance: first-stage F > 10 (|t| > 3.2 for one endogenous regressor). (3) Run 2SLS with software (never manual two-step — wrong SEs). (4) Diagnose: VAT/control-function endogeneity test; overid test if instruments > endogenous regressors.
**Trade-offs**: IV SEs are much larger than OLS; with weak instruments 2SLS can be worse than OLS.

## Panel: FD vs FE vs RE Decision
**When to use**: Same units observed T ≥ 2 periods with time-constant unobserved heterogeneity.
**How**: FE (within) is the default — consistent under strict exogeneity regardless of Corr(x, a_i). FD ≈ FE at T=2; prefer FE when idiosyncratic errors are serially uncorrelated, FD when they follow a random walk. RE only if Cov(x, a_i)=0 is credible — test with the Mundlak/CRE regression (add time-averages, F-test H₀: γ=0). Always cluster SEs by unit.
**Trade-offs**: FE discards all time-constant regressors and amplifies measurement error; RE is efficient but fragile.

## Difference-in-Differences (and DDD)
**When to use**: Policy varies across groups and time.
**How**: y = β₀ + δ₀d2 + β₁dT + δ₁(d2·dT) + controls; δ̂₁ is DiD. Defend parallel trends: plot pre-trends, add group-specific trends, or use a second control (DDD). Cluster at the policy-assignment level.
**Trade-offs**: Fails if treatment timing correlates with group trends; standard DiD breaks down under staggered timing with heterogeneous effects (see related staggered-did tooling).

## Binary Response: Logit/Probit with APE Reporting
**When to use**: Binary outcome where LPM's constant effects or heteroskedasticity bother you.
**How**: Estimate by MLE; test with LR = 2(L_ur − L_r) ~ χ²_q; report average partial effects (Stata `margins`), not raw coefficients. Compare LPM vs logit APEs — usually similar.
**Trade-offs**: MLE needs the full distribution right for consistency (unlike Poisson QMLE); no R² — use percent correctly predicted.

## Corner Solution / Count: Tobit vs Poisson QMLE
**When to use**: Outcome piles up at zero (or is a count).
**How**: If y ≥ 0 is a true corner in a continuous variable (hours worked, charitable giving) → Tobit, decompose effects by Φ(xβ/σ). If the object is E(y|x) for counts or corners → Poisson QMLE with exp(xβ) mean and robust (overdispersion-corrected) SEs. Never log(1+y).
**Trade-offs**: Tobit relies on normality+homoskedasticity of the latent error; Poisson QMLE only needs the mean right.

## Sample Selection: Heckit
**When to use**: y observed only for a selected subsample (wage offers for workers).
**How**: (1) Probit for selection on z (must contain an exclusion restriction — a variable in selection but not the outcome equation). (2) Compute IMR λ(zγ̂). (3) OLS of y on x and λ̂ on the selected sample; t-test on λ̂ tests selection bias.
**Trade-offs**: Fragile without a credible exclusion restriction; IMR is nearly linear in practice, so identification leans on functional form.

## Functional Form & Specification Diagnostics
**When to use**: Before settling a model.
**How**: RESET (add ŷ², ŷ³, F-test) for conditional-mean form; quadratic turning point |β̂₁/2β̂₂|; mean-center interactions so main effects are APEs; log-level dummy effects as 100[exp(δ̂)−1]%; compare nonnested models by adjusted R².
**Trade-offs**: RESET has no power against linear omitted variables or heteroskedasticity.

## Unit Root → Cointegration Workflow
**When to use**: Macro/persistent time series (ρ̂ > 0.9).
**How**: (1) (Augmented) Dickey-Fuller with DF critical values. (2) I(1)? Work in differences/growth rates. (3) If a long-run levels relation is the point: Engle-Granger cointegration test (DF on residuals); if cointegrated, estimate the ECM by the EG two-step or leads-and-lags for valid inference.
**Trade-offs**: DF tests have low power — "fail to reject unit root" ≠ "is unit root".

## Regression Discontinuity
**When to use**: Treatment assigned by a running-variable cutoff.
**How**: Local linear regression on both sides of the cutoff with IK bandwidth; fuzzy RD = IV with the cutoff indicator instrumenting treatment; check McCrary-style density continuity and covariate balance at the cutoff.
**Trade-offs**: Local effect only (at the cutoff); sensitive to bandwidth choice — report a grid.

## Treatment Effects under Unconfoundedness
**When to use**: Selection-on-observables is defensible (ATE.1) with overlap (ATE.2).
**How**: Estimator ladder — regression adjustment (RA) → propensity IPW → IPWRA (doubly robust: consistent if either model is right). Trim p̂ outside [0.1, 0.9] (Crump et al.). Report ATE and ATT.
**Trade-offs**: No insurance against unobserved confounding; pair with IV/RD/DiD when unconfoundedness is doubtful.
