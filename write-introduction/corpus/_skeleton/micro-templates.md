# micro-templates — 骨架子索引

> 由 `scripts/build_indices.py` 生成，可重复运行、幂等。请勿手改本文件。
> **底本单源**：verbatim 原句只存本索引；形状包与借句表只引 `id`，不复写正文。
> `状态=verbatim` 为逐字底本（无槽位、与源文件逐字一致，不得改写/拼接/补全）；`状态=模板` 为含 `[槽位]` 的填槽骨架，不可当逐字底本引用。
> 锚点格式 `标题-{序数}`：指向源文件中该引文所在标题块的文档序数（非已接受 verbatim 计数），块内增删其它 verbatim 不影响定位。
> `路径#锚点` 可用于回源核对；`--verify` 会断言每条底本可在其锚点块内逐字定位。人工剔除记录见 `scripts/skeleton_exclusions.txt`，待补录项见 `_unparsed.md`。

条目：verbatim 7 条 / 模板 30 条。

## Verbatim 底本

| id | citekey | verbatim 原句 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `key-line-patterns#1` | yangpandey2011 | While scholars have proposed compelling prescriptive models (Ebdon and Franklin 2006; Kweit and Kweit 1981; Thomas 1995; Walters, Aydelotte, and Miller 2000), **these models rarely have been tested with large-scale data**. | `corpus/micro-templates/key-line-patterns.md#标题-4` | verbatim（范文借句） |
| `key-line-patterns#2` | provanmilward1995 | **Absent from these views, however, is a focus on nonstructural outcomes** of the network as a whole. | `corpus/micro-templates/key-line-patterns.md#标题-4` | verbatim（范文借句） |
| `key-line-patterns#3` | astleyvandeven1983 | **Moreover**, economic historians such as Chandler (1977) and institutional economists such as Williamson (1975) contend that **industrial structure evolves in determinate ways**. | `corpus/micro-templates/key-line-patterns.md#标题-5` | verbatim（范文借句） |
| `key-line-patterns#4` | raineybozeman2000 | **In addition to** the stream of research on work satisfaction, **there are now many studies that compare the work values and motives of public and private employees**. | `corpus/micro-templates/key-line-patterns.md#标题-5` | verbatim（范文借句） |
| `key-line-patterns#5` | guoacar2005 | A key challenge for an individual organization in choosing among different collaboration forms, **therefore**, is to keep the dynamic balance between managing resource dependence and sustaining organizational autonomy (Gray & Wood, 1991, p. 7). | `corpus/micro-templates/key-line-patterns.md#标题-6` | verbatim（范文借句） |
| `key-line-patterns#6` | guoacar2005 | **In sum, the resource dependency theory suggests that** organizations with greater resource scarcity, as indicated by their smaller organizational size, might be more inclined to collaborate formally; conversely, organizations with greater resource sufficiency, as indicated by their larger annual budget size, might be less inclined to collaborate formally. | `corpus/micro-templates/key-line-patterns.md#标题-8` | verbatim（范文借句） |
| `key-line-patterns#7` | astleyvandeven1983 | **The focus of managerial decision making, therefore, is not on choice but on gathering correct information** about environmental variations and on using technical criteria to examine the consequences of responses to alternative demands. | `corpus/micro-templates/key-line-patterns.md#标题-8` | verbatim（范文借句） |

## 填槽模板（模板）

