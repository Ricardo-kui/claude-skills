---
type: sentences-archive
citekey: "charoenwong2025_mutual_fund_common_owners_returns_and_proxy_"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\charoenwong2025-mutual-fund-common-owners-returns-and-proxy-voting-OvisOCR2-20260813-144202.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# charoenwong2025_mutual_fund_common_owners_returns_and_proxy_ 句子库存

## theory
<!-- para 2 -->
The theoretical foundation for our approach comes from Rotemberg (1984), which provides a framework where firms with common owners balance the interests of various shareholders, incorporating competitors' profits into their objective functions.
However, the implications for market outcomes remain theoretically ambiguous.
For instance, López and Vives (2019) derive that common ownership can increase innovation and profits under certain conditions, while Azar and Vives (2021) distinguish between intra-industry common ownership (which may reduce competition) and inter-industry common ownership (which may enhance welfare).
Moreover, common owners may be unable or unwilling to promote anticompetitive behavior either because such actions may violate legal or regulatory constraints or because large, diversified funds (which are more likely to be common owners) have limited incentives or capacity to engage in firm-specific product-market decisions.
<!-- para 3 -->
Previous papers empirically studying the effect of common ownership on market-level outcomes have reported evidence suggesting anticompetitive effects.
Azar et al. (2018) find that common ownership among airlines was associated with higher ticket prices, and He and Huang (2017) document increased market share and reduced product-market competition following institutional cross-ownership events.
However, subsequent methodological critiques have raised questions about identification strategies and measurements used.
Koch et al. (2021) challenge the robustness of earlier airline industry findings, highlighting potential confounds in market structure analysis, Lewellen and Lowry (2021) identify limitations in empirical approaches used to establish causal relationships between institutional ownership patterns and product-market outcomes, and Dennis, Gerardi, and Sche none (2022) demonstrate that accounting for route-specific demand factors materially affects inferences about common ownership's competitive effects in airline prices.
<!-- para 4 -->
The empirical impact of common ownership on firm behavior and market outcomes remains an open question.
However, essentially all papers rely on a common premise: the payoff to common owners increases when firms consider these owners' broader portfolio interests.
Therefore, given the methodological challenges in the empirical literature, we take a different approach to studying common ownership.
Rather than attempting to establish causal effects on product-market competition—a task that has proven difficult, given the lack of plausibly exogenous variation—we analyze the behavior of mutual funds with varying levels of common ownership, focusing specifically on their performance outcomes and governance decisions.
This approach allows us to document systematic patterns in institutional investor conduct and incentives.
<!-- para 5 -->
Our first hypothesis tests whether active fund managers with common ownership positions achieve superior returns for themselves and their investors.
Higher returns from CO strategies could indicate that these funds encourage portfolio firms to behave anticompetitively.
Furthermore, such outperformance could create a self-reinforcing cycle: investors allocate more capital to high-CO funds, strengthening fund managers' incentives to engage actively with firm management.
However, the plausibility of this mechanism has been questioned in the literature.
Common owners may be unwilling or unable to support anticompetitive practices due to various reasons.
First, as agents, fund managers face inherent conflicts of interest (e.g., Agarwal, Gay, and Ling (2014), Bebchuk, Cohen, and Hirst (2017), and Cohen, Coval, and Pastor (2005)), and broker-sold active funds typically have weaker incentives to generate alpha (Guercio and Reuter (2014)), potentially discouraging efforts to pursue CO benefits.
Second, implementing CO strategies also involves costly managerial effort and possible legal risks, which must be weighed against potential gains, given that manager compensation depends on both fund size and fees (Berk and Green (2004)).
Finally, even if CO strategies produce short-term outperformance, such gains could diminish over time as other investors adopt similar approaches.
Moreover, alternative explanations—such as portfolio industry concentration, common stock selection, or CO stock-picking—may also drive the observed outperformance of high-CO funds.
<!-- para 6 -->
To address the concerns above, we proceed as follows: First, we develop a fund-level CO measure, capturing the extent to which funds internalize the future profits of competing firms in their portfolios.
Using this measure, we design tests to evaluate whether the superior returns observed in high-CO funds can be attributed to a common ownership channel.
Specifically, we conduct three distinct analyses: i) comparing returns of CO holdings directly against non-CO holdings within the same fund, ii) examining the impact of industry-level common ownership intensity on the relationship between fund CO and returns, and iii) exploring whether the relationship is stronger in concentrated industries where potential anticompetitive influence might be greater.
Furthermore, we also investigate whether economic incentives exist for managers to adopt CO strategies by examining how fund-level CO relates to fund fees and manager compensation.
Finally, to rule out alternative explanations, we implement matched-sample analyses and explicitly control for portfolio industry concentration, common stock selection, or the tendency to select firms with high common ownership.
<!-- para 7 -->
Our second hypothesis examines whether mutual fund managers exercise their governance rights in ways consistent with common ownership theory.
For example, Shekita (2022) documents 30 cases of interventions by common owners, all of which required not only the attention of the common owner but also the active participation in engaging with corporate managers.
This analysis requires linking financial payoffs with fund managers' voting patterns, focusing on votes that could facilitate inter-firm coordination or affect managerial incentives.
Specifically, we test whether voting behavior is consistent with theoretical predictions that common owners would reduce executive pay-performance sensitivity (Antón et al. (2023)).
While we do not establish causality, systematic patterns in voting behavior provide evidence of how funds exercise their governance rights under common ownership.
<!-- para 9 -->
We derive our fund-level measure of common ownership by building upon the established firm-level measure of common ownership used in the existing literature.
We begin with the concept of profit weights between firms, then extend this to create fund-specific profit weights, and finally aggregate these into our fund-level common ownership measure.
<!-- para 11 -->
The literature typically measures common ownership based on how much a firm considers competitors’ profits in its decision-making.
For a shareholder s of the firm m, we denote her cash flow right as $\beta_{s,m}$, which equals the ratio of shares she owns to the total number of shares outstanding in firm $m$. [^10] She is considered a common owner if she holds positive stakes in both firm m and its competitor $n(\text{i.e.}, \beta_{s,m} > 0 \text{ and } \beta_{s,n} > 0)$.
According to O’Brien and Salop (2000) and Backus et al. (2021), common owners have an incentive to maximize total portfolio profits, leading firm managers to internalize profits across firms held by the same shareholders.
The weight (termed “profit weight” or $\kappa_{m,n}$) that firm m places on its competitor n’s profits is defined as (1)
<!-- para 12 -->
$$ \kappa_{m,n}=\frac{\sum_{\forall s}\beta_{s,m}\beta_{s,n}}{\sum_{\forall s}\beta_{s,m}^{2}}. $$
<!-- para 13 -->
This weight represents the extent to which focal firm m incorporates competitor firm n's profits into its own objective function. [^11] The numerator of equation (1) is the inner product of common ownership across all common owners, and the denominator is the focal firm m's ownership concentration (akin to the Herfindahl–Hirschman Index) as a scalar.
Thus, this measure can be interpreted as the strength of common ownership relative to the ownership concentration of the focal firm.
Theoretically, when $\kappa_{m,n}=1$, firm $m$ values firm $n$'s profits equally to its own when maximizing its objective function. $\kappa_{m,n}$ could exceed one, indicating that firm $m$ places more weight on competitor $n$'s profits than its own.
These profit weights are key components of the “modified HHI delta” measure used in empirical studies of common ownership, such as Azar et al. (2018). [^12]
<!-- para 15 -->
To derive our fund-level measure, we first consider how a specific fund p contributes to the profit weight between firms.
By decomposing the numerator in equation (1), we define the pairwise profit weight $\kappa_{p,m,n}$ specific to fund p as (2)
<!-- para 16 -->
$$ \kappa_{p,m,n}=\frac{\beta_{p,m}\beta_{p,n}}{\sum_{\forall s}\beta_{s,m}^{2}}. $$
<!-- para 17 -->
This measures the value to focal firm m of a dollar of profit generated for competitor firm n, specifically attributable to fund p's common ownership.
Building on this, we calculate the aggregate value to firm m of profits generated by all its competitors, attributable to fund p: (3)
<!-- para 18 -->
$$ \kappa_{p,m}=\frac{\sum_{\forall n\neq m}\beta_{p,m}\beta_{p,n}}{\sum_{\forall s}\beta_{s,m}^{2}}. $$
<!-- para 19 -->
Specifically, the numerator of $\kappa_{p,m}$ represents the inner product of fund $p$'s common ownership in focal firm $m$ ( $\beta_{p,m}$) and competitors $n$ ( $\beta_{p,n}$), with competitors identified using Hoberg–Phillips TNIC data (Hoberg and Phillips (2016)). [^13] As a scalar, the denominator represents firm $m$'s ownership concentration based on all available ownership data sourced from 13F filings, 13D filings, 13G filings, and other public reports, not just fund $p$'s ownership. [^14]
<!-- para 20 -->
Finally, we define our fund-level common ownership measure, $CO_{p}$, by aggregating $\kappa_{p,m}$ across all portfolio firms held by fund p: (4)
<!-- para 21 -->
$$ CO_{p}=\sum_{m}w_{p,m}\kappa_{p,m}, $$
<!-- para 22 -->
where $w_{p,m}$ represents the proportion of fund $p$'s total portfolio value invested in firm $m$, calculated as the product of the firm's stock price and the number of shares held by the fund, divided by the fund's total investment value at each quarter-end.
<!-- para 23 -->
$CO_{p}$ measures the extent of common ownership within fund p's portfolio and can be interpreted as the portfolio-weighted average value, specific to fund p, of a dollar of profits accruing to competitors relative to a dollar of profits for the focal portfolio firms themselves.
The intuition is that as common ownership increases, portfolio firms may have an incentive to reduce competition and thus potentially gain larger profits, of which common owners receive a proportion. [^15] $CO_{p}$ not only measures the consideration for profits of competing firms but also the fund’s ability and incentive to influence the policies of firm m.
Since $CO_{p}$ depends critically on portfolio weights, we consider it part of a fund’s investment strategy. [^16]
<!-- para 24 -->
Our definition of fund common owners requires fund p to hold both firm m and its competitor n to make $\sum_{\forall n \neq m} \beta_{p,m} \beta_{p,n}$ in $CO_p$ nonzero. [^17] If fund p only holds firm m without holding its competitor n, then the incentive and the ability to facilitate coordination between firm m and n would be low.
Even if a fund obtains outperformance by holding only one side of a pair of competitors, it is possible that fund p simply picks stocks and free-rides on other funds holding both firms m and n.
Therefore, our empirical analyses will seek to disentangle these effects in Section III.D.
In the following analyses, CO refers to $CO_p$ from equation (4).
<!-- para 25 -->
The connection between our fund-level CO and industry-level common ownership (e.g., MHHI delta) has important empirical implications.
If fund-level CO is merely capturing idiosyncratic fund characteristics unrelated to broader competitive effects, we would not expect the relationship between fund CO and fund performance to vary with industry-level common ownership concentration.
However, if fund CO is capturing a fund's participation in potentially anticompetitive ownership structures, then the performance benefits should be more pronounced in industries with high common ownership concentration.
We test this prediction in Section III.C by examining how our fund-level CO effects vary with industry-level MHHI delta.
We acknowledge that our fund-level measure captures only a single fund's contribution to the overall common ownership structure rather than the complete industry-level common ownership central to theories of anticompetitive effects.
However, this approach allows us to directly examine which funds benefit from common ownership positions and how these benefits relate to broader industry structures, thereby addressing a key premise in the common ownership hypothesis.
<!-- para 27 -->
We construct our sample by merging fund characteristics, stockholdings, stock characteristics, and fund voting data from different databases.
In our analyses, we use observations from three levels: i) fund-by-month observations to study returns and fund characteristics, ii) fund-by-year observations to study fees and active monitoring activities, and iii) fund- (or fund-family-)by-proposal to study voting behavior on specific proposals.
<!-- para 28 -->
We obtain the fund names, monthly returns, monthly total net assets (TNA), investment objectives, and other fund characteristics from the CRSP Survivorship Bias-Free Mutual Fund Database.
Following Huang, Sialm, and Zhang (2011), we identify actively managed U.S. equity mutual funds based on their objective codes and their disclosed asset compositions. [^18] Because data coverage on the monthly TNA and quarterly portfolio holdings before 1999 is limited and of poor quality, our sample period spans from January 1999 to December 2018.
We restrict to funds domiciled in the United States, and exclude money market funds, index funds, fixed income funds, and funds that manage less than 5 million in the previous month and those whose total equity holding in dollar value (calculated from the mutual fund holding data discussed below) is less than 5 million in a quarter.
For funds with multiple share classes, we calculate the weighted average monthly fund returns by the weights of share class TNA.
<!-- para 29 -->
We obtain mutual funds’ portfolio holdings from the Thomson Reuters Mutual Fund Holdings Database (S12) and the CRSP Mutual Fund Holdings Database.
Recent studies show that the Thomson stockholdings data have problems with missing new funds after 2008, while CRSP portfolio holdings data are “inaccurate prior to the fourth quarter of 2007” (Schwarz and Potter (2016), Zhu (2020)).
To circumvent data quality problems, we consolidate the Thomson stockholdings data before the second quarter of 2010 with the CRSP stockholdings data on and after that quarter. [^19] Beyond mutual funds’ holding data, we also consolidate comprehensive ownership data containing both institutional and individual owners, using all available 13-F filings, 13-D filings, 13-G filings, and other publicly reported ownership.
We only keep firms with a minimum of 10% available aggregated ownership to circumvent the problem of missing ownership information, although our results remain robust without this restriction. [^20] To tackle asynchronicities in
<!-- para 30 -->
reported holdings, we keep the stockholdings reported at each quarter-end.
For those who did not report at the quarter-end, we use their most recent holding positions before each quarter-end.
To the best of our knowledge, this is one of the most comprehensive ownership data used for calculating common ownership. [^21] To identify firm competitors, we use the Hoberg–Phillips TNIC data that provide pairwise competition linkages based on textual analysis of firms’ product information (Hoberg and Phillips (2016)). [^22] In a robustness check, we use the Fama–French 12 Industry Classification to identify industry peers.
<!-- para 31 -->
At the stock level, we obtain stock fundamentals data from the CRSP–Compustat Merged database.
The returns of the Fama–French 5 factors and the momentum factor are sourced from Kenneth French's website.
The factor returns of the q-factor model are from the Hou–Xue–Zhang q-factors data library.
We study common stock held by mutual funds listed on the NYSE, Nasdaq, or AMEX stock exchanges.
We restrict our sample to stocks with non-missing information on month-end prices, monthly returns, 4-digit SIC industry code, and annual net sales.
Stock prices, returns, and the number of outstanding shares are sourced from CRSP.
Firm fundamentals data, such as firm sales, come from Compustat.
<!-- para 32 -->
For the fund voting analysis, we obtain fund voting data from the ISS Voting Analytics data set that includes all management and shareholder proposals for public companies in their proxy statements since 2003.
For each proposal, the data set contains the information on the short description of the proposal, the type of proposal categorized using ISS's system (ISSAgendaItemID), management and ISS recommendation, and mutual fund votes for the proposal—vote for, against, abstaining, and withholding.
We follow Peter Iliev's note to link mutual funds between ISS and CRSP and then to Thomson Reuters (see https://bpb-us-e1.wpmucdn.com/sites.psu.edu/dist/b/169215/files/2023/08/voting-link-note-v2.pdf).
A total of 3,121 funds in ISS are identified during the 2003–2018 period.
Because this study focuses on the proposals potentially related to competition, we keep the proposals on stock or stock option plans and elections of directors. [^23]
<!-- para 33 -->
Consolidating the above data sets results in a final sample that includes 6,681 actively managed equity funds with 379,806 fund-month observations.
Since we consolidate the CRSP and Thomson Reuters mutual fund data sets, 3,351 unique funds are identified in the CRSP sample and 3,332 in the TR sample.
Often, a fund has two separate identifiers, one in each subsample.
Table 1 reports summary statistics on CO and other fund characteristics commonly used in the mutual fund literature.
All variables are defined in the Appendix.
<!-- para 35 -->
*Table 1 presents summary statistics for mutual fund characteristics and the fund-level common ownership measure.
For each variable, we report the mean, standard deviation, and the 25th, 50th (median), and 75th percentiles.
The sample contains 379,806 fund-month observations, except for the rolling estimates of Fama–French 6-factor alphas, which have 330,588 observations due to the estimation window requirement.
All variables are defined in the Appendix*
<!-- para 36 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td></td><td>Mean</td><td>Std.
Dev.</td><td>25th</td><td>50th</td><td>75th</td></tr><tr><td>TOTAL_NET_ASSETS (TNA, $M)</td><td>1,155.612</td><td>2,681.423</td><td>77.400</td><td>266.900</td><td>922.675</td></tr><tr><td>FUND_RETURN (Monthly, %)</td><td>0.710</td><td>4.644</td><td>-1.673</td><td>1.077</td><td>3.475</td></tr><tr><td>6_FACTOR_ALPHA (Monthly, %)</td><td>-0.099</td><td>3.543</td><td>-0.972</td><td>-0.124</td><td>0.731</td></tr><tr><td>FUND_AGE (Years)</td><td>14.561</td><td>12.492</td><td>6.041</td><td>11.921</td><td>18.764</td></tr><tr><td>FUND_FLOWS (Monthly, %)</td><td>0.089</td><td>4.819</td><td>-1.457</td><td>-0.495</td><td>0.740</td></tr><tr><td>EXPENSE_RATIO (Annual, %)</td><td>1.041</td><td>0.571</td><td>0.807</td><td>1.100</td><td>1.390</td></tr><tr><td>MANAGEMENT_FEE (Annual, %)</td><td>0.606</td><td>0.385</td><td>0.431</td><td>0.684</td><td>0.851</td></tr><tr><td>TURNOVER_RATIO (Annual, %)</td><td>67.995</td><td>73.272</td><td>19.980</td><td>49.000</td><td>91.000</td></tr><tr><td>NUMBER_OF_STOCKS_HELD</td><td>100.709</td><td>152.469</td><td>43.000</td><td>65.000</td><td>101.000</td></tr><tr><td>PORTFOLIO_INDUSTRY_CONCENTRATION (PIC, Log)</td><td>5.970</td><td>1.232</td><td>5.324</td><td>5.902</td><td>6.481</td></tr><tr><td>RETURN_VOLATILITY (Quarterly, %)</td><td>8.968</td><td>6.625</td><td>5.752</td><td>7.494</td><td>10.273</td></tr><tr><td>IDIOSYNCRATIC_VOLATILITY (Quarterly, %)</td><td>2.366</td><td>4.537</td><td>1.344</td><td>1.864</td><td>2.751</td></tr><tr><td>CO (Quarterly, %)</td><td>0.226</td><td>0.937</td><td>0.000</td><td>0.002</td><td>0.029</td></tr></table>
</div>
<!-- para 38 -->
This section first describes mutual funds' common ownership (CO) characteristics and then studies the relationship between CO and fund returns.
We then address alternative explanations and potential confounders of the results.
<!-- para 40 -->
We observe a substantial variation in fund CO across U.S. actively managed equity mutual funds.
The maximum CO is 7.12% after winsorization at the 99th percentile, with a mean of 0.22% and a standard deviation of 0.94%.
Table 2 presents some of the top CO funds across different years in our sample. [^24]
<!-- para 41 -->
CO is a persistent characteristic of mutual funds: it has an autocorrelation of 0.809, driven by the extreme deciles of CO (see Supplementary Material Table B1).
The table also reports that a fund in the lowest decile of CO in a quarter is over 87% likely to stay in the same decile in the next quarter.
In contrast, those in the top decile are over 91% likely to stay in the same decile quarterly.
Other deciles are slightly less absorbing, with between 60% and 78% likely to stay in the same decile.
For example, the CO measure for Hodges Capital Small Intrinsic Value Fund, quoted in the introduction of this article, moved from below the 50th percentile in 2014 to above the 80th percentile in 2018.
This allocation is consistent with the portfolio construction methodology on Hodges Capital's site, which states that their managers may “concentrate the number of holdings in the portfolio within a certain sector during a sector pullback” (see https://hodgescapital.com/process as of July 20).
<!-- para 42 -->
We further study the factor exposures of funds with varying levels of CO.
We sort funds into decile portfolios based on their CO measure in the previous quarter
<!-- para 44 -->
*Table 2 presents the top 5 CO funds selected based on the CO measure as of the end of years 2000, 2005, 2010, 2015, and 2018.
The funds' CO (%), management fee (%), expense ratio (%), and TNA ($billion) are measured as of the end of each year*
<!-- para 45 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td>Year</td><td>Asset Manager: Fund Name</td><td>CO (%)</td><td>Management Fee (%)</td><td>Expense Ratio (%)</td><td>Fund TNA ($B)</td></tr><tr><td rowspan="5">2000</td><td>Seligman Communications and Information Fund, Inc.</td><td>0.837</td><td>0.822</td><td>1.621</td><td>6.537</td></tr><tr><td>Franklin Strategic Series: Franklin Small Cap Growth Fund</td><td>0.638</td><td>0.448</td><td>0.939</td><td>12.851</td></tr><tr><td>Firsthand Funds: The Technology Value Fund</td><td>0.622</td><td>1.824</td><td>1.830</td><td>3.301</td></tr><tr><td>The Munder Funds, Inc.: NetNet Fund</td><td>0.538</td><td>1.097</td><td>2.335</td><td>3.664</td></tr><tr><td>Franklin Strategic Series: Franklin Biotechnology Discovery Fund</td><td>0.398</td><td>0.560</td><td>1.090</td><td>1.342</td></tr><tr><td rowspan="5">2005</td><td>Fidelity Puritan Trust: Fidelity Low-Priced Stock Fund</td><td>0.704</td><td>0.676</td><td>0.880</td><td>36.721</td></tr><tr><td>HomeState Group: Emerald Select Banking &amp; Finance Fund</td><td>0.588</td><td>1.094</td><td>1.815</td><td>0.297</td></tr><tr><td>FBR Funds: FBR Small Cap Financial Fund</td><td>0.512</td><td>0.960</td><td>1.460</td><td>0.432</td></tr><tr><td>Fidelity Mt Vernon Street Trust: Fidelity Growth Company Fund</td><td>0.366</td><td>0.730</td><td>0.970</td><td>27.415</td></tr><tr><td>John Hancock Investment Trust II: John Hancock Regional Bank Fund</td><td>0.360</td><td>0.754</td><td>1.427</td><td>2.114</td></tr><tr><td rowspan="4">2010</td><td>Fidelity Mt Vernon Street Trust: Fidelity Growth Company Fund</td><td>0.499</td><td>0.637</td><td>0.807</td><td>37.341</td></tr><tr><td>Federated Equity Funds: Federated Kaufmann Fund</td><td>0.309</td><td>1.351</td><td>2.037</td><td>7.486</td></tr><tr><td>John Hancock Investment Trust II: John Hancock Regional Bank Fund</td><td>0.230</td><td>0.790</td><td>1.427</td><td>0.677</td></tr><tr><td>Fidelity Select Portfolios: Biotechnology Portfolio Growth Fund of America, Inc.</td><td>0.143</td><td>0.560</td><td>0.870</td><td>1.038</td></tr><tr><td rowspan="4">2015</td><td>Fidelity Select Portfolios: Biotechnology Portfolio</td><td>0.139</td><td>0.271</td><td>0.727</td><td>161.799</td></tr><tr><td>John Hancock Investment Trust II: John Hancock Regional Bank Fund</td><td>2.683</td><td>0.548</td><td>0.730</td><td>14.942</td></tr><tr><td>Fidelity Advisor Series VII: Fidelity Advisor Biotechnology Fund</td><td>0.326</td><td>0.774</td><td>1.363</td><td>0.833</td></tr><tr><td>Federated Equity Funds: Federated Kaufmann Fund</td><td>0.196</td><td>0.548</td><td>1.148</td><td>3.781</td></tr><tr><td rowspan="6">2018</td><td>T Rowe Price Small-Cap Value Fund, Inc.</td><td>0.141</td><td>1.352</td><td>1.999</td><td>5.513</td></tr><tr><td>Fidelity Select Portfolios: Biotechnology Portfolio</td><td>0.136</td><td>0.637</td><td>0.819</td><td>7.204</td></tr><tr><td>John Hancock Investment Trust II: John Hancock Regional Bank Fund</td><td>1.422</td><td>0.542</td><td>0.720</td><td>6.512</td></tr><tr><td>T Rowe Price Small-Cap Value Fund, Inc.</td><td>0.334</td><td>0.748</td><td>1.377</td><td>1.113</td></tr><tr><td>Federated Equity Funds: Federated Kaufmann Fund</td><td>0.221</td><td>0.640</td><td>0.760</td><td>8.523</td></tr><tr><td>PRIMECAP Odyssey Funds: PRIMECAP Odyssey Aggressive Growth Fund</td><td>0.127</td><td>0.000</td><td>0.000</td><td>5.529</td></tr><tr><td>0.119</td><td>0.000</td><td>0.000</td><td>0.000</td><td>9.204</td></tr></table>
</div>
<!-- para 46 -->
and then compute the value-weighted monthly returns for each decile portfolio, as well as the high-minus-low (HML) portfolio formed by buying high-CO portfolios and selling the low-CO portfolios.
Table 3 reports the Fama–French 6-factor (Fama and French (2015) with momentum) loadings of different CO decile portfolios.
We find that funds with higher CO tend to have higher loadings on the size factor, with the loading on the high-minus-low CO decile portfolio reaching 0.173 (t-stat >5). [^25] For these funds, we also observe a slight but statistically insignificant (at the 5% level) tilt toward value stocks and low profitability firms.
These style characteristics—the size tilt, value orientation, and focus on firms with potential for profitability improvement—align with patterns documented in the activist investor literature.
<!-- para 48 -->
*Table 3 reports the factor loadings in the Fama–French 6-factor model for each decile fund portfolio sorted by fund CO.
The factor loadings of the HML portfolios formed by buying the high-CO portfolios and selling the low-CO portfolios are reported in the bottom row.
All t-statistics of the estimated factor loadings are Newey–West-corrected with up to 3-month lags and reported in parentheses*
<!-- para 49 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table><tr><td>CO Bin</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mi>M</mi></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mi>M</mi></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mrow><mi>S</mi><mi>M</mi><mi>B</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mrow><mi>S</mi><mi>M</mi><mi>B</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mrow><mi>H</mi><mi>M</mi><mi>L</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mrow><mi>H</mi><mi>M</mi><mi>L</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mrow><mi>R</mi><mi>M</mi><mi>V</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mrow><mi>R</mi><mi>M</mi><mi>V</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mrow><mi>C</mi><mi>M</mi><mi>A</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mrow><mi>C</mi><mi>M</mi><mi>A</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B2;</mi><mrow><mi>J</mi><mi>M</mi><mi>D</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>&#x003B2;</mi><mrow><mi>J</mi><mi>M</mi><mi>D</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td></tr><tr><td>Low</td><td>0.960</td><td>(67.823)</td><td>-0.060</td><td>(-3.177)</td><td>-0.035</td><td>(-1.806)</td><td>0.066</td><td>(2.962)</td><td>0.039</td><td>(1.320)</td><td>-0.012</td><td>(-0.995)</td></tr><tr><td>2</td><td>0.972</td><td>(73.572)</td><td>-0.066</td><td>(-4.299)</td><td>0.000</td><td>(0.027)</td><td>0.060</td><td>(3.198)</td><td>-0.027</td><td>(-1.252)</td><td>-0.007</td><td>(-0.647)</td></tr><tr><td>3</td><td>0.984</td><td>(84.839)</td><td>-0.045</td><td>(-2.699)</td><td>-0.007</td><td>(-0.314)</td><td>0.063</td><td>(3.727)</td><td>-0.030</td><td>(-1.326)</td><td>0.003</td><td>(0.225)</td></tr><tr><td>4</td><td>0.982</td><td>(73.761)</td><td>-0.012</td><td>(-0.713)</td><td>-0.021</td><td>(-0.911)</td><td>0.061</td><td>(3.056)</td><td>-0.012</td><td>(-0.427)</td><td>0.006</td><td>(0.587)</td></tr><tr><td>5</td><td>1.002</td><td>(57.699)</td><td>0.068</td><td>(0.864)</td><td>-0.042</td><td>(-1.406)</td><td>0.105</td><td>(1.530)</td><td>0.066</td><td>(0.908)</td><td>0.030</td><td>(1.775)</td></tr><tr><td>6</td><td>0.997</td><td>(44.115)</td><td>0.004</td><td>(0.221)</td><td>-0.012</td><td>(-0.386)</td><td>0.052</td><td>(2.435)</td><td>0.013</td><td>(0.388)</td><td>0.006</td><td>(0.338)</td></tr><tr><td>7</td><td>1.003</td><td>(55.869)</td><td>0.021</td><td>(1.603)</td><td>-0.006</td><td>(-0.212)</td><td>0.022</td><td>(1.205)</td><td>0.013</td><td>(0.474)</td><td>0.017</td><td>(0.896)</td></tr><tr><td>8</td><td>1.006</td><td>(54.779)</td><td>0.046</td><td>(2.044)</td><td>-0.019</td><td>(-0.627)</td><td>0.001</td><td>(0.035)</td><td>-0.014</td><td>(-0.406)</td><td>0.001</td><td>(0.059)</td></tr><tr><td>9</td><td>0.976</td><td>(49.125)</td><td>0.099</td><td>(4.296)</td><td>-0.027</td><td>(-0.850)</td><td>-0.069</td><td>(-1.995)</td><td>0.019</td><td>(0.444)</td><td>0.020</td><td>(1.070)</td></tr><tr><td>High</td><td>0.964</td><td>(43.151)</td><td>0.114</td><td>(3.784)</td><td>-0.007</td><td>(-0.244)</td><td>-0.020</td><td>(-0.367)</td><td>0.007</td><td>(0.135)</td><td>-0.007</td><td>(-0.716)</td></tr><tr><td>HML</td><td>0.004</td><td>(0.206)</td><td>0.173</td><td>(5.152)</td><td>0.028</td><td>(0.979)</td><td>-0.085</td><td>(-1.835)</td><td>-0.032</td><td>(-0.732)</td><td>0.005</td><td>(0.373)</td></tr></table>
</div>
<!-- para 50 -->
Brav, Jiang, Kim et al. (2010) and Brav, Jiang, and Kim (2015) show that activist investors typically target smaller firms with lower valuations where they can more effectively influence corporate policies and enhance profitability.
<!-- para 51 -->
Although CO is defined based on competitors in the same industry classification, it is not primarily driven by funds specializing in a particular industry.
For example, the correlation between Kacperczyk et al.'s (2005) portfolio industry concentration (PIC) measure and CO is 0.12.
Removing sector funds from our analyses does not qualitatively alter the summary statistics and empirical results.
Therefore, although funds may not allocate their portfolios to hit a particular value of CO, funds' common ownership position is a persistent and unique fund characteristic that is not accounted for in traditional factor exposures or standard measures of portfolio industry concentration.
<!-- para 54 -->
To evaluate fund performance, we use both risk- and benchmark-adjusted return measures.
The former uses the 6-factor (Fama and French (2015) with momentum), Ferson and Schadt (1996), Pastor and Stambaugh (2003), and q-5-factor (Hou, Mo, Xue, and Zhang (2021)) models to calculate alpha.
For example, the Fama–French 6-factor alpha is the intercept from the following time-series regression: (5)
<!-- para 55 -->
$$ \begin{align*}r_{p,t}-r_{t}^{f}=&\alpha_{p}+\beta^{M}\Big(r_{t}^{M}-r_{t}^{f}\Big)+\beta^{S}SMB_{t}+\beta^{H}HML_{t}+\beta^{R}RMW_{t}\\&+\beta^{C}CMA_{t}+\beta^{U}UMD_{t}+\varepsilon_{p,t},\end{align*} $$
<!-- para 56 -->
where $r_{p,t}$ is the return in month $t$ for fund portfolio $p$, $r_t^f$ is the Treasury-bill rate in month $t$, $r_t^M$ is the value-weighted stock market return in month $t$, and $SMB_t$, $HML_t$, $RMW_t$, $CMA_t$, and $UMD_t$ correspond to the Fama–French size, value, profitability, investment, and momentum factors, respectively. [^26] Using the Morningstar benchmark data, we calculate the benchmark-adjusted returns as (6)
<!-- para 57 -->
$$ \alpha_{p}^{B M}=r_{p,t}-r_{t}^{B M(p)}, $$
<!-- para 58 -->
where the indices follow from equation (5) and $r_t^{BM(p)}$ is the return of the benchmark identified by Morningstar for fund portfolio $p$.
For all these analyses, standard errors are Newey–West-corrected up to 3 lags, allowing for autocorrelation in returns for up to 3 months.
<!-- para 59 -->
At the beginning of each quarter, we sort decile portfolios based on their most recent quarterly CO measures.
We then compute the value-weighted risk- and benchmark-adjusted monthly fund returns in the next quarter using the aforementioned models.
Table 4 reports the results of portfolio sorting.
<!-- para 60 -->
Panel A of Table 4 reports that U.S. actively managed equity mutual funds with a larger degree of common ownership exhibit better gross performance.
The adjusted returns of funds in the top decile of CO are 1.08%–1.92% per annum (9–16 BPS per month) greater than those in the bottom decile of CO.
Although the volatility of portfolio returns is higher, the overall annualized Sharpe ratio of high-CO funds is also 0.11 higher than those with low CO.
Panel B documents that the higher gross returns also appear to flow through to higher net-of-fee returns.
To visualize the performance history, Figure 1 shows the cumulative returns of the CO portfolios throughout our sample period.
<!-- para 62 -->
*Table 4 presents the performance of decile fund portfolios sorted by fund CO.
The portfolios are value-weighted by fund TNA, rebalanced at the end of each quarter, and held for 1 quarter.
The HML is the long-short portfolio formed by buying the high-CO decile portfolio and selling the low one.
All portfolio returns and return volatility are represented in percentages at a monthly rate.
Panel A reports the portfolio sorting results for the gross returns, whereas Panel B reports the net-of-expenses returns.
All t-statistics are Newey-West-corrected with up to 3-month lags*
<!-- para 63 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table><tr><td>COBin</td><td>Sharpe</td><td>SD</td><td>r</td><td>t(r)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>a</mi><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>a</mi><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>a</mi><mrow><mi>F</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>a</mi><mrow><mi>F</mi><mi>S</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>a</mi><mrow><mi>P</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>a</mi><mrow><mi>P</mi><mi>S</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>a</mi><mrow><mi>Q</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>a</mi><mrow><mi>Q</mi><mi>S</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>a</mi><mrow><mi>B</mi><mi>M</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msup><mi>a</mi><mrow><mi>B</mi><mi>M</mi></mrow></msup><mo stretchy="false">&#x00029;</mo></mrow></math></td></tr><tr><td colspan="15">Panel A.
Gross Returns</td></tr><tr><td>Low</td><td>0.328</td><td>4.078</td><td>0.378</td><td>(1.298)</td><td>-0.051</td><td>(-1.138)</td><td>-0.027</td><td>(-0.624)</td><td>-0.023</td><td>(-0.439)</td><td>-0.062</td><td>(-1.501)</td><td>0.002</td><td>(0.050)</td></tr><tr><td>2</td><td>0.338</td><td>4.135</td><td>0.395</td><td>(1.345)</td><td>-0.025</td><td>(-0.654)</td><td>0.015</td><td>(-0.369)</td><td>-0.014</td><td>(-0.317)</td><td>-0.044</td><td>(-1.271)</td><td>0.013</td><td>(0.400)</td></tr><tr><td>3</td><td>0.347</td><td>4.188</td><td>0.410</td><td>(1.375)</td><td>-0.025</td><td>(-0.639)</td><td>-0.025</td><td>(-0.617)</td><td>-0.012</td><td>(-0.246)</td><td>-0.054</td><td>(-1.452)</td><td>0.042</td><td>(1.047)</td></tr><tr><td>4</td><td>0.344</td><td>4.196</td><td>0.407</td><td>(1.347)</td><td>-0.041</td><td>(-1.004)</td><td>-0.044</td><td>(-1.147)</td><td>-0.021</td><td>(-0.462)</td><td>-0.054</td><td>(-1.450)</td><td>0.031</td><td>(0.748)</td></tr><tr><td>5</td><td>0.415</td><td>4.389</td><td>0.512</td><td>(1.667)</td><td>-0.011</td><td>(-0.222)</td><td>-0.009</td><td>(-0.195)</td><td>0.033</td><td>(0.474)</td><td>-0.037</td><td>(-0.777)</td><td>0.143</td><td>(1.454)</td></tr><tr><td>6</td><td>0.388</td><td>4.281</td><td>0.467</td><td>(1.506)</td><td>0.002</td><td>(0.039)</td><td>0.008</td><td>(-0.168)</td><td>0.011</td><td>(0.193)</td><td>-0.018</td><td>(-0.343)</td><td>0.093</td><td>(2.001)</td></tr><tr><td>7</td><td>0.360</td><td>4.329</td><td>0.439</td><td>(1.411)</td><td>-0.030</td><td>(-0.661)</td><td>-0.039</td><td>(-1.058)</td><td>-0.031</td><td>(-0.695)</td><td>-0.029</td><td>(-0.716)</td><td>0.053</td><td>(1.171)</td></tr><tr><td>8</td><td>0.395</td><td>4.471</td><td>0.496</td><td>(1.561)</td><td>0.038</td><td>(0.720)</td><td>0.032</td><td>(0.603)</td><td>0.025</td><td>(0.425)</td><td>0.040</td><td>(0.911)</td><td>0.132</td><td>(2.436)</td></tr><tr><td>9</td><td>0.408</td><td>4.451</td><td>0.510</td><td>(1.594)</td><td>0.055</td><td>(1.138)</td><td>0.027</td><td>(0.722)</td><td>0.021</td><td>(0.496)</td><td>0.052</td><td>(1.115)</td><td>0.124</td><td>(1.847)</td></tr><tr><td>High</td><td>0.444</td><td>4.398</td><td>0.547</td><td>(1.731)</td><td>0.086</td><td>(1.787)</td><td>0.068</td><td>(1.368)</td><td>0.063</td><td>(1.111)</td><td>0.058</td><td>(1.284)</td><td>0.164</td><td>(2.287)</td></tr><tr><td>HML</td><td>0.563</td><td>1.047</td><td>0.169</td><td>(2.932)</td><td>0.138</td><td>(3.406)</td><td>0.096</td><td>(1.904)</td><td>0.086</td><td>(1.839)</td><td>0.120</td><td>(3.085)</td><td>0.162</td><td>(2.897)</td></tr><tr><td colspan="15">Panel B.
Net-of-Expenses Returns</td></tr><tr><td>Low</td><td>0.256</td><td>4.080</td><td>0.296</td><td>(1.016)</td><td>-0.133</td><td>(-2.959)</td><td>-0.110</td><td>(-2.540)</td><td>-0.104</td><td>(-2.032)</td><td>-0.143</td><td>(-3.473)</td><td>-0.080</td><td>(-2.088)</td></tr><tr><td>2</td><td>0.270</td><td>4.141</td><td>0.317</td><td>(1.077)</td><td>-0.103</td><td>(-2.670)</td><td>-0.093</td><td>(-2.370)</td><td>-0.092</td><td>(-2.094)</td><td>-0.121</td><td>(-3.496)</td><td>-0.064</td><td>(-1.947)</td></tr><tr><td>3</td><td>0.282</td><td>4.191</td><td>0.335</td><td>(1.122)</td><td>-0.099</td><td>(-2.554)</td><td>-0.100</td><td>(-2.516)</td><td>-0.085</td><td>(-1.838)</td><td>-0.128</td><td>(-3.472)</td><td>-0.033</td><td>(-0.851)</td></tr><tr><td>4</td><td>0.280</td><td>4.199</td><td>0.333</td><td>(1.100)</td><td>-0.114</td><td>(-2.806)</td><td>-0.118</td><td>(-3.086)</td><td>-0.094</td><td>(-2.092)</td><td>-0.127</td><td>(-3.386)</td><td>-0.043</td><td>(-1.061)</td></tr><tr><td>5</td><td>0.355</td><td>4.392</td><td>0.439</td><td>(1.427)</td><td>-0.083</td><td>(-1.641)</td><td>-0.082</td><td>(-1.778)</td><td>-0.039</td><td>(-0.571)</td><td>-0.109</td><td>(-2.294)</td><td>0.070</td><td>(0.721)</td></tr><tr><td>6</td><td>0.324</td><td>4.284</td><td>0.392</td><td>(1.261)</td><td>-0.073</td><td>(-1.290)</td><td>-0.083</td><td>(-1.781)</td><td>-0.064</td><td>(-1.125)</td><td>-0.092</td><td>(-1.815)</td><td>0.018</td><td>(0.385)</td></tr><tr><td>7</td><td>0.295</td><td>4.332</td><td>0.362</td><td>(1.161)</td><td>-0.106</td><td>(-2.378)</td><td>-0.116</td><td>(-3.151)</td><td>-0.108</td><td>(-2.377)</td><td>-0.106</td><td>(-2.584)</td><td>-0.024</td><td>(-0.551)</td></tr><tr><td>8</td><td>0.330</td><td>4.474</td><td>0.416</td><td>(1.307)</td><td>-0.041</td><td>(-0.776)</td><td>-0.048</td><td>(-0.915)</td><td>-0.054</td><td>(-0.918)</td><td>-0.040</td><td>(-0.910)</td><td>0.052</td><td>(0.976)</td></tr><tr><td>9</td><td>0.342</td><td>4.453</td><td>0.429</td><td>(1.339)</td><td>-0.025</td><td>(-0.513)</td><td>-0.054</td><td>(-1.459)</td><td>-0.059</td><td>(-1.390)</td><td>-0.028</td><td>(-0.597)</td><td>0.043</td><td>(0.650)</td></tr><tr><td>High</td><td>0.385</td><td>4.399</td><td>0.476</td><td>(1.505)</td><td>0.016</td><td>(0.339)</td><td>-0.002</td><td>(-0.050)</td><td>-0.007</td><td>(-0.128)</td><td>-0.012</td><td>(-0.272)</td><td>0.093</td><td>(1.311)</td></tr><tr><td>HML</td><td>0.601</td><td>1.047</td><td>0.180</td><td>(3.127)</td><td>0.149</td><td>(3.677)</td><td>0.107</td><td>(2.127)</td><td>0.097</td><td>(2.077)</td><td>0.131</td><td>(3.362)</td><td>0.174</td><td>(3.095)</td></tr></table>
</div>
<!-- para 65 -->
*Figure 1 presents the cumulative returns of top and bottom decile fund portfolios formed based on funds' common ownership (CO, as defined in Section II.B).
The portfolios are value-weighted by fund TNA, rebalanced at the end of each quarter, and held for one quarter.
The HML is the long-short portfolio formed by buying the high-CO decile portfolio and selling the low one.
Graph A shows the cumulative raw returns of the high-CO (green line) and low-CO (red line) portfolios from 1999 to 2018.
Graph B shows the cumulative raw returns for the HML portfolio over the same period*
<!-- para 66 -->
**Panel A.** Cumulative returns of high and low CO portfolios
<!-- para 68 -->
**Panel B.** Cumulative returns of high-minus-low portfolios
<!-- para 70 -->
For robustness, we consider three alternative measures of funds’ common ownership, all detailed in the Supplementary Material.
We continue to find a positive relationship between active funds’ performance and their common ownership positions. [^27]
<!-- para 72 -->
In this analysis, we use Fama–MacBeth regression specifications that control for mutual fund characteristics that may be associated with fund performance using the following specification: (7)
<!-- para 73 -->
$$ r_{p,t}=a+\beta C O_{p,t-1}+c Z_{p,t-1}+\eta_{p,t}, $$
<!-- para 74 -->
where $CO_{p,t-1}$ is the measure of common ownership of fund p in the previous quarter-end, $Z_{p,t-1}$ is a matrix of fund control variables, including lagged 1-month log TNA, lagged 1-year expense (EXPENSE_RATIO), lagged 1-year turnover (TURNOVER_RATIO), lagged 1-month flows (FUND_FLOW), lagged 1-year age (FUND_AGE), and lagged 1-month net-of-fee raw returns (FUND_RETURN).
The dependent variable $r_{p,t}$ is either funds' monthly gross or net-of-fee raw returns, Fama–French 6-factor alpha, Ferson and Schadt (1996) alpha, Pastor and Stambaugh (2003) alpha, q-factor alpha, or benchmark-adjusted return.
The alphas are the difference between actual and expected fund returns, with factor loadings being estimated based on rolling 36-month regressions. [^28]
<!-- para 75 -->
Panel A of Table 5 reports the Fama–MacBeth regression results for gross returns, and Panel B reports the results for net-of-fee returns.
Across all specifications in both panels, fund performance is statistically significantly positively associated with CO after controlling for standard fund characteristics.
In terms of economic magnitude, moving from funds in the lowest 10th percentile of the CO distribution to the top 90th percentile of CO (equivalent to a 3.8-standard-deviation increase in CO) is associated with a 9-basis-point (2.364 × 3.8) increase in monthly Fama–French 6-factor net-of-expenses alpha in column 2 of Panel B.
The improvement in alpha is meaningful, given that the average net-of-fee alpha is negative 10 BPS monthly. [^29] As additional robustness, we consider panel regressions in Supplementary Material Table B4 with year-month fixed effects and standard errors clustered at the fund and year levels.
We find quantitatively and qualitatively similar results.
<!-- para 77 -->
*Table 5 reports the results of the Fama–MacBeth cross-sectional regressions.
The dependent variables are funds' monthly raw returns, estimated Fama–French 6-factor alpha, Ferson–Schadt alpha, Pastor–Stambaugh alpha, q-factor alpha, or benchmark-adjusted returns, all represented as monthly returns in percentages.
Returns are measured before expenses in Panel A and after expenses in Panel B, represented as a percentage.
The main independent variable is the fund's common ownership (CO) measured in the previous quarter-end.
The control variables are lagged 1-month log TNA, lagged 1-year EXPENSE_RATIO, lagged 1-year TURNOVER_RATIO, lagged 1-month FUND_FLOW, lagged 1-year FUND_AGE, and lagged 1-month FUND_RETURN.
All independent variables are winsorized at the 1% and 99% levels. ***, **, and * denote statistical significance at the 1%, 5%, and 10% levels, respectively*
<!-- para 78 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td rowspan="2"></td><td>r</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mover><mrow><mi>&#x003B1;</mi></mrow><mo>&#x0005E;</mo></mover></mrow><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mover><mrow><mi>&#x003B1;</mi></mrow><mo>&#x0005E;</mo></mover></mrow><mrow><mi>F</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mover><mrow><mi>&#x003B1;</mi></mrow><mo>&#x0005E;</mo></mover></mrow><mrow><mi>P</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mover><mrow><mi>&#x003B1;</mi></mrow><mo>&#x0005E;</mo></mover></mrow><mrow><mi>Q</mi><mi>S</mi></mrow></msup></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>a</mi></mrow><mrow><mi>B</mi><mi>M</mi></mrow></msup></mrow></math></td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td colspan="7">Panel A.
Gross Returns</td></tr><tr><td>CO</td><td>3.580***(1.380)</td><td>2.386***(0.747)</td><td>2.498***(0.868)</td><td>2.133***(0.742)</td><td>2.580***(0.780)</td><td>3.033***(1.027)</td></tr><tr><td>Constant</td><td>0.607**(0.243)</td><td>-0.061(0.062)</td><td>0.093(0.088)</td><td>0.115*(0.070)</td><td>-0.130(0.099)</td><td>0.092(0.116)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>379,806</td><td>330,588</td><td>330,588</td><td>330,588</td><td>330,588</td><td>379,806</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></math></td><td>0.827</td><td>0.130</td><td>0.147</td><td>0.141</td><td>0.177</td><td>0.271</td></tr><tr><td colspan="7">Panel B.
Net-of-Expenses Returns</td></tr><tr><td>CO</td><td>3.564***(1.380)</td><td>2.364***(0.747)</td><td>2.478***(0.869)</td><td>2.115***(0.741)</td><td>2.563***(0.779)</td><td>3.010***(1.027)</td></tr><tr><td>Constant</td><td>0.603**(0.243)</td><td>-0.066(0.062)</td><td>0.088(0.088)</td><td>0.110(0.070)</td><td>-0.135(0.099)</td><td>0.087(0.116)</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>379,806</td><td>330,588</td><td>330,588</td><td>330,588</td><td>330,588</td><td>379,806</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></math></td><td>0.828</td><td>0.130</td><td>0.146</td><td>0.140</td><td>0.176</td><td>0.270</td></tr></table>
</div>
<!-- para 79 -->
Overall, the results in the regression approach are consistent with those in the portfolio sorts.
Notably, funds with higher CO tend to have higher gross and net-off-fee returns.
These findings suggest that not only do funds with higher CO measure tend to do better in terms of average returns and Sharpe ratio, but they also share the gains with their end investors.
<!-- para 81 -->
In this section, we provide three sets of results that highlight the sources of the underlying outperformance of high-CO funds, distinct from simple industry specialization.
First, funds earn superior returns predominantly from positions with positive common ownership, as opposed to positions without such overlap.
We decompose each fund's portfolio into CO positions (defined as holdings with $\kappa_{p,m} > 0$) and non-CO positions ($\kappa_{p,m} = 0$) and then compute the holding-based returns for those CO and non-CO portfolios.
Applying both Fama-MacBeth and panel regression methods with appropriate controls, we find that CO positions of high-CO funds significantly outperform non-CO positions.
As reported in Table 6, the estimated coefficients for CO positions range from 0.954 to 2.964 and are statistically significant at the $1\%$ level, whereas those for non-CO positions are markedly smaller and often insignificant.
This pattern, observed in both raw and risk-adjusted returns, provides evidence that the superior performance of funds is driven directly by their common ownership positions.
<!-- para 83 -->
*Table 6 presents results on decomposed portfolios to explore the mechanisms underlying the superior performance of high-CO funds.
The table compares the performance of CO portfolios versus non-CO portfolios.
In the odd columns, the dependent variables are CO portfolio returns, which are holding-based returns, measured as the weighted average of the monthly returns of the portfolio firms in which the fund holds common ownership (i.e., $\kappa_{p,m} > 0$).
In the even columns, the dependent variables are non-CO portfolio returns, which are the weighted average of the monthly returns of the portfolio firms in which the fund does not hold common ownership (i.e., $\kappa_{p,m} = 0$).
To construct the weighted average portfolio returns, the weights are the investment weights of the fund in each firm measured in the previous quarter.
The monthly stock returns are measured as either raw returns or risk-adjusted returns using the 6-factor model.
Test of differences reports statistical tests comparing coefficients between regressions.
The key independent variable is the fund's common ownership (CO) measured at the previous quarter-end.
Control variables are the same as in Table 5.
Regressions are estimated using both Fama-MacBeth (FM) and panel approaches with month fixed effects.
Standard errors reported in parentheses are Newey-West-adjusted for up to 3-month lags in FM regressions and are clustered by fund and month in panel regressions. ***, **, and * indicate statistical significance at the $1\%$, $5\%$, and $10\%$ levels, respectively*
<!-- para 84 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td rowspan="2">Portfolios</td><td colspan="2">r</td><td colspan="2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>&#x003B1;</mi></mrow><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td colspan="2">r</td><td colspan="2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>&#x003B1;</mi></mrow><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td></tr><tr><td>CO</td><td>Non-CO</td><td>CO</td><td>Non-CO</td><td>CO</td><td>Non-CO</td><td>CO</td><td>Non-CO</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>CO</td><td>2.964***(1.014)</td><td>0.460(0.523)</td><td>1.613**(0.703)</td><td>0.781**(0.349)</td><td>1.279**(0.498)</td><td>0.379(0.287)</td><td>0.954***(0.348)</td><td>0.543***(0.207)</td></tr><tr><td>Test of Dif &gt; 0</td><td>2.504**(1.140)</td><td></td><td>0.832(0.785)</td><td></td><td>0.900*(0.575)</td><td></td><td>0.519*(0.403)</td><td></td></tr><tr><td>Regression</td><td>FM</td><td>FM</td><td>FM</td><td>FM</td><td>Panel</td><td>Panel</td><td>Panel</td><td>Panel</td></tr><tr><td>Fund Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Month</td><td></td><td></td><td></td><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>330,583</td><td>330,465</td><td>330,583</td><td>330,465</td><td>330,583</td><td>330,465</td><td>330,583</td><td>330,465</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></math></td><td>0.734</td><td>0.706</td><td>0.168</td><td>0.160</td><td>0.677</td><td>0.666</td><td>0.092</td><td>0.108</td></tr></table>
</div>
<!-- para 85 -->
Second, our CO measure captures an individual fund's common ownership positions, which differs from firm- and industry-level common ownership that aggregates common ownership across all shareholders' stakes.
When we stratify our sample by industry-level common ownership intensity—proxied by the MHHI delta used in Azar et al. (2018)—we observe that for portfolio firms in industries with high MHHI delta, CO positions yield robust and economically significant coefficients (ranging from 1.374 to 2.945, as reported in Panel A of Table 7).
In contrast, these effects are substantially muted in industries with low MHHI delta.
The differences between the coefficients on CO from the two regressions are statistically significant at the $1\%$ level across all specifications.
This finding shows that the benefits of CO are contingent on a broader ownership network that collectively influences industry competitive dynamics.[^30]
<!-- para 86 -->
Third, the effect of common ownership is further reinforced in concentrated industries, where market power enhances the ability of funds to influence competitive dynamics.
Using the Herfindahl–Hirschman Index (HHI) based on the Hoberg–Phillips 25 text-based industry classifications to measure industry concentration, we further partition the CO positions into portfolio firms in more concentrated industries (HHI above the median in a year-month) and those in less concentrated industries (below-median HHI industries). [^31] The results in Panel B of Table 7 demonstrate that the positive association between CO and fund performance is pronounced in concentrated industries, where funds can more effectively leverage their ownership positions to influence competitive outcomes.
In less concentrated industries, this relationship is weaker, underscoring the importance of market structure in enhancing the anti-competitive effects of common ownership.
<!-- para 88 -->
*Table 7 presents results on decomposed portfolios to explore mechanisms underlying the superior performance of high-CO funds across different industry characteristics.
We focus on the CO portfolios that consist of portfolio firms commonly held by funds ( $\kappa_{p,m} > 0$ ), as defined in Table 6.
Panel A examines the performance of CO portfolios partitioned by Modified Herfindahl-Hirschman Index Delta (MHHI Delta, referred to in Azar et al. (2018)).
The odd columns report results for CO portfolios consisting of firms in industries with above-median MHHI Delta among the portfolios, whereas the even columns present results for CO portfolios of firms in industries with below-median MHHI Delta.
Panel B examines CO portfolios partitioned by industry concentration (HHI).
The odd columns report results for CO portfolios consisting of firms from above-median HHI industries, whereas the even columns present results for CO portfolios consisting of firms from below-median HHI industries.
The monthly stock returns are measured as either raw returns or risk-adjusted returns using the 6-factor model.
The key independent variable is the fund's common ownership (CO) measured at the previous quarter-end.
Control variables are the same as reported in Table 5.
Regressions are estimated using both Fama–MacBeth (FM) and panel approaches with month fixed effects.
Test of differences reports statistical tests comparing coefficients between regressions.
Standard errors reported in parentheses are Newey–West-adjusted for up to 3-month lags in FM regressions and are clustered by fund and month in panel regressions. ***, **, and * indicate statistical significance at the 1%, 5%, and 10% levels, respectively.
In both panels, the sample period is from 1999 to 2015, during which the Hoberg–Phillips 25 industry classifications are available*
<!-- para 89 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td></td><td colspan="2">r</td><td colspan="2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>&#x003B1;</mi></mrow><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td colspan="2">r</td><td colspan="2"><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>&#x003B1;</mi></mrow><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td></tr><tr><td colspan="9">Panel A.
High- vs. Low-MHHI-Delta Portfolios (Conditional on CO Portfolios)</td></tr><tr><td>MHHI-Delta Portfolios</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>CO</td><td>2.945***(0.808)</td><td>0.421(0.477)</td><td>1.676***(0.597)</td><td>0.005(0.263)</td><td>1.731***(0.376)</td><td>0.246(0.249)</td><td>1.374***(0.275)</td><td>-0.166(0.189)</td></tr><tr><td>Test of Dif &gt; 0</td><td>2.524***(0.938)</td><td></td><td>1.671***(0.652)</td><td></td><td>1.485***(0.451)</td><td></td><td>1.540***(0.334)</td><td></td></tr><tr><td>Regression</td><td>FM</td><td>FM</td><td>FM</td><td>FM</td><td>Panel</td><td>Panel</td><td>Panel</td><td>Panel</td></tr><tr><td>Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Month</td><td></td><td></td><td></td><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>264,368</td><td>253,061</td><td>264,368</td><td>253,061</td><td>264,368</td><td>253,061</td><td>264,368</td><td>253,061</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mrow><mi>R</mi></mrow><mrow><mn>2</mn></mrow></msup></mrow></math></td><td>0.656</td><td>0.639</td><td>0.163</td><td>0.171</td><td>0.593</td><td>0.599</td><td>0.092</td><td>0.127</td></tr></table>
</div>
<!-- para 90 -->
**Panel B.** High- vs. Low-HHI Portfolios (Conditional on CO Portfolios)
<!-- para 91 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td>HHI Portfolios</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td><td>High</td><td>Low</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>CO</td><td>3.108***(0.851)</td><td>0.322(0.578)</td><td>2.031***(0.658)</td><td>-0.349(0.374)</td><td>2.144***(0.375)</td><td>-0.238(0.283)</td><td>1.697***(0.287)</td><td>-0.570***(0.201)</td></tr><tr><td>Test of Dif &gt; 0</td><td>2.786***(1.029)</td><td></td><td>2.380***(0.757)</td><td></td><td>2.382***(0.470)</td><td></td><td>2.267***(0.350)</td><td></td></tr><tr><td>Regression</td><td>FM</td><td>FM</td><td>FM</td><td>FM</td><td>Panel</td><td>Panel</td><td>Panel</td><td>Panel</td></tr><tr><td>Fund Controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Month</td><td></td><td></td><td></td><td></td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>264,368</td><td>242,077</td><td>264,368</td><td>242,077</td><td>264,368</td><td>242,077</td><td>264,368</td><td>242,077</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.637</td><td>0.652</td><td>0.154</td><td>0.248</td><td>0.583</td><td>0.600</td><td>0.090</td><td>0.196</td></tr></table>
</div> Altogether, these findings show that CO positions are associated with superior performance through a mechanism distinct from industry effects, though the relationship is amplified in environments with high overall common ownership and certain market structures.
<!-- para 93 -->
This section attempts to address omitted variable concerns on the positive relationship between fund-level common ownership positions and fund performance.
First, we matched high-CO funds with low-CO funds based on 12 observable fund characteristics.
Using the matched sample, we replicate the positive relationship.
Then, we consider three alternative explanations that may drive our results: portfolio industry concentration effects, common selection, and funds' tendency to select firms with high common ownership.
<!-- para 95 -->
To alleviate the omitted variable concerns, we first implement a matching strategy and additional robustness tests on fund performance.
We match high-CO funds with low-CO funds based on 12 observable characteristics—including all variables listed in Table 1 except for CO—using propensity score matching.
For each fund in the top half of the CO distribution, we identify a matched fund in the bottom half with the closest observable characteristics without replacement.
The matching is conducted quarterly to ensure contemporaneous relevance and avoid look-ahead bias.
<!-- para 96 -->
The covariate balance analysis demonstrates that treated (high-CO) and control (low-CO) funds are remarkably similar across all observable dimensions.
As reported in Supplementary Material Figure B3 and Supplementary Material Table B5, none of the differences in key fund characteristics are statistically significant.
This balanced matching helps mitigate concerns about selection on observables.
Subsequent fund performance regressions in Supplementary Material Table B6—estimated using both Fama–MacBeth and fixed-effects models—confirm that the positive relationship between CO and performance remains robust.
This holds across various performance measures, as well as across alternative matching samples based on coarsened exact matching and other characteristic combinations.
<!-- para 98 -->
Next, we evaluate three possible alternative explanations for our main finding: portfolio industry concentration (PIC), common selection (CS), and common-ownership stock picking (COSP) to ensure that the positive association between fund-level common ownership and fund performance is not driven by these confounders.
<!-- para 99 -->
First, actively managed funds with higher CO may concentrate their holdings in particular industries where they possess informational advantages.
Kacperczyk et al. (2005) demonstrate that funds with high PIC tend to outperform more diversified peers, raising the concern that our results might simply reflect a PIC effect.
Importantly, however, the PIC measure—constructed across 10 industries—does not necessarily imply high-CO, nor does a high-CO strategy require industry concentration.
Nevertheless, to address this, we include PIC as a control in our Fama–MacBeth regressions.
As reported in columns 1 and 2 of Table 8, the
<!-- para 101 -->
*Table 8 reports the results of the Fama–MacBeth cross-sectional regressions, controlling for variables that represent alternative explanations.
The dependent variables are funds' monthly returns and Fama–French 6-factor alpha, which are measured after expenses and represented as monthly returns in percentages.
The main independent variable is the fund's common ownership, measured by CO.
Columns 1 and 2 include KSZ's portfolio industry concentration (PIC) as the control variable.
Columns 3 and 4 include the measure of common selection of institutional investors (CS) as the control variable.
Columns 5 and 6 include the measure of stock picking on firm-level common ownership (COSP) as the control variable.
Other standard control variables are the same as reported in Table 5. ***, **, and * denote statistical significance at the 1%, 5%, and 10% levels, respectively*
<!-- para 102 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td rowspan="3">Additional Controls:</td><td colspan="2">PIC</td><td colspan="2">CS</td><td colspan="2">COSP</td></tr><tr><td colspan="6">Dependent Variable</td></tr><tr><td>r</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B1;</mi><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td>r</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B1;</mi><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td><td>r</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>&#x003B1;</mi><mrow><mi>F</mi><mi>F</mi><mn>6</mn><mi>F</mi></mrow></msup></mrow></math></td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>CO</td><td>2.748**(1.069)</td><td>1.714**(0.705)</td><td>3.238***(1.088)</td><td>2.202***(0.720)</td><td>1.618*(0.968)</td><td>2.084***(0.742)</td></tr><tr><td>Constant</td><td>0.257(0.229)</td><td>-0.170(0.106)</td><td>0.493**(0.220)</td><td>0.066(0.108)</td><td>0.981***(0.346)</td><td>0.028(0.102)</td></tr><tr><td>Fund controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>No. of obs.</td><td>379,806</td><td>330,588</td><td>379,806</td><td>330,588</td><td>379,806</td><td>330,588</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.857</td><td>0.163</td><td>0.858</td><td>0.165</td><td>0.845</td><td>0.146</td></tr></table>
</div>
<!-- para 103 -->
coefficient of CO remains positive and statistically significant even after accounting for PIC, whose correlation with CO is below 0.20.
<!-- para 104 -->
Second, the common selection (CS) effect posits that funds can co-hold stocks with superior intrinsic return potential, regardless of fund-level CO.
Following Alti and Sulaeman (2012) and Sias, Starks, and Titman (2006), we proxy for this effect by the portfolio-weighted change in the number of institutional investors.
For each stock in the portfolio of a fund, we calculate the quarterly change in the number of institutional holders and aggregate these changes using portfolio weights. [^32] Columns 3 and 4 of Table 8 include this CS measure as an additional control.
Again, the positive relationship between CO and performance remains unchanged, indicating that the selection of high-quality stocks in combination does not drive our results.
<!-- para 105 -->
Third, fund managers might simply select firms characterized by high firm-level common ownership (i.e., high profit weights) without necessarily holding stakes in their competitors.
To address this concern, we construct the CO stock-picking measure (COSP):
<!-- para 106 -->
$$ C O S P _ {p} = \sum_ {m} w _ {p, m} \kappa_ {m}, \tag {8} $$
<!-- para 107 -->
where $\kappa_{m} = \sum_{n} s_{n}\kappa_{m,n}$.
We first calculate the firm-level common ownership measure $\kappa_{m}$ by summing all pairwise profit weights, $\kappa_{m,n}$, of the firm $m$ to its competitors $n$ weighted by $s_{n}$, the relative sales percentage.
Then $COSP_{p}$ is the sum of the profit
<!-- para 108 -->
weights for all stocks held in the portfolio p, weighted by the portfolio weights of the stocks $w_{p,m}$.
Unlike the CO measure, $COSP_{p}$ considers the common ownership of all shareholders (based on our comprehensive ownership data sourced from 13F, 13D, 13G, and so forth) in a firm and does not require the fund to invest in both the focal firm and its competitors.
Funds that invest in a firm but do not invest in its competitors are less likely to actively engage in corporate decision-making to soften competition, as they would only gain if the focal firm outcompetes its competitors.
Columns 5 and 6 of Table 8 report that the CO coefficient remains significant after controlling for funds' stock picking on firms with varying degrees of common ownership.
<!-- para 109 -->
Although our robustness tests rule out the three alternative explanations, our analysis remains inherently correlational and cannot establish that common ownership causally reduces competition or increases fund returns.
Although our results align with theoretical predictions—such as greater CO effects for portfolio firms in industries with high overall common ownership and concentration—we cannot entirely rule out alternative mechanisms.
Yet, any viable competing explanation would need to satisfy three stringent criteria: i) produce superior returns at the individual position level (CO vs. non-CO holdings), ii) interact positively with industry-level common ownership intensity (MHHI delta), and iii) be amplified in highly concentrated industries (HHI).
Absent these features, alternative theories are unlikely to reproduce the cross-sectional and within-fund patterns we observe.
Establishing causality will require future research that exploits exogenous variation in CO or directly measures changes in competitive behavior.
<!-- para 111 -->
Our last analysis relating CO and fund performance examines whether the persistence in alphas aligns with the persistence in CO, as discussed in Section III.A.
Using the portfolio sort analysis, we study the long-term performance of CO decile portfolios with varying levels of past CO, ranging from 1 to 6 years.
Table 9 reports the results.
<!-- para 112 -->
We find that funds with high CO outperform those with low CO for at least 6 years after forming the portfolios.
The persistence in performance, coupled with the persistence in fund CO positions, shows a strategy that is profitable yet not widely replicated.
Several frictions may constrain wider adoption of CO strategies.
First, effective implementation requires specialized governance expertise and engagement resources to monitor and influence multiple portfolio firms.
Second, our measure captures meaningful ownership overlap across competitors, necessitating substantial position sizes that smaller funds may be unable to accumulate.
Third, regulatory scrutiny from antitrust authorities increases compliance costs and legal risks.
Finally, business relationships between institutional investors and portfolio companies may create conflicts that constrain governance engagement (Brickley, Lease, and Smith (1988)).
These barriers may explain why CO strategies remain profitable over extended periods without being arbitrated away.
If fund managers overcome these hurdles, they should be compensated accordingly.
We investigate this compensation question next by examining the incentives of fund managers to adopt CO strategies.
<!-- para 114 -->
*Table 9 reports the long-term performance measured by the 6-factor net-of-fee alphas of each decile portfolio sorted by their lagged n-year CO, using a calendar time portfolio approach.
For example, the column of $\mathrm{CO}_{t-2}$ reports the performance of the decile portfolios sorted by their past CO in the lagged 2 years.
The HML is the long-short portfolio formed by buying the high lagged n-year CO decile portfolio and selling the low one.
All t-statistics are Newey-West-adjusted*
<!-- para 115 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi><mi mathvariant="normal">B</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi></mrow></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>1</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>1</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>2</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>2</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>3</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>3</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>4</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>4</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>5</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>5</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>6</mn></mrow></msub></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>t</mi><mo stretchy="false">&#x00028;</mo><msub><mrow><mi mathvariant="normal">C</mi><mi mathvariant="normal">O</mi></mrow><mrow><mi>t</mi><mo>&#x02212;</mo><mn>6</mn></mrow></msub><mo stretchy="false">&#x00029;</mo></mrow></math></td></tr><tr><td>Low</td><td>-0.080</td><td>(-1.933)</td><td>-0.088</td><td>(-2.259)</td><td>-0.093</td><td>(-2.457)</td><td>-0.097</td><td>(-2.497)</td><td>-0.100</td><td>(-2.574)</td><td>-0.099</td><td>(-2.604)</td></tr><tr><td>2</td><td>-0.101</td><td>(-2.724)</td><td>-0.106</td><td>(-2.880)</td><td>-0.108</td><td>(-2.925)</td><td>-0.112</td><td>(-2.993)</td><td>-0.113</td><td>(-2.998)</td><td>-0.115</td><td>(-3.008)</td></tr><tr><td>3</td><td>-0.125</td><td>(-3.155)</td><td>-0.123</td><td>(-3.100)</td><td>-0.124</td><td>(-3.072)</td><td>-0.122</td><td>(-3.044)</td><td>-0.122</td><td>(-3.020)</td><td>-0.121</td><td>(-3.004)</td></tr><tr><td>4</td><td>-0.128</td><td>(-2.950)</td><td>-0.127</td><td>(-2.882)</td><td>-0.127</td><td>(-2.881)</td><td>-0.118</td><td>(-2.708)</td><td>-0.118</td><td>(-2.693)</td><td>-0.119</td><td>(-2.739)</td></tr><tr><td>5</td><td>-0.091</td><td>(-2.015)</td><td>-0.085</td><td>(-1.863)</td><td>-0.086</td><td>(-1.895)</td><td>-0.083</td><td>(-1.816)</td><td>-0.078</td><td>(-1.658)</td><td>-0.081</td><td>(-1.725)</td></tr><tr><td>6</td><td>-0.087</td><td>(-1.493)</td><td>-0.085</td><td>(-1.574)</td><td>-0.087</td><td>(-1.639)</td><td>-0.088</td><td>(-1.723)</td><td>-0.087</td><td>(-1.737)</td><td>-0.084</td><td>(-1.726)</td></tr><tr><td>7</td><td>-0.112</td><td>(-2.394)</td><td>-0.105</td><td>(-2.156)</td><td>-0.100</td><td>(-2.132)</td><td>-0.100</td><td>(-2.135)</td><td>-0.101</td><td>(-2.158)</td><td>-0.101</td><td>(-2.154)</td></tr><tr><td>8</td><td>-0.047</td><td>(-0.804)</td><td>-0.052</td><td>(-0.946)</td><td>-0.053</td><td>(-0.949)</td><td>-0.054</td><td>(-0.966)</td><td>-0.052</td><td>(-0.925)</td><td>-0.049</td><td>(-0.882)</td></tr><tr><td>9</td><td>-0.073</td><td>(-1.726)</td><td>-0.066</td><td>(-1.382)</td><td>-0.065</td><td>(-1.311)</td><td>-0.066</td><td>(-1.308)</td><td>-0.064</td><td>(-1.273)</td><td>-0.062</td><td>(-1.229)</td></tr><tr><td>High</td><td>0.009</td><td>(0.174)</td><td>0.006</td><td>(0.110)</td><td>0.001</td><td>(0.018)</td><td>0.000</td><td>(0.003)</td><td>-0.001</td><td>(-0.018)</td><td>0.002</td><td>(0.033)</td></tr><tr><td>HML</td><td>0.089</td><td>(2.323)</td><td>0.094</td><td>(2.642)</td><td>0.094</td><td>(2.634)</td><td>0.097</td><td>(2.811)</td><td>0.099</td><td>(2.928)</td><td>0.100</td><td>(2.937)</td></tr></table>
</div>
<!-- para 117 -->
In this section, we study how CO relates to fund manager payoffs.
To do so, we employ the framework from Berk and Green (2004) and consider the first-order effects of fund managers' payoffs from management fees.
Since high-CO funds earn positive gross and net-of-fee alphas, we next study whether fund managers also share in the surplus by charging higher fees.
Then, taking the results from fund returns and fees together, we conduct a back-of-the-envelope calculation to estimate the relationship between CO and fund managers' compensation.
<!-- para 119 -->
To study the differences in fees, we use a panel regression with fund-by-year observations with the following specification: (9) EXPENSE_RATIO $_{p,t}$ (MANAGEMENT_FEE $_{p,t}$ ) = $\alpha_{j(p),t} + \beta CO_{p,t} + X'_{p,t-1}\Gamma + \varepsilon_{p,t}$ , where $p$ indexes a fund, $j(p)$ is the fund family, and $t$ indexes a year.
The dependent variables are either fund expense ratios or management fees in year $t$.
The control variables in $X_{p,t-1}$ follow those in equation (7).
In addition, we include fund family-by-year fixed effects $\alpha_{j(p),t}$ to account for time-varying fund family policies (e.g., Gil-Bazo and Ruiz-Verdú (2009), Guercio and Reuter (2014), and Hortaçsu and Syverson (2004)).
Standard errors are clustered by both fund and year, allowing for shocks to fees that commonly affect all funds and autocorrelated shocks within a fund through time.
<!-- para 120 -->
*Table 10 reports that, after controlling for time-varying fund and fund-family characteristics, CO is positively associated with expense ratios and management fees—both in the cross section (columns 1 and 3) and within the fund family (columns 2 and 4).
Economically, a 1-standard-deviation increase in fund CO is associated with 4.38 BPS ( $4.673 \times 0.94\%$ ) higher expense ratios and 2.34 BPS ( $2.497 \times 0.94\%$ ) higher management fees*
<!-- para 122 -->
*Table 10 presents panel regressions studying the relationship between fund CO and fund fees.
The observations are at the fund-year level.
The dependent variables are annualized fees and expenses reported in CRSP, represented in percentages.
The main independent variable is the fund's average common ownership (CO) measured in the previous year.
The regressions controls for lagged 1-month log TNA, lagged 1-year EXPENSE_RATIO, lagged 1-year TURNOVER_RATIO, lagged 1-month FUND_FLOW, lagged 1-year FUND_AGE, and lagged 1-month FUND_RETURN.
In columns 1 and 3, the regressions incorporate year fixed effects, whereas in columns 2 and 4, the regressions include fund family-by-year fixed effects.
Robust standard errors are clustered by fund and year. ***, **, and * denote statistical significance at the 1%, 5%, and 10% levels, respectively*
<!-- para 123 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td rowspan="2"></td><td colspan="2">EXPENSE_RATIO (%)</td><td colspan="2">MANAGEMENT_FEE (%)</td></tr><tr><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>CO</td><td>4.673***(0.858)</td><td>2.551***(0.572)</td><td>2.497***(0.562)</td><td>1.253***(0.403)</td></tr><tr><td>Fund controls</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Year</td><td>Yes</td><td></td><td>Yes</td><td></td></tr><tr><td>FE: Fund family × Year</td><td></td><td>Yes</td><td></td><td>Yes</td></tr><tr><td>No. of obs.</td><td>33,093</td><td>33,093</td><td>33,093</td><td>33,093</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.282</td><td>0.590</td><td>0.161</td><td>0.575</td></tr></table>
</div>
<!-- para 124 -->
To assess whether the relationship between CO and fund manager fees is plausibly meaningful as an incentive for fund managers to adopt common ownership strategies, we next consider the average fund manager's compensation.
<!-- para 126 -->
We conduct a simple back-of-the-envelope calculation similar to Lewellen and Lewellen (2022).
However, where Lewellen and Lewellen (2022) consider an exogenous increase in the value of a portfolio position, we consider the payoff to a manager adopting a high-CO strategy.
Following Berk and Green (2004), fund managers' objective is to maximize their compensation, specified as: (10)
<!-- para 127 -->
$$ \begin{aligned}COMPENSATION_{p,t}&=TNA_{p,t-1}\times\left(1+r_{p,t}\right)\times\left(1+FUND\_{F}LOWS_{p,t}\right)\\&\times\left(1-EXPENSE\_{R}ATIO_{p,t}\right)\\&\times MANAGEMENT\_{F}EE_{p,t},\end{aligned} $$
<!-- para 128 -->
where $TNA_{p,t-1}$ is the lagged total net assets, $r_{p,t}$ is the gross monthly return, and $FUND\_FLOWS_{p,t}$ is the fund flow represented as a fraction of $TNA_{p,t-1}$. $EXPENSE\_RATIO_{p,t}$ and $MANAGEMENT\_FEE_{p,t}$ denote the fund's expense ratio and management fee, respectively.
<!-- para 129 -->
Using our most conservative estimates, funds with a 1-standard-deviation (0.94%) higher CO have 3.58 BPS higher monthly raw gross returns (column 1 of Panel A of Table 5), 2.55 BPS higher annual expense ratio (column 2 of Table 10), and 1.25 BPS higher annual management fees (column 4 of Table 10).
Supplementary Material Table B10 reports that average fund flows are not significantly affected by CO, conditional on fund returns, and there is no existing theory suggesting that fund-level CO should be unconditionally correlated with fund flows.
Therefore, we assume no relationship between CO and average fund flows.
<!-- para 130 -->
For a typical fund in our sample with the median value of all characteristics, fund managers earn around 2.2% (~$41,000) more annual compensation relative to the median$1.92 million if they adopt a strategy with a 1-standard-deviation higher CO.
Over 5 years, the fund manager earns around 17.4% (~$333,000) more cumulative compensation, since the increase in annual compensation compounds through the CO-return relationship.
This calculation shows that active mutual fund managers seem financially incentivized to pursue common ownership strategies.[^33]
<!-- para 132 -->
Our earlier findings reveal that funds with larger common ownership positions achieve higher performance and deliver superior returns to their investors despite charging higher fees.
These elevated fees could reflect compensation for costly monitoring efforts directed at corporate policies among competing firms.
Therefore, in this section, we study whether funds with higher CO intend to engage with their portfolio companies in ways consistent with the common ownership hypothesis.
Specifically, we investigate whether mutual funds with substantial ownership stakes across competing firms strategically vote to maximize their portfolio returns and reduce incentives for competition between product-market rivals.
<!-- para 133 -->
To this end, we focus on mutual funds’ voting on corporate policy proposals in shareholder meetings.
Motivated by the voice model of Edmans et al. (2019), which demonstrates that common owners have stronger monitoring incentives, we utilize classifications and recommendations from ISS to test: i) whether active mutual funds with higher CO tend to be more active monitors (Iliev and Lowry, 2015) and ii) whether they systematically vote to reduce executive pay-performance sensitivity (Antón et al. (2023)) and support the appointment of “common directors” who hold positions across competing firms (Azar and Vives (2021)).
<!-- para 135 -->
We first examine whether funds with larger common ownership are more active monitors of their portfolio firms.
Following Iliev and Lowry (2015), we define active monitoring as the propensity to vote independently of ISS recommendations.
Specifically, for each fund in a year, we calculate the percentage of votes where the fund votes differently from ISS recommendations.
We relate this proxy for active voting to funds' CO, along with other fund characteristics measured in the previous year at the fund-year level.
<!-- para 136 -->
*Table 11 reports the results.
In column 1, we find that funds with higher CO are associated with greater disagreement with ISS, which is proxied by the percentage of proposals in which the fund votes against ISS recommendations (Iliev and Lowry (2015)).
In terms of economic magnitude, a 1-standard-deviation increase in fund CO is associated with a 4.26-percentage-point ( $0.474 \times 0.09$) increase in disagreement with ISS recommendations, representing a substantial increase relative to the unconditional mean of 9.0%*
<!-- para 137 -->
In addition, we consider two variants of active voting measures: the percentage of votes where the fund votes differently from ISS recommendations among contentious proposals in column 2 and consensus proposals in column 3.
We find that high-CO funds are still positively related to disagreement with ISS.
Importantly, as evidenced in column 3, even for proposals where the recommendations of ISS and management align, high-CO funds are still more likely to disagree with them, indicating active voting. [^34]
<!-- para 139 -->
*Table 11 examines the relationship between funds' common ownership positions (CO) and measures of active voting.
Panel A presents results on disagreement with ISS voting recommendations.
The sample is at the fund-year level.
The dependent variable in column 1 is the percentage of all proposals where the fund votes differently from ISS recommendations.
Column 2 uses the percentage of contentious proposals where the fund votes differently from ISS recommendations, and column 3 uses the percentage of consensus proposals where the fund votes differently from ISS recommendations.
Contentious proposals are those where ISS and management recommendations differ, whereas consensus proposals are those where ISS and management recommendations align.
Panel B presents results on voting RPI, which is the voting reliance on public information introduced by Iliev and Lowry (2015).
The dependent variable in column 1 is the $R^2$ from a regression of fund votes on ISS recommendations among all governance and compensation proposals for a given fund in a year.
Column 2 uses the $R^2$ from regressions focusing on contentious governance and compensation proposals, and column 3 uses consensus governance and compensation proposals.
A lower $R^2$ indicates more active voting by a mutual fund.
All regressions include fund-level CO as the key independent variable along with fund controls, all measured in the previous year.
The regressions incorporate year fixed effects.
Standard errors clustered at the fund level are reported in parentheses. ***, **, and * denote statistical significance at the 1%, 5%, and 10% levels, respectively*
<!-- para 140 -->
**Panel A.** Disagreement with ISS
<!-- para 141 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td colspan="4">Dependent Variable: DISAGREEMENT_WITH_ISS</td></tr><tr><td rowspan="2">Dep Var Definition</td><td>Disagreement of All Proposals</td><td>Disagreement of Contentious Proposals</td><td>Disagreement of Consensus Proposals</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>CO</td><td>0.474***(0.118)</td><td>1.984***(0.416)</td><td>0.252***(0.095)</td></tr><tr><td>Fund controls</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Year</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Mean of Dep Var</td><td>0.090</td><td>0.511</td><td>0.043</td></tr><tr><td>SD of Indep Var</td><td>0.009</td><td>0.009</td><td>0.009</td></tr><tr><td>No. of obs.</td><td>11,632</td><td>11,373</td><td>11,623</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.051</td><td>0.040</td><td>0.032</td></tr><tr><td colspan="4">Panel B.
Voting RPI</td></tr><tr><td colspan="4">Dependent Variable: VOTING_RPI</td></tr><tr><td rowspan="2">Dep Var Definition</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math> from a Regression Based on All Proposals</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math> from a Regression Based on Contentious Proposals</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math> from a Regression Based on Consensus Proposals</td></tr><tr><td>1</td><td>2</td><td>3</td></tr><tr><td>CO</td><td>-1.667***(0.371)</td><td>-1.679***(0.419)</td><td>-4.291***(0.538)</td></tr><tr><td>Fund controls</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Year</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Mean of Dep Var</td><td>0.326</td><td>0.336</td><td>0.272</td></tr><tr><td>SD of Indep Var</td><td>0.009</td><td>0.009</td><td>0.009</td></tr><tr><td>No. of obs.</td><td>11,446</td><td>10,589</td><td>11,421</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.056</td><td>0.053</td><td>0.088</td></tr></table>
</div>
<!-- para 142 -->
An alternative proxy for active voting proposed by Iliev and Lowry (2015) is the voting RPI, defined as the $R^{2}$ value from a regression of fund votes on ISS recommendations.
Following their approach, we focus on governance- and compensation-related proposals that our sample funds vote on and estimate the above regression separately for each fund in a year.
A lower $R^{2}$ indicates more active voting by a mutual fund.
Then, we examine whether this active voting indicator is related to the fund's CO measured in the year prior to the proposals.
The results are reported in Panel B of Table 11.
In column 1, we find that the voting (Supplementary Material Table B9).
This suggests that common owners are likely to be long-term shareholders who exploit the common ownership effects, corroborating the findings of the active monitoring.
<!-- para 143 -->
behaviors of mutual funds with higher CO are less likely to be explained by ISS recommendations.
In terms of economic magnitude, a 1-standard-deviation increase in fund CO is associated with a 15-percentage-point ( $1.667 \times 0.09$) decline in the $R^{2}$ from regressions of fund votes on ISS recommendations.
These results are robust and even stronger when we estimate the $R^{2}$ using contentious or consensus governance and compensation proposals.
Again, these findings suggest that high-CO funds are active voters whose voting activities are less likely to be explained by ISS recommendations.
<!-- para 145 -->
We next investigate how mutual fund common owners vote on specific proposals related to executive compensation.
Antón et al. (2023) theoretically demonstrate that managerial compensation tends to be less sensitive to own-company performance in the presence of common ownership, as weaker managerial incentives can soften competition within industries.
Analogously, we test whether high-CO funds have an incentive to reduce competition among portfolio firms by voting against the proposals related to the approval of executives' performance-related compensation, such as stock or stock option plans.
<!-- para 146 -->
Using ISS Voting Analytics data, we estimate fund-by-proposal-level regressions of the form (11)
<!-- para 147 -->
$$ V O T E_{p,k(i,t)}=a_{j(p),t}+\gamma_{k(i,t)}+\beta C O_{p,i,t}+X_{p,t-1}^{\prime}\Gamma+\varepsilon_{p,k(i,t)t}, $$
<!-- para 148 -->
where $p$ indexes a fund, $i$ is a portfolio company, $k(i,t)$ is a specific corporate policy proposal for firm $i$ in year $t$, and $j(p)$ indicates the fund family of fund $p$.
Observations are structured at the fund-by-proposal level, where a portfolio company could have multiple proposals in the same year.
Control variables in $X_{p,t-1}$ are the same as those in equation (9), measured at the year-end preceding the proposal.
We incorporate proposal fixed effects $\gamma_{k(i,t)}$ and fund family-by-year fixed effects $\alpha_{j(p),t}$.
The former accounts for unobserved heterogeneity at the firm, proposal, and time period levels, whereas the latter controls for time-varying fund family voting patterns (e.g., a family's general propensity to follow ISS recommendations).
With these sets of fixed effects, our identification comes from exploiting variation in votes for a given proposal after controlling for time-varying family unobserved heterogeneity.
The dependent variable $VOTE_{p,k(i,t)}$ varies based on the specific analyses below, and the key independent variable is the previous year-end fund-firm CO measure (i.e., fund $p$'s common ownership in firm $i$ ($\kappa_{p,m}$ in equation (3))).
Standard errors are clustered at the fund level, allowing for correlated voting behavior across proposals within a fund (Iliev and Lowry (2015)).
<!-- para 149 -->
Recognizing the substantial influence of fund families on individual fund voting decisions, we also conduct parallel analyses at the fund family-by-proposal level using the following specification: (12)
<!-- para 150 -->
$$ \%VOTE_{j,k(i,t)}=a_{j,t}+\gamma_{k(i,t)}+\beta CO_{j,i,t}+\varepsilon_{j,k(i,t)t}, $$
<!-- para 152 -->
*Table 12 presents the results of the regressions that relate a mutual fund's voting decisions on specific proposals to the common ownership positions at the fund or fund family level.
In Panel A, the sample consists of proposals approving stock or stock option plans.
In column 1, the unit of observation is fund-by-proposal.
The dependent variable is an indicator variable that equals 1 if a fund votes against stock or stock option plans, and the key independent variable is fund-firm CO.
In column 2, the observation level is fund family-by-proposal.
The dependent variable is the percentage of voting against stock or stock option plans in the fund family, and the independent variable is the fund family-firm CO.
In column 3, the regression is estimated at the fund-year level.
The dependent variable is the logarithm of portfolio-weighted average executives' pay-performance sensitivity (delta) in portfolio firms held by a fund in a year, similar to the analysis Anton et al. (2023), and the independent variable is fund CO.
In Panel B, the dependent variables are indicator variables set to 1 if funds vote for director nominees in column 1 and the percentage of votes for director nominees in column 2.
Fund-firm CO and fund family-firm CO are the key independent variables in columns 1 and 2, respectively.
In all regressions, the control variables are lagged 1-year log TNA, EXPENSE_RATIO, TURNOVER_RATIO, FUND_FLOW, FUND_AGE, and FUND_RETURN.
All regressions except column 3 of Panel A include fund family-by-year and proposal fixed effects.
The regression in column 3 of Panel A includes fund family-by-year fixed effects.
The robust standard errors are clustered at the fund level for the fund-proposal analysis and at the fund family for the fund family-proposal analysis. ***, **, and * denote statistical significance at the 1%, 5%, and 10% levels, respectively*
<!-- para 153 -->
**Panel A.** Stock plans and pay-performance sensitivity
<!-- para 154 -->
<div style="overflow-x:auto; width:100%; -webkit-overflow-scrolling:touch;">
<table border=1><tr><td></td><td>VOTE AGAINST_STOCK_PLANS</td><td>%_OF_VOTING AGAINST_STOCK_PLANS</td><td>LOG_OF_PORTFOLIO_FIRMS_DELTA</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td></tr><tr><td>FUND_FIRM_CO</td><td>0.018***(0.005)</td><td></td><td></td></tr><tr><td>FUND_FAMILY_FIRM_CO</td><td></td><td>0.017***(0.006)</td><td></td></tr><tr><td>CO</td><td></td><td></td><td>-23.895***(2.728)</td></tr><tr><td>Fund controls</td><td>Yes</td><td></td><td>Yes</td></tr><tr><td>FE: Fund family x Year</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Proposal</td><td>Yes</td><td>Yes</td><td></td></tr><tr><td>Mean of Dep Var</td><td>0.18</td><td>0.17</td><td>5.90</td></tr><tr><td>No. of obs.</td><td>279,406</td><td>154,877</td><td>33,093</td></tr><tr><td>Observation level</td><td>Fund-Proposal</td><td>Family-Proposal</td><td>Fund-Year</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td>0.493</td><td>0.477</td><td>0.688</td></tr><tr><td colspan="4">Panel B.
Director Elections</td></tr><tr><td></td><td></td><td>VOTE_FOR</td><td>%_OF_VOTING_FOR</td></tr><tr><td></td><td></td><td>1</td><td>2</td></tr><tr><td>HIGH_FUND_FIRM_CO x CO_DIRECTOR_ELECTION</td><td></td><td>0.007**(0.003)</td><td></td></tr><tr><td>HIGH_FUND_FIRM_CO</td><td></td><td>-0.00005(0.001)</td><td></td></tr><tr><td>HIGH_FUND_FAMILY_FIRM_CO x CO_DIRECTOR_ELECTION</td><td></td><td></td><td>0.015**(0.007)</td></tr><tr><td>HIGH_FUND_FAMILY_FIRM_CO</td><td></td><td></td><td>0.002(0.001)</td></tr><tr><td>Fund controls</td><td></td><td>Yes</td><td></td></tr><tr><td>FE: Fund family x Year</td><td></td><td>Yes</td><td>Yes</td></tr><tr><td>FE: Proposal</td><td></td><td>Yes</td><td>Yes</td></tr><tr><td>Mean of Dep Var</td><td></td><td>0.93</td><td>0.93</td></tr><tr><td>No. of obs.</td><td></td><td>5,837,453</td><td>3,123,425</td></tr><tr><td>Observation level</td><td></td><td>Fund-Proposal</td><td>Family-Proposal</td></tr><tr><td>Adj. <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msup><mi>R</mi><mn>2</mn></msup></mrow></math></td><td></td><td>0.400</td><td>0.389</td></tr></table>
</div>
<!-- para 155 -->
where the subscripts follow equation (11).
In this analysis, the dependent variable is the percentage of votes for or against a proposal in a fund family.
The key independent variable is the weighted sum of common ownership in a firm across all funds affiliated with the fund family, using each fund's lagged 1-quarter TNA as the weights.
The regression includes proposal fixed effects, as well as the family-by-year fixed effects, which absorb any time-varying variations within a fund family.
<!-- para 156 -->
Thus, family characteristics are omitted from the regression.
The standard errors are clustered at the fund family level.
<!-- para 157 -->
In our fund-by-proposal-level analysis, the dependent variable is an indicator equal to 1 if a fund votes against proposals approving stock or stock option plans.
Column 1 of Panel A of Table 12 reveals that funds with larger common ownership in the firm are more likely to oppose such executive incentive plans.
A 1-standard-deviation increase in the fund-firm CO (0.13) corresponds to a 23-BPS (0.13 × 1.8%) increase in the probability of voting against stock or stock option plans.
Column 2 of Panel A confirms that families with higher common ownership are more likely to oppose these compensation mechanisms.
<!-- para 158 -->
To directly assess whether these voting patterns translate into lower pay-performance sensitivity, we examine the relationship between a fund's CO measure and the average executive compensation “delta”—the sensitivity of executive wealth to changes in stock price—across its portfolio firms.
Using executive delta data from 1999 to 2018 (Coles, Daniel, and Naveen (2006), Core and Guay (2002)), we construct a fund's portfolio delta as the logarithm of the weighted average executive delta of its portfolio firms at year-end (see https://sites.temple.edu/lnaveen/data/ for the data).
Column 3 of Panel A of Table 12 reports that fund-level CO is significantly negatively associated with portfolio-weighted executive compensation delta.
In economic terms, a 1-standard-deviation increase in fund-level CO (0.94%) correlates with a 22.4% decrease in the logarithm of portfolio-weighted executive compensation delta.
The higher propensity of mutual fund common owners to vote against executive stock compensation plans manifests in lower overall pay-performance sensitivity for portfolio firms' executives.
<!-- para 160 -->
Finally, we investigate whether high-CO funds support director nominees who simultaneously serve on boards of competing firms (“CO-directors”).
Such interlocking directorates could facilitate coordination between competitors by creating information channels and aligned governance across firms.
The existence of such directors might seem surprising, given Section 8 of the Clayton Act, which nominally prohibits horizontal directorships in competing corporations.
However, despite this legal prohibition, our data reveal the persistent presence of CO-directors.
From the proposal description, we extract the names of the proposed director nominees (52,951 directors from 227,638 distinct election proposals).
Using Hoberg–Phillips industry classifications, we identify 1,968 proposals involving CO-directors, corresponding to 660 individual directors during our sample period.
This prevalence aligns with findings from other studies, such as Gopalan, Li, and Zaldokas (2022), who identify 1,492 instances of new direct board connections to product-market peers over a similar period.
<!-- para 161 -->
The persistence of the CO-directors, despite legal restrictions, can be attributed to several institutional factors.
First, Section 8 suffers from definitional ambiguity regarding “competitors” and lacks clear guidelines for determining when companies truly compete (Nili (2020)).
Jorgensen and Clark (1979) documented how technical challenges in defining competition, determining “substantial” competitive relationships, and proving competitive harm, combined with a regulatory preference for voluntary compliance, created an environment where interlocks continued.
Second, historical enforcement of Section 8 has been irregular and lenient.
Kramer (1949) noted minimal enforcement in the Act's first 35 years, whereas Wilson (1976) characterized enforcement as “on-again-off-again,” with only brief periods of regulatory activism.
These enforcement challenges have persisted into the modern era—between 2010 and 2019, the FTC and DOJ brought zero Section 8 cases to trial. [^35]
<!-- para 162 -->
In our fund-by-proposal-level analysis, the sample includes all available director elections (both CO-director and other director elections) voted on by our sample funds.
We employ a similar specification as in equation (11).
The dependent variable is a binary indicator equal to 1 if a fund votes for a nominated director.
To facilitate interpretation, we interact an indicator for CO-director elections with a dummy for high fund-firm CO, which equals 1 if the fund-firm CO measure exceeds the family median at the year-end before the election.
Column 1 of Panel B of Table 12 reports that the propensity to vote for director nominees is significantly and positively related to the funds' common ownership in the firm when the directors have existing directorships in the firm's competitors.
In economic terms, funds with high common ownership are 0.7%–1.5% more likely to support CO-directors, representing approximately 10.3%–22.1% of the standard deviation in overall approval rates for director nominees.
However, the coefficient on high fund-firm CO alone is insignificant, suggesting that funds with higher common ownership are not generally more supportive of directors without cross-firm connections.
These results remain robust in our fund family-by-proposal analysis reported in column 2.
Through the lens of revealed preference, these results indicate that active mutual fund common owners strategically use proxy voting to support directors with positions across industry competitors.
This finding aligns with Azar and Vives (2021), who demonstrate that firm pairs with higher levels of common ownership have an increased probability of sharing directors.
<!-- para 163 -->
Collectively, these voting patterns suggest that high-CO funds actively use their governance rights in ways consistent with facilitating coordination among portfolio firms.
They vote more independently of ISS recommendations, oppose executive incentive plans that might intensify competition, and support CO-directors who could facilitate coordination across competing firms. [^36]
<!-- para 165 -->
Common ownership has risen in the United States over the past few decades.
While empirical studies examine whether common ownership has anticompetitive effects on firms or the industries they operate, this article takes a different perspective by investigating the benefits and incentives of common owners who jointly invest in product-market competitors.
Using U.S. actively managed equity mutual fund data from 1999 to 2018, we find a positive relationship between fund common ownership and performance, both before and after fees.
These findings suggest that common institutional investors and their end investors earn from higher returns, consistent with the common ownership hypothesis.
Funds with a larger degree of common ownership also charge higher fees.
Taking fund returns and fees together suggests that fund managers are financially incentivized to adopt the common ownership strategy.
To corroborate this incentive, we provide additional evidence that funds with higher common ownership are more active voters and appear to vote in ways that could soften firm competition.
