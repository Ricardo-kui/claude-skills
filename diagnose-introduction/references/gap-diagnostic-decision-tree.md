# Gap / Problematization Diagnostic Decision Tree

Use this reference to diagnose the user's gap type and conversation strategy.

## Core Question

Does the literature contain a real conflict / opposing theory?

```
├── Yes → Incommensurability (high tension)
│         Exemplars: Zhou 2017, Pontikes 2012, Keeves 2017, Park 2025, Hahl 2017
│         Signature language:
│         - "A consensus is building that..."
│         - "A long-standing debate centers on..."
│         - "Classic [discipline] treatments depict... But a large body of research since [decade] has shattered this image."
│         - You are challenging a widely accepted view or canonical theory
│         Risk: Needs strong evidence; cannot erect straw men. Classic theory disruption needs sufficient theoretical runway.
│
└── No → Is the literature one-directional but has important blind spots?
          ├── Yes → Inadequacy (medium tension, most common, ~45% of MVP30)
          │         Exemplars: Han 2024, Shipilov 2020, Lashley & Pollock 2020, Gamache 2020, Shen 2022, Employee Free Speech
          │         Signature language:
          │         - "failed to distinguish" (construct conflation)
          │         - "overlooks" (one-sided perspective)
          │         - "treated... as decontextualized" (decontextualization)
          │         - "conceptualizing... as universally... may paint too simplistic a picture" (oversimplification)
          │         - "assumes uniform effects across [groups]" (symmetric dual-track: same policy misapplied across groups)
          │         Risk: Must provide specific literature evidence supporting the "inadequacy" diagnosis
          │
          └── No → Is it merely "there is more to know"?
                    ├── Yes → Incompleteness (low tension, ~40% of MVP30)
                    │         Exemplars: Wu 2025, Eilert 2017, Toh 2023, Malshe 2015, Darby 2024
                    │         Signature language:
                    │         - "has gone largely unaddressed"
                    │         - "remains poorly understood"
                    │         - "limited attention"
                    │         - "This is surprising for three reasons..." (three-reason gap argument)
                    │         Risk: Most easily read as incremental; must explain the theoretical importance of the omission
                    │
                    └── No → Rethink your contribution
```

## Architecture-Specific Diagnostic Cues

| Architecture type | Diagnostic cue | Exemplar |
|-------------------|---------------|----------|
| Three-reason gap | User mentions crossing two disciplines with a bridge construct | Malshe 2015 |
| Symmetric dual-track | User describes same policy/practice having opposite effects on two groups | Employee Free Speech |
| Consensus challenge + counterexample | User challenges a meta-analytic or widely held consensus | Gamache 2023 |
| Classic theory disruption | User challenges Weber/Bourdieu or other canonical theory | Hahl 2017 |
| 2×2 construct differentiation | User disentangles a broad construct into sub-types with distinct mechanisms | Gamache 2020 |
