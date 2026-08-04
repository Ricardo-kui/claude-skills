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
| 模块密度 | 总字数 / 识别到的功能模块数 | 描述信息密度；必须按 build type 与期刊解释，不设通用优劣阈值 |
| Why-chain reasoning moves | 前提→过程→预测中有内容的推理转换数 | 判断推理是否足以承重；不按变量/中介数量计算，也不以越多越好 |
| Why chain 断裂点 | T3 中缺少理论依据的跳跃数量 | 断裂点 >=1 即标记为推理薄弱 |
| 主角集中度 | 主角（核心构念）提及次数 / 总构念提及次数 | 描述焦点分配；结合角色功能判断，不按百分比自动判定 |
| Citation 功能匹配 | 已映射到 premise/warrant/boundary/contrast/rebut 的 citation / 总 citation | 判断 citation list 风险；理论与实证引用承担不同功能 |
| 假设收敛方式 | directional / conditional / competing 收敛方式及其文本标记 | 判断预测能否由推理恢复；不按 Therefore 次数评分 |
| Scope condition 覆盖 | 有明确 scope condition 的构念 / 总构念数 | 判断构念界定精确性 |
| Boundary 嵌入深度 | Boundary condition 是在假设之后补丁，还是嵌入机制链中 | 嵌入机制链 > 假设后补丁 |
| Theory-to-Hypothesis 对齐 | T3 的机制关键词与 T4 假设关键词的重叠度 | 高/中/低。低对齐 = "机制与假设脱节" |
| Two-literature 清晰度 | T2 的理论文献是否与 Introduction 的 Gap 文献明显分离 | 高/中/低 |
| **T3/T4 论证功能完整性** | 前提→reasoning moves/证据→预测是否完整 | 标记 interwoven / separated / hybrid 及功能等价性，不按固定拍数评分 |
| **T1 定义功能** | definition、scope、lineage、differentiation、justification 中实际需要的功能 | 按新旧构念与贡献任务判断，不机械要求三拍 |
| **T2 理论视角功能** | 理论来源、适用性与 focal mapping 是否足以支撑推演 | 按理论熟悉度和整合任务判断 |
| **节奏变异度** | 段落节奏与标准节奏的偏离类型和幅度 | FULL_RHYTHM / RHYTHM_GAP / RHYTHM_BROKEN / RHYTHM_VARIANT |
| **跨段落节奏连贯性** | 连续推导 / 并行并列 / 分叉展开与理论任务的匹配 | 无通用排序；判断每段是否推进同一 knot |
| **连接词密度** | 连接词总数 / Theory 总词数 × 100 | 描述性统计；只有与 reasoning trace 隐晦或连接词堆砌共现时才诊断 |
| **因果连接词占比** | 因果类连接词数 / 总连接词数 | 按 build type 描述，不把低/高比例直接等同于逻辑质量 |
| **条件连接词占比** | 条件类连接词数 / 总连接词数 | 作为 conditionality 线索，须回到机制与假设形式核验 |
| **推理关系可恢复率** | 相邻 reasoning moves 中逻辑关系可由文本恢复的比例 | 连接词不是必要或充分条件；记录具体不可恢复位置 |
| **模块过渡功能** | 相邻功能模块是否存在必要的依赖/推进关系 | 按动态模块数判断，不以固定 5 个过渡点评分 |
| **连接词-构建类型一致性** | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用模式与构建类型预期偏离 |
| **T6 / Closure 策略**（v1.2.0 新增，同步 write-theory v3.3.0） | 最后假设后是否有独立 Closure 段？或采用局部收束/嵌入框架总结/Discussion 开篇整合？ | 独立 Closure 段 = 非管理学标准；局部收束 = 标准；嵌入框架总结/Discussion 整合 = 可选策略 |
| **T6 Voice 质量**（如存在框架总结） | 框架总结是否使用 accountable first-person（"we have argued"），无被动语态 | 通过/失败/null |
| **T6 叙事接力**（v1.2.0 新增） | 如存在框架总结，结尾能量级是否 ≥ 最后假设推导段 | 通过/倒退/null |
| **Human Face 功能适配** | 需要澄清的抽象/跨层/反直觉位置中，illustration 是否真正降低负荷 | needed_and_present / needed_but_missing / not_needed |
| **主动语态比例** | "We argue/hypothesize/predict" 次数 / 总主张句次数 | 描述作者责任声；不得单凭百分比判定质量 |
| **识别策略理论嵌入**（v1.2.0 新增，制度冲击类） | Theory 中嵌入识别假设论证的模块数 / 需要的模块数 | 3/3 为优秀（IV/DiD/RDD/生存各需特定论证） |
| **微观功能完整性** | 每个假设的必要前提、reasoning moves、warrant 与 prediction 是否齐备 | 按任务判断；Gap/Puzzle 非每段强制 |
| **双边论证覆盖率**（v1.4.0 新增） | 调节/边界条件假设中同时论证 high/low 条件的比例 | 1.0 为优秀，<0.5 为严重缺失（对应 write-theory C20） |
| **替代解释处置** | 主要可信 competing explanations 是否被区分、限定或诚实保留 | 关注最强替代解释，不追求数量清零 |
| **论点-论据安排模式**（v1.4.0 新增） | 论文主要使用的安排模式（Warrant-Embedded / Warrant-First / Evidence-Contrast / Cumulative / Parallel） | 标记模式 + 是否功能等价 |
| **Concrete Illustration 适配** | illustration 出现位置与理论负荷是否匹配 | needed_and_present / needed_but_missing / not_needed |
| **证据类型分布** | Empirical / Theoretical / Boundary / Negative / Analogical 的比例 | 描述分布并检查功能错配，不设通用配额 |
| **证据功能分布**（v1.4.0 新增） | support / qualify / contrast / pave / rebut 的比例 | support 为主但其他功能也需存在 |
| **引用功能匹配率** | 引用是否准确承担 premise / warrant / boundary / contrast / rebut | 理论引用不强制 concrete finding，实证引用不必同时承担完整 warrant |
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

