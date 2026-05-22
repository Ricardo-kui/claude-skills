---
name: write-methods
description: |
  当用户需要撰写或修改论文 Methods 部分时触发。根据设计类型（面板数据-OLS、DiD、生存分析、IV/2SLS 等）输出带占位符的可直接粘贴段落骨架，覆盖 M1-M10 全部槽位。
  与 distill-methods-exemplar 的区别：本 skill 生成段落（写/生成），distill-methods-exemplar 从范文提取模式（读/分析）。
  触发词：写 methods、methods 模板、方法部分怎么写、methodology 写法、method skeleton、写方法、方法论、variable definition、model specification、样本选择、变量操作化、识别策略、稳健性检验、模型设定、样本漏斗、内生性处理、估计方法。
version: 3.0.0
---

# Role

你是顶刊论文 Methods 的**填空模板生成器**。基于外置语料库 `academic-writing-corpus/` 中的骨架变体，输出可直接复制到 Word/LaTeX 中、填入用户具体信息即可成段的 Methods 骨架。

核心原则：Methods 要 **describe, explain, justify**。每个填空段落已经内置了这三重功能，用户只需替换方括号中的占位符。

## 调用方式

```
/write-methods <模型类型> [--hypotheses="..."] [--journal=AMJ] [--design-variant=标准] [--micro-template-tier=core]
```

**参数说明**：
- `<模型类型>`（必填）: `面板数据/OLS` | `自然实验/DiD` | `非线性模型` | `生存分析` | `SEM` | `实验` | `多研究` | `稀有结果` | `实证对象构建` | `事件历史+事件研究` | `同时方程` | `IV/2SLS` | `动态面板/GMM` | `匹配DiD/广义DiD` | `同伴效应/网络效应` | `文本构念测量` | `PSM匹配面板` | `堆叠扩散Logit` | `多行为者设计` | `推断二元结果`
- `[--hypotheses]`（可选但建议）: Theory 部分的假设列表，用于变量对齐检查
- `[--journal]`（可选）: 目标期刊，默认 `AMJ`
- `[--micro-template-tier]`（可选）: 微模板加载分级，`core`（默认，高频通用）| `extended`（含中频特定）| `full`（全部加载）

**如果省略模型类型**，进入交互式询问，确定设计类型后输出对应骨架。

## 前置检查

- [ ] 用户已明确模型类型和设计变体
- [ ] 用户已提供数据来源和时间范围
- [ ] 用户已了解：输出的是带 `[placeholder]` 的段落，需替换为实际内容

## 输入接口

可直接消费 `/write-theory` 的输出：
- `假设列表` → 用于构建假设-变量映射表
- `核心构念` → 用于变量操作化模板

## 叙事槽位目录（M1–M10）

| 槽位 | 名称 | 输出形式 |
|------|------|----------|
| M1 | 研究情境 / 实证背景 | 1 段填空；JM/ASQ 通常保留，AMJ 约 30% 缺失（被 Introduction 覆盖） |
| M2 | 数据来源与样本漏斗 | 1–2 段填空 |
| M3 | 因变量 | 1 段填空 |
| M4 | 自变量 / 核心预测变量 | 每假设 1 段填空 |
| M5 | 调节/中介/机制变量 | 每变量 1 段填空 |
| M6 | 控制变量与竞争性解释 | 1–2 段填空 |
| M7 | 模型规格与估计方法 | 1–3 段填空（含公式+文字） |
| M8 | 识别策略 / 效度 / 诊断检验 | 1–2 段填空；IV/DiD/实验/匹配 强制；OLS/FE 可选 |
| M9 | 多研究 / 实验程序 / 质性编码 | 多研究时逐研究重复 M1–M8 |
| M10 | Methods 到 Results 的过渡 | 1 段填空；**顶刊中极度罕见（<10%），可省略** |

## 标准顺序与特殊分支

**默认顺序**：M1 → M2 → M3 → M4 → M5 → M6 → M7 → M8 → M10

**特殊分支顺序调整**：
- **稀有结果**：M2 先说明抽样策略，再进入变量
- **实证对象构建**：M2 先说明数据构建逻辑
- **自然实验**：M1 中先说明冲击/处理/对照/时点；M8 前置或与 M7 合并
- **多研究**：M9 前置为总览，然后逐研究重复 M1–M8
- **事件历史+事件研究**：M3 分为过程时钟 DV 和市场时钟 DV 两段
- **同时方程**：M1 替换为概念框架→方程系统声明
- **IV/2SLS**：M4 增加工具变量合理性论证；M7 分两阶段说明；M8 增加排他性约束检验
- **动态面板/GMM**：M7 增加系统/差分 GMM 选择逻辑与过度识别检验
- **匹配DiD/广义DiD**：M2 增加匹配前后样本描述；M7 增加匹配估计量选择；M8 增加平行趋势与重叠支撑检验
- **同伴效应/网络效应**：M4 增加网络构念定义与反射性问题处理；M8 增加 falsification 检验
- **文本构念测量**：M3/M4 增加测量构建→效度检验→与人工程度相关性三段式
- **PSM匹配面板**：M2 增加倾向得分匹配步骤与共同支撑域；M7 增加匹配后估计量
- **堆叠扩散Logit**：M7 增加堆叠结构与条件Logit设定
- **多行为者设计**：M2 增加多数据源匹配；M3 区分主/辅行为者结果
- **推断二元结果**：M3 增加从连续/文本信号推断二元状态的逻辑与阈值

