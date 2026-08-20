---
name: reverse-validation-pipeline
description: "运行本地反向验证工具，检验 write-methods/write-results 语料能否反向复现蒸馏出的范文（M1-M10/R1-R9 槽位覆盖、模板选择、跨技能一致性）。Use after distill-* 产出 JSON 后。"
when_to_use: "触发词：反向验证、校验语料覆盖、coverage gap report。蒸馏用 distill-*，改语料先看 Gap 报告。"
whenToUse: "Use when running reverse validation to check whether write-methods or write-results corpora can regenerate distilled exemplar slot maps and produce a coverage gap report. Trigger words: 反向验证, reverse validation, 语料覆盖检查, 跑反向验证管线, coverage gap report, distilled JSON 校验"
---

# Reverse Validation Pipeline

Run the local `reverse_validation_pipeline` CLI to check whether the `write-methods` / `write-results` corpora can **reverse-generate** distilled top-journal exemplars. This is the QC loop opposite to the distill-* skills: distillation asks "what's in the exemplar", reverse validation asks "can our corpus write it out".

## When To Use

Use when the user has (or wants) distilled `*_methods_distilled.json` + `*_results_distilled.json` pairs and wants to verify corpus coverage, or explicitly asks for reverse validation.

Not for:
- distilling exemplars (→ `distill-methods-exemplar` / `distill-results-exemplar`)
- writing or reviewing Methods/Results prose (→ `write-methods` / `write-results` / `methods-review` / `results-review`)
- editing the corpora directly — run the report first, then fix the files it flags

## Entry Point

```bash
python ~/.claude/skills/reverse_validation_pipeline/reverse_validation_pipeline.py \
  --methods-json <methods_distilled.json> \
  --results-json <results_distilled.json> \
  --output-dir ./validation_output
```

Batch (all pairs in a directory):

```bash
python ~/.claude/skills/reverse_validation_pipeline/reverse_validation_pipeline.py \
  --batch-dir ./distilled_jsons \
  --output-dir ./validation_output
```

Exit code 0 = no critical gap; 1 = at least one critical gap (CI-gate friendly).

## Input Contract

Two JSON files, top-level `paper_id` / `phase_0` / `phase_1_slot_map`:

- **methods**: `phase_0.design_type`（自动推断亦可）+ `phase_1_slot_map.M3`（DV）/`M4`（IV/predictors）/`M5`（moderators/mediators）/`M9`（multi-study）…
- **results**: `phase_0.hypothesis_structure` + `phase_1_slot_map.R3`（hypotheses_covered / nonsignificant_hypotheses）…

Full schema + `design_type_map.json` mapping: see `README.md`.

## Output Contract

Per-paper validation report(s) in `--output-dir` (slot coverage, template selection, gap analysis, cross-skill consistency, integrated `methods_results_quality_check` severity), plus a batch summary for `--batch-dir` runs.

## Workflow

1. **Locate inputs**: find the distilled JSON pair (check the distill-* run's output dir; if none exists, route to distillation first).
2. **Normalize if needed**: if keys drifted (`M1 变量测量` vs `M1`), run `normalize_distilled_json.py` first.
3. **Run** the pipeline (single pair or batch).
4. **Report**: summarize per-paper coverage + which `write-methods`/`write-results` corpus files were hit/missed + critical gaps. Do not restate the full report.
5. **Suggest fixes**: critical gaps → point to the specific corpus files/`design_type_map.json` entries to extend; offer to route the fix through the distill-* Phase 4 writeback gate.

## Boundaries

- This tool validates corpus coverage; it does not invent templates or edit the corpora.
- `--skills-dir` must contain `write-methods/SKILL.md` and `write-results/SKILL.md` (default: repo root).
- If neither `--methods-json` nor `--batch-dir` is given, the tool exits with an error — collect inputs before running.
