---
type: canonical_reference
canonical_id: "12-setting-justification"
status: ✓ STANDARD
gap_type: all
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: LOW
source_papers:
  - wowak2025 (MS, 2025): "Medical products as high-risk, high-reward industry"
  - pollock2015 (ASQ, 2015): "VC industry ideal setting for several reasons — each maps to a theoretical requirement"
  - kalaignanam_kushwaha_eilert2013 (JM, 2013): "经济量级(3% GDP, 1/7 jobs) + 现象丰富度(bevy of recalls→longitudinal) + 外部审视 → 'single industry enhances internal validity' 方法论收束"
  - li_bapuji_talluri_singh_narayanan_2026_jscm (JSCM, 2026): "召回频发 + 长期依赖/关系可见 + 样本 OEM 市占 → US 汽车业 event study"
created: 2026-05-20
updated: 2026-08-06
source: Extracted from wowak2025 MS Introduction distillation
---

# 12-setting-justification — 行业/情境选择论证

## 功能描述

在 Introduction 中论证为什么选择特定的行业/情境来检验研究问题。不是简单描述 setting，而是展示**该情境的理论相关性**——为什么这个特殊的行业/情境能使理论机制最清晰地展现。

## 适用场景

- 单一行业设计的研究
- 需要在 Introduction 中说服读者 "为什么是医疗设备而非汽车？"
- 研究涉及行业特有的风险-回报结构或监管环境
- 理论预测在该行业中特别鲜明/可检验

## 句法模板

### 变体 A：High-Risk, High-Reward 型（wowak2025 型）

**模板**:
> "[Industry] present an ideal setting for examining [relationship] because it is a high-risk, high-reward industry. It is high-risk because [severe_consequences] ([citation]). However, it also offers high rewards for companies in the form of [economic_benefits], reaching as high as [quantified_benefit] on certain [products] ([citations]). With this risk-reward profile, the [industry] can have considerable [stakeholder_1] and [stakeholder_2] consequences.
>
> Interestingly, [theory_literature] indicates that [group_A] and [group_B] tend to prioritize [stakeholder_1] and [stakeholder_2] consequences quite differently. Whereas [group_A] typically emphasize [value_1] over [value_2] ([citation]), the opposite is true for [group_B] ([citation]). This prioritization juxtaposition may contribute to [prediction_divergence], leading us to the following research question: [RQ]?"

**来源**: wowak2025 (MS), P3

**原文锚定**:
> "Medical products, or more specifically pharmaceutical drugs and medical devices, present an ideal setting for examining the relationship between TMT political ideology and product recalls, as it is a high-risk, high-reward industry. It is high-risk because serious medical product defects can severely harm or even kill consumers. However, it also offers high rewards for companies in the form of substantial profit margins, reaching as high as 90% gross margin on certain medical products. With this risk-reward profile, the medical products sector can have considerable social and economic consequences. Interestingly, the political ideology literature indicates that liberals and conservatives tend to prioritize social and economic consequences quite differently. Whereas liberals typically emphasize social welfare over economic returns, the opposite is true for conservatives. This prioritization juxtaposition may contribute to more liberal TMTs approaching product quality decisions differently than more conservative TMTs, leading us to the following research question: ..."

**关键特征**:
- **"ideal setting"** → 明确声明行业选择的理论合理性
- **双面性论证**: high-risk (消费者伤亡) + high-reward (90% gross margin) → 张力最大化
- **量化好处**: "reaching as high as 90% gross margin" — 具体数字比 "high profits" 更有说服力
- **理论→行业**: 行业双面性 → 理论预测分化 → RQ — 完整的因果论证链
- **禁忌**: 不要只说 "X is an ideal setting because it's important"; 必须展示行业特性**如何使理论机制可观察**

## 组装规则

### 必须配对
- 与 **Theory Lens** 紧邻：Setting Justification 后应立即展示理论预测如何在行业中分化
- 与 **RQ** 紧邻：Setting+Theory 论证链的终点是 RQ

### 反模式提醒
- **不要用数据规模替代理论论证**: "X industry is worth $Y billion" 不是好的 setting justification
- **不要在 Methods 中才解释行业选择**: Introduction 中的 setting justification 是说服读者 "本文值得读" 的关键
- **不要忽视行业的负面特征**: high-risk 和 high-reward 同样重要

---

### 变体 B：多理由理论要求映射型（pollock2015 型）

