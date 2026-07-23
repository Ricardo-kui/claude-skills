---
type: canonical_hook
canonical_id: "26-dyadic-contagion"
status: EMERGING
gap_type: Incompleteness
cross_paper: EMERGING
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - pupovac2026 (POM, 2026): "Manufacturer-supplier dyadic contagion hook"
created: 2026-07-21
source: Distilled by distill-introduction-exemplar Phase 4.6
---

# 26-dyadic-contagion — 二元关系传染 Hook

## 功能描述

用关系双方的相互依赖开场，展示一方成功/失败如何传导至另一方，并落脚到负面事件（如召回）的跨组织溢出。这种 Hook 把读者注意力从单个组织转移到 dyadic relationship 的系统性风险上。

## 适用场景

- Gap 类型 = **Incompleteness**
- 研究 dyadic interdependence / spillover / contagion
- 一方行为或失败对另一方产生可观察后果
- 需要快速建立跨组织因果链条的相关性

## 验证状态

### 跨论文复现
- **EMERGING** (1 paper): pupovac2026 (POM)

### 生成力
- **ADAPTABLE**: "[Dyadic relationship] are intertwined... but also suffer" 模板可迁移到供应链、平台生态、战略联盟等多种双边关系

### 排他性
- **MEDIUM**: 必须有明确的双边依赖机制；不能泛化到无直接关系的双方

---

## 句法模板

### 变体 A：关系双面性型（pupovac2026 型）

**模板**:
> "[Dyadic relationship] are intertwined ([citation]). One party may become more prosperous because of the other's success ([citations]), but also suffer steep losses resulting from the other's failure ([citations]). For example, [negative event] by one party can spur a sharp, near-term drop in the demand for its [products/services] ([citations]) and, by extension, forecast uncertain demand for the other party's [offerings]. This [uncertainty] can translate into a drop in the [outcome]. Thus, [event] likely causes a [contagion term] on the [stakeholder value] ([citation])."

**来源**: pupovac2026 (POM), P18

**原文锚定**:
> "Manufacturer–supplier relations are intertwined... A supplier may become more prosperous because of a manufacturer's success... but also suffer steep losses resulting from the manufacturer's failure... For example, the manufacturer's product recall... can spur a sharp, near-term drop in the demand for the manufacturer's products... and, by extension, forecast uncertain demand for the supplier's products. This demand uncertainty can translate into a drop in the supplier's imminent cash flow... Thus, a manufacturer's recall likely causes a contagion (or negative spillover) on the supplier's shareholder value."

**关键特征**:
- 关系双面性：成功带来繁荣 vs 失败带来损失
- 用具体负面事件作为传导机制例证
- 从一方产品需求 → 另一方需求不确定性 → 结果变量，因果链清晰
- 结尾点明 contagion / spillover 术语，建立理论框架预期

**适用**: 供应链、平台生态、战略联盟、特许经营等存在 dyadic interdependence 且负面事件可跨组织传导的研究

**禁忌**: 不要用于无明确双边依赖关系的情境；避免过度概括到多方网络；不要在 Hook 中展开完整机制

---

## 组装规则

### 必须配对
- **Tension**: `01-despite-progress-unaddressed`（指出供应链传染文献遗漏了某机制/边界）或 `21-ideal-screen-unavailable`（当研究焦点是信息筛选时）
- **Theory Lens**: 常与 screening theory、resource dependence、或 information economics 配对

### 互斥
- **不能与 `03-data-shock` 同用**: 关系叙事与数据冲击的能量和参与机制不同，同用会造成焦点分裂
- **不能与 `06-paradigm-challenge` 同用**: 关系传染 Hook 是渐进式建立相关性，不是范式颠覆

### 反模式提醒
- 不要只描述关系而不给出负面事件锚点
- 不要把双方都写成同等受害，需明确方向性（谁对谁溢出）
- 不要在 Hook 中引用过多文献，建立基本事实即可

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| POM / JOM / MSOM | ⭐⭐⭐ 高 | 供应链/运营传染研究自然适配 |
| SMJ | ⭐⭐⭐ 中 | 需强化战略后果与竞争含义 |
| JM / JMR | ⭐⭐ 中 | 需连接消费者或市场反应机制 |
| AMJ / ASQ | ⭐⭐ 中 | 需更强的理论缺口或反常现象支撑 |

---

## 槽位填充正误对比

### `[dyadic relationship]` — 关系描述

❌ "Firms interact with each other." → 过于泛泛，未建立依赖机制

✅ "Manufacturer–supplier relations are intertwined because production ecosystems tie their fates to joint product-market performance." → 明确依赖机制与共同命运

### `[negative event]` — 负面事件

❌ "Bad things happen." → 无具体锚点，读者无法建立场景

✅ "A large product recall announced by a manufacturer-customer" → 具体、可观察、有文献支撑

### `[contagion term]` — 溢出术语

❌ "This affects the other firm." → 未激活理论对话

✅ "This demand uncertainty likely causes a contagion (or negative spillover) on the supplier's shareholder value" → 使用领域术语并指明方向

---

## 风格画像

> 以下风格特征是从使用本模板的多篇顶刊论文中聚合提取的。不是每篇论文都必须遵守，但偏离时应有明确理由。
> 最后更新: 2026-07-21 | 聚合论文数: 1

### 语气光谱
- **主语气**: matter-of-fact — 证据: "Manufacturer–supplier relations are intertwined" / "Thus, a manufacturer's recall likely causes a contagion"
- **次语气**: anticipatory — 证据: 用 "likely" / "would" 铺垫后续假设

### 段落节奏
- **典型节奏**: 关系定义（1句）→ 双面后果（1-2句）→ 具体负面事件（1-2句）→ 传导机制（2-3句）→ 结果/术语锚定（1句）

### 标志性叙事标记
- [[pupovac2026]]: 关系双面性 — "A supplier may become more prosperous because of a manufacturer's success but also suffer steep losses resulting from the manufacturer's failure"
- [[pupovac2026]]: 需求传导链 — "by extension, forecast uncertain demand for the supplier's products"

### 刻意回避
- [[pupovac2026]]: 避免 standalone Literature Turn — 文献支持嵌入 Hook 句中，功能由紧凑结构承担，但 AMJ/ASQ 投稿需谨慎
- [[pupovac2026]]: 避免独立 Stakes 段 — 经济/实践重要性嵌入 Hook 末尾

### 质量标记
- **最值得模仿**: 用一句话完成 "繁荣-失败-事件-传导-术语" 五层推进，信息密度高且不冗长
- **已知风险**: Hook 同时承担 Literature Turn 和 Stakes 功能，审稿人可能质疑 gap 论证是否充分；投稿 AMJ/ASQ 建议拆分为独立段落

### 模块比重参考
- Hook 50% / Literature Turn 20% (embedded) / Tension 0% / Stakes 15% (embedded) / Theory Lens 0% / Preview 0% / Contribution 0%
- *来源: pupovac2026*
