# phrasebank — 骨架子索引

> 由 `scripts/build_indices.py` 生成，可重复运行、幂等。请勿手改本文件。
> **底本单源**：verbatim 原句只存本索引；形状包与借句表只引 `id`，不复写正文。
> `状态=verbatim` 为逐字底本（无槽位、与源文件逐字一致，不得改写/拼接/补全）；`状态=模板` 为含 `[槽位]` 的填槽骨架，不可当逐字底本引用。
> 锚点格式 `标题-{序数}`：指向源文件中该引文所在标题块的文档序数（非已接受 verbatim 计数），块内增删其它 verbatim 不影响定位。
> `路径#锚点` 可用于回源核对；`--verify` 会断言每条底本可在其锚点块内逐字定位。人工剔除记录见 `scripts/skeleton_exclusions.txt`，待补录项见 `_unparsed.md`。

条目：verbatim 5 条 / 模板 91 条。

## Verbatim 底本

| id | citekey | verbatim 原句 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `methods-process#3` | morley2021 | Descriptive data were generated for all variables. | `corpus/phrasebank/methods-process.md#句子行-3` | verbatim（借句） |
| `methods-process#6` | morley2021 | Article references were searched further for additional relevant publications. | `corpus/phrasebank/methods-process.md#句子行-6` | verbatim（借句） |
| `methods-process#8` | morley2021 | Injection solutions were coded by a colleague to reduce experimenter bias. | `corpus/phrasebank/methods-process.md#句子行-8` | verbatim（借句） |
| `methods-process#35` | morley2021 | Reliability was calculated using Cronbach's alpha. | `corpus/phrasebank/methods-process.md#句子行-35` | verbatim（借句） |
| `methods-process#37` | morley2021 | A p value < 0.05 was considered significant. | `corpus/phrasebank/methods-process.md#句子行-37` | verbatim（借句） |

## 填槽模板（模板）

