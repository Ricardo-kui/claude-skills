# Chapter 2: The Simple Regression Model

## Core Idea
The simple regression model $y = \beta_0 + \beta_1 x + u$ estimates the ceteris paribus effect of $x$ on $y$ only under the zero conditional mean assumption $\mathrm{E}(u|x)=0$; OLS provides the estimation algebra, and the Gauss-Markov assumptions SLR.1–SLR.5 state exactly when the estimates are unbiased and how precise they are.

## Frameworks Introduced
- **Simple linear regression model (SLR)**: $y = \beta_0 + \beta_1 x + u$ in the population; $\beta_1$ is the effect of $x$ on $y$ holding all other factors (in $u$) fixed: $\Delta y = \beta_1 \Delta x$ if $\Delta u = 0$.
  - When to use: as the template for all regression work; rarely sufficient alone for causal claims with nonexperimental data.
  - How: define what goes into $u$ (all factors affecting $y$ other than $x$), then judge whether $u$ plausibly varies with $x$ before trusting $\hat\beta_1$.
- **Zero conditional mean assumption**: $\mathrm{E}(u|x) = \mathrm{E}(u) = 0$ — mean independence of the error from $x$; stronger than $\mathrm{Cov}(x,u)=0$ (correlation only captures linear dependence).
  - When to use: this is *the* identifying assumption; critique any bivariate causal claim by asking whether omitted factors in $u$ correlate with $x$.
- **OLS estimators**: choose $\hat\beta_0, \hat\beta_1$ to minimize the sum of squared residuals; equivalently solves the method-of-moments conditions $\mathrm{E}(u)=0$, $\mathrm{E}(xu)=0$.
  - How: $\hat\beta_1 = \sum(x_i-\bar x)(y_i-\bar y)/\sum(x_i-\bar x)^2$ (sample covariance / sample variance of $x$); $\hat\beta_0 = \bar y - \hat\beta_1 \bar x$.
- **Gauss-Markov assumptions SLR.1–SLR.5**: SLR.1–SLR.4 deliver unbiasedness (Theorem 2.1); adding SLR.5 yields the standard variance formulas (Theorem 2.2). See Reference Tables.
- **Binary regressor / difference-in-means**: with $x \in \{0,1\}$, $\hat\beta_1 = \bar y_1 - \bar y_0$ exactly.
  - When to use: treatment–control comparisons, group mean differences; SLR.3 just requires both groups observed.
- **Potential outcomes framework**: $te_i = y_i(1) - y_i(0)$; ATE $\tau_{ate} = \mathrm{E}[y(1)-y(0)]$; observed outcome $y_i = (1-x_i)y_i(0) + x_i y_i(1)$.
  - When to use: to define the causal estimand before any estimation.
  - How: random assignment ($x_i$ independent of $[y_i(0), y_i(1)]$) makes SLR.4 hold even with heterogeneous treatment effects, so the difference-in-means (OLS) estimator is unbiased for $\tau_{ate}$ — this is the logic of the RCT.

## Key Concepts
- **Error term (disturbance) $u$**: all factors other than $x$ affecting $y$; never observed — distinct from the residual $\hat u_i$.
- **Zero conditional mean**: $\mathrm{E}(u|x)=0$; the average of unobservables is the same in every slice of the population defined by $x$.
- **Population regression function (PRF)**: $\mathrm{E}(y|x) = \beta_0 + \beta_1 x$; fixed but unknown — the SRF $\hat y = \hat\beta_0 + \hat\beta_1 x$ estimates it from one sample.
- **Fitted value / residual**: $\hat y_i = \hat\beta_0 + \hat\beta_1 x_i$; $\hat u_i = y_i - \hat y_i$.
- **R-squared (coefficient of determination)**: $R^2 = \mathrm{SSE}/\mathrm{SST}$, the fraction of sample variation in $y$ explained by $x$; says nothing about bias.
- **Homoskedasticity**: $\mathrm{Var}(u|x) = \sigma^2$ constant; its failure is heteroskedasticity, which invalidates the usual variance formulas but not unbiasedness.
- **Standard error of the regression (SER)**: $\hat\sigma = \sqrt{\mathrm{SSR}/(n-2)}$, estimating the standard deviation of $u$.
- **Average treatment effect (ATE)**: population average of individual treatment effects $y_i(1)-y_i(0)$.
- **Random assignment vs random sampling**: assignment makes $x$ independent of the counterfactuals (gives SLR.4); sampling only gives i.i.d. draws (SLR.2). Do not conflate them.
- **Spurious correlation**: an apparent $x$–$y$ relationship driven by omitted factors in $u$ correlated with $x$.

