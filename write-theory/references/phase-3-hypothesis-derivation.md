# Phase 3: hypothesis derivation

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

### Phase 3: 假设推导

Theory 写作的心脏环节：路由假设结构，为每个假设生成逻辑严密、论证充分、段内布局合理的推导段落。

**3.1 假设结构路由**

```
假设体系包含哪些类型的假设？
│
├── 纯主效应 (X→Y) → 基础关系模板
├── 主效应 + 中介 (X→M→Y) → 机制推演模板 + 中介假设模板
├── 主效应 + 调节 (X×Z→Y) → 调节效应模板
├── 调节 + 中介 (Moderated mediation) → 机制推演 + 调节混合
└── 三向交互 (X×Z×W→Y) → 假设树模板
```

**3.2 Hypothesis Development 段落级逻辑协议**

**每个假设推导段落是一个微型论证单元**。

> **核心目标**：本阶段是 Theory 写作的**心脏环节**。不管构建类型是机制推演、调节效应、假设树还是竞争假设，最终都要落实到假设推导段落。本阶段的任务是：为每一个假设生成一个逻辑严密、论证充分、段内布局合理的推导段落。

#### 语料调用（本阶段必读）

按假设推导段落的需要，依次读取以下语料文件。不要跳过：

1. **核心骨架**：`../corpus/subprotocols/hypothesis_derivation_patterns.md`
   → 选择适合的微观动作序列（Anchor→Mechanism→Warrant→Prediction 或 Puzzle Turn 或 Multi-Mechanism Trunk 等）

2. **段落安排**：`../corpus/subprotocols/arrangement_patterns.md`
   → 确定本段是 Warrant-Embedded、Parallel、Cumulative 还是 Evidence-Contrast

3. **证据摆放**：`../corpus/subprotocols/evidence_patterns.md`
   → 为每个 Mechanism Move 选择 Warrant 类型（文献/案例/理论/反事实）和引用句式

4. **微观动作补充**：`../corpus/subprotocols/argumentation_patterns.md`
   → 当需要特殊动作（如反直觉 Anchor、间接调节论证）时调用

5. **调节假设句法**（如适用）：`../corpus/subprotocols/bilateral_argumentation_templates.md`
   → 为调节假设生成 high/low 双边论证

6. **假设形式输出**：`../corpus/sentences/hypothesis_forms.md`
   → 把推导收敛为正式假设的标准句法

7. **可靠性审计**（成稿后执行）：`../corpus/subprotocols/reasoning_soundness_protocol.md`
   → 前提三分法标注 + 最弱环节防守 + 机制必要性门控 + 反例压力测试，输出 Soundness Card

#### 标准结构：交织式论证链（Interwoven Logic Chain）

文献引用与理论推理**交织**而非先后排列——这是管理学顶刊的默认写法（验证自 14 篇 MVP30 论文）。

```
[1. Topic Sentence]  →  [2. Theoretical Reasoning + Literature Support]  →  [3. Hypothesis Transition]
        ↓                         ↓                                              ↓
  本段的单一理论主张        多步因果链，每步由文献锚定：                      收束推理，引出假设
  (1-2句)                  "Prior research shows X. However, Y                  (1-2句)
                           remains unclear. We argue that Z
                           because [mechanism] ([citations])."
```

**具体展开**：
```
[Topic Sentence]  → 本段的理论主张（1-2句）
     ↓
[Reasoning Step 1] → 前人发现 + 前人 argument 总结 → "This suggests that..."
     ↓
[Reasoning Step 2] → 前人发现 + "However, [gap/puzzle]" → "We argue that..."
     ↓
[Reasoning Step 3] → 机制逻辑（可再加文献锚定）→ "Consequently..."
     ↓
[Convergence] → "Taken together, these arguments suggest... Therefore, H:"
```

**备选结构：分离式（少数情况使用）**——当某一步的文献支持特别密集、需要单独展开时，可将 [Reasoning] 和 [Literature Support] 暂时分离。但整个段落的默认节奏是交织的。

**各要素 QC**：

| 要素 | 必须做到 | 最常见失败模式 |
|------|---------|--------------|
| **Topic Sentence** | 同时包含话题+核心观点+限定范围；**必须使用 active verb + concrete subject**（如 "We argue that..." 而非 "It is argued that..."）；**段首句在 15 词内说出核心判断**；不宽泛不局限 | 太宽泛/太局限；**无主语被动语态**（"It is argued that"）；**Burying the lead**（核心判断不在段首句） |
| **Paragraph Architecture** | 每段满足 PEEL/PEAL：Point（topic sentence）+ Evidence（文献/数据）+ Explanation（机制分析）+ Link（与下段衔接）；段落长度 150–350 词 | 段落过短（缺少 evidence/explanation）；段落过长（包含多个论点）；缺少 explanation 导致 "So what?" |
| **Theoretical Reasoning** | 从 X 到 Y 的每一步因果推理都明确写出；**每步间有 explicit transition**（Consequently/Thus/This leads to...） | **逻辑跳跃**：省略关键推理步骤；**Read my mind**：缺少 transition，从 A 直接跳到 C |
| **Literature Support** | 总结前人研究的 argument/finding + 说明链接 | **引用罗列**：只有名字没有 argument |
| **Hypothesis Transition** | 收束句总结推理链，自然引出假设 | 无理论收束直接 "we hypothesize" |

