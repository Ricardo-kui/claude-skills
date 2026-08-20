---
name: empirical-intake
description: "Structure an underspecified empirical project before coding — Intake Packet covering question, estimand, unit/time structure, data assets, sample, measures, risks, deliverables. No estimation or design choice here."
when_to_use: "Stage 0：拿到数据/想法但没有分析简报，或用户要求澄清实证项目时使用。"
whenToUse: "Use when an empirical task is underspecified and the question, data, estimand, and deliverables must be clarified into an Intake Packet before coding or estimation. Trigger words: empirical intake, intake packet, structure my project, clarify the analysis, 梳理实证项目, 明确研究需求, 给了数据但没说明白"
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
   - whether any analysis variable is produced by human coding, text/image/audio processing, an LLM or another fitted model, or synthetic generation

3. Inspect available assets before asking follow-up questions:
   - use `exploratory-data-analysis` for unknown files or unfamiliar formats
   - use `econometrics-agent` dataset inspection wrappers when the user wants that local CLI
   - use `api-data-fetcher` when data still needs to be pulled from public APIs

4. Surface only the critical unresolved risks:
   - identification risk for causal work
   - leakage or split risk for ML work
   - sample construction or missingness risk for any empirical work
   - construct, timing, validation, and provenance risk for derived measures or labels
   - unclear output contract for downstream writing

   When a derived measure is material, record its construct role, source corpus and time boundary, generation or coding process, available human-validation sample, and whether the same source or model also generates another variable in the analysis. Do not require these fields when all core variables are directly observed.

5. Route immediately after intake:
   - `huntington-klein-causal-design` for causal questions, then `causal-analysis` after the Design Packet is locked
   - `ml-analysis` for predictive workflows
   - `exploratory-data-analysis` for pure data audit
   - `review-code` / `check-methodology` when analysis exists but verification is missing; `empirical-writeup` only after verification

## Intake Packet Contract

Return a short memo with these fields:

- `task_type`
- `question`
- `estimand_or_target`
- `data_assets`
- `sample_and_structure`
- `variables_or_features`
- `derived_measurement_status` when applicable
- `main_risks`
- `requested_outputs`
- `unresolved_inputs`
- `recommended_next_skill`

## Default Downstream Pairings

- Unknown dataset + unclear goal -> `exploratory-data-analysis` then re-enter intake
- Public macro or policy series needed -> `api-data-fetcher`
- Quick causal smoke test requested -> lock a minimal Design Packet and Analysis Manifest first, then use `econometrics-agent`; label the result reconnaissance-only
- Staggered DiD or event study -> `huntington-klein-causal-design`, then `causal-analysis`; default execution is Stata via `staggered-did`
- Prediction or classification -> `ml-analysis`
- Regression tables, figures, methods/results prose -> verify first if needed, then `empirical-writeup`

## Reference

Read [references/intake-checklists.md](references/intake-checklists.md) for the exact field checklist.
Read [references/intake-outputs.md](references/intake-outputs.md) for standard intake memo templates.
