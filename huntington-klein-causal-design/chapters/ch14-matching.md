# Chapter 14: Matching

## Core Idea

Matching and weighting construct a comparison distribution that resembles the target group on observed pre-treatment covariates. They can reduce functional-form dependence and visible imbalance, but they cannot close unmeasured back doors.

## Matching Contract

Specify:

- target estimand: ATE, ATT, or another weighted effect;
- pre-treatment covariates justified by the DGP;
- distance, exact/coarsened, entropy-balancing, or propensity-score method;
- overlap/common-support rule;
- balance targets and acceptable thresholds;
- trimming and the population it removes;
- outcome estimator after design;
- inference accounting for estimated matches or weights.

## Design Workflow

1. Define the target population and estimand.
2. Select pre-treatment covariates before inspecting outcomes.
3. Inspect raw overlap and treatment propensity.
4. Choose the design:
   - exact/coarsened matching for substantively decisive discrete strata;
   - Mahalanobis/distance matching when scale and covariance can be represented well;
   - entropy balancing when explicit moment balance is the design target;
   - propensity weighting when treatment probability provides a useful balancing score.
5. Set calipers, replacement, ratio, trimming, and estimand-specific weights.
6. assess post-design balance and effective sample size without outcome data.
7. Revise or abandon the design when overlap or balance is inadequate.
8. Estimate the effect and propagate design-stage uncertainty.

## Core Assumptions

- **Conditional independence**: measured covariates close all relevant back doors.
- **Positivity/common support**: each target covariate profile has a nonzero chance of each treatment condition needed for the contrast.
- **Consistency and treatment definition**: observed treatment corresponds to the intervention.
- **No post-treatment matching**: matching variables are not caused by treatment.
- **SUTVA/interference condition**: one unit's treatment does not alter another's relevant potential outcome unless modeled.

## Balance and Overlap

Check standardized differences, distributional balance, tails, joint balance, weight concentration, and effective sample size. Predictive performance of the propensity model is not the goal. Extreme weights reveal weak overlap and can dominate results.

Balance on observed covariates is a design diagnostic, not proof of conditional independence. Failed balance can falsify the proposed implementation; successful balance cannot validate unmeasured comparability.

## Estimation

Weighted mean differences, weighted regression, and doubly robust estimators can follow the design. “Doubly robust” means consistency under one of two correctly specified nuisance models under the broader identification assumptions; it is not protection against unmeasured confounding or two arbitrary misspecifications.

Choose inference for the exact matching or weighting estimator. Ordinary nonparametric bootstrap can fail for nonsmooth fixed-neighbor matching; use estimator-valid analytic variance or a resampling procedure justified by the method's theory. For weighting or regression-adjusted pipelines, propagate every estimated design stage with a valid joint procedure.

## Design Choices and Trade-offs

| Choice | Gain | Cost / changed target |
|---|---|---|
| Tight caliper | Better local comparability | More discarded units; narrower population |
| Matching with replacement | Better matches for hard-to-match treated units | A few controls may dominate; dependence changes |
| More neighbors | Greater precision | Worse match quality and potential bias |
| Exact/coarsened matching | Transparent substantive strata | Empty cells and coarsening dependence |
| Entropy balancing | Direct control of selected moments | Extreme weights if constraints strain support |
| IPW | Flexible estimand weighting | Instability near propensity 0 or 1 |
| Trimming | Reduces extrapolation and extreme weights | Redefines the target population |
| Outcome regression after matching | Removes residual modeled imbalance | Adds outcome-model assumptions |

Report balance before and after design, but tune decisions without consulting the outcome. When several matching approaches all balance measured variables, choose using target-population clarity, weight stability, and measurement quality—not the largest final effect.

## Failure Modes

- Matching on instruments, colliders, or post-treatment variables.
- Using the outcome to tune the match.
- Keeping all observations despite no support.
- Treating propensity-score proximity as covariate balance.
- Ignoring uncertainty from estimated weights.
- Applying an ordinary bootstrap to a matching estimator whose nonsmooth assignment makes that bootstrap invalid.
- Reporting an ATT design as a population ATE.

## Completion Check

Finish only when the weighted target population, discarded support, covariate balance, effective sample size, and residual unmeasured-confounding assumption are explicit.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

The chapter considers whether being late on a credit-card payment in April affects being late again in September. April bill size is a pre-treatment common cause: larger balances can raise both April and later delinquency.

A one-variable illustration matches late and on-time payers on April bill size. A real design would add every defensible pre-April common cause, inspect overlap, and choose the target:

- matching controls to resemble late payers targets an ATT;
- weighting both groups to a common population can target an ATE if overlap supports it.

After matching, compare bill-size and other covariate distributions—not only propensity scores. If high-risk late payers have no comparable on-time payers, trim them and state that the estimand now excludes that region. If the final weighted estimate uses regression adjustment, propagate the full matching/weighting and outcome-estimation pipeline with an uncertainty procedure valid for that estimator.

## Connects To

- [Ch10](ch10-treatment-effects.md): estimand-specific weights.
- [Ch13](ch13-regression.md): outcome adjustment after design.
- [Ch21](ch21-partial-identification.md): sensitivity to unmeasured confounding.
