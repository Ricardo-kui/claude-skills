# Chapter 17: Limited Dependent Variable Models and Sample Selection Corrections

## Core Idea
When y is binary, fractional, a count, corner-solution, censored, truncated, or observed only for a nonrandom subsample, the linear model fails in a specific, diagnosable way — match the data type to its MLE-based model (logit/probit, fractional logit, Poisson QMLE, Tobit, censored/truncated regression, Heckit) and report average partial effects, because raw coefficients in nonlinear models are not magnitudes.

## Frameworks Introduced
- **Binary response models (logit/probit)**: $P(y=1|\mathbf{x}) = G(\beta_0 + \mathbf{x}\beta)$, $G$ = logistic cdf $\Lambda(z)$ or standard normal cdf $\Phi(z)$; derived from the latent variable model $y^* = \beta_0 + \mathbf{x}\beta + e$, $y = 1[y^* > 0]$.
  - When to use: 0/1 outcomes (labor force participation, takeover) where the LPM's out-of-range fitted probabilities and constant partial effects are objectionable.
  - How: maximize the Bernoulli log-likelihood $\sum_i \{y_i\log G(\mathbf{x}_i\beta) + (1-y_i)\log[1-G(\mathbf{x}_i\beta)]\}$ (Stata: `logit y x` / `probit y x`); get APEs with `margins, dydx(*)`; test exclusions with `lrtest` or `test` (Wald).
- **Fractional response model (Papke–Wooldridge)**: same $G(\cdot)$ conditional mean for $y \in [0,1]$, estimated by Bernoulli quasi-MLE (QMLE).
  - When to use: shares/rates with mass at 0 or 1 (401(k) participation rate).
  - How: `glm y x, family(binomial) link(logit) robust` — robust SEs are mandatory since the Bernoulli variance is wrong by construction.
- **Exponential mean / Poisson regression**: $\mathrm{E}(y|\mathbf{x}) = \exp(\mathbf{x}\beta)$; Poisson QMLE consistent for $\beta$ even if y is not Poisson and not a count.
  - When to use: counts (arrests, patents) or any nonnegative/corner-solution outcome; coefficients read as semi-elasticities.
  - How: `poisson y x, robust`; inflate SEs for overdispersion under $\mathrm{Var}(y|\mathbf{x}) = \sigma^2\mathrm{E}(y|\mathbf{x})$ (or just use fully robust SEs); never `log(1+y)` instead.
- **Tobit model for corner solutions**: $y^* = \beta_0 + \mathbf{x}\beta + u$, $u|\mathbf{x} \sim \mathrm{Normal}(0,\sigma^2)$, $y = \max(0, y^*)$.
  - When to use: y piles up at zero with a broad range of positive values (hours worked, charitable giving) and the same mechanism governs participation and intensity.
  - How: `tobit y x, ll(0)`; report APEs on $\mathrm{E}(y|\mathbf{x})$ via `margins, dydx(*) predict(ystar(0,.))`; informally check the Tobit restriction by comparing Tobit $\hat\beta_j/\hat\sigma$ with probit coefficients on $1[y>0]$.
- **Censored normal regression**: $y_i = \beta_0 + \mathbf{x}_i\beta + u_i$, $u_i|\mathbf{x}_i,c_i \sim \mathrm{Normal}(0,\sigma^2)$, $w_i = \min(y_i, c_i)$ (right censoring).
  - When to use: data-collection censoring — top coding, durations still running at follow-up. $\beta_j$ interpreted as in a linear model.
  - How: `tobit logy x, ul(ul)` with censoring indicator; keep censored observations — never drop or treat as uncensored.
- **Truncated normal regression**: density $g(y|\mathbf{x}_i,c_i) = f(y|\mathbf{x}_i\beta,\sigma^2)/F(c_i|\mathbf{x}_i\beta,\sigma^2)$, $y \le c_i$.
  - When to use: units outside the sampling rule are excluded entirely (sample restricted to income below a threshold); OLS on the truncated sample is biased toward zero.
  - How: `truncreg y x, ll(#)` or `ul(#)`.
