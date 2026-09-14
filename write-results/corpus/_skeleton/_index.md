# write-results 骨架索引路由（两级）

> **本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（在 `write-results/` 目录下；`--check` 干跑、`--verify` 回源校验）。**
> **两层结构**：本路由 + 每模型族一份二级清单（或槽位拆分子清单）。先读「何时读它」定位模型族，再整份读入对应二级清单。
> **一级轴 = 模型族**；**二级槽位维度 = R1–R9**（见各二级清单「适配槽位」列）。
> 状态列：`verbatim` = 逐字原句（无槽位、与源卡片逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架。抽取规则全文见各二级清单头部。

| 模型族 | 对应 corpus 文件 | 变体数 | 何时读它 |
|---|---|---|---|
| [`ols-fe`](ols-fe.md) | `OLS-FE.md` | 99 | 主模型是 OLS/FE/动态面板/SUR 时写 R1–R9 结果段，或需要表导航/幅度翻译/稳健性叙述 |
| [`logit-probit-ordered-probit`](logit-probit-ordered-probit.md) | `Logit-Probit-Ordered-Probit.md` | 59 | DV 是二元/有序/类别变量，需要 OR/概率尺度翻译或分样本二元模型裁决 |
| [`survival-analysis`](survival-analysis.md) | `生存分析.md` | 19 | DV 是时长/生存时间，需 hazard/exp(β) 或「四拍+百分比」风险结果 |
| [`did`](did.md) | `DiD.md` | 25 | 因果设计是 DiD/准实验，需交互项幅度翻译、pre-trend 或 placebo 稳健性 |
| [`count-models`](count-models.md) | `计数模型.md` | 35 | DV 是计数（召回次数/专利数），需发生率比翻译或计数诊断 |
| [`experiments`](experiments.md) | `实验.md` | 5 | 数据来自实验/多研究，需 F/p/η² 或 PROCESS 中介报告 |
| [`multi-study`](multi-study.md) | `多研究.md` | 8 | 一篇论文含多个 study，需跨研究综合或差异解释 |
| [`qualitative-process`](qualitative-process.md) | `定性过程研究.md` | 6 | 定性 Findings（过程模型/引语），非量化假设检验 |
| [`iv-2sls`](iv-2sls.md) | `IV-2SLS.md` | 17 | 需内生性修正（2SLS/IV），报第一阶段 F、排他性或弱识别诊断 |
| [`matched-did`](matched-did.md) | `匹配DiD.md` | 1 | DiD 前用匹配（CEM/PSM）构造可比处理/对照 |
| [`tobit`](tobit.md) | `Tobit.md` | 1 | DV 在 0 处删失/受限（如召回延迟下限），需 Tobit 报告 |
| [`stacked-diffusion-logit`](stacked-diffusion-logit.md) | `堆叠扩散Logit.md` | 0 | 扩散/采纳 Logit 结构模型（当前无验证变体） |
| [`peer-network-effects`](peer-network-effects.md) | `同伴效应-网络效应.md` | 0 | 同伴效应或网络效应结果（当前无验证变体） |
| [`binary-outcome-inference`](binary-outcome-inference.md) | `推断二元结果.md` | 0 | 二元结果的因果推断（当前无验证变体） |
| [`cross-audience-construct`](cross-audience-construct.md) | `跨受众构念对比.md` | 1 | 同一 IV 在两受众/两 DV 上符号相反，需镜像对比报告 |
| [`three-way-interaction`](three-way-interaction.md) | `三向交互.md` | 4 | 模型含三向交互，需条件两向分解或简单斜率差异 |
| [`construct-exposure-decomposition`](construct-exposure-decomposition.md) | `构造暴露分解.md` | 0 | 构造暴露分解结果（当前无验证变体） |
| [`sem-moderated-mediation`](sem-moderated-mediation.md) | `SEM-moderated-mediation.md` | 8 | SEM/调节中介报告（路径系数、条件间接效应、fit 指标） |
| [`event-study`](event-study.md) | `事件研究法.md` | 17 | 事件研究 CAR/AR，需分组裁决、t 检验或主效应保护段 |
| [`varx-pvar`](varx-pvar.md) | `VARX-PVAR.md` | 7 | 向量自回归/脉冲响应，需弹性表或方差分解解读 |
| [`blp-state-space`](blp-state-space.md) | `BLP-状态空间.md` | 5 | 结构需求或状态空间模型，需拟合/反事实报告 |

合计：21 模型族 / verbatim 292 条 / 模板 312 条。

## 待补录

- [`_unparsed.md`](_unparsed.md)：4 条未自动命中或结构不规整，**待人工判定**。
