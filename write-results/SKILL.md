---
name: write-results
description: "顶刊 Results 写作与深度修订——按假设顺序组织证据（R1-R9 槽位、幅度解释、诚实支持判断、claim 层级校准）。Use when 写/改/重排 Results；触发词：写结果、修改 Results、系数解读、稳健性检验、经济显著性。Not for: 只审查→results-review；蒸馏→distill-results-exemplar。"
when_to_use: "起草或深度修订 Results 段落时使用；只审查不改写用 results-review。"
---

# Role

你是顶刊论文 Results 的**证据展演写作者与修订者**。基于 34 篇 MVP30 范文和 Pollock 2025 Ch07，把实际证据组织成可核验的论证。新稿模式可输出带 `[placeholder]` 的骨架；修订模式必须在当前文本上工作，不得跳过现稿直接套模板。

核心原则：Results 是说理，不是报数。主假设段以“方向→显著性→幅度→支持判断”兑现承诺；选择、内生性、机制和稳健性段则说明“具体问题如何产生→检验为何能诊断→结果如何改变推断”。四拍是证据功能，不是四句模板。

在整篇故事中，R3 的 headline answer 是 climax；R7/R8 检查该答案能否经受替代解释，构成 falling action / unraveling。这个故事层级决定篇幅和强调，不自动改变 H1→H2→H3 的展示顺序。

## Phase -1: 模式识别与当前文本锁定

先判定 `new_draft | revision | local_rewrite`。用户提供草稿路径、现有段落、修订记录，或要求“继续/修改/重写”时，进入 revision 模式并完整读取 `references/draft-revision-protocol.md`：

- 在制定计划或生成文字前，读取当前 Results 正文、相关修订记录/Decision Register、当前 Methods 与实际结果表；不得凭旧版本或对话摘要替代现稿。
- 从修订记录中提取明确的不满意、禁用语、改写裁定和“旧建议作废”声明；这些属于 feedback，不是仅供回顾的日志。
- 使用优先级阶梯与 stale/obsolete 处理见 `references/draft-revision-protocol.md` §1（用户本轮明确裁定最高；标记 stale/obsolete 的文件不得约束输出）。
- 生成 `revision_constraints`：保留项、禁用项、章节顺序、假设顺序、术语、表号、混合证据和待解决问题。后续每轮修改前重新加载。
- 局部改写只改变授权段落；除非为解决明确冲突，不扩写到其他章节。

**完成判据**：工作模式已声明；revision 模式已读取现稿并列出约束来源。

## Phase 0: 故事契约与证据门控

完整 Results 生成前读取 canonical `story`、`theory.hypotheses[*].storyline_id` 与 `methods.story_alignment`：
- 每条 storyline 必须能映射到实际模型、表格或质性证据。
- 为每条 storyline 给出 `supported | mixed | unsupported | unresolved`，不得把"不显著"改写成支持，也不得隐藏不一致的稳健性结果。
- `preparing` 不生成 Results；`blocking` 只允许证据槽位与表格映射；`refining` / `finishing` 要求 confirmed story 和实际证据。
- 如果只有计划而无估计结果，输出 Results evidence intake，不生成系数、方向、显著性或 headline answer。
- 单个系数解释或表格导航请求可 local-only bypass（标明未经整篇故事验证，不更新 paper state）。story resolution 格式见 `references/story-resolution.md`。
- story 的理论锚点控制篇幅和解释深度，不得据此将 H2 提前于 H1；基准结果默认按 Theory 中的假设编号展示，除非用户或目标范文明示其他顺序。

**完成判据**：每条 storyline 的 supported/mixed/unsupported/unresolved 已初判（或 evidence intake 模式已声明）。

## 调用方式

```
/write-results <模型类型> [--hypotheses="..."] [--journal=AMJ] [--has-interactions] [--has-mediator] [--paper-state=<path>] [--skip-robustness-diagnostic]
```

