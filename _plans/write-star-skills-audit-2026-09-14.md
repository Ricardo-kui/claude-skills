# write-* 系列审查（write-theory / write-methods / write-results + 横向）

- 日期：2026-09-14
- 触发：write-introduction 本轮优化后，用户要求核查同源问题是否存在于另外三个写作 skill
- 方法：四条只读审查车道并行；统一七轴（生成层 / 语料形态与索引 / 表达层 / 完成判据可核性 / 门禁与审查契约 / 契约对齐 / 登记与资产），判断标准挂 `writing-for-agents`
- 证据纪律：以下每条均有 `file:line` + 原文引用；本页只记录审查结论，不含改进方案
- 状态：**待用户裁定**（§9 列出四项须先裁定的问题，裁定前不应动手修）

---

## 1. 总判：四 skill × 三层的强弱矩阵

| skill | 生成层 | 语料迁移层 | 表达层 | 登记执行链 | 改稿分支 | 证据→主张承接 |
|---|---|---|---|---|---|---|
| write-introduction | 强（本轮补：O1–O3 大纲 + G1 借句表） | 强（本轮补：`corpus/_skeleton/` 390 verbatim/556 模板 + `build_indices.py`） | 中（有底本 id 与水位门，但入口分散） | **弱（无 record_feedback / 无语言 lint）** | 中（本轮才补「含改稿」触发词） | 弱（无 claim ladder / 支持判断 / story resolution） |
| write-theory | 弱（段落功能图无来源 id） | 弱（24 卡、无索引、无脚本） | 弱（phrasebank 只在 QC 后被提及） | 弱（声称接 `critique.per_file`，实为空壳且未披露） | 弱（无改稿分支） | **强（Soundness 协议 / 前提三分 / argument graph / conditionality gate）** |
| write-methods | 弱（M1–M10 已定义且真调用，但无段级布局产物、无底本记账） | 弱（95+ 变体，无索引；且字母变体有索引死角） | 中偏强（18 类微模板 + phrasebank + 因果档位有真实调用点） | **强（record_feedback.py + feedback-registry.json 24 条 + lint_methods_language.py）** | **强（Phase -1 三态 + revision_constraints）** | 中（可检验性门控 Phase 0） |
| write-results | 弱（R1–R9 定序存在，无借句表 / 底本 id / 覆盖率门） | 弱（99 变体、~350 原句锚点，无整读索引、无重建脚本） | 中（系数解读 / 经济显著性 / 幅度 / 诚实支持四类有句级 slot 底本） | **强（record_feedback.py + registry 28 active，schema 1.1.0 + lint_results_language.py）** | **强（Phase -1 + draft-revision-protocol）** | **强（hypothesis-fulfillment-map 双层支持判断 + claim-calibration 七级 ladder + story-resolution）** |

**总判一句话**：这不是「三个 skill 落后于 write-introduction」，而是**四者各缺一块**。write-introduction 本轮补上的恰好是另三个都缺的「布局层 + 语料入口 + 举证门」；而另三个已有的「登记执行链 + 改稿分支 + 证据→主张承接」，是 write-introduction 完全没有的。正确动作是双向移植，不是单向推广。

---

## 2. 共同根因（四条，四 skill 皆中）

### R-1 生成层缺「准入产物」：有功能定序，没有底本账本
四者都有「要写什么」的序列（intro 功能序列 / theory 段落功能图 / methods M1–M10 / results R1–R9），但只有 intro 本轮有了「先落借句表再落句」的准入产物。

- `write-theory/references/phase-2-architecture.md:52`「输出：**推荐的段落序列**」——只给功能标签，无来源 id
- `write-methods/SKILL.md:85`「尽量使用对应 slot 通用段落…改编，而非脱离语料自拟」——软约束，无 id
- `write-results/SKILL.md:88`「语料句式为改编底本…而非自拟」——同上，无 id
- 三者的 `SKILL.md` 均无 outline/generation protocol 等价物（grep 0 命中）

