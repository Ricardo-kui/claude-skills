# R6 blinded acceptance evaluation (2026-08-07)

## Protocol integrity

`R6_ACCEPTANCE_TASKS.yaml` was frozen before generation with SHA-256
`321fda9922cb7906c7ce819a6755caf4d010b1beb1fda992707ff647212402ff`.
Fresh governed and legacy generators answered the same 12 novel tasks in
isolated threads. The governed route used the current skill and governed
catalog; the legacy route used direct corpus navigation without the catalog,
generation guards, process operators, or manifest. Raw outputs and the
anonymized X/Y pair file were hashed before judging (`R6_GENERATION_SHA256.txt`),
and judge files were hashed after scoring (`R6_JUDGING_SHA256.txt`).

Two fresh judges independently scored every anonymized pair on the eight
pre-registered dimensions. They were instructed to read only the blinded pair
file. Per-task pairwise votes used X=+1, tie=0, Y=-1; opposing votes cancel to
a tie. Any judge-reported critical failure counts conservatively.

The governed retrieval manifest validates with 21 chained events (12
`list-references`, 9 `render`) and covers all 12 task IDs. It therefore passes
the pre-registered manifest integrity requirement.

Protocol note: repairs to the shared corpus variant files (G same-outcome
locking, B horizon-contingency QC lines) are visible to both routes, because
the legacy route navigates the same corpus directly. The governed-only repairs
(E boundary-scope graph notation, D terminal-state closure, D open-agenda QC)
live in SKILL.md, the generation guards, and the registry contract, which the
legacy route does not read.

## Pairwise and score results

| Task | Stratum | Governed label | Governed mean /40 | Legacy mean /40 | Aggregated result |
|---|---|---:|---:|---:|---|
| R6Q01 | targeted | Y | 39.5 | 36.0 | Win |
| R6Q02 | targeted | X | 35.0 | 38.0 | Loss |
| R6Q03 | targeted | X | 39.0 | 35.5 | Win |
| R6Q04 | targeted | X | 39.0 | 32.5 | Win |
| R6Q05 | targeted | X | 36.0 | 36.0 | Loss |
| R6Q06 | targeted | Y | 38.5 | 38.0 | Win |
| R6Q07 | preservation | X | 37.5 | 39.0 | Loss |
| R6Q08 | preservation | X | 36.5 | 38.0 | Loss |
| R6Q09 | preservation | Y | 36.5 | 37.5 | Tie |
| R6Q10 | preservation | X | 39.0 | 39.0 | Tie |
| R6Q11 | preservation | Y | 37.0 | 35.0 | Win |
| R6Q12 | preservation | Y | 38.0 | 36.0 | Win |

| Stratum | Governed wins | Governed losses | Ties | Governed mean | Legacy mean | Delta |
|---|---:|---:|---:|---:|---:|---:|
| Targeted | 4 | 2 | 0 | 37.83 | 36.00 | +1.83 |
| Preservation | 2 | 2 | 2 | 37.42 | 37.42 | 0.00 |
| **Overall** | **6** | **4** | **2** | **37.63** | **36.71** | **+0.92** |

Both judges marked the governed output explicitly compliant on all 12 tasks.
No judge reported any critical failure on either route.

## Pre-registered decision

| Condition | Threshold | Observed | Result |
|---|---|---:|---|
| Governed critical failures | 0 | 0 | Pass |
| Governed explicit compliance | 12/12 | 12/12 | Pass |
| Valid manifest task coverage | 12/12 | 12/12; chain valid | Pass |
| Pairwise superiority | wins > losses | 6 > 4 | Pass |
| Mean-score superiority | >= legacy +0.25 | +0.92 | Pass |
| Targeted consistency | losses <=1 | 2 | **Fail** |
| Preservation critical failures | 0 | 0 | Pass |
| Preservation noninferiority | >= legacy -0.50 | 0.00 | Pass |

R6 is **not accepted** because the pre-registered targeted-consistency
condition failed (2 targeted losses against a maximum of 1). No task, label,
score, threshold, or aggregation rule was changed after generation began.

## Failure localization

- **R6Q02 (E, hypotheses):** both judges preferred the legacy output. The
  governed answer collapsed the prediction into one comparative moderation
  statement ("more negative when stakes are high than when low"), whereas the
  prompt's requested form was per-state signed conditional predictions; the
  legacy output supplied two signed conditional hypotheses (negative under
  high stakes, positive under low stakes) with richer state-specific traces.
  The R5 boundary-scope repair held (no graph–prose inconsistency was
  reported); the loss is a hypothesis-form granularity issue in hypotheses
  mode.
- **R6Q05 (G, propositions):** split decision (judge A legacy, judge B tie)
  aggregating to a loss. The R5 repair held — judge B explicitly credited the
  governed output's symmetric blades on a single outcome. The legacy edge was
  a finer dominance rule: severity-minus-expectation gap and remediability as
  two independently testable conditions, versus the governed single
  remediation-capacity threshold.
- **R6Q07 (A, preservation):** judge A preferred legacy (cleaner named
  dimensions, dynamic accrue/decay temporal scope, discriminating
  observations against both adjacent constructs); judge B tied the pair.
- **R6Q08 (B, preservation):** both judges marginally preferred legacy for
  more specifically named warrants (psychological safety, error-reporting
  research) and sharper observable implications (recurrence intervals
  conditioned on completed structural action items).

## Interpretation

The R5 failure mechanisms did not recur: zero critical failures (R5Q01's
graph–prose inconsistency class is eliminated), the D terminal-state closure
held (R6Q03 and R6Q11 both won), the G same-outcome locking held (judge B's
explicit credit on R6Q05), and the discriminating open agenda appeared in
R6Q04 (the largest single-task margin, 39.0 vs 32.5). The remaining gap is
finer-grained: per-state signed hypothesis forms in E hypotheses mode, and
dominance rules decomposed into independently testable conditions in G.
Preservation regressed relative to R5 (delta 0.00 vs +0.25), driven by R6Q07
and R6Q08, where legacy outputs named warrants and discriminating
observations more specifically; this stays within the noninferiority margin
but should be watched in R7.

## Materials

- `R6_ACCEPTANCE_TASKS.yaml` (frozen pre-registration)
- `R6_PREREGISTRATION_SHA256.txt`
- `R6_GOVERNED_OUTPUTS.md`, `R6_LEGACY_OUTPUTS.md`
- `R6_GOVERNED_RETRIEVAL_MANIFEST.json` (21 events, valid)
- `R6_BLINDED_PAIRS.md`, `R6_LABEL_MAP.yaml`
- `R6_GENERATION_SHA256.txt`, `R6_JUDGING_SHA256.txt`
- `R6_JUDGE_A.yaml`, `R6_JUDGE_B.yaml`
- `R6_SCORE_SUMMARY.yaml`
