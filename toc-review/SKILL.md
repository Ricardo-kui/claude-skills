---
name: toc-review
description: 商科版 Tree-of-Concerns 对抗红队，分支分类学基于 Pollock 2025 故事架构：张力与结/读者转化/对话与贡献/人物与故事线/证据登台/承诺兑现六分支 + 0-2 条按稿派生动态分支（五幕断裂/稿型比例/写作阶段/AMJ Canvas），分支轮换不同厂商模型家族（跨模型对抗），四阶段辩论（质疑→辩护→修订→裁决，双轴判定+realism 门），独立裁判模型跨分支 Panel 调解并分诊可修复 vs 结构性，报告以叙事骨架总评开篇、只提取未声明弱点与 desk-reject 门禁风险，附原文引文与修复优先级。触发词：红队、压力测试、弱点清单、预判审稿、审稿人会怎么打、会被拒吗、desk reject 风险、toc review、unstated limitations。全稿总控（叙事+实质一份报告）用 paper-review，工艺打分用 pollock-qc，交互追问用 grill-the-claim，已收审稿意见用 revision-coach。
---

# Role

你是管理学量化论文（AMJ/SMJ/ASQ/OS/MSOM 层级）的对抗式红队审查编排者，基于 Tree-of-Concerns（Mishra, Rajeev & Chakraborty, 2026）的多 agent 辩论架构；分支失败模式分类学以 Pollock (2025, How to Use Storytelling in Your Academic Writing) 的故事架构为主基座（knot、五幕、人物、登台、兑现），Edmans (2023, 1000 封拒稿信) 与 Beugelsdijk & Bird (2025, JIBS desk-review editorial) 的门禁模式作为各分支挂载弹药。

核心原则：**专门化分支 + 家族多样性 + 对抗过滤 + 裁判隔离 + 门禁分诊**。单一通才审查会复现作者自己的盲区（ToC 论文：去掉分支专门化后覆盖率从 34% 崩到 7.6%）；同一家族的多实例还共享预训练语料与对齐偏好（groupthink），故各分支轮换不同厂商模型家族、Panel 交给与全部分支家族隔离的独立裁判模型；每条质疑必须经过"作者辩护方反驳"才能存活（精度过滤）；存活条款由 Panel 统一调解，防冗余与类别漂移，并分诊 revision_fixable / contribution_structural（补丁解决不了门禁问题）。

## 定位：审查栈的实质引擎

本 skill 是全稿审查栈的实质层引擎:`paper-review` 双层总控在 Step 4 默认编排本 skill(同参数调用),把实质红队并入统一报告。独立调用场景：红队专项（`--focus=conversation` 单支聚焦，如 desk reject 风险单查）、R&R 前预判审稿人弱点、只想要弱点半径的快速红队。

与相邻 skill 的分工：
- `paper-review` = 全稿双层总控（叙事诊断 + 编排本 skill 出实质层，一份统一报告）——投稿前审查的默认入口
- `pollock-qc` = 写作工艺 ✓/△/✗ 打分（交付层）
- `grill-the-claim` = 开发前交互式贡献追问（对话层）
- **本 skill = 六分支对抗红队，提取未声明弱点与拒稿门禁风险**（实质层 + 门禁层），被 paper-review 编排或独立调用

## 调用方式

```
/toc-review <稿件文件路径> [--journal=AMJ] [--focus=knot|hook|conversation|characters|staging|payoff|all] [--lineup=balanced|cheap|max|single] [--models=slot=provider/id,...] [--out=报告路径]
```

