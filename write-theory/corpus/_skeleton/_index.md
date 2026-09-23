# write-theory 骨架索引（Batch 2 全量）

> 本目录由脚本重建；重建命令 = `python scripts/build_indices.py`（`--check` 干跑、`--verify` 回源校验）。
> **统一 schema**：`id | func | citekey | status | kind | text | anchor`（7 字段，三来源字段名完全一致）。
> **verbatim** 逐字回源；**锚点** 指向真实标题/变体号/pattern_id；**citekey** 不编造（无机器可读 token 标「未标注」）。

## 一级路由：变体族 A–G

| 族 | 来源文件 | 子清单 | verbatim | 模板 |
|---|---|---|---|---|
| A（构念辨析型） | `corpus/variants/A_construct_differentiation.md` | [`variants-A_construct_differentiation.md`](variants-A_construct_differentiation.md) | 17 | 14 |
| B（机制推演型） | `corpus/variants/B_mechanism_elaboration.md` | [`variants-B_mechanism_elaboration.md`](variants-B_mechanism_elaboration.md) | 23 | 15 |
| C（假设树型） | `corpus/variants/C_hypothesis_tree.md` | [`variants-C_hypothesis_tree.md`](variants-C_hypothesis_tree.md) | 20 | 13 |
| D（质性/过程理论型） | `corpus/variants/D_process_theory.md` | [`variants-D_process_theory.md`](variants-D_process_theory.md) | 9 | 7 |
| E（调节效应型） | `corpus/variants/E_moderation.md` | [`variants-E_moderation.md`](variants-E_moderation.md) | 43 | 39 |
| F（竞争假设型） | `corpus/variants/F_competing_hypotheses.md` | [`variants-F_competing_hypotheses.md`](variants-F_competing_hypotheses.md) | 11 | 9 |
| G（辩证对立型） | `corpus/variants/G_dialectical_opposition.md` | [`variants-G_dialectical_opposition.md`](variants-G_dialectical_opposition.md) | 41 | 27 |

## 来源子清单：subprotocols pattern 库

| 库 | 来源文件 | 子清单 | verbatim | 模板 |
|---|---|---|---|---|
| hypothesis_derivation_patterns | `corpus/subprotocols/hypothesis_derivation_patterns.md` | [`subprotocols-hypothesis_derivation_patterns.md`](subprotocols-hypothesis_derivation_patterns.md) | 17 | 45 |
| argumentation_patterns | `corpus/subprotocols/argumentation_patterns.md` | [`subprotocols-argumentation_patterns.md`](subprotocols-argumentation_patterns.md) | 32 | 35 |
| hypothesis_organization_patterns | `corpus/subprotocols/hypothesis_organization_patterns.md` | [`subprotocols-hypothesis_organization_patterns.md`](subprotocols-hypothesis_organization_patterns.md) | 15 | 32 |
| evidence_patterns | `corpus/subprotocols/evidence_patterns.md` | [`subprotocols-evidence_patterns.md`](subprotocols-evidence_patterns.md) | 10 | 15 |
| construct_differentiation_patterns | `corpus/subprotocols/construct_differentiation_patterns.md` | [`subprotocols-construct_differentiation_patterns.md`](subprotocols-construct_differentiation_patterns.md) | 11 | 11 |
| moderator_selection_frameworks | `corpus/subprotocols/moderator_selection_frameworks.md` | [`subprotocols-moderator_selection_frameworks.md`](subprotocols-moderator_selection_frameworks.md) | 8 | 13 |
| bilateral_argumentation_templates | `corpus/subprotocols/bilateral_argumentation_templates.md` | [`subprotocols-bilateral_argumentation_templates.md`](subprotocols-bilateral_argumentation_templates.md) | 3 | 17 |

## 来源子清单：sentences 句式库

| 文件 | 子清单 | verbatim | 模板 |
|---|---|---|---|
| acknowledgment_response | [`sentences-acknowledgment_response.md`](sentences-acknowledgment_response.md) | 14 | 21 |
| closure | [`sentences-closure.md`](sentences-closure.md) | 6 | 26 |
| construct_definition | [`sentences-construct_definition.md`](sentences-construct_definition.md) | 35 | 26 |
| cost_benefit_calculus | [`sentences-cost_benefit_calculus.md`](sentences-cost_benefit_calculus.md) | 1 | 14 |
| hypothesis_forms | [`sentences-hypothesis_forms.md`](sentences-hypothesis_forms.md) | 44 | 106 |
| leitmotif-section-opener | [`sentences-leitmotif-section-opener.md`](sentences-leitmotif-section-opener.md) | 12 | 8 |
| mechanism_chain | [`sentences-mechanism_chain.md`](sentences-mechanism_chain.md) | 96 | 76 |
| moderation | [`sentences-moderation.md`](sentences-moderation.md) | 36 | 42 |

合计：22 个子清单 / verbatim 504 条 / 模板 611 条。

## 待补录

- [`_unparsed.md`](_unparsed.md)：0 条（每条附「为什么进不了主清单」）。
