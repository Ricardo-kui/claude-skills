# Write-Theory 设计反馈闭环

本协议把“范文中出现了一个可迁移模式”与“write-theory 的设计存在缺陷”分开处理。每次单篇或批量 Theory 蒸馏都必须执行；没有缺陷时输出 `observations: []`，不得为了产生反馈而制造问题。

## 1. Paper-first 比较纪律

先完成论文自身的 build type、功能模块、why-chain、假设组织和 story-fidelity 提取，再打开 `write-theory` 对照。禁止先看规则、再把论文硬套成反例。

提出设计缺陷前必须：

1. 打开目标文件并复制最小、逐字 `rule_excerpt`；
2. 说明该规则为何会误路由、误拒合法写法或放过明显缺陷；
3. 确认当前 skill 尚未通过条件分支支持该写法；若已支持，只登记 confirming evidence；
4. 区分论文的已发表做法、作者论证薄弱点与 skill 设计缺陷。顶刊发表本身不证明每个局部写法都应成为规则。

## 2. 缺陷分类

| classification | 判断问题 | 常见目标 |
|----------------|----------|----------|
| `corpus_gap` | 规则正确，只缺少可迁移骨架/句式/反模式？ | `corpus/variants`、`subprotocols`、`sentences`、证据注册表 |
| `routing_defect` | build type、B0/B1、conditionality 或子协议路由漏掉合法分支/错误耦合？ | `corpus/meta/routing_table.md`、`SKILL.md` Selection rules |
| `validator_defect` | 合格 Theory 会被误拒，或逻辑断裂会被放过？ | post-generation validator、soundness/QC 协议 |
| `output_contract_defect` | 固定段号、固定模块顺序或必填字段妨碍合法理论结构？ | `SKILL.md`、phase references、output format |
| `schema_defect` | canonical story、hypothesis 或 mechanism mapping 无法表达必要状态？ | paper-state/story schema；高风险 |
| `stage_gate_defect` | preparing/refining/finishing 或 local-only 门控错误？ | story gate；高风险 |

## 3. 证据等级与行动资格

只有直接读取并核验论文 Theory 全文才算 `full_text_verified`。

| 证据 | 状态 | 可执行动作 |
|------|------|------------|
| 功能摘要/元数据 | EMERGING | 只登记，不修改核心 |
| 1–2 篇完整文本 | EMERGING | corpus optional variant；核心只登记 |
| ≥3 篇完整文本且跨 ≥2 期刊 | VERIFIED | 有边界 core patch 候选 |
| ≥5 篇完整文本且跨 ≥2 期刊 | ROBUST | 稳健候选，仍受适用范围约束 |
| 1 篇完整文本决定性推翻“必须/永远/只能” | FALSIFIER | 只可 conditionalize/decouple 绝对规则，不得建立相反绝对规则 |

“某做法在样本中未出现”通常不是排他性证据。跨论文累计时保留 `applicability`（build type、hypothesis family、journal/setting boundary），不得把特定架构证据升级为全类型规则。

## 4. 硬化输出

```yaml
skill_design_feedback:
  batch_id: "batch_YYYY-MM-DD"
  last_updated: "YYYY-MM-DD"
  observations:
    - defect_id: "stable-rule-level-id"
      classification: "routing_defect"
      current_rule: "[现行规则的准确概括]"
      rule_excerpt: "[从 target 逐字复制的最小片段]"
      rule_locator: "[标题或行号提示]"
      target: "write-theory/corpus/meta/routing_table.md"
      diagnosis: "[为何是技能设计问题，不只是 corpus gap]"
      absolute_rule: false
      decisive_falsifier: false
      risk: "low / medium / high"
      applicability:
        build_types: ["机制推演型"]
        hypothesis_families: ["main_effect_only"]
        boundary: "[修订只适用到哪里]"
      evidence:
        papers:
          - id: "author_year"
            journal: "AMJ"
            build_type: "机制推演型"
            evidence_anchor: "Theory H1 development: [功能描述]"
            evidence_quality: "full_text_verified / functional_summary / metadata_only"
      proposed_change:
        action: "decouple / conditionalize / add_branch / correct_validator / revise_output_contract"
        summary: "[最小、有边界修正]"
      regression_cases:
        positive:
          prompt: "[新模式的真实写作任务，不泄露答案]"
          expected_invariants: ["[功能性质]"]
        preservation:
          prompt: "[必须保持的旧模式任务]"
          expected_invariants: ["[旧行为性质]"]
      resolution: null
```

字段纪律：

- `defect_id` 描述规则层问题，同一问题跨论文复用；不得包含论文 ID。
- `target` 只能是 `.claude/skills` 下的相对文件路径，不带行号、`..` 或盘符。
- `rule_excerpt` 必须由持久化脚本在当前目标中逐字核验；找不到则不得登记。
- `evidence_anchor` 记录段落/句群的功能证据，不复制长原文。
- 非 `corpus_gap` 必须提供 positive 与 preservation 两个回归案例。
- `resolution` 仅在实际尝试修订后填写：`{status, modified_targets, validation, date}`。

## 5. 持久化

将上述 YAML 保存为临时文件后运行：

```powershell
python C:\Users\admin\.claude\skills\distill-theory-exemplar\_update_design_feedback.py <feedback.yaml>
```

脚本写入 `write-theory/corpus/_skill_design_feedback.yaml`，负责去重、累计论文/期刊/适用范围、计算状态和行动资格。脚本**只记账，不修改核心 skill**。

## 6. 核心自动修订门控

仅在以下条件全部满足时应用核心修改：

1. 用户已授权更新 write 系列 skill（当前任务授权或持久化工作协议）；
2. 目标规则和全文证据锚点均已核验；
3. 状态为 VERIFIED/ROBUST，或为针对绝对规则的 full-text FALSIFIER；
4. 修改是有边界的 conditionalize、decouple、add branch 或 validator correction；
5. 不涉及 schema/stage gate、跨技能字段语义、`risk: high` 或破坏性迁移；
6. positive 与 preservation regression cases 均已定义；
7. 不覆盖用户已有、无关的工作区修改。

不满足时只登记。schema、stage gate、高风险或跨技能契约变更始终输出人工审核包。

## 7. 修订后验证与 resolution

1. 用 `skill-creator/scripts/quick_validate.py` 验证 distill-theory 和 write-theory。
2. 解析所有 YAML，检查 Markdown 链接、路径与 whitespace。
3. 运行脚本 `--self-test` 与 `--dry-run`。
4. 分别前向测试 positive 与 preservation 原始任务，不向测试者泄露预期修复。
5. 任一失败，撤回本轮核心修改，保留 registry 条目并记录 `needs_revision`。
6. 全部通过后，再提交同一 `defect_id` 的 resolution。`applied` resolution 必须提供 `modified_targets`、目标文件中可逐字核验且不同于旧规则的 `rule_excerpt_after`、`old_rule_excerpt_absent`（若旧绝对规则应删除）以及三项验证结果；不得只凭布尔声明把未修改的规则标为 resolved。

共享 Junction 会使 `.agents/skills/write-theory` 与 `.claude/skills/write-theory` 立即保持一致。