| id | citekey | 模板 | 卡片路径#锚点 | 状态 |
|---|---|---|---|---|
| `critique-phrases#1` | morley2021 | [Prior study / This stream of research] is limited by its reliance on [specific data source / method]. | `corpus/phrasebank/critique-phrases.md#句子行-1` | 模板（借句（含槽位，模板）） |
| `critique-phrases#2` | morley2021 | [A shortcoming of X (Year)] is that [specific measurement / sample / identification] does not fully capture [construct/threat]. | `corpus/phrasebank/critique-phrases.md#句子行-2` | 模板（借句（含槽位，模板）） |
| `critique-phrases#3` | morley2021 | [X (Year)] [focuses on / examines] [context], which [limits / constrains] the [generalizability / external validity] of its findings to [other contexts]. | `corpus/phrasebank/critique-phrases.md#句子行-3` | 模板（借句（含槽位，模板）） |
| `critique-phrases#4` | morley2021 | Although [X (Year)] [contribution], the study [does not address / cannot rule out] [specific alternative explanation / threat]. | `corpus/phrasebank/critique-phrases.md#句子行-4` | 模板（借句（含槽位，模板）） |
| `critique-phrases#5` | morley2021 | The [findings / conclusions] of [X (Year)] should be interpreted in light of [specific limitation]. | `corpus/phrasebank/critique-phrases.md#句子行-5` | 模板（借句（含槽位，模板）） |
| `critique-phrases#6` | morley2021 | [Prior theory / This perspective] [fails to account for / overlooks / neglects] [specific factor / mechanism]. | `corpus/phrasebank/critique-phrases.md#句子行-6` | 模板（借句（含槽位，模板）） |
| `critique-phrases#7` | morley2021 | [Existing research] has [tended to / predominantly] [assumed / focused on] [X], leaving [Y] [unexplored / undertheorized]. | `corpus/phrasebank/critique-phrases.md#句子行-7` | 模板（借句（含槽位，模板）） |
| `critique-phrases#8` | morley2021 | While [theory A] explains [phenomenon], it does not address [specific boundary / mechanism] that [our study examines]. | `corpus/phrasebank/critique-phrases.md#句子行-8` | 模板（借句（含槽位，模板）） |
| `critique-phrases#9` | morley2021 | A [limitation / gap] of this [approach / framework] is that it [assumes / treats] [X] as [uniform/static], whereas [evidence/theory] suggests [X is heterogeneous/dynamic]. | `corpus/phrasebank/critique-phrases.md#句子行-9` | 模板（借句（含槽位，模板）） |
| `critique-phrases#10` | morley2021 | [X's (Year)] findings are [specific to / bound by] [context/condition], and may not [extend to / hold in] [other context]. | `corpus/phrasebank/critique-phrases.md#句子行-10` | 模板（借句（含槽位，模板）） |
| `critique-phrases#11` | morley2021 | The [generalizability / applicability] of [X (Year)] is [constrained / limited] by [scope condition]. | `corpus/phrasebank/critique-phrases.md#句子行-11` | 模板（借句（含槽位，模板）） |
| `critique-phrases#12` | morley2021 | [Prior work] has examined [X] primarily in [context A]; whether [the relationship] holds in [context B] remains an [open / empirical] question. | `corpus/phrasebank/critique-phrases.md#句子行-12` | 模板（借句（含槽位，模板）） |
| `critique-phrases#13` | morley2021 | [This limitation / gap] motivates our [examination / approach], which [addresses / overcomes] it by [specific design choice]. | `corpus/phrasebank/critique-phrases.md#句子行-13` | 模板（借句（含槽位，模板）） |
| `critique-phrases#14` | morley2021 | We [build on / extend] [X (Year)] by [specific contribution] that [addresses the limitation / relaxes the assumption]. | `corpus/phrasebank/critique-phrases.md#句子行-14` | 模板（借句（含槽位，模板）） |
| `critique-phrases#15` | morley2021 | To [address / overcome] this [limitation / concern], we [employ a different design / incorporate additional data / theorize the mechanism]. | `corpus/phrasebank/critique-phrases.md#句子行-15` | 模板（借句（含槽位，模板）） |
| `critique-phrases#16` | morley2021 | Although [X (Year)] [makes an important contribution / advances our understanding of], its [approach / findings] are [limited / constrained] by [specific issue]. | `corpus/phrasebank/critique-phrases.md#句子行-16` | 模板（借句（含槽位，模板）） |
| `critique-phrases#17` | morley2021 | [Building on / Extending] [X's (Year)] [contribution], we [address / examine] [the limitation / the unanswered question] by [approach]. | `corpus/phrasebank/critique-phrases.md#句子行-17` | 模板（借句（含槽位，模板）） |
| `critique-phrases#18` | morley2021 | [X (Year)] [advanced / pioneered] [the study of], yet [left open / did not resolve] [specific question]—which we [take up / address] here. | `corpus/phrasebank/critique-phrases.md#句子行-18` | 模板（借句（含槽位，模板）） |
| `hedging-strength#1` | morley2021 | A likely/probable/possible explanation is that [X]... | `corpus/phrasebank/hedging-strength.md#句子行-1` | 模板（借句（含槽位，模板）） |
| `hedging-strength#2` | morley2021 | This inconsistency may be due to [specific methodological/theoretical reason]. | `corpus/phrasebank/hedging-strength.md#句子行-2` | 模板（借句（含槽位，模板）） |
| `hedging-strength#3` | morley2021 | It is possible that this result is due to [mechanism]. | `corpus/phrasebank/hedging-strength.md#句子行-3` | 模板（借句（含槽位，模板）） |
| `hedging-strength#4` | morley2021 | This discrepancy could be attributed to [factor]. | `corpus/phrasebank/hedging-strength.md#句子行-4` | 模板（借句（含槽位，模板）） |
| `hedging-strength#5` | morley2021 | A possible explanation for this might be that [mechanism]. | `corpus/phrasebank/hedging-strength.md#句子行-5` | 模板（借句（含槽位，模板）） |
| `hedging-strength#6` | morley2021 | This rather contradictory result may be due to [boundary condition not theorized]. | `corpus/phrasebank/hedging-strength.md#句子行-6` | 模板（借句（含槽位，模板）） |
| `hedging-strength#7` | morley2021 | There are several possible explanations for this result. First, [explanation A]. Alternatively, [explanation B]. | `corpus/phrasebank/hedging-strength.md#句子行-7` | 模板（借句（含槽位，模板）） |
| `hedging-strength#8` | morley2021 | A possible explanation for these results may be the lack of adequate [measurement/temporal scope/context]. | `corpus/phrasebank/hedging-strength.md#句子行-8` | 模板（借句（含槽位，模板）） |
| `hedging-strength#9` | morley2021 | These findings must be interpreted with caution because [limitation]. | `corpus/phrasebank/hedging-strength.md#句子行-9` | 模板（借句（含槽位，模板）） |
| `hedging-strength#10` | morley2021 | We cannot exclude the possibility that [alternative explanation]. | `corpus/phrasebank/hedging-strength.md#句子行-10` | 模板（借句（含槽位，模板）） |
| `hedging-strength#11` | morley2021 | It should be noted that [boundary condition limiting generalizability]. | `corpus/phrasebank/hedging-strength.md#句子行-11` | 模板（借句（含槽位，模板）） |
| `hedging-strength#12` | morley2021 | Further research is needed to confirm whether [finding] holds in [different context]. | `corpus/phrasebank/hedging-strength.md#句子行-12` | 模板（借句（含槽位，模板）） |
| `methods-process#1` | morley2021 | Data were collected using [source/instrument]. | `corpus/phrasebank/methods-process.md#句子行-1` | 模板（借句（含槽位，模板）） |
| `methods-process#2` | morley2021 | Data were gathered from multiple sources at various time points during [period]. | `corpus/phrasebank/methods-process.md#句子行-2` | 模板（借句（含槽位，模板）） |
| `methods-process#4` | morley2021 | Data management and analysis were performed using [software/version]. | `corpus/phrasebank/methods-process.md#句子行-4` | 模板（借句（含槽位，模板）） |
| `methods-process#5` | morley2021 | Published studies were identified using a search strategy developed in [prior work]. | `corpus/phrasebank/methods-process.md#句子行-5` | 模板（借句（含槽位，模板）） |
| `methods-process#7` | morley2021 | The participants were asked to [rate / indicate / describe / recall] ... | `corpus/phrasebank/methods-process.md#句子行-7` | 模板（借句（含槽位，模板）） |
| `methods-process#9` | morley2021 | The [materials] were coded by [independent coders] to reduce [coder] bias. | `corpus/phrasebank/methods-process.md#句子行-9` | 模板（借句（含槽位，模板）） |
| `methods-process#10` | morley2021 | Prior to [data collection / analysis], [step]. | `corpus/phrasebank/methods-process.md#句子行-10` | 模板（借句（含槽位，模板）） |
| `methods-process#11` | morley2021 | (Immediately) After [step], the [samples/data] were [next step]. | `corpus/phrasebank/methods-process.md#句子行-11` | 模板（借句（含槽位，模板）） |
| `methods-process#12` | morley2021 | On [arrival at / completion of / obtaining X], [step] was carried out. | `corpus/phrasebank/methods-process.md#句子行-12` | 模板（借句（含槽位，模板）） |
| `methods-process#13` | morley2021 | Once the [Xs] were [located/extracted/matched], it was first necessary to ... | `corpus/phrasebank/methods-process.md#句子行-13` | 模板（借句（含槽位，模板）） |
| `methods-process#14` | morley2021 | Following [correction for / confirmation of] X, [step]. | `corpus/phrasebank/methods-process.md#句子行-14` | 模板（借句（含槽位，模板）） |
| `methods-process#15` | morley2021 | The [data] were then [processed], and this [value] was recorded as ... | `corpus/phrasebank/methods-process.md#句子行-15` | 模板（借句（含槽位，模板）） |
| `methods-process#16` | morley2021 | When [dividing/constructing] X, care was taken to ... | `corpus/phrasebank/methods-process.md#句子行-16` | 模板（借句（含槽位，模板）） |
| `methods-process#17` | morley2021 | Finally, [questions were asked as to / tests were conducted on] ... | `corpus/phrasebank/methods-process.md#句子行-17` | 模板（借句（含槽位，模板）） |
| `methods-process#18` | morley2021 | Comparisons between the two groups were made using [test]. | `corpus/phrasebank/methods-process.md#句子行-18` | 模板（借句（含槽位，模板）） |
| `methods-process#19` | morley2021 | The relationship between X and Y was examined using [estimator]. | `corpus/phrasebank/methods-process.md#句子行-19` | 模板（借句（含槽位，模板）） |
| `methods-process#20` | morley2021 | [Subjects/Firms] were recruited using [channel/criteria]. | `corpus/phrasebank/methods-process.md#句子行-20` | 模板（借句（含槽位，模板）） |
| `methods-process#21` | morley2021 | Firms were selected using [criteria]. | `corpus/phrasebank/methods-process.md#句子行-21` | 模板（借句（含槽位，模板）） |
| `methods-process#22` | morley2021 | The data were recorded ... and transcribed using [tool]. | `corpus/phrasebank/methods-process.md#句子行-22` | 模板（借句（含槽位，模板）） |
| `methods-process#23` | morley2021 | The texts were processed using [tool/library]. | `corpus/phrasebank/methods-process.md#句子行-23` | 模板（借句（含槽位，模板）） |
| `methods-process#24` | morley2021 | In order to [investigate/identify] the effects of X, [step]. | `corpus/phrasebank/methods-process.md#句子行-24` | 模板（借句（含槽位，模板）） |
| `methods-process#25` | morley2021 | In order to address these [concerns], the following steps were taken: ... | `corpus/phrasebank/methods-process.md#句子行-25` | 模板（借句（含槽位，模板）） |
| `methods-process#26` | morley2021 | To avoid [problem], [step]. | `corpus/phrasebank/methods-process.md#句子行-26` | 模板（借句（含槽位，模板）） |
| `methods-process#27` | morley2021 | To test whether ..., [step]. | `corpus/phrasebank/methods-process.md#句子行-27` | 模板（借句（含槽位，模板）） |
| `methods-process#28` | morley2021 | To establish whether ..., [step]. | `corpus/phrasebank/methods-process.md#句子行-28` | 模板（借句（含槽位，模板）） |
| `methods-process#29` | morley2021 | To address the possibility of [alternative], [step]. | `corpus/phrasebank/methods-process.md#句子行-29` | 模板（借句（含槽位，模板）） |
| `methods-process#30` | morley2021 | For the purpose of [analysis/measurement], [step]. | `corpus/phrasebank/methods-process.md#句子行-30` | 模板（借句（含槽位，模板）） |
| `methods-process#31` | morley2021 | A [test] was [conducted/performed/carried out] to assess whether ... | `corpus/phrasebank/methods-process.md#句子行-31` | 模板（借句（含槽位，模板）） |
| `methods-process#32` | morley2021 | A [test] was [run/used] to test the hypothesis that ... | `corpus/phrasebank/methods-process.md#句子行-32` | 模板（借句（含槽位，模板）） |
| `methods-process#33` | morley2021 | A [test] was conducted to compare the [means/distributions] of ... | `corpus/phrasebank/methods-process.md#句子行-33` | 模板（借句（含槽位，模板）） |
| `methods-process#34` | morley2021 | A [test] was performed to determine whether there was a difference between ... | `corpus/phrasebank/methods-process.md#句子行-34` | 模板（借句（含槽位，模板）） |
| `methods-process#36` | morley2021 | All analyses were carried out using [Stata/SPSS/R], version [x]. | `corpus/phrasebank/methods-process.md#句子行-36` | 模板（借句（含槽位，模板）） |
| `quantities-trends#1` | morley2021 | Over half of [those surveyed / the sample firms] indicated that ... | `corpus/phrasebank/quantities-trends.md#句子行-1` | 模板（借句（含槽位，模板）） |
| `quantities-trends#2` | morley2021 | Nearly half of the respondents (48%) [agreed / reported] that ... | `corpus/phrasebank/quantities-trends.md#句子行-2` | 模板（借句（含槽位，模板）） |
| `quantities-trends#3` | morley2021 | Almost two-thirds of [the observations] (64%) ... | `corpus/phrasebank/quantities-trends.md#句子行-3` | 模板（借句（含槽位，模板）） |
| `quantities-trends#4` | morley2021 | Of the [270] [firms], nearly one-third [did not / failed to] ... | `corpus/phrasebank/quantities-trends.md#句子行-4` | 模板（借句（含槽位，模板）） |
| `quantities-trends#5` | morley2021 | Less than a third of [those who responded] (32%) ... | `corpus/phrasebank/quantities-trends.md#句子行-5` | 模板（借句（含槽位，模板）） |
| `quantities-trends#6` | morley2021 | The response rate was [60]% at [six months] and [56]% at [12 months]. | `corpus/phrasebank/quantities-trends.md#句子行-6` | 模板（借句（含槽位，模板）） |
| `quantities-trends#7` | morley2021 | [Just over / Well over / More than / Almost / Around / Approximately] [half / a third / a quarter] of [those surveyed / the respondents / the sample] ... | `corpus/phrasebank/quantities-trends.md#句子行-7` | 模板（借句（含槽位，模板）） |
| `quantities-trends#8` | morley2021 | The mean [age/value] of [Xs] was [48.3] ± [6.3] [years/units]. | `corpus/phrasebank/quantities-trends.md#句子行-8` | 模板（借句（含槽位，模板）） |
| `quantities-trends#9` | morley2021 | The mean [X] for the [two groups] was subjected to [analysis] to determine ... | `corpus/phrasebank/quantities-trends.md#句子行-9` | 模板（借句（含槽位，模板）） |
| `quantities-trends#10` | morley2021 | [Group A] had a much [lower/higher] than average [X]. | `corpus/phrasebank/quantities-trends.md#句子行-10` | 模板（借句（含槽位，模板）） |
| `quantities-trends#11` | morley2021 | The respondents had practised X for an average of [15] years (range [6] to [35] years). | `corpus/phrasebank/quantities-trends.md#句子行-11` | 模板（借句（含槽位，模板）） |
| `quantities-trends#12` | morley2021 | The sample firms had been [listed/active] for an average of [N] years (range [a] to [b]). | `corpus/phrasebank/quantities-trends.md#句子行-12` | 模板（借句（含槽位，模板）） |
| `quantities-trends#13` | morley2021 | The participants were aged [19] to [25] ... | `corpus/phrasebank/quantities-trends.md#句子行-13` | 模板（借句（含槽位，模板）） |
| `quantities-trends#14` | morley2021 | The [firms/observations] span [years/values] from [a] to [b]. | `corpus/phrasebank/quantities-trends.md#句子行-14` | 模板（借句（含槽位，模板）） |
| `quantities-trends#15` | morley2021 | Rates of [decline] ranged from [2.71] to [0.08] [units] (Table [x]) with a mean of [0.97]. | `corpus/phrasebank/quantities-trends.md#句子行-15` | 模板（借句（含槽位，模板）） |
| `quantities-trends#16` | morley2021 | Most estimates of X range from [200] to [700] and, in some cases, up to [a million]. | `corpus/phrasebank/quantities-trends.md#句子行-16` | 模板（借句（含槽位，模板）） |
| `quantities-trends#17` | morley2021 | X had the [highest/lowest] proportion of Y at only [14] per cent. | `corpus/phrasebank/quantities-trends.md#句子行-17` | 模板（借句（含槽位，模板）） |
| `quantities-trends#18` | morley2021 | The [annual rate] dropped from [44.4] to [38.6] per [1000] per [annum]. | `corpus/phrasebank/quantities-trends.md#句子行-18` | 模板（借句（含槽位，模板）） |
| `quantities-trends#19` | morley2021 | The proportion of [X] was [65]% higher in [A] than [in B]. | `corpus/phrasebank/quantities-trends.md#句子行-19` | 模板（借句（含槽位，模板）） |
| `quantities-trends#20` | morley2021 | The graph shows that there has been a [slight / steep / sharp / steady / gradual / marked] [fall / rise / drop / decline / increase / decrease] in the [number/rate] of ... | `corpus/phrasebank/quantities-trends.md#句子行-20` | 模板（借句（含槽位，模板）） |
| `quantities-trends#21` | morley2021 | Figure [x] reveals that there has been a [marked] [increase] in ... | `corpus/phrasebank/quantities-trends.md#句子行-21` | 模板（借句（含槽位，模板）） |
| `quantities-trends#22` | morley2021 | What is striking in this [table/figure] is the [growth of / variability of / difference between] ... | `corpus/phrasebank/quantities-trends.md#句子行-22` | 模板（借句（含槽位，模板）） |
| `quantities-trends#23` | morley2021 | What stands out in this [figure] is the [rapid decrease in / steady decline of] ... | `corpus/phrasebank/quantities-trends.md#句子行-23` | 模板（借句（含槽位，模板）） |
| `quantities-trends#24` | morley2021 | What can be clearly seen in this [table] is the [general pattern of / dominance of] ... | `corpus/phrasebank/quantities-trends.md#句子行-24` | 模板（借句（含槽位，模板）） |
| `quantities-trends#25` | morley2021 | [X] peaked in [year/period]. | `corpus/phrasebank/quantities-trends.md#句子行-25` | 模板（借句（含槽位，模板）） |
| `quantities-trends#26` | morley2021 | The [number/rate] of Xs reached a peak during [period]. | `corpus/phrasebank/quantities-trends.md#句子行-26` | 模板（借句（含槽位，模板）） |
| `quantities-trends#27` | morley2021 | [X] reached a low point in [year]. | `corpus/phrasebank/quantities-trends.md#句子行-27` | 模板（借句（含槽位，模板）） |
| `quantities-trends#28` | morley2021 | The rate fell to a low point of [value] at the end of [period]. | `corpus/phrasebank/quantities-trends.md#句子行-28` | 模板（借句（含槽位，模板）） |
| `quantities-trends#29` | morley2021 | The [rate/number] of X is [likely to / expected to / projected to] [fall / rise / level off / remain steady] [after 2030]. | `corpus/phrasebank/quantities-trends.md#句子行-29` | 模板（借句（含槽位，模板）） |
