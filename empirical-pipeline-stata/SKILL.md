---
name: empirical-pipeline-stata
description: Use when the user wants to RUN a complete empirical analysis in Stata from clean data all the way to paper-ready tables/figures — the end-to-end execution pipeline (sample & spec → descriptives & event study → baseline & modern staggered DiD → robustness battery → mechanism/heterogeneity/mediation → publication tables). Especially use when the work needs modern staggered-DiD estimators IN STATA (csdid / eventstudyinteract / did_imputation / sdid / did_multiplegt_dyn), the rigorous robustness battery (Oster δ* / Romano-Wolf rwolf / wild cluster bootstrap boottest / randomization inference ritest / specification curve / bacondecomp / honestdid), mechanism & mediation tests (medsem / khb / outcome ladder), or survival/duration models for recall-timing (stcox / streg AFT Weibull). Trigger on "实证流水线", "把数据跑成论文表格", "从清洗到表格", "跑完整实证", "empirical pipeline", "main results table", "稳健性检验箱", "csdid / 现代 DiD / 交错 DiD Stata", "Oster / Romano-Wolf / wild bootstrap / ritest", "机制检验 / 中介 / 异质性 Stata", "recall timing / 生存 / AFT / 持续期". Do NOT use for pure Stata syntax lookup (use stata), for choosing/routing the identification design (use causal-analysis), or for writing the paper prose (use write-* / write-results). This skill EXECUTES the Stata pipeline and produces tables/figures; it does not decide the design or write the narrative.
---

# Empirical Pipeline — Stata(实证执行流水线)

## 目标
把一份已经基本清洗好的面板数据,**在 Stata 里**一路跑成投稿级的表与图:样本与规格 → 描述与事件研究 → 基准与现代交错 DiD → 稳健性检验箱 → 机制/异质性/中介 → 发表级表图。它是**执行流水线**,不是语法手册、不是设计路由、不是写作工具。

## 与你已有栈的分工(关键)
| 你已有的 skill | 职责 | 本 skill 的关系 |
|---|---|---|
| `causal-analysis` | **路由/设计**:选 DiD/IV/RDD/匹配,规划识别 | 先由它定设计,再用本 skill **执行** |
| `did-analysis` | 现代交错 DiD,但**在 R 里** | 本 skill 给**Stata 版**的现代 DiD(csdid 等),互补 |
| `stata` / `stata-regression` / `stata-data-cleaning` | **语法查阅**与单步执行 | 本 skill 是**编排**:把各步按论文顺序串起来 |
| `xianzhu-skill` | 规格搜索纪律(口径/变换) | 本 skill 跑的是**正式主表+稳健性箱**,不是探索性搜索 |
| `latex-tables` / `write-results` | 表格排版 / 结果写作 | 本 skill 产出 esttab/coefplot 原始表图,交给它们排版与写作 |

**铁律**:设计上的取舍(要不要 IV、平行趋势成不成立、选哪个识别策略)归 `causal-analysis`;本 skill 假设设计已定,负责把它在 Stata 里跑出来并配上完整稳健性。

## AMJ/SMJ 输出口径(与应用微观经济学的差异)
本流水线的方法与命令改编自 AER/QJE 风格的实证 pipeline,但**输出按战略管理学期刊口径调整**:

- **按假设组织表格**:主表不只是 M1→M6 渐进,更要让每一列/每一个系数**对应一个假设(H1, H1a, H1b)**,并在表注说明"该列检验 H_x"。
- **经济意义优先**:报告系数时同时给标准化或单位经济含义(1 SD / 一倍标准差 / 百分比),不要只甩 p 值。呼应你的 [[feedback-process-over-significance]]。
- **稳健性进附录/online supplement**:主表干净,完整的稳健性箱(Oster/Romano-Wolf/wild bootstrap/ritest/spec curve)放附录或线上补充材料,但**必须跑**。
- **调节假设靠 marginsplot**:AMJ/SMJ 的调节(H2)几乎标配交互项 + marginsplot,不是只报交互系数。
- **自选择/Heckman**:战略样本常有自选择,审稿人常要求 Heckman 或 PSO 稳健性。

