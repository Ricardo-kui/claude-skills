# write-introduction + 两库分层 优化方案（最终版 · 2026-09-14）

> 依据：`~/.pi/skills/writing-for-agents/SKILL.md` 的写作杠杆 + 五路只读审计（write-introduction 文档/语料层、检索与 registry 层、跨 skill 契约层、story-blueprints 资产分层、corpus 分层与重复度）+ Kimi 方案（12 条）逐条裁决。
> **裁定已定**：`corpus/story-archetypes/` 上收 story-blueprints 作 worked example（见 §5 P1-5.7 的三拆分迁移）。
> 本文件为方案定稿；落地完成后归档或删除，避免成为第二事实源。

---

## 0. 结论摘要

1. **Kimi 的 P0 五条与今日 15:21–15:23 已落盘的补丁逐条重合**（映射表 / 语料吸收证明 / anti-defense budget / God-view detector / professional-expression gate 均已在 `corpus-first-generation.md` 与 `style-fidelity-gate.md` 内，God-view 触发词表甚至逐字相同）。追加即重复建设。真正的问题不是"还没想到这些规则"，而是这批规则写成了**文件里的参考**，没有写成**带产物的步骤**——参考型规则不会被生成动作调用，自评型完成判据会被提前判定通过。那批补丁是 15:08 复盘后的编码，**尚未被任何一次生成验证过**。
2. **Kimi 未触及本轮最大发现**：两个库都不在你要的层上——story-blueprints 的段落级信息（Five acts）未入 catalog、且被自身 schema 禁止当模板；corpus 的段级卡 verbatim 半被功能说明遮蔽且无稳定 id；Phase 2 的段落大纲由 write-introduction 从 gap_type 查表自造，与 story-blueprints **零接线**。
3. **最终方案 = 层合同（不搬库）+ 一个缺层（大纲）+ 两个调用接口（索引 / 形状包）+ 举证型 PASS + 重写门**。从 Kimi 采纳 4 项（形状包、对照卡、期刊维度、逐卡缺失条件），从你的自我诊断补 1 项机制（底本覆盖率 → 重写门）。
4. **story-archetypes 裁定**：上收 story-blueprints 作 worked example；其内容按三拆分迁移（底本 → 索引，失败写法 → 对照卡，适配成品与槽位 → worked example），原 `corpus/story-archetypes/` 目录退役。

---

## 1. 与 Kimi 方案的对比裁决

### 1.1 关键时间线（决定裁决措辞）

| 时刻 | 事件 |
|---|---|
| 14:13–14:52 | 前几版修订；14:42 诊断出上帝视角 + 过度防御 |
| 15:08 | corpus-first 重写，用户认可 |
| **15:21–15:23** | **补丁落盘**：`corpus-first-generation.md`（新建）、`style-fidelity-gate.md`（新建）、`quality-gates.md` §6、`SKILL.md` Phase3 Step0 + Phase4 §5 |

→ 补丁是今日复盘的编码，不是被验证过的机制。裁定措辞：Kimi 的 P0 既不是错的也不是新的，而是**同一个做法（写规则）再做一遍**。

### 1.2 逐条裁决

| Kimi | 现状事实 | 裁决 | 落点 |
|---|---|---|---|
| 1 corpus-first protocol（映射表，未完成不许生成） | 已存在 `corpus-first-generation.md` Step 1，表头即 Kimi 的表；SKILL.md Phase 3 Step 0 已写同名禁令 | **不追加**；改造为 `generation-protocol.md` G1，触发条件从"完整 Introduction"改为**任何要产出最终句子的请求（含单模块、含改稿）** | P0-1 |
| 2 语料吸收证明 | 已存在（同文件 Step 3 三问） | **不追加**；升级为**进输出合同的借句表**，只允许引用索引 id | P0-1 |
| 3 anti-defense budget | 已存在（`style-fidelity-gate.md` §三，含"最多一次/贡献段最多一个限定句"） | **不追加**；升级为计数式判据，检查点前移到生成期 | P0-3 |
| 4 God-view detector | 已存在（§二，触发词表与 Kimi 逐条相同） | **不追加**；改造为生成期 G4「机制语气库」（正面底本），门控只核对 | P0-3 |
| 5 professional-expression gate | 已存在（§五，8 项 ⊇ Kimi 的 7 项） | **合并**：Introduction 专属只留姿态/预算/元语言，表达项归各自单一源 | P0-2 |
| 6 改造 retrieval（fuzzy/semantic/NN/top 6/分数/缺失条件/anchors） | 同意 fallback、解释、anchors；**不同意 semantic matching 与 top 6** | **部分采纳** | P1-4 |
| 7 story-archetype exemplar packs | 方向对，命名与归属有冲突 | **采纳并改造**为「叙事形状包」`corpus/packs/` | P0-0 |
| 8 journal-specific prose profiles | 维度可采纳；JOM 取值**无证据** | 维度采纳 + 证据门（≥5 卡） | P1-6 |
| 9 reviewer 两层 fidelity | 已提议（§六），但实现断裂 | **采纳 + 补机制**：pass-contract 单源 + 举证型 PASS | P0-2 |
| 10 失败案例库（6 个版本） | 新贡献 | **采纳并改造**为「对照卡」，与 G3 互为镜像 | P0-3 |
| 11 feedback registry 三类分流 | 方向对，诊断不足 | **采纳并加深**：84% 是语料变体需求 | P2-7 |
| 12 orchestration layer（六步） | 六步里两步与既有硬规则冲突 | **部分采纳**：四层 + 交接物约束 | P1-5 |

### 1.3 Kimi 的四处硬冲突（不可采纳）

