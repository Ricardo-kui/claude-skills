# Paper Distillation Manifest (PDM) — Schema v1.0

PDM 是 `distill-paper-exemplar` 唯一的跨层交接物：一篇论文一份，承载整篇输入消费的
分解结果、四节蒸馏产物索引、跨节一致性、story 卡状态与写回门禁。schema 无独立顶层 key，
文件即 manifest。

## 文件布局（并行安全）

```
<distill-work>/<citekey>.pdm.yaml        # PDM 根，仅主循环写（默认随工作目录落在
                                         # ~/.claude/distill-work/；--outdir 留档时同跟随）
<distill-work>/<citekey>.pdm/            # L0 工作目录（preprocess_l0.py 生成；默认
                                         # ~/.claude/distill-work/ 下，Vault 之外，
                                         # 可随意删；--outdir 才落到论文旁留档）
  fulltext.text-only.md                  # 剥除 base64 后的全文（唯一可读的“全文”）
  l0_manifest.json                       # 切片检测报告（行区间、词数、unknown 节、
                                         # structure_type: classic-imrad | extended-intro
                                         # | formal-model | unknown —— extended-intro 时
                                         # theory 路由到引言切片，见 SKILL.md L0）
  sections/introduction.md               # 物化切片（text-only；L1 子任务的输入）
  sections/theory.md / methods.md / results.md / discussion.md
  sections/<section>.json                # 各分节 skill 的 JSON/报告（子任务写）
  sections/<section>.report.md           # （可选）该节 skill 的 markdown 报告
  feedback/<section>.feedback.yaml       # 该节 skill_design_feedback（子任务写）
  writeback_plan.<section>.yaml          # corpus_precheck.py 产物：选带/查重/锚点（写回的唯一依据）
```

**铁律**：原始 paper-import MD 含 base64 图片（单文件 44–89% 字节、单行可达 100KB），
任何 distill 代理都不得直接读取；一律经 `fulltext.text-only.md` 与 `sections/*.md`。
切片检测保守：识别不出的节在 manifest 标 `unknown`，主循环人工补齐，不猜。

并行分发时，子任务只写自己的 `sections/*` 与 `feedback/*`；主循环在每节完成后把
`status`/`writeback`/`identity` 合并进根文件。**任何进程不得同时改写根文件。**

## Schema

```yaml
pdm_version: 1.0
paper_id: "<citekey>"
title: ""
authors: []
year: ~
journal: ""

source_provenance:
  fulltext_md: "<绝对路径>"            # 权威源（MinerU/OvisOCR2 输出；含 base64，禁止直读）
  text_only_md: "<citekey>.pdm/fulltext.text-only.md"   # L0 预处理产物，代理可读
  zotero_ref: "<path 或 citekey>"     # 元数据源（Zotero）
  ingestion: "paper-import (OvisOCR2|MinerU)"
  section_slices:                     # 物化切片路径（L0 脚本生成；人工补切时手填）
    introduction: "<citekey>.pdm/sections/introduction.md"
    theory: ""
    methods: ""
    results: ""
    discussion: ""                    # 可选：归 results 或单列

status: manifest | distilling | integrated   # 论文级状态机

distill_track:                        # 每节一个条目，key 为 section 名
  introduction:
    skill: distill-introduction-exemplar
    status: pending | distilled | verified   # verified = 该节写回已确认
    section_json: "sections/introduction.json"
    section_report: "sections/introduction.report.md"
    feedback: "feedback/introduction.feedback.yaml"
    identity:                         # 供 L2 一致性检查抽取（由主循环填充）
      gap_type: ""
      contribution_dimension: ""
    writeback:
      target: "write-introduction/corpus/<dir>/"
      gate: awaiting_confirm | confirmed | written
      items: []                       # 该节写回条目计数/概览
  theory:
    skill: distill-theory-exemplar
    status: pending | distilled | verified
    section_json: "sections/theory.json"      # 无 json 契约时改存 profile/report 路径
    section_report: "sections/theory.report.md"
    feedback: "feedback/theory.feedback.yaml"
    identity:
      theory_building_type: ""
    writeback:
      target: "write-theory/corpus/"
      gate: awaiting_confirm | confirmed | written
  methods:
    skill: distill-methods-exemplar
    status: pending | distilled | verified
    section_json: "sections/methods.json"
    feedback: "feedback/methods.feedback.yaml"
    identity:
      design_family: ""
    writeback:
      target: "write-methods/corpus/"
      gate: awaiting_confirm | confirmed | written
  results:
    skill: distill-results-exemplar
    status: pending | distilled | verified
    section_json: "sections/results.json"
    feedback: "feedback/results.feedback.yaml"
    identity:
      estimator_family: ""
    writeback:
      target: "write-results/corpus/"
      gate: awaiting_confirm | confirmed | written

cross_section_identity:               # L2 填充，单节模式标 unknown
  gap_type: ""
  theory_building_type: ""
  design_family: ""
  estimator_family: ""
  coherence: ok | flagged | partial
  flags:                              # 每项一条
    - check: ""
      observation: ""
      severity: info | warn
      source: "<节>"
      target: "<节>"

story_track:
  skill: distill-story-exemplar
  status: pending | card_drafted | card_confirmed | validated
  card_path: "story-blueprints/v4/blueprints/<...>.md"
  validated: false
  catalog_rebuilt: false
  fed_flags: false                     # L2 flag 是否已作为 assessment 参考输入

feedback_ledger:                       # L4 核验汇总（best-effort，见「已知摩擦」①）
  persisted: [<feedback 文件路径>...]   # 实际落盘的 feedback 文件
  missing: []                          # 未落盘的；每项须在 note 注明根因（能力缺口 vs 运行缺失）
  note: ""                             # missing 的根因说明，缺省留空
```

