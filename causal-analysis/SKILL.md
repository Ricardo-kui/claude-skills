---
name: causal-analysis
description: Coordinate causal-inference workflows for business-school empirical research. Use when Codex needs to design, run, or audit fixed-effects, DiD, event-study, IV, RDD, matching, or treatment-effect analyses; choose between econometrics-agent, did-analysis, R, Stata, and Python implementations; or plan robustness, placebo, heterogeneity, and verification steps for an empirical paper.
---

# Causal Analysis

## Overview

Use this skill as the routing layer above your existing econometrics stack. It decides which installed skill should lead, what the minimum specification set should be, and how to verify that high-stakes results are reproducible.

## Default Stack

- `did-analysis`: first stop for staggered DiD, event study, TWFE diagnostics, HonestDiD
- `econometrics-agent`: fast local baseline, dataset inspection, and specification sweeps
- `r-econometrics`: production R code for IV, DiD, and RDD
- `stata`: production Stata code, community packages, and table-ready workflows
- `python-panel-data`: panel preprocessing or estimation when the pipeline is already in Python
- `review-code`: correctness and reproducibility check after scripts stabilize
- `empirical-writeup`: tables, figures, methods/results prose after results are verified

## Routing Rules

- DiD or event study with staggered timing: run `did-analysis` before choosing code.
- User explicitly wants the local CLI, a quick result, or a sweep: use `econometrics-agent`.
- User needs final production code in R: use `r-econometrics`.
- User needs final production code in Stata or Stata-specific packages: use `stata`.
- Data cleaning and panel assembly are already in Python: use `python-panel-data` for the implementation lane.
- If the design is still conceptually weak, stop and diagnose identification before coding more specifications.

## Minimum Spec Before Execution

- design type
- outcome
- treatment or endogenous regressor
- unit and time identifiers when panel-like
- clustering level
- core controls
- baseline sample rule
- main threats and planned diagnostics

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
   - modern DiD decision support -> `did-analysis`
   - production R -> `r-econometrics`
   - production Stata -> `stata`
   - Python-native panel pipeline -> `python-panel-data`

4. Verify before expanding:
   - confirm sample size and panel structure
   - confirm coefficient sign, magnitude, SE, and clustering
   - for important headline results, reproduce in a second script or second environment when feasible

5. Hand off only verified artifacts:
   - cleaned analysis data or exact input path
   - script path
   - output table and figure paths
   - residual identification risks
   - next output task for `empirical-writeup`

## Non-Negotiables

- Do not use TWFE by reflex for staggered adoption.
- Do not report causal language beyond what the design can support.
- Do not let heterogeneity or mechanism work outrun baseline credibility.
- Do not present a sweep as evidence unless the preferred specification is justified.

## Reference

Read [references/causal-routing.md](references/causal-routing.md) for the design-to-skill matrix and verification checklist.
Read [references/causal-outputs.md](references/causal-outputs.md) for standard planning, verification, and handoff templates.
Read [references/robustness-battery.md](references/robustness-battery.md) for the identification-threat → robustness-test planning checklist (design layer; the Stata command-level implementation lives in `empirical-pipeline-stata/references/03-robustness-battery.md`).
