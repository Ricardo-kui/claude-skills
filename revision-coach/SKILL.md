---
name: revision-coach
description: Use when the user receives peer-reviewer comments or a decision letter (R&R, major/minor revision, revise-and-resubmit, desk reject with resubmission invitation) and wants to (a) parse the comments into a structured Revision Roadmap + Response-to-Reviewers letter skeleton, or (b) audit an existing response/rebuttal draft for coverage gaps and risk flags. Trigger on "审稿意见", "我收到审稿意见了", "R&R", "major revision", "minor revision", "revise and resubmit", "回复审稿人", "response letter", "rebuttal", "审稿意见没回完吗", "帮我理一下审稿意见", "parse reviews", "revision roadmap". Do NOT use this skill to rewrite manuscript sections (use write-* / humanizer) or to re-run empirical analysis (use causal-analysis / stata / stata-regression). This skill plans and QA's the author's response; it does not write the revision itself or fabricate that a comment was addressed.
---

# Revision Coach — R&R 解析规划与回复体检

## 目标
把一份(往往混乱的)审稿意见 + 决定信,变成一份**可执行、无遗漏、可贴回**的修改路线图与回复信骨架;或对作者已写好的回复草稿做一次**逐条覆盖体检**。它解决 R&R 阶段最常见的两个失败:**漏点**(某条意见没回)与**错位**(回复没回答审稿人真正问的)。

它**不**负责:重写正文(交给 write-* / humanizer)、重跑实证(交给 causal-analysis / stata)、或替作者决定要不要 push back(只呈现信息与风险,决定权在作者)。

## 硬边界
- **No comment left behind**:每一条审稿意见都必须被解析、归类、出现在路线图里,不得静默丢弃。
- **保留审稿人原意**:转述时忠实于审稿人想说的,不夸大、不弱化、不曲解。
- **rebuttal-audit 只做体检、不代写**:它对已有回复草稿出 advisory 报告,**绝不**生成新回复、**绝不**标记"已可投稿"或"全部已回应"、**绝不**伪造某条已解决。
- **不伪造证据**:回复里声称"新增了分析/表格/段落"的,必须指向稿件中真实存在的位置;实证类要求(重跑回归、换识别)要如实标注"需交由 causal-analysis / stata 执行",不要在回复里编造结果。
- **作者拍板**:是否 push back、是否追加数据,由作者决定;本 skill 只给出 pushback 的可行性、风险与建议姿态(接受/抵抗决策规则与真实回复句式见 `references/gbl-r-and-r-dynamics.md` §2–3)。

## 两种模式(按输入形态判定)

### 模式 A:revision-coach(解析规划)— 生成骨架
- **输入**:审稿意见(必需,任意格式)+ 稿件草稿(可选)+ 编辑决定信(可选)。
- **输出**:Revision Roadmap(分类 / 优先级 / 分节映射 / 修改顺序)+ Response-to-Reviewers 骨架(每条意见一个占位回复块)+ 可选修改追踪表。
- **判定信号**:用户只有审稿意见、还没写回复;或说"帮我理一下审稿意见""怎么改""revision roadmap"。

### 模式 B:rebuttal-audit(回复体检)— 只审不写
- **输入**:审稿意见 + 已有的回复/反驳草稿(两者都必须有)。
- **输出**:逐条覆盖表(addressed / partially / missing)+ 缺口清单 + 风险标记(语气过冲、无证据的断言、误读审稿人论点)+ 改进建议(advisory)。
- **判定信号**:用户两样都给了,且说"帮我看看回复""漏没漏点""check my rebuttal""审稿意见回完了吗"。
- **路由铁律**:只有审稿意见、没有回复草稿 → 走模式 A;两样都有 → 走模式 B;不清就问,不要猜。

详见 `references/rebuttal-audit-protocol.md`。

## 标准工作流(模式 A)

