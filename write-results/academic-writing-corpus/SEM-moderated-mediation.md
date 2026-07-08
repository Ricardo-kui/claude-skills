---
type: canonical_results
canonical_id: "SEM-moderated-mediation"
status: EMERGING
design_type: SEM / Path Model / Moderated Mediation
estimator: Mplus / SEM
source_papers:
  - habel2016 (JM, 2016): "CSR → benefit/cost markup → price fairness, moderated by attribution; Preacher & Hayes (2008) indirect effects"
  - "bamberger_homburg_wielgos_2021_wage_inequality_jm (Journal of Marketing): inconsistent mediation → suppressor variable, opposing direct/indirect effects"
  - "vadakkepatt_arora_martin_paharia_2022_lobbying_jm (Journal of Marketing): simultaneous-equation SEM reporting with IV diagnostics + Granger causality"
variants_count: 3
created: 2026-06-03
updated: 2026-07-07
source: Distilled from Habel et al. (2016, JM) by distill-methods-exemplar
---

# SEM Moderated Mediation 报告模式

## 功能描述

当 Theory 提出 moderated mediation（条件间接效应）时，Results 需要报告：直接效应、间接效应的路径系数、交互项系数、以及条件间接效应在不同 moderator 水平下的显著性。本模板基于 Preacher & Hayes (2008) 同时估计法。

## 适用场景

- Theory 包含 "间接效应随 moderator 变化" 的假设（H2a/H2b 型）
- SEM / Path Model 估计（Mplus, LISREL, PLS）
- 特别适合辩证对立双路径框架：正/负间接效应在不同条件下此消彼长

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): habel2016 (JM) — Studies 2, 3

---

## 报告骨架

### 1. 模型拟合报告

```
We estimated the path model depicted in [Figure N] using [Mplus N] ([citation]). 
For the estimation of the mediation model, we followed Preacher and Hayes's (2008) 
recommendations and estimated the indirect effects and the direct effect simultaneously. 
The model achieved an adequate fit (CFI = [N]; TLI = [N]; RMSEA = [N]; SRMR = [N]). 
[Table N] shows the estimated path coefficients.
```

### 2. 路径系数表格式

按功能分组呈现，非按变量字母序：

| 分组 | 路径 | 假设 | 系数 |
|------|------|------|------|
| **Warm-Glow Path** | IV → M1 (benefit) | | β |
| | M1 → DV | | β |
| **Extra-Charge Path** | IV → M2 (cost) | | β |
| | M2 → DV | | β |
| **Outcome** | DV → Downstream outcome | | β |
| **Interaction Effects** | M1 × W → DV | H2a: + | β |
| | IV × W → M2 | H2b: − | β |
| **Main Effects of Moderator** | W → DV | | β |
| | W → M2 | | β |
| **Controlled Effects** | IV → DV (direct) | | β |
| | Controls → DV/mediators | | β |

### 3. 条件间接效应解读模板

**H2a 型（正间接效应被 moderator 增强）**:
```
In H[N], we proposed that the indirect effect of [IV] → [M1] → [DV] is more positive 
for higher levels of [moderator] because [moderator] positively moderates the effect of 
[M1] on [DV]. The results show that the effect of [M1] on [DV] is significantly 
[positive/negative] (β = [N], p < [N]) and moderated by [moderator] (β = [N], p < [N]). 
Consequently, the indirect effect of [IV] on [DV] through [M1] depends on [moderator]: 
it is significantly positive as long as [moderator] is higher than [threshold] (see the 
"[Level of Moderator]" rows at the bottom of [Table N]). Thus, in [full/partial] support 
of H[N], we find that [moderator] positively moderates the indirect effect of [IV] on 
[DV] through [M1].
```

**H2b 型（负间接效应被 moderator 减弱）**:
```
In H[N], we proposed that the indirect effect of [IV] → [M2] → [DV] becomes more 
negative for lower levels of [moderator] because [moderator] negatively moderates the 
effect of [IV] on [M2]. The results show that the effect of [IV] on [M2] is 
[insignificant/significant] (β = [N], p [><] [N]) but [positively/negatively] moderated 
by [moderator] (β = [N], p < [N]). Consequently, the indirect effect of [IV] on [DV] 
through [M2] depends on [moderator]: it is significantly negative as long as [moderator] 
is lower than [threshold] (see the bottom of [Table N]). Thus, [moderator] negatively 
moderates the indirect effect of [IV] on [DV] through [M2], in support of H[N].
```

