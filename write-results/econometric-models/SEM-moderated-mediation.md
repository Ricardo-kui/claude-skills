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
  - "ilicic_brennan_2026_jm (Journal of Marketing): ten-study multimethod investigation of political ideology and consumer responses to addictive products; sense of agency -> perceived product danger mechanism; personally directed threat appeal moderator"
  - "reinwald_kanitz_bamberger_backmann_hoegl_2026_orsc (Organization Science): event-contingent indirect effects remain interpretable despite inconsistent direct interaction, with pre/post bootstrap CIs"
  - "kashmiri_nicol_arora_2017_jams (Journal of the Academy of Marketing Science): one shared mediator tested across heterogeneous outcome branches; two indirect effects supported and one explicitly unsupported"
variants_count: 7
created: 2026-06-03
updated: 2026-08-08
source: Distilled from Habel et al. (2016, JM) by distill-methods-exemplar
---
# SEM Moderated Mediation 报告模式

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| R2 | 1 | 3 |
| R3 | 3 | 1, 2, 7 |
| R4 | 2 | 4, 6 |
| R6 | 1 | 5 |

### R2（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | 联立方程 SEM + IV 诊断前置 | 联立方程含内生性处理：主检验前报 Hansen's J + Kleibergen-Paap + 多列表格逐列导航 | 区别于变体 1（无内生性版本）：IV 诊断前置 + 多列表格 | EMERGING | Vadakkepatt et al. 2022 JM |

### R3（3）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | SEM 基本报告模板（Preacher & Hayes 同时估计） | 标准 moderated mediation：拟合指标+路径系数表+条件间接效应解读+直接效应声明 | 基础模板，变体 2–7 均为其扩展 | EMERGING | Habel et al. 2016 JM |
| 2 | 不一致中介 → 抑制变量报告 | direct 与 indirect 方向相反且含 mediator 后 direct 增强 | 区别于变体 1 常规报告：升华为 suppressor 叙事（MacKinnon et al. 2000 背书） | EMERGING | Bamberger et al. 2021 JM |
| 7 | 共享中介跨分支证据账本 | 一中介连多 outcome（不同估计器/量纲）：a-path 报一次逐分支判定 | 区别于变体 2 单分支抑制叙事：分支账本 + 失败分支保留为机制边界 | VERIFIED | Kashmiri et al. 2017 JAMS |

### R4（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | Reverse-Code + Wald 持续性比较 | H3 型 differential-persistence：两通道方向相反、比较时间动态 | 区别于变体 5（顺序问题）：比较两条通道**持续性**（reverse-code 后 Wald χ²） | EMERGING | Qiao, Hiatt & Sine 2026 SMJ |
| 6 | 事件条件间接效应分层报告 | X×event→M→Y 且直接交互不一致：事件前/后 bootstrap CI 分层报 | 区别于变体 1（连续 moderator 条件）：事件条件性 + 直接交互不复制声明 | EMERGING | Reinwald et al. 2026 ORSC |

### R6（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | Reverse-Order 中介顺序敏感性 | 序列中介竞争排序检查：反转 M1/M2 重测 | 区别于变体 4（方向问题）：**顺序问题**，CI 含零≠排除、不确认因果序 | EMERGING | Ilicic & Brennan 2026 JM |

## 功能描述

当 Theory 提出 moderated mediation（条件间接效应）时，Results 需要报告：直接效应、间接效应的路径系数、交互项系数、以及条件间接效应在不同 moderator 水平下的显著性。本模板基于 Preacher & Hayes (2008) 同时估计法。

## 适用场景

- Theory 包含 "间接效应随 moderator 变化" 的假设（H2a/H2b 型）
- SEM / Path Model 估计（Mplus, LISREL, PLS）
- 特别适合辩证对立双路径框架：正/负间接效应在不同条件下此消彼长

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 标准 SEM 报告；条件间接效应必须报告 |
| SMJ | ⭐⭐⭐⭐ | 需要更强的理论-结果对齐 |
| AMJ | ⭐⭐⭐ | 需要额外内生性讨论 |
| MSOM | ⭐⭐⭐⭐ | 适合运营 trade-off 类研究 |

## 反模式

