# Chapter 7: Multiple Regression Analysis with Qualitative Information

## Core Idea

Dummy (binary/indicator) variables let qualitative information — group membership, ordinal ratings, treatment status, and binary outcomes — enter standard OLS, where their coefficients read directly as ceteris paribus group differences, slope differences, or changes in response probabilities. OLS mechanics and inference change not at all; only interpretation changes.

## Frameworks Introduced

- **Single dummy with base group**: $y = \beta_0 + \delta_0 \cdot female + \beta_1 x + u$, where $\delta_0 = E(y|female=1,x) - E(y|female=0,x)$ is an intercept shift under zero conditional mean.
  - When to use: estimating a group gap (gender wage gap, discrimination test) while controlling for covariates.
  - How: name the dummy for the $=1$ event; keep the overall intercept; include $g-1$ dummies for $g$ groups; test $H_0: \delta_0 = 0$ with the usual t statistic. Simple regression of $y$ on a constant and one dummy is a comparison-of-means test between two groups.

- **Dummy coefficients with $\log(y)$**: approximate percentage difference is $100\cdot\hat\delta$; exact is $100\cdot[\exp(\hat\delta)-1]$.
  - When to use: any log-level model with dummy regressors.
  - How: use the exact formula whenever $|\hat\delta|$ is large; the $100\cdot\hat\delta$ approximation conveniently lies between the two base-group versions of the exact estimate.

- **Dummy×quantitative interactions (different slopes)**: $y = \beta_0 + \delta_0 D + \beta_1 x + \delta_1 (D\cdot x) + u$ — $\delta_0$ shifts the intercept, $\delta_1$ shifts the slope.
  - When to use: testing whether an effect (return to education, discrimination) varies across groups.
  - How: generate the interaction and run OLS; test $H_0: \delta_1 = 0$ by t (equal slopes, intercept may differ) or $H_0: \delta_0 = \delta_1 = 0$ by F (identical functions). Re-center: replace $D\cdot x$ with $D\cdot(x - \bar x)$ so $\delta_0$ measures the group gap at the mean of $x$, where it is precisely estimated and interesting.

- **Chow test (full regression-function difference)**: test all $k+1$ coefficients equal across two groups via
  - When to use: "do the two groups follow the same regression function?"
  - How: estimate the pooled restricted regression ($SSR_P$) and separate regressions per group ($SSR_1, SSR_2$); compute the F statistic below. To allow an intercept difference under the null, include the group dummy in the pooled regression and test only the $k$ interactions. Valid only under homoskedasticity — equal error variances across groups under the null. There is no simple R-squared form when separate regressions are used.

- **Linear probability model (LPM)**: OLS on binary $y$; under MLR.4, $P(y=1|\mathbf{x}) = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k$, so $\beta_j$ is the change in response probability per unit change in $x_j$.
  - When to use: quick, interpretable models of binary outcomes (arrest, approval, participation), especially with many covariates/FEs.
  - How: run OLS as usual; name $y$ after the $y=1$ event; always use heteroskedasticity-robust standard errors because $\operatorname{Var}(y|\mathbf{x}) = p(\mathbf{x})[1-p(\mathbf{x})]$ is inherently heteroskedastic; judge fit by percent correctly predicted (predict 1 if $\hat y \ge 0.5$), not just $R^2$.

- **Regression adjustment for program evaluation (RRA vs URA)**: estimate the ATE $\tau$ of treatment $w$ under unconfoundedness — $w$ independent of $[y(0), y(1)]$ conditional on $\mathbf{x}$.
  - When to use: estimating a treatment/program effect from observational data or an RCT.
  - How (Stata recipe for URA): demean every covariate (`gen c_x = x - r(mean)`); regress `y w c_* w#c.c_*`; the coefficient on $w$ is $\hat\tau_{ura}$ with a valid SE. Equivalent: regress $y$ on $\mathbf{x}$ separately by group, predict both potential outcomes for every unit, and average $[\hat y_i(1) - \hat y_i(0)]$. RRA (7.36) omits the interactions and imposes a constant treatment effect. Under randomized assignment, URA is never less asymptotically efficient than the simple difference in means (Negi & Wooldridge 2021) — but SDM is unbiased in finite samples while RA estimators are only consistent; run placebo (balance) tests comparing pre-treatment covariate means across arms.

## Key Concepts