### 4. 直接效应声明

```
Notably, the direct effect of [IV] on [DV] is [not significant / significant] (β = [N], 
p [><] [N]), indicating that the proposed inferential mechanisms [fully mediate / 
partially mediate] this relationship, thus providing [additional / no] support for our 
conceptual framework.
```

---

## Supplemental Analyses 模板

### 替代 DV 验证

```
We analyzed our conceptual model for alternative outcome variables beyond [focal DV]—
that is, [alternative DV 1], [alternative DV 2], and [alternative DV 3]. The results 
appear in [Table N] and are largely consistent with our main model: (1) [Pattern for 
alt DV 1]. (2) [Pattern for alt DV 2]. (3) [Pattern for alt DV 3]. The high consistency 
across outcome variables underlines the robustness of our results.
```

### 交互效应探测

```
We analyzed whether [M1] and [M2] exert a two-way interaction effect, or even a 
three-way interaction effect with [moderator], on [DV]. However, we found no significant 
interaction effects.
```

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 标准 SEM 报告；条件间接效应必须报告 |
| SMJ | ⭐⭐⭐⭐ | 需要更强的理论-结果对齐 |
| AMJ | ⭐⭐⭐ | 需要额外内生性讨论 |
| MSOM | ⭐⭐⭐⭐ | 适合运营 trade-off 类研究 |

---

## 反模式

- 只报告主效应不报告条件间接效应 → moderated mediation 的核心就是条件间接效应
- 交互项显著但不解读间接效应 → 必须按 moderator 的不同水平计算和报告间接效应
- 模型拟合指标缺失 → CFI, TLI, RMSEA, SRMR 四项至少报告三项
- 不报告直接效应 → 直接效应是否显著是"完全中介 vs 部分中介"的关键证据
- 替代 DV 不验证 → 构念效度需要至少一个替代 DV 的 robustness check

---

## 比较两条方向相反通道的持续性：Reverse-Code + Wald Test (qiao2026 型)

### 功能描述

当 Theory 提出一个 **differential-persistence meta-hypothesis**（"通道 A 的效应比通道 B 的效应更持久"），而两条通道方向相反（一正一负）时，不能直接比较两个交互系数。本模板解决"如何统计检验两条对立通道的时间动态是否可区分"。

### 适用场景

- Theory 含 H3 型 meta-hypothesis：[内嵌构念] 的效应比 [受众认知构念] 的效应**衰减更慢**
- 两条通道与时间（age）的交互系数方向都为正（因为负向通道的主效应为负，age 交互为正意味着负效应被侵蚀）
- 主模型为生存分析或非线性模型，交互项以 hazard/系数形式呈现

### 报告骨架

```
To facilitate clear interpretation of interaction coefficients, we mean-centered the 
continuous moderator variable ([age / tenure / elapsed time]) before creating interaction 
terms with the two [imprint] measures. [Binary variables require no centering]. The results 
in [Column] show that the interaction between [time] and [channel A] is [positive] (β = 
[N], p < [N]), indicating that [channel A] effects [strengthen over time]. The interaction 
between [time] and [channel B] is also [positive] (β = [N], p < [N]), indicating that 
[channel B] effects [erode over time] (with the main effect being negative). Because one 
[channel] is positively and the other negatively related to [outcome], we reverse-coded 
[channel B] to make them directionally consistent and then compared these coefficients with 
a Wald test. The test confirms that these interaction coefficients differ significantly 
(χ² = [N], p < [N]), demonstrating that [channel A] and [channel B] exhibit statistically 
distinguishable temporal dynamics.
```

### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. Mean-center 时间变量 | center [age] before interaction | 提升主效应可解释性，不改变交互系数 |
| 2. 报告两个 time×channel 交互 | 方向都为正时仍需解释衰减 | 正向通道主效应+→ age 交互+ = 增强；负向通道主效应−→ age 交互+ = 侵蚀 |
| 3. Reverse-code 负向通道 | 使两系数同向 | Wald test 才可直接比较幅度 |
| 4. Wald test | 检验两交互系数差异 | 统计判定"持续性差异"是否成立 |

### 反模式

- **不 reverse-code 直接比较**：一正一负的系数无法用 Wald 比较"哪条衰减更慢"
- **混淆"占优"与"持续"**：本检验回答的是"哪条通道的时间动态更陡"，而非"哪条通道当前更强"——后者是 net effect，前者是 persistence meta-hypothesis
- **断点/分段不一致**：若主模型用 piecewise 分段，reverse-code + Wald 应在同一分段设定下进行

