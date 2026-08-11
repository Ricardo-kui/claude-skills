# R2 forward-validation record (2026-08-06)

## Scope and boundary

This is a six-task **forward smoke test**, not the 24-task formal acceptance
benchmark.  It tests whether the blinded-evaluation plumbing works and whether
the catalog route causes an obvious degradation.  It does **not** establish a
quality improvement claim.

Two independent generators received the same six pre-registered tasks:
`TG04`, `TG08`, `TG11`, `TG15`, `TG18`, and `TG22`.  One used the governed
catalog route; one used the legacy direct-index route.  Outputs were randomly
labeled `X` and `Y` before an independent evaluator applied
`evaluator_rubric.md`.  The evaluator was not told the route-label mapping.

Route mapping retained for audit: `X = legacy direct-index`; `Y = governed
catalog`.

## Result

| Task | Blinded preference | Result for governed catalog |
|---|---|---|
| TG04 | Tie | Tie |
| TG08 | X | Loss |
| TG11 | Tie | Tie |
| TG15 | X | Loss |
| TG18 | X | Loss |
| TG22 | X | Loss |

No critical failures were identified in either condition.  The evaluator's
main reason for preferring X in four tasks was greater operational detail, not
an argument-structure violation in Y.

## Decision

The catalog/governance change passed this smoke test only for **non-degradation
and auditability**: no critical failure, but no demonstrated writing-quality
gain.  The subsequent full blinded evaluation is recorded in
`R2_FULL_BLIND_EVALUATION.md`.

The full evaluation did not establish a writing-quality improvement.  Continue
to use the governed route for corpus safety, discoverability, evidence-state
correctness, and bounded reference selection; inspect generated prose for
adequate mechanism, warrants, and setting-specific detail.
