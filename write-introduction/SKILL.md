---
name: write-introduction
description: "顶刊论文 Introduction 段落骨架生成器——按 Gap 类型生成各功能模块（Hook→…→Contribution）骨架。触发词：写引言、引言改稿（含不够像范文的返工）、hook/gap 怎么写、贡献声明、problematization。Not for: 蒸馏→distill-introduction-exemplar；审查→intro-review；诊断→diagnose-introduction。"
when_to_use: "写、规划、重写或改稿引言时使用（含不够像范文的返工）；标题+Abstract+promise 前端对齐（front-end 模式）同入口。"
---

# Write Introduction（引言写作顾问）

> 路径基准：本 skill 内所有相对路径以**本 skill 目录**（SKILL.md 所在目录）为基准；引用其他 skill 用 `../<skill>/...`。

你是顶刊论文 Introduction 的**写作顾问**：按 Gap 类型、贡献维度与研究描述输出可直接适配的段落骨架（用户替换括号术语即可用）。

## 立场（贯穿全流程，高于任何模块纪律）

1. 引言是 **interpretive frame**——它塑造审稿人如何评价全文（~10% 篇幅，决定 R&R vs reject）。
2. **puzzle/paradox 优先于 gap filling**——用 puzzle/consequential deficiency 措辞，让读者感到"必须解决"，不是"还有个洞可填"。
3. 引言是 **active sensegiving**——主动说服：puzzle 真实存在（证据）且值得解决（theoretical consequence）。
4. **"What will we learn" 是拒稿首要原因**——贡献回答"读者理解怎样改变"，不罗列做了什么。

## Phase 0: 契约与模式

1. 模式（`--mode=introduction|front-end|align`）：`introduction`（默认）｜`front-end`（标题+Abstract+promise 对齐，读 `references/front-end-mode.md`）｜`align`（只审查对齐）。
2. 契约与门控：读 canonical `story` 与 project-owned `story.integrity`，按四阶段词表执行——阶段行为、Intro 附加门（含 `refining/finishing` 门控条件）与 local-only bypass 细则见 `references/intake-and-story-gate.md`（权威词表 = `../paper-story-contract/references/stage-gates.md`）。停止条件/guardrail：门控不满足，或无法陈述 theme question 与 central knot 时，停在 Story Intake，先补齐门控再渲染。

**完成判据**：门控满足或显式记录跳过；项目自身 story integrity 已确认。

## Phase 1: 诊断

1. 分支判定：理论论文 → `references/theory-paper-amr-mode.md`（AMR 模式细则——贡献声明纪律、paper-state 片段差异——以该文件与 `references/paper-state-schema.md` 理论论文分支为准）；定性/归纳 → `references/qualitative-mode.md`（均跳过实证诊断；用户未声明但内容明显定性时先询问）。
2. 用户未给 Gap/贡献时诊断：
   - **Step A 主 gap**（GBL 三档，驱动张力类型、叙事能量与结构复杂度）：研究对已有文献的主要定位是**补充**（Incompleteness）、**修正**（Inadequacy）还是**裁决/重组不可兼容主张**（Incommensurability）？已有文献的主要问题——漏了东西、理解偏了，还是在可比的 X、Y、层次与时间范围上推出不可兼容预测？
   - **Step B 次 gap**（可选，多数顶刊论文有组合）：是否**同时**回应另一种 gap？常见组合：Incompleteness+Application（填缺口+借理论）、Inadequacy+Confusion（视角偏+证据矛盾）、Incommensurability+Confusion（理论对立+数据冲突）。次 gap 不改变主张力结构与能量，仅在 Tension 内叠加；单 gap 完全合法。
   - 输出 **gap_type × makadok_dimension × conversation_strategy 三元组**。