### R-2 语料迁移层缺可整读索引与重建脚本 → 语料体量大但不被消费
- `write-theory`：无 `corpus/_skeleton/` 目录、无 `scripts/`；原文锚点分散在 24 张卡内
- `write-methods`：`scripts/` 仅 lint/validate/record 三个，无索引重建；corpus 仅 `INDEX.md`（296 行 changelog）
- `write-results`：`scripts/` 仅三个；`corpus/INDEX.md` 混有历史快照声明（`:59`）与三个不同总变体数（`:107/195/229`）
- 三者生成时实际消费的是「registry 选择」或「2–4 变体比较节奏」，不是底本 id

### R-3 门禁与审查出口不同源 →「合规但平庸的 PASS」在三个节都可复现
- `write-theory` 出口 `theory-review`：`references/output-format.md:11` 用 ✓/△/✗，无 PASS 字段、无底本 id、无姿态/防御预算/元语言检查
- `write-methods` 出口 `methods-review`：`SKILL.md:36-40` ✓/△/✗ 表；且与本 skill 门**直接冲突**——`methods-review/SKILL.md:73` 把「标准误调整」列为必查项，而 write-methods 侧已放宽为可选（`wmf_1349cfa0`）；`methods-review/SKILL.md:60` 要求 Heckman/PSM 作为选择偏差检验，与 `robustness-menu.md:13` 的 Methods–Results 分工冲突
- `write-results` 出口 `results-review`：完成判据仅列 Step1-4，无 PASS 字段契约；确定性检查只有 `scripts/lint_results_language.py`（只扫 prohibited_patterns）
- 三者均无「底本覆盖率 / 水位 / 防御预算」这三件能量化拦住平庸输出的量

### R-4 完成判据为自评语言，不可布尔核对
- `write-theory/SKILL.md:26`「构念顺序 + 机制深度已定」；`:33`「审计 1–4 无未修复项」
- `write-methods/SKILL.md`：8 处完成判据中 6 处自评（`:33`「当前文本、修订边界和 feedback rules 已锁定」、`:44`、`:52`、`:75`、`:81`、`:106`）
- `write-results/SKILL.md:53`「输入来源已确定；假设-结果映射可用」；`:109`「自检清单逐条全过；反模式零命中」

---

## 3. write-theory 问题表

| # | 轴 | 问题 | 证据 | 严重度 | 映射 |
|---|---|---|---|---|---|
| T1 | 门禁/审查 | 无 quality-gates/water-level/pass-contract；出口用 ✓/△/✗，无 PASS 字段与底本 id → 可放行表达不达标的合格骨架 | `theory-review/references/output-format.md:11`；write-theory 无 pass-contract.md | **P0** | W-5 |
| T2 | 生成层 | 段落序列自撰，无来源枚举（连 intro 旧的 `routing:` 登记都没有） | `phase-2-architecture.md:52`；`SKILL.md:25` | P1 | W-1 |
| T3 | 生成层 | 无 O1–O3 大纲协议、无 G1 借句表：段序列与落句之间无准入产物 | `SKILL.md:29`「先骨架后句子，语料顺序≠段落顺序」（有纪律无产物） | P1 | W-1/W-2 |
| T4 | 语料形态 | 无 `_skeleton/` 等价索引、无脚本 | 目录不存在 | P1 | W-2 |
| T5 | 语料形态 | 原文锚点分散卡内，无 verbatim/模板计数与借句入口 | grep `原文锚点` 命中 24 文件；`SKILL.md:127` | P1 | W-2/W-7 |
| T6 | 表达层 | phrasebank/micro-templates 生成时不被调用，只在 QC 后提及 | `SKILL.md:100-106`；仅 `phase-1-diagnosis.md:116` 提 transition-signals | P1 | W-3 |
| T7 | 契约对齐 | alignment 只对账 5 维 story 字段；claim ceiling / unsupported_moves / 假设编号无逐条对账 | `corpus/meta/alignment_protocol.md` 输出表 4 行；`corpus/meta/paper_state_fragment.md` 无 claim_ceiling 字段 | P1 | W-9 |
| T8 | 生成层 | 无改稿/返工触发分支 | `SKILL.md` 与 references 无「改稿」 | P1 | W-10 |
| T9 | 登记 | 声称接 `critique.per_file`，该键为注释空壳，且未如实披露 | `SKILL.md:122`；registry `:7078-7084` 全为注释示例 | P1 | W-8 |
| T10 | 表达层 | 无自有机制语气库，指向 intro 的 phrasebank | `SKILL.md:105` 指向 `../write-introduction/corpus/phrasebank/hedging-strength.md` | P2 | W-3 |
| T11 | 完成判据 | Phase 2/4 判据为自评语言 | `SKILL.md:26`、`:33` | P2 | W-4 |
| T12 | 资产 | 死指针：registry 指向本 skill 不存在的 `scripts/` | `corpus/_evidence_registry.yaml:18`「MOVED to scripts/status_policy.yaml」 | P2 | W-7 |
| T13 | 登记 | leading word 漂移：同一段落图三命名（段落功能图 / 推荐的段落序列 / 段落功能地图） | `SKILL.md:35`、`phase-2:52`、`output-format.md:41` | P2 | W-6 |

