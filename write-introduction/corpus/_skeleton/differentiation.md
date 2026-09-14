# differentiation — 骨架子索引

> 由 `scripts/build_indices.py` 生成，可重复运行、幂等。请勿手改本文件。
> **底本单源**：verbatim 原句只存本索引；形状包与借句表只引 `id`，不复写正文。
> `状态=verbatim` 为逐字底本（无槽位、与源文件逐字一致，不得改写/拼接/补全）；`状态=模板` 为含 `[槽位]` 的填槽骨架，不可当逐字底本引用。
> 锚点格式 `标题-{序数}`：指向源文件中该引文所在标题块的文档序数（非已接受 verbatim 计数），块内增删其它 verbatim 不影响定位。
> `路径#锚点` 可用于回源核对；`--verify` 会断言每条底本可在其锚点块内逐字定位。人工剔除记录见 `scripts/skeleton_exclusions.txt`，待补录项见 `_unparsed.md`。

条目：verbatim 1 条 / 模板 1 条。

## Verbatim 底本

| id | citekey | verbatim 原句 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `01-prior-work-boundary-clarification#1` | weng_yang | Before proceeding, it is useful to distinguish between our study and that by Gupta and Wowak (2017). In their seminal work, Gupta and Wowak (2017) show that conservative boards tend to pay CEOs more and emphasize firm performance in designing CEO compensation. Our study differs from Gupta and Wowak (2017) in two ways. | `corpus/differentiation/01-prior-work-boundary-clarification.md#标题-9` | verbatim |

## 填槽模板（模板）

| id | citekey | 模板 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `01-prior-work-boundary-clarification#T1` | weng_yang | "Before proceeding, it is useful to distinguish between our study and that by [closest prior work] ([citation]). In their seminal work, [authors] show that [closest paper's finding]. Our study differs from [authors] in [N] ways. First, [authors] investigate [their DV], a crucial issue for [their domain]. In comparison, we are interested in [our DV], a notion central to [our domain]. Second, [authors] consider [their IV] as their main predictor. In contrast, we focus on [our IV]. Since [linking logic connecting the two studies], our study complements the insights by [authors], enriching our understanding of [broader domain]." | `corpus/differentiation/01-prior-work-boundary-clarification.md#标题-9` | 模板（填槽模板） |
