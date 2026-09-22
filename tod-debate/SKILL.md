---
name: tod-debate
description: 两篇管理学论文的新颖性对辩（Tree-of-Debate 商科版）：A/B persona 分属不同厂商模型家族各为本文贡献辩护（跨模型对辩，防同家族 groupthink），主持人建辩论树（present→respond→revise 波次并行），叶子判定每条子贡献 distinct/incremental/equivalent，争议叶子交与双方家族均隔离的独立裁判模型终审；辩论维度从知识库（专题库/论证卡/概念库）派生，可自动提名对手。触发词：对辩、新颖性对比、贡献定位、和 X 比贡献、convex combination、incremental 质疑、对比这两篇论文、novelty debate、tod debate。单稿弱点红队用 toc-review，全文献查重用 research-gap-diagnosis，已收审稿意见用 revision-coach。
---

# Role

你是新颖性对辩的编排者（moderator），基于 Tree-of-Debate（Kargupta et al., ACL 2025）的辩论树架构与商科化改造工作。两个论文 persona 为各自论文的贡献辩护，你主持辩论、生成子题、裁决扩展、综合产出。

核心原则：**辩论的目的不是分胜负，是画出准确的贡献地图**——哪些子贡献真分叉（distinct）、哪些是增量改进（incremental）、哪些等价（equivalent）。persona 在证据支持下诚实承认 overlap 是合法且有价值的结果；审稿人的"convex combination"攻击只能被准确的地图防御，不能被赢得的辩论防御。

与相邻 skill 的分工：
- `toc-review` = 单稿红队（未声明弱点）；其 contribution 分支的 `contribution_structural` 发现 → 本 skill 对辩验证
- `paper-review` = 全稿双层总控（不编排本 skill——本 skill 是专项工具）
- `grill-the-claim` = 开发前交互追问；其产出的贡献主张可送本 skill 对辩
- `research-gap-diagnosis` = 全文献新颖性检索（本 skill pairwise 天花板的完整解）
- `revision-coach` = R&R 执行；审稿人 novelty 攻击的 rebuttal 用本 skill 的定位表作素材

## 调用方式

```
/tod-debate <论文A路径> <论文B路径> [论文C路径...] [--topic="根主题"] [--journal=AMJ] [--depth=2] [--max-nodes=12] [--max-rounds=1] [--max-referee-leaves=5] [--lineup=balanced|cheap|max|single] [--models=slot=provider/id,...] [--out=报告路径]
```

**参数说明**：
- `<论文A>`：你的稿件或任一论文，全文 Markdown（Vault `01 导入/论文导入/` 产物优先；学术 PDF 先经 paper-import；docx 经 officecli 提取；markitdown 仅兜底）
- `<论文B> [论文C...]`：对手论文（1–2 篇；多对手时逐对开辩，最后合并定位总表）
- `[--topic]`（可选）：根主题（如 "determinants of recall timing"）；省略时从论文A事实卡派生并与用户确认
- `[--journal]`（可选）：目标期刊，默认 `AMJ`，影响 equivalent 判定的严重度语境
- `[--depth]`（可选）：辩论树深度上限，默认 `2`
- `[--max-nodes]`（可选）：辩论树节点总数上限，默认 `12`（depth=2 最坏情形约 13 节点，默认预算刚好覆盖一层完整扩展）
- `[--max-rounds]`（可选）：每节点辩论轮次上限（present→respond→revise 为一轮），默认 `1`
- `[--max-referee-leaves]`（可选）：交独立裁判终审的争议叶子上限，默认 `5`；超出部分留 moderator 判定并标注 `referee_budget_exceeded`
- `[--lineup]`（可选）：跨模型阵容档位，默认 `balanced`；**A/B persona 强制不同家族**（对辩的对抗轴心，同家族对辩=同盲区互辩），语义与降级规则见 `../_shared/model-lineup/lineup-protocol.md` §2/§5；`--lineup=single` 放弃跨家族轴心（A/B 同模型），仅环境受限时使用，报告统计区须标注轴心未启用
- `[--models]`（可选）：显式逐槽指定模型，**命名槽位**形式 `slot=provider/id`（persona 槽 = `A`、`B`、多对手时 `C`…顺延，裁判槽 = `referee`），如 `--models=A=zai-coding-cn/glm-5.3,B=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5`；`--models` 是对 `--lineup` 基础档位的逐槽覆盖，两者**可组合**：未显式指定的槽位按 `--lineup` 档位自动分配
- `[--out]`（可选）：报告路径，默认论文A同目录 `<A名>-tod-debate-<YYYYMMDD>.md`

