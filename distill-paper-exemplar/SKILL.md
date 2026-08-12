---
name: distill-paper-exemplar
description: >-
  整篇顶刊论文蒸馏编排入口——输入完整论文（PDF/MD/路径），按 PDM（Paper Distillation
  Manifest）协议将整篇分解为 Introduction/Theory/Methods/Results 四节，分发到对应
  distill-*-exemplar skill 并行蒸馏，执行跨节一致性检查，再交由 distill-story-exemplar
  生成整篇 story blueprint 学习卡；最终收敛为三路输出：write-* 语料更新 +
  story-blueprints 卡 + skill_design_feedback 台账。这是「整篇输入消费」的定式化编排层，
  四个分节 distill skill 本体零改动。Use when 用户给出一篇完整论文要求整篇蒸馏学习 /
  整篇输入消费 / 蒸馏这篇论文（全篇）。Not for: 单节蒸馏（→ 对应 distill-*-exemplar）；
  单节草稿审查（→ intro-review / theory-review / methods-review / results-review）；
  全稿 QC（→ pollock-qc）；写自己的论文（→ write-*）。
---

# Distill Paper Exemplar — 整篇蒸馏编排协议

把一篇完整顶刊论文从 PDF/MD 一路消化为三类学习资产：**write-* 分节语料**（槽位级辅导）、
**story-blueprints 学习卡**（叙事级辅导）、**skill_design_feedback 台账**（skill 自改进）。
本 skill 不做任何蒸馏，只做分解、分发、校验、归拢——蒸馏能力全部复用既有 5 个 skill。

## 目标与边界

- **目标**：让"整篇输入"成为定式——同一篇论文的 4 个分节 profile 与 1 张整篇卡产生于同一
  数据包（PDM），可复核、可续跑、可机器消费。
- **非目标**：不重写蒸馏逻辑；不改动四个 `distill-*-exemplar` skill 本体；不做全自动写回
  （人审闸由各分节 skill 与 story skill 自己执行，本 skill 不得绕过）。
- **人审是特性**：L1 写回预览确认、L3 blueprint 卡确认是既有 skill 的内建门禁。本协议只是
  编排它们，不替代它们。

## 整篇消费模型（L0–L4）

```
L0 获取与分解     paper-import(OvisOCR2/MinerU) → 全文 MD
                 → 切片 4 段 + frontmatter/citekey → 创建 PDM（status: manifest）
L1 分节蒸馏 ×4    并行分发 distill-introduction/theory/methods/results-exemplar
   （复用，零改动） 每节 → section JSON/报告 + skill_design_feedback
                 → 该节自己的写回预览门禁（gate ①，不绕过）→ write-* corpus
L2 跨节一致性      由本 skill 执行（读 references/cross-section-coherence.md）
   （本层新建）    从 PDM 四节 identity 交叉校验 → ok | flagged，只标记不擅改
L3 整篇整合        distill-story-exemplar ← 全文 + PDM 已验证分节蒸馏
   （复用）        → blueprint v0.4-lite 卡 → 卡确认门禁（gate ②）→ validate + build_catalog
L4 反馈收敛        核对 design_feedback 已持久化；报告三路输出落点
```

## 数据契约：PDM（Paper Distillation Manifest）

每篇论文一份 PDM，是本协议唯一的跨层交接物。schema、状态机与文件布局见
`references/pdm-schema.md`。要点：

- **每节一个子文件**（`sections/<section>.json` / `feedback/<section>.feedback.yaml`），
  并行分发时由各子任务写入；**PDM 根文件只由本 skill（主循环）合并更新**——避免并发写同一 YAML。
- **写回状态独立记录**（`gate: awaiting_confirm | confirmed | written`），供续跑时定位断点。
- 分节 skill 已内建的 JSON 输出尽量启用（`--output-format=json`）；theory 无 JSON 契约时，
  存其 yaml profile 或报告路径，identity 字段由本 skill 从报告抽取。

## 工作流

