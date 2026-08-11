# 完整示例 — Pollock QC（introduction 模式）

仅在需要端到端示例时阅读本文件；常规 QC 不预加载。

### 输入
```
/pollock-qc introduction
[粘贴 Introduction 文本]
--journal=SMJ
```

### 输出
```
## Pollock QC 报告（introduction）

### 检查项评分
| QC 项 | 评分 | 问题摘要 | 优先级 |
|-------|------|---------|--------|
| Hook | ✓ | Cold-start definition，温和建立领域，符合 SMJ 风格 | 低 |
| Conversation | △ | 文献回顾较完整，但缺少明确的理论定位（RBV vs 动态能力） | 中 |
| Problematization | ✗ | "few studies have examined" 是典型禁忌，未呈现 puzzle | **高** |
| So what | ✗ | 未解释为什么机制缺失是理论上重要的 | **高** |
| What we learn | △ | Mechanism 维度声明存在，但不够具体 | 中 |

### 最需要修复的 3 个问题
1. **Problematization 使用 "few studies have examined"** — 这是 Incompleteness Gap 的最大风险信号 — 改用 "the mechanism through which... remains unclear" 并增加 "theoretically important because..." — 推荐：`/intro-review <文件路径>`
2. **So what 缺失** — 读者不知道为什么要关心这个研究 — 补充：如果不考虑这个机制，就无法解释为什么有些企业数字化转型成功而有些失败 — 推荐：`/write-introduction Incompleteness Mechanism`
3. **Conversation 理论定位模糊** — 文献回顾像罗列而非对话 — 明确加入理论对话： "While the resource-based view emphasizes... the dynamic capabilities perspective suggests... yet both perspectives overlook..." — 推荐：`/intro-review <文件路径>`

### 修复后回流检查
修改后请确认：
- [ ] Problematization 是否超越了 "few studies have examined"？
- [ ] So what 是否解释了 omission 的理论重要性？
- [ ] Conversation 是否明确加入了理论对话（而非罗列文献）？
```
