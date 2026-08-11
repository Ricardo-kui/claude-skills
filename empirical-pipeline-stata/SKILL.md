---
name: empirical-pipeline-stata
description: Execute a locked empirical design as a complete Stata pipeline from analysis-ready data to reproducible scripts, logs, diagnostics, tables, and figures. Use for broad Stata execution covering baselines, modern staggered DiD, robustness, mechanisms, heterogeneity, mediation, or survival models. Require a Design Packet and Analysis Manifest first. Do not use for design choice, isolated Stata syntax, or paper prose.
---

# Empirical Pipeline — Stata(实证执行流水线)

## 目标
把已锁定设计与分析就绪数据在 **Stata** 中执行成可复现的脚本、日志、诊断、表与图。只运行 Analysis Manifest 授权的基准、设计专属诊断、威胁对应检验及预先指定的扩展。它不是语法手册、设计路由或写作工具。

## 与你已有栈的分工(关键)
| 你已有的 skill | 职责 | 本 skill 的关系 |
|---|---|---|
| `huntington-klein-causal-design` | **识别设计**:estimand、反事实、假设、stop rules | 它锁定设计 |
| `causal-analysis` | **执行规划**:运行时、估计器、诊断与输出 | 它生成 Analysis Manifest,本 skill 执行 |
| `did-analysis` | 现代交错 DiD,但**在 R 里** | 本 skill 给**Stata 版**的现代 DiD(csdid 等),互补 |
| `stata` / `stata-data-cleaning` | **语法查阅**与单步执行 | 本 skill 是**编排**:把各步按论文顺序串起来 |
| `xianzhu-skill` | 规格搜索纪律(口径/变换) | 本 skill 跑的是**正式主表+稳健性箱**,不是探索性搜索 |
| `latex-tables` / `write-results` | 表格排版 / 结果写作 | 本 skill 产出 esttab/coefplot 原始表图,交给它们排版与写作 |

**铁律**:识别取舍归 `huntington-klein-causal-design`;`causal-analysis` 只把锁定设计转成执行计划。本 skill 不得自行更换设计、比较组、样本、聚类规则或 estimand。

## 入口与出口契约

执行前必须读取 `huntington-klein-causal-design` 的 Design Packet 与 `causal-analysis` 的 Analysis Manifest。若二者冲突,停止并退回设计阶段,不得由执行代码自行选择口径。

执行后返回 Run Manifest 与 Results Inventory,至少包括:

- 精确输入数据、do-file、log、Stata/包版本与退出状态
- 实际样本、估计式、固定效应、聚类规则及相对 Analysis Manifest 的偏离
- 每个诊断和 stop rule 的通过/失败状态
- 表图路径、未解决警告与不可授权的主张

把这些产物交给 `review-code` / `check-methodology` 核验;核验完成后才进入 `empirical-writeup`。

## AMJ/SMJ 输出口径(与应用微观经济学的差异)
本流水线的方法与命令改编自 AER/QJE 风格的实证 pipeline,但**输出按战略管理学期刊口径调整**:

- **按假设组织表格**:主表不只是 M1→M6 渐进,更要让每一列/每一个系数**对应一个假设(H1, H1a, H1b)**,并在表注说明"该列检验 H_x"。
- **经济意义优先**:报告系数时同时给标准化或单位经济含义(1 SD / 一倍标准差 / 百分比),不要只甩 p 值。呼应你的 [[feedback-process-over-significance]]。
- **稳健性对应威胁**:只运行 Design Packet / Analysis Manifest 为具体威胁授权的检验;不存在通用“全套必须跑”。
- **机制与异质性有门槛**:只有理论预先指定、设计允许且基准通过诊断时才执行;不得为了丰富故事自动加入。
- **方法不由期刊惯例替代设计**:Heckman、Oster、RI、不同聚类层级等均需满足各自前提,不能因为“审稿人常问”就自动运行。

