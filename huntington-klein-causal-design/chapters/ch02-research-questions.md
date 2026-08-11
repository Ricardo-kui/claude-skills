# Chapter 2: Research Questions

## Core Idea

A good empirical research question is answerable by conceivable evidence and would change what is understood about the world. A causal question must name a manipulable or interpretable treatment contrast rather than merely ask whether variables covary.

## Question Contract

Write the question in this form:

> For units in population **P**, what is the effect of changing **X** from **x0** to **x1** on **Y** over horizon **T**, relative to the specified counterfactual?

Then record:

- theoretical mechanism;
- unit and level of analysis;
- treatment assignment or exposure process;
- outcome timing;
- target estimand;
- evidence that would support, weaken, or redirect the theory.

## Quality Tests

1. **Answerability**: Can any possible evidence settle or materially update the question?
2. **Theory relevance**: Would different plausible answers imply different lessons?
3. **Result symmetry**: Can both a positive and a null/opposite result be interpreted without inventing a new question afterward?
4. **Precision**: Are “best,” “effective,” “impact,” and similar terms operationally defined?
5. **Causal contrast**: Is the intervention and counterfactual coherent?
6. **Feasibility without dilution**: Can the question be studied without changing its theoretical object merely to fit available data?

## Theory and Data

Theory can precede the question or be refined by observations, but causal inference remains theory-driven: contextual knowledge constrains the DGP and tells the researcher which patterns count as evidence. Exploratory pattern-finding is valuable for description and prediction; it does not become confirmatory causal evidence simply by adding a causal label later.

## Failure Modes

- **Outcome fishing**: Searching many outcomes and presenting the most favorable one as pre-specified.
- **Proxy drift**: Replacing the construct with a convenient measure without discussing lost coverage.
- **Post-result theorizing**: Treating an explanation invented after seeing the estimate as if it generated the test.
- **Vague treatment**: Asking about “technology,” “policy,” or “leadership” without defining exposure, dose, timing, or comparison.

## Completion Check

Proceed only when potential results—including null and sign-reversed results—have pre-specified interpretive consequences.

## Worked Example

> Source-grounded reconstruction from Huntington-Klein (2025); compressed and paraphrased.

Start with the theory that students respond to incentives. “Are incentives good?” is not answerable because the treatment, outcome, population, and evaluative standard are vague. A better question is: “Among students in a specified school system, what is the effect of offering a fixed payment for meeting a pre-specified grade threshold during one semester on study effort and achievement by semester end, compared with no payment?”

Before seeing data, write the result map:

- higher effort and achievement would support responsiveness to the incentive in this setting;
- higher effort but unchanged achievement would separate motivation from production of learning;
- no behavioral change would weaken the proposed mechanism or indicate an ineffective treatment version;
- crowd-out after payments stop would change the policy horizon and theoretical interpretation.

The example is ready for design only after assignment, treatment versions, spillovers among peers, outcome timing, and the target estimand are specified.

## Connects To

- [Ch5](ch05-identification.md): determine whether the question is identified.
- [Ch10](ch10-treatment-effects.md): choose the population and treatment-effect average.
- [Ch23](ch23-under-the-rug.md): validate the measures and treatment definition.
