---
name: distill-paper-exemplar
description: "整篇顶刊论文蒸馏编排入口——把完整论文按 PDM 协议分发到四个分节 distill skill 并行蒸馏，跨节一致性检查后收敛为 write-* 语料更新 + story-blueprints 卡 + 反馈台账。"
when_to_use: "用户给一篇完整论文要求整篇蒸馏/整篇学习时；单节蒸馏去对应 distill-*-exemplar。"
whenToUse: "Use when 用户给出一篇完整论文要求整篇蒸馏学习，需要按 PDM 协议分解为四个分节并行蒸馏、做跨节一致性检查并生成整篇 story blueprint。Trigger words: 整篇蒸馏, 蒸馏这篇论文, 整篇输入消费, 全文蒸馏学习, distill whole paper"
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
L1 分节蒸馏 ×4    2+2 波次并行分发（intro+theory → methods+results；2026-08-29 起；
   （复用，零改动） --serial 回退串行；4 个全并行禁止：2026-08 实测触发限流，整批作废
                 重发，重试开销 30–40%）；子代理契约 references/l1-subagent-protocol.md；
                 主循环只收 ≤20 行摘要
                 输入 = PDM 切片文件（非全文）；每节 → section JSON/报告 + feedback
                 → corpus_precheck.py 产出 writeback plan（选带/查重/锚点，确定性；
                   2026-08-29 起 fail-fast：缺 block_text、candidates:/items: schema
                   写反、锚点文件不可解析 → exit 4 当场令子代理返工，不进 gate ①；
                   手写/修复后的 plan 先 `--check-plan` 校验再执行）
                 → 各节 plan 攒齐后**一次性批量呈审**（gate ① 按论文不按节，
                   2026-08-20 起；--auto-write / 查漏补缺重蒸馏时跳过呈审按 plan 直写）
                 → corpus_writeback.py 执行确认后的 plan（幂等：溯源标记+同体检测，
                   重跑不重复；dry-run diff→--apply；自动续变体编号、更新
                   _index/registry、SKIP 拒写；create_new_file 条目自动生成
                   canonical 模块脚手架+新 _index 行——字段契约见
                   l1-subagent-protocol.md，2026-08-29 v2）
                 → verify_writeback.py 终验（块唯一性/registry 无双计/残项工作单）
                 → write-* corpus
L2 跨节一致性      由本 skill 执行（读 references/cross-section-coherence.md）
   （本层新建）    从 PDM 四节 identity 交叉校验 → ok | flagged，只标记不擅改
L3 整篇整合        distill-story-exemplar ← 全文 + PDM 已验证分节蒸馏
   （复用）        → blueprint v0.4-lite 卡 → 卡确认门禁（gate ②）→ validate + build_catalog
                   （2026-08-29 v2：verify PASS 后，残项同步 pass 与 story 卡
                   **并行分发**——前者只动 write-* registry/INDEX，后者只动
                   story-blueprints，文件零重叠，实测安全）
