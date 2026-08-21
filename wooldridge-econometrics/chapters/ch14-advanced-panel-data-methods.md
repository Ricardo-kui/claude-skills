# Chapter 14: Advanced Panel Data Methods

## Core Idea
When the unobserved effect $a_i$ may be correlated with the regressors, the fixed effects (within) transformation removes $a_i$ before OLS — random effects is more efficient but consistent only if $a_i$ is uncorrelated with all regressors, and the correlated random effects (Mundlak) approach unifies the two while restoring time-constant variables.

## Frameworks Introduced
- **Fixed effects (within) estimator**: Pooled OLS on time-demeaned data, $\ddot{y}_{it} = \beta_1\ddot{x}_{it1} + \dots + \beta_k\ddot{x}_{itk} + \ddot{u}_{it}$. Time-demeaning sweeps out $a_i$ and every time-constant regressor.
  - When to use: Default whenever $a_i$ may be arbitrarily correlated with regressors; identifies effects only from within-unit time variation. Unbiased/consistent under FE.1–FE.4.
  - How: `xtset id year; xtreg y x1 x2 i.year, fe vce(cluster id)`. Correct df is $N(T-1) - k$ (lose one df per unit). Time-constant variables (educ, race, birth place) drop out; they can only enter interacted with time-varying variables (e.g. `educ × year dummies`). Recover $\hat{a}_i = \bar{y}_i - \hat{\beta}_1\bar{x}_{i1} - \dots$ afterward if needed.
- **Two-way fixed effects (TWFE)**: FE plus a full set of time-period dummies.
  - When to use: Policy evaluation with panel data; omitting time dummies attributes aggregate trends to the policy.
  - How: Add `i.year`. Keep the model flexible (allow lagged policy effects); TWFE failures are usually a too-restrictive model, not the estimator's fault.
- **Dummy variable regression**: Regress $y_{it}$ on N unit dummies plus regressors — identical $\hat{\beta}_j$ to within estimation, with df computed correctly. Use it for intuition and F tests on the $a_i$, not for computation.
- **Random effects (RE) estimator**: Feasible GLS on quasi-demeaned data, $y_{it} - \theta\bar{y}_i = \beta_0(1-\theta) + \beta_1(x_{it1} - \theta\bar{x}_{i1}) + \dots$, with $\theta = 1 - [\sigma_u^2/(\sigma_u^2 + T\sigma_a^2)]^{1/2}$. Nests pooled OLS ($\theta = 0$) and FE ($\theta = 1$).
  - When to use: Only when the key RE assumption $\operatorname{Cov}(x_{itj}, a_i) = 0$ for all $t, j$ is plausible (e.g. treatment randomly assigned); it is the only way to keep coefficients on time-constant regressors. $\hat\theta$ signals whether estimates lean toward pooled OLS or FE.
  - How: `xtreg y x1 x2 educ black, re vce(cluster id)`.
- **Correlated random effects (CRE, Mundlak)**: Model $a_i = \alpha + \gamma\bar{x}_i + r_i$, add unit time averages $\bar{x}_{ij}$ to the equation, estimate by RE. Reproduces $\hat\beta_{FE}$ exactly and restores coefficients on time-constant $z_i$.
  - When to use: To synthesize FE and RE, get a regression-based RE-vs-FE test, or obtain time-constant-variable coefficients with FE robustness.
  - How: Compute time averages of **all** time-varying regressors (including squares/interactions) over the estimation periods only; run `xtreg y x* xbar_* z*, re vce(cluster id)`; test $H_0: \gamma_1 = \dots = \gamma_k = 0$ (joint F/Wald on the time averages) — reject ⇒ use FE. Include all time-constant $z$'s in the test equation. On unbalanced panels, average only over complete cases ($s_{it}=1$) and include time averages of aggregate time variables too.
- **Cluster-robust standard errors**: Allow arbitrary within-unit serial correlation and heteroskedasticity, clustered on the cross-sectional unit.
  - When to use: Always for pooled OLS, RE, and FE with large N and small T. Never cluster on ex-post groupings of a random sample (clustering assumes many clusters, each small).
  - How: `vce(cluster id)`. In dummy-variable regression, clustered SEs on the $\hat{a}_j$ coefficients themselves are meaningless — only the $\hat\beta_j$ SEs are valid.
