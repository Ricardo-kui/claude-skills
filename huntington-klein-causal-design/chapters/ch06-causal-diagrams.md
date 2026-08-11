# Chapter 6: Causal Diagrams

## Core Idea

A causal diagram is a compact, contestable model of the data-generating process. Nodes represent variables; directed arrows represent causal relations. Its purpose is to expose why treatment and outcome are associated and which assumptions allow a causal contrast.

## Diagram Contract

Include enough structure to represent:

- the treatment and outcome;
- causes of treatment;
- causes of outcome;
- common causes;
- mediators;
- selection and measurement processes when relevant;
- treatment timing and feedback through temporally indexed nodes;
- moderators as effect modification, described alongside rather than confused with an ordinary causal arrow.

For every omitted variable class, state why it is irrelevant, absorbed into another node, or outside the target estimand.

## Causal Effect

Interpret “X causes Y” as an intervention claim: changing X while holding the relevant causal system fixed would change Y. Distinguish:

- **direct effect**: a path from X to Y without an intermediate node;
- **indirect effect**: an effect transmitted through one or more mediators;
- **total effect**: all causal paths from X to Y included in the research question;
- **controlled/direct-effect target**: requires additional assumptions and a different conditioning strategy.

## Workflow

1. Define the treatment contrast and outcome horizon.
2. Set the temporal order before drawing arrows.
3. Add causes of treatment and outcome using theory and institutional knowledge.
4. Mark mediators, selection, and measurement nodes.
5. Identify the causal paths that constitute the target effect.
6. Identify noncausal paths that could explain the observed association.
7. Translate graph features into explicit identifying assumptions.
8. Derive observable implications where possible.

## Failure Modes

- **Control-list DAG**: drawing only variables that happen to exist in the dataset.
- **Arrow by correlation**: using observed association to set causal direction.
- **Post-treatment confusion**: labeling mediators as baseline confounders.
- **Missing selection**: omitting the process that determines sample inclusion or observation.
- **Timeless feedback**: drawing a cycle instead of indexing variables across time.

## Completion Check

The graph is useful only when another researcher can challenge an arrow, an omitted path, or a temporal ordering and see how that challenge changes the design.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Observed police presence and crime can be positively associated even if police reduce crime. A minimal time-ordered DAG might include:

- prior crime → current police deployment;
- prior crime → current crime;
- police deployment → expected cost of offending → current crime;
- local economic shocks → police deployment and current crime.

The target total effect includes the deterrence path through expected cost. Conditioning on that mediator would no longer estimate the total effect. Controlling for prior crime may close part of the deployment back door, but local shocks remain unless measured or isolated through a design.

The diagram does not prove deterrence. It explains why the raw positive association is compatible with a negative causal effect and exposes what the design must address. A useful answer should present at least one rival DAG—for example, police deployment responding to unobserved current crime risk—and explain how the chosen variation distinguishes them.

## Connects To

- [Ch7](ch07-drawing-causal-diagrams.md): construct and simplify the graph.
- [Ch8](ch08-causal-paths.md): enumerate paths and choose adjustment.
- [Ch23](ch23-under-the-rug.md): add measurement, missingness, and interference.
