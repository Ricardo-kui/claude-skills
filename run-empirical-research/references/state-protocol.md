# Empirical State Protocol v1.0

Maintain one YAML file per empirical project. Store paths relative to the project root when practical. Use `null` for unknown values; never invent them.

```yaml
protocol: empirical-state/v1.0
project_id: null
updated_at: null
current_stage: intake
runtime_default: stata

stages:
  intake:
    status: not_started
    artifact: null
    owner: empirical-intake
  data:
    status: not_started
    artifact: null
    owner: null
  design:
    status: not_started
    artifact: null
    owner: null
  execution_plan:
    status: not_started
    artifact: null
    owner: null
  execution:
    status: not_started
    artifact: null
    owner: null
  verification:
    status: not_started
    artifact:
      code_report: null
      method_report: null
      aggregate_report: null
    owner: run-empirical-research
  evidence:
    status: not_started
    artifact: null
    owner: empirical-writeup
  writing_handoff:
    status: not_started
    artifact:
      handoff: null
      drafts: []
    owner: null
  ml_delivery:
    status: not_started
    artifact: null
    owner: null

design_lock:
  question: null
  task_type: null
  estimand_or_prediction_target: null
  unit: null
  time: null
  assignment_unit: null
  outcome_definition: null
  outcome: null
  treatment_or_features: null
  treatment_timing: null
  comparison_group: null
  identifying_sample: null
  comparison_or_split_rule: null
  sample_rule: null
  estimator_family: null
  clustering_or_uncertainty: null
  assumptions: []
  diagnostics: []
  stop_rules: []

ml_contract:
  prediction_point: null
  label_horizon: null
  split_rule: null
  primary_metric: null
  holdout_policy: null
  leakage_checks: []
  threshold_rule: null
  model_artifacts: []

artifacts:
  raw_data: []
  analysis_data: []
  scripts: []
  logs: []
  tables: []
  figures: []
  hashes: {}

decisions: []
deviations: []
open_issues: []
authorized_claims: []
qualified_claims: []
prohibited_claims: []
```

## Status values

- `not_started`: no valid artifact exists.
- `in_progress`: owner is working and the gate is not yet satisfied.
- `blocked`: a named missing input or failed diagnostic prevents advancement.
- `ready`: the artifact passed its gate and downstream work may start; resume from the next stage.
- `complete`: a later stage consumed the artifact and its file links or hashes were verified.
- `superseded`: an upstream decision changed; affected downstream artifacts must not be reused.

An `artifact` may be one path, a list of paths, or a named map of subartifacts. Use a named map whenever a gate aggregates multiple owners.

## Artifact contracts

- **Intake Packet:** task type, question, target, assets, unit/time structure, requested outputs, unresolved risks.
- **Data Contract:** source paths, grain, keys, time coverage, sample funnel, missingness, merges, variable dictionary, reproducible build path.
- **Design Packet:** estimand, counterfactual, assumptions, identification diagram or logic, threats, diagnostics, falsification tests, stop rules, claim ceiling.
- **Analysis Manifest:** Design Packet path, Data Contract path and hash, runtime, package/command versions, estimator, formula, fixed effects, uncertainty rule, sample rule, planned outputs, deviations policy.
- **Run Manifest:** script/log paths, environment, exact inputs, exit status, warnings, deviations, results inventory.
- **Verification Report:** reproduction status, code findings, diagnostic results, fatal issues, material caveats, disposition.
- **Aggregate Verification Report:** code- and method-report paths and hashes, deterministic aggregate disposition, deduplicated findings, disagreements and resolution, affected artifacts, and authorized/qualified/prohibited claim reconciliation.
- **Evidence Packet:** claim-to-table/figure/script map, magnitude, uncertainty, caveats, authorized/qualified/prohibited claims.
- **Writing Handoff:** section targets, evidence pointers, claim limits, unresolved uncertainty, appendix needs.
- **ML Delivery Handoff:** model and preprocessing artifacts, environment, scoring interface, validation and holdout metrics, calibration/threshold rule, known failure slices, monitoring needs, and noncausal interpretation limits.

## Invalidation rule

If the estimand, treatment timing, assignment unit, comparison group, outcome definition, identifying sample, data lineage or hash, sample rule, estimator family, or uncertainty rule changes, append a deviation with its reason and mark every affected downstream stage `superseded`. Do not overwrite the prior decision silently.
