# Chapter 6: Multiple Regression Analysis: Further Issues

## Core Idea
Functional form, scaling, and regressor-selection choices change how OLS coefficients are interpreted, how precise they are, and how predictions are made — misreading quadratics, overcontrolling, or naively exponentiating a fitted log(y) model silently distorts conclusions, even though the estimation mechanics never change.

## Frameworks Introduced
- **Data scaling invariance**: rescaling y or an x changes coefficients, SEs, and CIs by the rescaling factor; t statistics, F statistics, and R² are unchanged. With log(y), changing y's units shifts only the intercept — slopes are invariant.
  - When to use: choosing units for readable tables; checking cross-study comparability.
- **Beta (standardized) coefficients**: regress z-scored y on z-scored x's; $\hat{b}_j = (\hat{\sigma}_j/\hat{\sigma}_y)\hat{\beta}_j$.
  - When to use: comparing the relative importance of regressors measured in different units. "x_j up one sd → y changes by b_j sds." t statistics identical to unstandardized regression.
- **Quadratic specifications**: $y = \beta_0 + \beta_1 x + \beta_2 x^2 + u$; partial effect $\hat{\beta}_1 + 2\hat{\beta}_2 x$ varies with x.
  - How: compute the partial effect at mean/quartiles of x; locate the turning point $x^* = |\hat{\beta}_1/(2\hat{\beta}_2)|$ and check whether it lies inside the sample range; if only 1–2% of observations fall past it, ignore that branch.
- **Interaction terms**: $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_1 x_2 + u$; partial effect of $x_2$ is $\beta_2 + \beta_3 x_1$.
  - How: reparameterize by centering — interact $(x_1 - \bar{x}_1)(x_2 - \bar{x}_2)$ so the level coefficients become effects at the mean *with correct SEs directly from the regression*. Jointly test $\beta_1 = \beta_6 = 0$ with an F test, never by reading two separate t statistics.
- **Average partial effect (APE)**: average the unit-level partial effect across the sample, e.g. $\widehat{APE}_{atndrte} = \hat{\beta}_1 + \hat{\beta}_6\,\overline{priGPA}$.
  - When to use: one-number summary of a nonlinear model. Centering forces level coefficients to equal APEs and reduces spurious collinearity with the interaction.
- **Bad control / overcontrolling discipline**: never control for a variable that is itself an outcome of the policy variable (a mediator) or a component of the dependent variable.
  - When to use: deciding the control set. Ask "what should be allowed to change when x changes?" — not "does it raise R²?".
- **Adding regressors to reduce error variance**: include variables that affect y and are uncorrelated with the regressors of interest (e.g. controls under random assignment) — no bias, no population multicollinearity, smaller SEs in large samples.
- **CI for E(y|x=c) vs prediction interval for y⁰**: reparameterize by regressing on $(x_j - c_j)$; the new intercept is $\hat{\theta}_0$ with its SE. Prediction interval adds the error variance: $\mathrm{se}(\hat{e}^0) = \{[\mathrm{se}(\hat{y}^0)]^2 + \hat{\sigma}^2\}^{1/2}$.
- **Predicting y from a log(y) model (retransformation)**: naive $\exp(\widehat{\log y})$ systematically underestimates. Correct with $\hat{\alpha}_0 \exp(\widehat{\log y})$; estimate $\alpha_0$ by $\exp(\hat{\sigma}^2/2)$ under MLR.1–MLR.6, by Duan's smearing estimate $n^{-1}\sum \exp(\hat{u}_i)$, or by regressing y on $\hat{m}_i = \exp(\widehat{\log y}_i)$ through the origin.

## Key Concepts
- **Standardized coefficient / beta coefficient**: effect of a one-sd change in x_j on y, measured in sds of y.
- **Semi-elasticity**: $100\cdot\beta$ in a log-level model, the approximate % change in y per unit change in x.
- **Exact percentage change in log models**: $\%\Delta\hat{y} = 100[\exp(\hat{\beta}_2\Delta x_2) - 1]$ — use when $|\hat{\beta}_2\Delta x_2|$ is large; the log approximation always falls between the exact increase and decrease.
- **Turning point**: $x^* = -\hat{\beta}_1/(2\hat{\beta}_2)$, where the partial effect of x changes sign.
- **Moderating effect**: interaction interpretation — x₂ moderates the effect of x₁ when $\beta_3 \neq 0$.
- **Population R-squared**: $\rho^2 = 1 - \sigma_u^2/\sigma_y^2$, the object R² estimates.
- **Adjusted R-squared (R-bar squared)**: $\bar{R}^2 = 1 - [\mathrm{SSR}/(n-k-1)]/[\mathrm{SST}/(n-1)]$ — penalizes added regressors; can be negative.
- **Nonnested models**: neither model is a special case of the other; F tests don't apply, $\bar{R}^2$ comparison does (same dependent variable only).
- **Residual analysis**: inspecting $\hat{u}_i = y_i - \hat{y}_i$ to flag under-/over-priced houses, over-/under-performing schools or athletes.
- **Duan's smearing estimate**: $\hat{\alpha}_0 = n^{-1}\sum_i \exp(\hat{u}_i)$, a normality-free retransformation factor (always > 1).

