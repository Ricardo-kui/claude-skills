---
name: distill-story-exemplar
description: "Distill a published paper as an integrated academic story into the story-blueprints learning corpus. Use when studying how a whole exemplar tells its story or comparing whole-paper narratives. Not for drafting."
when_to_use: "整篇故事层学习卡；在四节蒸馏完成后，或用户要研究整篇叙事结构时使用。"
whenToUse: "Use when 用户要把一篇已发表论文作为完整学术故事来学习，重建其问题、构念、证据与结局并生成 story-blueprints 学习卡。Trigger words: 蒸馏整篇故事, story blueprint, 学习这篇论文的叙事, 整篇故事学习卡, 论文故事蒸馏"
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

Prefer the complete paper plus any verified section distillations. **When the paper comes from the PDM pipeline, read the materialized slices, not the merged fulltext** — slice paths are in the PDM `source_provenance.section_slices`. Read in attention order: `sections/introduction.md` + `sections/theory.md` first (the primary story-reading object), then `sections/results.md` + `sections/discussion.md` for the payoff checks, and `sections/methods.md` only for the story-alignment audit. `fulltext.text-only.md` re-carries the reference list and front matter (no story signal) — read it only as fallback when a slice is missing or marked `unknown`. The raw paper-import MD carries base64 images (up to ~90% of bytes) and must never enter context. Read `references/vault-retrieval-protocol.md` for the Vault retrieval route when a Vault source is supplied. If only partial text is available, record `coverage: partial` and do not make the card eligible for recommendations in unobserved sections.

## Workflow

1. **Register scope.** Record paper identity, publication status, paper type, source version, sections read, and why this paper enters the learning corpus. Do not guess missing metadata.
2. **Descriptive reading.** Start with the Introduction and Theory slices, then read the Results, Discussion, and Methods slices as payoff and alignment checks. Write the theme question, a continuous whole-story synopsis, main/supporting characters with role reasons, storylines, five acts, and—only when useful—the source and construction of tension. Do not score quality at this point.
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

## Context discipline

Read the two primary slices (introduction + theory) first and complete the descriptive reading on them before opening the later slices. Do not read the merged `fulltext.text-only.md` when the slices exist — its reference list and front matter carry no story signal and were the largest single token cost of L3. Never read the raw paper-import MD (base64 images up to ~90% of bytes).
