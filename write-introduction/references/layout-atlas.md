# Introduction 布局图谱

## 布局类型总览

| 布局类型 | 段落数 | 适用组合 | 核心特征 | 典型范文 |
|---------|--------|---------|---------|---------|
| **标准型（Standard）** | 6–7段 | 大多数组合 | Hook→Literature→Gap→Stakes/Theory→Preview→Contribution | Wu 2025, Han 2020 |
| **扩展型（Extended）** | 8–9段 | Incommensurability+Mechanism, Inadequacy+Phenomenon | 增加独立 Stakes 段、Epigraph Hook、多理论对话 | Zhou 2017, DesJardine 2023 |
| **紧凑型（Compact）** | 5段 | Incompleteness+Mechanism/Boundary | 直接切入，减少背景铺垫，Hook 与 Literature 合并 | Eilert 2017 |

---

## 通用段落功能定义

无论哪种布局类型，Introduction 的段落功能遵循以下层级：

| 段落 | 功能标签 | 核心任务 | 字数 | 模块来源 |
|------|---------|---------|------|---------|
| **P1** | Hook | 建立读者注意力，设定 stakes | 40–100 | `hooks/` |
| **P2** | Literature Turn | 建立学术对话，展示已有知识 | 40–100 | Conversation 策略 + `transitions/hook-to-literature` |
| **P3** | Gap | 刺破共识，精确定位缺口 | 40–80 | `tensions/` + `transitions/literature-to-gap` |
| **P4** | Stakes / Theory Lens | 解释缺口重要性，或引入理论视角 | 60–100 | `stakes/` 或内部模板 |
| **P5** | Preview | 预览机制、策略或发现 | 60–140 | 内部模板（论文特异性强） |
| **P6–P7** | Contribution | Makadok 声明 + 对话定位 | 70–110 each | `makadok-frames.md` + `transitions/gap-to-contribution` |
| **P8**（扩展型） | Identification / Roadmap | 识别策略或文章结构预告 | 40–80 | 内部模板 |

### 布局变体规则

**何时选用扩展型**：
- Gap = Incommensurability（需要更多空间建立颠覆性论证）
- Contribution = Phenomenon（需要更多背景建立新现象域）
- 涉及多理论对话（如 Zhou 2017 的效率逻辑 vs 制度逻辑）
- 使用 Epigraph Hook（需要独立段落承载引语）

**何时选用紧凑型**：
- Gap = Incompleteness（低强度 Gap 不需要戏剧化铺垫）
- 领域已高度成熟（读者不需要大量背景）
- 期刊偏好简洁（如 SMJ 的 Introduction 通常比 ASQ 短）

---

## 组合特定布局

### Combo 1: Incompleteness + Mechanism

> **代表范文**: Wu 2025（OrgSci）
> **叙事张力**: Progressive omission
> **默认布局**: 紧凑型（5段）或标准型（6段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Background / cold-start definition | 50–90 | ✅ | `03-data-shock` 或 `13-domain-gap` |
| P2 | Literature review（Progressive Coherence）→ mechanism gap | 40–80 | ✅ | `01-despite-progress-unaddressed` + `transitions/literature-to-gap` |
| P3 | Theoretical lens introduction | 60–100 | ✅ | 内部模板（Drawing on...） |
| P4 | Mechanism preview + identification strategy | 80–140 | ⚠️ | 内部模板 |
| P5 | Findings preview | 60–90 | ✅ | 内部模板 |
| P6–P7 | Contribution statements（文献推进 + 机制识别） | 70–110 each | ✅ | Makadok Mechanism |

**布局变体**:
- **紧凑型**: P1 与 P2 合并为 "Background + Progressive Coherence" 一段
- **扩展型**: 在 P3 前增加独立 Stakes 段（`02-quantified-economic-loss`）

**风险提醒**: 必须解释"为什么这个机制的缺失是理论上重要的 omission"，而不能只说"few studies have examined"。

---

### Combo 2: Incompleteness + Boundary

> **代表范文**: Eilert 2017（JM）
> **叙事张力**: Progressive omission
> **默认布局**: 紧凑型（5–6段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Data/statistics hook | 50–80 | ✅ | `03-data-shock` 或 `14-cost-benefit-tension` |
| P2 | Literature review → boundary condition gap | 40–80 | ✅ | `01-despite-progress-unaddressed` |
| P3 | Theoretical argument（core relationship + boundary logic） | 60–100 | ✅ | 内部模板 |
| P4 | Findings preview | 60–90 | ✅ | 内部模板 |
| P5–P6 | Contribution statements（behavior + performance） | 70–110 each | ✅ | Makadok Boundary |

**布局变体**:
- **标准型**: 增加独立 P3 "Mechanism preview"

---

### Combo 3: Inadequacy + Constructs

