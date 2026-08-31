# Empirical Skill Routing

Use this matrix only after the project stage and required artifact are clear. A narrower specialist outranks a broad executor for its owned method.

## Stage 4 execution owners

| Need | Primary skill | Boundary |
|---|---|---|
| Complete Stata project from a locked design | `empirical-pipeline-stata` | Owns the project-level Run Manifest and Results Inventory; it consumes rather than chooses the design |
| Staggered-adoption DiD in Stata | `staggered-did` | Owns the cohort-aware estimation module and DiD diagnostics; in a whole-project run, `empirical-pipeline-stata` composes its outputs without re-estimating them |
| Explicit local Econometrics-Agent CLI run | `econometrics-agent` | Reconnaissance or supported CLI workflows only |
| Explicit R modern DiD | `did-analysis` | R-specific implementation; do not select by default |
| Explicit R IV or RDD | no dedicated executor | Keep Stage 4 blocked; return to `causal-analysis` and select the locked Stata lane, or install/create and validate a dedicated R executor first |
| Python-native end-to-end analysis | `empirical-pipeline-python` | Executes a locked causal or ML Analysis Manifest; it does not choose the design |
| General Stata code, regression, or one command family | `stata` | Reference and narrow implementation aid, not the project coordinator |
| Data cleaning in Stata | `stata-data-cleaning` | Owns transformations and data-contract checks |
| Governed specification or measure search | `xianzhu-skill` | Requires a locked question, estimand, sample, baseline model, uncertainty rule, admissible search universe, and stopping rule; cannot choose the preferred claim by significance |

## Planning and review owners

| Need | Primary skill | Boundary |
|---|---|---|
| Clarify an underspecified project | `empirical-intake` | Produces intake, not estimates |
| Define or audit causal identification | `huntington-klein-causal-design` | Owns causal question, estimand, DAG/assumptions, threats, diagnostics, and stop rules |
| Convert a locked causal design into an execution plan | `causal-analysis` | Routes runtime and specification plan; cannot weaken the Design Packet |
| Plan prediction/ML validation | `ml-analysis` | Prediction is not causal identification |
| Inspect unfamiliar data | `exploratory-data-analysis` | Descriptive evidence only |
| Review implementation correctness | `review-code` | Code/reproducibility review, not identification design |
| Review econometric credibility | `check-methodology` | Identification and estimator audit, not prose polish |
| Package verified evidence | `empirical-writeup` | Claims remain bounded by the Verification Report |

## Overlap decisions

- Keep `staggered-did` and `did-analysis`: they implement the same method family in different runtimes; Stata is default and R is explicit-only.
- Keep `empirical-pipeline-stata` and `staggered-did`: the first owns whole-project assembly and the Run Manifest; the second is the exclusive staggered-DiD estimator module. The narrower owner outranks the broad executor only inside that module.
- Merge `stata-regression` into `stata`: the latter already owns regression syntax, diagnostics, `reghdfe`, `esttab`, and `outreg2`; a second thin trigger added no distinct artifact.
- Keep `empirical-writeup` and `write-methods-and-results`: the first constructs an evidence/claim contract; the second drafts prose.
- Keep `causal-analysis` and `huntington-klein-causal-design`: conceptual identification precedes operational routing.
- Replace `full-empirical-analysis-python` with `empirical-pipeline-python`: retain only reproducible Stage 4 execution and remove the mixed textbook/catalog/orchestrator role.
- Retire `full-empirical-analysis-stata`: its execution role is absorbed by `empirical-pipeline-stata`, `staggered-did`, and `stata`.
- Retire `r-econometrics`: it promised IV/DiD/RDD coverage but supplied only a thin conventional TWFE template. Keep `did-analysis` for explicit modern DiD in R; do not advertise an installed R IV/RDD executor until one is implemented and tested.