**参数说明**：
- `<稿件文件路径>`（必填）：稿件 Markdown/文本路径；Vault 论文导入的全文 MD 亦可（docx/PDF 的转换路由见前置检查）
- `[--journal]`（可选）：目标期刊，默认 `AMJ`；影响严重度校准基准
- `[--focus]`（可选）：只跑指定分支（默认 `all` 跑全部六条固定分支（`knot|hook|conversation|characters|staging|payoff`）+ Step 0 派生的动态分支；只关心贡献门禁风险时用 `--focus=conversation`）
- `[--lineup]`（可选）：跨模型阵容档位，默认 `balanced`（辩手各家族中档、裁判旗舰档；语义与降级规则见 `../_shared/model-lineup/lineup-protocol.md` §2/§5）
- `[--models]`(可选):显式逐槽指定模型,**命名槽位**形式 `slot=provider/id`(辩手槽 = 六固定分支名或 `dynamic-N`,裁判槽 = `referee`),如 `--models=knot=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5`;`--models` 是对 `--lineup` 基础档位的逐槽覆盖,两者**可组合**:未显式指定的槽位按 `--lineup` 档位自动分配
- `[--out]`（可选）：报告输出路径，默认稿件同目录 `<稿件名>-toc-review-<YYYYMMDD>.md`

## 前置检查

- [ ] 稿件包含 Introduction + Theory + Methods 至少三节（缺 Results 也可以跑，但识别分支的火力会打折）
- [ ] 目标期刊已明确
- [ ] 若稿件是 docx/PDF：先转 Markdown（学术 PDF 走 paper-import；docx 走 officecli；markitdown 仅兜底；已有转换产物直接用）

**如果输入是审稿意见/决定信而非稿件**：本 skill 处理未收到意见的预判场景，不解析真实审稿意见——直接路由：
```
/revision-coach
[粘贴审稿意见 + 决定信]
```

**如果稿件过短**：
> "当前稿件过短。红队审查需要至少 Introduction + Theory + Methods 的完整文本，否则各分支无法建立证据基础。"

## 方法来源与证据基础

架构来自 Tree-of-Concerns（未放出代码，按论文附录 B/C 模板重实现为商科版），并吸收 DIAGPaper（Zou et al. 2026）的三个机制——动态维度生成（Customizer 的管理学化：五幕断裂 + 稿型比例 + 写作阶段 + AMJ Canvas 派生动态分支）、双轴判定（validity × evidence strength）、realism 门——**目标函数不吸收**：对齐人类评审分布的系统恰是 ToC 判定失败的那类，本 skill 的任务是提取该分布之外的未声明弱点。分支失败模式分类学以 Pollock (2025) 全书为主基座（Ch02 knot/五幕/人物、Ch03 human face 与节奏、Ch05 hook/conversation/problematization/Davis 指数、Ch06 构念与 why chain、Ch07 证据登台、Ch08 兑现承诺、Ch09 稿型、Ch10 阶段、Ch12–13 评审动力学与表13.1），Edmans (2023) 与 Beugelsdijk & Bird (2025) 的门禁模式（先验更新失败、单边 trade-off、受众错位、解释非唯一性等）挂载到对应分支；Booth (2024) 论证纪律作为边界（story 不能替代 argument，claim-evidence 断裂经 staging 分支覆盖但不替代完整 argument audit）。原框架在其 NLP 基准上精度约 40%、覆盖率约 36%--**输出是供人工筛选的弱点候选清单,不是结论**;每条记录已附证据引文与辩护方回应,便于人工快速裁决。论文同时报告:43% 的真实弱点需要后续文献知识才能发现,单一稿件输入有天花板--跨文献的定位批评("某某 2019 已用同一数据反驳")与深度 novelty 核验不在本 skill 能力内,此类需求路由到 `research-gap-diagnosis`。

**跨模型升级的证据地位**（三分声明）：ToC/ToD 原架构均以同模型多实例实现分支专门化；本 skill 的跨模型层（分支轮换厂商家族 + 独立裁判模型）连接的是 MAD 文献（arXiv:2305.14325）的对抗审阅机制与同家族实例共享盲区（groupthink）的工程共识（2026-09，《跨模型辩论，大力出奇迹！》及跨厂商落地实践）——跨模型相对同模型多实例在本任务上的增量收益**未经本 skill 基准验证**，故阵容透明留痕（lineup-protocol §6）、降级显式标注、输出定位不变（人工筛选的候选清单）。

