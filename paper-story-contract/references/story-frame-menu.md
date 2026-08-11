# Story Frame Menu — 故事框架选择菜单（v0.1）

> 消费 `../story-blueprints/` 语料（knot 类型词表与原型状态的唯一权威 = `../story-blueprints/_schema.md`；各型实例计数 = `../story-blueprints/blueprints/_index.md` knot 主型列实时统计；布局实证见 `../story-blueprints/layout-inventory.md`）。给定研究描述，生成 2-3 个候选故事框架（knot 类型 × 解法性格），由用户拍板后写入 story 契约的 `story_frame` 字段。
> **Gate**：发生在 Story Intake（theme_question + central_knot 初判）之后、契约定稿之前。菜单是**选择工具不是强制模板**——用户可拒绝全部候选自定框架；被拒候选记入 `alt_frames`（含拒绝理由）。
> **多原型优先（≥2 份 blueprint 实证）**：优先级 irony-reversal / paradigms-at-war / neglected-arena / overlooked-alternative / half-domain-gap / consensus-puzzle / assumption-flip / tangled-constructs（实例计数动态演进，以 `_index.md` 统计为准）；单原型（cross-domain-unification）与待建（paradox）使用时需对照原型 blueprint 的"适用/禁忌"核对前提。

## Step A: 冲突定位诊断（研究描述 → knot 类型候选）

从研究描述判断**冲突发生在哪里**（一个问题可以命中多条，全部列出作候选）。

> **⚠️ 区分两类命中（2026-08-09 实测缺陷修正）**：诊断命中分两类，**不要混为同级候选**——
> - **knot 候选**（本步产出）：冲突的**位置**（现象内 / 文献共识 vs 现实 / 两阵营 / 子域空白…）→ 下表 10 问
> - **对话策略信号**（非 knot）：研究描述里"与某篇具体论文的差异化"（如"与 Qiao 2026 按不同轴区分"）属于 **Conversation 策略层**（Progressive / Synthesized / Non-Coherence，见 `literature-turns/_index.md` 3×3 矩阵），由 Intro 的 literature turn 处理——**不要**把它包装成 overlooked-alternative 候选。判断规则：若差异化的对象是一篇/一类具体论文（"extend along a different axis"），是对话策略；若主流视角是**集体共识**（"Most research underscores..."可实指多篇），才是 overlooked-alternative knot。


| # | 诊断问题 | 命中 → knot 类型 |
|---|---------|----------------|
| 1 | 同一 X 对**不同对象/受众**意义相反，或行动产生与预期相反的结果（监督制造地下化、解药变毒药）？ | `irony-reversal` 反讽反转 |
| 2 | **文献强共识预测**被行为/证据/条件持续违背（共识说惩罚，行为还在用）？ | `consensus-puzzle` 共识谜团（结构性异质性或条件）；纯宏观对照点则取 `counterevidence` 子结构增强 |
| 3 | **两套立场**（两个理论 / 同一构念两极）各持完整观点推出相反预测？ | `paradigms-at-war` 范式对决 |
| 4 | 现象/子域**整个没人做**（文献注意力移走或从未到达）？ | `neglected-arena` 被忽视战场 |
| 5 | 现象**已被研究**但主流视角看漏一个**替代面**（manage 做了 remove 没做）？ | `overlooked-alternative` 主导视角批评 |
| 6 | 两个**构念被混同/单向化**，实为动态关系？ | `tangled-constructs` 构念纠缠 |
| 7 | 现象有**天然双极**（equity/debt、成功/失败、进入/退出），一极已做一极空白？ | `half-domain-gap` 互补半区 |
| 8 | 两个**分离研究域从未对话**，可由同一机制统一解释？ | `cross-domain-unification` 跨域统一 |
| 9 | **文献共识的前提本身可疑**（挑战隐含假设）？→ 用 `../diagnose-introduction/references/assumption-challenging.md` 的五类假设定位挑战的是哪一类（in-house / root-metaphor / paradigm / ideology / field）——`field` 类=跨传统共享的深层挑战（可升级 overlooked-alternative 领域级变体）；`in-house` 类=单一传统内部；root-metaphor/paradigm 类风险最高需论证跑道 | `assumption-flip` 前提倒置（**六原型实证**——paruchuri2020/shipilov2020/hahl2017/lovelace2021/darby2025/li2026；骨架见讲法汇编家族 10） |
| 10 | 纯悖论现象（违背常理、无文献派别、无共识可挑战）？ | `paradox`（**待建类型**——提示用户该框架无实证原型，建议重构为上面某型） |

## Step B: 解法性格选择（研究者姿态 → resolution 候选）

与 knot 正交，但受倾向配对与研究者姿态约束：

| 研究者姿态（用户偏好） | resolution 候选 | 倾向配对 |
|----------------------|----------------|---------|
| "我要**整合出新的**"（两派各对一半 → 新形状） | `arbitration` 仲裁 | paradigms-at-war |
| "我要**展示被忽略的**"（换视角/解结/翻面/换镜头/拉开幕布） | `revelation` 揭幕（最通用——irony/overlooked/assumption-flip/tangled **100% 实证**，neglected 2/9、consensus 5/7 亦常见；见 layout-inventory 联合分布） | 任意（neglected 主流仍是 exploration，选 revelation 需有"换镜头"理由） |
| "我要**补地图**"（空白战场/空白半区） | `exploration` 拓荒 | neglected-arena / half-domain-gap |
| "我要**配解药**"（已知惩罚/低效 + 缓解条件） | `remedy` 解药 | consensus-puzzle / 惩罚共识 |
| "我要**改判规则**"（对立预测在 DV 不同维度各成立） | `dimension-split` 维度分裂 | paradigms-at-war |
| "我要**发现共同引擎**"（两分离域由同一机制统一） | `unification` 统一 | cross-domain-unification |