## Mental Models
- Think of $\beta_1 = \rho_{xy}(\sigma_y/\sigma_x)$ as a rescaled correlation: without an identifying assumption, simple regression *is* correlation analysis — read causality into it only when $\mathrm{E}(u|x)=0$ is defensible.
- Use $\mathrm{Var}(\hat\beta_1) = \sigma^2/\mathrm{SST}_x$ when designing a study: precision rises with more variation in $x$ and larger $n$, falls with error variance. If you can choose, spread the $x_i$ out.
- Think of a low $R^2$ as "large $\mathrm{Var}(u)$ relative to $\mathrm{Var}(y)$", not as bias — unbiasedness lives in SLR.1–SLR.4, none of which mentions $R^2$.
- Use "regress $y$ on $x$" to always mean estimating an intercept plus slope; regression through the origin is the rare exception and biases $\tilde\beta_1$ when $\beta_0 \neq 0$.

## Anti-patterns
- **Reading causality from a bivariate slope with observational data**: omitted factors in $u$ are typically correlated with $x$ (ability in the wage equation; poverty in the lunch-program example), violating SLR.4 and biasing OLS.
- **Judging a regression by its $R^2$**: a low $R^2$ signals large error variance, not bias (JTRAIN2: $R^2 = 0.018$ yet the estimate is unbiased under random assignment); a high $R^2$ says nothing about causality.
- **Confusing residuals with errors**: $\hat u_i \neq u_i$; using SSR/$n$ instead of SSR/$(n-2)$ gives a biased estimator of $\sigma^2$ because residuals obey two first-order-condition restrictions (only $n-2$ degrees of freedom).
- **Saying "another year of education increases log(wage) by 8.3%"**: in a log-level model the percentage interpretation is $100\cdot\beta_1$ on $y$ itself; never attach % to $\log(y)$.
- **Regression through the origin by default**: if $\beta_0 \neq 0$, $\tilde\beta_1$ is biased; also its reported $R^2$ (computed without demeaning $y$) is not comparable to the usual one and the centered version can be negative.
- **Assuming random sampling implies random assignment**: retrospective data on self-selected treatment (e.g., SAT prep courses) fails SLR.4 even with a perfectly random sample — the self-selection problem.

## Key Equations & Formulas
Population model and PRF:
$$y = \beta_0 + \beta_1 x + u, \qquad \mathrm{E}(y|x) = \beta_0 + \beta_1 x \quad\text{under } \mathrm{E}(u|x)=0$$
OLS estimators:
$$\hat\beta_1 = \frac{\sum_{i=1}^n (x_i-\bar x)(y_i-\bar y)}{\sum_{i=1}^n (x_i-\bar x)^2} = \hat\rho_{xy}\frac{\hat\sigma_y}{\hat\sigma_x}, \qquad \hat\beta_0 = \bar y - \hat\beta_1\bar x$$
Sum-of-squares decomposition and goodness-of-fit:
$$\mathrm{SST} = \mathrm{SSE} + \mathrm{SSR}, \qquad R^2 \equiv \mathrm{SSE}/\mathrm{SST} = 1 - \mathrm{SSR}/\mathrm{SST}$$
Algebraic properties (any sample): $\sum \hat u_i = 0$, $\sum x_i \hat u_i = 0$, $(\bar x, \bar y)$ on the OLS line.
Sampling variance (SLR.1–SLR.5):
$$\mathrm{Var}(\hat\beta_1) = \frac{\sigma^2}{\mathrm{SST}_x}, \qquad \mathrm{se}(\hat\beta_1) = \hat\sigma/\sqrt{\mathrm{SST}_x}$$
Error variance estimator:
$$\hat\sigma^2 = \frac{1}{n-2}\sum_{i=1}^n \hat u_i^2 = \mathrm{SSR}/(n-2)$$
Binary regressor: $\hat\beta_0 = \bar y_0$, $\hat\beta_1 = \bar y_1 - \bar y_0$; ATE: $\tau_{ate} = \mathrm{E}[y(1)] - \mathrm{E}[y(0)]$.

## Reference Tables

**Gauss-Markov assumptions for simple regression**

