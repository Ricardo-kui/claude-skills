---
name: run-empirical-research
description: "实证研究全流程总控协调器：从需求澄清、数据就绪、设计锁定到执行、核验、证据打包与写作交接，编排多个实证 skill 协同工作。用于完整实证项目流程或判断下一步该调用哪个实证 skill；单一明确的语法/估计/审查/写作任务请直接调用对应专项 skill。"
whenToUse: "当用户要跑一个完整实证项目、做因果实证全流程、从数据一路做到论文结果、或问接下来该用哪个实证 skill 时使用。触发词：实证全流程、完整实证分析、跑一遍实证 pipeline、从数据到结果、总控协调、实证项目怎么推进"
---

# Run Empirical Research

## Purpose

Act as the control plane for the installed empirical skills. Preserve decisions across stages, select one primary owner per stage, and prevent execution or prose from silently changing the research design.

Do not reproduce specialist instructions here. Route to them and require their contracted artifact before advancing.

The gates below apply only after this coordinator is activated. For one Stata option, one named estimator/runtime, one already-verified prose block, or one governed specification-search request, invoke the narrow specialist directly and do not create pipeline state.

## Operating Rules

1. Create or load one `empirical-state.yaml` using [references/state-protocol.md](references/state-protocol.md).
2. Resume from the earliest incomplete or invalidated gate. Do not restart completed stages without recording why.
3. Assign one primary skill to each stage. Secondary skills may support but may not redefine the primary output.
4. Treat Stata as the default causal execution runtime. Use R only when the user explicitly requests it. Use Python when the project is Python-native or explicitly requests Python.
5. Record every design or sample deviation. Never let an executor silently replace the estimand, comparison group, treatment timing, sample rule, or clustering rule.
6. Stop rather than optimize for significance when a gate fails.

## Pipeline

| Stage | Gate | Primary owner | Required artifact |
|---|---|---|---|
| 0. Intake | question and deliverables are defined | `empirical-intake` | Intake Packet |
| 1. Data readiness | files, unit, time, keys, missingness, and sample funnel are known | this coordinator, using `exploratory-data-analysis` and/or `stata-data-cleaning` audit-only evidence | Data Contract |
| 2. Design lock | estimand, counterfactual, assumptions, threats, diagnostics, and stop rules are explicit | `huntington-klein-causal-design` for causal work; `ml-analysis` for prediction | Design Packet |
| 3. Execution plan | runtime, estimator, baseline, diagnostics, robustness, and output paths are fixed | `causal-analysis` or `ml-analysis` | Analysis Manifest |
| 4. Execution | scripts run reproducibly and preserve the locked design | method/runtime specialist | Run Manifest + Results Inventory |
| 5a. Implementation verification | code and outputs reproduce the Analysis Manifest | `review-code` | Code Verification Report |
| 5b. Method verification | causal identification or predictive validation, diagnostics, inference/metrics, and stop rules support the claim | `check-methodology` | Method Verification Report or ML Method Verification Report |
| 5c. Verification aggregation | both reports are reconciled under the deterministic rule below | this coordinator | Aggregate Verification Report |
| 6. Evidence packaging | every authorized claim points to verified evidence and caveats | `empirical-writeup` | Evidence Packet |
| 7. Writing handoff/drafting | evidence and claim limits are accepted by the writing stack | `paper-writing-stack` or section writer | Writing Handoff + requested draft |

Read [references/skill-routing.md](references/skill-routing.md) only when choosing the Stage 4 executor or resolving overlap between skills.

## Gate Logic

- Do not estimate a causal model before Stages 0–3 are ready, except a clearly labeled reconnaissance run that cannot authorize claims.
- Do not expand into mechanisms, heterogeneity, or a robustness battery until the baseline design and diagnostics are credible.
- Do not pass results to prose when verification is missing, failed, or materially inconsistent with the locked design.
- Do not convert predictive importance, association, or specification-search output into a causal claim.
- If evidence changes a material design decision, mark downstream stages `superseded`, revise the Design Packet, and rerun affected stages.
- Aggregate code and methodology verification as `fail` if either fails, `conditional` if either is conditional, and `pass` only if both pass. Missing core logs or Run Manifest caps the aggregate at `conditional`.

For operational ML, Stage 6 and Stage 7 are conditional. If the requested endpoint is a verified model, scoring artifact, or deployment handoff rather than a manuscript, finish with an ML Delivery Handoff and do not force a writing stage.

## Trigger Boundary

Use this coordinator for `全流程`, `end-to-end`, `从数据到结果`, a multi-stage continuation, an unclear next empirical stage, or a request that spans multiple specialist skills.

Do not use it for:

- one Stata syntax or option -> `stata`
- one named estimator in an explicit runtime -> its method/runtime specialist
- already-verified outputs that only need prose -> `empirical-writeup`
- one specification-search request -> `xianzhu-skill`, subject to its design-lock and anti-p-hacking boundary

## Minimal Interaction Pattern

At each turn:

1. State the current stage and gate status.
2. Inspect existing artifacts before asking questions.
   - If no project/data path is supplied and the current directory is a broad home or workspace root, ask for the project directory or primary data/code path; do not recursively search the entire root.
3. Ask only for unresolved information that changes routing or validity.
4. Invoke the primary skill for that stage.
5. Validate its artifact against the state protocol.
6. Update state and name the next stage.

## Completion Standard

The pipeline is complete only when:

- the empirical state links the final data, scripts, logs, and every artifact applicable to the requested endpoint (tables/figures for papers; model/preprocessing/scoring/monitoring artifacts for operational ML);
- the Verification Report identifies no unresolved fatal issue;
- the Evidence Packet distinguishes authorized, qualified, and prohibited claims;
- the Writing Handoff includes residual uncertainty and does not overstate identification, and every requested section draft has been delivered; or an operational ML project has a verified ML Delivery Handoff.
