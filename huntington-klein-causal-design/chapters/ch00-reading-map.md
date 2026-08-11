# Reading Map

## Core Idea

Load only the branch needed for the current causal-design problem. The chapter sequence is cumulative: method chapters assume the question, estimand, DGP, and identifying variation have already been clarified.

## Routes

| Need | Read first | Then |
|---|---|---|
| Form a causal research question | Ch1–2 | Ch5, Ch10 |
| Describe data without causal overclaiming | Ch3–4 | Ch13 |
| Build or audit a DAG | Ch5–8 | Ch9 or a method chapter |
| Find quasi-experimental variation | Ch9 | Ch16–20 |
| Choose an estimand | Ch10 | the selected method chapter |
| Stress-test uncertain assumptions | Ch11 | Ch15, Ch21, Ch23 |
| Use covariate adjustment | Ch8 | Ch13–14 |
| Use panel/time variation | Ch16 | Ch17–18 |
| Use an instrument | Ch9 | Ch19 |
| Use a cutoff | Ch9 | Ch20 |
| Report bounded rather than point-identified conclusions | Ch21 | Ch23 |

## Reading Depth

- **Concept**: Read the Core Idea, Identification Contract, and Failure Modes.
- **Design**: Also read Workflow, Diagnostics, and the connected design chapters.
- **Execution**: Verify current software syntax and estimator guidance outside this book before running code.
- **Audit**: Start from the claimed estimand and work backward through assumptions to the actual source of variation.

## Non-Substitutions

- Regression is not a research design.
- Fixed effects are not automatically DiD.
- An event-study plot is not automatically a causal event study.
- Covariate balance is not proof of no unobserved confounding.
- A strong first stage is not proof of instrument validity.
- A smooth RDD plot is not proof against manipulation.
- Robustness across specifications is not identification if all specifications share the same failed assumption.

## Connects To

Use the root [cheatsheet](../cheatsheet.md) for method selection and [patterns](../patterns.md) for reusable audit contracts.
