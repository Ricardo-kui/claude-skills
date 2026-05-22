# Corpus Entry Verification Standards

> 借鉴 Nuwa-Skill 三重验证机制，为叙事模板语料库建立入库标准。
> 每个 corpus entry 在收录前必须通过至少 **2/3 项验证**。

---

## 一、三重验证标准

### 验证 1: Cross-Paper Recurrence（跨论文复现）

**标准**：同一叙事 pattern 在至少 **2 篇不同期刊/不同作者/不同年份**的顶刊论文中出现。

**操作化**：
- 记录每篇来源论文的完整引用信息（作者、年份、期刊）
- 如果 pattern 只在一篇论文中出现 → 标记为 `⚠️ SINGLE-INSTANCE`（单例观察），降级使用
- 如果 pattern 在 2+ 篇同期刊论文中出现 → 标记为 `✓ VERIFIED`，但注明期刊偏向
- 如果 pattern 在 2+ 篇跨期刊论文中出现 → 标记为 `✓✓ ROBUST`（跨期刊稳健）

**反例检测**：
- 如果同一 pattern 在某期刊中**从未**出现 → 标记 `🚫 NOT-FOR-[journal]`

### 验证 2: Generative Power（生成力）

**标准**：用此模板能为新的研究生成合理的段落结构，而非只能复现原论文。

**操作化**：
- 选 1 篇训练集外的顶刊论文，用此模板预测其对应段落的结构
- 如果模板预测的结构与原论文段落的实际功能匹配度 ≥ 70% → `✓ GENERATIVE`
- 如果模板只能描述原论文但不能泛化 → `✗ NON-GENERATIVE`，降级为 "参考示例" 而非 "模板"

**测试方法**：
1. 取一篇未在训练集中的论文（如 2024 年 AMJ 论文）
2. 用模板生成该论文应使用的段落结构
3. 对比原始论文的实际段落功能标签
4. 计算功能匹配率

### 验证 3: Exclusivity（排他性）

**标准**：此 pattern 是某类 Gap/贡献/期刊策略特有的，不是所有论文的通用写法。

**操作化**：
- 检查此 pattern 是否与特定 Gap 类型（Incompleteness/Inadequacy/Incommensurability）绑定
- 检查此 pattern 是否与特定 Makadok 贡献维度绑定
- 检查此 pattern 是否与特定期刊叙事人格绑定
- 如果 pattern 是 "所有论文都这样写" 的通用写法 → `✗ GENERIC`，降级但保留（仍有参考价值）

**排他性强度**：
| 级别 | 条件 | 示例 |
|------|------|------|
| **高排他** | 只在 1 种 Gap × 1 种期刊中出现 | ASQ 的跨学科类比 hook，仅适用于 Incommensurability 类型 |
| **中排他** | 在 1-2 种 Gap 类型中出现 | "Progressive coherence" conversation 策略，适用于 Incompleteness |
| **低排他** | 跨多种 Gap 类型通用 | "However, prior research has not examined..." — 几乎无处不在 |
| **通用** | 所有论文的正交要求 | 描述性统计表格、假设编号格式 |

---

## 二、入库决策矩阵

| 跨论文复现 | 生成力 | 排他性 | 决策 | 标记 |
|-----------|--------|--------|------|------|
| ✓✓ ROBUST | ✓ GENERATIVE | 高/中排他 | **正式入库** | `⭐ PREMIUM` |
| ✓ VERIFIED | ✓ GENERATIVE | 任意 | **正式入库** | `✓ STANDARD` |
| ⚠️ SINGLE | ✓ GENERATIVE | 高排他 | **条件入库** | `🔬 EXPERIMENTAL` |
| ✓ VERIFIED | ✗ NON-GEN | 任意 | **降级为参考** | `📋 REFERENCE` |
| ⚠️ SINGLE | ✗ NON-GEN | 低排他 | **不入库** | `❌ REJECT` |
| 任意 | 任意 | ✗ GENERIC | **降级保留** | `📌 BASIC` |

---

## 三、现有 Corpus 条目的回溯验证状态

### Hooks（12/20 已完成）

| # | 文件名 | 跨论文 | 生成力 | 排他性 | 状态 |
|---|--------|--------|--------|--------|------|
| 01 | cross-disciplinary-analogy | ⚠️ 仅 Pollock et al. ASQ | 待验证 | 高（ASQ+Incommensurability） | `🔬 EXPERIMENTAL` |
| 02 | extreme-situation | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 03 | data-shock | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 04 | puzzle-paradox | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 05 | literature-consensus-blindspot | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 06 | paradigm-challenge | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 10 | practical-puzzle | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 12 | surprising-fact | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 13 | domain-gap | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 14 | cost-benefit-tension | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 15 | classic-debate-constraint | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 16 | theory-contradiction-empirical-paradox | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |

**当前状态**：所有已完成条目均为 `🔬 EXPERIMENTAL`——每条仅基于 1 篇论文，尚未进行跨论文验证和生成力测试。

### Tensions（3/10 已完成）

| # | 文件名 | 跨论文 | 生成力 | 排他性 | 状态 |
|---|--------|--------|--------|--------|------|
| 01 | despite-progress-unaddressed | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 04 | reality-contradicts-consensus | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |
| 08 | cost-vs-benefit | ⚠️ 仅 1 篇 | 待验证 | 待评估 | `🔬 EXPERIMENTAL` |

### Stakes / Transitions

| 条目 | 状态 |
|------|------|
| 全部 2 stakes + 3 transitions | `🔬 EXPERIMENTAL`（均仅基于 1 篇论文） |

---

## 四、验证路线图

### Phase 1: 跨论文验证（立即开始）

对于每个已完成条目：
1. 在 MVP30 的 28 篇论文中搜索是否出现相同 pattern
2. 每发现一篇新来源论文，记录到条目的 "例句" section
3. 达到 2+ 篇来源 → 升级为 `✓ VERIFIED`
4. 达到 2+ 篇跨期刊来源 → 升级为 `✓✓ ROBUST`

### Phase 2: 生成力测试（累积足够条目后）

1. 选 3 篇训练集外论文（建议：2024-2025 AMJ/SMJ/ASQ 各一篇）
2. 对每个 `✓ VERIFIED` 条目执行生成力测试
3. 通过测试 → 升级为 `✓ GENERATIVE`
4. 失败 → 降级为 `📋 REFERENCE`

### Phase 3: 排他性标注（持续进行）

每完成一篇新的 narrative analysis，更新对应 corpus 条目的排他性标签。

---

## 五、条目文件格式扩展

每个 corpus 条目文件在现有 6-section 结构上，增加**验证区块**：

```markdown
## 验证状态
- **跨论文复现**: [✓✓ ROBUST / ✓ VERIFIED / ⚠️ SINGLE-INSTANCE]
- **来源论文**: [Author Year (Journal)] × N
- **生成力**: [✓ GENERATIVE / 待验证 / ✗ NON-GENERATIVE]
- **排他性**: [高 / 中 / 低 / 通用]
- **期刊限制**: [无限制 / 不适用于 ASQ / 仅适用于 SMJ+AMJ]
- **收录状态**: [⭐ PREMIUM / ✓ STANDARD / 🔬 EXPERIMENTAL / 📋 REFERENCE / 📌 BASIC]
```
