# Chapter 13: Pooling Cross Sections across Time — Simple Panel Data Methods

## Core Idea
Use the time dimension as a control: year dummies remove aggregate shocks, difference-in-differences (DD) identifies policy effects from natural experiments, and first differencing (FD) removes time-constant unobserved heterogeneity $a_i$ so that pooled-OLS heterogeneity bias disappears.

## Frameworks Introduced
- **Independently pooled cross section (repeated cross section)**: random samples drawn independently from the same population at different times.
  - When to use: CPS/GSS-style surveys; observations independent across time, so no serial correlation problem.
  - How: pool the years, include dummies for all but one year; interact year dummies with key regressors to test whether slopes changed. With a log dependent variable, aggregate price deflators are absorbed into year dummies — do not deflate manually.
- **Chow test for structural change across time**: $F = [(\mathrm{SSR}_r - \mathrm{SSR}_{ur})/\mathrm{SSR}_{ur}][(n-T-Tk)/(T-1)k]$ where $\mathrm{SSR}_{ur} = \mathrm{SSR}_1+\dots+\mathrm{SSR}_T$ from separate period regressions.
  - When to use: test whether slope coefficients are stable before pooling periods; usually allow intercepts to shift and test only slopes.
  - How: SSR-based version is not heteroskedasticity-robust; for robustness, build year-dummy interactions and joint-test them in the pooled regression.
- **Difference-in-differences (DD/DID) estimator**: $y = \beta_0 + \delta_0 d2 + \beta_1 dT + \delta_1 d2\cdot dT + \text{other factors}$.
  - When to use: natural experiment (quasi-experiment) with a control group, a treatment group, and before/after cross sections.
  - How: regress the outcome on period dummy, group dummy, interaction (the treatment indicator), and controls; $\delta_1$ is the ATE. Add covariates to absorb compositional change and shrink the error variance. Identifying assumption: **parallel trends** — absent treatment, both groups would trend the same.
- **DDD estimator**: difference two DD estimators — either add a second control group ($\hat\delta_{DDD} = \hat\delta_{DD,B} - \hat\delta_{DD,A}$ via the triple interaction $d2\cdot dL\cdot dB$) or add a second control period ($\tilde\delta_{DDD}$ adjusts the DD for the pre-period trend difference; regression equivalent includes a group-specific linear trend $dB\cdot t$).
  - When to use: parallel trends is questionable.
  - How: test pre-trends ($H_0: \gamma = 0$ on $dB\cdot t$, or the placebo interaction $dB\cdot d2$); beware the **pre-testing problem** (Roth 2022) — low power means you drop the trend too often.
- **General multi-group, multi-period policy model**: $y_{igt} = \lambda_t + \alpha_g + \beta x_{gt} + \mathbf{z}_{igt}\gamma + u_{igt}$.
  - When to use: staggered adoption, rescinded policies, multiple policies, exposure-dependent effects (lags $p_{g,t-1}$ or exposure dummies $e0_{gt}\dots eJ_{gt}$). Do NOT force these into basic DD/DDD form.
  - How: pooled OLS with full time dummies and group dummies; relax common trends with group-specific trends $\psi_g t$ ($T \ge 3$); never use full $\theta_{gt}$ cell dummies together with a group-level policy variable (perfect collinearity).
- **Unobserved effects (fixed effects) model + first-differenced estimator**: $y_{it} = \beta_0 + \delta_0 d2_t + \beta_1 x_{it} + a_i + u_{it}$; difference adjacent periods, $\Delta y_i = \delta_0 + \beta_1\Delta x_i + \Delta u_i$, run OLS on the changes.
  - When to use: panel (longitudinal) data where the same units are followed and $a_i$ plausibly correlates with $x_{it}$ (ability, city culture, firm management). Pooled OLS is then biased and inconsistent — **heterogeneity bias**.
  - How (Stata): `xtset id year`, then `reg D.(y x1 x2), vce(cluster id)`; keep an intercept and include time dummies $d3_t\dots dT_t$ in place of differenced dummies for a proper R-squared. With $T=2$ and one treated group, FD equals the panel DD estimator $\hat\beta_1 = \overline{\Delta y}_{treat} - \overline{\Delta y}_{control}$.

