# 入库 corpus 文件模板

> 外置自 `distill-introduction-exemplar/SKILL.md`。何时加载：Phase 4.6 写入 corpus 文件前加载。

---

### 变体 [字母]：[变体类型名]（[来源论文]型）
                                          ↑ 来源: Phase 2.2 [变体类型名]

**模板**:
> "[句法模板]"
   ↑ 来源: Phase 2.2 [骨架]

**来源**: [作者_年份] ([期刊]), P[段落号]
                                        ↑ 来源: Phase 2.2 [来源段落]

**原文锚定**:
> "[原文关键句，保留原文措辞]"
   ↑ 来源: Phase 2.2 [原文锚定句]

**关键特征**:
- [特征1：为什么与已有变体不同]
- [特征2：独特的说服机制]
- [特征3：标志性语言特征]
   ↑ 来源: Phase 2.2 [关键特征列表]（逐条展开）

**适用**: [什么研究情境下选这个变体而非其他变体]
   ↑ 来源: Phase 2.2 [适用情境]

**禁忌**: [如有使用禁忌]
   ↑ 来源: Phase 2.2 [使用禁忌]
```

**字段映射总表**（Phase 2.2 → corpus .md）：

| corpus .md 字段 | Phase 2.2 来源字段 | 直接复制？ |
|----------------|-------------------|----------|
| `### 变体 X：[名称]` | `[变体类型名]` | 是 |
| `**模板**` | `[骨架]` | 是 |
| `**来源**` | `[来源段落]` | 是 |
| `**原文锚定**` | `[原文锚定句]` | 是 |
| `**关键特征**` | `[关键特征列表]` | 逐条展开为 bullet points |
| `**适用**` | `[适用情境]` | 是 |
| `**禁忌**` | `[使用禁忌]` | 是 |

4. **定位插入点**：找到文件中 `## 组装规则` 标题（如无则用 `## 期刊适配`，如无则追加到文件末尾）。在它**之前**插入新变体块。
5. **用 Edit 工具写入**
6. **更新文件 frontmatter**：新变体写入后，读取文件顶部 `---...---` 之间的 frontmatter，做以下三项更新：

   **6a. 追加 source_papers**：将新论文以以下格式追加到 `source_papers` 列表末尾：
   ```yaml
   source_papers:
     - author_year (journal, year): "brief description of what this paper contributes to the template"
   ```
   如果该论文已在 `source_papers` 中存在，跳过。`brief description` 从 Phase 2.2 的 `[变体类型名]` 和 `[关键特征列表]` 提取。

   **6b. 重算 cross_paper**：根据 `source_papers` 列表重新计算：
   - 从每条 `source_papers` 条目提取期刊名（括号中的缩写，如 `ASQ`、`SMJ`）
   - 计数：`paper_count = len(source_papers)`，`journal_count = len(unique journals)`
   - 判定规则（与 `_evidence_registry.yaml` 状态规则一致）：
     - `paper_count ≥ 5` 且 `journal_count ≥ 2` → `cross_paper: ROBUST`
     - `paper_count ≥ 3` → `cross_paper: VERIFIED`
     - `paper_count ≤ 2` → `cross_paper: EMERGING`

   **6c. 更新日期**：如果 frontmatter 中有 `updated:` 字段 → 更新为当前日期。如果没有 → 在 `source:` 行之前新增 `updated: [当前日期]`。

   **更新方式**：使用 Edit 工具，`old_string` = 当前 frontmatter 块（从第一个 `---` 到第二个 `---`），`new_string` = 更新后的 frontmatter 块。**注意**：只改 `source_papers`、`cross_paper`、`updated` 三个字段，不修改其他 frontmatter 字段（`type`、`canonical_id`、`status`、`gap_type`、`generativity`、`exclusivity`、`created`、`source` 等保持不变）。

7. **验证**：读回文件 frontmatter 和新变体段落，确认 frontmatter 更新正确、变体编号正确、格式正确

#### 操作 B：创建新模板文件（`create_new_file`）

当蒸馏发现 corpus 中不存在的新 canonical_id 时：

**步骤**：

1. **确定文件路径**：`corpus/[module]/[canonical_id].md`
2. **确认不重复**：Phase 4.5 已在注册表中创建条目，确认该 canonical_id 在注册表中 `status = EMERGING` 且 `paper_count = 1`
3. **创建文件**，使用以下完整骨架：