`write-theory` 独有而 intro 缺失的机制（可反向移植）：
- A–G 七变体族 + routing_table + 17 个子协议（`SKILL.md:43-55`、`corpus/meta/routing_table.md`）
- Hard constraints #1–16 扁平台账（`SKILL.md:61-82`，每条附细则指针而非复述语料）
- Soundness 协议：前提三分 [D]/[S]/[E] + warrant 五测试 + 机制必要性门控 + 反例压力测试（`phase-4-qc-alignment.md:76-88`、`corpus/subprotocols/reasoning_soundness_protocol.md`）
- Contestability 反命题测试（`phase-4-qc-alignment.md:73`）
- 逐假设 argument graph（`SKILL.md:32`）
- Conditionality gate（`phase-3-hypothesis-derivation.md:9-19`）
- 段内四段位 Topic→Reasoning→Tokens→Wrap + 三类论据决策矩阵（`corpus/subprotocols/paragraph_layout.md`）
- Incommensurability L0–L3 + R1–R4 两阶段门控（`SKILL.md:16`、`:54`）

---

## 4. write-methods 问题表

| # | 轴 | 问题 | 证据 | 严重度 | 映射 |
|---|---|---|---|---|---|
| M1 | 生成层 | 无段级布局产物；槽位表即布局，无「先定功能再落句」步骤 | `SKILL.md:85` | **P0** | W-1 |
| M2 | 生成层 | 生成时无逐段底本 id 登记（无 G1 借句表 / 无来源列） | grep 无 outline/generation protocol；`SKILL.md:54-95` | **P0** | W-1/W-2 |
| M3 | 语料索引 | 无 `_skeleton/` 等价索引、无索引重建脚本 | `scripts/` 仅 3 文件；corpus 仅 `INDEX.md` | **P0** | W-2 |
| M4 | 语料索引 | `自然实验-DiD.md` 31 个变体标题中 11+ 字母变体（O–Y）不在「变体速查表」，而该表自称唯一入口 | `自然实验-DiD.md:15`「类型内变体选择的唯一入口」 | **P0** | W-2/W-7 |
| M5 | 语料索引 | validator 只匹配 `### 变体 \d+`，字母变体被静默漏计 → 数量对账通过是假阳性 | `validate_write_methods.py:126` | **P0** | W-7 |
| M6 | 审查契约 | 无 pass-contract 六字段；出口无底本覆盖率要求 | `methods-review/SKILL.md:36-40` | **P0** | W-5 |
| M7 | 审查契约 | 出口要求「标准误调整」必查，本 skill 门已放宽为可选 | `methods-review/SKILL.md:73` vs `wmf_1349cfa0` | **P0** | W-5 |
| M8 | 审查契约 | 出口要求 Heckman/PSM 作选择偏差检验，与 robustness-menu 的节间分工冲突 | `methods-review/SKILL.md:60` vs `robustness-menu.md:13` | P1 | W-5 |
| M9 | 完成判据 | 8 处判据中 6 处自评 | `SKILL.md:33/44/52/75/81/106` | P1 | W-4 |
| M10 | 表达层 | 微模板有调用点但无「每句位必须绑底本 id」；短语库是外部 intro 文件 | `SKILL.md:87`、`:88` | P1 | W-3 |
| M11 | 表达层 | M8 通用骨架鼓励含糊免责句，与本 skill 语态纪律直接矛盾 | `slot-M8.md:15`「Although… cannot be directly tested…helps reduce concerns」 vs `draft-revision-protocol.md:44` | P1 | W-3 |
| M12 | leading word | 槽位文件用 PREMIUM/STANDARD/EXPERIMENTAL，corpus 用 ROBUST/VERIFIED/EMERGING，双轨并存 | `slot-M1.md:5` vs `corpus/INDEX.md:23` | P1 | W-6 |
| M13 | 反馈登记 | R1 通道真实（JSON+script+lint），R2 仅一句声明、无写入通道 → 半实现 | `SKILL.md:116`；scripts 无 R2 脚本 | P1 | W-8 |
| M14 | 指针 | 23 处指向不存在的锚点「槽位骨架加载」（实际标题为「槽位目录与加载」） | `corpus/IV-2SLS.md:60` vs `SKILL.md:54` | P2 | W-6 |
| M15 | 复述 | Methods–Results 分工在 5 处复述 | `SKILL.md:24`、`robustness-menu.md:5`、`draft-revision-protocol.md:40`、`slot-M8.md:3`、`post-generation-checklist.md` | P2 | W-7 |
| M16 | 数字冲突 | SKILL 称「AMJ 约 30% 缺 M1」，slot-M1 称「28/28 篇使用」 | `SKILL.md:55` vs `slot-M1.md:5` | P2 | W-7 |
| M17 | 假想惯例 | 「变量名与 Results 表格完全一致」「排列顺序 DV→IV→Controls→Method」被写成硬规则，无范文现货证据 | `post-generation-checklist.md` Clarity 段；`methods-review/SKILL.md:52` | P2 | W-5 |
| M18 | 契约对齐 | 消费 story/storyline 属实，但无 claim ceiling / unsupported_moves 逐条对账 | `SKILL.md:37-42`；grep 仅命中 `draft-revision-protocol.md:3` | P2 | W-9 |

