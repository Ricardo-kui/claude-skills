# Phase 3: DNA report

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 3 — Academic Introduction DNA 量化与结构化报告

量化该论文 Introduction 的"叙事 DNA"，生成 fine-grained profile。

### 惰性生成原则（Lazy Generation）

借鉴 grill-with-docs 的 "Create files lazily" 原则：

- **模块不存在时不生成空壳**：如果某模块（如 Stakes）在原文中确实缺失，Fine-Grained Profile 中直接省略该模块的标题和占位符，不生成 "N/A" 或 "Missing" 填充
- **骨架不可迁移时标记即停**：如果某表达骨架因论文特殊性无法泛化，只记录 "Non-Transferable" 标签，不强行抽象
- **批量模式分桶后再聚合**：Phase 4 的聚合报告只在同一 Gap×Contribution 组合内统计，不同组合的数据不混为一谈

### Introduction DNA 指标

#### 基础 DNA 指标（v2.0 已有）

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 模块密度 | 总字数 / 识别到的模块数 | 判断 Introduction 的信息密度（顶刊中位数约 120-150 词/模块） |
| Hook-to-Puzzle 距离 | Hook 首句到首次出现 puzzle 陈述的句数 | 判断兴趣建立效率。<=3 句为优秀，>6 句为低效 |
| "Few studies" 密度 | "few studies" / "little is known" / "underexplored" 出现次数 | 判断 Gap 语言质量。>=1 次即标记为 generic gap language 风险 |
| Tension 深度 | Tension 中是否包含 (a) 具体文献批评 (b) 理论后果 (c) 反例/矛盾 | 0-3 分。3 分为优秀，0-1 分为薄弱 |
| Stakes 具体性 | Stakes 模块是否包含量化数据/具体理论成本/明确实践后果 | 高/中/低。Incompleteness 必须有高 Stakes |
| Transition 链完整性 | 相邻模块间是否有 explicit transition 句子 | 0-6 分（7 个模块间 6 个过渡点） |
| Theory Lens 回应度 | Theory Lens 是否直接回应 Tension 提出的 gap（关键词重叠度） | 高/中/低。低回应度 = "理论引入与 gap 脱节" |
| Makadok 可见性 | Contribution 中 Makadok 维度关键词出现的清晰度 | 0-8 分。>=4 分为可见 |
| JTBD 6-Block 覆盖 | Simsek & Li (2022) 的 6 个 block 是否都有对应内容 | 0-6 分 |
| Contribution-Discussion 可兑现度 | Contribution 的每个声明是否能在 Theory/Methods/Results 中找到支撑线索 | 高/中/低 |

#### Story Architecture DNA 指标（Pollock Ch02-Ch05，v2.1.0 新增）

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| Central Knot 清晰度 | 是否能从 Gap 段推断出包含冲突的一句话 | 高/中/低/null。低 = "无明确核心冲突" |
| 主角集中度 | 主角构念提及次数 / 总构念提及次数 | >=60% 为集中，<40% 为分散 |
| Characters 出场秩序 | 主角/配角/群演是否按正确顺序出场 | 群演出现在前 3 段 = 风险 |
| 叙事弧线一致性 | Hook 能量级 ≤ Gap 能量级 ≤ Stakes 能量级 | 检测"高开低走"或阶段倒退 |
| Davis 有趣性匹配度 | 推断的 Davis 类型数量 | >=1 为正常，0 标记 ⚠️（非阻塞） |
| 前端一致性 | Title/Abstract 是否包含 central_knot 关键词 | true/false/null |
| Fat Suit 指数 | P1 词数 / 前 3 段词数 | P1 > 120 词或前 3 段 > 350 词 = ⚠️ |
| Burying the Lead 指数 | 各段段首句在 15 词内说出核心判断的比例 | >=80% 为优秀，<50% 为风险 |
| Sentence Stuffing 指数 | 单句 >30 词或含 >2 从句的句子比例 | >20% 为风险 |

