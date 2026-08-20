---
name: ml-analysis
description: "为实证研究中的机器学习任务做规划与治理：预测/分类目标定义、特征工程、训练-验证-测试划分、数据泄漏控制、模型比较与调参、可解释性与 ML 稳健性。触发：机器学习、预测模型、分类、特征重要性、模型评估。"
whenToUse: "当用户说“用机器学习预测……”“做个分类/预测模型”“训练验证测试集怎么切”“防止数据泄漏”“比较几个模型”“调超参”“看特征重要性/SHAP 解释”“做 ML 稳健性检验”时使用；设计锁定后交 empirical-pipeline-python 执行。"
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