- 只报告主效应不报告条件间接效应 → moderated mediation 的核心就是条件间接效应
- 交互项显著但不解读间接效应 → 必须按 moderator 的不同水平计算和报告间接效应
- 模型拟合指标缺失 → CFI, TLI, RMSEA, SRMR 四项至少报告三项
- 不报告直接效应 → 直接效应是否显著是"完全中介 vs 部分中介"的关键证据
- 替代 DV 不验证 → 构念效度需要至少一个替代 DV 的 robustness check

## 累积变体

### 变体 1: SEM 基本报告模板（Preacher & Hayes 同时估计 + 条件间接效应解读）

**来源论文**: Habel et al. 2016 (JM) Studies 2–3
**验证状态**: EMERGING（1 paper；canonical 模板持续使用）
**写入日期**: 2026-06-03
**槽位**: R3
**跨论文复现**: EMERGING (1 paper): habel2016 (JM) — Studies 2, 3

#### 1. 模型拟合报告

```
We estimated the path model depicted in [Figure N] using [Mplus N] ([citation]). 
For the estimation of the mediation model, we followed Preacher and Hayes's (2008) 
recommendations and estimated the indirect effects and the direct effect simultaneously. 
The model achieved an adequate fit (CFI = [N]; TLI = [N]; RMSEA = [N]; SRMR = [N]). 
[Table N] shows the estimated path coefficients.
```

#### 2. 路径系数表格式

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

#### 3. 条件间接效应解读模板

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

#### 4. 直接效应声明

```
Notably, the direct effect of [IV] on [DV] is [not significant / significant] (β = [N], 
p [><] [N]), indicating that the proposed inferential mechanisms [fully mediate / 
partially mediate] this relationship, thus providing [additional / no] support for our 
conceptual framework.
```

#### 补充：替代 DV 验证

```
We analyzed our conceptual model for alternative outcome variables beyond [focal DV]—
that is, [alternative DV 1], [alternative DV 2], and [alternative DV 3]. The results 
appear in [Table N] and are largely consistent with our main model: (1) [Pattern for 
alt DV 1]. (2) [Pattern for alt DV 2]. (3) [Pattern for alt DV 3]. The high consistency 
across outcome variables underlines the robustness of our results.
```

#### 补充：交互效应探测

```
We analyzed whether [M1] and [M2] exert a two-way interaction effect, or even a 
three-way interaction effect with [moderator], on [DV]. However, we found no significant 
interaction effects.
```

### 变体 2: 不一致中介 → 抑制变量报告

**来源论文**: Bamberger, Homburg & Wielgos 2021 (Journal of Marketing)
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R3

#### 功能描述

当 direct effect 与 indirect effect 方向相反，且控制 mediator 后 direct effect 反而增强时，将统计现象升华为"不一致中介—抑制变量"的理论叙事。

#### 报告骨架

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

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 报告 direct effect | 显著+方向 | 建立 baseline |
| 2. 报告 aggregated indirect | 显著+反方向+CI | 建立 inconsistency |
| 3. 命名"inconsistent mediation" | 引用 MacKinnon et al. (2000) | 统计背书 |
| 4. 升华为 suppressor | "unaware of the suppressive effect... may have underestimated" | 贡献锚定 |

#### 反模式

- 在 indirect 不显著时声称 inconsistent mediation → 两个效应必须都显著
- 不报告 CI → indirect effect 的 CI 是判断 suppression 是否成立的关键
- 声称 suppression 但不引用 MacKinnon et al. (2000) → 需要方法论引用

### 变体 3: 联立方程 SEM 结果报告 + IV 诊断前置

**来源论文**: Vadakkepatt, Arora, Martin & Paharia 2022 (Journal of Marketing)
**验证状态**: EMERGING
**槽位**: R2/R3

#### 功能描述

当论文使用联立方程 SEM 且含内生性处理时，Results 需要在主假设检验前报告 IV 诊断（Hansen's J + Kleibergen-Paap），并用多列表格呈现多个方程的估计结果。

