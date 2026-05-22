---
category: because-clauses
description: because 从句架构——控制变量理由、样本排除逻辑、构念效度论证的核心句法单元。
function: 抗辩性/对齐性——每个 because 从句完成一个微型论证
slots: M2, M3, M4, M6, M7, M8
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# because 从句架构（Because Clauses）

## 设计原则

because 从句是 Methods 中**最密集的说服单元**。一个 because 从句的质量决定了审稿人是否会追问 "why this control?" 或 "why this measure?"。

## 六大 because 类型

### 1. 竞争性解释型（Rival Explanation）

**功能**：论证控制变量排除的是哪一个替代理论或遗漏变量威胁。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `...because [larger and older firms] may have more resources for both [IV] and [DV].` | 安全 | M6 |
| `...because [rival theory] predicts that [alternative mechanism] drives [outcome].` | 安全 | M6 |
| `...because [omitted variable] may confound the [IV-DV] relationship by [mechanism].` | 安全 | M6 |
| `...because [actor] may be sensitive to [outcome] ([citation]), so it is important to control for [related_factor].` | 安全 | M6 |
| `...because [time-varying shocks] may simultaneously affect [IV] and [DV].` | 安全 | M6 |

**关键区分**：
- 弱：`...because [variable] is important.`（没有说明威胁什么）
- 强：`...because [variable] may confound [IV-DV] by [mechanism].`（明确的 omitted variable 逻辑）

### 2. 构念效度型（Construct Validity）

**功能**：论证测量捕捉了理论构念。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `This measure captures [construct] because [construct-validity logic].` | 安全 | M3, M4 |
| `The measure captures [construct] because [theoretical link between text feature and underlying construct].` | 安全 | 文本构念 |
| `We chose this source because [theoretical reason for text reflecting construct].` | 安全 | 文本构念 |
| `This variable corresponds to Hypothesis [x] because it captures [mechanism].` | 安全 | M4 |
| `Following extant research ([citation]), we used [measure] as our primary measure because it broadly reflects [N] mechanisms: [mechanism_list].` | 安全 | M4 |

### 3. 样本排除型（Sample Exclusion）

**功能**：为每一步样本损失提供理由。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We excluded [cases] because [comparability/measurement/identification reason].` | 安全 | M2 |
| `We also excluded firms with fewer than [three] years of consecutive data to ensure sufficient within-firm variation for fixed-effects estimation.` | 安全 | M2 |
| `Because testing [moderation/mechanism] requires [additional source], the sample for H[x] is restricted to [available period/units].` | 安全 | M2 |
| `Because [outcome] is rare, a simple random sample would yield too few [cases]; we therefore used [sampling strategy].` | 安全 | M2 |

### 4. 机制解释型（Mechanism Linkage）

**功能**：在变量操作化段落中，连接构念→测量→理论机制。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `...because it captures [mechanism], which links [IV] to [DV] through [process].` | 安全 | M4 |
| `...because [theoretical_rationale], and research indicates that [IV] is one of the most effective tools to do so ([citation]).` | 安全 | M4 |
| `...because [measure] proxies for [mechanism_A] through [rationale] ([citation]).` | 安全 | M4, M5 |
| `The results suggest that the effect of [IV] is driven by the within-component rather than the between-component. That is, it is not..., but, rather, a relative increase...` | 安全 | M5 |

### 5. 估计器选择型（Estimator Justification）

**功能**：论证为什么选这个估计器而不是替代方案。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `Because [DV] is [continuous/binary/ordinal/count/censored/time-to-event], we use [model].` | 安全 | M7 |
| `We employ [unit] fixed effects rather than random effects because the Hausman test rejects...` | 安全 | M7 |
| `Because [DV] is persistent and our panel is short, fixed-effects estimation may be biased (Nickell bias). We therefore estimate...` | 安全 | M7 |
| `Because the shape of [event timing] is not known ex ante, we compare [distributions] and select [distribution] based on [fit criterion].` | 安全 | M7 |
| `Coefficients indicate direction, but substantive interpretation requires [marginal effects/predicted probabilities/hazard ratios].` | 安全 | M7 |

### 6. 识别策略型（Identification Defense）

**功能**：在识别策略段落中，论证为什么威胁不严重或已被处理。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Shock/event] creates variation in [treatment] that is plausibly exogenous to [outcome] because [reason].` | 安全 | M8 |
| `It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor].` | 安全 | M8 |
| `Although [assumption] cannot be directly tested, the evidence below helps reduce concerns about [threat].` | 安全 | M8 |
| `Because [network-based construct] may capture common shocks rather than true peer influence, we conduct falsification tests.` | 安全 | M8 |

---

## because 密度标杆

| 密度等级 | M6 because 覆盖率 | MVP30 顶刊表现 |
|---------|-------------------|----------------|
| 优秀 | >= 60% | Darby2026 JOM (~85%) |
| 良好 | 40–59% | SMJ/JM/ASQ 多数 |
| 及格 | 30–39% | MVP30 中位数 (~35%) |
| 需关注 | < 30% | AMJ 约 30% 可低至 0% |

**目标**：每个控制变量、每个样本排除步骤、每个关键测量都应有 because 从句。

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We control for Size, Age, and ROA.` | 无 because 逻辑 | `We control for firm size because larger firms have more resources for both [IV] and [DV].` |
| `We excluded missing values.` | 无排除理由 | `We excluded observations with missing [variable] because [reason for missingness threatening validity].` |
| `This measure is good because it is reliable.` | 循环论证 | `This measure captures [construct] because [theoretical link], validated by [external benchmark].` |
| `Because the data say so.` | 无理论机制 | `Because [theory] predicts that [mechanism] links [IV] to [DV].` |