- **Heckit two-step selection correction**: selection $s = 1[\mathbf{z}\gamma + v \ge 0]$, outcome $y = \mathbf{x}\beta + u$, $\mathrm{E}(u|\mathbf{x},\mathbf{z})=0$, $(u,v)$ jointly normal with $\mathrm{E}(u|v) = \rho v$, giving $\mathrm{E}(y|\mathbf{z}, s=1) = \mathbf{x}\beta + \rho\lambda(\mathbf{z}\gamma)$.
  - When to use: incidental truncation — y observed only because of another variable's outcome (wage offers only for workers).
  - How: (i) probit of $s_i$ on $\mathbf{z}_i$ using all n observations, compute $\hat\lambda_i = \lambda(\mathbf{z}_i\hat\gamma)$; (ii) OLS of $y_i$ on $\mathbf{x}_i, \hat\lambda_i$ on the selected sample. t test on $\hat\lambda$ tests $\mathrm{H}_0: \rho = 0$ (no selection bias). Requires an exclusion restriction: some $z_h \notin \mathbf{x}$ affecting selection but not y. Stata: `heckman y x, select(z)`.

## Key Concepts
- **Limited dependent variable (LDV)**: a dependent variable restricted in range — binary, fractional, count, corner-solution, censored, or truncated.
- **Latent variable model**: unobserved $y^*$ generating observed y through a threshold rule; motivates logit/probit/Tobit but $y^*$ rarely has units.
- **Quasi-maximum likelihood estimation (QMLE)**: maximizing a possibly misspecified log-likelihood that still yields consistent mean parameters (Bernoulli QMLE for fractional y, Poisson QMLE for nonnegative y).
- **Average partial effect (APE) / average marginal effect (AME)**: sample average of individual partial effects; preferred summary of magnitudes in nonlinear models.
- **Partial effect at the average (PEA)**: partial effect evaluated at covariate means; problematic with discrete or nonlinearly-entered regressors.
- **Likelihood ratio statistic**: $LR = 2(\mathcal{L}_{ur} - \mathcal{L}_r) \overset{a}{\sim} \chi^2_q$; the nonlinear-model analog of the F test (log-likelihoods are negative — preserve the signs).
- **Pseudo R-squared**: McFadden's $1 - \mathcal{L}_{ur}/\mathcal{L}_0$, or squared correlation between $y_i$ and fitted $\hat y_i$; fit is secondary to ceteris paribus effects.
- **Inverse Mills ratio**: $\lambda(c) = \phi(c)/\Phi(c)$; the omitted term $\rho\lambda(\mathbf{z}\gamma)$ in selected-sample regressions.
- **Corner solution response**: outcome piles at zero with a continuum of positive values — a feature of the population, not a data problem.
- **Censoring vs truncation**: censoring — x observed, y recorded only up to a threshold; truncation — units outside the rule excluded from the sample entirely.
- **Incidental truncation**: y missing due to the outcome of another variable (selection equation), corrected by Heckit.
- **Exogenous vs endogenous sample selection**: selection depending only on exogenous x (or random) leaves OLS consistent; selection depending on u does not.

## Mental Models
- **Use the data type to pick the model, not habit.** Binary → logit/probit; fractional → fractional logit QMLE; count/nonnegative → exponential mean with Poisson QMLE; corner at zero → Tobit (or two-part); censored/truncated → censored/truncated MLE; nonrandom selection → Heckit.
- **Think of the coefficient as a sign and significance carrier only.** In any nonlinear model, $\hat\beta_j$ gives the direction and (via its t statistic) significance; the magnitude lives in the APE, which multiplies $\hat\beta_j$ by a data-dependent scale factor.
- **Think of selection bias as omitted-variable bias.** With $\rho \ne 0$, the selected-sample regression omits $\rho\lambda(\mathbf{z}\gamma)$, which is correlated with x — the Heckit is an omitted-variables fix, and its test is the t statistic on $\hat\lambda$.
- **Use OLS as the benchmark, not the answer.** OLS coefficients on the full sample often approximate APEs surprisingly well; run the nonlinear model to check diminishing effects and out-of-range predictions, then compare APEs against OLS.