## 状态机

- 论文级 `status`：`manifest`（刚建骨架）→ `distilling`（任一节进行中）→ `integrated`
  （story 卡 validated，全链路完成）。
- 节级 `status`：`pending` → `distilled`（该节子任务完成）→ `verified`（写回 gate 已
  `confirmed` 且 corpus 写入完成）。
- 续跑规则：PDM 已存在时复用——`pending`/`distilled` 节重跑，`verified` 节跳过（除非用户
  显式要求重新蒸馏）。已 `written` 的写回不自动撤销。

## 示例（填充态，节选）

```yaml
pdm_version: 1.0
paper_id: "borah_tellis_2016"
status: distilling
source_provenance:
  fulltext_md: "D:/Onedrive/Obsidian Vault/文献笔记库/01 导入/论文导入/borah_tellis_2016.md"
  section_slices:
    introduction: "title...## Literature Review"
    methods: "## Data...## Estimation"
distill_track:
  introduction:
    status: verified
    section_json: "sections/introduction.json"
    feedback: "feedback/introduction.feedback.yaml"
    identity: {gap_type: Inadequacy, contribution_dimension: Method}
    writeback: {target: "write-introduction/corpus/tensions/", gate: written, items: 2}
  theory:
    status: distilled
    writeback: {gate: awaiting_confirm}
  methods:
    status: pending
  results:
    status: pending
cross_section_identity:
  coherence: partial
  flags:
    - check: gap->theory
      observation: "intro 为 Inadequacy（隐性假设错误），theory 构建类型尚待抽取"
      severity: info
story_track:
  status: pending
```

## 规则

- 一论文一 PDM；多轮蒸馏以最新为准，续跑而非重造。
- `.raw/` 与全文 MD 只读；PDM 及子文件是唯一写入物。
- `identity` 字段由主循环从各节输出抽取，不改动分节 skill 本体。
- flag 只标记不修正；跨节不一致本身是学习信号（可传给 story 卡 assessment）。

## 已知摩擦（2026-08-12 全链路走查实证）

PDM v1.0 在 ridgeetal2024（CEO Paranoia, AMJ 2024）全链路走查中暴露三个编排假设
与现实的偏差。这些是协议自身的修正方向，改协议前先与用户确认：

