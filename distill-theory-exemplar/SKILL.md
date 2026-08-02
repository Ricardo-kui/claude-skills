---
name: distill-theory-exemplar
description: |
  Theory & Hypotheses 范文蒸馏 meta-skill。输入单篇或批量论文的 Theory 文本，输出结构化提炼报告：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架、以及 write-theory 更新建议。
  从已发表论文的 Theory 中提炼可复用骨架：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架。不验证用户写作——Theory 写作 QC 请使用 `/theory-review`。
  核心原则：Theory 内容高度非标准化（因研究问题而异），但功能框架和推理结构是标准化的。提炼 HOW they explain why, not WHAT they explain。不复制具体机制内容，只提取可跨论文复现的理论论证组织方式和 why-chain 结构。
  触发词：「蒸馏 theory」「理论范文分析」「拆解 theory」「提取 theory 模板」「处理新论文 theory」「theory 骨架提炼」「why chain 提炼」。
---

# Distill Theory Exemplar

Distill the architecture and reasoning of a published Theory section into reusable patterns without copying its substantive claims.

## Workflow

1. Read `references/intake-and-classification.md`; identify theory-building type, hypothesis structure, evidence boundaries, and story-fidelity classification.
2. Load only the phase required:
   - module mapping, special institutional-shock lenses, and coverage: `references/phase-1-module-map.md`
   - persuasive actions, expression skeletons, and why-chains: `references/phase-2-extraction.md`
   - DNA/profile reporting and DNA→validator reflux (Phase 3.5): `references/phase-3-dna-report.md`
   - cross-paper validation and corpus writeback: `references/phase-4-validation-writeback.md`
   - final QC, honesty boundaries, and downstream interface: `references/phase-5-qc-and-boundaries.md`
3. Load supporting protocols only as needed: `protocols/corpus_taxonomy.md`, `protocols/phase2_extraction_frameworks.md`, `protocols/profile_template.md`, `protocols/phase5_qc.md`, `protocols/connector_patterns.md`, `protocols/pollock_annotations.md`, and `protocols/writeback_reminders.md`.
4. Compare against the sibling `write-theory/corpus/` only after the paper-first extraction is complete.
5. Treat single-paper patterns as candidates, not stable corpus rules. Only reference-level variants may be written automatically; core candidates require explicit human review.

## Output contract

Return the theory-building classification, functional module map, why-chain, construct relationships, hypothesis organization, transferable skeletons, non-transferable boundaries, evidence anchors, and QC findings. Label inference explicitly and never copy source sentences as templates.