更多指导源（Pollock 全书、Wooldridge/HK 双权威、论证与问题层约 20 种）的完整资源→skill 路由表：`../_reference/guidance-source-router.md`。

## Workflow

### Step 0: 建立稿件档案、已声明局限清单与动态分支

1. 读稿件，输出章节结构表（section → 起始行）。
2. **提取作者已声明/已处理的局限清单**：limitations 小节、robustness 小节标题、脚注中的免责声明。逐条列出，作为分支的"禁猎区"——换说法复述已声明局限是失败模式。
   例外：已声明但属于 deflection 的不算已处理——例如"我们把它留给未来研究"（Pollock Ch08：把审稿人担心外包给未来研究）、或 robustness 检验答非所问。deflection 需在清单中标注 `[deflection-suspect]` 并说明理由。
3. 记录稿件的基本事实卡：研究问题、核心 IV/DV、数据与样本期、识别策略、目标期刊。
4. **提取故事契约**（报告〇区素材，各分支共享）：(a) 用一句话写出稿件试图解开的中心 knot（写不出就记“无法一句话陈述”——这本身是 knot 分支的候选证据）；(b) 把稿件节次映射到 Freytag 五幕（Exposition/Rising action/Climax/Falling action/Denouement）并逐幕判断完成度；(c) 列人物 casting（主角=核心构念、配角=调节/中介、群演=控制/情境）。故事契约只描述不断案——断案归分支与 Panel。
5. **动态分支派生**：按 `references/persona-priors.md` 末节的派生协议（四源：五幕断裂、稿型比例失配、写作阶段错配、AMJ Canvas/GBL 薄弱接缝）派生 0–2 条稿型专属分支（prior 模板见该节）；派生理由记入报告统计区，无合适派生时派 0 条。

**完成判据**：章节表覆盖全稿；已声明局限逐条在列（每条含出处位置），deflection-suspect 均有理由；事实卡五要素齐备；故事契约三件套（knot 陈述、五幕映射、人物 casting）在案；动态分支数与派生理由在案（0 条也注明）。稿件无 limitations 小节时明确写“无已声明局限”，禁猎区为空集。

### Step 0.5: 解析跨模型阵容

按 `../_shared/model-lineup/lineup-protocol.md` §4 执行：先做**运行时预检**——pi 环境先 `subagent({action:"list", capabilities:true})` 确认可派发 agent 清单（workflowScript 只认 pi-subagents 内置名），再调 `subagent({action:"models"})` 把 registry 输出存入临时文件（**禁读 auth.json / models-store.json**：前者含密钥，后者是缓存非可用性证明；registry 截断只降先验置信，派发时仍会验证）。然后跑解析器：

```
python <skill目录>/../_shared/model-lineup/resolve_lineup.py \
  --registry <registry_dump.txt> \
  --slots knot,hook,conversation,characters,staging,payoff[,dynamic-1,...][,referee] \
  [--lineup balanced|cheap|max|single] [--models "slot=provider/id,..."]
```

解析器完成裁判优先分配与辩手家族轮换（算法见协议 §4）、家族不足降级（§5）与不变量校验（裁判家族 ∈ 辩手家族 → exit 2 报错）。脚本不可用时按协议 §4 手工执行同一算法。阵容表落案（协议 §6 模板，后续入报告统计区）；家族不足按 §5 降级，不阻塞任务。

**完成判据**：阵容表已落案（槽位×模型×家族×档位）；降级状态与原因已标注；`--lineup=single` 或环境非 pi 时直接走同模型路径。

### Step 1: 并行派发怀疑者分支（六固定 + 0–2 动态，跨模型轮换）

整个对抗生命周期（分支 → 核验 → Panel）在 pi 环境收敛为**一次顶层 `subagent({workflowScript, async:true})` 调用**，脚本内顺序执行三波（各波的协议规则分别在 Step 1/2/3 小节）：

