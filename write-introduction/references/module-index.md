# Introduction 模块索引

## 模块体系概览

Introduction 由以下五类模块组装而成。每个模块都是独立的"修辞功能单元"，可根据论文特征自由组合。

| 模块类别 | 功能 | 语料库位置 | 当前规模 | 三重验证分布 |
|---------|------|-----------|---------|-------------|
| **Hooks** | 开场吸引，建立初始注意力 | `../academic-writing-corpus/hooks/` | 20种（全部已收录，其中4个已审计） | 2 ⭐ PREMIUM / 2 ✓ STANDARD / 16 🔬 EXPERIMENTAL |
| **Tensions** | Gap 构建，刺破文献共识 | `../academic-writing-corpus/tensions/` | 10种（全部已收录，其中5个已审计） | 0 ⭐ PREMIUM / 3 ✓ STANDARD / 7 🔬 EXPERIMENTAL |
| **Stakes** | 重要性论证，回答"so what" | `../academic-writing-corpus/stakes/` | 7种（4已收录，3待写） | 0 ⭐ PREMIUM / 1 ✓ STANDARD / 3 🔬 EXPERIMENTAL |
| **Transitions** | 段落过渡，确保叙事流 | `../academic-writing-corpus/transitions/` | 6种（3已收录，3待写） | 0 ⭐ PREMIUM / 3 ✓ STANDARD / 0 🔬 EXPERIMENTAL |
| **Contributions** | 贡献声明，Makadok 维度 | `references/makadok-frames.md` | 8维度 | 8 ✓ 已验证（跨论文复现 ≥5） |

> **使用原则**：模块之间通过 Transition 链连接，形成 `Hook → Literature → Gap → Stakes/Theory → Preview → Contribution` 的叙事流。

---

## 三重验证框架

每个语料库模块必须通过以下三项验证才能升级收录状态。该框架借鉴 nuwa-skill 的"心智模型验证"方法论，专门针对学术写作语料库的质量控制进行适配。

### 验证一：跨论文复现（Cross-Paper Reproduction）

**问题**：这个修辞模式是单一论文的 idiosyncrasy，还是顶刊中的 recurrent pattern？

| 等级 | 标准 | 收录状态映射 | 检查方法 |
|------|------|-------------|---------|
| **ROBUST** | 同一模块在 ≥3 篇不同论文（不同第一作者、不同期刊、不同年份）中独立出现 | ⭐ PREMIUM | 在 MVP30 + 个人文献库中检索相同句法结构 |
| **VERIFIED** | 同一模块在 ≥2 篇不同论文中出现 | ✓ STANDARD | 至少找到1个除来源论文外的独立案例 |
| **SINGLE-INSTANCE** | 仅在1篇来源论文中观察到 | 🔬 EXPERIMENTAL | 标记为待复现 |
| **UNAUDITED** | 文件已收录，但尚未执行复现检索 | 🔬 EXPERIMENTAL (未审计) | 优先审计队列 |

### 验证二：生成力（Generativity）

**问题**：这个模块能否在不同研究领域生成有效的 Introduction 变体，还是只能原样复刻来源论文？

| 等级 | 标准 | 实操测试 |
|------|------|---------|
| **GENERATIVE** | 用此模块能生成 ≥3 个不同研究领域的 Introduction 变体，且每个变体都能被该领域专家认可为"自然的学术表达" | 随机抽取3个 ASQ/SMJ/AMJ 论文标题，尝试用该模块写 P1/P3 句，检查是否违和 |
| **ADAPTABLE** | 能生成1-2个领域的变体，但需要调整关键词和语气 | 可用，但需人工适配 |
| **FRAGILE** | 只能原样复刻来源论文的语境，换个领域显得生硬或做作 | 限制使用范围，等待更多案例积累 |

### 验证三：排他性（Exclusivity）

**问题**：这个模块是否只出现在特定的 Gap 类型或贡献维度中？如果到处都能用，它的诊断价值就低。

