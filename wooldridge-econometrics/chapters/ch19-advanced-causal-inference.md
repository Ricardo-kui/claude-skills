# Chapter 19: Advanced Methods for Causal Inference

## Core Idea
Credible treatment-effect estimates come from explicitly naming the parameter (ATE, ATT, or LATE) and matching it to an identification strategy — regression adjustment, IPW, IPWRA, IV/LATE, RD, or control functions — whose assumptions you can state and partially check.

## Frameworks Introduced

- **Potential outcomes + ATE/ATT/ATU**: Each unit has $y(0), y(1)$; only one is observed (fundamental problem of causal inference). $\tau_{ate} = E[y(1)-y(0)]$, $\tau_{att} = E[y(1)-y(0)|w=1]$, and $\tau_{ate} = (1-\rho)\tau_{atu} + \rho\tau_{att}$.
  - When to use: Frame every policy question this way before choosing an estimator. ATT is identified under weaker assumptions than ATE — only $E[y(0)|w=1] = E[y(0)|w=0]$ is needed; units may self-select on the gain.
  - How: The naive difference in means equals $\tau_{att}$ plus selection bias $E[y(0)|w=1] - E[y(0)|w=0]$; diagnose that bias first.

- **Assumptions ATE.1 (unconfoundedness in mean) + ATE.2 (overlap)**: $E[y(w)|w,\mathbf{x}] = E[y(w)|\mathbf{x}]$ for $w=0,1$; and $0 < p(\mathbf{x}) < 1$ for all $\mathbf{x}$, where $p(\mathbf{x}) = P(w=1|\mathbf{x})$ is the propensity score.
  - When to use: Justifies RA, IPW, IPWRA. For ATT only ATE.1(i) and ATE.2(i) are needed.
  - How: Rich $\mathbf{x}$ helps ATE.1 but threatens ATE.2 — the central tension. Check overlap via the estimated PS before trusting estimates.

- **Regression adjustment (RA)**: Estimate $m_0(\mathbf{x}), m_1(\mathbf{x})$ on control and treated subsamples separately, then average $\hat{m}_1(\mathbf{x}_i) - \hat{m}_0(\mathbf{x}_i)$. Linear: coefficient on $w_i$ in $y_i$ on $1, w_i, \mathbf{x}_i, w_i\cdot(\mathbf{x}_i - \bar{\mathbf{x}})$ (unrestricted LRA). Binary/fractional $y$: separate logits. $y \geq 0$: separate Poisson QMLEs with exponential mean.
  - When to use: Unconfoundedness plausible; want ATE/ATT with flexible outcome types. Prefer unrestricted over restricted RA (Słoczyński 2022); prefer logit/Poisson-exponential because fitted-value averages equal outcome averages, giving an unambiguous ATT.
  - How: In Stata, `teffects ra` / `teffects ipw` / `teffects ipwra` give proper SEs accounting for sampling variance in $\bar{\mathbf{x}}$.

- **Inverse probability weighting (IPW)**: Estimate PS by logit; weight treated by $1/\hat{p}_i$, controls by $1/(1-\hat{p}_i)$; use normalized weights. Equivalent to WLS on $y_i$ on $1, w_i$ with weights $(1-w_i)/(1-\hat{p}_i) + w_i/\hat{p}_i$. For ATT weights: $w_i + (1-w_i)\hat{p}_i/(1-\hat{p}_i)$.
  - When to use: Works unchanged for any outcome type (no mean model needed); forces you to confront overlap directly. Avoid LPM for the PS (fitted values outside (0,1) wreck the weights).
  - How: Estimate flexible logit PS → inspect $\hat{p}_i$ for values near 0/1 → trim or redefine population (Crump et al. 2009 rule: keep $0.1 < \hat{p}_i < 0.9$) → re-estimate PS on the trimmed sample from scratch. PS-based sample selection uses only $(w, \mathbf{x})$, so it induces no selection bias.

- **IPWRA (doubly robust)**: WLS with PS weights on the unrestricted RA regression (19.40). Consistent if either the conditional mean or the PS model is correct (Wooldridge 2007). Also doubly robust with logit, fractional logit, Poisson-exponential QMLE.
  - When to use: Default estimator under unconfoundedness — combines RA and IPW resiliency, often smaller SEs.

