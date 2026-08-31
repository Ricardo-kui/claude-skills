---
name: check-methodology
description: "方法论可信度审查：核验已执行的因果/计量/预测 ML 分析是否支撑其主张——识别、推断、稳健性、安慰剂检验、数据泄露、校准、派生变量测量与主张上限，产出方法学 Verification Report。不用于文笔润色或代码风格审查。"
whenToUse: "当用户要检查实证结果是否可信、审查识别假设与稳健性是否到位、核验显著结果能否支撑因果主张、或检查 ML 分析有没有泄露时使用。触发词：方法审查、这个结果可信吗、核验一下、稳健性够不够、check methodology、Verification Report"
---

# Check Methodology

## Purpose

Determine whether the executed analysis supports its intended empirical claim. Treat coefficient significance as evidence to interpret, not as proof of identification; treat predictive performance as out-of-sample evidence, not as causal evidence.

## Inputs

- research question and intended claim
- causal or ML Design Packet
- Analysis Manifest
- sample construction and variable definitions
- model outputs, metrics, and diagnostics
- robustness, placebo, falsification, or sensitivity results
- measurement provenance and validation artifacts when a treatment, outcome, covariate, feature, or label is derived rather than directly observed
- code-review findings when available

## Audit Workflow

1. Classify the lane as causal/econometric or predictive ML. Do not combine their claim standards.
2. For causal/econometric work, reconstruct the estimand, treatment contrast, counterfactual, identifying variation, and identifying sample; check whether the estimator and comparison group target that estimand.
3. For causal/econometric work, audit assumptions and diagnostics:
   - timing, anticipation, treatment versions, reversals, and interference
   - selection, omitted variables, endogenous timing, measurement, and attrition
   - overlap, functional form, support, and influential observations
4. For causal/econometric work, audit inference:
   - assignment and dependence level
   - clustering or uncertainty rule
   - number of independent clusters and small-sample correction
   - multiple testing when the claim family requires it
5. For staggered adoption, reject uncorrected TWFE as the default and inspect cohort support, comparison groups, heterogeneous effects, pre-period evidence, and sensitivity to parallel-trend violations.
6. For predictive ML, audit the prediction point, label horizon, target population, unit, feature-availability boundary, and group/time-aware split; then verify:
   - preprocessing and feature selection were fit on training data only;
   - duplicates, entities, and future information do not cross split boundaries;
   - tuning stayed inside the declared training/validation budget and the final holdout remained untouched until selection was locked;
   - the model improves on prespecified naive and transparent benchmarks under the primary metric;
   - probability outputs are calibrated when relevant and any threshold or decision rule was fixed without test-set optimization;
   - error slices, uncertainty, and temporal or population shift are reported where the ML Design Packet requires them.
7. When any core variable is produced by human coding, text/image/audio processing, an LLM or another fitted model, audit it as a measurement process rather than a known truth. Classify its role in the estimand or prediction task; inspect construct and temporal validity, source reuse and mechanical dependence, gold-standard evidence, error slices, stability, and the inferential consequences of measurement error. Read [references/derived-measurement-audit.md](references/derived-measurement-audit.md) for this branch.
8. Match each robustness, falsification, or validation check to a named threat. Do not count an unrelated battery as evidence.
9. Apply the Design Packet's stop rules. If they fail, lower the claim ceiling even when estimates are significant or predictive metrics look strong. Use the in-flight severity vocabulary that `staggered-did` and `did-analysis` adopt from the `causal-did` protocol (FATAL / SERIOUS): a FATAL condition such as a clear pre-treatment trend, treatment timing correlated with outcome shocks, or a degraded comparison group must appear verbatim in the Verification Report rather than being softened into a caveat.
10. Separate what is established by evidence, what is a supported inference, and what remains assumption or judgment. Feature importance, SHAP values, or subgroup performance do not establish a causal mechanism.

## Methodology Verification

Return:

- `disposition`: `pass`, `conditional`, or `fail`
- target estimand and identifying variation
- assumption ledger with evidence and sensitivity status
- inference assessment
- for predictive ML: leakage, split integrity, untouched-holdout, benchmark, calibration, threshold, and error-slice assessments
- for derived measures: construct role, provenance sufficiency, validation and stability evidence, dependence/leakage risks, measurement-error implications, and claim ceiling
- design–estimator mismatches
- stop-rule status
- severity-ranked methodological findings
- authorized, qualified, and prohibited claims
- required redesign, re-estimation, or additional evidence

Do not prescribe more robustness tests without stating the threat each one addresses.
