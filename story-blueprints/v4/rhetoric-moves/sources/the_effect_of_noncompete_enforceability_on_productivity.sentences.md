---
type: sentences-archive
citekey: "the_effect_of_noncompete_enforceability_on_productivity"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\The Effect of Noncompete Enforceability on Productivity.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# the_effect_of_noncompete_enforceability_on_productivity 句子库存

## introduction
<!-- para 1 -->
We estimate the effects of NCA enforceability using a stacked difference-in-differences design (Cengiz et al., 2019).
Each subexperiment corresponds to a single state-year change in enforceability and compares treated states to states that do not experience any enforceability changes over the sample period.
To ensure clean pre- and post-treatment dynamics, we restrict attention to state-years with no other enforceability changes in the four years before or after the event.
<!-- para 2 -->
Observations are at the state-year-granular industry (3-digit SIC or 4-digit NAICS)-subexperiment level, where granular industries belong to broad industries (2-digit SIC) in order to create a consistent time series across years. [^1] We exclude observations with missing or implausible values for wages or value added; details are provided in the Supplemental Appendix.
<!-- para 3 -->
Formally:
<!-- para 4 -->
$$
Y_{s,t,n,b}=\beta\,\mathrm{Enforceability}_{s,t}+\rho_{s,b}+\gamma_{t,N(n),b}+\alpha_{n,b}+\varepsilon_{s,t,n,b} \tag{1}
$$
<!-- para 5 -->
where  $Y_{s,t,n,b}$ denotes the outcome in state s, year t, granular industry n in broad industry  $N(n)$, and subexperiment b.
The specification includes state-by-subexperiment fixed effects, year-by-broad industry-by-subexperiment fixed effects, and granular industry-by-subexperiment fixed effects, absorbing permanent differences across states, common shocks within broad industries over time, and permanent differences across granular industries.
We cluster standard errors at the state-subexperiment level and weight observations by pre-period employment.

