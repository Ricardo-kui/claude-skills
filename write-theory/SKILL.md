---
name: write-theory
description: >-
  Theory & Hypotheses 写作引擎——诊断理论构建问题、选架构、生成可落地假设骨架（7 变体：构念辨析/机制推演/假设树/过程理论/调节效应/竞争假设/辩证对立）。Use when writing theory or hypotheses for a management-journal paper。Not for: 蒸馏范文（→ distill-theory-exemplar）；审查草稿（→ theory-review）；全稿 QC（→ pollock-qc）。分工：识别策略的理论论证属本 skill（Theory 段嵌入），实现属 write-methods。
---

# Write Theory and Hypotheses

Diagnose the theory-building problem, choose the correct architecture, and produce a paper-specific theory and hypothesis scaffold grounded in the bundled corpus.

## Intake

Collect the core constructs, theoretical lens, intended contribution, level of analysis, empirical setting, and any Introduction contribution contract. If `paper-state.yaml` exists, validate its canonical `story` first; use legacy Introduction story fields only through the migration map in the sibling `paper-story-contract` skill.

## Story gate

Full Theory generation requires a valid story contract. Theory is rising action: every construct and why-chain must deepen the central knot, every hypothesis must include a `storyline_id`, and new main characters require a contract update. Preparing-stage work is diagnosis only; refining and finishing require a confirmed contract. A local hypothesis may bypass the full gate only with an explicit local-only notice and no paper-state update.

**knot 架构检查（非门禁，frame_type 存在时执行）**：若 `story.story_frame.frame_type` 已选定（经 Introduction 输出的 `story.story_frame` 或契约），生成假设前读 `corpus/storytelling/knot-architecture-modulation.md` 对应节的**签名假设架构**——对照目标架构（双边对置 / 竞争假设 / 复现-消解 / 双轨并行 / 挑战先行 / 2×2 对称等）与 knot 签名是否一致；不一致时输出架构偏差标注与理由（或建议回契约调整 frame_type）。frame_type 缺失时跳过本检查，走默认路径。

## Workflow

1. 诊断构建类型：读 `references/phase-1-diagnosis.md` + `corpus/meta/routing_table.md`。主 Gap = Incommensurability 时先读 `references/incommensurability-resolution-routes.md`（L0 稳定推理内核 + R1–R4），再把 A–G 视为候选架构；route 不规定假设数量、编号、变量数量或模型形式，低置信时保留 L0 并报告两个候选路线。冲突定位由理论对象与预测分歧裁定；Makadok 维度只校验贡献方向。路由后查 `corpus/_index.md` 快速决策表（variant→文件名映射 + 应配 subprotocols/sentences）；推荐任何 pattern 前，查 `corpus/_evidence_registry.yaml` 的 EMERGING/VERIFIED/ROBUST 状态——EMERGING 须标注单/双源，不作默认。
   **完成判据**：变体已选；EMERGING 已标注。
2. 用 `references/phase-2-architecture.md` 定构念顺序、机制深度、假设结构与叙事弧。
   **完成判据**：构念顺序 + 机制深度已定。
3. 先执行 conditionality gate（稳定无条件效应是否有理论依据？）；再按 `references/phase-3-hypothesis-derivation.md`（含 8 项语料调用清单）通过完整 why-chain 推导每个假设；只 load 所选变体 `corpus/variants/[variant_filename]` 与必要的 sentence-pattern 文件。
   **完成判据**：每个假设有完整 why-chain + storyline_id；硬约束 #1–#16 逐条过。
4. 用 `references/phase-4-qc-alignment.md` 审计构念一致性、替代机制、假设可检验性、段落架构与跨节承诺。
   **完成判据**：四维审计无未修复项。
5. 产出骨架 + storyline 链接假设 + 段落功能图 + 证据缺口 + QC 结果 + `paper-state.yaml` theory 字段；格式按 `references/output-format.md`。
   **完成判据**：输出合同全项（含 paper-state 片段、机制与条件性审计）。

