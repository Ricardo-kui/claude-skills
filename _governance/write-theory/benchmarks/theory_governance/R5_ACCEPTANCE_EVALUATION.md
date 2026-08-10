# R5 blinded acceptance evaluation (2026-08-07)

## Protocol integrity

`R5_ACCEPTANCE_TASKS.yaml` was frozen before generation with SHA-256
`df1320a05bcb0ae8f008aabfad0a122aec2c696c7b87ba3c6a61ea6003dae211`.
Fresh governed and legacy generators answered the same 12 novel tasks in isolated
threads. The governed route used the current skill and catalog; the legacy route
used direct corpus navigation. Raw outputs and the anonymized X/Y pair file were
hashed before judging, and all four hashes remained unchanged after judging.

Two fresh judges independently scored every anonymized pair on the eight
pre-registered dimensions. They were instructed to read only the blinded pair
file. Per-task pairwise votes used X=+1, tie=0, Y=-1; opposing votes cancel to a
tie. Any judge-reported critical failure counts conservatively.

The governed retrieval manifest validates with 21 chained events (15
`list-references`, 6 `render`) and covers all 12 task IDs. It therefore passes
the pre-registered manifest integrity requirement.

## Pairwise and score results

| Task | Stratum | Governed label | Governed mean /40 | Legacy mean /40 | Aggregated result |
|---|---|---:|---:|---:|---|
| R5Q01 | targeted | X | 36.5 | 40.0 | Loss |
| R5Q02 | targeted | Y | 40.0 | 40.0 | Tie |
| R5Q03 | targeted | Y | 39.0 | 40.0 | Loss |
| R5Q04 | targeted | X | 40.0 | 37.5 | Win |
| R5Q05 | targeted | Y | 40.0 | 38.0 | Win |
| R5Q06 | targeted | X | 40.0 | 40.0 | Loss |
| R5Q07 | preservation | Y | 39.5 | 37.0 | Win |
| R5Q08 | preservation | X | 40.0 | 39.0 | Win |
| R5Q09 | preservation | X | 40.0 | 39.0 | Win |
| R5Q10 | preservation | Y | 40.0 | 38.0 | Win |
| R5Q11 | preservation | Y | 35.5 | 40.0 | Loss |
| R5Q12 | preservation | X | 39.0 | 39.5 | Loss |

| Stratum | Governed wins | Governed losses | Ties | Governed mean | Legacy mean | Delta |
|---|---:|---:|---:|---:|---:|---:|
| Targeted | 2 | 3 | 1 | 39.25 | 39.25 | 0.00 |
| Preservation | 4 | 2 | 0 | 39.00 | 38.75 | +0.25 |
| **Overall** | **6** | **5** | **1** | **39.125** | **39.000** | **+0.125** |

Both judges marked the governed output explicitly compliant on all 12 tasks.
One judge reported one governed critical failure on R5Q01: its argument graph
placed high/low scarcity downstream of data-center expansion, even though the
rationale treated scarcity as the prior boundary state. Under the conservative
pre-registration rule, this counts as one critical failure.

## Pre-registered decision

| Condition | Threshold | Observed | Result |
|---|---|---:|---|
| Governed critical failures | 0 | 1 | **Fail** |
| Governed explicit compliance | 12/12 | 12/12 | Pass |
| Valid manifest task coverage | 12/12 | 12/12; chain valid | Pass |
| Pairwise superiority | wins > losses | 6 > 5 | Pass |
| Mean-score superiority | >= legacy +0.25 | +0.125 | **Fail** |
| Targeted consistency | losses <=1 | 3 | **Fail** |
| Preservation critical failures | 0 | 0 | Pass |
| Preservation noninferiority | >= legacy -0.50 | +0.25 | Pass |

R5 is **not accepted** because three independently pre-registered conditions
failed. No task, label, score, threshold, or aggregation rule was changed after
generation began.

## Failure localization

- **R5Q01 (E, critical):** the prose followed the intended boundary-first logic,
  but the compact graph encoded `expansion -> scarcity`, turning a moderator into
  a downstream state. The final graph and prose were therefore internally
  inconsistent.
- **R5Q03 (D):** the governed account supplied the transition condition, prior
  marker, next decision actor, and failed branch, but one judge preferred the
  legacy account because it carried authorization through routinized adoption;
  the governed account stopped at procurement and implementation planning.
- **R5Q06 (D):** transport and branch structure were complete. The loss came from
  one judge preferring the legacy account's more discriminating open empirical
  agenda concerning redesign versus selection; the other judge scored a tie.
- **R5Q11 (G, preservation):** both judges preferred the legacy reconciliation,
  which held the two mechanisms on the same evaluation outcome and derived
  dominance more coherently from remediability and value-capture timing.
- **R5Q12 (B, preservation):** one judge tied the outputs; the other preferred
  the legacy account's more explicit horizon-contingent net effect and account of
  how local problem solving reproduces tacit coordination.

These results support the manifest and preservation layers, but they do not yet
support formal acceptance of the revised governed generator.