---

## 外置语料库与按需加载

本 skill 的所有填空骨架存储于外置语料库分片文件中，**不再硬编码于本文件内**。执行时按需读取对应设计类型的语料库文件，按 M1–M10 槽位组装输出。

### 语料库位置

```
~/.claude/skills/write-methods/academic-writing-corpus/
├── INDEX.md                      # 语料库索引与质量状态
├── _evidence_registry.yaml       # 证据注册表（paper_count、status、common_failures）
├── 面板数据-OLS.md
├── 自然实验-DiD.md
├── 生存分析.md
├── IV-2SLS.md
├── 匹配DiD-广义DiD.md
├── ... (共 21 个设计类型分片)
└── 两阶段模型.md
```

### 可用设计类型（与调用参数对应）

| 调用参数 | 语料库分片文件 |
|----------|---------------|
| `面板数据/OLS` | `面板数据-OLS.md` |
| `自然实验/DiD` | `自然实验-DiD.md` |
| `非线性模型` | `非线性模型.md` |
| `生存分析` | `生存分析.md` |
| `SEM` | `SEM.md` |
| `实验` | `实验.md` |
| `多研究` | `多研究.md` |
| `稀有结果` | `稀有结果.md` |
| `实证对象构建` | `实证对象构建.md` |
| `事件历史+事件研究` | `事件历史+事件研究.md` |
| `同时方程` | `同时方程.md` |
| `IV/2SLS` | `IV-2SLS.md` |
| `动态面板/GMM` | `动态面板-GMM.md` |
| `匹配DiD/广义DiD` | `匹配DiD-广义DiD.md` |
| `同伴效应/网络效应` | `同伴效应-网络效应.md` |
| `文本构念测量` | `文本构念测量.md` |
| `PSM匹配面板` | `PSM匹配面板.md` |
| `堆叠扩散Logit` | `堆叠扩散Logit.md` |
| `多行为者设计` | `多行为者设计.md` |
| `推断二元结果` | `推断二元结果.md` |
| `两阶段模型` | `两阶段模型.md` |

### 读取与组装协议

1. **定位分片文件**：根据用户指定的 `<模型类型>`，映射到上表中的 `.md` 文件。
2. **读取 frontmatter**：提取 `design_type`、`status`、`variants_count`、`source_papers`。
3. **按 M1–M10 槽位遍历**：
   - 每个分片文件按 `## M1.`、`## M2.` … `## M10.` 组织。
   - 槽位内包含 `### 主骨架（通用）` 和零至多个 `### 变体 N: [变体名]`。
4. **变体选择策略**：
   - `⭐ PREMIUM`：跨所有设计类型复现，必须输出。
   - `✓ STANDARD`：该设计类型的标准写法，默认输出。
   - `🔬 EXPERIMENTAL`：仅 1–2 篇范文出现，**默认不输出**。仅在用户明确要求扩展或该变体与论文设计强相关时才提供。
   - 带有 `⚠️ 保守替代` 的变体：仅在主骨架不适用时输出，并提示保守替代方案。
5. **累积变体区**：每个分片文件末尾的 `## 累积变体` 区块由 `distill-methods-exemplar` Phase 4 产出，供参考，**不自动纳入默认输出**。
6. **即时加载**：每次 `/write-methods` 调用时，实时读取对应分片文件内容，确保语料库更新立即可用。

### 输出格式

对每个存在的槽位，按以下结构输出：

```markdown
### M[slot]. [槽位名称]

**[变体标签]**: [变体说明]

```text
[骨架文本，含 [placeholder]]
```

[如适用，附保守替代提示或设计变体说明]
```

### 微模板组装层（Sentence-Level Assembly）

段落骨架解决"段落的结构功能"问题；**句法微模板**解决"段落内部的表达多样性"问题。

#### 微模板库位置

```
academic-writing-corpus/micro-templates/
├── INDEX.md                      # 微模板分类索引
├── opening-anchors.md            # 段首锚定短语
├── because-clauses.md            # because 从句架构
├── causal-hedging.md             # 因果动词梯度
├── transitions.md                # 过渡衔接短语
├── funnel-rhythm.md              # 样本漏斗节奏
├── identification-foreshadowing.md # 识别策略预告
├── variable-operationalization.md  # 变量操作化句式
└── robustness-foreshadowing.md   # 稳健性检验预告
```

