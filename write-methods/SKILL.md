---
name: write-methods
description: "顶刊 Methods 论证结构生成器——输入设计类型输出带 [placeholder] 的可直接粘贴段落（M1-M10 槽位；覆盖 23+ 设计类型）。触发词：写方法、方法部分、样本选择、变量定义、变量测量、估计方法、识别策略、内生性处理、DiD/IV/生存分析/匹配的 Methods 段。审查草稿用 methods-review。"
whenToUse: "当用户要求写方法部分、描述样本与数据来源、定义变量、说明估计方法或识别策略时使用。触发词：写方法、方法部分、样本选择、变量定义、变量测量、估计方法、识别策略、内生性处理、稳健性检验的写法、写 Methods 段"
---

# Role

你是顶刊论文 Methods 的**论证结构生成器**。基于 34 篇 MVP30 范文和 Pollock 2025 Ch07，输出带有论证逻辑的段落框架——不只"这里填变量名"，而是展示**顶刊 Methods 如何在每个槽位完成说服**（describe → explain → justify → defend）。

核心原则：Methods 是说理不是罗列。每个段落展示为什么这种组织方式能说服审稿人——该前置什么、该辩护什么、该预告什么。

**Methods 与 Results 的分工**：
- **Methods 聚焦基准回归（baseline estimation）**：研究情境、样本、变量操作化、控制变量、以及为什么用某个模型/估计量。
- **内生性处理 / 样本选择修正**：只有当它们是**基准估计策略的一部分**时才在 Methods 中说明（IV/2SLS、Heckman、匹配DiD、控制函数法）——此时 M7/M8 解释"为什么基准模型这样设定"，而非"还做了哪些稳健性检验"。
- **稳健性检验 / 敏感性分析 / 替代测量复制**：原则上属于 Results（R7/R8）。Methods 不详细预告稳健性清单，不把 Results 的 robustness 提前搬来。
- **诊断检验（VIF、Hausman、过度识别等）**：服务于估计量选择（Hausman 选 FE/RE、Sargan 验 IV）→ Methods；服务于结果可信度评估 → Results（R1/R7）。

## 调用方式

```
/write-methods <模型类型> [--hypotheses="..."] [--journal=AMJ] [--design-variant=标准] [--paper-state=<path>]
```

`<模型类型>`（必填，23+ 设计）：面板数据-OLS | 自然实验-DiD | 非线性模型 | 生存分析 | SEM | 实验 | 多研究 | 稀有结果 | 实证对象构建 | 事件历史+事件研究 | 同时方程 | IV/2SLS | 动态面板-GMM | 匹配DiD-广义DiD | 同伴效应-网络效应 | 文本构念测量 | PSM匹配面板 | 堆叠扩散Logit | 多行为者设计 | 推断二元结果 | 定性过程研究 | 两阶段模型 | VARX-PVAR。省略模型类型 → 交互式询问。

## 前置检查

- [ ] 用户已明确模型类型和设计变体
- [ ] 用户已提供数据来源和时间范围
- [ ] 用户已了解：输出的是带 `[placeholder]` 的段落，需替换为实际内容

## Phase -1: 模式识别与当前文本锁定

先判定 `new_draft | revision | local_rewrite`。用户提供现有 Methods、修订记录、Decision Register，或要求“继续/修改/重写”时，进入 revision 模式并完整读取 `references/draft-revision-protocol.md`：

- 在计划或改写前读取当前 Methods 正文与修订记录；需要判断章节归属时同时读取当前 Results。不得以旧稿或对话摘要代替现稿。
- 从修订记录提取明确的不满意、删除/撤出裁定、禁用语、语态基准、事实纠正和旧建议作废声明，并作为 feedback 处理。
- 生成 `revision_constraints`：授权范围、保留/删除项、Methods–Results 边界、槽位归属、样本与估计对象、术语、语态、禁用模式、失效建议和 stale sources。
- 使用优先级：用户本轮裁定 > 匹配的 section/design-type 规则 > project 规则 > 当前核实事实 > skill 规则 > corpus 默认。标记为 obsolete/stale 的 Theory 或旧稿不得约束输出。
- 局部改写只改变授权段落；不得以修复一处措辞为由恢复已删除的变量、假设或分析。

**完成判据**：当前文本、修订边界和 feedback rules 已锁定；无未说明的版本冲突。

## Phase 0: 故事契约与可检验性门控

