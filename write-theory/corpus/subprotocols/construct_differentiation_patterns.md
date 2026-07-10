# Construct Differentiation Patterns

本文件收集 Theory 中 T1 构念辨析段落的可复用模式。当研究需要界定一个新构念、或重新定义一个易混淆构念时使用。

---

<!-- 
pattern_id: table_construct_differentiation
build_type: 构念辨析型 / 现象驱动型
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Table-Based Construct Differentiation

**适用场景**: 新构念与多个相关构念在多个维度上存在差异，需要建立清晰边界。
**微观动作序列**: Naming（构念命名）→ Differentiation dimensions table（多维度对比表）→ Scope condition → Theoretical consequence
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety vs product recall / scandal / brand spillover / customer complaints / algorithmic error）

**骨架**:
```
Among varied perspectives on [domain], [construct] represents a distinct form of [phenomenon] that has not received a lot of attention in extant research. In [Table X] (and an expanded literature review in [appendix]), we provide explicit comparisons of [construct] with other types of [related concepts] (e.g., [concept A], [concept B], [concept C]). In our proposed conceptual framework, [construct] represents a distinct phenomenon that requires specific consideration and that exerts unique effects on [outcome], relative to other types of [related concepts].
```

**为什么有效**: 表格将多个差异化维度同时呈现，降低读者认知负担；为后续机制推演建立清晰的研究对象边界。

**注意事项**:
- 表格维度需与后续理论论证直接相关（如 Advertising Focused? / Crisis Source / Brand Control / Digital）
- 避免维度过多导致读者疲劳；3-6 个维度为宜
- 表格后需用 1-2 句话总结最关键的差异维度及其理论后果

**反模式**: 若新构念与相关构念差异单一，不要用表格，用 1-2 句对比即可；若表格维度与后续 Theory 无关，会显得装饰性。

---

<!--
pattern_id: simultaneously_recognize_leverage
build_type: 跨类型
source_papers: ["Grewal_Vana_Stephen_2025_JM"]
confidence: medium
status: ready_for_corpus
-->

## Pattern: Simultaneously Recognize X but Leverage Y

**适用场景**: 研究对象与现有文献中的相关现象有相似性但机制不同，需要借用相关文献同时避免混淆。
**微观动作序列**: Recognition of difference → Leveraging similarity → Concrete illustration → Prediction transfer
**范文来源**: Grewal, Vana, and Stephen (2025), *Journal of Marketing*（brand safety vs contagion/spillover/proximity effects）

**骨架**:
```
We simultaneously (1) recognize that the mechanisms by which [related phenomenon] [affect actors] in [context] differ from the mechanism we propose for [construct], but we also (2) leverage insights from prior research in [domain A], [domain B], and [domain C] to derive some initial, potential explanations of why [construct] is likely to evoke [effect]. For example, [concrete illustration from domain A]. We apply this notion to [target context] to predict that [specific prediction].
```

**为什么有效**: 主动承认边界避免审稿人质疑 "这不是 A 研究吗？"，同时清晰说明借用理由；比简单 "Drawing on..." 更能处理文献流交织。

**注意事项**:
- 必须真正解释机制差异，不能流于形式；差异陈述要具体
- "leverage" 的文献必须与研究对象有足够相似性，否则显得牵强
- 建议在差异陈述后立即给出具体预测，避免停留在文献综述

**反模式**: 若相关文献与研究对象机制完全不同，不要强行 leverage；若只承认差异而不说明借用价值，会削弱理论贡献。

---

## 与相邻语料文件的关系

- [`../sentences/construct_definition.md`](../sentences/construct_definition.md)：微观句式模板（如 "We define X as..."）
- [`../subprotocols/argumentation_patterns.md`](argumentation_patterns.md)：微观动作组合
- [`../variants/A_construct_differentiation.md`](../variants/A_construct_differentiation.md)：构念辨析型整篇结构

> **使用顺序**：先查本文件确定 T1 辨析策略 → 再查 `construct_definition.md` 填充具体句式 → 再查 `argumentation_patterns.md` 组织论证动作。
