# Chapter 12: Serial Correlation and Heteroskedasticity in Time Series Regressions

## Core Idea

Serial correlation in time series errors leaves OLS consistent (under TS.1′–TS.3′) but invalidates the usual OLS standard errors — which typically understate true sampling variation — so valid inference requires either Newey-West/HAC standard errors or feasible GLS (Cochrane-Orcutt/Prais-Winsten); and serial correlation found in a "fully dynamic" model signals dynamic misspecification, not just an inference problem.

## Frameworks Introduced

- **AR(1) error model**: $u_t = \rho u_{t-1} + e_t$ with stability condition $|\rho| < 1$; the benchmark model of serial correlation.
  - When to use: static and finite distributed lag models, where positive residual autocorrelation is nearly universal.
  - How: test $H_0\!: \rho = 0$ by regressing OLS residuals on lagged residuals; if rejected, apply HAC standard errors or FGLS quasi-differencing.
- **Newey-West (HAC) standard errors**: serial correlation–robust (and heteroskedasticity-robust) standard errors for OLS coefficients, requiring only contemporaneous exogeneity (TS.3′) for consistency.
  - When to use: default fix for static/FDL models; the only safe route when strict exogeneity fails or the model has lagged dependent variables.
  - How: (i) OLS of $y_t$ on regressors → save "se"$(\hat\beta_1)$, $\hat\sigma$, residuals $\hat u_t$; (ii) auxiliary regression of $x_{t1}$ on other regressors → residuals $\hat r_t$; form $\hat a_t = \hat r_t \hat u_t$; (iii) compute $\hat v$ from (12.12) with bandwidth $g$; (iv) se$(\hat\beta_1) = [\text{"se"}(\hat\beta_1)/\hat\sigma]^2\sqrt{\hat v}$. In Stata: `newey y x1 ... xk, lag(g)`.
- **Breusch-Godfrey test for AR(q)**: $LM = (n-q)R^2_{\hat u}$ from regressing $\hat u_t$ on $\hat u_{t-1},\dots,\hat u_{t-q}$ and all regressors; $LM \sim_a \chi^2_q$ (or use the joint F test).
  - When to use: general check for serial correlation, valid with or without strictly exogenous regressors (lagged dependent variables allowed).
  - How: run OLS → save residuals → auxiliary regression (12.28) → F or LM test. In Stata: `estat bgodfrey, lags(q)`.
- **Feasible GLS — Cochrane-Orcutt / Prais-Winsten**: quasi-difference the data as $\tilde y_t = y_t - \rho y_{t-1}$, $\tilde x_{tj} = x_{tj} - \rho x_{t-1,j}$ using $\hat\rho$; PW additionally rescales the first observation by $(1-\hat\rho^2)^{1/2}$, CO drops it.
  - When to use: only under **strict exogeneity** (TS.3, not just TS.3′) and substantial serial correlation, when efficiency matters — e.g., Newey-West standard errors too large to learn anything.
  - How: OLS → regress $\hat u_t$ on $\hat u_{t-1}$ → $\hat\rho$ → OLS on quasi-differenced equation (12.39), intercept $x_{t0} = 1-\hat\rho$; iterate until $\hat\rho$ stabilizes. In Stata: `prais y x1 ... xk` (add `, corc` for CO).
- **ARCH(1)**: $\mathrm{E}(u_t^2 \mid u_{t-1}) = \alpha_0 + \alpha_1 u_{t-1}^2$, $\alpha_0>0$, $0\le\alpha_1<1$ — dynamics in the conditional variance with serially uncorrelated errors.
  - When to use: financial returns, inflation volatility — anywhere squared residuals are autocorrelated but the errors themselves are not.
  - How: regress $\hat u_t^2$ on $\hat u_{t-1}^2$; a large t on $\hat\alpha_1$ signals ARCH; OLS point estimates remain fine (ARCH satisfies TS.1′–TS.5′ if Gauss-Markov holds) but WLS/ML exploiting the variance equation is more efficient.

## Key Concepts

