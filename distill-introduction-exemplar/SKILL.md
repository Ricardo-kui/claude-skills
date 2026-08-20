---
name: distill-introduction-exemplar
description: "蒸馏顶刊论文 Introduction 范文——拆解功能模块、叙事结构模式与修辞策略 DNA（提炼 HOW they stage，不是 WHAT they say），并反馈 write-introduction 语料缺口。当用户要求学习/蒸馏某篇论文引言的写法时使用。"
whenToUse: "当用户要求蒸馏、提炼、学习某篇（或批量）论文 Introduction 部分的写法与叙事手法时使用。触发词：蒸馏 introduction、提炼这篇引言、学习范文引言写法、分析这篇 intro 怎么写的、introduction 范文蒸馏、批量蒸馏引言"
---

# Distill Introduction Exemplar

Distill how a published Introduction works—not what it says—into reusable, evidence-traceable writing assets.

## Workflow

1. Confirm whether the request is exemplar distillation or validation of a drafted Introduction；用户只说"分析/蒸馏这篇论文"未指定 section 时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。
2. Read `references/intake-and-classification.md`, classify Gap × Contribution, and apply the shared story-fidelity gate before extracting or adopting patterns. For Incommensurability, also read `../write-introduction/references/incommensurability-introduction-routing.md`; produce its L0–L3 full-text distillation profile before extracting skeletons.
3. Load only the phase reference needed for the current step:
   - module mapping: `references/phase-1-module-map.md`
   - coverage and narrative quality: `references/phase-1-5-coverage.md`
   - rhetorical and expression extraction: `references/phase-2-extraction.md`
   - DNA/profile reporting: `references/phase-3-dna-report.md`
   - cross-paper validation and writeback: `references/phase-4-validation-writeback.md`
   - final QC: `references/phase-5-qc.md`
   - completed-draft validation: `references/product-validation-and-boundaries.md`
4. Load supporting protocols only when their output is required: `protocols/batch_mode.md`, `protocols/profile_template.md`, `protocols/story_architecture_fields.md`, `protocols/product_validation.md`, `protocols/phase4_output_blocks.md`, `protocols/corpus_file_templates.md`, and `protocols/json_output_schema.md`.
5. Preserve evidence provenance. Do not promote a one-paper pattern to a stable corpus rule. Use fine-grained Incommensurability routes for retrieval and comparison, not as mandatory templates: L2 tactics remain optional variants and L3 paper signatures never enter core routing.
6. In Phase 4, compare observed practice with current `write-introduction` rules and emit `skill_design_feedback`. Persist every candidate with `_update_design_feedback.py`; distinguish corpus gaps from routing, validator, output-contract, schema, and stage-gate defects.
7. Auto-write reference variants. Apply bounded core corrections only when the evidence and authorization gates in `references/phase-4-validation-writeback.md` pass; always review schema or stage-gate changes explicitly.

**完成判据**：①请求性质已确认（蒸馏 vs 校验；section 已消歧）；②Gap × Contribution 分类 + story-fidelity 判定已输出（Incommensurability 时含 L0–L3 profile 与 route confidence）；③所用 phase 的输出件按请求深度齐全（module map / coverage / skeletons / DNA / QC）；④每个写入变体附带原文锚定字段；⑤`skill_design_feedback` 已用 `_update_design_feedback.py` 持久化；⑥core 修正仅经 phase-4 证据与授权门禁。

## 选材 Gate（轻量版：读 _index 验证状态）

蒸馏选材时，读目标目录的 `write-introduction/academic-writing-corpus/<目录>/_index.md` 验证状态列（ROBUST/VERIFIED/EMERGING）做三带判定：

| 带 | 判定条件 | 处理 |
|----|---------|------|
| **gap** | _index 中无此类变体/模块 | **HIGH**：ADD 候选，优先深读 |
| **薄弱** | 目标变体 EMERGING（单篇来源）或验证状态低 | **HIGH**：EXTEND/REPLACE 候选 |
| **quiet** | 目标变体 ROBUST/VERIFIED | MEDIUM：正常蒸馏（除非论文带来明确新维度） |

批量模式按带排序优先处理 HIGH 档。单篇论文（用户明确指定）不拒绝，但输出带判定。

## 原文锚定提取规则（语料锚点层）

每个待写入变体必须附带 `**原文锚定**` 字段——来源论文 1-2 句 verbatim 原句（15-50 tokens），风格参照用：

- **选句标准**：最能代表该变体叙事手法的句子（如 Hook 的数据冲击句、Tension 的 however 对比句、Stakes 的重要性论证句），不是信息量最大的句子
- **提取来源**：优先本次蒸馏论文原文；缺失时按知识库检索（mvp30 / Clippings / 论文导入 / 写作指导 四源，见各 corpus 文件惯例）
- **检索不到原文**：锚定标"待补"，不阻塞写入
- **边界**：锚定是风格参照不是复制源——不得保留专有名词/数字；citation 链接还原为纯文本

## Output contract

Return the requested depth level, the functional module map, transferable expression skeletons, rhetorical logic, boundary conditions, evidence anchors, QC findings, and `skill_design_feedback`. For Incommensurability, include the L0–L3 profile, route confidence, closest alternative, and any unclassified residual. Separate direct evidence from inference, corpus updates, and core-skill defect hypotheses. Never copy source sentences as reusable templates.

## Context discipline

Do not preload every phase or the full writing corpus. Search the sibling `write-introduction/academic-writing-corpus/` indexes first, then open only the referenced files needed for comparison or writeback.
