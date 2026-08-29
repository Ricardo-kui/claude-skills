# 蒸馏启动提示词模板 — v1.0

用户继续用整篇输入消费丰富 skills 时的标准提示词指南。**提示词管 WHAT（蒸馏哪篇、学什么），
skill 管 HOW（L0-L4、PDM、gate、写回）**。提示词只填 4 个槽位：动作 / 来源 / 焦点 / 约束，
其余流程决策全部由 `distill-paper-exemplar` 协议继承，不在提示词里重述。

## 核心原则

- 提示词标准化 = 让"整篇输入消费"走 PDM 定式，不现场发明流程。
- 一旦在提示词里描述 HOW（切分、并行、一致性、归拢……），就会与协议漂移——协议一改，
  所有旧提示词全部过期。正确姿势：只给路径和焦点。
- 人审门禁（gate ① 写回预览 / gate ② blueprint 卡确认）是内建纪律，不由提示词控制。

## 路由决策表：先选入口，再写提示词

| 目标 | 入口 | 提示词形态 |
|---|---|---|
| 整篇蒸馏（默认；学 HOW + 写回全部语料） | `/distill-paper-exemplar` | 路径 + 可选焦点 |
| 只学某节 HOW（Intro/Theory/Methods/Results） | `/distill-<节>-exemplar` | 切片路径 + 该节目标 |
| 学整篇叙事（story 卡） | `/distill-story-exemplar` | 全文路径 |
| 批量多篇 | `/distill-paper-exemplar` 逐篇 | 目录 + 清单 + `--dry-run` |

## 模板 A — 整篇蒸馏（默认推荐）

```
蒸馏这篇论文来丰富 write-* 语料和 story-blueprints：
路径：<粘贴 .md 绝对路径>
学习焦点（可省略，缺省整篇）：<学哪 1-2 个 HOW，写给哪层语料>
约束（可省略，缺省继承协议）：<如：不动 write-theory/SKILL.md 硬约束>
```

## 模板 B — 单节定向

```
蒸馏这篇论文的 <Introduction|Theory|Methods|Results> 部分（单节）：
切片路径：<粘贴切片，或给全文 MD + 节名>
目标：<如：学它 Incompleteness gap 的铺陈逻辑，反馈给 write-introduction>
```

## 模板 C — 批量

```
批量蒸馏以下论文（整篇输入消费）：
目录：<论文目录>
清单：<列出 2-5 篇文件名>
约束：每篇先 --dry-run 出分发计划，我确认后再跑
```

## 模板 D — 查漏补缺重蒸馏（2026-08-29 起）

同一篇论文已有旧蒸馏痕迹（story 卡、语料条目），要补齐遗漏而非重造：

```
重新蒸馏这篇论文，对之前的蒸馏查漏补缺，优化 write-* 语料和 story 卡：
路径：<粘贴 .md 绝对路径>
既有蒸馏痕迹（可省略，主循环自动盘点）：<story 卡路径 / 已知语料条目>
约束（可省略）：已授权按 precheck plan 直写、事后呈审计报告（协议缺省）
```

## 纪律清单（继承到所有提示词，不写进提示词本身）

1. **提炼 HOW not WHAT**——学"怎么论证"，不抄"说了什么"（防抄写纪律；gate ①/② 人审不绕过）。
2. **SKILL.md 硬约束（#N 规则）改动必须先人审**——C11 教训：随蒸馏 commit 溜入未确认的
   carve-out。
3. **强制落 `sections/<section>.json`**——PDM 脊柱依赖它，缺失则 L2/L3 无法协调
   （见 `pdm-schema.md` 已知摩擦②）。无 JSON 契约的节写 yaml profile。
4. **feedback 是 best-effort**——仅 intro/theory 蒸馏 skill 有 `_update_design_feedback.py`；
   methods/results 缺基础设施，`feedback_ledger.missing` 注明根因，不阻塞 integrated
   （已知摩擦①）。
5. **新 skill 目录须加 `.gitignore` 白名单**（`!<dir>/` + `!<dir>/**`）——否则 git status
   假 clean，文件永远不会提交。
6. **`.raw/` 与全文 MD 只读**；PDM 及子文件是唯一写入物。
7. **子代理模型**：`CLAUDE_CODE_SUBAGENT_MODEL` 须为 `deepseek-v4-flash`（改完需重启会话
   生效；设错则所有 Agent 子任务 400）。
8. **子代理写回纪律（2026-08-29 固化）**：plan 条目必须执行器 v2 schema
   （`items:` + block_text 全文内嵌 + index_note），子代理**禁止运行
   `corpus_writeback.py`**——写回权收归主循环，残项同步 pass 同样禁止
   （防"手补代理重跑写回 → 重复插入"事故复发）。
9. **写回终验强制（2026-08-29 固化）**：全部子代理退出后跑
   `scripts/verify_writeback.py`（块正文唯一性 / registry 无双计 / YAML / INDEX 残项
   → `writeback_residuals.yaml`），FAIL 未处理不得进入 story 卡与清理。

## 反模式

- ✗ `"请先切分 Intro/Theory/Methods/Results，再并行分发 4 个 skill，然后做跨节一致性
  检查，最后归拢反馈……"` —— 在提示词里重述协议，协议一改全过期。
- ✗ 不给路径只说"帮我分析这篇论文" —— 无 provenance 锚点，Agent 只能现场 improvis。
- ✗ 让提示词承担 gate 职责（"写回前一定给我看"）—— gate 是 skill 内建门禁，重复声明
  反而制造两条不一致的纪律源。

## 一个填好的示例

```
蒸馏这篇论文来丰富 write-* 语料和 story-blueprints：
路径：D:/Onedrive/Obsidian Vault/文献笔记库/01 导入/论文导入/Ridge-2025-Avoidance and
      Aggression in Stakeho-OvisOCR2-20260810-173132.md
学习焦点：学它 H2 主效应 null 但调节显著的"条件兑现"表达，反馈给 write-results；
          学它的 CEO 特质构念引入，反馈给 write-theory
约束：不动 write-theory/SKILL.md 硬约束
```