| 等级 | 标准 | 使用含义 |
|------|------|---------|
| **HIGH** | 模块与特定 Gap 类型强绑定（如 `06-paradigm-challenge` 几乎只在 Incommensurability 中出现）| 选择该模块 = 向读者暗示特定的 Gap 强度 |
| **MEDIUM** | 模块跨 Gap 类型可用，但在某些类型中更常见 | 需要搭配其他模块来精确 Gap 定位 |
| **LOW** | 模块通用，几乎所有 Introduction 都能用 | 不会误导读者，但也不会提供额外的 Gap 信号 |

### 升级路径

```
🔬 EXPERIMENTAL (UNAUDITED)
        ↓ 执行跨论文检索 + 记录来源
🔬 EXPERIMENTAL (SINGLE-INSTANCE)
        ↓ 找到第2个独立案例
   ✓ STANDARD (VERIFIED)
        ↓ 找到第3个独立案例 + 通过生成力测试
   ⭐ PREMIUM (ROBUST + GENERATIVE)
```

**当前审计进度**：
- Hooks：4/20 已完成审计（05, 06 为 PREMIUM；03, 04 为 STANDARD）
- Tensions：5/10 已完成审计（01, 02, 04 为 STANDARD；03 为 EXPERIMENTAL）
- Stakes：1/4 已完成审计（07 为 STANDARD）
- Transitions：3/3 已完成审计（全部为 STANDARD）

> 审计详情见各模块文件头部的 `## 验证状态` 区块。未审计模块的收录状态默认为 🔬 EXPERIMENTAL，不代表质量低，仅代表尚未执行系统性的复现检索。

---

## Hook 选择器

Hook 的选择由 **Gap 强度** 决定。弱 Gap 需要温和开场，强 Gap 需要颠覆性开场。

### 按 Gap 强度推荐

| Gap 强度 | 能量等级 | 推荐 Hook 类型 | 代表模块 | 文件路径 | 状态 |
|---------|---------|--------------|---------|---------|------|
| **Incompleteness** | 低 | 冷启动定义、数据冲击、实践难题、领域缺口 | `03-data-shock`, `10-practical-puzzle`, `13-domain-gap` | `hooks/03-data-shock.md`, `hooks/10-practical-puzzle.md`, `hooks/13-domain-gap.md` | 部分完成 |
| **Inadequacy** | 中 | 文献共识盲点、经典辩论+约束放松、惊人事实、跨学科类比 | `05-literature-consensus-blindspot`, `15-classic-debate-constraint`, `12-surprising-fact`, `01-cross-disciplinary-analogy` | `hooks/05-literature-consensus-blindspot.md`, `hooks/15-classic-debate-constraint.md`, `hooks/12-surprising-fact.md`, `hooks/01-cross-disciplinary-analogy.md` | 部分完成 |
| **Incommensurability** | 高 | 范式挑战、理论矛盾+经验悖论、反直觉发现、前瞻性视角转移 | `06-paradigm-challenge`, `16-theory-contradiction-empirical-paradox`, `20-counterintuitive-finding`, `19-forward-looking-shift` | `hooks/06-paradigm-challenge.md`, `hooks/16-theory-contradiction-empirical-paradox.md`, `hooks/20-counterintuitive-finding.md`, `hooks/19-forward-looking-shift.md` | 部分完成 |

### 按贡献维度补充推荐

| 贡献维度 | 额外推荐 Hook | 理由 |
|---------|-------------|------|
| **Constructs** | `02-extreme-situation`, `12-surprising-fact` | 构念辨析需要让读者"意识到混淆的存在"，极端情境或惊人事实最有效 |
| **Mechanism** | `05-literature-consensus-blindspot`, `06-paradigm-challenge` | 机制论文需要展示"现有解释不足"，文献盲点或范式挑战都适合 |
| **Boundary** | `04-puzzle-paradox`, `15-classic-debate-constraint` | 边界条件论文需要呈现"何时有效、何时失效"的谜题感 |
| **Phenomenon** | `03-data-shock`, `09-evolving-social-issue`, `17-phenomenon-market-evolution` | 新现象域论文适合用数据或趋势开场 |
| **Level** | `01-cross-disciplinary-analogy`, `19-forward-looking-shift` | 跨层次论文需要桥接不同分析层次，跨学科类比最有效 |
| **Mode** | `02-extreme-situation`, `08-quotation-hook` | 过程理论论文适合用沉浸式叙事或引语建立时间感 |

