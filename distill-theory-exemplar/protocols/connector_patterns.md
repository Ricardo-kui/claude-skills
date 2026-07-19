# 连接词使用模式提炼（Phase 2.5）

> 外置自 `distill-theory-exemplar/SKILL.md`。何时加载：Phase 2 骨架提炼完成后执行连接词分析时加载。

---

### 2.5 连接词使用模式提炼（Connector Pattern Distillation）

连接词是 Theory 论证逻辑的**显式标记**——它们将隐含的因果、对比、递进关系暴露给读者。蒸馏连接词使用模式可以直接反哺 `write-theory` 的连接词与收束语料（Phase 3 段落级 transition 诊断 + Phase 5 `corpus/sentences/closure.md` 收束/过渡句式）。

#### 蒸馏目标

对论文 Theory 中使用的连接词进行**三层提取**：

1. **连接词密度与分布**：哪些逻辑关系的连接词被使用？频率如何？
2. **模块-连接词映射**：不同模块（T1–T6）偏好哪些连接词类型？
3. **构建类型-连接词映射**：不同构建类型偏好的连接词模式（可跨论文聚合）

#### 连接词分类法（与 write-theory §5.6 对齐）

| 逻辑关系 | 英文连接词 | 中文对应 | 典型出现模块 | 蒸馏计数标记 |
|---------|-----------|---------|-------------|-------------|
| **因果** | Therefore, Thus, Accordingly, Consequently, As a result, Hence, This leads to | 因此、由此、从而 | T3（机制推演）, T4（假设收敛） | `causal_N` |
| **对比** | In contrast, By comparison, Unlike, However, Whereas, On the other hand, Conversely | 相比之下、与之不同、然而 | T1（构念区分）, T5（边界条件） | `contrast_N` |
| **递进** | Furthermore, Moreover, In addition, Additionally, Beyond this, More importantly | 更进一步、此外、更重要的是 | T3（多步机制链的步骤间衔接） | `additive_N` |
| **条件** | When, If...then..., Only if, Provided that, Contingent on, Depending on | 当…时、若…则…、仅在 | T5（边界条件）, 假设树型 T3 | `conditional_N` |
| **让步** | Although, While, Despite, Even though, Nevertheless, Nonetheless | 尽管、虽然、即便如此 | T5（边界承认后转回主论证） | `concessive_N` |
| **例证** | Specifically, In particular, For example, For instance, To illustrate | 具体而言、例如 | T3（机制具体化）, T1（构念维度展开） | `specificity_N` |
| **总结** | Taken together, In sum, Overall, Collectively, In summary | 综上、整体而言 | 嵌入最后假设段末尾的框架总结 / 假设段落的最后一句 | `summary_N` |
| **强调** | Notably, Importantly, Critically, It is worth noting that, Key to this argument | 值得注意的是、关键在于 | T2（理论核心洞察）, T4（假设关键方向） | `emphasis_N` |

#### 段落内连接词节奏（Beat Connector Pattern）

连接词在论证节奏的**拍间过渡**中承担特定功能。蒸馏时记录每拍的拍间连接词类型：

```text
交织式论证链的拍间连接词模式：
[拍1-方向] → [拍2-机制+证据交织]:
  典型连接词: "Specifically, ..." / "We argue that..." / "Prior research shows..."
  蒸馏标记: beat1→2_connector = "specificity" / "evidence_pivot" / "none (direct)"

[拍2-机制+证据交织] → [拍3-收敛]:
  典型连接词: "Therefore, ..." / "Thus, ..." / "Accordingly, ..." / "Taken together, these arguments suggest..."
  蒸馏标记: beat2→3_connector = "causal" / "summary"
```

**拍间连接词缺失为高风险**：如果机制到假设的过渡没有因果连接词（直接 "H1: X is positively related to Y"），标记为 "无收敛信号"——假设像是从天而降，而非从机制推导。

**交织式典型信号**：当段落中出现 "Prior research shows X. However, what if Y? We argue that Z because..." 时，记录为文献与推理交织的标准模式。

#### 模块间过渡连接词模式

记录 T1→T2→T3→T4→T5→T6 模块序列中每个过渡点的连接词：

| 过渡点 | 典型连接词 | 功能 | 缺失风险 |
|--------|-----------|------|---------|
| T1→T2 | "Drawing on [theory], we..." / "To explain [these relationships], we adopt..." | 从构念界定过渡到理论框架 | T2 像硬插入的新话题 |
| T2→T3 | "Building on this lens, we develop..." / "[Theory] suggests that..." | 从理论框架过渡到机制推演 | T2 说完就扔，未驱动 T3 |
| T3→T4 (每假设) | "Therefore, we hypothesize:" / "Accordingly:" / "Thus:" | 从机制链收敛到假设 | 假设无推导信号 |
| T4(H_n)→T4(H_{n+1}) | "Having established H1, we next consider..." / "Beyond this direct effect, we further argue..." / "However, this relationship may not hold uniformly..." | 假设间逻辑递进 | 假设间无递进逻辑 |
| T4→T5 | "However, the [baseline effect] is likely contingent on..." / "Thus far we have assumed [condition]; yet..." | 从主效应过渡到边界条件 | T5 像是事后补丁 |
| T5→T6 / Closure | "Taken together, our theoretical framework suggests..." / "In sum, we have argued that..."（仅当存在独立或嵌入的框架总结时出现） | 从分散假设收束为整体框架 | 如假设间逻辑关系不自明且无框架总结，可能导致追问 |
| T5→METHODS | （无连接词，最后假设直接结束） | 管理学标准做法 | 无——这是正常结尾 |

