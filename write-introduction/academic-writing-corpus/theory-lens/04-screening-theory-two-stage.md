---
type: canonical_theory_lens
canonical_id: "04-screening-theory-two-stage"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: GENERATIVE
exclusivity: MEDIUM
source_papers:
  - pupovac2026 (POM, 2026): "Screening theory two-stage procedure"
created: 2026-07-21
source: Distilled by distill-introduction-exemplar Phase 4.6
---

# 04-screening-theory-two-stage — Screening Theory 两阶段筛选

## 功能描述

在 Introduction 中引入 screening theory，解释当理想筛选不可得时，决策者如何通过多阶段筛选（如先检查自愿披露，再检查具体依赖度）降低信息不对称。这种 Theory Lens 把读者的注意力从“有没有信息”转向“如何在没有理想信息的情况下做推断”。

## 适用场景

- Gap 类型 = **Incompleteness**
- 研究 shareholders、消费者、或其他决策者如何解读组织信号
- 核心机制是信息筛选与信号解读
- 理想指标缺失，需要替代性筛选程序

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): pupovac2026 (POM)

### 生成力
- **GENERATIVE**: "screening for cues" + "two-stage screening" 模板可迁移到信息披露、信号解读、利益相关者反应等多种情境

### 排他性
- **MEDIUM**: 必须有明确的筛选主体、筛选对象和替代性 cues；不能泛化为一般的信息搜索

---

## 句法模板

### 变体 A：两阶段筛选型（pupovac2026 型）

**模板**:
> "We reason that [decision makers] attempt to resolve their uncertainty about [target state] by 'screening' for [actor]-provided 'cues' about [information domain] ([citation]). Thus, we rely on [screening theory] ([citations]) to explore [actor's] prior information cues that may lower [decision makers'] perceived [uncertainty]. [Decision makers] overcome the unavailability of their preferred screen by undertaking a two-stage screening. First, they check whether [actor] demonstrates [stage-one cue] by going beyond [baseline requirement]. The intuition is that [stage-one logic]. Second, in cases where [stage-one condition], [decision makers] screen [stage-two cue]. The intuition is that [stage-two logic]."

**来源**: pupovac2026 (POM), P20 + P24

**原文锚定**:
> "We reason that the supplier's shareholders attempt to resolve their uncertainty about the demand for the supplier's products by 'screening' for supplier-provided 'cues' about its customers (Connelly et al., 2021). Thus, we rely on screening theory (Stiglitz, 1975; Zhang et al., 2023) to explore a supplier's prior (i.e., in the pre-recall period) information cues that may lower its shareholders' perceived demand uncertainty. We reason that the supplier's shareholders overcome the unavailability of their preferred screen by undertaking a two-stage screening. First, they check whether the supplier voluntarily disclosed customer information by going beyond legal requirements and accounting standards. The intuition is that the supplier's voluntary disclosure of customer information assuages shareholders' perceived demand uncertainty after the manufacturer's recall, thereby mitigating their punitive reactions. Second, in cases where the supplier discloses customer information, shareholders screen the supplier's revenue dependence on the recalling manufacturer. The intuition is that the higher the supplier's dependence, the greater the shareholders' perceived demand uncertainty and, thus, the more punitive their reactions."

**关键特征**:
- 用引号标注 "screening" / "cues" 建立术语
- 先声明理论透镜，再解释两阶段过程
- 每个阶段都有明确条件、行动、直觉
- 与 Tension 中的"理想筛选不可得"直接呼应

**适用**: screening theory 应用；信息不对称；自愿披露；信号解读；利益相关者反应

**禁忌**: 不要写成完整的 screening theory 文献综述；Introduction 中 2-3 句承诺即可

---

## 组装规则

### 必须配对
- **Tension**: `21-ideal-screen-unavailable` 或 `01-despite-progress-unaddressed`
- **Preview**: 必须与两阶段 empirics 一致（第一阶段全样本，第二阶段子样本）

### 互斥
- **避免与 `01-agency-theory-standard` 同时作为主导理论透镜**: 可辅助引用 principal-agent 关系，但主理论应明确为 screening / information economics

### 反模式提醒
- 不要引入 screening theory 而不解释具体筛选对象
- 不要省略两阶段之间的逻辑条件（"in cases where"）
- 两阶段逻辑必须在 Theory section 完整展开，Introduction 只是承诺

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| POM / JOM / MSOM | ⭐⭐⭐ 高 | 运营/供应链信息问题适配 |
| JM / JMR | ⭐⭐⭐ 高 | 消费者/股东信息筛选研究适配 |
| SMJ | ⭐⭐ 中 | 需连接战略决策含义 |
| AMJ / ASQ | ⭐⭐ 中 | 需要更精细的理论机制论证 |

---

## 槽位填充正误对比

### `[screening object]` — 筛选对象

❌ "We use screening theory to study information." → 无具体对象

✅ "We rely on screening theory to explore a supplier's prior information cues that may lower its shareholders' perceived demand uncertainty." → 对象 + 机制 + 结果

### `[two-stage logic]` — 两阶段逻辑

❌ "First, we look at disclosure. Second, we look at dependence." → 无理论直觉

✅ "First, shareholders check whether the supplier voluntarily disclosed customer information... The intuition is that voluntary disclosure assuages perceived demand uncertainty. Second, in cases where the supplier discloses, shareholders screen revenue dependence... The intuition is that higher dependence signals greater demand risk." → 每阶段有条件、有行动、有直觉

### `[decision makers]` — 筛选主体

❌ "The market screens information." → 主体抽象

✅ "The supplier's shareholders attempt to resolve their uncertainty by screening for supplier-provided cues" → 主体明确且有理论依据

---

## 风格画像

> 以下风格特征是从使用本模板的多篇顶刊论文中聚合提取的。不是每篇论文都必须遵守，但偏离时应有明确理由。
> 最后更新: 2026-07-21 | 聚合论文数: 1

### 语气光谱
- **主语气**: theoretical-commitment — 证据: "Thus, we rely on screening theory..."
- **次语气**: mechanism-forward — 证据: 直接推进到 two-stage intuition，不过度综述

### 段落节奏
- **典型节奏**: 筛选行为声明（1句）→ 理论透镜声明（1句）→ 两阶段程序展开（2-3句，First / Second）

### 标志性叙事标记
- [[pupovac2026]]: 术语引号 — "screening" for supplier-provided "cues"
- [[pupovac2026]]: 两阶段标记 — "First, they check... Second, in cases where..."

### 刻意回避
- [[pupovac2026]]: 避免 screening theory 文献综述 — 仅用 Stiglitz (1975) 和 Zhang et al. (2023) 建立合法性
- [[pupovac2026]]: 避免在 Introduction 展开 rival-poaching 等次要机制 — 留给 Theory section

### 质量标记
- **最值得模仿**: 用极简语句完成 "理论来源 → 筛选对象 → 两阶段程序 → 每阶段直觉" 四层结构
- **已知风险**: 两阶段 empirics 必须兑现；若第二阶段子样本过小或选择偏差未处理，会被质疑程序有效性

### 模块比重参考
- Hook 0% / Literature Turn 0% / Tension 0% / Stakes 0% / Theory Lens 45% / Preview 0% / Contribution 0%
- *来源: pupovac2026*
