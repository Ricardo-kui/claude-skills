# write-* 系列第二轮优化方案（write-theory / write-methods / write-results + 横向收口）

- 制定日期：2026-09-14
- 上游依据：`_plans/write-star-skills-audit-2026-09-14.md`（四车道只读审查，逐条附 `file:line` 与原文引用）
- 本方案只覆盖**审计已证据化的缺陷**；审计未覆盖的面不在本轮目标内
- 状态：§7 八项裁定已定（2026-09-14，见下表）；据此展开。裁定落地后新暴露的**执行细节**已在 §9 定稿（2026-09-14 用户确认 §9.1 用 `_shared/`），全部可直接执行。

---

## 0. 已完成的前置批次（Batch 0，本方案的前提）

| 项 | 交付 | 校验 |
|---|---|---|
| D-A1 五病三层归位 | 定义层 = `pollock-qc/references/prose-pathology.md`（唯一源，已加声明）；操作层 = `_polish-protocol.md` §3（保留三条独有增量）；嵌入层 = `prose-craft-checklist.md` §5（保留跨节嵌入点）；Overclaiming 与 Defensive prose 拆为 §6.1/§6.2，判定权归 `water-level-gate` 姿态与防御预算 | 6 个引用方 20 处旧号已改，全库 `§5.6/§5.7` 残留 0 |
| D-A2 能量阶梯撤回 | 删除自造的六元链与不存在的「语料卡能量标注」字段；`render-rules.md` Hook #4 恢复三元链；三处消费方（`output-format`、`SKILL.md`、`reader-conversion-sequence`）改为「叙事阶段 + 倒退检测」，唯一源 = `tension-escalation-protocol.md` | `能量标注` / 六元链 / `§能量阶梯` 在运行时文件中残留 0 |
| D-A3 路径基准 | 四个 `write-*/SKILL.md` 第 9 行写入基准声明；24 处 `../../<sibling>` → `../<sibling>`（逐一双向验证）；新增 `skill_pointer_check.py` | 假阳性由 889 降到 250（五 skill）；脚本三基准可分类计数 |
| 路径存量分诊（部分） | 12 处「文件目录基准」家族的跨 skill 指针已登记待改（附正确目标形态） | 12 条改写形态 `exists=True` 全通过 |

**Batch 0 的教训（写入纪律）**：唯一源化必须先在库里核实是否已存在同义定义处；本轮的「能量阶梯」与「五病」两处重复，都是局部唯一源化制造的。

---

## 1. 本轮成功判据（可验收，非自评）

1. **生成层**：三个 skill 各自能回答「这一段从哪个底本 id 来、为什么这么排」——即有段级布局产物（含来源列）+ 底本记账（借句表），且完成判据可布尔核对。
2. **语料层**：三个 skill 各有可整读骨架索引 + 可重跑的重建脚本；`write-methods` 的字母变体死角归零（索引条目数 = 文件内变体标题数）。
3. **门禁层**：三个 review 出口与对应 write-* 的门字段一一对应，且能挡住「合规但平庸」——判据里必须有至少一个**可计算的量**（底本覆盖率或等价物）。
4. **登记层**：`write-introduction` 补上可执行的代码键与语言 lint；四者 registry schema 统一。
5. **指针层**：`skill_pointer_check.py --strict` 在四个 write-* 内 missing=0，或每条 missing 都有分诊结论。

---

## 2. 工作项（按批次，含证据与做法）

### Batch 0.5｜提交当前工作区为基线（D-B8 = 先提交，第一步做）

- 现状：工作区 64 项未提交（13 未跟踪 / 3 删除 / 47 修改 / 1 增改），含 Batch 0 三条裁定的全部落地与新增 `skill_pointer_check.py`（被根 `.gitignore *` 忽略，须 `git add -f`）。
- 动作：把这 64 项**作为一个基线 commit** 提交（信息覆盖 D-A1/A2/A3 + 脚本），再开 Batch 1 起的新批次。理由：本轮已发生一次「路径基准判断反复」，需要清晰的回滚粒度与事故隔离。
- 边界：只提交、不推送（除非你明确要求）；不把可能含密文件纳入；`_plans/` 两份方案文件一并提交。
- 验收：`git status` 干净（或仅剩你有意保留的未跟踪项）；`git log -1` 为本基线；`skill_pointer_check.py` 已被跟踪。

