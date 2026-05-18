---
name: check-alignment
status: deprecated
description: 此 Skill 的功能已合并到 paper-review 中。请使用 /paper-review 获取跨 Section 对齐检查（假设-变量映射、承诺-兑现对照、5 种断裂识别、3 分钟快速测试）。
version: 1.1.0-merged
---

# 已合并

`check-alignment` 的功能已整合至 `/paper-review` 的 **Step 1b: 跨 Section 对齐检查** 中。

## 替代用法

```
/paper-review <文件路径>
```

在 `/paper-review` 的输出中，您将获得：
- **1b.2 Theory ↔ Methods 对齐**：假设-变量映射表
- **1b.4 Results ↔ Discussion 对齐**：承诺-兑现对照表
- **1b.5 断裂识别**：5 种常见断裂类型
- **1b.6 3 分钟快速测试**：4 个快速验证问题

## 合并时间

2026-05-16 — 作为 skill 重构优化的一部分，减少冗余并提升总控 skill 的完整性。
