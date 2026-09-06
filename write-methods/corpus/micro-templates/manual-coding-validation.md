---
category: manual-coding-validation
description: 手工编码与效度检验叙述句法——描述如何从原始文本/痕迹中提取构念并进行编码效度验证。
function: 对齐性——论证文本/档案构念的测量确实捕捉了理论构念
slots: M3, M4
extracted_from: malik2025_jom / mayo2023_poms
created: 2026-05-22
updated: 2026-05-22
---

# 手工编码与效度检验（Manual Coding Validation）

## 设计原则

当变量需要从原始文本、档案或行为痕迹中手工构建时，审稿人会质疑：编码是否可靠？不同编码者是否一致？替代操作化是否得到相似结果？这类句法提供**从原始痕迹到分析变量的完整可审计链**。

---

## 类型 1：编码流程总起句

**功能**：概述手工编码的整体流程。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We [downloaded / collected] all [documents] from [source] for the sample period and [processing step].` | 安全 | M3/M4 |
| `Two coders—the [author] and an external researcher [description]—independently reviewed [flagged items] and developed codes to determine [coding objective].` | 安全 | M3/M4 |
| `We created a special program in [software] to parse [text elements] into separate columns from the downloaded files.` | 安全 | M3/M4 |

---

## 类型 2：编码标准说明句

**功能**：说明编码的判断标准和分类规则。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We flagged [documents] if they contained the following word roots: [word list].` | 安全 | M3/M4 |
| `We assigned [variable] a value of [code A] if [condition], and [code B] otherwise.` | 安全 | M3/M4 |
| `We designated [observation] as [category] if [matching condition], otherwise we coded it as [alternative category].` | 安全 | M3/M4 |
| `We searched for the presence of [keyword] in each [document] and reviewed all [documents] that contained the word to match against [dataset].` | 安全 | M3/M4 |

---

## 类型 3：编码者一致性句

