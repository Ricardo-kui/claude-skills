# Chapter 18: Difference-in-Differences

## Core Idea

Difference-in-differences (DiD) identifies effects by comparing treated-group outcome changes with a credible untreated counterfactual change. Parallel trends is a counterfactual assumption, not something a pre-trend significance test can prove.

## DiD Contract

State:

- treatment definition, adoption date, reversals, and anticipation window;
- treated cohorts and eligible control groups;
- outcome and event-time horizon;
- target cohort-time effects and aggregation weights;
- conditional or unconditional parallel-trends assumption;
- no-anticipation and interference conditions;
- estimator appropriate to treatment timing and heterogeneity;
- assignment-level inference.

## Design Workflow

1. Plot group/cohort outcomes and treatment timing.
2. identify never-treated and not-yet-treated comparison observations.
3. explain institutionally why their untreated changes proxy treated units' counterfactual changes.
4. define ATT(g,t): the effect for cohort g at time t.
5. estimate cohort-time effects using a modern staggered-adoption method.
6. aggregate by event time, cohort, calendar time, or overall ATT with transparent weights.
7. examine anticipation, pre-treatment estimates, composition, spillovers, and concurrent shocks.
8. cluster at the treatment-assignment level and use small-cluster corrections when needed.
9. report support: which cohorts and horizons are actually identified.

## Estimator Rule

- A simple two-group/two-period or common-adoption design can use the standard DiD contrast or its equivalent fixed-effects regression.
- For staggered adoption, do not default to an uncorrected TWFE treatment coefficient or conventional TWFE event study.
- Prefer cohort-aware estimators such as Callaway–Sant'Anna group-time effects, interaction-weighted/event-study approaches, or Borusyak–Jaravel–Spiess imputation, selected to match the data and assumptions.
- A Goodman–Bacon decomposition can diagnose where a legacy TWFE estimate gets its comparisons; it does not repair the design.

## Parallel Trends Evidence

Use pre-treatment estimates and plots as falsification evidence:

- assess magnitudes and confidence/equivalence regions, not only p-values;
- examine power to detect substantively important deviations;
- look for differential trends, compositional changes, and anticipation;
- use negative-control outcomes, fake adoption dates, alternative valid comparison groups, and covariate-adjusted estimators when justified.

A flat or insignificant pre-period does not verify post-period parallel trends.

## Covariates

Covariates should support a conditional parallel-trends argument. Prefer baseline or properly modeled pre-treatment covariates. Time-varying covariates affected by treatment are post-treatment controls; generic regression adjustment can bias the target effect. Use estimators that explicitly support the intended covariate structure.

## Dynamic Effects

Event-time profiles can show onset, growth, and decay, but horizons may be supported by different cohorts. Display cohort composition and avoid interpreting changing weights as dynamics. Bin distant leads/lags only with a substantive reason and disclose what is combined.

## Design Cases

| Treatment timing | Recommended logic |
|---|---|
| Two groups, two periods | Direct 2×2 DiD contrast |
| Multiple periods, one common adoption date | Standard DiD with dynamic effects if needed |
| Staggered absorbing adoption | Cohort-time estimator with never/not-yet controls |
| Treatment reversals | Use a design explicitly supporting reversals; absorbing-treatment estimators do not apply |
| Varying intensity | Define dose and counterfactual; binary adoption DiD may not identify it |
| Universal eventual adoption | Not-yet-treated controls may identify early horizons only |
| Spatial/network spillovers | Redefine exposure/control groups or model interference |

When selecting a modern estimator, compare:

- eligible control groups;
- conditional versus unconditional parallel trends;
- support for covariate adjustment;
- treatment-effect aggregation;
- anticipation handling;
- unbalanced-panel behavior;
- inference and software implementation.

Present cohort-time support next to the event-time plot. Later horizons often contain only early adopters, so apparent dynamics may be changes in cohort composition.

## Failure Modes

- Already-treated units serving as controls under heterogeneous effects.
- Inferring validity from a nonsignificant joint pre-trend test.
- Ignoring anticipation, treatment reversal, or varying treatment versions.
- Selecting a control group for similar levels rather than credible untreated changes.
- Adding treatment-induced controls.
- Reporting a pooled coefficient without cohort-time weights.
- Treating clustered SEs as a remedy for biased comparisons.

## Completion Check

A DiD result is complete only when the comparison cohorts, cohort-time estimands, aggregation weights, parallel-trends basis, anticipation window, and inference are visible.

## Source and Frontier Boundary

Huntington-Klein (2025) covers Callaway–Sant'Anna and imputation approaches and warns about rollout TWFE. Because staggered DiD remains active, verify current method and software guidance before publication or execution.

## Technical Artifact

For cohort g and time t, target ATT(g,t): the treated cohort's observed outcome minus its estimated untreated counterfactual. Aggregate only after estimating valid cohort-time effects, with weights tied to the target question.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

Counties receive broadband in 2001, 2002, or 2003. New-business formation is the outcome. A conventional TWFE regression compares newly treated counties not only with untreated counties but also with counties treated earlier. If effects grow over time, those already-treated comparisons contaminate the pooled coefficient.

Instead:

1. create adoption cohorts;
2. use never-treated or not-yet-treated counties as controls where eligible;
3. estimate ATT(g,t);
4. inspect pre-treatment estimates for each cohort;
5. aggregate by years since adoption with cohort composition shown;
6. cluster by the policy-assignment unit;
7. test spillovers into neighboring counties and anticipation by firms.

A pre-period graph without obvious differences is supportive but does not establish parallel trends. Add a calibrated sensitivity analysis for differential trends.

## Connects To

- [Ch14](ch14-matching.md): construct comparison-group weights.
- [Ch16](ch16-fixed-effects.md): within and time variation.
- [Ch17](ch17-event-studies.md): event-time displays.
- [Ch21](ch21-partial-identification.md): sensitivity to trend violations.
