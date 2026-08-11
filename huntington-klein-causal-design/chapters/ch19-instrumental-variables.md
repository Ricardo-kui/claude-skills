# Chapter 19: Instrumental Variables

## Core Idea

Instrumental variables (IV) isolate treatment variation induced by an instrument. The design can address unmeasured treatment–outcome confounding only if the instrument shifts treatment, has no open path to the outcome except through treatment, and supports the claimed local estimand.

## IV Contract

State:

- instrument, endogenous treatment, outcome, and controls;
- institutional source of instrument variation;
- first-stage population and strength;
- independence/as-if-random basis;
- exclusion restriction;
- monotonicity/no-defier argument when interpreting LATE;
- affected complier population;
- weak-instrument-robust inference;
- sensitivity to plausible exclusion/validity violations.

## Assumptions

1. **Relevance**: the instrument changes treatment.
2. **Independence/validity**: instrument variation is not connected to unblocked causes of the outcome.
3. **Exclusion**: the instrument affects the outcome only through the modeled treatment pathway.
4. **Monotonicity**: the instrument does not push some units' treatment in the opposite direction when a complier LATE is claimed.
5. **SUTVA and well-defined versions**: instrument and treatment versions are coherent and spillovers are addressed.

Controls may make an instrument conditionally valid, but that claim needs its own DGP and overlap.

## Estimation Workflow

1. Show the assignment mechanism and DAG.
2. report the first stage, its units, shape, and uncertainty.
3. estimate reduced form and 2SLS/IV effect using one integrated procedure; do not manually regress on fitted treatment with naive second-stage SEs.
4. define the IV estimand and complier group.
5. use weak-instrument-robust confidence sets or tests.
6. test observable implications and negative controls tied to validity.
7. probe plausible direct effects or residual confounding using sensitivity/bounds.
8. align clustering with instrument assignment.

## Weak Instruments

A first-stage p-value or rule-of-thumb F threshold is insufficient. Strength requirements depend on the number of instruments/endogenous variables, desired bias, and inference. Report relevant partial/robust diagnostics and prefer weak-IV-robust inference such as Anderson–Rubin-type confidence sets when applicable. LIML or related estimators may reduce weak-instrument bias but do not validate the instrument.

## Validity Evidence

Overidentification or endogeneity tests cannot prove validity; they may have low power and test only relative restrictions. The main evidence is institutional: why instrument assignment is unrelated to potential outcomes and why no direct pathway exists. Use balance, placebo outcomes, timing, mechanism tests, and alternative instruments as falsification—not certification.

## Nonlinear and Panel Settings

Do not use a nonlinear first stage followed by an arbitrary second stage (“forbidden regression”). Use estimators designed for the nonlinear target. With fixed effects, verify that the instrument has within variation and remains valid after conditioning.

## Evidence Matrix

| IV component | Evidence to provide | What remains untestable |
|---|---|---|
| Assignment/independence | Institutional rule, balance, timing, no sorting | Independence from all potential outcomes |
| Relevance | First-stage magnitude, partial/robust diagnostics, heterogeneity | Stability outside observed support |
| Exclusion | Enumerated direct pathways, placebo outcomes, mechanism evidence | Every unmeasured direct channel |
| Monotonicity | Behavioral/institutional argument, subgroup first stages | Individual no-defier status |
| LATE population | Complier-characteristic analysis or weighting interpretation | Effects for never-/always-takers |
| Inference | Weak-IV-robust confidence sets and assignment clustering | Precision under invalidity |
| Validity sensitivity | Bounds under calibrated direct effects/confounding | Correct calibration range |

Show the reduced-form effect even when the 2SLS estimate is the target. It reveals the policy effect of the instrument itself and prevents a small first stage from turning a modest reduced form into an apparently dramatic causal estimate without context.

## Failure Modes

- Selecting an instrument because it predicts treatment strongly.
- Describing exclusion in one sentence without enumerating direct pathways.
- Treating LATE as ATE.
- Instrument proliferation without a substantive validity argument.
- Dropping a weak-IV project only after observing a low F, creating selection.
- Reporting conventional 2SLS intervals despite weak identification.
- Controlling for treatment or a collider to “test” exclusion.

## Completion Check

An IV claim is complete only when the first stage, reduced form, validity story, exclusion threats, monotonicity, complier population, and weak-IV-robust inference are all visible.

## Technical Skeleton

First stage: X_i = πZ_i + W_i′γ + v_i.

Reduced form: Y_i = ρZ_i + W_i′δ + u_i.

In the single-instrument linear case, the Wald ratio ρ/π motivates the IV estimate. Estimate and infer through a valid IV procedure, not a manually fitted second-stage regression.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Random assignment to judges with different sentencing tendencies can instrument actual incarceration. Relevance requires judge assignment to shift incarceration. Independence requires assignment to be effectively random conditional on the court process. Exclusion requires judge assignment not to affect the outcome through other channels such as case handling, fees, or program placement. Monotonicity requires harsher judges not to reduce incarceration for some defendants while increasing it for others in the relevant comparison.

The estimate is local to defendants whose treatment changes with judge tendency. Show assignment balance, first-stage heterogeneity, reduced form, weak-IV-robust intervals, and direct-channel threats. A large first-stage F cannot rescue nonrandom assignment or a violated exclusion restriction.

## Connects To

- [Ch9](ch09-finding-front-doors.md): isolate cleaner variation.
- [Ch10](ch10-treatment-effects.md): LATE and ITT.
- [Ch20](ch20-regression-discontinuity.md): fuzzy RDD as IV.
- [Ch21](ch21-partial-identification.md): bounds for imperfect validity.
