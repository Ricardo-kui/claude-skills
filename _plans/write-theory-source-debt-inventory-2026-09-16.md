# write-theory 来源标注欠账清单 — 564 条（status 口径）

> 生成：2026-09-16，基线 commit 3551ea3（来源标注补全后）。
> 口径：骨架索引 7 列中 `status == 未标注` 的条目，与 `build_indices --verify` SUMMARY 一致；
> 其中 citekey 已知 **267** 条（仅 status 待升档）、citekey 仍缺 **297** 条。

## 类别分布与闭合路径

| 类别 | 条数 | 含义 | 闭合路径 |
|---|---|---|---|
| status待升档 | 171 | 裸 wb 标注块（citekey 已落，status 待 registry） | registry 升档（同题≥2篇复现 + regression_case，或 expert_audit_override） |
| 已标注-status待升 | 71 | 重编号前已有标注的块，pattern 未入 registry | 块已有 wb/来源行但 pattern 未入 registry status——按升档路径处理 |
| 无仓内证据 | 266 | 五通道证据均未命中的块 | 回源 PDF 补 `**原文锚点**`/wb 标记，或用户裁定归属；无源则保持未标注 |
| 脚手架节 | 6 | 速查表/子协议索引/QC/功能地图等脚手架 | 设计上无单源归属——保持未标注（如需可挂所属协议父节来源） |
| matrix硬编码 | 50 | 决策矩阵单元格模板（解析器硬编码） | 解析器改造：`_matrix_templates` 继承所在节/块的 citekey |
| 证据冲突待人审 | 0 | 块内出处证据互相冲突 | 块内多处出处互相冲突——需人审定主源 |

## 分文件明细

