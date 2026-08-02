# Paragraph Layout — 段内论点-论据-总结句布局协议

本文件是**假设推导段落内部**的论证布局协议：一个假设推导段如何从论点句展开，如何选择并摆放论据（文献/理论/案例），如何收束。**职责边界**：
- 本文件 = **段内**（一个假设推导段内部如何布局）
- [`arrangement_patterns.md`](arrangement_patterns.md) = **段间**（多个假设段落之间如何组织，如 common trunk → parallel branches）
- [`hypothesis_derivation_patterns.md`](hypothesis_derivation_patterns.md) = **段落级骨架**（Anchor→Mechanism→Warrant→Prediction 完整序列）
- [`evidence_patterns.md`](evidence_patterns.md) = **论据细节**（每类论据的完整 pattern，本文件只做决策入口）

> **来源标注**：本文件整合四源——Dunleavy (LSE "How to write paragraphs") 的 Topic-Body-Tokens-Wrap 四段位与段内病理；Indiana University Writing Tutorial Services 的段落 coherence 技术；Belcher (2019) Week 2 的 Toulmin grounds-claim-warrant 与"argument = 吸引怀疑 + 提供证据"；Jonsen, Fendt & Point (2018) 的 first-order quote ↔ second-order theory 桥接修辞。凡标注"skill 操作化"处为本库综合，非原书原话。

---

## 1. 段内四段位模型（Topic → Reasoning → Tokens → Wrap）

来源：Dunleavy (LSE) 的 "Topic, Body, Tokens, Wrap" 序列。**核心洞察**：理性、扫读型读者对段首与段尾给予特殊关注（"速读"技术的依据），因此**段首句（Topic）与段尾句（Wrap）必须最精心撰写**。Dunleavy 原文："the beginning and endings of paragraphs should always be the most carefully written materials."

skill 操作化（适配 Theory 假设推导段）：

| 段位 | 功能 | 句数 | 写作要求 | 失败模式（Dunleavy 6 病理） |
|------|------|------|---------|---------------------------|
| **Topic（论点句）** | 本段的核心理论主张——不是话题，是对话题的**判断** | 1 句 | active verb + concrete subject（"We argue that [IV] [direction] [DV] through [mechanism]"）；15 词内说出核心判断（skill 经验阈值，见 `phase-3`） | ① burying the lead（核心判断淹没在第2-3句）；② throat-clearing 开场（"本节讨论..."元评论）；③ **作者名开头**（"Smith (2020) showed..."——信号"本段是衍生性的"，读者降级/跳过） |
| **Reasoning（机制推理）** | 从 Topic 到 Prediction 的 why-chain，每步显式 | 2-3 步 | 每步间 explicit transition（Consequently / Thus / This leads to）；不允许 A 直接到 C 的逻辑跳跃（"read my mind"病理）；交织式论证（文献嵌入推理，非先推理后堆引用，见 `phase-3` §交织式论证链） | ④ 逻辑跳跃（缺中间步）；⑤ 引用罗列（只有名字无 argument） |
| **Tokens（论据）** | 为 Reasoning 的关键步骤提供证据支撑 | 1-3 条 | 按"三类论据决策矩阵"（见下节）选择；每条论据必须**回扣**到它支撑的具体推理步骤，不能是泛泛装饰 | ⑥ 案例无理论回收句（"For example... X. Then H1."——案例摆完不回机制）；⑦ token 膨胀（案例/数据过多把段落撑到 300+ 词，见段内病理 ⑤过长） |
| **Wrap（总结句）** | 收束推理链，自然引出假设 | 1 句 | 总结推理（"Taken together, these arguments suggest..."）而非简单重复 "we hypothesize"；段末停在引用上而无 Wrap 是 "abrupt stop" 病理（见 `phase-3` QC） | ⑧ 突兀结尾（token 后直接假设，无 Wrap）；⑨ Wrap 与 Topic 不匹配（读者困惑"这段到底论证了什么"） |

**四段位骨架**（可直接套用）：
```
[Topic]     We argue that [IV] [direction] [DV] through [mechanism].
[Reasoning] First, [IV] induces [state 1], which [effect] (transition).
            Consequently, [state 1] leads to [state 2] because [reason] (transition).
            This in turn [final mechanism step].
[Tokens]    [按决策矩阵选 1-3 条论据，每条回扣到上述某步——见 §2]
[Wrap]      Taken together, these arguments suggest that [IV] [direction] [DV].
            Therefore, we hypothesize: H[X]: ...
```

> **与 Toulmin 的对应**（Belcher 2019 Wk2）：Topic ≈ claim；Reasoning ≈ warrant（推理原则）；Tokens ≈ grounds（数据/证据）。Belcher："argument 是吸引读者怀疑并提供证据克服怀疑的话语。"——Topic 要**值得怀疑**（非常识谚语，见 SKILL 反模式"常识谚语当机制"），Tokens 要**足够克服怀疑**。

---

## 2. 三类论据决策矩阵（核心交付物）

来源：把 `evidence_patterns.md` 已有的 4 类论据整合为统一决策入口。用户核心诉求——在文献/理论/案例间选择。**决策判据**：论据要回答"读者在这一推理步骤会怀疑什么"，不同怀疑用不同论据回应。