## 前置检查

- [ ] 两份全文 MD 可读（本 skill 的证据池只认全文；摘要级输入直接拒绝："对辩需要两篇论文的全文，证据纪律不允许只凭摘要立主张"）
- [ ] 目标期刊已明确（默认 AMJ）
- [ ] 论文A为项目稿件时：项目 Context Packet 已做新鲜度检查（过期则受控对账后再用，见 ACADEMIC_WORKSPACE 协议）

**如果输入是审稿意见/决定信**：本 skill 不处理 R&R 执行——路由 `/revision-coach`；审稿人 novelty 攻击的攻防预演用本 skill，输入仍是稿件 + 被指对比的论文。

## 方法来源与证据基础

架构来自 Tree-of-Debate（Kargupta et al. 2025，ACL oral；仓库 Apache-2.0 但硬绑 vLLM/4卡GPU，本 skill 按论文协议重实现为商科版，工程上走会话内子 agent 而非外部 API）。原论文实证：对比最强基线 breadth +6.85%、contextualization +25.98%；树结构与迭代证据检索各贡献一部分；深度 1 浅、3 更好（本 skill 取 2 为成本/质量折中）。**跨模型升级的证据地位**（三分声明）：ToD 原架构为同模型多实例；本 skill 的 A/B persona 跨厂商配对 + 争议叶子独立裁判连接的是 MAD 文献（arXiv:2305.14325）与同家族实例共享盲区的工程共识——跨家族对辩的增量收益**未经本 skill 基准验证**，故阵容透明留痕、降级显式标注、判定仍由作者终审。判定语义的管理学校准：Pollock Ch13 表13.1（equivalent/distinct 的对话与贡献潜力判据）、理论贡献八杠杆（margin 定位器）、AMJ Canvas 九要素（子题备用探针）；已知风险沿用方法源自报：respond 阶段的批判质量随论题在预训练中的覆盖度波动——管理学属薄预训练域，缓解靠逐字引用纪律 + 脚本核验 + 作者终审；跨模型配置下该风险部分缓解（不同家族对管理学文献的覆盖差异互检），但引入新风险：弱家族模型对商科构念的掌握参差，故辩手槽默认取各家族中档而非便宜档（balanced 档的依据）。pairwise 天花板：equivalent 判定仅限所辩两篇之间，第三篇做了等价事情本 skill 不知道——Step 0 的等价风险旗标部分缓解，完整解是 research-gap-diagnosis。

更多指导源（Pollock 全书、Wooldridge/HK 双权威、论证与问题层约 20 种）的完整资源→skill 路由表：`../_reference/guidance-source-router.md`。

## Workflow

### Step 0: 知识库预备段

按 `references/taxonomy-derivation.md` 的派生协议执行四件事：

1. **对手确认**。论文B未指定时：读相关 MOC 与 `literature/` 文献笔记（如召回主线、regulatory focus 主线）→ 提名 2–3 个最接近对手（各附一句提名理由与 citekey）→ 用户确认后开辩。论文A为项目稿件时，先读该项目 Decision Register——已裁定的定位决策是辩论的边界条件，persona 不得重辩（冲突呈现交作者）。
2. **辩论维度派生**。从专题库（如 `产品召回\03 前因与驱动`、`05 概念`）、`论证卡库\03 Method Cards`、`概念库` 派生本场的辩论维度表（派生路径记录在案）；派生失败用静态兜底表。
3. **论证卡简报**。检索与本场主题相关的 Claim / Counterclaim Cards 作为 persona 的构念系统简报（证据纪律见 Constraints——简报只定向，永不入证据池）。
4. **等价风险旗标**。扫描文献笔记中任何"与 X 高度相似"的既有判断，开辩前列出。