### Batch 1｜write-methods 语料死角（P0，最小可独立交付｜D-B5 = 保留字母并修）

| 项 | 证据 | 动作 | 验收 |
|---|---|---|---|
| B1.1 字母变体索引死角 | `corpus/自然实验-DiD.md:15`「类型内变体选择的唯一入口」，但 11+ 个字母变体（O–Y）不在速查表 | **保留字母命名**（D-B5，不回改数字以免动正文引用）；把 O–Y 全部补进速查表 | 速查表条目数 = 文件内 `### 变体` 标题数 |
| B1.2 validator 正则漏计 | `scripts/validate_write_methods.py:126` `r"^### 变体 \d+"` | 正则改为 `^### 变体 [0-9A-Z]+`（覆盖数字与字母）；新增「索引条目数 = 变体标题数」断言 | 故意删一条索引 → 校验失败 |
| B1.3 残留占位标题 | `自然实验-DiD.md:95` `### 变体 N: [来源论文] (YYYY-MM-DD)` | 替换为真实来源或删除 | 无占位标题 |
| B1.4 双轨状态词表 | `slot-M1.md:5`（PREMIUM/STANDARD/EXPERIMENTAL）vs `corpus/INDEX.md:23`（ROBUST/VERIFIED/EMERGING） | 裁到单表：保留 corpus 的 ROBUST/VERIFIED/EMERGING（与 evidence_registry 同源），slot 那套改指针 | 全库单一状态词表 |
| B1.5 索引文件职责 | `corpus/INDEX.md` 混有历史快照与三个不同总变体数（`:59/107/195/229`） | 拆为「当前索引」与「变更日志」两段；总数只留一处 | 单一总数，且与脚本输出一致 |

> D-B5 说明：字母与数字混用是历史产物；回改数字需改动 corpus 内外所有对 `变体 O–Y` 的引用，风险高于收益。裁定为保留字母、把索引与校验补齐。

### Batch 1b｜能量级卡级标注声明定义处（D-B6 = 保留并声明定义处）

- 现状：`## 能量级` 小节真实存在于 4 张语料卡（`hooks/14-paired-disasters.md`、`hooks/21-dual-industry-trend.md`、`hooks/22-twin-complication.md`、`tensions/18-context-generalizability.md`），另有 2 个 mode 文件（`references/qualitative-mode.md:64`、`references/theory-paper-amr-mode.md:78`）称「Gap 类型决定 Tension 的能量级」。这是**卡级窄概念**，与 Batch 0 撤掉的「跨模块六元链」不是一回事。
- 动作：保留这 4 张卡的 `## 能量级` 标注；在 `corpus/hooks/_index.md`（或语料层单一处）声明「能量级 = 单卡内 Hook/Tension 开场强度档位，定义处见此；不构成跨模块单调链（跨模块顺序见 `tension-escalation-protocol.md` 的叙事阶段）」。两个 mode 文件的「能量级」加一句指针指向该定义处。
- 边界：不新增卡级能量标注、不把它接回任何跨模块规则、不与叙事阶段混用。
- 验收：`能量级` 仅作为卡级概念存在且有唯一定义处；grep `能量级` 命中均可追溯到该定义处或其指针；无任何「跨模块能量单调」表述复活。

### Batch 2｜骨架索引三件（工作量最大｜D-B1 = 两级）

