# Model Lineup Protocol — 跨模型对抗阵容协议 v1.1

`toc-review` 与 `tod-debate` 共用的模型阵容协议：把"多 agent 对抗"升级为"多模型对抗"时，如何发现模型、选家族、派槽位、处理失败与降级、并在报告中留痕。两个 skill 的 SKILL.md 引用本协议，本协议不重复其辩论逻辑。

## 0. 证据地位（三分声明，不得混同）

- **(a) 文献已确立**：多智能体辩论（MAD，arXiv:2305.14325, MIT/DeepMind）的对抗审阅机制可提升事实性与推理精度；ToC（Mishra et al. 2026）与 ToD（Kargupta et al. 2025）的原架构均以**同模型多实例**实现专门化分工。
- **(b) 本协议正在连接**：跨模型（cross-family）升级——不同厂商家族的预训练语料与对齐偏好不同，同家族多实例存在共享盲区（groupthink）；跨家族辩论去相关化这一主张来自 MAD 工程实践（2026-09 综述文章《跨模型辩论，大力出奇迹！》及随后端实现）。
- **(c) 未经检验**：跨模型相对同模型多实例在本 skill 任务（管理学弱点提取 / 新颖性对辩）上的**增量收益未在本 skill 基准上验证**。因此：阵容必须透明留痕、降级必须显式标注、输出定位不变（人工筛选的候选清单，作者终审）。

## 1. 家族目录（family = 厂商谱系，不是 pi provider）

本表是**候选偏好与档位启发式**，不是可用性来源。可用性只能来自 §4 的运行时发现 + 派发时验证。快照 2026-09-20：

| 家族 | 中档（mid） | 便宜（cheap） | 旗舰（high） | 备注 |
|---|---|---|---|---|
| GLM（智谱） | `glm-5.3`（纯文本） | `glm-5.3-flash` | — | |
| DeepSeek | `deepseek-v4-pro`（纯文本） | `deepseek-flash` | — | |
| OpenAI GPT | `gpt-5.6-terra` | `gpt-5.6-luna` | `gpt-5.6-sol` / `gpt-5.5` | 多 provider（openai-codex / github-copilot）；codex 通道 contextWindow 272k |
| Anthropic Claude | `claude-sonnet-5` | `claude-haiku-4-5` | `claude-opus-5` | copilot 通道的点式版本号 id（如 `claude-haiku-4.5`）已知会失效；Claude 家族实测经 cursor 通道（连字符版本号）可达——具体通道 id 以运行时 registry 为准 |
| Google Gemini | — | `gemini-3.8-flash` | — | 仅 cheap 档 |
| xAI Grok | `grok-4.6` / `grok-4.5` | — | — | |
| Moonshot Kimi | `kimi-k3` | `kimi-for-coding` | — | |

- **家族映射**按模型 id 词干（provider 之后部分）：`glm*`→GLM、`deepseek*`→DeepSeek、`gpt*|codex*`→GPT、`claude*|fable*`→Claude、`gemini*`→Gemini、`grok*`→Grok、`kimi*`→Kimi；其余（`composer`/`auto`/未知）不入跨模型池。
- **档位启发式**：表中列出的 id 用表内档位；未知 id 后缀含 `flash|luna|haiku|nano|mini`→cheap，含 `opus|sol|astra|fable|ultra`→high，否则 mid。
- **派发格式**：一律写全 `provider/model-id`。裸 id 在多 provider 同名时二义（如 `gpt-5.5` 同时存在于 openai-codex 与 github-copilot）。
- **派发时验证不可省**：registry 条目会漂移（模型下架/通道变更/版本号格式变化），派发失败按 §4 步骤 5 的 fallback 链处理并在报告留痕。
- **provider 偏好**：同家族多 provider 时优先非 `cursor` 前缀（cursor 通道有地区限制史与延迟代价；但个别家族可能仅 cursor 通道可达，此时 cursor 可用）；其次按 registry 列出顺序。
- 稿件/论文输入均为纯文本 MD；纯文本模型（glm-5.3、deepseek-v4-pro）可安全入阵。

## 2. 阵容档位（`--lineup`）

| 档位 | 辩手槽（分支 / persona） | 裁判槽 |
|---|---|---|
| `balanced`（默认） | 各家族 mid 档，一槽一家族 | 隔离家族的 high 档；无 high 档可用时用未用家族的最强 mid 顶替 |
| `cheap` | 各家族 cheap 档 | 同 balanced 裁判规则（裁判席不上 cheap——终审质量优先于成本） |
| `max` | 各家族可用的最高档 | 全场最强 high 档 |
| `single` | 跨模型关闭：全部槽位用会话默认模型 | 编排者自审 |

显式覆盖：`--models` 用**命名槽位**（见 §3），如 `--models=theory=deepseek/deepseek-v4-pro,referee=github-copilot/claude-opus-5`。未指定的槽按当前档位自动分配；自动分配避让已占用家族。命名指定的槽位跳过家族唯一性优化，但**裁判隔离与 tod 的 A/B 异族仍强制校验**：违反时报错并指出冲突槽位（修正后重跑；确要同族可用 `--lineup=single` 表达）。

## 3. 槽位定义（`--models` 的合法槽名）

| skill | 辩手槽名 | 裁判槽名 |
|---|---|---|
| `toc-review` | `identification` `construct` `theory` `scope` `alternative` `contribution`（六固定）+ `dynamic-1` … `dynamic-N`（0–2 动态） | `referee` |
| `tod-debate` | `A` `B`（多对手模式每加一对手加 `C` `D` …） | `referee` |

