---
result_type: "VARX-PVAR"
status: 🟢 EMERGING
source_papers:
  - "borah_tellis_2016_jmr (Journal of Marketing Research): GIRF-based halo metric (percentage of significant cross-effects), basis-points→dollars translation, FEVD relative importance, Venn diagram visualization, graded support language, dynamics (wear-in/wear-out), elasticity table"
variants_count: 7
created: 2026-07-15
updated: 2026-07-20
---

# VARX-PVAR — Results 骨架

## 主骨架

参见 `write-results/SKILL.md` → 填空段落骨架 → `VARX-PVAR`。

## 证据节奏摘要

VARX/PVAR Results 的叙事核心是**动态交叉效应的量化与可视化**。与传统 OLS 的"一个系数一个假设"不同，VARX/PVAR 需要管理：多实体间的 GIRF 溢出效应（percentage of significant cross-effects）、时间动态（wear-in/wear-out）、经济显著性（basis-points→dollars, FEVD relative importance）、以及多品牌重叠的可视化（Venn diagrams）。分级支持语言（"full/moderate/considerable support"）比二元"supported/not supported"更诚实。

## 累积变体

### 变体 1: R3 GIRF-based Halo Metric — Percentage of Significant Cross-Effects (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R3
**骨架**:
> We measure perverse halo as the percentage of times that concerns about any nameplate of one brand have a significant positive effect on concerns about any nameplate of another brand. A value of 0% would imply no perverse halo (brands are completely distinct), while 100% would imply perfect perverse halo (brands are indistinguishable). We compute this measure using the generalized impulse response function (GIRF) estimates from our VARX equations, counting the number of cross-nameplate effects that are significantly positive at the [N]% level. For the three Japanese brands, we find a total symmetric three-way perverse halo of [value]%, with the highest two-way overlap between [brand A] and [brand B] ([value]%). The exclusivity metric — the percentage of effects truly unique to one brand — is only [value]%. Thus, we find [full/moderate/considerable] support for Hypothesis [N]: perverse halo exists in online chatter.
**与原骨架差异**: 这是 **VARX/PVAR 设计下量化交叉效应的核心创新**。传统 OLS 报告单一系数，但 VARX 的 GIRF 产生 2,256 个交叉效应估计（48 nameplates × 47 cross-effects）。Borah & Tellis 的解决方案是将其聚合为"percentage of significant cross-effects"——0%=完全区分，100%=完全不可区分。这比报告单一系数或平均效应更能捕捉多实体间的溢出程度。
**范式排他性**: VARX/PVAR 专用。OLS/FE/Logit 不适用，因为它们不产生 GIRF 或 impulse response function。
**诚实边界**: GIRF percentage 的显著性检验应明确报告标准（如 one-standard-error band）和置信水平（如 p < .05）。不同标准可能导致 percentage 差异较大。若正文未报告置信区间，应在附录或脚注中说明显著性检验方法。

### 变体 2: R3 Graded Support Language — "Full/Moderate/Considerable Support" (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R3/R6
**骨架**:
> For Hypothesis [N], we predicted [prediction]. The results show [key_evidence]. Thus, we find [full/moderate/considerable] support for Hypothesis [N]. While the pattern is [consistent with theory], we note that [nuanced_finding: e.g., 17% reverse sign between Toyota and Chrysler] suggests that [boundary_condition] may moderate the effect.
**与原骨架差异**: 分级支持语言比二元"supported/not supported"更诚实。Borah & Tellis 使用：(1) "find support for H1" (full support, perverse halo exists); (2) "moderate support for H2" (mixed findings, same-country stronger but 17% reverse sign between Toyota-Chrysler); (3) "considerable support for H3" (asymmetric effects, downward 35% > upward 26%)。这种分级处理避免了将混合发现过度简化为"拒绝"或"支持"。
**范式排他性**: 无（通用）。适用于 OLS/FE/Logit/VARX/PVAR 等所有设计。
**设计变体**: 
  - Full support: 所有关键预测都得到支持
  - Moderate support: 主要预测得到支持，但存在例外或反向符号
  - Considerable support: 方向性预测得到支持，但幅度或边界条件与理论不完全一致
