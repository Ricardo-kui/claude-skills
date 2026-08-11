# Boundaries — 诚实边界与输出约束（从 SKILL.md 下沉，v0.1）

> 由 write-results 在涉及能力边界 / 设计排他性 / 披露纪律时**读取**。本 skill 的骨架与变体提炼自 MVP30 范文语料库（截至 2025 年，持续蒸馏扩充中；各变体的来源论文在 `econometric-models/INDEX.md` 按日期登记）。

## 诚实边界

1. **不能替代统计诊断**：提供段落骨架和 ritual 规范，但不能判断您的数据是否满足模型假设（平行趋势、过度识别、common support、VIF 等）。这些必须基于实际数据。
2. **不能消除期刊差异**：SMJ/AMJ/ASQ/JM/OS/JOM/ASR 对 Results 的 ritual 偏好不同（如 ASQ 更重视 construct validity 叙事，SMJ 更重视 identification）。本 skill 以"最大公约数"为主，投稿前需对照目标期刊最新范文调整。
3. **不能生成真实统计量**：所有 [placeholder] 中的系数、p 值、置信区间、边际效应必须由用户根据实际估计结果填入。本 skill 不虚构任何数字。
4. **语料库领域偏差**：范文主要来自战略管理、营销、组织行为。金融、会计、运筹等领域的 ritual 可能不同。
5. **不能覆盖最新方法论**：语料库截止于 2025 年，更新的估计量、识别策略或报告规范可能未覆盖。
6. **设计排他性不可违反**：不得为非 DiD 设计使用平行趋势语言；不得为非 IV 设计要求第一阶段/排他性约束检验；不得为非匹配设计要求重叠支撑检验。
7. **不得隐藏非显著假设**：非显著的**假设检验**必须在 Results 中报告（inline 或独立段均可），不得因不显著而跳过。非显著的**假设验证、判别效度或安慰剂检验**可放在 Supplemental Analyses（R8）。
8. **不得把稳健性检验包装成因果识别**：robustness check（安慰剂、模型替换、样本限制）只能回应对应的 validity threat，不能将其称为 "causal identification" 除非该检验实际解决了识别问题（如 IV 的排他性、DiD 的平行趋势）。
9. **不得在非线性模型中直接比较系数大小**：Logit/Probit/计数模型/生存分析必须报告边际效应、预测概率、风险比或事件时间变化，不能直接比较 raw coefficient 的大小。
10. **交互显著后主效应不可独立解释**：当交互项显著时，**强烈建议**在同一段落或紧随其后的段落中明确警告 "main effects cannot be interpreted independently"，并报告 conditional effects。若主效应本身已不显著或期刊惯例侧重条件效应图，可酌情省略。
11. **不得在稳健性检验中只报告一致的子集**：当某个稳健性维度下存在多个检验且部分 confirm、部分 disconfirm 时，必须在正文和汇总表中同时报告所有检验结果，不得选择性披露。Divergent findings 应框定为边界条件或测量敏感性，而非错误（Yuan et al. 2026 JOM, Section D）。
12. **不得将预处理选择隐藏为"标准做法"**：缺失数据处理方法（listwise deletion / multiple imputation / FIML）、离群值阈值（1st/99th vs. 5th/95th percentile）、变量转换（log / sqrt / untransformed）必须在 Methods 或 R7 中明确报告，不能仅以 "we followed standard practices" 概括（Yuan et al. 2026 JOM, REC B3.4）。

## 输出约束

- 必须提醒用户：替换所有 `[方括号占位符]` 为实际内容；不虚构 p 值、系数、支持状态或稳健性发现。
- 不要跳过不显著的假设——必须报告并解释。
- 经济显著性必须与统计显著性一起报告（已在 R3 扩展版中内置）。
- **四拍完整性强制要求**：每个显著假设的 R3 段落必须包含 Beat-3（幅度解释），使用具体数值基准（one-SD / one-unit / IQR / 概率变化 / 百分比），禁止仅写 "This indicates that [substantive interpretation]." 等模糊表述。
- 交互效应必须提供简单斜率或边际效应图（R4 模板已内置）。
- 稳健性检验必须按威胁组织，不能简单罗列（R7 已按 6 类威胁分设段落）。
- 事后分析必须与稳健性检验分开，并明确标记为探索性。
- 如果用户有具体的假设和模型，必须将其嵌入模板。
- 每个表格/模型引用应指向用户的实际表格。
- **表图设计纪律**：R2/R4/R7 涉及表格与图形设计时，遵循 `references/visual-evidence.md`（形式匹配效果 / 标题描述数据非主题 / 伦理四规则）；证据报告质量自检见 `references/evidence-standards.md`（五问审计）。
- **输出末尾追加 paper-state.yaml 片段**（schema 见 `references/paper-state-schema.md`）：包含 `results.estimator_family`、`results.hypothesis_results`、`results.story_resolution`、`results.key_findings`、`results.unexpected_findings`，供 paper-review 和 results-review 消费。