> **代表范文**: Pollock 2015（ASQ）; Han 2024（SMJ）
> **叙事张力**: Perspective blind spot
> **默认布局**: 标准型（6段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Interdisciplinary analogy / contrast case hook | 60–100 | ✅ | `01-cross-disciplinary-analogy` 或 `12-surprising-fact` |
| P2 | Construct conflation identified | 70–100 | ✅ | `03-structural-blindspot` 或 `05-overlooked-alternative` |
| P3 | Construct definition + systematic differences | 60–90 | ✅ | 内部模板（构念界定） |
| P4 | Theoretical argument（difference-based mechanism） | 70–120 | ✅ | 内部模板 |
| P5 | Findings preview | 60–90 | ✅ | 内部模板 |
| P6 | Contribution statement（construct refinement） | 70–110 | ✅ | Makadok Constructs |

**布局变体**:
- **扩展型**: 在 P2 后增加独立段 "Construct history and disciplinary divergence"（展示构念混淆的学科根源）

**风险提醒**: 必须展示两个构念的"系统差异"，不能只罗列定义。

---

### Combo 4: Inadequacy + Mechanism

> **代表范文**: Keeves 2017（ASQ）; Paruchuri 2020（SMJ）
> **叙事张力**: Perspective blind spot
> **默认布局**: 标准型（6段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Background / consensus establishment | 60–100 | ✅ | `05-literature-consensus-blindspot` |
| P2 | Literature one-sidedness identified | 60–100 | ✅ | `02-implicit-assumption-wrong` 或 `06-forward-vs-backward-looking` |
| P3 | New mechanism introduction | 70–120 | ✅ | 内部模板（对立力量/情境反转） |
| P4 | Hypothesis preview | 50–70 | ✅ | 内部模板 |
| P5 | Findings preview | 60–90 | ✅ | 内部模板 |
| P6 | Contribution statement（perspective innovation） | 70–110 | ✅ | Makadok Mechanism |

**关键模块组合**:
- P1 Hook 必须配对 P2 Tension：`05-literature-consensus-blindspot` → `02-implicit-assumption-wrong`
- P3 可接入 `../academic-writing-corpus/mechanisms/opposing-forces.md` 或 `context-reversal.md`

---

### Combo 5: Inadequacy + Boundary

> **代表范文**: Han 2020（AMJ）
> **叙事张力**: Perspective blind spot
> **默认布局**: 标准型（5段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Consensus + core gap | 60–100 | ✅ | `05-literature-consensus-blindspot` |
| P2 | Decontextualization critique | 60–100 | ✅ | `03-structural-blindspot` |
| P3 | Theoretical solution preview（boundary condition） | 70–120 | ✅ | 内部模板 |
| P4 | Empirical setting + findings preview | 60–100 | ✅ | 内部模板 |
| P5 | Contribution statement（importance of contextual factors） | 70–110 | ✅ | Makadok Boundary |

**风险提醒**: 必须说明"去情境化"为什么 problematic，不能只说"context matters"。

---

### Combo 6: Inadequacy + Phenomenon

> **代表范文**: DesJardine 2023（SMJ）
> **叙事张力**: Perspective blind spot
> **默认布局**: 扩展型（8–9段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Epigraph hook / trend hook | 40–70 | ✅ | `08-quotation-hook` 或 `17-phenomenon-market-evolution` |
| P2 | Macro trend + background | 60–90 | ✅ | `09-evolving-social-issue` |
| P3 | Core contradiction / problematization | 60–100 | ✅ | `08-cost-vs-benefit` 或 `10-constraint-vs-freedom` |
| P4 | Research question formally posed | 30–50 | ✅ | 内部模板 |
| P5 | Literature gap positioning | 50–80 | ✅ | `01-despite-progress-unaddressed` |
| P6 | Theoretical argument（core claim） | 70–110 | ✅ | 内部模板 |
| P7 | Mechanism elaboration + empirical preview | 60–100 | ✅ | 内部模板 |
| P8–P9 | Contribution statements（2–3个） | 60–90 each | ✅ | Makadok Phenomenon + Makadok Mechanism |

**布局特征**: 这是段落数最多的布局类型，因为新现象域需要大量背景铺垫。

---

### Combo 7: Incommensurability + Constructs

> **代表范文**: Pontikes 2012（ASQ）
> **叙事张力**: Consensus overturn
> **默认布局**: 标准型（6段）或扩展型（7段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Literature consensus establishment | 60–100 | ✅ | `06-paradigm-challenge` |
| P2 | Counterexample / contradiction identified | 70–100 | ✅ | `04-reality-contradicts-consensus` |
| P3 | Theoretical solution（construct reconstruction） | 70–120 | ✅ | 内部模板 |
| P4 | Construct definition + new role | 60–90 | ✅ | 内部模板 |
| P5 | Findings preview | 60–90 | ✅ | 内部模板 |
| P6 | Contribution statement（construct reconstruction） | 70–110 | ✅ | Makadok Constructs |

**关键模块组合**:
- P1 Hook 必须配对 P2 Tension：`06-paradigm-challenge` → `04-reality-contradicts-consensus`
- 这是**高能量组合**：P1 和 P2 的颠覆性必须足够强，否则后文的 construct reconstruction 会显得无力

