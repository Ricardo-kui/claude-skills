---
result_type: "Logit-Probit-Ordered-Probit"
status: 📋 TEMPLATE
source_papers:
  - "pfarrer_pollock_rindova_2010_tale_of_two_assets_amj (Academy of Management Journal): RE logit odds-ratio reporting, matched-pair hypotheses across positive/negative surprise tables, event-study CAR subgroup comparisons"
  - "malik_wang_martin_gomez-mejia_2025_mixed_gambles_jm (Journal of Management): Heckman probit two-stage + marginal effects CI-based testing + 1-SD→percentage point economic significance + dual DV parallel reporting"
  - "bendig_hensellek_schulte_2024_etp (Entrepreneurship Theory and Practice): binary-GEE inverted-U formal test + dual parallel curves + shift-vs-steepen differential moderation + probability-to-cost benchmark + threat-indexed robustness"
  - "lee_park_2024_giving_up_learning_smj (Strategic Management Journal): fractional-logit inverted-U evidence chain + turning-point-shift moderation + selective-path mechanism corroboration"
  - "hoffmann_cheong_phan_zurbruegg2024_jm (Journal of Marketing): DiD+conditional logit OR→relative probability + low-base-rate honesty + moderator attenuation % + two-step rival exclusion"
  - "lunetal2026 (Entrepreneurship Theory and Practice): Kitazawa semi-elasticity for conditional logit; AME grid with sign reversal; industry-within permutation null; system GMM on same binary DV; post-hoc QMS proxy"
  - "liuliuluo2016 (Journal of Marketing): hit rate vs PCC+25% premium; spillover-null for tenure interactions; probit exogeneity battery; Heckman-on-CAR relevance; total-effect bands; level vs proportion compensation"
variants_count: 29
created: 2026-05-18
updated: 2026-08-13
---

# Logit-Probit-Ordered-Probit — Results 骨架

## 变体速查表

> 检索辅助。状态词表（与 _evidence_registry.yaml 一致）：ROBUST > VERIFIED > EMERGING（含（可选）后缀）；LEGACY-DIAGNOSTIC 保留（工具诊断类）；召回主题条目按用户 2026-08-29 裁决单源 VERIFIED。完整骨架与诚实边界见下方变体正文。

### 槽位分布

| 槽位 | 变体数 | 变体编号 |
|---|---|---|
| R1 | 1 | 1 |
| R2 | 2 | 5, 24 |
| R3 | 7 | 2, 6, 8, 9, 14, 17, 19 |
| R4 | 6 | 3, 10, 12, 18, 20, 28 |
| R5 | 2 | 7, 15 |
| R6 | 1 | 25 |
| R7 | 7 | 4, 11, 16, 21, 22, 26, 29 |
| R8 | 3 | 13, 23, 27 |

### R1（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 1 | R1 四合一密集开场（描述统计+诊断+估计器+报告惯例） | 篇幅受限时把描述统计、共线性诊断、估计器声明、OR 报告惯例压成一段开场 | AMJ 风格高密度压缩——替代标准分节式 R1 | EMERGING | Pfarrer et al. 2010 AMJ |

### R2（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 5 | R2 Heckman 第一阶段表格 + 逆米尔斯比率进入第二阶段 | Heckman 作主识别策略时：第一阶段表格+instrument relevance+IMR 进入第二阶段声明 | 与 OLS/FE 的 R2（Model 1→2→3 递进）结构完全不同 | VERIFIED | Malik et al. 2025 JM |
| 24 | R2 hit rate vs PCC + 25% premium | 单方程二元模型：伪 R² + hit rate 对比例机会基准与 25% 溢价 | 区别于变体 5（Heckman 第一阶段表）：本变体是分类准确度导航，不是选择方程 | EMERGING | Liu, Liu & Luo 2016 JM |

### R3（7）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 2 | R3 Logit 主效应四拍（odds ratio + likelihood 翻译） | Logit 主效应：方向→OR+p→likelihood 翻译→支持判断 | 变体14 在其上强制加低基准诚实句与 stakes；本变体为纯四拍 | ROBUST | Pfarrer et al. 2010 AMJ |
| 6 | R3 Probit 边际效应 CI 检验（"CI does not cross zero" 支持标准） | 概率模型系数不可直接解释时以 AME 图 CI 不跨零作支持标准 | 与变体7 配套——检验标准放 CI、经济显著性单独成句 | VERIFIED | Malik et al. 2025 JM |
| 8 | R3 双 DV 平行对称报告 | 两个 IV 对同一 DV 对称反向预测时同段平行报告 | 与变体17 的区别——线性双 IV 平行 vs 双焦点倒 U 平行 | VERIFIED | Malik et al. 2025 JM |
| 9 | R3 Binary-GEE 曲线完整检验链（二次项→端点斜率→Fieller 区间） | 二元结果倒 U 完整证据链：二次项→U-test→拐点区间→预测概率图 | 与变体17 区别——单 IV 完整链 vs 双 IV 并列表；须标注 link/response 尺度 | VERIFIED | Bendig et al. 2024 ETP |
| 14 | R3 DiD+Logit 主效应（OR→相对概率 + 低基准诚实 + stakes） | 稀有二元结果（recall/fraud/退市）：相对概率+低基准 modest 诚实句+stakes | 变体2 之上强制低基准诚实句与 stakes 论证 | VERIFIED | Hoffmann et al. 2024 JM |
| 17 | R3 双焦点 IV 平行倒 U（分模型→联合模型→并列表 U-test） | 两个焦点 IV 对同一不利结果同形倒 U 的平行展演 | 与变体8 区别——双倒 U vs 线性双 IV；与变体9 区别——双 IV 并列表 vs 单 IV 链 | VERIFIED | Bendig et al. 2024 ETP |
| 19 | R3 条件Logit Kitazawa 半弹性幅度拍 | 稀有二元条件Logit：方向+显著性后用平均半弹性作幅度，而非 OR | 区别于变体2（OR→likelihood）与变体14（OR→相对概率+低基准诚实） | EMERGING | Lun et al. 2026 ETP |

### R4（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 3 | R4 事件研究 CAR 分组比较（非参数验证+t检验替代回归交互） | 理论预测离散类别序位差异时：分组均值比较+paired t 检验替代回归交互 | 先非参数验证 CAR 行为正常再做子组 t 检验——无需交互项 | EMERGING | Pfarrer et al. 2010 AMJ |
| 10 | R4/R5 条件曲线几何翻译 + 概率—成本—价值 benchmark | 单 IV 条件曲线：几何词汇（上移/变陡/拐点移动）+外部成本 benchmark 转管理后果（副槽位 R5） | 与变体12 的区别——一般几何翻译 vs 转折点位置型强制差异检验 | VERIFIED | Bendig et al. 2024 ETP |
| 12 | R4 转折点位置型调节（条件顶点 + 直接差异检验） | 理论明确预测拐点位置移动：报双顶点+差值+直接检验作主句 | 与变体10 互补——强制顶点差与直接检验而非只报交互显著 | VERIFIED | Lee & Park 2024 SMJ |
| 18 | R4 同调节双模式几何对比（shift vs steepen 分图裁决） | 同一调节对两 IV 预测不同几何（shift/steepen）时分图裁决+"同调节异几何"收束（副槽位 R5） | 与变体10 的区别——单 IV 几何 vs 双 IV 几何对比；交互同号不裁决几何 | VERIFIED | Bendig et al. 2024 ETP |
| 20 | R4 AME 网格把 weaken 推进到符号反转 | H 只预测 weaken 时：交互负显著 → AME 网格 → Interestingly 标反转（须标边际） | 区别于变体15（衰减%无反转） | EMERGING | Lun et al. 2026 ETP |
| 28 | R4 总效应带 + 两水平预测概率 | 无 AME 网格时：主效应+显著交互合成总效应带，再画两水平预测概率 | 不替代 Malik AME（变体 6/7）或 Lun 反转网格（变体 20） | EMERGING | Liu, Liu & Luo 2016 JM |

### R6（1）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 25 | R6 spillover-null：主效应成立但交互不溢出 | 调节主效应显著、对应交互 null：当场 do not support + does not spill over | 禁止藏 null；区别于只报显著交互 | EMERGING | Liu, Liu & Luo 2016 JM |

### R5（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 7 | R5 Probit 经济显著性（1-SD → 概率百分点变化） | probit/logit 经济显著性：1-SD 从均值→X%→Y% 概率变化，一句完成 | 与变体15 的区别——1-SD 概率变化 vs 25th→75th 处理效应衰减 % | VERIFIED | Malik et al. 2025 JM |
| 15 | R5 调节 — 25th→75th 处理效应衰减 % | 三向 DiD 交互配套：moderator 25th→75th 时处理效应衰减 %（副槽位 R4） | 与变体7 的区别——处理效应衰减 % vs 1-SD 概率变化 | VERIFIED | Hoffmann et al. 2024 JM |

### R7（5）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 4 | R7 GEE 补充回归 + Heckman 两阶段内生性纠正 | R7 补充回归+Heckman 两阶段报告，两段均保留诚实声明 | 与变体16 的区别——GEE/Heckman 结构 vs 理论 rival 两步排除 | EMERGING | Pfarrer et al. 2010 AMJ |
| 11 | R7 曲线关系的六威胁稳健性梯 | 曲线结果稳健性按六类威胁映射（lag/DV/估计器/测量/样本/内生性） | 与逐表罗列的区别——按威胁组织；5%→10% 降档如实报告 | VERIFIED | Bendig et al. 2024 ETP |
| 16 | R7 替代解释 — CONTROL + INTERACT 两步 + need/willingness 收束 | DiD/Logit 设计区分 observable need vs latent willingness 的 rival 排除 | 与变体4 的区别——理论 rival 两步排除 vs Heckman/GEE 结构 | VERIFIED | Hoffmann et al. 2024 JM |
| 21 | R7 行业内置换连续 IV 的抽样威胁 null 图 | 保持数据结构、行业内重分配连续 IV，生成 null 分布对照实际系数 | 区别于 DiD 置换处理时点 | EMERGING | Lun et al. 2026 ETP |
| 22 | R7 同二元 DV 的 system GMM（交互项作内生） | 稀有二元主分析的内生性 precaution：保持同一 DV，两向/三向列为内生 | 区别于计数模型换连续 DV 再 GMM | EMERGING | Lun et al. 2026 ETP |
| 26 | R7 probit 外生确认电池（设计拆联立 + CLR/Hansen + Wald/CF） | 观测 probit 的薪酬/激励内生性：先论证联立不成立，再 IV 诊断，Wald+CF 双路径 fail-to-reject 后留守主估计 | 区别于变体 22（GMM precaution）与变体 4（Heckman 纠正） | EMERGING | Liu, Liu & Luo 2016 JM |
| 29 | R7 水平 vs 比例测量 | 激励构念：水平/金额优先，比例作 confirmatory | 区别于变体 26（内生性电池）：本变体是测量威胁，不是识别威胁 | EMERGING | Liu, Liu & Luo 2016 JM |

### R8（2）

| # | 变体 | 适用场景 | 区别 | 状态 | 来源 |
|---|---|---|---|---|---|
| 13 | R8 曲线机制的选择性路径辨析（激活一条机制而不激活另一条） | 机制分工检验：选择只激活一条机制的对照暴露，linear 显著而平方项 null | 与泛化 additional analysis 的区别——证据对应曲线两段机制分工；措辞限 consistent with | EMERGING | Lee & Park 2024 SMJ |
| 23 | R8 post-hoc 机制代理另 DV（限 aligns with） | 不可观测过程用认证/系统类代理另 DV，与稳健性分节 | 区别于变体13（曲线两段对照暴露）；不是 mediation | EMERGING | Lun et al. 2026 ETP |
| 27 | R8 Heckman-on-CAR 管理相关性 | 主 probit 作选择方程，Heckman 估选择→CAR；负向市场反应对照消费者 | 区别于变体 23（机制代理另 DV）与变体 5（Heckman 作主识别）：本变体是补充相关性，不是假设检验 | EMERGING | Liu, Liu & Luo 2016 JM |

## 主骨架

参见 `write-results/SKILL.md` → 槽位骨架加载 → 本类型适用的 `references/slot-R*.md`（各 slot 文件内含 `Logit-Probit-Ordered-Probit` 专用变体）。

## 证据节奏摘要

<!-- 由 distill-results-exemplar 首次蒸馏后填充 -->

## 累积变体

<!-- distill-results-exemplar Phase 4 验证通过的变体写入此处 -->
<!-- 格式：
### 变体 N: [来源论文] (YYYY-MM-DD)
**验证状态**: 通过 / 需修正
**槽位**: R?
**骨架**:
> "..."
**与原骨架差异**: ...
-->

### 变体 1: R1 四合一密集开场 — 描述统计+诊断+估计器+报告惯例 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Table 1 presents descriptive statistics and a correlation matrix for the variables used in testing our hypotheses. The means and standard deviations reflect values for raw rather than transformed measures. All variance inflation factors were below five, with an average of 2.4. Thus, multicollinearity is not a concern (Chatterjee & Price, 1991; Pedhazur, 1997). … We report odds ratios to allow easier interpretation of the magnitude of effects. An odds ratio greater than one indicates the likelihood that an event will occur increases with a one-unit increase in the independent variable."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R1
**骨架**:
> [Table X] presents descriptive statistics and a correlation matrix for the variables used in testing our hypotheses. The means and standard deviations reflect values for raw rather than transformed measures. All variance inflation factors were below [threshold], with an average of [value]. Thus, multicollinearity is not a concern. We estimated [random-effects logit] because [justification]. We report odds ratios to allow easier interpretation. An odds ratio greater than one indicates the likelihood increases with a one-unit increase in the independent variable; an odds ratio less than one indicates the likelihood decreases.
**与原骨架差异**: AMJ 风格的高密度 R1——将描述统计、诊断、估计器声明、报告惯例四合一压缩为一段。适用于篇幅受限的顶刊。