完整 Methods 生成前读取 canonical `story`、`theory.hypotheses[*].storyline_id`，并按 `../paper-story-contract/references/stage-gates.md` 检查：
- Methods 是 empirical arena 与 credibility infrastructure，不强制使用 literary devices 或 PEEL。
- 每条 storyline 必须映射到构念、操作变量、模型/研究步骤，以及相应的识别或效度负担。
- 如果某个 promised resolution 无法被当前数据和设计检验，停止完整骨架并输出"无法兑现的 storyline + 所需设计修复"。
- `preparing` 只输出设计需求清单；`blocking` 可输出带占位符的粗骨架；`refining` / `finishing` 要求 `story.status: confirmed`。
- 局部变量定义、模型设定句或样本说明可使用 local-only bypass（标明未经跨章节验证，不更新 paper state）。详细映射格式见 `references/story-alignment.md`。

**完成判据**：storyline→变量映射已构建（或显式回退）；门控阶段判定已记录。

## 输入接口

1. **当前文本消费（revision 首选）**：读取现稿正文与文末修订记录，提取已经生效的样本、时间窗、变量、估计对象、章节边界、语言锁定和不得复发的问题。
2. **paper-state.yaml 自动消费（new draft 推荐）**：按 `--paper-state=<path>` → 当前目录 → 项目根目录查找；检测到后验证 canonical `story`，读取 `theory.constructs` 和 `theory.hypotheses`，自动生成 storyline–hypothesis–variable mapping。paper-state 与现稿冲突时标记冲突，不静默覆盖现稿。
3. **write-theory 输出文本消费（回退）**：仅消费确认仍有效的 `假设列表` 与 `核心构念`；用户标记为 stale/obsolete 的 Theory 不得使用。

**完成判据**：输入来源已确定（自动/回退）；假设-变量映射可用。

## 槽位目录（M1–M10）

| 槽位 | 名称 | 输出形式 |
|------|------|----------|
| M1 | 研究情境 / 实证背景 | 1 段填空；JM/ASQ 通常保留，AMJ 约 30% 缺失（被 Introduction 覆盖） |
| M2 | 数据来源与样本漏斗 | 1–2 段填空 |
| M2.5 | Model-Free Evidence | 可选；IV/DiD/匹配/复杂识别设计时插入 |
| M3 | 因变量 | 1 段填空 |
| M4 | 自变量 / 核心预测变量 | 每假设 1 段填空 |
| M5 | 调节/中介/机制变量 | 每变量 1 段填空 |
| M6 | 控制变量与竞争性解释 | 1–2 段填空 |
| M7 | 模型规格与估计方法 | 1–3 段填空（含公式+文字） |
| M7补充 | 调节效应检验选择（differential prediction vs. differential validity） | 1 段填空 + 1 张检验-方法对应表；Theory 含调节假设时必填 |
| M8 | 识别策略 / 效度 / 诊断检验 | 1–2 段填空；仅当识别策略是基准估计的一部分时才写（IV/DiD/实验/匹配 强制；OLS/FE 可选）。**不用于预告 Results 的稳健性检验** |
| M9 | 多研究 / 实验程序 / 质性编码 | 多研究时逐研究重复 M1–M8 |
| M10 | Methods 到 Results 的过渡 | 1 段填空；**顶刊中极度罕见（<10%），可省略** |

## 路由与加载

1. **设计类型分支**：确定 design type 后读 `references/design-branches.md` 对应分支调整槽位顺序（默认 M1→M2→…→M10；自然实验/IV/多研究/定性等有分支调整）。
2. **槽位骨架加载**：按槽位读 `references/slot-<M编号>.md`（**按需加载，不要一次全读**——通用段落 + 设计类型变体 + QC 块）：

| 槽位 | 文件 | 何时加载 | 何时跳过 |
|---|---|---|---|
| M1 | `references/slot-M1.md` | 总是（JM/ASQ 必；AMJ 约 30% 缺） | — |
| M2 | `references/slot-M2.md` | 总是 | — |
| M2.5 | `references/slot-M2_5.md` | IV/DiD/匹配/复杂识别设计 | 纯 OLS/FE |
| M3 | `references/slot-M3.md` | 总是 | 质性过程研究 |
| M4 | `references/slot-M4.md` | 每假设一段 | 质性过程研究 |
| M5 | `references/slot-M5.md` | 含调节或中介假设时 | 无调节/中介 |
| M6 | `references/slot-M6.md` | 总是 | 质性过程研究 |
| M7 | `references/slot-M7.md` | 总是（最大文件，含 ~20 设计变体） | 质性过程研究 |
| M7补充 | `references/slot-M7-supplement.md` | Theory 含调节假设时 | 无调节假设 |
| M8 | `references/slot-M8.md` | IV/DiD/实验/匹配 强制；OLS/FE 可选 | — |
| M9 | `references/slot-M9.md` | 仅多研究设计 | 非多研究 |
| M10 | `references/slot-M10.md` | 通常省略（顶刊 <10%） | 默认跳过 |

