# Opposing Forces Mechanism

## 功能定义
将现象解释为由两股对立力量（正向 vs. 负向、推力 vs. 拉力、促进 vs. 抑制）共同作用的结果，从而建立更细致的理论预测——不是简单的线性关系，而是两种力量的净效应。

## 句法模板

**模板 A（推拉理论型）**：
```
Our answer is our push-pull theory of [phenomenon], which is anchored
in [theoretical domain].

Pull Factors
[Theoretical logic for why actors are attracted/pulled toward outcome]
[Specific mechanism 1]: [Explanation with citations]
[Specific mechanism 2]: [Explanation with citations]

Push Factors
[Theoretical logic for why actors are propelled/pushed toward outcome]
[Specific mechanism 1]: [Explanation with citations]
[Specific mechanism 2]: [Explanation with citations]

The Combination of Push and Pull
[Argument for why push and pull interact rather than simply add]
[Theoretical prediction about combined effect]
```

**模板 B（对立效应型）**：
```
We distinguish between two countervailing effects of [X] on [Y].
On the one hand, [positive effect mechanism], which increases [Y].
On the other hand, [negative effect mechanism], which decreases [Y].
The net effect of [X] on [Y] depends on which of these two effects
dominates under different conditions.
```

**模板 C（净效应判定型）**：
```
Because both views offer valid arguments, we need to consider both
when examining the overall effect of [X] on [Y].
When [condition A], the [positive force] dominates because...
When [condition B], the [negative force] dominates because...
```

## 例句（来自 MVP30）

**来源**：The Push and Pull of Attaining CEO Celebrity — Lovelace et al., 2022 (AMJ)

> "Our answer is our push-pull theory of CEO celebrity attainment,
> which is anchored in the media's routines."

> "Pull Factors: When deciding what to cover and how to present a story,
> journalists face pressures to both inform and entertain... the media
> tend to focus on characteristics that deviate from the status quo
> (i.e., are nonconforming), and to report on change rather than stasis."

> "Push Factors: CEOs themselves are not bystanders in the celebrity-making
> process. Through their own self-promotion tactics, they can try to push
> their way into the limelight by becoming regular sources for journalists'
> stories."

> "The Combination of Push and Pull: Engaging in unusual behaviors or having
> unusual personal attributes does not guarantee that the media will notice
> and promote such distinctiveness in their narratives; similarly, self-promotion
> alone is less potent without something unusual to promote."

**来源**：State Ownership and Firm Innovation — Zhou et al., 2017 (ASQ)

> "Whereas the institutional view emphasizes the resource advantage brought
> by state ownership, the efficiency view highlights the dual agency problem
> caused by state ownership. Because both views offer valid arguments, we
> need to consider both when examining the overall effect of state ownership
> on innovation."

**改写模板**：
> "We distinguish between two countervailing effects of [X] on [Y].
> The [positive force] operates through [mechanism A], which enhances [Y].
> The [negative force] operates through [mechanism B], which diminishes [Y].
> Because both forces offer valid theoretical arguments, we need to consider
> both when examining the overall effect of [X] on [Y]."

## 使用场景

| 维度 | 建议 |
|------|------|
| **Outlet 偏好** | AMJ, ASQ — 适合复杂理论机制；SMJ 适合竞争性假设 |
| **理论类型** | 制度逻辑冲突、代理理论 vs. 资源基础观、推拉理论、竞争效应 |
| **前提条件** | 两股力量必须有独立的理论根源；不能只描述"一方面...另一方面"而无理论支撑 |
| **风险** | 若两股力量始终被同时激活，会被质疑为何不直接预测零效应；需要明确何时哪股力量主导 |

## 关键技巧

推拉理论的核心在于展示两种力量的**交互**而非简单相加：

| 弱表达 | 强表达 |
|--------|--------|
| "Both push and pull matter" | "Push tactics are most effective when coupled with distinctive behaviors that add to the story's appeal" |

## 反模式

| 反模式 | 问题 | 修正 |
|--------|------|------|
| 力量无交互 | 两股力量独立作用，无理论交集 | 必须论证为什么两股力量的组合会产生非线性效应 |
| 事后发现对立 | 先假设正向效应，发现负向后补第二个机制 | 两股力量必须在理论部分同时提出 |
| 净效应模糊 | "取决于情境"但不说清什么情境 | 明确给出边界条件或调节变量 |

## 相关语料

- 配合 `hypotheses/moderation-strengthening.md` 和 `moderation-weakening.md` 使用：调节假设决定哪股力量主导
- 配合 `tensions/07-same-policy-opposite-effects.md` 使用：同一政策的对立效应与推拉机制同源
- 配合 `results-exposition/interaction-marginal-effects.md` 使用：结果部分用边际效应展示力量转换

## 验证状态
- **跨论文复现**: ✓ VERIFIED（Lovelace et al. 2022; Zhou et al. 2017）
- **来源论文**: Lovelace et al. (AMJ) × 1; Zhou et al. (ASQ) × 1
- **生成力**: 待验证
- **排他性**: 中——适合制度逻辑冲突或竞争效应论文
- **期刊限制**: AMJ/ASQ 偏好；SMJ 可用但需更快给出管理启示
- **收录状态**: 🔬 EXPERIMENTAL