- **Contemporaneous exogeneity (TS.3′)**: $\mathrm{E}(u_t \mid \mathbf{x}_t) = 0$; sufficient for OLS consistency, basis for the HAC approach.
- **Strict exogeneity (TS.3)**: $\mathrm{E}(u_t \mid \mathbf{X}) = 0$ — error uncorrelated with regressors in *all* time periods; required for OLS unbiasedness and for FGLS consistency.
- **Quasi-differenced data**: $\tilde z_t = z_t - \rho z_{t-1}$; the GLS transformation that purges AR(1) errors.
- **Truncation lag (bandwidth) $g$**: controls how much autocovariance enters the Newey-West variance; rules of thumb: $g \approx \text{int}(4(n/100)^{2/9})$, $\text{int}(\frac34 n^{1/3})$, or $\text{int}(n^{1/4})$; $g=1\text{–}2$ for annual, $4\text{–}8$ quarterly, $12\text{–}24$ monthly.
- **Durbin-Watson statistic**: $DW \approx 2(1-\hat\rho)$; valid only under full CLM assumptions, with an inconclusive region between $d_L$ and $d_U$.
- **Durbin's alternative test**: t test on $\hat u_{t-1}$ in the regression of $\hat u_t$ on $\hat u_{t-1}$ and all regressors — valid without strict exogeneity.
- **HAC standard error**: heteroskedasticity- and autocorrelation-consistent; (12.13) reduces to the Chapter 8 heteroskedasticity-robust SE when the lag terms are dropped.
- **Feasible GLS (FGLS)**: GLS with $\hat\rho$ plugged in; consistent and asymptotically more efficient than OLS under strict exogeneity, but no tractable finite-sample properties.
- **Volatility clustering**: large squared errors predict large future squared errors — the empirical pattern ARCH captures.

## Mental Models

- Think of serial correlation as an **inference problem first, a specification problem second**: OLS stays consistent under TS.3′, but the standard errors lie (usually too small, so t statistics too large).
- Think of positive $\rho$ + positively autocorrelated $x_t$ as the **variance-inflation combination**: the neglected term in (12.4) is positive, so the usual OLS variance understates the truth — "we think $\hat\beta_1$ is more precise than it actually is."
- Use **serial correlation as a misspecification detector** when the model includes lagged dependent variables: finding AR(1) in a supposedly complete dynamic model means you are missing lags, not that you need PW. (Adding AR(1) errors to an AR(1) conditional mean just produces an AR(2) in $y$.)
- Choose the fix by exogeneity strength: **weak exogeneity → OLS + Newey-West; strict exogeneity → FGLS for efficiency.** When in doubt, HAC.

## Anti-patterns

- **"OLS is inconsistent with lagged dependent variables and serial correlation"**: false as a blanket statement. OLS is consistent if $y_{t-1}$ fully captures the conditional mean (TS.3′ holds); inconsistency arises only when you impose an AR(1) error structure on top of an already-complete dynamic mean — which is a misspecification, remedied by adding $y_{t-2}$.
- **Using Cochrane-Orcutt/Prais-Winsten without strict exogeneity**: FGLS requires $\mathrm{Cov}[(x_{t-1}+x_{t+1}), u_t]=0$ in addition to contemporaneous exogeneity; with lagged dependent variables or feedback from $u_t$ to future $x$, FGLS is inconsistent while OLS is not.
- **Interpreting large OLS–FGLS differences as "FGLS is better"**: divergence usually means the FGLS exogeneity conditions fail — OLS is then the consistent one. FGLS with $\hat\rho \approx 0.8$ is close to first-differencing, so the "difference" may just signal a levels relationship that does not exist.
- **Using the t test (12.20) or Durbin-Watson when regressors are not strictly exogenous**: invalid even asymptotically; use regression (12.24) including all regressors instead.
- **Applying heteroskedasticity tests before handling serial correlation**: serially correlated errors invalidate Breusch-Pagan/White tests; test for serial correlation first (with a heteroskedasticity-robust statistic), correct, then test for heteroskedasticity.
- **Throwing out R² because of serial correlation**: with stationary, weakly dependent data, $R^2$ and $\bar R^2$ still consistently estimate the population R-squared.
- **Trusting Newey-West in small samples with heavy autocorrelation**: poorly behaved even at $n \approx 100$ and sensitive to $g$ — consider FGLS (if exogeneity is credible) or differencing.
- **"If errors contain ARCH, they must be serially correlated"**: false — squared errors are autocorrelated; the errors themselves need not be.