### 变体 2: R3 Logit 主效应四拍 — odds ratio + likelihood 翻译 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "For positive surprises, Table 2 shows that high-reputation firms had an odds ratio of 0.48 (p < .01), which means they were less likely to generate a positive earnings surprise than firms that did not possess high reputation. However, Table 3 shows high reputation did not have a significant effect on the likelihood of negative surprises. Thus, Hypothesis 1a was supported, and Hypothesis 1b was not."
**验证状态**: ROBUST
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> Hypothesis [N] predicted that [IV] would be [positive/negative] associated with [DV]. [Table X] shows that [IV] had an odds ratio of [value] (p < [threshold]), which means [IV] firms were [less/more] likely to [DV] than [reference group]. Thus, Hypothesis [N] was supported.
**与原骨架差异**: Logit 专用 R3。四拍：(1) 方向→(2) odds ratio + p →(3) likelihood 翻译（"were less/more likely"）→(4) 支持判断。非显著版本缩减为三拍：方向→不显著→不支持，省略 likelihood 翻译。

### 变体 3: R4 事件研究 CAR 分组比较 — 非参数验证+t检验替代回归交互 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Initial nonparametric tests (Patell Z and generalized sign) indicated that the market viewed positive earnings surprises favorably (p < .05) and perceived negative earnings surprises as 'bad news' (p < .05). … The CARs for the high-reputation (2.30 percent) and celebrity categories (3.32 percent) were significantly larger than the CAR for the 'none' category (1.74 percent), and the CAR for celebrity was significantly larger than the CAR for high reputation (p < .05)."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R4
**骨架**:
> Initial nonparametric tests ([test names]) indicated that [market/audience] viewed [positive outcome] favorably (p < [threshold]) and perceived [negative outcome] as bad news (p < [threshold]). This pattern is consistent with previous studies. [Table Y] presents the size of each subsample category, the mean [outcome] for [condition A], [condition B], and [reference], the pairwise differences between means, and the significance of these differences based on paired t-tests of unequal variances. The [outcome]s for [condition A] ([value]) and [condition B] ([value]) were significantly [larger/smaller] than the [outcome] for [reference] ([value]). Thus, Hypotheses [X] and [Y] were supported.
**与原骨架差异**: 当理论预测离散类别间的序位差异（high/medium/low）而非连续交互时，分组均值比较+paired t-test 是有效替代——不需要回归交互项。先做非参数验证（Patell Z + generalized sign）确认事件研究指标行为正常，再做子组 t 检验。


### 变体 V: R4 差值列 worked-arithmetic 脚注 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "The difference between the mean CAR in each category is shown (e.g., 2.30% - 1.74% = 0.56%). Significance was determined by a t-test of unequal variances."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: R4
**骨架**:
> [Table note:] The difference between the mean [outcome] in each category is shown (e.g., [mean_A]% - [mean_B]% = [difference]%). Significance was determined by a [t-test] of [unequal variances]. The [baseline] category contains [units] labeled [0] on [both classification dimensions].
**与原骨架差异**: 分组比较表的『Difference』列易被误读为检验统计量——Pfarrer 在脚注里做一个 worked example（2.30%−1.74%=0.56%），一眼教会算法；同脚注打包三件套：差值算法示例 + 显著性检验类型（unequal variances t-test）+ 基线类目操作化定义（none = 在两个分类维度上均标 0）。与正文裁决节奏变体（r4_subgroup_mean_comparison_ttest）分层互补：一个管正文怎么裁，一个管表格脚注怎么自释。适用于任何带组间差值列的均值比较表（CAR 差异表、分组均值表）。

<!-- wb:pfarrer_pollock_and_rindova_2010:r4_worked_arithmetic_difference_footnote -->

### 变体 4: R7 GEE 补充回归 + Heckman 两阶段内生性纠正 (1篇高价值)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Because our tests did not allow us to control for other factors that can affect the size of a CAR, we ran GEE regressions that predicted the magnitude of the three-day CARs while controlling for a variety of other factors (Wade et al., 2006). … Using Bascle's (2008) criteria to select the appropriate estimation approach, we employed a Heckman correction model (Hamilton & Nickerson, 2003; Heckman, 1979). We included predictor variables in the first-stage models that were significantly associated with the likelihood of positive and negative surprises, but not with the CARs. The first-stage models were highly significant in predicting the likelihood of positive and negative surprises, but the selection correction instrument was not significant when entered into the second-stage models. Thus, endogeneity did not appear to be a significant problem in our study (Bascle, 2008; Mesquita & Brush, 2008; Tong, Reuer, & Peng, 2008)."
**验证状态**: EMERGING
**写入日期**: 2026-07-07
**槽位**: R7
**骨架**:
> Because our [primary] tests did not allow us to control for other factors that can affect the [size/magnitude] of [outcome], we ran [alternative estimator] regressions that predicted the [magnitude] of [outcome] while controlling for [factors]. It is important to note that these regressions do not directly test Hypotheses [X–Y], which address [original theoretical comparison]. Instead, the regressions examined if [IV_1] and [IV_2] had direct relationships with [outcome_magnitude]. We found that [IV_1] (b = [value], p < [threshold]) and [IV_2] (b = [value], p < [threshold]) had [positive/negative], significant relationships with [outcome], and their inclusion significantly improved the fit of the model.
>
> We also investigated whether endogeneity due to unobserved variables might have influenced our results. Using [Author_Year]'s criteria to select the appropriate estimation approach, we employed a [Heckman/two-stage] correction model. We included predictor variables in the first-stage models that were significantly associated with [selection_DV], but not with [outcome_DV]. The first-stage models were highly significant in predicting [selection_DV], but the selection correction instrument was not significant when entered into the second-stage models. Thus, endogeneity did not appear to be a significant problem in our study.
**与原骨架差异**: Pfarrer 的 R7 展现了两段式稳健性结构：补充回归的诚实声明 + Heckman 两阶段标准报告。两个段落的共同特征是在呈现补充证据时都保留了诚实声明。






### 变体 U: R4 非参数等价裁决 + 基线符号对比段节奏 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "The nonparametric tests indicated that the CARs for reputation and celebrity were not significantly different from their predicted values, but the CARs for firms in the 'none' category were significantly different."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: R4
**骨架**:
> Both [group_A] and [group_B] firms had slightly [positive] average [outcome] ([mean_A] and [mean_B], respectively), whereas firms in the [baseline] category had a significant, [negative] mean [outcome] ([mean_C]). The [nonparametric tests] indicated that the [outcome] for [groups A and B] were not significantly different from their predicted values, but the [outcome] for firms in the [baseline] category were significantly different. The [t-tests] showed that the mean [outcome] for [group A] and [group B] were significantly different from the [baseline] category's mean [outcome] and that the [outcome] for [group A] and [group B] were not significantly different from one another. Thus, Hypotheses [X]a and [X]b were supported, and Hypothesis [X]c was not.
**与原骨架差异**: 非参数检验（Patell Z / generalized sign）在语料中只收了主比较前的行为 sanity check 用法（r3_eventstudy_nonparametric_validation）——本变体是第二用法：在假设裁决段内部，用非参数检验把『处理组结果≈预测值（等价）』与『基线组显著偏离预测』分开陈述，再接参数 t 检验的组间差异，两个检验家族三角互证。段首另有一拍 whereas 符号对比（处理组微正 vs 基线显著负）为裁决铺垫；段尾拆分裁决自然带出 Hc 的不支持（两组彼此无差异）。适用于任何『处理组 vs 基线』分组比较的裁决段，尤其是『处理组表现符合预期、基线偏离』的等价性论证。

<!-- wb:pfarrer_pollock_and_rindova_2010:r4_nonparametric_equivalence_adjudication -->

### 变体 S：滞后结构括弧敏感性（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "In separate analyses, we examined whether the results were sensitive to this particular lag structure by examining the effect of [the predictor] over a more recent, [N]-year period ([t-2] to [t-1]) and over a [N+2]-year period ([t-4] to [t-1]). The results presented below were substantively unchanged, suggesting that our findings are not sensitive to the particular lag structure used in the models."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Analysis §Analyzing Increased Board Control Structure（P1 末）

**原文锚定**:
> "The results presented below were substantively unchanged, suggesting that our findings are not sensitive to the particular lag structure used in the models."

**关键特征**:
- 滞后窗以括弧形式向两侧外推（主窗 3 年 → 短 2 年 + 长 4 年），单向选择变双向夹逼——"结果对窗宽不敏感"的声明有了对称证据结构
- "The results presented below" 的前向定位：敏感性检验在 Analysis 报告、结果指向后文主表——1990s 的 Analysis/Results 分离惯例下，稳健性预告嵌入模型规格段
- "suggesting that our findings are not sensitive to..." 的结论句把检验目的（lag 结构任意性）显式复述——稳健性不仅"没变"，还说明"没变意味着什么"

**适用**: 时变预测变量滞后窗存在任意性的面板/事件史设计（治理变化、政策采纳扩散类）；主窗选择需向审稿人证明非 cherry-picking 的场景

**禁忌**: 括弧两端窗须落在机制实质时间尺度内（本篇由董事任期合同 1-3 年论证 3 年主窗），窗宽外推无实质依据则检验无意义；短窗结果若因机制延迟而显著变弱，不得以"方向一致"掩盖幅度差异

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 R：双 DV 收敛 + 理论标签现造（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "Taken together, these results suggest that there is not only a [substantive] substitution effect between [mechanism A] and [mechanism B], but also a [symbolic] substitution effect, whereby even a [decoupled form of A] can forestall [the outcome]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Results §Tables 3-4 P1（段末收束）

**原文锚定**:
> "Taken together, these results suggest that there is not only a substantive substitution effect between the use of incentives and monitoring, but also a symbolic substitution effect, whereby even a decoupled LTIP adoption can forestall changes in governance."

**关键特征**:
- "not only... but also..." 递进式标签现造：双 DV（职位分离 + 外部董事比率）各自支持后，一段末用对偶句把结果提升为新理论标签（symbolic substitution effect）—— Results 段内完成概念命名，Discussion 免于重复
- "Taken together" 收束词明确标记证据聚合动作，标签由两表共同背书而非单一模型
- "whereby even a decoupled..." 从句把标签的适用条件（形式采纳即可）内嵌进命名句——标签自带边界

**适用**: 双 DV（同一理论机制的两类后果）同时检验的设计；结果支持一个可命名的新机制（替代/挤出/信号）时

**禁忌**: 标签现造须两 DV 证据均成立且方向一致，单 DV 支撑不得用 "Taken together" 包装；现造标签须与既有文献概念（本篇 substantive substitution）对偶衔接，不得凭空造词

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 Q：四格系数差异的 Wald 正式确认（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We also used the Wald test to confirm that coefficients for [category with W] were significantly greater than coefficients for [category without W] (e.g., chi-square = [value] and p ≤ [threshold] for [group A] with vs. without [the moderator] in predicting [DV1]; F = [value], p ≤ [threshold], for the same comparison in models predicting [DV2]) ([citation]). Thus, [the moderator] decreased the likelihood of [the outcome], irrespective of whether [the implementation condition]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Results §Tables 3-4 P2（Wald 确认句）

**原文锚定**:
> "We also used the Wald test to confirm that coefficients for adoption with an agency explanation were significantly greater than coefficients for adoption without an explanation (e.g., chi-square = 5.09 and p ≤ .05 for symbolic adoption with an explanation vs. symbolic adoption without an explanation in predicting CEO/chair separation)."

**关键特征**:
- "to confirm that" 的定位：四格系数大小对比（目视排序）之后追加正式差异检验——排序证据升级为统计证据，调节裁决从暗示变确证
- 双 DV 双统计量并列报告（chi-square=5.09 用于 logit 事件史；F=15.98 用于 GLS 面板），各自带引用（Judge and Yancey 1986）——同一调节假设在两类估计器下分别确认
- "e.g." 引入代表例：完整检验组多于报告数（四格两两比较多对），只举关键对比——避免检验报告淹没主叙事

**适用**: 四格哑变量/分组系数设计的调节效应正式确认；同一假设跨多估计器（logit + 面板 GLS）复现的报告

**禁忌**: Wald 对比的自由度与协方差来源须可追溯（本篇引 Judge and Yancey 1986 的检验方法），不得裸报 chi-square；"e.g." 省略的其余对比须方向一致，否则必须逐一报告

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 P：四格设计中的 null 格确认性报告（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "Model [2] of table [x] shows a strongly significant negative effect of [the predictor] on [the outcome], for both [category A] and [category B], when [the moderator] is present. Similarly, model [2] of table [y] shows that [category A] with [the moderator] and [category B] with [the moderator] are both strongly and negatively related to [the outcome]. In contrast, model [2] of tables [x] and [y] indicates that both [category A] and [category B] without [the moderator] are generally not significantly related to [the outcomes]. ... Thus, [the moderator] decreased the likelihood of [the outcome], irrespective of whether [the implementation condition]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Results §Tables 3-4 P2

**原文锚定**:
> "In contrast, model 2 of tables 3 and 4 indicates that both symbolic and substantive LTIP adoptions without an agency explanation are generally not significantly related to increases in CEO/chair separation or increases in the outsider ratio."

