# Chapter 18: Advanced Time Series Topics

## Core Idea
When series are highly persistent (near or at a unit root), standard OLS inference breaks down — t statistics explode and R² becomes meaningless. The toolkit: unit-root tests to diagnose I(1), cointegration to know when a levels regression is still informative, error correction models for short-run dynamics around a long-run equilibrium, out-of-sample forecast evaluation, and single-unit event-study / synthetic-control designs for interventions.

## Frameworks Introduced
- **Infinite distributed lag (IDL) model**: $y_t = \alpha + \delta_0 z_t + \delta_1 z_{t-1} + \dots + u_t$, with $\delta_j \to 0$. The **long-run propensity** $LRP = \sum_j \delta_j$ measures the effect of a permanent one-unit increase in z.
  - When to use: long-run effects of a policy variable (money growth on inflation) without arbitrarily truncating lags.
  - How: restrict the $\delta_j$. **Geometric (Koyck) DL**: $\delta_j = \gamma\rho^j$, giving the estimable form $y_t = \alpha_0 + \gamma z_t + \rho y_{t-1} + v_t$. OLS is inconsistent here because $v_t = u_t - \rho u_{t-1}$ correlates with $y_{t-1}$; either use IV with instruments $(z_t, z_{t-1})$ under strict exogeneity (18.5), or assume $u_t = \rho u_{t-1} + e_t$ with the same $\rho$, making the equation dynamically complete so OLS is consistent. **Rational distributed lag (RDL)**: add $\gamma_1 z_{t-1}$ to allow the impact propensity to differ in sign from later lag coefficients; $LRP = (\gamma_0+\gamma_1)/(1-\rho)$.
- **Dickey-Fuller / augmented DF test**: regression $\Delta y_t = \alpha + \theta y_{t-1} + \gamma_1\Delta y_{t-1} + \dots + e_t$; H₀: θ = 0 (unit root, I(1)) vs H₁: θ < 0 (I(0)). The t statistic on $\hat\theta$ follows the Dickey-Fuller distribution, not standard normal — use Table 18.2 critical values (add a linear time trend for trending series, Table 18.3).
  - When to use: before choosing between levels, differences, or detrending any persistent series.
  - How: lag length by data frequency (1–2 annual, ~12 monthly); t and F tests on the lagged changes are asymptotically standard, so use them to choose lag length. Failing to reject never means "accepting" a unit root — report $\hat\rho = 1+\hat\theta$ and judge persistence.
- **Engle-Granger cointegration test**: y and x (both I(1)) are cointegrated if $y_t - \beta x_t$ is I(0). If β is hypothesized (e.g. β = 1), DF-test the constructed spread. If β is unknown, estimate it by the static regression $y_t = \hat\alpha + \hat\beta x_t$ and DF-test the residuals $\hat u_t$, using Engle-Granger critical values (Tables 18.4/18.5, larger in magnitude than DF values).
  - When to use: deciding whether a levels regression between I(1) series is informative (long-run equilibrium) or spurious.
- **Leads and lags estimator**: $y_t = \alpha_0 + \beta x_t + \phi_0\Delta x_t + \phi_1\Delta x_{t-1} + \gamma_1\Delta x_{t+1} + \dots + e_t$. Augmenting the cointegrating regression with leads/lags of $\Delta x$ makes $x_t$ strictly exogenous, so the t statistic on $\hat\beta$ is approximately standard normal.
  - When to use: valid confidence intervals/tests on the cointegrating parameter (e.g. H₀: β = 1). Use a serial-correlation–robust SE if $e_t$ is autocorrelated.
- **Error correction model (ECM)**: $\Delta y_t = \alpha_0 + \gamma_0\Delta x_t + \delta(y_{t-1} - \beta x_{t-1}) + u_t$ with $\delta < 0$; the error correction term pulls y back toward equilibrium after overshooting.
  - How: **Engle-Granger two-step procedure** — (1) estimate β by OLS or leads-and-lags; (2) regress $\Delta y_t$ on $\Delta x_t$ lags and $\hat s_{t-1} = y_{t-1} - \hat\beta x_{t-1}$ by OLS. Preliminary estimation of β can be ignored asymptotically. ECMs are more parsimonious than VARs in levels for cointegrated systems.
