# Causal Routing

## Design To Skill

- `staggered did / event study, Stata default` -> `staggered-did`
- `staggered did / event study, explicit R` -> `did-analysis`
- `complete locked Stata design` -> `empirical-pipeline-stata`
- `quick local baseline or sweep` -> `econometrics-agent`
- `iv / rdd in explicit R` -> no dedicated installed executor; keep execution blocked until the runtime changes to Stata or a dedicated R executor is installed or created and validated
- `stata package workflow` -> `stata`
- `python-native full pipeline` -> `empirical-pipeline-python`

## Minimum Spec Grid

- design
- outcome
- treatment or endogenous regressor
- ids and time
- controls
- clustering
- baseline sample
- diagnostics, falsification tests, and stop rules

## Handoff boundary

End after the Analysis Manifest. `run-empirical-research` owns execution and routes post-run implementation verification to `review-code` and methodological verification to `check-methodology`.