**[2b. Concrete Illustration]（可选但推荐）**：
每个因果步骤后，可插入 1 句 concrete illustration：
- "For example, when [Company] faced [situation], [mechanism] produced [outcome]."
- 或用比喻："This is akin to [familiar scenario]..."
- 规则：不允许连续 2 个推理步骤无 illustration

**[3b. 文献引用的 Human Face 要求]**：
- 每个引用必须总结其 **argument**（非罗列），并链接到 **concrete finding**
- 例："[Author] et al. ([year]) showed that firms [taking action X] experienced [Y]% greater [outcome] than firms [taking action Z]—a finding consistent with our argument that..."

**逻辑跳跃诊断**：逐句标记因果连接词（Consequently/Thus/Thereby/As a result/This leads to...）。缺少中间步骤 → 存在跳跃。

**[2c. 识别策略的理论论证]**（制度冲击 / 自然实验研究必须包含）：

使用 IV / DiD / RDD 时，Theoretical Reasoning 的 why chain 中必须嵌入识别假设的理论论证——IV 的排除限制与第一阶段理论渠道、DiD 平行趋势的理论基础、RDD 断点局部可比较性。各策略在 why chain 中的嵌入位置与句式见 `../corpus/subprotocols/institutional_shock_lens.md` 第 4 节。

**检查**：如果 Methods 中描述了识别策略，但 Theory 段落中完全没有提及识别假设的理论基础 → ⚠️ 标记为"识别策略与理论脱节"。

**Topic Sentence CV 反模式示例**：
- ❌ "It is argued that CEO overconfidence affects firm risk." → 无主语被动，违反 Conversational Voice（见 `../../write-introduction/academic-writing-corpus/storytelling/prose-craft-checklist.md` 禁用词表）
- ✅ "We argue that CEO overconfidence increases firm risk-taking because overconfident leaders systematically underestimate downside uncertainty." → active verb + concrete subject + 方向性预测
- 规则：Topic Sentence 是段落的第一印象，若用被动语态，读者会预期整段都是"报告腔"而非"论证声"。

#### 段落级 QC 检查表

- [ ] 主题句精准度：是否同时包含话题+核心观点？
- [ ] **Burying the lead**：段首句是否在 15 词内说出核心判断？段首句不是元评论？
- [ ] 推理链完整性：每个因果步骤是否都在文中明确写出？
- [ ] **Read my mind**：每步因果推理间是否有 explicit transition？无"显然"/"不难发现"？
- [ ] 引用嵌入度：每个引用是否都总结了其 argument/finding？
- [ ] 术语一致性：同一构念在全段用的是否同一个术语？
- [ ] 证据-论点匹配：每个引用是否直接支持它所在推理步骤？
- [ ] **Sentence stuffing**：单句 ≤ 30 词？单句从属连词 ≤ 2 个？
- [ ] 收束句质量：是否总结了推理链而非简单重复 "we hypothesize"？
- [ ] 段落独立性：单独阅读本段能否理解完整论证逻辑？
- [ ] **作者名开头**：why-chain 段段首句主语是否为他人姓名（"Smith (2020) showed..."）？→ topic sentence 必须是自己的理论主张，引用移到证据位（见 prose-craft-checklist §0.6-1）
- [ ] **段末 wrap**：段末句是否停在引用/证据上而无 "This suggests that..." 收束（abrupt stop）？→ 段末 1 句 wrap 回扣本段 claim；与"收束句质量"项互补——那项查收束是否简单重复 "we hypothesize"，本项查收束是否缺席（见 §0.6-5）
- [ ] **Caveat-first**：段首是否以 "Although prior work..." 让步开头，推迟核心 claim？→ claim 前置，caveat 移后（见 §0.6-4）
- [ ] **前提最弱点**：每个 Anchor/Warrant 前提已标注 [D]/[S]/[E] 类型？最弱前提是否有单独一句防守（或已降级 claim / 转显式假设）？（见 `reasoning_soundness_protocol.md` §1–2）
- [ ] **机制必要性门控**：Q1 主流更简单机制推不出同一预测？Q2 本机制有可区分的额外预测？Q3 删掉本机制故事不照样成立？（见 §3）
- [ ] **反例压力测试**：最弱前提所在步骤与反直觉步骤已回答"什么条件下这一步不成立"，处置（scope / 新假设 / 删除）已兑现？（见 §4）

---
