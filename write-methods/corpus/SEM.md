---
design_type: "SEM"
status: 📋 TEMPLATE
source_papers:
  - "vadakkepatt_arora_martin_paharia_2022_lobbying_jm (Journal of Marketing): simultaneous-equation SEM + IV + Granger causality + residual centering + table-based variable documentation"
variants_count: 6
created: 2026-05-18
updated: 2026-07-07
---
# SEM — Methods 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| M7 | 2 | 1、3 |
| M8 | 1 | 2 |
| M3 | 1 | 4 |

### M7（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | 联立方程 SEM + 工具变量 + 相关误差 | 多方程误差相关需联合估计（mediation/moderated mediation） | 首变体：解释为何联合估计（效率 + 共同遗漏变量偏误） | EMERGING | Vadakkepatt et al. 2022 (JM) |
| 3 | 残差中心化处理交互项多重共线性 | 连续×连续交互项与主效应高相关 | 区别于 mean-centering：残差中心化是升级方案 | EMERGING | Vadakkepatt et al. 2022 (JM) |

### M8（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | 面板 Granger 因果检验 + 平稳性检验前置诊断 | 时序方向性（X→Y vs Y→X）与变量进入形式（水平/差分）决策 | 两步都放 Methods（模型设定依据），非 Results | EMERGING | Vadakkepatt et al. 2022 (JM) |

### M3（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | 表格式变量文档 | 变量 10+ 个、逐段描述冗长的论文（副槽位 M4） | 标准变量表格化（Construct/Notation/Description/Citations/Source），正文只展开特殊变量 | EMERGING | Vadakkepatt et al. 2022 (JM) |


## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `SEM` 专用变体）。

## 设计特征摘要

<!-- 由 distill-methods-exemplar 首次蒸馏后填充 -->

## 累积变体

### 变体 1: M7 联立方程 SEM + 工具变量 + 相关误差 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We estimate [N] systems of equations. The first (Equations [1], [2], and [4]) tests [Hypotheses_set_A], whereas the second system (Equations [1], [3], and [4]) tests [Hypotheses_set_B]. We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors. Joint estimation across multiple equations yields more efficient estimates ([citation]), accounts for endogeneity due to common omitted variable bias ([citation]), and has been used to test mediation, moderation, and moderated mediation relationships in the presence of endogenous regressors ([citations]).
**与原骨架差异**: SEM/同时方程设计的 M7 核心——不是逐个方程估计，而是解释为什么联合估计（correlated errors → more efficient → accounts for common omitted variable bias）。两套方程系统的区分（主效应 vs. 交互效应）使 Hypothesis-Equation 映射清晰。

<!-- wb:vadakkepatt2022:legacy_SEM_1 -->
### 变体 2: M8 面板 Granger 因果检验 + 平稳性检验作为前置诊断 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: Prior to specifying our models, we conducted panel Granger causality tests to examine whether lobbying Granger-causes customer satisfaction or vice versa. They reveal that lobbying Granger-causes customer satisfaction (χ² = 5.04, p < .10) and not the reverse.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M8
**骨架**:
> Prior to specifying our models, we conducted panel Granger causality tests to examine whether [IV] Granger-causes [DV] or vice versa. They reveal that [IV] Granger-causes [DV] (χ² = [value], p < [threshold]) and not the reverse. Next, we examine independent variable stationarity with panel unit root tests. A lack of stationarity dictates how the variables enter the model. The [test_name] rejects the null hypothesis that the variables contain unit roots (p < [threshold]). We conclude the variable is mean-stationary and specify it in terms of levels.
**与原骨架差异**: 面板时间序列的前置诊断在 corpus 中首次出现。Granger 检验建立时序方向性（X→Y 而非 Y→X），平稳性检验决定变量是以水平值还是一阶差分进入模型。两步都应放在 Methods 而非 Results——它们是模型设定决策的依据。
<!-- wb:vadakkepatt2022:legacy_SEM_2 -->

### 变体 3: M7 残差中心化处理交互项多重共线性 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: In addition, to rule out multicollinearity concerns for the interaction terms (with r > .70), we residual-centered the interaction of lobbying with product market lobbying.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> To rule out multicollinearity concerns for the interaction terms (with r > [threshold]), we residual-centered the interaction of [IV] with [moderator]. Residual centering has been shown to reduce multicollinearity between an interaction term and its first-order effect term, to provide stable and unbiased results ([citation]), and has been used in recent literature ([citations]).
<!-- wb:vadakkepatt2022:legacy_SEM_3 -->
**与原骨架差异**: 当主效应和交互项高度相关时（常见于连续×连续交互），残差中心化是 mean-centering 的升级方案。两句话完成：why needed → what method → citation support。适用于任何有多个交互项的面板回归/SEM。

