# Chapter 11: Further Issues in Using OLS with Time Series Data

## Core Idea
OLS with time series data is asymptotically justified only when the series are **weakly dependent**; highly persistent (unit root, I(1)) series must usually be first-differenced before regression, or inference is misleading.

## Frameworks Introduced
- **Asymptotic Gauss-Markov assumptions TS.1′–TS.5′**: the replacement for TS.1–TS.6 when strict exogeneity and normality fail. TS.1′–TS.3′ give consistency (Theorem 11.1: plim β̂_j = β_j); adding TS.4′ and TS.5′ gives asymptotic normality (Theorem 11.2: usual OLS SEs, t, F, and LM statistics are asymptotically valid).
  - When to use: any time series regression where lagged dependent variables appear (strict exogeneity TS.3 then *cannot* hold) or errors may not be normal.
  - How: verify weak dependence (check ρ̂₁), then run OLS and use standard inference in moderate-to-large samples; no normality assumption needed.
- **I(0)/I(1) classification with first-differencing fix**: I(0) = weakly dependent in levels, use directly; I(1) = weakly dependent only after first differencing ("difference-stationary").
  - When to use: levels of interest rates, inflation, prices, log wages/productivity — series with ρ̂₁ near 1.
  - How: compute first-order autocorrelation ρ̂₁ (detrend first if the series trends); difference if ρ̂₁ > 0.9 (some use 0.8); use Δy_t or growth rate Δlog(y_t); first differencing also removes linear time trends, so drop the trend term after differencing.
- **Dynamically complete model**: enough lags included that E(y_t | x_t, y_{t−1}, x_{t−1}, …) = E(y_t | x_t) — no further lags of y or x help explain y_t.
  - When to use: models with lagged y (AR, ADL) where you want TS.5′ (no serial correlation) to hold by construction.
  - How: dynamic completeness implies TS.5′; test by adding lags (e.g. y_{t−1}) and checking significance. Do not force it on static/FDL models — serial correlation there is handled in Chapter 12, not by piling on lags.

## Key Concepts
- **Stationary (strictly stationary) process**: joint distribution of any collection (x_{t1},…,x_{tm}) is unchanged when shifted h periods.
- **Covariance stationary process**: constant mean, constant variance, and Cov(x_t, x_{t+h}) depends only on h, not t.
- **Weakly dependent (asymptotically uncorrelated)**: Corr(x_t, x_{t+h}) → 0 sufficiently fast as h → ∞; replaces random sampling so the LLN and CLT apply.
- **MA(1) process**: x_t = e_t + α₁e_{t−1}; stationary, weakly dependent, Corr(x_t,x_{t+1}) = α₁/(1+α₁²), zero beyond lag 1.
- **Stable AR(1) process**: y_t = ρ₁y_{t−1} + e_t with |ρ₁| < 1; Corr(y_t, y_{t+h}) = ρ₁^h dies out geometrically.
- **Contemporaneous exogeneity (TS.3′)**: E(u_t | x_t) = 0 — much weaker than strict exogeneity; allows feedback from past y to current x and allows lagged y as regressor.
- **Random walk / unit root process**: y_t = y_{t−1} + e_t (ρ₁ = 1); Var(y_t) = σ²_e·t grows, shocks persist forever, E(y_{t+h} | y_t) = y_t.
- **Random walk with drift**: y_t = α₀ + y_{t−1} + e_t; E(y_t) = α₀t, so it trends *and* is highly persistent.
- **First-order autocorrelation ρ̂₁**: sample correlation of y_t and y_{t−1}; consistent for ρ₁ when |ρ₁|<1 but biased downward when ρ₁ near 1.
- **Sequentially exogenous**: E(u_t | x_t, x_{t−1}, …) = 0; weaker than dynamic completeness when x_t excludes y_{t−1}; the right assumption for FDL models.

## Mental Models
- Think of **weak dependence as the time series substitute for random sampling**: without it the LLN/CLT fail and no asymptotic rescue exists for OLS.
- Use **ρ̂₁ as a persistence gauge, not a test**: ρ̂₁ > 0.9 → difference; between 0.8–0.9 judgment call; formal unit root tests wait until Ch 18.
- Think of **a random walk as a series with infinite memory**: today's value is the best forecast of any future value; a stable AR(1) forgets at rate ρ₁^h.
- Use **trending ≠ persistent**: a trend-stationary series is nonstationary but weakly dependent — include a time trend and proceed (Ch 10); a unit root series needs differencing. Detrend before computing ρ̂₁ or you overstate persistence.

## Anti-patterns
- **Regressing I(1) levels on each other and trusting t statistics**: CLM assumptions fail, LLN/CLT don't apply → spurious regression (Example 11.6: significant levels relationship vanishes in first differences).
- **Claiming OLS unbiasedness with a lagged dependent variable**: Cov(y_t, u_t) = Var(u_t) > 0, so TS.3 fails; only consistency holds, and β̂₁ is biased down when ρ₁ near 1 in small samples.
- **Confusing trend with unit root**: adding a time trend to a random walk (or differencing a trend-stationary series) mistreats the dynamics; diagnose persistence separately from trend.
- **Forcing dynamic completeness on static/FDL models**: serial correlation in a Phillips curve or FDL model signals genuine dynamics of interest, not necessarily misspecification — test and correct (Ch 12) rather than redefining the model.
- **Computing ρ̂₁ on a trending series without detrending**: biases upward toward a false unit root finding.

## Key Equations & Formulas
Stable AR(1) variance and autocorrelation:
$$\sigma_y^2 = \sigma_e^2/(1-\rho_1^2), \qquad \operatorname{Corr}(y_t, y_{t+h}) = \rho_1^h$$

