# Causal Design Cheatsheet

Use this as a decision aid. Open the selected chapter before making a substantive recommendation.

## Choose by Identifying Variation

| Variation/design fact | Candidate | Target | Central assumption | Immediate red flag |
|---|---|---|---|---|
| Rich measured pre-treatment common causes | Regression / matching | ATE or ATT | Conditional exchangeability + overlap | Controls chosen from availability or significance |
| Repeated units; treatment changes within unit | Fixed effects | Effect among within-unit changers | No relevant time-varying confounding | Almost no within variation |
| One event; counterfactual forecast from time series | Event study | Event-window/local time effect | Forecast remains valid post-event | Concurrent event or anticipation |
| Treated and comparison-group changes | DiD | ATT/cohort-time ATT | Parallel untreated trends | Staggered adoption analyzed with legacy TWFE |
| External encouragement shifts treatment | IV | ITT/LATE | Relevance, independence, exclusion, monotonicity | Strong first stage but plausible direct path |
| Assignment jumps at a cutoff | RDD | Cutoff-local effect | Continuity/no precise manipulation | Sorting, mass points, arbitrary polynomial |
| Point identification too assumption-heavy | Partial identification | Identified set | Calibrated violation range | Range selected to preserve preferred result |
| Few treated units; long pre-period and donors | Synthetic control | Treated-unit post effect | Weighted donors reproduce untreated path | Poor pre-fit or contaminated donor pool |
| Flexible nuisance relations under valid design | DML | Low-dimensional target | Base identification + overlap + cross-fitting | ML invoked as identification |

## Control-Variable Decision

| Variable role | Total-effect default |
|---|---|
| Pre-treatment common cause | Adjust if needed to close a back door |
| Cause of outcome only | May improve precision; defend support |
| Cause of treatment only / instrument-like | Usually omit unless the design requires it |
| Mediator | Omit for total effect; include only for a defined direct-effect target |
| Collider or collider descendant | Omit |
| Post-treatment confounder | Requires longitudinal/mediation methods; generic adjustment is unsafe |
| Sample-selection driver | Model selection/missingness process |
| Proxy | Audit construct and measurement error before adjustment |

## Diagnostic Semantics

| Diagnostic | Failure can show | Passing cannot show |
|---|---|---|
| Covariate balance | Implemented match/comparison is visibly poor | No unmeasured confounding |
| Pre-treatment DiD coefficients | Differential trends or anticipation | Post-treatment parallel trends |
| Placebo date/cutoff/outcome | Design produces effects where none should exist | All assumptions are valid |
| RDD density/covariate continuity | Sorting or discontinuous composition | No manipulation or omitted discontinuity |
| IV first stage | Weak relevance | Exclusion or independence |
| Overidentification test | Incompatibility among some restrictions | Every instrument is valid |
| Event-study pre-fit | Counterfactual model already misses observed data | Forecast stays valid after event |
| Robustness to specifications | Dependence on modeled choice | Identification if all models share one failed assumption |
| Negative control | A specific uncontrolled pathway | Absence of every rival pathway |

## Inference Router

| Dependence/assignment | Default direction |
|---|---|
| Independent cross-section with heteroskedasticity | Heteroskedasticity-consistent SE |
| Treatment assigned by cluster | Cluster at assignment level |
| Repeated observations within unit | Unit/dependence clustering |
| Few clusters | Small-cluster correction or randomization/wild-cluster approach |
| Serially dependent single series | HAC or explicit time-series model |
| Matching/weighting estimated from data | Use estimator-valid analytic variance or a resampling method justified for the specific estimator; ordinary bootstrap can fail for nonsmooth fixed-neighbor matching |
| Weak IV | Weak-identification-robust confidence sets/tests |
| RDD local polynomial | Robust bias-corrected local inference |
| Staggered DiD | Cohort-aware estimator with assignment-level clustering |

## Estimand Tells

- “Among those actually treated” → ATT.
- “For units induced by the instrument” → LATE.
- “At the threshold” → local RDD effect.
- “Effect of assignment/encouragement” → ITT.
- “Across cohort g at time t” → ATT(g,t).
- “All target units under both treatment states” → ATE, requiring support/transport beyond many local designs.
- Large, concentrated, or negative implicit weights → inspect aggregation before interpreting an average.

## Stop Rules

Stop causal interpretation when any applicable condition holds:

- the causal contrast or outcome timing is undefined;
- the source of treatment variation is unknown;
- treatment and outcome have no credible counterfactual comparison;
- controls include unexamined post-treatment variables or colliders;
- positivity/common support fails for the target population;
- staggered DiD relies on already-treated controls under heterogeneous effects;
- IV exclusion has a plausible unaddressed direct path;
- RDD assignment is manipulable or support near the cutoff is inadequate;
- event timing is chosen from the outcome or overlaps a major concurrent shock;
- inference treats dependent observations as independent;
- measurement, missingness, or treatment versions change with treatment in an unmodeled way.

When stopped, return the smallest descriptive result still supported and state what new evidence or design change is required.
