---
design_type: "动态面板-GMM"
status: ✓ POPULATED
source_papers:
  - pollock2015 (ASQ, 2015): "AB difference GMM — three-source endogeneity; status↔reputation coevolution"
variants_count: 7
created: 2026-05-18
updated: 2026-08-13
---
# 动态面板-GMM — Methods 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M7 | 3 | 1、2、5 |
| M8 | 1 | 3 |
| M4 | 1 | 4 |

### M7（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | AB difference GMM 三源内生性统一处理 | LDV + 同时性 + 未观测异质性三源内生性并存（副槽位 M8） | 首变体：逐一列举三源内生性及其方向，再以 AB 作统一解 | VERIFIED | Pollock et al. 2015 (ASQ) |
| 2 | difference GMM vs system GMM 选择（稳态/平稳性论证） | 样本处于发展早期、远离稳态（young firms）时 | 在效率（system GMM）与一致性（difference GMM）间做有理论依据的权衡 | VERIFIED | Pollock et al. 2015 (ASQ) |
| 5 | FD 后 t-2 工具化 LDV（Anderson–Hsiao） | FD+LDV 的 Nickell/差分内生，不必上 AB-GMM | 区别于变体1：只工具化 LDV，不处理同时性 | VERIFIED | Kalaignanam et al. 2013 JM |

### M8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | 工具变量滞后结构 per-sample 经验精调程序 | AB-GMM 工具选择需按样本精调滞后结构 | 先按变量外生性类别定起始滞后，再用 Hansen/diff-Sargan/AR(2) 逐变量精调 | VERIFIED | Pollock et al. 2015 (ASQ) |

### M4（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | 发展性调节无理论断点 → 多阈值分样本检验 | 发展性调节（age/stage）无理论断点时（副槽位 M8） | 区别于单一交互/单一切点：跨多阈值重复检验展示效应梯度 | VERIFIED | Pollock et al. 2015 (ASQ) |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `动态面板-GMM` 专用变体）。

## 设计特征摘要

动态面板-GMM 设计用于估计**同时包含滞后因变量（path dependence）、同时性（simultaneity）和未观测异质性（unobserved heterogeneity）**的纵向模型。三者各自引入不同来源的内生性，难以逐一处理；核心估计器 Arellano–Bond（AB）GMM 通过工具化内生变量（用预定/外生变量的滞后项作工具）+ 一阶差分消除固定效应，**统一处理三源内生性**。诊断依赖 Hansen *J* 过度识别检验、difference-in-Sargan/Hansen（工具子集正交性）、AR(2) 二阶残差自相关检验。典型场景：coevolution / reciprocal causation / 持久性构念（status、reputation、legitimacy）的纵向演化、发展性调节（age/stage）改变路径依赖。

首篇蒸馏：Pollock, Lee, Jin & Lashley (2015, *ASQ*) — 新创 VC 企业的 status↔reputation 共演。

## 累积变体

### 变体 1: Pollock et al. 2015 (ASQ) — AB difference GMM 三源内生性统一处理 (2026-07-30)
**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
**槽位**: M7/M8
**原始句锚点**: Although this model specification incorporating path dependence, simultaneity, and unobserved heterogeneity allowed us to test our theoretical arguments, each of these features introduced different kinds of endogeneity to the models. We addressed this issue by employing the Arellano–Bond (AB) estimator (Arellano and Bond, 1991) using the xtabond2 command (Roodman, 2009) in STATA 11.
**骨架**:
> "Although this model specification incorporating [path dependence, simultaneity, and unobserved heterogeneity] allowed us to test our theoretical arguments, each of these features introduced different kinds of endogeneity to the models. [The lagged dependent variable] is correlated with the error term ([citation]); the [simultaneity] implicit in our model specification, in which both causal effects are positive, is likely to overestimate the simultaneously determined parameters ([citation]); and [unobserved heterogeneity] is a source of endogeneity. While there are well-established econometric treatments for each source of endogeneity, it is difficult to address all three sources of endogeneity simultaneously. We addressed this issue by employing the Arellano–Bond (AB) estimator ([Arellano and Bond, 1991]) using the *xtabond2* command ([Roodman, 2009]) in STATA. The AB estimator addresses various kinds of endogeneity by instrumenting endogenous variables with predetermined as well as exogenous variables. The lagged terms of covariates can serve as valid instruments, given that they are predetermined and hence cannot be associated with the current error term, as long as error terms are not serially correlated. This estimator also addresses unobserved heterogeneity by first-differencing, which is similar to the fixed-effects estimator; thus time-constant control variables are not required. Taken together, the AB estimator addresses all three sources of endogeneity."
**与原骨架差异**: 首个动态面板-GMM 变体。核心手法：先**逐一列举三源内生性及其方向**（LDV 与误差项相关；同时性高估双方参数；异质性），声明"难以同时处理"，再以 AB 估计器作为**统一解**收束——把估计器选择包装为对识别威胁的系统性回应，而非技术默认。to address... we employed... Taken together 句式可原样保留。

