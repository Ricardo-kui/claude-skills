---
type: rhetoric_move
canonical_id: "counterfactual-reversal"
name_zh: "反向证伪"
cross_paper: single
created: 2026-08-24
updated: 2026-08-25
expansion_state: open
pattern_count: 3
distinct_sources: 2
expansion_note: "verbatim 一源（Castellaneta 2017 SMJ 假处理 placebo），moon2026 为模板级结构二源。resume=第二篇 verbatim 锚点到手即标 VERIFIED。"
---

# 修辞动作：反向证伪（Counterfactual Reversal / Fake-Treatment Placebo）

## 动作定义（学什么）

R7 识别确证动作：不满足于"效应存在"，而是**把处理逻辑反着做**——理论说 X↑→Y↑，那就找一个"X 被撤销"（treatment reversal）或"假 X 发生"（fake treatment）的情境，预期得到**相反符号**或 **null**。看到"反转/归零"才是识别成立。

**为什么值钱**：正向效应可以被混淆变量、趋势、同步事件冒充；反向证伪把赌注压在**逻辑本身**上——如果机制真成立，撤销处理应当产生镜像后果。它把"安慰剂"从 Methods 的补充检查升级为 Results 里识别确证的高潮段落。

**三种执行方式（2026-08-24）**——同一动作，三种镜像：
- **处理撤销反事实（moon2026，模板）**：某州先采纳后撤销 [制度]，以撤销组为处理组、仍保留组为对照组，预期**相反符号**。直接检验"正→反"的因果方向。
- **假处理安慰剂（Castellaneta 2017 SMJ，verbatim）**：把处理假装发生在 [±k 期]，预期 fake treatment 的**主效应与交互同时不显著**。
- **替代结局安慰剂（moon2026，模板）**：换一个理论不预测的结局变量（如一般经营费用），预期无效应——排除"处理只是普遍抬高了某类活动"的替代解释。

## 结构蓝图（可迁移骨架——不是可抄句子）

> 1. **威胁点名**：明确"可能被人质疑的是 [某个反事实/替代解释]"
> 2. **镜像构造**：描述如何构造反事实（撤销组 / 假处理时点 / 替代结局）
> 3. **预期声明**：先写"如果 [X]→[Y] 成立，那么 [反事实] 应产生 [相反符号/null]"
> 4. **结果 + 证据回指**：报告系数与显著性，回指到"consistent with our expectations" / "does not support the alternative argument"
> 5. **识别结论**：把反事实结果**翻译回因果方向断言**，不要停在系数上

**关键纪律**：预期 null 必须**预先声明**（不能事后说"我们本预期显著"）；反事实结果若是非预期，必须当 identification threat 报告，不得沉默。

## 信号词表（通用功能词，自由使用）

- **威胁点名**：To rule out the possibility that / A potential alternative explanation for the observed effect could be that / To address the concern that
- **镜像构造**：we create a placebo treatment by pretending that / offer a natural empirical setting for counterfactual analysis / using alternative dependent variables that reflect
- **预期声明**：we expect the fake treatment to have a weaker (or even null) effect / rejection is expected to have the opposite effect / if [X] increases [Y], [reverse] is expected to
- **结果回指**：neither the direct impact nor any interaction is significant / has a significant [opposite-sign] effect / we do not find empirical support for the alternative argument
- **识别结论**：These results are consistent with the direction we propose / the reversal corroborates the causal reading / the contrast provides evidence that

## 改写指引（如何用自己的话说）

1. **先选镜像类型**：你的识别威胁是什么？时间错置 → 假处理安慰剂；撤销样本 → 处理撤销反事实；替代解释 → 替代结局安慰剂。一种威胁对应一种镜像，别混搭。
2. **换对象、换机制、换句式**：Castellaneta 的"pretending that the change occurs ±k"→ 换到你的处理时点（"as if the reform had landed [m] years earlier than it did"）；moon2026 的"rejection is expected to have the opposite effect"→ 换到你的撤销事件。
3. **预期与结果分离写**：先一句"应该怎样"，再一句"实际怎样"；两句话之间用结果证据隔开，别压缩成一个"结果如预期"。
4. **识别结论要敢说**：反事实通过后，明说"这支持 [X]→[Y] 的因果方向而非 [替代解释]"——这是本动作的交付物。
5. **对照 zhang-idd 拒稿教训**：该稿的失败是"正文写着 results remain robust，附录却系统性复现负主效应"——反证若出现，必须**在正文显式叙述**，而不是让附录替你打脸。

## 参照句（可直接采用或改造；替换来源特异性内容）