#### 报告骨架

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

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 前置 IV 诊断 | Hansen's J (p>.10) + Kleibergen-Paap (p<.01) | 让读者在假设检验前确认 instrument validity |
| 2. 报告第一阶段 | Column A: IV→endogenous_var | 透明化 instrument relevance |
| 3. 多列表格 | 6列 (A-F) 覆盖 3个方程 × 2套系统 | 紧凑但完整——避免多个独立表格 |
| 4. 逐列叙述 | 按 Column A→B→C 顺序，每列对应一个方程 | 读者导航零负担 |

#### 反模式

- IV 诊断放在脚注或附录 → 当 IV 是主识别策略时，必须在正文报告
- 每个方程独立建表 → 多列表格更高效且便于跨方程对比
- 不报告 first-stage 系数 → 读者无法判断 instrument relevance 的方向和幅度

### 变体 4: Reverse-Code + Wald Test 对立通道持续性比较（differential persistence）

**来源论文**: Qiao, Hiatt & Sine 2026 (SMJ)
**验证状态**: EMERGING
**写入日期**: 2026-06-16
**槽位**: R4/R6

#### 功能描述

当 Theory 提出一个 **differential-persistence meta-hypothesis**（"通道 A 的效应比通道 B 的效应更持久"），而两条通道方向相反（一正一负）时，不能直接比较两个交互系数。本模板解决"如何统计检验两条对立通道的时间动态是否可区分"。

#### 适用场景

- Theory 含 H3 型 meta-hypothesis：[内嵌构念] 的效应比 [受众认知构念] 的效应**衰减更慢**
- 两条通道与时间（age）的交互系数方向都为正（因为负向通道的主效应为负，age 交互为正意味着负效应被侵蚀）
- 主模型为生存分析或非线性模型，交互项以 hazard/系数形式呈现

#### 报告骨架

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

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. Mean-center 时间变量 | center [age] before interaction | 提升主效应可解释性，不改变交互系数 |
| 2. 报告两个 time×channel 交互 | 方向都为正时仍需解释衰减 | 正向通道主效应+→ age 交互+ = 增强；负向通道主效应−→ age 交互+ = 侵蚀 |
| 3. Reverse-code 负向通道 | 使两系数同向 | Wald test 才可直接比较幅度 |
| 4. Wald test | 检验两交互系数差异 | 统计判定"持续性差异"是否成立 |

#### 反模式

- **不 reverse-code 直接比较**：一正一负的系数无法用 Wald 比较"哪条衰减更慢"
- **混淆"占优"与"持续"**：本检验回答的是"哪条通道的时间动态更陡"，而非"哪条通道当前更强"——后者是 net effect，前者是 persistence meta-hypothesis
- **断点/分段不一致**：若主模型用 piecewise 分段，reverse-code + Wald 应在同一分段设定下进行

#### 语料锚定

- qiao_hiatt_sine2026 (SMJ) — H3：内嵌 capability imprint 比外部 identity imprint 更持久。age×capability (+0.060) vs age×identity (+0.080)，reverse-code 后 Wald χ²=60.08, p<.001。配合 `../write-theory/corpus/sentences/mechanism_chain.md` "双重印记对立通道" 模板使用。

### 变体 5: Reverse-Order Mediation Sensitivity Test（竞争排序敏感性检查）

**来源论文**: Ilicic & Brennan 2026 (Journal of Marketing) Study 4
**验证状态**: EMERGING
**写入日期**: 2026-07-22
**槽位**: R6/R7

#### 功能描述

当 Theory 提出序列中介 [IV] -> [M1] -> [M2] -> [DV]，读者会追问"为什么是 M1->M2，而不是 M2->M1？"Reverse-order test 将两个中介交换后重新估计间接路径。若反向路径的 bootstrap CI 含零，只能说明样本没有为该替代序列提供清晰证据；它与提议排序相容，但不能单独排除替代顺序，更不能确认时间或因果方向。显著路径与不显著路径的差异本身也未必显著。

#### 适用场景

- 序列中介假设（X->M1->M2->Y）且 M1、M2 理论上可互换顺序
- measurement-of-process 设计（测量而非操纵中介）——可将反向模型作为竞争解释的敏感性检查，但必须另寻时间分离、操纵或纵向证据
- 区别于上方变体 4（qiao2026 "Reverse-Code + Wald"）：那是把两条**方向相反通道** reverse-code 后比较时间持续性（differential persistence）；本节只比较**同一序列中两个中介的位置**，不构成 causal-ordering confirmation