## Selection rules

- Use construct differentiation when the contribution changes what a construct means.
- Use mechanism elaboration when the contribution explains why or how an effect occurs. Route to B0 when the process is theoretical explanation only; route to B1 only when a mediator is a defined construct and the design can test the indirect effect.
- Use a hypothesis tree when several predictions share a common theoretical trunk.
- Use process theory for temporal stages or qualitative process models.
- Before selecting a main-effect structure, ask whether the mechanism is expected to operate stably across the stated scope. If not, make the conditional relationship primary; do not invent a moderator merely to make the model look richer.
- Use moderation only when a theoretically specified boundary changes a mechanism, exposure, capacity, or interpretation; distinguish within-level from cross-level interactions.
- Use competing hypotheses when credible theories predict opposing outcomes.
- Use dialectical opposition when the contribution depends on sustained tension between mechanisms.
- For Incommensurability, locate the conflict before choosing an architecture (differentiate X R1 / disaggregate Y R2 / opposing mechanisms R3 / contextual contingency R4); paired hypotheses, mediation, competing hypotheses, moderation, thresholds, and U/倒U are L2 candidates requiring a necessity warrant. Opposing mechanisms do not by themselves justify a U/倒U; same-sign moderation normally does not justify an Incommensurability label.

## Output contract

Return a tailored scaffold, not unsupported substantive claims. Mark every literature-dependent statement with an evidence placeholder until verified. Keep construct names stable across prose, hypotheses, methods, and results. State null, competing, or boundary predictions precisely enough to test. Include a mechanism-and-conditionality audit that distinguishes reasoning depth from mediator/moderator count. For Incommensurability, also report L0–L3, route confidence, closest alternative, unclassified residual, and why the selected hypothesis architecture is necessary.

## Hard constraints（协议层速查）

细则在指针所指的语料层；本节只列不可违反的协议规则，不重复语料内容。

| # | 硬约束 | 细则位置 |
|---|--------|---------|
| 1 | 每个假设前必须有足以连接前提与预测的因果/过程推理链；通常至少 2 个有内容的推理环节。环节数按推理移动计算，不按中介/调节变量数量计算；为凑步数机械添加的变量不计入环节 | `references/phase-3-hypothesis-derivation.md` + `corpus/subprotocols/hypothesis_derivation_patterns.md` |
| 2 | 假设推导段用交织式论证结构（文献嵌入推理，非罗列） | `references/phase-3-hypothesis-derivation.md` §交织式论证链 |
| 3 | 假设句必须明确 IV/DV/方向/形状/条件，形式与测量尺度匹配；禁 "is associated with" | `corpus/sentences/hypothesis_forms.md` 决策矩阵 |
| 4 | 新构念必须完成 definition + scope conditions + lineage + adjacent differentiation + justification（必要性/独特价值）五步 | `corpus/sentences/construct_definition.md`；justification 见 AMJ Management Research Canvas |
| 5 | 主角（核心构念）不超过 3 个；段落内术语统一 | 审查侧：`theory-review` Step 1、`pollock-qc` prose 表 |
| 6 | 调节假设必须指定交互模式类型并排除反向交互；区分 differential prediction 与 differential validity | `corpus/variants/E_moderation.md` + `corpus/sentences/moderation.md` |
| 7 | 跨层调节必须在 P1 声明 focal unit of analysis 与 nesting structure | `corpus/variants/E_moderation.md` + `corpus/meta/routing_table.md` |
| 8 | 默认不设独立 Closure；最后假设/命题自然收敛。仅当复杂构念或过程模型仍需整合时，允许在末段嵌入或紧随其后作最短必要回扣，不得增加新构念、命题或贡献 | `corpus/sentences/closure.md` |
| 9 | 竞争假设用非传统收敛信号（"Given these competing arguments…"），禁 "Therefore" | `corpus/variants/F_competing_hypotheses.md` |
| 10 | 辩证对立必须满足对称性 + dialectical turn 标记 + theory-based reconciliation；"反转"必须是方向反转而非强度变化（强度变化路由到 E 型） | `corpus/variants/G_dialectical_opposition.md` |
| 11 | ≥2 个 moderators 必须有理论驱动的选择理由（元框架/统一分类）；调节论证双边完整（high AND low） | `corpus/subprotocols/moderator_selection_frameworks.md` + `corpus/subprotocols/bilateral_argumentation_templates.md` |
| 12 | 连续谱 IV 需论证两端（+理论中间行为者作零效应基准） | `corpus/subprotocols/hypothesis_derivation_patterns.md` |
| 13 | 图作为文字理论的辅助呈现（文字承载论证）；Literature Support 必须是 argument 总结而非 citation 罗列 | `corpus/sentences/mechanism_chain.md` |
| 14 | 输出末尾自动附加 `### paper-state.yaml 片段` 块 | `corpus/meta/paper_state_fragment.md` |
| 15 | 主效应推导前必须执行 conditionality gate；若机制只在特定条件下成立，条件关系优先，主效应仅可作为有依据的基线 | `references/phase-3-hypothesis-derivation.md` + `corpus/storytelling/post-generation-validator.md` |
| 16 | Incommensurability 使用两阶段可比性门控：对话层只要求共享理论对象或可辩护的高阶 X/Y 家族；R3/R4 在正式假设推理前必须锁定具体 X、Y、层级、时间范围与 estimand。继续标记 L0–L3 与 R1–R4；A–G、H 数量及模型形式均为候选而非自动输出。R3 只有在机制相对强度随 X 系统变化时才推出 U/倒U，R4 必须双边推导并直接检验条件差异 | `references/incommensurability-resolution-routes.md` |

