# E1.1 分组调节（Categorical/Group-based Moderation）

> **适用**: Moderator 为分类变量（high/low, Type A/Type B, Class I/II/III）
> **与连续调节的区别**: 不检验交互项，而是分样本检验或比较组间系数差异
> **范文**: Darby_2024_MSOM (severity分组), Darby_2025_JSCM (defect type分组)
> **母变体**: E 调节效应型

---

## 关键句式模板

**分组差异预告**：
```
"The [effect of X on Y] will differ for [W=A] and [W=B], such that 
[effect description for group A] whereas [effect description for group B]."
```

**对比机制论证**：
```
"[W=A 时的机制]. In contrast, [W=B 时的机制]. This contrast arises because 
[underlying theoretical reason for the group difference]."
```

**对称对比结构**：
```
"For [W=A], [mechanism A]. [Evidence A]. In contrast, for [W=B], [mechanism B]. 
[Evidence B]. Given these differences, we expect:"
```

---

## 假设陈述格式

| 类型 | 模板 | 示例 |
|------|------|------|
| 分组差异 | "H[N]. The [positive/negative] effect of [X] on [Y] will be [stronger/weaker] for [W=A] than for [W=B]." | H2. Spillover effect stronger for manufacturing defects than design defects. |
| 分组方向差异 | "H[N]. [X] is [positively/negatively] related to [Y] for [W=A], but [unrelated/positively/negatively] related to [Y] for [W=B]." | H3. Effect exists for high-severity but not low-severity recalls. |

---

## 语料锚定

- **Darby 2024 (MSOM)** — severity 分组（high vs low）
  - 对称结构："For high-severity recalls... In contrast, for low-severity recalls..."
  - 机制差异：high-severity 触发更强的市场惩罚预期 → 更快响应；low-severity 惩罚预期弱 → 响应延迟

- **Darby 2025 (JSCM)** — defect type 分组（manufacturing vs design）
  - 对称结构："For manufacturing defects... In contrast, for design defects..."
  - 机制差异：manufacturing defects 责任明确 → 溢出效应强；design defects 责任模糊 → 溢出效应弱

---

## QC 检查点

- [ ] 分组是否基于理论上有意义的分类（而非数据驱动的中位数分割）？
- [ ] 是否对每组分别提供了独立的机制论证（而非只论证一组）？
- [ ] 是否使用 "In contrast" / "Conversely" 明确标记组间对比？
- [ ] 若使用分样本分析而非交互项，是否在 Methods 中说明原因？