### 变体 2: Pollock et al. 2015 (ASQ) — difference GMM vs system GMM 选择（稳态/平稳性论证）(2026-07-30)
**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
**槽位**: M7
**原始句锚点**: Although the system GMM estimator generates more efficient estimates (Blundell and Bond, 1998), we employed the AB difference GMM estimator because system GMM requires stationarity, or a steady state, for consistent estimation (Arellano, 2003).
**骨架**:
> "The AB estimator relies on the generalized method of moments (GMM) ([citation]). Although the system GMM estimator generates more efficient estimates ([Blundell and Bond, 1998]), we employed the AB difference GMM estimator because system GMM requires stationarity, or a steady state, for consistent estimation ([Arellano, 2003]). Given that our sample consists of [relatively young firms], it is unlikely that the evolutionary processes of their [outcome] are close to a steady state, particularly in the early years. To control for heteroscedasticity, we report robust standard errors."
**与原骨架差异**: 在效率（system GMM 更有效）与一致性（difference GMM 不需稳态）之间做**有理论依据的权衡**——用样本的发展阶段（young firms 远未达稳态）作为选择 difference GMM 的理由。把"为何不用更有效的估计器"这一审稿人必问问题前置回答。

### 变体 3: Pollock et al. 2015 (ASQ) — 工具变量滞后结构 per-sample 经验精调程序 (2026-07-30)
**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
**槽位**: M8
**原始句锚点**: We followed the procedures recommended by Roodman (2009) to select the instruments for our models. Any predictor-variable value can theoretically be used as an instrument, but to correctly specify the lag structure it is important to consider whether a focal variable is strictly exogenous, predetermined, or endogenous (Arellano, 2003).
**骨架**:
> "We followed the procedures recommended by [Roodman (2009)] to select the instruments for our models. Any predictor-variable value can theoretically be used as an instrument, but to correctly specify the lag structure it is important to consider whether a focal variable is strictly exogenous, predetermined, or endogenous ([citation]). [If the variable is strictly exogenous, then all its lagging, current, and leading values can be valid instruments; if predetermined, its one-period or earlier lags can be valid instruments; and if endogenous, its two-period or earlier lags can be valid instruments.] Because all our predictor variables except for the [time dummies] are potentially endogenous, we began selecting instruments using at least [two-year] lags. Then we determined whether each instrument met the orthogonality condition using Hansen's *J* statistic and the difference-in-Sargan statistic, and whether it induced second-order autocorrelation using the AB statistic. We fine-tuned each variable's lag structure using this procedure. Valid lag structures are empirically determined based on the sample. Because we used a variety of samples—[N] split samples for testing [age-contingent hypotheses] and the total sample for testing [other hypotheses]—we fine-tuned the lag structure for each sample used."
**与原骨架差异**: 把工具选择呈现为**经验驱动的迭代精调**而非机械规则：先按变量外生性类别（strictly exogenous / predetermined / endogenous）确定起始滞后阶数，再用 Hansen *J* + difference-in-Sargan + AR(2) 三诊断逐变量精调。关键诚实点："Valid lag structures are empirically determined based on the sample" + 分样本各自精调——避免一刀切滞后结构在不同子样本失效。