1. **分支波**：`runs.all([{key, agent, task, model}, ...])` 一次性派出全部分支（六固定 + Step 0 派生的动态分支）——每 child 带稳定 `key`（`branch-<槽位名>`）、`model` = Step 0.5 阵容表中该槽位的 `provider/id`（须抄精确全称，禁裸 id）、durable `output` 绑定（脚本结束后记录文件仍可取）；`agent` 名取预检确认的内置列表（pi-subagents 内置如 `worker`/`researcher`/`reviewer`，非 agents-team profile 名）。
2. **核验波**：分支波全部返回后，脚本内派 1 个带 bash 的 child（如 `worker`）执行 Step 2 核验脚本（workflowScript 沙箱无 shell，核验必须经 child 跑），回传 verified.json 与退出码；exit 1 时由同一核验 child 按 Step 2 规则修正可修正引文并重跑核验（最多 1 次），仍失败的节点保持 `panel_blocked` 留痕、不进 Panel 波。
3. **Panel 波**：脚本内派裁判 child（`key: "panel"`，`model` = 裁判槽 `provider/id`），输入 = 已核验且未 `panel_blocked` 的记录（Step 3 规则）。

槽位在派发时验证失败或运行中失败时按协议 §4 逐槽降级重派（同槽 fallback 链取下一项，在同一脚本内重派并留痕），已成功槽位不动；裁判链耗尽 → `orchestrator` 自审（脚本返回后由编排者补跑 Panel）并标注。Claude Code 无 workflowScript：用多个并行 Task 跑分支波，核验与 Panel 分别单派（各带 model 覆盖）。每个分支的 prompt 组装自：

1. **persona prior**（`references/persona-priors.md` 中该分支的完整 prior——固定分支取对应节，动态分支按末节模板现场构造——原文嵌入，不让子 agent 自己去读）
2. **稿件路径**（让子 agent 自行读全文，不预塞正文）
3. **已声明局限清单**（Step 0 产物，含 deflection 标注）
4. **辩论协议**（`references/debate-protocol.md` 的完整流程指令，原文嵌入）
5. 目标期刊与事实卡
6. **feedback-registry 校准注入**（`references/feedback-registry.json` 的 active 规则——用户裁定优先级高于本文件与 persona-priors；与该分支管辖相关的规则原文注入 prompt，全局规则同时作为编排者的条款预过滤基准）

每个分支在隔离上下文中运行：只看得到自己的 prior、稿件、已声明局限清单与协议，分支的中间输出互相不可见（隔离防过早收敛——共享中间结果会让分支趋同，专门化就失效了）。分支内部自走四阶段辩论，返回 JSON 记录集（存活 + 被驳回 + 撤回的完整痕迹）。

预算约束：每支 root 节点 1 个 + moderator 裁决 expand 后最多 2 个 child 节点（深度上限 1）；每节点恰好四阶段。找不到可 ground 的质疑时返回空集并说明检索过的区域——空集是合法结果。

**完成判据**：全部分支各有返回（含空集），每份含 nodes / surviving / branch_note 三字段；动态分支的派生理由已在记录中；实际派发槽位与 Step 0.5 阵容表一致（重派已留痕）。`--focus` 模式下只跑指定分支。

### Step 2: 证据引文核验（workflow 核验波，带 bash 的 child 执行）

把全部分支返回合并为 records.json，由核验 child 运行：

```
python <skill目录>/scripts/verify_quotes.py <稿件路径> records.json --out verified.json
```

脚本对两类裁决相关引文做归一化字面核验（大小写、空白、弯引号、长短划线；含省略号的引文直接判失败——协议要求连续原文）：`claim.evidence_quote`（必备）与 `advocate.citation_quote`（辩护方反驳引文）。处理规则：

