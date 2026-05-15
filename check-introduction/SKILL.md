---
name: check-introduction
status: deprecated
description: 此 Skill 的功能已合并到 intro-review --deep 模式中。请使用 /intro-review --deep 获取六层 QC、Gap/Makadok 推断、期刊风格匹配、范文对比和通用禁忌检查。
version: 1.1.0-merged
---

# 已合并

`check-introduction` 的功能已整合至 `/intro-review` 的 **`--deep` 深度模式** 中。

## 替代用法

**快速模式**（默认）：
```
/intro-review <文件路径>
```
提供：逐段结构解析 + 标准 QC 检查 + 改写建议

**深度模式**（原 check-introduction 功能）：
```
/intro-review <文件路径> --deep
```
额外提供：
- **六层 QC**：Hook-Gap / Conversation / Problematization / Makadok / 期刊风格 / 范文对比
- **推断诊断**：自动推断 Gap 类型、Makadok 维度、最接近范文
- **通用禁忌检查**："few studies" / "important because" / "purpose is to" 等禁忌检测

## 合并时间

2026-05-16 — 作为 skill 重构优化的一部分，将深度 QC 功能合并到 intro-review 中，通过 `--deep` 参数切换模式，减少 skill 数量并统一调用接口。