1. **feedback 产出能力不对称（best-effort 语义的由来）**。全 skills 目录仅
   `distill-introduction-exemplar` 与 `distill-theory-exemplar` 有
   `_update_design_feedback.py`；`distill-methods-exemplar` 与
   `distill-results-exemplar` **结构上无法**产出 `skill_design_feedback`。因此
   `feedback_ledger.missing` 须区分两类根因：**能力缺口**（该 skill 无基础设施，
   非编排违约）与**运行缺失**（有基础设施但本次未落盘，需查原因）。L4 核验
   best-effort：缺 skill 的 feedback 不能作为节状态回退的理由。
2. **PDM 脊柱强制力不足（已解决 2026-09-13）**。v1.0 假设四节 skill 会把
   `sections/<section>.json` 与 `feedback/<section>.feedback.yaml` 写入 PDM 目录；早期
   run 中分节 skill 自行写回 write-* 语料、未落 PDM 子文件。修正已落地：L1 分发契约
   （references/l1-subagent-protocol.md）强制子任务写 section 文件，缺失视为该节未完成、
   只重发该节；2026-09-13 Mao 2022 S5 整篇跑四节 JSON/feedback/plan 全部落盘，L2
   identity 合并与 L3 喂卡均走协议内建路径。
3. **identity 抽取时机**。`distill_track.*.identity` 应由主循环从 `sections/*.json`
   抽取；当子任务未落 section 文件时，只能从已写回 catalog/INDEX/feedback 反查
   （脆弱、非协议内建——2026-08-12 walkthrough 即走此回退路径）。**修正方向**：
   与 ② 同源，强制 section 文件落盘后 identity 抽取回到协议内建路径。

## v1.1 附录（2026-09-14）：pdm_tool 单写者与字段实践（问题 1+3 落地）

v1.0 正文保持原样作历史记录；本附录是现行契约。文件内 `pdm_version` 仍写 1.0，
不因本附录 bump。

### 单写者表（工具内置守卫，pdm_tool 硬拒 corpus/registry 写路径）

| 文件 | 唯一写者 |
|---|---|
| 根骨架（create-if-missing，现存根绝不触碰） | `preprocess_l0.py` |
| **根文件 L0 后一切变更** | **`scripts/pdm_tool.py`**（手写 `py - <<EOF` 改根 = 协议违约） |
| `sections/*.md`、`l0_manifest.json`、LOCK、slice_suggestions | `preprocess_l0.py` |
| `sections/<s>.json`、`feedback/*` | L1 子代理（根文件只读） |
| writeback plan | `corpus_precheck.py`（调用时显式 `--out writeback_plan.<s>.yaml`；其默认名 `<candidates>.plan.yaml` 与本文档命名分叉，以本文档为准，pdm_tool 发现策略另作兜底） |
| `write-*/corpus` + registry | `corpus_writeback.py` + `rebuild_apply.py`（A 项地盘，pdm_tool 不碰） |
| `~/.claude/fitness/**`（fitness 台账事件 + gate① 快照存档） | `fitness_ledger.py`（经 pdm_tool present/set-gate 调用；fail-open——遥测失败不阻塞状态机；目录在 distill-work 与仓库两树之外，`--clean/--sweep` 构造性免疫） |

### 命令 × 生命周期（L0 后根变更的唯一入口）

| 阶段 | 命令 |
|---|---|
| L1 每节子代理完成后 | `pdm_tool.py merge-section --pdm <root> --section <s> [--band …] [--set k=v]` |
| L1 plan 攒齐 | `set-gate --gate awaiting_confirm --plan <plan路径>`（登记路径+自动导出 items 计数） |
| L1 gate ① 呈审 | `present --mode gate1`（确定性生成呈审单；主循环不再读 plan 全文；同时自动存档快照+呈审单至 fitness 台账，`--stdout-only` 退出） |
| L1 用户确认后 / apply 后 | `set-gate --gate confirmed`（迁移时自动发射逐项接受事件至 fitness 台账；幂等重跑零事件） → `corpus_writeback --apply` → `set-gate --gate written`（auto-write 允许 awaiting_confirm→written 跳跃；written ⇒ 节 status=verified 级联） |
| L2 | `merge-cross --from <l2.yaml>`（flags 是 dict 列表，必须文件输入） |
| 节失败 | `fail-section --section <s> --reason …`（写节级 `error`，status 不动、不代宣布 verified） |
| L3 | `set-story --status … [--card-path …] [--validated] [--catalog-rebuilt] [--fed-flags]` |
| L4 | `set-paper --status integrated [--wb-citekey K] [--note …] [--ledger-note …]` → `verify_writeback` → **`present --mode audit`** → `--clean`（audit 必须在 clean 之前） |
| 续跑断点判定 | `show [--format json]` |