## results
<!-- para 4 -->
**Table 1.** The Effects of NCA Enforceability on Worker and Firm Outcomes in Manufacturing Data
<!-- para 5 -->
| (1) Average Earnings | (2) Manufacturing Value Added | (3) Value Added Per Worker | (4) Sales | (5) Capital | (6) Capital Per Worker | (7) Labor Share of Income | (8) Employment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NCA Score | -0.0713 (0.0763) | -1.69*** (0.597) | -0.85*** (0.309) | -0.794* (0.451) | 0.128 (0.256) | 0.129 (0.172) | 0.0407 (0.051) | -0.0434 (0.358) |
| N | 252,774 | 252,987 | 252,774 | 252,987 | 248,425 | 248,214 | 249,965 | 252,987 |
| Mean DV | 37,218 | 3.35† | 151,466 | 5.22† | 1.50† | 75,729 | 0.36 | 20,096
<!-- para 6 -->
*Notes.* This table reports estimates from the industry-by-state-level Poisson stacked regression model described in Equation 1 for all columns but Column 7, which reports estimates from a comparable industry-by-state-level OLS stacked regression model.
Different sample sizes result from small amounts of data missingness.
Each regression includes fixed effects for year × broad industry × subexperiment, state × subexperiment, and four-digit NAICS or three-digit SIC × subexperiment.
Standard errors clustered at state × subexperiment level in parentheses. *** p < 0.01, ** p < 0.05, * p < 0.1.
<!-- para 7 -->
*†* The mean dependent variables in Columns 2, 4, and 5 are in billions of dollars.
<!-- para 8 -->
The coefficient in Column 1 implies that making NCAs easier to enforce reduces manufacturing workers' earnings.
An enforceability increase equal to 10% of the observed variation in the NCA Score dataset results in an earnings decline of about 0.7% (calculated as  $exp(-0.0713 \times 10\%) - 1$), though the coefficient is not statistically significant.
This is quantitatively smaller than but qualitatively in line with previous findings for the economy as a whole. [^2] Figure 1, Panel (a), contains event study estimates demonstrating wage dynamics over time in response to NCA enforceability increases centered at time zero.
<!-- para 9 -->
**Figure 1.** Event Study Estimates for Average Wages and Manufacturing Value Added
<!-- para 10 -->
**Panel A.** Average earnings
<!-- para 12 -->
**Panel B.** Manufacturing value added
<!-- para 14 -->
*Notes.* Each figure contains coefficients and $95\%$ confidence intervals from Poisson pseudo-likelihood stacked difference-in-difference regression models, weighted by average employment before the treatment year in each state in each industry.
See Equation 1 for an analogous regression equation.
<!-- para 15 -->
One explanation for workers' earnings declines is that increases in NCA enforceability cause firms to be less productive, generating less surplus to be shared with workers.
We find (in Column 2) clear evidence of decreases in manufacturing output as measured by value added: an enforceability increase equal to $10\%$ of observed variation generates a value added decrease of $15.5\% (= exp(-1.69 * 10\%) - 1)$.
Figure 1, Panel (b), contains comparable event study estimates.
We also find a decline in productivity, as measured by value added per worker, of $8.1\%$ for the same enforceability increase (Column 3).
It is also reflected in reductions in sales (Column 4), and does not appear to be driven by reductions in capital (Columns 5 and 6), though the estimated effects on capital are noisy.[^3] We find zero effect on the labor share (Column 7), suggesting that any reductions in wages operate fully through the channel of productivity declines in the manufacturing sector, rather than changes in bargaining power.
In Column 8, we do not find major changes in employment.
<!-- para 16 -->
The estimated effects on output and productivity are large and difficult to reconcile with simple interpretations.
Changes in aggregate productivity may arise from a range of factors, including firm entry and exit, worker sorting, and within-plant changes.
State-level estimates may be confounded by reallocation of production across states, changes in industry composition associated with the SIC–NAICS transition, or other confounding factors.
In addition, the estimated effect of NCA enforceability on the labor share is counterintuitive: a back-of-the-envelope calculation using changes in earnings, employment, and value added would predict an increase in labor's share.
Distinguishing among these explanations likely requires plant-level data, which we leave to future work.
<!-- para 19 -->
**Table 2.** The Effects of NCA Enforceability on Worker and Firm Outcomes for All Sectors
<!-- para 20 -->
**Panel A: Manufacturing Only**
<!-- para 21 -->
| (1) Average Wages | (2) Manufacturing Value Added | (3) Value Added Per Worker | (4) Labor Share of Income | (5) Employment |
| --- | --- | --- | --- | --- | --- |
| NCA Score | -0.116 (0.122) | -1.05* (0.613) | -0.378 (0.476) | 0.0779 (0.115) | -0.295 (0.263) |
| N | 7,584 | 7,584 | 7,584 | 7,584 | 7,584 |
| Mean DV | 44,652 | 77.8† | 115,144 | 0.45 | 627,717
<!-- para 22 -->
**Panel B: All Sectors**
<!-- para 23 -->
| (1) Average Wages | (2) Value Added | (3) Value Added Per Worker | (4) Labor Share of Income | (5) Employment |
| --- | --- | --- | --- | --- | --- |
| NCA Score | -0.142** (0.0603) | 0.0114 (0.306) | -0.119 (0.149) | 0.01 (0.019) | 0.145 (0.218) |
| N | 66,379 | 66,379 | 66,379 | 66,379 | 66,379 |
| Mean DV | 35,243 | 72.5† | 84,345 | 0.48 | 1,278,797
<!-- para 24 -->
*Notes.* Panel A reports estimates from state-level Poisson stacked regression models analogous to that described in Equation 1 for all columns but Column 4, which reports estimates from a comparable state-level OLS stacked regression model.
Panel B is identical but is run at the broad sector-by-state level, where broad sectors correspond to 2-digit NAICS codes.
Each regression in Panel A includes fixed effects for state × subexperiment, and year × subexperiment.
Regressions in Panel B instead include state × subexperiment and year × broad sector × subexperiment fixed effects.
Standard errors clustered at state × subexperiment level in parentheses. *** p < 0.01, ** p < 0.05, * p < 0.1.
<!-- para 25 -->
*†* The mean dependent variables in Column 2 are in billions of dollars.
<!-- para 26 -->
The estimates in Column 1 further corroborate that increased NCA enforceability leads to lower average wages, both in manufacturing (Panel A) and overall (Panel B); the magnitudes are comparable, though the estimate is statistically significant only for the broader economy in Panel B.
<!-- para 27 -->
Columns 2 and 3 of Panel A report negative effects on value added and value added per worker in the manufacturing sector.
The coefficients are meaningfully smaller than those reported in Section III.A.
Interestingly, in Panel B, we show that these results do not hold for the economy as a whole: we estimate no effect of NCA enforceability on value added across all industries, and a much smaller effect on productivity.
This may be due to differential use of NCAs across industries, differential effects of NCAs on worker motivation or firm investment, differential importance of worker reallocation for aggregate productivity, or other factors.
Exploring this finding is a leading avenue for future work.
<!-- para 28 -->
Column 4 reports estimates of the effect of NCA enforceability on the labor share.
We find noisy null effects for both manufacturing and all sectors together.
In Column 5, we estimate a negative effect of NCA enforceability on manufacturing employment but a positive effect for all sectors.
Neither result is statistically significant.
<!-- para 30 -->
We assembled a novel dataset on state-level manufacturing production to analyze the effect of NCA enforceability on productivity.
We find that NCA enforceability strongly decreases output and value added per worker, but does not affect the labor share of income.
The manufacturing production dataset may be useful for other researchers studying how other forms of state-level policy variation affect productivity, such as investment taxation or environmental regulation.
<!-- para 32 -->
[^1]: We categorize broad industries as follows: apparel, chemical, electrical, fabricated metal, food, furniture, machinery, primary metal, miscellaneous, motor and transportation, nonmetal, paper, petroleum and coal, printing, rubber, textile, and wood.
One could alternatively specify a model with state-by-subexperiment and granular industry-by-year-by-subexperiment fixed effects.
However, due to the switch from SIC to NAICS that occurs in 1997 and the lack of a reasonable crosswalk between SIC and NAICS at the granular industry level, doing so eliminates the ability to use data from years prior to 1997—and therefore NCA law changes prior to 2002.
We opt instead to use the full suite of data and control for permanent differences across granular industries.
<!-- para 33 -->
[^2]: Johnson, Lavetti and Lipsitz (2025) find that the identical change in NCA score yields a 1.2% decline in earnings across all sectors.
<!-- para 34 -->
[^3]: We construct capital as described in the Supplemental Appendix.
To generate a consistent time series, we combine estimates of capital for years up until 1996 based on SIC codes with estimates of capital for 1997 forward based on NAICS codes.
<!-- para 35 -->
[^4]: In order to create a consistent time series, we focus attention on sectors for which SIC and NAICS codes are easily comparable, excluding those for which a straightforward cross-walk at the sectoral level is not available.
We group sectors as follows: Agriculture, Forestry, Fishing, and Hunting (NAICS 11; SIC 01-09); Mining, Oil, and Gas (NAICS 21; SIC 10-14); Utilities (NAICS 22; SIC 49); Construction (NAICS 23; SIC 15-17); Manufacturing (NAICS 31-33; SIC 20-39); Wholesale Trade (NAICS 42; SIC 50-51); Retail Trade and Services (NAICS 44-45, 56, 61, 62, 71, and 72; SIC 52-59 and 70-89); Transportation and Warehousing (NAICS 48-49; SIC 40-42 and 44-47); Finance, Insurance, and Real Estate (NAICS 52-53; SIC 60-67).
Note that the crosswalks are imperfect, and some sub-industries may cross industrial lines between NAICS and SIC years.
