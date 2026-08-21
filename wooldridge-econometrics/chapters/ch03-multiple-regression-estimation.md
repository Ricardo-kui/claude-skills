# Chapter 3: Multiple Regression Analysis — Estimation

## Core Idea

Multiple regression lets OLS estimate **ceteris paribus** effects by explicitly holding other factors fixed; its credibility rests on Assumptions MLR.1–MLR.4 (unbiasedness) plus MLR.5 (valid variances), with the zero conditional mean assumption MLR.4 doing all the causal work.

## Frameworks Introduced

- **Multiple linear regression model**: $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_k x_k + u$, where each $\beta_j$ is the partial effect of $x_j$ holding the other regressors fixed.
  - When to use: any time the question is "effect of $x_1$ controlling for $x_2, \dots, x_k$" — i.e., nearly all empirical work, since simple regression only measures partial effects when regressors are uncorrelated.
  - How: run OLS; the $k+1$ first-order conditions $\sum \hat{u}_i = 0$ and $\sum x_{ij}\hat{u}_i = 0$ pin down the estimates; interpret $\hat{\beta}_j$ as $\Delta\hat{y} = \hat{\beta}_j \Delta x_j$ with the other $x$'s fixed.
- **Partialling out (Frisch–Waugh theorem)**: $\hat{\beta}_1$ equals the slope from a simple regression of $y$ on $\hat{r}_1$, the residuals from regressing $x_1$ on $x_2, \dots, x_k$.
  - When to use: to understand what "controlling for" mechanically does — only the part of $x_1$ uncorrelated with the controls identifies $\hat{\beta}_1$.
  - How: $\hat{\beta}_1 = \sum_i \hat{r}_{i1} y_i \big/ \sum_i \hat{r}_{i1}^2$. Use it to judge whether adding/removing a control will move a coefficient much (via $\tilde{\beta}_1 = \hat{\beta}_1 + \hat{\beta}_2\tilde{\delta}_1$).
- **Omitted variable bias (OVB)**: underspecifying $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + u$ by dropping $x_2$ gives $\text{Bias}(\tilde{\beta}_1) = \beta_2 \tilde{\delta}_1$.
  - When to use: whenever a plausibly relevant variable is unobserved or excluded — reason about sign ($\text{sign}(\beta_2)\times\text{sign}(\text{Corr}(x_1,x_2))$) and rough size of bias instead of guessing.
  - How: bias vanishes only if $\beta_2 = 0$ or $x_1, x_2$ are uncorrelated; otherwise sign it with Table 3.2 logic.
- **Gauss–Markov theorem**: under MLR.1–MLR.5 the OLS estimators are BLUE (best linear unbiased estimators); any linear combination of OLS estimates is also best for the corresponding combination of parameters.
  - When to use: as the efficiency justification for OLS; failure of MLR.4 kills unbiasedness, failure of MLR.5 kills efficiency and the usual standard errors.
- **Bad controls**: a variable that is itself an outcome of the key explanatory variable (e.g., science4 in a classize4 → math4 regression) must not be controlled for, even though it predicts $y$.
  - When to use: when choosing the control set for causal inference — control for pre-treatment variables correlated with treatment; never for post-treatment variables.

## Key Concepts

- **Ceteris paribus interpretation**: each slope coefficient measures the change in $y$ from a one-unit change in $x_j$ holding all other included regressors fixed.
- **Zero conditional mean (MLR.4)**: $E(u \mid x_1, \dots, x_k) = 0$ — the error is mean-independent of every regressor combination; the key identifying assumption.
- **Exogenous / endogenous explanatory variable**: $x_j$ is endogenous if it is correlated with $u$ for any reason; MLR.4 requires all regressors exogenous.
- **Perfect collinearity**: one regressor is an exact linear function of others (violates MLR.3); OLS estimates then do not exist.
- **Multicollinearity**: high (but not perfect) correlation among regressors — $R_j^2$ near 1 — inflating $\text{Var}(\hat{\beta}_j)$; it is *not* an assumption violation.
- **Irrelevant variable (overspecification)**: a regressor with $\beta_j = 0$; including it costs variance but not unbiasedness.
- **Underspecification**: omitting a variable that belongs in the model; generally biases all OLS estimators.
- **SST / SSE / SSR**: total, explained, and residual sums of squares with $SST = SSE + SSR$; $R^2 = SSE/SST$ never falls when regressors are added.
- **Standard error of the regression (SER)**: $\hat{\sigma} = \sqrt{SSR/(n-k-1)}$, estimator of the error standard deviation (also root MSE).
- **Degrees of freedom**: $df = n - (k+1)$ = observations minus estimated parameters (including the intercept).

## Mental Models

