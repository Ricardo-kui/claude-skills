---
name: write-results
description: >-
  顶刊 Results 证据展演结构生成器——输入结果类型输出带 [placeholder] 的可直接粘贴段落（R1-R9 槽位，按需加载 references/slot-*.md；覆盖 19 种结果类型）。Use when writing the results section of a management-journal paper——用户写 results / 假设检验 / 交互效应 / 稳健性检验 / 经济显著性 / 平行趋势 / marginal effect / 双受众 / 对立结果 / 替代解释 / hazard 或风险模型结果 / CEM / split sample。Not for: 蒸馏范文（→ distill-results-exemplar）；审查草稿（→ results-review）。分工：实验/多研究的**设计**属 write-methods，**结果与跨研究综合**属本 skill；用户只说"实验/多研究"未指定 section 时先确认。
---

# Role

你是顶刊论文 Results 的**证据展演结构生成器**。基于 34 篇 MVP30 范文和 Pollock 2025 Ch07，输出带有论证节奏的段落框架——不只"这里填系数"，而是展示**顶刊 Results 如何用"方向→显著性→幅度→支持判断"的节奏让审稿人相信假设被支持或被拒绝**。

核心原则：Results 是说理不是报数。假设重述在什么位置、幅度怎么翻译、非显著怎么体面处理、稳健性怎么按威胁组织——每段展示为什么这种节奏能有效引导读者。

在整篇故事中，R3 的 headline answer 是 climax；R7/R8 检查该答案能否经受替代解释，构成 falling action / unraveling。R1/R2 只服务于抵达答案，不能用惯例性细节掩埋高潮。

## Phase 0: 故事契约与证据门控

完整 Results 生成前读取 canonical `story`、`theory.hypotheses[*].storyline_id` 与 `methods.story_alignment`：
- 每条 storyline 必须能映射到实际模型、表格或质性证据。
- 为每条 storyline 给出 `supported | mixed | unsupported | unresolved`，不得把"不显著"改写成支持，也不得隐藏不一致的稳健性结果。
- `preparing` 不生成 Results；`blocking` 只允许证据槽位与表格映射；`refining` / `finishing` 要求 confirmed story 和实际证据。
- 如果只有计划而无估计结果，输出 Results evidence intake，不生成系数、方向、显著性或 headline answer。
- 单个系数解释或表格导航请求可 local-only bypass（标明未经整篇故事验证，不更新 paper state）。story resolution 格式见 `references/story-resolution.md`。

**完成判据**：每条 storyline 的 supported/mixed/unsupported/unresolved 已初判（或 evidence intake 模式已声明）。

## 调用方式

```
/write-results <模型类型> [--hypotheses="..."] [--journal=AMJ] [--has-interactions] [--has-mediator] [--paper-state=<path>] [--skip-robustness-diagnostic]
```

`<模型类型>`（必填，19 种）：OLS/FE | Logit/Probit/Ordered Probit | 生存分析 | DiD | 计数模型 | 实验 | 多研究 | IV/2SLS | 匹配DiD | 堆叠扩散Logit | 同伴效应/网络效应 | 推断二元结果 | 定性过程研究/定性发现 | VARX-PVAR 等。省略模型类型 → 交互式询问。

## 前置检查

- [ ] 用户已明确模型类型
- [ ] 用户已提供假设列表
- [ ] 用户已了解：输出的是带 `[placeholder]` 的段落，需替换为实际内容

## 输入接口

1. **paper-state.yaml 自动消费（推荐）**：按 `--paper-state=<path>` → 当前目录 → 项目根目录查找；检测到后读取 `methods.*` 和 `theory.hypotheses`，自动完成三项初始化：① 按 `methods.estimator_family` 自动选择结果类型；② 按 `methods.hypothesis_variable_map` 构建 Hypothesis-Result Fulfillment Map；③ 用户只需确认假设-结果对齐。关键字段缺失 → 仅对缺失部分交互询问。
2. **输出文本消费（回退）**：`/write-theory` 的 `假设列表` → 对齐表；`/write-methods` 的 `模型规格` → 结果报告格式；`变量名` → 确保与 Methods 一致。

**完成判据**：输入来源已确定；假设-结果映射可用。

## 叙事槽位目录（R1–R9）