1. **返回 top 6** 违反库自身契约：`story-blueprints/references/retrieval-contract.md`——"Return **at most one primary learning object and one contrast object**… For every result show: matching reason, **one learnable move**, one non-transferable condition, and one comparison question."。放宽到 6 条会直接复现"语料只作引用清单、不承重"的失败模式。
2. **六步的 step 2「story-blueprints 定故事版本和范文包」** 违反 `paper-story-contract/SKILL.md:37`："Do not load `story-blueprints`, propose a story type, select an exemplar, or ask the user to choose a frame."。故事类型由 story contract 锁定；story-blueprints 只能在**故事已锁定之后**提供叙事形状。
3. **JOM 画像为无证据断言**（"偏运营现象/不喜欢元语言/稳健性不宜堆叠"）。本机 AGENTS.md 的评审校准规则要求惯例主张先给范文现货证据；现状 `journal-fit.md` 全文 6 行、JOM 与 JMS 合并。→ 维度采纳，取值必须由 catalog 派生。
4. **humanizer 进入主流路径**。学术语域去 AI 腔已有单一源（`_polish-protocol.md` §AI 腔速查 + `prose-craft-checklist`）；今日改善来自**底本采纳**，不是去 AI 腔。

### 1.4 Kimi 漏掉的诊断

- **层错位**：Five acts 未入 catalog；`v4-schema.md` 明令 "They do not prescribe a story for a user's project"、"never present the move as a writing template" —— Kimi 的 step 2 在 schema 层就无法执行。
- **无稳定 id**：要求"sentence anchors"，却未回答"借句表如何引用它们"。
- **Phase 2 自造大纲**：`功能序列` 来自 `_routing_tables.yaml` 的 gap_type 查表，与 story-blueprints 零接线——story-blueprints 没被用起来的唯一直接原因。
- **双边同源重复**：kundro_rothbard 的 P2 原句在 `corpus/tensions/14-debate-unresolved.md` 与 `rhetoric-moves/bidirectional-staging.md` 各存逐字副本；双理由枚举在 `stakes/06` 与 `mechanism-two-chain` 各定义一次；"语料优先改编"纪律三处。
- **死资产与失效指针**：`storytelling/` 6 张诊断卡无人读取，`_index.md` 仍称"被 SKILL.md 的 Story Architecture Layer 引用"（该节 grep 0 命中）。
- **`corpus/story-archetypes/` 越界**（P1–P6 完整大纲 + 段底本 + 槽位）。
- **完成判据不可判定 / no-op 句 / 8 处否定式指令 / leading word 跨文件漂移**。
- **active rules = 0 的机械原因**：95 条 defect 中约 84% 属 `append_variant` 家族（语料变体需求），进规则通道必然全卡 EMERGING。
- **三处 PASS 契约冲突**：`style-fidelity-gate` 要求 `exemplar_fidelity`，实际承接 Introduction 审查的 `intro-review` 不产出该字段 → 今天的 PASS 是契约允许的。

### 1.5 从 Kimi 采纳的 4 项（改造后并入）

| Kimi | 改造 | 理由（writing-for-agents） |
|---|---|---|
| 7 范文包 | 更名**叙事形状包** `corpus/packs/<shape-id>.md`，由 catalog 卡派生（不按项目派生） | 把大纲与底本打成一个可整份读入的调用单元；但"story fingerprint"命名会重新打开故事选择，与 paper-story-contract 冲突 → 改称形状 |
| 10 失败案例库 | 更名**对照卡**（失败句 → 顶刊底本句 → 差异字段） | "不要写成这样"是否定式，会把禁写内容拖进 context 并提高其可用性；对照卡是正向目标 + 可核对产物 |
| 8 期刊维度 | 并入（另加显式 caveat 容忍度、具名案例容忍度、段落节奏），取值 ≥5 卡证据 | 把"听起来对"变成"可核" |
| 6 逐卡缺失条件 | `--explain` 同时输出各门淘汰卡数 + 每张返回卡未满足的条件 | 低质量结果也要可诊断 |

### 1.6 你的自我诊断 → 机制归属

| 自省 | 机制承接 |
|---|---|
| ① 过度依赖门禁与 PASS | pass-contract 举证型 PASS（无底本 id 的 PASS 无效） |
| ② 把锁定边界直接翻译成正文语言 | G3 边界翻译表（生成期给正面底本，不再由门控事后抓） |
| ③ 把 corpus 当检查表而非写作底本 | G1 借句表 + 只引索引 id + 进输出合同 |
| ④ 太早接受局部优化 | **重写门**：水位门输出底本覆盖率；<80% 直接回 G1 全量重写 |
| ⑤ reviewer prompt 不查风格 | 三审查入口统一到 pass-contract，`intro-review` 必须产出四个风格字段 |

---

## 2. 诊断

**2.1 表层三条**：规则是"描述"不是"步骤"；PASS 是"未违规"型不是"举证"型；语料是"可参考"不是"可调用"。

**2.2 架构层**：**你设想的层分工没有实现层，两个库各自偏在对方的位置上。**

| 你的设想 | 实际 | 后果 |
|---|---|---|
| story-blueprints = 段落大纲 | 整篇叙事读解卡（Theme question / Whole-story synopsis / Characters / **Five acts** / Tension / Alternative readings + 7 维评估 + 逐节 ≤2 条结构动作） | Five acts **只活在 78 份 .md 正文，未入 catalog** → 段序列不可机读；`v4-schema.md` 又禁止当模板 → 生成侧无法合法引用 |
| corpus = 段内句子与词汇 | 106 张段级功能卡 + 7 张句级/词级卡 + 10 张诊断卡 | 段级卡内容约一半是 verbatim 借句（7 个大目录合计 **395 条无损原句 + 422 条填槽模板**），但 Phase 3 消费方式是"读卡"不是"取句" → 句被功能说明遮蔽 |
| 段落大纲由谁产出 | **Phase 2 从 `_routing_tables.yaml` 的 gap_type 查表自造** | story-blueprints 与 Phase 2 零接线 |

**2.3 两库"没被用起来"的机械原因（各三条，逐条可修）**

| story-blueprints | corpus |
|---|---|
| ① Five acts 未入 catalog → 检索器看不到段序列 | ① 无稳定 id → 无法被任何借句机制引用 |
| ② v4-schema 禁止当模板 → 生成侧无法合法引用 | ② verbatim 半被功能半遮蔽，Phase 3 只"读卡"不"取句" |
| ③ Phase 2 自造大纲，从不调用它 | ③ 与 rhetoric-moves 双边同源重复 → 不知该信哪边 |

---

## 3. 六个杠杆（writing-for-agents）