## Step C: 框架卡生成（2-3 个候选）

每个候选框架一张卡，格式：

```markdown
### 候选 N：<knot 类型> × <resolution 类型>（原型：<blueprint id>）
- **一句话故事**：<冲突与解法的一句话>
- **原型对照**：<blueprint 名>（同一类型的故事长这样）；对照对：<相关对照对>
- **五幕落点预告**（实证锚：`../story-blueprints/layout-inventory.md` <类型> 节）：knot 在哪里系紧（intro 模块）→ 在哪解开（theory 假设/results 位置）→ climax 落点（实证：该类型常见 Results 开头首揭 / 主表揭晓）→ falling action 项数（实证：该类型典型 N 项）
- **布局要点**（从实证样板取，可执行）：<开场形态、揭晓内容类型、falling_action 收束节奏、独特签名节奏（如 consensus 复现-消解、shipilov 复现-翻转）>
- **反派构造建议**：<谁当反派 + 用什么修辞构造>
- **前提风险**：<对照 blueprint 的"禁忌"核对——前提不成立则此框架弃用>
```

选择规则：① 多原型（≥2 实证）类型优先；② 从 Step A 命中的类型里按"冲突位置最精确"排序；③ 2-3 个候选需**跨类型**（避免 3 个都是同一型的微变）；④ 每个候选标注原型与风险，由用户拍板。

## 类型前提风险清单（从 blueprint 禁忌聚合）

| 类型 | 成立前提 | 常见翻车点 |
|------|---------|-----------|
| irony-reversal | 同一构念/行动对双方**同时**相反（两面共存） | 写成先后顺序（那是 half-domain-gap）；"监督→地下化"必须有机制依据（规避激励/可见性不对称） |
| paradigms-at-war | 对立阵营**各自有完整立场**与证据 | 稻草人——一方只有零散观点；'on the one hand/other hand' 需对称推导 |
| consensus-puzzle | 共识确实强（多情境加固）且违背确实持续 | "共识"是作者自封；行为持续需可观测证据（Pontikes 的持续 vs 惩罚并置） |
| overlooked-alternative | 主流视角**有代言人**（可引 Authority 原话）；替代面真实存在 | 替代面只是"另一个变量"而非"另一面"；deductive 版需 'Most research underscores...' 可实指 |
| neglected-arena | 子域确实空白（非"没检索到"） | 注意力转移解释需可引证据（Desai 的 'Indeed, although... much attention has turned to'） |
| tangled-constructs | 两构念在文献里**定义层纠缠**（可逐字锚定） | 构念其实已区分——退化为普通关系研究 |
| half-domain-gap | 双极**真实存在**且一极确实已做 | 'equity done/debt not' 必须可实指（引用半区文献）；跨学科嫁接需源学科证据背书 |
| cross-domain-unification | 两域**确实分离**（各自有文献流）且共用引擎可论证 | 硬凑统一——两域机制其实不同则退化为双域并列 |
| remedy | 惩罚/低效是**文献共识**（H1 可引用而非推导）；解药可操作化 | 解药不可测（cutolo 的文本特征可测量是前提）；缓解方向与惩罚反向对抗 |
| dimension-split | DV 有**可拆分的多个维度**且各维度有独立理论含义 | 维度是人为切分——各赢一维度需每个维度都有完整 why chain |
| assumption-flip | 共识前提**可被证明可疑**（有反例/悖论） | 挑战落空——前提其实成立则退化为 Incompleteness |

## 输出（写入 story 契约的 story_frame 字段）

```yaml
story_frame:
  frame_type: "<knot 类型>"
  resolution_type: "<resolution 类型>"
  one_liner: "<一句话故事>"
  exemplar_blueprint: "<blueprint id>"
  alt_frames:
    - frame: "<被拒候选>"
      rejected_reason: "<为什么被拒>"
  risk_notes: "<前提风险核对结果>"
```

## 与 story-blueprints 的联动

- 框架卡的原型对照直接引用 `story-blueprints/blueprints/_index.md` 的状态列（多原型 vs 单原型）与对照对；**布局实证**引用 `story-blueprints/layout-inventory.md`（climax 落点分布 / falling_action 项数 / knot×resolution 联合分布 / 逐类型布局样板）。
- **讲法家族索引**：`story-blueprints/tellings/alternative-tellings-compilation.md`（12 家族 × 实例，含被拒讲法清单）——Step C 的"原型对照"与风险栏（"审稿人可能替你讲单面/折中故事"）直接引用该汇编。
- 用户选定框架后，`story.central_knot` / `characters` / `storylines` 按所选框架填写（irony 需要"两面"都进角色表；paradigms-at-war 需要两阵营构念都声明等）。
- 若用户的研究与某 blueprint 构成**同构念对**（同一 X→Y），优先提示该对（'同作者同现象不同故事' desjardine2022↔2023 是最强示范：同现象可以有两套不相上下的故事）。