#### 骨架-微模板映射表

显式绑定关系定义在 `_slot_micro_template_bindings.yaml` 中。该文件声明：
- 每个 M-slot 有哪些**句法位置**（opening_anchor, because_clause, transition 等）
- 每个位置应加载哪些**微模板条目**（具体到文件、章节、模板标签）
- 每个条目的**加载分级**（core / extended / full）

```
academic-writing-corpus/
├── _slot_micro_template_bindings.yaml   # 映射表
├── _evidence_registry.yaml              # 证据注册表
└── micro-templates/                     # 微模板库
```

#### 组装协议

1. **骨架优先**：先按 M1–M10 输出段落骨架（结构功能）。
2. **读取映射表**：根据当前 slot，从 `_slot_micro_template_bindings.yaml` 中查询该 slot 的 `syntax_positions`。
3. **分级加载微模板**：
   - **core**（默认）：只加载高频、跨设计类型通用、低风险的微模板。单次调用最多读取 4 个微模板文件，每个位置最多 2 个选项。
   - **extended**（`--micro-template-tier=extended`）：加载中频或设计类型特定的微模板。每个位置最多 3 个选项。
   - **full**（`--micro-template-tier=full`）：加载全部微模板。每个位置最多 5 个选项。
4. **微模板替换**：在骨架的关键句法位置，用映射表推荐的微模板替换默认措辞，提供选项供用户选择：
   - **段首锚定**：每个段落的第一句
   - **because 从句**：控制变量/样本排除/构念效度的理由
   - **因果动词**：根据设计类型从强制词汇表中选择
   - **过渡衔接**：多句段落内部的逻辑推进
   - **样本漏斗节奏**：M2 数字叙事
   - **识别策略预告**：M8 诊断检验预告
5. **选项标注**：每个微模板选项标注 `[core]` / `[extended]` / `[design-specific]` 等标签，帮助用户选择。
6. **默认策略**：若用户未指定微模板偏好或分级，使用 **core 分级**（最大公约数，最安全）。
7. **design_type_filter 交叉过滤**：
   - 映射表中部分微模板条目带有 `design_type_filter`（如 `["自然实验-DiD"]`、`["实验"]`），表示该句式**仅在对应设计类型下可用**。
   - 加载顺序为**先分级、后过滤**：
     1. 按用户指定的 `--micro-template-tier` 确定允许加载的 tier（core → core+extended+full 中满足 tier 条件的条目）。
     2. 在允许的条目中，进一步检查 `design_type_filter`：若条目带有此字段，只有当用户指定的 `<模型类型>` 与之匹配时才加载；若无此字段，表示跨设计类型通用，始终加载。
   - 典型模式：
     - **core 层级**：通常不带 `design_type_filter`，适用于所有设计类型（如 M6 的通用控制声明）。
     - **extended/full 层级**：常带有 `design_type_filter`，仅在特定设计类型下追加（如 M1 的 DiD 政策冲击式、M4 的处理变量声明）。
   - 选项标注：带 `design_type_filter` 的条目在输出中自动标注 `[design-specific]` 或 `[<设计类型> 专用]`，帮助用户识别其适用范围。

#### 上下文加载优化

为控制单次调用的文件读取量：
- **默认**（core）：只读取当前 slot 必需的 1–2 个微模板文件（如 M6 只需 `opening-anchors.md` + `because-clauses.md` + `transitions.md`）。
- **扩展**（extended）：增加 1–2 个设计类型特定的微模板文件。
- **完整**（full）：读取全部 8 个微模板文件（仅在用户明确要求时使用）。

#### 示例：M6 控制变量的微模板组装

```
骨架（来自 面板数据-OLS.md M6 主骨架）：
  We include controls for [threat family 1] because [alternative explanation 1].
  At the [level] level, we control for [variables] to account for [rival process].
  We also include [fixed effects] to absorb [time-invariant/common/contextual shocks].

段首锚定选项（来自 opening-anchors.md）：
  A. [通用] "We include controls for [threat family] because [alternative explanation]."
  B. [高 because 密度] "We included a broad set of control variables that influence
     [DV] directly and those that help address alternative explanations ([citation])."

because 从句选项（来自 because-clauses.md）：
  A. [竞争性解释型] "...because [rival theory] predicts that [alternative mechanism]
     drives [outcome]."
  B. [遗漏变量型] "...because [omitted variable] may confound the [IV-DV] relationship
     by [mechanism]."

过渡衔接选项（来自 transitions.md）：
  A. [层级递进] "We first included [level_1]_level factors... We also controlled for
     [level_2]_level characteristics... Lastly, we included..."
```

用户选择不同组合，可生成风格迥异的段落，避免同质化。

---

### 填空段落骨架（示例）

以下示例展示组装后的最终效果。实际调用时，骨架来自外置语料库分片。

### 示例：面板数据 / OLS

**输入**：`/write-methods 面板数据/OLS --hypotheses="H1: DT -> Routine updating; H2: Routine updating -> Innovation" --journal=SMJ`

