---
type: canonical_reference
canonical_id: "04-public-health-safety"
status: ✓ STANDARD
gap_type: all
cross_paper: EMERGING
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - darby2023 (MSOM, 2023): "Fifteen injuries and one death prior to recall initiation"
  - ilicic_brennan2026 (JM, 2026): "economic burden + exposed population + annual deaths across addiction categories"
updated: 2026-08-03
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis + darby2023 distill
---

# 04-public-health-safety — 公共安全与健康 Stakes

## 功能定义

将研究问题连接到对公众健康、消费者安全或关键利益相关者的可感知伤害，使研究获得伦理 relevant 性和政策紧迫性。这种 stakes 特别适合涉及产品安全、质量失败、公共卫生、环境风险和监管响应的研究领域。

## 适用场景

- 研究涉及产品召回、医疗安全、食品安全、环境泄漏等可能造成人身伤害的领域
- 存在真实的或权威来源支持的伤害证据（FDA、WHO、CDC 数据）
- 目标期刊接受公共安全作为合法 stakes（MSOM、JOM、POM、JM、OS）
- 需要建立**伦理紧迫性**和**政策相关性**

---

## 句法模板

### 变体 A：具体伤害型（darby2023 型）

**模板**:
> "[Shocking human cost] — [number] [injuries / deaths / illnesses] are believed to have occurred [prior to / as a result of] [phenomenon]. [Second sentence: describe the vulnerable population and their dependence on the product/service]. [Third sentence: why this harm persists despite awareness or regulation]."

**来源**: darby2023 (MSOM), adapted

**原文锚定**:
> "Fifteen injuries and one death are believed to have occurred prior to recall initiation."
> "Unfortunately, despite the potential human costs, such examples of recall delays are all too common in the medical device industry. Patients, physicians, and regulators are left wondering why this is and what can be done to shift this paradigm."

**关键特征**:
- 以精确数字开场建立真实伤害感
- "despite the potential human costs" → 强调伤害本可避免
- 让脆弱人群变得具体可感

---

### 变体 B：风险递进型

**模板**:
> "[At the individual level], [phenomenon] subjects [vulnerable population] to [extended / prolonged] [safety / health / reliability] risks. [At the societal level], delays in [action] increase the likelihood that [escalating harm] will occur. [Third sentence: the scale of exposure — how many people or communities are affected]."

---

### 变体 C：监管-现实差距型

**模板**:
> "Although [regulatory body] establishes guidelines for [action], they rely upon [actors] to actually initiate [response]. [Second sentence: the gap between regulation and reality — delays of weeks, months, or even years]. [Third sentence: the human cost of this implementation gap]."

---

### 变体 D：成本—暴露—死亡三联量化型（ilicic_brennan2026 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "[Harmful domain] burdens [families/communities/systems], generating more than [annual economic cost] in [country]. [Focal subtype] affects approximately [population count and share], while [broader harm category] contributes to [annual mortality or morbidity] worldwide. These burdens make it important to understand [behavioral or institutional driver] and identify [intervention target]."

**来源**: Ilicic & Brennan (2026, *Journal of Marketing*), Introduction P1.

**关键特征**:
- 三个数字各承担不同功能：成本说明制度负担，人数/占比说明暴露面，死亡数说明后果严重性。
- 数字之后立即连接可解释的行为驱动与可干预目标，避免将公共健康统计写成装饰。
- 可与政治、文化或市场分群变量相接，但不得把群体平均差异写成个体诊断或污名化标签。

**诚实边界**:
- 三类数字必须口径兼容并有权威来源；“成瘾相关成本”和“某一成瘾类型人数”不能被误写成同一总体。
- 公共健康 stakes 证明问题重要，不证明本文自变量是这些损失的主要原因。
- 数字较多时不要再叠加同功能的 `02-quantified-economic-loss`，以免首段变成统计清单。

---

## 关键技巧：脆弱性的具象化

最有效的公共安全 stakes 不是笼统地说"影响消费者"，而是**让脆弱人群变得具体可感**：

| 弱表达 | 强表达 |
|--------|--------|
| "delays harm patients" | "subjecting heart patients to extended product safety and reliability risks" |
| "recalls affect consumers" | "individuals who depend upon the ICD for life-sustaining therapy" |
| "defective products are dangerous" | "a defective heart rate monitor used in a surgical ward that may inaccurately signal cardiac arrest" |

**双重 Stakes 策略**：
公共安全 stakes 可以与组织/财务 stakes 同时出现，形成双重紧迫性：
> "Recalling too slowly can put patients at prolonged risk and threaten the firm's reputation, whereas recalling too quickly can result in excessive costs or errors."

**严重等级分层**：
当研究领域存在梯度差异时，用分类框架（如 FDA Class I/II/III）来展示伤害的层次性：
> "Class I and Class II recalls involve severe defects; they can cause temporary illness, serious injury, or death. In contrast, Class III recalls involve low-severity defects..."

---

## 组装规则

### 必须配对
- **与 `07-cost-benefit-tension` (Hook) 或 `02-epigraph-quote-pivot` (Hook) 配对**: 公共安全 stakes 常与实践困境或新闻个案 hook 连用
- **与 `01-despite-progress-unaddressed` (Tension) 配对**: 尽管已有监管框架，但执行层面的缺口导致伤害持续

### 反模式提醒
- **伤害无来源**: 给出具体数字或引用权威来源（FDA, WHO, CDC）
- **伤害与研究脱节**: 必须连接到理论缺口："These losses persist because [mechanism] is poorly understood"
- **过度情感渲染**: 保持分析性距离，用"subjected to prolonged risks"或"exposed to safety hazards"
- **单一维度 stakes**: 产品召回类论文适合展示"公共安全 vs 组织利益"的张力

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| MSOM | ⭐⭐⭐⭐⭐ | 运营/供应链期刊高度认可公共安全 stakes |
| JOM | ⭐⭐⭐⭐⭐ | 产品安全、质量治理研究的经典 stakes |
| POM | ⭐⭐⭐⭐☆ | 可用，但需更快进入运营机制 |
| JM | ⭐⭐⭐☆☆ | 消费者福祉研究可用；需衔接营销理论 |
| OS | ⭐⭐⭐⭐☆ | 制度失灵、监管缺口研究适合 |

---

## 相关语料

- 配合 `hooks/10-practical-puzzle.md` 使用："为什么企业明知产品有问题却迟迟不召回？"
- 配合 `hooks/03-data-shock.md` 使用：伤亡数字可作为数据冲击开场的核心组成部分
- 配合 `tensions/04-reality-contradicts-consensus.md` 使用：监管框架存在但执行失败
