# Empirical State Protocol v1.0

Maintain one YAML file per empirical project. Use `null` for unknown values; never invent them.

## State ownership

| Concern | Authority | Coordinator action |
|---|---|---|
| Current empirical stage, gate status, design lock, run state, and empirical asset paths | `empirical-state.yaml` | Read and update here only |
| Full rationale and history for a material specification or design change | Decision Register | Append the complete decision; place only its ID in empirical state |
| `write-*` workflow metadata | `paper-state.yaml` | Leave to the writing workflow; only follow its pointers |
| Cross-domain orientation for humans | `PROJECT_STATUS.md` | Read as an index/projection; never use it to authorize, lock, or advance work |

When records disagree, the authority for that concern wins. Surface the conflict and stop automatic merging. Do not create a combined project-status spine or copy empirical fields into `paper-state.yaml`.

## Root pointers

Record both migratable location roots. `project_files` locates project files such as data, code, logs, and empirical state; `knowledge_project` locates the corresponding knowledge/writing tree. The root keys do not determine which root owns the Decision Register or `PROJECT_STATUS.md`. Resolve each through its own explicit, root-prefixed pointer (for example, `project_files:path/to/file` or `knowledge_project:path/to/file`). Files with the same name under both roots remain distinct: never merge them automatically or infer authority from name or root.

```yaml
protocol: empirical-state/v1.0
project_id: null
updated_at: null
roots:
  project_files: null
  knowledge_project: null
decision_register: null # when known, use project_files:<relative path> or knowledge_project:<relative path>
project_status: null # when known, use project_files:<relative path> or knowledge_project:<relative path>
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

decisions: [] # Decision Register IDs only
deviations: [] # decision ID plus affected stages; full rationale stays in the Decision Register
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

## Decision references and invalidation

For each material specification or design change:

1. Append the full old/new specification, rationale, evidence, author, and date to the Decision Register and obtain its stable decision ID.
2. Add that ID to `decisions`; a `deviations` entry contains only the ID and affected stages.
3. If the estimand, treatment timing, assignment unit, comparison group, outcome definition, identifying sample, data lineage or hash, sample rule, estimator family, or uncertainty rule changed, mark every affected downstream stage `superseded`.

Never copy the full decision into empirical state or overwrite the prior decision silently.

## PROJECT_STATUS projection

`PROJECT_STATUS.md` may link the two roots and summarize the latest authoritative records for human navigation. It is a read-only projection for this coordinator: never infer a lock, resolve a conflict, or advance a gate from it. When it is stale or conflicts with an authority, report the mismatch and leave reconciliation to an explicit human update of the relevant authority.

## Bidirectional re-entry

- **Empirical → writing:** enter through the verified Evidence Packet and Writing Handoff. The handoff points back to `empirical-state.yaml`; `paper-state.yaml` records only `write-*` metadata.
- **Writing → empirical:** an evidence, design, data, or execution issue re-enters at the earliest affected empirical gate through `empirical-state.yaml` and, for a material decision, a Decision Register ID.
- On either route, resolve each target from its explicit root-prefixed pointer, re-read the domain authority, report any cross-domain or same-name conflict, and stop before automatic merge.
