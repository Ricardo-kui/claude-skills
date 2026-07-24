# Phase 3: theory DNA report

> Imported from the upstream protocol. Resolve relative resource paths from this reference file's directory.

## Phase 3 — Academic Theory DNA 量化与结构化报告

量化该论文 Theory 的"理论 DNA"，生成 fine-grained profile。

### 惰性生成原则（Lazy Generation）

借鉴 grill-with-docs 的 "Create files lazily" 原则：

- **模块不存在时不生成空壳**：如果某模块（如 T5 Boundary Condition）在原文中确实缺失，Fine-Grained Profile 中直接省略该模块的标题和占位符
- **骨架不可迁移时标记即停**：如果某表达骨架因论文特殊性无法泛化，只记录 "Non-Transferable" 标签，不强行抽象
- **批量模式分桶后再聚合**：Phase 4 的聚合报告只在同一构建类型内统计，不同构建类型的数据不混为一谈
- **Why-chain 断裂点不美化**：如果 T3 存在推理跳跃，记录具体断裂位置，不为了"完整"而补全作者未论证的步骤

### Theory DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 模块密度 | 总字数 / 识别到的模块数 | 判断 Theory 的信息密度（顶刊中位数约 100-130 词/模块） |
| Why chain 步数 | T3 中独立机制步骤的数量 | 判断机制深度。单步为薄弱，两步为常规，三步+为深入 |
| Why chain 断裂点 | T3 中缺少理论依据的跳跃数量 | 断裂点 >=1 即标记为推理薄弱 |
| 主角集中度 | 主角（核心构念）提及次数 / 总构念提及次数 | 判断焦点是否分散。>=60% 为集中，<40% 为分散 |
| Citation 功能比 | 支持机制推演的 citation / 总 citation 数 | 判断 "citation list 代替理论" 风险。>=70% 为健康 |
| 假设推导句密度 | "Therefore" / "Thus" / "Accordingly" / "Consequently" 出现次数 / 假设数 | 判断假设是否从机制自然推导。>=1  per hypothesis 为健康 |
| Scope condition 覆盖 | 有明确 scope condition 的构念 / 总构念数 | 判断构念界定精确性 |
| Boundary 嵌入深度 | Boundary condition 是在假设之后补丁，还是嵌入机制链中 | 嵌入机制链 > 假设后补丁 |
| Theory-to-Hypothesis 对齐 | T3 的机制关键词与 T4 假设关键词的重叠度 | 高/中/低。低对齐 = "机制与假设脱节" |
| Two-literature 清晰度 | T2 的理论文献是否与 Introduction 的 Gap 文献明显分离 | 高/中/低 |
| **T3/T4 论证节奏完整性** | 假设推导段落的交织式论证完整比例（方向→机制/证据交织→收敛） | >=0.9 为优秀，0.7-0.89 为合格，<0.7 为薄弱。同时标记节奏变体：interwoven / separated / hybrid |
| **T1 定义节奏完整性** | 构念定义段落的三拍完整比例（命名→维度→范围） | >=2.5/3 为优秀，1.5-2.4/3 为合格 |
| **T2 理论视角节奏完整性** | 理论引入段落的三拍完整比例（来源→适用性→框架映射） | >=2.5/3 为优秀 |
| **节奏变异度** | 段落节奏与标准节奏的偏离类型和幅度 | FULL_RHYTHM / RHYTHM_GAP / RHYTHM_BROKEN / RHYTHM_VARIANT |
| **跨段落节奏连贯性** | 相邻假设段落的节奏衔接模式（连续推导 / 并行并列 / 分叉展开） | 连续推导 > 分叉展开 > 并行并列（但构建类型决定最优模式） |
| **连接词密度** | 连接词总数 / Theory 总词数 × 100 | 顶刊中位数约 3-4 词/100词；<2 为"论证隐式化"，>5 为"连接词过载" |
| **因果连接词占比** | 因果类连接词数 / 总连接词数 | 机制推演型预期 ≥30%；过高（>50%）可能为因果词堆砌 |
| **条件连接词占比** | 条件类连接词数 / 总连接词数 | 假设树型/调节效应型预期 ≥15%；机制推演型预期 <10%；过高泄露隐性假设树结构 |
| **拍间过渡完整性** | 有显式连接词的拍间过渡数 / 总拍间过渡数（每假设段落 2 个拍间过渡点：方向→机制/证据，机制/证据→收敛） | ≥80% 为优秀，<50% 为"论证断裂" |
| **模块过渡完整性** | 有显式连接词的模块过渡数 / 5 | 5/5 为优秀，<3/5 为"模块碎片化" |
| **连接词-构建类型一致性** | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用模式与构建类型预期偏离 |
| **T6 / Closure 策略**（v1.2.0 新增，同步 write-theory v3.3.0） | 最后假设后是否有独立 Closure 段？或采用局部收束/嵌入框架总结/Discussion 开篇整合？ | 独立 Closure 段 = 非管理学标准；局部收束 = 标准；嵌入框架总结/Discussion 整合 = 可选策略 |
| **T6 Voice 质量**（如存在框架总结） | 框架总结是否使用 accountable first-person（"we have argued"），无被动语态 | 通过/失败/null |
| **T6 叙事接力**（v1.2.0 新增） | 如存在框架总结，结尾能量级是否 ≥ 最后假设推导段 | 通过/倒退/null |
| **Human Face 覆盖率**（v1.2.0 新增） | 有具体 actor/场景/案例的模块数 / 总模块数 | Hook/新构念/why-chain 关键步骤 ≥1 个 illustration 为优秀 |
| **主动语态比例**（v1.2.0 新增） | "We argue/hypothesize/predict" 次数 / 总主张句次数 | >=80% 为优秀；<50% 为机器声风险 |
| **识别策略理论嵌入**（v1.2.0 新增，制度冲击类） | Theory 中嵌入识别假设论证的模块数 / 需要的模块数 | 3/3 为优秀（IV/DiD/RDD/生存各需特定论证） |
| **微观动作完整性**（v1.4.0 新增） | 每个假设段落中 Anchor → Gap → Mechanism Move → Warrant → Prediction 的完整比例 | 5/5 为优秀，缺失任意动作即标记为薄弱 |
| **双边论证覆盖率**（v1.4.0 新增） | 调节/边界条件假设中同时论证 high/low 条件的比例 | 1.0 为优秀，<0.5 为严重缺失（对应 write-theory C20） |
| **替代解释排除率**（v1.4.0 新增） | 已识别的 competing explanations 中被主动排除的比例 | 1.0 为优秀；0 为高风险 |
| **论点-论据安排模式**（v1.4.0 新增） | 论文主要使用的安排模式（Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel） | 标记模式 + 是否功能等价 |
| **Concrete Illustration 密度**（v1.4.0 强化） | 每个 why-chain 步骤后是否有 illustration；连续两步无 illustration 的段落数 | 零缺失为优秀；≥1 处缺失为需关注 |
| **证据类型分布**（v1.4.0 新增） | Empirical / Theoretical / Boundary / Negative / Analogical 的比例 | 支持机制推演的 empirical/theoretical 应 ≥70% |
| **证据功能分布**（v1.4.0 新增） | support / qualify / contrast / pave / rebut 的比例 | support 为主但其他功能也需存在 |
| **文献引用三要素完整率**（v1.4.0 新增） | 同时满足 concrete finding + argument summary + link to mechanism 的引用比例 | ≥80% 为优秀 |
| **交互模式明确度**（v1.4.0 新增，对应 write-theory C10） | 调节假设是否明确 enhancing/buffering/antagonistic/existence/competing | 明确为优秀；缺失为失败 |
| **竞争假设收敛信号**（v1.4.0 新增，对应 write-theory C14） | 竞争假设是否使用非 "Therefore" 收敛信号 | 符合为优秀；违规为失败 |
| **辩证对立对称性**（v1.4.0 新增，对应 write-theory C16-C17） | 两个对立机制的步骤数是否对称；方向是否真正反转 | 对称+方向反转为优秀 |
| **Moderator 选择框架**（v1.4.0 新增，对应 write-theory C18） | ≥2 moderators 时是否有元框架解释选择理由 | 有为优秀；无为失败 |
| **连续 IV 三点论证**（v1.4.0 新增，对应 write-theory C19） | 连续 IV 是否论证 high / middle / low 三点的行为差异 | 完整为优秀；缺失为失败 |

