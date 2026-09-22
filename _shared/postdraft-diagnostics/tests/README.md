# Regression fixtures — postdraft-diagnostics（当前基线见 v1.2.3 表）

`synth_draft.md` 是构造的边界用例草稿（三类 flag + 豁免 + 设计族差异）。预期输出（v1.2.3 验证）：did=4 / experiment=2 / unknown=4。词表修订后任一计数变化时，先核对是词表修订（升版本登记）还是规则回归。

已知刻意不修的 artifact：草稿内自注文字 `(T_DEFINITIVE produce → OVERCLAIM)` 会被自身命中（results s3），属测试文件构造噪音。

运行：
```
python ../analyze.py synth_draft.md --design did_natural_experiment
```
输出格式或 flag 数变化时，先核对是词表修订还是规则回归。

## floor test（Step 2.5 负对照回归，历史轨迹）

- `floor_test.py`：从句档 manifest（`~/.claude/skills/story-blueprints/v4/rhetoric-moves/sources/_backfill_manifest_2026-09-20.json`）抽 17 house + 24 field（seed 20260920），自动标注设计族后跑 analyze.py；设计标注证据需人工核对。
- 历史轨迹：v1.2.0 五轮 21.8→2.9 → v1.2.1 2.2 → v1.2.3 **2.1/千句**（当前，fixture `floor_test_1.2.3_results.json`）。
- 判读基准：范文 flag 不是误报就是词表-语料偏差记录；残差为噪声地板。词表再改动须先复跑本回归（密度不应显著低于 2，防过度抑制），synth 计数不变（did=4/experiment=2/unknown=4）。


## v1.2.3 基线（2026-09-20 冻结；探针套件并入回归体系）

| 基线 | 规模 | 实测 | fixture |
|---|---|---|---|
| Results 专项地板 | 91 篇 / 5381 results 句 | **1.49 /千句**（8 条残差，与 v1.2.1 冻结基线完全一致） | `floor_results_1.2.3_results.json` |
| 全量地板 | 41 篇 / 9432 句 | **2.1 /千句** | `floor_test_1.2.3_results.json` |
| synth 回归 | did=4 / experiment=2 / unknown=4 | 恒稳 | `synth_draft.md` |
| recall 探针 | 56 探针（42 真违规 + 4 PASS 期望 + 10 改判 NOT_A_VIOLATION） | **recall 0.976**（唯一 miss = 跨句语境，v1 接受）；PASS 特异度 4/4；改判一致性 10/10；0 污染 | `probe_gen.py` / `probe_run.py`（manifest 在 `probes_v1/`） |

探针语义注记：M3（we reveal）/M4（modal 剥离）变异在 124 范文实测零自然出现，探针只验证工具响应性，不代表范文分布。探针重生成前先删 `probes_v1/`（probe_gen 拒绝覆盖已有目录）。

**判读警戒**：
- Results 密度回升 > 3.0/千句 → 词表变更引入误报，逐条回溯；
- Results 密度 < 1.0/千句 → 过度抑制（Goodhart 侧风险），逐条检查新增守卫是否吞掉真阳性；
- 探针 recall < 0.80 或出现污染（对照孪生被 flag）→ 判定语义回归，先查守卫链是否吞掉目标句；
- 残差 8 条为已裁定分类（X/S/L/P），**不再追求归零**——归零即过度拟合。

**Runner 复现**：`python floor_results.py` / `python floor_test.py` / `python probe_run.py`；runner 从句档 manifest 选样、喂 source_md 全文，输出按当前 wordlists 版本号命名（避免再覆盖历史 fixture）。