| 杠杆 | 病灶 | 动作 | 验收 |
|---|---|---|---|
| **步骤 vs 参考** | 生成动作散在 4 文件（SKILL.md:75、render-rules:86-91、quality-gates:70、corpus-first-generation） | `generation-protocol.md` 成为唯一生成步骤（G1–G5），其余三处只留指针 | 生成层要求可在一个文件内读完 |
| **完成判据的清晰度与要求** | "模块跳过/压缩决策有理由""润色纪律满足"不可判定；映射表只在"完整 Introduction"强制 | 判据改可核对形态；大纲表与借句表**进输出合同** | 判据可用"是/否"回答；改稿请求也产出 |
| **举证型 PASS** | 检查项靠缺省通过 | `pass-contract.md` 唯一源；无底本 id 的 PASS 无效 | 第三方可按 id 复核 |
| **leading word + 单一事实源** | 五个概念跨 4–6 文件整句复述（AI 腔 6 处、五病 4 处、specificity 4 处、引用列队 4 处） | 收敛为 **大纲 / 底本 / 借句表 / 水位 / 姿态 / 预算** 六个 token，各一处定义 | grep 无同义整句复述 |
| **正向指令** | 8 处"不得/禁止/不默认" | 改正向目标句 | 禁止式仅剩无法正向表达的硬护栏 |
| **渐进披露 + 指针措辞** | Phase 4 内联概括水位门四检；Phase 3 Step 0 指针写成"完整 Introduction 强制"（今天真实入口是改稿） | 指针按**分支**写触发条件；内联下沉 | 每个 reference 只有一处指针，且写明何时必须读 |

---

## 4. 最终架构：层合同 + 一个缺层 + 两个接口

**不搬库、不重构 v4 schema、不做 134 卡全量迁移。**

| 层 | 所有者（不变） | 职责 | 产物 | 消费方式 |
|---|---|---|---|---|
| **L-Story** | `story-blueprints/v4/blueprints/`（78 卡） | 整篇叙事怎么讲 | 读解卡 | 只供**选叙事形状**；不选故事类型、不作句子来源 |
| **L-Outline（新，缺层）** | write-introduction Phase 2 | 段落序列 + 主导功能 + 承载信息 + 来源 | **大纲表**（进输出） | 下游 G1 逐段填底本 |
| **L-Sentence** | `corpus/` 段级卡 verbatim 半 + `phrasebank/` + `micro-templates/` | 段内句子与词汇 | **借句表**（每段一行，只引索引 id） | G2 落句 |
| **L-Move** | `story-blueprints/v4/rhetoric-moves/` | 跨节通用修辞动作 | 动作清单 | 句子级润色；**不存 verbatim 原句**（引 corpus id） |

**两个调用接口（脚本生成，人工不维护内容）**

| 接口 | 来源 | 内容 | 作用 |
|---|---|---|---|
| `corpus/_skeleton-index.md` | corpus 段级卡"原文锚定"块 + phrasebank/micro-templates 句行 | `{id, 修辞功能, 适用模块, citekey, verbatim 骨架, 卡片路径}`，首批 60–80 条 | 让 L-Sentence 可调用；借句表只能引这里的 id |
| **`corpus/packs/<shape-id>.md`（叙事形状包）** | 78 张 v4 blueprint 卡 × 底本索引的连接 | 形状指纹（**形状**，非故事类型）+ 段落序列（Five acts 一行式）+ 每段可用底本 id 列表 + 该形状的对照底本 | 让 L-Story 与 L-Outline 可调用：Phase 2 选形状、G1 直接取该形状下的底本 |

接口必须小到可整份读入——这是它们能被真正用上的前提。

**worked example 的家**：`story-blueprints/v4/worked-examples/`（新目录，与 `blueprints/` / `reading-pairs/` 同级）。

**层合同必须写清的三条边界**（否则与既有硬规则冲突）

1. **`v4-schema.md` 的放宽授权**：其 "do not prescribe a story / never present the move as a writing template" 针对"照搬整个故事"。精确放宽为：**形状包与 blueprint 卡的 `Five acts`、`section_learning` 可作段落大纲底本，不得作句子底本**。
2. **不得参与故事选择**：`paper-story-contract/SKILL.md:37` 禁止在 story contract 阶段加载 story-blueprints、提出故事类型、选范文。形状包只在**故事已锁定之后**提供形状与底本，且不反推故事类型。
3. **rhetoric-moves ↔ corpus 划界**：同一 verbatim 原句只作为**底本**存一处（存 corpus 卡 / 索引）；信号词表归 `micro-templates/transition-signals.md`；rhetoric-moves 只保留动作名 + 判据 + 来源 id。
   推论——**worked example 不得复制原始底本清单**，只保留"本项目适配后的成品段落 + 底本 id 引用 + 槽位说明 + 为什么这样换"。这样既守住单源，又保留了今天最有价值的内容（换血这一步）。

---

## 5. 问题 → 动作项

### P0-0｜大纲接线：让 story-blueprints 进入 Phase 2

1. 新建 `references/outline-protocol.md`，Phase 2 三步：**O1 取材**（取 Phase 1.5 推荐的主 blueprint 卡 → 读 `Five acts` 与 `section_learning.introduction.learn`；从 `packs/` 取 1 个形状最近的对照）→ **O2 合成**（与 `_routing_tables.yaml` 的 `paragraph_structures` 合成；**冲突时形状以卡优先**，gap_type 只定能量与复杂度）→ **O3 登记**（大纲表四列：段号 / 主导功能 / 承载信息 / 来源）。
2. `来源` 取值必须可核：`<blueprint-id>:<act名>`、`shape:<pack-id>`、`routing:<gap_type>` 或 `self-drafted`。
3. SKILL.md Phase 2 §4「开篇功能合同」保留为功能约束；「功能序列」改由 O1–O3 产出。
4. `scripts/build_indices.py` 生成 `packs/`：抽 78 卡 `Five acts` 每一幕一行 + 卡路径 + citekey + outlet + `learn` 首句。

**完成判据**：每次完整生成的输出含大纲表，每段 `来源` 非空且可核；`self-drafted` 占比如实记录。

### P0-1｜借句表与索引：把"可参考"变成"可调用"