### 全部 Hook 目录

| # | 文件名 | 功能描述 | Gap 强度 | 三重验证 | 状态 |
|---|--------|---------|---------|---------|------|
| 01 | `01-cross-disciplinary-analogy.md` | 跨学科类比 hook | 中-高 | SINGLE-INSTANCE (Pollock et al., ASQ) | 🔬 |
| 02 | `02-extreme-situation.md` | 极端情境 / "Imagine..." hook | 中-高 | 未审计 | 🔬 |
| 03 | `03-data-shock.md` | 数据冲击 hook（咨询公司数据 + 巨额数字 + 权威引语） | 低 | VERIFIED (3 papers: JMR, MSOM) | ✓ |
| 04 | `04-puzzle-paradox.md` | 谜题/悖论 hook | 中 | VERIFIED (4 papers: ASQ, SMJ) | ✓ |
| 05 | `05-literature-consensus-blindspot.md` | 文献共识 + 盲点 hook | 中 | ROBUST (5 papers: AMJ, SMJ, ASQ) | ⭐ |
| 06 | `06-paradigm-challenge.md` | 范式挑战 hook | 高 | ROBUST (6 papers: ASQ, SMJ, ASR, AMJ) | ⭐ |
| 07 | `07-headline-news.md` | 头条新闻/当日事件对比 hook | 低-中 | SINGLE-INSTANCE (Singh & Grewal 2023, JMR) | 🔬 |
| 08 | `08-quotation-hook.md` | 权威引语 + 日常类比 hook | 中 | SINGLE-INSTANCE (Paruchuri et al. 2020, SMJ) | 🔬 |
| 09 | `09-evolving-social-issue.md` | 演变中的社会问题 hook | 低-中 | 未审计 | 🔬 |
| 10 | `10-practical-puzzle.md` | 实践难题/从业者困境 hook | 低 | 未审计 | 🔬 |
| 11 | `11-current-affairs-debate.md` | 时事/社会辩论 hook | 中 | 未审计 | 🔬 |
| 12 | `12-surprising-fact.md` | "Contrary to popular belief" 惊人事实 hook | 中 | 未审计 | 🔬 |
| 13 | `13-domain-gap.md` | 领域缺口 hook | 低 | 未审计 | 🔬 |
| 14 | `14-cost-benefit-tension.md` | 成本-收益张力 hook | 低-中 | 未审计 | 🔬 |
| 15 | `15-classic-debate-constraint.md` | 经典辩论 + 约束放松 hook | 中 | 未审计 | 🔬 |
| 16 | `16-theory-contradiction-empirical-paradox.md` | 理论矛盾 + 经验悖论 hook | 高 | 未审计 | 🔬 |
| 17 | `17-phenomenon-market-evolution.md` | 现象驱动市场演变 hook | 低 | SINGLE-INSTANCE (Zhao & Ding 2022, OS) | 🔬 |
| 18 | `18-authority-quotation-dilemma.md` | 权威引语 + 系统性困境 hook | 中 | 未审计 | 🔬 |
| 19 | `19-forward-looking-shift.md` | 前瞻性视角转移 hook | 高 | 未审计 | 🔬 |
| 20 | `20-counterintuitive-finding.md` | 反直觉发现挑战 hook | 高 | 未审计 | 🔬 |

---

## Tension 选择器

Tension 的选择由 **Gap 类型** 决定。每种 Gap 类型对应不同的"刺破"策略。