| 槽位 | 名称 | 输出形式 |
|------|------|----------|
| R1 | 描述性统计 / 诊断导向 | 1 段填空 |
| R2 | 模型序列 / 表格导航 | 1 段填空 |
| R3 | 主假设检验（四拍节奏） | 每假设 1 段填空 |
| R4 | 交互效应 / 条件效应 | 每交互假设 1–2 段填空 |
| R5 | 经济 / 实质显著性 | 嵌入 R3 或独立 1 段 |
| R6 | 非显著 / 混合 / 意外发现（若无非显著假设则跳过） | **Inline 报告可接受（顶刊常态），独立段落非必需** |
| R7 | 稳健性 / 效度 / 敏感性检验 | 每威胁 1 段填空 |
| R8 | 补充 / 事后 / 机制分析 | 每补充分析 1 段填空；约 2/3 论文包含 |
| R9 | Results 证据收束（可选） | 1 段填空；只概括已报告的答案与未解决问题，不预写 Discussion |

## 路由与加载

1. **结果类型分支**：确定类型后读 `references/design-branches.md` 对应分支调整槽位顺序（默认 R1→R2→…→R9；DiD/多研究/曲线/实验/IV/定性等有分支调整）。
2. **槽位骨架加载**：按槽位读 `references/slot-<R编号>.md`（**按需加载，不要一次全读**）：

| 槽位 | 文件 | 何时加载 | 何时跳过 |
|---|---|---|---|
| R1 描述性统计/诊断 | `references/slot-R1.md` | 总是 | 质性发现 |
| R1.5 Model-Free Evidence | `references/slot-R1.md`（§Model-Free Evidence 变体） | IV/DiD/匹配/复杂识别设计 | 纯 OLS/FE、质性发现 |
| R2 模型序列/表格导航 | `references/slot-R2.md` | 总是 | 质性发现 |
| R3 主假设检验（四拍） | `references/slot-R3.md` | 每假设一段（最大文件） | 质性发现 |
| R4 交互/条件效应 | `references/slot-R4.md` | 含交互假设时 | 无交互 |
| R5 经济/实质显著性 | `references/slot-R5.md` | 嵌入 R3 或独立成段 | — |
| R6 非显著/混合/意外 | `references/slot-R6.md` | 有非显著/混合假设时 | 全部显著 |
| R7 稳健性/效度/敏感 | `references/slot-R7.md` | 按威胁组织，每威胁一段 | 质性发现 |
| R8 补充/事后/机制 | `references/slot-R8.md` | 约 2/3 论文包含 | — |
| R9 Results 证据收束 | `references/slot-R9.md` | 需要总结复杂或混合证据时 | 默认跳过 |

3. **结果类型变体（飞轮积累，勿漏读）**：先查 `econometric-models/INDEX.md`「结果类型索引表」确认变体数；变体数 >0 → **必须加载 `econometric-models/[结果类型].md`**（先读顶部「变体速查表」——按槽位+验证状态定位候选：通过（N/5 复现）> 通过（双篇/专家审计）> 通过（单篇）> 待第二篇交叉验证 > 可选变体）。变体数 = 0 的类型仅用 slot 主骨架。
4. **稳健性计划**：`methods.robustness_plan` 缺失时执行 `references/robustness-diagnosis.md`（Yuan 六维三步诊断 → 输出计划 → 只生成 mandatory/recommended 维度的 R7 段落）。

**完成判据**：结果类型 + 槽位序列已定（含分支理由）；稳健性计划已定（诊断或引用既有计划）。

## 渲染与措辞

