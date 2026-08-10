# R4 blinded acceptance evaluation (2026-08-07)

## Protocol

The 12 tasks, two strata, deterministic label rule, and decision thresholds were
fixed in `R4_ACCEPTANCE_TASKS.yaml` before generation. One generator used the
revised governed catalog route; another used the legacy direct-index route. Two
independent evaluators each scored six randomly labeled pairs using the same
eight-dimension rubric. Evaluators received only task prompts and X/Y outputs.

The pre-registered SHA256 rule produced this governed-label mapping:

- `X`: RQ01, RQ02, RQ03, RQ11, RQ12
- `Y`: RQ04, RQ05, RQ06, RQ07, RQ08, RQ09, RQ10

## Pairwise result

| Stratum | Governed wins | Legacy wins | Ties |
|---|---:|---:|---:|
| Targeted (RQ01–RQ06) | 3 | 3 | 0 |
| Preservation (RQ07–RQ12) | 4 | 0 | 2 |
| **Overall** | **7** | **3** | **2** |

Governed wins: RQ02, RQ05, RQ06, RQ08, RQ10, RQ11, RQ12.  Governed losses:
RQ01, RQ03, RQ04.  Ties: RQ07, RQ09.

## Score and integrity result

| Measure | Governed catalog | Legacy direct-index |
|---|---:|---:|
| Targeted score | 230 / 240 (38.33 mean) | 227 / 240 (37.83 mean) |
| Preservation score | 232 / 240 (38.67 mean) | 226 / 240 (37.67 mean) |
| Overall score | 462 / 480 (**38.50 mean**) | 453 / 480 (**37.75 mean**) |
| Explicit task compliance | 12 / 12 | 11 / 12 |
| Critical failures | 0 | 0 |

The legacy noncompliance was RQ03: its first proposition was an incomplete
fragment rather than a proposition, although the evaluator still preferred its
overall stage architecture.

## Pre-registered decision

| Condition | Threshold | Observed | Result |
|---|---|---:|---|
| Governed critical failures | <= 0 | 0 | Pass |
| Governed task compliance | 12 / 12 | 12 / 12 | Pass |
| Pairwise superiority | wins > losses | 7 > 3 | Pass |
| Mean-score superiority | >= legacy + 0.25 | +0.75 | Pass |
| Targeted consistency | losses <= 2 | 3 | **Fail** |
| Preservation critical failures | <= 0 | 0 | Pass |
| Preservation noninferiority | >= legacy - 0.50 | +1.00 | Pass |

R4 is **not provisionally accepted under its complete pre-registered rule**
because the governed route lost three targeted tasks rather than at most two.
The result nevertheless supplies evidence that the retrieval/rendering revision
improved aggregate and cross-architecture quality while preserving integrity.
Do not relabel this as a pass or change the threshold after observing it.

The remaining targeted inconsistency is narrow: preserve the revised retrieval
layer, then inspect RQ01 (verifiability mechanism precision), RQ03 (stage
proposition quality), and RQ04 (feedback-transmission detail) before deciding
whether another revision is warranted.
