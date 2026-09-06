# _immediate-exemplar-protocol.md — 即时范文学习对象（write-* 四节共用协议）

> 单一事实源：write-introduction Phase 1.5 / write-theory / write-methods / write-results 的「即时范文学习对象」共用本协议；各 SKILL.md 只保留差异项（section 名 / learning block / retrieval_signals 例）。
> 本次调用私有：不写项目文件、不改 canonical `story`、不更新 paper-state。

## 触发与跳过

- **执行**：该 section 的完整生成/重构请求，且本次 story gate 为 PASS 或 PROVISIONAL（results 的 evidence intake 模式已声明时同等有效）。
- **跳过**：单模块/单假设/单槽位/单系数请求、句子润色、标题、local-only/local_rewrite、显式 `--exemplars=off`。

## 步骤

1. **生成临时 request**（仅本次调用有效）：`section`（见差异表）、paper_type、当前 story needs、`retrieval_signals`（该节特有的形状信号）；`validated_conditions` 仅在本次 gate 已证实时填入，不确定留空——宁可不推荐也不放宽范文适用前提。
2. **检索**：`py ../story-blueprints/scripts/retrieve_exemplars.py --request <临时 JSON>`；结果非空则**只读**被选中的 1–2 张 v0.4-lite 卡的对应 learning block，不加载整库。
3. **推荐四问**：只回答"学什么 / 为何适配 / 不能照搬什么 / 应比较什么"。不得把范文类型改写成用户项目的强制 story frame，不得凭范文生成贡献、机制或结果。
4. **无匹配明示**：明确报告"当前 v0.4-lite 库无适合的 <section> 学习对象"并继续正常写作；不得凑数或回退未经评估的旧版蓝图。

## 完成判据

推荐已显示或已明确无匹配；推荐不改变该节诊断（Gap / 构建类型 / 设计类型 / 证据判决）与 story 契约的权威地位。

## 各节差异项

| skill | section | learning block | retrieval_signals 例 |
|---|---|---|---|
| write-introduction | `introduction` | v0.4-lite 卡 Introduction block | story needs：clarify-theme / establish-genuine-tension / introduce-main-characters |
| write-theory | `theory` | `section_learning.theory` | why-chain 形状、构念辨析、假设树组织、调节元框架 |
| write-methods | `methods` | `section_learning.methods` | M2.5 model-free evidence、M8 识别策略辩护、M6 竞争性解释组织 |
| write-results | `results` | `section_learning.results` | 四拍节奏、threat 组织的稳健性段、mixed/null 诚实披露、claim 层级校准 |