**关键特征**:
- null 格是假设证据的一部分：四格设计中"有调节显著 + 无调节不显著"共同构成调节假设（H4）的支持——不显著格用 "In contrast" 正面报告而非跳过，null 即确认
- "generally not significantly related" 的强度措辞：两 DV 多模型的 null 汇总不逐一罗列（hedge 措辞承认个别边际情形），支持判断只在汇总层面做出
- 双 DV 并轨导航（"model 2 of tables 3 and 4"）+ "Similarly/In contrast" 对仗连接词——两表四行的证据一段走完，irrespective of whether 尾从句再次回响理论边界

**适用**: 四格哑变量拆分（处理×披露）的回归/离散时间事件史结果报告；null 格承担确认功能的调节设计

**禁忌**: null 格确认逻辑必须由 Methods 侧前置的判定标准（"H# is thus supported if..."）授权，Results 不得事后把 null 追认为证据；"generally" 类汇总措辞若掩盖某一 DV 上方向反转的系数，属选择性报告反模式

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)

### 变体 5: R2 Heckman 第一阶段表格 + 逆米尔斯比率进入第二阶段 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**原始句锚点**: Table 2 presents the first-stage results, where the FDASIA variable exhibits a robust positive coefficient (b = 0.288, p < 0.05), confirming that FDASIA is highly relevant for predicting medical device recalls.
**验证状态**: VERIFIED
**写入日期**: 2026-07-07
**槽位**: R2
**骨架**:
> [Table X] presents the first-stage results, where the [instrument] variable exhibits a robust [positive/negative] coefficient (b = [value], p < [threshold]), confirming that [instrument] is highly relevant for predicting [selection event]. Therefore, the instrument is both conceptually valid and statistically significant for isolating the selection effect. Next, we included the predicted inverse Mills ratio in our regression models. Since our dependent variable is binary, we used [probit/logit] regressions. Following [citation], we employed a clustered correlation structure grouped by [cluster_level] and used robust standard errors.
**与原骨架差异**: Heckman 作为主识别策略时，R2 必须完成三件事：(1) 第一阶段表格（含 instrument 系数+显著性）；(2) 确认 instrument relevance；(3) 声明逆米尔斯比率已纳入第二阶段。与 OLS/FE 的 R2（"Table X Model 1→2→3"）结构完全不同。

### 变体 6: R3 Probit 边际效应 CI 检验 — "CI does not cross zero" 作为支持标准 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**原始句锚点**: The average marginal effect is visualized in Figure 1. The confidence intervals (CIs) of the marginal effects do not cross zero, thus supporting Hypothesis 1a.
**验证状态**: VERIFIED
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> Due to the difficulty in directly interpreting regression coefficients and significance levels in probability models ([citation]), and as hypotheses should not be tested solely by examining p-values ([citation]), the average marginal effect is visualized in [Figure X]. The confidence intervals (CIs) of the marginal effects do not cross zero, thus supporting Hypothesis [N]. A one-standard-deviation increase in [IV] from the mean value ([mean] to [mean+1SD] [units]) [increased/decreased] the probability of [DV] from [X]% to [Y]%.
**与原骨架差异**: Malik 的证据展演有三个独特点：(1) 先引用 Busenbark et al. (2022) 和 Wiersema & Bowen (2009) 建立"probit 系数不可直接解释"的权威背书；(2) 将检验从 p-value 移到 AME 图的 CI——"the CIs do not cross zero, thus supporting H1"；(3) 经济显著性嵌入同一句：1-SD → X%→Y% 概率变化。

### 变体 7: R5 Probit 经济显著性 — 1-SD → 概率百分点变化 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**原始句锚点**: A one-standard-deviation increase in the CEO's current option wealth from the mean value (18.7 to 44.1 million USD) increased the probability of initiating an inattention recall from 23% to 25%.
**验证状态**: VERIFIED
**写入日期**: 2026-07-07
**槽位**: R5
**骨架**:
> A one-standard-deviation increase in [IV] from the mean value ([mean] to [mean+1SD] [units]) [increased/decreased] the probability of [DV] from [X]% to [Y]%.
**与原骨架差异**: 与 OLS 的 "1-SD → N unit change" 或计数的 "e^β−1 = N%" 不同——probit/logit 的经济显著性应翻译为**概率百分点变化**（从 X% 到 Y%），同时给出均值和均值+1SD 的绝对值以锚定读者。一句完成，不需要独立段落。

### 变体 8: R3 双 DV 平行对称报告 (1篇高价值)
**来源论文**: Malik, Wang, Martin & Gomez-Mejia 2025 (Journal of Management)
**原始句锚点**: As Model 5 (Table 4) reports, the coefficient for CEO current option wealth was positive and significant (b = 0.012, p < 0.001). Furthermore, the coefficient for CEO prospective option wealth was negative and significant (b = −0.002, p < 0.01).
**验证状态**: VERIFIED
**写入日期**: 2026-07-07
**槽位**: R3
**骨架**:
> As Model [N] ([Table Y]) reports, the coefficient for [IV_1] was [positive/negative] and significant (b = [value], p < [threshold]). [Figure X] plots the marginal effect, supporting Hypothesis [Na]. A one-SD increase... [changed probability from A% to B%]. Furthermore, the coefficient for [IV_2] was [opposite_sign] and significant (b = [value], p < [threshold]). [Figure Y] visualizes the marginal effect, supporting Hypothesis [Nb]. A one-SD increase... [changed probability from C% to D%].
**与原骨架差异**: 当两个 IV 对同一 DV 有对称反向预测时，在同一段内平行报告——读者无需在表格间跳转。关键：对称的句法（"the coefficient for X was positive... the coefficient for Y was negative"），对称的经济显著性翻译，对称的图示引用。

### 变体 9: R3 Binary-GEE 曲线完整检验链 — 二次项→端点斜率→Fieller 区间 (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: All requirements for inverted U-shapes are met for CVC and alliance activity; the slopes at the low ends (XL) are positive, the slopes at the high end (XH) are negative and the extreme points lie within the Fieller intervals.
**验证状态**: VERIFIED（Bendig 2024 与经用户专家审计的 Lee & Park 2024 构成跨估计器验证）
**写入日期**: 2026-08-04
**槽位**: R3
**骨架**:
> Hypothesis [x] predicted a [U/inverted-U] relationship between [X] and the probability of [binary Y]. The squared term has the predicted sign and is statistically significant in Model [m] (b = [value], p [threshold]), providing the first indication of the hypothesized shape. A formal U-test further shows that the slope at the lower bound of X is significantly [positive/negative], whereas the slope at the upper bound is significantly [opposite]. The estimated turning point is [value], and its [Fieller/bootstrap] confidence interval falls within the observed support of X. Taken together, these joint restrictions support Hypothesis [x]. Figure [f] then plots predicted probabilities across X; coefficients from the logit-link model are not interpreted as probability changes directly.

**与原骨架差异**: 变体2只处理线性 logit 主效应；OLS-FE 的曲线变体要求同类三步，但不能直接搬用线性系数解释。本变体为二元 GEE/logit 明确区分：(1) 链接函数上的系数形状证据；(2) 正式端点斜率与拐点区间；(3) 预测概率展示。

**诚实边界**: 二次项显著不是充分证据；拐点须在有观测支持的范围内。形状检验不能确认理论机制，极端区间稀疏时应展示观测密度或置信带。当 Y 为不利事件（recall、failure、crisis）时，顶点是中间强度的最大风险区，不是绩效曲线意义上的“最优中间”；不得套用 stuck-in-the-middle 的 Discussion 措辞代替概率顶点报告，但应避免把 vertex 写成 desirable optimum。

### 变体 10: R4/R5 条件曲线几何翻译 + 概率—成本—价值 benchmark (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: Market turbulence moderates the relationship between CVC activity and product recall likelihood such that high turbulence shifts the curve up (vertex at 67% and six CVC deals) and low turbulence shifts the curve down (vertex at 52% and eight CVC deals).
**验证状态**: VERIFIED（单篇高价值）
**写入日期**: 2026-08-04
**槽位**: R4 / R5
**骨架**:
> The interaction between [W] and the squared term of [X] is [direction] and significant (b = [value], p [threshold]). Figure [f] shows what this means geometrically: at high W the curve [shifts upward/downward / becomes steeper/flatter], with its vertex at [X, predicted probability], whereas at low W the curve [contrasting shape]. Thus W changes [risk level / learning rate / turning-point location], supporting Hypothesis [x].
>
> To assess substantive magnitude, moving from [baseline X] to [curve location] changes the predicted probability of Y by [Δ percentage points]. Using an externally sourced average event cost of [C] as a transparent benchmark, this probability difference corresponds to an expected-cost magnitude of [Δp × C]. Relative to the average value of one [activity/deal], the implied risk cost is approximately [share]. This calculation illustrates scale; it is not a firm-specific realized-loss estimate.

**与原骨架差异**: 不把曲线调节压缩为“二次交互显著”。先用几何词汇说明究竟是上移、变陡或拐点移动，再把预测概率接到成本与活动价值 benchmark，形成从统计形状到管理后果的完整接力。单 IV 条件曲线用本变体；同一 W 下两 IV 预测不同几何（shift vs steepen）时改用变体 18。

**诚实边界**: 外部平均成本包含情境与测量误差，必须披露来源和假设；不得把期望成本写成已观察因果损失。若 ±1 SD 超出 X/W 支持范围，应使用实际分位数或范围内百分比。X²×W 系数符号本身不能区分垂直平移与变陡；几何裁决必须落到图或条件预测。

### 变体 11: R7 曲线关系的六威胁稳健性梯 (1篇高价值)
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: The squared alliance term showed lower significance at the 10% level. The other results remained stable.
**验证状态**: VERIFIED（单篇高价值）
**写入日期**: 2026-08-04
**槽位**: R7
**骨架**:
> We organize robustness checks by the inferential threat they address. To assess [lag choice], we use [alternative lags/windows]. To preserve information lost by the binary outcome, we estimate [count DV/alternative distribution]. To evaluate estimator dependence, we use [alternative panel estimator]. To assess focal-variable measurement, we replace [count] with [value/alternative proxy]. To test setting dependence, we expand the sample to [additional regulator/industry]. Finally, to probe omitted-variable endogeneity, we estimate [IV/control-function] models and report instrument diagnostics. The curve direction remains stable across these checks, although [specific branch] weakens to [threshold], which we report as reduced evidence strength rather than full invariance.

**与原骨架差异**: 不是按 Table 5/6/7 罗列模型，而是把每项检查映射到时间、DV、估计器、IV 测量、样本边界和内生性六种威胁。特别保留显著性降档，避免选择性胜利。

**诚实边界**: 未报告的工具变量结果只能作为补充，不能承担决定性识别；significance 从 5% 降至 10% 应如实说明。

### 变体 12: R4 转折点位置型调节 — 条件顶点 + 直接差异检验 (1篇高价值)
**来源论文**: Lee & Park 2024 (Strategic Management Journal)
**原始句锚点**: Testing the difference in inverted-U curves' inflection points (e.g., H2a–c) requires computing the inflection points for a given pair of surgeon types based on coefficient estimates and examining whether the two points statistically differs (see Medappa & Srivastava, 2019).
**验证状态**: VERIFIED（Lee & Park 2024 经用户专家审计为位置型曲线调节的典型范文；与变体 10 的一般曲线几何翻译互补）
**写入日期**: 2026-08-04
**槽位**: R4
**骨架**:
> Hypothesis [x] predicted that [W] would move the turning point of the [U/inverted-U] relationship to a [later/earlier] value of X. Model [m] includes both X×W and X²×W; these coefficients determine the conditional curves but do not by themselves adjudicate the hypothesis. The estimated turning point is [x₀, CI] under [condition 0] and [x₁, CI] under [condition 1]. Their difference is [Δx, test statistic/CI, p value], in the predicted direction, and both estimates lie within data-supported regions. Figure [f] plots the conditional predictions on the [response/link] scale with that scale named explicitly. Taken together, this evidence [supports/partially supports/does not support] Hypothesis [x].
**与原骨架差异**: 变体 10 允许一般的曲线平移、变陡或顶点移动；本变体只处理理论明确预测的 `turning-point location moderation`，并强制报告两个顶点、差值与直接检验。它把统计交互降为原料，把几何比较提升为结果段主句。
**诚实边界**: 不得从两个交互项的单独 p 值推断顶点差异；不得只写“更晚（p=...）”而省略两端顶点估计。若完整模型的证据弱于单独模型，应明确写“attenuated/mixed evidence”，不能概括为“all supported”。

### 变体 13: R8 曲线机制的选择性路径辨析 — 激活一条机制而不激活另一条 (1篇高价值)
**来源论文**: Lee & Park 2024 (Strategic Management Journal)
**原始句锚点**: Likewise, in Model 2, the squared term of surgeon's accumulated others' failures was statistically insignificant (p = .47), whereas the single term remained positive (p = .08), in line with our prediction.
**验证状态**: EMERGING（单篇机制辨析写法）
**写入日期**: 2026-08-04
**槽位**: R8
**骨架**:
> Our theory attributes the rising portion of the curve to [mechanism A] and the declining portion to [mechanism B]. As a mechanism-discriminating analysis, we examine [comparison exposure], which should activate A without imposing the same burden on B. Consistent with this distinction, the linear association with [Y] is [positive/negative] ([estimate/test]), whereas the squared term is not statistically distinguishable from zero ([estimate/test]). This contrast is consistent with the proposed division of mechanisms, but it does not constitute a mediation test because A and B are not directly measured or experimentally isolated.
**与原骨架差异**: 不用泛化的 additional analysis 堆叠更多相关性，而是选择一个能“保留机会、移除动机损耗”的对照暴露，使补充证据对应曲线两段的机制分工。
**诚实边界**: 该写法只允许 `consistent with`、`corroborates` 或 `helps distinguish`；访谈、替代暴露和 null quadratic 均不能升级为因果中介证据。

