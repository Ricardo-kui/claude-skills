---
name: distill-methods-exemplar
description: "Methods 范文蒸馏——输入范文 Methods，输出设计分类/M1-M10 槽位映射/表达骨架提炼报告并反馈 write-methods 语料。Use when 蒸馏 methods 范文（学 HOW they argue）。"
when_to_use: "输入是已发表范文且目标是学写法时；写作用 write-methods，审查用 methods-review。"
whenToUse: "Use when 用户要蒸馏已发表论文的 Methods 范文，提炼其论证结构、设计分类、M1-M10 槽位映射与表达骨架并写回 write-methods 语料。Trigger words: 蒸馏方法部分, 蒸馏 methods 范文, 学习这篇方法怎么写, exemplar distillation, 范文提炼"
---

# Distill Methods Exemplar

Distill how a published Methods section argues—not what it says—into reusable, evidence-traceable writing assets for `write-methods/econometric-models/`。

三层递进：学习顶刊叙述手法（Phase 0–2）→ 量化与跨论文对比（Phase 3–4）→ 沉淀到 corpus（Phase 4–5）。核心原则：How > What；范式排他性（只提取该类设计特别需要的组织方式）；每个骨架必须能直接指导新论文写出段落（可生成性）。

## Phase 0.5 — Story-Fidelity Gate

加载 `../paper-story-contract/references/distillation-gate.md` 并输出 `story_fidelity`。Methods 的 section role 是 `empirical_arena`：模式必须帮助测试 promised resolution 或提高可信度，不因其"像故事"而采用；ritual 记录为 `ritual_only`；与 story-to-design mapping 冲突的模式标记为 `reject`。

**完成判据**：story_fidelity 已输出；ritual/conflict 模式已分类。

## 调用方式

```
/distill-methods-exemplar <输入路径或文本> [--batch] [--design-filter=面板数据/DiD/实验/...] [--output-format=markdown/json]
```

- `<输入路径或文本>`（必填）：论文文件路径、PDF 路径、粘贴文本、或包含多篇论文材料的目录；省略时进入交互式询问。
- `--batch`：批量处理模式，输出跨论文模式聚合报告；`--design-filter`：只处理特定设计类型；`--output-format`：默认 markdown，可选 json 供脚本消费。
- **消歧**：用户只说"分析/蒸馏这篇论文"未指定 section 时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。`write-methods` 检测到蒸馏请求时路由到本 skill。

## Phase 0 — 论文类型与设计分类

读 `references/intake-and-classification.md`（五维分类表 + 输出 yaml），在读取正文前判定设计范式。

**完成判据**：`phase_0_design_profile` 五维齐全。

## Phase 0.75 — 选材 Gate（批评驱动）

运行 `python ../distill-paper-exemplar/scripts/corpus_query.py registry --section methods --query "<设计类型关键词>"`（确定性脚本，只输出命中块，默认 ≤50 行），用命中块的 `validation_history` 判定本文值不值得深蒸馏；**禁止整读 `_evidence_registry.yaml`**：

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap** | `slots_covered` 存在缺口（静态） | **HIGH**：ADD 候选，优先深读 |
| **critique_heavy** | `revise + reject >= 2` | **HIGH**：REPLACE/EXTEND 候选；`common_revise_reasons` 是精炼依据 |
| **quiet** | 其余 | MEDIUM：正常蒸馏 |

单篇不拒绝但必须输出带判定；批量按带排序。频繁使用且好用的变体提升路由权重，语料不因使用频率淘汰（registry `non_signals`）。

输出 yaml、执行规则、重复闸门（jaccard ≥ 0.33 → SKIP）与趋同批评聚合检查：读 `references/selection-gate.md`。

**完成判据**：band + priority + rationale 已输出；趋同批评 ≥2 时已追加聚合检查块。

## Phase 1 — 文本读取与槽位映射（M1–M10）

读 `references/phase-1-module-map.md`（槽位映射表 + quality/learn_worth 标记标准 + 输出 yaml），只定位段落功能，不做深入分析。

**完成判据**：每个槽位有 quality + learn_worth 标记。

