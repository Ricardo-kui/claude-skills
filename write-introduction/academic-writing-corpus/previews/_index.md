---
type: canonical_reference
canonical_id: "previews-index"
status: ✓ STANDARD
gap_type: all
cross_paper: VERIFIED
generativity: ADAPTABLE
exclusivity: LOW
source_papers:
  - zhou2017 (ASQ, 2017): Mechanism preview with theory lens
  - eilert2017 (JM, 2017): Findings preview with economic significance
  - gamache2023 (SMJ, 2023): Findings preview with counter-examples
  - keeves2017 (ASQ, 2017): Mechanism chain preview
  - ceo_regulatory_focus_ijrm (IJRM, 2021): Findings preview with effect size
  - darby2024 (MSOM, 2024): Two-layer causal chain preview
  - darby2023 (MSOM, 2023): Split dual-preview for dual-gap papers
  - darby2026 (JOM, 2026): Robustness-heavy preview
  - pfarrer2010 (AMJ, 2010): DV methodology defense preview
created: 2026-05-18
updated: 2026-05-19
source: Extracted from MVP30 narrative_analysis files
---

# Previews 索引

P5-P6 的功能：在理论框架建立之后，向读者预告"我们做了什么、发现了什么"。这是 Introduction 中的"承诺"段落——读者由此判断是否值得继续读下去。

## 文件清单

| 文件 | 内容 | 适用场景 |
|------|------|---------|
| [mechanism-preview.md](mechanism-preview.md) | 变体 A-C：理论整合型、分层机制型、挑战性预测型 | 需要预告核心理论逻辑的研究 |
| [findings-preview.md](findings-preview.md) | 变体 D-G, N：经济显著性型、反例驱动型、两层因果链型、调节效应预览型、分体式双预览型 | 需要预告实证结果的研究 |
| [robustness-preview.md](robustness-preview.md) | 变体 H：稳健性密集预览型 + 紧凑版 | 方法复杂、检验繁多的实证论文 |
| [extreme-case-justification.md](extreme-case-justification.md) | 变体 J：极端案例+混合方法辩护型 | 使用极端案例和多方法设计的研究 |
| [dv-methodology-defense.md](dv-methodology-defense.md) | 变体 I：DV 方法论辩护型（正负不对称性） | DV 有天然双情境的研究 |

## 组装规则

### 必须配对
- 机制预览 → Theory 段之后，发现预览之前
- 发现预览 → 必须有实证数据支撑，不能空承诺
- 两段必须语义连接：机制预览解释"为什么"，发现预览展示"我们找到了什么证据"

### 反模式提醒
- **不要在发现预览中列举所有假设**: Preview 是选择性预告，不是假设列表
- **不要把机制预览写成理论综述**: 2-3 句核心逻辑即可
- **不要只说 "we find support for our hypotheses"**: 必须说方向、大小、或意外发现
- **经济显著性必须有基线对比**: 不能说 "effect is large" 而不说 "large relative to what"

---

## 槽位填充正误对比

### `[empirical setting]` — 情境 justify

❌ "We test our theory using panel data of Chinese listed firms from 2005 to 2018." → 只描述数据不解释为什么这个情境是检验理论的好地方

✅ "We test our theory in China's post-WTO accession period (2005-2018), when government subsidies to politically connected firms increased by 340% — creating ideal conditions to observe the tension between resource acquisition and allocation efficiency." → 情境（post-WTO China）+ 为什么适合（340% subsidy increase creates variation）+ 理论锚定（tension between acquisition and allocation）

### `[finding direction]` — 发现预览

❌ "We find support for H1 (β=0.34, p<.01), H2 (β=-0.21, p<.05), H3..." → 预告所有假设 + 报告精确系数。Introduction 不是 Results

✅ "We find that political connections reduce innovation through diminished allocation efficiency, and that this effect is strongest when external governance is weak." → 核心发现的方向性预览，不给系数，细项留给 Results
