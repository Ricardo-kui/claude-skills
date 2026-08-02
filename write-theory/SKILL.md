---
name: write-theory
description: |
  诊断-路由-生成式 Theory & Hypotheses 写作引擎。
  覆盖 7 种理论构建变体（构念辨析型、机制推演型、假设树型、质性过程理论型、调节效应型、竞争假设型、辩证对立型）。
  蒸馏请求（「蒸馏 theory」「theory 范文分析」「处理新论文 theory」）不直接处理——自动路由到 `distill-theory-exemplar`；验证通过的模式回写 `corpus/`。
  触发词：「写theory」「写理论」「theory template」「理论部分」「hypothesis写作」「调节效应假设」「跨层调节」「构念界定」「机制推演」「why chain」「双受众」「对立机制」。
  **反向边界**：审查/润色已有 Theory 草稿用 `theory-review`；全稿 QC 用 `pollock-qc`；蒸馏范文用 `distill-theory-exemplar`。
  **与 write-methods 的识别策略分工**：识别策略的**理论论证**（IV 排除限制的理论依据、DiD 平行趋势的理论基础、RDD 断点局部可比较性）属本 skill（Theory 段嵌入）；识别策略的**实现**（IV 第一阶段、DiD 估计量、RDD 带宽选择）属 `write-methods`。
---

# Write Theory and Hypotheses

Diagnose the theory-building problem, choose the correct architecture, and produce a paper-specific theory and hypothesis scaffold grounded in the bundled corpus.

## Intake

Collect the core constructs, theoretical lens, intended contribution, level of analysis, empirical setting, and any Introduction contribution contract. If `paper-state.yaml` exists, validate its canonical `story` first; use legacy Introduction story fields only through the migration map in the sibling `paper-story-contract` skill.

## Story gate

Full Theory generation requires a valid story contract. Theory is rising action: every construct and why-chain must deepen the central knot, every hypothesis must include a `storyline_id`, and new main characters require a contract update. Preparing-stage work is diagnosis only; refining and finishing require a confirmed contract. A local hypothesis may bypass the full gate only with an explicit local-only notice and no paper-state update.

## Workflow

1. Diagnose the build type using `references/phase-1-diagnosis.md` and `corpus/meta/routing_table.md`. 确认路由后查 `corpus/_index.md` 快速决策表（variant→文件名映射 + 该变体应配的 subprotocols/sentences）；推荐任何 pattern 前，查 `corpus/_evidence_registry.yaml` 的 EMERGING/VERIFIED/ROBUST 状态，EMERGING 须标注单/双源不得作默认。
2. Choose construct order, mechanism depth, hypothesis structure, and narrative arc using `references/phase-2-architecture.md`.
3. Derive each hypothesis through a complete why-chain using `references/phase-3-hypothesis-derivation.md`（含 8 项语料调用清单）; load only the selected variant from `corpus/variants/[variant_filename]`（filename 来自 phase-1 输出；或查 `corpus/_index.md` 变体表） and the necessary sentence-pattern files.
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
| 4 | 新构念必须完成 definition + scope conditions + lineage + adjacent differentiation + justification（必要性/独特价值）五步 | `corpus/sentences/construct_definition.md`；justification 见 AMJ Management Research Canvas（"definition, differentiation, and justification"） |
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

## 反模式速查（加载语料前先生效；完整版见 `corpus/_index.md` 反模式速查）

| 反模式 | 一句话判据 |
|--------|-----------|
| 常识谚语当机制 | 某推理步骤用谚语/folk wisdom 替代理论文献支撑 |
| Citation list 冒充理论 | 段末堆叠引用、无机制推演；多理论"整合"实为名单 |
| 双刃剑不对称 | 好处面篇幅远大于坏处面，或两条路径机制区分不清 |
| 双 DV 同一机制 | 两个 DV 由同一机制链接、第二段用 "Similarly" 开头 |
| 共享调节器同向 | 两个调节假设方向相同且只用一条路径论证 |
| E3 未建第一层 | 三向交互未先建立第一层交互 |
| 假设树碎片化 | 4+ 假设各自独立、无逻辑递进 |
| 调解/中介链缺环 | E4 有中介的调节未先建立基础中介链 |

