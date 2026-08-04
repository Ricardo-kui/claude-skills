---
name: distill-theory-exemplar
description: |
  Theory & Hypotheses 范文蒸馏 meta-skill。输入单篇或批量论文的 Theory 文本，输出结构化提炼报告：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架，并将跨论文证据反馈为 write-theory 的语料缺口或技能设计缺陷。
  从已发表论文的 Theory 中提炼可复用骨架：理论构建类型识别、功能模块拆解、why-chain 模式、构念关系组织方式、模块级表达骨架。不验证用户写作——Theory 写作 QC 请使用 `/theory-review`。
  核心原则：Theory 内容高度非标准化（因研究问题而异），但功能框架和推理结构是标准化的。提炼 HOW they explain why, not WHAT they explain。不复制具体机制内容，只提取可跨论文复现的理论论证组织方式和 why-chain 结构。
  触发词：「蒸馏 theory」「理论范文分析」「拆解 theory」「提取 theory 模板」「处理新论文 theory」「theory 骨架提炼」「why chain 提炼」。
  **消歧**：用户未指定 section（只说"分析这篇论文""蒸馏一下"）时，先询问蒸馏哪个 section（Introduction/Theory/Methods/Results），不默认本 skill。
  **反向边界**：Theory 写作用 `write-theory`；审查已有 Theory 草稿用 `theory-review`；全稿 QC 用 `pollock-qc`。本 skill 只蒸馏范文，不生成写作、不做 QC。
---

# Distill Theory Exemplar

Distill the architecture and reasoning of a published Theory section into reusable patterns without copying its substantive claims.

## Workflow

1. Read `references/intake-and-classification.md`; identify theory-building type, hypothesis structure, evidence boundaries, and story-fidelity classification. For Incommensurability, also read `../write-theory/references/incommensurability-resolution-routes.md` and produce its L0–L3 full-text profile before extracting hypothesis skeletons.
2. Load only the phase required:
   - module mapping, special institutional-shock lenses, and coverage: `references/phase-1-module-map.md`
   - persuasive actions, expression skeletons, and why-chains: `references/phase-2-extraction.md`
   - DNA/profile reporting and DNA→validator reflux (Phase 3.5): `references/phase-3-dna-report.md`
   - cross-paper validation and corpus writeback: `references/phase-4-validation-writeback.md`
   - final QC, honesty boundaries, and downstream interface: `references/phase-5-qc-and-boundaries.md`
3. Load supporting protocols only as needed: `protocols/corpus_taxonomy.md`, `protocols/phase2_extraction_frameworks.md`, `protocols/profile_template.md`, `protocols/phase5_qc.md`, `protocols/connector_patterns.md`, `protocols/pollock_annotations.md`, and `protocols/writeback_reminders.md`.
4. Compare against the sibling `write-theory/corpus/` only after the paper-first extraction is complete.
5. Treat single-paper patterns as candidates, not stable corpus rules. For Incommensurability, use R1–R4 to compare reasoning, not to impose model form: L2 architectures remain optional and L3 model signatures never enter core routing. Reference-level variants may be written automatically; core candidates first enter the design registry and only bounded, eligible low/medium-risk corrections may auto-apply.
6. In Phase 4, load `references/design-feedback-loop.md`, compare observed practice with current write-theory rules, and always emit `skill_design_feedback`（无缺陷时 `observations: []`）. Persist candidates with `_update_design_feedback.py`.
7. Auto-write eligible reference variants. Apply bounded core corrections only when the evidence, authorization, risk, and dual-regression gates pass; schema/stage-gate/high-risk changes always require explicit review.

## Output contract

Return the theory-building classification, functional module map, why-chain, construct relationships, hypothesis organization, transferable skeletons, non-transferable boundaries, evidence anchors, QC findings, and `skill_design_feedback`. For Incommensurability, include L0–L3, route confidence, closest alternative, unclassified residual, architecture necessity, and the distinguishing prediction. Separate corpus enrichment from core-design defects, label inference explicitly, and never copy source sentences as templates.

## Context discipline

Do not preload the full write-theory corpus. Finish paper-first extraction, then inspect only the exact rule targets and corpus files needed for comparison, persistence, or writeback.