**输出骨架**（用户应直接复制以下段落，替换方括号内容）：

```text
We focus on [U.S. publicly traded manufacturing firms] for three reasons. First, [manufacturing industries have experienced substantial digital transformation pressures], providing sufficient variation in our key independent variable. Second, [publicly traded firms are required to disclose IT expenditure data], enabling reliable measurement of [digital transformation]. Third, [manufacturing firms' innovation outcomes are well-documented in patent databases], allowing us to construct a comprehensive measure of [innovation performance]. The unit of analysis is [firm-year].

We began with [all publicly traded manufacturing firms] from [Compustat North America] over [2010–2020]. We matched these observations to [Harte-Hanks CI Technology Database] to obtain [IT expenditure data] and to [NBER Patent Database] to obtain [patent filings]. We excluded [financial firms (SIC 6000–6999) and utilities (SIC 4900–4999)] because [their regulatory environments and accounting practices differ substantially from manufacturing firms]. We also excluded firms with fewer than [three] years of consecutive data to ensure sufficient within-firm variation for fixed-effects estimation. The final sample consists of [X] [firm-year observations] from [Y] [unique firms].

Our dependent variable is [firm innovation performance], measured as [the natural logarithm of one plus the number of patents filed by the firm in a given year, scaled by R&D expenditure] using [NBER Patent Database]. This measure captures both the quantity and efficiency of innovation output because [patent count correlates highly with other innovation indicators]. Higher values indicate [greater innovation efficiency].

Our focal independent variable, [digital transformation intensity], is measured as [IT expenditure divided by total assets] based on [Compustat item X]. This variable corresponds to Hypothesis 1 because it captures [the firm's relative investment in digital technologies]. We present the focal variables in the order of the theory: [digital transformation intensity], [organizational routine updating], and [absorptive capacity].

To capture [the moderating role of absorptive capacity], we measure [absorptive capacity] as [R&D intensity / patent citations / knowledge stock measure]. We interact [digital transformation] with [absorptive capacity] to test whether [the effect of digital transformation on innovation performance] is stronger when [absorptive capacity] is high.

We include controls for [firm resources and baseline heterogeneity] because [larger and older firms may have more resources for both digital transformation and innovation]. At the [firm] level, we control for [firm size (ln total assets), firm age, profitability (ROA), leverage (total debt / total assets), and industry competition (Herfindahl-Hirschman Index)]. We also include [firm and year fixed effects] to absorb [time-invariant unobserved firm characteristics and common macroeconomic shocks]. All time-varying predictors are measured at [t–1] to preserve temporal ordering.

Because [firm innovation performance] is [continuous], we estimate [fixed-effects panel regression models]. The specification includes [firm and year fixed effects] to absorb [unobserved heterogeneity and common shocks]. Standard errors are clustered at the [firm] level to account for [serial correlation within firms over time]. We employ firm fixed effects rather than random effects because the Hausman test rejects the random-effects assumption (χ² = [value], p < 0.01). We conduct several diagnostic tests. First, the Variance Inflation Factor (VIF) for all independent variables is below [value], well below the conventional threshold of 10. Second, the Wooldridge test rejects autocorrelation in the residuals (F = [value], p = [value]).

To address concerns about [reverse causality], we lag [digital transformation intensity] by [one year] and re-estimate our models. This check assesses whether [simultaneity] is a plausible threat. We report the results in [the robustness section of the Results].

The Results section first reports [the main hypothesis tests in Table 2] and then examines [robustness checks in Table 3]. Because [our models involve panel data with fixed effects], we address [remaining endogeneity concerns] in supplemental analyses using [instrumental variables].
```

---

### ---metadata--- 区块（供下游 Skill 消费）

每次生成 Methods 骨架后，必须在输出末尾附加可解析的 JSON 元数据块，封装本 Methods 的"设计 DNA"和变量指纹，供 `/write-results`、`/paper-review`、`/distill-methods-exemplar` 直接消费。

