# Causal Routing

## Design To Skill

- `staggered did / event study` -> `did-analysis` first, then `r-econometrics` or `stata`
- `quick local baseline or sweep` -> `econometrics-agent`
- `iv / rdd in r` -> `r-econometrics`
- `stata package workflow` -> `stata`
- `python-native panel pipeline` -> `python-panel-data`

## Minimum Spec Grid

- design
- outcome
- treatment or endogenous regressor
- ids and time
- controls
- clustering
- baseline sample

## Verification Checklist

- sample N matches expectation
- coefficient sign and scale are interpretable
- SE and clustering are explicit
- one robustness lane is completed before major expansion
- headline result reproduced in a second script or environment when feasible
