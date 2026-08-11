# Robustness Planning: Threat to Evidence

Use this reference while creating the Analysis Manifest. Plan only diagnostics, falsification, and sensitivity analyses that address a named threat in the locked Design Packet.

## Planning fields

For each planned item, record:

- `threat`
- `why_material`
- `test_or_sensitivity`
- `prerequisites`
- `decision_rule_or_stop_rule`
- `claim_impact`
- `executor`

## Common mappings

| Threat | Candidate evidence | Boundary |
|---|---|---|
| Few or influential assignment clusters | small-cluster-appropriate inference, leave-one-cluster-out | Cluster at the assignment/dependence level; do not search levels by p-value |
| Multiple prespecified outcomes | multiplicity adjustment for the locked family | Define the family before results |
| Staggered-treatment heterogeneity | cohort-aware estimator and support audit | TWFE decomposition is diagnostic, not a preferred estimator |
| Parallel-trend deviations | pre-period falsification and prespecified sensitivity | Nonsignificance is not proof |
| Omitted-variable sensitivity | a bound whose assumptions fit the model | Oster-style analysis is not universal |
| Weak or invalid IV | weak-IV-robust inference and exclusion evidence | First-stage strength does not prove exclusion |
| RDD manipulation/support | density, continuity, bandwidth, and support checks | Preserve the running-variable/cutoff contract |
| Weighting/matching support | overlap, balance, and weight diagnostics | Report the population lost to trimming |
| Measurement/specification ambiguity | governed multiverse via `xianzhu-skill` | Retain every result; no p-value-based selection |

The Stata implementation menu lives in `empirical-pipeline-stata/references/03-robustness-battery.md`. Explicit R modern DiD may use `did-analysis`. An item enters the manifest only when its prerequisites are plausible; there is no full battery that every design must run.

