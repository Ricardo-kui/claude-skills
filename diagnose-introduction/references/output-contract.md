# 输出接口契约（供下游 Skill 消费）

本 Skill 的诊断报告采用**结构化字段格式**，可被下游 Skill 自动解析。

## 机器可读字段

```yaml
diagnostic_schema_version: 2        # 必填. 当前版本为 2
gap_type: "Incompleteness"        # 必填. 取值: Incompleteness | Inadequacy | Incommensurability
gap_strength: "低"                 # 必填. 取值: 低 | 中 | 高
conversation_strategy: "Progressive Coherence"  # 必填. 取值: Progressive Coherence | Synthesized Coherence | Non-Coherence
makadok_dimension: "Mechanism"    # 必填. 取值: Constructs | Mechanism | Boundary | Phenomenon | Level | Mode | Question | Output
core_lever: "Why"                 # 必填. 取值: What | Why | When/Where | Where | Who | How | Input | Output
exemplar_paper: "Wu 2025"         # 必填. 最匹配的范文
exemplar_journal: "SMJ"           # 可选. 范文期刊
hook_strategy: "Cold-start definition"  # 可选. 推荐的 Hook 策略
target_journal: "SMJ"             # 可选. 用户目标期刊
risk: "最容易被解读为增量研究；必须解释遗漏的理论重要性"  # 必填. 核心风险提醒
puzzle: "数字化转型如何影响企业绩效？"  # 新增: broad puzzle 一句话陈述
puzzle_broadness: "合适"           # 新增: 必填. 取值: 合适 | 过宽 | 过窄 | 缺失
puzzle_gap_alignment: "有层次"     # 新增: 必填. 取值: 有层次 | 跳跃 | 混为一谈
audience_clarity: "高"             # 新增: 必填. 取值: 高 | 中 | 低
rq_contains_tension: "是"          # 新增: 必填. 取值: 是 | 否 | 部分
rq_quality: "高"                  # 新增: 必填. 取值: 高 | 中 | 低
jtbd:                             # JTBD 6-Block 交叉诊断
  target_audience: "technology strategy and organizational theory scholars"  # 具体受众描述
  gain_or_pain: "如果不考虑组织惯例更新机制，就无法解释为何有些企业数字化转型成功而有些失败"  # 具体 gain/pain 描述
  pain_specificity: "高"           # 必填. 取值: 高 | 中 | 低
  claim_fit: "是"                 # 必填. 取值: 是 | 否 | 部分
gbl_four_moves:
  significance: "pass"            # 必填. 取值: pass | partial | missing
  literature_situation: "pass"    # 必填. 取值: pass | partial | missing
  problematization: "pass"        # 必填. 取值: pass | partial | missing
  response_foreshadow: "pass"     # 必填. 取值: pass | partial | missing
  overall: "aligned"              # 必填. 取值: aligned | partial | incomplete
  repair_priority: "说明组织惯例更新如何直接回答机制缺口"  # 必填. 只列一个修复
```

## 兼容规则

- 缺少 `diagnostic_schema_version` 时按旧版输入读取；若没有
  `gbl_four_moves`，由 `/write-introduction` 使用现有字段推导。
- `diagnostic_schema_version: 2` 使用上述接口。
- 遇到大于 `2` 的未知版本时停止自动消费并提示重新运行诊断，不猜测字段语义。

## 消费方式

下游 Skill（如 `/write-introduction`）可直接解析上述字段：
- `gap_type` → `<gap-type>` 参数
- `makadok_dimension` → `<contribution-dimension>` 参数
- `exemplar_paper` → 用于匹配 combination 编号

**人工消费方式**：用户直接复制 "输出接口契约" 区块，粘贴到 `/write-introduction` 调用中。