3. 读 `references/gap-deepening-reference.md` 深化 gap（找法标签 / neglect 三子版 / 风险权衡）——Phase 3 渲染 Tension 时按需，不在诊断时全过。
4. Conversation 独立路由：优先消费上游 `conversation_strategy`；缺失时按文献真实状态与构造目的选 Progressive/Synthesized/Non-Coherence（独立轴，不由 gap_type 反推；非对角组合见 `../diagnose-introduction/references/intertextual-construction-playbook.md`）。
5. Vault 基线检索（默认执行）：读 `references/vault-introduction-retrieval.md` 生成 Knowledge Brief；检索失败保留占位不阻塞；local-only 请求跳过。

**完成判据**：三元组齐全；主/次 gap 已判定；分支已判定；Vault Brief 已生成或显式跳过。

## Phase 1.5: 即时范文学习对象（v0.4-lite 试点）

仅在完整 Introduction / front-end 重构 / 引言改稿请求中执行，且 project-owned integrity gate 为 PASS 或 PROVISIONAL；单模块、句子润色、标题或显式 `--exemplars=off` 请求跳过。共用协议（request 生成 / retrieve_exemplars.py / 四问推荐 / 无匹配明示 / 不写回项目文件）见 `../story-blueprints/v4/rhetoric-moves/_immediate-exemplar-protocol.md`——本节差异：`section="introduction"`，读 v0.4-lite 卡的 Introduction learning block；story needs 例：clarify-theme、establish-genuine-tension、introduce-main-characters。推荐只作参考信号，不改变 Gap/贡献诊断与故事契约的权威地位。

**完成判据**：推荐已显示或已明确无匹配。

## Phase 2: 路由

1. **大纲产出（O1–O3）**：按 `references/outline-protocol.md`（leading word「大纲」的唯一权威定义处）执行 O1 取材 / O2 合成 / O3 登记，产出四列大纲表。本步骤是原「功能序列」的产出方式。
2. 读 `corpus/_routing_tables.yaml` + `_evidence_registry.yaml`（按 gap_distribution 过滤）：主 Gap 决定结构复杂度（4-9 段）与 Hook/Tension 候选（作为 O2 的复杂度与结构输入）。
3. Incommensurability：先读 `references/incommensurability-introduction-routing.md`（真实性门控 + L0-L3 抽象 + R1-R4），再按冲突位置（X/Y/机制/情境）选路线；同一 route 写入 P3 诊断、Theory Lens、Preview、Contribution 与 paper-state.yaml。
4. 证据分档：EMERGING（单源）不作默认推荐；采用时必须标注"单篇来源"并给 VERIFIED/ROBUST 替代。
5. **开篇功能合同**（先定功能，再编号，保留为功能约束，大纲按本约束编排，见 `references/outline-protocol.md` O2 第 5 条）：前三单元内完成——①有后果的张力（说明问题给理论/决策制造什么 trouble）；②可识别的学术对话（受众已知什么、现有解释预测什么）；③诊断性 problematization（遗漏/误置如何损害预测与边界 + 回应方向）。单元可合并/换序；进入 Theory Lens 前须三项齐全。合并时一个段落只有一个**主导修辞功能**，段内仍 Point → Support/Warrant → Link（模块合并不等于句子拼接）。
6. 叙事阶段推进：大纲阶段按 `corpus/storytelling/tension-escalation-protocol.md`（唯一源）标注逐模块叙事阶段，并检查是否出现阶段倒退。
7. 异议预判清单（渲染前生成）：按 `references/quality-gates.md` §4 生成 problem 级异议清单（三类各 ≥1 条）并标注核销去向。

**完成判据**：大纲表已产出（每段 `来源` 非空且可核，`self-drafted` 占比已记录）；能量一致性已标注；异议预判清单已生成（三类各 ≥1 条）。

## Phase 3: 渲染

0. **生成协议前置（任何要产出最终句子的请求，含单模块与改稿）**：读 `references/generation-protocol.md`，按其 G1 先落借句表、再渲染正文（底本 id 来源与 `self-drafted` 口径以该协议为准）；若存在匹配的叙事形状，读 `corpus/packs/_index.md` 定位后读对应形状包（如 `corpus/packs/portfolio-governance.md`）。

