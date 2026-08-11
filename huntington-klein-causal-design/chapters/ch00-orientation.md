# Orientation: The Effect

## Core Idea

Treat causal inference as a reasoning and research-design problem before treating it as a statistical task. The target is not a coefficient but a credible answer to what would happen to an outcome if a treatment changed in a specified population and context.

## Author's Commitments

- Start from a causal question and a theory-informed account of the data-generating process (DGP).
- Use observational data only after identifying which variation can answer the question.
- Put institutional and contextual knowledge ahead of estimator sophistication.
- Use causal diagrams as a practical language for assumptions, while recognizing that this book uses a deliberately light version of structural causal models.
- Learn execution after identification logic; code cannot repair an unidentified design.

## Scope of the Book

Part I develops research questions, descriptions, identification, causal diagrams, adjustment logic, natural experiments, estimands, and robustness. Part II covers regression, matching, simulation, fixed effects, event studies, difference-in-differences, instrumental variables, regression discontinuity, partial identification, and selected advanced methods.

The treatment is intuition-first. It does not replace formal potential-outcomes notation, estimator proofs, asymptotic theory, or a current method-specific review.

## Use This Orientation When

- A request jumps straight from a dataset to a regression specification.
- A statistically significant estimate is being mistaken for causal evidence.
- The available method is driving the question rather than the reverse.
- The user needs to evaluate a causal claim without reproducing the analysis.

## Completion Check

Before proceeding to a method, state:

1. the causal contrast;
2. the unit, population, setting, and time;
3. why the observed variation could approximate that contrast;
4. the identifying assumptions;
5. what evidence could reveal a failed assumption.

## Source Boundary

This skill synthesizes Huntington-Klein (2025). For publication-facing work, combine it with current design-specific literature and software documentation. In particular, use modern staggered-adoption DiD estimators rather than an uncorrected TWFE default.

## Connects To

- [Ch1](ch01-designing-research.md) for design before analysis.
- [Ch5](ch05-identification.md) for variation and identification.
- [Ch12](ch12-opening-the-toolbox.md) for moving from concept to implementation.
- [Ch23](ch23-under-the-rug.md) for hidden threats that remain after estimation.