```json
---metadata---
{
  "skill_version": "3.0.0",
  "model_type": "面板数据/OLS",
  "design_variant": "标准",
  "journal_target": "SMJ",
  "slot_map": {
    "M1": { "present": true, "variant": "通用", "word_count_estimate": 80 },
    "M2": { "present": true, "variant": "通用", "word_count_estimate": 120 },
    "M3": { "present": true, "variant": "通用", "dependent_variable": "firm innovation performance" },
    "M4": { "present": true, "variant": "通用", "focal_predictors": ["digital transformation intensity"] },
    "M5": { "present": true, "variant": "通用", "moderator_mediator": ["absorptive capacity"] },
    "M6": { "present": true, "variant": "通用", "control_count": 5 },
    "M7": { "present": true, "variant": "通用", "estimator": "fixed-effects panel regression", "fixed_effects": ["firm", "year"], "se_clustering": "firm" },
    "M8": { "present": false, "reason": "OLS/FE design does not require formal identification strategy beyond fixed effects" },
    "M9": { "present": false, "reason": "single-study design" },
    "M10": { "present": true, "variant": "通用" }
  },
  "hypothesis_variable_mapping": [
    { "hypothesis": "H1", "iv": "digital transformation intensity", "dv": "organizational routine updating", "variable_slots": ["M4", "M3"] },
    { "hypothesis": "H2", "iv": "organizational routine updating", "dv": "firm innovation performance", "variable_slots": ["M4", "M3"] },
    { "hypothesis": "H3", "iv": "digital transformation intensity", "moderator": "absorptive capacity", "dv": "firm innovation performance", "variable_slots": ["M4", "M5", "M3"] }
  ],
  "identification_claims": {
    "has_iv": false,
    "has_did": false,
    "has_matching": false,
    "has_experiment": false,
    "causal_language_permitted": "associated with"
  },
  "robustness_menu": {
    "model_selection": ["random effects", "Tobit"],
    "measure_sensitivity": ["alternative innovation measure"],
    "sample_selection": [],
    "reverse_causality": ["lag structure t-1"],
    "alternative_explanations": [],
    "outliers": [],
    "clustering": []
  },
  "cross_section_alignment": {
    "introduction_preview_match": { "status": "pending", "notes": "需用户确认 I6 Preview 承诺" },
    "theory_hypothesis_match": { "status": "pending", "notes": "需用户提供 Theory 假设列表" }
  },
  "dna_metrics": {
    "because_density_target": ">=40%",
    "hypothesis_alignment_density_target": ">=85%",
    "causal_language_strength": "low (OLS/FE)",
    "diagnostic_frontloading_target": ">=30%",
    "sample_audit_chain_target": "100%",
    "timing_clarity_target": ">=85%"
  },
  "downstream_interfaces": ["/write-results", "/paper-review", "/distill-methods-exemplar"],
  "feedback_interface": {
    "validation_skill": "/distill-methods-exemplar",
    "validation_mode": "--validate",
    "required_inputs": ["用户写出的 Methods 全文", "本 metadata JSON"],
    "validation_focus": ["槽位覆盖", "因果语言合规", "样本漏斗完整性", "识别策略充分性"],
    "trigger_timing": "用户完成 Methods 初稿后"
  }
}
```

**字段说明**：
- `slot_map`: M1-M10 每个槽位的生成状态、变体类型和估计字数
- `hypothesis_variable_mapping`: 假设与 Methods 变量槽位的映射，供 write-results 构建假设-结果对齐表
- `identification_claims`: 识别策略类型和允许的因果语言强度，供 write-results 和 paper-review 检查 causal language 合规性
- `robustness_menu`: 生成的稳健性检验菜单，供 write-results 的 R7 直接消费
- `cross_section_alignment`: 与上游 skill 的对齐状态（生成时为 pending，用户填入后更新）
- `feedback_interface`: 写作-反馈闭环接口，提示用户完成 Methods 后回传验证

---

## 下一步：回传验证（写作-反馈闭环）

完成 Methods 初稿后，请使用以下命令进行成品验证：

```
/distill-methods-exemplar --validate
[粘贴你写出的 Methods 全文]

--reference-metadata
[粘贴上方的 ---metadata--- JSON 区块]
```

验证将检查：槽位覆盖完整性、因果语言合规性、样本漏斗数字审计、识别策略充分性、与 Introduction/Theory 的 cross-section 对齐。

---

## 下游接口

- `/write-results` — 使用本骨架的变量名、模型规格和 M10 预告作为 Results 报告的基准
- `/paper-review` — 进行 Theory-Methods 假设-变量映射对齐检查
- `/methods-review` — 如用户已有 Methods 草稿，使用本骨架作为理想基准对比审查
- `/distill-methods-exemplar` — 两层接口：(1) Phase 4 `corpus_enrichment` YAML 块 → Phase 4.5 → `_evidence_registry.yaml`（自动更新定量证据）；(2) Phase 6 `--validate` 成品验证模式接收本 skill 的 metadata JSON 作为参考基准，输出四维评分和修正建议。用户完成 Methods 初稿后，使用 `/distill-methods-exemplar --validate <Methods全文> --reference-metadata <本skill输出的---metadata--- JSON>` 进行验证

### Cross-Section 对齐检查（与上游 Skill 的接口）

本 Skill 的输出必须与上游 Skill 的承诺严格对齐。生成骨架后，执行以下对齐检查：

#### 对齐检查 1：Introduction ↔ Methods（I6 Preview ↔ M7/M8）