**参照 1 —— Castellaneta, Conti & Kacperczyk（2017, *Strategic Management Journal*；假处理安慰剂，原文直引）**：
> "We expect the fake treatment to have a weaker (or even null) effect on the dependent variable when compared with the actual treatment. Consistent with this idea, we find that neither the direct impact of our 'placebo treatment' nor any interaction is significant; results are shown in Table S3."

**参照 2 —— moon2026（*Journal of Marketing*；处理撤销反事实，模板重建，非原文直引）**：
> "Counterfactual analysis: treatment reversal. These rulings that reject [treatment] offer a natural empirical setting for counterfactual analysis. If [treatment] increases [outcome] of [units], [treatment] rejection is expected to have the opposite effect on [outcome]. … we find that [treatment] rejection has a significant [negative/opposite-sign] effect on [outcome] (coef = [value], p = [threshold]), which is consistent with our expectations."

**参照 3 —— moon2026（*Journal of Marketing*；替代结局安慰剂，模板重建）**：
> "Placebo tests with alternative dependent variables. A potential alternative explanation for the observed [positive] effect of [treatment] on [outcome] could be that it reflects a general increase in [overall operating costs / broader category] following [treatment]. … we do not find empirical support for the alternative argument that [treatment] is likely to lead to a general increase in [broader outcome category]."

**反向案例（zhang-idd-advertising-rejected，2026-08-23 复盘）**：用户稿件 "Beyond Employee Retention…"（SMJ/JAMS 两轮拒稿）对照 moon2026 的失败模式——① 调节全模型中处理主效应由正转负（−0.101, p=.008），正文仍写 "results remain robust"；② 附录表系统性复现负主效应仍无叙述；③ 用被处理影响过的变量当交互预测下游结果宣称 "confirms the mechanism"（bad-controls，两轮评审当场抓获）。**本 move 的正确用法与失败稿相反**：主动构造反事实去预期反转，且反转出现时在正文显式讨论。见 `story-blueprints/v4/blueprints/zhang-idd-advertising-rejected.md`。

## 改写演示（重点是通顺、符合学术表达规范、句长适中）

**演示 A（假处理时点安慰剂，Castellaneta 骨架保留预期声明 + 结果回指）**：
> "We expect the fake treatment to have a weaker effect than the actual treatment, so we reassigned the reform to a window two years earlier than the true roll-out, a timing shift that carries no legal force. Consistent with this idea, we find that neither the direct impact of the mis-timed reform nor any interaction is significant — the misplaced shock leaves recall activity indistinguishable from zero."

**演示 B（处理撤销反事实，moon2026 骨架保留 "natural empirical setting for counterfactual analysis / rejection is expected to have the opposite effect / consistent with our expectations"）**：
> "The repeal rulings, which we read as a natural empirical setting for counterfactual analysis, give us a built-in reversal experiment. If mandatory disclosure increases recall initiation among covered firms, its rejection is expected to have the opposite effect on recall timing. Comparing firms in repeal states against firms whose mandate never lapsed, we find that repeal has a significant negative effect on recall speed, consistent with our expectations."

**流畅性自查**：演示 A 借 Castellaneta 的 "We expect the fake treatment to have a weaker (or even null) effect" + "Consistent with this idea … neither the direct impact … nor any interaction is significant"；演示 B 借 moon2026 模板的 "natural empirical setting for counterfactual analysis"、"rejection is expected to have the opposite effect"、"consistent with our expectations"。共享句集中在骨架句，直接采用即可；镜像构造与对象（reassigned the reform / mis-timed reform / repeal rulings / mandate never lapsed）须按你的对象替换来源特异性内容。过流畅性门（通顺、句长适中、主谓宾可识别）即交付。

## 自查勾子

- **不设重复率闸门**（2026-08-25 用户裁决）：语料语句可直接采用，只需替换来源特异性内容（专名/数字/系数/表号）；质量闸门是流畅性门（通顺、符合学术表达、句子不过长），见 `_polish-protocol.md`。
- 预期 null 若**未预先声明**就写"结果如预期"→ 是事后合理化，回信号词表"预期声明"纪律。
- 反事实若得到**非预期显著结果**却沉默 → 复制 zhang-idd 拒稿模式；必须当 identification threat 报告。
- 把交互当机制确证（bad-controls）→ 对照反向案例第三条。
- **扩源开放（open）**：目前 verbatim 仅 1 源（Castellaneta）；待第二篇 verbatim 锚点到位即升级 VERIFIED 并转入饱和。

## 关联
- 姊妹动作（同一 results 叙事工具包）：`conditional-payoff-closing`（反证结果翻译成条件性结论）、`additional-analysis-embedding`（把反证作为嵌入段落而非附录堆料）。