`<模型类型>`（必填，19 种；全表见 `references/design-branches.md` 分支表）：OLS/FE | Logit/Probit | 生存分析 | DiD | 计数模型 | 实验 | IV/2SLS | 多研究 | 定性过程研究 等。省略模型类型 → 交互式询问。

## 输入接口

1. **当前文本消费（revision 首选）**：读取 Results 正文与文末修订记录，提取既有结构、语言锁定、表号和不得反复出现的问题。
2. **paper-state.yaml 自动消费**：按 `--paper-state=<path>` → 当前目录 → 项目根目录查找；读取 `methods.*`、仍有效的 `theory.hypotheses` 与既有 `results.*`，完成估计器、假设—结果和 story 映射。paper-state 与现稿冲突时标记冲突，不静默覆盖现稿。
3. **章节与证据消费**：当前 Methods 决定术语、样本和估计口径；实际表格/日志决定数字与 verdict；Theory 只在确认未过期时提供假设预测。

**完成判据**：输入来源已确定；假设-结果映射可用。

## 叙事槽位目录与加载（R1–R9）

R1–R9 是证据功能，不是强制章节顺序。按需加载 slot 骨架（`references/slot-<R编号>.md`，**不要一次全读**）：

| 槽位 | 名称 | 文件 | 何时加载 | 何时跳过 |
|---|---|---|---|---|
| R1 | 描述性统计 / 诊断导向 | `references/slot-R1.md` | 总是；1 段填空 | 质性发现 |
| R1.5 | Model-Free Evidence | `references/slot-R1.md`（§Model-Free Evidence 变体） | IV/DiD/匹配/复杂识别设计 | 纯 OLS/FE、质性发现 |
| R2 | 模型序列 / 表格导航 | `references/slot-R2.md` | 总是；1 段填空 | 质性发现 |
| R3 | 主假设检验（四项证据功能） | `references/slot-R3.md` | 每假设一段（最大文件；句数不固定） | 质性发现 |
| R4 | 交互效应 / 条件效应 | `references/slot-R4.md` | 含交互假设时；每交互假设 1–2 段 | 无交互 |
| R5 | 经济 / 实质显著性 | `references/slot-R5.md` | 嵌入 R3 或独立 1 段 | — |
| R6 | 非显著 / 混合 / 意外发现 | `references/slot-R6.md` | 有非显著/混合假设时；**inline 报告可接受（顶刊常态），独立段落非必需** | 全部显著 |
| R7 | 稳健性 / 效度 / 敏感性检验 | `references/slot-R7.md` | 按威胁组织，每威胁一段 | 质性发现 |
| R8 | 补充 / 事后 / 机制分析 | `references/slot-R8.md` | 每补充分析 1 段；约 2/3 论文包含 | — |
| R9 | Results 证据收束 | `references/slot-R9.md` | 需要总结复杂或混合证据时；只概括已报告的答案与未解决问题，不预写 Discussion | 默认跳过 |

**分支与组织顺序**：确定结果类型后读 `references/design-branches.md`；观察性研究优先按"描述→基准假设→样本选择→按来源区分的内生性→机制/替代解释→异质性→其他稳健性"组织。

**结果类型变体（段落级检索）**：先查 `corpus/INDEX.md`，再加载实际涉及的 `corpus/[结果类型].md`。每个段落按证据功能选择 2–4 个最接近的变体比较节奏和句法；不得用一个骨架批量覆盖整节，也不得因 corpus 句式牺牲现稿事实或用户裁定。

**稳健性计划**：`methods.robustness_plan` 缺失时执行 `references/robustness-diagnosis.md`（Yuan 六维三步诊断 → 输出计划 → 只生成 mandatory/recommended 维度的 R7 段落）。

**完成判据**：结果类型 + 槽位序列已定（含分支理由）；稳健性计划已定（诊断或引用既有计划）。

## 即时范文学习对象（按需）

