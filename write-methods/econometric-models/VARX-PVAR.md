---
design_type: "VARX-PVAR"
status: 🟢 EMERGING
source_papers:
  - "borah_tellis_2016 (JMR): VARX framework with Granger causality exogeneity tests, multi-level temporal aggregation (daily VARX + monthly PVAR + brand-level stock VARX), third-party NLP data with RA validation (86%/80%), online chatter as text construct, 3-reason VARX framework justification, impulse response cumulative effects"
variants_count: 8
created: 2026-07-15
updated: 2026-07-20
---
# VARX-PVAR — Methods 骨架

## 变体速查表

> 检索辅助。状态词表：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M1 | 1 | 变体 1 |
| M2 | 1 | 变体 2 |
| M3 | 2 | 变体 3、4 |
| M5 | 1 | 变体 5 |
| M7 | 2 | 变体 7、8 |
| M8 | 1 | 变体 6 |

### M1（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 行业情境 4-reason 辩护 | 为单行业时间序列设计辩护情境选择，按现象频度→数据可得→理论控制→经济重要性递进排列 | 与面板数据-OLS 通用 setting 论证互补，强调 temporal granularity 的数据需求 | 通过（单篇） | Borah & Tellis 2016 JMR |

### M2（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 品牌选择递进正当性 + Quasi-Experiment 设计 | 从行业 top-k 品牌中选择样本并论证品牌选择的理论正当性（含数据缺失诚实表述） | 与面板数据-OLS 样本交集漏斗互补，不靠逐层排除数字而靠品牌选择理论正当性 | 通过（单篇） | Borah & Tellis 2016 JMR |

### M3（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | 第三方 NLP 数据 + 人工链接匹配 | 使用第三方文本数据（RavenPack 等）且原始数据缺单位标识、需人工匹配到单位层时 | 与变体 4 互补——本变体管数据获取与人工链接，变体 4 管算法效度验证 | 通过（单篇） | Borah & Tellis 2016 JMR |
| 4 | 算法准确率双重验证 | 用分类算法测量文本构念、需报告算法-人工双重效度（interrater + accuracy）时 | 比单一 inter-coder agreement 更严格，增加算法准确率验证环 | 通过（单篇） | Borah & Tellis 2016 JMR |

### M5（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | VARX 框架 3-reason 辩护 | 论证 Why VARX 而非 OLS/DiD/IV（Granger 因果 + 非平稳稳健性 + 累积效应）时 | 与面板数据-OLS 的 RE 辩护/FE 选择互补，是时间序列设计的核心正当性 | 通过（单篇） | Borah & Tellis 2016 JMR |

### M7（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 7 | VARX 方程规格 | 需要系统方程表述 VARX/VAR/PVAR 设计（notation、三类控制变量、平稳性决定变量形式）时 | — | 通过（单篇） | Borah & Tellis 2016 JMR |
| 8 | VARX 估计细节 | 报告 VARX 估计诊断（BIC lag 选择、Newey-West HAC SE、parameter-to-observation 比）时 | 与面板数据-OLS 嵌套横截面聚类 SE 互补，是时间序列估计特有细节 | 通过（单篇） | Borah & Tellis 2016 JMR |

### M8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 6 | Granger Causality 作为外生性核心论证 | 为时间序列设计提供外生性识别论证（承认弱点 + Granger 检验 + quasi-experiment 表述）时 | 区别于 DiD 平行趋势与 IV 排他性限制，是时间序列设计特有的识别论证 | 通过（单篇） | Borah & Tellis 2016 JMR |


## 主骨架

参见 `write-methods/SKILL.md` → 填空段落骨架 → `VARX-PVAR`。

## 设计特征摘要

VARX/VAR/PVAR 是**多内生变量动态系统**的估计框架，核心识别策略是 **Granger causality**（区别于 DiD 的 parallel trends 与 IV 的 exclusion restriction）。关键设计特征：(1) 内生变量在同一系统中通过滞后值互动，外生变量（如召回/新产品发布）作为 shock 进入；(2) 平稳性（ADF / Phillips-Perron）与协整检验决定变量形式（levels vs differences）；(3) 通过 GIRF（generalized impulse response function）估计累积/脉冲响应效应；(4) 多 level 时间聚合（日度 VARX + 月度 PVAR）须说明不同 level 用不同估计器的理由（数据长度、参数数量、理论关注点）。Borah & Tellis (2016) 进一步融合第三方 NLP chatter 数据，要求算法准确率 + 人工 interrater 双重验证。

