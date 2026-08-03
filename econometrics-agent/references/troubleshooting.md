# Econometrics-Agent Troubleshooting

Use this reference when the installed local CLI fails or the user gives an underspecified request.

## 1. Command Not Found

Symptoms:

- `econometrics-agent` is not recognized

Fallback:

```powershell
C:\Users\admin\Econometrics-Agent\.venv\Scripts\python.exe C:\Users\admin\Econometrics-Agent\lite_econometrics_agent.py --help
```

If that also fails, check whether the local install still exists at `C:\Users\admin\Econometrics-Agent`.

## 2. Missing Or Wrong Variable Names

Symptoms:

- column not found
- outcome or treatment name does not exist
- model arguments do not match the dataset

Action:

1. Run the bundled dataset inspection wrapper.
2. Use the one-step draft-command wrapper with `-Data` to generate a first-pass command.
3. Ask one short question if outcome or treatment is still ambiguous.

Do not guess from partial name matches.

## 3. Unsupported File Type Or Bad Path

Supported file types:

- `csv`
- `dta`
- `parquet`
- `xlsx`

Action:

- verify the file path is absolute and exists
- verify the extension matches a supported type
- for Excel, add `-SheetName` during inspection when the default sheet is not the right one

## 4. FE, DID, Or Event-Study Fails

Common causes:

- missing `entity-id`
- missing `time-id`
- panel keys are present but misspelled
- event-study requested on treatment that is not monotone binary adoption

Action:

- inspect the dataset
- verify panel identifiers
- if the treatment turns on and off repeatedly, do not force event-study through this CLI

## 5. IV Fails

Common causes:

- missing `instrument`
- more than one instrument requested
- instrument column is misspelled

Action:

- verify a single instrument column exists
- rerun with `--model iv` if the user explicitly wants IV
- if the user wants multiple instruments or richer IV diagnostics, use another workflow

## 6. Propensity-Score Estimators Fail

Common causes:

- treatment is not binary
- no credible control covariates were provided
- overlap is poor

Action:

- verify treatment is binary
- inspect the covariate set
- report overlap or balance problems instead of hiding them

## 7. RDD Or Fuzzy-RDD Fails

Common causes:

- missing `running-variable`
- missing `cutoff`
- wrong model selected for the design

Action:

- verify the running variable and cutoff
- choose `--model rdd` for sharp designs
- choose `--model fuzzy-rdd` when the cutoff shifts treatment probability rather than assigning treatment deterministically

## 8. Covariance Or Clustering Fails

Common causes:

- `cluster-both` used without panel-style identifiers
- cluster variable missing
- HAC used where the model or design does not support it well

Action:

- fall back to `--cov-type robust` when the request is underspecified
- only use `cluster-both` when entity and time structure are actually present

## 9. When To Stop Retrying

Stop after one informed retry if the issue is structural rather than syntactic. Examples:

- the requested design is unsupported by this CLI
- the file type is unsupported
- the user has not provided enough information to identify the right variables

At that point, explain the blocker plainly and either ask one short question or route to a more suitable analysis workflow.