| Gap 类型 | 核心张力 | 推荐 Tension 模块 | 文件路径 | 三重验证 | 替代方案 |
|---------|---------|-----------------|---------|---------|---------|
| **Incompleteness** | 已有进展，但遗漏了某个维度 | `01-despite-progress-unaddressed` | `tensions/01-despite-progress-unaddressed.md` | VERIFIED (4+ papers) | `02-implicit-assumption-wrong` |
| **Inadequacy** | 现有视角片面，忽视了替代解释 | `03-structural-blindspot`, `05-overlooked-alternative` | `tensions/03-structural-blindspot.md`, `tensions/05-overlooked-alternative.md` | 03: SINGLE-INSTANCE; 05: 未审计 | `02-implicit-assumption-wrong` |
| **Incommensurability** | 理论共识与现实矛盾 | `04-reality-contradicts-consensus` | `tensions/04-reality-contradicts-consensus.md` | VERIFIED (3+ papers) | `07-same-policy-opposite-effects` |

### 全部 Tension 目录

| # | 文件名 | 功能描述 | Gap 类型 | 三重验证 | 状态 |
|---|--------|---------|---------|---------|------|
| 01 | `01-despite-progress-unaddressed.md` | "Despite progress... largely unaddressed" | Incompleteness | VERIFIED (4+ papers: ASQ, SMJ, AMJ, OS) | ✓ |
| 02 | `02-implicit-assumption-wrong.md` | "The implicit assumption is wrong" | Inadequacy | VERIFIED (5+ papers: SMJ, ASQ, JMR) | ✓ |
| 03 | `03-structural-blindspot.md` | "Structural blind spot" | Inadequacy | SINGLE-INSTANCE (Singh & Grewal 2023, JMR) | 🔬 |
| 04 | `04-reality-contradicts-consensus.md` | "Reality contradicts consensus" | Incommensurability | VERIFIED (3+ papers: ASQ, SMJ) | ✓ |
| 05 | `05-overlooked-alternative.md` | "Overlooked alternative strategy" | Inadequacy | 未审计 | 🔬 |
| 06 | `06-forward-vs-backward-looking.md` | "Forward-looking vs backward-looking" | Inadequacy | 未审计 | 🔬 |
| 07 | `07-same-policy-opposite-effects.md` | "Same policy, opposite effects" | Incommensurability | 未审计 | 🔬 |
| 08 | `08-cost-vs-benefit.md` | "Cost vs benefit trade-off" | 通用 | 未审计 | 🔬 |
| 09 | `09-resource-acquisition-vs-utilization.md` | "Resource acquisition vs utilization" | Inadequacy | 未审计 | 🔬 |
| 10 | `10-constraint-vs-freedom.md` | "Constraint vs freedom" | Incommensurability | 未审计 | 🔬 |

### Tension 强度与变体表达

| 强度 | 表达 | 适用情境 |
|------|------|---------|
| 温和 | "has received relatively little attention" | 合作关系良好的 literature |
| 中等 | "remains poorly understood" | 一般性缺口 |
| 强烈 | "is theoretically underspecified" | 理论驱动型期刊（ASQ, OS） |
| 强烈 | "rests on an untested assumption" | 直接挑战基础假设 |
| 惊讶 | "surprisingly understudied given its importance" | 显然重要但被忽视 |

---

## Stakes 选择器

Stakes 的选择由 **研究特征** 决定。在 Gap 建立之后，必须回答"so what"。

| 研究特征 | 推荐 Stakes 模块 | 文件路径 | 三重验证 | 替代方案 |
|---------|----------------|---------|---------|---------|
| 含市场/财务结果、治理议题 | `02-quantified-economic-loss` | `stakes/02-quantified-economic-loss.md` | 未审计 | `05-firm-value-stock-market` |
| 含股价/资本市场反应 | `05-firm-value-stock-market` | `stakes/05-firm-value-stock-market.md` | 未审计 | `02-quantified-economic-loss` |
| 含资源配置/战略决策 | `01-resource-allocation-guidance` | `stakes/01-resource-allocation-guidance.md` | 待写 | 内部模板 |
| 含隐性机制/长期后果 | `03-insidious-mechanism` | `stakes/03-insidious-mechanism.md` | 待写 | 内部模板 |
| 含公共政策/健康/安全 | `04-public-health-safety` | `stakes/04-public-health-safety.md` | 未审计（SINGLE-INSTANCE: Darby et al. 2023 MSOM） | 内部模板 |
| 含场域合法性/声誉危机/资本市场反应 | `07-reputation-legitimacy-crisis` | `stakes/07-reputation-legitimacy-crisis.md` | VERIFIED（Desai 2011 AMJ + Pfarrer 2010 AMJ） | `stakes/02-quantified-economic-loss` |
| 含竞争/生存压力 | `06-competitive-advantage` | `stakes/06-competitive-advantage.md` | 待写 | 内部模板 |