- **Out-of-sample forecast evaluation**: estimate on the first n observations, save the last m, compute RMSE or MAE of one-step-ahead forecast errors; prefer the smallest. Beats in-sample fit (adjusted R²) for model choice because forecasting is inherently out-of-sample.
- **VAR and Granger causality**: model each series on lags of all series; z Granger causes y if $\mathrm{E}(y_t|I_{t-1}) \neq \mathrm{E}(y_t|J_{t-1})$ where $I$ includes past z and $J$ does not. Test = F test for joint significance of lagged z in an autoregression for y. Says nothing about contemporaneous causality or exogeneity.
- **Single-unit DID with trends / synthetic control**: collapse treated/control averages to one series $d\bar y_t = \bar y_{1t} - \bar y_{0t}$ and regress on $post_t$ (+ trend terms) with Newey-West SEs. Requires $d\bar y_t$ to be I(0) (DF-test it pre-intervention) and parallel trends; allow differential linear trends via equation (18.73). SCM chooses nonnegative donor weights summing to one to fit pre-intervention outcomes; SDID unifies DID and SC.

## Key Concepts
- **Long-run propensity (LRP)**: sum of all lag coefficients in a DL model; long-run change in E(y) from a permanent one-unit increase in z.
- **Martingale difference sequence (MDS)**: $\mathrm{E}(y_{t+1}|y_t, y_{t-1}, \dots) = 0$ — the past is useless for predicting the future (approximate model for stock returns).
- **Unit root**: AR(1) with ρ = 1; shocks have permanent effects and usual asymptotics fail.
- **Spurious regression problem**: regressing independent I(1) series yields t statistics that diverge (66% rejection at 5% level with n = 50; 85% with n = 250) and R² converging to a random variable.
- **Cointegration**: two I(1) series with an I(0) linear combination; they cannot drift arbitrarily far apart (long-run equilibrium).
- **Error correction term**: $\delta(y_{t-1} - \beta x_{t-1})$, $\delta < 0$, driving the system back to equilibrium.
- **Conditional vs unconditional forecast**: conditional assumes known future z; unconditional forecasts z first or, better, uses only lagged information.
- **Forecast error / interval**: $se(\hat e_{n+1}) = \{[se(\hat f_n)]^2 + \hat\sigma^2\}^{1/2}$; 95% interval $\hat f_n \pm 1.96\, se(\hat e_{n+1})$ — dominated by $\hat\sigma$.
- **Exponential smoothing**: $f_t = \alpha y_t + (1-\alpha) f_{t-1}$; suitable only for very specific series.
- **Granger causality**: predictability of y from past z beyond past y — not structural causality.
- **Synthetic control method (SCM)**: data-driven weighted average of donor units matching the treated unit's pre-intervention path; weights nonnegative, sum to one.

## Mental Models
- Use a DF/ADF test when deciding levels vs differences; think of I(1) as "shocks never die" — standard CLT-based inference is void.
- Think of cointegration as an economic leash: two I(1) series can wander, but the spread keeps returning to its mean. No leash → difference the data; leash → levels regression is informative.
- Think of the ECM as a thermostat: $\Delta y$ responds to current changes plus a correction proportional to last period's deviation from equilibrium.
- Judge forecasts only out-of-sample; think of adjusted R² as measuring explanation, RMSE/MAE as measuring prediction — they routinely disagree.