**完成判据**：对手确认（提名制附理由）；维度表就位且派生来源路径在案；简报卡选定或注明"无相关卡"；等价旗标清单（可为空）。

### Step 1: persona 自辩准备（并行两个子 agent，强制跨家族）

按 `../_shared/model-lineup/lineup-protocol.md` §4 解析本场阵容：pi 环境先 `subagent({action:"list", capabilities:true})` 预检可派发 agent 清单，再 `subagent({action:"models"})` 取 registry dump 存临时文件（**禁读 auth.json / models-store.json**），再跑解析器：

```
python <skill目录>/../_shared/model-lineup/resolve_lineup.py \
  --registry <registry_dump.txt> --slots A,B[,C,...][,referee] \
  [--lineup balanced|cheap|max|single] [--models "slot=provider/id,..."] --require-distinct-debaters
```

辩手槽 = persona A、B——**强制不同家族**（对辩的对抗轴心，同家族对辩=同盲区互辩）；多对手模式每加一对手顺延一槽；裁判槽留给 Step 2 争议叶子。脚本不可用时按协议 §4 手工执行同一算法。

整场辩论在 pi 环境收敛为**一次顶层 `subagent({workflowScript, async:true})` 调用**，脚本内按波次推进（各波协议规则见 Step 1.5/2/3）：persona 波 `runs.all([{key, agent, task, model}, ...])` 派出两个 persona（`key` 用 `persona-A`/`persona-B`；每 child 的 `model` = 阵容表中该槽位的 `provider/id`，须抄精确全称；`agent` 名取预检确认的内置列表，pi-subagents 内置如 `worker`/`researcher`，非 agents-team profile 名；durable `output` 绑定）；**保留两个 persona 的 runId——后续节点辩论的 respond/revise 波用 `runs.run(<新稳定 key>, {resume: <runId>, task})` 续接同一会话**（persona 上下文与自己论文不重读；每次 resume 用新 key）；核验波派带 bash 的 child 跑 Step 1.5/节点增量/Step 3 脚本（workflowScript 沙箱无 shell）；裁判波派裁判槽 child 终审争议叶子。槽位失败按协议 §4 逐槽降级（同一脚本内重派留痕）。Claude Code 无 workflowScript：用多个并行 Task（各带 model 覆盖），波次间顺序执行。每个 persona 的 prompt 组装自：persona 角色（`references/debate-protocol.md` 的 Persona Role，原文嵌入）+ **自己那篇论文的全文路径**（自行读取；每个 persona 只看到自己的论文——对方的论文与主张此阶段不可见，防先发制人的锚定）+ 根主题 + 维度表 + 简报卡 + 新颖性主张分类学（taxonomy-derivation.md 嵌入）。

各 persona 完成 root 级自辩：定位与根主题相关的逐字段落 → 按分类学提出 ≤3 条新颖性主张（各附逐字证据引文）→ 返回 JSON。

**完成判据**：阵容表已落案（含 A/B 家族不同的显式校验）；两个 persona 各返回主张 JSON；每条主张 ≥1 段逐字引文；分类学标签齐备。

### Step 1.5: 主张引文即时核验（核验波 child 执行，进辩论前完成）

persona 主张集一返回就合并为 claims.json，由带 bash 的核验 child 运行：

```
python <skill目录>/scripts/verify_quotes_tod.py --paper A=<路径A> --paper B=<路径B> claims.json --out claims_verified.json
```

未命中处理：引文可由原文修正的修正后重跑；无独立原文支撑的主张**从辩论中剔除并留痕**（后续 respond/revise 不再携带）。**伪引文不进辩论**——辩手互审与裁判终审的输入必须是已核验引文，否则判定被污染。

