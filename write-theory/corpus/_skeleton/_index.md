# write-theory 骨架索引解析试点（Batch 2，三套块结构）

> 本目录由脚本重建；重建命令 = `python scripts/build_indices.py`（`--check` 干跑、`--verify` 回源校验）。
> 本试点只解析 3 个样本文件，验证 variants / subprotocols / sentences 三套块结构可统一为一种 entry schema；验证通过后即停，不全量。
> **统一 schema**：`id | func | citekey | status | kind | text | anchor`（7 字段，三套字段名完全一致）。

| 分支 | 来源文件 | 子清单 | verbatim | 模板 |
|---|---|---|---|---|
| ① variants（变体/技巧块） | `corpus/variants/A_construct_differentiation.md` | [`variants-A_construct_differentiation.md`](variants-A_construct_differentiation.md) | 6 | 3 |
| ② subprotocols（pattern 库） | `corpus/subprotocols/hypothesis_derivation_patterns.md` | [`subprotocols-hypothesis_derivation_patterns.md`](subprotocols-hypothesis_derivation_patterns.md) | 17 | 43 |
| ③ sentences（变体块+决策矩阵） | `corpus/sentences/hypothesis_forms.md` | [`sentences-hypothesis_forms.md`](sentences-hypothesis_forms.md) | 41 | 57 |

合计：3 分支 / verbatim 64 条 / 模板 103 条。

## 待补录

- [`_unparsed.md`](_unparsed.md)：6 条（非块内锚点/边界模糊矩阵句等，待人工判定）。