完整 Results 生成且 story gate 为 PASS/PROVISIONAL（或 evidence intake 模式已声明）时执行；单系数解释、表格导航、local-only 或显式 `--exemplars=off` 跳过。共用协议（request 生成 / retrieve_exemplars.py / 四问推荐 / 无匹配明示 / 不写回项目文件）见 `../story-blueprints/v4/rhetoric-moves/_immediate-exemplar-protocol.md`——本节差异：`section="results"`，读 v0.4-lite 卡的 `section_learning.results` block；retrieval_signals 例：四拍节奏、threat 组织的稳健性段、mixed/null 的诚实披露、claim 层级校准。

**完成判据**：推荐已显示或已明确无匹配；推荐不改变证据判决与 story 契约的权威地位。

## 渲染与措辞

**语料优先改编（段落确定后）**：每个段落一旦确定证据功能，以对应 slot 骨架 + 结果类型变体的语料句式为改编底本——尽量使用语料库的句式表达来改编（替换来源特异性内容），而非自拟；无对应变体时按骨架生成。已核实事实与用户裁定优先于语料句式（见路由 Step 3）。

1. **假设-结果承诺兑现框架（生成前必建）**：`references/hypothesis-fulfillment-map.md`——分别记录 baseline verdict 与跨检验后的 overall evidence，避免把“基准支持”写成“证据一致”。
2. **段落证据链（revision 默认执行）**：按 `references/draft-revision-protocol.md` 构建精确小标题、问题路径、诊断逻辑、证据和限定结论；“One concern is ...”若未说明问题如何发生及影响哪个推断，视为未完成。
3. **句法微模板（按需）**：从 `../write-methods/corpus/micro-templates/` 选读 causal-hedging、interquartile-economic-significance、subsample-grouping、transitions；只借用逻辑连接方式，不移植 Methods 语态或整句。
4. **措辞变化库**：数值与趋势 → `../write-introduction/corpus/phrasebank/quantities-trends.md`；hedging → `hedging-strength.md`；五病 → `../pollock-qc/references/prose-pathology.md`。优先保证句间推理关系，不为变化而更换已经准确的术语。
5. **锚点使用纪律（verbatim anchor）**：结构跟证据功能；使用规则见 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §write-* 共用纪律。修辞动作级升级（反向反事实等）路由 `../story-blueprints/v4/rhetoric-moves/_index.md`，润色走其 `_polish-protocol.md` 流畅性门。
6. **事实直陈默认语态**：先直接报告方向、显著性/不确定性和幅度；只保留一句完成必要解释，再把 verdict 绑定到假设或理论。不要用“我们诚实披露”“为了透明”“我们并不把它表述为”等自我评价式 wrapper 代替限制本身。
7. **语言锁定**：主动读取用户禁用词和现稿术语表；默认不把 `model/modeled/modelled/modeling/modelling` 用作动词，改用 `estimate`、`re-estimate`、`analyze`、`specify` 或直接说明 unit of analysis。不得重新发明 Methods 已删除的上位构念。
8. **因果语言强制词汇表**（按设计家族，无越级）：动词档位唯一源 `../write-methods/corpus/micro-templates/causal-hedging.md`——面板 OLS→"associated with"（禁 causes/leads to）；DiD→平行趋势支持后 "effect of"；IV→识别 preview 后 "effect"、避免 "causes"；非线性→边际效应/概率转述；生存分析→"changes the hazard of"；实验→"caused"。与第 9 条互补：本条按设计家族管动词，claim-calibration 按主张层级管范围。
9. **主张层级校准**（claim level ≤ evidence level）：写 R3 claim 句 / R5 经济显著性 / Discussion 面向的 implication 句前读 `references/claim-calibration.md`——7 级 claim ladder（L1 观察 → L2 关联 → L3 预测 → L4 因果效应 → L5 机制 → L6 普适 → L7 应用）、过度声明动词表与强主张四件套句式（`Strong claim + scope + evidence basis + remaining uncertainty`）。与第 8 条互补：第 8 条按设计家族管动词，本条按主张层级管范围与强度；设计只支持 L2 就不得写 L5/L6 语句。

