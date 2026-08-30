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

### 6. 章节级路标（Section-Level Signposting）— Morley 16 章收割

> **来源**：Morley (2021) Ch.16 *Signalling Transition* 的 section-preview / reintroduce / move-to-next 三类。
> **与 §1-5 的区别**：§1-5 是**段内/段间**的微观过渡（递进/枚举/转折/因果/程序）。本节是**跨 section 宏观路标**——section 开头预告本节将做什么、衔接上一节、或回指前文已定义的概念。在 write-methods/results/theory 的 section 开头与衔接处使用。
> **限定**：只取 Morley 的 section-preview / reintroducing-a-topic / moving-between-sections 三类，**跳过** chapter/thesis preview（学位论文语境，FT50 论文不用）。每个位置最多用 1 个路标，避免路标堆砌。

**预告本节内容（previewing a section）**— section 首段：
- Having established [the theoretical predictions / the construct definitions], we now turn to [the empirical strategy / the methods used to test them].
- To test these hypotheses, we first describe [the sample and data], then [the variable operationalizations], and finally [the estimation approach].
- This section outlines [the research context / the analytical approach] and justifies [the design choices].

**回指前文概念（reintroducing a topic）**— 跨 section 引用：
- As discussed above / As noted in the [theory] section, [construct] [captures/reflects] [definition].
- Recall that [Hypothesis X] predicted [relationship]; we test this by [method].
- Building on the [mechanism] developed earlier, we [hypothesize/examine]...

**节间移动（moving between sections）**— section 衔接：
- We now [examine / turn to] [the results / the robustness checks].
- Having [described the sample / defined the variables], we next [report / estimate]...
- These [design choices / identification concerns] motivate the [analyses / robustness checks] that follow.

**反模式（章节级）**：
- 路标堆砌（一段内用 3 个 "Having... we now... turning to..."）——每个 section 开头最多 1 个预告路标。
- 过度回指（"As mentioned in the Theory section, as we discussed, recall that..."）——一次回指即可。
- 学位论文式章节预览（"In this chapter, we will first... then... finally... across seven sections"）——FT50 论文 section 短，不需要整章路线图。

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| `We control for A. We control for B. We control for C.` | 无过渡，像清单 | 用层级递进过渡连接 |
| `And then... And then...` | 口语化 | 替换为 "Next," / "Building on this," |
| `So...` | 口语化 | 替换为 "Thus," / "Therefore," |
| `Anyway...` | 口语化 | 删除 |