## 累积变体

### 变体 1: 行业情境 4-reason 辩护 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: We select the U.S. automobile industry to analyze the effect of recalls for several reasons. First, this industry has a high frequency of recalls, which provides an ample number of recall events for our analysis.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M1
**骨架**:
> [Empirical setting] provides an appropriate context for examining [theoretical relationship] for [N] reasons. First, [setting property: high frequency of phenomenon] makes [mechanism: dynamic effects/innovation diffusion] observable. Second, [data feature: rich daily-level online chatter/media/advertising variation] allows us to observe [unit/process: temporal dynamics/wear-in-wear-out] over [period: daily/weekly/monthly]. Third, [scope condition: single-industry focus holding confounds constant] reduces [cross-industry heterogeneity/alternative explanations]. Fourth, [economic significance/industry importance: GDP share, employment impact, market size] enhances [theoretical relevance/practical implications].
**与原骨架差异**: 这是行业情境辩护的**递进版4-reason结构**。关键要素：(1) 从现象频度→数据可得性→理论控制→经济重要性递进排列；(2) 强调temporal granularity的价值（"daily-level variation"）；(3) 明确单行业设计的trade-off（internal validity > generalizability）。与面板数据-OLS变体1（通用setting论证）互补——本变体更强调**时间序列设计的数据需求**。
**诚实边界**: 若选择多行业样本，需在Second reason中论证"cross-industry variation in [phenomenon] allows us to test [moderator]"。

### 变体 2: 品牌选择递进正当性 + Quasi-Experiment 设计 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: We selected these brands because they constitute four of the five brands that had the most recalls in 2010.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M2
**骨架**:
> We selected [N] [units: nameplants/products/models] from [N] [brands/organizations] for our empirical analysis. We use the following [brands/organizations] in our sample: [list]. We selected these [brands/organizations] because they constitute [top-k leaders in phenomenon X] in [year]. We were unable to get [data: chatter/financials] for [excluded brand], but the remaining [brands] provide an ample number of [events: recalls/crises] to test [theoretical relationship]. In general, the [market share/ranking] for these [brands] has been [stable/fluctuating] for [period]. Even though [some brands] have been [changing location/supply chain], consumers still view these brands as [country/segment category], because of their [origin/ownership]. Thus, this sampling strategy allows us to evaluate to some extent whether [theoretical relationship] is moderated by [moderator_1: market share/dominance] and [moderator_2: country of origin/segment].
**与原骨架差异**: 适用于任何需要**从行业top-k中选择样本**的研究。关键要素：(1) 承认数据缺失的诚实表述（"unable to get data"）；(2) 市场排序稳定性说明；(3) 明确调节变量检验动机。与面板数据-OLS变体2（样本交集漏斗）互补——本变体不需要逐层排除数字，但需要说明**品牌选择的理论正当性**。
**诚实边界**: 若品牌选择有 survivorship bias（如排除破产品牌），需在稳健性中报告包含所有品牌的限制样本。

### 变体 3: 第三方 NLP 数据 + 人工链接匹配 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: In the original data provided to us, nameplates were not mentioned. Thus, we visited each specific blog, review, and forum and determined the nameplate discussed in order to link the chatter to the nameplate level.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M3
**骨架**:
> We obtained the [text data: online chatter/news/reviews] from a third-party data provider. The firm uses its proprietary software to mine and content-code the [text] using techniques such as natural language processing, machine learning, text mining, and statistical analysis. The [text data] span postings about the [units] on various platforms of social media. Overall, approximately [N] sites were sourced to obtain the data. In the original data provided to us, [key identifier: firm name/product name/ticker] were not mentioned. Thus, we [manual matching procedure: visited each specific site and determined the unit discussed to link chatter to unit level]. This effort took approximately [N man-hours: 250 man-hours]. The third-party data provider [scraped/collected] these sites to obtain any [text] across these [platforms] that mentioned the focal [units] across the time frame of our study. The firm then used its proprietary algorithm that quantifies the content of the [text] by generating tag data (similar to coding) on [N] dimensions at the [sentence/document] level: [dimension_1: subject], [dimension_2: attribute], and [dimension_3: valence].
**与原骨架差异**: 适用于任何使用第三方文本数据的研究（RavenPack、Bloomberg News、晨星新闻等）。关键要素：(1) 明确算法技术栈（NLP/ML/text mining）；(2) 说明数据源数量（~1000 sites）；(3) 承认原始数据的缺陷（missing identifiers）；(4) 报告人工匹配成本（250 man-hours）；(5) 简述分类维度。与 `micro-templates/manual-coding-validation.md` 类型7配合使用。
**诚实边界**: 若第三方算法完全专有（proprietary），需引用技术附录或数据源白皮书。若算法细节不可得，需通过人工验证样本提供透明度。

