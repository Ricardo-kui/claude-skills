# Post-Generation Checklist — 生成后自检清单（从 SKILL.md 下沉，v0.1）

> 由 write-methods 生成 Methods 段落后**逐条核对**。

## Completeness
- [ ] revision 模式已读取当前 Methods 正文与修订记录，并明确 manuscript/audit 边界
- [ ] M1：研究情境有至少 3 个理由，且与理论机制直接挂钩
- [ ] M2：样本漏斗包含起始总体 → 每步排除（理由+数字）→ 最终 N
- [ ] M2.5（如适用）：复杂识别设计前是否插入 model-free evidence 作为可信度铺垫
- [ ] M3：因变量有构念定义 + 操作化 + 测量来源 + 方向解释
- [ ] M4：每假设一段，含 Hypothesis 编号对齐，变量按理论顺序排列
- [ ] M5（如适用）：当前 Theory/设计确有调节、中介或机制变量时才写；已撤销变量不因旧稿或 corpus 恢复
- [ ] M6：每个控制变量都有 because [rival explanation]
- [ ] M7：estimator + fixed effects + SE clustering + 选择理由（文字+诊断）
- [ ] M7补充：若 Theory 含调节假设，检验方法（MMR / 分组相关比较 / HLM 跨层交互）与 differential prediction/differential validity 声明一致
- [ ] M8（如适用）：基准识别策略的关键假设 + 检验方法 + 结果位置；补充稳健性不提前搬入
- [ ] M10（如保留）：Results 预告不含系数、显著性或支持判断；无必要时省略

## Clarity
- [ ] 变量名与 Results 表格完全一致
- [ ] 时间顺序明确（滞后几期、事件窗口、观测期起止）
- [ ] 因果语言强度与 design strength 匹配
- [ ] 所有 [placeholder] 已被替换，无残留方括号
- [ ] 完成的研究程序使用主动过去时；定义、制度事实、公式项与估计器性质使用现在时
- [ ] active feedback 的术语、样本、时间窗、语态与 section/design-type 约束全部落实
- [ ] `supersedes` 指向的旧建议、旧构念和 stale source 没有复活
- [ ] `lint_methods_language.py` 已对正文运行并通过；修订记录中的反例未被误算为正文

## Credibility
- [ ] 识别假设有检验（平行趋势/过度识别/manipulation check）
- [ ] 样本漏斗可审计（每步有数字和排除理由）
- [ ] 模型选择有文字解释，不埋在方程里
- [ ] 非显著假设在 Methods 中未预告支持状态
- [ ] 非基准的 selection/endogeneity/robustness/mechanism/heterogeneity 分析仍由 Results 承担

### Three-horned dilemma 自我定位（McGrath 1982 / Pollock Ch07）
所有研究设计都 "fatally flawed"——沿**测量精度（measurement precision）/ 可推广性（generalizability）/ 情境真实度（contextual realism）**三维度排列，**最多只能在两个维度强、第三个弱**。
- [ ] **识别本设计在三角上的强弱位置**：实验（高 precision / 低 realism）；档案数据（高 realism / 低 precision / 受 context 限制）；调查（高 generalizability / obtrusive）。
- [ ] **承认弱点本身就是 credibility 来源**——"Demonstrating you are aware of your study's weaknesses enhances your credibility"。
- [ ] **限制 claims 与设计 strength 一致**：截面相关设计不用 "cause"；单情境研究不 overclaim generalizability。
- [ ] **桥接 Discussion limitations**：本设计在三角上的弱点分析直接成为 Discussion limitations 的论证基础（不是事后找借口，而是 Methods 已自我定位的延伸）。discussion-review 的 limitations 审查应回扣此处。

### 四类效度整体映射（Pollock Ch07）
Pollock 不把四类效度当 checklist 逐条回答，而是嵌入 describe-explain-justify + 三 C。但作者应能系统回答"本设计对哪类 validity 最强/最弱"：
- [ ] **Internal validity**（无替代解释的因果）——若做因果声明，是否排除威胁？截面相关应用 "associated with" 非 "cause"。
- [ ] **External validity**（跨主体/情境/时间稳定）——是否充分描述 context 让读者判断相似性？是否 bound 理论与 claims？
- [ ] **Construct validity**（操作化反映构念，三层面）——Theory 定义清楚 / Methods measures 反映构念 / Results 实证关系反映理论关系。
- [ ] **Statistical conclusion validity**（统计检验准确）——sample 够大无偏 / measures 准确 / 分析方法适合数据不向 Type I/II 偏斜。
- [ ] **元层判断**：本设计对哪类 validity 最弱？该弱点是否已在 three-horned dilemma 自我定位中承认、并在 Discussion limitations 中 bounded？

## 论证质量诊断
- [ ] **Because 密度**：M6 中每个控制变量都有 "because [rival explanation]"——这是 Methods 说服力的核心来源
- [ ] **假设对齐**：M4/M5 中每预测变量明确提及对应 Hypothesis 编号
- [ ] **因果语言自律**：面板数据用 "associated with"；自然实验识别支持后用 "effect of"；实验可用 "caused"。无越级
- [ ] **审计链完整**：M2 起始 N → 每步排除（含理由+数字）→ 最终 N，全程可追踪
- [ ] **时间逻辑清晰**：所有预测变量标注 t-1 / contemporaneous / event window
- [ ] **段落体裁适配**：Methods 段落遵循审计体裁约定——procedure-first（M2 样本漏斗）/ construct-first（M3–M5 变量）/ justification-first（M7 模型）为合法段首；通用段落规则见 `../write-introduction/corpus/storytelling/prose-craft-checklist.md` §0.0/§0.2/§0.5；§0.1/§0.3/§0.6 为说服体裁专用，不适用
- [ ] **反馈回归**：`feedback-registry.json` 中与 skill/project/section/design_type 匹配的 active rules 均有 pass/fail 结果

## 反向审查（可选但建议）
生成完成后，可使用 `/distill-methods-exemplar` 对输出段落进行反向蒸馏审查，生成 Vault 参考注释，供人工判断：
- 槽位覆盖是否完整（M1–M10）
- 表达骨架是否可迁移（无机构名/政策名残留）
- 因果语言强度是否与 design strength 匹配
- 识别策略和 validity threat 处理是否达到顶刊 ritual 标准

**注意**：反向审查产出存入 Vault，不自动修改本 skill 的骨架库。是否采纳为 skill 参考由人工决定。
