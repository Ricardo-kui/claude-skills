---
type: phrasebank
corpus_id: phrasebank-methods-process
function: 过程描述语法工具箱（Methods 句子级措辞变化）
source_tier: auxiliary
source: "Morley, J. (2021). Academic Phrasebank (3rd ed.). University of Manchester. Ch.03 Describing Methods."
top_journal_validated: false
status: EMERGING
risk_level: needs-context
created: 2026-07-27
---

# Phrasebank: Methods 过程描述（Morley 03 章收割）

> **层级定位**：auxiliary 语言实现层。顶刊蒸馏模板与 `write-methods/corpus/micro-templates/` 决定**说什么**；本文件只在其措辞反复使用时提供**怎么换个说法**。
>
> **使用规则**（每次调用必读）：
> 1. **调用顺序**：顶刊模板/微模板 → 本文件变化库 → claim-strength QC。骨架空白处优先用顶刊模板，本文件不填补结构缺口。
> 2. 每个位置最多取 **2–3 个候选**；同一段落不连续堆叠两个以上本文件句式。
> 3. **必须替换 X/Y 并具体化**（构念、数据源、程序细节）。
> 4. **Specificity gate**：替换后的句子若仍可不加修改放进任何论文 → 不合格，加入具体 actor / construct / context。
> 5. claim strength 列是语气上限；archival 描述用陈述语气即可，涉及因果的程序说明遵守 write-methods `causal-hedging.md`。
>
> **退役规则**：某功能一旦被顶刊蒸馏语料覆盖（经 distill-methods-exemplar 验证），对应条目从本文件删除。本文件不计入 MVP30 paper_count。

## 1. 过程叙述·被动动词（archival / survey 适配）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "Data were collected using [source/instrument]." | M2 样本 | descriptive | 低；最通用 |
| "Data were gathered from multiple sources at various time points during [period]." | M2 样本 | descriptive | 多源数据专用 |
| "Descriptive data were generated for all variables." | M3–M5 变量 | descriptive | 低 |
| "Data management and analysis were performed using [software/version]." | M7 模型 | descriptive | 低 |
| "Published studies were identified using a search strategy developed in [prior work]." | M2 样本 | descriptive | 仅文献样本（meta/综述式样本构建） |
| "Article references were searched further for additional relevant publications." | M2 样本 | descriptive | 同上 |
| "The participants were asked to [rate / indicate / describe / recall] ..." | M3–M5 测量 | descriptive | 仅 survey/实验设计 |
| "Injection solutions were coded by a colleague to reduce experimenter bias."→ 适配："The [materials] were coded by [independent coders] to reduce [coder] bias." | M3–M5 测量 | descriptive | 人工编码设计专用；与 `manual-coding-validation.md` 互补 |

## 2. Sequence words（程序步骤排序）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "Prior to [data collection / analysis], [step]." | M2/M7 | descriptive | 低 |
| "(Immediately) After [step], the [samples/data] were [next step]." | M2/M7 | descriptive | 低 |
| "On [arrival at / completion of / obtaining X], [step] was carried out." | M2/M7 | descriptive | 低 |
| "Once the [Xs] were [located/extracted/matched], it was first necessary to ..." | M2 样本 | descriptive | 样本构建链 |
| "Following [correction for / confirmation of] X, [step]." | M7 | descriptive | 低 |
| "The [data] were then [processed], and this [value] was recorded as ..." | M3–M5 | descriptive | 低 |
| "When [dividing/constructing] X, care was taken to ..." | M3–M5 | descriptive | 低 |
| "Finally, [questions were asked as to / tests were conducted on] ..." | M7 | descriptive | 低 |

## 3. using + instrument（工具/方法引入）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "Comparisons between the two groups were made using [test]." | M7 | descriptive | 匹配/分组设计 |
| "The relationship between X and Y was examined using [estimator]." | M7 | associational | 禁 causal 读法 |
| "[Subjects/Firms] were recruited using [channel/criteria]."→ archival 适配："Firms were selected using [criteria]." | M2 样本 | descriptive | 低 |
| "The data were recorded ... and transcribed using [tool]."→ archival 适配："The texts were processed using [tool/library]." | M3–M5 | descriptive | 文本研究 |

## 4. Infinitive of purpose（目的引出程序）

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "In order to [investigate/identify] the effects of X, [step]." | M7/M8 | descriptive | 禁用作识别论证本身 |
| "In order to address these [concerns], the following steps were taken: ..." | M8 识别 | descriptive | 程序陈述，非论证 |
| "To avoid [problem], [step]." | M3–M5/M7 | descriptive | 低 |
| "To test whether ..., [step]." | M7 | descriptive | 低 |
| "To establish whether ..., [step]." | M7 | descriptive | 低 |
| "To address the possibility of [alternative], [step]." | M8 识别 | descriptive | 程序陈述；论证句法归 `because-clauses.md` |
| "For the purpose of [analysis/measurement], [step]." | M3–M5/M7 | descriptive | 低 |

## 5. 统计程序动词变化（防同质化）

同一程序动词的备选（run / used / conducted / performed / carried out）：

| 句式骨架 | allowed slots | claim strength | 风险/注意 |
|---------|--------------|---------------|----------|
| "A [test] was [conducted/performed/carried out] to assess whether ..." | M7 | descriptive | 估计器名须具体 |
| "A [test] was [run/used] to test the hypothesis that ..." | M7 | descriptive | 低 |
| "A [test] was conducted to compare the [means/distributions] of ..." | M7 | descriptive | 低 |
| "A [test] was performed to determine whether there was a difference between ..." | M7 | descriptive | 低 |
| "Reliability was calculated using Cronbach's alpha." | M3–M5 测量 | descriptive | 仅 survey 量表 |
| "All analyses were carried out using [Stata/SPSS/R], version [x]." | M7 | descriptive | 低 |
| "A p value < 0.05 was considered significant." | M7 | descriptive | 低 |

## 禁区

- 本文件**不提供**：方法选择理由（归 `model-selection-comparison.md`）、方法拒绝理由（同）、识别策略论证（归 `identification-exogeneity.md` / `identification-foreshadowing.md`）、因果措辞梯度（归 `causal-hedging.md`）——这些已有顶刊源微模板，禁止用本文件的通用句式替代。
- "In order to investigate the effects of X" 类目的句**不等于识别论证**；M8 的因果主张仍需设计门控的措辞。