## Key Equations & Formulas

AR(1) errors: $u_t = \rho u_{t-1} + e_t$, $|\rho|<1$, $\mathrm{Var}(u_t) = \sigma_e^2/(1-\rho^2)$

OLS variance under AR(1) (why usual SEs fail):
$$\mathrm{Var}(\hat\beta_1) = \sigma^2/\mathrm{SST}_x + 2(\sigma^2/\mathrm{SST}_x^2)\sum_{t=1}^{n-1}\sum_{j=1}^{n-t}\rho^j x_t x_{t+j}$$

Newey-West variance kernel, with $\hat a_t = \hat r_t \hat u_t$:
$$\hat v = \sum_{t=1}^n \hat a_t^2 + 2\sum_{h=1}^g [1-h/(g+1)]\Big(\sum_{t=h+1}^n \hat a_t \hat a_{t-h}\Big), \qquad \text{se}(\hat\beta_1) = [\text{"se"}(\hat\beta_1)/\hat\sigma]^2\sqrt{\hat v}$$

Durbin-Watson:
$$DW = \frac{\sum_{t=2}^n (\hat u_t - \hat u_{t-1})^2}{\sum_{t=1}^n \hat u_t^2} \approx 2(1-\hat\rho)$$

Breusch-Godfrey LM:
$$LM = (n-q)R^2_{\hat u} \sim_a \chi^2_q$$

Prais-Winsten first-observation transform: $\tilde y_1 = (1-\rho^2)^{1/2} y_1$; quasi-difference for $t\ge2$: $\tilde y_t = y_t - \rho y_{t-1}$

FGLS consistency requirement beyond $\mathrm{Cov}(x_t,u_t)=0$:
$$\mathrm{Cov}\big[(x_{t-1}+x_{t+1}),\, u_t\big] = 0$$

ARCH(1): $\mathrm{E}(u_t^2 \mid u_{t-1}) = \alpha_0 + \alpha_1 u_{t-1}^2$

Combined heteroskedasticity + AR(1): $u_t = \sqrt{h_t}\,v_t$, $v_t = \rho v_{t-1} + e_t$ → divide through by $\sqrt{h_t}$, then apply CO/PW.

## Reference Tables

Test → null → statistic → remedy:

| Test | $H_0$ | Statistic | Regressor requirement | Remedy if rejected |
|---|---|---|---|---|
| Residual t test (12.20) | $\rho=0$ in AR(1) | t on $\hat u_{t-1}$, $\hat u_t$ on $\hat u_{t-1}$ | Strict exogeneity | HAC SEs or FGLS |
| Durbin-Watson | $\rho=0$ vs $\rho>0$ | $DW$; reject if $DW<d_L$, inconclusive $d_L \le DW \le d_U$ | Full CLM, strict exogeneity | same |
| Durbin's alternative (12.24) | $\rho=0$ | t on $\hat u_{t-1}$, regression includes all $x_{tj}$ | Any (lagged dep. var. OK) | HAC SEs; respecify dynamics |
| Breusch-Godfrey AR(q) (12.28) | $\rho_1=\dots=\rho_q=0$ | F on $\hat u_{t-1}\dots\hat u_{t-q}$, or $LM=(n-q)R^2_{\hat u}\sim\chi^2_q$ | Any | HAC with $g \ge q$; FGLS for AR(q) |
| Seasonal SC | $\rho_4=0$ (quarterly), $\rho_{12}=0$ (monthly) | t on $\hat u_{t-4}$ / $\hat u_{t-12}$ | t version: strict; with regressors: general | HAC with larger $g$ |
| Breusch-Pagan/White (Ch. 8) | $\delta_1=\dots=\delta_k=0$ in $u_t^2$ equation | F or LM on $\hat u_t^2$ regression | Errors serially uncorrelated | Heteroskedasticity-robust SEs; WLS |
| ARCH test (12.51) | $\alpha_1=0$ | t on $\hat u_{t-1}^2$ in $\hat u_t^2$ regression | Mean model complete | WLS/ML on variance eq.; robust SEs valid anyway |