## 流水线 8 步(总览)
每步只给最常用一种写法;深度变体见对应 reference。

- **Step −1 / 0 · 预注册与样本契约** — PAP(AEA RCT 风格)+ 样本构建日志 + 5 项数据契约。见 `references/01-pipeline-discipline.md`。
- **Step 1 · 数据导入与清洗** — `use/import`、`destring`、`misstable`、`duplicates`、`merge ... assert`、`xtset`。深度语法见 `stata-data-cleaning`;本 skill 只强调流水线里的契约。
- **Step 2 · 变量构造** — `winsor2`、`xtile`、`L./F./D./S.`、CPI 平减、交错 DiD 时间变量(first_treat / rel_p)。
- **Step 2.5 · 写方程与识别假设** — 在跑回归**前**显式写出估计方程 + 识别假设(平行趋势/外生性/无混淆),AMJ/SMJ Methods 必备。见 `references/01-pipeline-discipline.md`。
- **Step 3 / 3.5 · 描述统计与事件研究图** — Table 1(`tabstat`/`asdoc`/`balancetable`)+ 事件研究/平行趋势图(动机用)。见 `references/02-baseline-and-modern-did.md` 的事件研究段。
- **Step 4 · 诊断检验** — 12 类:`sktest/swilk`、`hettest/imtest`、`xtserial`、`vif`、`dfuller/kpss`、`hausman`、`estat overid`。深度见 `stata`。
- **Step 5 · 基准建模与现代交错 DiD** — `reghdfe`/`xtreg`/`ivreg2`/`heckman`/`ppmlhdfe` + **现代交错 DiD**(`csdid`/`eventstudyinteract`/`did_imputation`/`sdid`/`did_multiplegt_dyn`)。见 `references/02-baseline-and-modern-did.md`。
- **Step 6 · 稳健性箱** — 14 件套:渐进规格、聚类敏感性、`boottest`(wild)、`ritest`(RI)、`rwolf`(Romano-Wolf)、specification curve、Oster δ\*(`psacalc`)、`bacondecomp`、`honestdid`、留一法。见 `references/03-robustness-battery.md`。
- **Step 7 · 机制 / 异质性 / 中介** — 交互项 + `margins`/`marginsplot`、DDD、`suest`、outcome ladder、`medsem`/`khb`/SEM 中介。见 `references/04-mechanism-heterogeneity.md`。
- **Step 8 · 发表级表图** — `esttab`/`outreg2`/`asdoc` 出 `.tex/.rtf/.docx`、`coefplot`/`marginsplot`/`binscatter` 出 `.pdf`,按假设组织、附录放稳健性。
- **召回时机研究(生存/持续期)** — 若因变量是"到召回发生的时间",走 AFT/Cox。见 `references/05-survival-recall-timing.md`。

## 何时不要用
- 只想查某条 Stata 命令的语法 → 用 `stata`。
- 还没定识别策略、在 DiD/IV/RDD 之间选 → 用 `causal-analysis`。
- 在做探索性规格搜索(试到显著)→ 用 `xianzhu-skill`。
- 要写 Results/Discussion 文字 → 用 `write-results` / `write-discussion`。

## 需要按需读取的参考文件
- Step −1/0/2.5 预注册、样本契约、写方程与识别假设:`references/01-pipeline-discipline.md`
- Step 5 基准 + 现代交错 DiD(csdid/SA/did_imputation/sdid/did_multiplegt_dyn)+ 事件研究:`references/02-baseline-and-modern-did.md`
- Step 6 稳健性箱 14 件套:`references/03-robustness-battery.md`
- Step 7 机制/异质性/中介:`references/04-mechanism-heterogeneity.md`
- 召回时机的生存/持续期模型:`references/05-survival-recall-timing.md`

## 执行纪律(与 xianzhu-skill 一致)
- 每轮搜索/每张表独立成 do 文件与 log,不污染主回归链(见你已有的 Stata 输出约定)。
- 跑完要能回答三问:试了什么、为什么停、正文为什么选这一列。
- **过程优先于显著性**:稳健性箱是为了证明结论稳,不是为了筛出显著的列。
