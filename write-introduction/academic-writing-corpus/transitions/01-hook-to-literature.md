---
type: canonical_reference
canonical_id: "01-hook-to-literature"
status: ✓ STANDARD
gap_type: all
cross_paper: VERIFIED
generativity: GENERATIVE
exclusivity: LOW
source_papers:
  - lashley_pollock2020 (ASQ, 2020): "This puzzle is not merely an industry-specific curiosity"
  - eilert2017 (JM, 2017): "Variation in recall timing raises important questions"
  - wu2025 (SMJ, 2025): "From activism risk to corporate self-regulation"
  - han2020 (AMJ, 2020): "From misconduct event to contextual evaluation"
created: 2026-05-19
source: Migrated from global corpus + MVP30 validation
---

# 01-hook-to-literature — 从 Hook 到学术对话的过渡

## 功能描述

在 Hook 的震撼/悬念之后，用一个过渡句将读者从具体现象或案例拉入学术对话。这个过渡句是 Introduction 的"枢轴"——它决定了论文能否从"有意思"升级为"值得研究"。

## 适用场景

- 所有类型的 Hook 都需要这个过渡
- 无论 Hook 是数据、轶事、悖论还是引语，都需要"理论升维"
- 目标读者需要从"具体现象"切换到"抽象学术问题"

## 验证状态

### 跨论文复现
- **VERIFIED** (≥4 papers): lashley_pollock2020 (ASQ), eilert2017 (JM), wu2025 (SMJ), han2020 (AMJ)
- 跨 ASQ, SMJ, AMJ, JM 四个主要期刊

### 生成力
- **GENERATIVE**: 所有学术 Introduction 的必备结构，可适配任何领域

### 排他性
- **LOW**: 通用型过渡，不绑定特定 Gap 类型

---

## 句法模板

### 变体 A：现象→理论化型（lashley_pollock2020 型）

**模板**:
> "This [puzzle / pattern / tension] is not merely a [industry-specific curiosity / management anecdote]; it reflects a broader [theoretical gap / unresolved debate] concerning [core theoretical issue]."

**来源**: lashley_pollock2020 (ASQ), P1

**原文锚定**:
> "This puzzle is not merely an industry-specific curiosity; it reflects a broader theoretical gap concerning how stigmatized organizations manage legitimacy."

**关键特征**:
- **"not merely"** → 否定特异性
- **"reflects a broader"** → 肯定普遍性
- **"concerning [core theoretical issue]"** → 指向理论

**适用**: 反直觉现象、悖论型 Hook 后的过渡

---

### 变体 B：案例→普遍化型

**模板**:
> "While [specific case] is [striking / extreme], it is [not unique / representative of a broader pattern]. [Evidence of broader pattern]. Scholars in [field] have long recognized that [existing knowledge], yet [transition to gap]."

**关键特征**:
- 先承认案例的特殊性，再论证其普遍性
- 用证据展示更广泛的模式
- 自然引入学术对话

**适用**: 具体案例/轶事型 Hook 后的过渡

---

### 变体 C：直接提问→文献对话型

**模板**:
> "[The hook question] points to a [deeper / broader] issue that has [attracted / divided] scholars for [time period]: [theoretical debate]."

**关键特征**:
- 将 Hook 中的问题重新框定为学术辩论
- "divided scholars" → 暗示理论张力

**适用**: 问题驱动型 Hook

---

### 变体 D：隐喻→概念化型

**模板**:
> "The [metaphor from hook] captures a [phenomenon / process] that [theorists / researchers] have [examined / debated] under the rubric of [concept]."

**关键特征**:
- 将 Hook 中的隐喻转化为学术概念
- "under the rubric of" → 优雅的学术过渡

**适用**: 使用隐喻、类比或形象化语言的 Hook

---

## 关键技巧：过渡句的三要素

一个有效的 hook-to-literature 过渡必须包含：
1. **否定特异性**："not merely" / "not unique" / "not isolated"
2. **肯定普遍性**："broader" / "systematic" / "enduring"
3. **指向理论**：具体的理论概念或学术对话名称

---

## 组装规则

### 必须配对
- **所有 Hook 都需要这个过渡**: 没有过渡的 Hook 会显得像"营销噱头"
- **过渡后立即接入 Literature Turn**: 过渡句只有 1-2 句话，展开是 Literature Turn 的工作

### 反模式提醒
- **"因此，研究这个问题很重要"**: 过于直白，缺乏理论升维 → 用 "reflects a broader theoretical gap concerning..." 替代
- **突然跳转到作者罗列**: "Smith (2000), Jones (2005)..." → 先建立对话框架，再引入具体学者
- **停留在现象层面**: "Many firms face this problem" → 必须立即理论化

### 长度控制
过渡句通常只有 **1-2 句话**。它的工作是"转轴"，不是"展开"。

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| 所有期刊 | ⭐⭐⭐⭐⭐ | 通用必备结构 |
| ASQ | ⭐⭐⭐⭐⭐ | 偏好 "reflects a broader theoretical gap" 型 |
| SMJ | ⭐⭐⭐⭐⭐ | 偏好 "points to a deeper issue that has divided scholars" 型 |
| AMJ | ⭐⭐⭐⭐⭐ | 偏好 "not merely... it reflects..." 型 |
| JM/JMR | ⭐⭐⭐⭐⭐ | 偏好紧凑过渡（1句话），快速进入文献 |

---

## 相关语料

- 配合 `hooks/*` 各类 hook 使用：每个 hook 都需要一个 hook-to-literature 过渡
- 配合 `literature-turns/*` 使用：过渡后自然接入 Progressive / Synthesized / Non-Coherence 策略
- 配合 `tensions/01-despite-progress-unaddressed.md` 使用：过渡后自然接入"尽管已有进展..."的文献综述