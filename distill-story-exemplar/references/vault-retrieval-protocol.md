# Vault Retrieval Protocol — Phase 0 检索与全文定位规程（从 SKILL.md 下沉，v0.1）

> 由 distill-story-exemplar Phase 0 执行。**Vault Batch 报告检索（必做——memory 常低估蒸馏覆盖度）** + **全文检索（必做——报告区常缺 Results/Discussion 原文）**。

## 1. 报告区检索

按论文短名（作者姓氏+年份 / 现象短语，如 `lashley_pollock2020`、`waiting_to_inhale`）在 vault 报告区检索，基目录 `D:\OneDrive\Obsidian Vault\00 工作台\叙述模板训练集\narrative_analysis\`（缺失时用 Glob 定位）：

- `mvp30/<key>_narrative.md` — 整篇 narrative 文件
- `introduction/mvp30/fine_grained/**/<key>*distilled_introduction.md` — Intro 细蒸馏报告（batch_2026-05-21/24/26、batch_3、batch_individual 等）
- `theory/mvp30/fine_grained/**/<key>*distilled_theory.md` — Theory 细蒸馏报告（batch_2026-07-09 等）
- `methods_results/mvp30/fine_grained/batch_*/<key>*_fine_methods_results.md` — Methods/Results 细蒸馏（batch_08/09/12/13…）
- `methods_results/mvp30/deep_distillation/papers/<key>*deep_profile.md` — 深蒸馏 profile
- `methods_results/mvp30/methods/<key>_methods_narrative.md` + `results/<key>_results_narrative.md` — 单节 narrative
- `_story_arcs/<key>_story_arc.md` — 早期故事弧资产（见下）

检索到即更新 `distilled_sections`（memory 只记 intro/theory 但 batch 报告在 → 直接升 ROBUST，如 gamache2020/cutolo2024 先例；报告与 memory 冲突时以报告为准并在 blueprint 标注）。

**vault `_story_arcs/` 处理规则**：该目录是早期故事层资产（`<key>_story_arc.md` + `_story_arc_index.md`）。blueprint 与之是"链接不复制"关系——在 `corpus_links` 或 `vault_reports` 中引用其路径，不把其内容搬进 blueprint；若其字段与 blueprint 冲突（早期字段定义不同），以 blueprint 的 `_schema.md` 为准并标注差异。

## 2. 全文检索与回读

按论文短名 + 标题关键词在以下 vault 路径用 Glob 定位全文；命中即回读缺失区段补实五幕（climax/falling_action/denouement 的系数、支持状态、Discussion 收口）：

- `00 工作台/叙述模板训练集/_parsed_texts/mvp30/` — 标准 parsed 全文（**非唯一全文位置**）
- `文献笔记库/01 导入/论文导入/` — 论文导入区（命名如 `Pfarrer, Pollock, and Rindova 2010.md`；pfarrer2010 先例：此处 `_parsed_texts/` 无此文、全文实际在此，检索报告区会误判"原文不可得"）
- `Clippings/` — 网页剪藏区（命名不定，用作者姓氏+年份模糊 Glob）

## 3. 蒸馏记录检索与 corpus_links

检索现有蒸馏记录（memory 文件、`write-*` corpus 变体、distill-* 临时 YAML），收集 `corpus_links`：对照各 corpus 的 `_index.md` 验证变体名与状态列；找不到或名称存疑 → 链接标"路径待验证"，不阻塞。vault 报告路径写入 blueprint 文件头的 `vault_reports` 字段。

## 4. 既有 blueprint 检索

检索 `../story-blueprints/blueprints/_index.md`，判断是否存在同构念对 / 同 GBL 对角线 / 同设计类型的既有 blueprint（供 Phase 4 对照）。
