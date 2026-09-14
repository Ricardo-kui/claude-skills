# 选材带词表（distill 家族唯一源）

四个分节 distill skill（introduction/theory/methods/results）的选材 Gate 共用同一带集汇报：
**{gap, 薄弱, critique_heavy, quiet}**。本文件是带定义的唯一源；各节 SKILL.md 只保留自己的
判定数据源（_index / routing 表 / registry）与本节差异，不复述带定义。

| 带 | 定义 | 处理 | 使用节 |
|---|---|---|---|
| **gap** | 中/英复检后仍无命中（零命中≠缺口），或该设计类型/估计器的槽位覆盖存在缺口（静态） | **HIGH**：ADD 候选，优先深读 | 全部四节 |
| **薄弱** | 状态驱动：目标变体 EMERGING（单篇来源且不命中 status_policy 作者/域规则）/ 验证状态低 /「待第二篇交叉验证」 | **HIGH**：EXTEND/REPLACE 候选 | intro / theory |
| **critique_heavy** | 批评驱动：registry `revise + reject ≥ 2`；`common_revise_reasons` 是精炼依据 | **HIGH**：REPLACE/EXTEND 候选 | methods / results |
| **quiet** | 多篇验证 / 其余 | MEDIUM：正常蒸馏（除非论文带来明确新维度） | 全部四节 |

## 跨节规则

- 单篇论文（用户明确指定）不拒绝，但必须输出带判定。
- 批量模式按带排序，优先处理 HIGH 档。
- 频繁使用且好用的变体提升路由权重；语料不因使用频率淘汰（registry `non_signals`）。
- 判定数据源按节而异：introduction 查 `corpus_query.py index`，theory 查 `routing`，
  methods/results 查 `registry`——命令与关键词见各节 SKILL.md 的选材 Gate，本文件不复述。

## 路由行胶囊规范（速查表 / 决策表 / _index 行共用）

distill Phase 4 写入或更新的路由行（methods/results 的「变体速查表」行、intro/theory 的
`_index.md` 行）是路由胶囊，不是正文摘要。行格式纪律：

- **只复述正文已有的内容，不发明正文没有的规则**（Never invent a rule）——行与正文冲突时以正文为准。
- 触发列（适用场景）= 何时路由到该变体；区别列 = 与最近邻变体的分界（取 `distinct_from`）。
- 行内要点 ≤4 条；更多细节留给变体正文——压缩不得改变路由判断（不得为省字符丢失区分度）。
