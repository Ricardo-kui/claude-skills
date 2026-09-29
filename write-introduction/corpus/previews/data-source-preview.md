---
type: canonical_reference
canonical_id: "data-source-preview"
status: ✓ STANDARD
function: "Preview 子模块：构念映射数据源枚举型数据预告段——多数据库拼接的实证论文在 Introduction 内逐一声明每个构念的数据来源并以面板规格收束，交付测量可信度而不进入识别策略辩护。"
generativity: ADAPTABLE
exclusivity: LOW
created: 2026-09-29
source: "corpus_writeback.py create_new_file（gate ① 裁决新建模块）"
---

# data-source-preview — Preview 子模块：构念映射数据源枚举型数据预告段——多数据库拼接的实证论文在 Introduction 内逐一声明每个构念的数据来源并以面板规格收束，交付测量可信度而不进入识别策略辩护。

## 功能描述
Preview 子模块：构念映射数据源枚举型数据预告段——多数据库拼接的实证论文在 Introduction 内逐一声明每个构念的数据来源并以面板规格收束，交付测量可信度而不进入识别策略辩护。


## 组装规则
### 互斥

- 每个构念都必须有可对应来源，禁止出现无来源构念；不在本段辩护识别策略（robustness-preview 的职能）；来源列举顺序与 Theory 构念出场顺序一致


## 适用场景
- 多数据库拼接的 JAMS/JM 风格实证论文；构念来自异质数据源（监管数据库+游说记录+高管特征+财报）需逐一交代的研究；与机制预告段+发现预告段构成三段式 Preview


## 验证状态
### 单源验证
- 变体 A：构念映射数据源枚举型——(for construct) 逐源括号映射+面板规格三要素收束（giannetti_2022_corporate_lobbying_and_product_recalls_an_inv，EMERGING）
- 待第二篇跨论文复现后升 ROBUST


## 句法模板
### 变体 A：构念映射数据源枚举型（giannetti2022 型）

> 论证角色：Evidence（逐一声明每个构念的数据来源与最终面板规格，在预告层交付测量可信度）

**模板**:
> "To test the proposed [model type] ([method anchor citations]), we collect data from [source 1] (for [construct 1]), [source 2] (for [construct 2]), ..., and [source N] (for [construct N]). The final sample consists of [panel type] of [N] [units] ([N observations]) between [year] and [year]."

**来源**: giannetti_2022_corporate_lobbying_and_product_recalls_an_inv (JAMS), P6

**原文锚定**:
> "we collect data from the U.S. FDA Medical Device Product Recalls database (for product recalls), opensecrets.org (for corporate lobbying), BoardEx (for CEOs' functional backgrounds), ExecuComp (for CEOs' characteristics), and firms' 10-Ks (for quality certifications)."
> "The final sample consists of an unbalanced panel of 86 U.S. medical device firms (696 firm-years) between 2005 and 2018."

**关键特征**:
- 每个数据源后跟 "(for [construct])" 括号映射，构念—测量来源一一对应，提前化解测量效度疑问
- 段首以模型类型标签+方法锚引用开场（"the proposed second-stage moderated mediation model (see e.g., ...)"），承接机制预告段的方法承诺
- 收束句交付面板规格三要素：单位数、观测数、时间窗
- 数据预告独立成段，不与发现预告合并（区别于 findings-preview 变体 J/M 的一句带过）

**适用**: 多数据库拼接的 JAMS/JM 风格实证论文；构念来自异质数据源（监管数据库+游说记录+高管特征+财报）需逐一交代的研究；与机制预告段+发现预告段构成三段式 Preview

**禁忌**: 每个构念都必须有可对应来源，禁止出现无来源构念；不在本段辩护识别策略（robustness-preview 的职能）；来源列举顺序与 Theory 构念出场顺序一致

<!-- wb:giannetti_2022_corporate_lobbying_and_product_recalls_an_inv:intro_datapreview_new_module -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
