---
design_type: "结构需求-state-space"
status: 🟢 EMERGING
source_papers:
  - liu_shankar2015 (Management Science): BLP random-coefficient demand + Kalman-filter state-space for latent brand preference/advertising effectiveness/recall response; GMM; product-harm crises in U.S. auto
variants_count: 6
created: 2026-08-05
updated: 2026-08-05
---
# 结构需求-state-space — Methods 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M3 | 1 | 变体 1 |
| M7 | 2 | 变体 2、3 |
| M8 | 3 | 变体 4、5、6 |

### M3（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 约化式预备分析 → 结构模型动机桥（副槽位 M7） | "先 log-linear 探路、再 structural 正式估计"的设计，需把预备分析写成数据模式证明 + 结构模型必要性双步时 | — | 待交叉 | Liu & Shankar 2015 Management Science |

### M7（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 三层动态架构 — 品牌偏好累积 + 时变系数 transfer function + 事件特异 random walk | BLP/Kalman 设计需在同一段完成"偏好 stock→direct/indirect 通道→事件异质性→嵌入离散选择"架构导航时 | 首个在同一 M7 段完成三层架构导航的变体，避免只堆公式 | 待交叉 | Liu & Shankar 2015 Management Science |
| 3 | 估计栈 — contraction mapping + Kalman 转移/观测方程 + GMM | 需把 contraction→KF→GMM 三拍写成可读估计栈、并交代初始条件与归一化时 | 区别于 `动态面板-GMM` 的 moment conditions 叙述 | 待交叉 | Liu & Shankar 2015 Management Science |