**不变量（优先级从高到低）**：① 裁判家族 ∉ 辩手家族（裁判隔离）；② tod 的 A/B 必须异族（对辩轴心）；③ 辩手家族尽量唯一。家族不足时牺牲 ③ 保 ①②——宁可辩手复用家族，不牺牲裁判隔离。

## 4. 分配与解析流程（编排者在派发前执行）

1. **运行时发现**：调用当前环境的模型发现机制（pi：`subagent({action:"models"})`），把输出原样存临时文件作为 registry dump。解析其中 `provider/id` 行与 "Current session model" 行得到可用集；**会话默认模型本身入候选池**（guaranteed 可派发）。dump 截断（"... and N more"）只降低先验置信：不在 dump 中的目录候选仍可尝试，由派发时验证兜底。**禁止读 auth.json / models-store.json**（密钥暴露；缓存不证明可派发）。非 pi 环境用该环境的等价发现机制；完全不可得时走 §5 single 路径。
2. **优先用解析器**：`python _shared/model-lineup/resolve_lineup.py --registry <dump> --slots <逗号分隔槽名> [--lineup …] [--models …] [--require-distinct-debaters]`，输出 §6 模板所需 JSON（含每槽 fallback 链与降级标注）。脚本不可用时按本节算法手工执行同逻辑。
3. **裁判优先分配**：先从可用集中选裁判家族——偏好序：Claude > GPT > 其余有 high 档的家族（按 §1 目录序）> 未被辩手占用的家族中最强 mid。预留该家族后，辩手槽按 §1 目录序从**剩余家族**逐一分配（一槽一家族）；辩手槽多于剩余家族数时，先复用已用家族的**异档**模型，再允许同档。裁判预留家族绝不分配给辩手。
4. **派发**：pi 环境用**单次** `subagent` 调用的 `workflowScript`（`runs.all([{key, agent, task, model}, …])`）并行派发全部分支/persona（每 child 带 `model: "provider/id"`；裁判槽可加 `:high` thinking 后缀；`agent` 名取环境实际可用列表——pi-subagents 内置如 `worker`/`researcher`/`reviewer`/`scout`，agents-team 的 profile 名如 `explorer` 不可用）。其他环境用其等价并行子 agent 机制，每子任务带模型覆盖。
5. **失败重派（逐槽语义）**：某槽派发失败（模型不存在 / provider 报错）→ 只降级该槽，按其 fallback 链重派一次并留痕；再失败 → 该槽降为会话默认模型 + 标注。**已成功的槽不动**。按 provider 计数失败：同一 provider 累计两槽失败后，后续槽的回退链绕开该 provider。不存在"全场转 single"的级联（除非全部槽都失败降级，此时在报告注明有效阵容）。
   - **辩手 fallback 链**：同家族 ≤2 → 跨家族每族 1 席（排除裁判家族）→ `session-default`（仅当会话模型**不属**裁判家族；同属则跳过并标注——辩手运行时不得落进裁判家族）。
   - **裁判 fallback 链（fail-closed）**：**只允许原裁判家族内换模型**（会话模型同属裁判家族时已经由家族池入链）；家族耗尽 → 回退 `orchestrator` 自审（输出带 `fallback_exhausted_action: orchestrator`）。**绝不进入辩手家族**——裁判在辩手家族上复核等于辩手自我复核，比编排者自审更糟。
6. **显式请求保护**：用户显式传 `--lineup`（非默认）或 `--models` 但环境无模型覆盖能力（无 model 参数 / 无子 agent 机制）→ **停止并告知**，不静默降级。默认档遇此情形 → 降级 single 继续并在报告标注。

## 5. 降级规则

| 情形 | 行为 | 报告标注 |
|---|---|---|
| 可用家族 ≥ 辩手槽数 + 1 | 全跨模型 | `lineup: <档位>; degraded: false` |
| 可用家族 ≤ 辩手槽数（且 ≥ 3） | 裁判照常预留隔离家族；辩手家族复用（先异档后同档） | `degraded: partial (family reuse: N 槽)` |
| 可用家族 = 2 | 裁判占一家族（隔离），全部辩手在另一家族 | `degraded: partial (2 families: referee isolated, debaters same-family)` |
| 可用家族 = 1 | 跨模型关闭，等同 `single`；裁判回编排者 | `degraded: true (single-family fallback)` + 原因 |

降级不阻塞任务——审查/对辩照常执行，但 lineup 状态必须进报告统计区，人工裁决时须知悉本场的跨模型防线打了折扣。

## 6. 报告透明度记录（两个 skill 共用模板，嵌报告统计区）

```
**模型阵容**：lineup = {balanced|cheap|max|single|manual}；degraded = {false|partial|true}（原因）
| 槽位 | 角色 | 模型（provider/id） | 家族 | 档位 |
|---|---|---|---|---|
| identification | 辩手 | zai-coding-cn/glm-5.3 | GLM | mid |
| …（六固定 + 动态分支逐槽列全） | | | | |
| referee | 裁判 | github-copilot/claude-opus-5 | Claude | high |
运行时重派：{无 | 槽位→替代模型（原因）逐条}
```

## 7. 首次真实运行检查单（环境级验证，一次性）

首次在真实稿件上运行 toc-review / tod-debate 时补验以下项，验完在报告中记录"环境级验证已通过"：

- [ ] `subagent({action:"models"})` dump 中实际可见的家族与 §1 目录的差异（OAuth/授权变化、id 漂移）——差异回写本表快照日期注释。
- [ ] 每个 fallback 链首项真实可派发（各家族至少一次成功 child）。
- [ ] 裁判槽 thinking 后缀（`:high`）在当前 pi 版本被接受。
- [ ] 全流程一次真实稿件运行：六分支并行派发无孤儿、重派留痕落报告、Panel 独立裁判输出可解析。
