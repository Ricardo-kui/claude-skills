# Phase 5 — 质量验证、QC 输出、技能版本影响

生成最终的蒸馏质量报告，确保产出物可以安全进入 Skill 更新流程。

## QC Checklist

- [ ] **Completeness**: 所有强制槽位（根据设计类型）已被覆盖
- [ ] **Clarity**: 每个骨架都有明确的 [占位符] 和插入位置
- [ ] **Credibility**: 未将单篇论文的特殊做法泛化为通用规则
- [ ] **Replicability**: 骨架填入具体信息后，能生成类似顶刊风格的段落
- [ ] **Substance not Verbatim**: 具体事实已泛化为 [placeholder]；论证结构和过渡句式可保留原貌
- [ ] **Fact Boundary**: 所有不可迁移事实已被明确标记
- [ ] **Causal Language Audit**: 提取的骨架中因果语言强度与设计类型匹配
- [ ] **Skill Update Audit**: Phase 4 的每个 `ADD/EXTEND/REPLACE` 指令都有明确的目标文件和插入位置
- [ ] **Story Fidelity Audit**: 每个 adoption 指令都有 classification；单篇论文未改变核心规则

## 反向验证（可选 gate）

QC 通过后，本次蒸馏的 `*_methods_distilled.json` 可喂给本地反向验证工具 `reverse_validation_pipeline`，检验 `write-methods` 语料能否反向复现蒸馏出的 M 槽位结构与模板选择（"语料写不写得出来"）。用法与输出契约见 `reverse_validation_pipeline/SKILL.md`（skill：`reverse-validation-pipeline`；入口 `python reverse_validation_pipeline.py --methods-json ... --output-dir ...`）。critical gap → 先补语料/`design_type_map.json` 映射，再入库。

## skill_version_impact（新增）

每个 `ADD/EXTEND/REPLACE` 行动必须附带版本影响评估：

```yaml
phase_5_skill_version_impact:
  write_methods:
    current_version: "3.0.0"
    suggested_version: "3.1.0"  # 或 "3.0.0"（仅 minor 时不变）
    bump_reason: "ADD 6 个变体 / EXTEND 2 个变体 / 新增 1 个主骨架警告"
    changed_files:
      - "生存分析.md: +2 变体 (13-14)"
      - "面板数据-OLS.md: +1 变体 (9)"
      - "INDEX.md: 更新表行和计数"
    main_skeleton_updates:
      - "生存分析 M7: 增加 CEM 预处理建议行"
      - "面板数据-OLS M2: 增加多数据库合并替代方案注释"
  distill_methods:
    current_version: "1.1.0"
    suggested_version: "1.1.0"  # 本次蒸馏未发现 skill 自身协议需修改
```

## 最终输出物清单

1. **Phase 4 Skill Update Instructions**（候选技能更新指令——随待写入预览块输出，经用户确认后执行）
2. **Expression Skeletons**（仅含 `skill_gap != SKIP` 的骨架）
3. **Validity Logic Map**（该设计类型的 threat 处理模式）
4. **Methods DNA with Skill Comparison**（DNA 指标 + skill 对比解读）
5. **Skill Version Impact**（版本号建议 + 变更文件清单）
6. **学习要点**（3-5 条：这篇论文最值得学的叙事手法 + 为什么有效）
7. **可改进之处**（这篇顶刊论文 Methods 仍然可以做得更好的地方——反哺 skill 的警告列表）
8. **QC Result**（通过/需修正/拒绝入库）