对所选模块：读 `references/render-rules.md` 对应节（强制检查规则）+ corpus 句法变体，G1 底本 id 取自对应骨架子索引：

| 模块 | corpus 指针 | 骨架（G1 底本 id 来源） |
|------|------------|------------------------|
| Hook | `hooks/[canonical_id].md`（配对表见 `hooks/_index.md`） | `corpus/_skeleton/hooks.md` |
| Tension | `tensions/[canonical_id].md` | `corpus/_skeleton/tensions.md` |
| Stakes | `stakes/[canonical_id].md` | `corpus/_skeleton/stakes.md` |
| Literature Turn | `literature-turns/literature-turn-templates.md` | `corpus/_skeleton/literature-turns.md` |
| Theory Lens | `theory-lens/_index.md` 定位 → `theory-lens/[id].md` | `corpus/_skeleton/theory-lens.md` |
| Preview | `previews/_index.md` 定位 → `previews/[id].md` | `corpus/_skeleton/previews.md` |
| RQ | `research-questions/[canonical_id].md`（仅需显式 RQ 时；RQ 看起来 gap-driven 则读 `references/knowledge-weaving-rq.md`） | `corpus/_skeleton/research-questions.md` |
| Contribution | `contributions/_index.md` | `corpus/_skeleton/contributions.md` |
| Transitions | `transitions/[canonical_id].md`（按需：相邻模块骨架已定、段间缺过渡信号或润色衔接时读） | `corpus/_skeleton/transitions.md` |
| Differentiation | `differentiation/01-prior-work-boundary-clarification.md`（仅存在极易混淆的 prior work 时） | `corpus/_skeleton/differentiation.md` |
| 修辞动作/语言表达升级 | `../story-blueprints/v4/rhetoric-moves/_index.md`（动作自动匹配草稿修辞功能，无需用户点名；intro 默认=bidirectional-staging；润色走其 `_polish-protocol.md` 流畅性门） | `corpus/_skeleton/phrasebank.md` + `corpus/_skeleton/micro-templates.md` |

**语料优先改编 · 角色先于风格**：语料句式为改编底本（替换来源特异性内容、填槽位；corpus 无对应句式时再自拟并保持同构），论证型模块按论证单元角色序列组装（先骨架后句子，语料顺序≠段落顺序）——纪律、拼贴判据与 intro 角色接线（render-rules §段落论证文法）见 `../story-blueprints/v4/rhetoric-moves/_argument-grammar.md` + `_polish-protocol.md` §write-*；Hook/Preview/Transitions 为 framing 豁免。已核实事实与用户裁定优先于语料句式。

槽位：槽位值未知或拿不准填什么时读 `references/introduction-slot-contracts.md`，只填已知信息，不确定的槽位保留占位；缺证据的槽位按 `generation-protocol.md` 记录为待回填。

变体选择：按适用场景/证据状态/研究情境/期刊选主推变体并写明选择理由；仅实质改变故事路径时给 1 个备选。优先级：corpus 变体级约束 > 研究情境 > 路由表推荐 > story_frame 调制。

**完成判据**：按 `references/generation-protocol.md` 的 G5 逐条为「是」；每个跳过/压缩的模块在大纲表标注 `[skipped: 理由类型]`（理由类型取大纲表枚举）。

## Phase 4: 检查与润色