**功能**：报告编码者之间的一致性水平。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The coders discussed differences in coding (less than [percentage]% of cases) and reached a consensus.` | 安全 | M3/M4 |
| `Inter-coder agreement was [percentage]% / [Cohen's kappa = value], indicating [acceptable/substantial] reliability.` | 安全 | M3/M4 |
| `Differences were resolved through discussion until full agreement was reached.` | 安全 | M3/M4 |

---

## 类型 4：效度检验句

**功能**：论证编码结果的构念效度。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We checked the difference in [measure] before and after [event] by using [t-test] and found that [measure] became significantly [direction] after [event] (mean difference = [value], t = [value]), supporting the relevance of [measure] in shaping [outcome].` | 安全 | M3/M4（JOM media coverage） |
| `We validate this measure by [face-validity / convergent-validity check], showing that [correlation / pattern with external benchmark].` | 安全 | M3/M4 |
| `We assess the reliability of this coding by [inter-coder agreement / match rate], which was [value].` | 安全 | M3/M4 |

---

## 类型 5：替代操作化稳健性句

**功能**：说明用替代编码标准检验结果稳健性。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `As a robustness check, we [alternative operationalization: e.g., widened the window to 60 days / changed the keyword list / used a different coding threshold] and found [consistent / qualitatively identical] results.` | 安全 | M3/M4 |
| `We also examine [alternative operationalization] as a robustness check.` | 安全 | M3/M4 |
| `Our results are robust to [alternative window / alternative keyword / alternative classification].` | 安全 | M3/M4 |

---

## 类型 6：档案痕迹匹配句

**功能**：描述如何从档案文件（如 10-K）中搜索和匹配痕迹。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `For each [unit] in the study, we obtained all available [documents] for all years of the study period.` | 安全 | M3/M4 |
| `We searched for the presence of [keyword] in each [document] and reviewed all [documents] that contained the word to match against [dataset].` | 安全 | M3/M4 |
| `If a specific [observation] is mentioned in any of the [unit]'s [documents], we designate it as [category]; otherwise we code it as [alternative category].` | 安全 | M3/M4 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We coded the variable manually.` | 未说明编码标准、编码者、一致性 | `Two coders independently reviewed flagged press releases using predefined criteria; differences (<1%) were resolved by consensus.` |
| `The measure is reliable.` | 无证据 | `Inter-coder agreement was 98.5% (Cohen's kappa = 0.94), indicating near-perfect reliability.` |
| `We searched the 10-Ks.` | 未说明搜索关键词和匹配逻辑 | `We searched for "recall" in each 10-K and matched mentions against our recall dataset to classify discretion.` |


### 变体 A：反规则手册编码协议（westphal_zajac_1998_symbolic_management 型）

**模板**:
> "We decided not to furnish coders with an exhaustive rule book dictating the categorization of every possible phrase or combination of phrases; [methodologist] ([year]) noted that such coding strategies can artificially inflate reliabilities while sacrificing the content validity of the coding scheme. Accordingly, we simply provided coders with a summary description of [the theory], including a short list of key concepts characterizing the theory, and specific coding instructions. The coders included [coder descriptions]. We asked coders to determine whether [the construct] was present anywhere in [the document]. Thus, the ''recording unit'' (i.e., the unit of analysis) is the entire [document]. Pre-negotiation intercoder reliabilities were very high, with [coefficients] ranging from [.X] to [.X] and an agreement rate of [X] percent, suggesting minimal ambiguity in the coding scheme. [X] percent of [the documents] included [the coded construct]."

**来源**: westphal_zajac_1998_symbolic_management (ASQ), Method §Independent Variables / Agency Explanations

**原文锚定**:
> "We decided not to furnish coders with an exhaustive rule book dictating the categorization of every possible phrase or combination of phrases; Holsti (1968) noted that such coding strategies can artificially inflate reliabilities while sacrificing the content validity of the coding scheme."

**关键特征**:
- 把"没有穷尽式编码规则书"从潜在弱点预辩成方法论美德：引方法论权威（Holsti）论证规则书会人为推高信度而牺牲内容效度——预判审稿人"你的编码标准在哪"的质疑并提前化解
- 显式声明 recording unit（=整份文档）并补一句全文档扫查的 diligence 声明（"we nevertheless carefully checked the entire [section]"）——单元选择与遗漏风险一次封口
- 信度报告三件套：编码者构成（学生背景如实披露）+ pre-negotiation 相关系数区间与一致率 + "suggesting minimal ambiguity" 的解释性收尾，再接编码占比作为 prevalence 描述

**适用**: 理论构念（而非关键词匹配）的人工编码研究；预期审稿人质疑编码标准主观性时；用"低结构化+高信度"论证编码方案内容效度的场景

**禁忌**: 反规则手册策略必须以高 pre-negotiation 信度兑现（本篇 .903-.972/95%），否则等于承认方案模糊；引证的反对规则书的方法论权威必须真实存在且语境相符

**验证状态**: VERIFIED — expert_audit_override (user 2026-08-28: 单源足矣; paper_count=1)



### 变体 B：问卷量表开发效度链（carpenterwestphal2001 型）

**模式**: 预测试 → 题项依据 → 反偏差设计 → 信度 → 因子效度 → 因子计分，六环相扣，每环配方法论文献。

```
[预测试] To enhance the construct validity of the survey measures, we conducted a pretest involving in-depth pilot interviews with [N] [target respondents] ([methodology citation]).
[题项依据] The wording of each question was developed from available [qualitative research] ([citations]) suggesting how [respondents] describe [the construct domain]; in addition, we used feedback from the pilot interviews to further improve the clarity and face validity of each question.
[反偏差设计] Multiple response formats were used to reduce response bias, and items measuring each construct were scattered throughout the survey ([citation]); moreover, we carefully worded questions to minimize the likelihood of [social desirability] bias.
[信度] Cronbach's alpha for this scale was [.88], suggesting acceptable interitem reliability ([citation]).
[因子效度] After a factor analysis was applied to the survey items using the [iterated principal factors] method, a scree test indicated [k] common factor(s), and [promax] rotation verified that all items loaded on the same factor as expected, with loadings for each item greater than [.5].
[区分效度双界] [Rotation] indicated that the [construct A] and [construct B] items loaded on different factors as expected, with loadings for each item greater than [.5] on one factor and less than [.2] on the other.
[计分收口] Thus, we estimated [factor scores] using the [Bartlett] method ([citation]).
```
**要点**:
- 区分效度用"双界载荷"判据（目标因子 >.5 且竞争因子 <.2）——比单报告载荷更有判别力，可直接迁移
- 每个程序名（scree test / promax / Bartlett）照写并配文献，不解释教科书内容
- 题项"依据链"（质性文献 → 预测试反馈 → face validity）把测量扎根于既有质性研究，是问卷构念效度的正面论证
**诚实边界**: 本链是 1990s-2000s AMJ 惯例链；当代投稿通常还需 CFA 拟合指数与 HTMT，不要照抄当作充分条件。
**范文锚点**: "To enhance the construct validity of the survey measures, we conducted a pretest involving in-depth pilot interviews with 22 top managers and board members (cf. Fowler, 1993: 102). ... we carefully worded questions to minimize the likelihood of social desirability bias."

<!-- wb:carpenter_and_westphal_2001_strategic_context_of_external_ne:m3_survey_scale_development_validity_chain -->


### 变体 C：跨源构念效度三角化 — 独立评定者 kappa + 档案收敛/区分交叉矩阵（gulati_westphal1999 型）

**来源论文**: Gulati & Westphal 1999 (Administrative Science Quarterly, 44(3), 473-506)
**原始句锚点**: "The archival measure of control was significantly correlated with the survey measure of control (r = .42), while the archival measure of cooperation was significantly correlated with the survey measure of cooperation (r = .34). Moreover, the survey measure of cooperation was not significantly correlated with the archival measure of control, while the survey measure of control was not associated with the archival measure of cooperation."
**验证状态**: EMERGING（单源；Gulati 系单源即 VERIFIED，expert_audit_override 2026-09-06）
**写入日期**: 2026-09-06
**槽位**: M3/M4（关键自报构念的效度验证层）
**骨架**:
> [多源效度总起] We also conducted tests of [convergent] validity for our [survey] measures of [construct A] and [construct B]. [独立评定者层] We also assessed [interrater] reliability by comparing [primary respondents'] and [qualified independent respondents'] responses on the [construct] items, using [chance-corrected agreement statistic], which corrects for the level of [agreement] that would be expected by chance; values exceeding [threshold] typically indicate [excellent] agreement ([citations]). [档案复合测量层] First, we developed [archival] measures of each construct from [structural indicators] that are thought to [facilitate the construct's behavioral expression], combined into a [composite] using [standard scaling procedure] ([citations]). [收敛格×2] The [archival] measure of [construct A] was significantly correlated with the [survey] measure of [construct A] ([r = X]), while the [archival] measure of [construct B] was significantly correlated with the [survey] measure of [construct B] ([r = Y]). [区分格×2] Moreover, the [survey] measure of [construct B] was not significantly correlated with the [archival] measure of [construct A], while the [survey] measure of [construct A] was not associated with the [archival] measure of [construct B]. [交叉矩阵收口] This analysis provides further evidence for the construct validity of the [survey] measures. [相邻构念三角校验（可选第三层）] We also examined the correlation between [the archival measures] and a [survey] measure of [adjacent construct]; this measure showed high [interrater] reliability ([kappa]), and is [positively] associated with [construct A] ([r]) and [negatively] correlated with [construct B] ([r]). This further supports the [convergent] validity of the [survey] measures.
**与原骨架差异**: 变体 B（carpenterwestphal2001）是**问卷内部**量表开发六环链（预测试→题项依据→反偏差→信度→双界因子→计分）；本变体是**跨源三角化**——自报构念经三层独立证据验证：(1) 角色分离的独立评定者一致性（chance-corrected kappa，报告判定阈值）；(2) 档案复合测量的 2×2 收敛/区分交叉矩阵（各自收敛显著 + 交叉两格零相关——区分效度由**零相关格**承担而非单向高相关）；(3) 相邻构念符号模式校验（正/负号与理论方向一致）。区别于 post_2022 文本构念链（算法标注 vs 主体自分类）：此处两源均为传统测量（survey vs archival），关键手法是交叉矩阵的完整四格报告。
**诚实边界**: era_flags——LISREL CFA + Bartlett vs regression 因子估计法之辩（1999 年测量学惯用段）与 kappa 对连续题项按四分位离散化均不迁移。交叉矩阵要求四个相关格都报告（含零格）；只报两个收敛格会退化为普通 convergent 声明。档案复合测量本身的理论关联（为何这些结构指标是该构念的表现）需各配一句 because，否则收敛相关无解释力。


<!-- wb:gulati_westphal_1999_cooperative_or_controlling:m4_multisource_construct_validity_triangulation -->