## Key Concepts
- **Unobserved effect ($a_i$)**: all time-constant unobserved factors affecting $y_{it}$; also called fixed effect / unobserved heterogeneity.
- **Idiosyncratic error ($u_{it}$)**: time-varying unobserved factors.
- **Composite error**: $v_{it} = a_i + u_{it}$ in pooled OLS; positively serially correlated across $t$ ($\mathrm{Cov}(v_{i1},v_{i2}) = \mathrm{Var}(a_i)$), which invalidates usual pooled-OLS SEs.
- **Heterogeneity bias**: pooled-OLS inconsistency from $\mathrm{Cov}(x_{it}, a_i) \neq 0$; just omitted-variable bias on a time-constant factor.
- **Strict exogeneity**: $\mathrm{Cov}(x_{itj}, u_{is}) = 0$ for all $t,s,j$ (FD.4: $\mathrm{E}(u_{it}|\mathbf{X}_i, a_i)=0$); rules out lagged dependent variables.
- **Parallel trends assumption**: aggregate time effects $\lambda_t$ hit all groups equally; the identifying assumption behind DD-type designs.
- **Natural experiment (quasi-experiment)**: an exogenous event, usually a policy change, creates treatment and control groups; not randomized.
- **Cluster-robust standard errors**: valid under arbitrary within-unit serial correlation and heteroskedasticity; unit $i$ is the cluster; needs moderately large $N$, not-too-large $T$.
- **Pre-trends test / placebo test**: check for a treatment effect before treatment occurs; reject-equals-evidence against parallel trends.
- **Balanced panel**: same $T$ periods for all $N$ units.

## Mental Models
- Think of DD as subtracting two biases: the treatment group's before-after change contains policy + trend; the control group's change contains trend; their difference leaves policy.
- Think of first differencing as using each unit as its own control — anything constant within a unit (observed or not) is differenced away, which is why time-constant regressors drop out entirely.
- Use pooled cross sections when you have fresh random samples each year (precision + changing relationships); use panel FD when you follow the same units and fear correlated heterogeneity.
- Trade-off: differencing buys robustness to $a_i$ at the cost of variation in $\Delta x_i$ — little within-unit change means large SEs, and classical measurement error gets amplified.

## Anti-patterns
- **Pooled OLS when $a_i$ correlates with $x_{it}$**: heterogeneity bias — inconsistent (e.g. pooled crime-on-unemployment gives $\hat\beta_1 = 0.427$ insignificant; FD gives 2.22, significant).
- **Single post-treatment cross section**: the 1981-only regression confuses the pre-existing near-site discount with the incinerator effect; always get the pre-period.
- **Usual OLS SEs on the FD equation**: even if $u_{it}$ is serially uncorrelated, $\mathrm{Corr}(\Delta u_{it}, \Delta u_{i,t+1}) = -0.5$; use cluster-robust SEs (in Example 13.9 the robust SE on $\log(polpc)$ is nearly 4× the OLS one).
- **Lagged dependent variable among $x_{itj}$ with FD**: violates strict exogeneity; more periods do not reduce the inconsistency.
- **Bad controls in policy regressions**: including variables that can be affected by the intervention.
- **Differencing interactions by hand**: difference the full constructed term $\Delta(d04_t union_{it})$; computing $d04_t\Delta union_{it}$ is wrong. Use built-in FD commands.
- **Bogus first differences**: if the differenced regression reports $NT$ or $NT-1$ observations, you subtracted across units; set $t=1$ differences to missing.
- **Deciding trends by pre-test outcome**: dropping $dB\cdot t$ when $H_0:\gamma=0$ fails to reject creates a pre-testing problem; treat the p-value as evidence, not a switch.

## Key Equations & Formulas
$$\hat\delta_1 = (\bar y_{2,T} - \bar y_{2,C}) - (\bar y_{1,T} - \bar y_{1,C}) = (\bar y_{2,T} - \bar y_{1,T}) - (\bar y_{2,C} - \bar y_{1,C})$$
$$\tilde\delta_{DDD} = [(\bar y_{B,3}-\bar y_{B,2}) - (\bar y_{A,3}-\bar y_{A,2})] - [(\bar y_{B,2}-\bar y_{B,1}) - (\bar y_{A,2}-\bar y_{A,1})]$$
$$y_{it} = \beta_0 + \delta_0 d2_t + \beta_1 x_{it} + a_i + u_{it} \;\Rightarrow\; \Delta y_i = \delta_0 + \beta_1\Delta x_i + \Delta u_i$$
$$\Delta y_{it} = \alpha_0 + \alpha_3 d3_t + \beta_1\Delta x_{it1} + \dots + \beta_k\Delta x_{itk} + \Delta u_{it}, \quad t = 2,\dots,T$$
Serial correlation test in FD errors: pooled OLS of $\hat r_{it}$ on $\hat r_{i,t-1}$ ($r_{it} = \Delta u_{it}$), t-test on $H_0: \rho = 0$; $\hat\rho$ consistently estimates $\rho$.
Panel program-evaluation DD: $\hat\beta_1 = \overline{\Delta y}_{treat} - \overline{\Delta y}_{control}$ when participation starts in period 2.

## Reference Tables
**Assumptions FD.1–FD.7 (chapter appendix)**:

