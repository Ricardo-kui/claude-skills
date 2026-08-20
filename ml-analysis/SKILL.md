---
name: ml-analysis
description: "Structure ML workflows for empirical research — prediction, classification, feature engineering, train-test design, leakage control, tuning, interpretation, ML robustness on business/strategy/marketing/operations data."
when_to_use: "实证研究中的预测/分类/特征工程/ML 稳健性任务（Python 侧）时使用。"
whenToUse: "Use when structuring a machine-learning workflow for empirical research, covering target definition, train-validation-test splits, leakage control, baselines, tuning, and model interpretation. Trigger words: ML analysis, prediction model, feature engineering, train test split, leakage, model comparison, 机器学习流程, 预测模型, 特征工程"
---

# Ml Analysis

## Overview

Use this skill as the planning and governance layer for ML work in empirical projects. It locks target definition, splits, baselines, validation, and interpretation before `empirical-pipeline-python` executes the Analysis Manifest.

## Current Stack Reality

- `exploratory-data-analysis`: first pass on unfamiliar data files
- `jupyter-notebook`: use when the deliverable should be a notebook
- `empirical-pipeline-python`: execute the locked ML Analysis Manifest when Python is requested or already owns the project
- `empirical-writeup`: use after metrics, plots, and interpretation are stable
- `econometrics-agent`: use only for its supported econometric or propensity-score tasks, not as a general ML engine

## Minimum Inputs

- target variable
- unit of observation
- prediction timestamp or decision point
- candidate features
- split rule
- evaluation metric
- desired output: score, ranking, class, forecast, feature importance, or benchmark table

## Pipeline Contracts

At Stage 2, produce an **ML Design Packet** with the prediction point, label horizon, target population, unit, feature-availability boundary, split logic, primary metric, untouched holdout policy, leakage risks, and noncausal claim ceiling.

At Stage 3, produce an **ML Analysis Manifest** with the Data Contract path and hash, runtime, environment, data-build path, feature pipeline, benchmark ladder, tuning budget, threshold or decision rule, calibration plan, error-slice plan, output paths, and deviations policy.

Do not merge these contracts: the executor may tune implementation choices inside the manifest but may not redefine the prediction target or holdout policy.

## Standard Workflow

1. Define the task correctly:
   - regression
   - binary or multiclass classification
   - ranking
   - time-aware forecasting
   - auxiliary ML for an empirical paper

2. Lock the split before feature work:
   - random split only when iid assumptions are plausible
   - time split for panel or temporal data
   - group-aware split when the same firm, user, or product appears repeatedly

3. Run a model ladder instead of jumping to a complex model:
   - naive benchmark
   - transparent baseline such as linear, logit, or lasso
   - tree ensemble only if it improves out-of-sample performance materially

4. Guard against leakage:
   - exclude future information
   - exclude post-outcome or post-treatment fields unless explicitly intended
   - confirm that engineered features would exist at prediction time

5. Evaluate in business-research terms:
   - choose metrics that fit the task
   - check calibration when probabilities matter
   - inspect error slices by firm, cohort, or time period
   - separate predictive usefulness from causal interpretation

6. Interpret carefully:
   - feature importance is not causal evidence
   - SHAP, PDP, or partial effects should be post-validation interpretation tools
   - if the user really wants causal ML, state that this stack lacks a dedicated installed double-ML or causal-forest skill and tighten the scope first

## Deliverables

- data split rule
- feature list and exclusions
- model comparison table
- chosen model and hyperparameters
- out-of-sample metrics
- error analysis notes
- figure list for `empirical-writeup`
- or an ML Delivery Handoff when the endpoint is an operational model rather than a paper

## Reference

Read [references/ml-workflow.md](references/ml-workflow.md) for the model ladder, metric mapping, and leakage checklist.
Read [references/ml-outputs.md](references/ml-outputs.md) for standard experiment, evaluation, and interpretation templates.