### 变体 4: 算法准确率双重验证 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: The interrater agreement was 86%. We found the algorithm to have a classification accuracy of 80%; that is, 80% of the chatter classified as negative by the algorithm was also classified as negative by both research assistants.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M3
**骨架**:
> We independently checked the accuracy of the [algorithm/classification] with the help of [N] research assistants. For this purpose, we randomly selected [N] samples of [text data] from the total corpus of [category: negative chatter/tone]. Two research assistants independently read each [item: post/article] in the [corpus] and classified the [text] as [category_1], [category_2], or [category_3: positive/negative/neutral]. The interrater agreement was [percentage: 86%]%. We found the [algorithm] to have a classification accuracy of [percentage: 80]%; that is, [percentage]% of the [text] classified as [category: negative] by the [algorithm] was also classified as [category] by both research assistants.
**与原骨架差异**: 这是**文本构念测量的双重效度链**——(1) interrater agreement (人工-人工一致性)；(2) algorithm accuracy (算法-人工一致性)。比单一inter-coder agreement更严格，适用于任何使用分类算法的研究。关键要素：(1) 随机抽样验证（而非全量人工编码）；(2) 双重百分比报告（interrater + accuracy）；(3) 明确算法准确率的定义（"classified as X by algorithm was also classified as X by both RAs"）。
**诚实边界**: 算法准确率<70%时需考虑：(1) 重新训练算法，(2) 使用替代操作化，(3) 在稳健性中报告人工编码结果。

### 变体 5: VARX 框架 3-reason 辩护 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: We use the VARX framework for three reasons. First, it allows estimation of Granger causality among a set of variables (endogenous variables) through use of their lagged values.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M5
**骨架**:
> We use the [estimator: VARX/VAR/PVAR] framework for three reasons. First, it allows estimation of [statistical property: Granger causality/temporal ordering] among a set of variables (endogenous variables) through use of their [temporal property: lagged values]. Second, it ensures robustness of the model to issues of [statistical concerns: nonstationarity, spurious causality, endogeneity, serial correlation, and reverse causality]. Third, it permits estimation of the [effect type: long-term or cumulative effects] of causal variables using the [statistical technique: impulse response functions/GIRF].
**与原骨架差异**: 这是**VARX/VAR/PVAR 框架的标准M5论证**，完整回答"Why VARX而非OLS/DiD/IV?"。关键要素：(1) Granger causality作为时间序列识别策略；(2) 稳健性到非平稳/伪因果/内生性/序列相关；(3) 累积效应估计（impulse response）。与面板数据-OLS变体13（RE三重辩护）和变体10（Hausman FE选择）互补——本变体是**时间序列设计的核心正当性**。
**诚实边界**: VARX假设所有endogenous变量在同一系统中动态互动，且残差为white noise。需报告平稳性检验（ADF/PP）和协整检验结果支持假设。

### 变体 6: Granger Causality 作为外生性核心论证 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: We acknowledge that it is possible recalls could be endogenously determined by consumer reaction in online chatter, and thus our design is not a rigorous experiment.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M8
**骨架**:
> We acknowledge that it is possible [treatment variable: e.g., recalls/crises/shocks] could be endogenously determined by [outcome variable: e.g., consumer reaction in online chatter/media coverage], and thus our design is not a rigorous experiment. However, we test the assumption of [treatment] as a random shock in our empirical tests. We run the typical time series checks, such as testing for [diagnostics: serial correlation, trends, seasonality, and stationarity]. We find no evidence of temporal causality from [outcome] to [treatment]; that is, [outcome] does not Granger-cause [treatment]. We assume that a [treatment shock] leads to a big increase in [outcome measure]. But in the absence of [theoretical effect: e.g., perverse halo/spillover] (the null hypothesis), [treatment] should not affect [outcome] for other [units]. Thus, the effect of [treatment] on [outcome] allows for a quasi-experimental manipulation, and our design constitutes a repeated natural event or quasi-experiment.
**与原骨架差异**: 这是**VARX/VAR/PVAR 设计的核心识别策略**，区别于 DiD (parallel trends) 和 IV (exclusion restriction)。关键要素：(1) 承认设计弱点（"not a rigorous experiment"）；(2) Granger causality检验作为外生性证据；(3) 理论null作为对比基准（"treatment should not affect other units"）；(4) "quasi-experiment"的诚实表述。与面板数据-OLS变体18（dyad FE + 混淆源举例）互补——本变体是**时间序列设计特有的识别论证**。
**诚实边界**: Granger causality检验的滞后阶数影响结论。需报告检验的最大lag number（如20 lags）和lag selection准则（AIC/BIC）。若不同lag下结论改变，需报告稳健性。