- **Dummy (binary/indicator/zero-one) variable**: a 0–1 variable coding qualitative information; its coefficient is the ceteris paribus outcome difference relative to the base group.
- **Base group / benchmark group**: the omitted category carried by the overall intercept; every dummy coefficient is a difference from it — always state which group it is.
- **Dummy variable trap**: including $g$ dummies plus an intercept for $g$ groups creates perfect collinearity.
- **Uncentered R-squared** $R_0^2 = 1 - SSR/SST_0$: reported when the intercept is dropped; mechanically inflated and rarely a valid fit measure — avoid the no-intercept dummy specification.
- **Ordinal variable**: a ranked variable (credit rating, school rank) whose unit steps need not have equal effects; enter as category dummies, not linearly.
- **Response probability**: $p(\mathbf{x}) = P(y=1|\mathbf{x})$, linear in parameters in the LPM.
- **Self-selection problem**: participation decisions differ systematically by characteristics that also affect potential outcomes; breaks naive treatment-dummy identification.
- **Unconfoundedness / ignorability**: conditional on covariates $\mathbf{x}$, assignment $w$ is as good as random — the identifying assumption behind regression adjustment.
- **Average treatment effect (ATE)**: $\tau = E[y(1)] - E[y(0)]$; URA recovers it as the coefficient on $w$ when all covariates are demeaned before interacting.
- **Percent correctly predicted**: binary-outcome goodness-of-fit measure — fraction of observations where $\tilde y_i = 1[\hat y_i \ge 0.5]$ matches $y_i$.

## Mental Models

- Think of a dummy coefficient as an **intercept shift between parallel lines**; add a dummy×$x$ interaction and you tilt the line for one group.
- Use **g − 1 dummies plus an intercept** whenever you have g categories; if you find yourself adding the g-th dummy, you are in the trap.
- Think of the main effect $D$ in an interaction model as **the group gap evaluated at $x = 0$** — often uninteresting and imprecisely estimated; re-center $x$ so it reads as the gap at the sample mean.
- Use the LPM when you want **marginal effects on a probability in one line of OLS**; treat predictions outside [0,1] as a sign that the linear form is an approximation near sample means, not that OLS failed.

## Anti-patterns

- **Falling into the dummy variable trap**: $g$ dummies plus an intercept is perfect collinearity; some packages silently drop a column, which scrambles your interpretation of the base group.
- **Reading a large log-level dummy coefficient as an exact percentage**: $100\cdot\hat\delta$ overstates; use $100\cdot[\exp(\hat\delta)-1]$ — e.g. $-0.297$ is a 25.7% gap, not 29.7%.
- **Concluding "no group effect" from an insignificant main effect when interactions are present**: adding $D\cdot x$ inflates the SE on $D$ (the gap is then measured at $x=0$); the F test on all group terms may still reject strongly (Example 7.10: female t falls to 1.35 while F = 34.33).
- **Testing group equality with individual t statistics**: each interaction can be insignificant while the joint F soundly rejects (Example 7.22: all four female terms individually weak, F = 8.14).
- **Entering an ordinal variable linearly**: forces a constant effect per rank step; category dummies nest the linear form as a restriction ($\delta_2 = 2\delta_1$, …) testable by F.
- **Ignoring built-in heteroskedasticity in the LPM**: usual t/F statistics are invalid; use robust SEs (Chapter 8).
- **Claiming causality from a treatment dummy on observational data**: if participation self-selects on unobservables (grant applicants, AFDC participation), $\hat\tau$ is biased in either direction no matter how rich the covariates look.
- **Interacting with un-demeaned covariates in URA**: then the coefficient on $w$ is the ATE only for units with $x = 0$ (e.g., unmarried men), not the sample ATE.

## Key Equations & Formulas

Dummy as conditional-mean difference:
$$\delta_0 = E(y \mid D=1, \mathbf{x}) - E(y \mid D=0, \mathbf{x})$$

Exact percentage effect of a dummy in a log-level model:
$$\%\Delta\hat y = 100\cdot\left[\exp(\hat\beta_1) - 1\right]$$

Group-specific regression function (two groups, $k$ regressors):
$$y = \beta_{g,0} + \beta_{g,1}x_1 + \dots + \beta_{g,k}x_k + u, \quad g = 1,2$$

Chow statistic ($SSR_P$ pooled, $SSR_1+SSR_2$ from separate regressions):
$$F = \frac{\left[SSR_P - (SSR_1 + SSR_2)\right]}{SSR_1 + SSR_2}\cdot\frac{[n - 2(k+1)]}{k+1}$$
(divide by $k$ instead when the null allows an intercept shift).

LPM response probability and marginal effect:
$$P(y=1 \mid \mathbf{x}) = \beta_0 + \beta_1 x_1 + \dots + \beta_k x_k, \qquad \Delta P(y=1\mid\mathbf{x}) = \beta_j\,\Delta x_j$$

LPM conditional variance (built-in heteroskedasticity):
$$\operatorname{Var}(y \mid \mathbf{x}) = p(\mathbf{x})\,[1 - p(\mathbf{x})]$$

Unconfoundedness (conditional independence) for regression adjustment:
$$w \perp [y(0), y(1)] \mid \mathbf{x} = (x_1, \dots, x_k)$$