| 怀疑类型 | 读者在想 | 应使用的论据 | 详细 pattern（evidence_patterns.md） | 句式骨架 |
|---------|---------|-------------|--------------------------------------|---------|
| **"这真的会发生吗？"**（经验怀疑） | 这个机制步骤在现实世界中真的存在吗？有没有证据？ | **前人文献**（empirical finding） | Three-Element Citation | `[Author] (year) found that [concrete finding] — [argument summary]. This suggests that [mechanism step].` |
| **"凭什么这样推理？"**（逻辑怀疑） | 这个因果步骤的理论依据是什么？不是作者臆断？ | **经典理论**（conceptual warrant） | Theory as Warrant | `This is consistent with [theory], which posits that [core argument] ([foundational citation]).` |
| **"能让我看见吗？"**（具象怀疑） | 这个抽象机制在经验世界里长什么样？ | **现实案例**（case/illustration） | Case as Warrant for Mechanism Step | `For example, [company] [concrete situation]. As a result, [company] could not [action], suggesting that [mechanism step] operates in practice.` |
| （可选）**"这在实务界重要吗？"**（外部效度怀疑） | 这不只是学术象牙塔吧？ | **实务报告**（practitioner report） | Practitioner Report as Warrant | `According to a [year] [consulting firm] analysis of [N] [phenomenon], [finding]...` |

### 2.1 组合规则（单源 / 双源 / 三源）

- **单源**（最常见）：一个推理步骤用一类论据。机制链第一步常用**理论**（立合法性），中间步骤常用**文献**（实证锚定），最抽象步骤常用**案例**（具象化）。
- **双源**（推荐，增强说服力）：理论 + 文献（"合法且有据"）、理论 + 案例（"合法且可见"）、文献 + 案例（"有据且可见"）。
- **三源**（仅用于最关键/最反直觉的推理步骤）：理论 + 文献 + 案例。**警告**：三源会显著增加段落长度，超过 2 个步骤用三源 → 段落 >350 词 → 触发"段落过长"病理，应拆段。
- **禁忌组合**：理论 + 理论（两个理论 citation 无机制推演 = "citation list 冒充理论"反模式，见 SKILL 反模式速查）。

### 2.2 first-order quote ↔ second-order theory 桥接（Jonsen et al. 2018 借用）

案例类论据若用田野/访谈引语（first-order voice），必须桥接到 second-order 理论语言，不能让引语"自说自话"：
```
[first-order quote] As [informant] noted, "[direct quote showing the mechanism in their words]" ([citation]).
[bridge] This reflects [theoretical concept], whereby [mechanism explanation].
```
Jonsen et al. 强调：**tangible, plausible bridges** between first-order voices and second-order conceptualization 是说服力的关键（2018: "Convincing Qualitative Research"）。

---

## 3. 段内诊断清单（12 项）

来源：Dunleavy 6 病理（段位表）+ Indiana University coherence 四技。

### 3.1 段位病理（Dunleavy）
- [ ] **Topic 在第 1 句**：核心判断未淹没在第 2-3 句？（burying the lead）
- [ ] **Topic 非元评论**：段首句不是"本节讨论..."/"接下来..."？（throat-clearing）
- [ ] **Topic 非作者名开头**：段首句主语不是他人姓名？（"Smith (2020)..." → 读者降级）
- [ ] **Wrap 存在且匹配 Topic**：段末有总结句且回扣段首主张？（非突兀结尾 / Wrap 与 Topic 不匹配）
- [ ] **段落长度 100-250 词**：< 100 词（论证不足，合并）/ > 250 词（token 膨胀，拆分）。注：此为 Dunleavy 原文研究文本区间；Theory 假设推导段可放宽到 ~150-350 词（skill 经验阈值，见 `phase-3`）。
- [ ] **无 token 膨胀**：案例/数据未把段落撑到失控？（token 膨胀是"过长"主因）

### 3.2 coherence 技术（Indiana University Writing Tutorial Services）
- [ ] **关键术语重复一致**：同一构念全段用同一术语？（不 synonym 轮换构念名——Pollock Ch03）
- [ ] **平行结构**：并列的推理步骤/论据用平行语法？（"First... Second... Third..." 或 "When [W] high... When [W] low..."）
- [ ] **过渡词显式**：每步推理间有 Consequently/Thus/This leads to？（无"显然"/"不难发现"——read my mind 病理）
- [ ] **视角/时态/数一致**：未在 "we"/"this study"/"it" 间无故切换？

### 3.3 论据质量（skill 操作化）
- [ ] **每个 Token 回扣具体推理步骤**：不是泛泛装饰？（案例摆完有理论回收句）
- [ ] **三类论据搭配合理**：按怀疑类型选择，无"理论+理论"禁忌组合？

---

## 4. 与相邻语料文件的关系

| 需求 | 查的文件 |
|------|---------|
| 段内四段位骨架 + 论据决策 | **本文件**（paragraph_layout.md） |
| 论据的完整 pattern（每类的详细骨架+范文+反模式） | [`evidence_patterns.md`](evidence_patterns.md) |
| 段落级 Anchor→Mechanism→Warrant→Prediction 完整序列 | [`hypothesis_derivation_patterns.md`](hypothesis_derivation_patterns.md) |
| 连接词谱系 / 段落长度 / warrant 摆放三策略 | [`../sentences/mechanism_chain.md`](../sentences/mechanism_chain.md) §段内逻辑布局原则 (L695) |
| 交织式论证链（文献嵌入推理 vs 先推理后堆引用） | [`../../references/phase-3-hypothesis-derivation.md`](../../references/phase-3-hypothesis-derivation.md) §交织式论证链 |
| 段间多假设结构（common trunk / parallel branches） | [`arrangement_patterns.md`](arrangement_patterns.md) |

**使用顺序**：先查本文件确定段内四段位 + 论据组合 → 再查 evidence_patterns 填充具体论据句式 → 再查 mechanism_chain §段内逻辑布局原则 选连接词与 warrant 摆放策略。