### sentences/acknowledgment_response.md（24 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `2-1-there-are-causes-in-addi-69b440.a` | — | 无仓内证据 | verbatim | If your argument is about cause and effect, reme… | `2-1-there-are-causes-in-addi-69b440` |
| `2-1-there-are-causes-in-addi-69b440.t1` | — | 无仓内证据 | 模板 | [承认] Granted, [X] is not the only factor that ca… | `2-1-there-are-causes-in-addi-69b440` |
| `2-1-there-are-causes-in-addi-69b440.t2` | — | 无仓内证据 | 模板 | [承认] It is easy to [think/imagine/argue] that [Y… | `2-1-there-are-causes-in-addi-69b440` |
| `2-2-what-about-these-counter-43dd16.a` | — | 无仓内证据 | verbatim | No matter how rich your evidence, some skeptical… | `2-2-what-about-these-counter-43dd16` |
| `2-2-what-about-these-counter-43dd16.b` | — | 无仓内证据 | verbatim | People who do not understand statistical reasoni… | `2-2-what-about-these-counter-43dd16` |
| `2-2-what-about-these-counter-43dd16.t1` | — | 无仓内证据 | 模板 | [承认] It might seem that [counterexample] undermi… | `2-2-what-about-these-counter-43dd16` |
| `2-2-what-about-these-counter-43dd16.t2` | — | 无仓内证据 | 模板 | [承认] Admittedly, [case] does not fit our account… | `2-2-what-about-these-counter-43dd16` |
| `2-3-acknowledge-without-resp-eb776b.a` | — | 无仓内证据 | verbatim | Candidly acknowledge the issue and respond that … | `2-3-acknowledge-without-resp-eb776b` |
| `2-3-acknowledge-without-resp-eb776b.b` | — | 无仓内证据 | verbatim | It might seem that when jurors hear the facts of… | `2-3-acknowledge-without-resp-eb776b` |
| `2-3-acknowledge-without-resp-eb776b.t1` | — | 无仓内证据 | 模板 | [补偿姿态] Although our [measure/sample] cannot [lim… | `2-3-acknowledge-without-resp-eb776b` |
| `2-4-i-don-t-define-x-as-you--6cf055.a` | — | 无仓内证据 | verbatim | When your argument hinges on the meaning of a te… | `2-4-i-don-t-define-x-as-you--6cf055` |
| `2-4-i-don-t-define-x-as-you--6cf055.b` | — | 无仓内证据 | verbatim | If you use a technical term that also has a comm… | `2-4-i-don-t-define-x-as-you--6cf055` |
| `2-4-i-don-t-define-x-as-you--6cf055.t1` | — | 无仓内证据 | 模板 | [承认+定义] Although [construct] is often used loose… | `2-4-i-don-t-define-x-as-you--6cf055` |
| `2-4-i-don-t-define-x-as-you--6cf055.t2` | — | 无仓内证据 | 模板 | [次级论证] This definition is preferable to [alterna… | `2-4-i-don-t-define-x-as-you--6cf055` |
| `4-booth-9-5-f02af3.a` | — | 无仓内证据 | verbatim | While some organizations, such as the US Prevent… | `4-booth-9-5-f02af3` |
| `4-booth-9-5-f02af3.b` | — | 无仓内证据 | verbatim | We recognize that routine PSA screenings have re… | `4-booth-9-5-f02af3` |
| `5-rogerian-g-l-2017-ch04-feb285.t1` | — | 无仓内证据 | 模板 | [Theory X] offers a coherent account of [phenome… | `5-rogerian-g-l-2017-ch04-feb285` |
| `5-rogerian-g-l-2017-ch04-feb285.t2` | — | 无仓内证据 | 模板 | To be sure, [view] holds when [conditions] ([cit… | `5-rogerian-g-l-2017-ch04-feb285` |
| `5-rogerian-g-l-2017-ch04-feb285.t3` | — | 无仓内证据 | 模板 | We share with this literature the premise that [… | `5-rogerian-g-l-2017-ch04-feb285` |
| `5-rogerian-g-l-2017-ch04-feb285.t4` | — | 无仓内证据 | 模板 | Building on this shared premise, we propose [sol… | `5-rogerian-g-l-2017-ch04-feb285` |
| `matrix-1` | — | matrix硬编码 | 模板 | [Theory X] offers a coherent account of [phenome… | `5. Rogerian 四步对话结构（高威胁异议的降防御序列，G&L 2017 Ch04）` |
| `matrix-2` | — | matrix硬编码 | 模板 | To be sure, [view] holds when [conditions] ([cit… | `5. Rogerian 四步对话结构（高威胁异议的降防御序列，G&L 2017 Ch04）` |
| `matrix-3` | — | matrix硬编码 | 模板 | We share with this literature the premise that [… | `5. Rogerian 四步对话结构（高威胁异议的降防御序列，G&L 2017 Ch04）` |
| `matrix-4` | — | matrix硬编码 | 模板 | Building on this shared premise, we propose [sol… | `5. Rogerian 四步对话结构（高威胁异议的降防御序列，G&L 2017 Ch04）` |

### sentences/closure.md（23 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-fc7d9fc1.t1` | — | 无仓内证据 | 模板 | "Taken together, our theory posits that [一句话总结核心… | `cjk-fc7d9fc1` |
| `cjk-2bee3578.t1` | — | 无仓内证据 | 模板 | "In summary, these arguments suggest that [core … | `cjk-2bee3578` |
| `cjk-2bee3578.t2` | — | 无仓内证据 | 模板 | "In sum, [moderator] systematically [strengthens… | `cjk-2bee3578` |
| `cjk-2bee3578.t3` | — | 无仓内证据 | 模板 | "Our theory posited a [结构描述] framework comprisin… | `cjk-2bee3578` |
| `track-level-local-closure-d4743f.t1` | — | 无仓内证据 | 模板 | "In summary, [core mechanism of Track A] reduces… | `track-level-local-closure-d4743f` |
| `cjk-77730704.t1` | — | 无仓内证据 | 模板 | "Taken together, this suggests that [summary mec… | `cjk-77730704` |
| `cjk-2a032c5a.t1` | — | 无仓内证据 | 模板 | In sum, because [X] [mechanism summary], [X] sho… | `cjk-2a032c5a` |
| `cjk-2a032c5a.t2` | — | 无仓内证据 | 模板 | Taken together, the [enhancing/buffering] role o… | `cjk-2a032c5a` |
| `cjk-2a032c5a.t3` | — | 无仓内证据 | 模板 | These arguments suggest a mediated relationship:… | `cjk-2a032c5a` |
| `cjk-2a032c5a.t4` | — | 无仓内证据 | 模板 | The differential effects of [X1] and [X2] on [Y]… | `cjk-2a032c5a` |
| `cjk-2a032c5a.t5` | — | 无仓内证据 | 模板 | Given these competing arguments, we put forth th… | `cjk-2a032c5a` |
| `wowak-2020-female-directors--e2892d.a` | — | 无仓内证据 | verbatim | Taken together, these arguments bring us to the … | `wowak-2020-female-directors--e2892d` |
| `cjk-ba2a6a07.t1` | — | 无仓内证据 | 模板 | "Taken together, our 2×2 framework reveals a [di… | `cjk-ba2a6a07` |
| `cjk-ba2a6a07.t2` | — | 无仓内证据 | 模板 | "Taken together, our Y-shaped framework suggests… | `cjk-ba2a6a07` |
| `u-95e42d.a` | — | 无仓内证据 | verbatim | Hypothesis 2 (H2) Repeated alliance ties between… | `u-95e42d` |
| `u-95e42d.b` | — | 无仓内证据 | verbatim | Hypothesis 3 (H3) A firm's relative centrality v… | `u-95e42d` |
| `u-95e42d.t1` | — | 无仓内证据 | 模板 | "Taken together, as [moderator] between [actor] … | `u-95e42d` |
| `u-95e42d.t2` | — | 无仓内证据 | 模板 | "Taken together, [incentive] is enhanced at low … | `u-95e42d` |
| `matrix-1` | — | matrix硬编码 | 模板 | In sum, because [X] [mechanism summary], [X] sho… | `段落收束→假设过渡（按论证类型）` |
| `matrix-2` | — | matrix硬编码 | 模板 | Taken together, the [enhancing/buffering] role o… | `段落收束→假设过渡（按论证类型）` |
| `matrix-3` | — | matrix硬编码 | 模板 | These arguments suggest a mediated relationship:… | `段落收束→假设过渡（按论证类型）` |
| `matrix-4` | — | matrix硬编码 | 模板 | The differential effects of [X1] and [X2] on [Y]… | `段落收束→假设过渡（按论证类型）` |
| `matrix-5` | — | matrix硬编码 | 模板 | Given these competing arguments, we put forth th… | `段落收束→假设过渡（按论证类型）` |

### sentences/construct_definition.md（21 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `变体-B.a` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | More specifically, it suggests that decision-mak… | `变体-B` |
| `变体-B.t1` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | 模板 | "Although scholars have offered slightly differe… | `变体-B` |
| `变体-C.a` | — | 无仓内证据 | verbatim | This phenomenon—known as a spillover effect—occu… | `变体-C` |
| `变体-C.t1` | — | 无仓内证据 | 模板 | "[Construct] is broadly understood as [definitio… | `变体-C` |
| `变体-E.a` | weng_yang_jms | status待升档 | verbatim | In a recent review, Swigart et al. (2020) sugges… | `变体-E` |
| `变体-E.b` | weng_yang_jms | status待升档 | verbatim | Our study applies the cognitive lens of politica… | `变体-E` |
| `变体-E.t1` | weng_yang_jms | status待升档 | 模板 | "In a recent review, [authors] ([citation]) sugg… | `变体-E` |
| `cjk-98f6d2f0.a` | — | 无仓内证据 | verbatim | Problem severity refers to the seriousness of th… | `cjk-98f6d2f0` |
| `cjk-98f6d2f0.t1` | — | 无仓内证据 | 模板 | "[Construct], [定义/操作化描述] ([文献]), [机制逻辑开头]..." "W… | `cjk-98f6d2f0` |
| `scope-conditions-b4a2b7.t1` | — | 无仓内证据 | 模板 | "This definition applies to [temporal/geographic… | `scope-conditions-b4a2b7` |
| `变体-H.a` | — | 无仓内证据 | verbatim | The growth of digital markets such as app stores… | `变体-H` |
| `变体-H.b` | — | 无仓内证据 | verbatim | In short, digital markets enable hyper-different… | `变体-H` |
| `变体-H.t1` | — | 无仓内证据 | 模板 | [Layer 1 — Context Establishment: Why this conte… | `变体-H` |
| `quintessential-response-vari-b60004.a` | — | 无仓内证据 | verbatim | Because a recall relates to consumer safety and … | `quintessential-response-vari-b60004` |
| `quintessential-response-vari-b60004.t1` | — | 无仓内证据 | 模板 | Because a [trigger] relates to [core stake], we … | `quintessential-response-vari-b60004` |
| `句式-N.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | Pluralistic ignorance is typically defined at th… | `句式-N` |
| `句式-N.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | in part because the biases of individual group m… | `句式-N` |
| `句式-N.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | [Construct] is typically defined at the [group] … | `句式-N` |
| `fini-2017-t1-t3-f07e92.a` | fini_jourdan_perkmann_2017_amj | status待升档 | verbatim | We argue that such indices generally provide two… | `fini-2017-t1-t3-f07e92` |
| `fini-2017-t1-t3-f07e92.t1` | fini_jourdan_perkmann_2017_amj | status待升档 | 模板 | [Signal] generally provides two types of informa… | `fini-2017-t1-t3-f07e92` |
| `matrix-1` | — | matrix硬编码 | 模板 | In sum, [A] prioritize [X]; [B] prioritize [Y] | `变体 I：Framework-Anchored 双构念区分（han_pollock_paruchuri 型）` |

### sentences/cost_benefit_calculus.md（13 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `iv-liuliuluo2016-363a00.a` | Liu_Liu_Luo_2016_JM | status待升档 | verbatim | We first discuss two basic recall characteristic… | `iv-liuliuluo2016-363a00` |
| `iv-liuliuluo2016-363a00.t1` | Liu_Liu_Luo_2016_JM | status待升档 | 模板 | We first discuss two basic [event] characteristi… | `iv-liuliuluo2016-363a00` |
| `cjk-5acd22ab.t1` | chung_low_rust_2022_jams | status待升档 | 模板 | [Actors] high in [IV] see any drop in [metric] d… | `cjk-5acd22ab` |
| `cjk-5acd22ab.t2` | chung_low_rust_2022_jams | status待升档 | 模板 | Because high-[IV] [actors] are [bullish/optimist… | `cjk-5acd22ab` |
| `cjk-5acd22ab.t3` | chung_low_rust_2022_jams | status待升档 | 模板 | High-[IV] [actors] are inclined to believe that … | `cjk-5acd22ab` |
| `cjk-a977ac02.t1` | chung_low_rust_2022_jams | status待升档 | 模板 | Although the long-term value loss that comes wit… | `cjk-a977ac02` |
| `cjk-a977ac02.t2` | chung_low_rust_2022_jams | status待升档 | 模板 | High-[IV] [actors] tend to believe that any dete… | `cjk-a977ac02` |
| `cjk-a977ac02.t3` | chung_low_rust_2022_jams | status待升档 | 模板 | Because high-[IV] [actors] discount the likeliho… | `cjk-a977ac02` |
| `cjk-f9527efe.t1` | chung_low_rust_2022_jams | status待升档 | 模板 | Overall, we expect the perceived higher benefits… | `cjk-f9527efe` |
| `cjk-f9527efe.t2` | chung_low_rust_2022_jams | status待升档 | 模板 | In sum, when [actor] simultaneously views [actio… | `cjk-f9527efe` |
| `cjk-f9527efe.t3` | chung_low_rust_2022_jams | status待升档 | 模板 | Taken together, these arguments suggest that [IV… | `cjk-f9527efe` |
| `tmt-8e4781.t1` | chung_low_rust_2022_jams | status待升档 | 模板 | In contrast to [higher_actor], [lower_actor] fac… | `tmt-8e4781` |
| `tmt-8e4781.t2` | chung_low_rust_2022_jams | status待升档 | 模板 | Whereas [higher_actor] can capture [stock-based_… | `tmt-8e4781` |

### sentences/hypothesis_forms.md（103 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `1-cc7b55.t1` | — | 脚手架节 | 模板 | [Group A] will have [higher/lower] [Y] than [Gro… | `1-cc7b55` |
| `1-cc7b55.t2` | — | 脚手架节 | 模板 | The [greater/lesser] the [X], the [greater/lesse… | `1-cc7b55` |
| `1-cc7b55.t3` | — | 脚手架节 | 模板 | [X] has a [positive-then-negative / negative-the… | `1-cc7b55` |
| `1-cc7b55.t4` | — | 脚手架节 | 模板 | [X] is positively related to [Y], but at a decre… | `1-cc7b55` |
| `1-cc7b55.t5` | — | 脚手架节 | 模板 | [X] will have a [greater/lesser] effect on [Y] f… | `1-cc7b55` |
| `1-cc7b55.t6` | — | 脚手架节 | 模板 | [X1] will have a [greater/lesser] effect on [Y] … | `1-cc7b55` |
| `2-35951b.t1` | — | 无仓内证据 | 模板 | The [positive/negative] effect of [X] on [Y] is … | `2-35951b` |
| `2-35951b.t2` | — | 无仓内证据 | 模板 | The [positive/negative] effect of [X] on [Y] is … | `2-35951b` |
| `2-35951b.t3` | — | 无仓内证据 | 模板 | Although [X] and [Z] each [positively/negatively… | `2-35951b` |
| `2-35951b.t4` | — | 无仓内证据 | 模板 | [X] is [positively/negatively] related to [Y] fo… | `2-35951b` |
| `2-35951b.t5` | — | 无仓内证据 | 模板 | [X] is positively related to [Y] for [A], but ne… | `2-35951b` |
| `2-35951b.t6` | — | 无仓内证据 | 模板 | The [strength/correlation] of the [X]–[Y] relati… | `2-35951b` |
| `3-588118.t1` | — | 无仓内证据 | 模板 | becomes positive once [X] exceeds [threshold] | `3-588118` |
| `3-588118.t2` | — | 无仓内证据 | 模板 | Given [condition], [prediction] | `3-588118` |
| `cjk-5fe946eb.t1` | — | 无仓内证据 | 模板 | If [condition], then [outcome]. | `cjk-5fe946eb` |
| `cjk-5fe946eb.t2` | — | 无仓内证据 | 模板 | The [greater/lesser] the [X], the [greater/lesse… | `cjk-5fe946eb` |
| `cjk-9d5232fe.t1` | — | 无仓内证据 | 模板 | [X] will have a [greater/lesser] effect on [Y] f… | `cjk-9d5232fe` |
| `cjk-9d5232fe.t2` | — | 无仓内证据 | 模板 | [X1] will have a [greater/lesser] effect on [Y] … | `cjk-9d5232fe` |
| `cjk-9d5232fe.t3` | — | 无仓内证据 | 模板 | [Strategy A] is more [negatively/positively] rel… | `cjk-9d5232fe` |
| `句式-D.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | (b) this relationship will be mediated by a grea… | `句式-D` |
| `句式-D.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | (b) this interaction will be mediated by a reduc… | `句式-D` |
| `句式-D.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | Hypothesis N: (a) When [baseline], the greater [… | `句式-D` |
| `句式-E.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | the less outside directors have expressed their … | `句式-E` |
| `句式-E.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | Hypothesis N: When [baseline condition], the les… | `句式-E` |
| `变体-A.t1` | — | 无仓内证据 | 模板 | We expect that [treatment event] in [unit] is li… | `变体-A` |
| `句式-F.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | Here, we assume a non-linear relationship betwee… | `句式-F` |
| `句式-F.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | This assumption is consistent with theory and re… | `句式-F` |
| `句式-F.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | Here, we assume a [non-linear] relationship betw… | `句式-F` |
| `conditional-given-hypothesis-2e9833.t1` | — | 无仓内证据 | 模板 | Given [condition], [prediction]. | `conditional-given-hypothesis-2e9833` |
| `conditional-given-hypothesis-2e9833.t2` | — | 无仓内证据 | 模板 | Given [condition A], [prediction about B]. | `conditional-given-hypothesis-2e9833` |
| `conditional-given-hypothesis-2e9833.t3` | — | 无仓内证据 | 模板 | Given [condition B], [prediction about A]. | `conditional-given-hypothesis-2e9833` |
| `cjk-df240637.t1` | — | 无仓内证据 | 模板 | H[N]. [IV] is [positively/negatively] related to… | `cjk-df240637` |
| `cjk-df240637.t2` | — | 无仓内证据 | 模板 | H[N]. [Mediator] mediates the [positive/negative… | `cjk-df240637` |
| `cjk-df240637.t3` | — | 无仓内证据 | 模板 | H[N]. This prediction is formally equivalent to … | `cjk-df240637` |
| `cjk-df240637.t4` | — | 无仓内证据 | 模板 | H[N]. [IV] is [positively/negatively] related to… | `cjk-df240637` |
| `cjk-df240637.t5` | — | 无仓内证据 | 模板 | H[N]. [Group A / high-X actors] exhibit [directi… | `cjk-df240637` |
| `cjk-42536e43.a` | darby_2023_msom | status待升档 | verbatim | H3: The higher a brand's diversification, the st… | `cjk-42536e43` |
| `cjk-42536e43.b` | darby_2023_msom | status待升档 | verbatim | The recall-slowing effect of CEO stock ownership… | `cjk-42536e43` |
| `cjk-42536e43.t1` | darby_2023_msom | status待升档 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `cjk-42536e43` |
| `cjk-42536e43.t2` | darby_2023_msom | status待升档 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `cjk-42536e43` |
| `cjk-42536e43.t3` | darby_2023_msom | status待升档 | 模板 | H[N]. Although [X] and [Z] each [positively/nega… | `cjk-42536e43` |
| `cjk-42536e43.t4` | darby_2023_msom | status待升档 | 模板 | H[N]. [X] is [positively/negatively] related to … | `cjk-42536e43` |
| `cjk-42536e43.t5` | darby_2023_msom | status待升档 | 模板 | H[N]. [X] is positively related to [Y] for [grou… | `cjk-42536e43` |
| `cjk-9d0b2b62.a` | darby_2025_jscm | status待升档 | verbatim | H2. The spillover effect of activist investor st… | `cjk-9d0b2b62` |
| `cjk-9d0b2b62.b` | darby_2025_jscm | status待升档 | verbatim | H3. The spillover effect of activist investor st… | `cjk-9d0b2b62` |
| `cjk-9d0b2b62.t1` | darby_2025_jscm | status待升档 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `cjk-9d0b2b62` |
| `cjk-9d0b2b62.t2` | darby_2025_jscm | status待升档 | 模板 | H[N]. [X] is [positively/negatively] related to … | `cjk-9d0b2b62` |
| `cjk-39237b9e.a` | wowak_2025_ms | status待升档 | verbatim | Hypothesis 1(a). There is a negative relationshi… | `cjk-39237b9e` |
| `cjk-39237b9e.b` | wowak_2025_ms | status待升档 | verbatim | Hypothesis 1(b). There is a positive relationshi… | `cjk-39237b9e` |
| `cjk-39237b9e.t1` | wowak_2025_ms | status待升档 | 模板 | H[N]a: [X] is [negatively/positively] related to… | `cjk-39237b9e` |
| `cjk-39237b9e.t2` | wowak_2025_ms | status待升档 | 模板 | "Given these competing arguments, we put forth t… | `cjk-39237b9e` |
| `nondirectional-competing-mod-200f9c.a` | kalaignanametal2013 | status待升档 | verbatim | Given the presence of equivocal arguments for th… | `nondirectional-competing-mod-200f9c` |
| `nondirectional-competing-mod-200f9c.t1` | kalaignanametal2013 | status待升档 | 模板 | H[N]. The [positive/negative] relationship betwe… | `nondirectional-competing-mod-200f9c` |
| `nondirectional-competing-mod-200f9c.t2` | kalaignanametal2013 | status待升档 | 模板 | "Given the presence of equivocal arguments for t… | `nondirectional-competing-mod-200f9c` |
| `iv-dv-91e054.a` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Hypothesis 1a: The greater a CEO's current optio… | `iv-dv-91e054` |
| `iv-dv-91e054.b` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Hypothesis 2a: The greater a CEO's prospective o… | `iv-dv-91e054` |
| `iv-dv-91e054.c` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Hypothesis 3a: The positive relationship between… | `iv-dv-91e054` |
| `iv-dv-91e054.t1` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | 模板 | H[N]a: [X1] → [Y1] (+). H[N]b: [X1] → [Y2] (+). … | `iv-dv-91e054` |
| `cjk-75e7571b.t1` | — | 无仓内证据 | 模板 | H[N]. The moderating effect of [Z] on the [IV]→[… | `cjk-75e7571b` |
| `parenthetical-opposite-signe-33c254.a` | Liu_Liu_Luo_2016_JM | status待升档 | verbatim | The negative impact of product value on the like… | `parenthetical-opposite-signe-33c254` |
| `parenthetical-opposite-signe-33c254.t1` | Liu_Liu_Luo_2016_JM | status待升档 | 模板 | "The [negative/positive] impact of [X] on the li… | `parenthetical-opposite-signe-33c254` |
| `prose-italic-conditional-pai-bb3e38.t1` | — | 无仓内证据 | 模板 | We therefore hypothesize, Hypothesis [N]. *Given… | `prose-italic-conditional-pai-bb3e38` |
| `prose-numbered-hypothesis-sm-563ad3.t1` | — | 无仓内证据 | 模板 | Hypothesis H[N]. For a [firm type / condition], … | `prose-numbered-hypothesis-sm-563ad3` |
| `matrix-1` | — | matrix硬编码 | 模板 | [Group A] will have [higher/lower] [Y] than [Gro… | `1. 测量尺度 → 基础形式速查表` |
| `matrix-2` | — | matrix硬编码 | 模板 | The [greater/lesser] the [X], the [greater/lesse… | `1. 测量尺度 → 基础形式速查表` |
| `matrix-3` | — | matrix硬编码 | 模板 | [X] has a [positive-then-negative / negative-the… | `1. 测量尺度 → 基础形式速查表` |
| `matrix-4` | — | matrix硬编码 | 模板 | [X] is positively related to [Y], but at a decre… | `1. 测量尺度 → 基础形式速查表` |
| `matrix-5` | — | matrix硬编码 | 模板 | [X] will have a [greater/lesser] effect on [Y] f… | `1. 测量尺度 → 基础形式速查表` |
| `matrix-6` | — | matrix硬编码 | 模板 | [X1] will have a [greater/lesser] effect on [Y] … | `1. 测量尺度 → 基础形式速查表` |
| `matrix-7` | — | matrix硬编码 | 模板 | The [positive/negative] effect of [X] on [Y] is … | `2. 调节效应形式决策表` |
| `matrix-8` | — | matrix硬编码 | 模板 | The [positive/negative] effect of [X] on [Y] is … | `2. 调节效应形式决策表` |
| `matrix-9` | — | matrix硬编码 | 模板 | Although [X] and [Z] each [positively/negatively… | `2. 调节效应形式决策表` |
| `matrix-10` | — | matrix硬编码 | 模板 | [X] is [positively/negatively] related to [Y] fo… | `2. 调节效应形式决策表` |
| `matrix-11` | — | matrix硬编码 | 模板 | [X] is positively related to [Y] for [A], but ne… | `2. 调节效应形式决策表` |
| `matrix-12` | — | matrix硬编码 | 模板 | The [strength/correlation] of the [X]–[Y] relati… | `2. 调节效应形式决策表` |
| `matrix-13` | — | matrix硬编码 | 模板 | becomes positive once [X] exceeds [threshold] | `3. 关系形状与措辞匹配` |
| `matrix-14` | — | matrix硬编码 | 模板 | Given [condition], [prediction] | `3. 关系形状与措辞匹配` |
| `matrix-15` | — | matrix硬编码 | 模板 | If [condition], then [outcome]. | `基础关系` |
| `matrix-16` | — | matrix硬编码 | 模板 | [X] will have a [greater/lesser] effect on [Y] f… | `差异比较` |
| `matrix-17` | — | matrix硬编码 | 模板 | [X1] will have a [greater/lesser] effect on [Y] … | `差异比较` |
| `matrix-18` | — | matrix硬编码 | 模板 | [Strategy A] is more [negatively/positively] rel… | `差异比较` |
| `matrix-19` | — | matrix硬编码 | 模板 | [IV] is negatively related to [DV] | `Comparative Main Effect（比较型主效应；VERIFIED）` |
| `matrix-20` | — | matrix硬编码 | 模板 | H[N]a: The [greater/lesser] the [IV], the [highe… | `配对假设 (Paired Hypotheses a/b Format)` |
| `matrix-21` | — | matrix硬编码 | 模板 | H[N]a: The [positive/negative] relationship betw… | `配对假设 (Paired Hypotheses a/b Format)` |
| `matrix-22` | — | matrix硬编码 | 模板 | Given [condition], [prediction]. | `条件假设 (Conditional "Given..." Hypothesis Format)` |
| `matrix-23` | — | matrix硬编码 | 模板 | Given [condition A], [prediction about B]. | `条件假设 (Conditional "Given..." Hypothesis Format)` |
| `matrix-24` | — | matrix硬编码 | 模板 | Given [condition B], [prediction about A]. | `条件假设 (Conditional "Given..." Hypothesis Format)` |
| `matrix-25` | — | matrix硬编码 | 模板 | H[N]. [IV] is [positively/negatively] related to… | `中介效应` |
| `matrix-26` | — | matrix硬编码 | 模板 | H[N]. [Mediator] mediates the [positive/negative… | `中介效应` |
| `matrix-27` | — | matrix硬编码 | 模板 | H[N]. This prediction is formally equivalent to … | `中介效应` |
| `matrix-28` | — | matrix硬编码 | 模板 | H[N]. [IV] is [positively/negatively] related to… | `中介效应` |
| `matrix-29` | — | matrix硬编码 | 模板 | H[N]. [Group A / high-X actors] exhibit [directi… | `中介效应` |
| `matrix-30` | — | matrix硬编码 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `调节效应` |
| `matrix-31` | — | matrix硬编码 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `调节效应` |
| `matrix-32` | — | matrix硬编码 | 模板 | H[N]. Although [X] and [Z] each [positively/nega… | `调节效应` |
| `matrix-33` | — | matrix硬编码 | 模板 | H[N]. [X] is [positively/negatively] related to … | `调节效应` |
| `matrix-34` | — | matrix硬编码 | 模板 | H[N]. [X] is positively related to [Y] for [grou… | `调节效应` |
| `matrix-35` | — | matrix硬编码 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `分组调节` |
| `matrix-36` | — | matrix硬编码 | 模板 | H[N]. [X] is [positively/negatively] related to … | `分组调节` |
| `matrix-37` | — | matrix硬编码 | 模板 | H[N]a: [X] is [negatively/positively] related to… | `竞争假设` |
| `matrix-38` | — | matrix硬编码 | 模板 | H[N]. The [positive/negative] relationship betwe… | `单一非定向调节（Nondirectional Competing Moderator）` |
| `matrix-39` | — | matrix硬编码 | 模板 | H[N]a: [X1] → [Y1] (+). H[N]b: [X1] → [Y2] (+). … | `矩阵假设（多 IV × 多 DV）` |
| `matrix-40` | — | matrix硬编码 | 模板 | H[N]. The moderating effect of [Z] on the [IV]→[… | `三向交互` |

### sentences/leitmotif-section-opener.md（7 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `darby-2025-65bdd3.a` | darby_2025_jscm | status待升档 | verbatim | At the core of agency theory is the agency probl… | `darby-2025-65bdd3` |
| `darby-2025-65bdd3.b` | darby_2025_jscm | status待升档 | verbatim | Agency theory suggests that characteristics of t… | `darby-2025-65bdd3` |
| `darby-2025-65bdd3.c` | darby_2025_jscm | status待升档 | verbatim | Previous research suggests that the severity of … | `darby-2025-65bdd3` |
| `darby-2025-65bdd3.t1` | darby_2025_jscm | status待升档 | 模板 | "[Core theory] suggests that [characteristic of … | `darby-2025-65bdd3` |
| `句式-A.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | Personal friendship ties. On one level, personal… | `句式-A` |
| `句式-A.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | On one level, there are social risks from expres… | `句式-A` |
| `句式-A.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | [Moderator label]. On one level, [W] between [ac… | `句式-A` |

### sentences/mechanism_chain.md（101 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `why-chain-c0fd96.t1` | — | 无仓内证据 | 模板 | "X affects Y because [mechanism]." → "[First-ord… | `why-chain-c0fd96` |
| `zhou-2017-99b15c.a` | zhou_2017_asq | status待升档 | verbatim | We propose that state ownership should enable fi… | `zhou-2017-99b15c` |
| `zhou-2017-99b15c.t1` | zhou_2017_asq | status待升档 | 模板 | [Outcome] often requires substantial resources, … | `zhou-2017-99b15c` |
| `zhou-2017-bd5759.a` | zhou_2017_asq | status待升档 | verbatim | Shareholders of private firms may not always suc… | `zhou-2017-bd5759` |
| `zhou-2017-bd5759.b` | zhou_2017_asq | status待升档 | verbatim | Second, in many emerging economies, politicians … | `zhou-2017-bd5759` |
| `zhou-2017-bd5759.t1` | zhou_2017_asq | status待升档 | 模板 | [Actors] in [alternative setting] may not always… | `zhou-2017-bd5759` |
| `cjk-2f9c895e.a` | — | 无仓内证据 | verbatim | As the ownership stakes of activist investors in… | `cjk-2f9c895e` |
| `cjk-2f9c895e.t1` | — | 无仓内证据 | 模板 | "When [IV condition holds], [first-order consequ… | `cjk-2f9c895e` |
| `cjk-c0554a38.a` | keeves_2017_asq | status待升档 | verbatim | Thus our final hypothesis posits that feelings o… | `cjk-c0554a38` |
| `cjk-c0554a38.b` | keeves_2017_asq | status待升档 | verbatim | This prediction is formally equivalent to hypoth… | `cjk-c0554a38` |
| `cjk-c0554a38.t1` | keeves_2017_asq | status待升档 | 模板 | "When [IV condition holds], [first-order consequ… | `cjk-c0554a38` |
| `track-a-track-b-2d739f.a` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | In summary, high prospective wealth reduces CEOs… | `track-a-track-b-2d739f` |
| `track-a-track-b-2d739f.b` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Hypothesis 2a: The greater a CEO's prospective o… | `track-a-track-b-2d739f` |
| `track-a-track-b-2d739f.t1` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | 模板 | "[X_A] reflects '[定义]' ([文献]). However, this [状态… | `track-a-track-b-2d739f` |
| `track-a-track-b-2d739f.t2` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | 模板 | "[X_B] reflects '[定义]' ([文献]). [高X_B主体] are orie… | `track-a-track-b-2d739f` |
| `dialectical-opposing-indirec-0466cf.t1` | — | 无仓内证据 | 模板 | [Theory] suggests that [IV] potentially affects … | `dialectical-opposing-indirec-0466cf` |
| `dialectical-opposing-indirec-0466cf.t2` | — | 无仓内证据 | 模板 | All [N] focus groups participants acknowledged [… | `dialectical-opposing-indirec-0466cf` |
| `group-based-dual-track-for-m-7eda32.a` | — | 无仓内证据 | verbatim | Organizations that censor employees for prejudic… | `group-based-dual-track-for-m-7eda32` |
| `group-based-dual-track-for-m-7eda32.b` | — | 无仓内证据 | verbatim | We theorize that censorship of employees who pos… | `group-based-dual-track-for-m-7eda32` |
| `group-based-dual-track-for-m-7eda32.t1` | — | 无仓内证据 | 模板 | We theorize that [IV] differentially influences … | `group-based-dual-track-for-m-7eda32` |
| `a-vs-b-69b7c1.a` | wowak_2025_ms | status待升档 | verbatim | However, the literatures on recalls and politica… | `a-vs-b-69b7c1` |
| `a-vs-b-69b7c1.b` | wowak_2025_ms | status待升档 | verbatim | On the other hand, firms with more conservative … | `a-vs-b-69b7c1` |
| `a-vs-b-69b7c1.c` | wowak_2025_ms | status待升档 | verbatim | Given these competing arguments, we put forth th… | `a-vs-b-69b7c1` |
| `a-vs-b-69b7c1.t1` | wowak_2025_ms | status待升档 | 模板 | "However, the literatures on [领域A] and [领域B] off… | `a-vs-b-69b7c1` |
| `a-vs-b-69b7c1.t2` | wowak_2025_ms | status待升档 | 模板 | "On the one hand, [X_high] may [increase/decreas… | `a-vs-b-69b7c1` |
| `a-vs-b-69b7c1.t3` | wowak_2025_ms | status待升档 | 模板 | "On the other hand, [X_low] may [increase/decrea… | `a-vs-b-69b7c1` |
| `cjk-9f49b6dd.t1` | — | 无仓内证据 | 模板 | "To illustrate, consider [主体] holding [具体参数]. A … | `cjk-9f49b6dd` |
| `width-over-depth-three-paral-35b623.a` | gamache_etal_2020_smj | status待升档 | verbatim | Therefore, when CEOs with a high prevention focu… | `width-over-depth-three-paral-35b623` |
| `width-over-depth-three-paral-35b623.b` | gamache_etal_2020_smj | status待升档 | verbatim | Additionally, people high in prevention focus ha… | `width-over-depth-three-paral-35b623` |
| `width-over-depth-three-paral-35b623.c` | gamache_etal_2020_smj | status待升档 | verbatim | Finally, a prevention focus is associated with a… | `width-over-depth-three-paral-35b623` |
| `width-over-depth-three-paral-35b623.t1` | gamache_etal_2020_smj | status待升档 | 模板 | Applying [theory] to [empirical domain], we [fir… | `width-over-depth-three-paral-35b623` |
| `cjk-31e53569.t1` | — | 无仓内证据 | 模板 | "[Research stream] has shown that [specific mech… | `cjk-31e53569` |
| `dual-theory-architecture-variant-mayo-et.a` | mayo_ball_mills_2022_pom | status待升档 | verbatim | We leverage attribution theory to help explain t… | `dual-theory-architecture-variant-mayo-et` |
| `dv-kalaignanam2017-4fe554.t1` | kalaignanam_2017_jm | status待升档 | 模板 | There are two streams of research pertinent to u… | `dv-kalaignanam2017-4fe554` |
| `dv-kalaignanam2017-4fe554.t2` | kalaignanam_2017_jm | status待升档 | 模板 | The second relevant stream of research for under… | `dv-kalaignanam2017-4fe554` |
| `ability-motivation-eilert-20-bde4c8.a` | eilert_2017_jm | status待升档 | verbatim | The ability of the firm to provide a quick respo… | `ability-motivation-eilert-20-bde4c8` |
| `ability-motivation-eilert-20-bde4c8.b` | eilert_2017_jm | status待升档 | verbatim | Research has also shown that stakeholders are mo… | `ability-motivation-eilert-20-bde4c8` |
| `ability-motivation-eilert-20-bde4c8.t1` | eilert_2017_jm | status待升档 | 模板 | We expect [IV] to be related to [DV] because of … | `ability-motivation-eilert-20-bde4c8` |
| `alternative-mechanisms-9d92fe.a` | — | 无仓内证据 | verbatim | While we propose that perceived self-control is … | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.b` | — | 无仓内证据 | verbatim | A final alternative mechanism is dominance. Wome… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.c` | — | 无仓内证据 | verbatim | While the three mechanisms discussed above are p… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.t1` | — | 无仓内证据 | 模板 | "While we propose that [mediator] is a primary m… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.t2` | — | 无仓内证据 | 模板 | "[Alternative M1]. When [condition], they may be… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.t3` | — | 无仓内证据 | 模板 | "[Alternative M2] is another potential mechanism… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.t4` | — | 无仓内证据 | 模板 | "A final alternative mechanism is [Alternative M… | `alternative-mechanisms-9d92fe` |
| `alternative-mechanisms-9d92fe.t5` | — | 无仓内证据 | 模板 | "While the [N] mechanisms discussed above are pl… | `alternative-mechanisms-9d92fe` |
| `multi-theory-integration-6bba3f.a` | — | 无仓内证据 | verbatim | To understand the expectations that observers ha… | `multi-theory-integration-6bba3f` |
| `multi-theory-integration-6bba3f.b` | — | 无仓内证据 | verbatim | Moreover, we draw on expectancy violation theory… | `multi-theory-integration-6bba3f` |
| `multi-theory-integration-6bba3f.t1` | — | 无仓内证据 | 模板 | "To understand [phenomenon], we draw on [N] type… | `multi-theory-integration-6bba3f` |
| `multi-theory-integration-6bba3f.t2` | — | 无仓内证据 | 模板 | "Moreover, we draw on [理论C] to understand why [前… | `multi-theory-integration-6bba3f` |
| `om-shen-et-al-jom-de1772.a` | — | 无仓内证据 | verbatim | We suggest that political ties may inhibit opera… | `om-shen-et-al-jom-de1772` |
| `om-shen-et-al-jom-de1772.b` | — | 无仓内证据 | verbatim | Second, the resource benefits of political ties … | `om-shen-et-al-jom-de1772` |
| `om-shen-et-al-jom-de1772.t1` | — | 无仓内证据 | 模板 | "We suggest that [IV] may [direction] [DV] for t… | `om-shen-et-al-jom-de1772` |
| `变体-A.a` | — | 无仓内证据 | verbatim | Our central thesis is that the recognition of ID… | `变体-A` |
| `变体-A.t1` | — | 无仓内证据 | 模板 | [Shock] changes the attentional landscape for [a… | `变体-A` |
| `double-edged-sword-f386c8.a` | — | 无仓内证据 | verbatim | According to the political embeddedness perspect… | `double-edged-sword-f386c8` |
| `double-edged-sword-f386c8.b` | — | 无仓内证据 | verbatim | However, the political embeddedness perspective … | `double-edged-sword-f386c8` |
| `double-edged-sword-f386c8.c` | — | 无仓内证据 | verbatim | Although earlier studies have indicated various … | `double-edged-sword-f386c8` |
| `double-edged-sword-f386c8.t1` | — | 无仓内证据 | 模板 | "According to the [theoretical lens], [IV] can b… | `double-edged-sword-f386c8` |
| `double-edged-sword-f386c8.t2` | — | 无仓内证据 | 模板 | "However, the [theoretical lens] also suggests t… | `double-edged-sword-f386c8` |
| `double-edged-sword-f386c8.t3` | — | 无仓内证据 | 模板 | "Although earlier studies have indicated various… | `double-edged-sword-f386c8` |
| `macro-meso-micro-layered-mec-d6f2d2.a` | park_lange_jeon_smj | status待升档 | verbatim | Shareholder litigation risk can function as a go… | `macro-meso-micro-layered-mec-d6f2d2` |
| `macro-meso-micro-layered-mec-d6f2d2.b` | park_lange_jeon_smj | status待升档 | verbatim | However, much like other types of governance mec… | `macro-meso-micro-layered-mec-d6f2d2` |
| `macro-meso-micro-layered-mec-d6f2d2.c` | park_lange_jeon_smj | status待升档 | verbatim | We make that prediction recognizing that differe… | `macro-meso-micro-layered-mec-d6f2d2` |
| `macro-meso-micro-layered-mec-d6f2d2.t1` | park_lange_jeon_smj | status待升档 | 模板 | [Section 2.1: Governance/Institutional Mechanism… | `macro-meso-micro-layered-mec-d6f2d2` |
| `dual-perspective-contrast-fr-7ba053.a` | singh_grewal_2023_jmr | status待升档 | verbatim | Our conceptual foundation resonates with efficie… | `dual-perspective-contrast-fr-7ba053` |
| `dual-perspective-contrast-fr-7ba053.t1` | singh_grewal_2023_jmr | status待升档 | 模板 | Our conceptual foundation resonates with [perspe… | `dual-perspective-contrast-fr-7ba053` |
| `nested-extension-t2-architec-6f3988.a` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Grounded in classical agency theory, stock-optio… | `nested-extension-t2-architec-6f3988` |
| `nested-extension-t2-architec-6f3988.b` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | The BAM, introduced by Wiseman and Gomez-Mejia (… | `nested-extension-t2-architec-6f3988` |
| `nested-extension-t2-architec-6f3988.c` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | verbatim | Extending the BAM (DesJardine and Shi 2021; Mart… | `nested-extension-t2-architec-6f3988` |
| `nested-extension-t2-architec-6f3988.t1` | malik_wang_martin_gomez_mejia_2025_jm | status待升档 | 模板 | Grounded in [classical theory], [practice/phenom… | `nested-extension-t2-architec-6f3988` |
| `symmetric-opposing-dual-trac-3118eb.a` | — | 无仓内证据 | verbatim | Taken together, we expect that high overall diss… | `symmetric-opposing-dual-trac-3118eb` |
| `symmetric-opposing-dual-trac-3118eb.b` | — | 无仓内证据 | verbatim | In sum, we expect high evaluation heterogeneity … | `symmetric-opposing-dual-trac-3118eb` |
| `symmetric-opposing-dual-trac-3118eb.t1` | — | 无仓内证据 | 模板 | ##### [IV Dimension 1] and [DV 1] [IV dimension … | `symmetric-opposing-dual-trac-3118eb` |
| `2-2-cell-by-cell-2-2-moderat-167b29.a` | — | 无仓内证据 | verbatim | In contrast to its effect on reputation, low-lev… | `2-2-cell-by-cell-2-2-moderat-167b29` |
| `2-2-cell-by-cell-2-2-moderat-167b29.b` | — | 无仓内证据 | verbatim | Hypothesis 2. The positive relationship between … | `2-2-cell-by-cell-2-2-moderat-167b29` |
| `2-2-cell-by-cell-2-2-moderat-167b29.c` | — | 无仓内证据 | verbatim | In contrast, we expect availability cascades to … | `2-2-cell-by-cell-2-2-moderat-167b29` |
| `2-2-cell-by-cell-2-2-moderat-167b29.t1` | — | 无仓内证据 | 模板 | [Common Mechanism Preamble for Moderator A]: [Th… | `2-2-cell-by-cell-2-2-moderat-167b29` |
| `after-not-before-kalaignanam-d77e27.a` | kalaignanametal2013 | status待升档 | verbatim | Why do firms improve reliability after product r… | `after-not-before-kalaignanam-d77e27` |
| `after-not-before-kalaignanam-d77e27.t1` | kalaignanametal2013 | status待升档 | 模板 | Why do [actors] improve [process outcome M] afte… | `after-not-before-kalaignanam-d77e27` |
| `joint-necessity-gate-and-gat-5a34b8.t1` | — | 无仓内证据 | 模板 | [Condition A] alone is not sufficient. [Explanat… | `joint-necessity-gate-and-gat-5a34b8` |
| `cognitive-availability-durat-da6892.a` | paruchuri_pollock_kumar_2019_smj | status待升档 | verbatim | We also argue that reputation spillover effects … | `cognitive-availability-durat-da6892` |
| `cognitive-availability-durat-da6892.b` | paruchuri_pollock_kumar_2019_smj | status待升档 | verbatim | Extreme and frequently occurring stimuli tend to… | `cognitive-availability-durat-da6892` |
| `cognitive-availability-durat-da6892.c` | paruchuri_pollock_kumar_2019_smj | status待升档 | verbatim | However, since reputations need to be continuall… | `cognitive-availability-durat-da6892` |
| `cognitive-availability-durat-da6892.t1` | paruchuri_pollock_kumar_2019_smj | status待升档 | 模板 | We also argue that [outcome] effects will only p… | `cognitive-availability-durat-da6892` |
| `句式-B.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | a 'spiral of silence' can ensue (Noelle-Neumann,… | `句式-B` |
| `句式-B.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | A '[labeled spiral]' can ensue ([citation]) wher… | `句式-B` |
| `句式-C.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | before voicing their opinion they will tend to l… | `句式-C` |
| `句式-C.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | If other group members follow the same decision … | `句式-C` |
| `句式-C.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | [Individuals] will tend to [withhold the action]… | `句式-C` |
| `cost-benefit-calculus-mechan-9cc44b.a` | chung_low_rust_2022_jams | status待升档 | verbatim | Overall, we expect the perceived higher benefits… | `cost-benefit-calculus-mechan-9cc44b` |
| `cost-benefit-calculus-mechan-9cc44b.t1` | chung_low_rust_2022_jams | status待升档 | 模板 | [建立权衡] [Actors] have to weigh the benefits of [a… | `cost-benefit-calculus-mechan-9cc44b` |
| `cost-benefit-calculus-mechan-9cc44b.t2` | chung_low_rust_2022_jams | status待升档 | 模板 | In contrast to [higher_actor], [lower_actor] fac… | `cost-benefit-calculus-mechan-9cc44b` |
| `u-awareness-capacity-mutual--b1cab3.a` | — | 无仓内证据 | verbatim | First, increases in the proportion of explorator… | `u-awareness-capacity-mutual--b1cab3` |
| `u-awareness-capacity-mutual--b1cab3.b` | — | 无仓内证据 | verbatim | However, as the proportion of exploratory allian… | `u-awareness-capacity-mutual--b1cab3` |
| `u-awareness-capacity-mutual--b1cab3.t1` | — | 无仓内证据 | 模板 | Different compositions of [IV] have different im… | `u-awareness-capacity-mutual--b1cab3` |
| `u-awareness-capacity-mutual--b1cab3.t2` | — | 无仓内证据 | 模板 | In sum, firms are likely to develop [state A] wh… | `u-awareness-capacity-mutual--b1cab3` |
| `threat-processing-cascade-ri-519583.a` | ridge_hill_ingram_kolomeitsev_worrell_2024_amj | status待升档 | verbatim | hyper-vigilance, with individuals higher in para… | `threat-processing-cascade-ri-519583` |
| `threat-processing-cascade-ri-519583.b` | ridge_hill_ingram_kolomeitsev_worrell_2024_amj | status待升档 | verbatim | disproportionately believe that external entitie… | `threat-processing-cascade-ri-519583` |
| `threat-processing-cascade-ri-519583.c` | ridge_hill_ingram_kolomeitsev_worrell_2024_amj | status待升档 | verbatim | paranoia tends to be associated strongly with sa… | `threat-processing-cascade-ri-519583` |
| `threat-processing-cascade-ri-519583.t1` | ridge_hill_ingram_kolomeitsev_worrell_2024_amj | status待升档 | 模板 | [Trait 感知基底] Individuals higher in [trait] are [… | `threat-processing-cascade-ri-519583` |

### sentences/moderation.md（29 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `buffering-ae5bcf.a` | — | 无仓内证据 | verbatim | H2: The higher a brand's reliability, the weaker… | `buffering-ae5bcf` |
| `buffering-ae5bcf.t1` | — | 无仓内证据 | 模板 | "The [positive/negative] effect of [X] on [Y] is… | `buffering-ae5bcf` |
| `enhancing-959761.a` | — | 无仓内证据 | verbatim | H3: The higher a brand's diversification, the st… | `enhancing-959761` |
| `enhancing-959761.b` | — | 无仓内证据 | verbatim | Because of the short- versus long-term orientati… | `enhancing-959761` |
| `enhancing-959761.t1` | — | 无仓内证据 | 模板 | "The [positive/negative] effect of [X] on [Y] is… | `enhancing-959761` |
| `enhancing-959761.t2` | — | 无仓内证据 | 模板 | "Because of the short- versus long-term orientat… | `enhancing-959761` |
| `antagonistic-86d8ec.t1` | — | 无仓内证据 | 模板 | "Although [X] and [Z] each [positively/negativel… | `antagonistic-86d8ec` |
| `cjk-cdeee901.t1` | — | 无仓内证据 | 模板 | "We theorize [Z] as moderating the [X]→[Y] relat… | `cjk-cdeee901` |
| `fit-misfit-weng-yang-638122.a` | weng_yang_jms | status待升档 | verbatim | In our context, this means that the 'ideological… | `fit-misfit-weng-yang-638122` |
| `fit-misfit-weng-yang-638122.b` | weng_yang_jms | status待升档 | verbatim | In other words, the 'ideological misfit' between… | `fit-misfit-weng-yang-638122` |
| `fit-misfit-weng-yang-638122.t1` | weng_yang_jms | status待升档 | 模板 | "The extent to which [moderator characteristic] … | `fit-misfit-weng-yang-638122` |
| `weng-yang-6a6974.a` | weng_yang_jms | status待升档 | verbatim | We postulate that CEO power may alter the effect… | `weng-yang-6a6974` |
| `weng-yang-6a6974.b` | weng_yang_jms | status待升档 | verbatim | Alternatively, with limited power, a CEO, whethe… | `weng-yang-6a6974` |
| `weng-yang-6a6974.t1` | weng_yang_jms | status待升档 | 模板 | "We postulate that [moderator] may alter the eff… | `weng-yang-6a6974` |
| `cjk-12e1b086.a` | Liu_Liu_Luo_2016_JM | status待升档 | verbatim | Based on similar theoretical reasoning, we now e… | `cjk-12e1b086` |
| `cjk-12e1b086.t1` | Liu_Liu_Luo_2016_JM | status待升档 | 模板 | "Z [strengthens/weakens] the [X]→[Y] relationshi… | `cjk-12e1b086` |
| `cjk-9cfb60e0.a` | — | 无仓内证据 | verbatim | H2. The spillover effect of activist investor st… | `cjk-9cfb60e0` |
| `cjk-9cfb60e0.b` | — | 无仓内证据 | verbatim | H3. The spillover effect of activist investor st… | `cjk-9cfb60e0` |
| `cjk-9cfb60e0.t1` | — | 无仓内证据 | 模板 | "For [W=A], [mechanism A]. [Evidence A]. In cont… | `cjk-9cfb60e0` |
| `变体-A.t1` | — | 无仓内证据 | 模板 | The salience of [action] as an instrument to [go… | `变体-A` |
| `more-positive-more-negative--4f02ef.t1` | — | 无仓内证据 | 模板 | "The impact of [X] on [Y] will be more positive … | `more-positive-more-negative--4f02ef` |
| `more-positive-more-negative--4f02ef.t2` | — | 无仓内证据 | 模板 | "The impact of [X] on [Y] will be more negative … | `more-positive-more-negative--4f02ef` |
| `more-positive-more-negative--4f02ef.t3` | — | 无仓内证据 | 模板 | "### The enhancing effect of [X]" "### The hinde… | `more-positive-more-negative--4f02ef` |
| `u-flatten-steepen-bb7a14.a` | — | 无仓内证据 | verbatim | Hypothesis 2 (H2) Repeated alliance ties between… | `u-flatten-steepen-bb7a14` |
| `u-flatten-steepen-bb7a14.b` | — | 无仓内证据 | verbatim | Hypothesis 3 (H3) A firm's relative centrality v… | `u-flatten-steepen-bb7a14` |
| `u-flatten-steepen-bb7a14.t1` | — | 无仓内证据 | 模板 | "The slope in the relationship between [IV] and … | `u-flatten-steepen-bb7a14` |
| `u-flatten-steepen-bb7a14.t2` | — | 无仓内证据 | 模板 | "The slope in the relationship between [IV] and … | `u-flatten-steepen-bb7a14` |
| `mitigation-via-manifestation-125143.t1` | — | 无仓内证据 | 模板 | H[N]: There will be a [positive/negative] intera… | `mitigation-via-manifestation-125143` |
| `mitigation-via-manifestation-125143.t2` | — | 无仓内证据 | 模板 | - vs **Buffering（Eilert 2017）**: buffering 的机制是"… | `mitigation-via-manifestation-125143` |

### subprotocols/argumentation_patterns.md（21 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `a-direct-rejection-gamache-557581.t1` | gamache_etal_2020_smj | status待升档 | 模板 | [Alternative 1] One might intuitively expect tha… | `Pattern: A：Direct Rejection（Gamache 型）` |
| `b-competing-baseline-moderat-1278df.t1` | — | 已标注-status待升 | 模板 | [Competing Baseline] Institutional theory sugges… | `Pattern: B：Competing Baseline → Moderation Resolution（Desai 型）` |
| `audience-foil-then-focal-signal-single-c.a` | — | 已标注-status待升 | verbatim | However, it is likely that the stock market and … | `Pattern: Audience-Foil then Focal-Signal (Single Comparative H)` |
| `audience-foil-then-focal-signal-single-c.t1` | — | 已标注-status待升 | 模板 | [Foil] Prior work suggests [action X] has positi… | `Pattern: Audience-Foil then Focal-Signal (Single Comparative H)` |
| `audience-foil-then-focal-signal-single-c.t2` | — | 已标注-status待升 | 模板 | - 受众切换句 → `../sentences/acknowledgment_response.… | `Pattern: Audience-Foil then Focal-Signal (Single Comparative H)` |
| `a-t3-rival-prediction-rebuttal-moon2026.t1` | — | 无仓内证据 | 模板 | However, it can be argued that [treatment] is li… | `Pattern: A：T3_rival_prediction_rebuttal（moon2026）` |
| `b-counter-prediction-exclusi-3751c2.a` | — | 无仓内证据 | verbatim | One potential response to heightened product com… | `Pattern: B：反预测排除段（Counter-Prediction Exclusion before H1，ball_2018 型）` |
| `b-counter-prediction-exclusi-3751c2.t1` | — | 无仓内证据 | 模板 | One potential response to [IV] may be [opposite-… | `Pattern: B：反预测排除段（Counter-Prediction Exclusion before H1，ball_2018 型）` |
| `decision-rights-preamble-ind-3331aa.a` | — | 无仓内证据 | verbatim | In other words, boards do not make the recall de… | `Pattern: Decision-Rights Preamble → Indirect-Governance Chain（决策权前言→间接治理链）` |
| `decision-rights-preamble-ind-3331aa.t1` | — | 无仓内证据 | 模板 | 四源证据基础声明（文献+监管文件+业界访谈+监管者访谈）→ 决策权链条（谁监测→谁审议→谁建议→… | `Pattern: Decision-Rights Preamble → Indirect-Governance Chain（决策权前言→间接治理链）` |
| `decision-rights-preamble-ind-3331aa.t2` | — | 无仓内证据 | 模板 | To articulate our hypothesized relationships, we… | `Pattern: Decision-Rights Preamble → Indirect-Governance Chain（决策权前言→间接治理链）` |
| `c-westphal-zajac-1998-symbol-0de942.a` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | verbatim | Observing a positive market reaction to agency e… | `Pattern: C：判别式替代解释排除（westphal_zajac_1998_symbolic_management 型）` |
| `c-westphal-zajac-1998-symbol-0de942.t1` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | 模板 | We test whether [audience reactions] to [verbal … | `Pattern: C：判别式替代解释排除（westphal_zajac_1998_symbolic_management 型）` |
| `d-westphal-zajac-1998-symbol-593259.a` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | verbatim | While we do not assume strong-form market effici… | `Pattern: D：两极之间的假设声明段（westphal_zajac_1998_symbolic_management 型）` |
| `d-westphal-zajac-1998-symbol-593259.t1` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | 模板 | While we do not assume [strong-form extreme assu… | `Pattern: D：两极之间的假设声明段（westphal_zajac_1998_symbolic_management 型）` |
| `e-westphal-bednar2005-ed8dda.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | Social cohesion among group members is thought t… | `Pattern: E：同果近邻构念反号辨析型（westphal_bednar2005 型）` |
| `e-westphal-bednar2005-ed8dda.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | With groupthink, groups persist with failing str… | `Pattern: E：同果近邻构念反号辨析型（westphal_bednar2005 型）` |
| `e-westphal-bednar2005-ed8dda.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | The literature ... clearly distinguishes [focal … | `Pattern: E：同果近邻构念反号辨析型（westphal_bednar2005 型）` |
| `f-westphal-bednar2005-312809.a` | westphal_bednar2005 | 已标注-status待升 | verbatim | Though pluralistic ignorance has been observed i… | `Pattern: F：机制前提→情境放大映射型（westphal_bednar2005 型）` |
| `f-westphal-bednar2005-312809.b` | westphal_bednar2005 | 已标注-status待升 | verbatim | At the same time, the traditional board-room con… | `Pattern: F：机制前提→情境放大映射型（westphal_bednar2005 型）` |
| `f-westphal-bednar2005-312809.t1` | westphal_bednar2005 | 已标注-status待升 | 模板 | Though [construct] has been observed in a variet… | `Pattern: F：机制前提→情境放大映射型（westphal_bednar2005 型）` |

### subprotocols/construct_differentiation_patterns.md（1 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `table_construct_differentiation.t1` | Grewal_Vana_Stephen_2025_JM | 已标注-status待升 | 模板 | Among varied perspectives on [domain], [construc… | `table_construct_differentiation` |

### subprotocols/evidence_patterns.md（7 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `three_element_citation_mechanism_anchor.t1` | Singh_Grewal_2023_JMR | 已标注-status待升 | 模板 | [Author] (year) found that [concrete finding] — … | `three_element_citation_mechanism_anchor` |
| `b-audience-reality-warrant-3b8330.t1` | — | 已标注-status待升 | 模板 | [Academic evidence] establishes that [informatio… | `Pattern: B：利益相关者反应作为 Audience-Reality Warrant` |
| `a-interview-non-event-warran-e8a386.a` | — | 无仓内证据 | verbatim | As such, we spoke with a manufacturing manager a… | `Pattern: A：非事件访谈证据（Interview Non-Event Warrant，ball_2018 型）` |
| `a-interview-non-event-warran-e8a386.t1` | — | 无仓内证据 | 模板 | Identifying actual examples of [high-discretion … | `Pattern: A：非事件访谈证据（Interview Non-Event Warrant，ball_2018 型）` |
| `paired-opposite-default-inte-1a848b.a` | — | 无仓内证据 | verbatim | The default at this firm is to recall and to do … | `Pattern: Paired Opposite-Default Interview Vignettes（反向默认对偶访谈轶事）` |
| `paired-opposite-default-inte-1a848b.t1` | — | 无仓内证据 | 模板 | Informant A（决策聚焦客户伤害 + 3 天举证期 + 默认召回）→ 归因上游（"Thi… | `Pattern: Paired Opposite-Default Interview Vignettes（反向默认对偶访谈轶事）` |
| `paired-opposite-default-inte-1a848b.t2` | — | 无仓内证据 | 模板 | The [role A] mentioned that, at [her] firm, the … | `Pattern: Paired Opposite-Default Interview Vignettes（反向默认对偶访谈轶事）` |

### subprotocols/hypothesis_derivation_patterns.md（9 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `dual-channel-convergence-des-0b8c52.a` | — | 已标注-status待升 | verbatim | Influence begins with the discussions that occur… | `Pattern: Dual-Channel Convergence（双通道收敛，DesJardine–Li–Shi 2025 型）` |
| `dual-channel-convergence-des-0b8c52.b` | — | 已标注-status待升 | verbatim | On the other side of the equation, executives of… | `Pattern: Dual-Channel Convergence（双通道收敛，DesJardine–Li–Shi 2025 型）` |
| `dual-channel-convergence-des-0b8c52.c` | — | 已标注-status待升 | verbatim | Importantly, the opacity of the ESG rating proce… | `Pattern: Dual-Channel Convergence（双通道收敛，DesJardine–Li–Shi 2025 型）` |
| `dual-channel-convergence-des-0b8c52.t1` | — | 已标注-status待升 | 模板 | [通道 1：主动施加] Influence begins with the [channel 1… | `Pattern: Dual-Channel Convergence（双通道收敛，DesJardine–Li–Shi 2025 型）` |
| `why-not-reverse-boundary-dec-42a42f.a` | — | 已标注-status待升 | verbatim | There are two related reasons why we do not hypo… | `Pattern: Why-Not Reverse Boundary Declaration（"why not" 反向边界声明，DesJardine–Li–Shi 2025 型）` |
| `why-not-reverse-boundary-dec-42a42f.t1` | — | 已标注-status待升 | 模板 | There are two related reasons why we do not hypo… | `Pattern: Why-Not Reverse Boundary Declaration（"why not" 反向边界声明，DesJardine–Li–Shi 2025 型）` |
| `a-westphal-zajac-1998-symbol-8440c8.a` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | verbatim | By formally adopting 'institutionally | `Pattern: A：符号替代-预防-固权三步机制（westphal_zajac_1998_symbolic_management 型）` |
| `a-westphal-zajac-1998-symbol-8440c8.b` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | verbatim | procedures' (Walsh and Seward, 1990: 431) indica… | `Pattern: A：符号替代-预防-固权三步机制（westphal_zajac_1998_symbolic_management 型）` |
| `a-westphal-zajac-1998-symbol-8440c8.t1` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | 模板 | By using [symbolic action] to reduce [social unc… | `Pattern: A：符号替代-预防-固权三步机制（westphal_zajac_1998_symbolic_management 型）` |

### subprotocols/hypothesis_organization_patterns.md（12 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `dual-role-iv-shared-logic-compressed-t5.a` | — | 已标注-status待升 | verbatim | We then discuss how the CEO's personal interests… | `Pattern: Dual-Role IV → Shared-Logic Compressed T5` |
| `dual-role-iv-shared-logic-compressed-t5.t1` | — | 已标注-status待升 | 模板 | H1–H2 (opposing-force trunk) → H3–H4 (W 独立主效应) →… | `Pattern: Dual-Role IV → Shared-Logic Compressed T5` |
| `dual-role-iv-shared-logic-compressed-t5.t2` | — | 已标注-status待升 | 模板 | We first discuss two basic [event] characteristi… | `Pattern: Dual-Role IV → Shared-Logic Compressed T5` |
| `context-assigned-decision-ma-713f7f.a` | — | 无仓内证据 | verbatim | This distinction underlies our hypotheses, as we… | `Pattern: Context-Assigned Decision-Margin Split（情境分配决策边际拆分）` |
| `context-assigned-decision-ma-713f7f.t1` | — | 无仓内证据 | 模板 | [Margin partition opener] [Outcomes] differ in [… | `Pattern: Context-Assigned Decision-Margin Split（情境分配决策边际拆分）` |
| `a-pivot-westphal-zajac-1998--855535.a` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | verbatim | One important implication of holding such large … | `Pattern: A：受众异质性 pivot 至调节假设（westphal_zajac_1998_symbolic_management 型）` |
| `a-pivot-westphal-zajac-1998--855535.t1` | westphal_zajac_1998_symbolic_management | 已标注-status待升 | 模板 | While our discussion thus far has treated [stake… | `Pattern: A：受众异质性 pivot 至调节假设（westphal_zajac_1998_symbolic_management 型）` |
| `mechanism-matched-dual-path--b18430.a` | — | 无仓内证据 | verbatim | Because TMT change orientation and TMT risk-taki… | `Pattern: Mechanism-Matched Dual-Path → Shared Renewal Trunk（中介配对分流→共享重构主干，what_changes_after_women_enter_top_manage_2020 型）` |
| `mechanism-matched-dual-path--b18430.t1` | — | 无仓内证据 | 模板 | [区分证成段] Because [M1] and [M2] are conceptually d… | `Pattern: Mechanism-Matched Dual-Path → Shared Renewal Trunk（中介配对分流→共享重构主干，what_changes_after_women_enter_top_manage_2020 型）` |
| `response-portfolio-decomposi-3c1898.a` | — | 无仓内证据 | verbatim | the substitute brand can create a portfolio of s… | `Pattern: Response-Portfolio Decomposition（聚合行动 = 对立组件组合）` |
| `response-portfolio-decomposi-3c1898.b` | — | 无仓内证据 | verbatim | Although we cannot directly observe buyers' util… | `Pattern: Response-Portfolio Decomposition（聚合行动 = 对立组件组合）` |
| `response-portfolio-decomposi-3c1898.t1` | — | 无仓内证据 | 模板 | [组件1—机会服务] Increasing [component 1] can [enhance… | `Pattern: Response-Portfolio Decomposition（聚合行动 = 对立组件组合）` |

### subprotocols/moderator_selection_frameworks.md（6 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `environmental_organizational_resource_availability.t1` | Shen_Zhou_Wang_Zhang_2022_JOM | 已标注-status待升 | 模板 | We identify shift parameters that alter the impa… | `environmental_organizational_resource_availability` |
| `willing-and-able-dual-axis-d-54e163.a` | — | 已标注-status待升 | verbatim | Beyond the motivation to influence information i… | `Pattern: Willing-and-Able Dual-Axis（动机/能力双轴，DesJardine–Li–Shi 2025 型）` |
| `willing-and-able-dual-axis-d-54e163.t1` | — | 已标注-status待升 | 模板 | Beyond the motivation to influence [intermediari… | `Pattern: Willing-and-Able Dual-Axis（动机/能力双轴，DesJardine–Li–Shi 2025 型）` |
| `a-t5-moderator-metaframework-trilevel-mo.t1` | — | 无仓内证据 | 模板 | Research on [lens] argues that because [scarce r… | `Pattern: A：T5_moderator_metaframework_trilevel（moon2026）` |
| `newcomer-voice-integration-a-1103b5.a` | — | 无仓内证据 | verbatim | We select these moderators as they affect the in… | `Pattern: Newcomer Voice-Integration Axis（新声音整合轴，what_changes_after_women_enter_top_manage_2020 型）` |
| `newcomer-voice-integration-a-1103b5.t1` | — | 无仓内证据 | 模板 | [选择理由句——单一机制统一证成] We further theorize that the r… | `Pattern: Newcomer Voice-Integration Axis（新声音整合轴，what_changes_after_women_enter_top_manage_2020 型）` |

### variants/A_construct_differentiation.md（22 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-3a351067.a` | pollock_2015_asq | status待升档 | verbatim | Further, the two constructs have many similariti… | `cjk-3a351067` |
| `cjk-3a351067.b` | pollock_2015_asq | status待升档 | verbatim | Although these definitions are conceptually simi… | `cjk-3a351067` |
| `cjk-3a351067.c` | pollock_2015_asq | status待升档 | verbatim | First, status primarily reflects perceptions of … | `cjk-3a351067` |
| `cjk-3a351067.d` | pollock_2015_asq | status待升档 | verbatim | In contrast, reputation is derived from stakehol… | `cjk-3a351067` |
| `cjk-3a351067.e` | pollock_2015_asq | status待升档 | verbatim | Washington and Zajac's (2005) Jaguar example viv… | `cjk-3a351067` |
| `cjk-3a351067.f` | pollock_2015_asq | status待升档 | verbatim | Taken together, this research establishes clear … | `cjk-3a351067` |
| `cjk-3a351067.t1` | pollock_2015_asq | status待升档 | 模板 | "Although these definitions are conceptually sim… | `cjk-3a351067` |
| `cjk-3a351067.t2` | pollock_2015_asq | status待升档 | 模板 | "First, [Construct A] is derived from [theoretic… | `cjk-3a351067` |
| `cjk-3a351067.t3` | pollock_2015_asq | status待升档 | 模板 | "[Author]'s example vividly illustrated the diff… | `cjk-3a351067` |
| `cjk-3a351067.t4` | pollock_2015_asq | status待升档 | 模板 | "Taken together, this research establishes clear… | `cjk-3a351067` |
| `cjk-a5e32c5c.a` | pollock_2015_asq | status待升档 | verbatim | Hypothesis 1a (H1a): When VC firms are young, re… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.b` | pollock_2015_asq | status待升档 | verbatim | Hypothesis 1b (H1b): When VC firms are older, st… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t1` | pollock_2015_asq | status待升档 | 模板 | [Construct A] will have a [stronger/weaker] [pos… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t2` | pollock_2015_asq | status待升档 | 模板 | When [condition derived from differentiation], [… | `cjk-a5e32c5c` |
| `pollock-2015-6f07e5.a` | pollock_2015_asq | status待升档 | verbatim | Reputation... is best understood as broad public… | `pollock-2015-6f07e5` |
| `pollock-2015-6f07e5.b` | pollock_2015_asq | status待升档 | verbatim | Status, for organizations as well as individuals… | `pollock-2015-6f07e5` |
| `pollock-2015-6f07e5.c` | pollock_2015_asq | status待升档 | verbatim | Although these definitions are conceptually simi… | `pollock-2015-6f07e5` |
| `pollock-2015-6f07e5.t1` | pollock_2015_asq | status待升档 | 模板 | [Construct A] is best understood as [definition … | `pollock-2015-6f07e5` |
| `cjk-3a351067.t1` | pollock_2015_asq | status待升档 | 模板 | "In this subsection, to substantiate its eligibi… | `cjk-3a351067` |
| `cjk-3a351067.t2` | pollock_2015_asq | status待升档 | 模板 | "Importantly, [focal construct] likewise belongs… | `cjk-3a351067` |
| `cjk-3a351067.t3` | pollock_2015_asq | status待升档 | 模板 | "We selected [focal construct] as the key [DV/IV… | `cjk-3a351067` |
| `cjk-3a351067.t4` | pollock_2015_asq | status待升档 | 模板 | "Importantly, although we focus on [focal constr… | `cjk-3a351067` |

### variants/B_mechanism_elaboration.md（18 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `A.a` | ball_2018 | 无仓内证据 | verbatim | in two alternative ways; one purposeful and inte… | `A` |
| `A.t1` | ball_2018 | 无仓内证据 | 模板 | [IV] will be associated with [DV] in [N] alterna… | `A` |
| `cjk-a5e32c5c.a` | keeves_2017_asq | status待升档 | verbatim | Hypothesis 1. Following the enactment of anti-SL… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.b` | keeves_2017_asq | status待升档 | verbatim | This prediction is formally equivalent to hypoth… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t1` | keeves_2017_asq | status待升档 | 模板 | H[N]. [IV] is [positively/negatively] related to… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t2` | keeves_2017_asq | status待升档 | 模板 | H[N]. [Mediator] mediates the [positive/negative… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t3` | keeves_2017_asq | status待升档 | 模板 | H[N]. This prediction is formally equivalent to … | `cjk-a5e32c5c` |
| `cjk-ee756adf.a` | singh_grewal_2023_jmr | status待升档 | verbatim | Figure 3 depicts this 'iron triangle' interactio… | `cjk-ee756adf` |
| `cjk-ee756adf.b` | singh_grewal_2023_jmr | status待升档 | verbatim | Finally, firms interact with the regulator by le… | `cjk-ee756adf` |
| `cjk-ee756adf.t1` | singh_grewal_2023_jmr | status待升档 | 模板 | X → [actor/process state 1] → [state 2] → Y （B0，… | `cjk-ee756adf` |
| `cjk-d76601a3.a` | singh_grewal_2023_jmr | status待升档 | verbatim | Through this influence, media coverage in combin… | `cjk-d76601a3` |
| `cjk-d76601a3.t1` | singh_grewal_2023_jmr | status待升档 | 模板 | X → Y, but this effect is contingent on W1, W2, … | `cjk-d76601a3` |
| `cjk-f5cfffd7.a` | — | 无仓内证据 | verbatim | Taken together, we expect that high overall diss… | `cjk-f5cfffd7` |
| `cjk-f5cfffd7.b` | — | 无仓内证据 | verbatim | In sum, we expect high evaluation heterogeneity … | `cjk-f5cfffd7` |
| `cjk-f5cfffd7.t1` | — | 无仓内证据 | 模板 | Condition A → DV_dimension_1: + Condition A → DV… | `cjk-f5cfffd7` |
| `cjk-20c9ddca.a` | — | 无仓内证据 | verbatim | First, increases in the proportion of explorator… | `cjk-20c9ddca` |
| `cjk-20c9ddca.b` | — | 无仓内证据 | verbatim | However, as the proportion of exploratory allian… | `cjk-20c9ddca` |
| `cjk-20c9ddca.t1` | — | 无仓内证据 | 模板 | Low X → increasing Y (reason 1 + reason 2) High … | `cjk-20c9ddca` |

### variants/C_hypothesis_tree.md（30 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-bf796050.a` | pollock_2015_asq | status待升档 | verbatim | Research has established that status and reputat… | `cjk-bf796050` |
| `cjk-bf796050.b` | pollock_2015_asq | status待升档 | verbatim | Because both reputation and status provide benef… | `cjk-bf796050` |
| `cjk-bf796050.t1` | pollock_2015_asq | status待升档 | 模板 | Prior research has shown that [A] and [B] are po… | `cjk-bf796050` |
| `cjk-0cb8a796.a` | pollock_2015_asq | status待升档 | verbatim | During its early years a firm has little standin… | `cjk-0cb8a796` |
| `cjk-0cb8a796.b` | pollock_2015_asq | status待升档 | verbatim | Thus we expect that reputation will have a great… | `cjk-0cb8a796` |
| `cjk-0cb8a796.c` | pollock_2015_asq | status待升档 | verbatim | As such, we expect that as firms mature, status … | `cjk-0cb8a796` |
| `cjk-0cb8a796.t1` | pollock_2015_asq | status待升档 | 模板 | When firms are young, they lack standing in the … | `cjk-0cb8a796` |
| `cjk-bc08d954.a` | pollock_2015_asq | status待升档 | verbatim | Research has shown that initial conditions influ… | `cjk-bc08d954` |
| `cjk-bc08d954.b` | pollock_2015_asq | status待升档 | verbatim | Because reputation needs to be continually reinf… | `cjk-bc08d954` |
| `cjk-bc08d954.t1` | pollock_2015_asq | status待升档 | 模板 | Initial conditions strongly influence [B] when f… | `cjk-bc08d954` |
| `cjk-1efa45e0.a` | pollock_2015_asq | status待升档 | verbatim | Research on path dependence shows that significa… | `cjk-1efa45e0` |
| `cjk-1efa45e0.b` | pollock_2015_asq | status待升档 | verbatim | Thus when firms are young and unknown, we expect… | `cjk-1efa45e0` |
| `cjk-1efa45e0.t1` | pollock_2015_asq | status待升档 | 模板 | Highly visible positive events can alter organiz… | `cjk-1efa45e0` |
| `cjk-fbe6b726.a` | pollock_2015_asq | status待升档 | verbatim | Blockbuster deals provide valuable signals only … | `cjk-fbe6b726` |
| `cjk-fbe6b726.t1` | pollock_2015_asq | status待升档 | 模板 | Signals provide value only if they convey new in… | `cjk-fbe6b726` |
| `cjk-3a351067.a` | — | 无仓内证据 | verbatim | We argue that objective severity, reflected in t… | `cjk-3a351067` |
| `cjk-3a351067.b` | — | 无仓内证据 | verbatim | We argue that availability cascades weaken high … | `cjk-3a351067` |
| `cjk-3a351067.c` | — | 无仓内证据 | verbatim | Thus, for a negative event such as a capability … | `cjk-3a351067` |
| `cjk-3a351067.d` | — | 无仓内证据 | verbatim | Hypothesis 2. Given category members' high assoc… | `cjk-3a351067` |
| `cjk-3a351067.e` | — | 无仓内证据 | verbatim | This leads to our baseline expectation that both… | `cjk-3a351067` |
| `cjk-3a351067.f` | — | 无仓内证据 | verbatim | However, we further argue that differences in re… | `cjk-3a351067` |
| `cjk-3a351067.t1` | — | 无仓内证据 | 模板 | "We argue that [factor 1] influences [Construct … | `cjk-3a351067` |
| `cjk-3a351067.t2` | — | 无仓内证据 | 模板 | "We argue that the interaction between [IV] and … | `cjk-3a351067` |
| `cjk-3a351067.t3` | — | 无仓内证据 | 模板 | "Having established that [baseline effect], we n… | `cjk-3a351067` |
| `cjk-a5e32c5c.a` | — | 无仓内证据 | verbatim | Hypothesis 1. The positive relationship between … | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.b` | — | 无仓内证据 | verbatim | Hypothesis 4. The positive relationship between … | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t1` | — | 无仓内证据 | 模板 | H1. [IV] is [positively/negatively] related to [… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t2` | — | 无仓内证据 | 模板 | H2. The relationship between [IV] and [DV] is mo… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t3` | — | 无仓内证据 | 模板 | H3. The moderating effect of [Z] on the [IV]→[DV… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t4` | — | 无仓内证据 | 模板 | H2a: When [condition A], [effect A]. H2b: When [… | `cjk-a5e32c5c` |

### variants/D_process_theory.md（16 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-3a351067.a` | lashley_pollock_2020_asq | status待升档 | verbatim | Thus much of the research on core-stigmatized or… | `cjk-3a351067` |
| `cjk-3a351067.b` | lashley_pollock_2020_asq | status待升档 | verbatim | Our goal is to build theory that explains the pr… | `cjk-3a351067` |
| `cjk-3a351067.c` | lashley_pollock_2020_asq | status待升档 | verbatim | Thus while Adams's (2012) study provides a usefu… | `cjk-3a351067` |
| `cjk-3a351067.d` | lashley_pollock_2020_asq | status待升档 | verbatim | Our findings suggest that categorical stigma red… | `cjk-3a351067` |
| `cjk-3a351067.e` | lashley_pollock_2020_asq | status待升档 | verbatim | Each phase was triggered by an event or collecti… | `cjk-3a351067` |
| `cjk-3a351067.f` | lashley_pollock_2020_asq | status待升档 | verbatim | For example, creating a moral prototype and cate… | `cjk-3a351067` |
| `cjk-3a351067.g` | lashley_pollock_2020_asq | status待升档 | verbatim | A moral agenda based on broadly acceptable value… | `cjk-3a351067` |
| `cjk-3a351067.t1` | lashley_pollock_2020_asq | status待升档 | 模板 | "While prior research has focused on [static asp… | `cjk-3a351067` |
| `cjk-3a351067.t2` | lashley_pollock_2020_asq | status待升档 | 模板 | "Prior research on [phenomenon] has suggested [d… | `cjk-3a351067` |
| `cjk-3a351067.t3` | lashley_pollock_2020_asq | status待升档 | 模板 | "We develop a process model of [phenomenon] that… | `cjk-3a351067` |
| `cjk-3a351067.t4` | lashley_pollock_2020_asq | status待升档 | 模板 | "We propose that [Stage 1] is triggered by [cond… | `cjk-3a351067` |
| `cjk-3a351067.t5` | lashley_pollock_2020_asq | status待升档 | 模板 | "Proposition [N]: In [context], [actor]'s [actio… | `cjk-3a351067` |
| `lashley-pollock-2020-1dd70d.a` | lashley_pollock_2020_asq | status待升档 | verbatim | A key finding of our study is that the stigma re… | `lashley-pollock-2020-1dd70d` |
| `lashley-pollock-2020-1dd70d.b` | lashley_pollock_2020_asq | status待升档 | verbatim | This process is messy, as individual organizatio… | `lashley-pollock-2020-1dd70d` |
| `lashley-pollock-2020-1dd70d.t1` | lashley_pollock_2020_asq | status待升档 | 模板 | [Phase 1: Initiating a Moral Agenda] 行业行动者挪用被压制但… | `lashley-pollock-2020-1dd70d` |
| `lashley-pollock-2020-1dd70d.t2` | lashley_pollock_2020_asq | status待升档 | 模板 | Proposition [N]: In [context], [collective actio… | `lashley-pollock-2020-1dd70d` |

### variants/E_moderation.md（23 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-3a351067.t1` | — | 无仓内证据 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `cjk-3a351067` |
| `cjk-3a351067.t2` | — | 无仓内证据 | 模板 | H[N]. The [positive/negative] effect of [X] on [… | `cjk-3a351067` |
| `cjk-3a351067.t3` | — | 无仓内证据 | 模板 | H[N]. Although [X] and [Z] each [positively/nega… | `cjk-3a351067` |
| `cjk-3a351067.t4` | — | 无仓内证据 | 模板 | H[N]. [X] is [positively/negatively] related to … | `cjk-3a351067` |
| `cjk-3a351067.t5` | — | 无仓内证据 | 模板 | H[N]. [X] is positively related to [Y] for [grou… | `cjk-3a351067` |
| `cjk-3a351067.t6` | — | 无仓内证据 | 模板 | H[N]. There will be a [positive/negative] intera… | `cjk-3a351067` |
| `e2-897884.t1` | — | 无仓内证据 | 模板 | "The focal unit of analysis is [Level-1 unit, e.… | `e2-897884` |
| `e2-897884.t2` | — | 无仓内证据 | 模板 | "H[N]. The relationship between [Level-1 X] and … | `e2-897884` |
| `e5-a992d1.a` | — | 已标注-status待升 | verbatim | We maintain that increases in the proportion of … | `e5-a992d1` |
| `e5-a992d1.b` | — | 已标注-status待升 | verbatim | In this type of orientation, increases in the pr… | `e5-a992d1` |
| `e5-a992d1.c` | — | 已标注-status待升 | verbatim | As the proportion of exploratory alliances incre… | `e5-a992d1` |
| `e5-a992d1.d` | — | 已标注-status待升 | verbatim | retaliatory attacks from the partner may reach a… | `e5-a992d1` |
| `e5-a992d1.e` | — | 已标注-status待升 | verbatim | We argue that repeated collaboration attenuates … | `e5-a992d1` |
| `e5-a992d1.f` | — | 已标注-status待升 | verbatim | We expect audience identity proximity to conditi… | `e5-a992d1` |
| `e5-a992d1.t1` | — | 已标注-status待升 | 模板 | "We maintain that increases in [IV] facilitate [… | `e5-a992d1` |
| `e5-a992d1.t2` | — | 已标注-status待升 | 模板 | "Specifically, there are two reasons. First, [re… | `e5-a992d1` |
| `e5-a992d1.t3` | — | 已标注-status待升 | 模板 | "However, as [IV] continues to increase, [turnin… | `e5-a992d1` |
| `e5-a992d1.t4` | — | 已标注-status待升 | 模板 | "We argue that [moderator] [direction] moderates… | `e5-a992d1` |
| `e5-a992d1.t5` | — | 已标注-status待升 | 模板 | [Assumption] The negative effect rests on [peers… | `e5-a992d1` |
| `A.a` | ball_2018 | 无仓内证据 | verbatim | This is precisely the reason why the ANDA produc… | `A` |
| `A.t1` | ball_2018 | 无仓内证据 | 模板 | This study rests on the premise that [regime A] … | `A` |
| `B.a` | ball_2018 | 无仓内证据 | verbatim | the relationship should be even stronger for low… | `B` |
| `B.t1` | ball_2018 | 无仓内证据 | 模板 | [Moderator] is operationalized via [attribute of… | `B` |

### variants/F_competing_hypotheses.md（17 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `cjk-3a351067.a` | — | 无仓内证据 | verbatim | However, the literatures on recalls and politica… | `cjk-3a351067` |
| `cjk-3a351067.b` | — | 无仓内证据 | verbatim | On the one hand, firms with more liberal TMTs ma… | `cjk-3a351067` |
| `cjk-3a351067.c` | — | 无仓内证据 | verbatim | On the other hand, firms with more conservative … | `cjk-3a351067` |
| `cjk-3a351067.d` | — | 无仓内证据 | verbatim | Given these competing arguments, we put forth th… | `cjk-3a351067` |
| `cjk-3a351067.t1` | — | 无仓内证据 | 模板 | "However, the literatures on [领域A] and [领域B] off… | `cjk-3a351067` |
| `cjk-3a351067.t2` | — | 无仓内证据 | 模板 | "On the one hand, [X_high] may [increase/decreas… | `cjk-3a351067` |
| `cjk-3a351067.t3` | — | 无仓内证据 | 模板 | "On the other hand, [X_low] may [increase/decrea… | `cjk-3a351067` |
| `cjk-3a351067.t4` | — | 无仓内证据 | 模板 | "Given these competing arguments, we put forth t… | `cjk-3a351067` |
| `cjk-a5e32c5c.a` | — | 无仓内证据 | verbatim | Hypothesis 1(a). There is a negative relationshi… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.t1` | — | 无仓内证据 | 模板 | H1a: [X] is [negatively/positively] related to [… | `cjk-a5e32c5c` |
| `技巧-1.a` | wowak_2025_ms | 已标注-status待升 | verbatim | One could argue that more liberal TMTs would rec… | `技巧-1` |
| `技巧-1.t1` | wowak_2025_ms | 已标注-status待升 | 模板 | [直觉预测 + 机制] One could argue that [X_high] would … | `技巧-1` |
| `技巧-2.a` | wowak_2025_ms | 已标注-status待升 | verbatim | Conversely, firms with more conservative TMTs ma… | `技巧-2` |
| `技巧-2.t1` | wowak_2025_ms | 已标注-status待升 | 模板 | [极 A 直觉] One could argue that [X_high] would [be… | `技巧-2` |
| `技巧-3.a` | wowak2025 | 已标注-status待升 | verbatim | Whether the manager of a substitute brand interp… | `技巧-3` |
| `技巧-3.b` | wowak2025 | 已标注-status待升 | verbatim | Last, we foresee that the two interpretations ma… | `技巧-3` |
| `技巧-3.t1` | wowak2025 | 已标注-status待升 | 模板 | [不可观测声明] Whether [actor] interprets [trigger] as… | `技巧-3` |

### variants/G_dialectical_opposition.md（61 条）

| id | citekey | 类别 | kind | 摘录 | 锚点 vid |
|---|---|---|---|---|---|
| `t1.a` | — | 无仓内证据 | verbatim | Classification helps people make sense of a comp… | `t1` |
| `t1.t1` | — | 无仓内证据 | 模板 | Classification helps people make sense of a comp… | `t1` |
| `t2.a` | — | 无仓内证据 | verbatim | Previous research suggests that organizations th… | `t2` |
| `t2.t1` | — | 无仓内证据 | 模板 | Previous research suggests that [entities] that … | `t2` |
| `t3.t1` | — | 无仓内证据 | 模板 | Literature documenting hazards of [state] takes … | `t3` |
| `t4.a` | — | 无仓内证据 | verbatim | Despite research showing that people are put off… | `t4` |
| `t4.b` | — | 无仓内证据 | verbatim | For a market-maker, ambiguity presents an opport… | `t4` |
| `t4.t1` | — | 无仓内证据 | 模板 | Despite research showing [state] is [penalty], i… | `t4` |
| `reconciliation-f704d5.a` | — | 无仓内证据 | verbatim | The above hypotheses propose that ambiguous clas… | `reconciliation-f704d5` |
| `reconciliation-f704d5.t1` | — | 无仓内证据 | 模板 | The above hypotheses propose that [state] makes … | `reconciliation-f704d5` |
| `t7.a` | — | 无仓内证据 | verbatim | I tested the hypotheses using the empirical cont… | `t7` |
| `t7.b` | — | 无仓内证据 | verbatim | In addition, organizations in this industry soug… | `t7` |
| `t7.t1` | — | 无仓内证据 | 模板 | I tested the hypotheses using [industry/setting]… | `t7` |
| `cjk-0d4eac46.a` | Zhou 2017 | 无仓内证据 | verbatim | Institutional theory focuses on the interaction … | `cjk-0d4eac46` |
| `cjk-0d4eac46.t1` | Zhou 2017 | 无仓内证据 | 模板 | [Theory A] focuses on the interaction between [e… | `cjk-0d4eac46` |
| `cjk-43e8243d.a` | Zhou 2017 | 无仓内证据 | verbatim | We propose that state ownership should enable fi… | `cjk-43e8243d` |
| `cjk-43e8243d.t1` | Zhou 2017 | 无仓内证据 | 模板 | We propose that [IV] should enable firms to gain… | `cjk-43e8243d` |
| `cjk-4bae6b3e.a` | Zhou 2017 | 无仓内证据 | verbatim | Shareholders of private firms may not always suc… | `cjk-4bae6b3e` |
| `cjk-4bae6b3e.b` | Zhou 2017 | 无仓内证据 | verbatim | Second, in many emerging economies, politicians … | `cjk-4bae6b3e` |
| `cjk-4bae6b3e.t1` | Zhou 2017 | 无仓内证据 | 模板 | [Actors] in [alternative setting] may not always… | `cjk-4bae6b3e` |
| `u-267b3f.a` | Zhou 2017 | 无仓内证据 | verbatim | Whereas the institutional view emphasizes the re… | `u-267b3f` |
| `u-267b3f.t1` | Zhou 2017 | 无仓内证据 | 模板 | Whereas [Lens A] emphasizes the [advantage] brou… | `u-267b3f` |
| `cjk-cf2c2915.a` | Zhou 2017 | 无仓内证据 | verbatim | We posit that institutional development will wea… | `cjk-cf2c2915` |
| `cjk-cf2c2915.b` | Zhou 2017 | 无仓内证据 | verbatim | As a result, state start-ups suffer less from th… | `cjk-cf2c2915` |
| `cjk-cf2c2915.t1` | Zhou 2017 | 无仓内证据 | 模板 | [Institutional development] weakens the [IV] → [… | `cjk-cf2c2915` |
| `cjk-f802f566.a` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Hence, external venturing can bring major learni… | `cjk-f802f566` |
| `cjk-f802f566.t1` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | 模板 | [Resource lens] explains why organizations seek … | `cjk-f802f566` |
| `cjk-81c73d68.a` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Accordingly, and consistent with the notion of e… | `cjk-81c73d68` |
| `cjk-81c73d68.b` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Hypothesis 1: CVC activity has an inverted U-sha… | `cjk-81c73d68` |
| `cjk-81c73d68.t1` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | 模板 | At low-to-moderate [X], each additional activity… | `cjk-81c73d68` |
| `warrant-d8114e.a` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Upon investment, the investor tries to establish… | `warrant-d8114e` |
| `warrant-d8114e.b` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | This is why the most common form of learning in … | `warrant-d8114e` |
| `warrant-d8114e.t1` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | 模板 | [Mode A] instantiates the shared trunk through [… | `warrant-d8114e` |
| `cjk-7573339b.a` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Firms will likely engage in more diverse, opport… | `cjk-7573339b` |
| `cjk-7573339b.b` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | verbatim | Thus, we argue that market turbulence will initi… | `cjk-7573339b` |
| `cjk-7573339b.t1` | Bendig–Hensellek–Schulte 2024 | 无仓内证据 | 模板 | [Shared W] complicates search, valuation, and kn… | `cjk-7573339b` |
| `cjk-ec317dc6.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Therefore, according to theory and evidence on t… | `cjk-ec317dc6` |
| `cjk-ec317dc6.b` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Therefore, according to theory and evidence in t… | `cjk-ec317dc6` |
| `cjk-ec317dc6.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | Both [Theory A] and [Theory B] speak directly to… | `cjk-ec317dc6` |
| `cjk-15485503.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | is not acknowledged by applications of social co… | `cjk-15485503` |
| `cjk-15485503.b` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Therefore, tournament theory makes limited if an… | `cjk-15485503` |
| `cjk-15485503.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | We argue that research based on these theories c… | `cjk-15485503` |
| `cjk-f0a848fd.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Thus, each new failure offers unique knowledge t… | `cjk-f0a848fd` |
| `cjk-f0a848fd.b` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | However, as these failures repeat and accumulate… | `cjk-f0a848fd` |
| `cjk-f0a848fd.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | [Positive account] Repeated X expands [opportuni… | `cjk-f0a848fd` |
| `cjk-9672e512.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Hence, to effectively learn from their own failu… | `cjk-9672e512` |
| `cjk-9672e512.b` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Hypothesis H1. There will be an inverted-U-shape… | `cjk-9672e512` |
| `cjk-9672e512.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | [Y] requires sufficient A and B. Low X: low A × … | `cjk-9672e512` |
| `cjk-99b4e31e.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | This implies that individuals with higher percei… | `cjk-99b4e31e` |
| `cjk-99b4e31e.b` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Hence, we predict that the inverted-U-shaped rel… | `cjk-99b4e31e` |
| `cjk-99b4e31e.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | [W] gives actors a larger initial stock of B and… | `cjk-99b4e31e` |
| `cjk-a5e32c5c.a` | — | 无仓内证据 | verbatim | Organizations that affiliate with more ambiguous… | `cjk-a5e32c5c` |
| `cjk-a5e32c5c.b` | — | 无仓内证据 | verbatim | Organizations that affiliate with more ambiguous… | `cjk-a5e32c5c` |
| `dialectical-turn-cd9086.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Despite research showing that people are put off… | `dialectical-turn-cd9086` |
| `dialectical-turn-cd9086.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | "Despite research showing [hazard consensus], [s… | `dialectical-turn-cd9086` |
| `symmetric-mechanism-contrast.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Thus the way an ambiguous identity is regarded d… | `symmetric-mechanism-contrast` |
| `symmetric-mechanism-contrast.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | For [audience A], [state] makes [entities] [adje… | `symmetric-mechanism-contrast` |
| `t6-reconciliation.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | This may seem ironic, given that venture capital… | `t6-reconciliation` |
| `t6-reconciliation.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | "This may seem [paradoxical], given that [goal a… | `t6-reconciliation` |
| `two-source-construct-discrimination.a` | Ridge–Aime–White 2013 | 无仓内证据 | verbatim | Together, these studies suggest that ambiguous c… | `two-source-construct-discrimination` |
| `two-source-construct-discrimination.t1` | Ridge–Aime–White 2013 | 无仓内证据 | 模板 | "[Focal construct] can arise when [entities] [so… | `two-source-construct-discrimination` |

