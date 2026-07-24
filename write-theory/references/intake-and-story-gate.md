# Theory Intake and Story Gate

## Discovery Order

Find `paper-state.yaml` in this order:

1. explicit `--paper-state=<path>`;
2. current working directory;
3. project root.

Read canonical `story` first, followed by `introduction.theory_hints` and `introduction.contribution_contract`.

If `story` is absent, use the sibling `paper-story-contract/references/schema.md` migration map. Legacy `central_knot_statement`, `core_constructs`, and `narrative_arc` are read-only migration inputs; emit a provisional canonical block and do not write those aliases again.

## Gate

Full Theory requires:

- theme question and central knot;
- explicit main/supporting characters;
- at least one storyline with promised resolution;
- stage and evidence state.

Theory additionally requires each hypothesis to reference `storyline_id`. A new main character blocks confirmed output until the contract is updated. A new supporting construct may be proposed provisionally, but cannot silently enter a refining or finishing draft.

## Stage Behavior

- preparing: diagnose constructs, theories, mechanisms, and rival accounts only;
- blocking: produce a rough scaffold with labelled assumptions;
- refining: full Theory work, confirmed contract required;
- finishing: polish and QC only, no unsupported new storyline.

## Local Bypass

A single hypothesis, construct definition, or transition may be returned with:

> Local-only output: not validated against the whole-paper story contract.

Do not update paper state in this mode.
