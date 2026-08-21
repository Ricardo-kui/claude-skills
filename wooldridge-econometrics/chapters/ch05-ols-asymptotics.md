# Chapter 5: Multiple Regression Analysis — OLS Asymptotics

## Core Idea
OLS is consistent and asymptotically normal under the Gauss-Markov assumptions (MLR.1–MLR.5) *without* requiring normal errors, so t and F procedures stay valid in large samples. But more data fixes only variance and nonnormal errors — it never cures inconsistency from regressor–error correlation or invalid standard errors under heteroskedasticity.

## Frameworks Introduced
- **Theorem 5.1 (Consistency of OLS)**: Under MLR.1–MLR.4, $\text{plim}\,\hat{\beta}_j = \beta_j$ for all $j$.
  - When to use: As the minimal requirement on any estimator, especially when finite-sample unbiasedness fails (e.g., some time series settings in Ch 11).
  - How: Check the zero conditional mean (or at least zero correlation) holds; consistency follows by the law of large numbers applied to sample covariances.
- **Assumption MLR.4′ (Zero Mean and Zero Correlation)**: $\mathrm{E}(u)=0$ and $\mathrm{Cov}(x_j,u)=0$, $j=1,\dots,k$ — weaker than MLR.4's zero conditional mean, sufficient for consistency but not unbiasedness.
  - When to use: When interpreting OLS as the best linear approximation to the PRF rather than the PRF itself; the population moment condition behind IV estimation (Ch 15).
  - How: Verify each regressor is uncorrelated with the error; accept that nonlinear functions of the $x_j$ may still correlate with $u$.
- **Theorem 5.2 (Asymptotic Normality of OLS)**: Under MLR.1–MLR.5, $\sqrt{n}(\hat{\beta}_j-\beta_j) \overset{a}{\sim} \text{Normal}(0,\sigma^2/a_j^2)$ and $(\hat{\beta}_j-\beta_j)/\text{se}(\hat{\beta}_j) \overset{a}{\sim} \text{Normal}(0,1)$, whatever the error distribution (only finite variance needed).
  - When to use: Any time the dependent variable is skewed, bounded, or discrete (counts, participation rates) and $n$ is reasonably large (1,500+ is comfortably enough).
  - How: Run t tests, F tests, and CIs exactly as under the CLM assumptions — keep using the $t_{n-k-1}$ distribution rather than switching to standard normal, since $t_{df} \to \text{Normal}(0,1)$ and the t is exact under MLR.6.
- **Lagrange multiplier (LM) / n-R-squared statistic**: Tests $q$ exclusion restrictions using only the restricted model; $LM = nR_u^2 \overset{a}{\sim} \chi^2_q$.
  - When to use: Testing joint significance when only the restricted model is estimated; the template for auxiliary-regression diagnostic tests.
  - How: (i) Regress $y$ on the restricted set, save residuals $\tilde{u}$. (ii) Regress $\tilde{u}$ on **all** $k$ independent variables (same observations!), get $R_u^2$. (iii) Compute $LM = nR_u^2$. (iv) Reject if $LM > c$ from $\chi^2_q$, or use the p-value.
- **Theorem 5.3 (Asymptotic Efficiency of OLS)**: Under Gauss-Markov, OLS has the smallest asymptotic variance among estimators solving moment equations (5.19), which includes IV-type estimators.
  - When to use: As the benchmark for judging whether IV or GLS are worth their extra assumptions. Under heteroskedasticity, more efficient estimators exist (Ch 8).