- **LATE with binary IV**: Under LATE.1–LATE.4, simple IV/2SLS estimates the ATE for compliers — $\tau_{late} = E[y(1)-y(0)|w(1)-w(0)=1]$ — not the ATE.
  - When to use: Assignment confounded even conditional on $\mathbf{x}$; have an instrument (e.g., eligibility $z$) that shifts participation. First-stage difference $\bar{w}_1 - \bar{w}_0$ consistently estimates the complier fraction.
  - How: Run first stage $w_i$ on $1, z_i$; check sign/strength with robust t. With covariates (LATE.2′, LATE.5 overlap in the instrument propensity score $\eta(\mathbf{x})$): estimate (19.55) by IV — $y_i$ on $w_i, \mathbf{x}_i, z_i\cdot(\mathbf{x}_i-\bar{\mathbf{x}})$ with instruments $[1, z_i, \mathbf{x}_i, z_i\cdot(\mathbf{x}_i-\bar{\mathbf{x}})]$. Dropping the interactions can lose the LATE interpretation (Słoczyński 2024).

- **Sharp / Fuzzy RD**: Running variable $x$, cutoff $c$. Sharp: $w = 1[x \geq c]$ — overlap fails completely, so only $\tau_c = E[y(1)-y(0)|x=c]$ is identified under continuity (RDD.1). Fuzzy: jump in $P(w=1|x)$ at $c$ (RDD.2) plus unconfoundedness of the gain (RDD.3), or monotonicity → LATE at the cutoff.
  - When to use: Assignment rule has a known threshold (test scores, age eligibility, vote shares).
  - How: Local linear regression $y_i$ on $1, w_i, x_i - c, w_i\cdot(x_i-c)$ within $c \pm h$; coefficient on $w_i$ is $\hat{\tau}_c$. Choose $h$ by Imbens–Kalyanaraman MSE minimization; report a range of $h$. Fuzzy: IV estimation of (19.66) with $z_i = 1[x_i \geq c]$ instrumenting $w_i$ (HTV 2001 equivalence). Falsification: RD on pre-determined covariates, placebo cutoffs, McCrary density test for manipulation.

- **Control function (CF) for endogenous switching**: Probit for $w$ on $(\mathbf{x}, \mathbf{z})$; compute generalized residuals $gr_i = w_i\lambda(\mathbf{r}_i\hat{\pi}) - (1-w_i)\lambda(-\mathbf{r}_i\hat{\pi})$ ($\lambda$ = inverse Mills ratio); then OLS of $y_i$ on $1, w_i, \mathbf{x}_i, w_i\cdot(\mathbf{x}_i-\bar{\mathbf{x}}), gr_i, w_i\cdot gr_i$ (Procedure 19.1). Coefficient on $w_i$ is $\hat{\tau}_{ate}$; allows selection on the unobserved gain $u(1)-u(0)$.
  - When to use: Confounded assignment, at least one IV, but you want ATE/ATT rather than LATE and are willing to assume linear potential outcomes + probit selection + linear $E[u(w)|v]$.
  - How: Test exogeneity of $w$ via robust F-test of $H_0: \gamma_0 = 0, \theta = 0$ (no first-stage adjustment needed under $H_0$). Bootstrap both steps for valid SEs otherwise. ATT: average imputed $\hat{y}_i(1)-\hat{y}_i(0)$ over treated units.

## Key Concepts
- **Selection bias**: $E[y(0)|w=1] - E[y(0)|w=0]$ — systematic treated/control difference in the untreated-state outcome.
- **Propensity score**: $p(\mathbf{x}) = P(w=1|\mathbf{x})$, the assignment probability given covariates.
- **Overlap (common support)**: Every covariate cell contains both treated and control units; its failure makes RA extrapolate and IPW explode.
- **Complier**: Unit with $w(0)=0, w(1)=1$ — treatment status moves with the instrument; individually unidentifiable, but their population share is estimated by the first stage.
- **Defier**: Unit with $w(0)=1, w(1)=0$; ruled out by monotonicity (LATE.4).
- **One-sided noncompliance**: $w(0)=0$ always (ineligible cannot participate); no defiers possible, LATE = ATT for the eligible.
- **Instrument propensity score (IPS)**: $\eta(\mathbf{x}) = P(z=1|\mathbf{x})$; used to check overlap when the IV needs controls.
- **Doubly robust estimator**: Consistent if either the outcome model or the propensity score model is correctly specified.
- **Bandwidth $h$**: Window around the RD cutoff; smaller $h$ → less bias, more variance.
- **Generalized residual**: $E(v|w,\mathbf{x},\mathbf{z})$ from the treatment probit; enters the outcome equation as the control function.

## Mental Models
- Use "estimand first, estimator second" when reviewing any causal claim: an unnamed ATE/ATT/LATE is a red flag.
- Think of overlap failure as the silent killer: RA extrapolates quietly, IPW shouts via huge weights — read the PS distribution before any estimate.
- Think of IV as estimating an effect for the marginal units the instrument moves, not for the population; a different instrument means a different LATE (which is also why overidentification rejections are ambiguous under effect heterogeneity).
- Think of fuzzy RD as IV where the cutoff indicator $z = 1[x \geq c]$ is a natural instrument for $w$.

