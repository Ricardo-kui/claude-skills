# Boundaries — 诚实边界与约束（从 SKILL.md 下沉，v0.1）

> 由 write-methods 在涉及能力边界 / 设计排他性 / 因果语言合规时**读取**。本 skill 的骨架与变体提炼自 MVP30 范文语料库（截至 2025 年，持续蒸馏扩充中；各变体的来源论文在 `corpus/INDEX.md` 按日期登记）。

## 诚实边界

1. **不能替代统计诊断**：提供段落骨架和 ritual 规范，但不能判断您的数据是否满足模型假设（平行趋势、工具变量相关性、共同支撑域、VIF、序列相关等）。这些必须基于实际数据。
2. **不能消除期刊差异**：SMJ/AMJ/ASQ/JM/OS/JOM/ASR 对 Methods 的 ritual 偏好不同。本 skill 以"最大公约数"为主，投稿前需对照目标期刊最新范文调整。
3. **不能生成真实统计量**：所有 [placeholder] 中的系数、p 值、F 统计量、样本量、VIF 值必须由用户根据实际估计结果填入。本 skill 不虚构任何数字。
4. **语料库领域偏差**：范文主要来自战略管理、营销、组织行为。金融、会计、运筹、宏观等领域的 ritual 可能不同。
5. **不能覆盖最新方法论**：语料库截止于 2025 年，更新的估计量或识别策略可能未覆盖。
6. **设计排他性不可违反**：不能为不需要某诊断的设计强制插入该诊断。例如：非 IV 设计不得要求排他性约束检验；非 DiD 设计不得要求平行趋势检验；非匹配设计不得要求重叠支撑检验。
7. **动态面板必须提示 Nickell bias**：当面板时间维度较短（T < 10）且因变量具有持续性时，不能推荐固定效应而不提示 Nickell bias 或提供系统 GMM / 差分 GMM 替代方案。
8. **不得泛化特殊设计的 causal 语言**：OLS/FE 的骨架必须使用 "associated with"；自然实验在平行趋势/事件研究支持后才可使用 "effect of... on..."；实验设计可使用 "caused"。不得让面板数据 design 的段落中出现 "leads to" 或 "causes"。（因果语言强制词汇表见 SKILL.md 渲染节）

## 输出约束

- 必须提醒用户：替换所有 `[方括号占位符]` 为实际内容；不虚构样本量、来源、变量定义或诊断结果。
- 变量名必须与 Results 表格完全一致。
- 每个控制变量必须有明确的控制逻辑（已在段落骨架中内置 "because [rival explanation]" 槽位）。
- 样本漏斗必须包含每一步的数字和理由（已在 M2 骨架中内置）。
- 不报告支持状态在 Methods 中。
- 不要把模型选择埋在方程里而没有文字解释。
- **输出末尾追加 paper-state.yaml 片段**（schema 见 `references/paper-state-schema.md`）：包含 `methods.design_type`、`methods.estimator_family`、`methods.sample`、`methods.variables`、`methods.hypothesis_variable_map`、`methods.results_preview`，供下游 write-results Phase 0 自动消费。
