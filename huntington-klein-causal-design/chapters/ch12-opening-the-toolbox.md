# Chapter 12: Opening the Toolbox

## Core Idea

Select a method because its identifying comparison matches the DGP and estimand. The estimator executes a design; it does not create one.

## Method-Selection Sequence

1. State the question and estimand.
2. Draw or narrate the DGP.
3. Identify the source of treatment variation.
4. Determine the comparison licensed by that variation.
5. List assumptions and diagnostics.
6. Select the design family.
7. Select an estimator appropriate to treatment timing, heterogeneity, support, and data structure.
8. Select inference appropriate to assignment and dependence.
9. verify current software implementation.
10. report limitations and the population actually identified.

## Toolbox Families

| Problem structure | Candidate chapter |
|---|---|
| Rich pre-treatment covariates plausibly close back doors | Regression (Ch13), Matching (Ch14) |
| Need to understand estimator behavior or power | Simulation (Ch15) |
| Time-invariant unit confounding with within-unit change | Fixed Effects (Ch16) |
| Outcome deviations around an event | Event Studies (Ch17) |
| Treated and comparison groups with credible counterfactual changes | DiD (Ch18) |
| Exogenous encouragement shifts endogenous treatment | IV (Ch19) |
| Assignment changes at a threshold | RDD (Ch20) |
| Point identification requires indefensible assumptions | Partial Identification (Ch21) |
| Advanced/alternative data structures | Gallery of Rogues (Ch22) |

## Execution Boundary

The source chapter provides R, Stata, and Python code examples. Treat them as conceptual illustrations. Before live execution:

- verify package versions and estimator defaults;
- use design-specific diagnostics;
- reproduce the analysis from a clean script;
- align standard errors with assignment and dependence;
- prefer the machine's current Stata and causal-analysis skills for implementation.

## Failure Modes

- Choosing a method by dataset shape alone.
- Using software defaults as methodological decisions.
- Reporting the simplest textbook estimator when treatment timing or heterogeneity violates its interpretation.
- Confusing a successfully executed command with a successfully identified effect.

## Completion Check

A method is selected only after the design-to-estimator mapping and inference plan are explicit.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

A researcher has firm panel data and a policy adopted by states at different times. The data structure suggests fixed effects, but the assignment process suggests staggered DiD. The workflow is:

1. define state adoption cohorts and firm exposure;
2. identify never-treated or not-yet-treated comparisons;
3. state cohort-specific parallel trends and no anticipation;
4. target ATT(g,t), not a generic panel coefficient;
5. use a cohort-aware DiD estimator;
6. cluster at the policy-assignment level;
7. audit spillovers across states and firms;
8. aggregate cohort-time effects transparently.

The method follows from the assignment and comparison, not from the fact that the data are a panel. A conventional firm-and-year fixed-effects regression is a benchmark at most, not the default causal estimator.

## Connects To

Use the root [cheatsheet](../cheatsheet.md) for selection and [patterns](../patterns.md) for the full identification contract.