---

## Phase 3.5 — DNA → write-theory validator 回流（Validator Check Suggestions）

> **目的**：DNA 指标先作为描述性信号。只有当指标偏离与可说明的功能失败共同出现，并满足 `design-feedback-loop.md` 的全文证据、规则核验和双回归门槛时，才进入 validator 设计反馈；不得把样本均值直接硬化为写作阈值。

### 回流候选指标（描述信号，不是自动门槛）

下列指标可帮助定位功能问题。表中数值只能作为当前样本基准；必须进一步证明它对应推理断裂、条件化遗漏、构念不清或读者负荷问题。

| DNA 指标 | 描述基准 | validator 现状 | 形成候选的附加条件 |
|---------|---------|--------------|------------------------------|
| **连接词密度** | 当前样本分布 | validator 按功能检查逻辑关系 | 仅当连接词缺失/过载与无法恢复 reasoning trace 共现时登记候选 |
| **因果连接词占比** | 按 build type 记录分布 | validator 按 reasoning trace 审查 | 比例异常且存在具体不可恢复的因果转换 |
| **条件连接词占比** | 按 build type 记录分布 | conditionality gate 审查机制 | 条件语言与模型/机制不一致，而非单凭比例高低 |
| **模块过渡功能** | 按实际模块数记录 | validator 动态审查 dominant function | 相邻模块的理论依赖断裂或 storyline 漂移 |
| **连接词-构建类型一致性** | 高/中/低描述 | 无独立硬门槛 | 文本标记与实际理论结构冲突并导致误读 |
| **Concrete Illustration 密度** | 按抽象负荷解释 | validator 判断例子是否必要及是否替代理论 | 仅当跨层/反直觉步骤无法模拟时提示；不设置“每两步”配额 |
| **主动语态比例** | 当前样本分布 | validator 查作者责任声与被动堆积 | 被动表达系统性隐藏核心判断；不因单个百分比自动失败 |

### 不回流的指标（validator 已覆盖或无操作阈值）

- **推理关系可恢复性** → validator 已按 reasoning trace 覆盖；不另设连接词覆盖率
- **证据类型分布 / 引用功能匹配率** → paragraph_layout 已按论据功能诊断；不向 validator 回流通用比例

### 回流输出格式

```yaml
phase_3_5_validator_reflux:
  paper: "Zhou_Gao_Zhao_2017_ASQ"
  build_type: "B 机制推演 + G 辩证对立"
  deviations_found: 2
  validator_check_suggestions:
    - target_validator: "post-generation-validator.md 验证 7c"
      dna_metric: "推理关系可恢复性"
      paper_value: "2 处相邻 moves 无法恢复因果转换"
      descriptive_baseline: "同 build-type 样本分布（非硬阈值）"
      observed_functional_failure: "连接词与 warrant 均未说明 state A 如何改变 choice"
      suggested_check: |
        在 derivation trace 中检查相邻 moves 的行动者、层级与时间转换；
        连接词存在与否均不能替代 warrant。
      adoption_status: design_feedback_candidate
      cross_paper_evidence:  # 是否跨论文复现该偏离（≥2 篇才建议采纳）
        papers_showing_same_deviation: 1
        threshold_to_adopt: "遵循 design-feedback-loop：核心规则 VERIFIED 或 absolute-rule FALSIFIER"
    - target_validator: "post-generation-validator.md 验证 6c"
      dna_metric: "主动语态比例"
      paper_value: "0.91"
      descriptive_baseline: "当前样本分布"
      deviation: "none"  # 本篇未出现作者责任声问题，仅记录印证
      suggested_check: null  # 无偏离 → 不生成建议
  reflux_decision_rule:
    - "单篇偏离 → 记录为 EMERGING；若推翻绝对规则可标 FALSIFIER，但只允许条件化"
    - "跨论文达到 VERIFIED/ROBUST → 进入有边界 validator correction 候选"
    - "通过授权、风险和双回归门控 → 修订并记录 resolution；否则只登记"
```

### 与现有机制的分工

| 机制 | 触发 | 落点 | 自动化程度 |
|------|------|------|-----------|
| **Phase 4 语料沉淀**（writeback_reminders） | 句式/骨架复现 | corpus/variants, subprotocols, sentences | 证据门槛内可自动 reference 回写 |
| **Phase 3.5 validator 回流**（本节） | DNA 信号与功能失败共现 | `_skill_design_feedback.yaml` → validator | 达到核心门槛后有边界修订 |

**关键区别**：Phase 4 回流"写什么"（句式/骨架），Phase 3.5 回流"查什么"（validator 检查项）。两者互补：蒸馏发现的句式丰富 sentences，蒸馏发现的诊断规律丰富 validator。

### 诚实边界（回流专用）

- **不由指标直接改 validator**：先持久化设计反馈；只有低/中风险且通过核心门控才可自动 correction
- **单篇偏离不建立一般阈值**：只记 EMERGING；决定性反例也只能削弱绝对规则
- **不与现有检查重复**：回流候选已排除 validator 验证 1-8 覆盖的指标（见"不回流的指标"表）
- **阈值标注来源**：数值必须标明样本、构建类型和期刊覆盖，称为“描述基准”而非“顶刊硬阈值”