### 变体 7: Ridge, Aime & White 2013 (SMJ) — AB-GMM 诊断对报告链：零假设→违例含义→判定 (2026-09-12)
**验证状态**: EMERGING（单篇）
**槽位**: M8
**原始句锚点**: "We performed Arellano-Bond tests for autocorrelation and Hansen tests for the validity of the instrumentation strategy. ... Second-order autocorrelation would indicate that some lags of the dependent variable that are used as instruments are endogenous, but the tests reveal no such problem in our models"
**骨架**:
> "We performed [Arellano-Bond] tests for autocorrelation and [Hansen] tests for the validity of the instrumentation strategy. [For the former, we failed to reject the null of no autocorrelation in the first-differenced errors], which means that [the Arellano-Bond estimator] in our application is asymptotically consistent. [Second-order autocorrelation would indicate that some lags of the dependent variable that are used as instruments are endogenous], but the tests reveal no such problem in our models ([citations]). [Second, the Hansen test] showed that the moment restrictions in our models are valid or, in other terms, that the instruments are exogenous. The statistic for the test under the null hypothesis is distributed as [chi-square] with degrees of freedom equal to [the number of instruments minus the number of predictors]. Our tests show that our restrictions are valid (we failed to reject the null hypothesis) in all our models."
**与原骨架差异**: 区别变体 3（工具滞后结构的事前逐变量经验精调程序）——本变体是**事后诊断报告链**：开头一句并置两个诊断的分工（序列相关 vs 工具有效性），然后每个检验按三拍展开：零假设的白话陈述→违例意味着哪些工具失效（"Second-order autocorrelation would indicate that some lags... are endogenous"）→判定收口（failed to reject → 一致性 + 工具有效性）。 Hansen 拍附带分布与自由度陈述（χ²，自由度=工具数−预测变量数）。补齐 corpus 中缺失的"估计后诊断如何写"标准块（变体 1/3 只覆盖事前选择）。
**诚实边界**: AR(2) 的零假设是**无**二阶自相关——原文 "we failed to reject the null hypothesis of autocorrelation" 是零假设写反的病句（已登记反模式），骨架已改为 "no autocorrelation"，勿复制原句；原文对 Hansen 的解释在同段重复两次（冗余反模式），骨架合并为一次；AR(2) 行报 p 值、Hansen 行报 χ² 与自由度。
<!-- wb:ridge_aime_white_2013_smj:m8_ab_gmm_diagnostic_pair_reporting_chain -->


### 变体 4: Pollock et al. 2015 (ASQ) — 发展性调节无理论断点 → 多阈值分样本检验 (2026-07-30)
**验证状态**: VERIFIED — expert_audit_override（user 2026-09-06：Pollock/Westphal/Gulati 系单源即 VERIFIED）
**槽位**: M4/M8
**原始句锚点**: To test these hypotheses we ran a series of regressions splitting the sample into subsamples based on different age increments, presented in table 2. Because there is no theoretical reason to determine a specific break point, we tested this hypothesis using the results in table 2, which presents the relationships over a range of years.
**骨架**:
> "To test [developmental / age-contingent hypotheses H_a/H_b] we [ran a series of regressions splitting the sample into subsamples based on different age increments]. To have enough observations to conduct meaningful tests we began with [actors] less than or equal to, and [actors] greater than, [base age] years of age, and we increased the lower age break by [N] years in each regression. [Because there is no theoretical reason to determine a specific break point, we tested this hypothesis using the results over a range of age thresholds rather than imposing a single split.]"
**与原骨架差异**: 当发展性调节变量（age/stage）**无理论断点**时，不强行施加单一交互或单一分样本切点，而是**跨多个阈值切点重复检验**，报告效应随阈值变化的模式（如"效应在 ≤7 岁显著、8–10 岁不显著、≥11 岁反向"）。这把"无理论断点"从弱点转化为**展示效应梯度**的优势。配套 Results 需报告每个阈值子样本的 N 与系数（小 N 子样本结果需谨慎解读，参见配套 write-results 分样本叙事）。

