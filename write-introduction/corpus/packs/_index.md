# Narrative Shape Packs — 叙事形状包索引

> **接口**：L-Story（`story-blueprints/v4/`）与 L-Outline（write-introduction Phase 2）之间的调用单元。Phase 2 先查本目录取 1 个形状最近的对照，再按 `references/outline-protocol.md` O1–O3 出大纲表。
> **内容来源**：形状包由 corpus 段级锚点与原叙事型句库的段落底本派生，人工不维护 verbatim 正文。
> **单源纪律**：verbatim 底本只存在 `corpus/_skeleton/` 各子索引里；本目录只写底本 `id` 引用与状态。
> **边界**：形状包只在故事已锁定（story contract 之后）提供形状与底本，**不参与故事类型选择**，不反推故事类型（见 `../../references/library-contract.md` 边界 2）。

## 包清单

| pack-id | 形状指纹（形状，不写故事类型） | 适用条件 |
|---|---|---|
| [`portfolio-governance`](portfolio-governance.md) | 跨单位结构条件改变行动者目标/外部性权重 → 双边际治理结果；边界由该结构机制本身推出。段落形状：P1 裁量空间→结构条件 · P2 内部→外部→所有权 · P3 对立机制→裁定 · P4 一构念统摄两边界 · P5 量级+一次边界披露 · P6 问题转换+实践/政策收束 | 同一前因被分派到 ≥2 个决策边际；结构条件跨单位成立；closest paper 有可点名的 focal-firm premise；Gap 以 Incompleteness（可带 Mechanism）为主 |

> 当前仅 1 个形状包（2026-09-14 落地）。原叙事型句库已在三拆分 ③–⑥ 完成后退役，其余内容按 worked example 与对照卡分别落位。

## 包命名与固定结构

- 文件名即 `pack-id`，kebab-case，例如 `portfolio-governance.md`；引用记法 `shape:<pack-id>`。
- 每个包固定四段：
  1. 形状指纹（**形状**，非故事类型）
  2. 段落序列（每段：主导功能 + 承载信息 + 可用底本 id 列表）
  3. 每段底本状态：`verbatim`（引 `_skeleton/` 的 id）或 `模板`（引 archetype 原文并标 `模板`）
  4. 对照底本（失败写法清单归 `corpus/contrast-pairs/`，本目录不复写）

## 上下游

- 上游：原叙事型句库的段落底本（已退役；派生来源记为 worked example 与骨架索引）；`write-introduction/references/library-contract.md` 边界 1 的放宽授权（形状可作段落大纲底本，不得作句子底本）。
- 下游：`write-introduction/references/outline-protocol.md` O1 取材（`来源` 记 `shape:<pack-id>`）；G1 借句表按段取该包列出的底本 id。
- 生成工具：`scripts/build_indices.py`（骨架索引）；形状包以骨架索引 id 为准，id 变动时需同步复核。
