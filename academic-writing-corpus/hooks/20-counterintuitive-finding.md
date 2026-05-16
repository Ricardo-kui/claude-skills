# Counterintuitive Finding Challenge Hook

## 功能定义
先指出某一研究领域的 dominant valence——几乎所有研究都发现 X 导致 Y（如负事件导致负溢出）——然后告诉读者：我们发现了一个反直觉的例外（负事件可以产生正溢出），且这种例外不是偶然的轶事而是系统性的理论模式，从而建立"这篇文章会让你重新思考你以为你知道的东西"的悬念。

## 句法模板

**模板 A（Dominant Valence + 稀有例外型）**：
```
Most research on [topic] has focused on situations where [dominant direction — e.g., a focal firm's negative action has negative spillover effects]. We are aware of only [one / a handful of] stud[ies] where the valence of the [outcome] is different than the valence of the [action]. [Citation] found that [exception finding]. While [they] explored this effect, [limitation 1]. [They] also [limitation 2]. We [address these limitations by...].
```

**模板 B（反直觉对比型）**：
```
Intuitively, [phenomenon X] should [produce outcome Y]. However, we find the opposite: [phenomenon X] actually [produces outcome not-Y / Z]. This counterintuitive pattern emerges because [mechanism]. [Specific condition] determines whether the expected or counterintuitive pattern dominates.
```

## 例句（来自 MVP30）

**来源**：Paruchuri, Pollock & Kumar 2020 (SMJ)

> "Most research on [reputation spillovers] has focused on situations where a focal firm's negative action has negative spillover effects. We are aware of only one study where the valence of the spillover is different than the valence of the action... [Citation] found that [exception]. In this study we test these assumptions and explore how [construct 1] intersects with [construct 2] to influence [mechanism] and create a [counterintuitive outcome]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | SMJ, AMJ 极度适合；ASQ 也可用 |
| **理论类型** | 声誉/认知心理学/归因理论/竞争动态——任何涉及"方向反转"效应的研究 |
| **前提条件** | 反直觉发现必须有先验的理论推导（不是事后发现）；dominant valence 必须是真实的文献共识 |
| **风险** | 如果反直觉发现是噪音或特例而非稳健模式，reviewer 会挑战内部效度 |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 误判 dominant valence | 声称"所有研究都发现负→负溢出"，但实际上文献中已有正→负和负→正的多方向研究 | 在 P4 中审慎盘点例外文献，不夸大主流方向的一致性 |
| 反直觉无边界条件 | 声称"负事件→正溢出"适用于所有情况 | 必须在 Introduction 中预告边界条件 |
| 事后合理化 | 发现是数据挖掘的结果，然后强行编了一个理论 | 反直觉预测必须在 Theory 部分有 a priori 的因果链推理 |
| 技术反直觉但常识上不反直觉 | "我们发现高价格导致低销量"——这并不反直觉 | 反直觉必须是真的违背理论预期或行业常识的 |

## 验证状态
- **跨论文复现**: ⚠️ SINGLE-INSTANCE
- **来源论文**: Paruchuri, Pollock & Kumar 2020 (SMJ) × 1
- **生成力**: 待验证
- **排他性**: 高——需要有明确的反直觉实证发现
- **期刊限制**: SMJ/AMJ 首选；ASQ 定性论文如果基于反直觉田野观察也可用
- **收录状态**: 🔬 EXPERIMENTAL

## 相关语料
- 配合 `tensions/04-reality-contradicts-consensus.md`：反直觉发现直接挑战"常识"预期
- 配合 `mechanisms/opposing-forces.md`：两种对立力量在不同条件下此消彼长
- 配合 `hypotheses/05-moderation-reverses-main-effect.md`：边界条件决定了正向还是负向效应占主导