1. `build_indices.py` 同时生成 `_skeleton-index.md`（覆盖今天用到的 7 个模块，60–80 条）。
2. `generation-protocol.md` **G1**：借句表只能引用索引 id；表进输出合同（每段一行：段落 / 主导功能 / 底本 id / 借用骨架 / 替换清单 / 保留节奏）。
3. **G2** 固定顺序：取底本骨架 → 替换来源特异内容（专名/行业/样本/年份/数字）→ 填本文构念与方向 → 校验原句节奏（先主张后限定 / 先对立后裁定 / 先现象后理论）。无对应骨架才标 `self-drafted`。
4. 触发条件：**任何要产出最终句子的请求都走 G1**（含单模块、含改稿）。
5. 删 `corpus-first-generation.md` §三（复制自卡片），Step 结构意图迁入 generation-protocol。

**完成判据**：借句表出现在每次生成输出的固定位置；索引抽检 10 条人工核对通过。

### P0-2｜水位门、举证型 PASS、重写门

1. `style-fidelity-gate.md` → `water-level-gate.md`，Introduction 专属只留**姿态 / 预算 / 元语言**三检；表达细节指向单一源（`prose-craft-checklist` §0/§5、`_polish-protocol.md` §5），并要求把"是否执行"写进举证字段。
2. 新建 `references/pass-contract.md`，定义 6 字段：`boundary_compliance`（逐条锁定边界）、`exemplar_fidelity`（逐段底本 id）、`posture`、`defense_budget`、`meta_language`、`expression`。硬规则：**缺任一字段 = 审查未完成；只有"未违规"而无底本 id 的 PASS 无效**。
3. 三入口统一指向该契约，并修 `intro-review`。
4. `quality-gates.md` §6 空壳指针改指 pass-contract。
5. **重写门**：水位门输出 `底本覆盖率`（有底本 id 的论证型段落占比）；<80% → 回 G1 全量重写，不做句级修补；≥80% → 走 L-Move 句级修补。

**完成判据**：审查输出可被第三方按底本 id 复核；改稿请求自动产出覆盖率与重写/修补分支。

### P0-3｜边界翻译、姿态、对照卡

1. `generation-protocol.md` **G3 边界翻译表**：行 = 本项目实际锁定约束，列 = 失败写法（事实记录）/ 论文语言底本（**必须从范文卡抽 verbatim，标 citekey，不得自拟**）/ 出现位置。首批 6 行：

   | 锁定约束 | 今日失败写法（事实） | 论文语言底本 |
   |---|---|---|
   | sign 不是贡献 | "The sign is the estimand, not the contribution." | 待从 ball2018 / darby2026 抽 |
   | mixed evidence（H2/H3） | 结果段与贡献段各披露一次 | 集中披露底本句待抽 |
   | recall count 非纯质量 | "the implication is equally bounded" | 待抽 |
   | timing 仅作裁决 | "nonexclusive adjudication" | 待抽 |
   | 不写因果 | "should not be presumed…" | 待抽 |
   | 不写质量收益 | "not independent contextual additions…" | 待抽 |

2. **G4 机制语气库**：动词/句式底本（`can bundle / may reflect / we theorize / is consistent with / can change`）+ 回归 case：今日原句 `"Annual serious recall counts are therefore governance outcomes. They show…"` 必须判为姿态不合格并给出改写。
3. **对照卡**：`corpus/contrast-pairs/`，每卡 = 失败句 → 顶刊底本句 → 差异字段（姿态/预算/元语言/具体性）。今日 6 个版本（过度防御版、元语言版、文献画像 Hook 版、假 Darby 区分版、无 corpus-first 的平庸版、最终修正版）登记为对照卡；story-archetypes 原文件中的"禁止复活失败写法"块并入本目录。G3 与对照卡互为镜像（按约束类型 / 按失败案例），共用同一底本来源。
4. **预算计数式判据**（写入 `water-level-gate.md`）：同一 caveat 全篇集中披露 ≤1 次；贡献段限定句 ≤1；黄金段（Hook/Theory Lens/Contribution）无防御句；段落收尾用肯定式范围句。
5. 姿态与预算的检查点前移到 G3/G4；水位门只核对。

**完成判据**：6 行翻译表全部有 citekey 底本句；5 条今日失败原句作为 regression case 一次性通过；对照卡 ≥6 张且每张含底本句。

### P1-4｜检索修复（部分采纳 Kimi #6）

1. **语义修正**：`retrieve_exemplars.py` 中 `validated_conditions` 为空时不再视为"无已验证条件"（现行 ⇒ 只有 requires=[] 的 53/78 卡可过），改为标 `unknown`，requires 由硬门降为**排序罚分**。这解除"遵守协议 → 零结果"的反激励。
2. **Tier 2 fallback（规则化放宽序，可审计）**：(a) 忽略 `retrieval_signals` 交集，保留 `narrative_dynamics` / `theoretical_problem_form` 任一命中；(b) suitable 放宽至 partial；(c) 只按 outlet + paper_type 给同类候选。每条 Tier 2 结果标注"放宽了哪一条、命中了哪一条信号"。
3. **不做 semantic matching / embedding 排序**：仅 78 卡，索引与包可整份读入；不可审计的排序换来不可预测的输出。
4. **`--explain`**：输出各门淘汰卡数 **+ 每张返回卡未满足的条件**；空结果必须附这一行。
5. 修路径：`v4/rhetoric-moves/scripts/` 是空目录，脚本实际在 `story-blueprints/scripts/`。
6. 优先序：Phase 2 先查 `packs/`，Phase 3 先查 `_skeleton-index.md`，catalog 检索降为"整卡学习"通道。
7. 不再扩 `narrative_dynamics` 当模板轴：其取值 315 distinct / 317 tokens（`retrieval_signals` 319、`theoretical_problem_form` 164），绝大多数只出现 1 次，会复现稀疏交集空结果。

**完成判据**：今日的 Theory / Introduction exemplar request 不再返回裸 `results: []`；空结果必附淘汰计数；Tier 2 结果可追溯到放宽条件。

### P1-5｜划界、去重、死资产、story-archetypes 迁移