| Assumption | Statement | Role |
|---|---|---|
| SLR.1 Linear in Parameters | $y = \beta_0 + \beta_1 x + u$ holds in the population | Defines the model (logs etc. allowed — linear *in parameters*) |
| SLR.2 Random Sampling | Random sample of size $n$ from the population model | i.i.d. errors across $i$ |
| SLR.3 Sample Variation in $x$ | The $x_i$ are not all the same value | Needed to compute OLS at all |
| SLR.4 Zero Conditional Mean | $\mathrm{E}(u|x) = 0$ | Key identification: SLR.1–4 ⇒ unbiasedness |
| SLR.5 Homoskedasticity | $\mathrm{Var}(u|x) = \sigma^2$ | Yields variance formulas; *not* needed for unbiasedness |

**Functional forms involving logarithms (Table 2.3)**

| Model | Dependent | Independent | Interpretation of $\beta_1$ |
|---|---|---|---|
| Level-level | $y$ | $x$ | $\Delta y = \beta_1 \Delta x$ |
| Level-log | $y$ | $\log(x)$ | $\Delta y = (\beta_1/100)\%\Delta x$ |
| Log-level | $\log(y)$ | $x$ | $\%\Delta y = (100\beta_1)\Delta x$ (semi-elasticity) |
| Log-log | $\log(y)$ | $\log(x)$ | $\%\Delta y = \beta_1\%\Delta x$ (elasticity) |

Units changes: rescaling $y$ by $c$ rescales both coefficients by $c$; rescaling $x$ rescales only the slope; $R^2$ is invariant. With $\log(y)$, rescaling $y$ shifts only the intercept.

## Worked Example
**Evaluating a job training program (Example 2.14, JTRAIN2).** Question: does job training raise earnings? Data: 445 men with poor labor market histories randomly assigned to treatment ($train=1$, 185 men) or control (260 men); outcome $re78$ = real 1978 earnings in thousands. Model: $re78 = \beta_0 + \beta_1 train + u$. OLS gives $\widehat{re78} = 4.55 + 1.79\,train$, $n = 445$, $R^2 = 0.018$. Interpretation: $\hat\beta_1 = 1.79$ is the difference in means — participants earned \$1,790 more on average, ≈39% over the control mean of \$4,550, an economically large effect. Because assignment was random, SLR.1–SLR.4 hold and the estimate is unbiased for the ATE despite $R^2$ below 2%. Contrast with the lunch-program regression ($\widehat{math10} = 32.14 - 0.319\,lnchprg$): the negative "effect" of lunch eligibility on test pass rates reflects poverty in $u$ correlated with $lnchprg$ — SLR.4 fails, so the sign and magnitude signal bias, not causation.

## Key Takeaways
1. $\beta_1$ answers a ceteris paribus question only if $\mathrm{E}(u|x)=0$; state what is in $u$ and argue the assumption before reporting a causal reading.
2. Unbiasedness needs SLR.1–SLR.4 only; homoskedasticity (SLR.5) buys the standard variance formulas — heteroskedasticity breaks inference, not unbiasedness.
3. Precision of $\hat\beta_1$ falls with error variance and rises with sample variation in $x$ and $n$: $\mathrm{Var}(\hat\beta_1) = \sigma^2/\mathrm{SST}_x$.
4. Use the Table 2.3 log forms deliberately: log-level for constant percentage (semi-elasticity), log-log for constant elasticity; never interpret $\log(y)$ itself in percent.
5. With a binary $x$, OLS is exactly a difference in means; under random assignment it estimates the ATE even with heterogeneous treatment effects.
6. Never use $R^2$ to judge bias or causal validity — it measures fit only.
7. Estimate $\sigma^2$ with the degrees-of-freedom correction SSR/$(n-2)$, and keep errors ($u_i$, unobserved) conceptually separate from residuals ($\hat u_i$, computed).

## Connects To
- **Ch 3**: multiple regression — the fix when SLR.4 fails due to omitted observable factors; same Gauss-Markov logic generalized (MLR.1–MLR.5).
- **Ch 4**: statistical inference — the standard errors derived here become t statistics and confidence intervals.
- **Ch 8**: heteroskedasticity — testing and correcting the failure of SLR.5.
- **Ch 9**: proxy variables, measurement error, and nonrandom sampling — systematic treatment of SLR.2/SLR.4 failures.
- **Treatment-effect / program evaluation methods**: the potential-outcomes framework and RCT benchmark here ground later DiD, IV, matching, and RD designs.