```markdown
---
type: canonical_[module单数]
canonical_id: "[canonical_id]"
status: EMERGING
gap_type: [Gap类型]
cross_paper: EMERGING
generativity: [来自 Phase 2.4]
exclusivity: [来自 Phase 2.2 范式排他性]
source_papers:
  - [作者_年份] ([期刊], [年份]): "[论文核心主题]"
created: [当前日期]
source: Distilled by distill-introduction-exemplar Phase 4.6
---

# [canonical_id] — [模板中文名]

## 功能描述

[Phase 2.1 persuasive_action + 简洁的功能说明]

## 适用场景

- Gap 类型 = **[Gap类型]**
- [具体适用条件1]
- [具体适用条件2]

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): [作者_年份] ([期刊])

### 生成力
- [来自 Phase 2.4 generativity_test]

### 排他性
- [来自 Phase 2.2 范式排他性]

---

## 句法模板

### 变体 A：[变体类型名]（[来源]型）

**模板**:
> "[句法模板]"

**来源**: [作者_年份] ([期刊]), P[段落号]

**原文锚定**:
> "[原文关键句]"

**关键特征**:
- [特征1]
- [特征2]

---

## 组装规则

### 必须配对
- [如 Phase 2.3 rhetorical_logic 中有配对信息则填写，否则写"暂无跨论文配对数据"]

### 互斥
- [如 Phase 1.5 或 Phase 4 聚合分析中有互斥信息则填写]

### 反模式提醒
- [Phase 2.4 批评家发现的常见问题]

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| [期刊名] | [⭐/⭐⭐/⭐⭐⭐] [评级] | [具体注意事项] |

---

## 槽位填充正误对比

### `[关键槽位名]` — [槽位描述]

❌ "[错误填充示例]" → [为什么错]

✅ "[正确填充示例]" → [为什么对]

**填充检查**: [检查方法]
```

4. **写入文件**（Write 工具）
5. **同步注册表**：Phase 4.5 已创建注册表条目，Phase 4.6 创建 .md 文件后两者配对完整

#### 操作 C：写入/更新风格画像（`append_variant` 和 `create_new_file` 均执行）

> **目的**：让 Phase 3 的 Narrative Style Profile 数据进入 corpus 文件，供 write-introduction 消费。每个 corpus 文件末尾维护一个 `## 风格画像` 章节，随每次入库累积更新。

**步骤**：

1. **检查是否已有风格画像章节**：在目标 corpus 文件中搜索 `## 风格画像` 标题
2. **提取 Phase 3 风格数据**：从当前论文的 Fine-Grained Profile 中提取以下字段：
   - `narrative_style_profile.tone` + `tone_evidence`
   - `narrative_style_profile.paragraph_rhythm`
   - `narrative_style_profile.distinctive_features`
   - `narrative_style_profile.avoids`
   - `narrative_style_profile.quality_markers`
3. **合并写入**：

   - **如果文件已有 `## 风格画像` 章节**：读取已有内容，将新论文的 Distinctive Features 和 Avoids 中不重复的条目追加到对应列表末尾。新条目以 `[作者_年份]` 标注来源。Quality Markers 如果新论文的 strongest_aspect 比已有的更具体，替换。Tone 如果新论文的主语气与已有不同，追加为次语气（标注来源论文和适用条件）。

   - **如果文件尚无 `## 风格画像` 章节**：在文件末尾（`## 槽位填充正误对比` 之后，或文件最后一个 `---` 之后）创建该章节，严格按以下格式：

```markdown
---

## 风格画像

> 以下风格特征是从使用本模板的多篇顶刊论文中聚合提取的。不是每篇论文都必须遵守，但偏离时应有明确理由。
> 最后更新: [当前日期] | 聚合论文数: [N]

### 语气光谱
- **主语气**: [来自 Phase 3 Tone]
- **证据**: "[来自 Phase 3 tone_evidence]"

### 段落节奏
- **典型节奏**: [来自 Phase 3 Paragraph Rhythm]

### 标志性叙事标记
- [[作者_年份]]: [来自 Phase 3 Distinctive Feature 1] — "[原文例句]"
- [[作者_年份]]: [来自 Phase 3 Distinctive Feature 2] — "[原文例句]"

### 刻意回避
- [[作者_年份]]: [来自 Phase 3 Avoids 1] — 功能: [功能解释]
- [[作者_年份]]: [来自 Phase 3 Avoids 2] — 功能: [功能解释]

### 质量标记
- **最值得模仿**: [来自 Phase 3 strongest_aspect]
- **已知风险**: [来自 Phase 3 weakest_aspect]

### 模块比重参考
- Hook [N%] / Literature Turn [N%] / Tension [N%] / Stakes [N%] / Theory Lens [N%] / Preview [N%] / Contribution [N%]
- *来源: [作者_年份]*
```