- Think of a control variable as a filter: partialling out strips from $x_1$ everything linearly explained by the controls, and only the leftover variation estimates $\beta_1$. Weak leftover variation (high $R_j^2$, small $SST_j$) means imprecise estimates.
- Use the OVB sign table when a reviewer says "you omitted X": sign of bias = sign of X's effect on $y$ times sign of Corr$(x_1, X)$. Size matters too — a 0.1 pp bias on an 8.6% return to education is ignorable.
- Treat $R^2$ as a fit statistic, not a quality stamp: it never falls when variables are added, and a high $R^2$ says nothing about whether MLR.4 holds.
- Use "the procedure is unbiased, not the estimate" when interpreting output: an estimate is one fixed number; unbiasedness is a property of OLS across repeated samples.

## Anti-patterns

- **Including irrelevant variables "to be safe"**: costs precision (larger variances) without buying anything; add controls only when they are confounders of the key relationship.
- **Controlling for bad controls (post-treatment variables)**: e.g., science4 when estimating classize4 → math4 — you hold fixed part of the effect you want to measure, destroying causal interpretation.
- **Confusing MLR.3 with MLR.4**: MLR.3 (no perfect collinearity) is about relationships *among regressors* and is visible in the data; MLR.4 restricts the unobservable $u$ and can never be verified — it must be argued.
- **Reading causality from R-squared**: adding regressors always raises $R^2$; fit is not identification.
- **Mechanically interpreting the intercept**: with regressors like hsGPA or ACT, zero is outside the data range; the intercept is often meaningless on its own.
- **Trusting default standard errors under heteroskedasticity**: formula (3.58) relies on MLR.5; heteroskedasticity does not bias $\hat{\beta}_j$ but invalidates the usual standard errors (fix in Ch. 8).
- **Regression through the origin without reason**: suppressing the intercept forces residuals to violate $\sum \hat{u}_i = 0$, breaks $SST = SSE + SSR$, and can produce negative $R^2$.

## Key Equations & Formulas

Population model and zero conditional mean:
$$y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u, \qquad E(u \mid x_1, \dots, x_k) = 0$$

Partialling out (Frisch–Waugh):
$$\hat{\beta}_1 = \frac{\sum_{i=1}^n \hat{r}_{i1}\, y_i}{\sum_{i=1}^n \hat{r}_{i1}^2}, \quad \hat{r}_{i1} = \text{residuals from } x_1 \text{ on } x_2, \dots, x_k$$

Simple vs. multiple regression link:
$$\tilde{\beta}_1 = \hat{\beta}_1 + \hat{\beta}_2\,\tilde{\delta}_1, \quad \tilde{\delta}_1 = \text{slope from } x_2 \text{ on } x_1$$

Omitted variable bias:
$$\text{Bias}(\tilde{\beta}_1) = E(\tilde{\beta}_1) - \beta_1 = \beta_2\,\tilde{\delta}_1$$

Sampling variance of the OLS slope (under MLR.1–MLR.5):
$$\text{Var}(\hat{\beta}_j) = \frac{\sigma^2}{\text{SST}_j (1 - R_j^2)}, \quad \text{SST}_j = \sum_{i=1}^n (x_{ij} - \bar{x}_j)^2$$

Error variance estimator and standard errors:
$$\hat{\sigma}^2 = \frac{\text{SSR}}{n - k - 1}, \qquad \text{se}(\hat{\beta}_j) = \frac{\hat{\sigma}}{\left[\text{SST}_j (1 - R_j^2)\right]^{1/2}}$$

Goodness of fit:
$$R^2 = \frac{\text{SSE}}{\text{SST}} = 1 - \frac{\text{SSR}}{\text{SST}}$$

## Reference Tables

**Gauss–Markov assumptions (cross-sectional):**

| Assumption | Statement | Failure consequence |
|---|---|---|
| MLR.1 Linear in Parameters | $y = \beta_0 + \beta_1 x_1 + \cdots + \beta_k x_k + u$ in the population | Wrong model; nothing to estimate |
| MLR.2 Random Sampling | Random sample of $n$ observations from the MLR.1 population | Unbiasedness in jeopardy |
| MLR.3 No Perfect Collinearity | No regressor is constant or an exact linear function of the others; $n \geq k+1$ | OLS estimates do not exist |
| MLR.4 Zero Conditional Mean | $E(u \mid x_1, \dots, x_k) = 0$ | OLS biased (omitted variables, functional form misspecification, endogeneity) |
| MLR.5 Homoskedasticity | $\text{Var}(u \mid x_1, \dots, x_k) = \sigma^2$ | Variance formula and usual SEs invalid; OLS no longer BLUE |