- **General policy-analysis framework**: $y_{it} = \eta_1 + \alpha_2 d2_t + \dots + \alpha_T dT_t + \beta w_{it} + \mathbf{x}_{it}\psi + a_i + u_{it}$ with intervention indicator $w_{it}$ of any pattern (staggered adoption included); two-period DiD is the special case $T=2$, $w_{i1}=0$.
  - When to use: Any panel policy evaluation; do not shoehorn into 2×2 DiD.
  - How: Define $w_{it}=1$ when unit $i$ is treated at time $t$; estimate by FE (or FD) with cluster-robust SEs; add lags $w_{i,t-1}, w_{i,t-2}$ for dynamic effects. **Falsification test for feedback**: add the lead $w_{i,t+1}$ and test $\delta = 0$ (needs $T \ge 3$; lose last period). For units on different trends, use the heterogeneous trend model $a_i + g_i t$: first difference, then apply FE to the differenced equation ($T \ge 3$).
- **FE vs. FD choice**: Identical at $T=2$. For $T \ge 3$, efficiency hinges on serial correlation in $u_{it}$.
  - When to use: FE if $u_{it}$ serially uncorrelated (FE.6); FD if $u_{it}$ near a random walk ($\Delta u_{it}$ uncorrelated) or with large T / unit roots. FE bias from feedback shrinks at rate $1/T$; FD bias does not depend on T. Report both when they differ.

## Key Concepts
- **Unobserved effects model**: $y_{it} = \beta_1 x_{it1} + \dots + \beta_k x_{itk} + a_i + u_{it}$, splitting the error into time-constant $a_i$ and idiosyncratic $u_{it}$; the design question is how $a_i$ relates to the regressors.
- **Within transformation**: Time-demeaning each variable, $\ddot{x}_{it} = x_{it} - \bar{x}_i$; eliminates $a_i$ and all time-constant regressors.
- **Between estimator**: OLS on the time-averaged cross-sectional equation; biased when $a_i$ correlates with $\bar{x}_i$ — not a serious option.
- **Composite error term**: $\nu_{it} = a_i + u_{it}$; necessarily serially correlated with $\operatorname{Corr}(\nu_{it}, \nu_{is}) = \sigma_a^2/(\sigma_a^2 + \sigma_u^2)$, which is why pooled OLS SEs are invalid.
- **Strict exogeneity (FE.4)**: $E(u_{it} | \mathbf{X}_i, a_i) = 0$ — regressors uncorrelated with the idiosyncratic error in *all* periods; violated by lagged dependent variables and feedback.
- **Key RE assumption**: $\operatorname{Cov}(x_{itj}, a_i) = 0$ for all $t, j$; strong in most observational settings — FE is the default.
- **Unbalanced panel**: Missing periods per unit; FE time-demeaning uses each unit's observed periods, and single-period units drop out (no bias). FE allows attrition correlated with $a_i$ but not with $u_{it}$; FE uses more observations than FD under general missingness.
- **Matched pairs / cluster sample**: Families-of-siblings or sampled firms/schools; treat the cluster as the panel "unit" — differencing or the within transformation removes the cluster effect.
- **Falsification (lead) test**: Adding $w_{i,t+1}$ to the FE equation; significance indicates feedback (policy responds to past shocks), violating strict exogeneity.

## Mental Models
- Think of FE as controlling for each unit's *average level* of $x$ (the CRE interpretation): you compare a unit to its own history, so identification comes only from within-unit time variation.
- Think of $\theta$ as a dial between pooled OLS (0) and FE (1): large $\sigma_a^2$ or large T turns it toward FE — check $\hat\theta$ to see where your RE estimates live.
- Use RE only when treatment is as good as randomly assigned; otherwise the whole point of panel data is that $a_i$ correlates with the regressors.
- Think of clustering as answering "where does the assignment uncertainty live?": cluster at the level where the policy variable varies, never at ex-post groupings of a random sample.

