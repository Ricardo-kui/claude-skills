# 变体 F：竞争假设型（Competing Hypotheses Variant）

> **适用**: 两种对立理论都有文献支撑，实证数据作为"理论裁判"
> **范文**: Wowak et al. (2025, MS)
> **最佳期刊**: MS ⭐⭐⭐⭐⭐ | AMJ ⭐⭐⭐⭐ | SMJ ⭐⭐⭐⭐
> **新增于**: write-theory 2.1.0

---

## 段落功能地图

| 段落 | 功能 | 推荐词数 | 必须度 |
|------|------|----------|--------|
| P1 | 界定竞争预测涉及的核心构念、关系与 scope；只有竞争来自两个构念/维度时才做双构念界定 | 80-150 | ✅ |
| P2 | 理论视角引入（Drawing on...） | 60-100 | ✅ |
| P3-P4 | 竞争机制推演（路径A vs 路径B，严格对称） | 各 70-120 | ✅ |
| P5 | 竞争假设形式化（H1a / H1b） | 各 30-60 | ✅ |
| P6-P7 | [可选] 第二因变量的竞争推演 + H2a/H2b | 各 70-120 | ⚠️ |
| P8 | [不推荐] 独立 Closure 段落——管理学标准是最后一个假设后即进入 METHODS | — | ✗ 非标准 |

> **注意**: 管理学顶刊不要求独立的 Closure 段落。竞争假设的对立收敛即为 Theory 的终点。

---

## 关键句式模板

**构念界定**：同一 X→Y 的理论冲突只需稳定界定 X/Y；若竞争确实来自双维度，再参见 `corpus/sentences/construct_definition.md` 变体 D。禁止为获得对称形式发明第二构念或维度。

**竞争预告**：
```
"However, the literatures on [领域A] and [领域B] offer potentially conflicting 
arguments as to the influence of [X] on [Y]."
```

**原文锚点**:
> "However, the literatures on recalls and political ideology offer potentially conflicting arguments as to the influence of TMT political ideology on recall counts."

**路径A论证**：
```
"On the one hand, [X_high] may [increase/decrease] [Y] because [mechanism_A]. 
Research suggests that [X_high] are more [特征] and, correspondingly, [行为] 
([文献]). In other words, this research argues that [X_high] tend to [行为2]."
```

**原文锚点**:
> "On the one hand, firms with more liberal TMTs may experience fewer recalls because of their socially oriented quality prioritization during product design and manufacturing. ... In other words, this research argues that more liberal TMTs tend to engage in firm activities that minimize detrimental outcomes to society."

**路径B论证**：
```
"On the other hand, [X_low] may [increase/decrease] [Y] because [mechanism_B]. 
Indeed, research indicates that [结果] can be particularly [后果], so [X_low] 
who tend to focus on [价值] may be more motivated to [行为3] ([文献])."
```

**原文锚点**:
> "On the other hand, firms with more conservative TMTs may experience fewer serious recalls because they appreciate the long-term financial value of prioritizing product quality during the design and manufacturing phases, reducing the risk that products subsequently fail in the market and require a recall."

**竞争收敛（非传统 Therefore）**：
```
"Given these competing arguments, we put forth the following hypotheses for 
how [X] may influence [Y]:"
```

**原文锚点**:
> "Given these competing arguments, we put forth the following hypotheses for how liberal and conservative TMTs may influence a firm's recall count:"

---

## 假设陈述格式

| 类型 | 模板 | 示例 |
|------|------|------|
| 竞争假设对 | "H1a: [X] is [negatively/positively] related to [Y]. H1b: [X] is [positively/negatively] related to [Y]." | H1a: Liberalism → fewer recalls. H1b: Liberalism → more recalls. |

**原文锚点**:
> "Hypothesis 1(a). There is a negative relationship between top management team liberalism and the count of recalls. Hypothesis 1(b). There is a positive relationship between top management team liberalism and the count of recalls."

---

## 子协议索引

- **F1 主动管理读者/文献中的竞争预测**：参见 `corpus/subprotocols/argumentation_patterns.md`（**Preemptive Competing Account Management**——F 的核心微观动作：在读者提出反对前主动呈现并处理竞争解释）
- **F2 竞争基线 → 调节裁决（与 E4 的边界）**：参见 `corpus/subprotocols/argumentation_patterns.md`（competing_baseline_moderation_resolution）。**区分判据**：单一理论内部两个响应的竞争 → E4（调节裁决）；两个独立理论的竞争预测 → F（本变体）
- **F3 双机制汇聚 / 双理论两阶段**：参见 `corpus/subprotocols/argumentation_patterns.md`（dual_mechanism_same_direction / dual_theory_two_stage_iv）——当两条路径并非严格对立而是汇聚/分期时使用

---

## QC 检查点

- [ ] 路径A和路径B的论证是否**对称**（文献数量、论证长度、机制深度大致相等）？
- [ ] 两个竞争假设是否都源于**独立理论**（非同一理论的反面表述）？
- [ ] 竞争收敛信号是否使用 "Given these competing arguments" 而非 "Therefore"？
- [ ] Discussion 是否包含 "理论裁判" 解释（为什么路径A成立而路径B不成立）？
- [ ] 是否排除了 "一个假设明显更强" 的不对称风险？
- [ ] 竞争假设是否通过 "Given these competing arguments..." 自然收束？

---

## 进阶技巧（wowak2025）：自反性反机制 + 多 DV 递进竞争

> 以下两个技巧使竞争假设超越"两个理论各执一词"的初级形态，提升理论密度。源自 Wowak et al. (2025, MS) 第二个 DV（time-to-recall）的更复杂推导。

### 技巧 1：自反性反机制（Self-Counter-Mechanism via "Conversely"）

