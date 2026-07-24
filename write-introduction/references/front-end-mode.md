# Title–Abstract–Introduction Front-End Mode

Use this reference only for `--mode=front-end` or `--mode=align`.

First load `../academic-writing-corpus/storytelling/reader-conversion-sequence.md`. Treat Title, Abstract, and Introduction as progressively expanded versions of one promise:

1. Title names the phenomenon, relationship, or tension without claiming unsupported findings.
2. Abstract states the problem, approach, evidence status, headline answer or placeholder, and contribution.
3. Introduction establishes the conversation, ties the central knot, raises the stakes, previews the resolution, and states the reader shift.

## Front-End Output

```markdown
## One-Sentence Front-End Promise

## Title Candidates
1. [phenomenon-forward]
2. [relationship-forward]
3. [tension-forward]

## Abstract Skeleton
- Problem and conversation:
- Central knot:
- Approach and empirical setting:
- Headline answer: [actual finding or explicit placeholder]
- Reader shift / contribution:

## Introduction Skeleton
[functional paragraph map]

## Alignment Table
| Contract element | Title | Abstract | Introduction | Status |
|---|---|---|---|---|
| Theme question | | | | |
| Central knot | | | | |
| Main characters | | | | |
| Promised resolution | | | | |
| Reader shift | | | | |
```

## Evidence Boundary

- If `story.evidence_state: unstable`, use `[headline finding pending]`.
- If evidence is mixed, state the mixed pattern without converting it into a clean success claim.
- Do not place a contribution in the Title that the Abstract or Introduction cannot defend.
- `--mode=align` reports mismatches and repairs the promise; it does not generate a replacement manuscript.