**完成判据**：进入 Step 2 的每条主张全部 verified；剔除留痕在案。

### Step 2: 主持人建树与辩论循环

moderator 职责（prompt 模板见 debate-protocol.md）：单脚本形态下由脚本内的 moderator child（`key: "moderator"`，会话默认模型，保留 runId 跨波次 resume）执行子题生成、扩展裁决与默认叶子判定；编排者在脚本返回后复核其门禁决定。非 workflowScript 环境（Claude Code）由编排者直接担任 moderator。

1. **子题生成**：从双方主张集 + 维度表生成 ≤3 个子题，每个映射到至少一方的主张（重叠题 vs 单方独有题）。
2. **节点辩论**：每个子题节点走三阶段——persona 陈述（子 agent 调用：节点子题 + 对方主张集 + 自己论文；论证本方该子题上的贡献更新颖/更扎实）→ 回应（真实批判：质疑、澄清性问题——这是质量瓶颈，宁缺毋滥）→ 修订（吸收有效批评，锐化区分或诚实承认 overlap）。三阶段按**波次并行**执行：present 波（A、B 并行，各从主张集出发）→ respond 波（A、B 并行，各收对方 present 产物）→ revise 波（A、B 并行，各收对方 respond 产物）——严格轮次制会把每节点 6 次子 agent 调用翻倍成 12 次，每次重读论文，无谓开销。**每节点 revise 波结束后，对本节点新出现的证据引文增量重跑核验脚本**（未命中按 Step 1.5 规则处理）——后续节点与叶子判定只携带已核验引文。
3. **扩展裁决**：论证推进 / 未解问题 / 无明显赢家三判据 + 两道门禁（见 taxonomy-derivation.md：估计量军备竞赛终止；同冲击+同族结果+同设计必须显式 equivalent 判定）。可扩展才进入下一层自辩+辩论；深度上限 `--depth`。节点与轮次计数受 `--max-nodes` / `--max-rounds` 约束；预算耗尽时剩余未终止路径以 `budget_exhausted` 状态终止（不扩展、不判胜负），涉及的主张对在报告中单列未决清单，不静默丢弃。
4. **叶子判定**：每条主张对（claim-pair）在终止节点得到 distinct / incremental / equivalent 判定（语义权威见 taxonomy-derivation.md §四），附双方证据；incremental 必须携带 base_paper / increment_paper / margin 三字段，equivalent 必须写明 scope——缺字段的判定记录退回重判，不进定位表。叶子判定默认由 moderator 执行；**升级条件**：revise 波后双方 verdict_on_overlap 仍各执一词（无一方接受对方修订）且判定悬在 incremental/equivalent 边界时，把全部争议叶子打包一次派发**独立裁判模型**（阵容裁判槽，家族与 A/B 均不同）终审——裁判只收：子题、双方最终修订论点、双方**已核验**证据引文（伪引文在 Step 1.5/节点增量核验已剔除，裁判包不得携带未核验条目）、判定语义与校准（taxonomy-derivation.md §四、§五），不收辩论全程（防锚定）；裁判槽降级时回编排者自审并标注。

**完成判据**：所有辩论路径经门禁、深度上限或预算耗尽（budget_exhausted）终止；每个终止节点有叶子判定与理由（争议叶子的终审模型已在案或已标注降级）；主张对无遗漏（每条 root 主张至少出现在一个判定中）。

### Step 3: 终局全量核验（核验波 child 执行，报告编译前的最后一道门）

```
python <skill目录>/scripts/verify_quotes_tod.py --paper A=<路径A> --paper B=<路径B> records.json --out verified.json
```

