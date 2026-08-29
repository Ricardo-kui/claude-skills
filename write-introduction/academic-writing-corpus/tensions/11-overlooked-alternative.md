---
type: canonical_reference
canonical_id: "11-overlooked-alternative"
status: 🔬 EXPERIMENTAL
gap_type: Inadequacy
cross_paper: SINGLE-INSTANCE
generativity: ADAPTABLE
exclusivity: MEDIUM
source_papers:
  - zhao_ding2022 (OS, 2022): "Supply-side focus overlooked demand-side explanation for digital market entry"
created: 2026-05-19
source: Extracted from MVP30 narrative_analysis files
---

# 11-overlooked-alternative — 被忽视的替代解释张力

## 功能定义

指出文献中一个系统性的解释偏倚：学界默认从某一侧（如供给侧）解释现象，却始终忽略另一侧（如需求侧）的解释。这种偏倚不是偶然的，而是源于学科范式的"路径依赖"。

## 适用场景

- 研究领域存在明显的"默认解释"（如从企业内部/供给侧解释一切）
- 存在另一个理论上可行的替代解释（如需求侧、外部反馈、制度环境）
- 目标期刊接受视角转换型论证（OS、SMJ、ASQ）
- 替代解释能产生不同于主流解释的实证预测

---

## 句法模板

### 变体 A：供给侧 vs 需求侧转向型（zhao_ding2022 型）

**模板**:
> "The dominant approach to explaining [phenomenon] has focused on [supply-side/actor-internal factor] — namely, [specific factors]. This emphasis is understandable given [context]. However, this [supply/internal]-side focus has overlooked a more fundamental driver: [demand/external factor]. We argue that [actor]'s [decision] is better understood not by [internal orientation] but by [external cue]."

**来源**: zhao_ding2022 (OS), adapted

**原文锚定**:
> "Prior studies document how digitization expands product variety and heterogeneous positioning in settings such as film and music but have paid less attention to how entrants decide which positions to occupy. We complement this work by identifying external market feedback as a key driver of positioning decisions."

**关键特征**:
- 先承认主流解释的合理性（"understandable given"）
- "overlooked a more fundamental driver" → 精准但不过度攻击
- 明确宣布替代解释的优越性

---

### 变体 B：战略替代型

**模板**:
> "[Literature X] suggests that [actor] responds to [standard driver]. Yet, [actor] faces an alternative route: rather than [strategy A], they could [strategy B]. Under what conditions does this overlooked alternative become viable?"

---


### 变体 C：既存解释实证反驳型（westphal_bednar2005 型）

**模板**:
> "[Dominant theory] suggests that [actors] are well positioned to [remedial action] ([citations]). [Actor subgroup], in particular, should be less likely than [other actors] to [biased behavior], because [reason 1] and [reason 2] ([citations]). Yet there is considerable [qualitative/anecdotal] evidence that [remedial action] often fails, regardless of [conventional remedy's presence] ([citations]). One explanation for this failure is that [rival mechanism] ([review citation]). Empirical evidence does not consistently support this explanation, however: although [weakly supporting evidence domain], there is less evidence that [rival mechanism] affects [focal outcome]; moreover, [direct field/survey evidence against]. In this study, we offer a different explanation for why [puzzle]: [new mechanism]."

**来源**: westphal_bednar2005 (ASQ), P2-P4

**原文锚定**:
> "Empirical evidence from the corporate governance literature does not consistently support this explanation, however."
> "In this study, we offer a different explanation for why boards may often fail to prevent strategic persistence in the face of poor performance."

**关键特征**:
- 与变体 A 的区别：不是"文献忽视了替代解释"（overlooked），而是替代解释已在场、被公平陈述后用证据反驳——说服动作是"反驳既存解释"而非"揭示盲区"
- 双层证据反驳结构：先承认部分支持证据（"Although there is some evidence that..."），再指出核心结果上证据缺失（"there is less evidence that..."），最后补直接反向证据（"moreover, survey research suggests..."）
- 先 steelman 后反驳：rival explanation 以 "One explanation ... is that" 中性句式引出，避免稻草人化
- "a different explanation" 单句转轴把攻击对象限定在解释力而非文献整体，过渡零摩擦

**适用**: Inadequacy × Mechanism；现象存在主导理论预期 + 一个现成但证据不充分（mixed/inconsistent）的解释；适用于"监督者/纠偏者失灵"类谜题（董事会、监管者、审查者未能纠正偏差行为）的研究场景

**禁忌**: 反驳必须分层给证据（间接证据弱 + 直接证据反向），只引一处不支持的研究会被质疑选择性引用；rival explanation 必须以其最强形式陈述，不得弱化后再反驳；"different explanation" 之后必须立即给出新机制名称，不能只说"我们换个角度"

## 组装规则

### 必须配对
- **与 `01-cross-disciplinary-analogy` (Hook) 配对**: 跨学科引入常常带来被本领域忽视的替代视角
- **与 `05-literature-consensus-blindspot` (Hook) 配对**: 共识建立后揭示"视角偏狭"

### 反模式提醒
- **假替代**: 两个解释其实是同一机制的两个名称 → 必须证明替代解释基于不同的理论逻辑
- **替代但无后果**: 替代解释没有改变预测 → 替代解释必须产生不同于主流解释的推论
- **过度强调新颖性**: 忽略了已有少量文献也在用这个替代视角 → 必须承认先行者，但指出它们未系统化检验

---

## 期刊适配

| 期刊 | 适配度 | 注意事项 |
|------|--------|---------|
| OS | ⭐⭐⭐⭐⭐ | 理论创新型论文欢迎视角转换 |
| ASQ | ⭐⭐⭐⭐☆ | 适合制度理论中的视角重构 |
| SMJ | ⭐⭐⭐☆☆ | 可用，但需展示替代解释的战略后果 |
| AMJ | ⭐⭐⭐☆☆ | 可用，但需清晰的机制链 |

---

## 相关语料

- 配合 `hooks/01-cross-disciplinary-analogy.md` 使用：跨学科引入常带来被忽视的替代解释
- 配合 `hooks/19-forward-looking-shift.md`（全局）使用：视角转移型 hook 直接预告替代解释
