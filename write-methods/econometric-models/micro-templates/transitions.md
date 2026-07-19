---
category: transitions
description: 过渡衔接短语——段落内部的逻辑推进标记，让多句段落读起来有清晰的推进感而非堆砌。
function: 连贯性——连接段内不同层次的理由、变量、检验
slots: M1-M10 任意多句段落
extracted_from: 21 design-type corpus files
created: 2026-05-22
updated: 2026-05-22
---

# 过渡衔接短语（Transitions）

## 使用原则

过渡短语不是装饰，而是**论证推进的路标**。每当你要在同一段落中切换层级（从 firm-level 到 board-level）、切换变量（从控制 A 到控制 B）、或切换逻辑（从主论点到反论点），都需要过渡。

## 按功能分类

### 1. 层级递进（Level Progression）

用于控制变量段落（M6）中按分析层级递进时。

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `We first included [level_1]_level factors...` | 中 (4/28) | 安全 |
| `We also controlled for [level_2]_level characteristics...` | 中 (4/28) | 安全 |
| `In doing so, we aimed to address alternative explanations related to...` | 中 (4/28) | 安全 |
| `[Actor_type] can influence both [IV] and [DV], so [number] [actor_type] characteristics were controlled for.` | 中 (4/28) | 安全 |
| `Lastly, we included firm and year fixed effects...` | 中 (4/28) | 安全 |
| `Beyond these factors, we also controlled for...` | 低 (2-3/28) | 安全 |
| `In addition to [prior level] controls, we included...` | 低 (2-3/28) | 安全 |

### 2. 理由枚举（Reason Enumeration）

用于 M1 Setting 论证（"for N reasons"）或 M8 多维度威胁处理。

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `First, [setting property] makes [mechanism] observable.` | 高 (28/28) | 安全 |
| `Second, [scope condition] reduces [confound].` | 高 (28/28) | 安全 |
| `Third, [data feature] allows us to observe [unit/process] over [period].` | 高 (28/28) | 安全 |
| `Building on this logic, [next reason].` | 低 (1-2/28) | 安全 |
| `Moreover, [additional reason].` | 低 (2-3/28) | 安全 |

### 3. 逻辑转折（Contrast / Pivot）

用于引入竞争性解释、反例或边界条件。

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `However, [counter-argument or boundary].` | 中 (5-8/28) | 安全 |
| `Conversely, [alternative prediction].` | 低 (1-2/28) | 安全 |
| `Although [assumption] cannot be directly tested, [evidence reduces concern].` | 中 (3-4/28) | 安全 |
| `While [acknowledged limitation], [mitigating factor].` | 中 (3-4/28) | 安全 |
| `That is, it is not..., but, rather, [refined claim].` | 低 (1-2/28) | 安全 |

### 4. 因果/机制推进（Mechanistic Advance）

用于连接理论到操作化、或统计结果到机制解释。

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `This suggests that [mechanism] drives the relationship.` | 中 (4-5/28) | 需注意：不要在 Methods 中报告结果 |
| `By including [control_variable], [estimator] can generate unbiased coefficients.` | 低 (1-2/28) | 安全 |
| `Thus, although [acknowledged limitation], [conclusion].` | 低 (2-3/28) | 安全 |
| `Overall, prior studies conclude that [variable] is key to...` | 低 (1-2/28) | 安全 |

### 5. 程序推进（Procedural Advance）

用于描述多步骤方法时的衔接。

| 微模板 | 来源频率 | 风险 |
|--------|---------|------|
| `The model estimation proceeds in two stages.` | 低 (1-2/28) | 安全 |
| `In the first stage, we model...` | 低 (2-3/28) | 安全 |
| `In the second stage, we test...` | 低 (2-3/28) | 安全 |
| `To validate [assumption], we [next step].` | 低 (2-3/28) | 安全 |
| `Next, we [next procedure].` | 低 (2-3/28) | 安全 |

---

## 控制变量段落的完整过渡链示例

```text
We included a broad set of control variables that influence [DV] directly
and those that help address alternative explanations (Shang & Rönkkö 2022).
**We first included** recall-level factors that may influence how [DV] is handled.
**To address** alternative explanations stemming from [concern_1],
we included [control_1]...
**We also controlled for** firm-level characteristics that have been shown to
influence [DV]. **In doing so**, we aimed to address alternative explanations
related to [concern_3]...
**Lastly**, we included firm and year fixed effects to account for
[time_varying_concerns] as well as [time_invariant_concerns].
```

---

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We control for A. We control for B. We control for C.` | 无过渡，像清单 | 用层级递进过渡连接 |
| `And then... And then...` | 口语化 | 替换为 "Next," / "Building on this," |
| `So...` | 口语化 | 替换为 "Thus," / "Therefore," |
| `Anyway...` | 口语化 | 删除 |