**诚实边界**: "moderate support" 不能用于事后挽救失败假设——必须有理论或数据支持为何 mixed findings 仍是边界条件下的证据。若假设完全被拒绝，应诚实报告"not supported"而非"moderate support"。

### 变体 3: R5 Basis-Points→Dollars Translation (Event Study + VARX) (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R5
**骨架**:
> A one-unit shock in concerns about [brand] has a [cumulative/peak] impact on [brand]'s abnormal returns of [N] basis points over [N] days. In dollar terms, this translates into a loss of approximately $[N] million from [brand]'s average market capitalization (calculated as accumulated basis points × average outstanding shares × average share price over the sample period).
**与原骨架差异**: 这是 **事件研究/市场反应论文的经济显著性标准**。Borah & Tellis 不仅报告 basis points（Toyota −42 bps, Honda→Toyota −18 bps, Chrysler→Toyota +20 bps），还将其翻译为美元损失（−$17.1M, −$7.3M, +$8.2M）。这种翻译让统计显著性延伸到实质影响——basis points 对学者有意义，但美元损失对经理和投资者更有说服力。
**范式排他性**: Event Study + VARX 专用（需要 abnormal returns 和 market cap 数据）。OLS/FE/Logit 不适用。
**设计变体**: 
  - 累积效应（accumulated basis points over N days）
  - 峰值效应（peak basis points on day N）
  - 跨品牌比较（focal vs rival）
  - 正负效应对比（loss vs gain）
**诚实边界**: 美元翻译的计算方法必须在脚注或附录中透明化——包括 average outstanding shares、average share price、时间窗口的选取。若不同年份的 shares 或 price 变化较大，应报告加权或分段计算。

### 变体 4: R5 FEVD Relative Importance — Partial-R² Analog for PVAR (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R5
**骨架**:
> We use forecast error variance decomposition (FEVD) to assess the relative importance of each endogenous variable in explaining the deviation in [focal outcome] from its baseline expectations. At [N]-day horizon, [variable A] explains [N]% of the variance, while [variable B] explains [N]%. The FEVD measure is analogous to a partial R², indicating the marginal contribution of each variable when all other endogenous variables are included in the model. Thus, [variable A] accounts for substantially more of the variance in [focal outcome] than [variable B].
**与原骨架差异**: 这是 **PVAR 设计下量化变量相对重要性的标准方法**。Borah & Tellis 使用 FEVD 来分解销售变异：focal nameplate concerns 解释 6.6%，nearest rival concerns 解释 2.1%。FEVD 是 OLS 中 partial-R² 的时间序列等价物——它告诉读者"在控制了其他所有内生变量后，变量 X 解释了 Y 的变异的 N%"。
**范式排他性**: PVAR/VARX 专用。OLS/FE 有传统的 R² 和 partial-R²，不需要 FEVD。
**设计变体**: 
  - 不同时间 horizon（10-day, 20-day, 30-day）
  - 跨变量比较（focal vs rival vs controls）
  - 跨样本比较（Japanese brands vs Toyota-Chrysler）
**诚实边界**: FEVD 依赖于 VARX 的变量排序（ordering of Cholesky decomposition）。不同的排序可能导致不同的 FEVD 值。应在 Methods 或附录中说明排序的理论依据（如"we order variables based on temporal precedence: recall → concerns → sales"）。

### 变体 5: R3/R4 Venn Diagram Visualization of Halo Overlap (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R3/R4
**骨架**:
> Figure [N] illustrates the estimated perverse halo among [brands A, B, C] using area-proportional Venn diagrams. The overlapping regions represent the extent to which negative concerns about one brand spill over to concerns about another brand. We find [three-way overlap]% symmetric three-way halo among the three brands, with the highest two-way overlap between [brand A] and [brand B] ([value]%). The exclusivity metric — the non-overlapping portion — indicates that only [value]% of concerns are truly brand-specific. This pattern suggests that perverse halo is [extensive/limited] among [brands].
**与原骨架差异**: 这是 **多品牌 halo 重叠的可视化标准**。Borah & Tellis 使用三个 Venn diagram（Figure 2A/B/C）分别展示：(1) 对称三向/两向重叠（Figure 2A）；(2) Downward halo（dominant → less dominant, Figure 2B）；(3) Upward halo（less dominant → dominant, Figure 2C）。Venn diagram 比纯数字更直观——读者一眼就能看出 Toyota-Honda-Nissan 的 halo 是高度重叠的（exclusivity 仅 26–33%）。
**范式排他性**: VARX/PVAR + 交叉效应研究专用。OLS/FE/Logit 通常不产生多实体交叉效应，不需要 Venn diagram。
**设计变体**: 
  - 三向 Venn（Figure 2A 风格）
  - 单向 halo（downward vs upward, Figure 2B/C 风格）
  - 跨国家比较（Japanese brands vs Toyota-Chrysler）
  - 面积比例 Venn（area-proportional, 使用 Chow & Rodgers 2005 算法）
