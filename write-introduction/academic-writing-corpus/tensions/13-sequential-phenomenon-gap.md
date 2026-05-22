---
type: canonical_tension
canonical_id: "13-sequential-phenomenon-gap"
status: VERIFIED
gap_type: Incompleteness
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: HIGH
source_papers:
  - haunschild2015 (OS, 2015): "learning theory has not dealt with in a systematic way... we have good theory about A and good theory about B, but know little about sequential cycling"
created: 2026-05-19
source: Distilled from Haunschild, Polidoro & Chandler (2015), Organization Science
---

# 13-sequential-phenomenon-gap — 分割文献的盲区 / Sequential Phenomenon Gap

## 功能描述

Incompleteness 问题化的高阶 Tension：不是简单地指出"没人研究过 X"，而是指出**两个（或多个）成熟理论领域之间缺乏连接**——"我们有很好的 A 理论，也有很好的 B 理论，但不知道 A 和 B 如何 sequentially 关联"。这是比 "few studies have examined" 更高级的 Incompleteness 表达，适用于 Mechanism 贡献。

## 适用场景

- Gap 类型 = **Incompleteness**
- Contribution 维度 = **Mechanism** / **Constructs**
- 研究涉及两个（或多个）已被充分研究的构念/过程，但它们之间的**时间/因果顺序关系**未被理论化
- 常见于：学习-遗忘、探索-利用、创新-标准化、适应-惯性等成对概念
- 目标期刊: OS, ASQ, AMJ, SMJ

## 验证状态

### 跨论文复现
- **VERIFIED** (1 paper, distinctive): haunschild2015 (OS)
- **可迁移性验证**: 骨架中的 `[phenomenon A]` 和 `[phenomenon B]` 可替换为任何成对理论概念（exploration-exploitation, efficiency-flexibility, centralization-decentralization），逻辑保持完整

### 生成力
- **GENERATIVE**: "Although we have good theory about A and good theory about B, we know little about why they might exhibit both tendencies in succession" 模板高度可迁移

### 排他性
- **HIGH**: 标志性语言（"has not dealt with in a systematic way", "we have good theory about... but know little about"）几乎只在 Incompleteness 中出现

---

## 句法模板

### 变体 A：两段式递进型（haunschild2015 型）

**P1 — 初步解释 → 否定现有理论系统性**:
> "We believe that an important reason was [phenomenon A], followed by [phenomenon B]. Although intuitive, this is a sequential phenomenon that [field] theory has not dealt with in a systematic way. In spite of providing many insights into the factors that facilitate or inhibit [phenomenon A] (e.g., [citations]), existing theory is less clear about how [phenomenon A] and [phenomenon B] relate to each other, and also how they might combine to create [undesired outcome]."

**P2 — 精确 Gap 声明**:
> "That is, although we have good theory about [actors] [phenomenon A] and good theory about [actors] [phenomenon B], we know little about why they might exhibit both tendencies in succession and how such cycles might be repeated."

**来源**: haunschild2015 (OS), P3

**原文锚定**:
> "We believe that an important reason was NASA's ability to learn, followed by its tendency to forget. Although intuitive, this is a sequential phenomenon that learning theory has not dealt with in a systematic way. In spite of providing many insights into the factors that facilitate or inhibit organizational learning (e.g., Argote 2011, 2013), existing theory is less clear about how learning and forgetting relate to each other, and also how they might combine to create serial errors. That is, although we have good theory about organizations learning and good theory about organizations forgetting, we know little about why they might exhibit both tendencies in succession and how such cycles might be repeated."

**关键特征**:
- "Although intuitive" → 承认现象看起来简单，但理论处理不足（降低读者防御）
- "has not dealt with in a systematic way" → Incompleteness 的**高阶表达**：不是"没人研究"，而是"没有系统处理"
- "existing theory is less clear about how... relate to each other" → 指出两个理论领域之间的**连接缺失**
- "we have good theory about... and good theory about..., but know little about..." → **对称结构**强调两个领域的成熟度，反衬缺口的意外性
- 零次使用 "few studies have examined"

---

## 关键功能短语

| 短语 | 功能 | 适用 Gap |
|------|------|---------|
| "has not dealt with in a systematic way" | 指出理论处理不足（非空白） | Incompleteness |
| "existing theory is less clear about how... relate to each other" | 两个领域间连接缺失 | Incompleteness |
| "we have good theory about... and good theory about..., but know little about..." | 成熟领域 + 意外缺口 | Incompleteness |
| "exhibit both tendencies in succession" | 强调 sequential/cyclical 特性 | Incompleteness (Mechanism) |

---

## 组装规则

### 必须配对
- **与 `14-paired-disasters` (Hook) 配对**: 当 Hook 使用极端案例叙事时，sequential phenomenon gap 将具体案例转化为一般性理论缺口
- **与 `05-maxim-contrast` (Theory Lens) 配对**: Mechanism 贡献需要资源约束/竞争机制来解释 sequential cycling

### 互斥
- **不能与 `02-implicit-assumption-wrong` (Tension) 同用**: 本品承认已有进展（Incompleteness），前者挑战隐性假设（Inadequacy）
- **不能与 `04-reality-contradicts-consensus` (Tension) 同用**: 前者是 Incommensurability 逻辑，本品是 Incompleteness 逻辑
- **不能使用 Inadequacy 措辞**: 如 "fundamentally flawed", "overlooks", "conflated" 等会破坏 Incompleteness 的渐进式对话策略

---

## 反模式提醒

- **弱缺口**: 必须解释为什么 sequential phenomenon 是**理论重要**的。Haunschild 用 "how they might combine to create serial errors" 解释——不是"没人做"，而是"不做会导致连环错误"
- **不展示已有文献**: 必须先承认"文献对 A 和 B 分别做了什么"，才能说"但缺少 A→B 的连接"。直接跳到缺口会显得稻草人
- **滥用 "good theory"**: 只有在 A 和 B 确实各自有成熟理论支撑时才能使用。若 B 是空白领域，使用此骨架会造成虚假成熟感

---

## 与 generic gap 的区别

| | Generic gap | Sequential phenomenon gap |
|---|------------|--------------------------|
| 标志性语言 | "few studies have examined" | "has not dealt with in a systematic way" |
| 对已有文献态度 | 忽视/贬低 | 承认 + 尊重 |
| Gap 类型 | Incompleteness (基础) | Incompleteness (高阶) |
| 读者感受 | "又一个人来填空白" | "有趣，两个成熟领域居然没连接" |
| 适用贡献 | 任何 | Mechanism / Constructs |

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| OS | ⭐⭐⭐ 极高 | OS 偏好组织过程/学习研究，完美适配 |
| ASQ | ⭐⭐⭐ 高 | ASQ 需要更强的理论缺口，但本品可通过"how they might combine"升级 |
| AMJ | ⭐⭐⭐ 高 | 适用于心理/行为层面的成对构念（如 approach-avoidance） |
| SMJ | ⭐⭐⭐ 高 | 适用于战略层面的成对张力（如 exploration-exploitation） |
| JM/JMR | ⭐⭐ 中 | 需更强调管理/消费者行为含义 |