1. **收齐输入** — 审稿意见(必需)、稿件草稿与决定信(可选);做输入校验(意见缺失/过短/疑似贴错成正文都要先问)。详见 `references/comment-parsing.md`。
2. **逐条解析** — 按分隔符切分(R1/R2/编号/项目符号/分段/话题转换),每条抽出:审稿人 ID、原文、一句话转述、语气。
3. **归类** — Major(影响核心论证/方法/结论)/ Minor(质量完整性)/ Editorial(文字格式)/ Positive(优点,回复信里致谢)。识别 **storyline-level comments**(涉及 framing/contribution/focus/"what is the paper about" 的意见)——它们是 front/back 重写预告,工作量按 Substantial 起估;编辑点名的收窄要求("too many goals"/"contribution unclear")一律 P1(规则见 `references/gbl-r-and-r-dynamics.md` §1)。
4. **拆解承诺** — 把每条意见拆成具体的可交付项(加分析 / 加澄清 / 加引用 / 改结构 / 其他),并注明"满足它的证据在哪"(新表格 / methods 段 / discussion 段 / 仅致谢等)。详见 `references/comment-parsing.md` 的"承诺拆解"。
5. **分节映射** — 把每条映射到管理学论文的标准节:Title/Abstract、Introduction、Theory & Hypotheses、Sample & Methods、Results、Discussion、Conclusion、References、General。有稿件就用真实标题。
6. **排优先级** — P1 must_fix( Major / 编辑点名 / 不改会拒)/ P2 should_fix / P3 consider,并套用提升规则(编辑点名提一级、多人同问提一级)。详见 `references/comment-parsing.md`。
7. **生成路线图 + 回复骨架** — 见 `references/roadmap-and-response-template.md`;给出修改顺序建议与工作量估计(Light / Moderate / Substantial / Fundamental)。
8. **交给作者确认** — 先把解析结果交作者核对,再产出最终路线图;有 NEEDS_CLARIFICATION 的条目必须先问清。

## Storyline 级意见的 story contract 锚点(与 write 栈协同)

审稿人要求收窄/重定位 storyline 时(见 `references/gbl-r-and-r-dynamics.md` §1.2–1.3),处置前先读项目 `paper-state.yaml` 的 canonical `story`(如不存在,经 `/paper-story-contract` 反向诊断一个 provisional contract):

- **与 contract 冲突**(要求换掉 central knot / 主角 / 核心 storyline)→ R3 抵抗候选:向作者呈现冲突点、抵抗姿态(§3-B 句式)与风险,由作者拍板。
- **不冲突**(在既有 story 内收窄聚焦)→ 接受,并在路线图中标注"修改完成后同步更新 story contract",防止 contract 与修订稿漂移。
- 无 paper-state.yaml 的项目:跳过本锚点,按现有流程(不降级)。

## 与你已有栈的分工
- **实际重写正文某节**:路线图产出后,逐节交给 `write-introduction` / `write-theory` / `write-methods` / `write-results` / `write-discussion`;语言润色与去 AI 味交 `humanizer` / `proofread`。**路线图的每一行就是交给下游的工单**——"意见转述 + 责任节 + 兑现证据位置"三列原样传给对应 write-*/review skill,不重新转述(保留审稿人原意)。修改 storyline 的工单必须先过上面的 story contract 锚点。
- **实证类要求**(重跑回归、换识别、加稳健性):交 `causal-analysis`(再路由到 `did-analysis` / `econometrics-agent` / `stata-regression`),或规格搜索交 `xianzhu-skill`。
- **整体投稿前 QC**:交 `pollock-qc` / `paper-review`。
- 本 skill 只产出"改什么、按什么顺序、回复怎么搭骨架、回复体检",不越界做上面这些事。

## 需要按需读取的参考文件
- 解析 / 归类 / 承诺拆解 / 优先级规则:`references/comment-parsing.md`
- 路线图 + 回复信骨架 + 追踪表模板 + 工作量估计:`references/roadmap-and-response-template.md`
- 回复体检(模式 B)协议:`references/rebuttal-audit-protocol.md`
- 审稿人参与模式 + 接受/抵抗规则 + 真实回复句式(GBL Ch5):`references/gbl-r-and-r-dynamics.md`( storyline-level 意见识别、pushback 姿态预填、回复姿态审计时读取)
