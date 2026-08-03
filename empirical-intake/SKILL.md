---
name: empirical-intake
description: Structure empirical research intake before coding or estimation. Use when Codex needs to turn a vague empirical idea, dataset, or research design into an execution-ready brief covering question, estimand or prediction target, unit and time structure, sample, variables, threats, success criteria, and downstream deliverables. Trigger for requests such as "先帮我梳理这个实证项目", "先做 intake", "这份数据该怎么分析", "帮我把研究设计说清楚", or when a data file is provided without a clear analysis brief.
---

# Empirical Intake

## Overview

Use this skill to convert an underspecified empirical task into a compact handoff brief. Keep the intake short, evidence-backed, and explicitly routed to the next skill instead of mixing clarification, estimation, and writing in one pass.

## Core Rules

- Inspect files before asking for schema facts that can be discovered directly.
- Ask only for the highest-leverage unresolved choice when the data or design is still ambiguous.
- Do not guess variable names, treatment timing, target labels, or clustering levels.
- Separate four task types early: `causal`, `ml`, `descriptive`, `writeup`.
- Produce a handoff brief before deeper execution.

## Minimal Intake Workflow

1. Classify the task:
   - `causal`: DiD, event study, IV, RDD, FE, matching, policy shock
   - `ml`: prediction, classification, feature engineering, model comparison
   - `descriptive`: data audit, summary stats, exploratory inspection
   - `writeup`: methods/results text, tables, figures, appendix material

2. Collect the smallest workable brief:
   - research question
   - estimand or prediction target
   - unit of observation and time structure
   - outcome, treatment, key features, or labels
   - data asset paths and file formats
   - target outputs: table, figure, cleaned data, model object, draft text

3. Inspect available assets before asking follow-up questions:
   - use `exploratory-data-analysis` for unknown files or unfamiliar formats
   - use `econometrics-agent` dataset inspection wrappers when the user wants that local CLI
   - use `api-data-fetcher` when data still needs to be pulled from public APIs

4. Surface only the critical unresolved risks:
   - identification risk for causal work
   - leakage or split risk for ML work
   - sample construction or missingness risk for any empirical work
   - unclear output contract for downstream writing

5. Route immediately after intake:
   - `causal-analysis` for causal or panel designs
   - `ml-analysis` for predictive workflows
   - `exploratory-data-analysis` for pure data audit
   - `empirical-writeup` when the analysis already exists and the bottleneck is presentation

## Intake Memo Contract

Return a short memo with these fields:

- `task_type`
- `question`
- `estimand_or_target`
- `data_assets`
- `sample_and_structure`
- `variables_or_features`
- `main_risks`
- `requested_outputs`
- `recommended_next_skill`

## Default Downstream Pairings

- Unknown dataset + unclear goal -> `exploratory-data-analysis` then re-enter intake
- Public macro or policy series needed -> `api-data-fetcher`
- Quick causal smoke test requested -> `econometrics-agent` after intake
- Staggered DiD or event study -> `causal-analysis` with `did-analysis` first
- Prediction or classification -> `ml-analysis`
- Regression tables, figures, methods/results prose -> `empirical-writeup`

## Reference

Read [references/intake-checklists.md](references/intake-checklists.md) for the exact field checklist.
Read [references/intake-outputs.md](references/intake-outputs.md) for standard intake memo templates.