## 反模式速查（加载语料前先生效；完整版见 `corpus/_index.md`）

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

## 期刊适配

用户提及目标期刊时读 `references/journal-fit.md`（影响 Phase 1 变体选择，非仅措辞——AMJ/SMJ 变体 B/E/C 主场、ASQ/OS D/G 友好、AMR 纯理论等）。

## 措辞润色（QC 后、output 前默认执行）

骨架与 QC 完成后，对关键句位做一轮措辞增强。**默认执行**。按 section 分区查（不全读）：

| 句位 | 查的语料库 | 动作 |
|------|-----------|------|
| 构念定义 / why-chain / 假设句 / 让步反论 / 主导动机串联 | 按句位选择 `corpus/sentences/` 中一个匹配文件（`construct_definition` / `mechanism_chain` / `moderation` / `hypothesis_forms` / `acknowledgment_response` / `leitmotif-section-opener` / `closure`） | 为关键句位提供 2–3 个措辞变体；不预载整个目录 |
| 假设推导的 hedging 强度 | `../write-introduction/academic-writing-corpus/phrasebank/hedging-strength.md` | 对尚待检验的方向和机制使用与证据匹配的弱档 hedge；构念定义、已确立前提和逻辑关系可用明确陈述，不机械给每句加 hedge |
| 处理竞争机制/竞争理论的批判措辞 | `../write-introduction/academic-writing-corpus/phrasebank/critique-phrases.md`（先读同目录 `_index.md`） | 为 "prior theory fails to account for..." 类句提供变体（**必须配具体理论+局限**） |
| 角色 ordering 决策 | `corpus/subprotocols/character_ordering.md` | 多 IV/多 DV 时校验主角配角出场顺序 |
| 五病速查 | `../pollock-qc/references/prose-pathology.md` | 扫一遍五病，标 △ 处给改写建议 |

**润色纪律**：骨架优先，语料库只提供措辞变体不替代论证结构；每句位 ≤2-3 候选；specificity gate 强制具体化；hedging 强度不得突破 causal-hedging 设计家族上限。结果以 `### 措辞润色建议` 块附骨架末尾，不覆盖原文。

