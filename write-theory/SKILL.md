---
name: write-theory
description: |
  诊断-路由-生成式 Theory & Hypotheses 写作引擎。
  覆盖 7 种理论构建变体（构念辨析型、机制推演型、假设树型、质性过程理论型、调节效应型、竞争假设型、辩证对立型）。
  蒸馏请求（「蒸馏 theory」「theory 范文分析」「处理新论文 theory」）不直接处理——自动路由到 `distill-theory-exemplar`；验证通过的模式回写 `corpus/`。
  触发词：「写theory」「写理论」「theory template」「理论部分」「hypothesis写作」「调节效应假设」「跨层调节」「构念界定」「机制推演」「why chain」「双受众」「对立机制」。
---

# Write Theory and Hypotheses

Diagnose the theory-building problem, choose the correct architecture, and produce a paper-specific theory and hypothesis scaffold grounded in the bundled corpus.

## Intake

Collect the core constructs, theoretical lens, intended contribution, level of analysis, empirical setting, and any Introduction contribution contract. If `paper-state.yaml` exists, validate its canonical `story` first; use legacy Introduction story fields only through the migration map in the sibling `paper-story-contract` skill.

## Story gate

Full Theory generation requires a valid story contract. Theory is rising action: every construct and why-chain must deepen the central knot, every hypothesis must include a `storyline_id`, and new main characters require a contract update. Preparing-stage work is diagnosis only; refining and finishing require a confirmed contract. A local hypothesis may bypass the full gate only with an explicit local-only notice and no paper-state update.

## Workflow

1. Diagnose the build type using `references/phase-1-diagnosis.md` and `corpus/meta/routing_table.md`.
2. Choose construct order, mechanism depth, hypothesis structure, and narrative arc using `references/phase-2-architecture.md`.
3. Derive each hypothesis through a complete why-chain using `references/phase-3-hypothesis-derivation.md`; load only the selected variant from `corpus/variants/` and the necessary sentence-pattern files.
4. Audit construct consistency, alternative mechanisms, hypothesis testability, paragraph architecture, and cross-section promises using `references/phase-4-qc-alignment.md`.
5. Produce the scaffold, storyline-linked hypothesis statements, paragraph function map, evidence gaps, QC results, and the `paper-state.yaml` theory fields needed by Methods and Results.

## Selection rules

- Use construct differentiation when the contribution changes what a construct means.
- Use mechanism elaboration when the contribution explains why or how an effect occurs.
- Use a hypothesis tree when several predictions share a common theoretical trunk.
- Use process theory for temporal stages or qualitative process models.
- Use moderation for boundary conditions; distinguish within-level from cross-level interactions.
- Use competing hypotheses when credible theories predict opposing outcomes.
- Use dialectical opposition when the contribution depends on sustained tension between mechanisms.

## Output contract

Return a tailored scaffold, not unsupported substantive claims. Mark every literature-dependent statement with an evidence placeholder until verified. Keep construct names stable across prose, hypotheses, methods, and results. State null, competing, or boundary predictions precisely enough to test.

## Resource loading

Read `references/intake-and-story-gate.md` when paper-state is present, missing, or legacy-shaped. Do not preload `corpus/`. Start with `corpus/meta/routing_table.md`, then load only the chosen variant, required construct or mechanism patterns, and the relevant storytelling/QC file. Use sibling Introduction assets only for cross-section continuity checks.