### 变体 14: R3 DiD+Logit 主效应 — OR→相对概率 + 低基准诚实 + stakes（2026-08-05）
**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (Journal of Marketing)
**原始句锚点**: While the reduction in recall probability associated with the adoption of UD laws is sizeable in relative terms, the absolute change in probability is more modest given the low average base probability of any firm experiencing a product recall during the sample period (1.64%; see Table 3).
**验证状态**: EMERGING（单篇；2026-08-05 重蒸馏校准）
**story_fidelity**: `section_variant` / climax
**槽位**: R3
**骨架**:
> "Across model specifications, [treatment × post] is consistently [direction] and significant. The odds ratio is [OR], implying [X]% [less/more] likelihood of [outcome]. While sizeable in relative terms, the absolute change is modest given the low base probability ([Y]%). However, given serious consequences for [stakeholders], we document an important effect. Thus, H[x] is supported."
**与原骨架差异**: 变体2 只到 likelihood 翻译；本变体强制 **低基准率 modest absolute 诚实句** + **stakes 论证**，适用于稀有二元结果（recall, fraud, IPO withdrawal）。
**诚实边界**: stakes 论证不能替代幅度量化；若绝对变化可计算百分点，应在 appendix 报告。

### 变体 15: R5 调节 — 25th→75th 处理效应衰减 %（2026-08-05）
**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (Journal of Marketing)
**原始句锚点**: Moving from less to more customer-focused firms in this way reduces the impact of UD law adoption on product recall likelihood by 10.56%.
**验证状态**: EMERGING（单篇）
**槽位**: R5（嵌入 R4 调节段）
**骨架**:
> "Moving [moderator] from the 25th to the 75th percentile reduces the impact of [treatment] on [outcome] likelihood by [X]%, based on average predicted probabilities across the sample distribution."
**与原骨架差异**: 变体7 报告 1-SD→概率百分点；本变体报告 **treatment-effect attenuation %**，与三向 DiD 交互配套。
**诚实边界**: 衰减 % 的计算方法须在 Methods 或 footnote 可追溯（margins/average predicted probabilities）。

### 变体 16: R7 替代解释 — CONTROL + INTERACT 两步 + need/willingness 收束（2026-08-05）
**来源论文**: Hoffmann, Cheong, Phan & Zurbruegg 2024 (Journal of Marketing)
**原始句锚点**: That is, it is unlikely that the documented effect of the reduced threat of managers being sued by shareholders on firms' likelihood to recall is an artefact of a lower need for recalls instead of reflecting a lower willingness of managers to recall.
**验证状态**: EMERGING（单篇）
**槽位**: R7
**骨架**:
> "We rule out [rival: higher quality → lower need] through two steps: (1) CONTROL for [rival proxy]—[treatment × post] remains significant; (2) INTERACT [treatment × post] with [rival proxy]—interaction not significant. Combined, findings reflect lower willingness rather than lower need."
**与原骨架差异**: 变体4 为 Heckman/GEE 结构；本变体专用于 **理论 rival 区分 observable need vs latent willingness** 的 DiD/Logit 设计。
**诚实边界**: OPERATIONAL_IMPROVEMENT 类 rival 若主效应为正（更多 mention → 更多 recall），须在 Results 一句交代，避免读者混淆方向。

### 变体 17: R3 双焦点 IV 平行倒 U — 分模型→联合模型→并列表 U-test（2026-08-05 gap audit）
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: Hypothesis 1 predicts an inverted U-shaped relationship between CVC activity and recall likelihood. We found a significant negative relationship between the squared CVC activity and product recall likelihood (Model 2: β = −.021, p < .05) which indicates the inverted U-shape relationship.
**验证状态**: EMERGING（单篇；gap audit 补缺口）
**story_fidelity**: `section_variant` / climax
**槽位**: R3
**骨架**:
> Hypotheses [xa] and [xb] each predicted an inverted-U association between [IV_a / IV_b] and the likelihood of [binary adverse Y]. Model [m_a] introduces [IV_a] and its square; the squared term is [negative] and significant (b = [value], p [threshold]). Model [m_b] repeats the sequence for [IV_b] (b = [value], p [threshold]). Model [m_joint] retains both quadratic pairs. A formal U-test table then reports, for each IV, the slope at the lower bound, the opposite slope at the upper bound, the extremum, and the [Fieller/bootstrap] interval within observed support. Both curves meet these joint restrictions (p [threshold]). Taken together, the evidence supports Hypotheses [xa] and [xb] as parallel shape claims on the same outcome, not as rival substitutes. Predicted-probability figures display response-scale likelihoods; link-scale coefficients are not read as probability changes.
**与原骨架差异**: 变体8 是线性双 IV 对称报告；变体9 是单 IV 曲线检验链。本变体专用于**两个焦点活动对同一不利二元结果提出同形倒 U** 的平行展演：分模型建立各自二次项 → 联合模型确认共存 → 并列表正式 U-test 一次裁决两边。
**诚实边界**: 平行支持不等于两 IV 可互换或可加总为“总 venturing”；不得把观察性关联写成因果效应。若一侧仅边际显著，应分别校准支持强度，不可一句 “both supported” 抹平。

### 变体 18: R4 同调节双模式几何对比 — shift vs steepen 分图裁决（2026-08-05 gap audit）
**来源论文**: Bendig, Hensellek & Schulte (2024, Entrepreneurship Theory and Practice)
**原始句锚点**: We find that both relationships are moderated by market turbulence such that the inverted U-shapes will shift up (for CVC) and steepen (for alliances) if firms operate under high market turbulence.
**验证状态**: EMERGING（单篇；gap audit 补缺口）
**story_fidelity**: `section_variant` / climax（条件化）
**槽位**: R4（可嵌入 R5 双成本 benchmark）
**骨架**:
> Hypothesis [x_shift] predicted that [W] would [shift] the inverted-U between [IV_a] and [Y] [upward/downward]; Hypothesis [x_steepen] predicted that the same [W] would [steepen/flatten] the inverted-U for [IV_b]. In Models [m], both [IV_a]²×[W] and [IV_b]²×[W] are [same or differing signs] and significant, but matching interaction signs do not adjudicate geometry. Figure [f_a] shows the [IV_a] curves: at high [W] the curve [shifts up/down], with vertex at [[X_a], [p_a]], versus [[X_a'], [p_a']] at low [W]—a vertical risk-level change. Figure [f_b] shows the [IV_b] curves: at high [W] the inverted-U [steepens/flattens], peaking at [[X_b], [p_b]] and converging toward [lower/higher] likelihood beyond that point more [quickly/slowly] than under low [W]—a curvature/pace change. Thus the same contingency amplifies risk through different geometries across venturing modes. [Optional R5:] Translating each baseline-to-vertex probability change with an external average event cost and comparing to average [deal/alliance] value illustrates scale for each mode separately; these are benchmarks, not realized losses.
**与原骨架差异**: 变体10 处理单 IV 的几何翻译；OLS-FE 变体18 与 Lee–Park 变体12 分别覆盖 flatten/steepen 与转折点位移，但均为单曲线。本变体强制 **同一 W、两 IV、两种事前几何预测** 的对比节奏：先报交互原料 → 声明符号不裁决几何 → 分图分别命名 shift 与 steepen → 一句收束“同调节、异几何”。
**诚实边界**: 不得仅因两边 X²×W 同号就宣称“调节方式相同”；不得把 shift 写成 steepen（或反之）。观测关联/likelihood 语言；图示若用非 ±1 SD 的范围内百分比，须说明原因。stuck-in-the-middle 的理论收束属 Discussion，Results 只报告中间强度的 peak likelihood。

### 变体 19: R3 条件Logit Kitazawa 半弹性幅度拍 (2026-08-13)
**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (Entrepreneurship Theory and Practice)
**原始句锚点**: "Following the method suggested by Kitazawa (2012), we calculate the average semi-elasticity of product recall likelihood with respect to a unit change in EO to determine effect size."
**验证状态**: EMERGING
**槽位**: R3
**骨架**:
> To test H[N], we examine whether [IV] is associated with an increased likelihood of [rare binary DV] by estimating [conditional logit]. [Table X] Column [controls] includes only controls. In column [focal], we include [IV]. In support of H[N], we find that [IV] is positively and significantly associated with the likelihood of [DV] (β = [value], p < [threshold]). Following the method suggested by Kitazawa ([year]), we calculate the average semi-elasticity of [DV] likelihood with respect to a unit change in [IV] to determine effect size. Our results indicate that a one standard deviation increase in [IV] increases the probability of [DV] by [percent]%.
**与原骨架差异**: 变体2 用 OR→likelihood；变体14 用 OR→相对概率+低基准诚实。本变体是条件Logit 的 Kitazawa 平均半弹性。
**诚实边界**: 半弹性是幅度拍，不是因果效应；低基准时须另句说明绝对变化是否 modest。

### 变体 20: R4 AME 网格把 weaken 推进到符号反转 (2026-08-13)
**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (Entrepreneurship Theory and Practice)
**原始句锚点**: "Interestingly, the results suggest that COO power not only weakens the positive association between EO and product recalls, but also reverses the relationship from positive to negative at high levels of COO power."
**验证状态**: EMERGING
**槽位**: R4
**骨架**:
> In H[N], we predicted that the positive relationship between [IV] and [DV] would be weakened by [moderator]. To test this hypothesis, we included an interaction term in Model [M] of [Table X]. In support of H[N], we find that [moderator] negatively moderates the positive [IV]–[DV] relationship (β = [value], p < [threshold]). We then estimated the marginal effects of [IV] on [DV] likelihood at different levels of [moderator]. We focus on values of [moderator] between [low] and [high], which represented approximately [coverage]% of observations. Interestingly, the results suggest that [moderator] not only weakens the positive association, but also reverses the relationship from positive to negative at high levels of [moderator]. Specifically, the valence switches from positive to negative and is marginally significant when [moderator] is approximately [threshold]. To ease interpretation, Figure [F] plots the average effect of [IV] at different values of [moderator]. Estimates above (below) the horizontal zero-line indicate a positive (negative) association.
**与原骨架差异**: 变体15 是衰减%无反转。本变体是 AME 网格+零线图+超出 weaken 的 reversal。
**诚实边界**: H 只预测 weaken 时，符号反转须标 Interestingly；边际反转不得写成与 p<.05 同等 reversal。

### 变体 21: R7 行业内置换连续 IV 的抽样威胁 null 图 (2026-08-13)
**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (Entrepreneurship Theory and Practice)
**原始句锚点**: "This test examines whether our observed relationship between EO and recall likelihood could have emerged by chance or from industry-specific factors rather than firm-level EO."
**验证状态**: EMERGING
**槽位**: R7
**骨架**:
> To address potential concerns about our sampling strategy, we conducted a permutation test ([citation]). This test examines whether our observed relationship between [IV] and [DV] likelihood could have emerged by chance or from industry-specific factors rather than firm-level [IV]. We maintained the structure of our data but disrupted the hypothesized mechanism by randomly reassigning each [unit]'s [IV] score to another [unit] within the same industry. We then re-estimated our baseline model with these permuted values and recorded the resulting coefficient. This process was repeated [N] times to generate a null distribution. Our actual coefficient ([value], from [Table X]) exceeds [all / nearly all] permuted coefficients, placing it at approximately the [percentile] of the distribution. The contrast provides evidence that the relationship is not an artifact of our sampling approach or industry-level confounds, but instead represents a firm-level association.
**与原骨架差异**: DiD permutation 置换处理时点。本变体行业内重分配连续 IV。
**诚实边界**: 置换检验否定抽样/行业伪影，不创造外生识别。

### 变体 22: R7 同二元 DV 的 system GMM（交互项作内生） (2026-08-13)
**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (Entrepreneurship Theory and Practice)
**原始句锚点**: "In our implementation, we treat EO, COO power, and life cycle, as well as their two- and three-way interaction terms, as potentially endogenous variables."
**验证状态**: EMERGING
**槽位**: R7
**骨架**:
> Endogeneity also remains an important consideration. [IV] may be endogenous because of omitted time-varying practices, measurement error in the [IV] proxy, and reverse causality despite lagged regressors. As an additional precaution, we employ a system GMM estimation to address potential dynamic endogeneity, which occurs when today's independent variables are influenced by yesterday's dependent variables—particularly relevant where firms may strategically adjust [moderator/TMT structure]. In our implementation, we treat [IV], [W], and [Z], as well as their two- and three-way interaction terms, as potentially endogenous variables. [Table GMM] Column 1 tests H[1], column 2 the two-way, column 3 the three-way. The coefficient of [IV] remains positively and significantly associated with [DV] likelihood (β = [value], p < [threshold]); the [IV]×[W] interaction is negative and significant; the three-way term is negative and significant. The Arellano–Bond AR(1) test is significant, which is expected. Critically, AR(2) shows no evidence of remaining correlation. The Hansen test fails to reject joint instrument validity (p = [value]).
**与原骨架差异**: 计数模型变体21 换连续 DV 再 GMM。本变体保持同一二元 DV，两向/三向交互列为内生。
**诚实边界**: GMM-on-binary 是 precaution，系数句 associated with；有效性看 AR(2)+Hansen。原文未明示 LPM。

