---
name: huntington-klein-causal-design
description: "Identification-first causal-design and claim audit based on Huntington-Klein The Effect. Use when defining or auditing causal questions, estimands, identifying variation, controls, assumptions, or DiD/IV/RDD/matching choices."
when_to_use: "任何因果问题定义、识别假设审计、方法选型比较时使用；要执行时产出 design handoff 给 causal-analysis/Stata。"
whenToUse: "Use when defining, choosing, or auditing a causal identification strategy, estimand, DAG, control set, or causal claim before any estimation runs. Trigger words: identification, causal design, estimand, DAG, DiD design, IV, RDD, matching, 识别策略, 因果识别, 因果设计, 审计因果主张"
---

# The Effect: Causal Research Design

**Source**: Nick Huntington-Klein, *The Effect: An Introduction to Research Design and Causality*, 2nd ed. (2025) | **Coverage**: orientation plus Chapters 1–23 | **Protocol**: v1.2

## Route the Request

Classify the task, select one output mode, and load only the branch it needs.

- **Form or refine a causal question**: Read Ch1–2 and Ch10 from [chapter-index.md](chapter-index.md). Add Ch5 only when the user requests a design or identification strategy.
- **Draw or audit a DAG/control set**: Read Ch5–8. Add Ch23 when selection, measurement, missingness, treatment versions, or spillovers matter.
- **Choose or compare designs**: Read [cheatsheet.md](cheatsheet.md), Ch9–12, and the 2–3 closest method chapters. Compare assumptions and estimands, not shared data structures.
- **Develop an empirical design**: Read the selected method chapter, Ch11, Ch23, and the corresponding output contract in [patterns.md](patterns.md).
- **Audit a causal claim**: Read the claimed method chapter and use the Causal Claim Audit in [patterns.md](patterns.md). Add Ch23 when the data process or treatment definition is material.
- **Run or write code**: Complete the Design Packet and Execution Handoff in [patterns.md](patterns.md), then invoke the installed causal-analysis or Stata skill. Let the execution skill verify current syntax and defaults.
- **Explain a named method or chapter**: Open it directly through [chapter-index.md](chapter-index.md). Read connected chapters only when comparison or implementation is requested.
- **Define a term**: Read [glossary.md](glossary.md), then open the cited chapter if the definition affects a claim.
- **Make a publication-facing methods claim**: Apply the Frontier Check below and verify the current primary methods literature.
- **Trace guidance to the book**: Read [source-map.md](source-map.md) only for provenance, quotation checking, or source-boundary audits.

## Select the Output Mode

Use one mode unless the user explicitly asks for several. Explain mode uses the inline contract below; Audit, Design, and Handoff use [patterns.md](patterns.md).

- **Explain**: Return the concept, identifying comparison, estimand, assumptions, one diagnostic, and limit. Complete the mode when all six are present without inventing a project-specific design choice.
- **Audit**: Work backward from claim to estimate, estimand, variation, assumptions, diagnostics, threats, and smallest supported verdict.
- **Design**: Produce a complete Design Packet and satisfy the Identification Gate.
- **Handoff**: Produce the machine-readable Execution Handoff after Design mode is ready. Mark it `blocked` when execution would require guessing a design choice.

## Protocol Vocabulary

- **Design Packet**: the complete Design-mode output.
- **Variation Map**: every known source of treatment variation, with the identifying source and observations marked.
- **Assumption Ledger**: each identifying assumption linked to evidence, falsification implications, sensitivity analysis, or an untestable label.
- **Stop Rule**: an observable condition that blocks or narrows causal interpretation.
- **Epistemic Split**: design facts, supported inferences, required assumptions, project judgments, and unknowns reported separately.

## Identification-First Workflow

1. Classify the claim as descriptive, predictive, or causal.
2. Define the treatment contrast, outcome, unit, population, setting, time horizon, and estimand.
3. Reconstruct the DGP, including assignment, selection, measurement, and timing.
4. Locate the answer-bearing variation and the units/times supplying it.
5. State the identifying assumptions and plausible rival DGPs.
6. Select a design, estimator, and inference procedure that preserve that comparison.
7. Derive diagnostics and falsification tests from specific assumptions.
8. Audit transport, missingness, treatment versions, interference, and model uncertainty.
9. Return the Epistemic Split and apply every relevant Stop Rule.

## Identification Gate

Complete Design mode only when the Design Packet contains all nine items:

1. A precise causal question and estimand.
2. Treatment, outcome, unit, population, setting, and temporal order.
3. A DGP/DAG or explicit causal narrative.
4. The source of identifying variation and identifying observations.
5. Assumptions linking that variation to the estimand.
6. The closest rival design or explanation and why it is non-interchangeable.
7. An estimator and inference plan aligned with assignment and dependence.
8. Diagnostics, falsification evidence, and an assumption-relaxation analysis.
9. The Epistemic Split.

Use the inline completion criterion for Explain and the mode-specific Completion Rules in [patterns.md](patterns.md) for Audit and Handoff.

## Hard Method Guards

- Treat regression and fixed effects as estimators/design components, not automatic identification.
- For staggered adoption, use cohort-aware modern DiD; do not default to an uncorrected TWFE treatment coefficient or conventional TWFE event study.
- Treat pre-trend, balance, overidentification, density, and placebo tests as potential falsification evidence, not proof of validity.
- Keep post-treatment variables, mediators, colliders, and baseline confounders distinct.
- Report local or weighted effects as local or weighted; do not silently relabel LATE, ATT, or cutoff effects as ATE.
- Let uncertainty about identification, measurement, and model choice remain visible alongside sampling uncertainty.

## Frontier Check

The book is a structured conceptual base, not permanent method authority. Before publication or live execution:

1. verify the current design-specific primary literature and major reviews;
2. verify current software syntax, defaults, and estimand;
3. check post-2025 developments when the method is active or fast-moving;
4. reconcile any conflict with the project's governing method protocol;
5. label book-derived code and research prompts as instructional until verified.

## Reference Map

- [cheatsheet.md](cheatsheet.md) — method selection, diagnostics, inference, and stop rules
- [patterns.md](patterns.md) — reusable design, comparison, audit, simulation, and reporting contracts
- [chapter-index.md](chapter-index.md) — complete chapter and topic index
- [glossary.md](glossary.md) — causal-design and econometric terms
- [source-map.md](source-map.md) — book provenance and operational/frontier boundaries; load only for source audits
- [chapters/](chapters/) — 25 on-demand chapter syntheses

## Scope

Use this skill to reason from Huntington-Klein's identification-first framework and produce a decision-ready design protocol. Use project evidence and specialized execution skills for data-specific estimation, current software, and frontier claims.
