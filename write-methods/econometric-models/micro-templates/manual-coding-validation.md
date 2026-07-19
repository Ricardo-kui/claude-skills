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
