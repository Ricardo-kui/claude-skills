---
type: rhetoric_move
canonical_id: "additional-analysis-embedding"
name_zh: "嵌入型补充分析"
cross_paper: VERIFIED
created: 2026-08-24
updated: 2026-08-25
expansion_state: saturated
pattern_count: 4
distinct_sources: 3
expansion_note: "verbatim 2 源（Lee-Wu-Bednar OS 假设探测 / Darby2026 JOM 稳健性收束）+ 模板 1 源（moon2026 替代冲击）。扩源暂停；resume=新补充分析类型（如 subgroup 事前分层）。"
---

# 修辞动作：嵌入型补充分析（Embedding Additional Analyses in the Results Narrative）

## 动作定义（学什么）

把**补充分析**（前提探测、替代冲击复现、稳健性收束）**织进 Results 正文的叙事流**，而不是压进附录或做成孤立清单。每个补充分析自带"**为何做 → 测什么 → 结论收窄到什么程度**"的三段小循环，读者读完正文就已经完成了对证据强度的判断，不需要翻附录。

**为什么值钱**：附录是"读者不信时才去查"；嵌入是"让读者在流水中就信"。审稿人看到嵌入的前提探测会认为你**预见过质疑**；看到收束句会认为你**管得住范围**。这比事后堆 robustness 高一个论证层。

**三种嵌入方式（跨源已验证，2026-08-24）**——同一"把补充分析织进正文"动作，三篇论文各在一处用：
- **前提探测嵌入（Lee, Wu & Bednar, OS）**：主结果之后直接问"机制的可观察前提是否成立"，用一组补充回归**逐一核对前提**，并允许某个中介出现领域特定 null。
- **替代冲击复现嵌入（moon2026, JM，模板）**：正文内嵌"换一个相关但不同的政策采纳作替代冲击"的小节，复现主结论后回指附录表格。
- **稳健性收束嵌入（Darby2026, JOM）**：收束段一句话点明"做了 N 项稳健性检验，涵盖 [威胁类别清单]"，再一句"共同支持全部假设"——把附录的机器细节压缩成叙事裁决。

## 结构蓝图（可迁移骨架——不是可抄句子）

> 1. **嵌入点**：出现在主结果之后、下一个假设/异质性之前，不另起新 section
> 2. **动机句**：说明这个补充分析针对哪个可观察前提 / 替代解释（"To empirically assess this assumption…"）
> 3. **操作句**：交代测什么、怎么构造（对照测度 / 替代冲击样本 / N 项检验的威胁清单）
> 4. **裁决句**：逐项报结果（哪些一致、哪个 null 是领域特定），并**诚实标注范围**（corroborative / consistent with，不说 confirms）
> 5. **衔接回主叙事**：一行转回主结果继续往下走

**关键纪律**：每个补充分析**必须绑定一个明确的理论前提或威胁**——不为凑篇幅；出现领域特定 null 时应**收窄理论适用范围**而非"总体大致一致"吞掉。

## 信号词表（通用功能词，自由使用）

- **嵌入点衔接**：To empirically assess this assumption / Before moving to heterogeneity / An additional lens on the mechanism / Turning to the observable implications
- **动机句**：We next probe whether / A potential critique is that / we examine [trace outcome] to assess whether
- **操作句**：we regress [X] on [Y] / we construct an alternative treated and control group / we test if our conclusions are robust in an alternative empirical setting
- **裁决句**：is consistent with the visibility premise / consistent empirical support for our thesis / but not with higher [outcome] / the null for [mediator C] suggests that
- **收束句**：we conducted [N] checks to validate our findings / Taken together, these analyses illustrate the robustness of our results / These analyses corroborate selected premises but do not identify the causal mechanism

## 改写指引（如何用自己的话说）

