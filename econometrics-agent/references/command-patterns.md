# Econometrics-Agent Command Patterns

Use this reference when constructing commands for the installed local CLI.

## Entrypoints

Primary:

```powershell
econometrics-agent
```

Fallback:

```powershell
C:\Users\admin\Econometrics-Agent\.venv\Scripts\python.exe C:\Users\admin\Econometrics-Agent\lite_econometrics_agent.py
```

## Inspect Before You Run

Use this when the dataset is present but the right columns are not yet pinned down:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\admin\.claude\skills\econometrics-agent\scripts\inspect_dataset.ps1 -Data "C:\path\to\data.dta"
```

Add `-SheetName "Sheet1"` for Excel files when needed.

Save the inspection output when you want to generate a draft command:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\admin\.claude\skills\econometrics-agent\scripts\inspect_dataset.ps1 -Data "C:\path\to\data.dta" -OutFile ".\inspection.json"
```

Generate a draft `run` command from that inspection JSON:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\admin\.claude\skills\econometrics-agent\scripts\draft_run_command.ps1 -Inspection ".\inspection.json" -Model fe
```

Preferred one-step path:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\admin\.claude\skills\econometrics-agent\scripts\draft_run_command.ps1 -Data "C:\path\to\data.dta" -Model fe
```

Override fields explicitly when the heuristic draft is not enough:

```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\admin\.claude\skills\econometrics-agent\scripts\draft_run_command.ps1 -Inspection ".\inspection.json" -Model did -Outcome y -Treatment treated_indicator -EntityId firm_id -TimeId year -TreatGroup treated_firm -Post post_policy
```

## Subcommands

### `knowledge`

Use for method cards or capability explanations.

```powershell
econometrics-agent knowledge --model all
econometrics-agent knowledge --model iv
```

Supported `--model` values:

- `all`
- `ols`
- `fe`
- `iv`
- `did`
- `event-study`
- `psm`
- `ipw`
- `aipw`
- `ipwra`
- `rdd`
- `fuzzy-rdd`

### `demo`

Use for smoke tests or onboarding.

```powershell
econometrics-agent demo
econometrics-agent demo --output-dir "C:\path\to\demo_output"
```

### `run`

Core shape:

```powershell
econometrics-agent run `
  --data "C:\path\to\data.dta" `
  --query "estimate the policy effect with firm and year fixed effects" `
  --outcome y `
  --treatment treat
```

Core optional flags:

- `--controls x1 x2 ...`
- `--model auto|ols|fe|iv|did|event-study|psm|ipw|aipw|ipwra|rdd|fuzzy-rdd`
- `--cov-type auto|robust|cluster|cluster-both|hac`
- `--cluster cluster_var`
- `--weights weight_var`
- `--save-summary path.json`
- `--export-terms path.csv|path.tex`
- `--export-balance path.csv`
- `--export-narrative path.md`
- `--label-map labels.json`

Panel:

- `--entity-id`
- `--time-id`

DID:

- `--treat-group`
- `--post`

IV:

- `--instrument`

RDD and fuzzy RDD:

- `--running-variable`
- `--cutoff`
- `--bandwidth`
- `--kernel uniform|triangle|epanechnikov`
- `--rdd-mode auto|local-linear|global-poly`
- `--poly-order`

Propensity-score estimators:

- `--estimand ATE|ATT`
- `--matched-num`

Event-study:

- `--lead-window`
- `--lag-window`

### `sweep`

Use when the user wants multiple specifications compared in one pass.

```powershell
econometrics-agent sweep `
  --config "C:\path\to\sweep.json" `
  --export-models-table "C:\path\to\sweep_table.csv" `
  --export-results-paragraph "C:\path\to\sweep_results.md"
```

The config can use:

- `base_spec`
- `specs`
- `template`
- `expand`
- `table`

Built-in templates:

- `ols-covariance`
- `pscore-suite`
- `rdd-sensitivity`
- `panel-covariance`
- `smart`

## Common Templates

### FE

```powershell
econometrics-agent run `
  --data "C:\path\to\panel.dta" `
  --query "estimate the policy effect with firm and year fixed effects" `
  --outcome y `
  --treatment treat `
  --controls x1 x2 `
  --entity-id firm_id `
  --time-id year
```

### IV

```powershell
econometrics-agent run `
  --data "C:\path\to\iv_sample.csv" `
  --query "estimate the endogenous treatment effect with IV-2SLS" `
  --outcome y `
  --treatment treat `
  --controls x1 x2 `
  --instrument z `
  --model iv
```

### DID

```powershell
econometrics-agent run `
  --data "C:\path\to\did_panel.dta" `
  --query "estimate the policy effect with difference in differences" `
  --outcome y `
  --treatment treated_indicator `
  --controls x1 x2 `
  --entity-id firm_id `
  --time-id year `
  --treat-group treated_firm `
  --post post_policy `
  --model did
```

### RDD

```powershell
econometrics-agent run `
  --data "C:\path\to\cutoff_sample.csv" `
  --query "run a sharp RDD around the score cutoff" `
  --outcome y `
  --treatment treat `
  --controls x1 `
  --running-variable score `
  --cutoff 0 `
  --model rdd
```

## Output Expectations

The tool prints:

- structured JSON summary
- coefficient table
- diagnostics
- reflection notes when relevant

The most decision-useful fields are usually:

- `selected_model`
- `selection_reasons`
- `main_result`
- `diagnostics`
- `reflection`

For common failures and retry rules, open `troubleshooting.md` in the same `references/` folder.
