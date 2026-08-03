---
name: ml-analysis
description: Structure machine-learning workflows for empirical research. Use when Codex needs prediction, classification, feature engineering, train-validation-test design, leakage control, model comparison, tuning, model interpretation, or ML-oriented robustness checks on business, strategy, marketing, or operations datasets.
---

# Ml Analysis

## Overview

Use this skill as the planning and governance layer for ML work in empirical projects. It does not assume a dedicated installed ML executor; instead, it forces a clean workflow around target definition, splits, baselines, validation, and interpretation before coding.

## Current Stack Reality

- `exploratory-data-analysis`: first pass on unfamiliar data files
- `jupyter-notebook`: use when the deliverable should be a notebook
- `python-panel-data`: use when panel indexing, aggregation, or FE-style preprocessing is central
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

## Reference

Read [references/ml-workflow.md](references/ml-workflow.md) for the model ladder, metric mapping, and leakage checklist.
Read [references/ml-outputs.md](references/ml-outputs.md) for standard experiment, evaluation, and interpretation templates.