### Narrative Style Profile（叙事风格 DNA）

借鉴 model_papers_style.json 的多维度风格解剖框架，为每篇论文生成**可模仿的理论写作风格画像**。

| 维度 | 提炼问题 | 输出格式 |
|------|----------|----------|
| **Tone** | 整体语气光谱是什么？assertive / cautious / formal / mechanism-forward / concept-forward？ | 主语气 + 次语气，附证据句 |
| **Paragraph Rhythm** | 段落内部句法节奏是什么？claim→mechanism→evidence→hypothesis？还是 definition→distinction→consequence？ | 段落级节奏模板 |
| **Module Ratio** | 各模块的词数比例？（如 T1 占 20%、T3 占 40%、T4 占 15%） | 百分比 + 与同类范文的对比 |
| **Distinctive Features** | 该论文**特有**的理论叙事标记是什么？（如 paired concept contrasts / stepwise mechanism labels / explicit caveat embedding / rhetorical question architecture） | 列表，每项附原文例句 |
| **Avoids** | 该论文**刻意回避**的写法是什么？（如 avoids black-box econometrics / avoids overclaiming causality / avoids bullet-point prose） | 列表，说明回避的修辞功能 |
| **Quality Markers** | 为什么这个理论论证结构有效？最强/最弱的叙事技巧是什么？ | what_makes_effective / strongest_aspect / weakest_aspect |
| **Prose Craft Profile**（v1.2.0 新增） | Human Face / Showing vs Telling / Conversational Voice 的具体策略 | 见下方 Prose Craft 子维度 |

#### Prose Craft Profile 子维度（v1.2.0 新增）

| 子维度 | 提炼问题 | 输出格式 |
|--------|----------|----------|
| **Human Face 策略** | 论文如何在 T1 构念定义/T3 机制推演中嵌入具体场景？用公司名、人名还是行业实例？ | actor 类型分布 + 代表性例句 |
| **Showing 策略** | 论文如何在抽象因果步骤后配 concrete illustration？用案例、数字、场景还是具体研究？ | illustration 类型分布 + 代表性例句 |
| **Voice 策略** | 论文在假设推导中如何避免被动语态？使用哪些主动句式？T6 收束句式是什么？ | 主动句式模板 + 被动语态位置（如有） |
| **Stroke/Glide 控制** | 机制推演段落中动作（stroke）与评论（glide）的比例？是否有 forced march 或 ponderous pace？ | stroke/glide 比例 + 风险段落标记 |

**记录原则**：只记录该论文**明显区别于**同类构建类型其他范文的特征。通用特征（如"有 why chain"）不记入 Distinctive Features。

### 结构化报告输出（fine_grained profile）

```markdown
> **Fine-Grained Profile 输出模板**已外置：见 `../protocols/profile_template.md`。Phase 3 结构化报告输出时加载并严格遵循。

> **Corpus Taxonomy for write-theory**（v1.4.0）已外置：见 `../protocols/corpus_taxonomy.md`。Phase 4 沉淀建议映射到 write-theory corpus 结构时加载。