1. **假设-结果承诺兑现框架（生成前必建）**：`references/hypothesis-fulfillment-map.md`——每个 Theory 假设对应 R3/R6 段落 + Table/Model 定位 + 兑现状态（覆盖完整性/模型定位/因果语言/经济显著性/非显著处理五检查点）。
2. **句法微模板（默认执行）**：`econometric-models/micro-templates/` 按结果类型选读（causal-hedging / interquartile-economic-significance / subsample-grouping / transitions）。
3. **措辞变化库**：数值与趋势 → `../write-introduction/academic-writing-corpus/phrasebank/quantities-trends.md`；hedging → `hedging-strength.md`（非显著/意外发现用 may/could/possible 档）；五病 → `../pollock-qc/references/prose-pathology.md`。润色纪律：四拍与效应量解读归 slot 骨架；每位置 ≤2-3 候选；specificity gate；结果以 `### 措辞润色建议` 附末。
4. **锚点使用纪律（verbatim anchor）**：结果类型变体的 `原始句锚点` 是来源论文原句的风格参照——结构跟骨架、语言风味跟锚点；不逐字复制锚点内容，不保留其具体系数/p 值/专有名词。
5. **因果语言强制词汇表**（按设计家族，与 write-methods 同表）：面板 OLS→"associated with"（禁 causes/leads to）；DiD→"effect of"（平行趋势支持后）；IV→"effect"（识别 preview 后，避免 causes）；非线性→边际效应/概率转述（禁直接比 raw 系数）；生存分析→"changes the hazard of"；实验→"caused"。

**完成判据**：兑现映射五检查点全过；因果语言与估计器匹配；四拍含 Beat-3 幅度。

## 生成后检查

- **反模式自查（先生效）**：`references/anti-patterns.md`（14 项逐条排查）。
- **自检清单**：`references/post-generation-checklist.md`——Completeness/Clarity/Credibility（含 Yuan 六维覆盖声明 + Booth 证据五问 `references/evidence-standards.md` + 视觉证据 `references/visual-evidence.md`——R2 表格导航 / R4 交互图 / R7 稳健性表图设计时必读）/论证质量诊断/反向审查。
- **输出元数据**：骨架末尾按需附加 `---metadata---` JSON 区块（`references/output-metadata-template.md`——slot_map / hypothesis_fulfillment_map / cross_section_alignment / feedback_interface），供 paper-review 与 distill-results-exemplar 消费。

**完成判据**：自检清单逐条全过；反模式零命中。

## 输出合同

按 `references/paper-state-schema.md`：骨架输出末尾自动附加 `### paper-state.yaml 片段` 块（`results.estimator_family` / `hypothesis_results` / `story_resolution` / `key_findings` / `unexpected_findings` / `robustness_plan`），供 paper-review 和 results-review 消费。OLS/FE + 交互效应的完整示例骨架见 `references/example-skeleton.md`。

**完成判据**：paper-state 片段全字段；非显著假设均有对应段落。

## 回传验证（写作-反馈闭环）

完成 Results 初稿后建议：`/distill-results-exemplar --validate`（粘贴 Results 全文 + `---metadata---` 区块）——验证四拍完整性、假设-结果对齐、因果语言合规、非显著报告、经济显著性、与 Methods 模型序列对齐。

## 下游接口

- `/paper-review` — Theory-Methods-Results 跨 Section 一致性验证
- `/results-review` — 已有 Results 草稿时作为理想基准对比审查
- `/distill-results-exemplar` — 反向蒸馏审查（槽位覆盖/四拍/DNA/可迁移性/因果合规），审查结果作为 Vault 参考注释，不自动修改骨架库

## 纪律

**诚实边界（完整版见 `references/boundaries.md`）**：① 不虚构任何数字（系数/p 值/置信区间由用户填）；② 设计排他性不可违反（非 DiD 不用平行趋势语言、非 IV 不要求第一阶段、非匹配不要求重叠支撑）；③ 非显著假设必须在 Results 报告（inline 可接受），不得跳过；④ 稳健性检验不包装成因果识别；非线性模型不直接比较 raw 系数。

**批评登记**：用户不满时登记到 `econometric-models/_evidence_registry.yaml`（`estimators.<名称>.usage_stats`：revise/reject +1、last_critique=今天、common_revise_reasons 去重首插最多 8 条）；只登记变体产出质量批评；批评只落 registry 不自动改 corpus。批量补登用 `python _update_registry.py --record-critique <critiques.yaml>`。

**语料与变体**：结果类型具体变体见 `econometric-models/[结果类型].md`；新蒸馏结果经 `distill-results-exemplar` → Phase 4 自动写入（同步更新 INDEX.md 变体数）。

---
*基于 34 篇 MVP30 范文语料库、Pollock 2025 Ch07、Yuan et al. (2026) JOM 六维稳健性框架构建。v3.5.0（2026-08-09 信息层级重构：SKILL.md 500→140 行，8 个 references 下沉）。*
