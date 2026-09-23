# write-methods 骨架索引路由（两级）

> **本目录由脚本重建，手改会被覆盖；重建命令 = `python scripts/build_indices.py`（路径基准：以本 skill 目录（SKILL.md 所在目录）为基准；`--check` 干跑、`--verify` 回源校验）。**
> **两层结构**：本路由 + 每设计类型一份二级清单（或槽位拆分子清单）。先读「何时读它」定位设计类型，再整份读入对应二级清单。
> **一级轴 = 设计类型**；**二级槽位维度 = M1–M10（含 M2.5）与 Q1–Q8（定性）**（见各二级清单「适配槽位」列）。
> 状态列：`verbatim` = 逐字原句（无槽位、与源卡片逐字一致）；`模板` = 含 `[槽位]` 的填槽骨架。抽取规则全文见各二级清单头部。

| 设计类型 | 对应 corpus 文件 | 变体数 | 何时读它 |
|---|---|---|---|
| [`panel-ols`](panel-ols.md) | `corpus/面板数据-OLS.md` | 95 | 主模型是 OLS/FE/动态面板/SUR，需写设置合法性、样本漏斗、操作化与规格叙事 |
| [`did`](did.md) | `corpus/自然实验-DiD.md` | 26 | 因果设计是 DiD/准实验，需识别策略论证、预处理卫生或外生性辩护 |
| [`nonlinear`](nonlinear.md) | `corpus/非线性模型.md` | 22 | DV 是计数/二元/有序/受限，需分布诊断、估计器选择或交互项规格 |
| [`survival`](survival.md) | `corpus/生存分析.md` | 22 | DV 是时长/生存时间，需 hazard 操作化、分布选择或复发事件处理 |
| [`sem`](sem.md) | `corpus/SEM.md` | 4 | SEM/调节中介方法段（联合估计、交互共线性、时序方向诊断） |
| [`experiments`](experiments.md) | `corpus/实验.md` | 6 | 数据来自实验，需写被试→材料→操纵→测量标准段 |
| [`multi-study`](multi-study.md) | `corpus/多研究.md` | 10 | 一篇论文含多个 study，需跨研究设计总览或递进论证 |
| [`qualitative-process`](qualitative-process.md) | `corpus/定性过程研究.md` | 7 | 定性 Findings（过程模型/引语），非量化假设检验 |
| [`rare-outcome`](rare-outcome.md) | `corpus/稀有结果.md` | 3 | DV 低基线率（欺诈/破产/极端事故），FE 丢样本或 margin 分解 |
| [`construct-object`](construct-object.md) | `corpus/实证对象构建.md` | 17 | 分析单位需升级/构造（交易级、事件级、竞争组），需单位宣告与核验 |
| [`event-history-study`](event-history-study.md) | `corpus/事件历史+事件研究.md` | 30 | 事件研究/事件历史，需窗口选择、污染规避或 CAR 测量公式 |
| [`simultaneous-equations`](simultaneous-equations.md) | `corpus/同时方程.md` | 5 | 两个内生变量互为因果（status/reputation 型），需系统估计叙事 |
| [`iv-2sls`](iv-2sls.md) | `corpus/IV-2SLS.md` | 14 | 需内生性修正（2SLS/IV），报第一阶段 F、排除限制或弱识别诊断 |
| [`dynamic-panel-gmm`](dynamic-panel-gmm.md) | `corpus/动态面板-GMM.md` | 7 | 动态面板（滞后 DV），需 AB-GMM/Blundell-Bond 诊断链 |
| [`matched-did`](matched-did.md) | `corpus/匹配DiD-广义DiD.md` | 2 | DiD 前用匹配构造可比处理/对照 |
| [`peer-network`](peer-network.md) | `corpus/同伴效应-网络效应.md` | 15 | 同伴/网络效应结果，需网络构念操作化或 dyadic 依赖处理 |
| [`text-construct`](text-construct.md) | `corpus/文本构念测量.md` | 21 | 从文本（财报/访谈/媒体）测构念，需词典效度或编码信度 |
| [`psm-panel`](psm-panel.md) | `corpus/PSM匹配面板.md` | 4 | 用倾向得分/熵平衡匹配构造对照或稳健性 |
| [`stacked-diffusion-logit`](stacked-diffusion-logit.md) | `corpus/堆叠扩散Logit.md` | 0 | 扩散/采纳 Logit 结构模型（当前无验证变体） |
| [`multi-actor`](multi-actor.md) | `corpus/多行为者设计.md` | 3 | 多行为者/多层级设计，需聚合辩护或 dyad 拆分 |
| [`binary-outcome-inference`](binary-outcome-inference.md) | `corpus/推断二元结果.md` | 1 | 二元结果的因果推断（当前少量变体） |
| [`two-stage`](two-stage.md) | `corpus/两阶段模型.md` | 15 | 样本选择/可观测性选择，需 Heckman 或控制函数叙事 |
| [`varx-pvar`](varx-pvar.md) | `corpus/VARX-PVAR.md` | 8 | 向量自回归/脉冲响应，需滞后阶/GIRF/FEVD 规格 |
| [`state-space`](state-space.md) | `corpus/结构需求-state-space.md` | 6 | 结构需求或状态空间模型，需拟合/反事实方法规格 |

合计：24 设计类型 / 343 编号变体 / verbatim 348 条 / 模板 344 条。
另有 5 条不编号变体（`### 变体：`，fang2025 POM）与 5 条 EXTEND 子变体（`#### 变体：`）——已抽取进各二级清单但**不计入**上面的 342（口径与 validator/INDEX/速查表一致）。

## 待补录

- [`_unparsed.md`](_unparsed.md)：0 条未自动命中或结构不规整，**待人工判定**。
