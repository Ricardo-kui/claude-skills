# Python Runtime Checklist

Load this file only for Stage 4 Python execution.

## Library Selection

Prefer the smallest maintained stack that implements the locked manifest:

- data and serialization: `pandas` or `polars`, `pyarrow` when required;
- statistical models: `statsmodels`, `linearmodels`, or `pyfixest` when their estimator and covariance behavior match the manifest;
- prediction: `scikit-learn` pipelines and metrics;
- survival: `lifelines` or another manifest-approved implementation;
- tables and figures: derive exports from saved result objects with `pandas`, `matplotlib`, or `seaborn`.

Do not select a package because it yields a preferred estimate. Record the package version and any estimator limitation that affects interpretation.

## Minimum Artifact Layout

Adapt to an existing project layout. For a new project, the minimum is:

```text
data/              # source or analysis-ready inputs; never overwrite raw data
src/               # deterministic data build and analysis entry point
logs/               # stdout, stderr, warnings, run metadata
results/models/     # serialized fitted objects when stable and safe
results/tables/     # csv plus requested publication format
results/figures/    # vector format when possible
run_manifest.yaml
results_inventory.csv
```

## Reproduction Check

Before handoff, confirm:

1. the recorded command exits successfully in the declared environment;
2. input hashes and analytic row counts match the Run Manifest;
3. random components use recorded seeds and deterministic settings where available;
4. exported estimates or metrics can be regenerated from code and saved objects;
5. warnings, failed diagnostics, exclusions, and deviations remain visible;
6. no output path points outside the authorized project directory unless the user requested it.
