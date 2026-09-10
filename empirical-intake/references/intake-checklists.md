# Intake Checklists

## Core Fields

- `intake_mode`
- `question`
- `task_type`
- `estimand_or_target`
- `unit`
- `time`
- `sample`
- `outcome_or_label`
- `treatment_or_features`
- `data_paths`
- `requested_outputs`

## Causal Add-On

- identification strategy
- treatment timing
- clustering level
- core threats
- must-have diagnostics

## ML Add-On

- prediction point
- split rule
- metric
- leakage risks
- baseline benchmark

## Retrospective Add-On

Create a provenance row for every applicable field in **Core Fields**, **Causal Add-On**, and **ML Add-On**. Each row contains:

- `field`
- `recovered_value`
- `status`: `confirmed`, `pending_confirmation`, `conflict`, or `unknown`
- `source_path`
- `source_date`
- `freshness`

Use `null` for unavailable provenance. When sources conflict, preserve each source as a separate row; do not collapse sources into one reconciled value or select an authority silently.

For every recovered Causal Add-On field, keep `status: pending_confirmation` until a human provides dated sign-off. Record that sign-off separately as `design_lock_signoff` with signer and date; source recency or agreement does not substitute for sign-off.

## Handoff Template

```text
Intake mode:
Task type:
Question:
Estimand or target:
Data assets:
Sample and structure:
Variables or features:
Main risks:
Requested outputs:
Recommended next skill:
```