**风险提醒**: 共识必须是真实的，有充分文献支撑；挑战必须锚定在证据上，不能树立稻草人。

---

### Combo 8: Incommensurability + Mechanism

> **代表范文**: Zhou 2017（ASQ）
> **叙事张力**: Consensus overturn
> **默认布局**: 扩展型（8段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Consensus / interdisciplinary analogy / classic debate | 60–100 | ✅ | `06-paradigm-challenge` 或 `15-classic-debate-constraint` |
| P2 | Counterexample / contradiction identified | 70–100 | ✅ | `04-reality-contradicts-consensus` |
| P3 | Theoretical reframing | 60–90 | ✅ | 内部模板（制度逻辑引入） |
| P4 | Opposing predictions / new mechanism | 70–120 | ✅ | 内部模板（对立力量机制） |
| P5 | [Optional] Identification strategy | 50–80 | ⚠️ | 内部模板 |
| P6 | Findings preview | 60–90 | ✅ | 内部模板 |
| P7–P8 | Contribution statements（conversation join + perspective innovation） | 70–110 each | ✅ | Makadok Mechanism |

**关键模块组合**:
- P4 可接入 `../academic-writing-corpus/mechanisms/opposing-forces.md`
- 这是 Incommensurability 类论文中最常见的布局

---

### Combo 9: Incommensurability + Boundary

> **代表范文**: Zhou 2017（ASQ）; Park 2025
> **叙事张力**: Consensus overturn
> **默认布局**: 扩展型（7–8段）

**段落地图**:

同 Combo 8（Incommensurability + Mechanism），但在 P4 强调**边界条件如何调和/修正两个对立理论的适用范围**。

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Consensus / classic debate | 60–100 | ✅ | `06-paradigm-challenge` |
| P2 | Contradiction | 70–100 | ✅ | `04-reality-contradicts-consensus` |
| P3 | Theoretical reframing | 60–90 | ✅ | 内部模板 |
| P4 | Boundary condition as reconciliation | 70–120 | ✅ | 内部模板（边界逻辑） |
| P5 | Findings preview | 60–90 | ✅ | 内部模板 |
| P6–P7 | Contribution statements | 70–110 each | ✅ | Makadok Boundary |

**核心句式**: "We suggest that the disagreement between [Theory A] and [Theory B] can be reconciled by identifying [context] as a key boundary condition."

---

### Combo 10: Incommensurability + Level

> **代表范文**: Keeves 2017（ASQ）
> **叙事张力**: Consensus overturn
> **默认布局**: 扩展型（7段）

**段落地图**:

| 段落 | 功能 | 词数 | 必须度 | 推荐模块 |
|------|------|------|--------|---------|
| P1 | Background（function → means） | 60–100 | ✅ | `19-forward-looking-shift` 或 `01-cross-disciplinary-analogy` |
| P2 | One-directional effect gap（asymmetric relationship） | 60–100 | ✅ | `02-implicit-assumption-wrong` |
| P3 | Theoretical core（paradox） | 70–120 | ✅ | 内部模板 |
| P4 | Boundary condition | 60–100 | ⚠️ | 内部模板 |
| P5 | Cross-level consequence mechanism | 70–110 | ✅ | 内部模板 |
| P6 | Contribution statement（three dimensions） | 70–110 | ✅ | Makadok Level + Makadok Mechanism |

**布局特征**: 跨层次论文的 Introduction 需要同时在多个分析层次建立张力，P1 和 P2 通常分别对应不同层次。

---

## 布局选择决策树

```
输入: Gap类型 + 贡献维度
│
├─ Gap = Incommensurability?
│   ├─ YES → 默认扩展型（7-9段）
│   │   ├─ Contribution = Phenomenon/Mechanism/Boundary → 8-9段
│   │   └─ Contribution = Constructs/Level/Question → 7段
│   └─ NO → 继续判断
│
├─ Contribution = Phenomenon?
│   ├─ YES → 默认扩展型（8-9段）
│   └─ NO → 继续判断
│
├─ Gap = Incompleteness AND Contribution = Mechanism/Boundary?
│   ├─ YES → 默认紧凑型（5-6段）
│   └─ NO → 标准型（6-7段）
```

---

## 期刊偏好与布局调整

| 期刊 | 偏好布局 | 调整建议 |
|------|---------|---------|
| **ASQ** | 扩展型 | 允许更多理论铺垫；P1 可用引语 Hook；P3-P4 可详细展开理论对话 |
| **SMJ** | 紧凑型/标准型 | 偏好快速切入；Hook 不超过2句；Contribution 段控制在2段以内 |
| **AMJ** | 标准型 | 重视微观-宏观桥接；跨层次论文需明确层次转换 |
| **OrgSci** | 标准型/扩展型 | 欢迎机制深度；Mechanism preview 段可较长 |
| **JM** | 紧凑型 | 偏好数据冲击 Hook；快速进入核心问题 |
| **JMR** | 标准型 | 重视理论贡献的精准定位 |
