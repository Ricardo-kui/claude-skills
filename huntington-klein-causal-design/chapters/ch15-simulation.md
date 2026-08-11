# Chapter 15: Simulation

## Core Idea

Simulation makes assumptions executable. By generating data from a known DGP and repeatedly applying an estimator, the researcher can study bias, variance, coverage, power, and failure under controlled violations.

## Simulation Contract

Define:

- target estimand and true value;
- DGP equations and timing;
- sample size, clusters, periods, and treatment assignment;
- heterogeneity, nonlinearity, missingness, measurement error, and dependence;
- estimator and inference procedure;
- scenarios that vary one threat at a time;
- repetitions and Monte Carlo uncertainty;
- performance metrics.

## Workflow

1. Write the minimal DGP that captures the design.
2. Generate one dataset and verify distributions and causal relations.
3. Apply the exact estimator and standard-error procedure planned for the real study.
4. repeat across independent simulated samples.
5. compute bias, RMSE, empirical standard deviation, average reported SE, interval coverage, rejection rate, and convergence/failure rate.
6. Vary sample size, effect heterogeneity, treatment prevalence, overlap, confounding, clustering, and misspecification.
7. Compare candidate estimators on identical simulated draws.
8. explain which conclusions depend on DGP choices.

## Breaking Things Deliberately

Use a scenario grid rather than one favorable DGP. Examples:

- weaken overlap;
- add an unmeasured common cause;
- make treatment effects heterogeneous;
- introduce serial or within-cluster dependence;
- allow anticipation or staggered adoption;
- misspecify nonlinear trends;
- add outcome/treatment measurement error;
- violate an instrument's exclusion restriction;
- permit manipulation around an RDD cutoff.

A simulation demonstrates behavior under the simulated worlds—not universal estimator superiority.

## Power Analysis

Power depends on effect size, treatment variation, residual variation, sample size/effective clusters, design, and inference. Simulate the assignment and estimator actually planned. For clustered or panel designs, varying the number of observations within a few clusters is not equivalent to increasing the number of independent clusters.

Report power curves or minimum detectable effects over plausible parameter ranges rather than one assumed effect.

## Bootstrap

Bootstrap by resampling the independent units implied by the design:

- observation pairs for independent cross-sections;
- clusters for clustered assignment/dependence;
- blocks or time-series methods for serial dependence;
- the entire matching/weighting/model-selection pipeline when those stages are estimated.

Set reproducible seeds outside iteration functions so repeated samples differ while the run remains reproducible.

## Performance Metrics

| Metric | Question answered |
|---|---|
| Bias | Is the estimator centered on the target? |
| Empirical SD | How much do estimates vary across samples? |
| Mean reported SE | Does the uncertainty estimator track that variation? |
| RMSE | What is the combined bias–variance loss? |
| Coverage | Do nominal intervals contain the truth at the claimed rate? |
| Type I error | How often is a true null rejected? |
| Power | How often is a specified nonzero effect detected? |
| Failure rate | How often does estimation not converge or return unusable results? |
| Effective sample/clusters | What independent information actually supports the estimate? |

Separate a simulation used for estimator validation from a simulation used for application-specific power. The former varies DGP failures broadly; the latter must reproduce the planned assignment, missingness, clustering, and analysis pipeline. Archive scenario parameters with results so a favorable graph cannot be detached from the assumptions that produced it.

## Failure Modes

- Choosing a DGP that guarantees the preferred estimator wins.
- Reporting Monte Carlo noise as a substantive difference.
- Simulating IID data for clustered or serial designs.
- Holding nuisance models correctly specified in every scenario.
- Treating bootstrap as valid regardless of dependence or estimator nonregularity.

## Completion Check

A simulation claim is complete when the DGP, true estimand, scenario grid, repetitions, Monte Carlo uncertainty, and limitations are reproducible.

## Technical Artifact

A reusable simulation loop is:

1. generate data from a declared DGP;
2. estimate the target with every candidate method;
3. store the estimate, SE, interval, and failure flag;
4. repeat R times;
5. summarize bias, RMSE, coverage, and rejection;
6. repeat over a scenario grid.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

The chapter's “Agus estimator” keeps only extreme treatment values before regression, hoping greater treatment variance reduces standard errors. Simulate data where the true slope is known and compare this estimator with ordinary OLS on the same draws.

The extreme-value estimator may appear more precise under a correctly linear DGP, but selection on extremes can behave badly when the relationship is nonlinear, treatment has measurement error, or extreme observations have different error variance. The useful result is not “Agus wins” or “OLS wins.” It is a map of where bias, variance, and coverage change.

Add adversarial scenarios before drawing conclusions. Report Monte Carlo standard errors so a small difference across 1,000 iterations is not mistaken for a stable advantage.

## Connects To

Use this chapter to stress-test [Regression](ch13-regression.md), [Matching](ch14-matching.md), [DiD](ch18-difference-in-differences.md), [IV](ch19-instrumental-variables.md), and [RDD](ch20-regression-discontinuity.md).
