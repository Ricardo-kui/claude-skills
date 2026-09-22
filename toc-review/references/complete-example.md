# Complete Example — 端到端输入输出示例

虚构稿件（教学用途，非真实论文），展示六分支之一的辩论全程、Panel 裁决与报告片段。每轮真实运行参照此例的字段完整度与转述密度。

---

## 输入

```
/toc-review "D:\Projects\recall-focus\manuscript.md" --journal=AMJ
```

虚构稿件概要：CEO regulatory focus 与召回时点（time-to-recall），1995–2018 美国制造业召回面板，Cox 模型 + 交叠 DiD 补充。

## Step 0 产物（节选）

章节表：Introduction / Theory & Hypotheses / Methods / Results / Discussion / Limitations。

已声明局限清单（禁猎区）：

| # | 已声明内容 | 位置 | 标注 |
|---|---|---|---|
| 1 | 单一国家样本限制外推 | Limitations ¶1 | — |
| 2 | regulatory focus 测量依赖文本编码 | Limitations ¶2 | — |
| 3 | 机制检验不足 | Limitations ¶3 | [deflection-suspect]：原文"future research should unpack the psychological mechanism"——外包给未来研究，替代解释分支可打 |

事实卡：RQ = CEO regulatory focus 如何影响召回时点；IV = promotion/prevention focus（股东信文本编码）；DV = awareness-to-recall 天数；数据 = NHTSA 1995–2018；识别 = Cox 基线 + staggered DiD 稳健性；期刊 = AMJ。

## Step 1 分支返回（identification 支，节选）

```json
{
  "branch": "identification",
  "nodes": [
    {
      "node_id": "root",
      "topic": "staggered-did-estimator",
      "claim": {
        "topic": "staggered-did-estimator",
        "description": "Recalls adopt at heterogeneous dates, but the DiD robustness uses uncorrected TWFE; forbidden-signature comparisons may drive the estimate.",
        "evidence_quote": "We complement the hazard models with a difference-in-differences specification that includes firm and year fixed effects.",
        "evidence_section": "Methods, 'Robustness' subsection",
        "severity_guess": "major"
      },
      "advocate": {
        "acknowledges": false,
        "response": "The DiD is a secondary robustness check; the primary inference rests on the Cox models, which the concern does not touch.",
        "citation_quote": "Our baseline results are from Cox proportional hazard models (Table 3)."
      },
      "revision": {
        "revised_description": "Accepted that DiD is secondary; the unstated risk is narrower: the DiD is cited in the Discussion as corroborating causal timing, so a contaminated TWFE estimate is doing persuasive work beyond robustness.",
        "concedes": false
      },
      "moderator": {
        "verdict": "valid",
        "severity": "minor",
        "evidence_strength": "moderate",
        "realism": "fixable",
        "should_expand": true,
        "expansion_prompts": [
          "Does the Discussion's causal language lean on the DiD corroboration?"
        ],
        "reasoning": "Concern is grounded and survived rebuttal, but primary inference is Cox-based; severity downgraded to minor. The Discussion-usage angle merits one child."
      },
      "expanded_from": null
    }
  ],
  "surviving": ["root"],
  "branch_note": ""
}
```

注意此例展示的三种裁决轨迹：root 存活但降级（major→minor）、辩护方部分成功（claim 从估计量本身收窄到 Discussion 的使用方式）、child 只在 moderator 给出 expansion_prompt 时开。

## Step 2 核验输出（summary 行）

```
verified 9/11 quotes, 0 empty quotes skipped
```

两条未命中的处理：一条改引文后重跑命中；一条（theory 支）无独立原文支撑，Panel reject（reason: ungrounded）。

## Step 3 Panel 裁决（节选）

```json
{"verdict": "downgrade",
 "source_branch": "identification",
 "final_category": "identification",
 "final_severity": "minor",
 "fix_type": "revision_fixable",
 "cross_category_concerns": [],
 "reasoning": "Valid and unstated, but Cox carries the paper; the DiD issue is repairable by a modern estimator rerun. Endorse as minor, revision_fixable."}
```

另一条的 merge 示例：scope 支与 contribution 支都打了"单行业设定 + 泛化措辞"，Panel 将 scope 版并入 contribution 版（后者引用了 abstract 原文），cross_category_concerns 标注两支。