4. **更新聚合论文数**：已有章节的 `聚合论文数` +1
5. **用 Edit 工具写入**（在文件末尾追加，或在已有 `## 风格画像` 章节内更新）

**合并规则**：
- `[作者_年份]` 标签用于区分不同来源论文的风格贡献——同一模板被多篇论文使用时会自然累积
- 不覆盖已有内容，只追加——保留历史风格数据的完整性
- 如果新论文的 Distinctive Feature 与已有条目功能相同（如都在说"使用 paired contrasts"），追加为同一 feature 下的新 evidence 句，不创建重复条目

#### 操作 D：组合风格画像（已弃用 — v3.3.0）

> **write-introduction v3.3.0 已删除 `_combo_style_profiles.yaml`。** `style_profile_enrichment.per_combo_styles` 数据仍在 Phase 4 生成（供未来使用），但不再写入独立文件。`module_ratio_average` 是其中最可靠、最可自动化的字段——如果未来需要恢复组合风格数据，应从该字段开始重建。

当前 `per_combo_styles` 的输出去向：
- Phase 4 末尾的 `style_profile_enrichment` YAML 块中**仍然生成**（保留在对话输出中，供人工查阅）
- **不再回写**到 `corpus/` 下的任何文件
- write-introduction 的"风格提示"块目前仅依赖 corpus 文件的 `## 风格画像` 章节（单模板层），不依赖组合层数据

#### 安全规则

- **绝不覆盖已有变体**：追加前确认变体类型名不与已有变体重名
- **保留原文措辞**：句法模板和原文锚定保留 Phase 2.2 提炼的原始内容，不过度泛化
- **不修改已有内容**：追加操作只插入新变体块，不编辑文件中已有部分
- **注册表先更新**：Phase 4.5 在 Phase 4.6 之前执行——定量证据先于定性内容
- **文件不存在时**：`append_variant` 但目标文件不存在 → 降级为 `create_new_file`
- **重复检测**：如果新变体的句法模板与已有变体 ≥70% 相似 → 跳过并记录在摘要中

#### 输出

完成后在 Phase 4 末尾输出操作摘要和风格入库摘要：

```
### Phase 4.6 入库摘要

#### 语料库文件

| 操作 | 目标文件 | 详情 | 状态 |
|------|---------|------|------|
| 追加变体 | hooks/06-paradigm-challenge.md | +变体 F（监管冲击型），来源 darby2024 | ✓ 已写入 |
| 追加/更新风格画像 | hooks/06-paradigm-challenge.md | +Tone: assertive, +2 标志性标记, +1 刻意回避 | ✓ 已更新 |
| 追加变体 | tensions/01-despite-progress-unaddressed.md | +变体 I（制度冲突型），来源 lehman2014 | ✓ 已写入 |
| 追加/更新风格画像 | tensions/01-despite-progress-unaddressed.md | 已有风格画像，+1 论文风格数据，聚合论文数 8→9 | ✓ 已合并 |
| ~~更新组合风格画像~~ | ~~_combo_style_profiles.yaml~~ | 已弃用（v3.3.0）—— `per_combo_styles` 仍在 Phase 4 输出中生成，但不再回写文件 | — |
| 创建新文件 | stakes/08-supply-chain-disruption.md | 新 Stakes 模板 + 初始风格画像 | ✓ 已创建 |
| 跳过 | hooks/04-puzzle-paradox.md | 与已有变体 B 句法相似度 85%，合并而非新增 | — |
| 待修正 | tensions/03-structural-blindspot.md | Phase 2.4 REVISE — 事实边界测试未通过 | 待人工 |

**入库**：2 追加 / 1 新建 / 3 风格画像更新 / 1 组合画像更新 / 1 跳过 / 1 待修正
```
```

---