#### 报告骨架

```
To probe a competing ordering of the variables, we conducted a second serial mediation
analysis reversing the order of the mediators ([Fairchild and McDaniel 2017]), testing
whether [predictor] was associated with [M2_reversed], which in turn was associated with
[M1_reversed], and subsequently with [outcome]. The results showed that the 95%
bootstrapped CI for the indirect effect of [predictor] on [outcome] included zero
(effect = [value], SE = [value], 95% CI = [[lower], [upper]]), indicating no significant
serial mediation effect. The data therefore provide no clear evidence for this competing
sequence. Together with the theoretical argument and any temporal or experimental evidence,
this pattern is more consistent with the proposed ordering; by itself, however, it does not
establish temporal or causal order.
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 报告正向序列间接效应 | bootstrap CI 不含零 | 建立主假设支持 |
| 2. 反转中介顺序重测 | M2->M1 而非 M1->M2 | 构造竞争因果排序 |
| 3. 报告反向间接效应 | CI 含零 | 说明未检测到该竞争序列，不写"排除" |
| 4. 一句话收束 | "consistent with the proposed ordering, but not causal proof" | 将敏感性证据与识别边界同时交代 |

#### 反模式

- **把一显著、一不显著写成两者显著不同**：必须直接检验两个间接效应的差异，不能比较星号
- **把反向不显著写成确认因果顺序**：横截面 PROCESS 无法建立时间优先性；结果变量若先于中介测量，限制更强
- **只报正向序列不讨论竞争顺序**：若两个中介理论上可互换，应报告竞争模型，但结论保持为敏感性而非排除
- **混淆 reverse-order test 与 reverse-code**：reverse-order 反转中介位置（顺序问题）；reverse-code 改变变量符号（方向比较问题）——两者统计逻辑完全不同
- **用 reverse-order test 替代操纵或时间分离**：它可以补充 measurement-of-process，不能替代更强的机制识别

#### 语料锚定

- ilicic_brennan_2026_jm (Journal of Marketing) — Study 4：political ideology -> sense of agency (M1) -> perceived product danger (M2) -> gambling severity。正向间接效应 CI [.01, .02]；反转顺序后 CI [-.01, .01] 含零。该结果支持"提议排序更符合数据"的有限表述，但不能确认 agency->danger 的因果顺序；主文中 gambling severity 还先于两个中介测量。配 measurement-of-process 设计（见 `../write-methods/econometric-models/实验.md` 变体6）。

### 变体 6: 事件条件间接效应分层报告（直接交互不一致时）

**来源论文**: Reinwald, Kanitz, Bamberger, Backmann & Hoegl 2026 (Organization Science)
**验证状态**: EMERGING
**槽位**: R4

#### 验证状态说明

EMERGING（单篇来源；仅作 `section_variant`）。适用于回归/path model/多层模型中的 moderated mediation，不要求估计器一定是 SEM。

#### 报告骨架

```text
The [X × event] interaction on [mediator] was [coefficient and CI/p], indicating that [X] reduced [mediator] after the event but not before it. [Mediator] was associated with [outcome] in the predicted direction. The bootstrapped conditional indirect effect of [X] on [outcome] through [mediator] was [effect, 95% CI] after the event and [effect, 95% CI] before the event. Thus, the evidence supports an event-contingent indirect pathway. The direct [X × event] effect on [outcome] was [status]; accordingly, we do not claim that the direct behavioral interaction replicated across studies.
```

#### 强制顺序

1. 报告 `X × event → M`，再报告 `M → Y`。
2. 分别给出事件前与事件后的 conditional indirect effect 及 bootstrap CI；不能只报差值 index。
3. 单独报告 direct interaction 与 total effect 的状态。
4. 若使用两个机制维度/两个行为 DV，逐一列出，不挑选显著组合。

#### 语料锚定

- Study 2：事件后通过 social mindfulness 的间接效应对 lying 为 `.28 [.10, .50]`、对 forward-looking behavior 为 `-.15 [-.27, -.05]`；事件前区间均跨零。
- Study 3：事件后 perspective-taking 路径分别为 `.09 [.03, .16]` 与 `-.05 [-.10, -.02]`，empathic-concern 路径分别为 `.09 [.03, .16]` 与 `-.08 [-.14, -.03]`；四个事件前区间均跨零。

#### 诚实边界

- 显著间接效应在统计上不要求显著 total/direct effect；但它只支持条件性机制路径，不能把不显著 direct interaction 改写为"行为效应已复制"。
- `M → Y` 若与结果同时测量，因果方向仍依赖理论与设计，bootstrap CI 不会自动解决中介内生性。
- 若上游 threat 只在理论或补充研究中测量，主文的经验中介链应从实际观测到的 proximal mediator 开始。

### 变体 7: 共享中介跨异质结果分支的证据账本

**来源论文**: Kashmiri, Nicol & Arora 2017 (Journal of the Academy of Marketing Science)
**验证状态**: VERIFIED
**写入日期**: 2026-08-03
**槽位**: R3


### 变体 8: 两步预测中介 + 双 moderator 条件间接效应 + 双路径汇合（post_2022_women_tmt_strategic_renewal 型）

**来源论文**: Post, Lokshin & Boone 2022 (AMJ)
**验证状态**: VERIFIED（expert_audit_override, user 2026-08-29）
**槽位**: R8（承接 R3/R4 双路径铺垫；收敛全篇双路径回答）

#### 适用场景

- 面板 OLS/一阶差分设计：中介由第一阶段模型生成预测值（fitted/predicted shift），代入第二阶段 outcome 模型——区别于变体 1 的 SEM 同时估计
- 理论含两条并行机制路径（X→M1→Y1 与 X→M2→Y2），各配一个 moderator
- 粗粒度二手数据 + moderated mediation，统计功效受限时的校准主张

#### 报告骨架

```text
Hypothesis [H6] anticipated that, following [treatment], [outcome_A] would [grow] via an
[increase] in [mediator_A]. Supporting Hypothesis [H6] (Table [X], Model [N]), the
estimated coefficient for the predicted shift in [mediator_A] (obtained from Model [M] in
Table [Y]) is statistically significant (b = [value], p = [value]). That is, our model
predicts that a large shift (one standard deviation increase) in [mediator_A]
[increases/decreases] [outcome_A] by [value]%.
[H7 段镜像：另一条路径 → 另一 outcome，指明"via a drop in [mediator_B]"]
To assess whether the shifts in [mediators] in fact mediate the relationships between
[treatment] and [outcomes], we use the procedure described in [Preacher, Rucker, and
Hayes (2007)]. Because we have moderated mediations, we use the predicted change in
[mediator_A] and [mediator_B] from Models [M1] and [M2] for the [moderator_1] moderator
(and from Models [M3] and [M4] for the [moderator_2] moderator) in the [outcome] models.
Using bias-corrected confidence intervals for the two indirect effects, we find that the
indirect effects of [treatment] (a) on [outcome_A], via a [rise] in [mediator_A], and
(b) on [outcome_B], via a [drop] in [mediator_B], are statistically significant
(z = [value], p = [value]; z = [value], p = [value], respectively) when [moderator
condition].
Given the difficulties, statistically, in detecting moderated mediation in analyses
relying on coarse-grained, secondary data, we interpret our pattern of findings as
consistent with our theory that [treatment] affects [outcome], at least partially, via
shifts in [mediators], conditional on [moderator_1] and [moderator_2].
```

#### 关键技术点

| 步骤 | 操作 | 理由 |
|------|------|------|
| 1. 路径承载归因句 | "H6 anticipated that ... would grow **via an increase in [M1]**" | 明示哪条路径承载哪个结果，双路径汇合不被误读 |
| 2. 预测值溯源 | "(obtained from Model [M] in Table [Y])" | 两步法生成的 regressor 必须可溯源 |
| 3. moderator×模型映射 | 指明条件间接效应用哪组模型生成的预测值 | 双 moderator 设计时审计链不断裂 |
| 4. 双间接效应并行报 CI | (a)/(b) 编号并行，z 与 p 成对 | 两条路径一次汇合，避免叙事偏倚 |
| 5. 校准收束句 | "consistent with ... at least partially ... conditional on ..." | 以功效限制为由把主张压到"部分、条件性" |

#### 诚实边界

- 两步预测中介存在 generated-regressor 问题：第二阶段 SE 未反映第一阶段不确定性，主张强度须与该校准匹配（本篇以"at least partially"收束即为例范）。
- SEM 稳健性检验允许残差相关时，不得把"多数残差相关不显著"写成识别有效性的确证（本篇"confirming the validity of our approach"表述偏乐观，仅作节奏参照不作结论模板）。
- 间接效应仅在 moderator 条件成立时显著（本篇 incumbency>0 显著、小 cohort 边缘显著）——须按条件分层报告，不得汇总为主效应中介。

#### 原文锚定
- "Because we have moderated mediations, we use the predicted change in TMT risk-taking propensity and TMT change orientation from Models 6 and 8 for the incumbency moderator (and from Models 11 and 13 for the cohort size moderator) in the M&A and R&D models."（results.md 中介段）
- "Given the difficulties, statistically, in detecting moderated mediation in analyses relying on coarse-grained, secondary data, we interpret our pattern of findings as consistent with our theory that female TMT appointments affect strategic renewal, at least partially, via shifts in TMT cognition, conditional on TMT female incumbency and on the (small) size of the incoming TMT cohort."（results.md 收束段）

#### 与最近变体的区别
- 区别于变体 1（Preacher & Hayes 同时估计 SEM）：本变体是两步预测中介的面板 OLS 版本 + 双 moderator 条件间接效应分层 + "路径承载归因 → 双路径汇合 → 校准收束"的跨槽位节奏；区别于变体 7（共享中介跨分支账本）：本变体两条路径各配独立中介与 outcome，按承诺顺序汇合。

#### 验证状态说明

EMERGING（单篇来源；仅作 `section_variant`）。适用于同一中介被理论化为连接一个 predictor 与多个 outcome，且各 outcome 使用不同估计器或量纲。

#### 报告骨架

```text
We evaluate the proposed mediator separately for each outcome branch. The a-path from
[X] to [M] is reported once. For [Y1], the estimated indirect effect is [effect, CI],
supporting [H1b]. For [Y2], the interval [includes/excludes] zero, so [H2b] is [not]
supported even though the direct association between [X] and [Y2] is [status]. For [Y3],
the indirect effect is [effect, CI], supporting [H3b]. Thus, [M] transmits the relationship
to [supported branches], but the evidence does not show that it explains the full outcome
portfolio. We retain the unsupported branch as a mechanism boundary rather than treating
the significant direct effect as a substitute for mediation evidence.
```

#### 强制证据账本

| 分支 | 直接关系 | 间接效应与区间 | 假设判定 | 可写结论 |
|------|----------|----------------|----------|----------|
| `[Y1]` | `[status]` | `[estimate, CI]` | 支持/不支持 | `[M]` 部分传递该分支 |
| `[Y2]` | `[status]` | `[estimate, CI]` | 支持/不支持 | 直接关系不能挽救失败的中介假设 |
| `[Y3]` | `[status]` | `[estimate, CI]` | 支持/不支持 | 仅对该分支声明中介 |

#### 为什么有效

1. 把"一个共同中介"拆成多个可证伪的间接效应，避免用总体叙事覆盖分支差异。
2. 先共享 a-path，再逐 outcome 报 b-path/indirect effect，减少重复同时保留完整审计链。
3. 失败分支为 Discussion 提供精确边界：同一组织导向未必通过同一过程塑造速度、创新性与安全性。

#### 诚实边界

- Kashmiri et al. 的主分析使用 PROCESS/binary-mediation 与传统 causal-steps 语言；当前写作应优先报告估计的 indirect effect、bootstrap/Monte Carlo CI，并说明不同链接函数下的尺度。
- 不同 outcome 使用负二项、fractional logit 与 logit 时，间接效应不能直接比较原始系数大小；应使用兼容的边际量或分别解释。
- `partial mediation` 只说明直接路径仍存在，不证明遗漏机制的具体内容。
- 传统 Baron–Kenny 条件计数不能替代 moderated-mediation index 或条件间接效应区间。
