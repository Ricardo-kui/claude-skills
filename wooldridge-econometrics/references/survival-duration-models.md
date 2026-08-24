# Duration / Survival Models — beyond the book

> **⚠ beyond the book**: Wooldridge 8e does **not** cover duration/survival analysis (time-to-event outcomes, right censoring, hazard models). This card is a synthetic reference synthesized from the standard survival-analysis literature — Cleves et al., *An Introduction to Survival Analysis Using Stata* (3rd ed., 2016); Kalbfleisch & Prentice (2002); Therneau & Grambsch (2000); Cameron & Trivedi, *Microeconometrics* (2005) ch. 17–18. It is not book content; treat its claims as resting on that literature, not on Wooldridge. The assumption-rung notation below follows the convention of the rest of this skill.

**When to use**: the outcome is a duration / time-to-event — time to recall, time to exit, time to first event — with right censoring (the event has not happened for some observations by the end of the observation window). The Academic Baseline's method default is Cox proportional hazard as the baseline for duration models — never OLS on log duration.

## Core Idea

A duration outcome cannot be analyzed by OLS on log(y) whenever some observations are censored: the censored durations carry information (they survived that long) that OLS discards or misweights, biasing coefficients toward zero. Survival analysis models the **hazard** h(t) — the instantaneous event rate conditional on survival to t — and builds a likelihood that splits each observation into a density contribution (if the event is observed) and a survivor contribution (if censored).

## Frameworks

- **Cox proportional hazards (semiparametric)**
  - Model: h(t|x) = h₀(t)·exp(xβ). The baseline hazard h₀(t) is left unestimated; β comes from the **partial likelihood** (product over event times of exp(x_iβ)/Σ_{j∈R(t_i)} exp(x_jβ), where R(t_i) is the **risk set** of units still exposed at t_i).
  - When to use: the default. You want a hazard-ratio summary of covariate effects without committing to a hazard shape.
  - How: Stata `stset t, failure(d)`; `stcox x1 x2, vce(cluster id)`.
  - Assumption rung: **Cox.1** non-informative censoring; **Cox.2** proportional hazards (effects multiplicative, constant over t); **Cox.3** correct risk-set composition (no left truncation mishandled). Verify Cox.2 with Schoenfeld residuals / log(−log Ŝ) plots before trusting the HRs.
- **Accelerated failure time (AFT) — Weibull, log-logistic, log-normal**
  - Model: ln T = xβ + σε, so covariates stretch/compress time. Weibull is both PH and AFT; log-logistic has a non-monotonic hazard and is AFT-only. Report **time ratios** exp(β) (AFT) — "per SD, expected time to event is ×1.15".
  - When to use: PH is violated and you want the effect on duration directly, or you need a smooth/small-sample hazard. Your recall-timing work uses AFT Weibull with firm+year FE.
  - How: Stata `streg x1 x2, distribution(weibull) time vce(cluster id)`.
  - Assumption rung: **AFT.1** non-informative censoring; **AFT.2** the error distribution is right (Weibull ⇒ extreme-value ε). The distributional assumption is load-bearing — a misspecified error distribution biases the time ratios, unlike Cox's partial likelihood.
- **Right censoring & the likelihood**
  - Contribution: L = ∏ f(t_i)^{δ_i}·S(t_i)^{1−δ_i}, δ = event indicator. Censored observations contribute S(t), the probability of surviving past the censoring time — that is their information.
  - Assumption rung: **C.1** non-informative censoring — censoring is independent of the failure time conditional on covariates. If attrition out of the sample is itself driven by the outcome process, this rung fails.
- **Competing risks**
  - Multiple event types (recall severity classes, failure modes). Two targets: **cause-specific hazards** (standard Cox per cause) or the **subdistribution hazard** (Fine-Gray) if the substantive question is the cumulative incidence of one cause.
  - When to use: your recall data split severity/type into mutually exclusive events — treat them as competing, not as one pooled event.
  - Rung: the usual Cox rungs per cause + a stated target (cause-specific vs subdistribution) because the two answer different questions.
- **Frailty / repeated events / clustering**
  - Units experience multiple events (a firm issues many recalls). Within-unit dependence must be handled or SEs are too small and, with outcome-dependent recurrence, coefficients are biased.
  - Options: **cluster-robust SEs on the working-independence model** (robust to dependence, no random effect assumed); **shared frailty** (a unit random effect in the hazard, the survival analogue of RE); **stratified Cox by unit** (the survival analogue of FE — but only works with enough events per unit).
  - Rung: **R.1** within-unit dependence accounted for (cluster or frailty). Firm **fixed effects** in a duration likelihood suffer **incidental-parameters bias** that does not vanish with N — prefer shared frailty or stratified Cox; if you run AFT Weibull with firm+year FE anyway, report the bias direction and a frailty/cluster robustness.
- **Time-varying covariates / time-varying treatment**
  - Cox extends to time-varying x (tvc): the hazard at t uses x(t). This is how staggered treatments enter duration models.
  - Watch: **anticipation** (units responding before the treatment time) and **time-dependent confounding** (a covariate affected by earlier treatment). These are design questions, not estimation questions — the standard rungs are parallel to strict exogeneity in the panel setting.

## Key Concepts