### 变体 7: VARX 方程规格 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: We estimate the relationships between concerns and other endogenous variables of the various nameplates using the VARX framework. For ease of exposition, below is the specification using levels of the variables for the Japanese nameplates belonging to the Small Pickup segment.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M7
**骨架**:
> We estimate the relationships between [endogenous variables] of the various [units] using the [estimator: VARX] framework. For ease of exposition, below is the specification using [levels/differences/transformations] of the variables for the [segment/group]. Here [notation: ConTac, ConRid, ConFrt] denote [endogenous variables: concerns for different units]. [Other notation: MediaTac, MediaRid, MediaFrt] denote [other endogenous variables: media citations]. [Ad notation: AdTac, AdRid, AdFrt] denote [additional endogenous variables: advertising]. (Note that for ease of exposition, we have not included the endogenous variables for [additional variables: promotional ads, leasing ads] in Equation 1. This would add [N] more endogenous variables, thereby increasing the number of endogenous variables to [total N].) [Exogenous notation: Recalls, NewProduct] denote [exogenous variables]. The set x_1, …, x_p comprises the p control variables. Along with [exogenous variables], we add three additional controls: (1) [control_1: day of week dummies] to control for [temporal effect: weekday/weekend], (2) [control_2: holiday dummies] to control for [seasonal effect], and (3) [control_3: deterministic time trend], which captures the effect of omitted, gradually changing variables. The variables α, δ, β, and γ are the parameters to be estimated, and ε_t are white noise residuals, which are distributed as N(0, Σ). The coefficients β_{i,j} estimate the effect of [theoretical effect: perverse halo/spillover] of [variable_i] on [variable_j]. On the basis of the [statistical tests: augmented Dickey–Fuller, Phillips–Perron, and cointegration tests], we chose the proper appropriate specification for the endogenous variables that enter the [estimator] equation.
**与原骨架差异**: VARX方程的**标准统计写法**。关键要素：(1) 明确notation对应的具体变量；(2) 说明equation简化（"for ease of exposition"）；(3) 报告total endogenous variables数量；(4) 列举三类控制变量（temporal/seasonal/trend）；(5) 说明平稳性/协整检验决定变量形式（levels vs differences）。适用于任何需要系统方程表述的VARX/VAR/PVAR设计。
**诚实边界**: 若endogenous变量数量>15，需考虑简约模型（parsimonious specification）并报告稳健性。若ADF检验显示非平稳，需使用first differences而非levels。