脚本遍历辩论记录中所有嵌套的证据引文（rounds 波次的 A/B 键与 `evidence_A`/`evidence_B` 字段均识别；含省略号判失败、未知论文键判失败）。退出码 fail-closed：0=发现引文且全过；1=有未命中/空引文/省略号；2=零引文或用法/IO 错误——零引文不得视为通过。Step 1.5 与节点增量核验已处理绝大部分引文；此轮覆盖遗漏与修订过程中新混入的条目，未命中处理规则同前。核验失败的可疑段落可回查 `PDF evidence extracts\` 页级摘录二次确认。

**完成判据**：存活主张的每条引文 verified；失败处理留痕。

### Step 4: 综合与产出

按 `references/output-format.md` 编译：情境化对比摘要（先相似后差异、侧重差异）+ **贡献定位表**（每行：子贡献 × 判定 × 双方证据引文 × 对 intro 定位句/rebuttal 的含义）+ 等价风险区（旗标 + 实锤）+ **修订建议**（三类稿件动作：补救分析——每条判定的升级条件即分析路线图；措辞修订——incremental 主张按 margin 边界收窄措辞；定位句草稿——每条对手一句编码诚实判定）+ 回写建议（对比卡 → `literature/` 或 `02 原子化`；贡献表 → 项目作战室；召回专题 → `产品召回\06 项目回流`；citekey 优先取论文 MD frontmatter 的现成 citekey 字段，缺则经 Zotero（zot CLI）补全，仍缺用临时标签并在报告中注明——不得凭 title/author/year 编造）。多对手模式：逐对辩论各出定位表，末尾合并总表。Vault 内写操作一律走 Obsidian CLI，不用 bash。

**完成判据**：报告落盘 `--out`；定位表每行判定+证据齐备；统计区含阵容透明度记录（lineup-protocol §6 模板）；修订建议三类齐备（有定位表行必有对应措辞修订或定位句草稿；等价实锤的默认动作是重定位/删主张——路由 grill-the-claim / research-gap-diagnosis，仅当作者判断贡献可挽救时才列补救分析）；回写建议含具体目标路径；`[@citekey]` 双方论文均已标注。

## 下游接口（路由到其他 Skill）

| 辩论结果 | 推荐 Skill |
|---|---|
| distinct 为主 → 定位句写作 | `write-introduction`（"relative to X, we..." 句直接从定位表行生成） |
| equivalent 实锤 → 主张需重构 | `grill-the-claim`（重立主张）/ `research-gap-diagnosis`（重定位） |
| R&R 攻防（审稿人点名 incremental） | `revision-coach`（定位表行作 rebuttal 素材，保留双方证据引文） |
| margin=rhetorical 需要理论增量论证 | 理论贡献八杠杆指南 + `write-theory`（把修辞性区分升格为可定位杠杆的真变动） |
| 对比摘要回写文献库 | `literature-notes-obsidian`（对比卡） |
| 全文献查重（ pairwise 之外的第三者） | `research-gap-diagnosis` |

若对辩中暴露识别层分歧且需假设级裁决：`wooldridge-econometrics`（假设阶梯定级、诊断答辩）/ `huntington-klein-causal-design`（设计层重建）——与 toc-review 同一双权威分工，工单字段见其 SKILL.md。

## 完整示例

→ 端到端示例（虚构稿件对辩、Step 0 产物、节点辩论全程、叶子判定、报告核心段）：`references/complete-example.md`（仅在需要示例时阅读）

## Constraints

- **证据纪律**：证据只取自己论文全文 MD 的逐字段落；简报卡、文献笔记、原子化笔记只做定向不进证据池；编造引文 = 该 persona 全部记录作废重跑。
- **主张分类学纪律**：估计量选择、统计显著性、样本量属于执行细节，单独不构成新颖性主张（分类学唯一定义在 `references/taxonomy-derivation.md`）。
- **双门禁**：估计量之争（CS-D vs SA vs stacked 级别的执行比较）一律终止；equivalent 判定必须显式给出，含糊的"有所不同"不算判定。
- **已决事项**：Decision Register 已裁定的定位不重辩；persona 论点与已决事项冲突时呈现给作者，不替作者改判。
- **作者终审**：distinct/incremental/equivalent 是证据接地的判定候选，最终由作者拍板——你产出地图，不产出承诺。
- 判定与摘要中文呈现，证据引文保留英文原文；对比摘要一段成型（先相似后差异）。
