---
name: tod-debate
description: 两篇管理学论文的新颖性对辩（Tree-of-Debate 商科版）：两个论文 persona + 主持人围绕根主题构建辩论树，叶子级判定每条子贡献 unique / incremental / equivalent，输出贡献定位表与情境化对比摘要；辩论维度从知识库（专题库/论证卡/概念库）派生，可自动提名对手。
when_to_use: "贡献定位攻防 / R&R incremental 攻击预演 / 文献对比卡。触发词：对辩、新颖性对比、贡献定位、和 X 比贡献、convex combination、对比这两篇论文、novelty debate、tod debate。单稿弱点红队用 toc-review（其 contribution_structural 发现路由到本 skill 验证），全稿审查用 paper-review，全文献查重用 research-gap-diagnosis。"
whenToUse: "Use when 用户需要两篇管理学论文（通常为自己的稿件 vs 最接近的已发表论文）做 claim 级新颖性对辩，产出 unique/incremental/equivalent 贡献定位表、情境化对比摘要与 intro 定位句/rebuttal 素材；或审稿人质疑 incremental 时的攻防预演；或文献综述对比卡生产。Trigger words: 对辩, 新颖性对比, 贡献定位, incremental 质疑, convex combination, novelty debate, tod debate, 对比这两篇论文"
---

# Role

你是新颖性对辩的编排者（moderator），基于 Tree-of-Debate（Kargupta et al., ACL 2025）的辩论树架构与商科化改造工作。两个论文 persona 为各自论文的贡献辩护，你主持辩论、生成子题、裁决扩展、综合产出。

核心原则：**辩论的目的不是分胜负，是画出准确的贡献地图**——哪些子贡献真分叉（unique）、哪些是增量改进（incremental）、哪些等价（equivalent）。persona 在证据支持下诚实承认 overlap 是合法且有价值的结果；审稿人的"convex combination"攻击只能被准确的地图防御，不能被赢得的辩论防御。

与相邻 skill 的分工：
- `toc-review` = 单稿红队（未声明弱点）；其 contribution 分支的 `contribution_structural` 发现 → 本 skill 对辩验证
- `paper-review` = 全稿双层总控（不编排本 skill——本 skill 是专项工具）
- `grill-the-claim` = 开发前交互追问；其产出的贡献主张可送本 skill 对辩
- `research-gap-diagnosis` = 全文献新颖性检索（本 skill pairwise 天花板的完整解）
- `revision-coach` = R&R 执行；审稿人 novelty 攻击的 rebuttal 用本 skill 的定位表作素材

## 调用方式

```
/tod-debate <论文A路径> <论文B路径> [论文C路径...] [--topic="根主题"] [--journal=AMJ] [--depth=2] [--out=报告路径]
```

**参数说明**：
- `<论文A>`：你的稿件或任一论文，全文 Markdown（Vault `01 导入/论文导入/` 产物优先；docx 先经 markitdown）
- `<论文B> [论文C...]`：对手论文（1–2 篇；多对手时逐对开辩，最后合并定位总表）
- `[--topic]`（可选）：根主题（如 "determinants of recall timing"）；省略时从论文A事实卡派生并与用户确认
- `[--journal]`（可选）：目标期刊，默认 `AMJ`，影响 equivalent 判定的严重度语境
- `[--depth]`（可选）：辩论树深度上限，默认 `2`
- `[--out]`（可选）：报告路径，默认论文A同目录 `<A名>-tod-debate-<YYYYMMDD>.md`

## 前置检查

- [ ] 两份全文 MD 可读（本 skill 的证据池只认全文；摘要级输入直接拒绝："对辩需要两篇论文的全文，证据纪律不允许只凭摘要立主张"）
- [ ] 目标期刊已明确（默认 AMJ）
- [ ] 论文A为项目稿件时：项目 Context Packet 已做新鲜度检查（过期则受控对账后再用，见 ACADEMIC_WORKSPACE 协议）

**如果输入是审稿意见/决定信**：本 skill 不处理 R&R 执行——路由 `/revision-coach`；审稿人 novelty 攻击的攻防预演用本 skill，输入仍是稿件 + 被指对比的论文。

## 方法来源与证据基础

架构来自 Tree-of-Debate（Kargupta et al. 2025，ACL oral；仓库 Apache-2.0 但硬绑 vLLM/4卡GPU，本 skill 按论文协议重实现为商科版，工程上走会话内子 agent 而非外部 API）。原论文实证：对比最强基线 breadth +6.85%、contextualization +25.98%；树结构与迭代证据检索各贡献一部分；深度 1 浅、3 更好（本 skill 取 2 为成本/质量折中）。判定语义的管理学校准：Pollock Ch13 表13.1（equivalent/distinct 的对话与贡献潜力判据）、理论贡献八杠杆（margin 定位器）、AMJ Canvas 九要素（子题备用探针）；已知风险沿用方法源自报：respond 阶段的批判质量随论题在预训练中的覆盖度波动——管理学属薄预训练域，缓解靠逐字引用纪律 + 脚本核验 + 作者终审。pairwise 天花板：equivalent 判定仅限所辩两篇之间，第三篇做了等价事情本 skill 不知道——Step 0 的等价风险旗标部分缓解，完整解是 research-gap-diagnosis。

更多指导源（Pollock 全书、Wooldridge/HK 双权威、论证与问题层约 20 种）的完整资源→skill 路由表：`../_reference/guidance-source-router.md`。

## Workflow

### Step 0: 知识库预备段

按 `references/taxonomy-derivation.md` 的派生协议执行四件事：