**模板**:
> "[Setting] is an ideal setting for examining [theoretical relationship/issues] for several reasons. First, [theoretical requirement 1 of the study] is present: [setting-specific property] ([citation]). Second, [theoretical requirement 2]: [setting-specific feature that makes the mechanism observable/trackable over time] ([citations]). Finally, [theoretical requirement 3 / structural alignment]: [setting's structural property that mirrors the theoretical phenomenon] ([citations])."

**来源**: pollock2015 (ASQ), P5

**原文锚定**:
> "The VC industry is an ideal setting for examining these issues for several reasons. First, reputation has both symbolic and substantive benefits for the firms that VCs fund (Lee, Pollock, and Jin, 2011). Second, the extensive webs of interorganizational relations constructed through investment syndicates exert significant influence on VC firms' functioning and behavior (Hochberg, Ljungqvist, and Lu, 2007; Milanov and Shepherd, 2013) and make studying how the relationships evolve over time possible (Fund et al., 2008). Finally, the VC industry is bound together by an implicit coevolutionary network: start-ups depend on VCs for capital and other resources, VCs require access to promising start-ups that can provide investment returns that allow them to raise more and larger funds, and investors depend on VCs to identify and develop start-ups to help them grow their investment portfolios."

**关键特征**:
- **"ideal setting for examining [issues] for several reasons"**: 显式预告 + 枚举结构（与变体 A 的 "high-risk, high-reward" 双面性张力论证不同，本变体是 N 个理由的*平行可行性*枚举）
- **每个理由映射一个理论要求**——行业选择不是因"重要"而是因"理论机制在此最清晰可检验":
  - 理由 1 = 构念在该情境有意义（symbolic + substantive benefits 都存在）
  - 理由 2 = 关系随时间可观测（syndicate networks 使 longitudinal study 成为可能）
  - 理由 3 = 情境结构镜像理论现象（implicit coevolutionary network）
- **理由 3 用嵌套三角关系具象化**: start-ups↔VCs↔investors 的三角互依*直接镜像* "coevolution" 概念——行业结构本身就是理论现象的化身（structural isomorphism）
- **与变体 A 的区别**: 变体 A（wowak2025）是"行业双面性 → 理论预测分化"的*张力*论证；本变体是"行业特性 → 理论可检验性"的*可行性*论证

**适用**:
- 单一行业面板 / 网络研究，行业选择需论证理论相关性（而非数据便利）
- 研究涉及可观测的关系网络或随时间演化的过程
- 行业结构与理论构念存在结构同构（structural isomorphism）时尤其有力

**禁忌**:
- 不要用数据规模替代理论论证（"VC industry is worth $X" 不是理由）
- 每个理由必须明确连接到本研究的一个*理论要求*，而非泛泛列举行业特点
- 理由数（通常 ≤3）应来自不同维度（构念相关性 / 可观测性 / 结构同构），避免重复；>3 个理由读者会失去耐心

---

### 变体 C：经济重要性 + 现象丰富度 + 内部效度收束型（kalaignanam2013 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "We chose the [industry] as our empirical context because this sector is of considerable economic significance. For example, the [industry] represents more than [X]% of the [country] gross domestic product and accounts for one in [Y] jobs in the [domestic economy] ([citation]). Importantly, the [industry] has witnessed a bevy of [phenomenon], which allows us to longitudinally examine their impact on [outcomes]. Furthermore, analysts and regulators have closely scrutinized this industry. In summary, by focusing on a single industry, we are able to enhance the internal validity of the study and provide actionable insights into an important and crucial sector of the [country] economy."

**来源**: kalaignanam_kushwaha_eilert2013 (JM), P6

**原文锚定**:
> "We chose the automobile industry as our empirical context because this sector is of considerable economic significance. For example, the automobile business represents more than 3% of the U.S. gross domestic product and accounts for one in seven jobs in the U.S. domestic economy (Pauwels et al. 2004). Importantly, the automobile industry has witnessed a bevy of product recalls, which allows us to longitudinally examine their impact on reliability and market accidents. Furthermore, analysts and regulators have closely scrutinized this industry. In summary, by focusing on a single industry, we are able to enhance the internal validity of the study and provide actionable insights into an important and crucial sector of the U.S. economy."