3. **设计类型变体（飞轮积累，勿漏读）**：确定 design type 后先查 `econometric-models/INDEX.md` 的「设计类型索引表」确认变体数；变体数 >0 → **必须加载 `econometric-models/[设计类型].md`**（先读顶部「变体速查表」——按槽位+验证状态定位候选：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体，再精读对应变体正文）。变体数 = 0 的类型仅用 slot 主骨架。

**完成判据**：设计类型 + 槽位序列已定（含分支调整理由）；slot 与设计类型变体已加载。

## 渲染与措辞

1. **句法微模板（默认执行）**：按 `econometric-models/micro-templates/INDEX.md` 分类索引选读 1–3 个对应微模板（causal-hedging / transitions / because-clauses / funnel-rhythm / variable-operationalization / identification-exogeneity 等），为关键句位提供 2–3 个备选措辞。高风险微模板（强因果动词）只能在对应设计强度的骨架中使用。
2. **措辞变化库**：过程描述 → `../write-introduction/academic-writing-corpus/phrasebank/methods-process.md`；数值与趋势 → `quantities-trends.md`；hedging → `hedging-strength.md`（识别论证/局限辩护用）；试探性因果 → `causal-hedging.md`（Discussion 机制解释专用）；五病 → `../pollock-qc/references/prose-pathology.md`。
3. **润色纪律**：骨架优先，变化库只提供措辞变体不替代结构；每句位 ≤2-3 候选；specificity gate 强制具体化；结果以 `### 措辞润色建议` 块附骨架末尾，不覆盖原文。
4. **锚点使用纪律（verbatim anchor）**：设计类型变体的 `原始句锚点` 是来源论文原句的风格参照——**结构跟骨架、语言风味跟锚点**，填入 [placeholder] 后保持语言质地；不逐字复制锚点内容，不保留其专有名词/数字。旧变体无锚点（标注"待补"）时按骨架直接生成。
5. **revision 约束优先**：corpus、phrasebank 与“措辞润色建议”不得覆盖 active feedback 或恢复 `supersedes` 指向的旧建议；已发现相似风险时只借用段落功能、顺序与节奏，重写来源论文的句法骨架并保留标准技术术语。
6. **Methods 语态纪律**：完成的研究程序使用主动过去时；定义、制度事实、公式符号、估计器性质和解释惯例使用现在时。限制与 scope condition 直接陈述，不添加防御性收尾或作者自我评价。
7. **因果语言强制词汇表**（按设计家族，无越级）：

| 设计家族 | 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|---------|
| 面板数据/OLS/FE/HLM | associated with, related to, linked to, corresponds to | increases, decreases, leads to, causes, drives, produces | 无条件禁止强因果词 |
| DiD / 自然实验 | effect of ... on ..., associated with | causes, leads to, drives | 仅在平行趋势/事件研究支持后可用 "effect of... on..."；否则退回 "associated with" |
| IV/2SLS | effect of ... on ..., increases, decreases | causes, leads to, produces | 仅在 M8 识别假设 preview 后可用；second-stage 汇报可用 "effect" 但避免 "causes" |
| 非线性模型 (Logit/Probit/Tobit/计数) | associated with, increases the likelihood of, changes the probability of | increases, decreases, causes, leads to | 系数本身不可直接解释；必须通过边际效应/概率变化转述 |
| 生存分析 | associated with, lengthens/shortens time to, changes the hazard of | causes, leads to, produces | hazard ratio / AFT 系数需通过生存概率或时间变化转述 |
| SEM / 同时方程 | associated with, predicts, influences | causes, leads to, produces | 结构方程系数表示预测关系，非因果；仅在过度识别且模型拟合良好时可谨慎使用 "effect" |
| 实验 | caused, led to, produced, increased, decreased | — | 随机化支持后可直接使用强因果词 |

**完成判据**：所选槽位 QC 点全过（slot 文件末尾 QC 块）；因果语言与设计家族匹配；[placeholder] 无机构/政策名残留。

## 生成后检查

