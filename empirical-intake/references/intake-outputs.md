# Intake Outputs

## Standard Intake Packet

```text
Empirical Intake Packet

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

## One-Question Follow-Up Rule

When the brief is incomplete, ask only one question from this priority order:

1. missing outcome or target
2. missing treatment or key feature definition
3. missing unit or time structure
4. missing output contract

## Ready-To-Route Standard

Route onward when the memo contains:

- task type
- target
- data path
- sample or panel structure
- unresolved inputs are explicit
- next-skill recommendation

For a causal task, the next skill is normally `huntington-klein-causal-design`. Route to `causal-analysis` only after a Design Packet exists.
