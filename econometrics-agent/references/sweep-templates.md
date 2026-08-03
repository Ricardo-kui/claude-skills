# Sweep Templates (Robustness Design)

Source: extracted from `_template_sweep_specs` and `_suggest_sweep_template` in
`lite_econometrics_agent.py`. The `sweep` subcommand runs many specifications in
one pass and assembles a comparison table plus a results paragraph. The value
worth reusing is the **robustness-design logic** — which variants a careful
researcher compares for each design family — independent of the CLI that
executes them.

## Built-in templates

Each template expands to a fixed list of specifications:

| Template | Specifications it generates |
| --- | --- |
| `ols-covariance` | robust SE; HAC with 2 lags |
| `pscore-suite` | psm; ipw; aipw; ipwra |
| `rdd-sensitivity` | local-linear; global-poly order 2; global-poly order 3 |
| `panel-covariance` | FE with auto covariance; FE with two-way clustering |
| `smart` | picks one of the above from `base_spec` (see router below) |

The `smart` router inspects the base spec and chooses:

- running variable **and** cutoff present → `rdd-sensitivity`;
- entity_id **and** time_id present → `panel-covariance`;
- model is one of psm/ipw/aipw/ipwra, or query mentions those → `pscore-suite`;
- otherwise → `ols-covariance`.

## Three configuration modes

A sweep config (`sweep.json`) can combine three modes:

- **`specs`** — an explicit list of named specifications; each is a full run config.
- **`template`** — invoke a built-in template (above) by name, or a list of them.
- **`expand`** — declare a grid over parameters (e.g. `cov_type: [robust, hac]`, `hac_maxlags: [1, 2]`) and auto-expand the cross product.
- **`table`** — layout control for the assembled comparison table.

## Table layout fields (`table`)

Supported fields when assembling the multi-model table:

- `drop_terms` — terms to omit from the coefficient rows (e.g. `const`).
- `row_order` — explicit ordering of coefficient rows.
- `stats_rows` — footer statistics; beyond `N` and `R2` also supports `Model`, `Covariance`, `Estimand`, `Bandwidth`, `PolyOrder`, `RDDMode`, `MainTerm`.
- `model_labels`, `group_headers`, `title`, `depvar_label`, `notes`.

## Why this matters beyond the CLI

The templates encode a defensible default robustness narrative for each design
family: for OLS, show sensitivity to the covariance assumption; for propensity-
score work, show the full suite so the reader sees the estimate is not an
artifact of one weighting scheme; for RDD, show bandwidth/functional-form
sensitivity; for panel, show sensitivity to the clustering choice. When you
design a robustness section in Stata, the same families apply — these templates
are a checklist for which alternatives a referee will expect to see.

For exact CLI invocation, see `command-patterns.md`. For what each estimator in
a sweep means and where it fails, see `method-cards.md`.
