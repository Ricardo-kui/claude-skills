---
name: distill-results-exemplar
description: "蒸馏顶刊论文 Results 范文——估计器分类、R1–R9 槽位映射、假设-结果节奏与表达骨架（提炼 HOW they stage evidence），验证通过的变体写回 write-results 语料。当用户要求学习/蒸馏某篇论文结果部分的写法时使用。"
whenToUse: "当用户要求蒸馏、提炼、学习某篇（或批量）论文 Results 部分的证据展演方式时使用。触发词：蒸馏 results、提炼结果部分、学习这篇结果写法、分析 results 怎么写的、results 范文蒸馏、批量蒸馏结果部分"
---

# Distill Results Exemplar

Distill how a published Results section stages evidence—not what it found—into reusable, evidence-traceable writing assets for `write-results/econometric-models/`。

三层递进：学习顶刊证据展演手法（Phase 0–2）→ 量化与跨论文对比（Phase 3–4）→ 沉淀到 corpus（Phase 4–5）。核心原则：How > What；节奏 > 数字（"方向→显著性→幅度→支持判断"四拍 + 稳健性按 threat 组织）；范式排他性（只提取该类估计器特别需要的报告方式）。

## Phase 0.5 — Story-Fidelity Gate

加载 `../paper-story-contract/references/distillation-gate.md` 并输出 `story_fidelity`。Results 的 headline answer 分类为 `climax`；稳健性、异质性和补充分析说明它们如何 `unravel` 该答案并形成 `falling_action`。只报表格顺序而不改善答案揭示或可信度的模式标记为 `ritual_only`；隐藏 mixed/null evidence 或用模板替代判断的模式标记为 `reject`。

**完成判据**：story_fidelity 已输出；climax/falling_action 判定完成。

## 调用方式

```
/distill-results-exemplar <输入路径或文本> [--batch] [--estimator-filter=OLS/FE/DiD/Logit/...] [--output-format=markdown/json]
```

- `<输入路径或文本>`（必填）：论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录；省略时进入交互式询问。
- `--batch`：批量处理模式，输出跨论文模式聚合报告；`--estimator-filter`：只处理特定估计器类型；`--output-format`：默认 markdown，可选 json 供脚本消费。
- **消歧**：用户只说"分析/蒸馏这篇论文"未指定 section 时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。`write-results` 检测到蒸馏请求时路由到本 skill。

## Phase 0 — 估计器类型与 Results 结构分类

读 `references/intake-and-classification.md`（八维分类表 + 输出 yaml），在读取正文前判定证据架构。

**完成判据**：`phase_0_results_profile` 各维齐全。

## Phase 0.75 — 选材 Gate（批评驱动）

用 `write-results/econometric-models/_evidence_registry.yaml` 的 `usage_stats` 判定本文值不值得深蒸馏：

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap** | 该估计器 slots 覆盖存在缺口（静态） | **HIGH**：ADD 候选，优先深读 |
| **critique_heavy** | `revise + reject >= 2` | **HIGH**：REPLACE/EXTEND 候选；`common_revise_reasons` 是精炼依据 |
| **quiet** | 其余 | MEDIUM：正常蒸馏 |

单篇不拒绝但必须输出带判定；批量按带排序。频繁使用且好用的变体提升路由权重，语料不因使用频率淘汰（registry `non_signals`）。

输出 yaml、执行规则、重复闸门（jaccard ≥ 0.33 → SKIP）与趋同批评聚合检查：读 `references/selection-gate.md`。

**完成判据**：band + priority + rationale 已输出；趋同批评 ≥2 时已追加聚合检查块。

## Phase 1 — 文本读取与槽位映射（R1–R9）

读 `references/phase-1-module-map.md`（槽位映射表 + 特殊分支顺序记录 + 输出 yaml），只定位段落功能，不做深入分析。

**完成判据**：每个槽位有 quality + learn_worth 标记；actual_sequence 与 deviation 已记录。

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

读 `references/phase-1-5-coverage.md`（16 类估计器强制槽位表 + 质量摘要 yaml）。