1. **L0 获取与分解**。PDF → `paper-import`（80 页内 OvisOCR2，超长/图书 MinerU）；已是 MD
   则直接用。切分 Intro/Theory/Methods/Results（+Discussion 归 results 或单列）。登记
   frontmatter/citekey（Zotero 为元数据源）。创建 PDM 骨架。
2. **L1 分节蒸馏分发**。按用户范围（默认 4 节全跑）并行分发：
   `/distill-introduction-exemplar <切片> --output-format=json` → `sections/introduction.json`
   （theory/methods/results 同理）。每个子任务完成后：子任务写自己的 section 文件与
   feedback 文件 → 主循环合并进 PDM → 更新该节 `status`。
   **不得代答或代确认各分节 skill 的写回预览**（gate ① 归各 skill 自己）。
3. **L2 跨节一致性检查**。四节 identity（gap_type / theory_building_type / design_family /
   estimator_family）就位后执行 rubric（见 references/cross-section-coherence.md）。
   输出 `cross_section_identity` 块。仅标记，不自动修正；flag 汇总呈现给用户。
   若用户只蒸馏单节，fill 已知、标 `unknown`，不阻塞。
4. **L3 整篇整合**。用户确认 L2 结果后，分发 `distill-story-exemplar`，输入 = 全文 +
   PDM 中 `verified` 分节蒸馏。产出 blueprint 卡后**不代确认**（gate ② 归 story skill），
   确认后运行其内建 `validate_blueprints_v4.py` + `build_catalog_v4.py`。将 L2 flag 作为
   卡 assessment 的参考输入（论文内部不一致本身是可学习的信号）。
5. **L4 反馈归拢（best-effort）**。核对 `skill_design_feedback` 已持久化——仅
   intro/theory 两个 distill skill 内建 `_update_design_feedback.py`，methods/results
   无该基础设施（能力缺口），missing 不视为违约，须在 `feedback_ledger.note` 注明
   根因（能力缺口 vs 运行缺失，见 references/pdm-schema.md 已知摩擦①）；汇总三路输出落点。

## 调用方式

```
/distill-paper-exemplar <论文路径|PDF|MD|目录> [--sections=intro,theory,methods,results]
                       [--pdm=<path>] [--dry-run]
```

- `--sections` 默认四节全跑；可缩范围。
- `--pdm` 指定 PDM 文件位置；缺省 = `<论文 MD 同目录>/<citekey>.pdm.yaml`。
- `--dry-run`：只产出 PDM 骨架 + 分发清单，不实际分发（用于预览计划）。
- 单节请求应路由回对应 `distill-*-exemplar`，不进入本 skill。

## 完成判据

① PDM 就位且四节（或指定范围）状态为 `verified`（或明确 `partial`）；② 每节写回预览均已
经过该节 skill 自己的确认门禁并记录于 PDM `writeback.gate`；③ `cross_section_identity`
已填充（单节模式标注 `unknown`）；④ story 卡已确认并 validate/build 通过，`story_track`
已更新；⑤ design_feedback 已核验持久化（best-effort：缺产出能力的 skill 在 feedback_ledger.note 注明根因，不阻塞 integrated）；⑥ 向用户报告三路输出落点与任何 flag。

## 已知摩擦与边界

- intro/theory 的 SKILL.md 尚未同步 v1.9.0 重构且含重复块（完成判据/选材Gate/原文锚定各
  出现两次）——编排时以其 references/ 与协议字段为准，不依赖 SKILL.md 排版。
- theory 无 `--output-format=json` 契约——其 section 条目以 yaml profile/报告路径承接。
- 全自动不可行且不追求：gate ①/② 是人审闸，属防抄写纪律。
- 同一篇论文被多次蒸馏时，以新 PDM 为准；若已有旧 PDM，续跑而非重造（见 schema 状态机）。
- feedback 产出能力不对称（2/4）：见 `references/pdm-schema.md` 已知摩擦①；L4 为
  best-effort，missing 须区分能力缺口与运行缺失。

## Context discipline

不预读四个分节 skill 的语料；按 `references/pdm-schema.md` 维护 PDM，按需打开
`references/cross-section-coherence.md`。全文 MD 只读，PDM 是唯一写入交接物。
