---
name: distill-story-exemplar
description: >-
  整篇论文故事蒸馏 meta-skill（Pollock Ch02/Ch03 视角）——输入范文（全文/四区段文本/已有蒸馏记录），输出结构化故事快照（knot 类型与复合结构、反派构造、角色、五幕落点、解法性格、alternative tellings、Ch03 工具层）并写入 story-blueprints 语料库。Use when the user asks to 蒸馏 story / 整篇故事蒸馏 / 故事快照 / 讲法对比 / 同一关系不同故事，or supplies a paper and wants the story-level distillation (not section-level). 核心原则：论文是一个故事单元——提炼 HOW they tell the story, not WHAT they found。事实纪律：字段必须来自原文或已验证蒸馏记录，缺失标 `待补`，禁止编造。Not for: 自己论文的故事设计（→ paper-story-contract）；草稿审查（→ paper-review/pollock-qc）；section 级蒸馏（→ distill-introduction/theory/methods/results-exemplar）。消歧：用户只说"蒸馏这篇论文"未指定层面时，先询问 section 级还是 story 级，不默认本 skill。
---

# Distill Story Exemplar

Distill how a published paper works as one story—not what it found—into a reusable story blueprint.

> **核心理念**：先问"你是 theorist / empiricist / knowledge creator / reporter 中的哪一种？"——只把自己当 fact reporter 就把论文当 research report，战斗已输一半。本 skill 把每篇范文当**一个故事**蒸馏：记录范本怎么讲（plot 从角色与情境中长出），写作时故事从你的研究里长出来。

## 核心定位

- **Story 级 ≠ Section 级**：四个 distill-* skill 拆零件入库；本 skill 回答"这篇论文讲的是个什么故事、为什么这样讲、还能怎么讲"。
- **语料不淘汰**：blueprint 不复制、不取代 section 变体，只通过 `corpus_links` 链接（关系见 `../story-blueprints/README.md`）。
- **schema 权威版**：`../story-blueprints/_schema.md`（字段规范与 knot 类型表）。blueprint 模板见 `protocols/blueprint_template.md`。

## 输入优先级

1. **全文 / 四区段文本**（最佳：五幕落点可实证定位）
2. **已有蒸馏记录**（memory / 各 distill-* 的产物 YAML / corpus 变体）——section 事实用它，避免重复读全文
3. **两者皆有**（推荐）：section 事实用蒸馏记录，climax/falling action 落点必要时回读原文对应段落

## Workflow

### Phase 0: Intake 与覆盖评估

1. 记录论文身份、期刊、`distilled_sections`（哪些区段已有深度蒸馏 → 决定哪些五幕字段可靠）。
2. **Vault 检索（必做，报告 + 全文双通道）**：读 `references/vault-retrieval-protocol.md`——报告区检索（更新 `distilled_sections`，报告与 memory 冲突以报告为准）+ 全文定位回读（补实 climax/falling_action/denouement）+ `_story_arcs/` 链接不复制 + `corpus_links` 收集 + 既有 blueprint 对照（供 Phase 4）。
   **完成判据**：`distilled_sections` 已按检索结果更新；`corpus_links`/`vault_reports` 已填或标"路径待验证"。
3. 检索 `../story-blueprints/blueprints/_index.md`：确认同构念对 / 同 GBL 对角线 / 同设计类型的既有 blueprint（供 Phase 4 对照）。

### Phase 1: Knot 与角色

按 `_schema.md` 提取：`knot.primary_type` + `compound_types`（表内无适配类型 → 新类型候选附原型论文，写入 `skill_design_feedback`）｜`knot.statement`（含冲突双方，一句）｜`knot.tied_at`/`untied_at`（系紧/解开位置）｜`knot.antagonist` + `antagonist_built_by`（反派 + 构造修辞——section 蒸馏不产出的字段）｜`characters`｜`resolution_logic`。
**完成判据**：knot 六字段 + characters + resolution_logic 齐全；新类型候选已标注。

### Phase 2: 五幕映射（Freytag）

每幕给出**证据位置**（原文段落 / 蒸馏记录变体名）。未蒸馏区段对应幕标 `待补`。注意 Pollock 多研究/多实验结构：rising/falling 重复起伏（每 study 一轮 climax），如实记录节奏而非强套单峰。
**完成判据**：五幕全有证据位置或显式 `待补`；多研究节奏已如实记录。

### Phase 3: Ch03 讲故事工具层

`human_face` / `rhetorical_question` / `pacing_notes` / `showing_telling` / `voice`——凡可从记录或原文推断即填，否则 `待补`。pacing_notes 尤其记录"节奏决策"：climax 落点、falling action 反转数、节长分配、多研究起伏。
**完成判据**：五字段填或 `待补`（无编造）。

### Phase 4: Alternative Tellings 与跨论文对照

1. 列出本文**未被选中的故事版本**（文献已有讲法 / 常见 gap-filling 版 / 换反派的版本）+ 本文选择及理由。
2. 与现有 blueprints 的对照写入 `cross_paper_notes`：同 GBL 对角线不同故事（Zhou 裁决 vs Pontikes 揭幕）、同设计类型不同故事（Pollock/Malshe 同时方程）、同现象域不同讲法。
**完成判据**：alternative_tellings ≥2 条（含被拒理由）；cross_paper_notes 已对照既有 blueprint。

### Phase 5: QC 与 Writeback

- **Schema 校验**：对照 `_schema.md` 逐字段检查；`待补` 字段列清单。
- **一致性抽查**：knot 类型不与已入库 intro 变体的分类冲突（如故事主型 `paradigms-at-war` 与 `03-non-coherence` 变体A 的定位互相印证）；冲突 → 记录进 `skill_design_feedback`。
- **人工预览-确认 gate**：写入前把 blueprint 全文展示给用户确认；用户明确要求批量自动时才能跳过单篇预览（"新增 knot 类型必须人工确认"是硬门）。
- **Writeback**：写入 `../story-blueprints/blueprints/<id>.md`，更新 `blueprints/_index.md`，必要时更新 `_schema.md` 类型表（新类型须有人工确认）。
- 输出 `skill_design_feedback`：语料缺口、格式缺陷、与 section 蒸馏的矛盾点。
**完成判据**：Schema 校验通过（或 `待补` 清单已列）；gate 已走；写回完成。

## Output contract

一份 blueprint 文件（按模板）+ `待补` 字段清单 + 跨论文对照表 + `skill_design_feedback`。区分直接证据（原文/蒸馏记录）与推断（标注 `[推断]`）。

## 选材 Gate

- 优先回填**已深度蒸馏**的论文（四区段蒸馏记录在手，五幕落点可靠；Desai 2012 式部分蒸馏论文标记 `PARTIAL`）。
- 未蒸馏论文需要全文输入，成本高 → 与用户确认后再做。
- 批量模式按蒸馏覆盖度排序（全四区段 → 部分区段）。

## Boundaries

- 不生成自己论文的写作；不设计自己论文的故事（→ paper-story-contract）。
- 不重复 section 蒸馏（发现 section 缺口 → 写进 `skill_design_feedback`，路由给对应 distill-* skill）。
- 禁止编造原文细节：climax 落点、系数、案例均须可溯源；不可溯源标 `待补`。
- 单篇 blueprint 不改变任何 skill 的路由、门禁或核心规则；新增 knot 类型须两篇以上原型或用户确认。
