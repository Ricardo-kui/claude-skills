# Chapter 20: Regression Discontinuity

## Core Idea

Regression discontinuity (RDD) compares units just on either side of a treatment-assignment cutoff. It identifies a local effect when potential outcomes would vary smoothly through the cutoff absent treatment and units cannot precisely manipulate assignment in a way that changes comparability.

## RDD Contract

Specify:

- running variable, cutoff, and assignment rule;
- sharp, fuzzy, kink, geographic, or multi-cutoff design;
- treatment jump at the cutoff;
- local target population and estimand;
- continuity/no-precise-manipulation argument;
- bandwidth and polynomial order;
- kernel/weights and robust bias-corrected inference;
- mass points, heaping, clustering, and measurement precision.

## Workflow

1. Verify the institutional cutoff rule and who can influence the running variable.
2. Plot treatment probability and outcome against the centered running variable using transparent bins plus raw support.
3. inspect density, heaping, gaps, and sorting near the cutoff.
4. check pre-treatment covariates and placebo outcomes for discontinuities.
5. estimate local polynomials separately on each side using a defensible bandwidth.
6. use heteroskedasticity-robust and bias-aware inference appropriate to the estimator.
7. report sensitivity to bandwidth, polynomial order, kernel, donut exclusions, and discrete-score handling.
8. interpret the estimate only for units at the cutoff unless transport is separately defended.

## Sharp and Fuzzy Designs

- **Sharp RDD**: treatment status changes deterministically at the cutoff.
- **Fuzzy RDD**: treatment probability jumps but compliance is incomplete. Treat cutoff assignment as an instrument and defend relevance, exclusion, independence/continuity, and monotonicity. The result is local to cutoff compliers.

## Diagnostics

- density discontinuity/manipulation test;
- covariate continuity;
- placebo cutoffs and outcomes;
- bandwidth sensitivity;
- graphical inspection of raw support and fitted curves;
- first-stage jump for fuzzy RDD;
- influence and effective observations near the cutoff.

No single diagnostic validates continuity. A density test can miss manipulation; covariate continuity can fail by chance or multiplicity.

## Functional Form

Prefer local low-order polynomials with data-informed bandwidths. Global high-order polynomials can behave erratically and create artificial jumps. Narrower bandwidths reduce reliance on smoothness away from the cutoff but increase variance; wider bandwidths improve precision while increasing functional-form risk.

## Running-Variable Problems

Coarse scores, mass points, digit preference, and measurement error reduce the local-randomization intuition. Do not treat many identical score values as independent continuous support. Adjust inference and design claims to the number and spacing of unique values.

## RDD Reporting Table

| Element | Minimum report |
|---|---|
| Assignment rule | Exact threshold, implementation, exceptions, awareness |
| Running variable | Construction, precision, unique values, heaping |
| Treatment jump | Graph and estimate at cutoff |
| Outcome graph | Raw/binned data and separate-side fits |
| Bandwidth | Selection method plus sensitivity |
| Polynomial/kernel | Local order, weighting, and rationale |
| Inference | Bias correction, robust SE, clustering/mass-point handling |
| Manipulation | Density plus institutional evidence |
| Placebos | Covariates, outcomes, and fake cutoffs with multiplicity context |
| Estimand | Sharp/fuzzy/kink and local population |

“Donut” RDDs that exclude observations closest to the cutoff can address heaping or manipulation only by changing the identifying comparison. Explain why excluded values are contaminated and why the remaining gap still supports a local extrapolation. Geographic boundaries require special attention to sorting, spatial spillovers, and correlated outcomes.

## Failure Modes

- Choosing cutoff, bandwidth, or polynomial after seeing the desired estimate.
- Interpreting an RDD effect as population-wide.
- Assuming “administrative rule” means no manipulation.
- Using time as a running variable without separating RDD from interrupted time-series threats.
- Hiding a weak fuzzy first stage.
- Treating balance and density-test passes as proof.

## Completion Check

Report the assignment rule, local population, first-stage jump, bandwidth, support, manipulation evidence, functional-form sensitivity, and local estimand.

## Technical Skeleton

For a centered running variable R−c, estimate separate local functions on each side and interpret the discontinuity at c. In a fuzzy design, use crossing the cutoff as an instrument for treatment receipt.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

A grant is awarded when an application score is at least 80. Compare applicants near 80, not all applicants. First verify whether evaluators or applicants can precisely manipulate scores and whether other programs use the same threshold.

Plot score density, grant receipt, baseline covariates, and outcomes. Fit low-order local polynomials on each side using a justified bandwidth and robust bias-corrected inference. Repeat across defensible bandwidths and placebo cutoffs.

If only 70% of applicants above 80 receive the grant and some below do, the design is fuzzy. The cutoff identifies a local complier effect under IV assumptions. If scores are integer-valued with few support points, acknowledge that the continuous local approximation is strained and adapt inference rather than hiding mass points with a smooth plot.

## Connects To

- [Ch17](ch17-event-studies.md): time cutoffs and interrupted series.
- [Ch19](ch19-instrumental-variables.md): fuzzy RDD.
- [Ch21](ch21-partial-identification.md): sensitivity to continuity or manipulation.
