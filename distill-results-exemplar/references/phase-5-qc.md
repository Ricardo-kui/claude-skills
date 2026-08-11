# Phase 5 — 质量验证、QC 输出、技能版本影响

## QC Checklist

- [ ] **Completeness**: 所有强制槽位已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊统计发现泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的 Results 段落
- [ ] **Substance not Verbatim**: 具体事实已泛化为 [placeholder]；节奏标记和过渡句式可保留原貌
- [ ] **Fact Boundary**: 所有不可迁移统计事实已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与估计器类型匹配
- [ ] **Nonsignificant Audit**: 如果原文有非显著假设，蒸馏报告是否记录了其句式处理
- [ ] **Robustness Audit**: 稳健性检验是否按 threat 组织，而非机械列表
- [ ] **Skill Update Audit**: Phase 4 的每个 ADD/EXTEND/REPLACE 指令都有明确的目标文件和插入位置
- [ ] **Story Fidelity Audit**: headline answer/climax 与 robustness/falling action 已判定，单篇论文未改变核心规则

## skill_version_impact（新增）

```yaml
phase_5_skill_version_impact:
  write_results:
    current_version: "3.0.0"
    suggested_version: "3.1.0"
    bump_reason: "ADD 5 个变体 / EXTEND 2 个变体 / 新增 1 个 R7 主骨架要求"
    changed_files:
      - "生存分析.md: +2 变体"
      - "OLS-FE.md: +1 变体"
    main_skeleton_updates:
      - "生存分析 R3: 增加 exp(β)−1 百分比翻译拍"
      - "OLS-FE R7: 强制 threat-based 组织"
  distill_results:
    current_version: "1.1.0"
    suggested_version: "1.1.0"
```

## 最终输出物清单

1. **Phase 4 Skill Update Instructions**（候选技能更新指令——随待写入预览块输出，经用户确认后执行）
2. **Expression Skeletons**（仅含 skill_gap != SKIP 的骨架）
3. **Rhythm Map**（假设检验节奏、稳健性节奏）
4. **Results DNA with Skill Comparison**（DNA 指标 + skill 对比解读）
5. **Skill Version Impact**（版本号建议 + 变更文件清单）
6. **学习要点**（3-5 条：这篇论文最值得学的 Results 叙事手法 + 为什么有效）
7. **可改进之处**（这篇顶刊论文 Results 仍然可以做得更好的地方——反哺 skill 的警告列表）
8. **QC Result**（通过/需修正/拒绝入库）