### 变体 23: R8 post-hoc 机制代理另 DV（限 aligns with） (2026-08-13)
**来源论文**: Lun, Zurbruegg, Mount & Cheong 2026 (Entrepreneurship Theory and Practice)
**原始句锚点**: "Given that a firm's underlying approach to quality control is not directly observable, we use QMS certifications as a measurable indicator of formal quality control commitment."
**验证状态**: EMERGING
**槽位**: R8
**骨架**:
> Given our theorizing suggests that [IV] dampens a firm's focus on [mechanism construct], we empirically examine this mechanism. Given that [construct] is not directly observable, we use [proxy] as a measurable indicator of [commitment]. As shown in [Table M], [IV] is negatively and significantly associated with [proxy] (β = [value], p < [threshold]), suggesting that [high-IV] firms are less likely to implement [formal system]. This finding aligns with our general argument that [IV] may lead firms to operate with less structured [mechanism] processes. This is a post-hoc mechanism corroboration, not a mediation test.
**与原骨架差异**: 变体13 是曲线两段对照暴露。本变体是另 DV 代理不可观测质量过程。
**诚实边界**: QMS 类代理只 aligns with，须标 post-hoc 并与 R7 分节。

### 变体 24: R2 hit rate vs PCC + 25% premium (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "The hit rate exceeds both the proportional chance criterion, at 50.3% (Morrison 1969), and Hand, Manila, and Smyth's (2001) 25% premium above this benchmark, at 62.9% (50.3% × 1.25)."
**验证状态**: EMERGING
**槽位**: R2
**骨架**:
> [Table X] presents the estimation results for [Equation N]. The estimation produced significant model fit (p < [threshold]), an adjusted pseudo-R² of [value], and good prediction accuracy (hit rate = [pct]%; hit probability = [pct]%). The hit rate exceeds both the proportional chance criterion, at [pcc]% ([citation]), and [Author Year]'s 25% premium above this benchmark, at [pcc × 1.25]%. The joint tests for [variable group A] and for [variable group B] and their interactions with [group A] show they each provide significant contributions in explaining the variance of [binary DV]. We now discuss the specific results related to the hypotheses.
**与原骨架差异**: 变体 5 是 Heckman 第一阶段表。本变体是单方程二元模型的分类准确度导航。
**诚实边界**: hit rate 超过 PCC 不是经济显著性；不得用 hit rate 替代 AME。

### 变体 25: R6 spillover-null — 主效应成立但交互不溢出 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "Our results do not support H7 and H8. ... this adverse impact does not spill over into the likelihood of the company's actions according to either remedy cost or consumer harm."
**验证状态**: EMERGING
**槽位**: R6
**骨架**:
> Our results do not support H[N] and H[M]. There is no significant interaction between [moderator] and [X1] or between [moderator] and [X2]. Thus, even though [moderator] directly [reduces/increases] the likelihood of [DV], this [adverse/beneficial] impact does not spill over into the [firm]'s actions according to either [slope X1] or [slope X2].
**与原骨架差异**: 现有 R6 槽位为空。本变体把主效应显著、对应交互 null 当场收束为边界，禁止藏 null。
**诚实边界**: 不得把 fail-to-reject 写成"证明无调节"；Discussion 若回收主效应须同时回收该 null。

### 变体 26: R7 probit 外生确认电池 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "One major benefit of the control function approach is that one can directly test the presence of endogeneity through the statistical significance of residual terms. None of our control function residuals is significant."
**验证状态**: EMERGING
**槽位**: R7
**骨架**:
> One may worry about the potential endogeneity in [focal regressor] and whether this has influenced our estimation. Endogeneity could arise from either simultaneity or omitted variables. Simultaneity should not be an issue for our analysis. First, [event] occurs unexpectedly and infrequently, so [decision makers] are unlikely to incorporate a future [event] into [regressor]. Second, [regressor] is usually a multiyear contract and cannot be adapted in anticipation of a particular [event]. Third, we use [regressor] from the year before the [event], which breaks the simultaneity link. This leaves omitted variables as the possible reason for endogeneity. We address this issue with instrumental variables. We choose instruments that are correlated with [regressor] but unlikely to be correlated with the error terms of [DV] once [controls] are included, and we include the industry average of [regressor] as an additional instrument. We construct the corresponding instruments for the interaction terms. Because of the [probit] specification and multiple variables treated as potentially endogenous, we use the conditional likelihood ratio test to examine instrument strength; first-stage p-values corresponding to the likelihood ratio criterion are less than [threshold], rejecting the null that the instruments are weak. The Hansen J test cannot reject the null that the instruments are uncorrelated with the error terms (p > [threshold]). We then test endogeneity in two ways. First, the Wald test that accommodates the [probit] specification cannot reject the null that [regressor] is exogenous (p > [threshold]). Second, we employ the control function approach and include the first-stage residuals in the second-stage analysis; none of the control function residuals is significant. These tests do not reject exogeneity; we therefore retain the uninstrumented [probit] as the main specification.
**与原骨架差异**: 变体 22 是 GMM precaution；变体 4 是 Heckman 纠正。本变体是设计拆联立 + CLR/Hansen + Wald/CF 双路径外生确认、留守主估计。
**诚实边界**: fail-to-reject 外生不是证明外生；行业均值工具的排除限制须单独论证。不得把观测 probit 改写成准实验。

### 变体 27: R8 Heckman-on-CAR 管理相关性 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "Furthermore, the parameter estimate is negative—full remedy induces lower stock returns than partial remedy upon the announcement of recall. This presents an interesting contrast between investor and consumer behaviors."
**验证状态**: EMERGING
**槽位**: R8
**骨架**:
> Even though our study focuses on the determinants of [choice DV], we perform an analysis on how [choice] is associated with [performance metric] to further demonstrate managerial relevance. This is a supplemental analysis, not a hypothesis test. Because [choice] is driven by the determinants in [Equation N], the analysis of [choice] on [CAR] is a mediation-style test accounting for selection. We employ the Heckman model: the inverse Mills ratio from the [probit] of [Equation N] enters the second-step regression on [CAR_window]. Model identification requires at least one variable that affects [choice] but not [CAR]; we exclude [exclusion restriction] from the second step. [Table Y] reports three specifications to demonstrate robustness: [choice]-only, the full model, and a reduced model. Across specifications, [choice] is consistently associated with [CAR]; the estimate is negative—[full/proactive action] is associated with lower stock returns than [partial/less complete action] upon announcement. This presents a contrast between [audience A] and [audience B] behaviors: whereas [audience A] reacts positively to [responsive action], [audience B] appears to interpret a proactive action as a signal that the crisis is severe.
**与原骨架差异**: 变体 23 是机制代理另 DV；变体 5 是 Heckman 作主识别。本变体是补充相关性（选择→估值），含负向市场反应对照。
**诚实边界**: 须标 supplemental, not a hypothesis test。排他限制不能仅靠第二阶段 ns。骨架用 associated with，原文 induces 不得照搬。stepwise 删控制不入库。

### 变体 28: R4 总效应带 + 两水平预测概率 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "Figure 2, Panel A, shows the total effect of remedy cost, which becomes more negative as CEOcash increases and less negative as CEOequity increases."
**验证状态**: EMERGING
**槽位**: R4
**骨架**:
> Note that these effects were identified at the means of the moderating variables. In Figure [F2], we plot the total effects of [X1] and [X2]. For each [X], total effect is the sum of parameter estimates for the main effect and its interactions with the significant moderators ([W1] and [W2]); other variables in the interactions are fixed at their sample means. Figure [F2] Panel A shows the total effect of [X1], which becomes more [negative/positive] as [W1] increases and less [negative/positive] as [W2] increases. The dotted lines are the upper and lower bounds of 95% confidence intervals. Using [W1] and [X1] as examples, Figure [F3] further plots how the probability of [DV] changes with [W1] at two levels of [X1] ([low level] and [high level]); other variables, including covariates, are fixed at their sample means. Figure [F3] shows that higher [X1] makes [DV] less likely, and that for a higher level of [X1], greater [W1] reduces the probability to a greater extent than for a lower level of [X1].
**与原骨架差异**: 不替代 Malik AME（变体 6/7）或 Lun 反转网格（变体 20）。无 AME 网格时的总效应带 + 两水平预测概率。
**诚实边界**: 总效应带不是 1-SD AME；不得把交互模型上的主效应独立解释为无条件斜率。

### 变体 29: R7 水平 vs 比例测量 (2026-08-13)
**来源论文**: Liu, Liu & Luo 2016 (*Journal of Marketing*)
**原始句锚点**: "Nevertheless, to check the potential impact of cash versus equity incentives when they are measured as proportions, we conducted a separate analysis and found fairly consistent results."
**验证状态**: EMERGING
**槽位**: R7
**骨架**:
> Our theoretical development and empirical testing are based on how the [amounts/levels] of [component A] and [component B] motivate [actor]. We follow [field literature] to include [level measure A] and [level measure B] in the estimation. However, one might suggest that the proportions of [A] and [B] to their sum could be used as alternative measures. It is important to note that the [dollar/level] value is often the direct motivation: [actor] will likely react to [large amount] but is unlikely to be motivated when the amount is merely [small amount], regardless of the proportions. Nevertheless, to check the potential impact when [A] versus [B] are measured as proportions, we conducted a separate analysis and found fairly consistent results. The [A] proportion has a [negative/positive] association with the probability of [DV], and its interactions with [X1] and [X2] are both in the hypothesized direction. By the construction of these proportions, [B] proportion has the opposite effects to those of [A] proportion.
**与原骨架差异**: 变体 26 是内生性电池。本变体是水平测量优先、比例 confirmatory 的测量威胁节奏。
**诚实边界**: 比例由构造互为相反，不得把两边都写成独立发现。


### 变体 O：首事件建模范围的理论+经验双轨辩护（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We modeled only the likelihood of the first event during the time period, removing the [unit] from the risk set following [the change], because we assume that [the change] reflects a relatively fundamental and long-lasting change in [the underlying expectations] ([citation]). Consistent with this assumption, there were only [N] reversals in [the state] during the period of study, representing less than [X] percent of all changes. In effect, this model examines the role of [the predictor] in forestalling a lasting shift in [the orientation]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Analysis §Analyzing Increased Board Control Structure（P3）

**原文锚定**:
> "We modeled only the likelihood of the first event during the time period, removing the firm from the risk set following change, because we assume that increasing board control through structural change reflects a relatively fundamental and long-lasting change in shareholders' expectations about the board's role."

**关键特征**:
- 建模范围选择（只建模首事件、事件后退 出风险集）不靠断言靠双轨：理论轨（假设该变化是根本性长期转变，引文献 Useem）+ 经验轨（观测期内仅 N 次反转、占比 <X%，与假设一致）——假设被自己的数据反向验证
- "In effect, this model examines..." 收束句把技术选择翻译回理论任务（检验符号采纳能否阻止董事会的持久转向）——建模决定与理论问题闭环
- 反转占比数字如实披露（17 次、<5%）——用可复核的经验事实替代"反转可忽略"的定性断言

**适用**: 离散时间事件史/重复事件面板中"只建模首事件"的设定声明；事件可逆但理论上不可逆转变占绝对主导的情境

**禁忌**: 首事件假设必须与理论主张的"持久性"论证绑定（本篇是 fundamental and long-lasting change），不能为估计便利默默剔除后续事件；反转占比若不低（如 >10%），需报告含重复事件的敏感性分析

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


### 变体 T：普遍信念反转收束段（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "Overall, the results suggest that despite the widespread belief that [actors] are driving [substantive changes] in [the domain] to [increase capacity], [symbolic actions] can forestall such pressures."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Results §Tables 3-4 P3（末段收束）

**原文锚定**:
> "Overall, the results suggest that despite the widespread belief that institutional investors are driving substantive changes in board structure to increase the board's capacity to monitor and control top management, symbolic actions can forestall such pressures."

**关键特征**:
- "despite the widespread belief" 让步式反转：收束段把全文结果对准领域公认信念（机构投资者推动实质治理改革），一句话完成"证据 vs 共识"的立场对撞——Results 末段承接 Introduction 的 tension 而不越权进 Discussion
- "Overall, the results suggest" 的克制的强度：结论动词用 suggest 而非 demonstrate，反转主张留给证据自己说话
- 收束对象是压力机制（"can forestall such pressures"）而非单系数——把 H3a/H4a 的交互证据聚合为一个机制级命题

**适用**: 结果挑战领域共识/流行叙事的论文；Results 末段需要为 Discussion 的理论反转铺设跳板时

**禁忌**: "widespread belief" 必须在 Introduction/Theory 有文献铺垫，不得 Results 现造对手；让步反转只能指向机制级命题，不得在 Results 末段预先完成 Discussion 的贡献声明

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)