OLS vs FGLS:

| | OLS + Newey-West | FGLS (CO/PW) |
|---|---|---|
| Exogeneity needed | Contemporaneous (TS.3′) | Strict (TS.3) + $\mathrm{Cov}[(x_{t-1}+x_{t+1}),u_t]=0$ |
| Lagged dep. var. | OK | No |
| Efficiency | Less efficient if SC present | Asymptotically efficient if AR model right |
| Inference validity | Robust to arbitrary SC + heterosk. | Valid only if AR model right; fix: HAC on transformed eq. |
| Bandwidth choice | Yes ($g$) | No |

## Worked Example

**Puerto Rican minimum wage (Examples 12.1, 12.3).** Question: does the minimum wage coverage variable reduce the Puerto Rican employment rate? Model: $\log(\text{prepop}_t)$ on $\log(\text{mincov})$, $\log(\text{usgnp})$, $\log(\text{prgnp})$, and a linear trend, annual data. OLS elasticity $\hat\beta_1 = -0.2123$ with usual SE $0.0402$, $\hat\sigma = 0.0328$. Testing serial correlation without assuming strict exogeneity (regression of $\hat u_t$ on $\hat u_{t-1}$ + all regressors): $\hat\rho = 0.481$, $t = 2.89$, $p = 0.007$ — strong AR(1). Newey-West with $g=2$ gives $\hat v = 0.000805$, so se$(\hat\beta_1) = (0.0402/0.0328)^2\sqrt{0.000805} \approx 0.0426$ — only ~6% larger than OLS, HAC t ≈ −4.98, still highly significant. Interpretation: the estimated elasticity survives serial-correlation-robust inference; note that sizable residual autocorrelation need not move the robust SE much, because it is the autocorrelation of $\hat a_t = \hat r_t\hat u_t$ that matters, coefficient by coefficient.

## Key Takeaways

1. Serial correlation invalidates OLS standard errors, t, and F statistics — but not consistency of $\hat\beta_j$ under contemporaneous exogeneity, and not $R^2$ under stationarity.
2. With positive $\rho$ and positively autocorrelated regressors (the common case), usual OLS SEs understate true variance: significance claims are overstated.
3. Default modern practice: OLS + Newey-West HAC standard errors; choose $g$ by data frequency, and report sensitivity to $g$.
4. Test first: Breusch-Godfrey/Durbin's alternative is cheap and works with lagged dependent variables; a rejection in a dynamic model usually means add lags, not apply PW.
5. Reserve Cochrane-Orcutt/Prais-Winsten for strictly exogenous regressors; if OLS and FGLS differ materially, suspect the FGLS exogeneity requirement, and prefer OLS.
6. Wrong SC model under FGLS does not destroy consistency — fix inference by applying Newey-West to the quasi-differenced equation.
7. With $\hat\rho$ near 1 or suspected unit roots, first-difference the equation: differencing kills both serial correlation and unit roots, but changes the parameter being estimated.

## Connects To

- **Ch 8**: heteroskedasticity-robust inference and WLS — HAC nests the Ch 8 robust SE; the "wrong variance model + robust SEs" logic is identical.
- **Ch 10**: TS.1–TS.6 Gauss-Markov assumptions for time series; Ch 12 is about what fails when TS.5 (no serial correlation) fails.
- **Ch 11**: TS.1′–TS.5′, weak dependence, contemporaneous exogeneity — the consistency basis for OLS + HAC; differencing of I(1) series.
- **Ch 18**: unit roots, cointegration, and forecasting — the reason $\hat\rho \approx 1$ points to differencing rather than FGLS.
- **ARCH/GARCH in empirical finance**: volatility modeling extension of Ch 12's ARCH(1).
