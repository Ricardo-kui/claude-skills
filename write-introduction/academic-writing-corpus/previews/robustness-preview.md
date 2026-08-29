---
type: canonical_reference
canonical_id: "robustness-preview"
status: ✓ STANDARD
gap_type: all
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: LOW
source_papers:
  - darby2026 (JOM, 2026): Robustness-heavy preview with categorized listing
created: 2026-05-18
source: Extracted from MVP30 narrative_analysis files
---

# Robustness Preview — 稳健性/可信度预览句法

## 功能描述

不同于"发现预览"，稳健性预览的功能是让读者相信结果不会被内生性、测量误差或模型设定推翻。它不是预告发现了什么，而是预告**结果有多可信**。适用于方法复杂、检验繁多的实证论文。

---

## 变体 H：稳健性密集预览型（darby2026 型）

**模板**:
> "[Number] robustness checks provide further support for our findings. Our robustness checks included [category 1]; [category 2]; [category 3] to address [issue]; [category 4] to address [issue]; [category 5] to examine [issue]; [category 6] to address [issue]; [category 7] to examine [issue]; [category 8] to address [issue]; and [category 9] as alternative empirical strategies. To shed further light on the underlying mechanisms, we also conducted additional analyses using [mechanism test 1], [mechanism test 2], as well as [mechanism test 3]."

来源: darby2026 (JOM), P9

**原文锚定**:
> "Nineteen robustness checks provide further support for our findings. Our robustness checks included alternative vectors of matching covariates; propensity score matching; frailty models, shared frailty models, and marginal risk set models to address the recurrent nature of recall events; placebo treatment tests to address omitted variable concerns; panelized fixed effects models to examine reverse causality; alternative measures of institutional investor ownership to address simultaneity and measurement error; variance inflation factors to examine multicollinearity; winsorized values to address outliers; and Cox proportional hazard models and linear regression as alternative empirical strategies. To shed further light on the underlying mechanisms, we also conducted additional analyses using alternative measures of institutional investor ownership that reflect different magnitudes of ownership and different investment horizons as well as explore potential non-linearity."

**关键特征**:
- 用**分号**分隔不同类别，保持节奏感
- 每个类别后附带 "to address [issue]" 或 "to examine [issue]"，说明目的而非单纯罗列方法名称
- 最后一句区分 "robustness checks"（解决威胁）和 "additional analyses"（探索机制）
- 适用于：AFT + matching + frailty + placebo + alternative estimators 等方法复杂的论文

---

## 变体 H-紧凑版

**模板**:
> "Our findings are robust to [number] additional checks, including [method category 1], [method category 2], and [method category 3] ([specific issue addressed]). We also explore [mechanism exploration] to shed light on [theoretical question]."

**适用**: 当稳健性检验数量较少（3-5 项）或期刊篇幅限制较紧时

---


### 变体 I：三重识别+竞争层级排除预览型（wowak2020 型）
[功能标签]: Preview — 识别策略预告与竞争性解释排除（实质显著 null 作为证据）
[骨架]: "We address identification issues in robustness checks in [N] ways: [IV], [selection model], [reverse causality]... We test whether [rival actor] predicts [outcome] and serves as a mediator... we find no such evidence, substantiating our contention that [protagonist level], not [rival level], [drive outcome]."
[关键特征]: 稳健性预告不止防御（IV/selection/reverse causality 三联），还主动纳入一个竞争理论层级检验；把"竞争变量不显著"本身叙述为支持主角层级的实质性证据（substantiating our contention）；连接既有 board-level 文献收束
[适用]: 多层级治理研究（board vs TMT vs 职能高管），识别工具包成熟的 FE 设定
[禁忌]: 竞争变量需有真实理论对立资格；null 排除句必须回扣主角层级主张
**原文锚定**: "We test if the gender of the VP of quality predicts recall decisions and if it serves as a mediator in our model... We find no such evidence... substantiating our contention that the board of directors, and not managers, set the tone for recall decision-making."
**来源**: wowak_2020_female_directors_recalls (M&SOM), P7

## 组装规则

### 反模式提醒
- **不要只罗列方法名称**: 必须说明每个稳健性检验解决什么威胁（"to address endogeneity"）
- **不要把机制探索说成稳健性检验**: 区分 "robustness checks"（威胁处理）与 "additional analyses"（机制探索）
- **不要放在 Introduction 太靠前的位置**: 通常在贡献声明之前、实证预览之后
