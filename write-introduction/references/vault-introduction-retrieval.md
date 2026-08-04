# Vault evidence retrieval for Introduction

Use this reference only when building a full Introduction or front-end. Skip it for local-only Hook, Gap, or contribution-sentence requests.

## Retrieval order

1. If `paper-state.yaml` contains `vault.section_evidence_map`, read the Introduction rows and extract proposition ID, citation key, note path, evidence role, and the recoverable supporting claim. If `vault.war_room` exists, add the Gap state and canonical evidence buckets.
2. If the mapping is absent but a Vault root is configured, search by paper title, `story.characters`, Gap terms, and theory names. Prefer literature notes and project evidence maps; cap the result at 10–15 highly relevant records.
3. If an Obsidian semantic-search tool is available, prefer it over filename search. Otherwise use bounded filesystem search.
4. If the path is unavailable or no relevant evidence is found, report the attempted path and query, retain citation placeholders, and ask for either the correct Vault root or 3–5 core sources. Do not block Story Intake or architecture work while waiting.

Do not assume a particular directory layout. Take every project path from `paper-state.yaml`, the nearest project instructions, or the user.

## Knowledge brief

Return this block before the scaffold when evidence was retrieved:

```markdown
## Vault 知识简报（Introduction）

| 命题 ID | Citation key | Evidence role | Recoverable support | Source note |
|---|---|---|---|---|
| [I1] | [@citekey] | [theory / empirical / review / construct / context] | [原笔记可还原的命题] | [path] |

### Gap anchors
- [来自 evidence map 或 war room 的已核验定位]

### Evidence completeness
- 命中：[N]
- 检索方式：[configured mapping / semantic search / filesystem / user supplied]
- 尚缺：[不能由现有笔记支持的关键主张]
```

## Citation discipline

- Empirical papers support a finding direction, comparison, or boundary.
- Theory papers support an argument, mechanism, or proposition.
- Reviews and meta-analyses support consensus, heterogeneity, or debate status.
- Construct sources support definitions or differentiation.
- Context sources support factual setting claims.
- Never convert a theoretical or review source into a directional empirical finding.
- A citation count does not establish consensus. Verify the content used in the sentence.
- Distinguish Vault suggestions from sources selected by the user; flag material disagreement instead of silently replacing the user's choice.
