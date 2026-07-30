---
design_type: "动态面板-GMM"
status: ✓ POPULATED
source_papers:
  - pollock2015 (ASQ, 2015): "AB difference GMM — three-source endogeneity; status↔reputation coevolution"
variants_count: 4
created: 2026-05-18
updated: 2026-07-30
---

# 动态面板-GMM — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `动态面板-GMM` 专用变体）。

## 设计特征摘要

动态面板-GMM 设计用于估计**同时包含滞后因变量（path dependence）、同时性（simultaneity）和未观测异质性（unobserved heterogeneity）**的纵向模型。三者各自引入不同来源的内生性，难以逐一处理；核心估计器 Arellano–Bond（AB）GMM 通过工具化内生变量（用预定/外生变量的滞后项作工具）+ 一阶差分消除固定效应，**统一处理三源内生性**。诊断依赖 Hansen *J* 过度识别检验、difference-in-Sargan/Hansen（工具子集正交性）、AR(2) 二阶残差自相关检验。典型场景：coevolution / reciprocal causation / 持久性构念（status、reputation、legitimacy）的纵向演化、发展性调节（age/stage）改变路径依赖。

首篇蒸馏：Pollock, Lee, Jin & Lashley (2015, *ASQ*) — 新创 VC 企业的 status↔reputation 共演。

## 累积变体

### 变体 1: Pollock et al. 2015 (ASQ) — AB difference GMM 三源内生性统一处理 (2026-07-30)
**验证状态**: 通过（单篇，待第二篇交叉验证）
**槽位**: M7/M8
**骨架**:
> "Although this model specification incorporating [path dependence, simultaneity, and unobserved heterogeneity] allowed us to test our theoretical arguments, each of these features introduced different kinds of endogeneity to the models. [The lagged dependent variable] is correlated with the error term ([citation]); the [simultaneity] implicit in our model specification, in which both causal effects are positive, is likely to overestimate the simultaneously determined parameters ([citation]); and [unobserved heterogeneity] is a source of endogeneity. While there are well-established econometric treatments for each source of endogeneity, it is difficult to address all three sources of endogeneity simultaneously. We addressed this issue by employing the Arellano–Bond (AB) estimator ([Arellano and Bond, 1991]) using the *xtabond2* command ([Roodman, 2009]) in STATA. The AB estimator addresses various kinds of endogeneity by instrumenting endogenous variables with predetermined as well as exogenous variables. The lagged terms of covariates can serve as valid instruments, given that they are predetermined and hence cannot be associated with the current error term, as long as error terms are not serially correlated. This estimator also addresses unobserved heterogeneity by first-differencing, which is similar to the fixed-effects estimator; thus time-constant control variables are not required. Taken together, the AB estimator addresses all three sources of endogeneity."
**与原骨架差异**: 首个动态面板-GMM 变体。核心手法：先**逐一列举三源内生性及其方向**（LDV 与误差项相关；同时性高估双方参数；异质性），声明"难以同时处理"，再以 AB 估计器作为**统一解**收束——把估计器选择包装为对识别威胁的系统性回应，而非技术默认。to address... we employed... Taken together 句式可原样保留。

### 变体 2: Pollock et al. 2015 (ASQ) — difference GMM vs system GMM 选择（稳态/平稳性论证）(2026-07-30)
**验证状态**: 通过（单篇，待第二篇交叉验证）
**槽位**: M7
**骨架**:
> "The AB estimator relies on the generalized method of moments (GMM) ([citation]). Although the system GMM estimator generates more efficient estimates ([Blundell and Bond, 1998]), we employed the AB difference GMM estimator because system GMM requires stationarity, or a steady state, for consistent estimation ([Arellano, 2003]). Given that our sample consists of [relatively young firms], it is unlikely that the evolutionary processes of their [outcome] are close to a steady state, particularly in the early years. To control for heteroscedasticity, we report robust standard errors."
**与原骨架差异**: 在效率（system GMM 更有效）与一致性（difference GMM 不需稳态）之间做**有理论依据的权衡**——用样本的发展阶段（young firms 远未达稳态）作为选择 difference GMM 的理由。把"为何不用更有效的估计器"这一审稿人必问问题前置回答。

### 变体 3: Pollock et al. 2015 (ASQ) — 工具变量滞后结构 per-sample 经验精调程序 (2026-07-30)
**验证状态**: 通过（单篇，待第二篇交叉验证）
**槽位**: M8
**骨架**:
> "We followed the procedures recommended by [Roodman (2009)] to select the instruments for our models. Any predictor-variable value can theoretically be used as an instrument, but to correctly specify the lag structure it is important to consider whether a focal variable is strictly exogenous, predetermined, or endogenous ([citation]). [If the variable is strictly exogenous, then all its lagging, current, and leading values can be valid instruments; if predetermined, its one-period or earlier lags can be valid instruments; and if endogenous, its two-period or earlier lags can be valid instruments.] Because all our predictor variables except for the [time dummies] are potentially endogenous, we began selecting instruments using at least [two-year] lags. Then we determined whether each instrument met the orthogonality condition using Hansen's *J* statistic and the difference-in-Sargan statistic, and whether it induced second-order autocorrelation using the AB statistic. We fine-tuned each variable's lag structure using this procedure. Valid lag structures are empirically determined based on the sample. Because we used a variety of samples—[N] split samples for testing [age-contingent hypotheses] and the total sample for testing [other hypotheses]—we fine-tuned the lag structure for each sample used."
**与原骨架差异**: 把工具选择呈现为**经验驱动的迭代精调**而非机械规则：先按变量外生性类别（strictly exogenous / predetermined / endogenous）确定起始滞后阶数，再用 Hansen *J* + difference-in-Sargan + AR(2) 三诊断逐变量精调。关键诚实点："Valid lag structures are empirically determined based on the sample" + 分样本各自精调——避免一刀切滞后结构在不同子样本失效。

### 变体 4: Pollock et al. 2015 (ASQ) — 发展性调节无理论断点 → 多阈值分样本检验 (2026-07-30)
**验证状态**: 通过（单篇，待第二篇交叉验证）
**槽位**: M4/M8
**骨架**:
> "To test [developmental / age-contingent hypotheses H_a/H_b] we [ran a series of regressions splitting the sample into subsamples based on different age increments]. To have enough observations to conduct meaningful tests we began with [actors] less than or equal to, and [actors] greater than, [base age] years of age, and we increased the lower age break by [N] years in each regression. [Because there is no theoretical reason to determine a specific break point, we tested this hypothesis using the results over a range of age thresholds rather than imposing a single split.]"
**与原骨架差异**: 当发展性调节变量（age/stage）**无理论断点**时，不强行施加单一交互或单一分样本切点，而是**跨多个阈值切点重复检验**，报告效应随阈值变化的模式（如"效应在 ≤7 岁显著、8–10 岁不显著、≥11 岁反向"）。这把"无理论断点"从弱点转化为**展示效应梯度**的优势。配套 Results 需报告每个阈值子样本的 N 与系数（小 N 子样本结果需谨慎解读，参见配套 write-results 分样本叙事）。