## Anti-patterns
- **Omitting year dummies in policy evaluation**: attributes secular aggregate trends to the intervention — always include a full set of time dummies.
- **Dropping lagged treatment effects**: in the JTRAIN example, omitting $grant_{-1}$ shrinks the grant coefficient from −0.252 to −0.082 (insignificant) — a too-restrictive model, not a TWFE failure.
- **Using the Breusch-Pagan test of $\sigma_a^2 = 0$ to choose RE vs. pooled OLS**: it detects serial correlation in $\nu_{it}$, says nothing about consistency, and assumes normality/homoskedasticity.
- **Choosing FE vs. RE on whether $a_i$ is "a parameter or a random variable"**: wrongheaded; the only question is whether $a_i$ is uncorrelated with the regressors.
- **Using pooled OLS usual SEs on panel data**: the composite error $\nu_{it} = a_i + u_{it}$ is serially correlated, so default SEs are systematically too small — cluster.
- **Clustering at ex-post groupings of a random sample** (e.g. 50,000 randomly sampled students clustered by state): no theoretical justification, and with few large clusters the asymptotics fail.
- **Including experience with a full set of year dummies**: when every unit's experience rises by exactly one per year, its effect is unidentified against aggregate time effects.
- **Reading "heterogeneity exists" (F test on unit dummies rejects) as "pooled OLS is inconsistent"**: heterogeneity only breaks pooled OLS when it correlates with the regressors.

## Key Equations & Formulas
Within-transformed equation:
$$\ddot{y}_{it} = \beta_1\ddot{x}_{it1} + \beta_2\ddot{x}_{it2} + \dots + \beta_k\ddot{x}_{itk} + \ddot{u}_{it}, \quad df = N(T-1) - k$$

Recovering unit effects: $\hat{a}_i = \bar{y}_i - \hat{\beta}_1\bar{x}_{i1} - \dots - \hat{\beta}_k\bar{x}_{ik}$

RE transformation parameter and quasi-demeaning:
$$\theta = 1 - \left[\sigma_u^2/(\sigma_u^2 + T\sigma_a^2)\right]^{1/2}, \qquad y_{it} - \theta\bar{y}_i = \beta_0(1-\theta) + \sum_j \beta_j(x_{itj} - \theta\bar{x}_{ij}) + (\nu_{it} - \theta\bar{\nu}_i)$$
(Replace $T$ with $T_i$ for unbalanced panels.)

Composite-error serial correlation: $\operatorname{Corr}(\nu_{it}, \nu_{is}) = \sigma_a^2/(\sigma_a^2 + \sigma_u^2),\ t \neq s$

CRE specification and test:
$$y_{it} = \alpha_1 + \alpha_2 d2_t + \dots + \alpha_T dT_t + \sum_j \beta_j x_{itj} + \sum_j \gamma_j \bar{x}_{ij} + \sum_h \delta_h z_{ih} + r_i + u_{it}, \qquad H_0: \gamma_1 = \dots = \gamma_k = 0$$
with $\hat\beta_{CRE,j} = \hat\beta_{FE,j}$.

Feedback falsification test (estimate by FE, test $\delta = 0$):
$$y_{it} = \eta_1 + \alpha_2 d2_t + \dots + \alpha_{T-1}d(T-1)_t + \beta w_{it} + \delta w_{i,t+1} + \mathbf{x}_{it}\psi + a_i + u_{it}, \quad t = 1, \dots, T-1$$

Heterogeneous trend model: $y_{it} = \eta_1 + \sum \alpha_t d_t + \beta w_{it} + \mathbf{x}_{it}\psi + a_i + g_i t + u_{it}$ — first difference, then FE on the differenced equation.

## Reference Tables

FE and RE assumptions (Appendix 14A.1):

| Assumption | Statement |
|---|---|
| FE.1 | Linear model $y_{it} = \sum_j \beta_j x_{itj} + a_i + u_{it}$ with unobserved effect $a_i$ |
| FE.2 | Random sample from the cross section |
| FE.3 | Each regressor varies over time (for some $i$); no perfect collinearity |
| FE.4 | Strict exogeneity: $E(u_{it} \mid \mathbf{X}_i, a_i) = 0$ |
| FE.5 | Homoskedasticity: $\operatorname{Var}(u_{it} \mid \mathbf{X}_i, a_i) = \sigma_u^2$ |
| FE.6 | No serial correlation: $\operatorname{Cov}(u_{it}, u_{is} \mid \mathbf{X}_i, a_i) = 0$, $t \neq s$ |
| FE.7 | Normality: $u_{it} \mid \mathbf{X}_i, a_i \sim$ iid Normal$(0, \sigma_u^2)$ |
| RE.3 | No perfect collinearity (time-constant regressors allowed) — replaces FE.3 |
| RE.4 | FE.4 plus $E(a_i \mid \mathbf{X}_i) = \beta_0$ — the key RE assumption |
| RE.5 | FE.5 plus $\operatorname{Var}(a_i \mid \mathbf{X}_i) = \sigma_a^2$ |

