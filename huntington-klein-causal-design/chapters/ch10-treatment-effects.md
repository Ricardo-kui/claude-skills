# Chapter 10: Treatment Effects

## Core Idea

There is rarely one universal effect. The design and estimator weight heterogeneous unit-level effects into a particular estimand; the resulting average may differ from the policy-relevant target.

## Estimand Map

- **ATE**: average effect in the target population.
- **ATT**: average effect among treated units.
- **ATU/ATC**: average effect among untreated/control units.
- **CATE**: average effect conditional on characteristics.
- **ITT**: effect of treatment assignment or encouragement, regardless of receipt.
- **TOT**: effect of treatment receipt among treated under the relevant design.
- **LATE**: average effect for units whose treatment changes because of an instrument, under IV assumptions.
- **Local RDD effect**: effect for units at the cutoff.
- **Sample effect versus population effect**: differs when sampling or design weights change representation.

Use the exact terminology supported by the design; do not relabel a local or selected effect as “the effect.”

## Estimand Contract

State:

1. treatment versions and comparison level;
2. outcome and time horizon;
3. target population;
4. weighting of units, cohorts, times, or treatment propensities;
5. effect heterogeneity allowed;
6. estimand delivered by the design;
7. assumptions needed to transport it to another population or intervention.

## Design–Estimand Alignment

- Matching or weighting can target ATE or ATT depending on weights and support.
- IV usually targets a complier-specific LATE, not the population ATE.
- RDD targets units near the cutoff.
- DiD with staggered timing can aggregate cohort-time effects using explicit weights.
- Regression coefficients under heterogeneity may encode implicit and sometimes undesirable weights.

## Weighting Questions

For any reported average, ask:

1. Which units receive positive weight?
2. Can weights be negative or concentrated?
3. Do weights depend on treatment propensity, cohort size, instrument responsiveness, or distance to a cutoff?
4. Are the highest-weight units representative of the policy target?
5. Does aggregation mix treatment versions or effect horizons?
6. Would reweighting to the target population require extrapolation?

Report heterogeneity at a pre-specified, supported level. Subgroup effects discovered after inspecting estimates need held-out or confirmatory evidence.

## Failure Modes

- **Label inflation**: calling any causal estimate an ATE.
- **Population drift**: discussing effects for all firms when identification comes from a narrow changing or local subgroup.
- **Treatment-version collapse**: combining meaningfully different doses or implementations.
- **Aggregation opacity**: averaging dynamic or cohort-specific effects without showing weights.
- **Policy extrapolation**: assuming a local estimate transports without a mechanism or sampling argument.

## Completion Check

Report who is represented, which contrast is averaged, how weights arise, and what population remains outside the evidence.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

A voluntary management-training program has larger effects for managers who were willing to enroll. A matched analysis targeting treated participants estimates an ATT. An encouragement instrument based on randomly timed invitations identifies a LATE for managers whose enrollment responds to timing. A company-wide rollout question instead asks for an ATE across all eligible managers.

These are not interchangeable:

- ATT answers whether the program helped those who took it;
- LATE answers whether it helped invitation-responsive compliers;
- ATE answers what universal availability/participation would do on average.

Even with unbiased estimation, moving from LATE or ATT to ATE requires assumptions about effect heterogeneity and treatment take-up. Report observed support and compare complier/participant characteristics with the policy population before making the transport claim.

## Connects To

- [Ch14](ch14-matching.md): target-population weights.
- [Ch18](ch18-difference-in-differences.md): cohort-time treatment effects.
- [Ch19](ch19-instrumental-variables.md): ITT and LATE.
- [Ch20](ch20-regression-discontinuity.md): cutoff-local effects.