## Anti-patterns
- **Reading causality from a difference in means**: SDM = ATT + selection bias; without (conditional) independence of $y(0)$ it identifies nothing causal.
- **Restricted RA (no treatment–covariate interactions)**: inconsistent for ATE when effects vary with $\mathbf{x}$; use the unrestricted, demeaned-interaction form.
- **Ignoring overlap**: fitting RA/IPW with $\hat{p}_i$ near 0 or 1 and reporting the result for the original population; trim (e.g., $0.1<\hat{p}_i<0.9$) or redefine the target population and say so.
- **Forbidden regression**: plugging first-stage fitted $\hat{w}_i$ into a nonlinear or interacted second stage by OLS instead of proper 2SLS/CF.
- **CF without an excluded instrument**: without $\mathbf{z}$, $gr_i$ is just a nonlinear function of $\mathbf{x}_i$ — identification rests entirely on functional form.
- **Using all the data in sharp RD**: global linear fits extrapolate unchecked functional forms; use local linear regression with a chosen bandwidth.
- **Reporting "the treatment effect" from 2SLS**: it is LATE for compliers; external validity to the whole population is an extra assumption.

## Key Equations & Formulas
$$\tau_{att} + \text{selection bias}:\quad E(y|w=1) - E(y|w=0) = \tau_{att} + \{E[y(0)|w=1] - E[y(0)|w=0]\}$$
$$\hat{\tau}_{ate,ra} = (\hat{\alpha}_1 - \hat{\alpha}_0) + \bar{\mathbf{x}}(\hat{\boldsymbol\beta}_1 - \hat{\boldsymbol\beta}_0), \qquad \hat{\tau}_{att,ra} = \hat{\tau}_{ate,ra} + (\bar{\mathbf{x}}_1 - \bar{\mathbf{x}})(\hat{\boldsymbol\beta}_1 - \hat{\boldsymbol\beta}_0)$$
$$\hat{\tau}_{ate,ipw}:\ \min_{\mu_0,\tau} \sum_i (y_i - \mu_0 - \tau w_i)^2\left(\frac{1-w_i}{1-\hat{\Lambda}_i} + \frac{w_i}{\hat{\Lambda}_i}\right)$$
$$\tau_{late} = \frac{E(y|z=1) - E(y|z=0)}{E(w|z=1) - E(w|z=0)} = \frac{E(y|z=1)-E(y|z=0)}{P(w=1|z=1) - P(w=1|z=0)}$$
$$\tau_{late}\text{ with controls} = \frac{\tau_{ate,y|z}}{\tau_{ate,w|z}} = \frac{E[\mu_1(\mathbf{x}) - \mu_0(\mathbf{x})]}{E[\pi_1(\mathbf{x}) - \pi_0(\mathbf{x})]}$$
$$\text{Sharp RD: } E(y|x) = \mu_{0c} + \tau_c w + \beta_0(x-c) + \delta\, w\cdot(x-c);\quad \hat{\tau}_c \text{ from } y_i \text{ on } 1, w_i, x_i-c, w_i\cdot(x_i-c),\ |x_i - c| < h$$
$$\text{Fuzzy RD: } \tau_c = \frac{m^+(c) - m^-(c)}{F^+(c) - F^-(c)} = \frac{\text{jump in } E(y|x) \text{ at } c}{\text{jump in } P(w=1|x) \text{ at } c}$$
$$\text{CF: } y_i \text{ on } 1, w_i, \mathbf{x}_i, w_i\cdot(\mathbf{x}_i-\bar{\mathbf{x}}), gr_i, w_i\cdot gr_i,\quad gr_i = w_i\lambda(\mathbf{r}_i\hat{\pi}) - (1-w_i)\lambda(-\mathbf{r}_i\hat{\pi})$$

## Reference Tables

Assumptions (exact numbering):

| Assumption | Statement |
|---|---|
| ATE.1 (Unconfoundedness in mean) | (i) $E[y(0)\|w,\mathbf{x}] = E[y(0)\|\mathbf{x}]$; (ii) same for $y(1)$ |
| ATE.2 (Overlap) | (i) $p(\mathbf{x}) < 1$; (ii) $p(\mathbf{x}) > 0$ for all $\mathbf{x}$ |
| LATE.1 (Exclusion restriction) | $y(w,1) = y(w,0)$: $z$ affects $y$ only through $w$ |
| LATE.2 (Exogenous instrument) | $z$ independent of $[w(0), w(1), y(0), y(1)]$ |
| LATE.2′ | Same independence conditional on $\mathbf{x}$ |
| LATE.3 (Existence of compliers) | $P[w(1) > w(0)] > 0$ |
| LATE.4 (Monotonicity / no defiers) | $P[w(1) \geq w(0)] = 1$ |
| LATE.5 (Overlap in IPS) | $0 < \eta(\mathbf{x}) < 1$ for all $\mathbf{x}$ |
| RDD.1 (Continuity) | $\mu_0(x), \mu_1(x)$ continuous at $x = c$ |
| RDD.2 (Jump in treatment probability) | $F^+(c) \neq F^-(c)$ |
| RDD.3 (Unconfounded assignment of gain) | $E[y(1)-y(0)\|w,x] = E[y(1)-y(0)\|x]$ |