**完成判据**：coverage_verdict + skill_implication 已输出。

## Phase 2 — 深度提炼（节奏 / 骨架 / Validity Logic）

读 `references/phase-2-extraction.md`（R3 四拍与 R7 threat 节奏模板 + 骨架格式 + skill_gap 标准）。锚点规则见文末「原文锚定提取规则」。

**完成判据**：每个骨架有节奏标记 + skill_gap 标注 + 目标文件/槽位 + verbatim_anchor。

## Phase 3 — Results DNA 量化与结构化报告

读 `references/phase-3-dna-report.md`（五维诊断 + fine_grained profile 模板 + 反模式排查表）。每个诊断维度附带 skill 对比：`[定性判断] → 与 write-results 当前模板的关系 → [skill 改进方向]`。

**完成判据**：五维诊断齐全；反模式表逐条排查过；fine_grained profile 已生成。

## Phase 4 — 技能更新指令生成

读 `references/phase-4-validation-writeback.md`（指令格式 + 待写入预览块模板 + 批评登记）。**所有待写入内容先展示预览、用户确认后才写入**——单篇逐个确认，批量一次确认 ADD/EXTEND、REPLACE 仍逐个确认。

**完成判据**：每条 ADD/EXTEND/REPLACE 有 target_file + insert_after + distinct_from；预览块含骨架全文与原始句锚点。

## Phase 5 — 质量验证与版本影响

读 `references/phase-5-qc.md`（QC Checklist 11 项 + skill_version_impact 格式 + 最终输出物清单 8 项）。

**完成判据**：QC 11 项全过；每个 ADD/EXTEND/REPLACE 附带版本影响评估。

## 原文锚定提取规则（语料锚点层）

每个待写入变体必须附带 `verbatim_anchor`——来源论文 1–2 句 verbatim 原句（15–40 tokens），风格参照用：

- **选句标准**：最能代表该变体节奏/措辞手法的句子（如 R3 幅度翻译句、R7 threat 定位句）
- **拼接硬规则**：多句锚点保留省略号标记；跨段落/跨研究小节拼接必须显式标注（Study 1 段与 Study 2 段不得直接并置），同段删句用 "..." 标注
- **提取来源**：优先本次蒸馏论文原文；缺失时检索 Obsidian 三库（路径见 `references/phase-2-extraction.md`）；检索不到标"待补"，不阻塞写入
- **边界**：锚定是风格参照不是复制源——写入时 placeholder 泛化系数/表格编号，citation 链接还原为纯文本

## 红线

- 骨架用 [placeholder] 泛化具体内容（变量名、系数值、表格编号）；节奏标记短语（"Thus, Hypothesis [N] was supported" "As Figure [X] shows"）和稳健性过渡句式（"To address this concern"）保留原样——这些正是要学的证据展演节奏
- causal language 强度匹配估计器设计（OLS→"associated with"，DiD→"effect of"）
- 统计量与事实严格取自原文；原文薄弱处如实记录
- post hoc 机制检验与稳健性检验分开标注
- 选择性报告非显著结果：记录为反模式并显式标注

## 与下游 Skill 的接口

- **`write-results`** — Phase 4 `skill_update_instructions` 直接指定写入文件和插入位置
- **`results-review`** — Phase 1.5 槽位覆盖 + Rhythm Map 可复用

## Context discipline

按需加载单个 phase reference，不预读全部；先查 `write-results/econometric-models/INDEX.md` 与 `_evidence_registry.yaml`，再打开具体语料文件对比或写回。

---
*基于 Pollock 2025 Ch07、MVP30 范文语料库构建。版本 1.9.0（2026-08-10 writing-for-agents 结构优化：Phase 0–5 模板/表格/示例迁移至 references/ 八文件，SKILL.md 557→约 100 行；description 压缩；反模式表并入 phase-3 reference；保留 Phase 0.75 批评驱动选材 + 写入预览-确认两段式 + distinct_from 速查表维护 + 原文锚定规则）。*
