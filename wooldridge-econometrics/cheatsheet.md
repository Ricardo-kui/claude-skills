# Cheatsheet — Wooldridge 8e Decision Rules

## Which estimator for my data?

| Situation | Default method | Key assumption | Watch out for |
|---|---|---|---|
| Cross-section, continuous y | OLS + robust SE | MLR.4 zero conditional mean | Omitted variables; never interpret without ceteris paribus logic |
| Cross-section, binary y | LPM (robust SE) or logit APE | same as OLS / correct distribution | LPM is heteroskedastic by construction |
| Count / corner at zero | Poisson QMLE (robust SE) | E(y\|x) = exp(xβ) only | Never `log(1+y)`; Tobit only for true censoring |
| y seen only for a selected sample | Heckit | exclusion restriction in selection eq. | IMR ≈ linear ⇒ fragile without exclusion |
| Regressor measured with error | IV (or accept attenuation) | CEV | β̂ biased toward 0; other coefficients contaminated unpredictably |
| Endogenous regressor | 2SLS | instrument exogeneity + relevance (F>10) | Manual two-step SEs are wrong |
| Two periods, before/after policy | DiD / FD | parallel trends | Pre-trend plots; cluster at policy level |
| Panel T ≥ 2, unobserved heterogeneity | FE (within), cluster SEs | strict exogeneity (FE.4) | Lagged DV + FE is inconsistent; FE kills time-constant regressors |
| FE vs RE | Mundlak/CRE test | H₀: γ=0 on time-averages | RE inconsistent if Corr(x,aᵢ)≠0 |
| Time series, persistent (ρ̂>0.9) | Difference first | I(1) vs I(0) | Spurious regression in levels; check cointegration |
| Running-variable cutoff | RD local linear, IK bandwidth | continuity at cutoff | Local effect; bandwidth sensitivity |
| Selection on observables | IPWRA (doubly robust) | unconfoundedness + overlap | Trim p̂∉[0.1,0.9]; no cure for hidden confounding |

## Tells & smells (if you see X → suspect Y)

- Huge R² between two trending series → spurious regression, detrend or difference.
- Significant t statistics with multicollinearity but joint F insignificant… actually: individual t's all insignificant, F strongly significant → multicollinearity, test jointly.
- OLS vs WLS (or OLS vs FGLS) coefficients diverge a lot → mean equation misspecified; keep OLS with robust SEs.
- First-stage F < 10 → weak instrument; 2SLS biased toward OLS.
- Dummy in log-level model read as "δ × 100%" → wrong; use 100[exp(δ̂)−1]%.
- Quadratic term significant, sign flips across sample → check turning point |β̂₁/2β̂₂| lies inside the data range.
- "Controlling for" a variable caused by treatment (mediator, collider, outcome component) → bad control; you blocked the causal path.
- Stepwise/step-model selection choosing regressors → data mining; t/F inference invalid. Do sensitivity analysis instead and report the grid.
- Trend extrapolated forecast from a random walk → nonsense; forecast the change, not the level.
- Standard errors shrink 10× after switching to FE → probably forgot to cluster by unit.
- Only a handful of clusters (e.g. policy varies across 2–10 states) → cluster-robust SEs are unreliable even if computed; use wild cluster bootstrap or randomization inference (beyond the book — check current literature).

## Thresholds & defaults Wooldridge commits to

| Rule of thumb | Value |
|---|---|
| Weak-instrument screen | first-stage \|t\| > 3.2 (one endog.) / F > 10; under heteroskedasticity or serial correlation demand F ≳ 20 (Montiel Olea–Pflueger) |
| Difference the series when | AR(1) coefficient ρ̂₁ > 0.9 (detrend first if trending) |
| Overlap trimming for ATE | keep p̂(x) ∈ [0.1, 0.9] (Crump et al.) |
| Joint hypotheses | F = t² when q = 1; use SSR form when the dependent variable changes, R² form only for exclusion restrictions on the same n |
| Dummy-in-log exact effect | 100[exp(δ̂) − 1]% |
| Log-level prediction | retransform with smearing factor exp(σ̂²/2), not just exp(ŷ) |
| Mechanical FD error correlation | Corr(Δu_t, Δu_{t−1}) = −0.5 under uncorrelated levels ⇒ cluster/robust SEs |
| Significance language | "statistically different from zero at the 5% level" — never "proves" |

## Assumption ladders (what each rung buys)

- **SLR.1–4** → OLS unbiased · **+SLR.5** → variance formulas, BLUE · **+SLR.6** → exact t/F (Ch 2, 4)
- **MLR.1–4** → unbiased · **+MLR.5** → BLUE · **+MLR.6 (normality)** → exact inference; large n ⇒ MLR.6 droppable (Ch 3–5)
- **TS.1–3** (strict exogeneity) → unbiased · **TS.1–5** → BLUE · **TS.1′–3′** (contemporaneous) → consistency only; **TS.1′–5′** → valid asymptotic t/F (Ch 10–11)
- **FE.1–4** → FE consistent · **+FE.5–7** → classical FE inference (Ch 14)
- **ATE.1** unconfoundedness + **ATE.2** overlap → RA/IPW/IPWRA identify ATE (Ch 19)
