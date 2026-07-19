---
category: identification-exogeneity
description: 识别策略中的外生性论证句法——IV 排他性约束、自然实验外生性来源、控制函数识别变量的理论论证。
function: 可信性——让审稿人相信识别假设不仅是统计假设，更有理论基础
slots: M4, M7, M8
extracted_from: singh2023_jmr / eilert2017_jm
created: 2026-05-22
updated: 2026-05-22
---

# 识别策略外生性论证（Identification Exogeneity）

## 设计原则

识别策略的可信性不仅来自统计检验（F-statistic / Sargan-Hansen / 平行趋势），更来自**理论层面的外生性论证**。这类句法将统计假设转化为理论判断，是 IV/自然实验/控制函数设计的核心说服单元。

---

## 类型 1：外生性来源声明句

**功能**：直接声明识别变量的外生性来源。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `The exogeneity of [variable] stems from [theoretical reason].` | 安全 | M7/M8 |
| `[Variable] is exogenous because [institutional feature / policy design] ensures that [condition].` | 安全 | M7/M8 |
| `The exogeneity of [variable] stems from the efficient market hypothesis, which argues that the effects of [past events] should already be incorporated in [current prices / expectations].` | 安全 | M7（控制函数） |
| `Identification comes from [source of variation], which is plausibly exogenous to [outcome] because [reason].` | 安全 | M8 |

---

## 类型 2：IV 相关性论证句

**功能**：论证工具变量与内生变量的相关性（Relevance）。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We anticipate that [IV] and [endogenous variable] correlate [negatively/positively]: if [condition], [endogenous variable] should [decrease/increase].` | 安全 | M8 |
| `[IV] satisfies the relevance criterion because [theoretical mechanism linking IV to endogenous variable].` | 安全 | M8 |
| `Conceptually, this instrument meets the relevance criterion because [explanation of first-stage relationship].` | 安全 | M8 |

---

## 类型 3：IV 排他性约束论证句

**功能**：论证工具变量仅通过内生变量影响结果（Exclusion Restriction）。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Variable] seems unlikely to exhibit any association with [omitted factors] that determine [outcome]; rather, reasons to [observe variable] vary substantially across [units].` | 安全 | M8 |
| `[Variable] is unlikely to be directly associated with [outcome] because [theoretical / institutional reason].` | 安全 | M8 |
| `It satisfies the exclusion restriction because [theoretical argument for why instrument affects outcome only through predictor].` | 安全 | M8 |
| `Individual [variable] are unlikely to be directly associated with [firm-level outcome]; rather, reasons to [variable] likely vary substantially across individual [units].` | 安全 | M8（JMR 县级政治捐款 IV） |

---

## 类型 4：控制函数识别变量论证句

**功能**：在控制函数/Heckman 设计中论证第一阶段识别变量的外生性。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `[Variable] identifies the first stage because it should affect [first-stage outcome] but not [second-stage outcome], since [theoretical reason].` | 安全 | M7/M8 |
| `The exogeneity of [variable] stems from [efficient market hypothesis / institutional feature], which argues that [past information] is already incorporated in [prices/expectations] and therefore should not elicit [market reaction / behavioral response].` | 安全 | M7（JM 2017 past publicity） |
| `[Policy/shock] focused solely on [domain] and did not specify whether [decision] must [condition]. Therefore, it did not directly affect [outcome].` | 安全 | M7（JOM FDASIA） |

---

## 类型 5：统计验证预告句

**功能**：在理论论证后预告统计检验结果。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `We assess the empirical validity of the IV by examining its strength and exogeneity, using different tests.` | 安全 | M8 |
| `Before proceeding, we remove [contaminated observations] to ensure that [variable] is not confounded by [factor].` | 安全 | M8 |
| `The [F-test / Wu-Hausman test / Sargan-Hansen test] [rejects/fails to reject] the null hypothesis of [weak instruments / endogeneity / overidentification], supporting [conclusion].` | 安全 | M8 |

---

## 类型 6：概念论证→统计检验衔接句

**功能**：将理论层面的外生性声明与统计检验衔接。

| 微模板 | 风险 | 适用槽位 |
|--------|------|---------|
| `Conceptually, this instrument appears to meet the [relevance / exclusion restriction] criterion. [Statistical test] provides empirical support.` | 安全 | M8 |
| `The proposed instrument meets the [criterion] conceptually because [theory]. Empirically, [test result] confirms this.` | 安全 | M8 |

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `The IV is exogenous.` | 无论证，仅有断言 | `Individual contributions are unlikely to be directly associated with automotive recalls because reasons to donate vary substantially across contributors.` |
| `We use past publicity as an instrument because it is a good instrument.` | 循环论证 | `Past publicity is exogenous because the efficient market hypothesis argues that effects of past publicized recalls are already incorporated in stock prices.` |
| `The F-statistic is high, so the IV is valid.` | 混淆相关性与排他性 | `The F-test supports relevance; the Sargan-Hansen test does not reject the exclusion restriction.` |