| id | citekey | 模板 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `key-line-patterns#T1` | 未标注 | [承上: 承认上文观点/文献的价值] + [转折标记] + [启下: 指出其缺失/未检验之处] | `corpus/micro-templates/key-line-patterns.md#标题-4` | 模板（句法骨架） |
| `key-line-patterns#T2` | 未标注 | [递进标记] + [承上: 既有文献/观点] + [启下: 本段补充的新维度] | `corpus/micro-templates/key-line-patterns.md#标题-5` | 模板（句法骨架） |
| `key-line-patterns#T3` | 未标注 | [启下: 本段论点] + [因果标记 therefore/thus] + [承上: 由上段理由推出] | `corpus/micro-templates/key-line-patterns.md#标题-6` | 模板（句法骨架） |
| `key-line-patterns#T4` | 未标注 | [标记词] + [回扣段首 Point 的结论句（不是重复段首原句，是把论证结果上升一步）] | `corpus/micro-templates/key-line-patterns.md#标题-8` | 模板（句法骨架） |
| `thesis-models#T1` | 未标注 | Although many scholars have argued about [A and B], a careful examination suggests [C]. Although prior work often assumes that [assumption] ([citations]), we show that [C]. | `corpus/micro-templates/thesis-models.md#标题-2` | 模板（句法骨架） |
| `thesis-models#T2` | 未标注 | [Topic] remains largely unexplored: although [A] and [B] have been examined, [C] has received little systematic attention. | `corpus/micro-templates/thesis-models.md#标题-3` | 模板（句法骨架） |
| `thesis-models#T3` | 未标注 | Although [phenomenon] might appear to be [surface reading A], a closer look reveals [B]. | `corpus/micro-templates/thesis-models.md#标题-3` | 模板（句法骨架） |
| `thesis-models#T4` | 未标注 | Although we build on [prior framework]'s insight that [A] and [B] ([citations]), we [extend / refine / limit] it by [C: new mechanism / new boundary / new scope]. | `corpus/micro-templates/thesis-models.md#标题-4` | 模板（句法骨架） |
| `thesis-models#T5` | 未标注 | Some people explain [phenomenon] by suggesting [explanation A], but a close analysis reveals several compelling, but competing, explanations: [A] / [B] / [C]. We adjudicate among them by [distinctive data / design / test]. | `corpus/micro-templates/thesis-models.md#标题-5` | 模板（句法骨架） |
| `transition-signals#T1` | 未标注 | 常用词: again, and, also, besides, equally important, first (second, etc.), further, furthermore, in addition, in the first place, moreover, next, too | `corpus/micro-templates/transition-signals.md#标题-3` | 模板（词表） |
| `transition-signals#T2` | 未标注 | 学术写作偏好: furthermore, in addition, moreover, equally important | `corpus/micro-templates/transition-signals.md#标题-3` | 模板（词表） |
| `transition-signals#T3` | 未标注 | Prior research has focused on CEO overconfidence as a driver of risky decisions. **Furthermore**, recent work suggests that overconfidence also shapes how leaders interpret stakeholder feedback. | `corpus/micro-templates/transition-signals.md#标题-3` | 模板（示例行（无出处）） |
| `transition-signals#T4` | 未标注 | 常用词: for example, for instance, in fact, specifically, that is, to illustrate | `corpus/micro-templates/transition-signals.md#标题-4` | 模板（词表） |
| `transition-signals#T5` | 未标注 | 学术写作偏好: for example, for instance, specifically, that is, to illustrate | `corpus/micro-templates/transition-signals.md#标题-4` | 模板（词表） |
| `transition-signals#T6` | 未标注 | CEO communications can signal psychological traits. **For instance**, promotion-focused language tends to emphasize gains and aspirations, whereas prevention-focused language emphasizes safety and responsibility. | `corpus/micro-templates/transition-signals.md#标题-4` | 模板（示例行（无出处）） |
| `transition-signals#T7` | 未标注 | 常用词: also, in the same manner, likewise, similarly | `corpus/micro-templates/transition-signals.md#标题-5` | 模板（词表） |
| `transition-signals#T8` | 未标注 | 学术写作偏好: similarly, likewise, in the same manner | `corpus/micro-templates/transition-signals.md#标题-5` | 模板（词表） |
| `transition-signals#T9` | 未标注 | Investors attribute positive outcomes more to promotion-focused CEOs. **Similarly**, they may discount negative outcomes when prevention-focused CEOs are perceived as vigilant. | `corpus/micro-templates/transition-signals.md#标题-5` | 模板（示例行（无出处）） |
| `transition-signals#T10` | 未标注 | 常用词: although, and yet, at the same time, but, despite, even though, however, in contrast, in spite of, nevertheless, on the contrary, on the other hand, still, though, yet | `corpus/micro-templates/transition-signals.md#标题-6` | 模板（词表） |
| `transition-signals#T11` | 未标注 | 学术写作偏好: however, in contrast, nevertheless, although, despite, yet, conversely | `corpus/micro-templates/transition-signals.md#标题-6` | 模板（词表） |
| `transition-signals#T12` | 未标注 | Prior research has emphasized internal organizational processes. **However**, little is known about how external audiences interpret CEO motivational signals. | `corpus/micro-templates/transition-signals.md#标题-6` | 模板（示例行（无出处）） |
| `transition-signals#T13` | 未标注 | 常用词: accordingly, as a result, because, consequently, for this reason, hence, if, otherwise, since, so, then, therefore, thus | `corpus/micro-templates/transition-signals.md#标题-7` | 模板（词表） |
| `transition-signals#T14` | 未标注 | 学术写作偏好: therefore, thus, consequently, as a result, because, since, hence | `corpus/micro-templates/transition-signals.md#标题-7` | 模板（词表） |
| `transition-signals#T15` | 未标注 | Promotion-focused CEOs are perceived as pursuing maximal gains. **Therefore**, investors attribute positive earnings deviations more strongly to these CEOs. | `corpus/micro-templates/transition-signals.md#标题-7` | 模板（示例行（无出处）） |
| `transition-signals#T16` | 未标注 | 常用词: all in all, in conclusion, in other words, in short, in summary, on the whole, that is, therefore, to sum up | `corpus/micro-templates/transition-signals.md#标题-8` | 模板（词表） |
| `transition-signals#T17` | 未标注 | 学术写作偏好: in sum, together, taken together, in other words, thus, therefore | `corpus/micro-templates/transition-signals.md#标题-8` | 模板（词表） |
| `transition-signals#T18` | 未标注 | Promotion and prevention foci shape attributions through distinct mechanisms. **In other words**, the same earnings deviation can yield different investor reactions depending on the perceived CEO regulatory focus. | `corpus/micro-templates/transition-signals.md#标题-8` | 模板（示例行（无出处）） |
| `transition-signals#T19` | 未标注 | 常用词: after, afterward, as, as long as, as soon as, at last, before, during, earlier, finally, formerly, immediately, later, meanwhile, next, since, shortly, subsequently, then, thereafter, until, when, while | `corpus/micro-templates/transition-signals.md#标题-9` | 模板（词表） |
| `transition-signals#T20` | 未标注 | 学术写作偏好: subsequently, then, next, finally, earlier, previously, meanwhile | `corpus/micro-templates/transition-signals.md#标题-9` | 模板（词表） |
| `transition-signals#T21` | 未标注 | First, investors perceive the CEO's regulatory focus from annual report language. **Subsequently**, they use this perception as an interpretive frame when reacting to earnings deviations. | `corpus/micro-templates/transition-signals.md#标题-9` | 模板（示例行（无出处）） |
