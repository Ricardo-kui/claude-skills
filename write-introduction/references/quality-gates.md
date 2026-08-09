# Quality Gates — Introduction 生成后质量门（从 SKILL.md 下沉，v0.1）

> 由 write-introduction Phase 4 **必过**：JTBD 六模块完整性 + claim_fit + GBL Four-Move 对齐 + 首尾句测试。不合格项标入"提醒"段的修复建议。

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

## 3. 首尾句测试（JIBS）

只读每段首尾句——能否传达核心故事？四段首句连起来是否构成连贯叙事？不合格 = editor 在 2 分钟内判定 story diffuse，倾向 desk reject。