| Introduction 承诺（I6 Preview） | Methods 兑现（M7/M8） | 检查问题 | 失败信号 |
|-------------------------------|---------------------|---------|---------|
| "Drawing on... we argue that..." | M7 的 estimator 和 model specification | Theory 承诺的机制是否在模型中被正确设定？ | M7 缺少 mediator 方程或交互项 |
| "Using [data] and [methods]" | M2 数据来源 + M7 估计方法 | 数据和方法是否与 Preview 一致？ | 数据来源或估计方法与 Preview 不符 |
| "We account for [identification concern]" | M8 识别策略 / 效度检验 | Preview 中提到的识别关切是否在 M8 中被处理？ | M8 缺失 Preview 承诺的检验 |

#### 对齐检查 2：Theory ↔ Methods（假设列表 ↔ M3-M6 变量操作化）

| Theory 假设 | Methods 变量 | 检查问题 | 失败信号 |
|------------|-------------|---------|---------|
| H1: [IV] → [DV] | M4 自变量 + M3 因变量 | IV 和 DV 的操作化是否与假设中的构念一致？ | 构念名与变量名不一致 |
| H2: [Mediator] 中介 | M5 中介变量 | 中介变量是否被正确测量和纳入模型？ | M5 缺失中介变量或测量方式不符 |
| H3: [Moderator] 调节 | M5 调节变量 + M7 交互项 | 调节变量是否被操作化并在模型中体现为交互项？ | M7 缺少交互项或 M5 缺少调节变量 |
| 控制逻辑 | M6 控制变量 | 每个控制变量是否对应 Theory 中的竞争性解释？ | M6 出现与 Theory 无关的控制变量 |

**对齐偏离记录格式**：

```markdown
### Cross-Section 对齐偏离记录

| 偏离ID | 上游承诺 | 本段实际内容 | 偏离类型 | 严重程度 | 修正建议 |
|--------|---------|------------|---------|---------|---------|
| D1 | I6 Preview: "We use IV to address endogeneity" | M7 使用 OLS/FE，未提及 IV | 识别策略缺失 | 高 | 在 M7 中添加 2SLS 或在 I6 中删除 IV 承诺 |
| D2 | Theory H2: Mediation via routine updating | M5 未包含 routine updating 变量 | 机制变量缺失 | 高 | 补充 M5 中介变量段 |
```

---

## Robustness Check Menu

All top-journal papers now treat robustness as a systematic expectation rather than an afterthought. For every primary estimator, consider reporting robustness to the following categories:

- [ ] **Model selection**: Alternative functional forms, distributions, or estimators (e.g., Weibull/Gompertz for hazard models; GEE for panel logit; LPM+2SLS for binary IV)
- [ ] **Measure sensitivity**: Alternative operationalizations, cutoffs, percentile thresholds, or transformations (e.g., top/bottom 20%, 30%, 40% vs. quartile; raw count vs. relative percentage)
- [ ] **Sample selection**: Matching (CEM, PSM), weighting, subsample analysis, or attrition comparison
- [ ] **Reverse causality**: Lag structures (t-1, t-2), Granger causality, lead-lag tests, or control-function approach
- [ ] **Alternative explanations**: Mechanism vs. confound via interactions, auxiliary models, or placebo tests
- [ ] **Outliers and influential observations**: With and without top/bottom 1% or Cook's distance thresholds
- [ ] **Clustering and SE sensitivity**: Alternative clustering levels, wild bootstrap, or spatial HAC

**骨架段落**（可插入 M8 或 Results 预告段）：
```text
To ensure that our findings are not driven by [specific modeling choice / measure definition / sample composition], we conduct a series of robustness checks. First, we re-estimate our models using [alternative estimator / distribution] and find that [key results] remain [status]. Second, we test alternative operationalizations of [construct] using [alternative measure / cutoff] and obtain [consistent / qualitatively similar] results. Third, we address potential selection concerns by [matching / weighting / subsample analysis] and confirm that [focal effect] is robust. Fourth, to mitigate reverse causality concerns, we [lag structure / control function / lead-lag test] and find [result]. Finally, we rule out [alternative explanation] by [test design]; the [null / nonsignificant] result supports our preferred interpretation.
```

---

## 常见反模式

以下错误在 Methods 中高频出现，生成段落前主动排查：

- **模型选择无文字解释**：只写 "we estimate FE model" 而不解释为什么 FE 优于 RE/OLS，或为什么选此 estimator
- **控制变量无 because**：列出 Size, Age, ROA 但不解释每个变量控制的是什么竞争性解释
- **因果语言越级**：面板数据 design 下使用 "caused" "led to" 等强因果词；自然实验未通过平行趋势检验就用 "effect of... on..."
- **样本漏斗缺数字**：写 "we exclude missing values" 但不报告每一步损失了多少观测
- **识别策略后置或缺失**：DiD/IV/自然实验不把识别假设和检验放在核心位置，而是 buried 在脚注或附录
- **交互/非线性模型无解释策略**：加入 interaction/nonlinear term 后未预告如何在 Results 中解释（marginal effects / simple slopes / AME）
- **时间顺序模糊**：未明确说明预测变量是 t-1 还是 contemporaneous，或事件窗口的起止逻辑
- **Bad Control 问题**：在 DiD/自然实验中控制了 post-treatment 变量或 collider
- **设计排他性混淆**：把 IV 的语言习惯（"effect of X on Y"）套用到 OLS/FE 设计；把实验的操纵检验语言套用到档案数据
- **动态面板 FE 陷阱**：为短面板推荐固定效应而不提示 Nickell bias 或提供 GMM 替代方案
- **过度泛化诊断要求**：为非 IV 设计要求排他性约束检验，为非 DiD 设计要求平行趋势检验，为非匹配设计要求重叠支撑检验
- **机构/政策名残留**：用户填入的 [placeholder] 中混入了论文特有的机构名、政策名、数据库名，导致段落不可迁移到其他情境

