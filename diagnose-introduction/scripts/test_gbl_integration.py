#!/usr/bin/env python3
"""Deterministic checks for the GBL Introduction integration."""

import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = SKILL_ROOT.parent


def read(relative: str) -> str:
    return (PACKAGE_ROOT / relative).read_text(encoding="utf-8")


def require(name: str, condition: bool) -> None:
    if not condition:
        raise AssertionError(name)
    print(f"PASS: {name}")


def main() -> int:
    diagnose = read("diagnose-introduction/SKILL.md")
    introduction = read("write-introduction/SKILL.md")
    front_end = read("write-introduction/references/front-end-mode.md")
    complete_example = read("diagnose-introduction/references/complete-example.md")
    reference = read(
        "diagnose-introduction/references/golden-biddle-locke-four-moves.md"
    )

    require("diagnosis emits machine-readable Four-Move status", "gbl_four_moves:" in diagnose)
    require(
        "diagnostic interface is versioned",
        "diagnostic_schema_version: 2" in diagnose
        and "diagnostic_schema_version: 2" in complete_example,
    )
    require(
        "writer consumes the shared Four-Move reference",
        "../diagnose-introduction/references/golden-biddle-locke-four-moves.md"
        in introduction,
    )
    require(
        "writer keeps the existing public modes",
        "--mode=introduction|front-end|align" in introduction,
    )
    require(
        "front-end and align modes expose Four-Move output",
        "## GBL Four-Move Alignment" in front_end
        and "aligned / partial / incomplete" in front_end,
    )
    require(
        "canonical Gap taxonomy is reused",
        all(
            value in reference
            for value in ("Incompleteness", "Inadequacy", "Incommensurability")
        ),
    )
    require(
        "coherence and problematization remain independent",
        "Do not infer `gap_type` from `conversation_strategy`" in reference,
    )
    require(
        "GBL does not expand the paper-state schema",
        "Do not add GBL-specific fields to canonical `story`" in reference,
    )
    require(
        "Four Moves are not fixed paragraph slots",
        "Do not require one paragraph per move" in reference,
    )
    require(
        "missing moves are not confused with generation blocking",
        "`incomplete`: at least one move is missing" in reference
        and "aligned | partial | blocked" not in reference,
    )
    require(
        "quantitative and qualitative boundaries remain distinct",
        "Do not force field-story language onto quantitative papers" in reference
        and "For qualitative/process studies" in reference,
    )
    require(
        "unstable evidence requires placeholders rather than invented findings",
        "[headline finding pending]" in front_end
        and "without inventing a finding" in front_end,
    )

    playbook = read(
        "diagnose-introduction/references/intertextual-construction-playbook.md"
    )
    lit_index = read(
        "write-introduction/academic-writing-corpus/literature-turns/_index.md"
    )
    tension = read(
        "write-introduction/academic-writing-corpus/storytelling/"
        "tension-escalation-protocol.md"
    )

    require(
        "playbook covers all three coherence construction mechanisms",
        all(
            marker in playbook
            for marker in ("交点重写", "过滤式推进", "对垒阵营")
        ),
    )
    require(
        "playbook provides the nine-combination design space",
        "3×3" in playbook
        and "默认对角线" in playbook
        and "合法非对角组合" in playbook
        and "可疑组合" in playbook,
    )
    require(
        "playbook keeps the independence rule",
        "不得由 `gap_type` 推出 `conversation_strategy`" in playbook,
    )
    require(
        "straw-man passing condition is operationalized",
        "Outer Limits" in reference
        and "Representativeness" in reference
        and "Attributability" in reference
        and "Full-strength construction first" in reference,
    )
    require(
        "literature-turns index no longer asserts one-to-one pairing",
        "不存在一一对应" in lit_index
        and "默认对角线" in lit_index
        and "intertextual-construction-playbook.md" in lit_index,
    )
    require(
        "tension-escalation records the dual-axis discipline",
        "conversation_strategy" in tension
        and "intertextual-construction-playbook.md" in tension,
    )
    require(
        "diagnose skill wires the playbook on demand",
        "intertextual-construction-playbook.md" in diagnose,
    )
    require(
        "writer routes off-diagonal combinations through the playbook",
        "intertextual-construction-playbook.md" in introduction,
    )

    rr = read("revision-coach/references/gbl-r-and-r-dynamics.md")
    coach = read("revision-coach/SKILL.md")
    preview = read("paper-review/SKILL.md")

    require(
        "R&R reference covers the three gatekeeper dynamics",
        all(
            marker in rr
            for marker in ("Field story 吸引", "Multivocality 收窄", "Storyline 重写")
        ),
    )
    require(
        "R&R reference encodes accept/resist decision rules",
        all(
            marker in rr
            for marker in ("默认接受", "误读即清晰度信号", "抵抗的唯一正当理由", "修订丢失检查")
        ),
    )
    require(
        "R&R reference anchors verbatim response patterns by function",
        all(
            marker in rr
            for marker in ("接受 + 具体化", "重定向", "相关性边界", "设计边界", "空间边界")
        ),
    )
    require(
        "R&R reference keeps author-decides discipline",
        "决定权在作者" in rr and "是范文不是模板" in rr,
    )
    require(
        "revision-coach wires the R&R reference for both modes",
        "gbl-r-and-r-dynamics.md" in coach
        and "storyline-level comments" in coach,
    )
    require(
        "paper-review predicts reviewer reception via GBL Ch5",
        "审稿人接受度预测" in preview
        and "Multivocality 风险" in preview
        and "gbl-r-and-r-dynamics.md" in preview,
    )
    require(
        "paper-review routes decision letters to revision-coach",
        "已收到决定信/审稿意见" in preview and "/revision-coach" in preview,
    )
    require(
        "revision-coach anchors storyline decisions in the story contract",
        "story contract 锚点" in coach and "/paper-story-contract" in coach,
    )
    require(
        "revision-coach hands off roadmap rows as work orders",
        "工单" in coach,
    )

    twin = read(
        "write-introduction/academic-writing-corpus/hooks/22-twin-complication.md"
    )
    hooks_index = read(
        "write-introduction/academic-writing-corpus/hooks/_index.md"
    )
    registry = read(
        "write-introduction/academic-writing-corpus/_evidence_registry.yaml"
    )

    require(
        "twin-complication hook encodes the twin-tension architecture",
        all(
            marker in twin
            for marker in (
                "田野张力",
                "理论张力",
                "story the theory",
                "complicating the complications",
                "turner1976",
            )
        ),
    )
    require(
        "twin-complication hook enforces the twin-resolution contract",
        "双重 Resolution 纪律" in twin
        and "删除检验" in twin
        and "双 resolution 合同" in twin,
    )
    require(
        "twin-complication hook marks the field-vs-theory ordering difference",
        "从田野张力派生" in twin and "关键顺序差异" in twin,
    )
    require(
        "hooks index wires the twin-complication hook",
        "22-twin-complication" in hooks_index
        and "双重张力交织 Hook" in hooks_index
        and "双 resolution 合同" in hooks_index,
    )
    require(
        "hooks index records mutual exclusions for twin-complication",
        "`22-twin-complication` + `06-paradigm-challenge`" in hooks_index
        and "`22-twin-complication` + `03-data-shock`" in hooks_index,
    )
    require(
        "evidence registry tracks the twin-complication hook",
        "22-twin-complication:" in registry and "turner1976 (ASQ)" in registry,
    )
    require(
        "playbook points Move 1x3 interweaving to the twin-complication hook",
        "hooks/22-twin-complication.md" in playbook
        and "双重张力" in playbook,
    )
    require(
        "tension-escalation notes Haunschild as implicit twin-complication",
        "22-twin-complication.md" in tension
        and "双重张力交织" in tension,
    )

    soundness = read(
        "write-theory/corpus/subprotocols/reasoning_soundness_protocol.md"
    )
    phase3 = read("write-theory/references/phase-3-hypothesis-derivation.md")
    phase4 = read("write-theory/references/phase-4-qc-alignment.md")
    theory_index = read("write-theory/corpus/_index.md")
    theory_review = read("theory-review/SKILL.md")

    require(
        "soundness protocol encodes premise typing and weakest-link marking",
        all(
            marker in soundness
            for marker in (
                "Definitional",
                "Stipulation",
                "Empirical",
                "链条强度 = 最弱前提",
                "[D]/[S]/[E]",
            )
        ),
    )
    require(
        "soundness protocol encodes the necessity gate and stress test",
        all(
            marker in soundness
            for marker in (
                "替代充分性",
                "可区分性",
                "反事实塌陷",
                "什么条件下这一步不成立",
                "Soundness Card",
            )
        ),
    )
    require(
        "soundness protocol mirrors the Outer Limits honesty discipline",
        "Outer Limits" in soundness
        and "golden-biddle-locke-four-moves.md" in soundness,
    )
    require(
        "phase-3 wires the soundness protocol into derivation QC",
        "reasoning_soundness_protocol.md" in phase3
        and "前提最弱点" in phase3
        and "机制必要性门控" in phase3
        and "反例压力测试" in phase3,
    )
    require(
        "phase-4 adds the Soundness audit as a fourth audit",
        "审计 4: Soundness" in phase4
        and "四层审计" in phase4
        and "reasoning_soundness_protocol.md" in phase4,
    )
    require(
        "write-theory corpus index registers the soundness protocol",
        "reasoning_soundness_protocol.md" in theory_index
        and "soundness" in theory_index,
    )
    require(
        "theory-review audits soundness symmetrically with generation",
        "Step 2.6: Soundness 审查" in theory_review
        and "前提最弱点" in theory_review
        and "机制必要性" in theory_review
        and "反例未防守" in theory_review
        and "reasoning_soundness_protocol.md" in theory_review,
    )

    keyline = read(
        "write-introduction/academic-writing-corpus/micro-templates/"
        "key-line-patterns.md"
    )
    prose = read(
        "write-introduction/academic-writing-corpus/storytelling/"
        "prose-craft-checklist.md"
    )
    transitions_index = read(
        "write-introduction/academic-writing-corpus/transitions/_index.md"
    )

    require(
        "key-line patterns encode the three-type unified vocabulary",
        all(
            marker in keyline
            for marker in ("总起式", "连接式", "总结式", "诊断分流")
        ),
    )
    require(
        "key-line patterns dissect the dual-element connecting syntax",
        all(
            marker in keyline
            for marker in ("承上", "启下", "转折式", "递进式", "因果式", "并列式")
        )
        and "Provan & Milward" in keyline
        and "Yang & Pandey" in keyline,
    )
    require(
        "key-line patterns provide wrap corpus and the bookend variant",
        "前后夹击" in keyline
        and "Pitts & Fernandes" in keyline
        and "abrupt stop" in keyline,
    )
    require(
        "key-line patterns separate clarity from soundness and mark provenance",
        "reasoning_soundness_protocol.md" in keyline
        and "EMERGING" in keyline
        and "虚假路标" in keyline
        and "唐僧式重复" in keyline,
    )
    require(
        "prose-craft points topic-sentence and coherence sections to key-line",
        prose.count("key-line-patterns.md") >= 2,
    )
    require(
        "phase-3 wrap check points to the wrap corpus",
        "key-line-patterns.md" in phase3,
    )
    require(
        "transitions index states the module-vs-sentence division of labor",
        "key-line-patterns.md" in transitions_index
        and "模块级" in transitions_index,
    )

    ack = read("write-theory/corpus/sentences/acknowledgment_response.md")

    require(
        "soundness protocol integrates the Booth warrant five tests",
        all(
            marker in soundness
            for marker in (
                "sufficiently limited",
                "competing warrants",
                "appropriate to this field",
                "cover the reason and claim",
                "warrant 五测试",
            )
        ),
    )
    require(
        "soundness protocol encodes the When-X-then-Y canonical form",
        "When X, then Y" in soundness and "good instance" in soundness,
    )
    require(
        "soundness protocol adds the six warrant types as attack surface",
        all(
            marker in soundness
            for marker in (
                "Based on Experience",
                "Based on Authority",
                "Systems of Knowledge",
                "Cultural Warrants",
                "Methodological Warrants",
                "Articles of Faith",
            )
        ),
    )
    require(
        "soundness protocol adds acknowledge-without-response disposition",
        "承认但不回应" in soundness
        and "acknowledge without response" in soundness
        and "Goldilocks" in soundness,
    )
    require(
        "soundness protocol encodes warrant stating discipline and hard-evidence rule",
        "明言与隐去" in soundness
        and "跨领域读者" in soundness
        and "claim of fact" in soundness
        and "硬证据规则" in soundness
        and "What you don't say says who you are" in soundness,
    )
    require(
        "acknowledgment-response corpus covers the four objection types",
        all(
            marker in ack
            for marker in ("替代解释", "反例", "证据局限", "定义分歧")
        )
        and "Webster" in ack,
    )
    require(
        "acknowledgment-response corpus encodes weight-ordered marker vocabularies",
        all(
            marker in ack
            for marker in ("Granted", "To be sure", "does not bear on", "对事不对人")
        )
        or "direct it at the work rather than the person" in ack,
    )
    require(
        "acknowledgment-response corpus keeps ethos and anti-pattern discipline",
        "稻草人式承认" in ack and "词典定义" in ack,
    )
    require(
        "phase-3 and phase-4 wire the warrant layer into QC",
        "Warrant 表达" in phase3
        and "承认但不回应" in phase3
        and "warrant 五测试" in phase4
        and "明言/隐去纪律" in phase4
        and "硬证据规则" in phase4,
    )
    require(
        "theory-review audits warrant expression symmetrically",
        "Warrant 表达" in theory_review
        and "warrant 五测试" in theory_review
        and "居高临下" in theory_review,
    )
    require(
        "write-theory corpus index registers the acknowledgment-response corpus",
        "acknowledgment_response.md" in theory_index
        and "warrant 五测试" in theory_index,
    )

    require(
        "prose-craft adds the absolute-word blacklist and hedge bank",
        all(
            marker in prose
            for marker in ("Overclaiming", "no one", "wish to suggest", "In our opinion", "timid")
        ),
    )
    require(
        "prose-craft encodes limiting-condition patterns",
        "assuming today's conservation measures" in prose
        and "Based on available economic data" in prose,
    )
    require(
        "phase-4 audits hypothesis contestability and links the blacklist",
        "Contestability" in phase4
        and "反命题" in phase4
        and "prose-craft-checklist.md` §5.6" in phase4,
    )
    require(
        "theory-review audits hypothesis contestability",
        "Contestability" in theory_review and "反命题" in theory_review,
    )
    require(
        "prose-craft encodes the character-action diagnosis",
        "Character-Action" in prose
        and "6–7 词" in prose
        and "Locke frequently repeated himself" in prose,
    )
    require(
        "prose-craft encodes nominalization repair and old-before-new priority",
        "If X, then Y" in prose
        and "Old-before-New" in prose
        and "always choose the principle of old before new" in prose,
    )
    require(
        "prose-craft encodes the passive-voice exemption nuance",
        "被动语态豁免" in prose
        and "Eye movements were measured" in prose
        and "We conclude" in prose,
    )
    require(
        "cross-skill references cover the new Williams section",
        "§0–§6" in prose,
    )

    evidence_std = read("write-results/references/evidence-standards.md")
    visual = read("write-results/references/visual-evidence.md")
    results_skill = read("write-results/SKILL.md")
    slot_r4 = read("write-results/references/slot-R4.md")
    slot_r7 = read("write-results/references/slot-R7.md")
    elevated = read("write-discussion/references/limitations-elevated-plane.md")
    discussion_review = read("discussion-review/SKILL.md")
    stakes_index = read(
        "write-introduction/academic-writing-corpus/stakes/_index.md"
    )

    require(
        "evidence-standards encodes the Booth five evidence questions",
        all(
            marker in evidence_std
            for marker in (
                "appropriately precise",
                "Sufficient and representative",
                "Authoritative",
                "Clear and understandable",
                "audience does",
            )
        ),
    )
    require(
        "evidence-standards maps standards to quantitative reporting",
        "cherry-picking" in evidence_std
        and "诚实边界" in evidence_std
        and "非显著" in evidence_std
        and "EMERGING" in evidence_std,
    )
    require(
        "write-results SKILL wires both new references",
        "evidence-standards.md" in results_skill
        and "visual-evidence.md" in results_skill,
    )
    require(
        "visual-evidence encodes the table-vs-figure decision rule",
        "achieves the effect you want" in visual
        and "discrete numbers" in visual
        and "continuous change over time" in visual,
    )
    require(
        "visual-evidence encodes the title/legend discipline",
        "Heads of households" in visual and "flush left" in visual,
    )
    require(
        "visual-evidence encodes the four ethics rules",
        "manipulate a scale" in visual
        and "misleadingly simple" in visual
        and "state it" in visual,
    )
    require(
        "slot-R4 and slot-R7 wire the visual-evidence reference",
        "visual-evidence.md" in slot_r4 and "visual-evidence.md" in slot_r7,
    )
    require(
        "elevated-plane adds the Booth conclusion reverse three moves",
        "reverse order" in elevated
        and "more fully" in elevated
        and "keep the conversation alive" in elevated,
    )
    require(
        "discussion-review audits the reverse three moves symmetrically",
        "反向三步" in discussion_review
        and "新** significance" in discussion_review
        and "limitations-elevated-plane.md" in discussion_review,
    )
    require(
        "stakes index adds the cost-vs-benefit allocation rule",
        "motivated by a real cost" in stakes_index
        and "intensify your solution" in stakes_index
        and "So-what 测试" in stakes_index,
    )
    require(
        "soundness protocol has the voice firewall against defensive prose",
        "声音防火墙" in soundness
        and "诊断层" in soundness
        and "回答想象中的审稿人" in soundness,
    )
    require(
        "generation and review sides both check defensive technical prose",
        "防御性技术说明文风" in phase3
        and "频次预算" in ack
        and "声音防火墙" in theory_review,
    )
    require(
        "prose-craft adds the defensive-prose section with necessity calibration",
        "Defensive prose" in prose
        and "keep the substance, delete the posture" in prose
        and "unnecessary disclaimer" in prose
        and "EMERGING" in prose,
    )
    require(
        "prose-craft encodes negative-to-positive conversion and hedge de-stacking",
        "not X but Y" in prose
        and "The analysis focuses on" in prose
        and "could potentially influence" in prose,
    )
    require(
        "soundness firewall and phase-3 route defensive wording to prose-craft 5.7",
        "§5.7" in soundness and "§5.7" in phase3,
    )

    pb_methods = read(
        "write-introduction/academic-writing-corpus/phrasebank/methods-process.md"
    )
    pb_quant = read(
        "write-introduction/academic-writing-corpus/phrasebank/quantities-trends.md"
    )
    methods_skill = read("write-methods/SKILL.md")
    event_study = read("write-results/econometric-models/事件研究法.md")

    require(
        "phrasebank files carry the auxiliary-tier metadata",
        "source_tier: auxiliary" in pb_methods
        and "top_journal_validated: false" in pb_methods
        and "source_tier: auxiliary" in pb_quant
        and "top_journal_validated: false" in pb_quant,
    )
    require(
        "phrasebank files encode the usage rules and specificity gate",
        "Specificity gate" in pb_methods
        and "Specificity gate" in pb_quant
        and "退役规则" in pb_methods
        and "退役规则" in pb_quant,
    )
    require(
        "methods-process covers the process-grammar toolbox",
        "Prior to" in pb_methods
        and "infinitive of purpose" in pb_methods.lower()
        and "using + instrument" in pb_methods,
    )
    require(
        "quantities-trends covers quantities, approximators, and trends",
        "Just over" in pb_quant
        and "ranged from" in pb_quant
        and "peaked" in pb_quant,
    )
    require(
        "quantities-trends bans redundant approximator-precision mixing",
        "不得与精确数字同句并存" in pb_quant,
    )
    require(
        "three consumer skills wire the phrasebank as auxiliary layer",
        "phrasebank/methods-process.md" in methods_skill
        and "phrasebank/quantities-trends.md" in results_skill
        and "quantities-trends.md" in event_study,
    )


    # --- Greene & Lidinsky 2017 (From Inquiry to Academic Writing) wave ---
    thesis_models = read(
        "write-introduction/academic-writing-corpus/micro-templates/thesis-models.md"
    )
    gap_diag = read("research-gap-diagnosis/SKILL.md")
    lit_turns_index = read(
        "write-introduction/academic-writing-corpus/literature-turns/_index.md"
    )
    rebuttal = read("revision-coach/references/rebuttal-audit-protocol.md")
    pollock_qc = read("pollock-qc/SKILL.md")
    align_checks = read("write-discussion/references/alignment-checks.md")

    require(
        "thesis-models encodes all four G&L working-thesis models",
        all(
            marker in thesis_models
            for marker in ("纠错型", "补缺型", "修正型", "假设检验型", "表象—实质")
        ),
    )
    require(
        "thesis-models encodes the Although-subordination power allocation",
        "Although" in thesis_models
        and "从属" in thesis_models
        and "句法权力分配" in thesis_models,
    )
    require(
        "thesis-models is marked auxiliary and wired into write-introduction",
        "source_tier: auxiliary" in thesis_models
        and "micro-templates/thesis-models.md" in introduction,
    )
    require(
        "research-gap-diagnosis adds the Part IV synthesis chain",
        all(
            marker in gap_diag
            for marker in (
                "Part IV",
                "Why-they-differ",
                "What-if-neither",
                "Neither X nor Y",
            )
        ),
    )
    require(
        "research-gap-diagnosis adds the either-or pseudo-binary probe and generation mode",
        "Either-Or 伪二元探针" in gap_diag and "generation mode" in gap_diag,
    )
    require(
        "literature-turns index wires the upstream synthesis interface",
        "synthesis 操作链" in lit_turns_index
        and "关系陈述" in lit_turns_index,
    )
    require(
        "acknowledgment-response corpus adds the Rogerian four-step sequence",
        all(
            marker in ack
            for marker in ("Rogerian 四步", "共同地基", "共创方案", "deliberative democracy")
        ),
    )
    require(
        "acknowledgment-response frequency budget moved to the renumbered section",
        "## 6. 定量实证适配与分工" in ack
        and "acknowledgment_response.md` §6" in soundness,
    )
    require(
        "revision-coach audits the Rogerian de-escalation sequence",
        "Rogerian" in rebuttal and "降防御序列" in rebuttal,
    )
    require(
        "soundness protocol adds the management-translated fallacy probes",
        all(
            marker in soundness
            for marker in (
                "谬误探针",
                "False analogy",
                "Fallacy of division",
                "Either-or",
                "扫描镜头",
            )
        ),
    )
    require(
        "theory-review points to the fallacy probes",
        "谬误探针" in theory_review,
    )
    require(
        "pollock-qc adds the cited-evidence four-criteria audit",
        "Cited-evidence audit" in pollock_qc
        and "source's sources" in pollock_qc
        and "evidence-standards.md" in pollock_qc,
    )
    require(
        "prose-craft bans emotional rhetoric per the pathos tone discipline",
        "情绪化修辞禁令" in prose and "sarcasm" in prose and "loaded" in prose,
    )
    require(
        "write-discussion bans neutral comparisons",
        "Neutral comparison ban" in align_checks
        and "评价性" in align_checks,
    )

    # --- 2026-07-28 regression-audit invariants ---
    amr_mode = read("write-introduction/references/theory-paper-amr-mode.md")

    require(
        "theory-review counts five soundness checks and includes the fallacy row",
        "审查五项" in theory_review and "谬误探针" in theory_review,
    )
    require(
        "research-gap Part IV closes the loop with a post-generation audit",
        "Post-Generation Audit" in gap_diag and "pseudo-genre alert" in gap_diag,
    )
    require(
        "acknowledgment corpus bridges Booth priorities to soundness dispositions",
        "先排序，后处置" in ack,
    )
    require(
        "soundness protocol disambiguates the acknowledge-without-response pointer",
        "三姿态句式见该文件 §2.3" in soundness
        and "独立于上述句子级 0–2 预算" in soundness,
    )
    require(
        "AMR mode no longer references the deleted combination-templates file",
        "combination-templates" not in amr_mode,
    )
    require(
        "write-introduction scopes contribution listing to empirical papers",
        "theory_paper: true" in introduction
        and "references/theory-paper-amr-mode.md" in introduction,
    )

    # --- 2026-07-28 write-theory restoration invariants ---
    theory_skill = read("write-theory/SKILL.md")
    theory_output = read("write-theory/references/output-format.md")

    require(
        "write-theory restores the output-format template and wires it",
        "架构决策" in theory_output
        and "叙事弧线指南" in theory_output
        and "references/output-format.md" in theory_skill,
    )
    require(
        "write-theory restores the hard-constraints quick reference with corpus pointers",
        "Hard constraints" in theory_skill
        and "非传统收敛" in theory_skill
        and "bilateral_argumentation_templates.md" in theory_skill
        and "dialectical" in theory_skill,
    )
    require(
        "write-theory restores the downstream interface map",
        "Downstream interfaces" in theory_skill
        and "distill-theory-exemplar" in theory_skill,
    )

    runtime_names = (
        "diagnose-introduction",
        "paper-story-contract",
        "write-introduction",
    )
    alternation = "|".join(map(re.escape, runtime_names))
    claude_source_call = re.compile(rf"(?<![\w$/\\])\$(?:{alternation})\b")
    codex_source_call = re.compile(rf"(?<![\w$./\\])/(?:{alternation})\b")
    has_claude_calls = bool(codex_source_call.search(diagnose)) and bool(
        codex_source_call.search(introduction)
    )
    has_codex_calls = bool(claude_source_call.search(diagnose)) and bool(
        claude_source_call.search(introduction)
    )
    require(
        "runtime invocation style is internally consistent",
        has_claude_calls != has_codex_calls,
    )
    if has_claude_calls:
        require(
            "Claude canonical uses slash-style skill calls",
            not claude_source_call.search(diagnose)
            and not claude_source_call.search(introduction)
            and has_claude_calls,
        )
    else:
        require(
            "Codex mirror uses dollar-style skill calls",
            not codex_source_call.search(diagnose)
            and not codex_source_call.search(introduction)
            and has_codex_calls,
        )
    print("PASS: all GBL Introduction integration tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
