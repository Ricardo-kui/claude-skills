# 稳健性规划清单(设计层:威胁 → 检验)

本文件是 **causal-analysis 在设计/路由阶段规划稳健性**用的清单——按"要解决哪个识别威胁"组织,告诉你**该规划哪些检验、为什么**。具体的 Stata 命令实现在 `empirical-pipeline-stata/references/03-robustness-battery.md`,那里是执行层;这里是规划层。两者互补,不要重复。

> 纪律:稳健性是"换了之后方向量级还稳不稳"的检验,不是"挑最显著列"的搜索。后者见 `xianzhu-skill` 的 `references/robustness-levers.md`。

## 核心:识别威胁 → 检验对照表

| 识别威胁 | 该规划的检验 | 备注 |
|---|---|---|
| 规格任意性(控制变量/FE 选择) | **渐进规格 M1→M6** + **specification curve**(跑遍合理组合画系数分布) | 核心系数在增减控制/FE 下符号量级稳定 |
| 少聚类 / CRSE 低估 | **wild cluster bootstrap**(`boottest`)+ **随机化推断**(`ritest`)+ 聚类层级敏感性 | 聚类数 < 50 时必做 wild bootstrap |
| 不可观测选择(OVB) | **Oster δ\***(`psacalc`)| δ\*>1 基本、>2 强;报告偏误调整 β 界 |
| 多重检验(多结果变量) | **Romano-Wolf**(`rwolf`)/ Westfall-Young(`wyoung`)| 族错误率膨胀,必须校正 |
| 平行趋势违反(DiD) | **事件研究** + **HonestDiD**(Rambachan-Roth 敏感性)+ **安慰剂伪时点** | 前期系数≈0;HonestDiD 给"多大违反才翻结论" |
| 交错处理下 TWFE 偏误 | **bacondecomp**(权重诊断)+ 换现代估计器(csdid/SA/did_imputation) | 负权重大就必须换估计器,见 `did-analysis` |
| 弱工具(IV) | 第一阶段 **Kleibergen-Paap rk Wald F≥10** + Anderson-Rubin CI + 弱工具稳健推断 | F<10 → 系数/SE 不可信 |
| 过度识别(IV 多工具) | **Hansen J** / Sargan | 拒绝 → 工具非外生 |
| 带宽/操纵(RDD) | 带宽敏感性(×0.5/1/2)+ **rddensity**(操纵检验)+ 协变量平滑平衡 | 断点两侧协变量应平衡 |
| 匹配失衡(PSM/IPW) | **pstest/tebalance** 平衡 + 共同支撑 + 熵平衡(ebalance)版本 | 匹配后 SMD 应 <0.1 |
| 影响观测 | **留一法**(leave-one-out)+ 去 top Cook's D 重估 | 防个别公司/单位驱动结果 |
| 测量/口径敏感性 | 替代 y/x 定义(≥2–3)+ winsor/trim 敏感度 | 见 `xianzhu-skill` 的变换与口径纪律 |

## 按设计类型的最小稳健性附录

不同设计需要的子集不同;规划时按你的设计勾选:

| 设计 | 至少规划 |
|---|---|
| **DiD / event-study** | 渐进规格、聚类敏感性(+wild bootstrap 若少聚类)、事件研究前期、bacondecomp(若交错)、HonestDiD、安慰剂伪时点、ritest |
| **IV** | 弱工具 F、过度识别 Hansen J(若多工具)、替代工具、Oster δ\*、Anderson-Rubin CI |
| **RDD** | 带宽敏感性、rddensity、协变量平衡、断点处多项式阶数敏感性、donut(剔除断点附近) |
| **匹配 / IPW** | 平衡检验、共同支撑、熵平衡双轨、替代倾向分模型、Oster δ\* |
| **FE / 面板基准** | 渐进规格、聚类敏感性、替代 FE 结构、Oster δ\*、自相关/异方差诊断 |

## 规划时的三个判断
1. **先验列出威胁**:在跑回归前(见 `empirical-pipeline-stata` 的 Step 2.5"写方程+识别假设"),列出 2–3 个最可能的识别威胁,再**事先**对应到上面的检验——不要事后挑。
2. **主表 vs 附录**:主表干净(渐进规格 + 主识别),完整稳健性箱进附录/online supplement,但**必须跑**。
3. **诚实留痕**:任何一项让结论翻号,如实写进局限,而不是藏起来或换到不翻号的规格。

## 执行交接
规划定后,把"要跑的稳健性清单"交给执行层:
- **Stata 执行**:走 `empirical-pipeline-stata`(它的 `references/03-robustness-battery.md` 给每条检验的命令)。
- **R 现代DiD**:走 `did-analysis`(CS/SA/HonestDiD 在 R 侧)。
- **规格搜索纪律**(试到稳健/显著):走 `xianzhu-skill`。
