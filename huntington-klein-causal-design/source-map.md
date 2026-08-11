# Source and Provenance Map

Load this file only when tracing guidance to the source, checking whether an example is book-grounded, or separating textbook synthesis from operational or frontier guidance.

## Provenance Classes

- **Book synthesis** — compressed, paraphrased guidance grounded in the mapped Huntington-Klein chapter.
- **Operational synthesis** — agent-facing contracts, completion criteria, ledgers, Stop Rules, and handoff fields derived from the book's framework rather than quoted from it.
- **Frontier guardrail** — current-method caution that requires verification against primary methods literature and software documentation before publication or execution.

Worked examples label themselves as either `Source-grounded reconstruction` or `Synthetic application`. Treat neither label as a quotation. The normalized Markdown lacks stable page anchors, so verify quotations against the original edition rather than citing these syntheses.

## Local Source Root

`D:\Onedrive\Obsidian Vault\文献笔记库\02 原子化\写作指导\实证分析指导\Huntington-Klein - 2025 - The effect an introduction to research design and caus-20260810-135750\chapters`

## Chapter Mapping

| Skill reference | Normalized source file |
|---|---|
| `chapters/ch00-orientation.md` | `00-Introduction.md` |
| `chapters/ch00-reading-map.md` | `00-Finding-Stuff-in-This-Book.md`; `index.md` |
| `chapters/ch01-designing-research.md` | `01-Designing-Research.md` |
| `chapters/ch02-research-questions.md` | `02-Research-Questions.md` |
| `chapters/ch03-describing-variables.md` | `03-Describing-Variables.md` |
| `chapters/ch04-describing-relationships.md` | `04-Describing-Relationships.md` |
| `chapters/ch05-identification.md` | `05-Identification.md` |
| `chapters/ch06-causal-diagrams.md` | `06-Causal-Diagrams.md` |
| `chapters/ch07-drawing-causal-diagrams.md` | `07-Drawing-Causal-Diagrams.md` |
| `chapters/ch08-causal-paths.md` | `08-Causal-Paths-and-Closing-Back-Doors.md` |
| `chapters/ch09-finding-front-doors.md` | `09-Finding-Front-Doors.md` |
| `chapters/ch10-treatment-effects.md` | `10-Treatment-Effects.md` |
| `chapters/ch11-causality-with-less-modeling.md` | `11-Causality-with-Less-Modeling.md` |
| `chapters/ch12-opening-the-toolbox.md` | `12-Opening-the-Toolbox.md` |
| `chapters/ch13-regression.md` | `13-Regression.md` |
| `chapters/ch14-matching.md` | `14-Matching.md` |
| `chapters/ch15-simulation.md` | `15-Simulation.md` |
| `chapters/ch16-fixed-effects.md` | `16-Fixed-Effects.md` |
| `chapters/ch17-event-studies.md` | `17-Event-Studies.md` |
| `chapters/ch18-difference-in-differences.md` | `18-Difference-in-Differences.md` |
| `chapters/ch19-instrumental-variables.md` | `19-Instrumental-Variables.md` |
| `chapters/ch20-regression-discontinuity.md` | `20-Regression-Discontinuity.md` |
| `chapters/ch21-partial-identification.md` | `21-Partial-Identification.md` |
| `chapters/ch22-gallery-of-methods.md` | `22-A-Gallery-of-Rogues-Other-Methods.md` |
| `chapters/ch23-under-the-rug.md` | `23-Under-the-Rug.md` |

## Operational Extensions

Treat these as agent protocol rather than claims that the book presents the exact format:

- the four output modes and Design Packet in `SKILL.md` and `patterns.md`;
- the Variation Map, Assumption Ledger, Stop Rule, and Epistemic Split labels;
- mode-specific Completion Rules;
- the YAML-shaped Execution Handoff;
- the method-selection and stop-rule tables in `cheatsheet.md`;
- synthetic applications marked in chapter files.

## Frontier-Verification Triggers

Verify current primary literature and software documentation when the answer depends on:

- staggered-adoption DiD estimators, aggregation, covariate adjustment, or inference;
- weak-instrument diagnostics or weak-identification-robust procedures;
- RDD bandwidth, bias correction, mass-point handling, or geographic designs;
- matching-estimator variance and bootstrap validity;
- synthetic control, matrix completion, double machine learning, causal forests, causal discovery, or structural estimation;
- package-specific defaults, returned estimands, standard errors, or treatment-support rules.

## Completion Rule

Finish a provenance audit only when every contested statement is classified as book synthesis, operational synthesis, frontier guardrail, or project-specific judgment, and every publication-facing frontier claim has an external verification plan.
