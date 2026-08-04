---
name: distill-introduction-exemplar
description: |
  Introduction 范文蒸馏 meta-skill。输入单篇或批量论文的 Introduction 文本，输出结构化提炼报告：功能模块拆解、叙事结构模式、修辞策略 DNA、模块级表达骨架、Gap×Contribution 组合验证，并将跨论文证据反馈为 write-introduction 的语料缺口或技能设计缺陷。
  核心原则：Introduction 内容高度非标准化，但功能框架标准化。提炼 HOW they stage the narrative, not WHAT they say。不复制具体措辞，只提取可跨论文复现的功能组织方式和修辞策略。
  触发词：「蒸馏 introduction」「intro 范文分析」「拆解 introduction」「提取 intro 模板」「处理新论文 intro」「introduction 骨架提炼」。
  **消歧**：用户未指定 section（只说"分析这篇论文""蒸馏一下"）时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。
  **反向边界**：Introduction 写作用 `write-introduction`；审查已有 Introduction 草稿用 `intro-review`；写前深度诊断用 `diagnose-introduction`；全稿 QC 用 `pollock-qc`。本 skill 只蒸馏范文，不生成写作、不做 QC。
---

# Distill Introduction Exemplar

Distill how a published Introduction works—not what it says—into reusable, evidence-traceable writing assets.

## Workflow

1. Confirm whether the request is exemplar distillation or validation of a drafted Introduction.
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

## Output contract

Return the requested depth level, the functional module map, transferable expression skeletons, rhetorical logic, boundary conditions, evidence anchors, QC findings, and `skill_design_feedback`. For Incommensurability, include the L0–L3 profile, route confidence, closest alternative, and any unclassified residual. Separate direct evidence from inference, corpus updates, and core-skill defect hypotheses. Never copy source sentences as reusable templates.

## Context discipline

Do not preload every phase or the full writing corpus. Search the sibling `write-introduction/academic-writing-corpus/` indexes first, then open only the referenced files needed for comparison or writeback.
