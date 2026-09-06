# Anti-Patterns — 反模式清单（从 SKILL.md 下沉，v0.1）

> 由 write-introduction 输出骨架时**逐条自查**（Phase 4 反模式扫描）。

| 反模式 | 修复 |
|--------|------|
| **稻草人**: 把文献描绘得比实际更片面 | 用 review/meta、代表性研究和反例共同验证立场；被引量只表示影响力，不能证明共识 |
| **弱缺口**: "few studies have examined" 无解释 | 说明既有假设、构念边界、层次或冲突预测为何产生理论 trouble；新数据/方法只能是可研究性条件 |
| **缺 Stakes**: Gap 后直接跳贡献 | Gap 和 Contribution 间插入 1-2 句 stakes |
| **过度承诺**: "revolutionize""first to" | 用 "extend""refine""reconcile""clarify" |
| **贡献散弹**: 5+个贡献各一行 | 聚焦 2-3 个，每个充分展开（**实证论文**默认；理论论文走 AMR 模式单核自明，见 `references/theory-paper-amr-mode.md`） |
| **期刊错位**: ASQ 用数据开场 / SMJ 无案例 | 查期刊适配表（`references/journal-fit.md`） |
| **缺少人脸**: Hook 用 "many firms" | 除非期刊偏好纯学术开场（JMS），补充 >=1 个具体 actor |
| **机器声**: "It is argued that" / "By examining..." | 改用 "We argue that" / 直接写研究问题 |
| **胖子西装**: P1 或前三段因背景堆积而推迟 puzzle、对话或 problematization | 以约 120/350 词作为诊断提示而非自动失败线；按期刊和功能密度压缩背景到 Lit Turn |
| **埋没主旨**: 段首句不是核心判断 | 段首句 = 主语 + 主动动词 + 方向/发现 |
| **Preview 无 motion**: "In the next section, we describe..." / 被动语态 | 用 "To test these arguments, we..." 主动切换场景 |
| **假区分**: 声称"不同于X"但实际区别仅是样本/行业/年份 | 区分必须基于理论构念或研究问题的不同——DV不同+IV不同是最低门槛 |
| **两个贡献实质是一件事**: 第二贡献只是第一贡献的 "also" | 每个贡献锚定不同文献流（Literature A → Literature B）或不同 Makadok 维度 |
| **显式RQ无理论层次**: 两个 RQ 并列且无关（如 RQ1=主效应, RQ2=不同的主效应） | RQ 应有递进：RQ1=主效应 → RQ2=边界条件/调节 |
| **构念重命名** (Constructs 专属): 新构念只是旧构念的重新标签——A=高X, B=低X | 嗅探：两个构念能否在同一实体上**同时为高**？能否同时为低？若回答"否"→ tautology。修：重新定义构念使其独立（pontikes2012: market-taker vs market-maker 与组织属性无关，与受众视角有关）|
| **作者名开头**: 段首句主语为 "Smith (2020)"，段落沦为文献注脚 | 段首换成自己的 claim，作者名移到句中证据位；见 prose-craft-checklist §0.6-1 |
| **清嗓开头**: 段首为 "Before turning to..." / "It is worth noting..." 热身句 | 删除，或压缩成只承担必要衔接/背景功能的短句；见 §0.6-2 |
| **孤儿引语**: epigraph/引语独立存在，后无 pivot 解读句 | 引语后必须接 "This quote captures..." 式 pivot；见 §0.6-3 |
| **引文堆叠无锚点** (citation lumping): ≥2 引文的句子中无任何引文带独立发现从句，综合退化为"范畴断言+句末堆引" | 拆为发现锚定从句（"finding with direction ([cite]), whereas contrasting finding ([cite])"），或删去无法说明发现的引文；合格线：任取一个引文可还原其发现方向；句式见 `literature-turns/literature-turn-templates.md` 变体D |
| **方向压平** (direction flattening): 把方向相反的发现概括进 "X 和 Y 都影响 Z" 式无方向类别句 | 恢复 whereas/but 对比结构，让每个发现的 valence 可见；Constructs / Mechanism distinction 类贡献强制检查——方向对比往往是贡献的立论前提 |
| **未回应显见异议** (unanswered objection): 读者对问题/框架最可预期的质疑全文无一被承认——引言读起来像写给没有其他观点的受众（Booth Ch09：论证不仅是逻辑构造，还是社会互动） | Phase 2 生成异议预判清单（quality-gates §4 Gate 4），对最强异议三选一：正文回应（标记词库借 `../write-theory/corpus/sentences/acknowledgment_response.md` §3–4）、显式 park 到后文节、诚实让步 |