### 变体 4: M3/M4 表格式变量文档 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: Customer satisfaction, advertising spend, and R&D spend are widely used variables, so we do not detail their construction here, beyond the information provided in Table 2. Instead, we focus on the variables that require additional explanation or coding or are unique to our research.
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: M3/M4
**骨架**:
> Table [X] details the variables, operationalizations, references, and data sources. [Well-known variables A, B, C] are widely used, so we focus on variables that require additional explanation or coding. First, [unique_variable_1: operationalization + source + justification]. Second, [unique_variable_2: coding procedure + interrater reliability]. Third, [unique_variable_3].
**与原骨架差异**: 变量多的论文（10+个）逐个段落描述会冗长。表格式文档（Construct | Notation | Description | Citations | Source）将"标准变量"表格化，正文只展开需要额外解释的变量。这与 Mayo 的 Table 3（控制变量表）互补——本变体覆盖全部变量。
<!-- wb:vadakkepatt2022:legacy_SEM_4 -->

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
变体 <编号>: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: M?
**骨架**:
> "..."
**与原骨架差异**: ...
-->


### 变体 5: M7 中介因果序滞后错位链（giannetti2022 型）
**来源论文**: Giannetti & Srinivasan 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "As we test for mediation via lower emphasis on product safety, we lag corporate lobbying by two years and emphasis on product safety by one year."
**验证状态**: EMERGING
**写入日期**: 2026-09-28
**槽位**: M7（兼具 M8 色彩：以时间安排回应反向因果）
**骨架**:
> We use lagged independent variables to address endogeneity concerns created by reverse causality. As we test for mediation via [the mediator], we lag [the independent variable] by [two] years and [the mediator] by [one] year, so that [X] precedes [M] which precedes [the outcome] in the estimation design.
**与原骨架差异**: because-clauses 变体 B（anand_mukherjee）统一累积测量窗以使交互项可估——窗口由估计设计决定但只管长度；本变体把**中介因果序编码进滞后层级**：中介链上每个变量按其位置依次多滞后一期，一句话同时交付反向因果防御与中介时序可证性。适用于：滞后中介链设计（X t-k → M t-1 → Y t）的模型段；区别于统一滞后一期 IV 的面板模板——滞后层级与理论链一一对应而非全体同滞。
**诚实边界**: 滞后错位缓解（不消除）反向因果与遗漏变量疑虑——不含时不变混杂、预期效应与缓慢漂移混杂仍无解；这是时间安排论证而非识别策略，行文不得升格为 identification claim。

<!-- wb:giannetti_2022_corporate_lobbying_and_product_recalls_an_inv:methods_m7_mediation_lag_staggering_chain -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->


### 变体 6: M7 第二阶段被调节中介单方程交互实现（giannetti2022 型）
**来源论文**: Giannetti & Srinivasan 2022 (Journal of the Academy of Marketing Science)
**原始句锚点**: "Further, as our model is a second-stage moderated mediation model, we subsequently include both emphasis on product safety and its interactions with marketing CEO, R&D CEO, and focus on radical (vs. incremental) innovation." ... "To ensure the correct model specification, we include the main effect of marketing and R&D CEO and the main effect of focus on radical (vs. incremental) innovation in Eq. 2 above."
**验证状态**: EMERGING
**写入日期**: 2026-09-28
**槽位**: M7
**骨架**:
> Further, as our model is a second-stage moderated mediation model, we include [the mediator] and its interactions with [moderator a], [moderator b], and [moderator c] in the [outcome] equation. To ensure the correct model specification, we include the main effect of [each moderator] in the equation.
**与原骨架差异**: SEM 变体 1（Vadakkepatt）以联立 SEM 联合估计被调节中介——多方程 correlated errors 路线；本变体不另设方程：第二阶段调节直接实现为结果方程内 mediator×moderator 交互项，并以 "To ensure the correct model specification..." 一句声明低阶主效应齐备（层级原理合规），先发制人封堵"只报交互不报主效应"审稿意见。与非线性模型 变体 15（省略机械共线低阶项）方向相反：交互可估性在此靠补齐低阶项而非省略。适用于：计数/二元结果方程 + 调节作用于中介→结果路径的第二阶段被调节中介。
**诚实边界**: 非线性模型的交互系数不等于边际交互效应（交叉偏导随观测异质）——范文照搬此做法且未预告 predicted counts/IRRs 翻译，正中非线性模型 common_failures[1]；写作时应预告效应量翻译或改用条件间接效应分解，不得把交互系数直接当 moderated mediation 效应量宣读。

<!-- wb:giannetti_2022_corporate_lobbying_and_product_recalls_an_inv:methods_m7_secondstage_moderated_mediation_single_equation -->
<!-- wb-meta: gap=Incompleteness status=EMERGING -->