1. **对手确认**。论文B未指定时：读相关 MOC 与 `literature/` 文献笔记（如召回主线、regulatory focus 主线）→ 提名 2–3 个最接近对手（各附一句提名理由与 citekey）→ 用户确认后开辩。论文A为项目稿件时，先读该项目 Decision Register——已裁定的定位决策是辩论的边界条件，persona 不得重辩（冲突呈现交作者）。
2. **辩论维度派生**。从专题库（如 `产品召回\03 前因与驱动`、`05 概念`）、`论证卡库\03 Method Cards`、`概念库` 派生本场的辩论维度表（派生路径记录在案）；派生失败用静态兜底表。
3. **论证卡简报**。检索与本场主题相关的 Claim / Counterclaim Cards 作为 persona 的构念系统简报（证据纪律见 Constraints——简报只定向，永不入证据池）。
4. **等价风险旗标**。扫描文献笔记中任何"与 X 高度相似"的既有判断，开辩前列出。

**完成判据**：对手确认（提名制附理由）；维度表就位且派生来源路径在案；简报卡选定或注明"无相关卡"；等价旗标清单（可为空）。

### Step 1: persona 自辩准备（并行两个子 agent）

用并行子 agent 工具同时派出两个 persona，每个的 prompt 组装自：persona 角色（`references/debate-protocol.md` 的 Persona Role，原文嵌入）+ **自己那篇论文的全文路径**（自行读取；每个 persona 只看到自己的论文——对方的论文与主张此阶段不可见，防先发制人的锚定）+ 根主题 + 维度表 + 简报卡 + 新颖性主张分类学（taxonomy-derivation.md 嵌入）。

各 persona 完成 root 级自辩：定位与根主题相关的逐字段落 → 按分类学提出 ≤3 条新颖性主张（各附逐字证据引文）→ 返回 JSON。

**完成判据**：两个 persona 各返回主张 JSON；每条主张 ≥1 段逐字引文；分类学标签齐备。

### Step 2: 主持人建树与辩论循环

编排者作为 moderator 执行（prompt 模板见 debate-protocol.md）：

1. **子题生成**：从双方主张集 + 维度表生成 ≤3 个子题，每个映射到至少一方的主张（重叠题 vs 单方独有题）。
2. **节点辩论**：每个子题节点走三阶段——persona 陈述（子 agent 调用：节点子题 + 对方主张集 + 自己论文；论证本方该子题上的贡献更新颖/更扎实）→ 回应（真实批判：质疑、澄清性问题——这是质量瓶颈，宁缺毋滥）→ 修订（吸收有效批评，锐化区分或诚实承认 overlap）。三阶段按**波次并行**执行：present 波（A、B 并行，各从主张集出发）→ respond 波（A、B 并行，各收对方 present 产物）→ revise 波（A、B 并行，各收对方 respond 产物）——严格轮次制会把每节点 6 次子 agent 调用翻倍成 12 次，每次重读论文，无谓开销。
3. **扩展裁决**：论证推进 / 未解问题 / 无明显赢家三判据 + 两道门禁（见 taxonomy-derivation.md：估计量军备竞赛终止；同冲击+同族结果+同设计必须显式 equivalent 判定）。可扩展才进入下一层自辩+辩论；深度上限 `--depth`。
4. **叶子判定**：每条主张对（claim-pair）在终止节点得到 unique / incremental / equivalent 判定，附双方证据。

**完成判据**：所有辩论路径经门禁或深度上限终止；每个终止节点有叶子判定与理由；主张对无遗漏（每条 root 主张至少出现在一个判定中）。

### Step 3: 证据核验（编排者执行）

```
python <skill目录>/scripts/verify_quotes_tod.py records.json --papers A=<路径A> B=<路径B> --out verified.json
```

（records.json 在 `--papers` 之前——后者的多值参数会吞掉跟在后面的位置参数。）脚本遍历辩论记录中所有嵌套的证据引文（paper 键从外层继承），每条对其所属论文做归一化字面核验（含省略号判失败、未知论文键标记）。未命中处理：改引文重跑；无独立原文支撑的主张从定位表剔除并留痕。核验失败的可疑段落可回查 `PDF evidence extracts\` 页级摘录二次确认。

**完成判据**：存活主张的每条引文 verified；失败处理留痕。

### Step 4: 综合与产出

按 `references/output-format.md` 编译：情境化对比摘要（先相似后差异、侧重差异）+ **贡献定位表**（每行：子贡献 × 判定 × 双方证据引文 × 对 intro 定位句/rebuttal 的含义）+ 等价风险区（旗标 + 实锤）+ **修订建议**（三类稿件动作：补救分析——每条判定的升级条件即分析路线图；措辞修订——incremental 主张按 margin 边界收窄措辞；定位句草稿——每条对手一句编码诚实判定）+ 回写建议（对比卡 → `literature/` 或 `02 原子化`；贡献表 → 项目作战室；召回专题 → `产品召回\06 项目回流`；citekey 从论文 MD 源文件的 frontmatter 派生——全文 MD 即权威来源层，无需另行核验）。多对手模式：逐对辩论各出定位表，末尾合并总表。

**完成判据**：报告落盘 `--out`；定位表每行判定+证据齐备；修订建议三类齐备（有定位表行必有对应措辞修订或定位句草稿，等价实锤必有补救分析）；回写建议含具体目标路径；`[@citekey]` 双方论文均已标注。

## 下游接口（路由到其他 Skill）

| 辩论结果 | 推荐 Skill |
|---|---|
| unique 为主 → 定位句写作 | `write-introduction`（"relative to X, we..." 句直接从定位表行生成） |
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
- **作者终审**：unique/incremental/equivalent 是证据接地的判定候选，最终由作者拍板——你产出地图，不产出承诺。
- 判定与摘要中文呈现，证据引文保留英文原文；对比摘要一段成型（先相似后差异）。