为 `write-theory` / `write-methods` / `write-results` 各建 `corpus/_skeleton/` 等价物，**采用两级结构**（D-B1）：
- **一级路由页**（`_skeleton/_index.md`）：按各 skill 的现有选择轴列子索引入口——write-methods = 设计类型（面板数据-OLS / 自然实验-DiD / IV-2SLS / 事件研究法 …）；write-results = 模型族（OLS-FE / 计数模型 / DiD / 事件研究法 …）；write-theory = A–G 变体族（其现有 routing_table 的选择轴）。
- **二级模块内清单**（每个子索引一文件）：`id | 槽位/修辞功能 | citekey | 原文锚点 | 状态(verbatim/模板)`。槽位维度 = M1–M10（methods）/ R1–R9（results）/ 段落功能（theory）。
- 两级的理由（对齐裁定）：这三节语料体量远大于 intro（methods 95+ 变体、results 99 变体、theory 24 卡 + 17 子协议），单层清单读不完等于不被读；一级路由让「选设计类型 → 只读该类型的借句清单」成为可整读单位。
- 复用 `build_indices.py` 机制——**抽为共享索引器** `_shared/indexing/build_indices.py`（见 §9），按 skill 参数化 corpus 轴，保证 `--check --verify` 等价：verbatim 回源校验 + 锚点局部性校验。
- **可计算的量（覆盖率）定义**：coverage = 引用了二级底本 id 的「论证型槽位/段」占比。methods/results 属审计体裁，纯程序性槽位（如样本年份陈述）列入 framing 豁免、不进分母——**每个 skill 的豁免清单须在其 outline/generation 协议里显式列出**，否则覆盖率可被规避。
- 验收：抽样 20 条 verbatim 回源逐字一致；锚点可定位率 100%；一级路由页 ≤120 行、每个二级清单 ≤400 行（超出再拆）；「一次真实生成是否真的读了二级清单」纳入 Batch 7。

### Batch 3｜生成层协议三件

| skill | 段级布局产物 | 底本记账 | 完成判据布尔化 |
|---|---|---|---|
| write-theory | 新增等价 `outline-protocol`：段级功能序列 + **来源列**（A–G 变体族 + blueprint 卡 `section_learning.theory`） | 新增借句表（id 级） | `SKILL.md:26/33` 等自评判据改可回答「是/否」 |
| write-methods | 在已有 `design-branches.md` 的「设计类型→槽位顺序」之上加**来源列** | 新增借句表 | 6/8 自评判据改写 |
| write-results | R1–R9 与假设映射之上加**来源列** | 新增借句表 | 自评判据改写，并补一个可计算的量（覆盖率） |

三者的「可计算的量」按 D-B1 的索引轴定义（如「有底本 id 的论证型段占比」）。

### Batch 4｜审查契约统一与假想惯例降级（D-B2 = 共享文件；D-B4 = 降级为可选并标注）

- **审查契约提升为共享文件**（D-B2）：新建 `_shared/pass-contract.md`（六字段唯一源），把现 `write-introduction/references/pass-contract.md` 内容迁入并改为指针。`intro-review` / `theory-review` / `methods-review` / `results-review` 四个出口都引用该共享文件，各自只声明**节别增量字段**（不复制六字段定义）。理由：挂在 write-introduction 下会让 methods/results 反向依赖 intro。
- **四条假想惯例降级并标注**（D-B4，全部降为「可选风格建议」并附证据状态，不删除）：`methods-review/SKILL.md:73`（SE 调整必查）、`:60`（Heckman/PSM 必做）、`post-generation-checklist.md`（变量名与 Results 表格完全一致；列序 DV→IV→Controls→Method）。每条改写为「可选建议 · 证据状态：无 ≥5 卡范文现货支撑」，并登记进共享 registry（Batch 5）。
- **两条单一源冲突**（与 B4 同批但独立于降级）：修 `methods-review:60` 与 `robustness-menu.md:13` 的节间分工冲突；修 `slot-M8.md:15` 的通用免责骨架与 `draft-revision-protocol.md:44` 语态纪律的矛盾（M8 骨架改为「须点名具体威胁」）。
- 验收：四个 review 出口的 PASS 字段与共享六字段逐条对应；被降级项均带证据状态标签；两条冲突各收敛到单一源。

### Batch 5｜登记层抽共享 + 双向移植（D-B3 = 抽共享）