**核心**: 竞争机制不必来自两个对立理论或两个对立群体；**同一价值取向/同一群体内部**可衍生自反性反机制——驱动某行为的同一倾向，也内含削弱（甚至反转）该行为的种子。这把竞争从"人际/理论间"升级到"价值内在张力"。

**句式**:
```
[直觉预测 + 机制] One could argue that [X_high] would [behavior_A] because
[reason 1: their value orientation]. [X_high] may also view [behavior_A] as
[responsibility / moral duty] ([citation]).

[自反性反机制] Conversely, if [X_high] [the very tendency that predicted behavior_A],
it could foster [psychological state—e.g., overconfidence / risk perception / rigidity]
that [result] ([citation]), resulting in [behavior_OPPOSITE]. This line of thinking
is consistent with studies showing that [state] can result in [decision-making bias]
([citation]), which, in our context, may result in [behavior_OPPOSITE].
```

**原文锚点**:
> "One could argue that more liberal TMTs would recall products faster because not doing so might harm consumers, particularly in cases involving serious product quality issues. ... Conversely, if more liberal TMTs prioritize quality during product design and manufacturing, it could foster a sense of overconfidence that the product is better (i.e., of higher quality) than it actually is (Schwartz 2019, Reis 2020), resulting in slower response time when making recall decisions."

**wowak2025 范例（time-to-recall）**:
- **Liberal 直觉**: 自由派关心消费者/社会责任 → recall 更快
- **Liberal 自反性反机制**: 自由派优先质量投入 → **过度自信**产品优于实际 → 更慢识别质量问题 → 把问题归因于 random failure 而非 design/manufacturing → recall 更慢
- **Conservative 直觉**: 保守派关注股东财务 → responsive recall 财务最优 → recall 更快
- **Conservative 自反性反机制**: 保守派风险厌恶/不确定性回避 → 害怕 **"false alarm"**（不必要召回的财务惩罚）→ recall 更慢；且 hierarchical, internally structured processes 拖慢决策流程

**为什么有效**:
- 比单纯"两理论对立"理论密度更高：揭示**同一价值的内在张力**（quality orientation 既是质量保障，也是过度自信的来源）
- "overconfidence"/"false alarm" 等具体心理-行为机制让竞争不只是方向对立，而是**有机制内容的对立**
- 两极（liberal/conservative）各有**概念不同的**自反性反机制 → 形成对称且丰富的 2×2 机制空间

**禁忌**:
- 自反性反机制必须有**独立文献支撑**（如 overconfidence 引 Schwartz 2019, Reis 2020）——不能只是常识断言
- 两极的自反性反机制必须**概念不同**（liberal=overconfidence；conservative=false-alarm fear）——若两极用同一反机制则冗余
- 反机制必须真正"翻转"方向（faster → slower），而非只是"减弱"——只是减弱应路由到 [E] 调节效应型

### 技巧 2：多 DV 递进竞争（Progressive Multi-DV Competing Elaboration）

**核心**: 当同一 IV 对**多个 DV** 产生竞争预测时，第二个（及后续）DV 的机制空间可**比第一个更丰富**——通过引入自反性反机制，从 2-mechanism（每极一个）升级到 4-mechanism 2×2（每极两个自反性机制），最终仍折叠为一对竞争假设。展示"丰富机制空间 → 简洁假设"的压缩能力。

**递进结构（wowak2025）**:

| DV | 机制空间 | 折叠为 |
|----|---------|--------|
| DV1 (recall count) | 2-mechanism: liberal-fewer（quality priority）vs conservative-fewer（financial value of quality） | H1a (−) / H1b (+) |
| DV2 (time-to-recall) | 4-mechanism 2×2: liberal-faster（responsibility）vs liberal-slower（overconfidence）；conservative-faster（financial）vs conservative-slower（false-alarm fear） | H2a (−) / H2b (+) |

**句式（DV2 的 2×2 折叠）**:
```
[极 A 直觉]   One could argue that [X_high] would [behavior_A] because [mechanism].
[极 A 自反]   Conversely, [X_high]'s [same tendency] could foster [state] resulting
              in [behavior_OPPOSITE].
[极 B 直觉]   On the other hand, [X_low] may [behavior_A] because [mechanism].
[极 B 自反]   Conversely, [X_low]'s [tendency] may result in [behavior_OPPOSITE]
              because [mechanism].
[折叠收敛]    Given the above competing arguments, we put forth the following
              hypotheses for how [X] may influence [DV2]:
              H[X]a: [X] is [negatively] related to [DV2].
              H[X]b: [X] is [positively] related to [DV2].
```

**原文锚点**:
> "Conversely, firms with more conservative TMTs may recall products more slowly because of their tendency to be risk-averse and uncertainty-avoidant (Jost et al. 2007). In our context, these tendencies for risk aversion and uncertainty avoidance may result in more conservative TMTs recalling more slowly to avoid the risk of a 'false alarm,' or issuing a recall when it is not necessary."

**为什么有效**:
- 多 DV 研究中，每增加一个 DV **不应机械重复**同样的 2-mechanism 结构；自反性反机制让后续 DV 的理论论证逐级加深，避免"复制粘贴式"假设
- 2×2 → 一对竞争假设的折叠，展示了高理论密度与简洁假设形式的统一

**禁忌**:
- 第二个 DV 的机制必须**真正不同于**第一个 DV（time-to-recall 的 overconfidence 机制不适用于 recall count）——不能只换 DV 重复同样论证
- 2×2 的四个机制都必须可独立引用支撑，不能为追求对称而凑数
- 折叠后仍用 "Given the above competing arguments"（**非 Therefore**）收敛——竞争假设收敛信号不变（参见 write-theory C14）
