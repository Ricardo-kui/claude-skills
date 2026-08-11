# Reverse Validation Pipeline — write-methods / write-results 反向端到端验证工具

> **定位**：独立 Python CLI 工具（非 skill，无交互流程）。验证 `write-methods` / `write-results` 的语料槽位能否**反向复现**蒸馏出的顶刊范文——从成品反推模板是否可生成。与正向蒸馏（distill-methods/results-exemplar）闭环。
> **状态**：v2.5.0。手工运行；未纳入自动流程。

## 目的

正向链路：`distill-*-exemplar` 把顶刊论文的 Methods/Results 蒸馏成结构化 JSON（M1–M10 / R1–R9 槽位映射），验证通过的变体写回 `write-*` 语料。

本工具做**反向验证**：把蒸馏 JSON 再喂回来，检查 `write-methods` / `write-results` 的 SKILL.md 槽位模板 + `econometric-models/` 语料（经 `config/design_type_map.json` 的设计类型→变体映射）是否真的能覆盖这篇论文的每一项——即"语料声称覆盖的设计，能否反向生成原范文的蒸馏结构"。产物是 Gap 报告与跨技能一致性报告。

> 一句话：**蒸馏回答"范文里有什么"，反向验证回答"我们的语料写不写得出来"。**

## 输入格式

两份蒸馏 JSON（`*_methods_distilled.json` + `*_results_distilled.json`），顶层结构：

```jsonc
// methods
{
  "paper_id": "Zhou_Gao_Zhao_2017_ASQ",
  "phase_0": { "design_type": "ols/fe", "estimator_family": "OLS", "dependent_variable": "...", "independent_variables": "..." },
  "phase_1_slot_map": {
    "M3": { "located": true, "dv_construct": "...", "operationalization": "...", "source": "..." },
    "M4": { "located": true, "predictors": [{"name": "...", "hypothesis_link": "H1"}] },
    "M5": { "located": true, "moderators": ["..."], "mediators": ["..."] },
    "M9": { "located": false }
    // ... 其余 M 槽位
  }
}

// results
{
  "paper_id": "Zhou_Gao_Zhao_2017_ASQ",
  "phase_0": { "hypothesis_structure": "H1 ... H2a ...", "nonsignificant_findings": "..." },
  "phase_1_slot_map": {
    "R3": { "hypotheses_covered": ["H1", "H2a"], "nonsignificant_hypotheses": ["H2b"] }
    // ... 其余 R 槽位
  }
}
```

- `design_type` 可选值见 `config/design_type_map.json` 的 `distillation_to_skill` 键（如 `did` / `iv/2sls` / `aft/weibull/survival` / `logit/probit` / `psm + did` …），`_infer_design_type` 会从 Methods+Results 的 `phase_0` 自动推断，无需手工标注。
- 键名漂移时先用 `normalize_distilled_json.py` 归一化（M1→M1 槽位格式、R 前缀对齐）。

## 用法

### 单篇（一对 JSON）

```bash
python reverse_validation_pipeline.py \
  --methods-json zhou_2017_methods_distilled.json \
  --results-json zhou_2017_results_distilled.json \
  --output-dir ./validation_output
```

### 批量

```bash
python reverse_validation_pipeline.py \
  --batch-dir ./distilled_jsons \
  --output-dir ./validation_output
```

批量模式下自动配对目录内 `*_methods_distilled.json` 与 `*_results_distilled.json`，逐对跑完后写 `batch_summary`。

### 参数

| 参数 | 简写 | 默认 | 说明 |
|------|------|------|------|
| `--methods-json` | `-m` | — | Methods 蒸馏 JSON（单篇模式） |
| `--results-json` | `-r` | — | Results 蒸馏 JSON（单篇模式） |
| `--batch-dir` | `-b` | — | 批量目录（含多对蒸馏 JSON） |
| `--output-dir` | `-o` | `./validation_output` | 报告输出目录 |
| `--skills-dir` | — | 仓库根目录 | 含 `write-methods/` 与 `write-results/` 的目录 |
| `--version` | — | `2.5.0` | 报告头部版本字符串 |

退出码：0 = 无 critical gap；1 = 存在 critical gap（供 CI 门禁用）。

## 输出

- **逐篇验证报告**（`output-dir/<paper_id>/report.md` 等）：每篇的槽位覆盖、模板选择、Gap 分析、跨技能一致性结论。
- **批量汇总**：`batch_summary` 文件，列出各篇是否命中 critical gap。
- 内部集成根目录的 `methods_results_quality_check.py`（`MethodsChecker`/`ResultsChecker`）做前向质量检查，严重度分级（`Severity`）汇入报告。

## 配置

- `config/design_type_map.json`（三个映射）：
  - `distillation_to_skill`：蒸馏 `design_type` → 命中 `write-methods`/`write-results` 语料文件名/变体（如 `did/staggered` → `准自然实验/DiD`；`aft/weibull/survival` → `生存分析`）。
  - `special_marker_to_variant`：特殊标记（`u_shaped` / `three_way_interaction` / `event_study_car` …）→ 追加命中的变体。
  - `slot_composition_rules`：槽位组合规则（如 `M7` 对 `tobit + iv` / `poisson + iv` / `lpm + 2sls` 的组合设计要求）。
- 新增设计类型时，先在此 JSON 登记映射，再回填语料。

## 与周边资产的关系

| 资产 | 关系 |
|------|------|
| `distill-methods-exemplar` / `distill-results-exemplar` | 上游：产生本工具的输入蒸馏 JSON |
| `write-methods` / `write-results` | 被测对象：本工具验证其 SKILL.md 槽位与语料覆盖 |
| `methods_results_quality_check.py`（仓库根） | 前向质量检查模块，被本工具集成 |
| `normalize_distilled_json.py` | 蒸馏 JSON 键名归一化，跑本工具前的清洗步骤 |
| `econometrics-agent` | 同类 CLI 包装先例（SKILL.md 包装方式对齐） |

## 测试

`tests/` 内含 smoke test：构造最小 methods/results 蒸馏 JSON 对，跑通单篇流程，断言报告产出与 critical gap 判定。运行：

```bash
python -m pytest reverse_validation_pipeline/tests/ -v
```

## 未做（后续候选）

- [ ] 批量报告聚合为跨论文覆盖度表（哪些槽位在 N 篇中未命中）
- [ ] 接入 distill-* 的 Phase 5 作为可选自动 gate（当前为手工运行）
- [ ] CI 集成：跑完后以退出码驱动语料覆盖度门禁