#### 构建类型连接词特征

不同构建类型有其**标志性连接词组合**，蒸馏时识别该论文是否使用了其构建类型的预期连接词汇：

| 构建类型 | 标志性连接词组合 | 预期高频词 | 类型错配信号 |
|----------|----------------|-----------|-------------|
| **构念辨析型** | 对比+递进 | Whereas, In contrast, Unlike, Further | 大量使用 Therefore / Thus（滑向机制推演） |
| **机制推演型** | 因果+递进+具体化 | Therefore, Specifically, Consequently, In turn | 大量使用 Whereas / Unlike（混淆了构念辨析和机制推演） |
| **假设树型** | 条件+因果+让步 | When, However, Contingent on, Not uniform | 没有条件类连接词（缺少 moderator 信号），或因果连接词占绝对主导 |
| **质性过程理论型** | 时间序列+条件 | In Phase 1, As, Subsequently, When [condition] shifts | 使用因果链连接词（Therefore, Consequently）代替过程阶段标记 |
| **调节效应型** | 条件+因果+对比 | When [W] is high, In contrast, Therefore | 条件连接词只出现在假设句（H_x）而非机制段（T3） |

**连接词-构建类型一致性评分**：

```yaml
phase_2_5_connector_distillation:
  connector_density:
    causal: 12
    contrast: 3
    additive: 5
    conditional: 7
    concessive: 2
    specificity: 4
    summary: 2
    emphasis: 3
    total_connectors: 38
    connectors_per_100_words: 3.2
  beat_connector_patterns:
    H1_paragraph:
      beat1→2: "specificity (Specifically...)"
      beat2→3: "specificity (Consistent with...)"
      beat3→4: "causal (Therefore...)"
      beat_transitions_complete: true
    H2_paragraph:
      beat1→2: "none (direct)"
      beat2→3: "additive (Furthermore...)"
      beat3→4: "causal (Thus...)"
      beat_transitions_complete: false
      missing_beat_connector: "beat1→2 缺少方向→机制的过渡信号"
  module_transition_connectors:
    T1→T2: "To explain these relationships, we adopt..." (present)
    T2→T3: "missing — T3 直接从 'We argue' 开始，无理论框架过渡"
    T3→T4(H1): "Therefore, we hypothesize:" (present)
    T4(H1)→T4(H2): "Beyond this direct effect..." (present)
    T4→T5: "However, the above logic assumes..." (present)
    T5→T6: "Taken together..." (present)
    transition_completeness: "5/6"
    missing_transitions: ["T2→T3"]
  build_type_connector_alignment:
    detected_type: "机制推演型"
    expected_high_freq: ["Therefore", "Specifically", "Consequently"]
    actual_high_freq: ["Therefore(8)", "Specifically(4)", "However(5)"]
    alignment_issues:
      - "However 频率过高 (5次) 对机制推演型属于异常——可能暗示隐性假设树结构"
    connector_type_fidelity: "△ — 有条件连接词泄露"
  novel_connector_patterns:
    - "使用 'Stated differently' 作为机制重述信号 (非标准连接词，但功能等效于 specificity)"
    - "T3 步骤间使用 'This, in turn,...' 标记链式递进 (比 'Furthermore' 更精确)"
```

#### Phase 3 新增连接词 DNA 指标

| 指标 | 计算方式 | 用途 |
|------|----------|------|
| 连接词密度 | 连接词总数 / Theory 总词数 × 100 | 判断论证显式化程度。顶刊中位数约 3-4 词/100词 |
| 因果连接词占比 | 因果类连接词数 / 总连接词数 | 机制推演型预期 ≥30%；过高可能为"因果词堆砌" |
| 条件连接词占比 | 条件类连接词数 / 总连接词数 | 假设树型/调节效应型预期 ≥15%；机制推演型预期 <10% |
| 拍间过渡完整性 | 有显式连接词的拍间过渡数 / 总拍间过渡数 | 评估段落内部论证显式化程度 |
| 模块过渡完整性 | 有显式连接词的模块过渡数 / 5（T1→T2→T3→T4→T5→T6 共5个过渡点，T4内部不计） | 评估模块间叙事流显式化程度 |
| 连接词-构建类型一致性 | 标志性连接词组合匹配度 | 高/中/低。低匹配 = 连接词使用与构建类型不匹配 |

---