## 期刊适配（影响 Phase 1 变体选择，非仅措辞）

| 期刊 | Theory 偏好 |
|------|------------|
| AMJ / SMJ | Hypothesis-driven、机制链显式；变体 B/E/C 为主场 |
| ASQ / OS | 接受 proposition 与过程理论；变体 D/G 友好，理论密度高于假设数量 |
| MS / MSOM | 模型邻近；变体 F（竞争假设裁决）与命名机制友好 |
| AMR | 纯理论：proposition 而非实证假设；构念辨析（A）与 scope 扩展为主 |
| JM / JOM | 机制必须落到行动者可操作的杠杆；实践相关性前置 |

## 措辞润色（QC 后、output 前默认执行）

骨架与 QC 完成后，对关键句位做一轮措辞增强。**默认执行**。按 section 分区查（不全读）：

| 句位 | 查的语料库 | 动作 |
|------|-----------|------|
| 构念定义 / why-chain / 假设句 / 让步反论 / 主导动机串联 | `corpus/sentences/` 全部（`construct_definition` / `mechanism_chain`（含 `cost_benefit_calculus` 这条 why-chain voice） / `moderation` / `hypothesis_forms` / `acknowledgment_response` / `leitmotif-section-opener` / `closure`） | 为机制链步骤、构念定义、假设句提供 2-3 个措辞变体 |
| 假设推导的 hedging 强度 | `../write-introduction/academic-writing-corpus/phrasebank/hedging-strength.md` | Theory 假设推导用**弱档** hedge（方向性非确定性：is likely to / appears to），禁用无 hedge 确定句 |
| 处理竞争机制/竞争理论的批判措辞 | `../write-introduction/academic-writing-corpus/phrasebank/critique-phrases.md`（先读同目录 `_index.md`） | 为 "prior theory fails to account for..." 类句提供变体（**必须配具体理论+局限**） |
| 角色 ordering 决策 | `corpus/subprotocols/character_ordering.md` | 多 IV/多 DV 时校验主角配角出场顺序 |
| 五病速查 | `../pollock-qc/references/prose-pathology.md` | 扫一遍五病，标 △ 处给改写建议 |

**润色纪律**：骨架优先，语料库只提供措辞变体不替代论证结构；每句位 ≤2-3 候选；specificity gate 强制具体化；hedging 强度不得突破 causal-hedging 设计家族上限。结果以 `### 措辞润色建议` 块附骨架末尾，不覆盖原文。

## Downstream interfaces（供其他 Skill 消费）
- `/write-methods`、`/write-results` — 经 paper-state.yaml 消费 `theory.constructs` / `theory.hypotheses` / `theory.mechanism_chains`（假设-变量映射、Hypothesis-Result Fulfillment Map）
- `/write-discussion`（review 侧）— 以假设列表与机制链作为 Discussion 理论贡献的对齐锚点
- `/paper-review`、`/theory-review` — 以本 skill 输出作为跨 Section 对齐与 Theory 草稿审查的基准
- `/distill-theory-exemplar` — 新论文 Theory 蒸馏后回写 `corpus/`

## Resource loading

> **与 Workflow 的关系**：本节是加载**总则**（按需加载、不预载、查 registry 状态）；上方 Workflow step 1-5 是**执行顺序**。两者一致——按 Workflow 顺序执行，每步的文件选择服从本节总则。

Read `references/intake-and-story-gate.md` when paper-state is present, missing, or legacy-shaped. Do not preload `corpus/`. Start with `corpus/meta/routing_table.md`, then load only the chosen variant, required construct or mechanism patterns, and the relevant storytelling/QC file. Before recommending a pattern as the default approach, check its EMERGING/VERIFIED/ROBUST status in `corpus/_evidence_registry.yaml`; EMERGING patterns must be flagged as single-/dual-source, not presented as defaults. Use sibling Introduction assets only for cross-section continuity checks.
