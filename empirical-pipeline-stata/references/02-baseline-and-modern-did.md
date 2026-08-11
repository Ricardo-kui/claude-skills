# Step 5 · Baseline and Modern DiD in Stata

This reference governs execution boundaries. The Design Packet owns identification; the Analysis Manifest owns the exact specification. Examples here never override either artifact.

## Baseline models

Before estimating, verify that the manifest explicitly fixes:

- estimand and identifying variation
- outcome, treatment, timing, and comparison group
- identifying sample and exclusion rules
- formula, controls, fixed effects, weights, and uncertainty rule
- diagnostics, stop rules, and output paths

Use `reghdfe`, `xtreg`, `ivreghdfe`, `ppmlhdfe`, survival commands, or other estimators only when the locked design selects that family. Firm and time fixed effects are adjustments, not an identification strategy by themselves. Do not build an M1→M6 ladder unless each column has a design or hypothesis role fixed before results are inspected.

## Staggered-adoption DiD ownership

For absorbing treatment adopted at different times, delegate cohort-aware estimation to `staggered-did`. Do not recreate a conventional lead/lag TWFE event study inside this broad executor.

The specialist must validate rather than silently replace:

- cohort and treatment histories, reversals, and anticipation window
- never-treated and/or not-yet-treated comparison-group contract
- cohort/event-time support and identifying observations
- assignment-level clustering and small-cluster strategy
- estimator eligibility and target estimand

Preserve never-treated and otherwise valid comparison units. Missing cohort for never-treated units is a treatment-status representation, not a reason to delete them.

Consume the specialist's method status, normalized estimates, support tables, diagnostic outputs, and figures as the DiD module of the project-level Run Manifest. `empirical-pipeline-stata` owns outer assembly; it must not re-estimate or relabel the specialist's effects.

## Event-study interpretation

- Pre-treatment estimates and joint tests are falsification evidence, not proof of parallel trends.
- Report which cohorts and comparison observations identify each event horizon.
- Do not report horizons with inadequate support as population-wide dynamic effects.
- Use sensitivity analysis such as HonestDiD only when authorized and its inputs/assumptions match the estimator output.
- A conventional TWFE event study may appear only as a clearly labelled bias diagnostic, never as the preferred staggered-adoption estimator.

## TWFE decomposition

Use Bacon decomposition only when its data and design requirements are met and the Analysis Manifest authorizes it. Treat it as a diagnostic of a TWFE benchmark; it cannot validate the causal design or replace a cohort-aware estimator.

## Other treatment structures

Reversing treatment, continuous dose, multiple concurrent treatments, repeated cross-sections, or few treated clusters require an explicit design branch. Return to `huntington-klein-causal-design` if the locked packet does not cover that structure; do not coerce it into a binary absorbing-treatment template.

