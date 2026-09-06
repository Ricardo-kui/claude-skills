# Quality Gates — Introduction 生成后质量门（从 SKILL.md 下沉，v0.1）

> 由 write-introduction Phase 4 **必过**：JTBD 六模块完整性 + claim_fit + GBL Four-Move 对齐 + 首尾句测试 + 异议预判（Gate 4）+ 段落论证文法（Gate 5）。不合格项标入"提醒"段的修复建议。

## 1. GBL Four-Move 对齐（Phase 1.1 复用 + 输出核对）

完整 Introduction、`front-end` 或 `align` 输出均读取 `../diagnose-introduction/references/golden-biddle-locke-four-moves.md`。若上游 `/diagnose-introduction` 提供了 `gbl_four_moves`，先消费该块；否则从 canonical `story`、Gap 诊断、Audience 与 contribution promise 推导。接受缺失 `diagnostic_schema_version` 的旧诊断输出；版本为 `2` 时读取 `gbl_four_moves`；遇到大于 `2` 的未知版本时停止自动消费并提示重新诊断。

默认执行轻量 Four-Move 检查：

| Move | Introduction 功能 |
|------|-------------------|
| Significance | Hook + Stakes |
| Literature situation | Literature Turn |
| Problematization | Tension + theoretical consequence |
| Response foreshadow | Theory Lens + RQ/Preview + Contribution |

**Four Moves 是功能而非段数**：按期刊和 Introduction 长度合并功能，不机械要求一段一个 move。Four Moves 不构成新写作模式，也不写入 `paper-state.yaml`。缺失 move 时，在骨架中保留证据占位符并给出一个优先修复；不用 GBL 检查绕过故事阶段或证据门控。

定性/过程研究：Four-Move 导向从 predict 转为 **foreshadow**（Response foreshadow = 研究旅程预示而非假设预告），并检查 field engagement 是否被转化为一条面向学科读者的 theorized storyline；量化研究不强制使用 field-story 语言。

## 2. JTBD 交叉验证（Simsek & Li 2022——生成侧消费）

骨架渲染完成后，对照 JTBD 六模块验证 utility 完整性（diagnose-introduction Step 6 的交叉验证在生成侧复现）：

| JTBD Block | 验证问题 | 不合格信号 |
|-----------|---------|-----------|
| **1. Target audience** | Hook 是否锁定具体受众（研究流/理论社群），非泛泛 "researchers/managers"？ | 受众太宽 = "why should anyone care" |
| **2. Progress/challenges** | Literature Turn 是否准确建立已有进展、共享语境及仍待解决的挑战？ | 只列文献，不说明已知与争议 |
| **3. Gain/pain** | Tension+Stakes 是否具体到后果/成本（"state costs or consequences when presenting problems; state benefits to intensify solution"）？ | 只有 "important" 无后果 = gain/pain 太弱 |
| **4. Proposed solution** | Theory Lens/RQ 是否直接回应 gain/pain，而不是另起一个理论问题？ | solution 与 tension 关键词和机制脱节 |
| **5. Credibility** | Preview 是否提前交代理论依据/方法/证据强度（不止描述数据）？ | 只描述数据不 justify 可信度 |
| **6. Implications** | Contribution 是否回到目标受众，说明其理解将从什么转向什么？ | broad claim，未兑现 reader shift |

另做 `claim_fit_check`：Theory Lens 的理论承诺与 Preview 的方法、数据和因果措辞是否匹配；不匹配即列为必须修复。

**Contribution 主张质量（claim_fit 扩展，Booth Ch06）**——对核心贡献句（Contribution 模块与 Theory Lens 的 core claim）加测三项：
- **Contestability 反命题测试**：写出贡献句的反命题，命中任一弱主张信号即不合格——纯主题宣告（反命题无意义："本研究考察 X"）、易验证事实（反命题明显为假，无人会主张）、伪争议（反命题显然为真，本无对立）。真贡献须有读者可能不信——a reasonable reader could believe otherwise。
- **Specificity**：贡献句点名核心构念与方向/形状——构念名即论证路线图（vague claims lead to vague arguments）；"advances our understanding of X" 类无构念表达不合格。
- **Hedge 校准**：主张逻辑强度与证据状态匹配——anti-pattern ④ 管词面夸大词，此处管逻辑强度：证据只支撑 "more likely" 时不得写 "drives"；措辞档位查 `corpus/phrasebank/hedging-strength.md`。

## 3. 首尾句测试（JIBS）

只读每段首尾句——能否传达核心故事？四段首句连起来是否构成连贯叙事？不合格 = editor 在 2 分钟内判定 story diffuse，倾向 desk reject。

## 4. 异议预判（Gate 4，Booth Ch09 §9.1 + Ch14）

论证是社交互动：GBL 四动与 JTBD 门检查"问题讲清楚了没有"，本门检查"**对问题的抵抗被预判了没有**"。审稿人读引言时最先问的往往不是"结论对不对"，而是"这算个问题吗"——problem 级质疑无人接管时，引言读起来像写给没有其他观点的受众（worst verdict 是 "I don't care"，不是 "I don't agree"）。

**清单生成（Phase 2 规划时完成，本门核销；渲染前未做则在此反向补做并回填骨架）**：对以下三类各列 **≥1 条最强审稿异议**（Booth Ch09 §9.1 五问归并）：

| 质疑类 | 读者的问题 | 预判自问 |
|---|---|---|
| **问题真实性** | "你凭什么说这是个问题？" | 成本/后果是否重大且**受众也在乎**？Stakes 是否只对作者成立？ |
| **问题定义** | "问题定义对吗？范围管得住吗？" | 读者会不会认为这其实是另一个问题——practical/conceptual 错位、构念错置、范围过大或过小？ |
| **方案可信度** | "信不信这个项目答得了？" | 数据/方法/情境能否让读者相信本文能解决问题（JTBD 模块 5 的怀疑者立场反问）？ |

**核销**：每条异议三选一处置，并标注到具体模块/句位——

1. **正文回应**：Tension/Stakes/Theory Lens/Contribution 内做承认与回应动作（标记词库与回应强度梯度跨节通用：`../write-theory/corpus/sentences/acknowledgment_response.md` §3–§4）；
2. **显式 park**：骨架与提醒段注明由后文哪一节回应（如 Preview 承诺识别策略、Methods 承诺稳健性）；
3. **诚实让步**：无法回应且读者会想到 → 在相应模块用 although 从句加厚主张（承认受众既有信念/冲突证据/限定条件之一）并承诺后文回应（Booth Ch06 thicken the claim）。

**完成判据**：三类各 ≥1 条最强异议；每条有可指认的处置；未处置的最强异议列入"提醒"段并说明为何可留。

## 5. 段落论证文法抽查（Gate 5，Booth Ch05 五要素）

文法与拼贴判据见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md`（先骨架后句子：语料句式按论证角色填位，风格让位于角色）。抽查对象：四个论证型模块（Tension/Stakes/Theory Lens/Contribution）各取信息量最大的一段：

- **五问**：claim（段首 topic sentence）、reason（可质疑的推理 moves）、evidence 锚点（承重 reason 各配）、warrant（需要时）、A&R（预算内）各有句位可指认；
- **拼贴判据**逐条不命中：不承重 / 证据孤儿 / warrant 悬空 / 无主段落 / 引用列队。

不合格处置 = 按角色序列重组该段（骨架重排，语料句子保留），并列入"提醒"段。与首尾句测试（§3）的分工：§3 查跨段叙事连贯，本门查段内论证形状。
