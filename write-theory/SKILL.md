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
5. Produce the scaffold, storyline-linked hypothesis statements, paragraph function map, evidence gaps, QC results, and the `paper-state.yaml` theory fields needed by Methods and Results. Structure the full reply per `references/output-format.md`.

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

## Hard constraints（协议层速查）

细则在指针所指的语料层；本节只列不可违反的协议规则，不重复语料内容（旧约束 #15 纪律）。

| # | 硬约束 | 细则位置 |
|---|--------|---------|
| 1 | 每个假设前必须有 2–3 步因果/过程推理链；禁止逻辑跳跃 | `references/phase-3-hypothesis-derivation.md` + `corpus/subprotocols/hypothesis_derivation_patterns.md` |
| 2 | 假设推导段用交织式论证结构（文献嵌入推理，非罗列） | `references/phase-3-hypothesis-derivation.md` §交织式论证链 |
| 3 | 假设句必须明确 IV/DV/方向/形状/条件，形式与测量尺度匹配；禁 "is associated with" | `corpus/sentences/hypothesis_forms.md` 决策矩阵 |
| 4 | 新构念必须完成 definition + scope conditions + lineage + adjacent differentiation 四步 | `corpus/sentences/construct_definition.md` |
| 5 | 主角（核心构念）不超过 3 个；段落内术语统一 | 审查侧：`theory-review` Step 1、`pollock-qc` prose 表 |
| 6 | 调节假设必须指定交互模式类型并排除反向交互；区分 differential prediction 与 differential validity | `corpus/variants/E_moderation.md` + `corpus/sentences/moderation.md` |
| 7 | 跨层调节必须在 P1 声明 focal unit of analysis 与 nesting structure | `corpus/variants/E_moderation.md` + `corpus/meta/routing_table.md` |
| 8 | 无独立 Closure 段——最后一个假设后即进 METHODS | `corpus/sentences/closure.md` |
| 9 | 竞争假设用非传统收敛信号（"Given these competing arguments…"），禁 "Therefore" | `corpus/variants/F_competing_hypotheses.md` |
| 10 | 辩证对立必须满足对称性 + dialectical turn 标记 + theory-based reconciliation；"反转"必须是方向反转而非强度变化（强度变化路由到 E 型） | `corpus/variants/G_dialectical_opposition.md` |
| 11 | ≥2 个 moderators 必须有理论驱动的选择理由（元框架/统一分类）；调节论证双边完整（high AND low） | `corpus/subprotocols/moderator_selection_frameworks.md` + `corpus/subprotocols/bilateral_argumentation_templates.md` |
| 12 | 连续谱 IV 需论证两端（+理论中间行为者作零效应基准） | `corpus/subprotocols/hypothesis_derivation_patterns.md` |
| 13 | 图不能替代文字理论；Literature Support 必须是 argument 总结而非 citation 罗列 | `corpus/sentences/mechanism_chain.md` |
| 14 | 输出末尾自动附加 `### paper-state.yaml 片段` 块 | `corpus/meta/paper_state_fragment.md` |

## Downstream interfaces（供其他 Skill 消费）

- `/write-methods`、`/write-results` — 经 paper-state.yaml 消费 `theory.constructs` / `theory.hypotheses` / `theory.mechanism_chains`（假设-变量映射、Hypothesis-Result Fulfillment Map）
- `/write-discussion`（review 侧）— 以假设列表与机制链作为 Discussion 理论贡献的对齐锚点
- `/paper-review`、`/theory-review` — 以本 skill 输出作为跨 Section 对齐与 Theory 草稿审查的基准
- `/distill-theory-exemplar` — 新论文 Theory 蒸馏后回写 `corpus/`

## Resource loading

Read `references/intake-and-story-gate.md` when paper-state is present, missing, or legacy-shaped. Do not preload `corpus/`. Start with `corpus/meta/routing_table.md`, then load only the chosen variant, required construct or mechanism patterns, and the relevant storytelling/QC file. Use sibling Introduction assets only for cross-section continuity checks.
