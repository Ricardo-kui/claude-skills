# Story Learning Card — Chen, Li, and Li (2025, Outlet Unverified)

## Metadata

```yaml
schema_version: "4.0-lite"
id: chen2025-free-expression-stock-crash-risk
paper:
  citekey: null
  title: "Freedom of Expression and Stock Price Crash Risk: Evidence from a Natural Experiment"
  outlet: unverified
  year: 2025
  publication_status: unverified
  paper_type: quantitative
  source_version: parsed_full_text
  inclusion_rationale: "A partial learning object for turning a civic institution into a capital-market story in which outside disclosure changes both managers' ability and incentives to hoard bad news."
reading_scope:
  sections_read: [introduction, theory, methods, results, discussion]
  coverage: complete
  source_records: ["Chen 等 - 2025 - Freedom of Expression and Stock Price Crash Risk Evidence from a Natural Experiment.md"]
analysis_focus:
  primary: [introduction, theory]
  supporting: [results, discussion]
  audit: [methods]
  departure_note: "Results receive added attention because the paper separates ability and incentive pathways before using crash versus jump events to distinguish bad-news flow from a generic information-flow change."
mechanism_evidence:
  status: partly_probed
  basis: "The study observes crash risk, media and stakeholder tone, reporting and investment proxies, and theory-consistent boundaries, but not managers' withheld-news stock, their beliefs about third-party revelation, or public stakeholders' legal concerns."
classification:
  theoretical_problem_form: [civic-institution-to-capital-market-outcome, bad-news-hoarding]
  narrative_dynamics: [ability-and-incentive-dual-channel, disclosure-before-crash, bad-news-not-good-news]
  retrieval_signals: [anti-slapp, free-expression, stock-price-crash-risk, bad-news-disclosure, stakeholder-monitoring]
  confidence: reviewed
section_learning:
  introduction:
    suitable: "yes"
    requires: []
    learn:
      - "Introduce an indirect institutional effect by specifying the information actor the law protects, the managerial behavior that actor constrains, and the downstream market consequence."
      - "Keep an adverse possibility alive—more speech could also spread rumor—so the policy-to-crash direction becomes an empirical question rather than an assumption."
    caveat:
      - "This setup needs a credible account of who receives protection and why that actor has value-relevant information; a general transparency claim is not enough."
  theory:
    suitable: "yes"
    requires: []
    learn:
      - "Give parallel mechanisms distinct jobs: public revelation reduces managers' ability to hide news, while anticipated third-party revelation raises the cost and lowers the incentive to hide it."
      - "Derive different boundary predictions from each pathway before tests, rather than treating heterogeneity as a generic credibility exercise."
    caveat:
      - "The distinction transfers only if the two mechanisms imply genuinely different observable conditions; neither pathway is directly proven merely by a lower crash measure."
  methods:
    suitable: "partial"
    requires: []
    learn:
      - "Use a stacked adoption design with clean not-yet-treated controls when a state legal shock is mapped to headquarters-state exposure and the payoff is a firm-year outcome."
    caveat:
      - "Headquarters matching depends on jurisdiction and local-information arguments specific to defamation and anti-SLAPP law; it is not a generic treatment assignment."
  results:
    suitable: "yes"
    requires: []
    learn:
      - "Unravel the market outcome through timing, mechanism-discriminating boundaries, stakeholder-tone evidence, and manager-action evidence before testing whether only negative—not positive—extreme returns change."
      - "Use the crash-versus-jump contrast to make the claimed informational direction observable rather than merely reporting another robustness result."
    caveat:
      - "Tone, accruals, and investment measures are indirect proxies; a long result sequence should not be read as direct observation of a complete hoarding process."
  discussion:
    suitable: "partial"
    requires: []
    learn:
      - "Return from a market anomaly to the institutional condition that determines whether third parties can make bad news public."
    caveat:
      - "The ending should not turn lower crash risk into proof that all additional expression is accurate or welfare improving."
story_assessment:
  overall_role: partial_exemplar
  mode: single_read
```

## Story Reading

### Theme question

Can protection from retaliatory lawsuits make bad news enter prices before it accumulates into a crash, by reducing both managers' ability and incentive to conceal it?

### Whole-story synopsis