L4 反馈收敛        核对 design_feedback 已持久化；报告三路输出落点
                   → --clean（本篇工作目录）→ --sweep（跨篇：__pycache__、
                     已消费工作目录；保留状态记录/句子库存/在跑现场）
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
   **切片兜底（2026-08-29 起）**：检测为空或可疑（任一切片 <300 词、标题层级断裂）时，
   脚本自动打印全标题树（行号+自动判定节）并写 `slice_suggestions.yaml`；主循环一次
   确认起止行后用 `--slices <该文件>` 重跑即完成补切，不再逐节 sed 手切。
   **结构自适应（2026-08-20 起）**：先读 manifest 的 `structure_type`——
   `extended-intro`（长引言内嵌理论/假设，直接进 Data，经济学/金融风格）时，theory
   蒸馏路由到 `sections/introduction.md`（标注 `embedded: true`，由 intro 蒸馏按功能
   映射模块），**不再要求人工补切 theory**；`formal-model`（"Theoretical Model" 节）
   时 theory 蒸馏按模型类内容处理，不套假设发展模板；`classic-imrad` 为默认。
   登记 frontmatter/citekey（Zotero 为元数据源）。创建 PDM 骨架，把 manifest 的
   切片路径写入 `source_provenance.section_slices`。
   **工作目录纪律（2026-08-20 用户裁决）**：PDM 工作目录默认在
   `~/.claude/distill-work/<citekey>.pdm/`（`DISTILL_WORK_ROOT` 可改）——**Vault/OneDrive
   之外**，不向论文目录生成中间文件；全部产物可从源 MD 确定性重建，可随意删。
   仅当需要随论文留档时才用 `--outdir` 显式放到论文旁。
   **零留痕（用户裁决）**：feedback/sections/slices/plan 等中间产物对用户无价值，
   不得落论文目录或任何长期位置；L4 `--clean` 是强制收尾，不是可选。
   **句子库存例外（2026-08-24 起，P1a）**：`preprocess_l0.py <MD> --keep-sentences`
   把各节切片抽取成 `story-blueprints/v4/rhetoric-moves/sources/<citekey>.sentences.md`
   （逐句一行 + `<!-- para N -->` 段落溯源，`--clean` **不删**它）。这是跨源合成的
   原料池，不是中间产物；当用户目标含叙事/语言学习（而非仅结构）时主循环应默认加
   此 flag，L4 不清理该归档。
2. **L1 分节蒸馏分发（子代理）**。按用户范围（默认 4 节全跑）以 **2+2 波次并行**分发
   （第一波 intro+theory，完成后再发 methods+results；2026-08-29 起，实测零限流；
   `--serial` 回退串行，4 个全并行仍禁止）。分发机制与提示词模板见
   `references/l1-subagent-protocol.md`：Claude Code 用 `Task` 工具（general-purpose），
   Codex/Kimi Code 用各节 `agents/openai.yaml` 子代理，Cursor/Zcode 按其子代理机制。
   每个子代理完成后：写自己的 section 文件与 feedback 文件 → 回传 ≤20 行摘要 →
   主循环把 identity/band 合并进 PDM → 更新该节 `status`。**主循环不打开 phase 参考
   文件、语料索引或切片**（这些只在子代理上下文里读，约省 60% 主上下文 fresh input）。
   **gate ① 按论文批量呈审（2026-08-20 起）**：整篇模式下各节子任务跑到 writeback
   plan 产出即暂停写回；四节（或指定范围）plan 攒齐后，由主循环汇总为一份批量呈审
   （每节：verdict 摘要 + anchor_candidates top-3 + 拟写回文件），用户一次确认全部，
   主循环再逐节调 `corpus_writeback.py` 执行。单节蒸馏不受此限，仍随产随审。
   主循环**只汇总呈审，不代用户确认**；`--auto-write` 时跳过呈审逐节直写。
   **查漏补缺重蒸馏默认 `--auto-write`（2026-08-29 起）**：同一论文已有旧蒸馏痕迹
   （story 卡/语料条目）的重跑，若用户请求本身已授权写回（如"优化 corpus"），主循环
   按 auto-write 语义直写（查重由 corpus_precheck 确定性完成，SKIP 项永不写回），
   但必须 (a) 写回后、全部子代理退出后立即跑 `verify_writeback.py` 终验，(b) L4 呈报
   事后审计报告（各节变体清单 + verify 结果 + 残项），用户保留否决权。首次蒸馏仍走
   批量呈审，不适用本默认。
3. **L2 跨节一致性检查**。四节 identity（gap_type / theory_building_type / design_family /
   estimator_family）就位后执行 rubric（见 references/cross-section-coherence.md）。
   输出 `cross_section_identity` 块。仅标记，不自动修正；flag 汇总呈现给用户。
   若用户只蒸馏单节，fill 已知、标 `unknown`，不阻塞。
4. **L3 整篇整合**。用户确认 L2 结果后，分发 `distill-story-exemplar`，输入 = **PDM 切片**
   （intro/theory 优先，路径见 PDM `source_provenance.section_slices`；切片缺失/`unknown` 时回退
   `fulltext.text-only.md`，非原始 MD）+ PDM 中 `verified` 分节蒸馏。产出 blueprint 卡后**不代确认**（gate ② 归 story skill），
   确认后运行其内建 `validate_blueprints_v4.py` + `build_catalog_v4.py`。将 L2 flag 作为
   卡 assessment 的参考输入（论文内部不一致本身是可学习的信号）。
