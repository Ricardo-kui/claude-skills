# 审稿意见解析、归类与优先级

本文件支撑 revision-coach 模式 A 的 Step 2–6。改编自 ARS `revision_coach_agent`,去掉了流水线专有机制,适配管理学实证论文。

## Step 1 · 收齐输入并校验

**收集**:
1. 审稿意见(必需)——接受任意格式:邮件粘贴、PDF 文本、编号列表、项目符号、自由段落、多审稿人混排。
2. 稿件草稿(可选但推荐)——用于精确分节映射。
3. 编辑决定信(可选)——用于把握总体裁决与编辑点名项。

**校验**:
- 审稿意见缺失或为空 → 要用户补。
- 全部意见合计过短(< 50 字)→ 确认是否就是全部。
- 内容疑似稿件本身(不是评审)→ 提醒用户并要求更正。

## Step 2 · 逐条解析

**切分分隔符(按优先级)**:
1. 显式审稿人标签:"Reviewer 1:" / "R1:" / "审稿人 1" / "Reviewer #1"。
2. 编号列表:"1." "2." 或 "(1)" "(2)"。
3. 项目符号:"-" "*" "•"。
4. 段落分隔:双换行且话题不同。
5. 话题转换:同一段内主题切换也要拆。

**每条抽出**:
- **审稿人 ID**:R1 / R2 / R3 / Editor / Unknown。
- **原文**:逐字保留。
- **一句话转述**:审稿人到底要什么。
- **语气**:Positive / Constructive / Critical / Unclear。

**歧义处理**:
- 一条里含多个独立要点 → 拆成多条。
- 审稿人身份不明 → 标 Unknown 并问用户。
- 含糊(如"需要进一步深化")→ 标 `NEEDS_CLARIFICATION`,问用户怎么理解。

## Step 3 · 归类(四类)

| 类型 | 定义 | 动作 |
|---|---|---|
| **Major** | 影响核心论证、方法或结论;不改很可能导致拒稿 | Must fix |
| **Minor** | 影响质量或完整性,但不影响核心有效性 | Should fix |
| **Editorial** | 语法、用词、格式、错别字、引用样式 | Quick fix |
| **Positive** | 肯定、认可优点、同意思路 | 回复信致谢,无需改稿 |

**归类信号**:
- "I strongly recommend…" / "This is a fundamental flaw…" / "cannot be accepted without…" → Major
- "It would be helpful to…" / "Consider adding…" / "A minor point…" → Minor
- "Typo on page…" / "Please check the formatting…" → Editorial
- "The authors do a good job of…" / "This is an interesting approach…" → Positive

## Step 3.5 · 承诺拆解(关键防漏点)

在分节映射**之前**,把每条审稿意见分解为**显式的可交付承诺**。一条意见可能含 0 个或 N 个具体承诺,每个都要单独追踪——这是堵住"一条意见里藏了三个要求,只回了一个"的漏点。

**做法**:
1. 读每条已解析的意见。
2. 识别祈使或隐含祈使短语:"please add" / "expand on" / "clarify whether" / "we suggest" / "it would strengthen" / "consider adding" / "请补充" / "建议" / "能否" / "需要进一步"。
3. 每个短语产出一个承诺对象:
   - `commitment_text`:逐字或最小归一化的承诺(如"对 X 子样本做异质性分析")。
   - `commitment_type`:`add_analysis` / `add_clarification` / `add_citation` / `restructure` / `add_experiment`(实证重跑)/ `other`。
   - `required_evidence_type`:满足它的证据在哪——`new_section` / `new_table` / `new_figure` / `new_citation` / `methods_paragraph` / `discussion_paragraph` / `prose_edit` / `acknowledgment_only`(仅回复信致谢,无需改稿)。
4. 无可拆承诺的意见(纯肯定、总结性致谢)→ 空列表 `[]`,合法。
5. 复合要求("请补充 X,并澄清 Y")→ 拆成两条,不要并成一条。

**输出示例**:
```yaml
- concern_id: R1-1
  commitments:
    - commitment_text: "对制造业子样本做异质性分析"
      commitment_type: add_analysis
      required_evidence_type: new_table
    - commitment_text: "解释为什么用固定效应而不是随机效应"
      commitment_type: add_clarification
      required_evidence_type: methods_paragraph
```

**注意**:这一步**不判断**承诺是否合理、作者是否该接受;只把结构摊出来,供后续体检(模式 B)核对是否兑现。

## Step 4 · 分节映射(管理学论文结构)

| 节 | 意见中的关键词 |
|---|---|
| Title / Abstract | "title" "abstract" "keywords" "标题" "摘要" |
| Introduction | "introduction" "motivation" "background" "引言" "动机" "贡献" |
| Theory & Hypotheses | "theory" "hypothesis" "mechanism" "literature" "理论" "假设" "机制" |
| Sample & Methods | "method" "sample" "data" "identification" "measure" "方法" "样本" "测量" "识别" |
| Results | "results" "findings" "table" "figure" "robustness" "结果" "表格" "稳健性" |
| Discussion | "discussion" "implications" "contribution" "讨论" "启示" "贡献" |
| Conclusion | "conclusion" "future" "limitation" "结论" "局限" "未来" |
| References | "references" "citation" "引用" "参考文献" |
| General | 整篇层面或落点不清的意见 |

若用户提供了稿件草稿,用真实节标题做更精确映射。

## Step 5 · 优先级

| 优先级 | 标签 | 标准 |
|---|---|---|
| P1 | `must_fix` | Major;编辑点名;不改会拒 |
| P2 | `should_fix` | Minor;审稿人"strongly recommend" |
| P3 | `consider` | 建议性、可选改进、editorial |

**提升规则**:
- 编辑在决定信里点名某条 → 提到 P1。
- 多名审稿人提出同一关切 → 提一级。
- 落在编辑点名节里的 Minor → 提到 P2。

## 边界情形(简表)

| 情形 | 处理 |
|---|---|
| 一条可归 Major 也可归 Minor | 默认 Major(保守),标出请作者确认 |
| 一条跨多节 | 按节拆成多条 |
| 一条是提问而非指令 | 归 Minor;建议动作="在正文与回复信中澄清" |
| 两条审稿人意见相左 | 标记矛盾,并列两种立场,问作者倾向哪个 |
| 只有一名审稿人 | 正常处理,在概述里注明 |
| 非英文意见 | 原文解析,转述译成作者偏好语言 |
| 含人身攻击/不专业用语 | 标记不专业,抽取可执行内容,建议作者必要时联系编辑 |

## 质量自检(产出路线图前)

1. **覆盖**:原文每条意见都有对应行。
2. **一致性**:相似意见归到同一类。
3. **分节准确**:每条映射到正确节(有稿件就对照核对)。
4. **优先级合理**:P1 确实比 P2/P3 关键。
5. **可执行**:每条非 Positive 都有具体建议动作(不能只是"改进这一节")。
6. **无遗留问号**:所有 `NEEDS_CLARIFICATION` 都已与作者澄清。
7. **无静默丢弃**:解析条数 ≥ 原文可识别意见数。
