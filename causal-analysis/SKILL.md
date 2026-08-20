---
name: causal-analysis
description: "Turn a locked causal Design Packet into an operational Analysis Manifest and route execution across econometrics skills. Use after huntington-klein-causal-design, before any estimation. Not for inventing the estimand."
when_to_use: "Use when design is locked and the task is estimator choice, diagnostics, robustness lanes, or execution routing (FE/DiD/event-study/IV/RDD/matching)."
whenToUse: "Use when a causal design is already locked and the Design Packet must be turned into an executable Analysis Manifest routed to Stata, R, or Python executors. Trigger words: causal analysis plan, analysis manifest, route execution, choose estimator runtime, 执行规划, 因果分析执行"
---

# Causal Analysis

## Overview

Use this skill as the operational routing layer above the econometrics stack. It consumes a causal Design Packet, decides which installed executor should lead, and emits an Analysis Manifest. Return to `huntington-klein-causal-design` if the estimand, counterfactual, assumptions, or stop rules remain unresolved.

## Default Stack

- `staggered-did`: default Stata executor for staggered adoption, cohort-aware event studies, and DiD diagnostics
- `empirical-pipeline-stata`: default whole-project Stata executor after the design is locked
- `econometrics-agent`: fast local baseline, dataset inspection, and specification sweeps
- `did-analysis`: modern DiD in R only when the user explicitly requests R
- `stata`: production Stata code, community packages, and table-ready workflows
- `empirical-pipeline-python`: Python-native Stage 4 execution when Python is requested or already owns the project
- downstream verification and evidence packaging are owned by `run-empirical-research`, not this router

## Routing Rules

- DiD or event study with staggered timing: use `staggered-did` by default; use `did-analysis` only for an explicit R lane.
- User explicitly wants the local CLI, a quick result, or a sweep: use `econometrics-agent` only after the minimum Design Packet and Analysis Manifest exist; label reconnaissance output as non-authorizing.
- User explicitly needs modern DiD in R: use `did-analysis`. There is no dedicated installed R executor for IV or RDD; do not imply otherwise. Keep execution blocked until the runtime is changed to the locked Stata lane or a dedicated R executor is installed or created and validated.
- User needs final production code in Stata or Stata-specific packages: use `stata`.
- The project is Python-native or Python is explicit: use `empirical-pipeline-python` for the implementation lane.
- If the design is still conceptually weak, stop and diagnose identification before coding more specifications.

## Required Design Packet Before Execution

- design type
- outcome
- treatment or endogenous regressor
- unit and time identifiers when panel-like
- clustering level
- core controls
- baseline sample rule
- main threats and planned diagnostics
- falsification tests and stop rules
- maximum defensible claim

## Standard Workflow

1. Classify the design:
   - `DiD/event-study`
   - `IV`
   - `RDD/fuzzy-RDD`
   - `matching or weighting`
   - `FE / panel baseline`

2. Build the first specification set:
   - baseline model
   - SE or clustering choice
   - one alternative sample or coding choice
   - one main robustness lane (plan the full battery by identification threat — see [references/robustness-battery.md](references/robustness-battery.md))
   - one heterogeneity or mechanism lane only if the core result is credible

3. Choose the execution lane:
   - quick reconnaissance -> `econometrics-agent`
   - modern DiD in Stata -> `staggered-did`
   - whole-project Stata execution -> `empirical-pipeline-stata`
   - explicit modern DiD in R -> `did-analysis`
   - narrow production Stata task -> `stata`
   - Python-native pipeline -> `empirical-pipeline-python`

4. Emit the Analysis Manifest before execution:
   - locked design artifact path
   - Data Contract path and hash
   - runtime and executor
   - estimator, formula, fixed effects, and uncertainty rule
   - sample rule, diagnostics, stop rules, and planned outputs
   - deviation policy

5. Return control to `run-empirical-research`, which owns execution, verification, evidence packaging, and writing handoff. This skill ends after the Analysis Manifest and must not mark results verified.

## Non-Negotiables

- Do not use TWFE by reflex for staggered adoption.
- Do not report causal language beyond what the design can support.
- Do not let heterogeneity or mechanism work outrun baseline credibility.
- Do not present a sweep as evidence unless the preferred specification is justified.
- Do not change the Design Packet silently. Record deviations and invalidate downstream artifacts when material choices change.

## Reference

Read [references/causal-routing.md](references/causal-routing.md) for the design-to-skill matrix and verification checklist.
Read [references/causal-outputs.md](references/causal-outputs.md) for standard planning, verification, and handoff templates.
Read [references/robustness-battery.md](references/robustness-battery.md) for the identification-threat → robustness-test planning checklist (design layer; the Stata command-level implementation lives in `empirical-pipeline-stata/references/03-robustness-battery.md`).
