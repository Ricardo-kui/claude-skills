# 机制推演句语料库

## Why chain 连接词谱系

```
"X affects Y because [mechanism]." 
→ "[First-order effect] occurs when [condition]."
→ "This in turn generates [second-order effect] because [reason]."
→ "Consequently, [DV] [increases/decreases/changes] through [final mechanism step]."
```

**因果链信号词**：
"Consequently," / "As a result," / "This in turn" / "Thereby" / "Thus" / 
"Through this process," / "These dynamics suggest that" / "Building on this logic,"

---

## 单步机制链（基础）

**模板**：
```
"When [IV condition holds], [first-order consequence] occurs because [mechanism step 1]. 
Consequently, [DV outcome] emerges through [final link]. Thus:"
```

**语料锚定**：
- Darby 2024 (MSOM) — recall speed → spillover 单步链

---

## 两步机制链（标准）

**模板**：
```
"When [IV condition holds], [first-order consequence] occurs because [mechanism step 1]. 
This [first-order consequence] in turn generates [second-order consequence] because 
[mechanism step 2]. Consequently, [DV outcome] emerges through [mechanism step 3]. 
Thus:"
```

**语料锚定**：
- Wu 2025 (OrgSci) — digital transformation → routine updating → innovation
- Keeves 2017 (AMJ) — 标准两步链范式

---

## 双轨并行机制链（Track A / Track B）

**Track A（损失规避/保护路径）**：
```
"[X_A] reflects '[定义]' ([文献]). However, this [状态] remains vulnerable to 
[威胁]. Since [机制] are highly sensitive to [波动源], even small changes can 
dramatically alter their worth, creating powerful incentives for [主体] to protect 
[X_A] ([文献]). To illustrate, consider [具体数字例子]."

"According to [理论]'s focus on [心理机制A], [主体] are likely to take actions 
to minimize these losses. More specifically, we propose that [主体] might [行为]. 
Therefore: H[N]: [X_A] → [Y] (+)"
```

**Track B（追求/增益路径）**：
```
"[X_B] reflects '[定义]' ([文献]). [高X_B主体] are oriented toward [长期目标]. 
[文献] supported this distinction, demonstrating that [证据]."

"We argue that [高X_B主体] are more likely to prioritize [长期目标] by opting 
for [开放行为]. While [情境] may have short-term negative impacts, [正面重framing]. 
[短期行为] might yield short-term benefits. However, as information emerges, these 
tactics are likely to be revealed, reducing their effectiveness. Furthermore, 
[开放行为] can help [主体] engage [利益相关者], leading to [积极结果]."

"In summary, high [X_B] reduces [主体]'s reliance on short-term [Y]. Therefore: 
H[M]: [X_B] → [Y] (-)"
```

**语料锚定**：
- Malik 2025 (JM) — current wealth (loss aversion) vs prospective wealth (long-term focus)

**轨道切换信号词**：
"Conversely" / "In contrast" / "Whereas" / "On the other hand"

---

## 竞争机制链（路径 A vs 路径 B）

**竞争预告**：
```
"However, the literatures on [领域A] and [领域B] offer potentially conflicting 
arguments as to the influence of [X] on [Y]."
```

**路径 A**：
```
"On the one hand, [X_high] may [increase/decrease] [Y] because [mechanism_A]. 
Research suggests that [X_high] are more [特征] and, correspondingly, [行为] 
([文献]). In other words, this research argues that [X_high] tend to [行为2]."
```

**路径 B**：
```
"On the other hand, [X_low] may [increase/decrease] [Y] because [mechanism_B]. 
Indeed, research indicates that [结果] can be particularly [后果], so [X_low] 
who tend to focus on [价值] may be more motivated to [行为3] ([文献])."
```

**语料锚定**：
- Wowak 2025 (MS) — liberal vs conservative CEO recall behavior

---

## 数字实例化机制句

**适用**：金融/会计概念（option value, stock price sensitivity）、概率/统计概念

**模板**：
```
"To illustrate, consider [主体] holding [具体参数]. A [百分比] decline in 
[变量] to [新参数] would cause [百分比] loss of [指标], as [解释]. Similarly, 
[文献] found that [实证证据]. On average, [统计数字]."
```

**语料锚定**：
- Malik 2025 (JM) — "$99 strike price... A 1% decline in stock price to $99 would cause a 100% loss of the option's intrinsic value"

**QC**：数字例子必须明确标注 "To illustrate"（非 "For example"）

---

## 用文献支撑机制（非罗列）

**模板**：
```
"[Research stream] has shown that [specific mechanism element]. [Author A (year)] 
found that [specific finding], suggesting that [theoretical interpretation]. 
[Author B (year)] extended this logic by demonstrating that [additional mechanism 
element]. Together, these studies suggest that [synthesis], yet they have not 
considered [gap that current hypothesis addresses]."
```

**反模式**：
❌ "(Author A, 2018; Author B, 2019; Author C, 2020)" — 无 argument 总结
✅ "Author A (2018) found that [finding], suggesting that [interpretation]..."
