# Chapter 16: Fixed Effects

## Core Idea

Fixed effects isolate variation within a group or unit and remove confounding that is constant within that fixed-effect category. They do not remove time-varying confounding, reverse causality, dynamic selection, or measurement error.

## Identification Contract

State:

- fixed-effect dimensions;
- treatment variation remaining after residualization;
- units that switch or vary enough to identify the coefficient;
- why time-varying untreated potential outcomes are conditionally comparable;
- treatment and outcome timing;
- whether slopes/effects are assumed common;
- clustered inference and small-sample strategy.

## Within-Variation Workflow

1. Decompose treatment and outcome into within- and between-unit variation.
2. Verify the treatment changes within identifying units and periods.
3. Explain why between-unit variation is confounded and why within changes are cleaner.
4. Add time fixed effects when common shocks affect all units.
5. Add group-specific trends or other controls only when they correspond to a defensible counterfactual—not as automatic robustness.
6. inspect treatment leads/lags, reversals, persistence, and anticipation.
7. identify the implicit weighting under effect heterogeneity.
8. cluster inference at the assignment/dependence level, often—but not mechanically—the unit level.

## What Fixed Effects Remove

A unit fixed effect absorbs every characteristic that is constant within unit over the observed period, whether measured or not. A time fixed effect absorbs shocks common to all units in a period. Neither absorbs:

- unit-specific time-varying shocks;
- treatment responses that alter future treatment;
- spillovers;
- differential measurement changes;
- unobserved trends;
- time-varying composition.

## Multiple Fixed Effects

Two-way fixed effects leave variation net of unit and time means. That algebra is useful across panel models, but its causal interpretation depends on treatment structure. With staggered adoption and heterogeneous effects, a conventional TWFE treatment coefficient can combine problematic already-treated comparisons. Route such designs to Ch18.

## Fixed versus Random Effects

Random-effects models impose structure on unit effects and usually require a credible relation between unit effects and regressors. Efficiency gains do not justify an assumption that changes the identifying comparison. Correlated random-effects or multilevel models can be useful when their structure is explicit.

## Nonlinear Models

High-dimensional fixed effects in logit, Poisson, or other nonlinear models raise incidental-parameter, separation, and interpretation issues. Use model-specific estimators and verify the estimand; demeaning is not generally equivalent to linear FE.

## Variation Audit

| Question | Why it matters |
|---|---|
| Which units switch treatment? | Non-switchers may contribute to nuisance effects but not the treatment contrast |
| When do switches occur? | Common shocks, anticipation, and dynamic effects depend on timing |
| How persistent is treatment? | Reversals and absorbing adoption imply different designs |
| What remains after unit/time residualization? | The coefficient uses residual, not raw, treatment variation |
| Are slopes/effects heterogeneous? | A common coefficient averages with implicit weights |
| Is treatment measured with error within units? | Demeaning can magnify attenuation/noise |
| What time-varying causes remain? | Unit FE cannot absorb them |
| At what level is assignment generated? | This determines clustering and effective sample size |

Time fixed effects absorb shocks common to all units, not shocks that affect units differently. Unit-specific trends can absorb gradual confounding but also remove treatment dynamics and rely on extrapolated trends. Add them only when the untreated-outcome model makes that restriction credible.

## Failure Modes

- Calling any panel regression causal because it has unit and year dummies.
- Ignoring that only switchers identify the effect.
- Using contemporaneous treatment when outcome timing implies lags or anticipation.
- Clustering by convenience rather than assignment/dependence.
- Adding high-dimensional fixed effects that remove nearly all meaningful treatment variation.

## Completion Check

Report the residualized variation, identifying units/times, remaining time-varying threats, and estimand under heterogeneity.

## Technical Skeleton

A two-way fixed-effects model is:

Y_it = α_i + λ_t + βX_it + ε_it.

It removes unit means and common time shocks. The coefficient β is identified by residualized within-unit treatment variation, not by all observations equally.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Suppose individuals choose how often an app sends healthy-eating reminders, while exact reminder days vary. Person fixed effects remove stable differences such as baseline diet preferences. Day/time effects remove shocks shared by everyone.

The design still fails if people request more reminders precisely when an unobserved time-varying health concern also improves eating. Examine what generates day-to-day reminder variation, lag treatment appropriately, and show which individuals actually change exposure. Cluster by the assignment/dependence unit.

If treatment adoption is absorbing and occurs at different dates across people, the question has become staggered DiD. A pooled TWFE coefficient may then use already-treated people as controls and should be replaced with a cohort-aware estimator.

## Connects To

- [Ch17](ch17-event-studies.md): event-time deviations.
- [Ch18](ch18-difference-in-differences.md): comparison-group changes and staggered adoption.
- [Ch23](ch23-under-the-rug.md): timing, measurement, and interference.