5. **L4 反馈归拢（best-effort）**。核对 `skill_design_feedback` 已持久化——仅
   intro/theory 两个 distill skill 内建 `_update_design_feedback.py`，methods/results
   无该基础设施（能力缺口），missing 不视为违约，须在 `feedback_ledger.note` 注明
   根因（能力缺口 vs 运行缺失，见 references/pdm-schema.md 已知摩擦①）；汇总三路输出落点。
   **写回终验（2026-08-29 起，强制）**：在全部子代理退出之后、清理之前，运行
   `scripts/verify_writeback.py --plan <各节 plan> --paper <citekey>`——逐项校验块正文
   唯一性（重复插入=FAIL）、registry 无双计（FAIL）、YAML 可解析，并把 registry/INDEX
   残项写成 `writeback_residuals.yaml` 工作单交由单个同步 pass 消费（该 pass 不得运行
   corpus_writeback.py）。写回器本身已幂等（块尾 `<!-- wb:<paper>:<item> -->` 溯源标记 +
   同体检测），同一 plan 误跑两次 --apply 不再产生重复。
   完成后运行 `preprocess_l0.py <MD> --clean` 清除整个工作目录（默认位置在 Vault 外，
   删除零成本）；中断续跑则保留现场；`--unlock` 仅放锁不删文件。
   **跨篇清扫（2026-08-29 v2，--clean 之后的最后一步）**：运行
   `preprocess_l0.py --sweep`——清除 skill 树全部 `__pycache__`/`*.pyc` 与已消费的
   PDM 工作目录（根 yaml `status: integrated` 者及 >12h 的 orphan），保持 skill
   树零字节码膨胀。**绝不触碰**：`<citekey>.pdm.yaml` 状态记录、句子库存归档、
   story-blueprints、LOCK <12h 的在跑工作目录。

## 调用方式

```
/distill-paper-exemplar <论文路径|PDF|MD|目录> [--sections=intro,theory,methods,results]
                       [--pdm=<path>] [--dry-run] [--serial] [--auto-write]
```

- `--sections` 默认四节全跑；可缩范围。
- `--pdm` 指定 PDM 文件位置；缺省 = `~/.claude/distill-work/<citekey>.pdm.yaml`（Vault 之外）。
- `--dry-run`：只产出 PDM 骨架 + 分发清单，不实际分发（用于预览计划）。
- `--serial`：L1 退回全串行分发（缺省 2+2 波次并行：intro+theory → methods+results，
  见 L1 注释；4 个全并行已禁止——实测触发账户限流）。
- `--auto-write`：预先授权各分节 skill 按 corpus_precheck 的 writeback plan 直接写回
  ADD/EXTEND 项（SKIP 项永不写回），跳过 gate ① 的逐条确认；缺省仍需人审。
  查漏补缺类重蒸馏（同论文已有旧蒸馏痕迹且用户请求已授权写回）缺省即按本语义执行，
  事后呈审计报告。
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
- **单窗口纪律（2026-08-20 起）**：同一 PDM 同一时间只在一个 Claude Code 会话跑——
  L0 脚本会创建 `<citekey>.pdm/LOCK`（12h 内拒绝二次启动，陈旧锁用 `--force`，
  完成后 `--unlock`）。2026-08 实测双窗口把 L1–L3 整链路跑两遍，是单次运行最大浪费源。

## Context discipline

不预读四个分节 skill 的语料；按 `references/pdm-schema.md` 维护 PDM，按需打开
`references/cross-section-coherence.md`。L1 分发到子代理后，**主循环只读 PDM 与各节
≤20 行摘要**——phase 参考文件、语料索引、切片一律只在子代理上下文里读（见
`references/l1-subagent-protocol.md` 主循环纪律）。**原始全文 MD（含 base64 图片）禁止读入
上下文**——所有阅读只经 `<citekey>.pdm/fulltext.text-only.md` 与 `sections/*.md` 切片；
原始 MD 只读存档，PDM 是唯一写入交接物。