### 变体 5: M7 FD 后用 t-2 工具化 LDV（Anderson–Hsiao 式） (2026-08-13)

**来源论文**: Kalaignanam, Kushwaha & Eilert 2013 (*Journal of Marketing*)

**原始句锚点**: "The lagged dependent variable in Model 1b ... is likely to be correlated to the random error. ... we use the second lag (t - 2) of the dependent variable as an instrument for the lagged dependent variable."

**验证状态**: VERIFIED

**写入日期**: 2026-08-13

**槽位**: M7

**骨架**:
> The lagged dependent variable in [the first-differenced equation] is likely to be correlated to the random error. Consistent with previous research ([citations]), we use the second lag ([t-2]) of the dependent variable as an instrument for the lagged dependent variable.

**与原骨架差异**: 区别变体 1（AB-GMM 统一处理 LDV/同时性/异质性）——本变体只用 t-2 工具化 FD 后的 LDV，不声称处理同时性。避免所有 FD+LDV 被路由到 xtabond2。

**诚实边界**: 未报 Hansen J / AR(2) 时不得写成 GMM；这是 Anderson–Hsiao 简易 IV。工具化相关误差，不升级为因果效应。



<!-- wb:kalaignanam_2013_jm:legacy_动态面板-GMM_5 -->
### 变体 6: Ridge, Aime & White 2013 (SMJ) — 短面板适用性陈述 + 估计器优势枚举 (2026-09-12)
**验证状态**: EMERGING（单篇）
**槽位**: M7
**原始句锚点**: "This dynamic panel technique is especially suited to analyzing autoregressive-distributed lag models from panels with cross-sectional units observed for relatively few time periods like the panels that are typically used in this area of research."
**骨架**:
> "We use dynamic panel techniques to analyze our data with [firm and year fixed effects]. In particular, we perform our analysis using the [Arellano-Bond] method. This dynamic panel technique is especially suited to analyzing [autoregressive-distributed lag models] from panels with cross-sectional units observed for relatively few time periods like the panels that are typically used in this area of research. There are several advantages to this dynamic panel approach in our estimation. First, it controls for [lagged values of the dependent variable] as [outcomes] are likely related to [prior levels of performance] ([citation]). Second, [GMM] estimation with robust standard errors provides better estimates in the presence of unknown heteroscedasticity and autocorrelation in dynamic panels ([citation]). Finally, since any independent variables that are not strictly exogenous become potentially endogenous because they may be correlated to past and future realizations of the error, it uses deep lagged values of relevant regressors and exogenous variables as instruments of the independent variables to deal effectively with potential endogeneity in our model."
**与原骨架差异**: 区别变体 1（威胁先行：逐一列举三源内生性→声明难以同时处理→AB 统一解）与变体 2（difference vs system GMM 稳态权衡）——本变体是**适用性先行 + 优势正面枚举**：先一句立短面板适用性（relatively few time periods），再以 "There are several advantages... First... Second... Finally..." 正面列举三重优势（LDV 与误差相关/Nickell 型问题、稳健 SE 对未知异方差与序列相关、深度滞后工具对内生性）。适用场景：审稿人未点名具体内生性威胁、需要一段轻量"为什么用这个估计器"的正面辩护。
**诚实边界**: 优势枚举不能替代威胁定位——LDV 为何与误差相关仍须给出依据（可引 Greene 2000 或 Nickell 1981）；若审稿人可能质疑 difference vs system GMM 的选择，需叠加变体 2 的稳态论证；因果语言保持在 "address/deal with potential endogeneity"，不升级为因果识别主张。原文未注明软件与命令（如 xtabond2/Roodman），写入时应补。
<!-- wb:ridge_aime_white_2013_smj:m7_ab_gmm_short_panel_advantage_enumeration -->