`write-methods` 独有而 intro 缺失的机制：
- **真实执行链的反馈登记**：`scripts/record_feedback.py`（fingerprint 去重 + supersedes）+ `references/feedback-registry.json`（24 条，schema 1.0.0）+ `scripts/lint_methods_language.py`（按 `prohibited_patterns` 扫描并在日期化修订记录前停止）
- `robustness-menu.md:5` 把节间分工写成「唯一权威载体」并以指针收敛（比 intro 更彻底的单一源声明）
- 可检验性门控 Phase 0：blocked storyline 时停止生成并输出「无法兑现的 storyline + 所需设计修复」
- `design-branches.md:5-30` 设计类型 → 槽位顺序重排 + 不适配槽位跳过
- `revision_constraints` 结构化 schema + stale source 作废 + 优先级链

（W-10 不适用：write-methods 有 Phase -1 三态模式 + `draft-revision-protocol.md`，返工分支完整。）

---

## 5. write-results 问题表

| # | 轴 | 问题 | 证据 | 严重度 | 映射 |
|---|---|---|---|---|---|
| R1 | 生成层 | 无可执行的段级生成序列，仅「段落确定后」松散改编，无 id | `SKILL.md:88` | P1 | W-1 |
| R2 | 生成层 | 零接线 story-blueprints（仅在即时范文检索处引用） | `SKILL.md:82` | P1 | W-1 |
| R3 | 语料/索引 | 无整读骨架/借句索引；`INDEX.md` 为变更日志 + 三个不同总变体数 | `corpus/INDEX.md:59/107/195/229` | P1 | W-2 |
| R4 | 语料/索引 | 生成消费 = 「比较节奏句法」，无底本覆盖率、无 self-drafted 占比登记 | `SKILL.md:74` | P1 | W-2 |
| R5 | 表达层 | 句法微模板/措辞库只作「按需选读」指针，无调用与验收 | `SKILL.md:92-94` | P1 | W-3 |
| R6 | 完成判据 | 多处自评语言；且无任何可计算通过量 | `SKILL.md:53`、`:109`、`:100` | P1 | W-4 |
| R7 | 门禁/审查 | `results-review` 无 PASS 字段契约，与本 skill 七门不同源 | `results-review/SKILL.md` 完成判据；`validation-protocol.md:1-7` | P1 | W-5 |
| R8 | 门禁/审查 | 「合规但平庸」通道：确定性检查仅 lint prohibited_patterns | `scripts/lint_results_language.py:1` | P1 | W-5 |
| R9 | 契约对齐 | 不读 `story.unsupported_moves` / claim ceiling，无逐条对账 | `SKILL.md:29` vs `paper-story-contract/references/schema.md:38` | P1 | W-9 |
| R10 | 契约对齐 | `claim-calibration` 七级 ladder 自建，未与项目锁定 claim boundary 对账 | `references/claim-calibration.md:11` | P1 | W-9 |
| R11 | 资产 | 失效指针：`SKILL.md:88`「（见路由 Step 3）」在本 skill 无定义处 | `SKILL.md:88` | P1 | W-7 |
| R12 | 资产 | 双层支持判断散见 12 个文件（规则多处复述） | `hypothesis-fulfillment-map.md:19-28` 等 | P2 | W-7 |
| R13 | 资产 | 「非显著必须报告」≥6 处、「因果语言」~20 文件复述 | `SKILL.md:126`、`boundaries.md:13` 等 | P2 | W-7 |
| R14 | 资产 | 陈旧资产：pilot 索引自标 shadow_only 且绑定旧 46 变体 | `corpus/_pilot_r2_index.yaml:2`、`:13` | P2 | W-7 |
| R15 | leading word | 「底本」在本 skill 泛指无 id 变体，与 intro 的「底本该附 id 与 citekey」漂移 | `SKILL.md:88` vs `generation-protocol.md` | P2 | W-6 |
| R16 | 登记 | 登记通道真实，但留软出口可降级为不落盘 | `feedback-protocol.md` §2.3 | P2 | W-8 |
| R17 | mixed 展演 | 有正面写法雏形与「不堆叠」禁令，但「例外集中披露一次」无单一规则句 | `slot-R7.md` Fragility 变体；`anti-patterns.md` | P2 | W-4/7 |
| R18 | mixed 展演 | 支持判断判据有书面定义，但无布尔核对，靠自评 | `hypothesis-fulfillment-map.md:19-21` | P2 | W-4 |
| R19 | 结构 | `slot-R7.md` 单文件 308 行承载 20+ EXPERIMENTAL 子变体，层级失衡；「按需加载」不足以保护 | `SKILL.md:57` | P2 | W-7 |
| R20 | 未验证资产 | `post-generation-checklist.md:38` 要求「至少报告一种预处理稳健性检验」，而 `slot-R7.md` 对应变体标「尚未经范文蒸馏验证」 | 两处 | P2 | W-2 |

