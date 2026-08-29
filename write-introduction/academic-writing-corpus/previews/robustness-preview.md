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


### 变体 J：单句枚举+同市场跨事件复制预览型（fang2025 型） EMERGING（1 篇范文）

**模板**:
> "We report [N] robustness tests using [an alternate estimation window], [an augmented estimation strategy], [an alternate estimator], [a falsification test], and [alternative measures of the lever]. Last, aiming to boost the generalizability of our findings, we replicate the identified effects with [another same-type event in the same market] and obtain consistent results."

**来源**: fang_et_al_2025_rival_recall_ad_spend (Production and Operations Management), P14

**原文锚定**:
> "Last, aiming to boost the generalizability of our findings, we replicate the identified effects with another car recall event in the same market and obtain consistent results."

**关键特征**:
- **单句枚举极限压缩**：五项检验用 "using A, B, C, D, and E" 一句带过，不给逐项威胁说明——与变体 H（逐项 to address X）相反的压缩极
- **跨事件复制作为泛化装置**：句子的重心不在稳健性而在 generalizability——用同市场内另一同类事件复制效应，把"结果稳健"升级为"规律可迁移"；既有变体 H/I 均以识别防御收尾，无复制装置
- **"Last, ..." 收束位**：复制句置于 preview 链最末、贡献段之前，作为可信度的最终一击

**适用**: 单一事件研究且同市场存在可比第二事件的准实验论文；篇幅受限、检验自明的场景；POM/MSOM/JM 事件研究

**禁忌**: 单句枚举仅当各检验名称自明（alternate estimator / falsification test）时可用，否则按文件反模式补 "to address [threat]"；复制事件必须与主事件同市场、同机制、不同标识，否则复制句不成立；复制结果须在正文/附录真实兑现

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