### Stakes 插入位置指南

| 布局类型 | 推荐插入位置 | 形式 |
|---------|------------|------|
| 紧凑型 | Gap 段末尾（1-2句） | Inline |
| 标准型 | P3 末尾或独立 P4（2-3句） | Inline 或独立段 |
| 扩展型 | 独立 P4（3-4句）+ 数据/案例 | 独立段 |

---

## Conversation 策略选择器

| Gap 类型 | 推荐策略 | 核心逻辑 | 适用场景 |
|---------|---------|---------|---------|
| **Incompleteness** | Progressive Coherence | 从广泛共识逐步聚焦到具体缺口 | 已有丰富文献的领域 |
| **Inadequacy** | Synthesized Coherence | 承认多方观点，展示盲区 | 存在竞争性解释的文献 | `../academic-writing-corpus/literature-turns/synthesized-coherence.md` | ✓ STANDARD |
| **Incommensurability** | Non-Coherence | 建立对立，然后颠覆 | 理论矛盾尖锐的领域 |

---

## Transition 链

| 过渡位置 | 功能 | 模块文件 | 三重验证 | 必须度 |
|---------|------|---------|---------|--------|
| **Hook → Literature** | 现象→理论化 | `../academic-writing-corpus/transitions/hook-to-literature.md` | VERIFIED (universal) | ✅ |
| **Literature → Gap** | 共识→缺口 | `../academic-writing-corpus/transitions/literature-to-gap.md` | VERIFIED (universal) | ✅ |
| **Gap → Contribution** | 缺口→贡献 | `../academic-writing-corpus/transitions/gap-to-contribution.md` | VERIFIED (universal) | ✅ |
| **Contribution → Roadmap** | 贡献→结构 | `../academic-writing-corpus/transitions/contribution-to-roadmap.md` | 待写 | ⚠️ |
| **Theory → Hypothesis** | 理论→假设 | `../academic-writing-corpus/transitions/theory-to-hypothesis.md` | 待写 | Theory 部分用 |
| **Results → Implications** | 结果→启示 | `../academic-writing-corpus/transitions/results-to-implications.md` | 待写 | Discussion 部分用 |

### Transition 链组装原则

1. **每段必须有 Transition**：不允许段落之间无转接直接跳跃
2. **Transition 长度 1-2 句**：过渡是"转轴"，不是"展开"
3. **能量守恒**：高能量 Hook 后需要适度降温的 Transition，低能量 Hook 后需要升温的 Transition

---

## 模块收录状态图例

| 图例 | 含义 | 三重验证标准 | 使用建议 |
|------|------|-------------|---------|
| ⭐ PREMIUM | 跨多篇论文复现，高生成力 | 跨论文复现 = ROBUST (≥3篇) + 生成力 = GENERATIVE | 优先使用；模块句法骨架可靠，适配时只需替换领域术语 |
| ✓ STANDARD | 跨论文初步复现，中等生成力 | 跨论文复现 = VERIFIED (≥2篇) + 生成力 = ADAPTABLE | 可用；句法结构可信，但建议对比原文确认语气强度 |
| 🔬 EXPERIMENTAL | 已收录但验证不充分 | 跨论文复现 = SINGLE-INSTANCE 或 UNAUDITED | 参考性使用，需人工判断；建议在使用前查阅模块文件中的 `验证状态` 区块确认来源论文和适用边界 |
| 待写 | 语料库尚未收录 | — | 使用通用模板或内部模板替代；如需该功能，建议从个人文献库中提取并贡献 |