**诚实边界**: Venn diagram 的区域面积应与实际 percentage 成正比（area-proportional）。若使用标准 Venn（面积不按比例），应在图注中说明。推荐使用 Matlab 的 Chow & Rodgers (2005) 算法生成面积比例 Venn diagram。

### 变体 6: R5 Elasticity Table for Symmetric Two-Way Halo (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R5
**骨架**:
> Table [N] displays the elasticities of online chatter for symmetric two-way perverse halo between brand pairs. The elasticity of [brand pair A] is [value]%, meaning a 1% increase in negative chatter about one nameplate increases negative chatter about another nameplate of the same country by approximately [value]%. For cross-country pairs (e.g., [brand pair B]), the elasticity is lower ([value]%), suggesting that perverse halo is weaker when brands are from different countries.
**与原骨架差异**: 这是 **VARX/PVAR 设计下报告交叉效应弹性的标准方式**。Borah & Tellis 报告 symmetric two-way elasticities：Toyota-Honda 12.1%, Honda-Nissan 7.0%, Toyota-Nissan 7.1%, Toyota-Chrysler 5.9%。弹性比系数更易解释——1% increase in X → Y% increase in Y。这与 OLS 中的 elasticity 解释（β × SD(X)/SD(Y)）不同，VARX 的 elasticity 直接来自 GIRF 的累积效应。
**范式排他性**: VARX/PVAR 专用。OLS/FE 的 elasticity 需要额外计算（mean-centering + SD rescaling），而 VARX 的 elasticity 直接由 GIRF 提供。
**设计变体**: 
  - 单向弹性（one-way perverse halo: Toyota→Honda 17.0%, Honda→Toyota 7.1%）
  - 对称两向弹性（symmetric two-way: Toyota-Honda 12.1%）
  - 跨国家比较（Japanese brands avg 8.73% vs Toyota-Chrysler 5.9%）
**诚实边界**: Elasticity 的计算方法应在附录或脚注中说明（如 "arc elasticity formula used to calculate elasticity, following Trusov, Bucklin, & Pauwels 2009"）。若使用 log-linear specification，elasticity 直接等于系数；若使用 level-level specification，elasticity 需要额外标准化。

### 变体 7: R3 Dynamics — Wear-in/Wear-out Period (1篇高价值)
**来源论文**: Borah & Tellis 2016 (Journal of Marketing Research)
**验证状态**: 通过（单篇入库，待第二篇交叉验证）
**写入日期**: 2026-07-15
**槽位**: R3
**骨架**:
> Regarding the dynamics of perverse halo, we find that the effect has a short wear-in period of [N] day, and most of the accumulated effect reaches the asymptote within [N] days. This suggests that [management implication: e.g., firms should respond quickly to recall events to prevent persistent damage].
**与原骨架差异**: 这是 **时间序列/脉冲响应分析的关键补充**。Borah & Tellis 报告 perverse halo 的 wear-in period 为 1 day，asymptote 为 6 days。这意味着负面溢出效应很快达到峰值，并在一周内趋于稳定。这比仅报告"显著效应"更有管理启示——firm 可以据此制定危机沟通的时间表（如"前 3 天是关键窗口"）。
**范式排他性**: VARX/PVAR 专用。OLS/FE/Logit 无法捕捉时间动态（除非使用滞后项或 distributed lag models）。
**设计变体**: 
  - Wear-in period（从 0 到峰值的时间，如 1 day）
  - Wear-out period（从峰值衰减到 0 的时间，如 10 days）
  - 渐近时间（达到 90% 最终效应的时间，如 6 days）
  - 滞后效应（lagged effects, 如 t+2, t+3）
