# Chapter 7: Drawing Causal Diagrams

## Core Idea

A credible DAG is built from substantive knowledge about the DGP, not generated mechanically from the observed correlations. Simplification is necessary, but every simplification is an assumption.

## Construction Workflow

1. **Anchor the question**: write treatment, outcome, population, and time horizon.
2. **Research the setting**: identify assignment rules, actor incentives, timing, institutions, and prior findings.
3. **Build forward in time**: ask what causes treatment, what treatment can change, and what causes the outcome.
4. **Add common causes**: search for variables that precede and influence both treatment and outcome.
5. **Represent selection and measurement**: include causes of being observed and causes of measurement error when they affect identification.
6. **Separate time slices**: turn apparent feedback cycles into ordered nodes such as X_t and Y_t+1.
7. **Simplify by causal equivalence**: combine nodes only when doing so preserves all paths relevant to the target effect.
8. **Record disputed assumptions**: retain plausible alternative diagrams when they imply different adjustment sets or designs.

## Simplification Tests

A node can be omitted or combined only if:

- it does not create or close a treatment–outcome path relevant to identification;
- its timing and role are preserved by the aggregate node;
- omitting it does not hide treatment-induced selection or mediation;
- the decision is documented, not merely convenient.

## Assumption Ledger

For each arrow, missing arrow, and omission, label the basis:

- established contextual or scientific knowledge;
- evidence from prior studies;
- design fact or institutional rule;
- simplifying assumption;
- untested judgment.

This prevents a clean diagram from creating false certainty.

## Failure Modes

- **Everything graph**: so detailed that no design implication can be read.
- **Dataset graph**: limited to measured fields.
- **Acyclicity by deletion**: removing feedback rather than representing its timing.
- **Consensus theater**: presenting one DAG when multiple plausible graphs imply different conclusions.
- **Aesthetic simplification**: dropping a node because the graph looks crowded.

## Completion Check

Finish only when all plausible pre-treatment common causes and selection processes have been considered, time ordering is coherent, and alternative diagrams that change the design are disclosed.

## Worked Example

> Synthetic application derived from the chapter's framework; not a documented case from the source.

Question: What is the effect of adopting an AI decision-support system on product-recall speed?

Build in time order:

1. prior quality problems, IT capability, regulatory scrutiny, and managerial risk preferences can affect adoption;
2. adoption can change detection, information flow, and decision speed;
3. incident severity affects detection and recall speed;
4. adoption may alter which incidents become recorded;
5. prior recalls can affect later adoption, so represent prior recall at t−1 and current adoption/outcome at t.

A compact DAG may combine related stable capabilities into one node only if their separate paths do not imply different controls or mechanisms. Preserve the recording/selection node because conditioning on observed incidents alone may select on a treatment-induced collider.

Keep two rival diagrams if adoption either improves detection (more severe-looking observed cases) or only accelerates decisions. Those diagrams imply different outcomes, samples, and interpretations.

## Connects To

- [Ch6](ch06-causal-diagrams.md): diagram semantics.
- [Ch8](ch08-causal-paths.md): path-based implications.
- [Ch15](ch15-simulation.md): simulate rival DGPs when intuition is uncertain.