URA estimating regression (covariates demeaned at $\bar x_j$):
$$y_i \ \text{on}\ w_i,\ x_{i1},\dots,x_{ik},\ w_i(x_{i1}-\bar x_1),\dots,w_i(x_{ik}-\bar x_k); \quad \hat\tau_{ura} = \text{coefficient on } w_i$$

Counterfactual-imputation form of the same ATE:
$$\hat\tau = n^{-1}\sum_{i=1}^{n}\left[\hat y_i(1) - \hat y_i(0)\right]$$

## Reference Tables

| Specification | What it allows | Key test | Watch out for |
| --- | --- | --- | --- |
| $y$ on $D$ + controls | intercept shift only | t on $\delta_0$ | base-group bookkeeping |
| $\log y$ on $D$ + controls | percentage gap | t; report $100[\exp(\hat\delta)-1]$ for large $\hat\delta$ | approximation bias |
| $D$ + $D\cdot x$ | intercept + slope shift | t on $\delta_1$; F on $(\delta_0,\delta_1)$ | main effect now at $x=0$; re-center |
| Full interactions (7.20) | all coefficients differ by group | Chow F on all group terms | needs homoskedasticity; use joint F, not t's |
| LPM | binary $y$ | robust t/F | predictions outside [0,1]; heteroskedastic by construction |
| RRA (7.36) | constant treatment effect | t on $w$ | biased if effect is heterogeneous |
| URA (7.42) | ATE with heterogeneous effects | t on $w$; F on interactions | demean covariates first; needs unconfoundedness |

| Assignment | Unbiased estimator | Efficiency | Caveat |
| --- | --- | --- | --- |
| Randomized | SDM $\bar y_1 - \bar y_0$ (unbiased) | URA ≥ SDM asymptotically; never worse | URA only consistent; small samples may favor SDM |
| Observational | none without unconfoundedness | URA ≥ RRA asymptotically | self-selection bias runs both ways |

## Worked Example

**Question**: Do women earn less than comparable men? (WAGE1, $n = 526$.)

- **Model**: $\log(wage) = \beta_0 + \delta_0 female + \beta_1 educ + \beta_2 exper + \beta_3 exper^2 + \beta_4 tenure + \beta_5 tenure^2 + u$ (Eq. 7.9).
- **Estimate**: $\hat\delta_0 = -0.297$ (se 0.036); adding the interaction $female\cdot educ$ gives $-0.0056$ (se 0.0131, $t \approx -0.43$) — returns to education do not differ by gender, so prefer the constant-gap model.
- **Interpretation**: the exact gap is $100[\exp(-0.297)-1] \approx -25.7\%$; women earn about 25.7% less than men with identical educ/exper/tenure (the raw "$-29.7\%$" overstates). When the interaction is included, the t on *female* collapses to 1.35 only because the gap is then evaluated at $educ = 0$ — the joint F of 34.33 confirms a large differential. Compare with the no-controls regression (7.5): raw gap $-\$2.51$ shrinks to $-\$1.81$ once productivity controls are added — controls matter, but a large ceteris paribus gap remains.

## Key Takeaways

1. Dummy regressors change only interpretation, not OLS mechanics or inference: estimate by OLS, test with ordinary t/F.
2. Always track the base group; $g$ groups need $g-1$ dummies plus an intercept — never $g$ dummies with an intercept, and rarely $g$ dummies without one (uncentered $R^2$ is garbage).
3. In log-level models report $100[\exp(\hat\delta)-1]$ whenever the dummy coefficient is large.
4. With interactions, read the main effect at $x = 0$ — re-center covariates so the group gap is evaluated at the sample mean, and test joint hypotheses with F, never coefficient-by-coefficient t scanning.
5. The LPM is a legitimate workhorse for binary outcomes: interpret $\hat\beta_j$ as a probability change, use robust SEs ($\operatorname{Var}(y|\mathbf{x}) = p(1-p)$), and check percent correctly predicted; move to logit/probit (Ch. 17) when out-of-range predictions matter.
6. A treatment dummy identifies the ATE only under unconfoundedness; URA (demeaned covariates + full interactions) relaxes the constant-effect assumption at no efficiency cost, and placebo balance tests on pre-treatment variables are the standard credibility check.

## Connects To

- **Ch 3**: zero conditional mean (MLR.4) underlies every dummy-coefficient interpretation; potential outcomes first appear in 3-7e.
- **Ch 4**: t/F testing machinery used for group-gap and Chow tests.
- **Ch 6**: semi-elasticity calculation behind the $\exp(\hat\delta)-1$ correction; interactions and moderators.
- **Ch 8**: heteroskedasticity-robust inference the LPM requires.
- **Ch 13–15**: panel, IV, and advanced methods for when self-selection defeats regression adjustment.
- **Ch 17**: logit/probit as nonlinear alternatives to the LPM.