### M8（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | 直接 vs 间接效应识别 — 约化式交互类比 | 结构式中 direct/indirect/spillover/特征调节四类识别逻辑需显式映射到预备回归交互时 | 区别于"黑箱结构"写法，识别逻辑与约化式交互一一对应降低不信任 | 待交叉 | Liu & Shankar 2015 Management Science |
| 5 | 监管强制召回外生性 — 法定披露窗口论证 | 强制召回情境（NHTSA/CPSC 法定披露窗口）需论证 recall 外生于管理裁量时 | 区别于 Hoffmann 裁量权子样本与 IV/DiD 识别，补强制召回 regulatory exogeneity 通道 | 待交叉 | Liu & Shankar 2015 Management Science |
| 6 | State-space 可观测等价排除 — 附录解析证明 + 模拟恢复 | 需排除 state-space 可观测等价系统、证明参数识别（构造等价系统→约束→文献先例→模拟）时 | 区别于 VARX 的 Granger 与 IV 的 exclusion restriction，是 state-space 专属识别论证 | 待交叉 | Liu & Shankar 2015 Management Science |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`。本设计类型覆盖 **BLP 类随机系数离散选择需求** 与 **Kalman filter state-space 潜变量动态** 的集成估计（contraction mapping → KF 恢复状态 → GMM）。

## 设计特征摘要

- **数据形态**: 面板（通常为 product/market × time，如 nameplate-month sales + marketing + shock events）
- **核心架构**: 观测方程（market share ↔ mean utility，BLP contraction）+ 转移方程（latent brand preference / time-varying coefficients 的 AR/transfer function）
- **估计栈**: Θ₁（消费者异质性）+ Θ₂（均值效用/状态参数）分步恢复；KF/Bayesian updating 生成 ξ̂；GMM 最小化二次型
- **识别**: 约化式 pattern-finding（可选 §Preliminary）→ 结构式 direct/indirect 效应分解；价格 BLP-IV；广告/媒体 control function
- **与 VARX-PVAR 边界**: 非 reduced-form Granger 系统，而是结构需求 + 潜状态；与 `动态面板-GMM` 边界：非 AB/system GMM 动态面板，而是非线性离散选择与状态空间集成
- **召回交叉验证**: 与生存分析/面板 OLS 召回语料互补——本类型处理 **需求侧动态品牌偏好与广告效力**，而非 time-to-recall 或 firm-year FE 约化式

## 累积变体

### 变体 1: M3/M7 约化式预备分析 → 结构模型动机桥（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: Although the preliminary analysis suggests that we indeed observe decreases in sales and advertising effectiveness during a product-harm crisis in the automobile industry, it does not capture the richness of the processes or mechanisms by which product recalls affect demand.

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M3 / M7

**骨架**:
> To identify basic patterns in the data before estimating the structural model, we estimate a simple [reduced-form specification: e.g., log sales as function of lagged advertising, own-shock, shock×advertising interactions, spillover shocks, and controls]. The results confirm [pattern_1: e.g., negative own-shock effect], [pattern_2: e.g., differential advertising-effect erosion across ad types], and [pattern_3: e.g., spillover to sibling products under the same parent brand]. We then extend the specification to allow [shock characteristics: media/severity/prior quality] to moderate consumer response; model comparison ([AIC/BIC]) favors the richer specification and the interaction terms are [direction/significance summary]. Although this preliminary analysis establishes that [phenomenon] is present in the data, it does not capture [dynamic mechanism: e.g., latent preference accumulation, long-run carryover, or time-varying coefficients]. We therefore develop a [state-space / structural demand] model in the next section that incorporates [list of mechanisms the reduced form cannot capture].

**与原骨架差异**: corpus 召回家族多从 survival/FE 直接进入主模型；本变体把 **§Preliminary Analysis** 写成可审计的"数据模式证明 + 结构模型必要性"双步——约化式只负责 establish patterns，结构式负责 mechanisms。关键过渡句："does not capture the richness of the processes" → "therefore we develop..."。

**诚实边界**: 约化式系数不可直接当作结构参数解读；若预备分析已用 IV/FE，结构模型须说明为何仍需要（异质性、动态状态、非线性份额映射）。

**适用**: BLP/Kalman/动态离散选择论文；任何"先 log-linear 探路、再 structural 正式估计"的营销/IO 设计。

---

### 变体 2: M7 三层动态架构 — 品牌偏好累积 + 时变系数 transfer function + 事件特异 random walk（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: Brand preference is an unobserved stock variable captured as a state space model based on Kalman filtering (KF). We then integrate this KF process with a random coefficient demand model based on BLP (1995).

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M7

**骨架**:
> Brand preference is modeled as an unobserved stock that evolves according to a [transfer-function / state-space] accumulation equation: [g_it = δ·g_{i,t−1} + q^A·ln(Ad_{t−1}+1) + q^R·ln(Shock_{t−1}+1) + spillover term + error]. This layer captures (1) carryover of preference damage via δ, (2) direct effects of [negative shock] and [positive marketing inputs], and (3) spillovers to [sibling units under the same parent]. Advertising effectiveness and consumer response to [shock] are not fixed parameters; they follow separate transfer functions [q^A_t = δ^A q^A_{t−1} + q^A_0 + λ^A·f(Shock_t) + ν^A] and [q^R_t = δ^R q^R_{t−1} + q^R_0 + λ^R·M_t + ν^R], where M_t is a vector of [event characteristics: media/severity/prior quality]. Event-specific moderation enters through [λ_t] modeled as a [random walk: λ_t = λ_{t−1} + ν^λ], allowing differential responses across events while keeping the baseline system parsimonious. The demand side integrates this Kalman-filter process with a [random-coefficient logit / BLP] choice model so that observed [market shares] map to mean utilities through [contraction mapping], linking latent states to consumer choice.

**与原骨架差异**: 首个把 **偏好 stock + 双通道时变系数 + 事件 random walk** 与 BLP 需求在同一 M7 段落完成架构导航的变体。叙述顺序：latent stock → direct/indirect channels → event heterogeneity → 嵌入离散选择——避免只堆公式不解释三层分工。

**诚实边界**: δ、random-walk λ 的识别依赖事件时间与份额变化的联合变异；短面板或事件稀疏时须报告模拟/附录 identification 或简化规格稳健性。

---

### 变体 3: M7 估计栈 — contraction mapping + Kalman 转移/观测方程 + GMM（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: By minimizing a quadratic form of these error terms, we obtain the model parameters with a GMM procedure similar to BLP (1995).

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M7

**骨架**:
> We recover two sets of parameters: (1) [Θ₁: consumer heterogeneity parameters — e.g., variance of random tastes] and (2) [Θ₂: mean-utility and state-equation parameters]. For a given Θ₁, we obtain mean utilities via [contraction mapping / BLP inversion] from observed [market shares]. Given Θ₂ and the recovered mean utilities, we use a [Kalman filter / Bayesian updating] process on the [transition equation: α_t = Γ_{t−1}·α_{t−1} + Υ + ε_v] and [observation equation: φ_t = Z·α_t + K_t + ξ_t] to recover unobserved states [brand preference, time-varying coefficients, event moderators] and the implied demand shocks ξ̂_t. We then estimate Θ₂ by minimizing a GMM objective in the quadratic form of ξ̂_t, following [BLP / Sriram et al. / Pancras et al.]. Initial conditions for [states at t=0] are set for parsimony [e.g., parent-brand-level initial preference with one base brand normalized to zero; mean-reverting initial values for q and λ], with [σ_ξ] and event-zero assumptions stated explicitly.

**与原骨架差异**: 把 BLP 文献中分散的 **contraction → KF → GMM** 三拍合成 Methods 可读栈，并强制交代 **初始条件与归一化**（base brand、无召回稳态均值）。区别于 `动态面板-GMM` 的 moment conditions 叙述。

**诚实边界**: "details available upon request" 不足以替代关键识别假设；至少须说明 ξ_t 矩条件所用工具/权重矩阵来源；初始条件强假设需在 limitation 承认。

---

### 变体 4: M8 直接 vs 间接效应识别 — 约化式交互类比（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: The identification of the direct and indirect effects (through advertising effectiveness) of product recall on preference is analogous to the identification of the main effect of product recall and the interaction effect of product recall and advertising in the simple regression model discussed in §3.

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M8

**骨架**:
> In our model, [shock] affects preference through both a direct channel [q^R·ln(Shock)] and an indirect channel operating via [time-varying advertising effectiveness λ^A·ln(Shock)]. Identification of these channels is analogous to distinguishing the main effect of [shock] from the [shock×advertising] interaction in the preliminary reduced-form regression. The direct effect is identified from [market share changes during events after controlling for advertising and observables]. The indirect effect is identified from differential [market share responses to advertising shocks] with versus without [event exposure], holding other factors constant. Time-varying moderation by [event characteristics] is identified from differential share movements across events with different [media/severity/prior quality], after controlling for levels of advertising and [shock intensity]. Spillover effects are identified from share changes on [non-focal siblings] when another [unit under the same parent] experiences [shock], controlling for own-unit exposure.

**与原骨架差异**: 结构式识别很少写"与预备回归的项一一对应"；本变体把 **direct/indirect/spillover/characteristic moderation** 四类识别逻辑显式映射到约化式交互，降低审稿人对"黑箱结构"的不信任。可迁移至任何 direct+mediated（经时变系数）动态结构。

**诚实边界**: 类比不等于等价——结构式还嵌入份额非线性与异质性；须声明模拟或附录证明不可观测等价系统被排除。

---

### 变体 5: M8 监管强制召回外生性 — 法定披露窗口论证（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: According to the National Traffic and Motor Vehicle Safety Act of 1966, an automaker has five business days to inform the NHTSA after it discovers a problem. Therefore, product recall is outside management control and is therefore treated as an exogenous variable in this study.

**验证状态**: EMERGING（单篇；与 Hoffmann 裁量权子样本形成对照）

**槽位**: M8

**骨架**:
> In [industry], manufacturers are legally required to notify [regulator] and consumers and execute a [recall/shutdown] when [safety defect threshold] is met. Under [statute name/year], an automaker has [N business days] to inform the regulator after discovering a problem; refusal triggers [enforcement action]. Therefore, [product recall] is largely outside short-run managerial discretion and is treated as exogenous in this study, distinct from settings where firms choose whether and when to recall under reputational or legal-liability trade-offs. We complement this institutional argument by showing [no significant effect of recall on aggregate product features / null reduced-form feature regressions], consistent with recalls affecting demand through information and preference rather than immediate product redesign.

**与原骨架差异**: 召回语料库现有 **裁量权边界**（Hoffmann 2024 推断二元结果）与 **IV/DiD 识别**；本变体补 **强制召回 regulatory exogeneity** 通道——适合 NHTSA/CPSC 强制召回情境。末句可选补特征不变性实证支撑。

**诚实边界**: 强制披露不等于召回时点/规模完全外生（firm 仍可能影响 remedial scope）；severity/media 仍可能内生——须配合 CF/IV（见 `两阶段模型` 变体7）。

---

### 变体 6: M8 State-space 可观测等价排除 — 附录解析证明 + 模拟恢复（1篇高价值）

**来源论文**: Liu & Shankar 2015 (Management Science)
**原始句锚点**: The mean utility parameters are identified if there exists no other system observationally equivalent to the one specified in Equations (11b) and (12b) (Harvey 1991, Bass et al. 2007).

**验证状态**: EMERGING（单篇；待第二篇交叉验证）

**槽位**: M8

**骨架**:
> Mean-utility parameters in the state-space system are identified if no observationally equivalent system reproduces the same forecasted [market shares] given observed [shares] and parameters ([Harvey 1991; Bass et al. 2007]). We construct a generic observationally equivalent transformation [α_{1t} = L·α_t] and show that identification requires [L = I] in our specification [details in Appendix]. This approach follows [Bass et al. 2007] for advertising state-space models. We further validate the estimation algorithm with [simulated data], recovering true parameters with [high accuracy / summary statistic]; simulation details are reported in [Appendix / upon request].

**与原骨架差异**: VARX 用 Granger；IV 用 exclusion restriction；本变体是 **state-space 专属的 observational-equivalence 排除**——Methods 只写四步：等价系统构造 → 约束 L=I → 文献先例 → 模拟恢复。避免在正文展开全长证明。

**诚实边界**: 单篇模拟不能替代多初始值/多规格稳健性；`upon request` 应改为附录可审计摘要；若 Z 矩阵秩不足，须报告不可识别参数组合。

## 反模式

- **只有方程无架构导航**: 堆 Eq.(7)–(12) 但不解释 direct/indirect/spillover 三层分工 → 审稿人视为 IO 黑箱。
- **预备分析与结构式脱节**: 约化式显著但不在 M7 声明"结构式额外捕捉什么" → 预备分析沦为冗余表格。
- **把 recall 外生当全局免罪**: 强制召回不能免除 media/advertising/price 内生性处理。
- **Kalman 初始条件静默**: 不报告 base-brand 归一化、$q_0/(1-\delta)$ 稳态假设 → 状态识别不可审计。

## 诚实边界（设计级）

- 本设计 **因果强度为结构/预测解释**，不宜写 "effect of recall on sales" 而不加 "structural/implied" 或 "model-based" 限定，除非配合明确识别段落。
- BLP 份额数据 + 少量时期 → 初始条件与归一化假设对结果敏感；须在 limitation 讨论。
- 与 `product_recall_cross_validation` 生存分析家族分工：time-to-recall / hazard → `生存分析`；需求侧动态偏好 → 本类型。