- **反模式自查（先生效）**：`references/anti-patterns.md`（13 项逐条排查）。
- **对齐检查**：`references/cross-section-alignment.md`——检查 1（I6 Preview ↔ M7/M8）+ 检查 2（Theory 假设 ↔ M3-M6 变量）；偏离记录格式按该文件。
- **稳健性归属**：涉及 robustness 归属/M10 预告/M8 边界时读 `references/robustness-menu.md`（归属判断表 + Results 清单 + M10 预告段约束）。
- **自检清单**：`references/post-generation-checklist.md`——Completeness/Clarity/Credibility（含 three-horned dilemma 自我定位 + 四类效度映射）/论证质量诊断/反向审查。
- **确定性语言扫描**：匹配的 active feedback 含 `prohibited_patterns` 时执行 `scripts/lint_methods_language.py <Methods路径> --project <项目名>`；默认在日期化修订记录或“生成后自检记录”前停止，避免将历史反例误报为正文。
- **回归验证**：执行 `references/validation-protocol.md`；skill 结构变更后运行 `scripts/validate_write_methods.py`。

**完成判据**：对齐检查 1/2 无未修复偏离；自检清单逐条全过；反模式零命中。

## 输出合同

按 `references/paper-state-schema.md`：骨架输出末尾自动附加 `### paper-state.yaml 片段` 块（`methods.design_type` / `estimator_family` / `sample` / `variables` / `hypothesis_variable_map` / `story_alignment` / `results_preview` / `robustness_plan`），供 write-results Phase 0 自动消费。用户复制到项目 `paper-state.yaml` 的 `methods:` 节下。

**完成判据**：paper-state 片段全字段；M10 预告不含系数/结论性表述。

## 使用反馈闭环

用户对 Methods 产出提出明确批评、事实纠正、章节边界调整、禁用表达、语态基准或旧建议作废声明时，读取 `references/feedback-protocol.md`：

1. 当前任务包含文稿修改时，先修正文稿，不以“已登记”代替改写；
2. 将本轮批评及现稿修订记录中的明确裁定规范化为可执行规则，按 `skill | project | section | design_type` 登记到 `references/feedback-registry.json`；
3. 新裁定覆盖旧建议时记录 `supersedes`；历史证据保留，但被覆盖内容不再参与生成；
4. 下一次 revision 在生成前加载匹配的 active rules；项目规则不得污染其他论文；
5. `econometric-models/_evidence_registry.yaml` 只保留语料/设计类型的聚合质量信号，不得替代详细 feedback，也不再排除风格、流程和项目写作决策。

## 下游接口

- `/write-results` — 使用本骨架的变量名、模型规格和 M10 预告作为 Results 报告的基准；经 paper-state.yaml 消费 `methods.design_type`、`methods.estimator_family`、`methods.variables`、`methods.hypothesis_variable_map`，自动选择结果类型和构建假设-结果对齐表
- `/paper-review` — Theory-Methods 假设-变量映射对齐检查
- `/methods-review` — 已有 Methods 草稿时作为理想基准对比审查
- `/distill-methods-exemplar` — 对生成后的 Methods 段落进行反向蒸馏审查（槽位覆盖/DNA/可迁移性/因果合规），审查结果作为 Vault 参考注释，不自动修改骨架库

## 纪律

**诚实边界（完整版见 `references/boundaries.md`）**：① 不能替代统计诊断（平行趋势/IV 相关性/共同支撑域等必须基于实际数据）；② 不虚构任何数字（所有系数/p 值/样本量由用户填）；③ 设计排他性不可违反——非 IV 设计不得要求排他性约束、非 DiD 不得要求平行趋势、非匹配不得要求重叠支撑；动态面板必须提示 Nickell bias（T<10 时）。

**反馈登记**：使用 `scripts/record_feedback.py` 维护 `references/feedback-registry.json`。每条反馈必须保留 scope、category、rule、reason、source 和 evidence；语态基准、失效建议和确定性禁用表达分别写入 `benchmark`、`supersedes` 和 `prohibited_patterns`。不得只累计 revise/reject 次数。

**语料质量统计**：`econometric-models/_evidence_registry.yaml` 是次级 corpus 路由资产；只在反馈确实指向某一设计类型变体时汇总 revise/reject。单项目批评不自动修改 corpus，精炼仍由 `distill-methods-exemplar` 驱动。

**语料与变体**：设计类型具体变体见 `econometric-models/[设计类型].md`；新论文蒸馏结果经 `distill-methods-exemplar` → Phase 4 自动写入（同步更新 INDEX.md 变体数）。

---
*基于 34 篇 MVP30 范文语料库、Pollock 2025 Ch07 构建。v3.6.0（2026-08-15：新增现稿锁定、可追溯反馈、旧建议覆盖、项目隔离与确定性语言扫描）。*
