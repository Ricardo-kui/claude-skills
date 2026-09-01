---

> **⚠ 休眠状态（2026-09-01）**：底层 CLI `~/Econometrics-Agent` 在本机未安装（PATH 无、目录不存在）。本 skill 仍保留在 causal-analysis/empirical-intake 的路由体系中；触发时会提示 CLI 缺失，安装后再启用。
name: econometrics-agent
description: "Run the local econometrics-agent CLI (~/Econometrics-Agent) on csv/dta/parquet/xlsx — OLS, FE, IV, DiD, event-study, PSM, IPW, RDD, balance/coef tables, spec sweeps. Use only when this specific CLI is wanted."
when_to_use: "Trigger on explicit mentions of econometrics-agent 或本地计量 agent；不用于纯方法论咨询。"
whenToUse: "Use when the user explicitly wants the local econometrics-agent CLI to run econometric models, inspect a dataset, or produce balance and coefficient tables quickly. Trigger words: econometrics-agent, local econometrics CLI, 本地计量工具, quick regression run, specification sweep, dataset inspection"
---

# Econometrics Agent

Use the installed `econometrics-agent` command as a local execution layer for quick, structured econometric runs. Prefer this skill when the user wants this specific CLI or wants a fast local result instead of hand-written R, Stata, or Python code.

## Decide Whether To Use It

Use this skill when the user wants one of these:

- the `econometrics-agent` tool itself
- this installed local econometrics agent or local econometrics CLI
- a quick local run with structured JSON plus a coefficient table
- a dataset inspected before choosing variables for this CLI
- exports such as balance tables, term tables, narrative markdown, or sweep outputs
- a smoke test of the installed econometrics agent

Do not use this skill when the task is mainly:

- conceptual estimator choice without execution
- identification critique or methodology review
- manuscript writing or rewriting
- code review of hand-written Stata, R, or Python

In those cases, prefer the existing econometrics or writing skills unless the user explicitly asks for this CLI.

## Use The Right Entry Point

Prefer the global command, provided by a shim in `~/.local/bin` (an extensionless bash shim for git-bash, and `econometrics-agent.cmd` for PowerShell/cmd):

```powershell
econometrics-agent
```

If the shim is ever missing, fall back to the fixed local install:

```powershell
~/Econometrics-Agent/.venv/Scripts/python.exe ~/Econometrics-Agent/lite_econometrics_agent.py
```

## Inspect The Dataset Deterministically

If the user gives a data file but does not clearly specify the usable column names, inspect it before building the `run` command.

Prefer the bundled wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/econometrics-agent/scripts/inspect_dataset.ps1 -Data "C:\path\to\data.dta"
```

This prints a compact JSON profile with:

- row and column counts
- column names and dtypes
- missingness
- simple sample values
- candidate id, time, and binary-treatment columns

The preferred one-step path is:

```powershell
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/econometrics-agent/scripts/draft_run_command.ps1 -Data "C:\path\to\data.dta" -Model fe
```

If you want a two-step path with a saved inspection artifact, save the JSON and pass it to the bundled draft-command wrapper:

```powershell
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/econometrics-agent/scripts/inspect_dataset.ps1 -Data "C:\path\to\data.dta" -OutFile ".\inspection.json"
powershell -ExecutionPolicy Bypass -File ~/.claude/skills/econometrics-agent/scripts/draft_run_command.ps1 -Inspection ".\inspection.json" -Model fe
```

If the user still has not chosen `outcome` or `treatment` after inspection, ask one short follow-up question. Do not guess.

## Gather The Minimum Spec

Collect these before running:

- required for almost every `run`: `data`, `outcome`, `treatment`
- optional but common: `controls`, `query`, `model`, `cov-type`, `cluster`
- panel models: `entity-id`, `time-id`
- DID: `treat-group`, `post`, usually also `entity-id` and `time-id`
- IV: `instrument`
- RDD and fuzzy RDD: `running-variable`, `cutoff`, optionally `bandwidth`, `rdd-mode`, `poly-order`
- propensity-score estimators: usually `controls`, optionally `estimand`

If the user gives a file but not the column names, inspect the dataset schema first with the bundled inspection script. Do not guess variable names.

## Choose The Subcommand

- `knowledge`: explain what a model does or what the tool supports
- `demo`: smoke-test the installation or show example outputs
- `run`: execute one specification
- `sweep`: run multiple specifications from a JSON config and export a comparison table or results paragraph

Open [command-patterns.md](~/.claude/skills/econometrics-agent/references/command-patterns.md) when you need exact command templates or option reminders. Open [troubleshooting.md](~/.claude/skills/econometrics-agent/references/troubleshooting.md) when the command fails or the user gives an incomplete specification.

## Method Knowledge (Reusable Across Skills)

The econometric reasoning behind this CLI is documented as prose so other skills (`causal-analysis`, `did-analysis`, `stata`, and the write/review stack) can reuse it, not just this CLI:

- [method-cards.md](~/.claude/skills/econometrics-agent/references/method-cards.md) — per-estimator cards: when to use, identification logic, diagnostics, failure modes, and a **Tool boundary** line marking where this CLI stops and Stata should take over.
- [model-selection-rules.md](~/.claude/skills/econometrics-agent/references/model-selection-rules.md) — the transparent, rule-based routing tree and how selection reasons are generated.
- [diagnostics-and-reflection.md](~/.claude/skills/econometrics-agent/references/diagnostics-and-reflection.md) — what the CLI auto-detects (routing upgrades, data cleaning, per-estimator diagnostics) and what the researcher still owes.
- [sweep-templates.md](~/.claude/skills/econometrics-agent/references/sweep-templates.md) — robustness-sweep design (covariance, pscore-suite, RDD sensitivity, panel clustering).

When the user asks conceptual estimator-choice or identification questions without wanting this CLI, read these reference files instead of running the tool.

## Execute Carefully

When building commands:

- keep the user's intent in `--query`; the tool uses it for routing and explanation
- prefer absolute paths for input and export files
- only use supported flags; do not invent shorthand or new options
- choose explicit `--model` when the user has already decided the estimator
- keep `--model auto` when the user wants the tool to route based on structure and query

If the user asks for exported artifacts and does not specify paths, write them into the current working directory with descriptive names derived from the task.

## Recover From Common Failures

Before retrying, identify which class of failure you have:

- path or format problem
- missing variable names or wrong variable names
- model-specific argument mismatch
- covariance or clustering mismatch
- unsupported design for this CLI

Use the smallest fix that addresses the failure. Prefer one retry after inspecting the error. If the design itself is unsupported, say so explicitly and route to a more appropriate workflow instead of forcing this CLI.

## Report The Result

After execution, summarize the output in user-facing language:

- `selected_model`
- `selection_reasons`
- the main coefficient, uncertainty, and significance
- diagnostics and reflection notes
- any exported files that were created
- any identification or support limitations the tool itself surfaced

Do not restate the full JSON unless the user asks for it. Pull out the economically relevant result and the main caveats.

## Respect The Tool Boundaries

Keep these constraints visible:

- supported file formats: `csv`, `dta`, `parquet`, `xlsx`
- FE, DID, and event-study need `entity-id` and `time-id`
- IV currently supports one instrument
- event-study assumes monotone binary treatment adoption
- PSM, IPW, AIPW, and IPWRA are for binary treatment settings
- `cluster-both` is mainly for panel-style models
- this tool helps execute designs; it does not replace identification judgment