## Anti-patterns
- **Reading logit/probit/Tobit coefficients as marginal effects**: they index the latent index, not the probability or observed mean; always convert to APEs (or PEAs for quick summaries).
- **Using $\log(1+y)$ for nonnegative y with zeros**: it fixes neither nonnegativity nor the zero problem, and results are not invariant to rescaling y; use the exponential mean with Poisson QMLE instead.
- **Applying Tobit to censored data (or vice versa)**: corner solutions are population features; censoring is a data-collection artifact — the likelihoods and coefficient interpretations differ.
- **OLS on only the $y>0` subsample of a corner-solution outcome**: $\mathrm{E}(y|y>0,\mathbf{x}) = \mathbf{x}\beta + \sigma\lambda(\mathbf{x}\beta/\sigma) \ne \mathbf{x}\beta$, so OLS on the positives is inconsistent for $\beta$.
- **Dropping censored observations or treating censored values as exact**: throws away information or shrinks coefficients toward zero; use censored MLE with the known thresholds.
- **Running Heckit without an exclusion restriction**: with $\mathbf{z} = \mathbf{x}$, identification rests solely on the nonlinearity of $\lambda(\cdot)$; selection becomes indistinguishable from functional-form misspecification.
- **Reporting percent correctly predicted overall only**: high overall rates can hide zero predictive power for the rare outcome; report $\hat q_0$ and $\hat q_1$ separately.
- **Using Poisson MLE standard errors without the overdispersion adjustment**: $\mathrm{Var}(y|\mathbf{x}) = \mathrm{E}(y|\mathbf{x})$ rarely holds; scale SEs by $\hat\sigma$ or use fully robust SEs.

## Key Equations & Formulas
$$\mathrm{P}(y=1|\mathbf{x}) = G(\beta_0 + \mathbf{x}\beta), \quad \Lambda(z) = \frac{\exp(z)}{1+\exp(z)}, \quad \Phi(z) = \int_{-\infty}^{z}\phi(v)\,dv$$
$$\frac{\partial p(\mathbf{x})}{\partial x_j} = g(\beta_0 + \mathbf{x}\beta)\,\beta_j$$
$$\ell_i(\beta) = y_i\log[G(\mathbf{x}_i\beta)] + (1-y_i)\log[1-G(\mathbf{x}_i\beta)]$$
$$LR = 2(\mathcal{L}_{ur} - \mathcal{L}_r) \overset{a}{\sim} \chi^2_q$$
$$\text{APE scale factor (binary/fractional)}: \; n^{-1}\sum_{i=1}^{n} g(\hat\beta_0 + \mathbf{x}_i\hat\beta); \qquad \mathrm{E}(y|\mathbf{x}) = \exp(\mathbf{x}\beta), \;\; \%\Delta\mathrm{E}(y|\mathbf{x}) \approx 100\beta_j \Delta x_j$$
$$\mathrm{E}(y|y>0,\mathbf{x}) = \mathbf{x}\beta + \sigma\lambda(\mathbf{x}\beta/\sigma), \qquad \frac{\partial\mathrm{E}(y|\mathbf{x})}{\partial x_j} = \beta_j\,\Phi(\mathbf{x}\beta/\sigma)$$
$$\mathrm{E}(y|\mathbf{z}, s=1) = \mathbf{x}\beta + \rho\lambda(\mathbf{z}\gamma), \qquad \lambda(c) = \phi(c)/\Phi(c)$$

## Reference Tables

| Outcome type | Model | Estimator | Key validity condition | Stata |
|---|---|---|---|---|
| Binary | Logit / probit | MLE | Correct $G(\cdot)$, correct index | `logit` / `probit` |
| Fractional $[0,1]$ | Fractional logit | Bernoulli QMLE | Correct conditional mean; robust SEs | `glm, family(binomial) link(logit) robust` |
| Count / nonnegative | Exponential mean | Poisson QMLE | Correct conditional mean only; adjust SEs for overdispersion | `poisson, robust` |
| Corner at zero | Tobit | MLE | Normality + homoskedasticity of latent u | `tobit, ll(0)` |
| Censored y (top code, durations) | Censored normal regression | MLE | Normality + homoskedasticity; thresholds known | `tobit, ul()` |
| Truncated sample | Truncated normal regression | MLE | Normality + homoskedasticity; MLR.2 fails | `truncreg` |
| Incidental truncation | Heckit two-step | Probit + OLS with $\hat\lambda$ | Exclusion restriction; joint normality of (u,v) | `heckman` |

| Diagnostic | Null | Statistic | Remedy if rejected |
|---|---|---|---|
| Exclusion restrictions (logit/probit/Tobit/Poisson) | q coefficients = 0 | $LR = 2(\mathcal{L}_{ur}-\mathcal{L}_r) \sim \chi^2_q$ or Wald | Keep the variables |
| Tobit single-mechanism restriction | Tobit $\beta_j/\sigma$ = probit $\gamma_j$ | Compare $\hat\beta_j/\hat\sigma$ with probit coefficients | Hurdle / two-part model |
| Overdispersion (Poisson) | $\sigma^2 = 1$ in $\mathrm{Var}(y|\mathbf{x}) = \sigma^2\mathrm{E}(y|\mathbf{x})$ | $\hat\sigma$ from residuals | Scale SEs by $\hat\sigma$; quasi-LR |
| Sample selection bias | $\rho = 0$ | t statistic on $\hat\lambda_i$ in (17.55) | Use Heckit estimates or full MLE |

## Worked Example
**Example 17.6 — Wage offer equation for married women (MROZ).** Question: how do educ, exper, exper² affect log(wage), and is the 428-of-753 working subsample selected? Data/model: wage offers observed only for workers; selection equation adds variables affecting participation but not the offered wage (exclusion restriction). Estimates: OLS on the 428 workers gives educ 0.108 (0.014); Heckit adds $\hat\lambda$ from the participation probit, giving educ 0.109 (0.016), with t = 0.239 on $\hat\lambda$. Interpretation: $\mathrm{H}_0: \rho = 0$ not rejected — no evidence of sample selection bias here, so OLS on the selected sample stands; had $\hat\lambda$ been significant, the Heckit coefficients (or full MLE) would replace OLS. Companion Example 17.5 (recidivism, RECID): 893 of 1,445 durations censored; censored normal regression on log(durat) shows workprg −0.063 (0.120) — no effect — while OLS treating censored durations as exact shrinks all coefficients toward zero (priors −0.137 → −0.059).

## Key Takeaways
1. Diagnose the dependent variable first: binary, fractional, count, corner, censored, truncated, or selected — each has a matched estimator, and OLS fails differently in each case.
2. MLE is consistent, asymptotically normal, and efficient under general conditions; t tests, Wald, and LR ($\chi^2_q$) work as usual — LR needs both models estimated.
3. Never interpret nonlinear-model coefficients as magnitudes: report APEs; use PEAs only as quick scale factors, and discrete-change formulas (17.8/17.17) for dummies.
4. Poisson QMLE needs only a correctly specified conditional mean for consistency — robust to non-Poisson and non-count y — but SEs require the overdispersion or fully robust adjustment.
5. Tobit's restriction is that one mechanism drives both participation and intensity; if the probit comparison $\hat\beta_j/\hat\sigma$ disagrees, move to a hurdle/two-part model.
6. Censoring and truncation attack the sample, not the population; both censored and truncated MLEs collapse under nonnormality or heteroskedasticity — a real cost versus OLS on uncensored data.
7. Sample selection is ignorable when selection depends only on exogenous variables (or is random); correct it with Heckit only when you have a credible exclusion restriction, and test first with the t statistic on $\hat\lambda$.

## Connects To
- **Ch 7**: the LPM (Section 7-5) is the benchmark logit/probit improve upon; percent correctly predicted carries over.
- **Ch 8**: heteroskedasticity motivates robust/Adjusted SEs for QMLE; MLE automatically accounts for $\mathrm{Var}(y|\mathbf{x})$.
- **Ch 9**: Section 9-5's exogenous vs endogenous selection is generalized systematically here.
- **Ch 15–16 (IV/2SLS)**: consistency of 2SLS on selected samples requires $\mathrm{E}(sz_h u) = 0$; selection plus endogenous regressors needs joint corrections.
- **Ch 19**: logit plays a special role in estimating average treatment effects.
- **External — Santos Silva & Tenreyro (2006)**: Poisson QMLE for gravity/trade equations with many zeros; **Heckman (1976)**: the Heckit; **Papke & Wooldridge (1996)**: fractional response QMLE; modern duration analysis (Cox PH) supersedes censored normal regression for durations.