## Anti-patterns
- **OLS on the Koyck equation treating $y_{t-1}$ as exogenous**: $v_t = u_t - \rho u_{t-1}$ is correlated with $y_{t-1}$ (an MA(1) error with lagged dependent variable) — inconsistent estimates of γ and ρ.
- **Using standard normal critical values in a unit-root test**: rejects a true unit root far too often (use −2.86, not −1.65, at 5%).
- **Trusting "significant" levels regressions among trending/unit-root series**: t statistics explode and R² is meaningless unless the series are cointegrated.
- **Reading causality from Granger causality**: it is only incremental predictability; silent on contemporaneous exogeneity.
- **Choosing forecast models by in-sample fit**: better fit need not forecast better (the richer unemployment model lost in 2011 but won on 7-year out-of-sample RMSE).
- **Forecasting a random walk with drift using a linear trend**: error variance is $\sigma^2(t+h)$ instead of $\sigma^2 h$ — never extrapolate deterministic trends far for I(1) series.
- **DID on a persistent gap without checking**: if $d\bar y_t$ has a unit root, the DID estimate may be spurious; and a pre-treatment gap that is changing (not just nonzero) violates parallel trends.
- **Hand-picking controls to get a desired result**: SCM/SDID choose weights systematically; even then, donor pool and fit variables are researcher choices.

## Key Equations & Formulas
- IDL long-run propensity: $LRP = \delta_0 + \delta_1 + \delta_2 + \dots$; geometric DL: $LRP = \gamma/(1-\rho)$; RDL: $LRP = (\gamma_0+\gamma_1)/(1-\rho)$.
- Koyck estimating equation: $y_t = \alpha_0 + \gamma z_t + \rho y_{t-1} + v_t$, $v_t = u_t - \rho u_{t-1}$.
- (Augmented) Dickey-Fuller regression: $\Delta y_t = \alpha + \delta t + \theta y_{t-1} + \gamma_1\Delta y_{t-1} + \dots + \gamma_p\Delta y_{t-p} + e_t$; test H₀: θ = 0 with DF critical values; $\hat\rho = 1+\hat\theta$.
- Cointegrating regression: $y_t = \hat\alpha + \hat\beta x_t$; Engle-Granger test = (augmented) DF on residuals $\hat u_t$.
- Leads and lags estimator: $y_t = \alpha_0 + \beta x_t + \phi_0\Delta x_t + \phi_1\Delta x_{t-1} + \phi_2\Delta x_{t-2} + \gamma_1\Delta x_{t+1} + \gamma_2\Delta x_{t+2} + e_t$.
- Error correction model: $\Delta y_t = \alpha_0 + \gamma_0\Delta x_t + \delta(y_{t-1} - \beta x_{t-1}) + u_t$, $\delta < 0$.
- One-step forecast and interval: $\hat f_n = \hat\delta_0 + \hat\alpha_1 y_n + \hat\gamma_1 z_n$; $se(\hat e_{n+1}) = \{[se(\hat f_n)]^2 + \hat\sigma^2\}^{1/2}$.
- Out-of-sample criteria: $RMSE = (m^{-1}\sum_{h=0}^{m-1}\hat e_{n+h+1}^2)^{1/2}$; $MAE = m^{-1}\sum_{h=0}^{m-1}|\hat e_{n+h+1}|$.
- Multi-step AR(1) forecast: $\hat f_{n,h} = (1+\hat\rho+\dots+\hat\rho^{h-1})\hat\alpha + \hat\rho^h y_n$; $\mathrm{Var}(e_{t,h}) = \sigma^2[\rho^{2(h-1)}+\dots+1]$ (=$\sigma^2 h$ for a random walk).
- Single-unit DID: $d\bar y_t = \alpha + \beta\, post_t + \gamma(t-\bar t_{pre}) + \delta\, post_t(t-\bar t_{post}) + u_t$, Newey-West SEs; effect at exposure time $et$: $\hat\beta_0 + \hat\delta\cdot et$.

## Reference Tables

Unit-root / cointegration critical values (asymptotic):

| Significance level | 1% | 2.5% | 5% | 10% |
|---|---|---|---|---|
| Unit-root t test, no trend (Table 18.2) | −3.43 | −3.12 | −2.86 | −2.57 |
| Unit-root t test, linear trend (Table 18.3) | −3.96 | −3.66 | −3.41 | −3.12 |
| Engle-Granger, no trend (Table 18.4) | −3.90 | −3.59 | −3.34 | −3.04 |
| Engle-Granger, linear trend (Table 18.5) | −4.32 | −4.03 | −3.78 | −3.50 |

