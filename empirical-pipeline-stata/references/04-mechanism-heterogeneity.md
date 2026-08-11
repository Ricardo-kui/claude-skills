# Step 7 · Conditional Mechanism and Heterogeneity

Run this stage only when all three gates pass:

1. theory prespecifies the mechanism, moderator, subgroup, or mediation target;
2. the Design Packet and Analysis Manifest authorize the contrast and its assumptions;
3. the baseline estimate and core diagnostics are credible enough to support expansion.

No minimum number of moderators, subgroups, outcomes, or mediation models is required.

## Distinguish the questions

- **Treatment-effect heterogeneity:** does the same estimand differ across prespecified baseline characteristics?
- **Moderation:** does theory predict a conditional effect, and is the interaction estimand identified on observed support?
- **Mechanism evidence:** does treatment move a preregistered intermediate outcome in the predicted temporal sequence?
- **Causal mediation:** what direct/indirect effects are identified under additional sequential-ignorability or alternative mediation assumptions?

Do not label subgroup differences or a treatment–mediator–outcome regression as a mechanism by themselves.

## Implementation rules

- Prefer a fully interacted model with an explicit Wald test over comparing significance across separate subgroup regressions.
- Use `margins`/`marginsplot` only over observed support and report the underlying interaction test.
- Keep moderators and subgroup definitions pretreatment unless the design explicitly targets post-treatment variables.
- For staggered DiD, use heterogeneity procedures compatible with the cohort-aware estimator rather than adding interactions to a conventional TWFE model.
- Treat an outcome ladder as ordered auxiliary evidence, not proof of mediation.
- Run mediation only when treatment, mediator, and outcome timing are coherent and the extra assumptions are stated. Otherwise call it exploratory mechanism-consistent evidence.
- Check optional commands with `which`; never use unconditional `ssc install ..., replace`.

## Required output

For each authorized extension, record:

- theoretical prediction and estimand
- subgroup/moderator/mechanism definition and timing
- support and sample
- model and inference rule
- multiplicity family when applicable
- estimate, uncertainty, and joint test
- identifying assumptions and competing explanations
- effect on authorized claims

If the baseline gate fails, return `not_authorized_baseline_failed` and do not run this stage.

