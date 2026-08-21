# Claim Calibration（主张层级校准）

> 来源：抽取改写自 good-story (Rimagination) `references/overclaim-calibration.md`，管理实证情境化。与 Booth 证据五问（`evidence-standards.md`）、soundness 层证据标准、`../SKILL.md` 因果语言强制词汇表同向；本文件管**主张层级（范围与强度）**，词汇表按**设计家族**管动词，两者互补。
> 适用：R3 主假设 claim 句、R5 经济显著性、Discussion 面向的 implication 句。生成前校准"主张层级 ≤ 证据层级"。

## Claim Ladder（7 级）

| 层级 | 语句型 | 需要什么证据 | 管理实证对应 |
|---|---|---|---|
| L1 Observation | "We observe that …" | 描述性统计 / model-free 证据 | R1 描述性统计、R1.5 Model-Free Evidence |
| L2 Association | "X is associated with Y" | 面板 OLS/FE，非因果 | 观察性基准（OLS/FE 设计家族的默认层级） |
| L3 Prediction | "X predicts Y under these conditions" | 条件效应 / 预测模型 | R4 交互 / 条件效应（带限定条件的陈述） |
| L4 Causal effect | "The effect of X on Y is …" | 识别设计（DiD/IV/实验）+ 对应诊断通过 | DiD / IV / 实验设计家族 |
| L5 Mechanism | "X changes Y through Z" | 中介检验或能区分渠道的设计 | R8 机制 / 中介分析 |
| L6 Generality | "This pattern holds across contexts" | 跨情境 / 异质性 / 多研究证据 | 异质性、多研究、边界条件 |
| L7 Application | "This can guide practice / policy" | 前序层级证据 + 具体决策者 | Discussion 实践启示 |

**规则**：证据支持 L_n，就不要写 L_{n+2} 或更高的故事。设计只支持 L2，Results 里不得出现 L5 语句；一条结果支持 L4，就不得在同一段写成 L6。

## 过度声明动词表

| 诱惑性写法 | 风险 | 更稳写法 |
|---|---|---|
| proves / demonstrates conclusively | 通常过强 | supports / is consistent with / provides evidence for |
| drives / causes / leads to | 暗示因果 | 按 `../SKILL.md` 因果语言强制词汇表（面板→"associated with"；DiD→"effect of"） |
| mechanism / pathway（作为已证） | 暗示过程证据 | possible mechanism / candidate pathway / consistent with |
| universal / general（无边界） | 暗示普适 | 明确 tested contexts 与样本范围 |
| transformative / paradigm-shifting | 无领域后果支撑的 hype | 具体说明读者能做什么、能推断什么 |
| first / novel（未查文献） | 优先权声明脆弱 | to our knowledge |
| explains（完整解释） | 过夸完整性 | helps explain / accounts for part of |
| reveals（非直接证据） | 暗示直接发现 | suggests / is consistent with |

## 强主张四件套句式

`Strong claim + scope + evidence basis + remaining uncertainty`

Results 示例（placeholder，不填真实数字）：

- 未校准："X 提高 Y。"（无范围、无证据锚、无不确定性）
- 校准："X 与 Y 正相关（β = [x]，SE = [x]；Table [n]），在本样本的 [识别设计] 下成立；该关系在 [稳健性子集] 中保持一致，但其因果解读取决于 [具体假设] 成立。"

Discussion 示例：

- 未校准："本研究证明 X 机制驱动 Y。"
- 校准："本研究提供了 X 通过 Z 影响 Y 的证据（限于 [样本/情境]）；直接机制检验仍受 [测量/设计限制] 约束，跨情境推广性需进一步检验。"

## 何时保留大胆声明（勿过度回缩）

下列条件全部满足时保留强主张，而不是改成怯懦的弱化句：

1. 设计直接检验该主张；
2. 关键替代解释已被处理（R7 稳健性）；
3. 主张范围与证据范围一致（L 层匹配）；
4. 含义从结果推出，而非从期望推出；
5. 不确定性被陈述，但不掩埋贡献。

**最佳校准不是"尽量小"，而是恰好等于证据允许的大小。** 弱化到比证据小的主张同样丢失信息——与目标层级"distinguish significant from credible evidence"纪律同向。不做过度回缩，也避免把弱证据包装成强结论（见 `anti-patterns.md` "基准支持冒充总体稳定"）。

## 校准问题（写 claim 句前逐条过）

- 现在这句最精确的主张是什么？
- 哪条证据直接支持它？哪条只是暗示？
- 还有哪个替代解释仍合理？
- 哪条结果是负的、null 的或限制性的？
- 什么样本、设计、测量、时段框定了它？
- 一个挑剔的审稿人会说我缺什么？
- 哪个词需要限定语？