- **hazard** h(t) = f(t)/S(t): the instantaneous event rate given survival to t.
- **survivor** S(t) = P(T > t) = exp(−Λ(t)); **cumulative hazard** Λ(t) = ∫₀ᵗ h(s)ds.
- **risk set** R(t): units still under observation and not yet failed just before t — the denominator of every Cox term.
- **partial likelihood** (Cox): removes h₀(t), so no assumption on the hazard's shape — the semiparametric payoff.
- **time ratio** (AFT): exp(β) multiplies expected duration; a hazard ratio (Cox) multiplies the hazard. Same covariate, two different quantities — say which you report.
- **non-informative censoring**: censoring carries no information about the failure time conditional on covariates — the survival analogue of the zero-conditional-mean rung.

## Mental Models & Leading Words

- **censoring is data, not missing** — the entire discipline. A firm that has not recalled yet by the end of the window is evidence of *long survival*, not a missing outcome.
- **hazard vs duration** — two parameterizations of the same clock. PH multiplies the hazard (constant ratio); AFT stretches time. Choose by which quantity the theory speaks in, then test the other.
- **risk set** — "who is still exposed" is the survival version of "who is in the sample."
- **frailty ≈ RE, stratified ≈ FE** — the panel analogy that keeps duration-model design honest.

## Anti-patterns

- **OLS on log(y) as the baseline for a censored duration outcome** — biased; the Academic Baseline's default is Cox PH.
- **Dropping censored observations** or coding them as events — both discard information; censored obs are the survivor contributions.
- **Pooling repeated events per firm as independent** — within-unit dependence deflates SEs; cluster or frailty.
- **Firm FE in the duration likelihood without acknowledging incidental-parameters bias** — the panel move does not port cleanly; prefer frailty/stratified, or report the bias.
- **Reporting hazard ratios without testing the PH assumption** — an unchecked Cox.2 makes every HR questionable.
- **Pooling competing event types into one event** — a severity-heterogeneous recall is not one hazard; run cause-specific or Fine-Gray.
- **Time-varying treatment without checking anticipation** — treatment measured before it bites biases the hazard toward zero.

## Key Equations

Hazard / survivor link:
$$h(t) = \frac{f(t)}{S(t)}, \qquad S(t) = \exp\!\left(-\int_0^t h(s)\,ds\right)$$

Cox proportional hazards and partial log-likelihood:
$$h(t\,|\,\mathbf{x}) = h_0(t)\exp(\mathbf{x}\boldsymbol{\beta}), \qquad \ell = \sum_{i:\ \delta_i = 1} \left[\mathbf{x}_i\boldsymbol{\beta} - \log\sum_{j \in R(t_i)} \exp(\mathbf{x}_j\boldsymbol{\beta})\right]$$

AFT:
$$\ln T = \mathbf{x}\boldsymbol{\beta} + \sigma\varepsilon, \qquad \text{time ratio } = \exp(\beta_j)$$

Weibull hazard (both PH and AFT):
$$h(t) = \lambda p(\lambda t)^{p-1}, \quad p > 1 \text{ increasing hazard}, \ p < 1 \text{ decreasing}, \ p = 1 \text{ exponential (memoryless)}$$

## Reference Table

| Situation | Model | Assumption rung to defend |
|---|---|---|
| Baseline duration model | **Cox PH**, HRs | Cox.1 non-informative censoring; Cox.2 proportional hazards; Cox.3 risk set |
| Effect on expected duration, PH violated | **AFT** (Weibull / log-logistic) | AFT.1 censoring; AFT.2 error distribution right |
| Multiple event types | **cause-specific Cox** or **Fine-Gray** | per-cause rungs + stated target |
| Repeated events per firm | Cox/AFT + **cluster** or **shared frailty** | R.1 within-unit dependence |
| Staggered treatment on a duration outcome | Cox with tvc / recent survival-DiD methods | no anticipation + time-dependent confounding handled |
| Firm FE inside a duration model | last resort — **stratified Cox** or **frailty** instead | incidental-parameters bias disclosed |

## Worked Example

Time-to-recall with repeated events and competing severities. Data: firm-level, multiple recalls per firm, right censoring (many firms never recall in the window). Stata: `stset days_to_recall, id(firmid) failure(recall)`; baseline `stcox treatment controls, vce(cluster firmid)`; test PH with `estat phtest` (Schoenfeld). If PH fails on the treatment, switch to `streg ..., distribution(weibull) time` and report time ratios. Because a firm recurs, keep the cluster on firmid (or try `stcox ..., shared(firmid)` as the frailty robustness); because severity classes are mutually exclusive, run a cause-specific Cox per class rather than pooling. Staggered treatment: enter treatment as tvc and check anticipation by leading it.

## Key Takeaways

1. The identifying rung for any duration model is **non-informative censoring**; the second is the model-specific one (Cox: PH; AFT: error distribution).
2. Cox PH is the baseline; report hazard ratios after testing the PH assumption.
3. AFT (Weibull/log-logistic) is the fix when PH fails or the theory speaks in duration; report time ratios.
4. Repeated events ⇒ cluster by unit or shared frailty; firm FE is the fragile port from panel methods.
5. Competing event types are separate hazards, not one pooled event.
6. Time-varying treatment needs an anticipation check.

## Connects To

- **Ch 13–14 (panel)**: frailty ≈ RE, stratified Cox ≈ FE — the panel rungs (strict exogeneity, within-unit dependence) have direct duration analogues.
- **Ch 17**: Poisson QMLE handles *counts* of events; duration models handle *time to* events — distinct objects, don't conflate.
- **[workflow.md](../workflow.md) Step 4**: this card is the "beyond the book" routing target for survival outcomes.
- **`stata` skill / econometrics-agent**: `stset`, `stcox`, `streg`, `estat phtest` execution; econometrics-agent for Cox/PH/Weibull on dta/parquet.
