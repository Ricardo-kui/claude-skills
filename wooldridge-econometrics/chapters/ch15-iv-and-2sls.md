# Chapter 15: Instrumental Variables Estimation and Two Stage Least Squares

## Core Idea
When an explanatory variable is endogenous (omitted variables, measurement error, simultaneity), an instrumental variable that is exogenous — Cov(z, u) = 0 — and relevant — Cov(z, x) ≠ 0 — identifies the causal parameter via IV/2SLS. But exogeneity is untestable in the just-identified case, and weak or invalid instruments can make 2SLS worse than OLS.

## Frameworks Introduced
- **Instrumental Variables (IV) estimator**: $\hat\beta_1 = \frac{\sum_i (z_i-\bar z)(y_i-\bar y)}{\sum_i (z_i-\bar z)(x_i-\bar x)} = \hat\gamma_1/\hat\pi_1$ (ratio of two OLS slopes: reduced form ÷ first stage). Reduces to OLS when z = x.
  - When to use: simple regression $y = \beta_0 + \beta_1 x + u$ with $\text{Cov}(x,u) \neq 0$ and a credible z available.
  - How: verify relevance by regressing x on z (t test on $\pi_1$, check the *sign* makes economic sense); argue exogeneity from economic reasoning/natural experiments — never testable with OLS residuals.
- **Two Stage Least Squares (2SLS)**: use the first-stage fitted value $\hat y_2$ as the IV; equivalent to OLS of $y_1$ on $\hat y_2$ and exogenous regressors. The best linear combination of multiple instruments.
  - When to use: multiple regression with endogenous regressor(s), one or more excluded instruments.
  - How (Stata recipe): (1) first stage — `reg educ exper exper2 motheduc fatheduc`, joint F test on excluded IVs; (2) `ivregress 2sls lwage (educ = motheduc fatheduc) exper exper2, vce(robust)` — never run the second stage manually: manual SEs are invalid because the second-stage error contains $v_2$, not $u_1$; (3) `estat firststage`, `estat endogenous`, `estat overid` for diagnostics.
