# Chapter 9: More on Specification and Data Issues

## Core Idea
Most threats to OLS in applied cross-sectional work — functional form misspecification, unobserved confounders, measurement error, nonrandom samples, outliers — can be diagnosed and often mitigated without new data; the craft is knowing which fix matches which failure.

## Frameworks Introduced

- **RESET (Ramsey's regression specification error test)**: add $\hat{y}^2, \hat{y}^3$ to the original regression and F-test $H_0: \delta_1 = 0, \delta_2 = 0$ ($F_{2,\,n-k-3}$ under the null).
  - When to use: routine functional form check after a baseline model; cheaper on degrees of freedom than adding quadratics of every regressor.
  - How: estimate the model, save fitted values, regress $y$ on the $x$'s plus $\hat{y}^2, \hat{y}^3$, run the joint F test (make it heteroskedasticity-robust). Rejection signals neglected nonlinearity in the conditional mean — and nothing else: RESET has no power against omitted variables linear in the included $x$'s, nor against heteroskedasticity, and it gives no direction on which fix to apply.

- **Davidson-MacKinnon test (nonnested alternatives)**: to test model A against nonnested model B, add B's fitted values $\check{y}$ to A and t-test their coefficient.
  - When to use: choosing between levels vs. logs, or any two nonnested models with the same dependent variable, when the F test is unavailable.
  - How: estimate B, get fitted values $\check{y}$; regress $y$ on A's regressors plus $\check{y}$; a significant t on $\check{y}$ rejects A. Reverse the roles to test B. Both may be rejected (more work needed) or neither (choose by adjusted R-squared); rejecting A does not prove B correct.

- **Proxy variable / plug-in solution**: for $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3^* + u$ with $x_3^*$ unobserved, plug in a proxy $x_3$ satisfying $x_3^* = \delta_0 + \delta_3 x_3 + \nu_3$, $\delta_3 \neq 0$.
  - When to use: a key confounder (ability, motivation) is unobservable but something correlated with it exists (IQ, KWW score, computer use at home).
  - How: the plug-in regression of $y$ on $x_1, x_2, x_3$ consistently estimates $\beta_1, \beta_2$ provided (1) $u$ is uncorrelated with $x_1, x_2, x_3^*, x_3$, and (2) $\mathrm{E}(x_3^* \mid x_1, x_2, x_3) = \mathrm{E}(x_3^* \mid x_3)$ — the proxy soaks up everything $x_3^*$ shares with the other regressors. You recover $\alpha_3 = \beta_3\delta_3$, not $\beta_3$; the intercept is not interpretable. If (2) fails, the bias shrinks but does not vanish.

- **Lagged dependent variable as proxy**: include $y_{-1}$ (e.g., prior crime rate) to control for persistent unobserved heterogeneity correlated with policy variables.
  - When to use: policy analysis on a cross section where unobserved historical factors drive both the outcome and the regressors, and no clean proxy exists.

- **Random coefficient (slope) model**: $y_i = a_i + b_i x_i$ with unit-specific slopes; OLS estimates the average partial effect (APE/AME) $\beta = \mathrm{E}(b_i)$.
  - When to use: justifying OLS as an APE when effects are heterogeneous across units.
  - How: sufficient is mean independence $\mathrm{E}(a_i|x_i)=\mathrm{E}(a_i)$ and $\mathrm{E}(b_i|x_i)=\mathrm{E}(b_i)$. The composite error $u_i = c_i + d_i x_i$ is almost surely heteroskedastic — report robust standard errors.

- **LAD (least absolute deviations)**: minimize $\sum_i |y_i - b_0 - b_1 x_{i1} - \cdots - b_k x_{ik}|$; estimates the conditional median, not the conditional mean.
  - When to use: as a robustness supplement to OLS when outliers may drive estimates; only large-sample inference is available.
  - How: run LAD alongside OLS; if they diverge, check whether the gap reflects outliers or a mean–median difference under an asymmetric error distribution. LAD consistently estimates conditional-mean parameters only under symmetry of $u$ (or independence of $u$ and $x$).

## Key Concepts
- **Functional form misspecification**: wrong relationship between $y$ and the observed $x$'s (omitted quadratics/interactions, level vs. log); biases OLS but is detectable with the data in hand.
- **Average partial effect (APE)**: population average of a heterogeneous slope, $\beta = \mathrm{E}(b_i)$.
- **Classical errors-in-variables (CEV)**: measurement error $e_1$ uncorrelated with the true variable, $\operatorname{Cov}(x_1^*, e_1) = 0$.
- **Attenuation bias**: under CEV, the OLS coefficient on the mismeasured regressor is biased toward zero, $\operatorname{plim}\hat\beta_1 = \beta_1 \cdot \sigma_{x_1^*}^2/(\sigma_{x_1^*}^2 + \sigma_{e_1}^2)$.
- **MCAR (missing completely at random)**: missingness independent of both the $x$'s and $u$; complete-case OLS is fine, just smaller.
- **MAR (missing at random)**: missingness may depend on the $x$'s but not on $u$; complete-case OLS remains consistent.
- **Exogenous sample selection**: sample chosen on the independent variables (or independent of $u$) — harmless for OLS.
- **Endogenous sample selection**: selection based on $y$ or correlated with $u$ — always biases OLS for the population model.
- **Influential observation**: dropping it changes key estimates by a practically large amount.
- **Studentized residual**: residual scaled by its estimated standard deviation; equals the t statistic on a dummy for that observation.

## Mental Models
- Use RESET as a smoke alarm, not a diagnosis: it tells you the conditional mean is wrong, not which repair applies.
- Think of a proxy variable as a filter: it must absorb *all* correlation between the unobservable and the other regressors ($\mathrm{E}(x_3^*|x_1,x_2,x_3) = \mathrm{E}(x_3^*|x_3)$), not just be "related to" the confounder.
- Use "measurement error in $y$ costs precision, measurement error in $x$ costs consistency" as the default triage — under CEV, error in the dependent variable only inflates the error variance, while error in a regressor attenuates its coefficient and contaminates the others unpredictably.
- Think of selection questions as "does the sampling rule touch $u$?": selection on $x$ (or independent of $u$) leaves OLS intact; selection on $y$ or on $u$ breaks it.

## Anti-patterns
- **Using RESET as a general misspecification test**: it has no power against omitted variables linear in the included $x$'s or against heteroskedasticity — it is a functional form test for the conditional mean only.
- **Dropping variables for multicollinearity when one is a proxy**: correlation between $educ$ and $IQ$ is the price of controlling for ability; including the proxy also shrinks the error variance.
- **Flagging outliers by raw OLS residuals**: OLS bends the line toward the outlier, so its residual can look unremarkable; use studentized residuals or dummy-variable t statistics instead.
- **Zero-filling missing data without the missing indicator**: setting missing $x_k$ to zero with no indicator $m_{ik}$ biases everything; even the full missing indicator method (MIM) needs MCAR plus $x_k$ uncorrelated with the other regressors — complete cases is the more robust default.
- **Treating LAD as a robust estimator of the conditional mean**: it targets the median; under asymmetric errors, OLS–LAD gaps may be mean–median differences, not outlier effects.
- **Reporting results only on the full sample when one observation is clearly influential**: reestimate with suspects excluded and show both.

## Key Equations & Formulas

RESET expanded equation:
$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + \delta_1 \hat{y}^2 + \delta_2 \hat{y}^3 + error, \qquad H_0: \delta_1 = \delta_2 = 0$$

Proxy equation and key assumption:
$$x_3^* = \delta_0 + \delta_3 x_3 + \nu_3, \qquad \mathrm{E}(x_3^* \mid x_1, x_2, x_3) = \mathrm{E}(x_3^* \mid x_3) = \delta_0 + \delta_3 x_3$$

Random slope error variance (necessary heteroskedasticity):
$$\operatorname{Var}(u_i \mid x_i) = \sigma_c^2 + \sigma_d^2 x_i^2$$

CEV attenuation (simple regression):
$$\operatorname{plim}(\hat{\beta}_1) = \beta_1\left(\frac{\sigma_{x_1^*}^2}{\sigma_{x_1^*}^2 + \sigma_{e_1}^2}\right)$$

CEV attenuation with other regressors ($r_1^*$ = population residual from regressing $x_1^*$ on $x_2, x_3$):
$$\operatorname{plim}(\hat{\beta}_1) = \beta_1\left(\frac{\sigma_{r_1^*}^2}{\sigma_{r_1^*}^2 + \sigma_{e_1}^2}\right)$$

LAD objective and log-model median:
$$\min_{b} \sum_{i=1}^n \left| y_i - b_0 - b_1 x_{i1} - \cdots - b_k x_{ik} \right|, \qquad \operatorname{Med}(y \mid \mathbf{x}) = \exp(\beta_0 + \mathbf{x}\boldsymbol\beta)$$

## Reference Tables

| Problem | Diagnostic | Consequence for OLS | Remedy |
|---|---|---|---|
| Functional form | Quadratics F test, RESET, Davidson-MacKinnon | Biased partial effects | Add terms, switch logs; nonnested test for level vs. log |
| Unobserved confounder | — (theory) | Omitted variable bias | Proxy (plug-in), lagged $y$, later: panel methods, IV |
| Measurement error in $y$ | — | None under CEV; larger error variance | Better data |
| Measurement error in $x$ | — | Attenuation under CEV; other coefficients biased unpredictably | Multiple measures (error variance falls as $\sigma_e^2/m$); IV (Ch. 15) |
| Missing data | MCAR vs. MAR | MCAR/MAR: harmless for complete cases | Complete cases (default); avoid naive MIM |
| Selection on $x$ (exogenous) | — | None | Proceed |
| Selection on $y$ or $u$ (endogenous) | — | Biased and inconsistent | Sample selection corrections (Ch. 17) |
| Outliers | Summary stats, studentized residuals | OLS can swing on one point | Report with/without; logs narrow range; LAD supplement |

Proxy plug-in consistency requirements:
| # | Assumption | Content |
|---|---|---|
| 1 | $u$ uncorrelated with $x_1, x_2, x_3^*, x_3$ | proxy irrelevant once $x_3^*$ included |
| 2 | $\nu_3$ uncorrelated with $x_1, x_2, x_3$ | $x_3$ is a "good" proxy: $\mathrm{E}(x_3^*\mid x_1,x_2,x_3) = \mathrm{E}(x_3^*\mid x_3)$ |

## Worked Example
**IQ as a proxy for ability (Example 9.3, WAGE2, n = 935).** Question: is the return to education overstated because unobserved ability is correlated with schooling? Model: $\log(wage)$ on educ, exper, tenure, married, south, urban, black — with and without IQ as a plug-in proxy. Without IQ the return to education is 6.5% (se 0.006); adding IQ drops it to 5.4% (se 0.007), consistent with positive ability bias in the naive estimate. IQ itself is significant: 10 more IQ points predict 3.6% higher earnings; one SD of IQ (15 points) ≈ one year of education (5.4%). R-squared barely moves (0.253 → 0.263), and the Black–White gap survives (–14.3%, highly significant). A centered educ×IQ interaction is insignificant (t ≈ 0.89) and tiny — report the column without it. Interpretation: the proxy reduces but may not eliminate bias (if $\mathrm{E}(abil|educ, IQ)$ still depends on educ, $\operatorname{plim}\hat\beta_{educ} = \beta_1 + \beta_3\delta_1 > \beta_1$).

## Key Takeaways
1. Functional form problems are detectable in-sample (quadratics F test, RESET, Davidson-MacKinnon); omitted-variable problems are not — this asymmetry should shape your workflow.
2. A proxy only needs to be correlated with the unobservable, but for consistency it must fully absorb the unobservable's correlation with the other regressors; a partial proxy reduces bias without eliminating it.
3. With two periods, a lagged dependent variable is a cheap control for persistent unobserved heterogeneity — expect the policy coefficient to move a lot when you add it (city crime: elasticity of crime w.r.t. law enforcement went from +0.20 to −0.14).
4. Under CEV, noise in $y$ is benign; noise in a regressor attenuates its coefficient toward zero and biases the rest in unknown directions — discount "insignificant" findings on badly measured variables.
5. Selection on the independent variables is harmless; selection on $y$ or on $u$ is fatal for the population model — classify your sampling scheme before estimating.
6. Complete-case OLS is more robust than the missing indicator method, which needs MCAR plus zero correlation between the missing-prone regressor and the others.
7. Always reestimate without influential observations; if results hinge on one data point, say so and consider LAD or logs.

## Connects To
- **Ch 3**: omitted variable bias formula — the proxy and lagged-$y$ strategies are damage control for it.
- **Ch 6**: functional forms (logs, quadratics, interactions) that RESET and nonnested tests adjudicate among.
- **Ch 8**: heteroskedasticity — random slopes generate $\operatorname{Var}(u|x) = \sigma_c^2 + \sigma_d^2 x^2$; robust inference applies throughout this chapter.
- **Ch 13–14**: panel data methods (first differencing, FE) as structural alternatives to lagged-$y$ proxies for unobserved heterogeneity.
- **Ch 15**: IV/2SLS — the remedy for measurement error and endogeneity when proxies fail.
- **Ch 17**: sample selection corrections (Heckman) and limited dependent variable models for endogenous selection.