1. `references/library-contract.md` 声明四层所有权、交接物（无大纲表不得进 G1；无借句表不得进句子润色）与 §4 的三条边界。
2. **双边同源重复归零**：删 `bidirectional-staging.md` 的 kundro_rothbard 原句副本、`mechanism-two-chain.md` 的 moon2026 原句副本，改引 id。
3. **同类问题定义处从 4–6 降到 1**：AI 腔 6 处 → `_polish-protocol.md` §AI 腔速查（humanizer 仅非学术）；五病 4 处 → `prose-pathology.md`；specificity 4 处 → `_polish-protocol.md:131`；引用列队 4 处 → `_argument-grammar.md:30`；"语料优先改编" 3 处 → `generation-protocol.md`。
4. 修 polish"八查/七查"口径不一致。
5. **编排（部分采纳 Kimi #12）**：四层 + 交接物；**humanizer 不入学术路径**。顺序：L-Story → L-Outline → L-Sentence(G1/G2) → L-Move 句级动作。
6. **死资产二选一定夺**：`storytelling/` 6 张诊断卡（central-knot-diagnostic / central-knot-throughout-check / character-map / hook-type-mapping / tension-escalation-protocol / post-generation-validator）当前无人读取，`_index.md` 仍称"被 SKILL.md 的 Story Architecture Layer 引用"（grep 0 命中）→ 接回 Phase 0/2 或删除并修 `_index.md`。同类：`phrasebank/methods-process.md`、`phrasebank/quantities-trends.md`、`micro-templates/key-line-patterns.md`（加指针或删）。
7. **`corpus/story-archetypes/` 三拆分迁移（裁定：上收作 worked example）**——**顺序不可颠倒，先抽后收**：

   | 步 | 动作 | 落点 |
   |---|---|---|
   | ① 抽底本 | 把 P1–P6 每段的 citekey + verbatim 骨架抽进索引，标 `pack_id: portfolio-governance` | `corpus/_skeleton-index.md` |
   | ② 建包 | 生成形状包：形状指纹 + P1–P6 段序列 + 每段可用底本 id | `corpus/packs/portfolio-governance.md` |
   | ③ 抽失败写法 | 原文件"禁止复活失败写法"块转成对照卡 | `corpus/contrast-pairs/` |
   | ④ 上收 | 原文件迁为 worked example，**内容只保留**：本项目适配后的成品段落 + 每段底本 id 引用 + 槽位说明 + 为什么这样换；**删除原始底本清单**（已在 ①）与失败写法（已在 ③） | `story-blueprints/v4/worked-examples/portfolio-governance.md` |
   | ⑤ 声明身份 | worked example 头部元数据：`kind: worked-example`、`derived_from: <6 citekeys>`、`runtime_eligibility: no`；并在 `story-blueprints/README.md` 的运行时权限声明处补一行（README 已是 legacy 层权限的既有单一源）| 文件头 + `README.md` |
   | ⑥ 退役与改指针 | 删 `corpus/story-archetypes/`（含 `_index.md`）；`write-introduction/SKILL.md:57` 由 `corpus/story-archetypes/_index.md` 改指 `corpus/packs/_index.md`（全树仅此一处引用点，已核实） | SKILL.md + corpus |

   **worked example 的定位纪律**：它是**管线的使用示范**，不是规则来源、不进 `catalog.json`、不被 `retrieve_exemplars.py` 返回、不参与故事类型选择（与 §4 边界 2 一致）。

**完成判据**：四层各有所有者与交接物；双边同源 verbatim 归零；同类问题定义唯一；死资产清零；story-archetypes 目录消失且那 6 篇范文的底本仍可从索引与包中取到。

### P1-6｜期刊画像（维度采纳 Kimi #8，取值证据化）

1. `journal-fit.md` 重写为画像表，列 = outlet / Hook 类型偏好 / 现象 vs 理论起点 / Stakes 形态 / Contribution 写法（theory–practice–policy 配比）/ 显式 RQ / Differentiation 段 / robustness preview 容忍度 / **显式 caveat 容忍度** / **具名案例容忍度** / **段落节奏** / 元句容受 / 段数区间。
2. **证据门（2026-09-14 修订，见 §8 D-01）**：每个取值必须附**证据来源标签**——`catalog≥5`（同 outlet ≥5 张卡，标卡 id）｜`corpus-hooks`（`corpus/hooks/*.md` 的 `## 期刊适配` 表，28/28 卡有该表）｜`routing-journal_styles`（`corpus/_routing_tables.yaml` §9）｜`未核查`。标签为 `catalog≥5` 时须真的满足 ≥5 卡；其它标签须标出具体文件与位置，并**如实标明其为语料手工证据、非范文现货证据**。无任何来源的格子写 `未核查`。
3. **JOM 行**：现 catalog 仅 1 张 JOM 卡（darby2026）、JMS 0 张，故 JOM 画像**在本机证据下无法产出**。处理方式：JOM 行保留并标注 `未核查 — 需先向 v4 卡扩样 ≥5 篇 JOM 论文`，不得用手工印象或从 JMS 行推断代替。
4. 消除口径冲突：元句容受由画像回答；`water-level-gate` 的元语言禁令改为"除非目标期刊画像允许"。

**完成判据（已修订）**：13 个维度全部有取值或显式 `未核查`；每个非 `未核查` 取值附证据来源标签，`catalog≥5` 标签者满足卡数门槛，其它标签者可指认到具体文件位置；JOM 行的 `未核查` 附扩样条件。**判据不再要求「每取值附 ≥5 卡证据」**——该门槛在本机语料下不可达，强行要求会逼出编造。

### P2-7｜登记层（采纳 Kimi #11，加深诊断）

1. **Triage 95 条**：`proposed_change.action` 分布 `append_variant` 家族 60 + `add_variant` 13 + `add_branch` 7 → **约 84% 是语料变体需求**，直接执行成 corpus 变体；`add_branch`/`conditionalize` 进对应 reference 文件的条件句；其余留账本。
2. **诚实处理 R1/R2**：R1 不存在（无 `feedback-registry.json`、无 `record_feedback.py`）；R2 的 `critique.per_file` 为 `null`。二选一：真接线，或从 SKILL.md 删除该承诺。留一个自称存在而零数据的通道比没有通道更糟。
3. **promotion 规则**：同一 defect 在 ≥2 篇论文复现 + 有 regression_case → 提升为对应 reference 文件里的规则句（**不新建文件**），回写 `rule_locator` 与 `status: VERIFIED`。现状：95 条全 EMERGING / open / `log_only` / `absolute_rule=false` 0 条 / `decisive_falsifier=true` 0 条 → active = 0。
4. 今日 5 条失败原句写入 `regression_cases`（字段 95/95 非空但内容待补）。

