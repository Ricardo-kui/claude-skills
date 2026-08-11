# Chapter 3: Describing Variables

## Core Idea

Quantitative evidence begins with distributions. Variable type, support, missingness, skew, mass points, and sampling process constrain every later causal estimand and estimator.

## Description Contract

For each treatment, outcome, control, running variable, instrument, and clustering unit, record:

- construct and operational definition;
- unit and observation level;
- variable type: continuous, count, binary, categorical, ordinal, or duration;
- empirical support and impossible values;
- distribution shape, mass points, outliers, and transformations;
- missingness and whether zero, absence, and missing are distinct;
- sample versus target-population distribution;
- measurement timing relative to treatment and outcome.

## Workflow

1. Inspect frequency tables or density/histogram views appropriate to the variable type.
2. Use summaries that match the distribution: mean and standard deviation when informative; quantiles, median, IQR, or category shares when they better describe the data.
3. Compare distributions across treatment status, time, cohort, and sample-inclusion stages.
4. Examine whether transformations change the estimand or only the functional representation.
5. Distinguish the observed sample distribution from the theoretical or population distribution it is intended to represent.

## Why It Matters for Causal Design

- Sparse treatment support can make overlap assumptions implausible.
- Extreme skew can make average effects depend on a few observations.
- A mass at a policy cutoff may signal manipulation in RDD.
- Limited within-unit variation can make fixed-effects estimates uninformative.
- Missing treatment or outcome values can create selection paths.

## Failure Modes

- Reporting only a mean for a highly skewed or multimodal variable.
- Treating an ordinal scale as interval-valued without defending the interpretation.
- Winsorizing or trimming without showing how the target population changes.
- Logging zero or negative values through undocumented recoding.
- Calling a convenience sample representative because its N is large.

## Completion Check

A variable is ready for design work when its observed support, timing, measurement process, and relation to the target construct are explicit.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

Suppose a study examines the effect of regulatory inspections on firm safety incidents. Before modeling, inspect:

- **Inspections**: count, with many zeros and repeat inspections triggered by prior incidents.
- **Incidents**: count with a long right tail; zero may mean safety or underreporting.
- **Firm size**: continuous and skewed; affects exposure time and detection.
- **Safety score**: ordinal, recorded only for inspected firms.
- **Exit**: firms leaving the panel may have failed, merged, or stopped reporting.

A mean-only table would hide assignment, zero inflation, selective measurement, and attrition. Plot distributions by treatment timing, normalize incidents by a defensible exposure measure if the estimand calls for it, and show how much within-firm variation remains. This description can reveal that the apparent outcome is partly a reporting process and that the observed score is post-treatment, changing the later DAG and estimator.

## Connects To

- [Ch4](ch04-describing-relationships.md): conditional distributions and relationships.
- [Ch10](ch10-treatment-effects.md): population weighting and heterogeneity.
- [Ch14](ch14-matching.md): overlap and balance.
- [Ch23](ch23-under-the-rug.md): construct validity and missingness.
