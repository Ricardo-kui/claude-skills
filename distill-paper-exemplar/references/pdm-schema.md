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
      target: "write-introduction/academic-writing-corpus/<dir>/"
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
      target: "write-methods/econometric-models/"
      gate: awaiting_confirm | confirmed | written
  results:
    skill: distill-results-exemplar
    status: pending | distilled | verified
    section_json: "sections/results.json"
    feedback: "feedback/results.feedback.yaml"
    identity:
      estimator_family: ""
    writeback:
      target: "write-results/econometric-models/"
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
    writeback: {target: "write-introduction/academic-writing-corpus/tensions/", gate: written, items: 2}
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
2. **PDM 脊柱强制力不足**。v1.0 假设四节 skill 会把 `sections/<section>.json` 与
   `feedback/<section>.feedback.yaml` 写入 PDM 目录；实际 run 中分节 skill 自行写回
   write-* 语料、未落 PDM 子文件，主循环因此无法在 L2 合并 identity、L3 无法把
   L2 flags 喂给 story 卡（`story_track.fed_flags` 落 false）。**修正方向**：L1 分发
   时强制子任务写 section 文件（无 JSON 契约的 theory 写 yaml profile），缺失即视为
   该节未完成，L2 不启动。
3. **identity 抽取时机**。`distill_track.*.identity` 应由主循环从 `sections/*.json`
   抽取；当子任务未落 section 文件时，只能从已写回 catalog/INDEX/feedback 反查
   （脆弱、非协议内建——2026-08-12 walkthrough 即走此回退路径）。**修正方向**：
   与 ② 同源，强制 section 文件落盘后 identity 抽取回到协议内建路径。