**完成判据**：`active ≠ 0`；open 数因变体落地显著下降；每条规则句可追 ≥2 篇来源。

### P2-8｜去重、no-op、判据可判定化

1. 按 §1.4/§2 清单定唯一权威并删其余处正文（留指针 + 该处特有增量）。已知重复：段落论证文法 3 处；首尾句测试 2 处；GBL 对齐 3 处；Hook 能量 3 处；异议预判 4 处。
2. **删 no-op 句**：SKILL.md:77"不编造引文/数字/发现方向"；corpus-first-generation.md:32"不能是'综合感觉'"；style-fidelity-gate.md:11"是否真正吸收 corpus 句型"；corpus-first-generation.md:8 的解释段。整句删除。
3. SKILL.md 完成判据改可核对形态：
   - "模块跳过/压缩决策有理由" → "每个跳过/压缩的模块在大纲表标注 `[skipped: 理由类型]`（枚举）"
   - "润色纪律满足" → "水位门 6 字段全部有取值，每个 FAIL 附原句与底本 id"
   - "能量一致性已标注" → "Hook/Gap/Stakes 能量级同行标注且满足 Hook ≤ Gap ≤ Stakes"
4. 8 处否定式指令逐条改正向：如"未完成映射不得进入正文生成" → "先落借句表，再渲染正文"；"禁止堆叠的短语组" → "同一段只保留一次 caveat，收尾用肯定式范围句"。
5. SKILL.md frontmatter description 增加分支触发词：引言**改稿**（含"不够像范文"的返工）。

**完成判据**：SKILL.md ≤90 行且判据可"是/否"回答；同义整句复述 grep 归零。

---

## 6. 实施批次

| 批次 | 内容 | 预计 | 依赖 |
|---|---|---|---|
| **Batch 0** 口径清理 | polish 八查/七查；`v4/rhetoric-moves/scripts/` 路径说明；journal-fit 元句与水位门口径冲突；修 `storytelling/_index.md` 失效指针 | 0.5h | 无 |
| **Batch 1** 大纲接线 | `outline-protocol.md` + Phase 2 三步 + 层合同的 §4 三条边界 + `build_indices.py` 生成 `packs/` | 2h | 脚本需抽 78 卡 Five acts |
| **Batch 2** 生成层核心 | `generation-protocol.md`（G1–G5 + 边界翻译表 + 机制语气库）+ `water-level-gate.md` + `pass-contract.md` + 重写门 + SKILL.md Phase 3/4 重写 | 3h | 需从 6 篇范文抽底本句 |
| **Batch 3** 语料与检索 | `_skeleton-index.md` + `retrieve_exemplars.py` 语义修正 / Tier 2 / `--explain` + 对照卡 ×6 + journal-fit 证据化 + story-archetypes 三拆分迁移①②③ | 2.5h | Batch 2 的底本抽取可复用 |
| **Batch 4** 登记与上收 | registry triage 与变体落地 + promotion 规则 + 死资产处置 + story-archetypes 迁移④⑤⑥（上收 worked example、声明身份、删目录、改 SKILL.md:57 指针） | 1.5h | Batch 3 的①②③ 必须先完成 |
| **Batch 5** 验收 | 端到端重跑 + 回归集 | 1h | 全部 |

**风险与反制**：门越加越多 → 水位门只留 3 个 intro 专属检项，其余走指针；借句表形式化（填 id 不换血）→ 举证要求首句与底本的差异清单 + regression case 抽查；索引抽取质量差 → 条目必须含 verbatim 原句与卡路径，抽检 10 条不过则退回；底本回填时自拟 → 必须标 citekey 且可在卡中定位，找不到就标 `self-drafted`；大纲接线与 v4-schema 冲突 → 放宽授权必须落文；**worked example 与索引争夺底本归属** → 迁移顺序先抽后收（③ 之后原文件不再含原始底本清单）。

---

## 7. 验收实验（端到端）

**Case**：共同所有权 × 产品召回 Introduction（定稿 `Introduction_0913.md` SHA `153d79c6…`；中间态 `f12a8adb…`、`629b872e…`）。

**协议**：新会话，只给 Story Contract 与项目事实，**不提示"要像范文"**；并**另跑一次改稿路径**（喂中间态那版，看是否触发重写门）。

| # | 判定项 | 通过标准 |
|---|---|---|
| a | 大纲表 | 每段有主导功能、承载信息与可核 `来源` |
| b | story-blueprints 实际被消费 | `来源` 中至少一段引用具体 blueprint 卡的 act 名或 pack id |
| c | 借句表 | 每段一行，含索引 id 或 `self-drafted` |
| d | 姿态回归 | 5 条今日失败原句均判 FAIL 并给出改写 |
| e | 预算 | 同一 caveat 全篇集中披露 ≤1 次；贡献段限定句 ≤1 |
| f | 元语言 | 无 `estimand / locked / contribution boundary / adjudication` 泄漏 |
| g | 检索 | exemplar request 非空；若走 Tier 2，标注放宽条件与未满足条件 |
| h | 重写门 | 喂中间态草稿时，底本覆盖率 <80% → 输出要求全量重写而非句级修补 |
| i | 迁移完整性 | story-archetypes 目录已删；那 6 篇范文的底本仍可从 `_skeleton-index.md` 与 `packs/portfolio-governance.md` 取到；worked example 不含原始底本清单且 `runtime_eligibility: no` |

**通过线**：≥7/9，且 a、c、d、h 必须通过。
**失败处理**：a/b 失败 → Batch 1 的 O1–O3 未真正执行（典型表现：来源栏全填 routing 或 self-drafted）；c/h 失败 → G1 被降级为"原则"或重写门未接线；d/e/f 失败 → pass-contract 未被 intro-review 消费；i 失败 → 先抽后收的顺序被颠倒。

---

## 8. Decision Register（执行段）

### D-01｜P1-6 期刊画像完成判据修订（2026-09-14，执行段）