全局不变量：幂等（同参重跑 = no-op）；状态机只进不退（回退须 `--force` 且 `--note`
记录理由）；每次变更前滚动保留 `<root>.bak`；`set-paper --status integrated` 守卫 =
**status≠pending 的节**全 verified + cross_section_identity 已填（story pending 只告警
不阻塞）。

### 实践漂移字段的成文（v1.0 正文未列、实盘在用）

- 根级：`wb_citekey`（承重：执行器 `--paper` 键、wb 标记、registry join；唯一写入口
  `set-paper --wb-citekey`）、`wb_citekey_note`、`note`（如指纹不一致注记）、
  `source_provenance.structure_type`、`distiller_fingerprint`。
- 节级：`band`、`writeback.note`、`writeback.items`（**整数**——scaffold 曾产 `[]`，
  set-gate 写入时归一化）、`writeback.plan`（set-gate 登记，audit 的权威路径源）、
  `error`（fail-section）、`section_report`（merge-section 探测 `sections/<s>.report.md`
  自动记录）。
- `feedback_ledger.causes: {节: 根因}`：能力缺口 vs 运行缺失由 pdm_tool **运行时探测**
  `distill-<s>-exemplar/_update_design_feedback.py` 存在性判定（不硬编码，基建演进自动
  跟随），`note` 由 causes 自动合成，`set-paper --ledger-note` 可覆盖。
- **band 消歧**：节级 `band`（子代理 ≤20 行摘要的学习焦点信号，merge-section 写入）与
  plan 条目级 `band`（corpus_precheck 的机械选择门信号）是两个东西，勿混用。
- 路径基准两种历史形态并存：`distill_track.*` 裸相对（`sections/x.json`）、
  `source_provenance.*` 带 `<citekey>.pdm/` 前缀——pdm_tool resolver 双基准兼容，新
  写入沿用各字段既有惯例。

### identity 契约（merge-section 的提取序）

分发模板要求 section JSON **必须含顶层 `identity: {...}`**（2026-09-14 起成文；此前
该字段只活在 ≤20 行摘要里，从未进分节 skill 文档——契约链见 l1-subagent-protocol.md）。
必需键 = 脚手架真值：introduction={gap_type, contribution_dimension}、
theory={theory_building_type}、methods={design_family}、results={estimator_family}；
其余 identity.* 键（如 methods 的 estimator_family）可选捕获。提取失败时从摘要
`--set k=v` 补填是退路，不是默认。

### 复审裁定（2026-09-14 质量审查后成文）

1. **STALE 不阻塞**：呈审单的 STALE⚠ 是给人看的注记，不影响退出码——gate1 的
   exit 4 仅由 fail_fast 触发；audit 的 exit 4 由 verify FAIL 或 wb 标记 0（未落盘）
   触发。呈审单正是人看 STALE 的地方，机器不得代拦。
2. **换行归一化**：PDM 根磁盘历史混杂（scaffold `write_text` 产 CRLF，EOF 时代
   产物以 LF 为主）。pdm_tool 原子写统一落盘为 **LF**——触碰过的根即归一化；
   幂等判定在内存文本上进行，不受换行影响。
3. **`--from` 收缩**：自由文本经 argv 直传已实证可靠（CLI 冒烟：中文
   note/band/error 经 Git Bash→py→落盘无损）。`--from` 仅保留于 fail-section
   （长理由逃生门）与 merge-cross（结构性必需：flags 是 dict 列表，argv 装不下）；
   merge-section 曾声明但未实现的 `--from` 已摘除——CLI 表面不得有无效选项。
4. **error 生命周期**：`fail-section` 写节级 error、status 不动；`merge-section`
   成功即清除该节 error（重发成功 = 恢复）——否则 show 的续跑断点视图会永久
   挂着过期失败标记，误导"只重发未完成节"的判定。