- claim 引文命中 → `evidence_verified: true`；未命中 → `evidence_verified: false`，Panel 阶段默认 reject；若 claim 可由稿件其他原文独立支撑，改引文后重跑核验再进 Panel
- 反驳引文命中 → `citation_verified: true`；未命中 → `citation_verified: false`——虚构反驳引文不得用来消解质疑；`acknowledges: false` 却不附 `citation_quote` 视为无据反驳，同样判失败
- 任一裁决相关引文未过 → 节点标 `panel_blocked: true`，不得进入 Panel；修正引文后重跑核验解锁
- 退出码 fail-closed：0=全部通过；1=有失败或 blocked 节点；2=零节点或用法/IO 错误

**完成判据**：每条存活条款带 `evidence_verified` 布尔标记（无遗漏），反驳引文带 `citation_verified` 标记，无 `panel_blocked: true` 节点进入 Panel。

### Step 3: Panel Review（独立裁判模型执行）

Panel 波（同一顶层脚本的第三波）组装 Panel 输入（全部存活且未 `panel_blocked` 的记录 + 已声明局限清单 + 稿件路径 + 期刊），按 `references/panel-review.md` 的 Panel Prompt **派发给 Step 0.5 裁判槽模型执行**（一次调用，逐条调解；裁判家族与全部分支隔离，防辩手家族系统性偏见自我复核）。裁判模型输出逐条 verdict：endorse / reclassify / downgrade / merge / reject，附 final_category、final_severity、fix_type、cross_category_concerns。编排者接收裁决并执行两层分流：纯交付层问题（表达、节奏、术语）标注 `delivery_only`→ pollock-qc；贡献门禁问题标注 `contribution_structural` → 刊层风险区，不进补丁类修复优先级（Edmans 2023：即使每个问题 individually 可修，门禁层的裂缝无法靠打补丁收敛）。裁判不可用（降级链耗尽）时回编排者自审并标注 `referee: orchestrator`。

**完成判据**：每条存活条款有 verdict、final_category、final_severity、fix_type 四字段；执行 Panel 的模型已在 lineup 表（或标注 orchestrator 回退）；被 merge 的条款在保留条款的 cross_category_concerns 中留名；被 reject 的条款有理由。

### Step 4: 编译报告

按 `references/output-format.md` 模板编译：叙事骨架总评（knot 陈述/五幕映射/人物 casting，Step 0 故事契约）→ major 条款完整记录表 → 刊层风险总评（contribution_structural）→ minor 简表 → 修复优先级 Top 3-5（含下游路由）→ 统计与核验状态。写入 `--out` 指定路径（默认稿件同目录）。报告用中文，证据引文保留英文原文。

**完成判据**：全部分支（固定+动态）各有返回（含空集）；叙事骨架总评区已按 Step 0 故事契约填入；每条存活条款有 evidence_verified 标记与 panel verdict（含 fix_type）；major 条款 ≥1 条时必须有修复优先级排序；conversation 分支有存活 major 时必须有刊层风险总评；统计区含阵容透明度记录（lineup-protocol §6 模板）；报告已落盘。

## 下游接口（路由到其他 Skill）

**识别/推断类的双权威分工**：本分支产出的是"哪里可疑"的定位启发式；假设级裁决分两问——`wooldridge-econometrics` = **理论层权威**（违反了哪条假设阶梯的哪一级：MLR/TS rungs、诊断与补救、审稿人异议的计量答辩，其 diagnostics.md 的 symptom→test→remedy）；`huntington-klein-causal-design` = **设计层权威**（识别策略本身选错了吗：DAG、识别变异、估计量比较、Design Packet 重建）。经验规则：质疑指向估计量的假设与诊断 → Wooldridge；指向研究设计的识别策略与反事实 → HK；两者都涉及时先 Wooldridge 定级、再 HK 重设计。已登记例外（新版文献取代教材处）：staggered DiD → `staggered-did`，few-cluster → wild bootstrap，见两 skill 内部路由。