## Key Concepts
- **Consistency**: The estimator's distribution collapses onto the true parameter as $n\to\infty$; Granger's dictum: "If you can't get it right as n goes to infinity, you shouldn't be in this business."
- **Inconsistency (asymptotic bias)**: $\text{plim}\,\hat{\beta}_1 - \beta_1 = \mathrm{Cov}(x_1,u)/\mathrm{Var}(x_1)$; persists and sharpens with more data.
- **Asymptotic normality**: Standardized OLS estimators are approximately normal in large samples via the CLT, regardless of the (immutable) population distribution of $u$.
- **Asymptotic standard error**: The usual OLS standard error, understood to have only large-sample justification when $u$ is nonnormal.
- **1/√n rule**: $\text{se}(\hat{\beta}_j) \approx c_j/\sqrt{n}$; halving the se requires 4× the data.
- **Auxiliary regression**: A regression run only to compute a test statistic (e.g., $\tilde{u}$ on all $x$'s); its coefficients are not of interest.
- **Score statistic**: Alternative name for the LM statistic, from constrained optimization.
- **Jarque-Bera test**: Test of MLR.6 from third and fourth moments of OLS residuals; itself only asymptotically valid.

## Mental Models
- Think of consistency as the floor, not the ceiling: an inconsistent estimator converges *confidently to the wrong number* — more data makes the wrong answer more precise, not less wrong.
- Use the two-column ledger when n grows: **fixed by asymptotics** (nonnormal errors, estimator variance) vs. **never fixed** (endogeneity/Cov(x,u)≠0, heteroskedasticity for usual se's, functional-form misspecification).
- Think of the population distribution of $u$ as immutable: the CLT acts on the *sampling distribution of $\hat{\beta}_j$*, not on $u$ itself — sampling 10 or 10,000 men changes nothing about how narr86 is distributed.
- Use MLR.4′ as the "best linear approximation" lens: OLS consistently estimates a linear projection even when the PRF is nonlinear; use full MLR.4 when you need partial effects on $\mathrm{E}(y|x)$.

## Anti-patterns
- **Assuming large n rescues endogeneity**: correlation between any $x_j$ and $u$ makes OLS inconsistent; the bias persists at every sample size and typically contaminates *all* coefficients via regressor correlation.
- **Trusting usual t statistics under heteroskedasticity at large n**: Theorem 5.2 requires MLR.5; the CLT does not fix $\text{Var}(y|x)$ nonconstant — switch to heteroskedasticity-robust se's (Ch 8).
- **Reporting Jarque-Bera to justify inference**: circular logic — the normality test is itself only asymptotically valid, and with large n you don't need normality anyway.
- **Using unrestricted residuals in the LM auxiliary regression**: OLS residuals are exactly uncorrelated with included regressors, so $R_u^2 = 0$ mechanically; must use restricted-model residuals $\tilde{u}$ on **all** regressors.
- **Mixing samples across LM steps**: steps (i) and (ii) must use the same observations; re-estimate the restricted model on the reduced data set if excluded variables have missings.
- **Ignoring $n$ in $nR_u^2$**: a tiny $R_u^2$ (e.g., 0.0015) can still reject when $n$ is large — always multiply.
- **Believing one bad regressor contaminates only its own coefficient**: if $x_1$ correlates with $u$ and with $x_2$, then $\hat{\beta}_2$ is inconsistent too; only if $x_1$ is uncorrelated with the other regressors does the damage stay isolated.

## Key Equations & Formulas

Inconsistency (simple regression):
$$\text{plim}\,\hat{\beta}_1 - \beta_1 = \frac{\mathrm{Cov}(x_1,u)}{\mathrm{Var}(x_1)} \tag{5.4}$$

Omitted-variable inconsistency ($u = \beta_2 x_2 + v$ when $x_2$ omitted):
$$\text{plim}\,\tilde{\beta}_1 = \beta_1 + \beta_2\delta_1, \qquad \delta_1 = \frac{\mathrm{Cov}(x_1,x_2)}{\mathrm{Var}(x_1)} \tag{5.5–5.6}$$

Asymptotic normality:
$$\frac{\hat{\beta}_j - \beta_j}{\text{se}(\hat{\beta}_j)} \overset{a}{\sim} \text{Normal}(0,1) \tag{5.7}$$

Estimated variance:
$$\widehat{\mathrm{Var}}(\hat{\beta}_j) = \frac{\hat{\sigma}^2}{\mathrm{SST}_j(1-R_j^2)} \tag{5.9}$$

1/√n rule:
$$\text{se}(\hat{\beta}_j) \approx \frac{c_j}{\sqrt{n}}, \qquad c_j = \frac{\sigma}{\sigma_j\sqrt{1-\rho_j^2}} \tag{5.10}$$

LM statistic for $q$ exclusion restrictions, $\mathrm{H}_0: \beta_{k-q+1}=0,\dots,\beta_k=0$:
$$LM = nR_u^2 \overset{a}{\sim} \chi^2_q$$

General moment-condition estimators (OLS when $g_0=1$, $g_j = x_{ij}$):
$$\sum_{i=1}^{n} g_j(\mathbf{x}_i)\left(y_i - \tilde{\beta}_0 - \tilde{\beta}_1 x_{i1} - \dots - \tilde{\beta}_k x_{ik}\right) = 0 \tag{5.19}$$

## Reference Tables

What asymptotics can and cannot fix:

| Problem | Fixed by large n? | Remedy |
|---|---|---|
| Nonnormal errors (MLR.6 fails) | Yes — CLT gives valid t/F | None needed if n large |
| Estimator variance | Yes — shrinks at 1/n | More data, more x-variation, less collinearity |
| Cov($x_j$, u) ≠ 0 (endogeneity) | **No** — inconsistent | IV (Ch 15), better controls |
| Heteroskedasticity (MLR.5 fails) | **No** — usual se's invalid | Robust se's, FGLS (Ch 8) |
| Functional-form misspecification | **No** | Respecify, nonlinear models (Ch 17) |

LM vs. F for exclusion restrictions:

| | F | LM (n-R²) |
|---|---|---|
| Models estimated | Restricted + unrestricted | Restricted only |
| Statistic | $F \overset{a}{\sim} F_{q, n-k-1}$ | $LM = nR_u^2 \overset{a}{\sim} \chi^2_q$ |
| df that matter | q and unrestricted df | q only |
| Large-sample agreement | Same asymptotic Type I error; discrepancies rare when n large |

## Worked Example
**Economic model of crime (Example 5.3, CRIME1, n = 2,725).** Question: do avgsen (average sentence) and tottime (total prison time) affect narr86 (arrests in 1986), controlling for pcnv, ptime86, qemp86? Note narr86 is 0 or 1 for 92% of men — normality hopeless, but asymptotics applies. (i) Restricted regression of narr86 on pcnv, ptime86, qemp86 → residuals $\tilde{u}$. (ii) Auxiliary regression of $\tilde{u}$ on all five regressors → $R_u^2 \approx 0.0015$. (iii) $LM = 2725 \times 0.0015 \approx 4.09 < 4.61$ (10% critical value, $\chi^2_2$); p-value ≈ 0.129. Fail to reject joint insignificance of avgsen and tottime at 10%. The F test gives p ≈ 0.131 — nearly identical, as expected asymptotically. Caveat: a linear model for a mostly-zero/one outcome may still have functional-form and heteroskedasticity problems that large n does not fix.

## Key Takeaways
1. Demand consistency of every estimator; treat unbiasedness as desirable but dispensable.
2. Sign omitted-variable bias with $\text{plim}\,\tilde{\beta}_1 = \beta_1 + \beta_2\delta_1$ — sign of $\beta_2$ times sign of Cov($x_1,x_2$).
3. With skewed, bounded, or count outcomes and n in the thousands, run t and F procedures exactly as usual — MLR.6 is not needed.
4. Budget precision with the 1/√n rule: se's shrink like $c_j/\sqrt{n}$; quadrupling n halves the se (birth-weight example: predicted ratio 0.707, actual 0.662).
5. The CLT never rescues heteroskedasticity — if MLR.5 fails, usual se's are wrong at every n; go to Chapter 8.
6. Use LM when only the restricted model is handy; it is also the template for auxiliary-regression diagnostics later (Breusch-Pagan, White, RESET-style tests).
7. OLS is asymptotically efficient under Gauss-Markov within the moment-condition class (5.19) — alternatives must justify themselves with weaker assumptions, not better variance under the same ones.

## Connects To
- **Ch 3–4**: Gauss-Markov assumptions MLR.1–MLR.6, unbiasedness, exact t/F inference under normality — this chapter drops MLR.6.
- **Ch 8**: Heteroskedasticity — robust inference and more efficient estimators when MLR.5 fails.
- **Ch 11–12**: Time series settings where OLS can be biased yet consistent; serial correlation.
- **Ch 15**: IV/2SLS — the estimator class in (5.17)/(5.19) and the remedy when Cov(x,u) ≠ 0 makes OLS inconsistent.
- **Ch 17**: Nonlinear (limited dependent variable) models for outcomes like narr86 where the linear PRF approximation is poor.