Estimator properties: FE.1–FE.4 ⇒ FE unbiased, consistent (N→∞, T fixed); FE.1–FE.6 ⇒ FE is BLUE and beats FD; full RE set (FE.1, FE.2, RE.3, RE.4, RE.5, FE.6) ⇒ RE consistent, asymptotically normal, and most efficient.

Choosing among estimators:

| Situation | Estimator | Why |
|---|---|---|
| $a_i$ may correlate with regressors | FE (or FD) | Robust to arbitrary $a_i$–$x$ correlation |
| Key regressor time-constant | RE (or CRE) | FE sweeps it out |
| $u_{it}$ serially uncorrelated | FE | More efficient (FE.6) |
| $u_{it}$ near random walk / large T, unit roots | FD | $\Delta u_{it}$ weakly dependent; FE bias sensitive |
| Feedback from shocks to future $x$ | FE over FD | FE bias → 0 at rate 1/T |
| $T = 2$ | Either | FE ≡ FD |
| General missing data patterns | FE | Uses more observations than FD |
| Cluster sample, cluster-level policy variable only | RE/pooled OLS + cluster SEs | FE infeasible (no within-cluster variation) |

## Worked Example
**A wage equation with three estimators (Example 14.4, WAGEPAN).** Question: how do estimates of wage determinants change once unobserved individual effects are handled? Data: 545 men, 1980–1987. Model: $\log(wage)$ on exper, exper², married, union, educ, race dummies, year dummies.

- Pooled OLS: married 0.108, union 0.182 — but usual SEs invalid (serially correlated $\nu_{it}$).
- Random effects ($\hat\theta = 0.643$, closer to FE than to POLS): married 0.064, union 0.106.
- Fixed effects (educ, black, hispan, exper all drop out): married 0.047 (0.018), union 0.080 (0.019).

Interpretation: the marriage premium falls by more than half from pooled OLS to FE — consistent with higher-$a_i$ men being more likely to marry, so much of the OLS "premium" is selection. The remaining 4.7% is consistent with either a true productivity effect or employer signaling; the data cannot separate them. The drop of the union premium from 18.2% to 8.0% strongly suggests positive correlation between union status and the unobserved effect.

## Key Takeaways
1. FE is the default: it allows arbitrary correlation between $a_i$ and the regressors; use RE only when $\operatorname{Cov}(x_{itj}, a_i)=0$ is genuinely defensible.
2. Always include a full set of time dummies (TWFE) in policy analysis, and make the model flexible enough — lagged treatment effects, heterogeneous trends.
3. Use cluster-robust SEs (clustered on the unit) for pooled OLS, RE, and FE whenever N is large and T small; never cluster on ex-post groupings of a random sample.
4. Use the CRE/Mundlak approach to reproduce FE estimates, test RE vs. FE with a simple joint test on the time averages, and recover coefficients on time-constant variables.
5. Choose between FE and FD by the serial correlation in $u_{it}$; report both when they give substantively different answers.
6. Test for feedback with the lead regressor $w_{i,t+1}$ before trusting FE/FD policy estimates.
7. Attrition correlated with $a_i$ is fine under FE; attrition correlated with $u_{it}$ biases everything — understand *why* the panel is unbalanced.

## Connects To
- **Ch 13**: First differencing, two-period DiD, and testing serial correlation in $\Delta u_{it}$ — the T=2 equivalence and the FE/FD efficiency tradeoff build directly on it.
- **Ch 12**: GLS under serial correlation — RE is feasible GLS on the composite error's equicorrelated structure.
- **Ch 9**: Missing-data indicators and sample selection — the complete cases indicator $s_{it}$ and attrition bias.
- **Ch 11**: Unit roots and weak dependence — why FD is preferred with large T and integrated processes.
- **Modern staggered DiD literature**: de Chaisemartin–D'Haultfœuille (2020), Goodman-Bacon (2021), Sun–Abraham (2021) — TWFE applied to too-restrictive models; the general $w_{it}$ framework here is the flexible starting point.
