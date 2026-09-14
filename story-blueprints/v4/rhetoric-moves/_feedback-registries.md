# 批评双登记（write-* 家族唯一源）

write-* 四 skill 的用户批评登记共用双 registry 分工，两者不互相替代。本文件是分工定义的
唯一源；各 SKILL.md 只保留触发条件与本 skill 差异，不复述 registry 内容。

| 通道 | registry | 职能 | 内容与维护 |
|---|---|---|---|
| **R1 可执行修订规则** | 各 skill 自有 `<skill>/references/feedback-registry.json` | 下一轮 revision 生成前加载执行 | `<skill>/scripts/record_feedback.py` 维护；每条含 scope/category/rule/reason/source/evidence，不得只累计 revise/reject 次数；新裁定覆盖旧建议记 `supersedes`；语态基准/失效建议/确定性禁用表达分入 `benchmark`/`supersedes`/`prohibited_patterns`；scope 维度按节（methods=`skill\|project\|section\|design_type`，results=`skill\|project\|section\|estimator`） |
| **R2 语料精炼信号** | 各 skill 自有 `<skill>/corpus/_evidence_registry.yaml` 的 `critique.per_file` | 供对应 `distill-*-exemplar` 选材 Gate 消费，驱动语料精炼 | `revise`/`reject` +1；reasons 去重首插 ≤8 条；不登记风格偏好与流程抱怨 |

## 家族共性

- 先修正文稿，不以「已登记」替代当前任务。
- 项目规则不得污染其他论文；单项目批评不自动修改 corpus——精炼由对应 distill skill 的选材 Gate 驱动。
- 相同规则跨案例重复或累计达到阈值后，才进入 distill 侧的 ADD/EXTEND/REPLACE 候选。

## 各 skill 差异

- **write-results**：双轨全接（参照实现）。
- **write-methods**：双轨全接；R2 仅当批评确实指向某一设计类型变体时汇总聚合质量信号。
- **write-theory**：接 R2（差异项：只登记对**变体产出质量**的批评）；规则层缺陷走演化通道
  `<skill>/corpus/_skill_design_feedback.yaml`（门控见 `../distill-theory-exemplar/references/design-feedback-loop.md`）；R1 未建设。
- **write-introduction**：接 R2；R1 未建设（需要可执行修订规则时先建
  `<skill>/references/feedback-registry.json` + `record_feedback` 脚本）。