Estimator map:

| Estimator | Identifies | Key assumptions | Failure mode |
|---|---|---|---|
| SDM $\bar{y}_1 - \bar{y}_0$ | ATE=ATT | Random assignment | Selection bias |
| Linear RA (unrestricted) | ATE, ATT | ATE.1 (+ATE.2 for honesty) | Extrapolation under poor overlap |
| IPW (normalized) | ATE, ATT | ATE.1, ATE.2, correct PS | Extreme weights near $p\in\{0,1\}$ |
| IPWRA | ATE, ATT | Mean **or** PS correct (doubly robust) | Severe misspecification of both |
| Simple IV / Wald | LATE | LATE.1–LATE.4 | Endogenous IV; no external validity |
| IV with controls (19.55) | LATE | LATE.1, 2′, 3, 4, 5 | Dropping interactions loses LATE meaning |
| Sharp RD (LLR) | $\tau_c$ | RDD.1 | Global fits; bandwidth sensitivity |
| Fuzzy RD (IV local) | $\tau_c$ or $\tau_{late,c}$ | RDD.1, 2 (+3 or monotonicity) | Manipulation of running variable |
| Control function (probit + $gr$) | ATE, ATT, ATU | Linear means, probit selection, linear $E[u\|v]$, relevant IV | No excluded IV → pure functional-form ID |

## Worked Example
Example 19.1 (JTRAIN98): Does non-randomized job training raise 1998 earnings? $n = 1{,}130$ men, 376 treated; controls: age, educ, earn96, unem96 (levels, squares, interactions). Full-sample ATE estimates: SDM −2.05 (0.47); linear RA 2.15 (0.82); IPW 1.26 (0.54); IPWRA 2.11 (0.53). The SDM's negative sign is pure selection bias. Disagreement among ATE estimates signals weak overlap: 339 of 1,130 observations have $\hat{p}_i < 0.1$. Applying the Crump et al. trim ($0.1 < \hat{p}_i < 0.9$, $n = 791$) and re-estimating everything: ATE = 1.97 (RA), 2.19 (IPW), 2.01 (IPWRA); ATT ≈ 1.78 across all methods. Interpretation: training raises earnings by roughly \$1,700–\$2,000; IPWRA is notably stable across samples — the doubly robust estimator earns its keep, and the trimmed estimand applies to a different (more eligible-like) subpopulation, which must be stated.

## Key Takeaways
1. Name the estimand before estimating: ATE, ATT, and LATE answer different policy questions and need different assumption sets.
2. ATT needs only unconfoundedness of $y(0)$ and one-sided overlap — it is the more defensible target when overlap is weak.
3. Always estimate the propensity score and inspect it, even if you plan to use RA; trim on the PS, then redo the whole analysis on the trimmed sample.
4. Default to IPWRA under unconfoundedness: double robustness plus often smaller standard errors.
5. Interpret 2SLS as LATE for compliers; the first stage estimates the complier share, and overidentification rejections may reflect different compliers across IVs rather than invalid instruments.
6. In RD, identify only the effect at the cutoff: local linear fits, IK bandwidth, placebo covariates/cutoffs, and a McCrary manipulation test.
7. Control functions recover ATE/ATT under confounded assignment but only with a genuinely excluded instrument and explicit functional-form assumptions — bootstrap both steps.

## Connects To
- **Ch 15 (IV/2SLS)**: LATE.1–LATE.4 formalize what the simple IV estimator actually identifies; overidentification tests re-read under heterogeneous effects.
- **Ch 7 (dummy variables/interactions)**: unrestricted RA is the demeaned-interaction regression; RA under random assignment improves on SDM efficiency (Negi–Wooldridge).
- **Ch 17 (limited dependent variables)**: logit/fractional logit/Poisson QMLE supply the nonlinear RA pieces; probit generalized residuals supply the control function; sample-selection (Heckman) machinery is the same inverse-Mills algebra.
- **Ch 2 (randomized experiments)**: with random assignment all effects coincide and RA is an efficiency device, not a bias fix.
- **External: Angrist–Pischke / Imbens–Rubin**: LATE monotonicity, matching estimators, and modern RD practice (CCT bandwidths) extend this chapter's toolkit.
