# L1 子代理分发协议（2026-08-22 起）

L1 的四个分节蒸馏在**子代理**里跑，主循环只收紧凑摘要。分节 skill 的 phase 参考
文件（7–24KB/个 × 5–7 个）、语料索引与切片只进子代理上下文；主上下文只背 SKILL.md +
PDM + 各节摘要，实测可降主上下文 fresh input 约 60%（此前四节全部载荷累积在同一窗口，
cache_read 是 fresh input 的 3.5 倍）。

## 子代理提示词模板

```
<skill 名> <切片路径> --output-format=json --pdm <pdm路径>
按该 skill 的 phase 流程蒸馏。输出契约：
1. 把 section JSON 写入 <pdm>/sections/<section>.json，feedback 写入
   <pdm>/feedback/<section>.feedback.yaml（skill 无该基础设施时注明缺失）
2. 写回候选停在 writeback plan 产出（gate ① 由主循环批量呈审）
3. 最终回复只允许 ≤20 行紧凑摘要：
   - identity: gap_type / theory_building_type / design_family / estimator_family
   - band: gap|薄弱|quiet + 一句依据
   - writeback_candidates: 每个候选一行（action + target + 变体名）
   - feedback_path / section_json_path
   - 任何 flag
不得把 phase 报告全文、DNA profile 或语料文件内容贴进回复。
```

各工具的子代理机制：

| 工具 | 分发机制 |
|---|---|
| Claude Code | `Task` 工具（subagent_type: general-purpose），prompt 用上方模板 |
| Codex / Kimi Code | 各节 `agents/openai.yaml` 定义的子代理（default_prompt 已含 PDM 输出契约） |
| Cursor / Zcode | 按其各自的子代理/task 机制，prompt 用上方模板 |

## 主循环纪律

- 主循环**只读**：PDM 根文件、各节 `sections/<section>.json`、子代理的 ≤20 行摘要。
- 读 `sections/<section>.json` 时校验 `identity` 字段非空；空或缺文件 → 该节视为未完成，只重发该节（不整链路重跑）。
- 主循环**不得打开**：任何分节 skill 的 references/、protocols/、语料索引
  （_index / INDEX / _evidence_registry / routing 表）、论文切片——这些只在子代理里读。
- 合并：每节完成后主循环把摘要中的 identity/band 写入 PDM 该节条目、更新 `status`；
  JSON 文件由子代理写入，主循环不代写。
- 中断续跑：以 PDM 各节 `status` 为断点，只重发未完成节，不整链路重跑。

## 节奏与限流

- 默认**串行**（一次 1 个子代理）。2026-08 实测并行 4 agent 触发限流→整批作废重发，
  重试开销 30–40%；`--parallel` 显式开启并行，限流风险自负。
- 子代理内仍按分节 skill 自己的 phase 纪律按需加载参考文件（不预读全部 phase）。