Test decision table:

| Test | Null | Test statistic | Remedy if rejected / not rejected |
|---|---|---|---|
| DF / ADF | H₀: θ = 0 (unit root) | t on $\hat\theta$, DF critical values | Reject → series I(0), use levels; fail → treat as I(1), difference or test cointegration |
| Engle-Granger | No cointegration | (A)DF t on residuals $\hat u_t$ | Reject → levels regression informative, build ECM; fail → regress in first differences |
| Granger causality | Lagged z jointly zero | F test in AR for y | Reject → include lagged z in forecasting model |

## Worked Example
**California smoking restrictions and cigarette sales (Example 18.11, SMOKING).** Question: did California's 1989 excise tax plus local smoking bans cut per-capita cigarette sales? Annual data 1970–2000; treated unit = CA, controls = CO, MT, NV, UT. Outcome: log sales; form $d\bar y_t = y_{CA,t} - \bar y_{0t}$. Pre-checks: pre-1989 AR(1) coefficient of $d\bar y_t$ ≈ 0.43 (far from one; DF strongly rejects a unit root), and the pre-treatment mean gap is 0.0034 ≈ 0 — the controls track CA closely. Basic DID (18.71) with NW(2) SEs: $\hat\beta = -0.299$ (t ≈ −5.25), about a 30% average post-law drop. Allowing differential trends (18.76): average effect −0.267, post-trend difference −0.0338 (large and significant); the immediate 1989 effect is −0.081. Tracing exposure time (Table 18.6): −0.115 in 1990, −0.284 in 1995, −0.453 in 2000 (≈ −36% after log correction). With midwestern controls (parallel trends visibly violated pre-1989), plain DID is misleading, but adding the trend terms (18.73) recovers essentially the same estimate (−0.261) — evidence the trend-adjusted specification, not the control pool, drives the result. ADH's synthetic control automates the weighting; SDID unifies the two.

## Key Takeaways
1. Always run a DF/ADF test before regressing persistent series in levels; never use standard normal critical values.
2. Failing to reject a unit root is not accepting one — report $\hat\rho$ and judge persistence, especially in small samples.
3. Regressing one I(1) series on another is spurious unless they are cointegrated; test with Engle-Granger before believing any levels result.
4. Cointegration implies an ECM: estimate β first (OLS or leads and lags), then run the dynamic regression in differences with the error correction term — inference on the second step is asymptotically unaffected by the first.
5. Evaluate forecasting models out-of-sample with RMSE/MAE, not adjusted R²; multiple-step-ahead forecast variances grow with the horizon (without bound for a random walk).
6. Never extrapolate linear trends far for I(1) series; forecast the difference and add the level instead.
7. Single-unit event studies work with enough pre/post periods: check that the treated–control gap is I(0) and trend-stationary pre-intervention, use Newey-West SEs, and let differential trends or synthetic controls rescue weak control groups.

## Connects To
- **Ch 10–12**: finite distributed lags, trends/seasonality, strict exogeneity (TS.3), serial correlation and Newey-West SEs — the baseline toolkit this chapter stress-tests under persistence.
- **Ch 11**: I(0)/I(1), weak dependence, dynamically complete models — the assumptions unit roots violate.
- **Ch 13**: DID and the parallel trends assumption — extended here to single treated units with long time series and trend violations.
- **Ch 15–16**: IV estimation — used to estimate the Koyck equation with instruments $(z_t, z_{t-1})$.
- **ARDL / bounds testing (Pesaran-Shin)**: the modern generalization of the leads-and-lags and ECM framework.
- **Johansen cointegration / VECM**: multi-variable extension of Engle-Granger when several cointegrating relations may exist.
- **Staggered DiD / synthetic control literature (ADH 2010, SDID)**: the modern causal-inference descendants of Section 18-6.