### 语料锚定

- qiao_hiatt_sine2026 (SMJ) — H3：内嵌 capability imprint 比外部 identity imprint 更持久。age×capability (+0.060) vs age×identity (+0.080)，reverse-code 后 Wald χ²=60.08, p<.001。配合 `write-theory/.../mechanism_chain.md` "双重印记对立通道" 模板使用。

---

## 不一致中介 → 抑制变量报告 (Bamberger 2021 JM 型)

### 功能描述

当 direct effect 与 indirect effect 方向相反，且控制 mediator 后 direct effect 反而增强时，将统计现象升华为"不一致中介—抑制变量"的理论叙事。

### 报告骨架

```
[IV] has a [positive/negative] direct effect on [DV] (β = [value], p < [threshold]).
By contrast, [IV] has an aggregated [negative/positive] indirect effect on [DV]
through [mediator(s)] (β = [value], p < [threshold], 95% CI: [[lower], [upper]]).
These opposing indirect and direct effects reflect an inconsistent mediation
([citation]), suggesting that [benefit] is mitigated by [cost].

More precisely, by including [mediator] in the model, the direct effect of [IV]
on [DV] becomes [stronger]. Previous research—unaware of the suppressive effect
of [mediator]—may have underestimated the direct effect of [IV] and therefore
may have reached ambiguous conclusions.
```

### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 报告 direct effect | 显著+方向 | 建立 baseline |
| 2. 报告 aggregated indirect | 显著+反方向+CI | 建立 inconsistency |
| 3. 命名"inconsistent mediation" | 引用 MacKinnon et al. (2000) | 统计背书 |
| 4. 升华为 suppressor | "unaware of the suppressive effect... may have underestimated" | 贡献锚定 |

### 反模式
- 在 indirect 不显著时声称 inconsistent mediation → 两个效应必须都显著
- 不报告 CI → indirect effect 的 CI 是判断 suppression 是否成立的关键
- 声称 suppression 但不引用 MacKinnon et al. (2000) → 需要方法论引用

---

## 联立方程 SEM 结果报告 + IV 诊断前置 (Vadakkepatt et al. 2022 JM 型)

### 功能描述
当论文使用联立方程 SEM 且含内生性处理时，Results 需要在主假设检验前报告 IV 诊断（Hansen's J + Kleibergen-Paap），并用多列表格呈现多个方程的估计结果。

### 报告骨架

```
Before discussing our results, we note that the results of Hansen's J test 
reveal that the instruments are valid (p > [threshold]). The Kleibergen-Paap 
test also shows that our instruments are relevant (p < [threshold]), increasing 
our confidence in the use of these variables as instruments. Likewise, we 
examine the instrument effects on [endogenous_var] (Table [X], Column [A]). 
[Instrument_1] has a [direction], [significant/nonsignificant] effect on 
[endogenous_var] (α = [value]; p [relation] [threshold]), and [Instrument_2] 
has a [direction], significant effect (α = [value]; p < [threshold]).

[Table X] reports the results. Column [A] shows [first_stage_equation]. 
Column [B] reports [DV1_equation]. The coefficient for [IV] is 
[positive/negative] and significant (α = [value], p < [threshold]), 
supporting Hypothesis [N]. Column [C] reports [DV2_equation]. The coefficient 
for [IV] is [opposite_sign] and significant (α = [value], p < [threshold]), 
supporting Hypothesis [N+1].
```

### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 前置 IV 诊断 | Hansen's J (p>.10) + Kleibergen-Paap (p<.01) | 让读者在假设检验前确认 instrument validity |
| 2. 报告第一阶段 | Column A: IV→endogenous_var | 透明化 instrument relevance |
| 3. 多列表格 | 6列 (A-F) 覆盖 3个方程 × 2套系统 | 紧凑但完整——避免多个独立表格 |
| 4. 逐列叙述 | 按 Column A→B→C 顺序，每列对应一个方程 | 读者导航零负担 |

### 反模式
- IV 诊断放在脚注或附录 → 当 IV 是主识别策略时，必须在正文报告
- 每个方程独立建表 → 多列表格更高效且便于跨方程对比
- 不报告 first-stage 系数 → 读者无法判断 instrument relevance 的方向和幅度