- **Stock–Yogo weak-instrument rule**: proceed with usual IV inference only if first-stage |t| > $\sqrt{10} \approx 3.2$ (one IV) or first-stage F > 10 on excluded instruments (not the overall F). With heteroskedasticity/serial correlation, Montiel Olea–Pflueger suggests F ≈ 20+.
- **Order condition for identification**: at least as many excluded exogenous variables as included endogenous explanatory variables — necessary, easy to check by counting. The sufficient **rank condition** underlies joint first-stage F tests.
- **Variable Addition Test (VAT) / control function for endogeneity**: regress $y_2$ on all exogenous variables, save residuals $\hat v_2$; add $\hat v_2$ to the structural OLS regression; t test on $\delta_1 = 0$. Reject → $y_2$ endogenous. Bonus: the OLS coefficients in this augmented regression are identical to the 2SLS estimates.
- **Overidentifying restrictions test**: regress 2SLS residuals $\hat u_1$ on all exogenous variables; $nR_1^2 \overset{a}{\sim} \chi^2_q$, q = (# outside instruments − # endogenous regressors). Rejection → at least one IV is invalid; passing gives only weak comfort.
- **IV for errors-in-variables**: use a second mismeasured proxy $z_1 = x_1^* + a_1$ as IV for $x_1 = x_1^* + e_1$, valid when $\text{Cov}(a_1, e_1) = 0$ (e.g., spouse-reported education, twin-reported schooling, two test scores).
- **IV after differencing (panel)**: first difference to remove $a_i$, then instrument $\Delta x$ (e.g., grant as IV for $\Delta$hrsemp). Lagged dependent variable panels require lags of y as IVs for $\Delta y_{i,t-1}$.

## Key Concepts
- **Structural equation**: the equation whose $\beta_j$ measure causal effects; contrast with reduced form.
- **Reduced form equation**: an endogenous variable written as a linear function of all exogenous variables (e.g., $y_2 = \pi_0 + \pi_1 z_1 + \dots + \pi_k z_k + v_2$).
- **Instrument exogeneity**: $\text{Cov}(z,u)=0$ — z has no partial effect on y and is uncorrelated with omitted factors; fundamentally untestable when just identified.
- **Instrument relevance**: $\text{Cov}(z,x)\neq 0$ — testable partial correlation in the first stage.
- **Exclusion restrictions**: the assumptions that $z_2, z_3, \dots$ do not appear in the structural equation and are uncorrelated with $u_1$.
- **Weak instruments**: low (but nonzero) z–x correlation; 2SLS stays biased and non-normal even in huge samples (Staiger–Stock 1997).
- **Just identified vs. overidentified**: exactly as many instruments as endogenous regressors (exogeneity untestable) vs. q extra instruments (q testable restrictions).
- **Intention-to-treat (ITT)**: $\gamma_k = \beta_1\pi_k$, the reduced-form effect of eligibility — effect of *offering* the program, not of participating; IV recovers the participation effect $\beta_1 = \gamma_k/\pi_k$.
- **Control function estimator**: adding $\hat v_2$ to the structural equation and running OLS renders $y_2$ exogenous; SEs valid only under $H_0: \delta_1 = 0$.
- **Natural experiment**: exogenous variation from an external event (draft lottery, quarter of birth via compulsory schooling laws, randomized eligibility) supplying instruments.

## Mental Models
- Think of 2SLS as purging: the first stage splits $y_2$ into $y_2^*$ (clean, uncorrelated with $u_1$) and $v_2$ (dirty); the second stage uses only the clean piece.
- Think of IV variance as OLS variance ÷ $R_{x,z}^2$: $\text{Avar}(\hat\beta_{1,IV}) = \sigma^2/(n\sigma_x^2\rho_{x,z}^2)$ vs. OLS $\sigma^2/(n\sigma_x^2)$. A weak first stage inflates SEs multiplicatively — consistency is bought with precision.
- Use the plim comparison when weighing IV vs. OLS: IV inconsistency = $\frac{\text{Corr}(z,u)}{\text{Corr}(z,x)}\cdot\frac{\sigma_u}{\sigma_x}$ vs. OLS = $\text{Corr}(x,u)\cdot\frac{\sigma_u}{\sigma_x}$. If Corr(z,x) = 0.2, Corr(z,u) must be under 1/5 of Corr(x,u) before IV even beats OLS on bias.
- Use "an estimator is a rule for combining data" when language slips: there is no "IV model" — there is a model, and a choice of estimation method.

## Anti-patterns
- **Testing exogeneity with OLS residuals**: correlating z with $\hat u$ from an OLS fit proves nothing — the residuals are built on the inconsistent OLS coefficients; likewise an insignificant z added to the OLS regression is uninformative.
- **Running the two stages by hand**: second-stage OLS standard errors and test statistics are invalid; always use the software's 2SLS/IV command.
- **Using an included regressor as an IV**: $z_1$ in the structural equation cannot instrument $y_2$; you need an *excluded* exogenous variable.
- **Reading goodness of fit after IV**: 2SLS R-squared can be negative and has no variance-decomposition interpretation; never use SSR/R² forms of F tests after 2SLS. OLS maximizing R² is irrelevant — IV targets the ceteris paribus effect.
- **Accepting a merely significant first stage**: rejecting $\pi_1 = 0$ at 5% is not enough; weak instruments distort inference even at large n. Apply the Stock–Yogo thresholds.
- **Piling on instruments**: adding IVs improves asymptotic efficiency only if they are truly exogenous; many weak instruments (Angrist–Krueger quarter-of-birth dummies) can badly bias 2SLS even with hundreds of thousands of observations (Bound–Jaeger–Baker 1995).
- **Comfort in a passed overid test**: instruments chosen by similar reasoning (motheduc, fatheduc) can be similarly invalid and produce similar, jointly inconsistent estimates.
- **Using lagged dependent variables as IVs after quasi-differencing**: the AR(1)-correction instruments must be strictly exogenous; lagged y fails.

## Key Equations & Formulas
Instrument conditions and IV estimator:
$$\text{Cov}(z,u)=0,\quad \text{Cov}(z,x)\neq 0;\qquad \hat\beta_1 = \frac{\text{Cov}(z,y)}{\text{Cov}(z,x)}$$
Asymptotic variance of IV (homoskedasticity $E(u^2|z)=\sigma^2$):
$$\text{Avar}(\hat\beta_1) = \frac{\sigma^2}{n\sigma_x^2\rho_{x,z}^2} = \frac{\hat\sigma^2}{SST_x\cdot R_{x,z}^2}$$
Inconsistency comparison (IV vs. OLS):
$$\text{plim}\,\hat\beta_{1,IV} = \beta_1 + \frac{\text{Corr}(z,u)}{\text{Corr}(z,x)}\cdot\frac{\sigma_u}{\sigma_x};\qquad \text{plim}\,\hat\beta_{1,OLS} = \beta_1 + \text{Corr}(x,u)\cdot\frac{\sigma_u}{\sigma_x}$$
First stage (single endogenous regressor): $y_2 = \pi_0 + \pi_1 z_1 + \dots + \pi_{k-1}z_{k-1} + \pi_k z_k + v_2$, identification requires $\pi_k \neq 0$ (partial correlation).
2SLS asymptotic variance (multicollinearity amplifier):
$$\text{Avar}(\hat\beta_1) \approx \sigma^2\big/\left[\widehat{SST}_2\left(1-\hat R_2^2\right)\right]$$
Overidentification test: $nR_1^2 \overset{a}{\sim}\chi^2_q$ from regressing 2SLS residuals on all exogenous variables.
AR(1) test after 2SLS: re-estimate by 2SLS adding lagged residual $\hat u_{t-1}$ as its own instrument; t test on $\hat\rho$. Correction uses quasi-differenced variables $\tilde x_{tj} = x_{tj} - \hat\rho\, x_{t-1,j}$ and instruments $\tilde z_{tj}$.

## Reference Tables

**Diagnostic test map:**

| Test | Null | Statistic | Remedy if rejected |
|---|---|---|---|
| First-stage relevance | $\pi_k = 0$ (excluded IVs) | t (one IV) or F; need \|t\|>3.2, F>10 | Find stronger instruments; do not proceed |
| Endogeneity (VAT/Hausman) | $\delta_1 = 0$: $y_2$ exogenous | t on $\hat v_2$ added to structural OLS | Use 2SLS; if not rejected, prefer OLS (more efficient) |
| Overidentifying restrictions | all IVs uncorrelated with $u_1$ | $nR_1^2 \sim \chi^2_q$ | At least one IV invalid; rethink instrument set |
| Heteroskedasticity after 2SLS | homoskedasticity | F on joint significance in $\hat u^2$ on all z | Robust SEs; weighted 2SLS if variance form known |
| AR(1) serial correlation after 2SLS | $\rho = 0$ | t on $\hat u_{t-1}$ (2SLS re-run) | Serial-correlation-robust SEs or quasi-differenced 2SLS |

**OLS vs. 2SLS:**

| | OLS | 2SLS |
|---|---|---|
| Consistent when | $\text{Cov}(x,u)=0$ | IV exogeneity + relevance hold |
| Asymptotic variance | $\sigma^2/SST_x$ | $\sigma^2/(SST_x R_{x,z}^2)$ — always larger |
| Small-sample bias | — | Essentially never unbiased when actually needed; prefer large n |
| R² interpretation | variance share explained | none; can be negative |

## Worked Example
**Return to education for working women (MROZ, n = 428).** Question: causal return of an extra year of schooling to log(wage), with ability omitted into u. OLS: $\widehat{\log(wage)} = -0.185 + 0.109\,educ$ (se 0.014) → 11% return, but upward-biased if educ correlates with ability. Instrument: father's education (fatheduc), maintained uncorrelated with u. First stage: $\widehat{educ} = 10.24 + 0.269\,fatheduc$, t = 9.28 — relevance confirmed, sign sensible. IV estimate: 0.059 (se 0.035) — barely half the OLS estimate, consistent with omitted ability bias, but the SE is 2.5× larger and the IV confidence interval contains the OLS estimate, so the difference is not statistically established. With motheduc + fatheduc as two IVs (first-stage F = 124.76, far above 10), 2SLS gives 0.061 (se 0.031); the overidentification test ($nR_1^2 = 0.385$, p = 0.535) does not reject instrument exogeneity, and the endogeneity VAT (t = 1.67 on $\hat v_2$) shows only moderate evidence that educ is endogenous — so both OLS and 2SLS should be reported. Lesson: IV trades a large precision loss for consistency, and the data often cannot statistically separate the two estimates.

## Key Takeaways
1. IV consistency rests on two pillars — exogeneity (argue, cannot test) and relevance (always test via the first stage, checking sign and magnitude, not just significance).
2. Always report the first stage and apply Stock–Yogo: |t| > 3.2 or F > 10 (F ≈ 20+ under heteroskedasticity); a weak instrument amplifies even small exogeneity violations into large bias.
3. Never compute 2SLS manually stage-by-stage — use the package's IV command for valid standard errors (`ivregress 2sls ... , vce(robust)`).
4. Test whether 2SLS is needed (VAT/control-function t test); if exogeneity is not rejected, OLS is preferred on efficiency grounds.
5. With surplus instruments, run the overidentification test — but treat a pass as weak evidence, since similarly-motivated IVs can be similarly invalid.
6. Adding instruments raises asymptotic efficiency only if they are exogenous; many weak instruments bias 2SLS even in very large samples.
7. IV extends cleanly to time series (test/correct AR(1) via lagged 2SLS residuals), pooled cross sections, and panels — difference first, then instrument the differenced endogenous variable.

## Connects To
- **Ch 9**: proxy variables and classical errors-in-variables — IV is the remedy when proxies fail or measurement error is present; a second mismeasurement is the natural IV.
- **Ch 13–14**: fixed effects and first differencing remove time-constant unobserved effects; IV handles remaining time-varying endogeneity after differencing.
- **Ch 8**: heteroskedasticity-robust inference and weighted estimation carry over to 2SLS.
- **Ch 12**: serial correlation testing and quasi-differencing (Prais–Winsten first-period transformation) extend to time-series 2SLS.
- **Ch 16**: simultaneous equations models — structural/reduced form language and 2SLS as the workhorse estimator.
- **RCT noncompliance**: randomized eligibility as IV for actual participation — IV estimate = ITT ÷ first-stage compliance (Wald/LATE logic).