1. 质量门（生成后必过）：`references/quality-gates.md`——GBL Four-Move 对齐（共享规则见 `../diagnose-introduction/references/golden-biddle-locke-four-moves.md`）+ JTBD 六模块完整性 + claim_fit（含贡献主张质量：contestability/specificity/hedge）+ 首尾句测试 + 异议预判（Gate 4）+ 段落论证文法（Gate 5：五问/拼贴）；不合格项入"提醒"段。
2. 反模式自查：`references/anti-patterns.md` §1 高频 5 项逐条扫描（§2 长尾 16 项由 `intro-review` Step 2 承接，投稿前跑一次兜底）+ 拒稿信号 `references/rejection-signals.md`。
3. 期刊适配：用户提目标期刊时读 `references/journal-fit.md`（期刊差异优先于通用规则）。
4. 措辞润色（默认执行；blocking 只出骨架时跳过）：按句位查语料库——Hook/human face → `storytelling/prose-craft-checklist.md` §0/§5；批判措辞 → `phrasebank/critique-phrases.md`；hedging → `phrasebank/hedging-strength.md`；过渡 → `transitions/` + `micro-templates/transition-signals.md`；段内/段际 key line（三分法与连接式双要素句法）→ `micro-templates/key-line-patterns.md`；中心论点定位 → `micro-templates/thesis-models.md`；五病 → `../pollock-qc/references/prose-pathology.md`；人设 → `storytelling/authorial-persona.md`；因果声明 → `../write-methods/corpus/micro-templates/causal-hedging.md`。纪律：不改骨架占位；共用纪律见 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §write-*。
5. **水位门（生成后必过，与质量门并列）**：读 `references/water-level-gate.md`（姿态 / 预算 / 元语言 / 底本覆盖率与重写门）；审查输出字段与举证要求以 `references/pass-contract.md` 为准。质量门与水位门两层都 PASS 才算通过。

6. 消耗登记（best-effort，失败不阻塞交付）：成文后调 `py ../distill-paper-exemplar/scripts/fitness_ledger.py log-consumption`（stdin JSON：`{"skill": "write-introduction", "section": "introduction", "project": "<项目>", "corpus_files": ["<实际读过的 corpus 文件>"], "variants": ["<!-- wb:citekey:item -->"], "blueprint_cards": ["<实际采用的蓝图卡 id>"], "note": ""}`）——fitness 台账策展数据面（检索命中率、从未被检索变体），漏登可接受，不重登。

**完成判据**：质量门（`references/quality-gates.md`）全过；水位门按 `references/pass-contract.md` 产出且满足其完成判据；底本覆盖率已计算并触发重写/修补分支；无未修复的 🔴/🟡 标记。

## 输出合同

按 `references/output-format.md`：Gap×维度标题 → 大纲表 → 借句表 → 前三段合同表 → 动态段落骨架 → 提醒 → 证据置信度（EMERGING 标注单/双源）→ GBL 对齐表 → **paper-state.yaml 片段**（schema 见 `references/paper-state-schema.md`；用户未提及协议时注释头含使用说明）。完整请求在此之前附 `## 本次可学习的顶刊对象`：至多一篇主学习对象与一篇对照对象；每篇仅列匹配、可学习动作、不可照搬条件与比较问题。

快速模式：只请求单模块 → 输出该模块句法骨架 + 槽位提示 + 1 个反模式提醒。

## 纪律

- 原文锚定与润色纪律：见 `../story-blueprints/v4/rhetoric-moves/_polish-protocol.md` §write-* 共用纪律。
- 批评登记（现状如实陈述）：本 skill 的语料精炼通道（`corpus/_evidence_registry.yaml` 的 `critique.per_file`）当前为零数据（该键为 null）；可执行规则通道在 skills 树内不存在。唯一可行的登记路径是 `corpus/_skill_design_feedback.yaml`——每条 defect 以 `channel` 字段路由到目标文件：`corpus_variant`（目标是一张语料卡缺变体/模板）、`rule`（目标是某个 reference 文件里的规则句）、`obsolete`（所指规则已不存在或被取代）。不再宣称不存在的通道。
- 提升路径（promotion）：同一 defect 在 ≥2 篇论文复现且带 regression_case 时，提升为对应 reference 文件里的规则句（不新建文件），并回写 `rule_locator` 与 `status: VERIFIED`；单篇未复现者留在 `_skill_design_feedback.yaml` 账本并记录其 `channel`。
- 注册表缺失时回退 `_routing_tables.yaml` 静态推荐，不中断输出；但**必须在输出末尾附加降级声明**："⚠ registry 缺失，语料验证状态（EMERGING/VERIFIED/ROBUST）未经核验，本次按静态路由表推荐"——回退时显式声明。