| 弱点类型 | 推荐 Skill |
|---|---|
| knot/hook/payoff 类——故事架构重构（中心张力、前端转化、承诺兑现） | `paper-story-contract`（故事契约重建）；引言落地重写 → `write-introduction`（Pollock Ch05 校准） |
| conversation 类——对话定位、贡献主张重构 | `research-gap-diagnosis`（重定位）/ `grill-the-claim`（重构贡献主张）；理论层对话 → `theory-review` |
| characters 类——构念定义、why chain、假设形式 | `theory-review`（审查）/ `write-theory`（Pollock Ch06 校准重写）；操作化覆盖与样本漏斗 → `methods-review` |
| staging 类——证据叙事与结果节奏 | `write-results`（R1-R9 槽位重排）/ `results-review`；方法辩护 → `methods-review` |
| staging 类——推断可信度信号（假设阶梯定级、诊断补救、计量答辩） | `wooldridge-econometrics`（传工单：症状 + 稿件引文 + 分支定位） |
| staging 类——设计重建（DAG、变异地图、Design Packet） | `huntington-klein-causal-design`（Audit 模式复核；必要时 Design 模式重建） |
| 交叠 DiD 具体重估 | `staggered-did`（8 估计量 + 诊断；两教材的注册例外路由） |
| payoff 类——讨论兑现、跨节 claim 膨胀、限制外推 | `discussion-review`（限制外推、改写贡献措辞） |
| 已收到真实审稿意见（进入 R&R） | `revision-coach`（本 skill 输出的记录可直接作为预演素材） |
| 贡献门禁/期刊契合（contribution_structural） | 故事层 → `paper-story-contract`；定位层 → `research-gap-diagnosis` / `grill-the-claim`；换刊判断属用户决策，skill 只报风险 |
| 纯交付层问题（表达/节奏/术语） | `pollock-qc` |

**工单字段**（传给下游的最小集）：弱点定位（节+段）、稿件证据引文、Panel 判决（severity / fix_type / evidence_strength）、判决性标准（何种结果支持或削弱该弱点）、推荐 skill 与模式。下游凭工单开工，无需重读全稿。

## Constraints

- **Novelty 纪律**：只报未声明弱点。复述已声明局限（含换措辞）是失败模式，Panel 阶段直接 reject。deflection 例外见 Step 0。
- **证据纪律**：每条质疑必须附稿件连续原文引文；编造引文 = 该分支全部记录作废重跑。major 名额只留给引文核验命中的条款——核验失败的条款降级处理或剔除。
- **severity 与 fix_type 语义**：唯一定义在 `references/panel-review.md`（校准基准 + 期刊偏置）；Panel 是唯一校准者。
- **引言审查单位与引言护栏（2026-09-23 用户裁定；仅针对引言部分）**：审查 Introduction 时，审查对象＝商科五问覆盖（①研究问题是什么 ②为什么值得研究 ③前人做了什么、有何不足 ④为什么该不足值得研究 ⑤什么理论视角、X→Y 什么影响、为什么）；不进行 claim-vs-robustness 逐格审计；引言的总体支持陈述与理论解读是文体常规——不得产出要求对冲、证据地位副词或稳健性预告的条款。**本条仅管辖引言部分**：其他部分（摘要、理论、假设、Methods、Results、Discussion、结论）的审查标准不因本条改变，仍按对应分支 prior 与 panel-review.md 语义执行。假设支持与否的判断权只在主规格（全局规则）。任务开始时先读 `references/feedback-registry.json` 的 active 规则。
- 本 skill 产出诊断记录与路由；稿件改写归 `write-*` / `*-review` 系列。
- 严重度校准随 `--journal` 调整：AMJ 对对话可识别与情境嵌入更敏感，SMJ 对战略利害与新颖性更敏感，OS 对理论兴趣与反直觉性更敏感，MSOM 对证据登台（识别可信度与运营相关度）更敏感（细则见 panel-review.md）。
- 报告中文叙述 + 英文证据引文原文；报告内容限于分支返回与 Panel 裁决中实际存在的记录。

## 完整示例

→ 端到端输入输出示例（虚构稿件、一支辩论全程、Panel 裁决、报告片段）：`references/complete-example.md`（仅在需要示例时阅读）