### 变体 W: R2 DV 家族换场小节标题 (pfarrer2010 型)
**来源论文**: Pfarrer, Pollock & Rindova 2010 (Academy of Management Journal)
**原始句锚点**: "Hypotheses 3a-3c and 4a-4c predict the effects of firm reputation and celebrity on investors' reactions to earnings surprises."
**验证状态**: EMERGING
**写入日期**: 2026-09-05
**槽位**: R2
**骨架**:
> [Unnumbered subsection heading naming the construct pair and outcome:] Effects of [asset_A] and [asset_B] on [outcome_family_B]. [Block opener restating the full hypothesis set:] Hypotheses [X]a-[X]c and [Y]a-[Y]c predict the effects of [asset_A] and [asset_B] on [outcome_family_B].
**与原骨架差异**: Results 覆盖两个 DV 家族（surprise 发生概率 / 投资者反应 CAR）时需要换场装置——Pfarrer 用不带编号、构念命名的子小节标题（Effects of Reputation and Celebrity on Investors' Reactions to Surprises）重开证据流，标题本身预告新 DV 与构念对；随后首句整组重述全部待检假设（Hypotheses 3a-3c and 4a-4c predict the effects of...），让新小节自足可读。与 r2_binary_outcome_hypothesis_pair_table 互补：该变体管同 DV 家族内 H1a/1b 双表镜像导航，本变体管 DV 家族之间的结构换场。适用于多 DV/多结果族 Results（incidence + severity、adoption + performance 等）。

<!-- wb:pfarrer_pollock_and_rindova_2010:r2_dv_family_pivot_heading -->


### 变体 X: R2 相关替代测量分模型括弧 — 似然模型嵌套序列 (gulati1999 型)
**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "The two variables that assess the level of network resources of firms, Cliques and Closeness, were relatively highly correlated (0.66) and were examined separately in the statistical analysis. ... Models 2 and 3 provide two alternative tests for Hypothesis 1."（跨 R1/R2 段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-05
**槽位**: R2
**骨架**:
> Table [X] presents the correlations and descriptive statistics for the variables included in the analysis. The two variables that assess [construct], [measure_A] and [measure_B], were relatively highly correlated ([r]) and were examined separately in the statistical analysis. I assessed the hypotheses sequentially in a series of [estimator] models, presented in Table [Y]. The first model is the base model, which includes the control variables and examines the effects of [control_block]. Models [2] and [3] provide two alternative tests for Hypothesis [1]: Model [2] tests the additional effect of [construct] as measured by [measure_A] on [DV]; Model [3] is identical to Model [2] except that it uses an alternative measure of [construct]—[measure_B]. The two measures of [construct] are correlated and thus are introduced in separate models. Models [4] and [5] introduce [predictor_2] while retaining the two measures for [construct] separately in each model. All five models were significant overall, as indicated by the [fit_test] using their [fit_statistic] values, and the significant improvement in the [fit_test] statistic suggests a better-fitting model once the measures of [construct] are included.
**与原骨架差异**: R1 高相关门不止安抚（对比 VIF 式"多重共线性不担忧"），而是当场预告分析后果（examined separately）并在 R2 兑现；R2 用 "two alternative tests for Hypothesis [N]" 把同一构念的替代操作化升格为并列主检验（各进独立模型），再以 2×2 网格并入第二焦点预测子；结尾用整体拟合+嵌套增量拟合（卡方/对数似然）作非线性模型的 ΔR² 类比证据拍。适用于似然/非线性模型下同一构念多操作化；线性模型可平移（卡方增量→ΔR²）。
**区别于**: 变体 24——那是 hit rate/PCC 分类准确度导航，本变体是替代测量括弧主检验架构。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:r2_alternative_measure_bracketing_probit -->



### 变体 AH: R6 竞争机制衰减裁决 — 基线设伏+拟合增量+非对立供认+趋势重读 (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "Moreover, the effect of density became non-significant at the .01 level once we introduced structural differentiation into this model. This suggests that the systemic effects on tie formation captured by density may actually be mediated by the structural differentiation of the network."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R6
**骨架**:
> In Model [1], [rival_mechanism_variable] has a [direction] and significant coefficient, suggesting that [rival_theory_reading]. Introducing [focal_construct] in Model [k] leads to a significant improvement in the fit of the model, as measured by the [fit_test] statistics. Moreover, the effect of [rival_mechanism_variable] became non-significant at the [.01] level once we introduced [focal_construct] into this model. This suggests that the [systemic effects] captured by [rival_mechanism_variable] may actually be mediated by [focal_construct]. Although Hypothesis [N] was not formulated as an alternative for a [rival_theory] process, the statistical insignificance of [rival_mechanism_variable] in Model [k] suggests that [outcome] is perhaps best explained by [focal_mechanism], rather than a consequence of [rival_mechanism] driven by [rival_process]. Thus, the [observed trend] may be prompted by [focal_mechanism], rather than [rival_mechanism].
**与原骨架差异**: 竞争机制不是另测的中介代理，而是 rival 理论自带的系统层变量（如 legitimization 之于 density）：先在基线模型给它显著性并配 rival 理论解读（设伏拍），焦点构念进入后用拟合增量拍（[fit_test] 显著改善）+该变量衰减至非显著完成裁决；"Although Hypothesis [N] was not formulated as an alternative" 供认拍显式标注裁决相对假设陈述的事后性（post hoc 标注合规）；收束拍把时期趋势（[observed trend]）重读为焦点机制驱动而非 rival 机制。四层节奏：设伏→衰减→供认→趋势重读。
**禁忌**: 衰减方向必须与理论预期一致（rival 变量衰减、焦点构念稳定显著）才可作裁决；焦点构念与 rival 变量同时衰减时不得挪用此句式；"mediated by" 是叙事性中介语言，不得包装成正式中介检验结论。
**区别于**: 变体 Y（R2 控制变量解释消去——单一控制变量代理焦点构念的正向重读）；变体 AG（机制电池另测竞争机制）；变体 16（rival 两步排除）——本变体不另测机制，让 rival 理论关键变量在基线设伏、在焦点模型处被吸收，升级为两套实质理论的整体裁决。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r6_rival_mechanism_adjudication_nested_attenuation -->

### 变体 Y: R2 控制变量解释消去 — 跨嵌套模型衰减的理论重读 (gulati1999 型)
**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "In Models 2 and 3, which include the network resources variables, however, Time is insignificant, suggesting that these temporal effects are interpreted by the network resource variables included in these models. In other words, Time was capturing differences in network resources over time."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-05
**槽位**: R2
**骨架**:
> In Model [1], [control] has a [direction] and significant coefficient ([coef], p < [threshold]), suggesting that [naive_temporal_or_compositional_reading]. In Models [2] and [3], which include the [focal_construct] variables, however, [control] is insignificant, suggesting that these [control] effects are interpreted by the [focal_construct] variables included in these models. In other words, [control] was capturing differences in [focal_construct]. [Optional robustness coda: The inclusion of a [functional_form] term for [control] did not alter these results; its coefficient was also insignificant. The main effects for the key variables did not change when I included [alternative_specification].]
**与原骨架差异**: 把控制变量跨嵌套模型的显著性衰减正向重读为理论证据——"was capturing differences in [focal_construct]" 一句完成解释消去，控制变量叙事因此服务焦点构念的解释力主张而非默默消失；可选收束拍补功能性形式/替代设定的不变性。区别于 OLS-FE 两处近似：交互家族互相吸收的 caveat（absorb each other's moderating effect，事后辩解衰减）与 Cinelli-Hazlett（explain away 指混淆强度足以解释关联）——本变体是嵌套序列内的正向重读。
**禁忌**: 只有衰减方向与理论一致（控制变量衰减、焦点变量稳定显著）时可用；焦点变量同时衰减是坏消息，不得反向挪用此句式。
**区别于**: 变体 24 与 OLS-FE 吸收 caveat——本变体是控制变量衰减→代理焦点构念的正向理论重读。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:r2_control_attenuation_explaining_away -->


### 变体 Z: R6 构念家族混合证据 — mixed 标题拍+核心显著+辅助 null 全披露 (gulati1999 型)
**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "The results for the influence of alliance formation capabilities on subsequent alliances show mixed results. ... While past experience with alliances was significant, no significant results were obtained from three additional measures of alliance capabilities that assessed the diversity of alliances each firm had previously entered and the time duration since it last entered an alliance (results not reported here)."（跨段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-05
**槽位**: R6
**骨架**:
> The results for the influence of [construct_family] on [DV] show mixed results. As Table [X] suggests, [core_measure], which measured the effects of [core_dimension] on [DV], was [direction] and significant in both Models [a] and [b]. This indicates that [substantive_reading_of_core_measure]. It is important to highlight that [estimator_credibility_sentence_reinforcing_estimate_quality]. While [core_measure] was significant, no significant results were obtained from [k] additional measures of [construct_family] that assessed [alternative_dimension_1] and [alternative_dimension_2] (results not reported here). [Alternative_specification_1] were insignificant. Furthermore, [alternative_specification_2] of [dimension] were also not significant (results not reported here).
**与原骨架差异**: 构念家族层面的混合证据框架——mixed 标题拍先行定调，核心操作化走完整四拍（方向→显著性→实质解读→估计器可信度强化），辅助操作化逐项 null 且全部显式披露（results not reported here 标注而非静默省略）。区别于变体 25（spillover-null：主效应成立但对应交互当场 do not support）——本变体管同构念多操作化的证据分裂，不管调节溢出。
**禁忌**: mixed 必须指家族内分裂（核心显著+辅助 null）；核心测量本身不稳定时不得用 mixed 弱化。null 项须逐项披露，不得只报幸存的显著操作化。
**区别于**: 变体 25——那是调节交互不溢出的当场 do-not-support；本变体是构念操作化家族的 mixed 标题+核心/辅助分层披露。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:r6_construct_family_mixed_evidence -->



### 变体 AM: R3 判决后构念效度同调拍 — congruent 同调句+替代测量一行复证 (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "This result is congruent with research on the role of interdependence in alliance formation and helps enhance the construct validity of our indicator. Our alternative measure for interdependence, using membership in the clusters corroborated by industry experts, yielded similar results."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R3
**骨架**:
> As predicted in Hypothesis [N], [units with condition] were more likely to [outcome]. This result is congruent with research on [related literature stream] and helps enhance the construct validity of our indicator. Our alternative measure for [construct], using [alternative operationalization], yielded similar results.
**与原骨架差异**: 四拍判决后追加两小拍收尾弧——(1) 同调拍：以 "congruent with research on [stream]" 把结果与先行文献对齐，并直接升格为构念效度证据（"helps enhance the construct validity of our indicator"——显著结果反哺测量质量主张），(2) 替代测量一行复证拍：替代操作化 "yielded similar results" 一行带过，不另开模型叙事——把测量稳健性压缩进假设块而不膨胀结构。
**禁忌**: 同调句引用的文献须真实支撑同方向发现，不得把任何相关文献都说成 congruent；替代测量复证只报相似与否，不得重跑四拍；构念效度升格仅在结果方向与文献一致时成立，方向相悖时须改报 divergence。
**区别于**: 变体 X（R2 相关替代测量分模型括弧——事先声明的各进独立模型架构）；变体 Z 的估计器可信度强化拍（估计质量自证）——本变体是判决后的测量构念效度外部同调证词+替代测量一行复证 coda。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r3_construct_validity_congruence_coda -->

### 变体 AA: R7 随机效应方差份额自证 — Rho 作为纠正生效证据 (gulati1999 型)
**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "The random-effects model used generates a coefficient Rho, which indicates the extent to which unobserved heterogeneity was found and corrected for by the model. The positive and significant coefficient for Rho across all models suggests that unobserved factors that could influence the alliance behavior of firms were accounted for by the statistical model."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-05
**槽位**: R7
**骨架**:
> The [random_effects_estimator] used generates a coefficient [Rho / variance_share_statistic], which indicates the extent to which unobserved heterogeneity was found and corrected for by the model. The [direction] and significant coefficient for [Rho] across all models suggests that unobserved factors that could influence [DV] were accounted for by the statistical model. [Optional companion: I later tested the robustness of my findings with a [alternative_within_unit_estimator] and found consistent results.]
**与原骨架差异**: 随机效应面板专属的"设计内生自证"——用估计器自带的方差份额统计量（Rho）把"未观测异质性被纠正"从 methods 设定声明升级为 Results 内的经验证据（跨模型显著→纠正生效），置于 Results 收尾位；可搭配跨估计器一致性句（FE 复检 found consistent results）。区别于变体 4/26——那些是外部诊断电池（GEE/Heckman、IV 诊断），本变体是估计器自带统计量的威胁回应。
**适用**: 随机效应面板（RE probit/logit/linear）；固定效应无此统计量。
**禁忌**: Rho 不显著时不得伪造"纠正生效"叙事，应如实报告异质性有限。
**区别于**: 变体 4/26——外部诊断电池 vs 本变体的估计器自带方差份额自证。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:r7_random_effects_variance_share -->


### 变体 AB: R7 虚拟变量显著≠斜率异质性 — 无约束分组模型检验主效应同质性 (gulati1999 型)
**来源论文**: Gulati 1999 (Strategic Management Journal, 20(5), 397-420)
**原始句锚点**: "While the relative significance of the sector dummies indicates whether there may be intrinsic differences across the three industries in the likelihood that alliances will be used, it does not tell us whether the main effects hypothesized in this paper differ across the three industries. Rather, they simply suggest that the constant terms for each of the industries may differ."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-05: 用户点名 Gulati 为最喜爱学者之一，其论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-05
**槽位**: R7
**骨架**:
> While the relative significance of the [group_dummies] indicates whether there may be intrinsic differences across the [groups] in the likelihood that [DV] will [occur], it does not tell us whether the main effects hypothesized in this paper differ across the [groups]. Rather, they simply suggest that the constant terms for each of the [groups] may differ. To assess the [group] differences further, I estimated unrestricted models for each of the [groups] (results not presented here). By examining each of the [groups] independently, no restrictions were imposed on the slope coefficients. The signs of the coefficients indicated that the postulated directionality of the main effects observed in the pooled sample do indeed hold true in each of the [groups]. I also conducted a similar test for [alternative_partition]. The results suggested that the main effects were consistent across [alternative_partition].
**与原骨架差异**: 先做概念区分拍（虚拟变量显著只证截距差异，不证斜率异质性——"Rather, they simply suggest that the constant terms... may differ"），再上无约束分组模型动作拍（no restrictions were imposed on the slope coefficients），以主效应方向一致性判定收束，最后以第二分区（如国籍）重复——把 pooled 主效应的可推广性从默认假设变成被检验对象。范式通用（不限似然模型）。
**禁忌**: 分组须理论驱动（行业/国籍是理论边界），不得事后切样本找一致性；分组后主效应方向不稳时须如实报告，不得归入附录掩盖。
**区别于**: 变体 11（六威胁梯）与变体 16（rival 排除）——本变体防御 pooled 主效应的跨组同质性，不是外部威胁或替代解释。

