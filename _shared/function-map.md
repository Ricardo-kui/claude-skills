# 功能→语料载体地图（write-* 家族）

> **用途**：写作中"要写/借一个 X 功能的句子或词"时的单问单答路由——按节直达该节功能表、骨架索引与词汇载体；跨节借句（写 theory 时借 hook 句、写 results 时查因果动词档位）从本图进入。
> **纪律**：各节功能系统**异构即正典**（体裁决定功能，不归一）；本图只列轴名、代表功能与唯一源指针，**不复述**各节索引内容（SSOT：功能描述归各节自有一级索引）。关键词查询工具（`distill-paper-exemplar/scripts/corpus_query.py`）属蒸馏维护期，写作期不走。
> **机器看守**：`_shared/indexing/check_all.py` 的 function-map 节逐指针断言（目标可解析；索引/骨架目标条目非空）。本图由此自成 fixtures——图上每条指针即一条"功能→非空范本"断言。

## write-introduction — 功能模块轴（叙事功能）

- 轴与代表功能：Hook / Tension / Stakes / Literature Turn / Theory Lens / Preview / RQ / Contribution / Transitions / Differentiation
- 功能→语料→骨架三列表（唯一源）：`write-introduction/SKILL.md` Phase 3 表
- 骨架借句 id（G1 底本）：`write-introduction/corpus/_skeleton/_index.md`（13 子索引路由）
- 句子级：key line 三分法 `write-introduction/corpus/micro-templates/key-line-patterns.md`；中心论点 `write-introduction/corpus/micro-templates/thesis-models.md`；过渡信号 `write-introduction/corpus/micro-templates/transition-signals.md`
- 词汇/档位：hedging 强度 `write-introduction/corpus/phrasebank/hedging-strength.md`；批判措辞 `write-introduction/corpus/phrasebank/critique-phrases.md`；数值趋势 `write-introduction/corpus/phrasebank/quantities-trends.md`；过程描述 `write-introduction/corpus/phrasebank/methods-process.md`

## write-theory — 变体族轴（段落功能）+ 句库轴（句子功能）

- 段落级 A–G：构念辨析 / 机制推演 / 假设树 / 过程理论 / 调节 / 竞争假设 / 辩证对立
- 句子级 8 库：mechanism_chain / hypothesis_forms / moderation / construct_definition / cost_benefit_calculus / leitmotif-section-opener / acknowledgment_response / closure
- 功能表（唯一源）：`write-theory/corpus/_index.md` 快速决策表（贡献类型→族/句库）；选择判据 `write-theory/corpus/meta/routing_table.md`
- 骨架借句 id：`write-theory/corpus/_skeleton/_index.md`（22 子清单路由）
- 词汇/档位：hedging 借 `write-introduction/corpus/phrasebank/hedging-strength.md`；批评档位 `distill-paper-exemplar/references/band-vocab.md`

## write-methods — 槽位轴（段落功能）+ 微模板轴（句子功能）

- 段落级 M1–M10：研究情境 / 样本漏斗 / Model-Free / DV / IV / 调节中介 / 控制变量 / 模型规格 / 识别策略 / 多研究 / 过渡
- 句子级 18 类全表（唯一源）：`write-methods/corpus/micro-templates/INDEX.md`（段首锚定 / because 从句 / 因果动词梯度 / 过渡衔接 / 样本漏斗节奏 / 识别预告 / 变量操作化 / 稳健预告 / 模型比较 …）
- 槽位表（唯一源）：`write-methods/SKILL.md` M1–M10 表；设计类型→槽位顺序 `write-methods/references/design-branches.md`
- 骨架借句 id：`write-methods/corpus/_skeleton/_index.md`（24 设计类型路由）
- 词汇/档位：因果动词梯度（家族唯一源）`write-methods/corpus/micro-templates/causal-hedging.md`

## write-results — 模型族轴 + 证据功能槽位轴

- 段落级 R1–R9：描述统计 / 表格导航 / 主假设四拍 / 交互 / 经济显著性 / 非显著混合 / 稳健性 / 补充机制 / 收束
- 句法级：句法微模板借 `write-methods/corpus/micro-templates/`（causal-hedging / interquartile-economic-significance / subsample-grouping / transitions，只借逻辑连接不移植语态）
- 槽位表（唯一源）：`write-results/SKILL.md` R1–R9 表；模型族→corpus 文件 `write-results/corpus/INDEX.md`
- 骨架借句 id：`write-results/corpus/_skeleton/_index.md`（21 模型族路由）
- 词汇/档位：claim 层级与过度声明动词表 `write-results/references/claim-calibration.md`；数值/hedging 借 intro phrasebank

## 跨节词汇/档位速查（唯一源指针）

- 因果动词档位（按设计家族）→ `write-methods/corpus/micro-templates/causal-hedging.md`
- hedging 强度 → `write-introduction/corpus/phrasebank/hedging-strength.md`
- claim 层级（L1–L7 + 过度声明动词表）→ `write-results/references/claim-calibration.md`
- 批评/审稿回应档位 → `distill-paper-exemplar/references/band-vocab.md`
