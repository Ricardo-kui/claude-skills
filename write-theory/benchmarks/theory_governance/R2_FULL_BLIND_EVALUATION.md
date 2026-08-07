# R2 full blinded evaluation (2026-08-07)

## Protocol

All 24 pre-registered tasks in `tasks.yaml` were generated independently by
two routes:

- **Governed catalog:** `write-theory` catalog-first route.
- **Legacy direct-index:** raw `_index.md` and linked corpus files.

Both generators were constrained to a 110–150 word scaffold plus an argument
graph and uncertainty line.  Two independent evaluators each received 12
randomly labeled pairs, the task prompt, and `evaluator_rubric.md`; they were
instructed not to inspect corpus, benchmark records, or output provenance.
Labels were revealed only after both evaluations completed.

## Retained label mapping

| Task | Label used for governed catalog |
|---|---|
| TG01 | X |
| TG02 | Y |
| TG03 | Y |
| TG04 | X |
| TG05 | Y |
| TG06 | X |
| TG07 | Y |
| TG08 | X |
| TG09 | X |
| TG10 | Y |
| TG11 | X |
| TG12 | Y |
| TG13 | X |
| TG14 | Y |
| TG15 | X |
| TG16 | Y |
| TG17 | Y |
| TG18 | X |
| TG19 | Y |
| TG20 | X |
| TG21 | Y |
| TG22 | X |
| TG23 | Y |
| TG24 | X |

## Results

| Measure | Governed catalog | Legacy direct-index |
|---|---:|---:|
| Pairwise preference | 8 wins | 11 wins |
| Ties | 5 | 5 |
| Mean eight-dimension score (max 40) | 36.0 | 36.9 |
| Critical failures | 0 | 1 |

The one legacy critical failure was TG24: it imposed numbered competing
hypotheses despite a deliberately provisional, local-only diagnostic that
explicitly prohibited paper-state writeback.  No output fabricated a source or
triggered another critical-failure category.

## Decision

The governed route passes an **integrity and non-catastrophic-degradation
check**: it completed all architectures and modes without a critical failure.
It does **not** pass a writing-quality-improvement claim.  Legacy received more
pairwise preferences and a 0.9-point higher mean score; no superiority threshold
was pre-registered, so this result must not be converted post hoc into a formal
accept/reject threshold.

Keep the governed route as the required corpus-safety and evidence-governance
layer.  Treat the next revision as a retrieval-and-prompt-quality task, focused
on preserving the governed route's explicit theory detail (especially concrete
high/low mechanism derivation, temporal transitions, and local-only mode
suppression) before rerunning a newly pre-registered benchmark.