**Properties ladder:** MLR.1–4 ⇒ unbiasedness (Thm 3.1) · MLR.1–5 ⇒ $\text{Var}(\hat{\beta}_j)$ formula (Thm 3.2) and $E(\hat{\sigma}^2) = \sigma^2$ (Thm 3.3) · MLR.1–5 ⇒ BLUE (Thm 3.4).

**Direction of OVB (Table 3.2), when $x_2$ is omitted:**

| | Corr$(x_1, x_2) > 0$ | Corr $= 0$ | Corr $< 0$ |
|---|---|---|---|
| $\beta_2 > 0$ | Positive bias | No bias | Negative bias |
| $\beta_2 = 0$ | No bias | No bias | No bias |
| $\beta_2 < 0$ | Negative bias | No bias | Positive bias |

**What inflates $\text{Var}(\hat{\beta}_j)$:** larger error variance $\sigma^2$ (get better data/more controls that explain $y$) · smaller $\text{SST}_j$ (get more observations or more variation in $x_j$) · larger $R_j^2$ (multicollinearity; often the price of controlling well).

## Worked Example

**Question:** Does job training raise earnings? (Example 3.7, JTRAIN98; $n = 1{,}130$ men.)

**Model:** $earn98 = \beta_0 + \beta_1\,train + \beta_2\,earn96 + \beta_3\,educ + \beta_4\,age + \beta_5\,married + u$, earnings in thousands; assignment to training is not random — selection into participation tracks past earnings.

**Estimates:**
- Simple regression: $\widehat{earn98} = 10.61 - 2.05\,train$, $R^2 = 0.016$ — trainees appear to earn **$2,050 less**, reflecting negative selection, not the program effect.
- With controls: $\widehat{earn98} = 4.67 + 2.41\,train + 0.373\,earn96 + 0.363\,educ - 0.181\,age + 2.48\,married$, $R^2 = 0.405$ — training now estimated to raise earnings by **$2,410**.

**Interpretation:** the sign flip from −2.05 to +2.41 is exactly what the OVB formula predicts when $train$ is negatively correlated with omitted earnings potential ($\beta_2 > 0$, $\tilde{\delta}_1 < 0$ ⇒ negative bias). Controlling for pre-program earnings and demographics removes much of the selection. Caveat: controls may not fully restore MLR.4 — motivation remains in $u$ — and significance is not yet assessed (Ch. 4).

## Key Takeaways

1. Interpret every slope as a partial effect: $\hat{\beta}_j$ holds the *other included* regressors fixed — nothing else.
2. MLR.4 is the assumption that matters and the one you cannot test; argue it by naming what sits in $u$ and whether it correlates with the regressors.
3. Sign omitted variable bias before lamenting it: $\text{Bias}(\tilde{\beta}_1) = \beta_2\tilde{\delta}_1$; use theory for $\beta_2$'s sign and intuition for the correlation.
4. Omitting a relevant variable biases; including an irrelevant one only inflates variances. But neither license holds for bad controls — never control for consequences of the treatment.
5. Multicollinearity is a data problem (large $\text{Var}(\hat{\beta}_j)$ via $R_j^2$ near 1), not an assumption failure — do not "fix" it by dropping confounders.
6. $R^2$ measures fit only; never use it to judge causality, and never compare $R^2$ across models with different dependent variables or no intercept.
7. Under MLR.1–MLR.5 OLS is BLUE; heteroskedasticity leaves estimates unbiased but breaks the default standard errors.

## Connects To

- **Ch 2 (Simple Regression)**: SLR assumptions are the $k=1$ special case; $\tilde{\beta}_1 = \hat{\beta}_1 + \hat{\beta}_2\tilde{\delta}_1$ links the two.
- **Ch 4 (Inference)**: $\text{se}(\hat{\beta}_j)$ from (3.58) feeds the $t$ statistics and confidence intervals; MLR.6 adds normality.
- **Ch 5 (Asymptotics)**: formula (3.51) remains the quantity estimated in large samples; consistency needs only a weaker MLR.4′.
- **Ch 8 (Heteroskedasticity)**: remedies when MLR.5 fails — robust standard errors and WLS.
- **Ch 9 (Specification Issues)**: formal tests for functional form misspecification and proxy-variable solutions to omitted variables.
- **Ch 15 (IV/2SLS)**: what to do when MLR.4 fails and controls cannot fix endogeneity.
- **frisch-waugh-lovell**: the partialling-out result (3.22) — foundation for understanding fixed effects and partialling out in panel data (Ch. 14).
- **Potential outcomes / treatment effects**: Example 3.7 frames regression as estimating an ATE under selection-on-observables — the bridge to modern policy evaluation (Ch. 16, DiD, matching).