- **抽共享实现**（D-B3）：把 methods/results 已有的 `record_feedback.py`（fingerprint 去重 + supersedes）与语言 lint 引擎抽到 `_shared/feedback/`——`record_feedback.py`（共享脚本）+ `schema.json`（共享 schema）；各 skill 保留自己的 `references/feedback-registry.json`（数据）与 `prohibited_patterns.*`（各自违禁词表），只引用共享引擎与 schema。
- **schema 统一**：核对 methods 与 results 现有 registry 结构，以较新者为基准统一；对旧结构条目写一次性迁移并记录。**硬约束：抽取过程不得改动两份现有 registry 的数据内容**，抽完各自跑一次原 validator 证明零回归。
- **移植回 write-introduction**：补 `references/feedback-registry.json`（数据）+ 引用共享引擎 + `prohibited_patterns`（覆盖 `estimand / locked / adjudication / bounded scope conditions / contribution boundary` 等元语言，与水位门的 meta_language 字段同源）。
- 收口 `write-methods` 的 R2 半实现（`SKILL.md:116` 只声明无通道）。
- 验收：四个 skill 用同一引擎与 schema；故意写入一条违规句 → lint 报错并定位；methods/results 原 validator 仍全绿（零回归）。

### Batch 6｜指针存量分诊 + 上严格基准（D-B7 = 上）

| 桶 | 数量（五 write-*） | 处理 |
|---|---|---|
| 文件目录基准家族 | 12 | 按已裁定基准改写（清单已备，`../../../<sibling>/` → `../<sibling>/`；`../../references/` → `references/`） |
| `no_baseline` | 95 | 逐条判定：是「裸 `<sibling>/...`」还是文档约定；前者批量补 `../`（改成 `../<sibling>/...`） |
| `file_absent` | 155 | 人工分诊：工作区产物（`paper-state.yaml`、`status.csv` 等）→ 加入白名单；跨 skill 裸文件名 → 补前缀；真断链 → 修或删 |

- **上严格基准**（D-B7）：给 `skill_pointer_check.py` 加 `--strict`（只认三条裁定基准 A/B/C，不采「多基准兜底」的宽松匹配），把 12 + 95 处按裁定基准批量改到位，使严格模式下 `missing = 白名单` 而非既存断链。
- 白名单单列一个文件（`_shared/pointer-allowlist.txt`，或脚本内常量），每条附一句「为什么它不是断链」。
- 验收：`skill_pointer_check.py --strict write-introduction write-theory write-methods write-results` 的 missing 仅剩白名单条目；每次批量改动后复跑并抽样双向解析。

### Batch 7｜验收

- 每个 skill 跑一次真实生成（建议用第二个项目而非共同所有权，避免与已完成稿混淆），检查：是否有底本 id、覆盖率、段级来源可核、完成判据是否可布尔回答。
- 把本轮审计的 P0 项各转成一条可重跑断言（methods 索引死角、validator 正则、三份 review 的字段对齐、write-introduction 的 lint）。

> **执行记录（2026-09-15，终验残留收口）**：四条 P0 断言中三条已并入各自维护期脚本（methods 索引死角 = `validate_write_methods.py` 对账硬断言、validator 正则 `[0-9A-Z]+`、write-introduction 语言 lint = `lint_introduction_language.py`）；第四条「review 字段对齐」落地为根目录 `pass_contract_check.py`——契约侧三检（§一 六字段冻结集、§二 硬规则在位、§三 消费方表登记）+ 四出口四检（指针 / 节别增量声明 / 免本地字段定义 / 免漂移拼写），并接入 `_shared/indexing/check_all.py`（`== pass-contract ==` 节，维护期一次跑全）。首跑即抓到并修正一处真实词汇漂移（intro-review「调用增量」→「节别增量」，与契约 §三及另三出口统一）；负向验证：注入漂移拼写与删除增量声明均 FAIL。**三节真实生成验收仍未留痕**（theory/methods/results 各一次端到端，见 2026-09-15 终验报告），为 Batch 7 唯一未闭环项。

---

## 3. 依赖与顺序

```
Batch 0（已完成：D-A1/A2/A3）
  └─ Batch 0.5 提交基线（D-B8，必须先做，是后续所有批次的前置）
       ├─ Batch 1   write-methods 死角（独立）
       ├─ Batch 1b  能量级卡级定义处（独立，小）
       ├─ Batch 2 ── 索引两级（D-B1 已定）
       ├─ Batch 3 ── 依赖 Batch 2（借句表需要二级 id）
       ├─ Batch 4 ── D-B2/D-B4 已定；先建 _shared/pass-contract.md
       ├─ Batch 5 ── D-B3 已定；先建 _shared/feedback/
       ├─ Batch 6   指针分诊 + --strict（独立，可与 2/3 并行）
       └─ Batch 7 ── 依赖 1–6
```

