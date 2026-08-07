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

<!--
pattern_id: geometric_sibling_construct_minimal_pair
build_type: 构念辨析型（showing device）
source_papers: ["Li_Bapuji_Talluri_Singh_Venkataraman_2026_POM"]
confidence: low
status: needs_validation
related: argumentation_patterns.md::minimal_pair_contrast_vignette（语言/表征最小对）；本模式 = 空间/结构几何最小对
-->

## Pattern: Geometric Sibling-Construct Minimal Pair（几何兄弟构念最小对）

**适用场景**: 两个兄弟维度（sibling dimensions of an umbrella construct）在文献中被互换测量，需要在 Theory 开篇用**受控几何对比**证明它们可独立变化——固定维度 A、只变维度 B——从而合法地把后续机制分工建立在"可分离构念"上。

**微观动作序列**: Define A + Define B → Hold A constant / vary B（Figure）→ State that managing challenges differ → Bridge to mechanism division

**范文来源**: Li, Bapuji, Talluri, Singh & Venkataraman (2026), *Production and Operations Management*（Figure 1：supply bases A and B 平均地理距离同为 d，但 A 集中、B 分散）

**骨架**:
```text
Although [dimension A] and [dimension B] are related, they capture different aspects of [umbrella].
[Dimension A] refers to [definition A]; [dimension B] represents [definition B].
As Figure [N] illustrates, [quantity of A] is the same for [unit set 1] and [unit set 2]
(both equal to [constant]). However, [units] are more [low on B] in [set 1] and more
[high on B] in [set 2]. As a result, the challenges of managing [set 1] differ from those
of managing [set 2]. Thus, theoretically distinguishing [A] and [B] and assessing their
empirical effects are important.
```

**原文锚定**:
> Although geographical distance and geographical dispersion are related, they capture different aspects of complexity. Geographical distance refers to the physical distance between the buyer firm and its direct suppliers (Bray et al., 2019); geographical dispersion represents the extent to which suppliers are spread across different areas (Lorentz et al., 2012). As Figure 1 illustrates, the average geographical distance between buyers and suppliers is the same for supply bases A and B (both equal to d). However, suppliers are more concentrated in supply base A and more dispersed in supply base B. As a result, the challenges of managing supply base A are different from those of managing supply base B.

**关键特征**:
- **几何最小对，不是 vignette 叙事**: 固定一个可测标量（平均距离 d），只变空间构型（集中 vs 分散）——实验设计逻辑移植到构念辨析图
- **证明可分离性先于机制**: 图的功能是"A 与 B 可独立变化"，不是直接推 H；机制分工放在后续小节
- **与 Intro 变体 D 接力**: Intro `tensions/05` 变体 D 立互换测量缺口；本模式在 Theory 用图兑现"概念上可分"

**为什么有效**: 读者对"相关但不同"的口头主张常存疑；同 d、异分散的图把可识别性一次钉死，后续 monitoring vs coordination 双轨才站得住。

**注意事项**:
- 图中被固定的量必须是维度 A 的**充分统计量**（如平均距离），被变化的必须是维度 B 的构型；若图同时动了供应商数量等第三变量，最小对失效
- 辨析段后必须接机制分工（见 `sibling_ivs_mechanism_division_shared_buffer`）；图 alone 不是贡献
- 单篇 EMERGING：未跨论文验证前不作 write-theory 默认路由

**反模式**:
- 用真实供应链地图堆砌例子却不控制平均距离——失去 minimal
- 把图写成装饰性"概念框架图"而不做 hold-constant 对比
- 与 Cutolo 语言最小对混用：本模式服务**构念可分**，彼模式服务**机制显形**

**与近邻区分**:
- vs `minimal_pair_contrast_vignette`（Cutolo）：语言/表征变量的两句并置；本模式是空间几何构型
- vs `table_construct_differentiation`：多维表格边界；本模式是二维几何证明可分离
- vs B2 / sibling dual-track：那些推机制与 H；本模式只完成 T1 可分证明

---

## 与相邻语料文件的关系

- [`../sentences/construct_definition.md`](../sentences/construct_definition.md)：微观句式模板（如 "We define X as..."）
- [`../subprotocols/argumentation_patterns.md`](argumentation_patterns.md)：微观动作组合（含语言版 minimal pair）
- [`../subprotocols/hypothesis_organization_patterns.md`](hypothesis_organization_patterns.md)：兄弟 IV 机制分工 + 共享缓冲（本模式之后的组织）
- [`../variants/A_construct_differentiation.md`](../variants/A_construct_differentiation.md)：构念辨析型整篇结构

> **使用顺序**：先查本文件确定 T1 辨析策略 → 再查 `construct_definition.md` 填充具体句式 → 再查 `argumentation_patterns.md` / `hypothesis_organization_patterns.md` 组织论证动作。
