---
name: revision-coach
description: "收到审稿意见或 decision letter（R&R、major/minor revision）后：解析为 Revision Roadmap + Response letter 骨架，或审计已有回复稿的覆盖缺口与风险。不代写修改稿本身。"
when_to_use: "任何涉及审稿意见解析/回复信/修改路线图的任务；触发词：审稿意见、R&R、response letter、rebuttal。"
whenToUse: Use when the user has received reviewer comments or a decision letter and needs a revision roadmap, a response-to-reviewers skeleton, or an audit of an existing rebuttal draft. Trigger words: 审稿意见, R&R, major revision, 回复审稿人, rebuttal, response letter, 帮我理一下审稿意见
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
2. **识别编辑决定类型(Belcher Week X 七种)** — 若提供决定信,先用 `references/editorial-decision-types.md` 判定属于哪一种(unconditional accept / warm R&R minor / warm R&R major / desk reject / cool R&R / rejected-dismissed / rejected-no-reports)。决定类型决定 urgency 与姿态:warm R&R→最高 urgency 快速重投;major R&R warm→标准全流程倾向重投同刊;各类 reject→不走修订流程转期刊选择;cool R&R→呈现重投 vs 改投权衡。这是按"决定类型"的第二维度分流(与按输入形态的模式 A/B 分流互补)。
3. **逐条解析** — 按分隔符切分(R1/R2/编号/项目符号/分段/话题转换),每条抽出:审稿人 ID、原文、一句话转述、语气。
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
- **实证类要求**(重跑回归、换识别、加稳健性):交 `causal-analysis`(再路由到 `did-analysis` / `econometrics-agent` / `stata` / `empirical-pipeline-stata`),或规格搜索交 `xianzhu-skill`。
- **整体投稿前 QC**:交 `pollock-qc` / `paper-review`（总控：叙事诊断 + `toc-review` 实质红队双层，一份统一报告）。路线图完成后、下次投稿前，可先跑 `toc-review` 做弱点预判，其清单可直接作为路线图预演素材。
- 本 skill 只产出"改什么、按什么顺序、回复怎么搭骨架、回复体检",不越界做上面这些事。

## 审稿信号回流（critique-driven，路线图交付后的收尾步骤）

R&R 产出后,把**审稿人反复质疑的方法/写作论点**登记回 write-* 批评 registry(`corpus/_evidence_registry.yaml`)。审稿人是比日常用户批评更高权重的信号源(editor 背书 + 跨轮次重复出现);登记后直接进入下一轮蒸馏的 critique_heavy 判定(revise + reject ≥ 2 → REPLACE/EXTEND 优先),与 Phase 0.75 选材闭环。

**登记条件**(只登写作可改进点,避免噪音登记):
- 同一方法/写作论点**跨审稿人或跨轮次(R1/R2)反复出现**;或
- 针对论证结构/报告方式(而非实证结果本身)的质疑——结果层面的拒绝属于论文缺陷,不属于语料缺陷,不回流。

**映射规则**:审稿质疑 → 论文主分析估计器/设计 → registry 键名
- 主分析估计器 → results registry `estimators` 键(如 `OLS_FE`、`DiD`、`生存分析`)
- Methods 设计 → methods registry `by_design_type` 键(如 `面板数据-OLS`、`自然实验-DiD`)
- 同一质疑可双侧登记(如"稳健性检验组织混乱"→ methods M8 与 results R7 双侧)

**执行**(回复骨架交付后):

```bash
# critiques.yaml 格式(同 distill Phase 4.5):
# critique_updates:
#   - estimator_family: "OLS_FE"    # results 侧键名(estimator_family);methods 侧用 design_type
#     verdict: "revise"             # revise=需大改 / reject=被弃用重写
#     reason: "审稿人 R1#2 与 R2#5 两轮均质疑 R3 经济显著性缺幅度翻译"
#     date: "YYYY-MM-DD"            # 可选,默认今天
python ../distill-results-exemplar/_update_registry.py --record-critique critiques.yaml
python ../distill-methods-exemplar/_update_registry.py --record-critique critiques.yaml
```

登记后可选跑一次体检确认 critique_heavy 触发:`python ../corpus_health_check.py --type both`。

## 需要按需读取的参考文件
- 解析 / 归类 / 承诺拆解 / 优先级规则:`references/comment-parsing.md`
- 路线图 + 回复信骨架 + 追踪表模板 + 工作量估计:`references/roadmap-and-response-template.md`
- 回复体检(模式 B)协议:`references/rebuttal-audit-protocol.md`
- 审稿人参与模式 + 接受/抵抗规则 + 真实回复句式(GBL Ch5):`references/gbl-r-and-r-dynamics.md`( storyline-level 意见识别、pushback 姿态预填、回复姿态审计时读取)
- 编辑决定七分类 + 应对策略(Belcher Week X):`references/editorial-decision-types.md`(模式 A step 2 决定类型识别时读取——判定 warm/cool R&R / desk reject / rejected 后决定 urgency 与重投 vs 改投姿态)