写者纪律：
- Batch 2 与 Batch 3 触及同一批 `corpus/` 与 `references/` 文件，必须**同一写者串行**。
- Batch 1、1b、4、5、6 可与 2/3 并行（文件集不交）。
- **Batch 4 与 Batch 5 都要写 `_shared/`**：两者先各自建独立子路径（`_shared/pass-contract.md` vs `_shared/feedback/`），不撞文件，可并行；`_shared/README.md` 由先完成的一方建、另一方只追加，或由 orchestrator 收口。另须在 Batch 0.5 之后的第一个 commit 里带上 `.gitignore` 的 `!_shared/` 两行，避免新目录被静默忽略。

---

## 4. 不做（沿用第一轮的边界，并新增本轮教训）

- 不搬库、不重构 `story-blueprints` v4 schema、不做 embedding/语义检索、不新增 skill 层、不在学术路径引入 humanizer。
- 不把审计的 P2 文档漂移全部当缺陷修；P2 只在被证据说明会影响运行时行为时才修。
- 无 ≥5 卡证据不写期刊惯例；撤下的假想惯例不换成新的自造惯例。
- **新增**：任何「唯一源化」先 grep 全库同义定义处，找不到反证才立声明（Batch 0 的两处重复即此教训）。

---

## 5. 风险

| 风险 | 影响 | 缓解 |
|---|---|---|
| Batch 2 抽取量估计不足 | 三个 skill 的 corpus 体量远大于 intro（methods 95+ 变体、results 99 变体、theory 24 卡） | 先抽一个 skill 试点并估算，再决定是否分批；索引不足则先做「模块级路由 + 模块内 verbatim 清单」两级 |
| 索引轴选错 | 索引建立后使用习惯错位，等于再造一个不被读的资产 | D-B1 优先裁定；试点的验收标准包含「一次真实生成是否真的读了它」 |
| 审查契约统一打断现有 review 流程 | 三份 review skill 同时改，短期不可用 | 逐份改、每份改完即跑一次对应审查 |
| 指针批量改动误伤 | 已发生一次（24 处 `../../` 的基准之争） | 只按已裁定基准改；每批改动跑 `--strict` 并抽样双向解析 |
| 改动量累积未提交 | 当前工作区 64 项未提交（13 未跟踪 / 3 删除 / 47 修改） | 见 D-B8 |

---

## 6. 建议执行顺序（资源视角）

0. **Batch 0.5 提交基线（0.2h，第一步）**
1. Batch 1（1.5h）+ Batch 1b（0.3h）+ Batch 6（2h）三者并行
2. Batch 2 试点一个 skill（2h）→ 估算后 Batch 2 其余（2–4h）
3. Batch 3（3h，紧接 Batch 2 同写者）
4. Batch 4（1.5h）与 Batch 5（2h）并行（各自 `_shared/` 子路径）
5. Batch 7 验收（2h）

D-B1–D-B7 均已裁定，无需再等裁定门；唯一建议你开工前确认的是 §9 的一项（共享物理位置与 schema 基准的最终形态）。

---

## 7. Decision Register（2026-09-14 已裁定）

| # | 问题 | 裁定 | 落到批次 |
|---|---|---|---|
| D-B1 | 骨架索引组织轴 | **两级**：一级模块路由页 + 二级模块内清单 | Batch 2 |
| D-B2 | 审查契约落法 | **提升为共享文件**：`_shared/pass-contract.md`（2026-09-14 定址），四出口引用 + 各声明节别增量 | Batch 4 |
| D-B3 | 登记链实现 | **抽共享**：`_shared/feedback/`（共享引擎 + schema，2026-09-14 定址），各 skill 只留数据与违禁词表 | Batch 5 |
| D-B4 | 四条假想惯例 | **降级为可选并标注证据状态**（不删除） | Batch 4 |
| D-B5 | 字母变体命名 | **保留字母并修**索引与校验（不回改数字） | Batch 1 |
| D-B6 | 卡级「能量级」 | **保留并声明定义处**（卡级窄概念，与跨模块链解耦） | Batch 1b |
| D-B7 | 指针严格基准 | **上** `--strict`；12 + 95 处按裁定基准批量改到位 | Batch 6 |
| D-B8 | 64 项未提交 | **先提交为基线**再开新批次 | Batch 0.5 |