**关键特征**:
- **三重理由递进**：经济量级（3% GDP, 1 in 7 jobs——量化宏观重要性）→ 现象丰富度（"bevy of recalls" 使 longitudinal 检验可行——方法论可行性）→ 外部审视（analysts/regulators closely scrutinized——隐含数据可得性与议题公共性）
- **"In summary, ... internal validity" 方法论自觉收束**：显式声明单行业设计是**主动选择**而非数据局限——"enhance the internal validity" 把潜在的外部效度弱点重构为方法论优势。这是变体 A/B 都没有的 trade-off 自觉
- **"actionable insights" 实践相关性标记**：JM 风格——setting justification 不仅说服审稿人"可检验"，也说服实践界"值得读"
- **与变体 A（wowak2025）的区别**：变体 A 用行业双面性（high-risk/high-reward）制造**理论预测张力**；本变体用行业特性论证**研究可行性与方法论严谨性**——引擎是 internal validity 而非 tension
- **与变体 B（pollock2015）的区别**：变体 B 的每个理由映射一个**理论要求**（构念相关性/可观测性/结构同构）；本变体的理由映射**研究设计的实际约束**（经济重要性→议题相关性；现象丰富度→统计功效；外部审视→数据可得性）

**适用**: 单行业面板研究；行业有公认的宏观经济量级（GDP 占比/就业占比可引）；现象在该行业频发（足以支撑纵向设计）；需预防"为什么不做跨行业"的审稿质疑——用 internal validity 收束主动化解

**禁忌**:
- 经济量级数据必须真实可引（Pauwels et al. 2004），不可约估——"more than 3% of GDP" 的精度是说服力来源
- "bevy of [phenomenon]" 必须与后续样本量匹配——若实际只有个位数事件，此论证失效
- "internal validity" 收束不能掩盖真实的外部效度关切——Discussion 仍需 Limitations 段讨论 generalizability
- 外部审视理由（analysts/regulators scrutinized）只在确实因此产生高质量数据时使用；若数据主要来自自愿披露，此理由不成立

---

### 变体 D：召回频发 + 关系依赖可见型（li_narayanan_2026_jscm 型）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**模板**:
> "This study tested the hypotheses using [phenomenon] and [network] data from the [country] [industry]. It focused on the [industry] for two reasons. First, [negative events] are common in the [industry] and have become a serious concern to its stakeholders ([citation]). Second, compared with other industries, [upstream actors] build long-term relationships with [downstream actors] and have a higher dependency on them. As a result, [relationship information] is more visible to [market audience]. Together, these firms serve [X]% of the entire [product market] in [country] ([citation])."

**来源**: li_bapuji_talluri_singh_narayanan_2026_jscm (JSCM), §3.1

**原文锚定**:
> "This study tested the hypotheses using product recall and supply network data from the US automobile industry. It focused on the automobile industry for two reasons. First, product recalls are common in the automobile industry and have become a serious concern to its stakeholders (Astvansh et al., 2022). Second, compared with other industries, suppliers build long-term relationships with automakers and have a higher dependency on them. As a result, buyer-supplier relationship information is more visible to investors."

**关键特征**:
- **双理由结构（非 WEIRD 泛化）**：现象频发 + 关系结构使溢出可观察——第二理由把**设计优势**锚定在 investor visibility，不是 GDP 量级
- **市占率一句收束**：66.92% 乘客车市占证明样本代表性，可与 Methods 七库合并段衔接
- **常位于 Methods §3.1 或 Intro→Methods 过渡**：与 event study 设计天然配对

**适用**: 单一行业 event study + dyad 面板；buyer–supplier 关系对投资者可观察；召回/危机溢出类研究；JSCM/JOM/MSOM

**禁忌**:
- 第二理由必须解释为何**该行业**比跨行业混合更能识别 vertical spillover——不能只说 "recalls are common"
- 市占统计须可引第三方（MarkLines 等），不可自估
- 若研究目的是 WEIRD 泛化检验，用 `tensions/18` + POM 型 setting 变体，不用本变体

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| MS | ⭐⭐⭐⭐⭐ | MS 鼓励详细的行业论证 |
| MSOM | ⭐⭐⭐⭐⭐ | 运营期刊偏好行业特性论证 |
| JOM | ⭐⭐⭐⭐☆ | 产品安全/召回研究的标准做法 |
| SMJ | ⭐⭐⭐⭐☆ | 需强调 strategic importance |
| JM/JMR | ⭐⭐⭐☆☆ | 需更早进入消费者/市场维度 |