## 流水线 8 步(总览)
每步只给最常用一种写法;深度变体见对应 reference。

- **Step −1 / 0 · 预注册与样本契约** — PAP(AEA RCT 风格)+ 样本构建日志 + 5 项数据契约。见 `references/01-pipeline-discipline.md`。
- **Step 1 · 数据导入与清洗** — `use/import`、`destring`、`misstable`、`duplicates`、`merge ... assert`、`xtset`。深度语法见 `stata-data-cleaning`;本 skill 只强调流水线里的契约。
- **Step 2 · 变量构造** — `winsor2`、`xtile`、`L./F./D./S.`、CPI 平减、交错 DiD 时间变量(first_treat / rel_p)。
- **Step 2.5 · 写方程与识别假设** — 在跑回归**前**显式写出估计方程 + 识别假设(平行趋势/外生性/无混淆),AMJ/SMJ Methods 必备。见 `references/01-pipeline-discipline.md`。
- **Step 3 / 3.5 · 描述统计与设计专属图** — Table 1 与 Analysis Manifest 指定的事件研究或诊断图。
- **Step 4 · 诊断检验** — 只跑与估计器、数据结构和识别威胁对应的诊断,不做无关的固定清单。
- **Step 5 · 基准建模与现代交错 DiD** — `reghdfe`/`xtreg`/`ivreg2`/`heckman`/`ppmlhdfe` + **现代交错 DiD**(`csdid`/`eventstudyinteract`/`did_imputation`/`sdid`/`did_multiplegt_dyn`)。见 `references/02-baseline-and-modern-did.md`。
- **Step 6 · 威胁对应检验** — 从 `references/03-robustness-battery.md` 选择已授权的最小充分集合。
- **Step 7 · 条件扩展** — 仅按预先指定理论与通过的门控执行机制、异质性或中介。见 `references/04-mechanism-heterogeneity.md`。
- **Step 8 · 发表级表图** — `esttab`/`outreg2`/`asdoc` 出 `.tex/.rtf/.docx`、`coefplot`/`marginsplot`/`binscatter` 出 `.pdf`,按假设组织、附录放稳健性。
- **生存/持续期** — 若因变量是到事件发生的时间,默认 Cox PH;当 PH 不成立或目标是时间比且分布假设有依据时,使用预先指定的 AFT 替代。见 `references/05-survival-recall-timing.md`。

## 何时不要用
- 只想查某条 Stata 命令的语法 → 用 `stata`。
- 还没定识别策略、在 DiD/IV/RDD 之间选 → 先用 `huntington-klein-causal-design`,设计锁定后再用 `causal-analysis` 生成执行计划。
- 在做探索性规格搜索(试到显著)→ 用 `xianzhu-skill`。
- 要写 Results/Discussion 文字 → 用 `empirical-writeup` 先建立 Evidence Packet,再交给 `write-methods-and-results` / `write-discussion-and-conclusion`。

## 需要按需读取的参考文件
- Step −1/0/2.5 预注册、样本契约、写方程与识别假设:`references/01-pipeline-discipline.md`
- Step 5 基准 + 现代交错 DiD(csdid/SA/did_imputation/sdid/did_multiplegt_dyn)+ 事件研究:`references/02-baseline-and-modern-did.md`
- Step 6 威胁 → 检验映射:`references/03-robustness-battery.md`
- Step 7 条件机制/异质性/中介:`references/04-mechanism-heterogeneity.md`
- 召回时机的生存/持续期模型:`references/05-survival-recall-timing.md`

## 执行纪律(与 xianzhu-skill 一致)
- 每轮搜索/每张表独立成 do 文件与 log,不污染主回归链(见你已有的 Stata 输出约定)。
- 跑完要能回答三问:试了什么、为什么停、正文为什么选这一列。
- **过程优先于显著性**:稳健性箱是为了证明结论稳,不是为了筛出显著的列。
