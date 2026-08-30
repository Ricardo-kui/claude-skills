---
type: phrasebank
corpus_id: phrasebank-quantities-trends
function: 量化表达与趋势描述（Results R1/R5 与图形趋势的措辞变化）
source_tier: auxiliary
source: "Morley, J. (2021). Academic Phrasebank (3rd ed.). University of Manchester. Ch.13 Describing Quantities + Ch.12 Describing Trends and Projections."
top_journal_validated: false
status: EMERGING
risk_level: needs-context
created: 2026-07-27
---

# Phrasebank: 量化表达与趋势描述（Morley 13+12 章收割）

> **层级定位**：auxiliary 语言实现层。slot-R1–R9 骨架决定**说什么**（四拍、导航、经济显著性）；本文件只在 R1 描述性统计、样本描述与图形趋势处提供**措辞变化**，防止跨论文表达同质化。
>
> **使用规则**（每次调用必读）：
> 1. **调用顺序**：顶刊 slot 骨架/变体 → 本文件变化库 → claim-strength QC。
> 2. 每个位置最多取 **2–3 个候选**；同一表格的转述不连续堆叠两个以上本文件句式。
> 3. **必须替换 X/Y 并具体化**（变量名、数值、样本）。
> 4. **Specificity gate**：替换后的句子若仍可不加修改放进任何论文 → 不合格，加入具体变量、幅度或基准。
> 5. 数字必须与估计输出逐位一致（`write-results/references/evidence-standards.md` 第 1 问）；approximator（nearly/approximately/just over）只在无法给出精确值时使用，且**不得与精确数字同句并存**（"nearly 48%" 是冗余——要么 "nearly half"，要么 "48%"）。
>
> **退役规则**：某功能一旦被顶刊蒸馏语料覆盖，对应条目从本文件删除。本文件不计入 MVP30 paper_count。

## 1. 分数与百分比（R1 / 样本描述）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "Over half of [those surveyed / the sample firms] indicated that ..." | R1 | descriptive | survey 偏管理档案研究改 "the sample firms" |
| "Nearly half of the respondents (48%) [agreed / reported] that ..." | R1 | descriptive | approximator 与精确数择一（见使用规则 5） |
| "Almost two-thirds of [the observations] (64%) ..." | R1 | descriptive | 低 |
| "Of the [270] [firms], nearly one-third [did not / failed to] ..." | R1 | descriptive | 样本筛选链可用 |
| "Less than a third of [those who responded] (32%) ..." | R1 | descriptive | 低 |
| "The response rate was [60]% at [six months] and [56]% at [12 months]." | R1/M2 | descriptive | 仅 survey |
| **Approximator 组合表**："[Just over / Well over / More than / Almost / Around / Approximately] [half / a third / a quarter] of [those surveyed / the respondents / the sample] ..." | R1 | descriptive | 同一节内 approximator 不重复用同一个 |

## 2. 均值与离散（R1）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "The mean [age/value] of [Xs] was [48.3] ± [6.3] [years/units]." | R1 | descriptive | ± 记法须与表格一致 |
| "The mean [X] for the [two groups] was subjected to [analysis] to determine ..." | R1/R7 | descriptive | 低 |
| "[Group A] had a much [lower/higher] than average [X]." | R1 | descriptive | 比较描述，非检验 |

## 3. 范围（R1 / 样本描述）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "The respondents had practised X for an average of [15] years (range [6] to [35] years)."→ 适配："The sample firms had been [listed/active] for an average of [N] years (range [a] to [b])." | R1 | descriptive | range 括注式 |
| "The participants were aged [19] to [25] ..."→ 适配："The [firms/observations] span [years/values] from [a] to [b]." | R1 | descriptive | 低 |
| "Rates of [decline] ranged from [2.71] to [0.08] [units] (Table [x]) with a mean of [0.97]." | R1 | descriptive | 附表引 |
| "Most estimates of X range from [200] to [700] and, in some cases, up to [a million]." | R1/Discussion | descriptive | 文献数值汇总时 |

## 4. 比率与比例（R1 / R5 经济显著性辅助）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "X had the [highest/lowest] proportion of Y at only [14] per cent." | R1 | descriptive | 低 |
| "The [annual rate] dropped from [44.4] to [38.6] per [1000] per [annum]." | R1 | descriptive | 率的分母须明确 |
| "The proportion of [X] was [65]% higher in [A] than [in B]." | R1/R5 | descriptive | 相对比较，非效应 |

## 5. 趋势描述（事件研究 / 时间序列图）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "The graph shows that there has been a [slight / steep / sharp / steady / gradual / marked] [fall / rise / drop / decline / increase / decrease] in the [number/rate] of ..." | R7/事件研究 | descriptive | 程度副词必须有视觉依据（visual-evidence.md §5 不夸大） |
| "Figure [x] reveals that there has been a [marked] [increase] in ..." | R7/事件研究 | descriptive | 同上 |

## 6. 图表趋势高亮（R2 导航 / 图解读句的变化）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "What is striking in this [table/figure] is the [growth of / variability of / difference between] ..." | R2/R7 | descriptive | 每篇至多一次，防套路 |
| "What stands out in this [figure] is the [rapid decrease in / steady decline of] ..." | R2/R7 | descriptive | 同上 |
| "What can be clearly seen in this [table] is the [general pattern of / dominance of] ..." | R2 | descriptive | 同上 |

## 7. 高低点（图描述）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "[X] peaked in [year/period]." | R7/事件研究 | descriptive | 低 |
| "The [number/rate] of Xs reached a peak during [period]." | R7/事件研究 | descriptive | 低 |
| "[X] reached a low point in [year]." | R7/事件研究 | descriptive | 低 |
| "The rate fell to a low point of [value] at the end of [period]." | R7/事件研究 | descriptive | 低 |

## 8. 外推语气（**仅限 Discussion**，Results 禁用）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "The [rate/number] of X is [likely to / expected to / projected to] [fall / rise / level off / remain steady] [after 2030]." | Discussion | speculative | **禁止**在 Results 用预测语气陈述事实；外推必须有模型依据 |

## 禁区

- 本文件**不提供**：假设检验四拍（归 slot-R3）、null findings 深化（归 slot-R6）、效应量解读（归 slot-R5）、趋势背后的因果解读（归 Theory/Discussion）——数值转述≠证据解释。
- 图表的**设计**纪律（截断纵轴、CI 显示、标题）归 `write-results/references/visual-evidence.md`；本文件只管措辞。
