# R3 generation-guard blinded evaluation (2026-08-07)

## Pre-registered protocol

The task matrix and decision rule were fixed in `R3_GUARD_TASKS.yaml` before
generation.  Two independent generators completed all eight tasks, one through
the governed catalog route and one through the legacy direct-index route.  A
third evaluator received randomly labeled pairs, task prompts, and the existing
eight-dimension rubric; it also assessed the task-explicit generation guard.

Retained mapping: governed catalog was label `X` on RG01, RG03, RG05, and RG07;
it was label `Y` on RG02, RG04, RG06, and RG08.

## Results

| Pre-registered measure | Governed catalog | Legacy direct-index | Rule | Result |
|---|---:|---:|---:|---|
| Critical failures | 0 | 0 | Governed <= 0 | Pass |
| Guard compliance | 8 / 8 | 6 / 8 | Governed all tasks | Pass |
| Mean eight-dimension score (max 40) | 31.50 | 31.75 | Governed >= legacy - 0.50 | Pass |
| Pairwise preference | 3 wins / 5 losses | 5 wins / 3 losses | Governed losses <= 3 | Fail |

The catalog output improved the targeted governance behavior: it complied on all
eight guard-focused tasks.  The two legacy guard failures were an omitted
directional interaction in cross-level moderation and an under-specified process
transition.  No source fabrication, paper-state violation, or forced numbered
claim occurred in the governed condition.

## Decision

R3 is **not provisionally acceptable under its own pre-registered composite
rule**, because governed catalog incurred five pairwise losses, exceeding the
maximum of three.  It does establish that the new contract is enforceable and
improves guard compliance without a material average-score decline.

Do not loosen the R3 threshold after observing this result.  The next revision
must address comparative prose quality separately from structural compliance:
retain the contract, then improve the architecture-specific content supplied to
the governed route (especially concrete transition warrants, audience/actor
roles, and diagnostic observations) before defining a fresh benchmark.