- **原规格**：`journal-fit.md` 每行由 catalog 同 outlet 卡片归纳，≥5 卡门槛；完成判据要求「JOM 行回答全部维度且每取值附 ≥5 卡证据」。
- **调整依据（Wave2-B 实测事实）**：① catalog 78 卡的 11 个字段中，13 个画像维度里**只有 1 维**（显式 caveat 存在性）可派生，且各 outlet 均为 100%（78/78 卡的 introduction.caveat 非空）→ **无区分度**，用它回填只会得到 6 行相同的取值。② 字面分组达 ≥5 卡的 outlet 有 SMJ 11 / AMJ 10 / JM 9 / MS 7 / POM 6（合并 ASQ 三种拼写别名后 ASQ 6）；**JOM 仅 1 卡、JMS 0 卡**。③ 额外来源实测：`corpus/hooks/*.md` 的 `## 期刊适配` 表 28/28 卡存在（可给出 hook × journal 适配度）；`_routing_tables.yaml` §9 `journal_styles` 是唯一按期刊分组的表，但只覆盖 ASQ/SMJ/AMJ/OS/ASR/JM_JMR，缺 MS/POM，JOM 不列；`exemplar_anchoring` 按「GapType × Contribution」分组，journal 只是副字符串。④ 抽样读 v4 卡正文：全量 78/78 卡有 `### Five acts`（语义节拍，非段数）；显式给出 intro 段数的仅 2/78（均 SMJ）→ 正文抽取不能使任一维度达 ≥5 卡门槛。
- **调整内容**：完成判据由「每取值附 ≥5 卡证据」改为「取证来源分层标注」——`catalog≥5` / `corpus-hooks` / `routing-journal_styles` / `未核查` 四类标签，每类有各自的举证要求；JOM 行定为 `未核查` 并附扩样条件。
- **原结果事实保留**：现 `journal-fit.md` 为 6 行表、JOM 与 JMS 合并、无元句维度、无 Contribution 列——这些事实不变，只是不再用手工印象补 13 列。
- **残余风险**：`corpus-hooks` 与 `routing-journal_styles` 是手工撰写语料，其证据基是 MVP30/distills 而非 78 卡；若将来 v4 卡扩样到各 outlet ≥5 张，应把标签升级为 `catalog≥5` 并复核取值。

### D-02｜骨架索引底本来源修正（2026-09-14，执行段）

- **原假设**：骨架索引可从 v4 blueprint 卡抽 verbatim 底本（方案 §4 写「corpus 段级卡原文锚定块 + phrasebank/micro-templates 句行」，但 §5 P0-0 的 packs 生成句暗示卡片含可借句）。
- **调整依据（Wave1-B 实测）**：v4 卡正文（`Story Reading` / `Learn` / `Do not copy`）**全部是转述，无任何 verbatim 原句**；六篇范文的 verbatim 只能从 corpus 段级卡的「原文锚定」块定位，且仅 darby2026 / wowak2025 / lu2022 有锚；anton2025 / denicolo2025 / ball2018 仅存在填槽模板。
- **调整内容**：索引底本来源**唯一确定为 corpus 段级卡锚定块与 phrasebank/micro-templates 句行**；形状包只放 id 引用与 `verbatim` / `模板` 状态标注，不复制底本正文；antonym2025/denicolo2025/ball2018 的段底本一律标 `模板`。
- **原结果事实保留**：archetype 文件头部「Wowak et al. 2021, MSOM」在 catalog 无对应卡（wowak2025=MS 2025、wowak2020=MSOM 2020、wowak2015=SMJ 2015）；anton2025/denicolo2025/wowak2025/darby2026 的 catalog `citekey` 字段为 null；id 命名短 id 与长 slug 混用。

### D-03｜G3 边界翻译表的缺口处理（2026-09-14，执行段）

- **原规格**：G3 六行每行必须从范文卡抽 verbatim 正面限定句并标 citekey。
- **调整依据（Wave1-B 实测）**：六行中仅 2 行（mixed evidence 集中披露、一构念统摄两边界）在六篇范围内有可定位 verbatim；另 4 行（sign 不是贡献 / recall count 非纯质量 / timing 仅作裁决 / 不写因果）在六篇内**无正面底本**。
- **调整内容**：取证范围由「六篇范文」扩大为**全部 484 条索引底本**（2026-09-14 勘误：索引状态重分类后实测 verbatim 390 / 模板 556，见 corpus/_skeleton/_index.md；原「484」为分类前的初始计数）（按修辞功能检索）；仍找不到的行标 `self-drafted` 并**登记为语料变体需求**（进 P2-7 的 triage 流程），不得用自拟句冒充底本。

### D-04｜检索放宽、契约对账与验收文书（2026-09-14，执行段）

- **原规格**：`retrieve_exemplars.py` 保持 requires 为硬门；空结果视为「可信弃权」合法输出；不得扩大返回条数。
- **调整依据（实测）**：① `validated_conditions` 留空（guide 明确要求的做法）只能命中 requires=[] 的 53/78 卡，叠加 `retrieval_signals` 交集门后合法产出空结果——协议合规反成零结果；② 45 个 fixture 实跑 0 空结果后，出现新副作用：`writer-side-fini` 请求返回 zhou2017 而非 fini2017，根因是标签词表稀疏（请求 `cross-audience-partial-incommensurability` vs 卡 `cross-audience-partial-criterion-overlap`）加「tier 1 一旦非空即 break」。
- **调整内容**：requires 由硬门降为排序罚分（−15/条）；`validated_conditions` 空 → `validation=unknown`；新增 Tier 阶梯 1→2a→2b→2c 与退化 tier 护栏（`theoretical_problem_form` 命中为空且 unmet≥1 时不定胜，必要时标 `low_confidence`）；新增 `references/tag-normalization.yaml` 人工同义词表（禁 embedding/语义/子串匹配）；`--explain` 输出淘汰计数与未满足条件；保留 1+1 上限。同步对账 `retrieval-contract.md` 与 `v4/writer-side-acceptance.md`，并新增 `tests/regression_retrieval.py`（四组断言）。
- **实测结果**：fini 请求恢复主推 fini2017（70 分）并排在 zhou2017（45 分）之前；43/43 fixture 无空结果。
- **残余限制**（已写入验收文书，不当作已完成）：标签词表仅首批、别名未全覆盖；`tier 2a` 在请求无 `retrieval_signals` 时为空转档。

