# Intake Outputs

## Standard Intake Packet

```text
Empirical Intake Packet

Intake mode:
Task type:
Question:
Estimand or prediction target:
Outcome or label:
Treatment / key features:
Unit of observation:
Time structure:
Data assets:
Sample rule:
Main risks:
Requested outputs:
Unresolved inputs:
Recommended next skill:
```

For `retrospective` mode, append:

```text
Field evidence:
- Field: <name>
  Status: <confirmed | pending_confirmation | conflict | unknown>
  Source path: <path | null>
  Source date: <date | null>
  Freshness: <current | stale | undetermined>
Design lock sign-off: <signer and confirmation date | pending_confirmation>
```

Repeat the field-evidence row for every intake field and retain separate rows for conflicting sources.

## One-Question Follow-Up Rule

When the brief is incomplete, ask only one question from this priority order:

1. missing outcome or target
2. missing treatment or key feature definition
3. missing unit or time structure
4. missing output contract

## Ready-To-Route Standard

Route onward when the memo contains:

- intake mode
- task type
- target
- data path
- sample or panel structure
- unresolved inputs are explicit
- next-skill recommendation

For a causal task, the next skill is normally `huntington-klein-causal-design`. Route a retrospectively recovered design to `causal-analysis` only after a Design Packet exists and the user explicitly signs off its lock.