Random walk moments:
$$y_t = y_{t-1} + e_t, \quad \operatorname{Var}(y_t) = \sigma_e^2\, t, \quad \mathrm{E}(y_{t+h}|y_t) = y_t, \quad \operatorname{Corr}(y_t, y_{t+h}) = \sqrt{t/(t+h)}$$

First difference of an I(1) series is I(0):
$$\Delta y_t = y_t - y_{t-1} = e_t$$

Growth rate approximation:
$$\Delta \log(y_t) \approx (y_t - y_{t-1})/y_{t-1}$$

Minimal consistency condition (weaker than TS.3′):
$$\mathrm{E}(u_t) = 0, \quad \operatorname{Cov}(x_{tj}, u_t) = 0, \; j = 1,\dots,k$$

Dynamic completeness (implies TS.5′):
$$\mathrm{E}(y_t \mid \mathbf{x}_t, y_{t-1}, \mathbf{x}_{t-1}, \dots) = \mathrm{E}(y_t \mid \mathbf{x}_t)$$

Sequential exogeneity:
$$\mathrm{E}(u_t \mid \mathbf{x}_t, \mathbf{x}_{t-1}, \dots) = 0$$

Natural rate from the expectations-augmented Phillips curve (Δinf_t = β₀ + β₁unem_t + e_t):
$$\hat{\mu}_0 = \hat{\beta}_0/(-\hat{\beta}_1)$$

## Reference Tables

Asymptotic Gauss-Markov assumptions (summary table from the chapter):

| Assumption | Name | Statement |
|---|---|---|
| TS.1′ | Linearity and Weak Dependence | {(x_t, y_t)} stationary, weakly dependent, follows y_t = β₀ + β₁x_{t1} + … + β_kx_{tk} + u_t |
| TS.2′ | No Perfect Collinearity | No regressor constant or a perfect linear combination of others |
| TS.3′ | Zero Conditional Mean | Contemporaneous exogeneity: E(u_t \| x_t) = 0 |
| TS.4′ | Homoskedasticity | Contemporaneously homoskedastic: Var(u_t \| x_t) = σ² |
| TS.5′ | No Serial Correlation | E(u_t u_s \| x_t, x_s) = 0 for all t ≠ s |

Which assumptions buy what:

| Assumptions | Result |
|---|---|
| TS.1′–TS.3′ | OLS consistent (Theorem 11.1); not necessarily unbiased |
| TS.1′–TS.5′ | OLS asymptotically normal; usual SEs, t, F, LM valid (Theorem 11.2) |

Exogeneity hierarchy (strong → weak): strict (TS.3) ⇒ sequential ⇒ contemporaneous (TS.3′); dynamic completeness ⇒ sequential exogeneity; with y_{t−1} in x_t, dynamic completeness = sequential exogeneity.

Process guide:

| Process | Weakly dependent? | Treatment |
|---|---|---|
| MA(1), stable AR(1) (\|ρ₁\|<1), i.i.d. | Yes (I(0)) | Use in levels |
| Trend-stationary | Yes, after detrending | Include time trend, use levels |
| Random walk / unit root (with or without drift) | No (I(1)) | First difference; drop trend |

## Worked Example
**Example 11.5 — Expectations-augmented Phillips curve.** Question: is there a tradeoff between unanticipated inflation and cyclical unemployment? Model under adaptive expectations (inf_t^e = inf_{t−1}): Δinf_t = β₀ + β₁unem_t + e_t, expecting β₁ < 0. Data: PHILLIPS through 2006, n = 58. Estimates: Δinf̂_t = 2.82 (1.18) − 0.515 (0.202) unem_t, R² = 0.104, p ≈ 0.014. A one-point rise in unemployment lowers unanticipated inflation by over half a point — the tradeoff appears only in the change equation, unlike the static Phillips curve of Example 10.1 (slightly positive). Implied natural rate μ̂₀ = 2.82/0.515 ≈ 5.48, inside the conventional 5–6% range (SE via delta-method-type calculation: 0.577, 95% CI ≈ [4.35, 6.61]). Lesson: specifying expectations as inf^e = inf_{t−1} converts a levels tradeoff into a difference regression — exactly the fix for persistent inflation.

## Key Takeaways
1. Before trusting time series OLS, ask whether the series are weakly dependent — this, not stationarity per se, is the load-bearing assumption in TS.1′.
2. With lagged dependent variables, strict exogeneity is impossible; settle for consistency under TS.3′ and use large-sample inference.
3. ρ̂₁ near 1 (rule of thumb: > 0.9, detrended if trending) signals I(1): switch to first differences or growth rates.
4. First differencing kills two birds: it renders unit root series weakly dependent and removes linear trends.
5. In a dynamically complete model the errors are automatically serially uncorrelated; failure of dynamic completeness flags possible serial correlation for Ch 12 treatment.
6. First-difference estimates can overturn levels results (fertility example) — when series are highly persistent, put more faith in the differenced specification.
7. Usual t/F statistics are only *asymptotically* valid under TS.1′–TS.5′; exact finite-sample distributions require the full CLM set from Ch 10.

## Connects To
- **Ch 10**: TS.1–TS.6 and strict exogeneity; this chapter relaxes them to TS.1′–TS.5′ and contemporaneous exogeneity.
- **Ch 12**: testing and correcting serial correlation and heteroskedasticity (incl. dynamic forms) when TS.4′/TS.5′ fail.
- **Ch 18**: formal unit root tests (H₀: ρ₁ = 1), spurious regression, cointegration — the advanced treatment of I(1) variables in regression.
- **Efficient markets hypothesis**: AR(p) tests of predictability are direct applications of TS.3′ + Theorem 11.2.