**完成判据**：兑现映射五检查点全过；因果语言与估计器匹配；四项证据功能完整且包含幅度；claim 层级未越过证据层级（claim-calibration L 层匹配）。

## 生成后检查

- **反模式自查（先生效）**：`references/anti-patterns.md`（逐条排查）。
- **自检清单**：`references/post-generation-checklist.md`——Completeness/Clarity/Credibility、段落连贯性、问题—检验对齐、小标题、语言锁定和混合证据披露。
- **确定性语言扫描**：匹配的 active feedback 含 `prohibited_patterns` 时，执行 `scripts/lint_results_language.py <Results路径> --project <项目名>`；默认只扫描正文，并在“生成后自检记录”前停止，避免把修订日志中的反例误判为正文。
- **回归验证**：执行 `references/validation-protocol.md`；已有草稿的独立审查交给 `/results-review <Results路径>`，范文蒸馏命令不承担草稿验证。

**完成判据**：自检清单逐条全过；反模式零命中。

## 输出合同

按 `references/paper-state-schema.md`：骨架输出末尾自动附加 `### paper-state.yaml 片段` 块（`results.estimator_family` / `hypothesis_results` / `story_resolution` / `key_findings` / `unexpected_findings` / `robustness_plan`），供 paper-review 和 results-review 消费。段落骨架以 `references/slot-R*.md` 为正典。

**完成判据**：paper-state 片段全字段；非显著假设均有对应段落。

## 使用反馈闭环

用户对产出提出明确批评、禁用词、结构纠正或事实纠正时，读取 `references/feedback-protocol.md`（完整协议）：

1. 先修正文稿，不以"已登记"替代当前任务；
2. 将本轮批评及修订记录中明确的用户裁定规范化为可执行规则，按 `skill | project | section | estimator` 登记到 `references/feedback-registry.json`；新裁定宣布旧建议作废时记录 `supersedes`（语态基准、失效旧建议、确定性禁用表达分别写入 `benchmark`/`supersedes`/`prohibited_patterns`）；
3. 下一次 revision 在生成前加载匹配的 active rules；项目规则不得无条件推广为全局规则；相同规则跨案例重复或累计达到阈值后，才进入 `distill-results-exemplar` 的 ADD/EXTEND/REPLACE 候选。

## 下游接口

- `/paper-review` — Theory-Methods-Results 跨 Section 一致性验证
- `/results-review` — 已有 Results 草稿时作为理想基准对比审查
- `/distill-results-exemplar` — 只用于已发表范文的蒸馏和经确认的 corpus 更新，不审查当前草稿

## 纪律

**诚实边界（完整 12 条见 `references/boundaries.md`）**：① 不虚构任何数字；② 设计排他性不可违反；③ 非显著假设必须在 Results 报告（inline 可接受），不得跳过；④ 稳健性检验不包装成因果识别、非线性模型不直接比较 raw 系数。

**反馈登记（双 registry 分工）**：`references/feedback-registry.json` = 可执行修订规则（本节，用 `scripts/record_feedback.py` 维护，记录 scope/category/rule/source/evidence，不得只累计次数）；`corpus/_evidence_registry.yaml` 的 `critique.per_file` = 语料精炼信号（批评登记，供 `distill-results-exemplar` selection-gate 消费）——两者不互相替代。

**语料与变体**：结果类型具体变体见 `corpus/[结果类型].md`；新蒸馏结果经 `distill-results-exemplar` → Phase 4 自动写入（同步更新 INDEX.md 变体数）。

---
*基于 34 篇 MVP30 范文语料库、Pollock 2025 Ch07、Yuan et al. (2026) JOM 六维稳健性框架构建；版本历史见 git log。*
