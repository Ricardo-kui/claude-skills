---
name: empirical-pipeline-python
description: "Python 实证执行流水线：把锁定的 Analysis Manifest 在 Python 中执行为可复现脚本、环境记录、日志、诊断、表图与 Run Manifest。仅当项目明确要求 Python 或已是 Python-native 时使用；需已有 Design Packet 与 Analysis Manifest，不用于选 estimand、追显著性或写正文。"
whenToUse: "当用户明确要用 Python（而非 Stata）执行实证分析、用 Python 跑回归/机器学习/因果估计、或项目本来就是 Python 原生时使用。触发词：用 Python 跑、Python 版回归、Python 实证执行、用 linearmodels/statsmodels 做"
---

# Empirical Pipeline — Python

## Purpose

Own only Stage 4 execution. Convert an approved Analysis Manifest into reproducible Python artifacts without changing the research question, estimand or prediction target, sample rule, split rule, estimator family, uncertainty rule, or stop rules.

For an end-to-end project, enter through `run-empirical-research`. Use this skill directly only when the required design and plan artifacts already exist.

## Entry Gate

Require:

- a causal Design Packet or ML Design Packet;
- its matching Analysis Manifest;
- the Data Contract path and hash recorded in the Analysis Manifest;
- explicit Python selection or an existing Python-native project;
- resolvable input data and output paths.

If the Data Contract is missing, mark execution `blocked` and return to Stage 1. If a design or planning artifact is missing or the artifacts conflict, stop and return to `huntington-klein-causal-design` plus `causal-analysis`, or to `ml-analysis`. Do not infer a convenient design from the available columns.

## Execution Workflow

1. Read the project-local `AGENTS.md`, existing environment files, data-build scripts, and Analysis Manifest. Inspect before creating a new project structure.
2. Record the interpreter, OS, package versions, random seeds, input hashes, and command used to run the analysis. Reuse the project's declared environment; otherwise create a minimal lock file appropriate to the project.
3. Verify the actual Data Contract file hash against the Analysis Manifest, then validate the input against that contract: unit and time keys, uniqueness, missingness, treatment timing or label horizon, sample funnel, merge cardinality, and row counts. Stop on a material mismatch.
4. Build one deterministic entry point such as `src/run_analysis.py` or an explicitly requested notebook plus a non-interactive runner. Keep data construction, estimation, and export separable enough to audit.
5. Execute only the baseline, diagnostics, robustness checks, and conditional extensions authorized by the Analysis Manifest. A failed diagnostic is a result, not permission to switch specifications.
6. Capture stdout/stderr, warnings, convergence status, actual analytic sample, model formula, covariance or resampling rule, and every deviation from the manifest.
7. Export stable machine-readable results alongside publication-facing tables or figures. Test that a clean rerun succeeds and that reported numbers are generated from saved model objects rather than copied manually.

Read [references/runtime-checklist.md](references/runtime-checklist.md) only when selecting libraries, laying out artifacts, or checking a run.

## Method Boundaries

- For ordinary regression, panel, IV, RDD, weighting, or survival work, use a maintained Python implementation only when it can reproduce the estimator and inference rule named in the Analysis Manifest.
- For staggered-adoption DiD, the default owner remains `staggered-did` in Stata. Run it here only when Python was explicitly selected and the manifest names a validated cohort-aware Python implementation. Never substitute conventional TWFE or silently bridge to R.
- For prediction, use leakage-safe preprocessing inside the fitted pipeline, honor group/time splits and the untouched holdout, and report benchmark-relative out-of-sample performance, calibration when relevant, and prespecified error slices.
- For causal ML, require a causal Design Packet and explicit nuisance, overlap, cross-fitting, estimand, and inference rules. Feature importance or CATE heterogeneity alone does not establish a causal mechanism.
- Do not manufacture a universal diagnostic or robustness battery. Each check must map to a declared estimator requirement or identification threat.

## Output Contract

Return a **Run Manifest** containing:

- exact inputs and hashes;
- entry command, scripts/notebooks, environment and seed;
- actual sample, formula/features, estimator, inference/split rule, and runtime status;
- diagnostics and stop-rule outcomes;
- deviations, warnings, and unresolved failures;
- paths to logs, models, tables, figures, and machine-readable results.

Return a **Results Inventory** in which every result has an ID, model or metric definition, sample, estimate and uncertainty or evaluation metric, artifact path, diagnostic status, and claim ceiling.

Hand both artifacts to `review-code` and `check-methodology`. Do not mark results verified and do not hand unverified results directly to a section writer.

## Fail-Closed Rules

- Do not replace unavailable packages with a different estimator without revising the Analysis Manifest.
- Do not install or upgrade packages silently when that would change the environment.
- Do not tune on the test set, choose a headline specification by p-value, hide failed runs, or relabel association as causation.
- If dependency preflight fails, still write a failure-state Run Manifest and a schema-valid zero-row Results Inventory; do not advance to verification or writing.
- If Python cannot implement the locked design credibly, mark execution `blocked`, record the incompatibility, and return to `causal-analysis` for an explicit runtime decision.