<!-- wb:gulati_1999_network_location_and_learning_the_influence_of_n:r7_dummy_significance_vs_slope_homogeneity -->


### 变体 AC: R2 假设级风险集递进导航 — 每假设各配可估样本 (gulati_westphal_1999 型)
**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "Since hypotheses 2-4 assume that an interlock tie exists, ..., the risk set narrows here from all possible dyads to only those dyads for which there was an interlock tie between the two firms."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R2
**骨架**:
> Because Hypothesis [1] concerns whether [focal predictor] affects [DV] at all, the risk set for this analysis includes all possible [dyad] combinations between [focal units] and the [full sampling frame] ([N_all] [dyads]). Because Hypotheses [2-4] assume that [prior condition] exists—[treatment] only occurs when [prior condition] holds—the risk set narrows to only those [dyads] for which [prior condition] was present ([N_narrow]). Model [1] in Table [X] tests Hypothesis [1] on the full risk set; Model [2] tests Hypotheses [2-3] on the narrowed risk set of [N_narrow] [dyads].
**与原骨架差异**: dyad/网络设计的风险集随假设前提逐级收窄（全体可能 dyad → 存在 prior condition 的 dyad → 个体层子样本），导航句把"哪条假设在哪个可估样本上检验"写成显式逻辑（前提不成立则 treatment 无定义），表格 N 行与正文导航一一对应——风险集从 methods 设定声明升级为 Results 导航结构。
**适用**: dyad/网络二元结果设计；每条假设的可估样本不同（风险集随假设前提收窄）；堆叠扩散 Logit 等"风险集未解释"高风险场景可直接借用。
**禁忌**: 风险集收窄必须由假设前提逻辑驱动（treatment 在前提缺失时无定义），不得为提显著性事后切样本；收窄产生的选择效应须另行交底（本文用 Heckman 选择模型，见变体 5 与 R3 双估计器共证变体）。
**区别于**: 变体 X（相关替代测量分模型括弧——同一风险集内的测量变体嵌套）；变体 5（Heckman 第一阶段导航——选择纠正修辞）；本变体是"假设前提→可估样本"的导航层。registry 现存唯一"风险集"条目仅是堆叠扩散Logit 的 high_risk_missing 警示，无骨架。

<!-- wb:gulati_westphal_1999_cooperative_or_controlling:r2_hypothesis_riskset_narrowing_dyads -->


### 变体 AD: R6 null 主假设前置 pivot — 判决先行冒号句 + In summary 权变化收束 (gulati_westphal_1999 型)
**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "The results in model 1 do not support this hypothesis: after controlling for the extent of market constraint ... the existence of an interlock tie is not significantly related to subsequent alliance formation. ... In summary, the first set of results indicates that the mere presence of a board interlock tie ... does not predict the formation of strategic alliances between firms; instead, such ties may either increase or decrease the likelihood of alliance formation, depending on the nature of the CEO-director relationship that underlies the tie."（跨段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R6
**骨架**:
> The results in Model [1] do not support Hypothesis [1]: after controlling for [covariate family], [focal predictor] is not significantly related to [DV]. [Supported hypotheses follow in parallel models on the conditional sample.] In summary, the first set of results indicates that the mere presence of [focal predictor] does not predict [DV]; instead, [focal predictor] may either increase or decrease the likelihood of [DV], depending on [relational content / boundary attribute].
**与原骨架差异**: null 主假设不被埋位也不被道歉，而是置于假设序列首位并配"判决先行冒号句"（verdict → colon → scope condition → null 陈述，scope condition 同时暗示检验的保守性）；随后 In summary 段把"总效应 null + 两个异号条件效应"收束成权变论题——null 从遗憾变成核心答案的一半，为调节假设让台。
**适用**: 理论核心是权变（X 的效应取决于 W/关系内容）且 X 主效应预期不显著的设计；主效应 null 首位呈现使后续条件效应成为"答案"而非"补救"。
**禁忌**: 仅当权变论题真的把 null 变成可解释结果（存在已检验的异号条件效应）时使用；若主效应 null 只是失败且无条件效应兜底，不得借用此节奏包装；scope condition 从句必须与实际控制变量一致。
**区别于**: 变体 Y（控制变量衰减的理论重读——跨嵌套模型解释消去）；变体 Z（构念家族 mixed 证据——mixed 标题拍）；变体 P（四格设计 null 格确认——组间比较）；本变体是主假设 null 的序列位置学（首位 pivot）+ 权变化收束。

<!-- wb:gulati_westphal_1999_cooperative_or_controlling:r6_null_main_effect_contingency_synthesis -->


### 变体 AE: R4 对称放大调节镜像判决句 — 单 moderator 同向放大异号双主效应 (gulati_westphal_1999 型)
**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "Consistent with hypothesis 4a, the results show that as the number of third-party ties between the CEO and outside directors increases, the negative relationship between board control over the CEO and the likelihood of subsequent alliance formation ... becomes stronger."
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R4
**骨架**:
> The interaction effects in Model [3] of Table [X] support Hypothesis [4]. Consistent with Hypothesis [4a], the results show that as [moderator] increases, the negative relationship between [predictor1] and the likelihood of [DV] becomes stronger. The results also support Hypothesis [4b]: as [moderator] increases, the positive relationship between [predictor2] and the likelihood of [DV] also becomes stronger. [Optional close: The hypothesized interaction effects were also supported in [parallel estimator] models, as shown in Model [k] of Table [Y].]
**与原骨架差异**: 单一 moderator 同时放大两个异号主效应（一负一正，强度放大而非方向改变）时，用镜像判决句法让对称性在句法层可见——同一 "becomes stronger" 在 H4a/H4b 两句中重复，Consistent with / also support 的衔接标记假设对的配对性；无图、无简单斜率、无 AME，纯句法对称承载理论对称（intensity not direction）。
**适用**: 对称放大调节（symmetric amplification）假设对；两个交互项同表相邻列；调节的理论点恰是"同一机制放大两种关系内容"。
**禁忌**: 两交互若非同向放大（一放大一衰减）禁用镜像句法；"becomes stronger" 不得写成方向反转（由负转正）；镜像句两侧的假设编号与系数符号必须与表格一致。
**区别于**: 变体 18（同调节双模式几何对比——shift vs steepen 分图裁决，需交互图）；变体 20（AME 网格把 weaken 推进到符号反转）；本变体无图无 AME，靠句法镜像承载对称放大主张。

<!-- wb:gulati_westphal_1999_cooperative_or_controlling:r4_symmetric_amplification_mirror_verdicts -->


### 变体 AF: R3 双估计器并列共证 — 双表导航 + 逐假设一行跨估计器确认 (gulati_westphal_1999 型)
**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "Table 4 provides the results of the logistic regression analysis of alliance formation, and table 5 gives the Heckman selection model results. ... The hypothesized effects of board control and cooperation were also supported in Heckman selection models of alliance formation, as shown in model 1 of table 5."（跨段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R3
**骨架**:
> Table [X] provides the results of the [primary estimator] analysis of [DV], and Table [Y] gives the [parallel estimator] results. Model [2] tests Hypotheses [2] and [3]. [Hypothesis verdicts on the primary estimator.] The hypothesized effects of [predictor1] and [predictor2] were also supported in [parallel estimator] models of [DV], as shown in Model [k] of Table [Y].
**与原骨架差异**: 平行估计器不是内生性补丁而是并列主估计——开场一句双表导航（主估计表 + 平行估计表并列），此后每个假设块尾随一行跨估计器确认句（"were also supported in [parallel estimator] models..., as shown in Model [k] of Table [Y]"）；主结论的证据等级由"单估计器+稳健性"升为"双估计器共证"，确认句只报支持与否、不重跑幅度叙事。
**适用**: 二元 DV 同时担心选择效应的 dyad/panel 设计（logit + Heckman selection 并列）；两估计器共用同一假设编号体系与控制变量集。
**禁忌**: 确认句逐假设块各一行即可，不得在第二估计器上重复完整四拍叙事；两估计器结论不一致时必须显式报告分歧，不得静默只引一致者；平行估计器的第一阶段细节不进 Results 正文导航。
**区别于**: 变体 5（Heckman 第一阶段表格+逆米尔斯比率——选择纠正导航）；变体 4（GEE+Heckman 内生性稳健性——事后补丁位）；变体 AA 的 companion 句（FE 复检 found consistent results——RE 家族内部替代估计器一行带过）；本变体是双估计器全程并列共证的架构级节奏。

<!-- wb:gulati_westphal_1999_cooperative_or_controlling:r3_dual_estimator_coprimary_confirmation -->


### 变体 AG: R8 探索性中介五拍弧 — 供认→竞争机制电池→系数衰减判定→反向因果反驳 (gulati_westphal_1999 型)
**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "While our theoretical argument suggests that trust in the CEO-board relationship can explain how control and cooperation affect alliance formation, our primary analyses did not explicitly model the mediating effect of trust. Thus, one ... might question whether other, related social processes mediate these relationships."（原文跨表 7 排版中断，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R8
**骨架**:
> While our theoretical argument suggests that [mediator] can explain how [X] affects [Y], our primary analyses did not explicitly model the mediating effect of [mediator]. Thus, one might question whether other, related social processes mediate these relationships. To assess the relative importance of these different social processes, we conducted further exploratory analyses using [measures of the mediator and rival mechanisms]. As shown in Models [3] and [4] of Table [X], [mediator] has a strong and [direction] relationship with [DV], while the effects of [rival mechanism 1] and [rival mechanism 2] are nonsignificant. In addition, when [mediator] is added to the models, the effects of [X] become nonsignificant, suggesting that [mediator] mediates the effects of [X] on [DV] ([mediation citation]). The results are not consistent with the view that [reverse causal ordering]; the findings suggest that [mediator] mediates the effects of [X], and not the reverse.
**与原骨架差异**: 事后中介分析的五拍诚实弧——(1) 供认主分析未建模中介（"did not explicitly model"）；(2) "Thus, one might question" 引出同族竞争机制；(3) 探索性标签 + 竞争机制实测并全数 null（ingratiation、board approval 在所有模型中不显著）；(4) 中介判定用系数衰减并引方法出处（Baron and Kenny, 1986）；(5) 反向因果反驳（"and not the reverse"）——把"为什么是 A 中介而不是 B 机制、不是反向因果"一次答完。
**适用**: 理论机制（如信任）未在主分析直接建模、且有可实测的同族竞争机制（政治影响/认可）可排除的设计；主效应已确立后的机制补证。
**禁忌**: exploratory 标签必须保留，post hoc 中介与稳健性检验分开标注，不得包装成确证性检验；中介判定须引方法出处；竞争机制须真实测量而非"不太可能"口头排除；反向反驳须有经验证据（如时序或替代测量复检）支撑。
**区别于**: 变体 13（曲线机制选择性路径辨析——激活哪条机制）；变体 23（post-hoc 机制代理另 DV——限 aligns with）；变体 27（Heckman-on-CAR 管理相关性）；本变体是"供认→竞争电池→中介判定→反向反驳"完整弧，且含反向因果方向裁决。

<!-- wb:gulati_westphal_1999_cooperative_or_controlling:r8_exploratory_mediator_competing_mechanism_battery -->


### 变体 AI: R6 null 主效应条件重估与构念域重划 — less conclusive 降级判决+分离重估+子域收束 (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "The evidence for hypothesis 5, which predicts an increase in the probability of an alliance between organizations with similar centrality, is less conclusive. ... Thus, the homophily tendency implicit in hypothesis 5 only applies to central organizations."（跨段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R6
**骨架**:
> The evidence for Hypothesis [N], which predicts [predicted relation], is less conclusive. The results indicate that [focal measure] does not have a statistically significant influence on [DV]. In separate estimations, however, we found that [alternative operationalization] was [direction] and significant if [co-test variable] was excluded from the model. To interpret this result, it is worth noting that [geometric or substantive property of the measure]. Thus, the [tendency] implicit in Hypothesis [N] only applies to [subpopulation]. Once [co-test variable] is controlled for, the effect of [focal measure] is no longer significant. Viewed in this light, these results are consistent with [prior distinction citation], which suggests that [construct boundary between subpopulations].
**与原骨架差异**: null 假设不被 pivot 到序列首位也不被 family-mixed 定调，而是在原位降级判决（"less conclusive"——比 do not support 温和的诚实措辞）后当场披露分离重估（[alternative operationalization] 在排除 [co-test variable] 后才显著），再用测量的几何/实质性质注记把 null 重划为"机制只适用于子群"，并引 prior distinction 文献锚定构念边界——null 判决保持不变，被重划的是适用域；五步节奏：降级判决→null 陈述→分离重估披露→性质注记→子域收束+文献锚定。
**禁忌**: 分离重估必须如实披露"排除共测变量后才显著"这一条件性，不得只报幸存设定；重划后的"只适用于子群"须有几何性质或文献证据支撑，不得纯口头挽救 null；"less conclusive" 只适用于证据分裂情形，单侧干净 null 应直接报告不支持。
**区别于**: 变体 AD（null 主假设首位 pivot + In summary 权变化收束——null 是答案的一半）；变体 Z（构念家族 mixed 标题拍——家族内分裂）；变体 P（四格 null 格确认）——本变体是 null 原位降级判决 + 分离重估 + 适用域重划三步法，null 不翻案、只划界。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r6_null_main_conditional_reestimation_rescoping -->