#### Prose Craft DNA 指标（Pollock Ch03，v2.1.0 新增）

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| Human Face 覆盖率 | 有具体 actor 的模块数 / 总模块数 | >=50% 为优秀（Hook 必须 >=1） |
| Showing 比率 | 有 concrete illustration 的抽象主张数 / 总抽象主张数 | >=70% 为优秀 |
| Passive Voice 密度 | "It is argued that" / "It is shown that" / "It is hypothesized that" 出现次数 | 0 为优秀，>=1 为需修正 |
| Inflated Symbolism 标记 | "paradigm shift" / "fundamentally transforms" / "revolutionize" 出现次数 | 0 为优秀，>=1 为需降级 |
| Read-aloud 自然度 | Hook + Contribution 大声朗读是否自然 | 主观评级：自然/生硬/机器声 |
| 模块跳过合理性 | 跳过模块数 + 跳过理由充分性 | 安全压缩 / 风险跳过 |

### Narrative Style Profile（叙事风格 DNA）

借鉴 model_papers_style.json 的多维度风格解剖框架，为每篇论文生成**可模仿的风格画像**。这是 Introduction 蒸馏的核心增值产出——不仅提炼结构，更提炼**语气、节奏和句法创新**。

| 维度 | 提炼问题 | 输出格式 |
|------|----------|----------|
| **Tone** | 整体语气光谱是什么？assertive / cautious / vivid / formal / policy-facing？ | 主语气 + 次语气，附证据句 |
| **Paragraph Rhythm** | 段落内部句法节奏是什么？claim→context→evidence→transition？还是 claim→evidence→interpretation？ | 段落级节奏模板 |
| **Module Ratio** | 各模块的词数比例？（如 Hook 占 15%、Literature Turn 占 25%、Tension 占 20%） | 百分比 + 与同类范文的对比 |
| **Distinctive Features** | 该论文**特有**的叙事标记是什么？（如 paired contrasts / rhetorical questions / signpost triads / self-critique embedding） | 列表，每项附原文例句 |
| **Avoids** | 该论文**刻意回避**的写法是什么？（如 avoids overclaiming causality / avoids bullet-point prose） | 列表，说明回避的修辞功能 |
| **Quality Markers** | 为什么这个叙事结构有效？最强/最弱的叙事技巧是什么？ | what_makes_effective / strongest_aspect / weakest_aspect |
| **Prose Craft Profile**（v2.1.0 新增） | Human Face / Showing vs Telling / Conversational Voice 的具体策略 | 见下方 Prose Craft 子维度 |

#### Prose Craft Profile 子维度（v2.1.0 新增）

| 子维度 | 提炼问题 | 输出格式 |
|--------|----------|----------|
| **Human Face 策略** | 论文如何在关键槽位嵌入具体 actor？Hook 用公司名还是人名？Consensus 引用用作者名还是 "many scholars"？ | actor 类型分布 + 代表性例句 |
| **Showing 策略** | 论文如何在抽象主张后配 concrete illustration？用案例、数字、场景还是具体研究？ | illustration 类型分布 + 代表性例句 |
| **Voice 策略** | 论文在 Gap/Theory Lens/Contribution 中如何避免被动语态？使用哪些主动句式？ | 主动句式模板 + 被动语态位置（如有） |
| **Fat Suit 控制** | 论文如何控制背景长度？P1 是否倒金字塔？前 3 段背景占比？ | P1 词数 + 前 3 段背景占比 |
| **Burying the Lead 控制** | 各段段首句结构：是否在 15 词内说出核心判断？段首句功能（核心判断/元评论/过渡） | 段首句功能统计 |
| **Sentence Stuffing 控制** | 长句拆分策略：复杂从句如何处理？括号内容是否独立成句？ | 平均句长 + 最长句分析 |

**记录原则**：只记录该论文**明显区别于**同类 Gap×Contribution 组合其他范文的特征。通用特征（如"有 Hook"）不记入 Distinctive Features。

### 结构化报告输出（fine_grained profile）

```markdown
> **Fine-Grained Profile 输出模板**已外置：见 `../protocols/profile_template.md`。Phase 3 结构化报告输出时加载并严格遵循。