### 变体 8: VARX 估计细节 (1/1 复现)
**来源论文**: Borah & Tellis 2016 (JMR)
**原始句锚点**: The optimal lag length is 1 for most of the 17 VARX equations, except in a few cases in which it is 2, as per the (Schwartz's) Bayesian information criterion.
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: M7
**骨架**:
> The optimal lag length is [N: lag 1 for most equations] for most of the [N: 17] [estimator: VARX] equations, except in a few cases in which it is [N: lag 2], as per the (Schwartz's) Bayesian information criterion. Our results are not affected by the presence of any residual correlation, nonnormality of residuals, or heteroskedasticity. We estimate the [estimator] models using an ordinary least squares regression, accounting for heteroskedasticity and potential serial correlation with the Newey–West estimator. The average parameter-to-observation ratio for each equation across the [N] [estimator] models is [ratio: 1:16.6]. Note that because each equation contains exactly the same set of regressors, the ordinary least squares estimates are numerically identical to seemingly unrelated regression estimates ([Zellner 1962]). Using these estimates, we then compute the effect of one variable on another over time, taking current and carryover effects, using the generalized impulse response function (GIRF), explained in [Web Appendix/Technical Appendix].
**与原骨架差异**: VARX/PVAR估计的**标准诊断段落**。关键要素：(1) BIC lag selection结果；(2) Newey-West HAC标准误；(3) parameter-to-observation ratio（防止overfitting）；(4) OLS=SUR简化说明；(5) 预告impulse response分析。与面板数据-OLS变体7（嵌套横截面聚类SE）互补——本变体是**时间序列估计特有**的细节写法。
**诚实边界**: parameter-to-observation ratio < 1:10时需警惕overfitting。若lag number > 3，需报告AIC/BIC对比并解释为何选择较长lag。

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **Granger causality检验仅说"we ran tests"未报告具体结果** | 仅说"find no evidence of temporal causality"——未报告F统计量、p值、lag number | 报告完整结果："Granger causality tests up to 20 lags showed no significant effects (F = [value], p > .05 for all lags)" |
| **第三方NLP数据未报告算法准确率** | 使用第三方算法但仅报告"we obtained data from [provider]" | 必须报告算法准确率(如80%)和人工验证的interrater agreement(如86%)，否则无法论证构念效度 |
| **VARX方程未报告平稳性检验** | 直接估计VARX但未说明变量是否平稳 | 必须报告ADF/Phillips-Perron检验结果："All variables are stationary at levels/differences, based on ADF test (p < .05)" |
| **Granger因果检验滞后阶数不报告** | 仅说"we ran tests"未说明检验了几个lag | 明确报告："Granger causality tests up to [N] lags" + lag selection准则 (AIC/BIC) |
| **多level时间聚合未明确区分** | 同时有日度、月度、年度分析但未说明为何不同level用不同估计器 | 明确说明："Because daily data allows fine-grained dynamics, we use VARX for daily chatter; monthly sales data are too short for VARX, so we use PVAR" |

## 诚实边界

- **VARX框架假设**：残差为white noise (N(0,Σ))，且所有endogenous变量在同一系统中动态互动。若理论预测某些变量间不存在因果链，需通过简约模型（parsimonious specification）或block exogeneity检验验证。
- **Granger causality检验**：滞后阶数选择影响结论。需报告检验的最大lag number（如20 lags）和lag selection准则（AIC/BIC）。若不同lag number下结论改变，需报告稳健性检验。
- **第三方NLP数据**：算法细节通常不公开（proprietary），需引用技术附录或数据源白皮书说明分类逻辑。若算法完全黑箱，需通过人工验证样本（如本研究的500个样本）提供透明度。
- **平稳性假设**：若ADF检验显示变量非平稳，需使用first differences而非levels。若变量混合阶单整（I(0)和I(1)共存），需使用Johansen协整检验或Toda-Yamamoto approach。
- **Impulse response horizon**：需报告累积效应的观测窗口（如6天、10期、1年）。若不同horizon下结论改变，需报告稳健性。
- **多level时间聚合**：同一理论问题在不同temporal granularity下用不同估计器（日度VARX + 月度PVAR + 年度cross-section）需说明为何不同level对应不同估计器（数据长度、参数数量、理论关注点）。

## 与其他设计类型的关系

| 设计类型 | 共同要素 | 差异 |
|---------|---------|------|
| **面板数据-OLS** | 控制变量because逻辑、固定效应vs随机效应选择 | VARX强调temporal dynamics和Granger causality，OLS关注cross-sectional variation和FE/RE选择 |
| **自然实验-DiD** | Quasi-experiment设计、外生性论证 | DiD用parallel trends检验外生性，VARX用Granger causality检验 |
| **IV-2SLS** | 内生性担忧、外生性论证 | IV用exclusion restriction + overidentification test，VARX用Granger causality + serial correlation tests |
| **文本构念测量** | 文本数据获取、效度验证 | VARX融合文本与档案数据（chatter + recalls + sales），纯文本构念研究仅关注text-derived variables |
| **事件历史+事件研究** | 事件中心分析、时间窗口 | 事件研究用CAR/abnormal returns，VARX用impulse response和cumulative effects |

---
*Created: 2026-07-15*  
*Source Paper: Borah & Tellis (2016) "Halo (Spillover) Effects in Social Media", Journal of Marketing Research*  
*Design Type: VARX-PVAR (Vector Autoregressive with Exogenous Variables, Panel VAR)*  
*Status: 🟢 EMERGING — 8 variants（单篇 Borah & Tellis 2016 入库，待第二篇时间序列论文交叉验证）*
*Next Review: After second time-series paper distilled*  