### D-05｜登记层 triage 的事实修正（2026-09-14，执行段）

- **原规格**：把 95 条 defects 中约 84% 的 `append_variant` 家族「直接执行成 corpus 变体」。
- **调整依据（实测）**：95 条的 `proposed_change.summary` **均不含可直接插入的完整变体正文**，只指向一个树内不存在的 writeback_plan；而逐条核验后发现 81 条所要求的变体**早已落在对应语料卡内**。即这批登记不是「需求未满足」，而是「登记未同步」。
- **调整内容**：改为以 `channel` 字段路由（`corpus_variant` 83 / `rule` 3 / `obsolete` 9，另新增 5 条今日失败记录的 `channel=rule, risk=high` 条目）；81 条逐条登记 `executed_on` / `executed_locator`（注明为「既有变体核验后补登记」，非本轮新写入）；2 条无法落地的记 `blocked_reason` 与解除条件。
- **诚实保留**：`status=VERIFIED` 与 `lifecycle=closed` 仍为 0——按新写入 SKILL.md 的 promotion 规则（同题 ≥2 篇复现 + 带 regression_case），当前无条目达标。不得为凑数虚标。

### D-06｜死资产处置决定（2026-09-14，执行段）

处置规则：被 `paper-story-contract` 或现有 Phase 覆盖且无外部指针 → 删；有独有内容或外部指针 → 保留并在 `_index` 写明入口与触发条件。

| 资产 | 决定 | 依据 |
|---|---|---|
| `storytelling/central-knot-diagnostic.md` | 删 | `story.central_knot` 字段 + Phase 0 门已覆盖 |
| `storytelling/central-knot-throughout-check.md` | 删 | post-generation-validator 的 knot_coverage 项已覆盖 |
| `storytelling/hook-type-mapping.md` | 删 | `hooks/_index.md` 的 Pollock 类型速查已覆盖 |
| `storytelling/character-map.md` | 保留 | 独有 Intro 前三段角色 staging |
| `storytelling/tension-escalation-protocol.md` | 保留 | 独有 `conversation_strategy` 双轴纪律 |
| `storytelling/post-generation-validator.md` | 保留 | 独有 Intro 后生成验证器 |
| `phrasebank/methods-process.md`、`quantities-trends.md` | 保留 | 被 write-methods / write-results 引用，已标跨节用途 |
| `micro-templates/key-line-patterns.md` | 保留并接线 | Phase 4 加显式指针 |

### D-07｜端到端验收实测（方案 §7 的实测记录）

**跑法**：新会话扮演 write-introduction 调用，输入 Story Contract 本地副本，目标期刊 JOM；**禁止读今日任何一版既成草稿与 `corpus/contrast-pairs/`**（污染控制）。

| # | 判定项 | 实测 | 结论 |
|---|---|---|---|
| a | 大纲表每段 `来源` | 5 段全部为 `anton2025:<act名>`（Exposition / Rising action / Climax / Falling action / Denouement），`self-drafted` 0/5 | 通过 |
| b | story-blueprints 实际被消费 | 五幕全覆盖，O2 冲突时按「形状以卡优先」折入 pack 的 P4 | 通过 |
| c | 借句表 | 9 个底本 id 全部可在 `corpus/_skeleton/<module>.md` 定位 | 通过 |
| d | 姿态回归（今日 5 条失败原句） | 正文上帝视角句 0、元语言 0；但**未逐条对照那 5 条原句**（污染控制禁止读 contrast-pairs），故只有间接证据 | 未直接检验 |
| e | 预算 | 同一 caveat 集中披露 1 次、贡献段限定句 1、黄金段防御 0 | 通过 |
| f | 元语言 | `estimand / locked / adjudication / bounded scope conditions` 全部 0 | 通过 |
| g | 检索 | tier 1 命中 anton2025（主）+ desardine2023（对照），无空结果、无退化护栏 | 通过 |
| h | 重写门 | 覆盖率 100%，未触发；本轮无既成草稿可喂 | 未检验 |
| i | 迁移完整性 | 目录已删、零引用；六篇底本在索引与包中可取；worked example 不含底本清单与失败写法；头部元数据与 README 声明齐备 | 通过 |

**结果**：通过 7 项，未直接检验 2 项（d 仅间接、h 未跑）。按 §7 的通过线（≥7/9 且 a/c/d/h 必须通过）**不宣称达标**。
**过程事实**：本次跑在 `blocking` stage（项目 Downstream 未解），故产出的是带占位符的脚手架而非润色终稿——机制得到验证，refining/finishing 路径未验证。
**两个缺口（已在验收运行中如实报告）**：① Vault Brief 因 scope 内无 vault root 且唯一候选受污染控制禁用而跳过，保留引文占位；② 质量门的 GBL/JTBD/claim_fit/首尾句/Gate5 未单列成文件产物，只以结论形式核对。
**后续最小补测**：另跑一次带既成草稿的验收以检验重写门（h），并把今日 5 条失败原句作为固定回归集对照（d）。

---

## 9. 保留与本方案不做

**保留**：Story gate 与 Hypothesis Lock；七模块 taxonomy 与功能合同；反模式清单；78 张读解卡、32 份 reading-pairs、`tellings/` 讲法汇编；catalog 的三组标签；`_routing_tables.yaml`；`_evidence_registry.yaml` 证据分档；review 层对硬伤的发现能力。

**不做**
- 不搬库、不重构 v4 schema、不做 134 卡全量迁移——用索引与形状包作接口，卡片保持原样。
- 不把 story-blueprints 改造成模板生成器——它仍是读解层；段落大纲是 Phase 2 的产物，由它派生而非由它生成。
- 不做语义/embedding 检索，不返回 top 6（违反 `retrieval-contract.md` 的 1+1 与 one-learnable-move 纪律）。
- 不把 95 条 defect 全转规则（约 84% 是语料变体需求）。
- 不新增 skill 层级——层合同用一份声明文件实现。
- humanizer 不入学术写作路径。
- 不为任何期刊手写未经 catalog 核查的惯例（≥5 卡门槛）。
- 新规则一律正向句式；禁止式仅保留无法正向表达的硬护栏。
