# Phase 0 — 论文类型与设计分类

> **输入纪律（2026-08-20 起）**：若输入来自 distill-paper-exemplar 编排（PDM 工作目录），
> 只读 `<citekey>.pdm/sections/<本节>.md` 物化切片；需要全文上下文时读
> `fulltext.text-only.md`。**禁止直接读原始 paper-import MD**——其中 44–89% 字节是
> base64 图片单行巨串，读入即炸上下文。单独调用本 skill 且只有原始 MD 时，先运行
> `distill-paper-exemplar/scripts/preprocess_l0.py <MD>` 再读产物。

在读取正文前，先判断这篇论文 Methods 的**设计范式**，决定后续槽位检查清单和蒸馏焦点。

## 分类维度

| 维度 | 选项 |
|------|------|
| 数据形态 | 面板数据 / 截面数据 / 实验 / 多研究 / 质性→量化 |
| 识别策略 | OLS/FE / 自然实验/DiD / IV/2SLS / RDD / 匹配 / 实验随机化 |
| 估计器 | 线性 / Logit/Probit / 生存分析 / 计数模型 / SEM / GMM / Tobit |
| 特殊结构 | 多行为者 / 网络效应 / 文本构念 / 堆叠扩散 / 同时方程 |
| 因果强度 | 描述性 / 预测性 / 因果识别（quasi-experimental）/ 实验因果 |

## 输出格式

```yaml
paper_id: "[作者_年份_期刊]"
phase_0_design_profile:
  data_architecture: "面板数据 / 截面 / 实验 / ..."
  identification_strategy: "OLS+FE / DiD / IV / ..."
  estimator_family: "线性 / 非线性 / 生存 / ..."
  special_structure: "无 / 匹配DiD / 文本构念 / ..."
  causal_ambition: "描述 / 预测 / 准实验因果 / 实验因果"
```