## Mental Models
- Use beta coefficients when coefficient magnitudes across differently-scaled regressors tempt you to rank "importance" — raw coefficient size is unit-dependent and meaningless for ranking.
- Think of a quadratic's tiny $\hat{\beta}_2$ as a slope-change rate, not an effect size — judge it by computing partial effects across the x range, never by its decimal places.
- Think of the control set as defined by the ceteris paribus question, not by fit: if R² jumps when you add a variable that the treatment itself moves, that variable is blocking the channel you want to measure.
- Think of a prediction interval as two error budgets: estimation error (shrinks with n) plus irreducible error $\sigma^2$ (does not) — in most applications $\sigma^2$ dominates and individual prediction stays wide even with huge n.

## Anti-patterns
- **Reading the level coefficient in an interaction model as "the effect"**: it is the effect at x₁ = 0, often outside the data range (e.g. attendance effect at priGPA = 0). Center at means instead.
- **Testing joint significance of level + interaction (or level + quadratic) via separate t statistics**: individual insignificance does not imply joint insignificance — use the F test (Example 6.3: both t's insignificant, joint p = 0.014).
- **Controlling for mediators**: beer consumption in a beer-tax→fatalities regression, doctor visits in a pesticide→health-expenditures regression — you estimate the direct effect net of the channel, not the policy effect.
- **Comparing R² or $\bar{R}^2$ across different dependent variables** (y vs log(y)): SSTs differ; the comparison is invalid. Use the squared correlation between y_i and $\hat{m}_i$, or SSR-based measure (6.48), after retransformation.
- **Maximizing raw R² to select regressors**: R² never falls when regressors are added; use $\bar{R}^2$ — and remember it is R², not $\bar{R}^2$, that enters the F statistic (4.41).
- **Using log(1+y) as if it were log(y)**: coefficients are not invariant to y's units, and the % interpretation fails near zero (Mullahy & Norton 2023; Chen & Roth 2023).
- **Naive exponentiation** $\hat{y} = \exp(\widehat{\log y})$: systematically understates E(y|x) because E[exp(u)] > 1.

## Key Equations & Formulas

Beta coefficients:
$$\hat{b}_j = (\hat{\sigma}_j/\hat{\sigma}_y)\,\hat{\beta}_j$$

Exact percentage change in a log-level model:
$$\%\Delta\hat{y} = 100\cdot[\exp(\hat{\beta}_2\Delta x_2) - 1]$$

Quadratic partial effect and turning point:
$$\Delta\hat{y}/\Delta x \approx \hat{\beta}_1 + 2\hat{\beta}_2 x, \qquad x^* = \left|\hat{\beta}_1/(2\hat{\beta}_2)\right|$$

Interaction partial effect (centered reparameterization):
$$y = \alpha_0 + \delta_1 x_1 + \delta_2 x_2 + \beta_3(x_1-\mu_1)(x_2-\mu_2) + u, \qquad \delta_2 = \beta_2 + \beta_3\mu_1$$

Adjusted R-squared:
$$\bar{R}^2 = 1 - \frac{\mathrm{SSR}/(n-k-1)}{\mathrm{SST}/(n-1)} = 1 - (1-R^2)\frac{n-1}{n-k-1}$$

Prediction-error standard error and 95% prediction interval:
$$\mathrm{se}(\hat{e}^0) = \left\{[\mathrm{se}(\hat{y}^0)]^2 + \hat{\sigma}^2\right\}^{1/2}, \qquad \hat{y}^0 \pm t_{.025}\cdot\mathrm{se}(\hat{e}^0)$$

Retransformation from log(y):
$$\hat{y} = \hat{\alpha}_0\exp(\widehat{\log y}), \quad \hat{\alpha}_0 = n^{-1}\textstyle\sum_i \exp(\hat{u}_i) \ \text{(Duan)}, \quad \check{\alpha}_0 = \left(\sum \hat{m}_i^2\right)^{-1}\sum \hat{m}_i y_i$$

## Reference Tables

| Choice | Rule |
| --- | --- |
| Which R² for F tests | Only R² (restricted vs unrestricted), never $\bar{R}^2$ |
| $\bar{R}^2$ rises on adding a variable | iff its \|t\| > 1 (a group: iff its F > 1) |
| $\bar{R}^2$ model comparison | valid for nonnested models with the *same* dependent variable; invalid for y vs log(y) |
| When logs help | y > 0 dollar amounts, large counts; often closer to CLM assumptions, narrows range, dampens outliers |
| When logs hurt | proportions near zero (log creates extreme values); zeros/negatives (log undefined; log(1+y) has unit-dependence problems) |
| Controls under random assignment | safe to add any covariate not itself affected by the treatment — gains precision, cannot bias the treatment effect |
| CI for E(y\|x=c) | regress on $(x_j - c_j)$, read intercept ± 1.96·se — narrowest at $c_j = \bar{x}_j$ |
| Interval for an individual y⁰ | add $\hat{\sigma}^2$ inside the SE; typically much wider than the CI for the mean |

## Worked Example
**Effects of attendance on final exam performance (Example 6.3, ATTEND, n = 680).**
Question: does class attendance (atndrte, %) improve the standardized final score (stndfnl), and does it depend on prior GPA?
Model: $stndfnl = \beta_0 + \beta_1 atndrte + \beta_2 priGPA + \beta_3 ACT + \beta_4 priGPA^2 + \beta_5 ACT^2 + \beta_6 priGPA\cdot atndrte + u$.
Estimates: $\hat{\beta}_1 = -0.0067$ (t insignificant), $\hat{\beta}_6 = 0.0056$ (t insignificant), but the F test of $\beta_1 = \beta_6 = 0$ gives p = 0.014 — jointly significant. Interpretation: $\hat{\beta}_1$ alone is the effect at priGPA = 0, which no one in the sample has (minimum ≈ 0.86). The partial effect at the mean priGPA = 2.59 is $-0.0067 + 0.0056(2.59) = 0.0078$: a 10-point attendance increase raises the score by 0.078 sd. Re-running with $(priGPA - 2.59)\cdot atndrte$ delivers se = 0.0026, t = 3 — significant. Lesson embedded in one regression: center interactions, evaluate effects at meaningful covariate values, and test nonlinear terms jointly.

## Key Takeaways
1. Rescaling variables is cosmetic — coefficients and SEs move proportionally, inference does not; with log(y), unit changes move only the intercept.
2. In quadratics and interactions, no single coefficient is "the effect": compute partial effects at interesting x values, locate the turning point, and check it against the data range.
3. Center regressors at their sample means before forming interactions/quadratics: level coefficients become APEs with correct SEs, and collinearity with the interaction terms falls.
4. The control set follows from the ceteris paribus question. Omit mediators and outcome components (bad controls); add covariates uncorrelated with the treatment to shrink error variance — especially valuable under random assignment.
5. Low R² says nothing about bias — MLR.4 (zero conditional mean) governs unbiasedness; low R² only means imprecise individual prediction, offset by large n for estimating the $\beta_j$.
6. Use $\bar{R}^2$ to compare nonnested models on the same dependent variable; never compare R² between y and log(y) specifications directly.
7. To predict y from a log(y) model, multiply $\exp(\widehat{\log y})$ by a smearing factor ($\exp(\hat{\sigma}^2/2)$, Duan's $\hat{\alpha}_0$, or the regression estimate $\check{\alpha}_0$); if $\check{\alpha}_0 < 1$, suspect the independence assumption.

## Connects To
- **Ch 3**: MLR.4 zero conditional mean, multicollinearity/VIF, and the omitted-variables counterpart to overcontrolling.
- **Ch 4**: F tests for joint significance, linear-combination SEs (Section 4-4 reparameterization trick reused for prediction CIs), nested model testing.
- **Ch 5**: large-sample validity without normality — motivates normality-free smearing estimates.
- **Ch 7**: dummy variables and interaction extensions; potential-outcomes framing of controls under randomization.
- **Ch 9**: outlying observations and functional-form misspecification tests (RESET).
- **Ch 17**: APEs in models nonlinear in parameters (logit/probit/Tobit), where retransformation issues return.
- **DAG "bad control" / mediator literature (Pearl; Cinelli & Hazlett)**: formal identification language for the overcontrolling problem.
