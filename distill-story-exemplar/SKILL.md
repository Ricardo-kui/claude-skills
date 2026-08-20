---
name: distill-story-exemplar
description: "把整篇已发表论文作为一个完整学术故事蒸馏成 story-blueprints 学习卡——重构主题、角色、故事线与五幕结构，提取可迁移的结构手法。当用户要求学习某篇范文如何讲故事、比较整篇叙事、或生成学习卡时使用。"
whenToUse: "当用户要求从整篇范文学习叙事结构、对比两篇论文的整篇故事、或向 story-blueprints 语料库新增学习卡时使用。触发词：故事蒸馏、story blueprint、学习卡、这篇论文的故事怎么讲、整篇叙事分析、对比两篇论文的故事、生成 blueprint 卡"
---

# Distill Story Exemplar

Create learning assets for reading excellent (and imperfect) academic papers as whole research stories. The goal is to build structural sensitivity: understand how a paper's real question, constructs, design, evidence, and ending form one story.

## Modes and authority

- **v0.4-lite (default for new work):** Write a new card under `../story-blueprints/v4/blueprints/` using `protocols/blueprint_v4_lite_template.md`.
- **v0.3 compatibility:** Read or repair an existing legacy blueprint only when the user explicitly requests it. Do not relabel the existing 59 cards or infer that `ROBUST` means narratively exemplary.
- `../story-blueprints/references/v4-schema.md` is the v0.4-lite schema authority. Read `story-assessment-rubric.md` only after completing the descriptive reading. Read `learning-affordance-protocol.md` only when extracting learning moves.

## Non-negotiable boundaries

- Reconstruct the paper's actual story before judging whether it works.
- Treat the story reading as an interpretation of the whole paper, not as a collection of paragraph-level facts. Record reading scope and mark counterfactual readings as analyst-generated.
- Do not treat a top-journal publication as proof that the paper's story is exemplary.
- Do not turn a paper's story into a template for the user's project. A learning move must state both its transfer conditions and what cannot be copied.
- Do not create a project learning package or write to a project file. Cards are reusable corpus assets only.

## Default attention allocation

Whole-paper coverage does **not** mean equal analytical attention. For a conventional empirical management paper, use this default allocation unless the paper's own architecture gives a reason to depart from it:

| Section | Default attention | Story question |
|---|---:|---|
| Introduction | 40% | What theme, knot, characters, and promise does the paper give the reader? |
| Theory | 25% | How do the constructs and mechanisms make the promised plot emerge? |
| Results | 15% | Where is the promised answer revealed, and does the evidence stage it clearly? |
| Discussion | 15% | Does the ending return to and transform the opening question? |
| Methods | 5% | Does the design make the promised evidence possible? |

The first two sections are the primary story-reading object; Results and Discussion test whether the promise is paid off; Methods is a story-alignment audit, not a second technical-methods distillation. Read all observed sections before declaring complete coverage, but do not force equal-length notes. Record any material departure from this profile in the card's `analysis_focus` field.

## Inputs

Prefer the complete paper plus any verified section distillations. **When the paper comes from the PDM pipeline, read only `<citekey>.pdm/fulltext.text-only.md`** — the raw paper-import MD carries base64 images (up to ~90% of bytes) and must never enter context. Read `references/vault-retrieval-protocol.md` for the Vault retrieval route when a Vault source is supplied. If only partial text is available, record `coverage: partial` and do not make the card eligible for recommendations in unobserved sections.

## Workflow

1. **Register scope.** Record paper identity, publication status, paper type, source version, sections read, and why this paper enters the learning corpus. Do not guess missing metadata.
2. **Descriptive reading.** Start with Introduction and Theory, then read Results, Discussion, and Methods as payoff and alignment checks. Write the theme question, a continuous whole-story synopsis, main/supporting characters with role reasons, storylines, five acts, and—only when useful—the source and construction of tension. Do not score quality at this point.
3. **Section learning check.** For each section actually read, decide `yes`, `partial`, or `no` as a learning object. State one or two learnable structural moves and at least one caveat. A paper may be useful for Results but not for Introduction.
4. **Assessment.** Apply the rubric only to distinguish effective, partial, cautionary, and descriptive learning roles. Assess storytelling only; do not infer research quality, causal credibility, or journal value from the story assessment.
5. **Comparison.** Add an alternative reading only when it is documented in the literature, signaled by the authors, or clearly labelled as an analyst counterfactual. Add a cross-paper comparison only when it gives a concrete reading question.
6. **Write and validate.** Show the completed card to the user before writeback unless the user explicitly authorizes batch work. Run `python ../story-blueprints/scripts/validate_blueprints_v4.py` and `python ../story-blueprints/scripts/build_catalog_v4.py` after each approved write.

## Output

Return the v0.4-lite learning card, a short distinction between descriptive reading and assessment, and the section-specific learning moves. Do not generate the user's manuscript prose.

## References

- Schema and card fields: `../story-blueprints/references/v4-schema.md`
- Assessment terms: `../story-blueprints/references/story-assessment-rubric.md`
- Learning-move extraction: `../story-blueprints/references/learning-affordance-protocol.md`
- Dynamic writer integration: `../story-blueprints/references/retrieval-contract.md`