The paper starts from the chilling effect of SLAPPs and turns free-expression protection into a capital-market question. Local citizens, employees, journalists, investors, and other third parties have information about nearby headquarters firms but may stay silent if litigation is costly. Anti-SLAPP statutes lower that cost. The theoretical middle has two linked channels: more willing third parties reveal bad news and reduce managers' ability to hoard it; the prospect that a third party will expose withheld news also raises managers' litigation, career, and reputation costs, reducing their incentive to manipulate earnings or overinvest. Rumor and media slant supply an author-signaled counterforce. A stacked state-adoption design finds lower NCSkew and DUVol after enactment. The predicted effect is stronger where local information or dissemination capacity is greater and where dismissal or shareholder-litigation costs are higher. Negative tone in newspapers, employee reviews, and Seeking Alpha content, especially for firms with worse future performance, supports the ability channel; lower accrual manipulation, forecast beating, fraud propensity, and overinvestment support the incentive channel. The crash-event but not jump-event result closes the story as a bad-news-specific rather than generic-news-flow outcome. The conclusion returns to the opening claim that legal protection of expression can prevent the delayed release of accumulated bad news.

### Characters and storylines

- **Institutional character:** anti-SLAPP statutes, which lower expected litigation costs for public criticism.
- **Information characters:** geographically close public stakeholders and media, whose knowledge and dissemination capacity determine how hard bad news is to suppress.
- **Manager character:** the manager, who can hoard adverse information but faces a greater ex post cost when third parties reveal it.
- **Two pathway characters:** ability to conceal and incentive to conceal, which connect speech protection to distinct boundary and behavioral predictions.
- **Outcome character:** stock price crash risk, the terminal release of accumulated bad news; jump events serve as its directional boundary.
- **Storyline:** protection → third-party disclosure and anticipated exposure → less ability and incentive to hoard bad news → fewer accumulated-news crashes.

### Five acts

- **Exposition:** SLAPPs chill legitimate negative information, while crash theory explains how managerial hoarding turns dispersed bad news into a sudden market collapse.
- **Rising action:** Anti-SLAPP protection makes outside disclosure more likely and more costly for managers to ignore; slant and rumor make the direction uncertain.
- **Climax:** Stacked-DiD estimates show lower crash-risk measures after enactment with no pretrend.
- **Falling action:** Ability and incentive boundaries, negative stakeholder/media tone, and reduced manipulation and overinvestment populate the two mechanisms.
- **Denouement:** Fewer crash but not jump events reframe speech protection as smoother incorporation of bad news rather than a uniform change in information flow.

### Tension

- **Source:** More expression can reveal hidden adverse facts but could also amplify misinformation, so it is not self-evident that legal protection stabilizes prices.
- **Construction:** The paper renders this contestable by separating bad-news-specific outcomes from positive jump events and by giving the two channels distinct predicted conditions.

### Alternative readings

- **author-signaled-alternative:** Less constrained media can spread rumor or slant, potentially reducing market efficiency and increasing crash risk.
- **analyst_counterfactual:** The news tone and manager-action results can be consistent with other changes in local information environments. They do not directly inventory withheld news or show managers' beliefs about revelation.

## Story Assessment

- **Theme coherence:** `works` — free expression, bad-news hoarding, and crash risk remain linked through the paper.
- **Character discipline:** `works` — third parties, managers, ability, incentive, and crash each have a noninterchangeable role.
- **Knot integrity:** `works` — the ambiguity of freer speech and the otherwise hidden accumulation of bad news create a real problem.
- **Plot emergence:** `works` — the two pathways generate distinct boundaries and supporting outcomes rather than a single generic monitoring claim.
- **Tie–unravel alignment:** `partly_works` — the terminal crash payoff and several pathway-consistent measures align, but the core withholding and belief processes remain unobserved.
- **Ending quality:** `works` — crash-versus-jump evidence returns to the opening distinction between bad-news accumulation and general information flow.
- **Boundary:** This evaluates storytelling only; it is not a judgment about causal identification or research quality.

## Learning Affordances

### Introduction and Theory

The paper is useful when an outside actor's ability to publicize private information can change both what managers can conceal and why concealment becomes costly. Its two-channel architecture cannot be copied if mechanisms have no different boundary predictions or the proposed stakeholders lack credible information access.

### Methods and Results

The evidence sequence makes a downstream market outcome meaningful by stepping backward through conditions, stakeholder expression, and manager actions, then separating crashes from jumps. This only transfers when every measure answers a named part of the mechanism rather than serving as an accumulated list of proxies.

### Discussion

The ending works by showing that the relevant consequence is smoother bad-news incorporation, not unrestricted good news. Do not generalize it to all speech settings or claim direct observation of the entire disclosure process.

## Comparison prompt

Should a paper treat bad-news concealment itself as the central outcome, or treat it as an intervening story that only becomes consequential when accumulated information produces a market crash?
