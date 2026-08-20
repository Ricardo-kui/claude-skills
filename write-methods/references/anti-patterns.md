# Anti-Patterns — Methods 常见反模式（从 SKILL.md 下沉，v0.1）

> 由 write-methods 生成段落前**先生效**——以下错误在 Methods 中高频出现，生成前主动排查。

- **模型选择无文字解释**：只写 "we estimate FE model" 而不解释为什么 FE 优于 RE/OLS，或为什么选此 estimator
- **控制变量无 because**：列出 Size, Age, ROA 但不解释每个变量控制的是什么竞争性解释
- **因果语言越级**：面板数据 design 下使用 "caused" "led to" 等强因果词；自然实验未通过平行趋势检验就用 "effect of... on..."
- **样本漏斗缺数字**：写 "we exclude missing values" 但不报告每一步损失了多少观测
- **识别策略后置或缺失**：DiD/IV/自然实验不把识别假设和检验放在核心位置，而是 buried 在脚注或附录
- **交互/非线性模型无解释策略**：加入 interaction/nonlinear term 后未预告如何在 Results 中解释（marginal effects / simple slopes / AME）
- **调节假设检验错位**：Theory 声明 differential validity（关系强度变化）却用 MMR 交互项检验；或声明 differential prediction（slope 变化）却用分组相关比较检验
- **时间顺序模糊**：未明确说明预测变量是 t-1 还是 contemporaneous，或事件窗口的起止逻辑
- **Bad Control 问题**：在 DiD/自然实验中控制了 post-treatment 变量或 collider
- **设计排他性混淆**：把 IV 的语言习惯（"effect of X on Y"）套用到 OLS/FE 设计；把实验的操纵检验语言套用到档案数据
- **动态面板 FE 陷阱**：为短面板推荐固定效应而不提示 Nickell bias 或提供 GMM 替代方案
- **过度泛化诊断要求**：为非 IV 设计要求排他性约束检验，为非 DiD 设计要求平行趋势检验，为非匹配设计要求重叠支撑检验
- **机构/政策名残留**：用户填入的 [placeholder] 中混入了论文特有的机构名、政策名、数据库名，导致段落不可迁移到其他情境
- **旧稿压过现稿**：未读取当前 Methods 与修订记录，继续用旧 Theory、旧 DOCX 或会话摘要恢复已删除的假设、变量或章节
- **Methods–Results 回流**：把非基准的内生性、样本修正、替代测量、机制或异质性分析重新塞入 Methods，只因为 corpus 中存在相似段落
- **槽位越界**：在 M3–M5 的测量定义中提前解释估计器、条件 estimand 或结果，或在 M7 重新定义变量
- **反馈只计数**：只把用户不满记成某设计类型 revise/reject 次数，没有保留原因、范围、替代规则和旧建议覆盖关系
- **失效建议复活**：revision history 或 corpus 中仍出现旧措辞，生成时因此把用户已作废的建议重新写入正文
