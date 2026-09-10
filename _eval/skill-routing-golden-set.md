# Skill 路由黄金集 v1

> **用途：** 诊断"skill 为什么没被用起来"的回归测试集。每条 = 真实用户口吻请求 + 期望首选技能。测试：零上下文子代理只给原始请求，回答首选技能；对比计分。目标首选命中率 ≥80%。
> **条目来源：** 2026-09-10 会话真实请求 + 用户技能清单触发词。v1 · 2026-09-10。
> **判分规则：** 命中期望首选 = hit；命中可接受备选 = half；其他/未路由 = miss。miss 条目进 feedback 待登记（用户裁定后再入 registry）。

| # | 请求（原文口径） | 期望首选 | 可接受备选 |
|---|---|---|---|
| G1 | 我已经跑完回归，但不知道这个设计能声称什么 | check-methodology | run-empirical-research |
| G2 | 这组交错 DID 应该用哪个估计量 | staggered-did | did-analysis（仅当明确要求 R） |
| G3 | vault 里找关于共同所有权的论文 | vault-search | zotero-cli |
| G4 | 隔了两周，继续「共同所有权 × 产品召回」项目 | run-empirical-research | — |
| G5 | 根据这些结果重写 Methods | write-methods | — |
| G6 | 帮我写 Results 部分 | write-results | — |
| G7 | 审一下我的 Theory 部分写得怎么样 | theory-review | — |
| G8 | 全稿投稿前帮我做一次审查 | paper-review | pollock-qc（快速 QC 时） |
| G9 | 收到 R&R decision letter 了，帮我规划修改 | revision-coach | — |
| G10 | 开始写引言，hook 和 gap 怎么处理 | write-introduction | — |
| G11 | 这段英文太像 AI 写的，帮我升级表达 | polish | humanizer（纯去 AI 腔时） |
| G12 | 压力测试我的贡献主张 | grill-the-claim | — |
| G13 | 帮我定义因果问题，该用 DiD 还是 IV | huntington-klein-causal-design | — |
| G14 | 审计我的数据，先别改任何东西 | stata-data-cleaning | — |
| G15 | 期刊要 AI 使用声明，怎么写 | ai-disclosure | — |
| G16 | 这两篇论文的新颖性对辩一下 | tod-debate | — |
| G17 | Discussion 部分帮我看看 | discussion-review | — |
| G18 | 读这篇论文，做成证据卡笔记进 vault | literature-notes-obsidian | — |

**测试参数（v1 基线）：** 载体 = pi-subagents `delegate`（零上下文）；cwd = C:\Users\admin；子代理可自行查看 `C:\Users\admin\.agents\skills` 与 `C:\Users\admin\.pi\agent\skills` 的技能清单（等价于真实会话的启动横幅）；输出格式强制 `SKILL: <名或NONE> | 一句话理由`。

## v1 基线结果（2026-09-10）

**18/18 首选命中，命中率 100%（门槛 ≥80%）。** 零 miss，无条目需进 feedback-registry。

诚实限定：① v1 条目多带明确触发词，区分度高——真正会 miss 的是模糊请求（“帮我看看这个”）、复合请求（一句话含两个意图）与近邻技能对（polish vs humanizer、check-methodology vs run-empirical-research）；② 子代理能读技能 description，与真实会话信息条件一致，但不能完全代表多轮真实对话中的路由；③ 结论：当前触发词覆盖对明确请求已足够，“没被用起来”的主因不是路由失败，而是重入成本（已由双向重入协议解决）。v2 建议：加入 6–8 条模糊/复合/近邻对抗条目后再面件评估。

执行注：18 并发会触发供应商 429 限流，须按批 ≤5 并行 + 失败串行重试。