`write-results` 独有而 intro 缺失的机制：
- **真实可执行反馈登记**：`scripts/record_feedback.py` + `feedback-registry.json`（28 active，schema 1.1.0）+ `lint_results_language.py`
- **双层支持判断判据**：`hypothesis-fulfillment-map.md:19-28`（baseline_verdict 4 值 + overall_evidence 4 值，含证据要求）
- **故事收束表**：`story-resolution.md:5` 八列 + Status Rules
- **claim 层级校准**：`claim-calibration.md:11` 七级 ladder + 过度声明动词表 + 「强主张四件套」
- **改稿分支**：Phase -1 + `draft-revision-protocol.md`

---

## 6. 横向：接线矩阵 / 重复定义 / 悬空引用 / 可移植性

### 6.1 接线矩阵

| skill | blueprint 卡（Five acts / section_learning） | packs | worked-examples | rhetoric-moves | `corpus/_skeleton` | gen/outline/water/pass 协议 |
|---|---|---|---|---|---|---|
| write-introduction | 真读（`outline-protocol.md:8-10` 读 `Five acts` + `section_learning.introduction.learn`） | 真读（`SKILL.md:78`；1 包） | **未接线**（仅 packs 内记派生来源） | 真读（多处） | 真读 | 齐全 |
| write-theory | 真读（间接，经 `section_learning.theory`） | 未接线 | 未接线 | 真读 | 未接线（无目录） | 无 |
| write-methods | 真读（间接，`section_learning.methods`） | 未接线 | 未接线 | 真读 | 未接线 | 无 |
| write-results | 真读（间接，`section_learning.results`） | 未接线 | 未接线 | 真读 | 未接线 | 无 |