## Phase 1.5 — 槽位覆盖检查与调研质量摘要

读 `references/phase-1-5-coverage.md`（16 类设计强制槽位表 + 质量摘要 yaml）。

**完成判据**：coverage_verdict + skill_implication 已输出。

## Phase 2 — 深度提炼（功能 / 骨架 / Validity Logic）

读 `references/phase-2-extraction.md`（说服动作表 + 骨架格式 + skill_gap 标准 + 输出 yaml）。锚点规则见文末「原文锚定提取规则」。

**完成判据**：每个骨架有 skill_gap 标注 + 目标文件/槽位 + verbatim_anchor。

## Phase 3 — 论证手法诊断

读 `references/phase-3-dna-report.md`（五维诊断 + fine_grained profile 模板）。每个诊断维度附带 skill 对比：`[定性判断] → 与 write-methods 当前模板的关系 → [skill 改进方向]`。

**完成判据**：五维诊断齐全；fine_grained profile 已生成。

## Phase 4 — 技能更新指令生成

读 `references/phase-4-validation-writeback.md`（指令格式 + 待写入预览块模板 + 批评登记）。**所有待写入内容先展示预览、用户确认后才写入**——单篇逐个确认，批量一次确认 ADD/EXTEND、REPLACE 仍逐个确认。

**完成判据**：每条 ADD/EXTEND/REPLACE 有 target_file + insert_after + distinct_from；预览块含骨架全文与原始句锚点。

## Phase 5 — 质量验证与版本影响

读 `references/phase-5-qc.md`（QC Checklist 9 项 + skill_version_impact 格式 + 最终输出物清单 8 项）。

**完成判据**：QC 9 项全过；每个 ADD/EXTEND/REPLACE 附带版本影响评估。

## 原文锚定提取规则（语料锚点层）

每个待写入变体必须附带 `verbatim_anchor`——来源论文 1–2 句 verbatim 原句（15–40 tokens），风格参照用：

- **选句标准**：最能代表该变体叙事手法的句子，不是信息量最大的句子
- **拼接硬规则**：多句锚点保留省略号标记；跨段落/跨小节拼接必须显式标注，同段删句用 "..." 标注
- **提取来源**：优先本次蒸馏论文原文；缺失时检索 Obsidian 三库（路径见 `references/phase-2-extraction.md`）；检索不到标"待补"，不阻塞写入
- **边界**：锚定是风格参照不是复制源——写入时 placeholder 泛化专有名词/数字，citation 链接还原为纯文本

## 红线

- 骨架用 [placeholder] 泛化具体内容（变量名、数据库名、系数值）；关键论证连接词（"because" "however" "in contrast"）和叙事结构短语（"for three reasons" "to address this concern"）保留原样——这些正是要学的手法
- causal language 强度匹配设计类型（OLS→"associated with"，DiD→"effect of"，实验→"increases"）
- 统计量与事实严格取自原文；原文薄弱处如实记录
- 设计类型分桶处理，骨架只在同范式内迁移

## 与下游 Skill 的接口

- **`write-methods`** — Phase 4 `skill_update_instructions` 直接指定写入文件和插入位置
- **`methods-review`** — Phase 1.5 槽位覆盖检查可复用

## Context discipline

按需加载单个 phase reference，不预读全部；先经 `python ../distill-paper-exemplar/scripts/corpus_query.py index --section methods --query "<槽位/设计类型关键词>"` 与 `... registry --section methods --query "<关键词>"` 查命中行（确定性，默认 ≤50 行），再打开具体语料文件对比或写回——**整读 INDEX.md / _evidence_registry.yaml 已废止**。

---
*基于 Pollock 2025 Ch07、MVP30 范文语料库构建。版本 1.9.0（2026-08-10 writing-for-agents 结构优化：Phase 0–5 模板/表格/示例迁移至 references/ 八文件，SKILL.md 548→约 100 行；description 压缩；保留 Phase 0.75 批评驱动选材 + 写入预览-确认两段式 + distinct_from 速查表维护 + 原文锚定规则）。*
