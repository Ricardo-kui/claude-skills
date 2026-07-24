# Phase 5: quality control

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 5 — 质量验证与 QC 输出

生成最终的蒸馏质量报告。

### QC Checklist

#### 功能层 QC（原有）
- [ ] **Completeness**: 所有强制模块（根据 Gap×Contribution 组合）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和适用 Gap 类型标注
- [ ] **Credibility**: 未将单篇论文的特殊现象泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的模块
- [ ] **No Verbatim Copy**: 输出中未出现可直接追溯到原文的连续 8+ 词短语
- [ ] **Fact Boundary**: 所有不可迁移事实（特定现象、行业名、具体学者名）已被明确标记
- [ ] **Gap-Type Fidelity**: 骨架的标志性语言与 Gap 类型匹配（Incompleteness!="conflated"）
- [ ] **Dorobantu Coverage**: 核心问题链（Puzzle/Audience/RQ/Constructs）都有对应模块
- [ ] **Combo Honesty**: 未将 Incommensurability 的骨架错误归类为 Incompleteness

#### 叙事层 QC（Pollock Ch02-Ch05，v2.1.0 新增）
- [ ] **Central Knot 贯穿性**: 如已推断 central_knot，检查每个段落是否服务于该 knot
- [ ] **叙事阶段顺序**: 段落功能按 Exposition → Rising Action → Denouement 推进，无阶段倒退
- [ ] **Characters 秩序**: 主角 ≤2、配角 ≤3、群演不出现在前 3 段
- [ ] **前端一致性**: Title/Abstract/Introduction 的 central knot 描述一致（如有 Title/Abstract）
- [ ] **Narrative Arc 能量守恒**: Hook 能量级 ≤ Gap 能量级 ≤ Stakes 能量级

#### Prose QC 层（Pollock Ch03，v2.1.0 新增）
- [ ] **Human Face**: Hook 中 >=1 个具体 actor（人名/公司名/机构名）？
- [ ] **Showing**: 每个 major construct 有 concrete illustration（例子/数字/场景）？
- [ ] **Conversational Voice**: 无 "It is argued that" / "It is shown that" / "It is hypothesized that"？
- [ ] **Contribution Voice**: Contribution 用 "We extend/refine/reconcile..." 而非 "This study contributes by..."？
- [ ] **无 Inflated Symbolism**: 无 "paradigm shift" / "fundamentally transforms"？
- [ ] **Read-aloud 测试**: Hook + Contribution 大声朗读是否自然？
- [ ] **Fat Suit 控制**: P1 ≤ 120 词，前 3 段 ≤ 350 词？前 3 段背景占比 ≤ 60%？
- [ ] **Burying the Lead**: 每段段首句在 15 词内说出核心判断？段首句不是元评论？
- [ ] **Sentence Stuffing**: 无单句 > 30 词？无单句含 > 2 个从句？无单段 > 150 词只有 1-2 句？
- [ ] **Read my Mind**: 每段与前一段有 explicit transition？无"显然"/"不难发现"？因果推理无跳跃？
- [ ] **Pompous Prose**: 无 unnecessary nominalization / jargon / 过度正式化？可用降级词表替换？

### 最终输出物清单

1. **Fine-Grained Profile**（单篇）或 **Batch Aggregation Report**（批量）
2. **Expression Skeleton Corpus**（新增骨架列表，含 Gap 变体）
3. **Rhetorical Logic Map**（Audience/Puzzle-Gap-RQ/Contribution Contract 处理模式）
4. **Introduction DNA Metrics**（可对比的量化指标）
5. **Dorobantu 问题链覆盖度表**
6. **Corpus Reference Notes**（供人工审阅的语料库沉淀注释，不自动修改 skill）
7. **QC Result**（通过/需修正/拒绝入库）
8. **Narrative Risk Ledger**（模仿风险提示，见下）

### Narrative Risk Ledger（叙事风险台账）

借鉴 paper_factory 的 `audit_issue_ledger.md`：蒸馏过程发现的原文叙事薄弱点不是要被"修复"（论文已发表），而是作为**"模仿风险提示"**记录，防止用户在模仿时踩坑。

**台账格式**：

```markdown
# Narrative Risk Ledger: [作者_年份_期刊]

| 风险ID | 发现阶段 | 风险类型 | 原文表现 | 模仿后果 | 建议处理 |
|--------|----------|----------|----------|----------|----------|
| R1 | Phase 1.5 (Stakes 压力测试) | Stakes 薄弱 | "This is theoretically important" (generic) | 模仿后审稿人问 So what? | 替换为同类型其他论文的具体 Stakes 骨架 |
| R2 | Phase 2 (Tension 提炼) | Gap 语言模糊 | 同时使用 "remains unclear" + "overlooks" | 模仿后 Gap 类型定位不清 | 明确选择一种 Gap 类型，不要混合标志性语言 |
| R3 | Phase 2.4 (骨架批评) | 骨架过度抽象 | Tension 骨架提炼为 "We study X" | 失去组织叙事的启示 | 保留关键功能短语 |
| R4 | Phase 1.5 (对齐检查) | Contribution→Theory 断裂 | Contribution 承诺 Mechanism 但 Theory 无中介假设 | 模仿后 Introduction 承诺无法兑现 | 确保 Theory 部分的假设与 Intro 贡献声明严格对齐 |
| R5 | Phase 3 (Prose QC) | Fat Suit | P1 > 120 词或前 3 段 > 350 词 | 读者迟迟看不到 central knot | 压缩背景到 Lit Turn；P1 只保留理解 paradox 的最小上下文；采用倒金字塔 |
| R6 | Phase 3 (Prose QC) | Burying the Lead | 段首句未在 15 词内说出核心判断；段首句是元评论 | 读者只读段首句时无法判断论证方向 | 重写段首句为"核心判断句"：主语+主动动词+方向/发现；元评论移到段尾 |
| R7 | Phase 3 (Prose QC) | Sentence Stuffing | 单句 > 30 词或含 > 2 从句；单段 > 150 词只有 1-2 句 | 阅读负担过重，核心判断被淹没 | 拆分为 2-3 短句；每句一个核心判断；括号内容独立成句或删除 |
| R8 | Phase 3 (Prose QC) | Read my Mind | 段落间无 explicit transition；因果推理从 A 直接跳到 C；使用"显然""不难发现" | 读者无法跟随推理链条 | 每段段首加 transition 信号词；why chain 每步用 1 句话说明；删除"显然"类表述 |
| R9 | Phase 3 (Prose QC) | Pompous Prose | 不必要的 nominalization（"the transformation of"）、jargon（"utilize""leverage"）、过度正式化 | 显得做作、不自然 | 用降级词表替换为直接表达；nominalization 改回动词；Read-aloud test 检测 |
| R10 | Phase 3 (Prose QC) | 无人脸 | Hook 用 "many firms" 而非具体公司名；Gap 用 "some studies" 而非具体论文 | 缺乏可信度和代入感 | 每个关键槽位补充 >=1 个具体 actor |
| R11 | Phase 3 (Prose QC) | 机器声 | "It is argued that" / "This study contributes by" / "By examining..." | 像模板自动生成而非研究者写作 | 改用 "We argue that" / "We extend" / 直接写研究问题 |
```

**记录原则**：
- **不修复**：论文已发表，薄弱点是客观存在的
- **不美化**：不能为了让骨架"好看"而掩盖原文问题
- **可行动**：每条风险必须附带"建议处理"，告诉用户如果模仿此处该怎么做
- **跨论文可比较**：批量模式下，同类型风险的频率可作为"该组合类型的常见陷阱"沉淀

---