| Assumption | Statement | Role |
|---|---|---|
| FD.1 | Model is $y_{it} = \beta_1 x_{it1}+\dots+\beta_k x_{itk}+a_i+u_{it}$ | Linear unobserved effects model |
| FD.2 | Random sample from the cross section | Sampling |
| FD.3 | Each regressor varies over time for some $i$; no perfect collinearity | Identification (drops time-constant regressors) |
| FD.4 | $\mathrm{E}(u_{it}\mid \mathbf{X}_i, a_i) = 0$ — strictly exogenous conditional on $a_i$ | Unbiasedness/consistency of FD |
| FD.5 | $\mathrm{Var}(\Delta u_{it}\mid \mathbf{X}_i) = \sigma^2$ | Homoskedastic differenced errors |
| FD.6 | $\mathrm{Cov}(\Delta u_{it}, \Delta u_{is}\mid \mathbf{X}_i)=0$, $t\neq s$ (implies $u_{it}$ random walk) | No serial correlation in FD errors |
| FD.7 | $\Delta u_{it}$ i.i.d. normal given $\mathbf{X}_i$ | Exact t/F inference |

FD.1–FD.4 → unbiased and consistent (fixed $T$, $N\to\infty$). FD.1–FD.6 → FD is BLUE. Violate FD.5/FD.6 → use cluster-robust SEs.

**DD cell means**:

| | Before | After | After − Before |
|---|---|---|---|
| Control | $\beta_0$ | $\beta_0+\delta_0$ | $\delta_0$ |
| Treatment | $\beta_0+\beta_1$ | $\beta_0+\delta_0+\beta_1+\delta_1$ | $\delta_0+\delta_1$ |
| Treat − Control | $\beta_1$ | $\beta_1+\delta_1$ | $\delta_1$ |

## Worked Example
Kiel–McClain incinerator siting (KIELMC). Question: did a new garbage incinerator lower nearby housing prices? Data: independent cross sections of houses sold in 1978 (pre) and 1981 (post) in North Andover; `nearinc` = within 3 miles. Naive 1981-only regression: $-30{,}688$ on `nearinc` — but 1978 gives $-18{,}824$, so the site was already cheaper. DD regression $rprice = \beta_0 + \delta_0 y81 + \beta_1 nearinc + \delta_1 y81\cdot nearinc + u$ gives $\hat\delta_1 = -11{,}864$ ($t\approx-1.59$). Adding house characteristics (age, intst, land, area, rooms, baths) moves $\hat\delta_1$ to $-14{,}178$ with $t=-2.84$; in logs with full controls, $-0.132$ ($t=-2.53$): houses near the site lost about 13.2% of value. Lesson: control variables both fix compositional shifts and shrink SEs; the pre-existing group difference is absorbed by the `nearinc` main effect.

## Key Takeaways
1. Always include year dummies when pooling over time; with log dollar outcomes they absorb aggregate deflators, so slopes are unaffected.
2. DD identifies the ATE only under parallel trends; support it with pre-trends/placebo checks or relax it with a second control group, a second control period, or group-specific trends ($T\ge3$).
3. For general staggered or rescinded policies, estimate $y_{igt} = \lambda_t + \alpha_g + \beta x_{gt} + \mathbf{z}\gamma + u$ by pooled OLS — never contort the design into a basic DD.
4. Pooled OLS on panel data is inconsistent whenever the unobserved effect correlates with regressors; first differencing restores consistency under strict exogeneity (FD.4).
5. FD cannot estimate effects of time-constant variables and suffers when $\Delta x$ has little variation (e.g. adult education barely changes — huge SEs).
6. Classical measurement error hurts FD more than pooled OLS because differencing shrinks signal relative to noise.
7. Default to cluster-robust standard errors at the unit level for any FD/panel policy regression; differenced errors are mechanically serially correlated.

## Connects To
- **Ch 7**: Chow test mechanics; dummy interactions; $\exp(\hat\beta)-1$ for dummy coefficients in log models.
- **Ch 8**: heteroskedasticity-robust inference, Breusch–Pagan/White tests, WLS with year-varying variance.
- **Ch 9**: lagged $y$ as alternative control for historical differences; classical errors-in-variables (why FD amplifies bias).
- **Ch 14**: fixed effects (within) and random effects — alternatives to FD when $T > 2$ or efficiency matters.
- **Ch 15–16**: IV/2SLS for regressors still endogenous after differencing (e.g. police per capita, simultaneity).
- **Ch 19**: modern staggered-adoption designs and event studies with many periods.
- **staggered-did / Callaway–Sant'Anna**: the general framework (13.21) with staggered timing is exactly where TWFE-DD breaks down and modern estimators take over.
