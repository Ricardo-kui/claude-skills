---
design_type: "SEM"
status: 📋 TEMPLATE
source_papers:
  - "vadakkepatt_arora_martin_paharia_2022_lobbying_jm (Journal of Marketing): simultaneous-equation SEM + IV + Granger causality + residual centering + table-based variable documentation"
variants_count: 4
created: 2026-05-18
updated: 2026-07-07
---

# SEM — Methods 骨架

## 主骨架

参见 `write-methods/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-M*.md`（各 slot 文件内含 `SEM` 专用变体）。

## 设计特征摘要

<!-- 由 distill-methods-exemplar 首次蒸馏后填充 -->

## 累积变体

### 变体 1: M7 联立方程 SEM + 工具变量 + 相关误差 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> We estimate [N] systems of equations. The first (Equations [1], [2], and [4]) tests [Hypotheses_set_A], whereas the second system (Equations [1], [3], and [4]) tests [Hypotheses_set_B]. We have multiple equations in which the errors across them can be correlated, so we estimate the equations jointly using a structural equation model approach with correlated errors. Joint estimation across multiple equations yields more efficient estimates ([citation]), accounts for endogeneity due to common omitted variable bias ([citation]), and has been used to test mediation, moderation, and moderated mediation relationships in the presence of endogenous regressors ([citations]).
**与原骨架差异**: SEM/同时方程设计的 M7 核心——不是逐个方程估计，而是解释为什么联合估计（correlated errors → more efficient → accounts for common omitted variable bias）。两套方程系统的区分（主效应 vs. 交互效应）使 Hypothesis-Equation 映射清晰。

### 变体 2: M8 面板 Granger 因果检验 + 平稳性检验作为前置诊断 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: Prior to specifying our models, we conducted panel Granger causality tests to examine whether lobbying Granger-causes customer satisfaction or vice versa. They reveal that lobbying Granger-causes customer satisfaction (χ² = 5.04, p < .10) and not the reverse.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M8
**骨架**:
> Prior to specifying our models, we conducted panel Granger causality tests to examine whether [IV] Granger-causes [DV] or vice versa. They reveal that [IV] Granger-causes [DV] (χ² = [value], p < [threshold]) and not the reverse. Next, we examine independent variable stationarity with panel unit root tests. A lack of stationarity dictates how the variables enter the model. The [test_name] rejects the null hypothesis that the variables contain unit roots (p < [threshold]). We conclude the variable is mean-stationary and specify it in terms of levels.
**与原骨架差异**: 面板时间序列的前置诊断在 corpus 中首次出现。Granger 检验建立时序方向性（X→Y 而非 Y→X），平稳性检验决定变量是以水平值还是一阶差分进入模型。两步都应放在 Methods 而非 Results——它们是模型设定决策的依据。

### 变体 3: M7 残差中心化处理交互项多重共线性 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: In addition, to rule out multicollinearity concerns for the interaction terms (with r > .70), we residual-centered the interaction of lobbying with product market lobbying.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M7
**骨架**:
> To rule out multicollinearity concerns for the interaction terms (with r > [threshold]), we residual-centered the interaction of [IV] with [moderator]. Residual centering has been shown to reduce multicollinearity between an interaction term and its first-order effect term, to provide stable and unbiased results ([citation]), and has been used in recent literature ([citations]).
**与原骨架差异**: 当主效应和交互项高度相关时（常见于连续×连续交互），残差中心化是 mean-centering 的升级方案。两句话完成：why needed → what method → citation support。适用于任何有多个交互项的面板回归/SEM。

### 变体 4: M3/M4 表格式变量文档 (1篇高价值)
**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**原始句锚点**: Customer satisfaction, advertising spend, and R&D spend are widely used variables, so we do not detail their construction here, beyond the information provided in Table 2. Instead, we focus on the variables that require additional explanation or coding or are unique to our research.
**验证状态**: 待第二篇交叉验证
**写入日期**: 2026-07-07
**槽位**: M3/M4
**骨架**:
> Table [X] details the variables, operationalizations, references, and data sources. [Well-known variables A, B, C] are widely used, so we focus on variables that require additional explanation or coding. First, [unique_variable_1: operationalization + source + justification]. Second, [unique_variable_2: coding procedure + interrater reliability]. Third, [unique_variable_3].
**与原骨架差异**: 变量多的论文（10+个）逐个段落描述会冗长。表格式文档（Construct | Notation | Description | Citations | Source）将"标准变量"表格化，正文只展开需要额外解释的变量。这与 Mayo 的 Table 3（控制变量表）互补——本变体覆盖全部变量。

<!-- distill-methods-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: M?
**骨架**:
> "..."
**与原骨架差异**: ...
-->
