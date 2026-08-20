---
name: distill-paper-exemplar
description: "整篇顶刊论文蒸馏编排入口——按 PDM 协议把完整论文分解为 Intro/Theory/Methods/Results 四节并行蒸馏、跨节一致性检查、生成 story blueprint 学习卡，最终写回 write-* 语料。触发词：整篇蒸馏、蒸馏这篇论文、整篇输入消费。单节蒸馏走对应 distill-*-exemplar。"
whenToUse: "当用户给出一篇完整论文（PDF/MD/路径）要求整篇学习、整篇消化时使用。触发词：整篇蒸馏、蒸馏这篇论文、整篇输入消费、把这篇论文整个消化一遍、全文蒸馏、整体学习这篇顶刊论文、这篇论文全篇蒸馏"
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
                 → scripts/preprocess_l0.py（确定性，无 LLM）：剥 base64 图
                   （paper-import MD 的 44–89% 字节是 data:image 单行巨串，
                   直读全文会炸上下文）→ <citekey>.pdm/fulltext.text-only.md
                   + 物化切片 sections/<section>.md → 创建 PDM（status: manifest）
L1 分节蒸馏 ×4    并行分发 distill-introduction/theory/methods/results-exemplar
   （复用，零改动） 输入 = PDM 切片文件（非全文）；每节 → section JSON/报告 + feedback
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
   则直接用。**随后必跑** `python scripts/preprocess_l0.py <全文MD>`（确定性脚本，不经 LLM）：
   剥除 base64 图片（→ `![fig-N](image-ref-N)` 占位符）生成 `<citekey>.pdm/fulltext.text-only.md`，
   并按标题物化切片 `sections/introduction|theory|methods|results|discussion.md`；
   检测不到的节在 l0_manifest.json 标 `unknown`，由主循环人工切分补齐，不阻塞。
   登记 frontmatter/citekey（Zotero 为元数据源）。创建 PDM 骨架，把 manifest 的
   切片路径写入 `source_provenance.section_slices`。
2. **L1 分节蒸馏分发**。按用户范围（默认 4 节全跑）并行分发：
   `/distill-introduction-exemplar <切片> --output-format=json` → `sections/introduction.json`
   （theory/methods/results 同理）。每个子任务完成后：子任务写自己的 section 文件与
   feedback 文件 → 主循环合并进 PDM → 更新该节 `status`。
   **不得代答或代确认各分节 skill 的写回预览**（gate ① 归各 skill 自己）。
3. **L2 跨节一致性检查**。四节 identity（gap_type / theory_building_type / design_family /
   estimator_family）就位后执行 rubric（见 references/cross-section-coherence.md）。
   输出 `cross_section_identity` 块。仅标记，不自动修正；flag 汇总呈现给用户。
   若用户只蒸馏单节，fill 已知、标 `unknown`，不阻塞。
4. **L3 整篇整合**。用户确认 L2 结果后，分发 `distill-story-exemplar`，输入 = **text-only 全文**
   （`<citekey>.pdm/fulltext.text-only.md`，非原始 MD）+ PDM 中 `verified` 分节蒸馏。产出 blueprint 卡后**不代确认**（gate ② 归 story skill），
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
- 用户侧标准提示词模板（WHAT 槽位 + 纪律清单，反模式）见 `references/launch-prompt-template.md`；
  提示词只填 动作/来源/焦点/约束，HOW 全部由本协议继承，不在提示词里重述流程。

## 完成判据

① PDM 就位且四节（或指定范围）状态为 `verified`（或明确 `partial`）；② 每节写回预览均已
经过该节 skill 自己的确认门禁并记录于 PDM `writeback.gate`；③ `cross_section_identity`
已填充（单节模式标注 `unknown`）；④ story 卡已确认并 validate/build 通过，`story_track`
已更新；⑤ design_feedback 已核验持久化（best-effort：缺产出能力的 skill 在 feedback_ledger.note 注明根因，不阻塞 integrated）；⑥ 向用户报告三路输出落点与任何 flag。

## 已知摩擦与边界

- ~~intro/theory 的 SKILL.md 含重复块~~（2026-08-20 已修：三个重复块各删一份；T6 输出块与
  Phase 1.5 t6_closure_quality 的内部重复已合并）。
- theory 无 `--output-format=json` 契约——其 section 条目以 yaml profile/报告路径承接。
- 全自动不可行且不追求：gate ①/② 是人审闸，属防抄写纪律。
- 同一篇论文被多次蒸馏时，以新 PDM 为准；若已有旧 PDM，续跑而非重造（见 schema 状态机）。
- feedback 产出能力不对称（2/4）：见 `references/pdm-schema.md` 已知摩擦①；L4 为
  best-effort，missing 须区分能力缺口与运行缺失。

## Context discipline

不预读四个分节 skill 的语料；按 `references/pdm-schema.md` 维护 PDM，按需打开
`references/cross-section-coherence.md`。**原始全文 MD（含 base64 图片）禁止读入上下文**——
所有阅读只经 `<citekey>.pdm/fulltext.text-only.md` 与 `sections/*.md` 切片；原始 MD 只读存档，
PDM 是唯一写入交接物。
