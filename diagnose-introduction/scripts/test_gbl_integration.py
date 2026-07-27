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