1. **先问"这个补充分析绑定哪个前提"**：没有可观察前提/威胁可绑 → 不要嵌入，那是凑数。有 → 动机句一句话点破。
2. **换测度、换样本、换威胁清单**：Lee/Wu/Bednar 的"national newspaper coverage"→ 换你的传播/追踪结局；moon2026 的"alternative policy adoption"→ 换你的替代冲击；Darby 的"19 checks + threat list"→ 换成你的威胁类别清单（选配变量、遗漏、反向因果、测量、策略）。
3. **裁决句要诚实分级**：一致的中介用 "consistent with"；出现 null 的中介用 "suggests that this actor may operate through…"，把理论范围收窄——这是审稿人最看重的信号。
4. **嵌入不等于堆砌**：一段一节、每节一裁决；超过 3 个嵌入点就退回附录汇总表 + 正文一收束句。
5. **衔接句必须存在**：补充分析结束要一行转回主结果，否则读者在附录式细节里迷路。

## 参照句（可直接采用或改造；替换来源特异性内容）

**参照 1 —— Lee, Wu & Bednar（*Organization Science*；前提探测嵌入，原文直引）**：
> "To empirically assess this assumption, we regress national newspaper coverage, analyst coverage, and credit rating coverage on firms' CSR engagement … higher CSR engagement is indeed associated with increased national newspaper coverage and greater analyst attention, but not with higher credit rating coverage."

**参照 2 —— Darby2026（*Journal of Management*；稳健性收束嵌入，原文直引）**：
> "We conducted 19 robustness checks to validate our findings and address potential concerns surrounding the selection of matching covariates and matching method, omitted variables, simultaneity and reverse causality, measurement error, multicollinearity and outliers, and empirical strategy. Taken together, these analyses illustrate the robustness of our results and provide additional support for all three hypotheses."

**参照 3 —— moon2026（*Journal of Marketing*；替代冲击复现嵌入，模板重建）**：
> "In addition, we also test if our conclusions are robust in an alternative empirical setting that uses [related but distinct policy adoption] as an alternative shock. … We estimate the simple diff-in-diff models on these alternative treated and control groups and find consistent empirical support for our thesis (see [appendix table] for more details)."

## 改写演示（重点是通顺、符合学术表达规范、句长适中）

**演示 A（前提探测嵌入，换对象到召回机制）**：
> "To empirically assess this assumption, we regress media queries, agency inquiry speed, and insurer renewals on firms' recall events. Higher recall activity is indeed associated with increased media coverage and greater analyst attention, but not with higher renewal premiums; the null for renewals marks the boundary of the mechanism."

**演示 B（稳健性收束嵌入，换威胁清单到召回设计）**：
> "Reviewers typically worry that our estimates ride on design choices rather than the underlying pattern. We conducted a battery of robustness checks to validate our findings and address concerns surrounding the selection of matched controls, the exposure window, and the coding of severe versus minor events. Taken together, these analyses illustrate the robustness of our results and reinforce support for our hypotheses, with the full battery reported in the appendix."

**流畅性自查**：演示 A/B 与参照共享的是**可迁移骨架**——Lee/Wu/Bednar 的 "To empirically assess this assumption" + "两个一致一个 null" 三段结构、Darby 的 "We conducted [N] checks … to validate our findings and address concerns surrounding" + "Taken together, these analyses illustrate the robustness of our results"。共享句全部落在骨架句上，直接采用即可；对象与威胁清单（media queries / agency inquiry speed / renewal premiums / matched controls / exposure window）须按你的对象替换来源特异性内容。过流畅性门（通顺、句长适中、主谓宾可识别）即交付。

## 自查勾子

- **不设重复率闸门**（2026-08-25 用户裁决）：语料语句可直接采用，只需替换来源特异性内容（专名/数字/系数/表号）；质量闸门是流畅性门（通顺、符合学术表达、句子不过长），见 `_polish-protocol.md`。
- 补充分析若**绑定不了明确前提/威胁** → 回改写指引第 1 条，改做附录汇总而非嵌入。
- 出现领域特定 null 却写"总体大致一致" → 回信号词表"裁决句"纪律，必须收窄范围。
- 嵌入点 ≥3 而无收束 → 读者迷路；退回"附录汇总表 + 一段收束"。
- **扩源暂停（saturated）**：已达 3 篇论文（2 verbatim + 1 模板），暂停继续加锚点；resume=用户点名 / 新补充分析类型（如 subgroup 事前分层、跨设计复现）。

## 关联
- 姊妹动作（同一 results 叙事工具包）：`counterfactual-reversal`（嵌入的反证类补充）、`conditional-payoff-closing`（裁决句后把结果翻译成条件性结论）。