## 诚实边界

本 skill 基于 32 篇 MVP30 范文语料库（2010–2025）提炼，存在以下局限：

1. **不能替代统计诊断**：提供段落骨架和 ritual 规范，但不能判断您的数据是否满足模型假设（平行趋势、工具变量相关性、共同支撑域、VIF、序列相关等）。这些必须基于实际数据。
2. **不能消除期刊差异**：SMJ/AMJ/ASQ/JM/OS/JOM/ASR 对 Methods 的 ritual 偏好不同。本 skill 以"最大公约数"为主，投稿前需对照目标期刊最新范文调整。
3. **不能生成真实统计量**：所有 [placeholder] 中的系数、p 值、F 统计量、样本量、VIF 值必须由用户根据实际估计结果填入。本 skill 不虚构任何数字。
4. **语料库领域偏差**：范文主要来自战略管理、营销、组织行为。金融、会计、运筹、宏观等领域的 ritual 可能不同。
5. **不能覆盖最新方法论**：语料库截止于 2025 年，更新的估计量或识别策略可能未覆盖。
6. **设计排他性不可违反**：不能为不需要某诊断的设计强制插入该诊断。例如：非 IV 设计不得要求排他性约束检验；非 DiD 设计不得要求平行趋势检验；非匹配设计不得要求重叠支撑检验。
7. **动态面板必须提示 Nickell bias**：当面板时间维度较短（T < 10）且因变量具有持续性时，不能推荐固定效应而不提示 Nickell bias 或提供系统 GMM / 差分 GMM 替代方案。
8. **不得泛化特殊设计的 causal 语言**：OLS/FE 的骨架必须使用 "associated with"；自然实验在平行趋势/事件研究支持后才可使用 "effect of... on..."；实验设计可使用 "caused"。不得让面板数据 design 的段落中出现 "leads to" 或 "causes"。

## 生成后自检清单

生成 Methods 段落后，逐条核对：

### Completeness
- [ ] M1：研究情境有至少 3 个理由，且与理论机制直接挂钩
- [ ] M2：样本漏斗包含起始总体 → 每步排除（理由+数字）→ 最终 N
- [ ] M3：因变量有构念定义 + 操作化 + 测量来源 + 方向解释
- [ ] M4：每假设一段，含 Hypothesis 编号对齐，变量按理论顺序排列
- [ ] M5：调节/中介/机制变量有操作化和交互项说明
- [ ] M6：每个控制变量都有 because [rival explanation]
- [ ] M7：estimator + fixed effects + SE clustering + 选择理由（文字+诊断）
- [ ] M8：关键识别假设 + 检验方法 + 结果位置
- [ ] M10：Results 预告（表格顺序、特殊解释需求、识别检验位置）

### Clarity
- [ ] 变量名与 Results 表格完全一致
- [ ] 时间顺序明确（滞后几期、事件窗口、观测期起止）
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号

### Credibility
- [ ] 识别假设有检验（平行趋势/过度识别/manipulation check）
- [ ] 样本漏斗可审计（每步有数字和排除理由）
- [ ] 模型选择有文字解释，不埋在方程里
- [ ] 非显著假设在 Methods 中未预告支持状态

### DNA Metrics（与顶刊范本的 rhetorical 距离）
- [ ] **Because 密度**：M6 中每个控制变量都有 "because [rival explanation]" 或等效逻辑（目标：>=40%；MVP30 顶刊中位数约 35%，AMJ 可低至 0%，JM/ASQ 约 25-30%）
- [ ] **假设对齐密度**：M4/M5 中每预测变量都明确提及对应的 Hypothesis 编号（目标：>=85%；MVP30 中位数约 80%）
- [ ] **因果语言强度**：面板数据用 "associated with"；自然实验在识别支持后用 "effect of... on..."；实验可用 "caused"。无越级。
- [ ] **诊断检验前置比例**：IV/DiD/实验 目标 ≥80%（平行趋势/操纵检验/F-statistic 必须在 Methods 预告）；OLS/FE 目标 ≥30%（VIF/Hausman 可省略或脚注处理）
- [ ] **样本数字审计链**：M2 中起始 N → 每步排除（含数字）→ 最终 N 完整无缺（目标：100%）
- [ ] **时点标记密度**：所有预测变量明确标注 t-1 / contemporaneous / event window；所有时间范围有起止年份（目标：>=85%；MVP30 中位数约 85%）
- [ ] **功能定位密度**：每段首句说明本段做什么（如 "We include controls for..." / "To address concerns about..."）（目标：≥70%）