### 变体 AJ: R4 预期符号翻译+共线性分模型声明+主效应存活综合 (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "We tested these models separately because of concerns of multicollinearity across the interaction terms. ... However, interdependence on its own has a positive impact on alliance formation across all models."（跨段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R4
**骨架**:
> Models [a], [b], and [c] assess the moderating influence of [moderator] on both [driver family 1] and [driver family 2] of [DV]. We had predicted that [moderator] would moderate the influence of [driver 1] on [DV] (Hypothesis [x]). This prediction should translate into a significant and [direction] coefficient for the interaction between [driver 1] and [moderator]. But we also predicted that the effect of [driver 2] on [DV] would [diminish/increase] with [moderator] (Hypothesis [y]). This effect should yield a significant and [direction] coefficient for the interaction between [driver 2] and [moderator]. We tested these models separately because of concerns of multicollinearity across the interaction terms. Model [a] introduces an interaction term between [driver 2] and [moderator]. The [direction] coefficient for the interaction term supports Hypothesis [y] and suggests that [attenuation/amplification reading]. However, [driver 2] on its own has a [direction] impact on [DV] across all models. Thus, while [driver 2] does influence [DV], [the growing moderator] [mitigates/amplifies] the effects of [driver 2] on [DV].
**与原骨架差异**: 调节检验开场先把语言假设翻译成预期交互系数符号（"This prediction should translate into a significant and [direction] coefficient"——读者可先核对判定标准再看系数），再显式声明因交互项间多重共线性而分模型检验（"We tested these models separately because of concerns of multicollinearity"）；逐模型判决后补主效应存活句（"on its own has a [direction] impact across all models"）——交互不是取代主效应而是限定其边界，收束成双驱动综合（[driver family 1] 被缓解 / [driver family 2] 被放大）。四拍：符号翻译→分模型声明→判决+存活句→驱动综合。
**禁忌**: 分模型必须由共线性或理论驱动并显式声明理由，不得为凑显著拆模型；存活句不得违反"交互后主效应独立解释"反模式——它限定主效应的边界条件而非重复宣称独立效应；预期符号必须与表内交互系数方向一致；衰减读法（mitigates）不得写成方向反转。
**区别于**: 变体 AE（镜像判决句——单调节同向放大异号双主效应，靠句法对称）；变体 28（总效应带+两水平预测概率——需预测概率）；变体 18（双模式几何对比——需交互图）；本变体无图无 AME，靠"符号翻译→分模型声明→存活句→综合"四拍承载权变主张。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r4_interaction_sign_translation_separate_models -->


### 变体 AK: R6 null 分量+显著交互坦白段 — 让步从句+弱证据边界+双向 hedge (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "Although similarity in centrality was not a significant predictor of alliance formation, the interaction between this variable and structural differentiation is statistically significant. ... although this tendency is not strong enough to make the difference in centrality statistically significant during the period of observation."（同段拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R6
**骨架**:
> Although [component measure] was not a significant predictor of [DV], the interaction between this variable and [moderator] is statistically significant. This suggests that, with [the growth of moderator], [units] may become increasingly [sensitive] to [component dimension] when [choosing/acting], although this tendency is not strong enough to make [component measure] statistically significant during the period of observation. [Optional speculative mechanism: The more [structural condition] becomes apparent, the more difficult it may become for [disadvantaged units] to [outcome]. Although this does not mean that such [outcomes] will not occur, it does suggest that [disadvantaged units] may need to possess some unique attributes that can enhance their attractiveness in order to [outcome].]
**与原骨架差异**: 主效应 null 但交互显著的组件级坦白——让步从句开头承认 null 分量，随即指出交互显著并给出"随调节变量增长单元对该维度日益敏感"的机制解读，再用 "although this tendency is not strong enough... during the period of observation" 显式标注证据强度边界（观察期内不足以显著）；可选推测机制拍用 may 措辞并保留 "does not mean that such [outcomes] will not occur" 的双向 hedge——坦白与推测分层，不把弱证据包装成定论。
**禁忌**: 只可用于交互假设本身获支持的情形；推测机制必须保留 may / does not mean 双向 hedge，不得引入未测量的新构念断言；不得把 null 分量写成"实际显著"；证据边界句（not strong enough during the period of observation）不得删除。
**区别于**: 变体 AD（null 主假设是答案一半的首位 pivot——权变即核心结论）；变体 AB（虚拟变量显著≠斜率异质性的概念区分拍）；本变体处理已获支持的调节假设内部的 null 分量，功能是坦白+边界标注而非翻案或概念澄清。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r6_null_component_significant_interaction_candor -->


### 变体 AL: R7 曲线形式脚注稳健性 — 差异化发现+线性不受影响+简约保留裁决 (gulati_ajs1999 型)
**来源论文**: Gulati 1999 (American Journal of Sociology, 104(5), 1439-1493)
**原始句锚点**: "The results suggest that the relationship between previous alliances and future alliances within the dyads is best described as an inverted U-shape relationship, captured by a second-order polynomial function. ... We report the results of the linear model for the sake of parsimony."（同脚注内拼接，省略号标注）
**验证状态**: VERIFIED — expert_audit_override (user 2026-09-06: Gulati 系论文蒸馏单源即 VERIFIED; paper_count=1)
**写入日期**: 2026-09-06
**槽位**: R7
**骨架**:
> We also tested [polynomial transformations] of the [focal predictors] to account for nonlinear effects. The results suggest that the relationship between [predictor 1] and [DV] is best described as an [inverted U-shape] relationship, captured by a [second-order polynomial] function. The effect, however, is [exponential] for [predictor 2]: as [predictor 2] increases, the likelihood of [DV] increases disproportionately. The inclusion of the [functional form] transformations does not affect the results obtained with the [baseline form]. We report the results of the [baseline form] for the sake of parsimony.
**与原骨架差异**: 功能形式威胁的脚注级三拍——(1) 检验动作（[polynomial transformations]）并对各焦点预测子给出差异化曲线发现（一个 [inverted U-shape]、一个 [exponential]/disproportionate，而非笼统"非线性"），(2) 不变性拍（"does not affect the results obtained with the [baseline form]"），(3) 简约保留裁决（"We report the results of the [baseline form] for the sake of parsimony"）——发现非线性但不切换主设定，把裁决与理由同时交给读者。
**禁忌**: 曲线发现若实质改变解释（inverted U 意味着效应变号）不得只留脚注，应进正文并改主设定；简约保留裁决必须以不变性拍为前提；脚注披露须完整到可复现（测量定义/公式/指数形式），不得只报"不显著"；venue caveat：AJS 1999 把稳健性放脚注是期刊惯例，现代目标期刊应升级为专节——骨架可平移，容器需升级。
**区别于**: 变体 9（Binary-GEE 曲线完整检验链——二次项→端点斜率→Fieller 区间作主分析）；变体 11（曲线六威胁稳健性梯）；本变体是把曲线检验降为脚注披露+简约保留裁决的紧凑型，适用于理论以线性为主、非线性仅作敏感性检查的设计。

<!-- wb:gulati_1999_where_do_interorganizational_networks:r7_curvilinear_footnote_parsimony_retention -->
<!--
pattern_id: switching_reg_first_stage_intermediate_navigation
estimator_family: switching regression / endogenous switching（mlogit 第一阶段 + 分组 OLS 第二阶段）
slot: R2（第一阶段导航）/ R8（自有价值旁注，显式标记探索性）
source_papers: ["gulati2005-adaptation-vertical"]
confidence: EMERGING（单篇 full_text_verified，待第二篇交叉验证）
-->

### 变体 AN：内生转换回归第一阶段选择模型——"中间步骤导航 + 自有价值旁注"报告节奏（Intermediate-Step Navigation with Own-Merit Aside）

**适用场景**: 两阶段选择修正估计器（内生转换回归 / Heckman 型 / 控制函数）的第一阶段选择模型（mlogit/logit/probit）不直接检验假设，但读者需要一套交底规则才能读表：两步骤预告、IV 排他声明、基线类解释规则、IV 相关性与分阶段样本损耗——之后用"自有价值旁注"把第一阶段的有趣结构（往往是机制旁证）与主流程明确区隔。

**报告节奏**: [两步骤预告] → [排他声明] → [基线解释] → [IV 相关性与样本损耗] → [自有价值旁注(可选)] → [过渡回主流程]

**骨架**:
```
[两步骤预告] We used a [two-stage estimator] that attempts to account for possibly endogenous
choices of [treatment category]. This model is estimated in two stages. First, a [multinomial
choice model] is used to explain [treatment category]. Second, we estimate separate [outcome]
regressions for subsamples of observations on each [category], in which we include the
[non-selection correction] as a control variable.
[排他声明] [Instruments] function as instrumental variables in our model, and do not appear in
the second-stage models predicting [outcome]. While they are expected to affect [treatment
category], we assume that [instruments] do not directly affect [outcome] once we control for
[covariates].
[基线解释] The baseline category in [Table X] is [category C], so that the coefficients must
be interpreted as affecting the odds of choosing [category A] or [category B], relative to the
odds of choosing [category C].
[IV 相关性与样本损耗] We note that our instrumental variables do affect [treatment category],
as assumed: across all three categories they are jointly significant at the [p] level. Data
limitations reduced the number of observations at the first and second stage of the analysis to
[N1] and [N2] respectively.
[自有价值旁注] While we use the results in [Table X] as an intermediate step in estimating a
[two-stage estimator], these results are worth noting for their own merit: [interpretive reading
of the choice coefficients; label any puzzle as non-focal]. While not the focus of our research,
we believe that further analysis of [the puzzle] may prove fruitful.
[过渡] We now turn to the second step in estimating the [two-stage estimator].
```

**为什么有效**: 读者在进入第二阶段前拿到全部"读表协议"（基线=联盟、系数即相对联盟的 odds、IV 仅进第一阶段），第二阶段的分组回归就不会被误读；样本损耗（[N1]/[N2]）在同一处透明交代，避免表后补漏。第一阶段选择结果与主假设无关却被给予"own merit"旁注——把探索性结构（如买卖双方资产专用性的不对称）显式标记为值得后续研究的旁证，而不是把它包装成 confirmatory 发现。

**注意事项**: 旁注须自带非焦点标签（"not the focus of our research"）并将进一步分析 deferred；若第一阶段系数进入理论解读（如选择不对称的机制故事），需同时承认其推测性质。IV 排他声明是两阶段设计的识别命门——假设句必须完整落到"一旦控制 [协变量] 即无直接效应"的形式，不能只写"不出现在第二阶段"。

**反模式**: 第一阶段只报显著性不报基线类与解释规则（读者无法还原系数含义）；把第一阶段选择结果当作假设证据（它只支持选择侧的机制旁证，不检验绩效假设）；或反之完全跳过第一阶段结果（后续机制主张失去落点）。

**原文锚点**: "While we use the results in Table 4 as an intermediate step in estimating a switching regression model, these results are worth noting for their own merit."（Table 4 评论段首句；第二阶段交底句式见 Table 5 前段 "We now turn to the second step in estimating the switching regression model"）

**范文来源**: Gulati, Lawrence & Puranam (2005), *Strategic Management Journal* — RESULTS 前三段（Table 4 第一/二阶段交底）。

<!-- wb:gulati2005-adaptation-vertical:switching_reg_first_stage_intermediate_navigation -->

## 曲线结果写作反模式

- **正式 U 检验后置**：在主结果只凭二次项宣称支持、再把端点斜率与转折点区间埋进 robustness，会让核心结论先于核心证据。正式形状检验应紧邻假设判断。
- **交互项替代几何比较**：若假设预测顶点位置，必须比较顶点；若预测陡峭度或垂直位移，则应改用相应几何与预测量。
- **同号交互抹平异几何**：同一调节下两 IV 的 X²×W 同号时，不得省略分图对比而写成“调节方式相同”；shift 与 steepen 须分别命名。
- **不利倒 U 顶点写成最优中间**：adverse Y 的 vertex 是最大风险中间区，不是 performance optimum；Discussion 的 stuck-in-the-middle 隐喻不可替代 Results 的概率顶点报告。
- **尺度未标注**：logit-link 上的预测值不能被写成原始概率或结果单位变化；图与正文必须说明 response scale 或 link scale。
- **无效 p 值格式**：不得写 `p = .00` 或 `p < .00`，应写 `p < .001` 或报告可用的准确值。
- **选择性支持总结**：单独模型显著、完整模型仅边际显著时，应报告证据衰减，而不是用一句“全部支持”抹平差异。
- **附录稳健性无 threat 定位**：编号清单 + 一句 “results support our main analyses”，不逐条 threat 定位。
- **H 预测 weaken 却把边际反转写成同等 reversal**：须标 Interestingly；边际不得与 p<.05 混写。