要点：**blueprint 卡与 rhetoric-moves 已全线接线**；缺的是 `packs` 与 `_skeleton` 这后两类入口。`story-blueprints/v4/packs` 目录不存在；`v4/worked-examples/` 仅本轮上收的 1 个文件。

### 6.2 重复定义（须先裁定唯一源）

| 资产 | 冲突 | 判定 |
|---|---|---|
| **五病** | `write-introduction/corpus/storytelling/prose-craft-checklist.md` §5（7 项，含 Overclaiming / Defensive prose）vs `pollock-qc/references/prose-pathology.md`（5 项）vs `_polish-protocol.md:37-41` | **不一致，且 write-introduction 内部两处路由到不同源**：`water-level-gate.md:75` 称 prose-craft §5 为「唯一源」，`SKILL.md:89` 却路由到 pollock-qc。数量 5 vs 7 |
| **能量阶梯** | `render-rules.md:7-11`（本轮新建，自称唯一源）vs `corpus/storytelling/tension-escalation-protocol.md`（自带同义单调与断裂规则表）；`storytelling/_index.md:31` 又称后者为「模块能量级定义与断裂检测」 | **不一致**——本轮唯一源化只做了局部，制造了新的重复定义 |
| GBL Four-Move | `diagnose-introduction/references/golden-biddle-locke-four-moves.md` 定义 → `quality-gates.md:5-18` 映射 → `front-end-mode.md:40-46` 指针 | 一致 |
| 首尾句测试 | `quality-gates.md:44-46` vs `rejection-signals.md:5-7` 指针 | 一致 |
| 段落论证文法 | 唯一定义 `_argument-grammar.md:10-57`，其余 6 处为指针 | 本体一致；但**「五问」名称被 4 套规则复用**（论证五问 / Booth 证据五问 / Booth Ch09 五问 / warrant 五测试）——术语碰撞 |
| 异议预判 problem 级三类 | `quality-gates.md:48-64` 唯一 | 单一定义 |
| 语料优先改编 / 角色先于风格 | `_argument-grammar.md:8` + `_polish-protocol.md:17` + 4 个 SKILL.md + 6 个 rhetoric-move 文件逐字同一段 | 措辞一致但多处复述；methods/results 版本**漏掉「角色先于风格」与角色序列**，概念覆盖不全 |

### 6.3 悬空引用

**真缺失（整库不存在）**
- `write-introduction/corpus/storytelling/prose-craft-checklist.md:600` → `references/alignment-checks.md`
- `write-introduction/corpus/storytelling/prose-craft-checklist.md:602` → `ACADEMIC_COMMUNICATION.md`
- `write-results/references/claim-calibration.md:3` → `references/overclaim-calibration.md`
- `write-methods/references/paper-state-schema.md:52` → `references/robustness-diagnosis.md`（write-methods 无此文件；该文件在 write-results 侧）

**路径基准（见 §8 的推翻说明，不得按 w27 原报告批量改）**

**零引用/弱引用卡片**
- `write-methods/corpus/micro-templates/multi-source-matching.md`、`opening-anchors.md`：仅出现在 `micro-templates/INDEX.md`，SKILL.md 只泛读 INDEX → 弱引用
- `write-theory` / `write-results` corpus：无零引用卡

### 6.4 write-introduction 五机制的可移植性

| 新机制 | 判定 | 理由 |
|---|---|---|
| `outline-protocol` | 需按节改写 | O1 依赖 blueprint `Five acts` + `section_learning` + packs，只有叙事节有；theory 用 phase-2-architecture、methods/results 用槽位序列作段结构底座 |
| G1 借句表 | 需按节改写 | 依赖各节骨架索引；三者无 `_skeleton`，须先建等价 id 表 |
| 水位门（含底本覆盖率与重写门） | 需按节改写；覆盖率子项对三者暂不适用 | 覆盖率需要借句表 + 骨架索引两件前置；methods/results 为审计体裁，framing 豁免口径不同 |
| **pass-contract 六字段** | **可原样搬** | 字段为通用审查输出合同，语义按节微调即可 |
| `corpus/_skeleton` 骨架索引 | 需按节改写 | `build_indices.py` 机制可复用，索引内容按节组织 |