**诚实边界**: 时间动态的定义应在 Methods 或附录中标准化（如 "wear-in period = time to peak effect; wear-out period = time from peak to 0"）。若使用 asymptote，应说明"90% of final effect"或"95% of final effect"的阈值标准。

## 反模式

| 反模式 | 表现 | 应做 |
|--------|------|------|
| **VARX 结果仅报 GIRF 系数但不报 percentage** | 仅报告单一 GIRF 系数或平均效应，不聚合为 percentage of significant cross-effects | 使用变体 1 的 GIRF percentage 作为核心效应测度 — 它比单一系数更能捕捉多实体间的溢出程度 |
| **事件研究仅报 basis points 但不翻译为美元** | 仅报告统计显著性（basis points），不报告经济显著性（美元损失） | 使用变体 3 的 basis-points→dollars translation — 让统计显著性延伸到实质影响 |
| **FEVD 未报告为 partial-R² 类比** | 仅报告 FEVD 数值，不解释其为"relative importance"或"partial-R²" | 使用变体 4 的 FEVD relative importance 解释 — 读者更易理解 |
| **混合发现二元化** | 将混合发现（如 H2 的 17% reverse sign）简化为"支持"或"拒绝" | 使用变体 2 的分级支持语言 — "moderate support"比"拒绝"更诚实 |
| **Venn diagram 面积不按比例** | 使用标准 Venn（面积不按实际 percentage），误导读者对重叠程度的感知 | 使用面积比例 Venn diagram（area-proportional，Chow & Rodgers 2005 算法） |
| **Dynamics 未报告或仅嵌入脚注** | 时间动态（wear-in/wear-out）仅在脚注或附录中提及 | 使用变体 7 将 dynamics 作为独立段落 — 这是 VARX/PVAR 的核心优势 |

## 诚实边界

- **GIRF percentage 的显著性标准**: 必须在正文或脚注中说明显著性检验方法（如 one-standard-error band, p < .05）和置信水平。不同标准可能导致 percentage 差异较大。
- **Basis-points→dollars 的计算透明性**: 美元翻译的计算方法必须在脚注或附录中透明化——包括 average outstanding shares、average share price、时间窗口的选取。
- **FEVD 的变量排序依赖性**: FEVD 依赖于 VARX 的变量排序（Cholesky decomposition ordering）。应在 Methods 或附录中说明排序的理论依据。
- **Venn diagram 的面积比例**: 若使用标准 Venn（面积不按比例），应在图注中说明。推荐使用面积比例 Venn（area-proportional）。
- **分级支持的边界**: "moderate support" 不能用于事后挽救失败假设——必须有理论或数据支持为何 mixed findings 仍是边界条件下的证据。
- **时间动态的定义标准化**: Wear-in/wear-out/asymptote 的定义应在 Methods 或附录中标准化（如 "asymptote = 90% of final effect"）。

## 跨 Skill 对齐

- **write-methods/VARX-PVAR.md**: Methods 应预告 GIRF percentage、basis-points→dollars、FEVD、Venn diagram 的设计和计算方法。
- **write-theory/ halo-theory.md**: Theory 应明确定义"perverse halo"为 0–100% 的连续测度，而非二元"存在/不存在"。
- **write-discussion/ managerial-implications.md**: Discussion 应使用 dynamics（wear-in 1 day, asymptote 6 days）和美元损失（$3.8M/mo）来制定管理建议。

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| JM/JMR | ⭐⭐⭐⭐⭐ | 标准 VARX/PVAR 报告；GIRF percentage、basis-points→dollars、FEVD、Venn diagram 全部需要 |
| SMJ | ⭐⭐⭐⭐ | 需要更强的理论-结果对齐；dynamics 和经济显著性必须清晰 |
| AMJ | ⭐⭐⭐ | 需要额外内生性讨论；FEVD 的变量排序需要理论背书 |
| MSOM | ⭐⭐⭐⭐⭐ | 适合运营 trade-off 类研究；dynamics 是关键优势 |
| Marketing Science | ⭐⭐⭐⭐ | 需要 robust technical appendix（VARX specification, GIRF calculation, FEVD ordering） |

---

**Created: 2026-07-15**
**Distilled from: Borah & Tellis 2016 (JMR)**
**Status: EMERGING (待第二篇交叉验证)**
