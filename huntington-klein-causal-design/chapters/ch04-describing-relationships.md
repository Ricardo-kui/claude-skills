# Chapter 4: Describing Relationships

## Core Idea

A relationship describes how the distribution of one variable changes with another. Conditional means, smoothers, and fitted lines summarize association; causal interpretation requires a separate identification argument.

## Relationship Contract

For each reported relationship, state:

- whether it is unconditional or conditional;
- the conditioning set and why it was chosen;
- the functional form used for summary;
- the part of the support supplying the comparison;
- whether the estimand is descriptive, predictive, or causal.

## Workflow

1. Plot raw data and show conditional distributions or means before imposing a line.
2. Compare flexible summaries with the proposed functional form.
3. Inspect support: avoid interpreting fitted values where observations are absent.
4. Add controls only when the DGP says conditioning closes a bad path or improves precision without changing the target effect.
5. Interpret residuals as unexplained relative to the fitted model—not as variation automatically purged of confounding.
6. Separate uncertainty about sampling from uncertainty about model form and identification.

## Controlling for a Variable

Conditioning compares observations at common values of controls. It can close confounding paths, but it can also:

- block a mediator and change a total effect into a direct-effect estimand;
- open a collider path;
- restrict the comparison to sparse or non-overlapping regions;
- amplify measurement error or functional-form dependence.

A “controls included” statement is therefore incomplete without a causal reason for each variable.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

The chapter moves from conditional distributions and local conditional means to line fitting. The lesson is not that regression makes the relationship causal; regression offers a compact approximation to conditional means. The DGP determines whether that conditional relationship answers the causal question.

## Descriptive-to-Causal Ladder

1. **Joint distribution**: How do X and Y co-occur?
2. **Conditional distribution**: How does Y vary across X within specified Z?
3. **Modeled relationship**: What functional summary approximates that conditional distribution?
4. **Identified contrast**: Why does the remaining X variation represent intervention rather than rival paths?
5. **Causal estimand**: Which population-weighted effect does the model recover?

Stop at the highest rung justified. A regression table can answer rung 3 even when rungs 4–5 fail.

## Failure Modes

- Extrapolating a linear effect beyond observed support.
- Reading a coefficient as a universal effect under interactions or nonlinear transformations.
- Treating a high model-fit statistic as causal credibility.
- Using a long control list as a substitute for a diagram or assignment story.

## Connects To

- [Ch8](ch08-causal-paths.md): decide what conditioning opens or closes.
- [Ch13](ch13-regression.md): estimate conditional relationships.
- [Ch23](ch23-under-the-rug.md): model and measurement uncertainty.