---

## 7. 本轮自查出的两处「我造成的重复定义」（须认领并修）

1. **能量阶梯**：我为了唯一源化新建 `render-rules.md` §能量阶梯，但未处理既有的 `tension-escalation-protocol.md`（同义单调 + 断裂规则）与 `storytelling/_index.md:31` 的「定义处」声明 → 制造了三处并存。
2. **五病**：`water-level-gate.md:75` 指向 `prose-craft-checklist.md` §5，而 `SKILL.md:89` 既有路由指向 `pollock-qc/references/prose-pathology.md`，两份定义数量还不同（7 vs 5）→ 同一 skill 内两个「唯一源」。

教训与用户既定规则一致：**唯一源化必须先在库里核实是否已存在同义定义处**，否则局部声明会制造新的重复。

---

## 8. 被推翻 / 存疑的审查结论（不得据原报告行动）

1. **w27 称「`contrast-pairs/` 整目录不可达、不被任何 reference 指向」——已证伪。**
   实际有三处指针：`corpus/packs/portfolio-governance.md:101`、`corpus/packs/_index.md:23`、`references/generation-protocol.md:93`（明确写「见 `../corpus/contrast-pairs/_index.md`；……两目录互为镜像」）。
   准确表述应为：目录可达，但它是 G3 的**镜像表**而非流程**步骤**，没有任何步骤要求在生成时读它 → P2 级「提到不作为步骤」，不是 P0 级「不可达」。

2. **w27 的「`../` 应为 `../../`」批量修法——判定为方向错误，禁止执行。**
   pi 的解析约定为「相对 skill 目录（SKILL.md 所在目录）解析」；按此约定，`references/*.md` 中的 `../story-blueprints/...` 解析为 `skills/story-blueprints/...`，**正确**；而少数写成 `../../story-blueprints/...` 的（如 `write-theory/references/phase-4-qc-alignment.md:27`、`write-results/references/` 部分文件）会解析到 `skills` 的父目录，**才是异常**。
   佐证：同一字符串在四个 skill 的 `SKILL.md`（skill 根）与 `references/*.md` 中写法一致，说明意图统一是「自 skill 目录」；`writing-for-agents/SKILL.md` 无路径解析规定。
   **该项须先由用户裁定基准，再决定改哪一侧。**

---

## 9. 待裁定清单（裁定前不动手）

| # | 待裁定 | 影响面 |
|---|---|---|
| D-A1 | 五病唯一源：`prose-craft-checklist.md` §5（7 项）还是 `pollock-qc/references/prose-pathology.md`（5 项）？ | write-introduction 两处路由 + 四 skill 的措辞润色入口 |
| D-A2 | 能量阶梯唯一源：`render-rules.md` §能量阶梯 还是 `tension-escalation-protocol.md`？（本轮新造重复，须消解） | write-introduction 四个消费方 |
| D-A3 | 路径基准：`../` 是「自 skill 目录」还是「自当前文件目录」？ | 约 30 处指针的改法方向 |
| D-A4 | 审查出口是否统一到 pass-contract 六字段（三处 review skill 各改一次），还是每节自立契约？ | `theory-review` / `methods-review` / `results-review` 与三个 write-* 的门对齐 |
| D-A5 | 反馈登记是否抽成共享实现（现为各 skill 一份，且 schema 1.0.0 vs 1.1.0 不一致）？ | 四个 skill 的登记链 + write-introduction 需新建 |
| D-A6 | `methods-review` 两条假想惯例（SE 必查、Heckman 必做）与 `post-generation-checklist` 两条（变量名一致、DV→IV→Controls→Method 列序）是否按评审校准规则撤下？ | Methods 审查标准 |
| D-A7 | 三个 skill 是否各自建 `corpus/_skeleton` 等价索引（成本：3 × 抽取 + 回源校验）？ | 语料迁移层能否真正被消费 |