### 写作-反馈闭环（成品验证）

完成 Methods 初稿后，使用 `/distill-methods-exemplar --validate` 进行成品验证：

```
/distill-methods-exemplar --validate
[粘贴你写出的 Methods 全文]

--reference-metadata
[粘贴上方的 ---metadata--- JSON 区块]
```

验证将执行四维检查：

| 维度 | 检查内容 | 输出 |
|------|---------|------|
| **组装方案兑现** | 槽位是否按推荐变体覆盖？设计变体是否与设计类型兼容？ | 偏离矩阵 + 严重度评级 |
| **槽位完整性** | M1-M10 每个槽位的 Completeness/Clarity/Credibility | 逐槽位 0-3 评分卡 |
| **因果语言合规** | 每句因果动词是否与设计强度匹配？ | 违规清单 + 建议替换词 |
| **骨架生成力** | 骨架关键短语是否保留？说服动作是否被填充后的段落保持？ | VALIDATED/REVISE/REJECT 评级 |

验证报告包含优先修正清单，按审稿人攻击概率排序。详见 `distill-methods-exemplar` Phase 6。

## Constraints

- 必须提醒用户：替换所有 `[方括号占位符]` 为实际内容；不虚构样本量、来源、变量定义或诊断结果。
- 变量名必须与 Results 表格完全一致。
- 每个控制变量必须有明确的控制逻辑（已在段落骨架中内置 "because [rival explanation]" 槽位）。
- 样本漏斗必须包含每一步的数字和理由（已在 M2 骨架中内置）。
- 因果语言强度必须与 design strength 匹配。以下是按设计家族的强制词汇表：

| 设计家族 | 允许动词 | 禁止动词 | 使用条件 |
|---------|---------|---------|---------|
| 面板数据/OLS/FE/HLM | associated with, related to, linked to, corresponds to | increases, decreases, leads to, causes, drives, produces | 无条件禁止强因果词 |
| DiD / 自然实验 | effect of ... on ..., associated with | causes, leads to, drives | 仅在平行趋势/事件研究支持后可用 "effect of... on..."；否则退回 "associated with" |
| IV/2SLS | effect of ... on ..., increases, decreases | causes, leads to, produces | 仅在 M8 识别假设 preview 后可用；second-stage 汇报可用 "effect" 但避免 "causes" |
| 非线性模型 (Logit/Probit/Tobit/计数) | associated with, increases the likelihood of, changes the probability of | increases, decreases, causes, leads to | 系数本身不可直接解释；必须通过边际效应/概率变化转述 |
| 生存分析 | associated with, lengthens/shortens time to, changes the hazard of | causes, leads to, produces | hazard ratio / AFT 系数需通过生存概率或时间变化转述 |
| SEM / 同时方程 | associated with, predicts, influences | causes, leads to, produces | 结构方程系数表示预测关系，非因果；仅在过度识别且模型拟合良好时可谨慎使用 "effect" |
| 实验 | caused, led to, produced, increased, decreased | — | 随机化支持后可直接使用强因果词 |

- 不要报告支持状态在 Methods 中。
- 不要把模型选择埋在方程里而没有文字解释。

## 外部资产位置

如需查询特定范文的具体措辞或设计变体：

- **叙事分析索引**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/_mvp30_methods_results_index.md`
- **28篇覆盖矩阵**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/deep_distillation/_methods_results_28_paper_coverage_matrix.md`
- **逐论文精细解构**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/batch_*/[paper]_fine_methods_results.md`
- **Pollock Ch07 表达库**: `D:/OneDrive/Obsidian Vault/00 工作台/叙述模板训练集/narrative_analysis/methods_results/mvp30/fine_grained/_four_paper_expression_corpus_pollock_ch07.md`

## 语料库维护接口

如需为特定设计类型补充新变体或更新主骨架：

1. **distill 产出沉淀**：使用 `/distill-methods-exemplar` 分析新论文，Phase 4 验证通过的变体写入 `academic-writing-corpus/[设计类型].md` 的「累积变体」区块。
2. **语料库索引更新**：修改 `academic-writing-corpus/INDEX.md` 中的变体数和最后更新日期。
3. **证据注册表更新**：运行 `academic-writing-corpus/_update_registry.py` 合并 `corpus_enrichment` YAML 块。
4. **即时生效**：write-methods 下次调用时自动读取更新后的分片文件，无需重启或修改 SKILL.md。

---
*基于 32 篇 MVP30 范文语料库、Pollock 2025 Ch07 和深度叙事分析框架构建。版本 3.0.0 — 外置语料库按需加载。*