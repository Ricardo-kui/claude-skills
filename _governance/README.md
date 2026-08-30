# _governance — 语料库治理层（维护期工具，非运行期门禁）

本目录是从 write-* 技能本体裁撤的脚本化治理基础设施的恢复副本（2026-08-10 从
`~/.agents/skills_backup_20260810` 恢复）。定位：**只在语料维护期使用**，不参与
write-* 技能的日常写作运行；写作技能的运行期纪律由各自的 SKILL.md 文本规则
（硬约束表、registry 状态带、选材 Gate）承载。

## 目录结构

- `write-theory/benchmarks/theory_governance/` — R2–R6 盲评资产：tasks.yaml（24 任务
  预注册矩阵）、evaluator_rubric.md、各轮 blinded pairs / judge 评分 / score summary。
  这是全库唯一的**回归检测**能力：语料变更后生成质量是否退化，靠它判定。
- `write-theory/scripts/theory_governance_benchmark.py` — 校验/冻结盲测矩阵
  （自包含，直接可运行）。
- `write-results/scripts/r2_forward_benchmark.py`、`select_r2_pilot.py` +
  `tests/r2_forward_{prompts,gold}.yaml` — Results 侧 R2 前向盲测 harness。
- `write-introduction/scripts/` + `tests/fixtures/` — Introduction 治理 benchmark
  （依赖 `introduction_asset_catalog.py`）。

## 语料连接

三个语料目录是指向 live 技能的 junction，治理工具读到的始终是当前语料：

- `write-introduction/corpus` → `../../write-introduction/corpus`
- `write-theory/corpus` → `../../write-theory/corpus`
- `write-results/corpus` → `../../write-results/corpus`
  （`_pilot_r2_index.yaml` 因此放回了 live write-results 的 corpus/ 下）

## 触发时机

1. 每次 distill-* 技能向 write-* 语料回写（ADD/EXTEND/REPLACE）之后；
2. 定期体检（建议每月或每积累 5+ 篇新蒸馏）：先跑 skills 根目录的
   `corpus_health_check.py --type all`（exit 1 = 存在 critique_heavy 类型，
   下一轮蒸馏应优先 REPLACE/EXTEND）；
3. 大改语料结构（删除变体、改 registry schema）前后各跑一次 theory 盲测矩阵校验：
   `python _governance/write-theory/scripts/theory_governance_benchmark.py`。

## 已知边界

- 盲评的"生成-评判"两步由 agent/人按 rubric 执行，脚本只负责矩阵校验、抽样与计分；
- `r2_forward_benchmark.py` 生成的盲测 prompt 默认指向 live write-results
  （环境变量 `WRITE_RESULTS_ROOT` 可覆盖）；
- `introduction_asset_catalog.py` 已打兼容补丁：新版 registry 没有 `asset_governance` 段时
  按旧版默认值合成（全部资产 active、无 overrides/snapshot），并跳过快照一致性检查——
  意味着 Introduction 侧治理工具退化为"目录检索 + 盲测矩阵校验"，不再有资产生命周期管控；
- 旧的 write-methods 只有 catalog + 单元测试，无盲评资产，未恢复（见备份）。