---

## 8. 本方案与第一轮方案的关系

第一轮（`write-introduction-optimization-2026-09-14.md`）解决的是 intro 单节的「布局层 + 语料入口 + 举证门」；本轮解决的是**同源缺陷在另外三节的存在形式**，并首次做**双向移植**（把 methods/results 已有的登记执行链、改稿分支、证据→主张承接移植回 write-introduction）。两轮共用同一条教训：**先证明资产真的被读，再谈质量**。

---

## 9. 开工前需确认的执行细节

裁定已定，但落地时有几处口径要先说清楚——只有第 1 项建议你点头，其余为可直接执行的默认口径，列出供你否决。

1. **`_shared/` 的物理形态与 schema 基准（2026-09-14 用户已确认 `_shared/`）**：D-B2/D-B3 都落在新建的 `_shared/`（`_governance/` 章程自述「只在语料维护期使用，不参与日常写作运行」，不接纳运行期门禁件，故不用它）。拟定结构：
   - `_shared/pass-contract.md`（六字段唯一源；现 `write-introduction/references/pass-contract.md` 内容迁入，原处改指针）
   - `_shared/feedback/record_feedback.py` + `_shared/feedback/schema.json`（共享引擎与 schema）
   - 各 skill 保留 `references/feedback-registry.json`（数据）与各自 `prohibited_patterns.*`
   - **schema 基准**：以 `write-results` 的 1.1.0 为准统一（较新），`write-methods` 1.0.0 数据做一次性迁移。
   - 落地附带：新建 `_shared/README.md` 声明「运行期共享件」定位与 `_governance/`（维护期治理）的边界；`.gitignore` 追加 `!_shared/` `!_shared/**`（allowlist 式忽略，漏加即静默丢文件）；`_governance/README.md` 章程不改，其自身 3 处 `../../` 仍归 Batch 6。
2. **共享索引器的落点**（默认执行）：Batch 2 的重建脚本核心抽为 `_shared/indexing/build_indices.py`，各 skill 传参调用（语料轴、模块名表、卡片路径规则按 skill 配置）。
   - **执行记录（2026-09-15，已落地）**：引擎落位 `_shared/indexing/indexing_engine.py`（有意不叫 `build_indices.py`——消除与各 skill 适配器同名遮蔽的脆弱性，偏离本条字面路径、意图不变）；承接工具层 / Entry·Unparsed / materialize（钩子化）/ verify 回源与抽样 / 渲染原语 / 写盘 / CLI / `entrypoint`（SUMMARY 行 + OSError·ValueError→exit 2）。三个适配器同名同路径保留（生成物头部措辞零改动），theory 的四分支解析器、registry 状态链、7 字段 Entry 与本地 verify（e.file/截断口径）及 methods/results 的模板文本、锚点校验器各自保留——引擎只承接逐字同源代码。零回归证明 = blob 哈希门（results 23 / methods 26 / theory 24 个生成物逐字节一致）+ 双 validator PASSED；新增维护期漂移门 `_shared/indexing/check_all.py`（commit 1f41fe0 / 34873c3 / 4dd8195 + 收尾批）。write-introduction 的解析器不同源、本轮不并入（2026-09-15 用户裁定）。
3. **覆盖率分母的豁免清单**（默认执行）：methods/results 的程序性槽位（样本年份、变量名陈述等）列入 framing 豁免、不进覆盖率分母，豁免清单显式写在各自 outline/generation 协议里（否则覆盖率可被规避）。
4. **review 出口短期不可用的窗口**（默认执行）：Batch 4 三份 review 逐份改、每份改完即跑一次对应审查，不同时停三份。
5. **不推送**（默认执行）：Batch 0.5 只 `git commit` 不 `git push`，除非你明确要求。