## Downstream interfaces（供其他 Skill 消费）

- `/write-methods`、`/write-results` — 经 paper-state.yaml 消费 `theory.constructs` / `theory.hypotheses` / `theory.mechanism_chains`（假设-变量映射、Hypothesis-Result Fulfillment Map）
- `/write-discussion`（review 侧）— 以假设列表与机制链作为 Discussion 理论贡献的对齐锚点
- `/paper-review`、`/theory-review` — 以本 skill 输出作为跨 Section 对齐与 Theory 草稿审查的基准
- `/distill-theory-exemplar` — 新论文 Theory 蒸馏后回写 `corpus/`

## 原文锚点使用纪律（verbatim anchor）

语料变体/句式模板的 `**原文锚点**` 字段是来源论文原句的风格参照（由 distill-theory-exemplar 提取）。生成段落时：**结构跟骨架、语言风味跟锚点**——填入 [placeholder] 后保持锚点的句式节奏与措辞质感；不逐字复制锚点内容，不保留其专有名词/数字。无锚点的旧变体（标注"待补"）按骨架直接生成。选材时参照"选材 Gate"（distill-theory-exemplar）的 routing 表 + 验证状态三带判定。

## 批评登记（critique-driven stats）

**当用户对本 skill 产出表示不满时，当场把批评登记到 `corpus/_evidence_registry.yaml` 的 `critique.per_file` 段**——这是语料精炼的反馈信号，无需询问用户。

- 定位：本次调用涉及的 corpus 文件（如 `corpus/variants/E_moderation.md`、`corpus/sentences/mechanism_chain.md`）
- 登记：`revise` +1（需大改）或 `reject` +1（弃用/换写法）、`last_critique`=今天、批评要点去重插入 `reasons` 首位（最多 8 条）
- 不登记满意信号；同一会话中同一缺陷只登记一次
- 只登记对**变体产出质量**的批评，不登记对 [placeholder] 填充流程的抱怨、风格偏好或与语料无关的意见
- 批评只落 registry，不自动修改 corpus 文件——由后续蒸馏（distill-theory-exemplar 选材 Gate）驱动精炼

## Evidence-driven evolution

范文蒸馏对本 skill 的影响分两条通道：reference-level 模式更新 `corpus/` 与 `_evidence_registry.yaml`；规则层反例/缺陷更新 `corpus/_skill_design_feedback.yaml`。执行演化任务时读取 `../distill-theory-exemplar/references/design-feedback-loop.md`：单篇模式不得直接建立普遍规则；只有 VERIFIED/ROBUST 或针对绝对规则的 full-text FALSIFIER，且通过授权、风险、positive regression 与 preservation regression 门控后，才可 conditionalize、decouple、add branch 或修正 validator。`resolved` 还必须核验目标文件中的 `rule_excerpt_after`；schema/stage-gate/high-risk 变更始终人工审核。

## Resource loading

> **与 Workflow 的关系**：本节是加载**总则**（按需加载、不预载、查 registry 状态）；上方 Workflow step 1-5 是**执行顺序**。两者一致——按 Workflow 顺序执行，每步的文件选择服从本节总则。

Read `references/intake-and-story-gate.md` when paper-state is present, missing, or legacy-shaped. Do not preload `corpus/`. Start with `corpus/meta/routing_table.md`; when the primary gap is Incommensurability, also load `references/incommensurability-resolution-routes.md`. Then load only the chosen variant, required construct or mechanism patterns, and the relevant storytelling/QC file. Before recommending a pattern as the default approach, check its EMERGING/VERIFIED/ROBUST status in `corpus/_evidence_registry.yaml`; EMERGING patterns must be flagged as single-/dual-source, not presented as defaults. Use sibling Introduction assets only for cross-section continuity checks.