## Step 4 报告片段（节选）

报告头部统计区（含阵容透明度块，lineup-protocol §6 模板）：

```markdown
# ToC 红队审查报告 — 共同所有权与产品召回（虚构稿）

- 目标期刊：AMJ　审查日期：2026-09-20
- 分支：identification / construct / theory / scope / alternative / contribution（all 模式）＋ 动态分支 1 条（dynamic-1：机制边界——threat perception 的行业外推接缝，AMJ Canvas 要素 4×要素 7 薄弱接缝派生）
- 节点统计：辩论 9 个节点 → 存活 5 / 被驳回 3 / 撤回 1
- 模型阵容：lineup = balanced；degraded = partial（6 个非裁判家族 < 7 个辩手槽位，dynamic-1 复用 DeepSeek 异档）

  | 槽位 | 角色 | 模型（provider/id） | 家族 | 档位 |
  |---|---|---|---|---|
  | identification | 辩手 | deepseek/deepseek-v4-pro | DeepSeek | mid |
  | construct | 辩手 | zai-coding-cn/glm-5.3 | GLM | mid |
  | theory | 辩手 | openai-codex/gpt-5.6-terra | GPT | mid |
  | scope | 辩手 | github-copilot/grok-4.6 | Grok | mid |
  | alternative | 辩手 | kimi-coding/k3 | Kimi | mid |
  | contribution | 辩手 | zai-coding-cn/glm-5.3 | GLM | mid（家族复用，异档不可用时同档异模） |
  | dynamic-1 | 辩手 | deepseek/deepseek-flash | DeepSeek | cheap（家族复用取异档） |
  | referee | Panel 裁判 | github-copilot/claude-opus-5 | Claude | high |

  运行时重派：construct 槽首进模型派发验证失败，按 fallback 链重派 zai-coding-cn/glm-5.3-flash 成功（留痕）
- Panel 处置：endorse 3 / reclassify 0 / downgrade 1 / merge 1 / reject 1
- 证据核验：5/5 引文字面命中稿件
- 定位：本报告提取未声明弱点（已声明局限 4 条已列为禁猎区，其中 1 条判定为 deflection-suspect）
```

后续报告体（Major 记录块、刊层风险总评等）示例：

```markdown
### M1　[贡献与期刊契合] 泛化措辞超出单行业证据（合并 scope 支同类条款）

- **严重度**：major（Panel 裁决：merge）　**分支**：contribution（+scope）　**证据核验**：true　**修复类型**：contribution_structural
- **质疑**：摘要与讨论使用无行业限定的普遍表述，而样本仅含制造业召回；收窄措辞到设定内则贡献主张同步缩水
- **证据引文**："Our findings reveal how executive psychology shapes firm responses to product crises."（Abstract）
- **作者辩护方的回应**：引 Theory 节"we theorize at the level of threat perception, which is industry-agnostic"（acknowledges: false）
- **为何仍然成立**：理论层行业无关 ≠ 证据层可泛化；设定内收窄后，"first to link regulatory focus to recall timing"的贡献主张需重新定位
- **修复动作**：重写摘要与讨论的泛化句；或论证 threat perception 机制在服务业召回的成立条件
- **下游路由**：research-gap-diagnosis（重定位）/ grill-the-claim（重构贡献主张）

## 二、刊层风险总评（contribution_structural 条款）

| # | 门禁风险 | 证据要点 | 含义 | 路由 |
|---|---------|---------|------|------|
| 1 | 泛化措辞 vs 单行业样本 | Abstract 无限定表述 + Methods 制造业样本 | 收窄措辞或补定位论证 | research-gap-diagnosis |

总评：本稿在 AMJ 的最大门禁风险是贡献主张的泛化强度——机制理论（regulatory focus × threat perception）有跨行业野心，证据只覆盖制造业。
```

---

## 给运行者的对照点

- 辩论记录四阶段字段齐全，advocate 的回应保留原文引用
- 存活条款的质疑转述是中文、引文是英文原文
- deflection-suspect 的局限（机制外包）被替代解释支合法命中，已声明的 1、2 条无人复述
- moderator 降级（major→minor）与 Panel 再降级的双层校准路径可见
- merge 条款只出现一次，另一支在 cross_category_concerns 留名
- contribution_structural 条款进刊层风险区，修复优先级里只有 revision_fixable
