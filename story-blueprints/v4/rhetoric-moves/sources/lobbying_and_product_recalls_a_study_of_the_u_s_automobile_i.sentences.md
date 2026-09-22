---
type: sentences-archive
citekey: "lobbying_and_product_recalls_a_study_of_the_u_s_automobile_i"
source_md: "D:\Onedrive\Obsidian Vault\00 工作台\项目\Reference for Recalls\Lobbying and Product Recalls A Study of the U.S. Automobile Industry - Khimendra Singh, Rajdeep Grewal, 2023.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# lobbying_and_product_recalls_a_study_of_the_u_s_automobile_i 句子库存

## introduction
<!-- para 1 -->
During a product crisis, media help disseminate risk-related information to the public ([Bednar, Boivie, and Prince 2013](#bibr2-00222437221131568)).
If consumer complaints or fatalities arise due to defective products, the media can publicize relevant information to enhance its reach and visibility ([King 2008](#bibr53-00222437221131568)).
In the absence of media coverage, product risk information would spread less widely.
Media also uncover data related to defects, and the dissemination of such detailed information should affect public perceptions and shape markets.
Through this influence, media coverage in combination with lobbying should mediate the moderating effect of death reports, as a measure of defect severity, on the lobbying–recall decision link.
That is, when media publicize death reports, we predict that it mediates the influence of defect severity on recall decisions.
<!-- para 2 -->
We depict these complex potential links among lobbying, recall decisions, death reports, and media coverage in [Figure 4](#fig4-00222437221131568).
Model B is similar to the indirect moderation model that [Van Kollenburg and Croon (2021)](#bibr97-00222437221131568) propose as a missing link in discussions of mediation and moderation effects.
A key difference between Models A and B is that the former predicts that the moderating effect of Deaths on the relationship between lobbying and recalls decreases in magnitude but remains statistically significant in the presence of an interaction of Media with lobbying, but in the latter, the moderating effect of Deaths becomes statistically nonsignificant in the presence of a Media × Lobbying interaction term.
In the absence of media, which disseminate defect severity information and make the defect report salient, the effect of defect severity on the lobbying and recall relationship may not be statistically significant.
<!-- para 3 -->
> **H <sub>4</sub>**: The interaction of media coverage and lobbying mediates the moderating effect of defect severity (deaths) on the relationship between lobbying and recall decisions.

## methods
<!-- para 2 -->
We collect data from multiple sources.
First, we gather recalls and consumer complaint information from the NTHSA database.
To identify firms’ lobbying expenditures and the corresponding lobbied issues, we refer to the U.S. Senate database.[^9] We use Compustat to obtain financial indicators (e.g., capital expenditures, liability), then turn to *Automotive News* for sales, LexisNexis for the media coverage measure, and *Consumer Reports* for vehicle quality ratings ([Web Appendix Table W1](#supplementary-materials) provides definitions of these variables).
<!-- para 4 -->
The NHTSA maintains records of recall data.
Its website provides detailed information about both consumer complaints and vehicle recalls, including the name of the firm, make, and model; the number of affected units; and a brief description of the defect.
A balanced panel over a nine-year period (2008–2016; starting year determined by when quarterly lobbying expenditure data are available) features data related to 16 automotive firms (BMW, Daimler, Ford, GM, Honda, Hyundai, Jaguar, Kia, Mazda, Mitsubishi, Nissan, Porsche, Subaru, Tesla, Toyota, and Volkswagen).
Consistent with previous recall research (e.g., [Kalaignanam, Kushwaha, and Eilert 2013](#bibr50-00222437221131568)), we select a representative sample of firms, which account for approximately 95% of total automotive industry sales of passenger cars in the United States.
The firms were involved in 678 vehicle recalls over the nine-year period;[^10] GM faced the highest number of total recalls (113) during this period.
The data identify consumer complaints received by the NHTSA, according to the automobile firm's name; the make, model, and model year; and a brief description of the complaint.
We also obtain death data from this database.
The descriptive statistics are in [Table 3](#table3-00222437221131568), Panel A.
<!-- para 6 -->
<table><thead><tr><th colspan="6">A: Descriptive Statistics</th><th colspan="13">B: Correlation Table</th></tr><tr><th>Variables</th><th>Min</th><th>Max</th><th>Median</th><th>Mean</th><th>SD</th><th>1</th><th>2</th><th>3</th><th>4</th><th>5</th><th>6</th><th>7</th><th>8</th><th>9</th><th>10</th><th>11</th><th>12</th><th>13</th></tr></thead><tbody><tr><td>1.
Lobbying</td><td>0</td><td>7.86</td><td>.21</td><td>.59</td><td>.88</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2.
Complaints</td><td>0</td><td>4,078</td><td>147</td><td>390.15</td><td>561.79</td><td><b>.79</b></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3.
Deaths</td><td>0</td><td>19</td><td>0</td><td>.42</td><td>1.66</td><td><b>.35</b></td><td><b>.55</b></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4.
States</td><td>6</td><td>57</td><td>43</td><td>38.93</td><td>13.53</td><td><b>.54</b></td><td><b>.59</b></td><td><b>.20</b></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5.
Rating</td><td>1.7</td><td>5</td><td>.67</td><td>2.89</td><td>.86</td><td><b>−.21</b></td><td><b>−.21</b></td><td>−.05</td><td><b>−.57</b></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6.
Firm size</td><td>0</td><td>19</td><td>11.93</td><td>9.77</td><td>5.87</td><td><b>.20</b></td><td><b>.22</b></td><td>.07</td><td><b>.31</b></td><td>.003</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7.
Firm age</td><td>1.61</td><td>7.61</td><td>4.42</td><td>4.64</td><td>1.26</td><td>−.09</td><td>−.05</td><td>−.02</td><td><b>.28</b></td><td><b>−.29</b></td><td>−.09</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8.
Advertising</td><td>0</td><td>925.82</td><td>66.98</td><td>109.99</td><td>124.61</td><td><b>.78</b></td><td><b>.76</b></td><td><b>.35</b></td><td><b>.63</b></td><td><b>−.21</b></td><td><b>.25</b></td><td>−.06</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9.
Media</td><td>0</td><td>919</td><td>3</td><td>10.07</td><td>43.05</td><td><b>.16</b></td><td><b>.33</b></td><td><b>.33</b></td><td><b>.14</b></td><td>0</td><td>.05</td><td>−.03</td><td><b>.18</b></td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>10.
R& D Intensity</td><td>0</td><td>.26</td><td>.01</td><td>.01</td><td>.03</td><td>−.04</td><td>−.05</td><td>−.005</td><td><b>−.32</b></td><td><b>.39</b></td><td>−.01</td><td><b>−.38</b></td><td>−.07</td><td>−.02</td><td>1</td><td></td><td></td><td></td></tr><tr><td>11.
CAPEX Intensity</td><td>0</td><td>.28</td><td>.020</td><td>.03</td><td>.04</td><td>.04</td><td>.04</td><td>.04</td><td><b>−.18</b></td><td><b>.33</b></td><td><b>.23</b></td><td><b>−.35</b></td><td>.06</td><td>−.01</td><td><b>.59</b></td><td>1</td><td></td><td></td></tr><tr><td>12.
Agency Costs</td><td>−1.51</td><td>.06</td><td>0</td><td>0</td><td>.07</td><td>.05</td><td>.06</td><td>.01</td><td><b>.17</b></td><td><b>−.16</b></td><td>.10</td><td>.09</td><td>.08</td><td>.02</td><td><b>−.44</b></td><td><b>−.21</b></td><td>1</td><td></td></tr><tr><td>13.
Sales</td><td>0</td><td>.83</td><td>.07</td><td>.14</td><td>.16</td><td>.<b>77</b></td><td><b>.73</b></td><td><b>.25</b></td><td><b>.64</b></td><td><b>−.23</b></td><td><b>.24</b></td><td>−.10</td><td><b>.78</b></td><td><b>.18</b></td><td>−.07</td><td>.04</td><td>.08</td><td>1</td></tr></tbody></table>
<!-- para 7 -->
*Notes*: In the correlation table, *p* -values <.01 are in bold.
<!-- para 8 -->
In this data set, the number of quarterly voluntary recalls ranges from 0 to 15 per firm; the number of quarterly mandatory recalls ranges from 0 to 5 per firm.
The mean quarterly number of complaints is 390 per firm.
We observe 591 voluntary recalls and 87 mandatory recalls during the nine-year period.
In [Figure 5](#fig5-00222437221131568), we highlight some notable data distributions.
The bar graphs of the frequency distribution of voluntary and mandatory recalls (Panels A and B) indicate that, on an aggregate firm level, voluntary recalls span 51.38% of the total data points, whereas mandatory recall events are sparse, accounting for only 11.97% of the total data points.
The line graphs (Panels C and D) also indicate variation in lobbying expenditures and voluntary recalls, aggregated over firms for 36 quarters (nine-year period).
<!-- para 11 -->
The complaint data set further reveals 37 complaint categories,[^11] which we classify into issues that should be attributed to the original equipment manufacturer (OEM; e.g., powertrain) or not (e.g., air bags), according to automotive industry experts (not associated with this study).
Each third-party-supplied part (i.e., non-OEM group) could be present in several car makes, so a defect in a non-OEM part would likely trigger recalls for multiple firms, thereby creating an indirect correlation.
We instead focus on the OEM group, which represents 43% of the total recalls, to avoid such codependency.
Specifically, we consider seven OEM complaint categories, each of which represents at least 2% of all OEM recalls in our data set (electrical system, fuel system \[gasoline\], powertrain, engine \[engine cooling\], suspension, exterior lighting, and structure).
These seven categories account for more than 94% of all OEM recalls.
<!-- para 12 -->
The number of complaints and deaths are primary determinants of recalls; they indicate defect severity and the seriousness of the consequences for consumer safety.
Severe recalls attract more negative responses from stakeholders ([Hoffer, Pruitt, and Reilly 1988](#bibr43-00222437221131568); [Liu and Shankar 2015](#bibr63-00222437221131568); [Ni, Flynn, and Jacobs 2014](#bibr20-00222437221131568)).
Therefore, the number of complaints and deaths are key covariates.
More complaints indicate a widespread vehicle defect ([Eilert et al. 2017](#bibr30-00222437221131568)); the number of complaints also proxies for the potential reach of the recall.
Deaths represent personal losses to consumers.
<!-- para 14 -->
We collect corporate lobbying expenditures from the U.S. Senate website, including spending by firms and their subsidiaries through internal (in-house) lobbyists and external, professional lobbying firms.
As we noted previously, the Lobbying Disclosure Act offers definitions and requirements for lobbyists and lobbying activities; it mandates that each lobbyist indicate for which issues it lobbied in any period.
The resulting reports reveal that firms invest in lobbying to address diverse issues (e.g., accounting, aerospace, automotive industry, energy/nuclear, homeland security, immigration, tobacco, transportation); [Web Appendix Table W2](#supplementary-materials) contains a complete list. [Figure W1](#supplementary-materials) in the [Web Appendix](#supplementary-materials) presents an excerpt from the lobbying report submitted by BMW for its lobbying expenditures for October–December 2016.
Senate records contain lobbying expenditures at the parent firm or holding company level, so we only observe firm-level lobbying expenditures.
We use aggregated expenditure value, which is a sum of external and internal lobbying spending by the firm.
<!-- para 15 -->
Since 2008, cumulative U.S. lobbying expenditures have exceeded $3 billion, with a peak of $3.51 billion in 2009.
In our study, the 16 focal automotive firms spent $338.56 million over nine years (2008–2016).
GM ranked highest during this period, with $99.95 million in total spending, and 2008 marked the year the automotive firms spent the most ($44.90 million).
The median value of quarterly lobbying spending was $212,900; Ford Motors accounts for the highest quarterly expenditure, in the fourth quarter of 2013 ($7.86 million).
In the 36 quarters we study, Subaru did not make any lobbying expenditures, and for Mitsubishi, we observe only one nonzero observation.
The lobbying issue category that attracted the most investments, 11.5% of spending, is the broad “automotive industry,” followed by “taxation” (10.4%).
We exclude Chrysler, which underwent multiple different mergers (Daimler, Fiat); management changes and corresponding regulatory exposure make it a potentially unstable data point for our study.
<!-- para 16 -->
Lobbying expenditures below some reasonable threshold appear as zero values in the Senate data, but we expect this data limitation to have minimal impact.
Firms primarily employ external lobbying firms, for which the reporting threshold is low ($3,000).
In our data, the mean and median values of quarterly lobbying expenditures are $587,789 and $212,882, respectively, and approximately 99% of firm-quarter observations with positive lobbying expenditures include amounts greater than $20,000.
We do not observe any clustering around the threshold.
Therefore, the potential for measurement error due to reporting requirements should be minimal.
<!-- para 18 -->
We include several factors that might affect a firm's recall decisions and lobbying activity.
For example, we consider the geographical dispersion of the defect complaints by counting the unique number of U.S. states where consumers registered complaints.
This variable can account for how widespread the potential defect is, beyond sheer magnitude indicators (i.e., number of complaints and deaths).
We account for a firm's size, using total assets ([Ridge, Ingram, and Hill 2017](#bibr82-00222437221131568)), because larger firms usually feature a more diversified, complex product base, which could lead to more recalls ([Steven, Dong, and Corsi 2014](#bibr87-00222437221131568)).
Firm size may determine lobbying and political power too ([Kerr, Lincoln, and Mishra 2014](#bibr52-00222437221131568)), in that politics tends to be more important to larger, more visible firms.
We consider the number of vehicle units sold because more vehicles on the road suggest more potentially defective vehicles.
<!-- para 19 -->
To control for the firm's capital intensity, we use capital expenditures (CAPEX), normalized by firm assets ([Steven, Dong, and Corsi 2014](#bibr87-00222437221131568)); CAPEX includes investments for purchases, improvements, or maintenance of long-term assets to enhance the firm's efficiency or capacity.
For example, investing in fixed assets should enhance the firm's product quality and thus reduce the number of defective products and recalls.
However, high capital expenditures may limit the resources it has available for recalls and lobbying.
We account for the firm's research and development (R&D) intensity, or R&D expenditures divided by assets ([Kashmiri and Mahajan 2017](#bibr51-00222437221131568)); firms that invest more in R&D likely develop more products, which may affect recall likelihood.
Our model also includes a domestic dummy variable, which indicates whether the firm is listed on a U.S. stock market index (NYSE/NASDAQ).
We gauge the firm's age as well (natural log of the difference between observation year and firm's incorporation year).
The model controls for the presidential ruling party (Democratic/Republican) using fixed effects.
<!-- para 20 -->
Next, we address potential agency issues.
For example, each firm aims to maximize its market value, a goal that might not align with managers’ preferences to maximize their personal interests.
Self-interest could drive a top manager to pursue political action for private gain.
We cannot observe all lobbying activity and its outcomes ([Richter, Samphantharak, and Timmons 2009](#bibr80-00222437221131568)), so to account for potential agency issues, we use a measure of the agency costs of free cash flows (FCF).
If a firm has excess cash flows to finance projects efficiently, managers should be more likely to invest in projects that enhance their personal utility ([Jensen 1986](#bibr46-00222437221131568)).
Such concerns may be more prevalent in low-growth firms, which generally have substantial FCF for managers to invest.
Therefore, following [Jensen (1986)](#bibr46-00222437221131568) and [Doukas, Kim, and Pantzalis (2000)](#bibr29-00222437221131568), we proxy for agency costs with the interaction of a poor growth opportunities indicator and FCF, standardized by total assets; we measure FCF as operating income before depreciation minus the sum of taxes, interest expense, and dividends paid ([Lehn and Poulsen 1989](#bibr61-00222437221131568)).
Finally, a growth indicator equals 1 if the Tobin's q is less than 1 (poorly managed firm or poor growth opportunities), and 0 otherwise.
<!-- para 21 -->
We incorporate the quarterly advertising expenditures of each firm, which we gather from Kantar media data ([Ozturk, Chintagunta, and Venkataraman 2019](#bibr74-00222437221131568)).
Because media coverage of a recall likely influences firm decisions, we determine the number of news articles that report defects, consistent with previous research (e.g., [Tirunillai and Tellis 2012](#bibr93-00222437221131568)).
LexisNexis is a popular source of such information ([Borah and Tellis 2016](#bibr14-00222437221131568)).
We also source vehicle quality information from *Consumer Reports* at the model level (e.g., Accord), then use an average to aggregate these values to the firm level (consistent with the lobbying data).
Because vehicle quality likely correlates with the number of recalls, this variable enables us to account for the potential impact of quality on recalls.
Defects may take some time to appear, so we use ratings lagged by one quarter in the analysis.
<!-- para 24 -->
We begin by presenting model-free evidence for the relationship between lobbying expenditures and recalls.
We split the sample into low- and high-intensity lobbying groups, based on the mean value of the entire sample's lobbying expenditures, namely, US 0.59 million.
The high-intensity group, with values above the overall mean, includes 177 observations and exhibits mean lobbying expenditures of US 1.61 million.
The low-intensity group instead encompasses 399 observations, and its mean lobbying expenditures are US.13 million.
Because more complaints likely lead to recall action, we standardize the number of recalls for each group, by dividing by the corresponding number of complaints.
The pattern in [Figure 6](#fig6-00222437221131568) suggests a relationship between recalls and lobbying expenditures.
A t-test (M <sub>highintensity</sub>  =.002, M <sub>lowintensity</sub>  =.023, *p*  <.01) suggests that the number of standardized voluntary recalls is lower in the high-intensity lobbying group than the low-intensity group, which represents model-free evidence of a negative relationship between recalls and lobbying. [Figure 6](#fig6-00222437221131568) also suggests fewer standardized mandatory recalls for the high-intensity lobbying group (M <sub>highintensity</sub>  =.0003, M <sub>lowintensity</sub>  =.0008, *p*  <.01).
We repeat this analysis using the median value of expenditures (US$.21 million) and uncover a similar pattern (see [Figure 6](#fig6-00222437221131568)).
<!-- para 27 -->
We estimate the recall process ([Figure 1](#fig1-00222437221131568)) with an instrumental variable (IV) model and simultaneous equation system.
Additional specifications, including a nonlinear model, help ensure the robustness of the results.
<!-- para 29 -->
We could use ordinary least squares and exploit between- and within-data dimensions to establish the link of recall decisions and lobbying ([Wooldridge 2010](#bibr100-00222437221131568)), but such a model might suffer from an endogeneity bias, because the firm-level, time-varying variables correlate with both lobbying and product recalls, and fixed effects cannot account for them.
A failure to address endogeneity can lead to statistically inconsistent parameter estimates.
Solutions to address endogeneity include field experiments ([Johnson, Lewis, and Reiley 2017](#bibr15-00222437221131568)), natural experiments ([Shapiro 2018](#bibr85-00222437221131568)), and IVs ([Pattabhiramaiah, Sriram, and Sridhar 2018](#bibr75-00222437221131568)); we choose the latter.
With a two-stage least squares model (2SLS; [Wooldridge 2010](#bibr100-00222437221131568)), we attempt to identify a valid instrument that meets relevance and exclusion restrictions (with conceptual justification).
<!-- para 31 -->
Lobbying activities are strategic decisions for firms, which invest because they anticipate potential benefits.
An omitted variable bias, or endogeneity, might arise if a time-varying omitted variable influences the decisions to lobby and to recall, such as a firm's strategic philosophy toward regulatory risk management.
The prominence and dynamism of regulations across markets creates a situation in which the regulatory environment constitutes a primary risk for business ([Ernst & Young 2011](#bibr31-00222437221131568); [Ross 2005](#bibr26-00222437221131568)), and consulting agencies offer regulatory risk management products ([Dannemiller, DeWitt, and Gajjaria 2017](#bibr24-00222437221131568)).
In the automotive industry, dynamic factors such as product safety disputes (e.g., orders for unrepaired recalls; Federal Trade Commission 2017), societal developments (e.g., reducing greenhouse gas emissions; The White House 2012), or politically induced scenarios (e.g., appointment of new administrators; Laing 2019) all drive regulatory changes.
In turn, a link likely exists between a firm's regulatory risk management strategy and its lobbying.
For example, in anticipation of future recalls, firms might invest proactively in lobbying to influence key stakeholders and create safeguards.
More than 30 lobbyists worked for Toyota in 2009 (a year before its unintended acceleration recall) to represent its interests before Congress and federal agencies ([Krumholz and Levinthal 2010](#bibr18-00222437221131568)).
In 2014 (during an ongoing ignition switch recall debate), GM hired two new lobbying firms to assist with “product and safety recall issues” ([Tau 2014](#bibr91-00222437221131568)).
Other industries also exhibit ramped-up lobbying when regulatory scrutiny increases ([Tracy 2019](#bibr94-00222437221131568)).
Such a strategy, flowing from an organizational mindset that is embedded throughout the organization and based in managerial experience and business knowledge, is difficult to quantify.
The absence of a measure of regulatory risk management, which correlates with both recalls and lobbying, thus creates an omitted variable bias that raises endogeneity concerns ([Wooldridge 2010](#bibr100-00222437221131568)).
With 2SLS, we aim to identify an IV that meets the relevance and exclusion restrictions to address this concern.
<!-- para 33 -->
The quarterly aggregated political contributions of residents living in counties where a firm has its headquarters or production facilities provide a potential IV.
In the United States, individual contributors may donate to any political candidate or committee; the Federal Election Commission (FEC) maintains a database of all contributions.
For example, Toyota has a presence in seven counties (headquarters in Los Angeles County, California; plants in Madison County, Alabama; Gibson County, Indiana; Scott County, Kentucky; Union County, Mississippi; Bexar County, Texas; and Putnam County, West Virginia).[^12] We sum the individual contributions from these counties.
With the prediction that a firm with a larger geographical footprint is more likely to be active in lobbying at both its headquarters and plant locations, we gather headquarters and plant information for each firm from various sources (e.g., company websites, annual reports).
Then we search websites maintained by the Office of Policy Development and Research and Department of Agriculture to find county codes and corresponding zip codes for each county.
We enter these zip codes into the FEC website to identify individual contribution data over the nine-year study period.
<!-- para 35 -->
To satisfy the relevance criterion, the IV should correlate with the endogenous regressor, which is lobbying expenditures.
We anticipate that they correlate negatively: if residents who live in counties where a firm has its headquarters or production facilities increase (decrease) their contributions, firms’ lobbying expenditures should decrease (increase).
In general, a person might make political donations to signal political engagement or share views on issues related to local policies, jobs, infrastructure development, and so on; those issues might also be relevant to firms with a presence in those local counties.
When political donations increase, firms may be motivated to dedicate less money to lobbying activities, because they know their interests already are being represented by contributions in the political system.
Donations also fund the political ambitions of elected officials, so those officials likely account for the signaled interests of contributors in their legislative decisions.
As [Hill et al. (2013)](#bibr42-00222437221131568) determine, if more politicians already represent the interests of the citizens of a state in which a firm is present, the firm's need to hire lobbyists decreases.
If, instead, individual donations decrease, firms may be motivated to allocate more money to lobbying to ensure adequate representation of their interests.
Conceptually, this instrument appears to meet the instrument relevance criterion.[^13]
<!-- para 37 -->
The proposed instrument should not correlate with the omitted variable absorbed by the error term ([Wooldridge 2010](#bibr100-00222437221131568)).
Individual political contributions seem unlikely to exhibit any association with omitted variables (e.g., vehicle quality) that determine the recall decisions by a firm or regulator; rather, reasons to donate likely vary substantially across individual contributors ([Powell 2012](#bibr24-00222437221131568)).
Citizens usually make political contributions to express a personal political orientation or ideology ([Ansolabehere, De Figueiredo, and Snyder 2003](#bibr5-00222437221131568)) or out of a sense of civic duty; an environmentally conscious voter might contribute to a committee that is raising support for an environmental bill.
Others might donate to align with the norms of their networks of friends or professional relationships.
In all these cases, individual contributions are unlikely to be directly associated with omitted variables that determine automotive recalls, so conceptually, it also meets the exclusion restriction criterion.
<!-- para 39 -->
We assess the empirical validity of the IV by examining its strength and exogeneity, using different tests.
Before doing so, we remove contributions from individuals associated with any automotive firm, according to employer information included in FEC data.
We consider many variations of firms’ names (e.g., General Motor, General Motor Co., General Motors Corp., General Motors; see [Web Appendix Table W4](#supplementary-materials)) to identify employees.
Significant heterogeneity appears in individual contributions across firm locations.
The county-level median and maximum values of quarterly contributions are $81,912 and $74.90 million, respectively.
Over the nine-year study period (2008–2016), the sum of all individual contributions is $2.73 billion.
California's contribution, aggregated across its all locations, is the largest (48.9% of the total amount).
West Virginia records the lowest aggregated contributions.
Los Angeles County is the biggest contributor among all counties ($845.77 million).
<!-- para 40 -->
In [Table 4](#table4-00222437221131568), we report the first-stage results of the two-stage estimator, which show that our IVs are significant predictors of firm lobbying.
For both set of equations, the IV coefficients are significant and empirically support the proposed relationship with the endogenous variable.
A negative sign indicates that a greater (lower) degree of individual contributions lowers (increases) firms’ need to hire lobbyists.
For voluntary recalls, the F-test rejects the null hypothesis of weak instruments (statistic = 6.23 (d.f. = 2, 535), *p* <.05).
The first-stage equation also controls for other exogenous variables, such as firm-, year-, and quarter-level fixed effects.
A Wu–Hausman test suggests the presence of endogeneity in the system, in that it rejects the null hypothesis (statistic = 7.26 (d.f. = 1, 535), *p* <.05).
Furthermore, a Sargan–Hansen test ensures the validity of the instruments; it does not reject the null hypothesis that the instruments are exogenous and thus valid (statistic =.11 (d.f. = 1), n.s.).
We find similar statistics for mandatory recalls.
An F-test rejects the null hypothesis of weak instruments (statistic = 6.75 (d.f. = 2, 539), *p* <.05); the Wu–Hausman test suggests the presence of endogeneity (statistic = 5.29 (d.f. = 1, 539) *p* <.05); and a Sargan–Hansen test does not reject the null hypothesis that the instruments are exogenous (statistic =.93 (d.f. = 1), n.s.).
<!-- para 42 -->
<table><thead><tr><td></td><th colspan="4">A: Voluntary Recall</th><th colspan="4">B: Mandatory Recall</th></tr><tr><td></td><th colspan="2">First Stage</th><th colspan="2">Second Stage</th><th colspan="2">First Stage</th><th colspan="2">Second Stage</th></tr><tr><td></td><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th></tr></thead><tbody><tr><td>Intercept</td><td>.199</td><td>(1.912)</td><td>12.353***</td><td>(4.269)</td><td>−.13</td><td>(1.379)</td><td>−.587</td><td>(.920)</td></tr><tr><td>Contribution_hq</td><td>.0002</td><td>(.003)</td><td></td><td></td><td>.000003</td><td>(.003)</td><td></td><td></td></tr><tr><td>Contribution_plant</td><td>−.017***</td><td>(.005)</td><td></td><td></td><td>−.018***</td><td>(.005)</td><td></td><td></td></tr><tr><td>Lobbying</td><td></td><td></td><td>−2.473**</td><td>(1.004)</td><td></td><td></td><td>−.600***</td><td>(.223)</td></tr><tr><td>Complaints</td><td>−.03 × 10 <sup>−4</sup></td><td>(.0001)</td><td>.002</td><td>(.001)</td><td>−.04 × 10 <sup>−4</sup></td><td>(.0001)</td><td>.0004***</td><td>(.0001)</td></tr><tr><td>Deaths</td><td>−.007</td><td>(.014)</td><td>.072***</td><td>(.025)</td><td>−.01</td><td>(.014)</td><td>.005</td><td>(.008)</td></tr><tr><td>States</td><td>.002</td><td>(.011)</td><td>.01</td><td>(.029)</td><td>.003</td><td>(.011)</td><td>.004</td><td>(.009)</td></tr><tr><td>Rating</td><td>−.104</td><td>(.124)</td><td>−.917</td><td>(.603)</td><td>−.137</td><td>(.121)</td><td>−.135</td><td>(.155)</td></tr><tr><td>Firm size</td><td>.002</td><td>(.004)</td><td>−.01</td><td>(.015)</td><td>.0004</td><td>(.004)</td><td>−.005</td><td>(.004)</td></tr><tr><td>Domestic</td><td>1.280***</td><td>(.266)</td><td>2.113*</td><td>(1.129)</td><td>1.517***</td><td>(.228)</td><td>.749*</td><td>(.387)</td></tr><tr><td>Firm age</td><td>.016</td><td>(.382)</td><td>−1.806**</td><td>(.765)</td><td>.089</td><td>(.257)</td><td>.197</td><td>(.142)</td></tr><tr><td>Advertising</td><td>−.00003</td><td>(.0003)</td><td>.001</td><td>(.001)</td><td>.00003</td><td>(.0003)</td><td>−.001***</td><td>(.0002)</td></tr><tr><td>Media</td><td>.0003</td><td>(.001)</td><td>.001</td><td>(.003)</td><td>.0003</td><td>(.001)</td><td>.0001</td><td>(.001)</td></tr><tr><td>Rulingparty</td><td>.048</td><td>(.100)</td><td>−1.009**</td><td>(.493)</td><td>.08</td><td>(.095)</td><td>.189</td><td>(.133)</td></tr><tr><td>RD_intensity</td><td>.469</td><td>(1.461)</td><td>.324</td><td>(2.449)</td><td></td><td></td><td></td><td></td></tr><tr><td>CAPEX_intensity</td><td>−1.166</td><td>(.799)</td><td>−5.273*</td><td>(2.841)</td><td></td><td></td><td></td><td></td></tr><tr><td>Agency_costs</td><td>.024</td><td>(.298)</td><td>.424**</td><td>(.172)</td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>.576*</td><td>(.304)</td><td>−.473</td><td>(3.73)</td><td></td><td></td><td></td><td></td></tr><tr><td>Fixed effects (firm, year, quarter)</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Adjusted R <sup>2</sup></td><td colspan="2">.79</td><td colspan="2">.39</td><td colspan="2">.79</td><td colspan="2">.11</td></tr><tr><td>F-statistic</td><td colspan="2">54.752*** (d.f. = 40, 535)</td><td colspan="2">—</td><td colspan="2">60.261*** (d.f. = 36, 539)</td><td colspan="2">—</td></tr></tbody></table>
<!-- para 43 -->
*\*p*   *<*  *.*10*. \*\*p*   *<*.05*. \*\*\*p*   *<*  *.*01.
<!-- para 44 -->
*Notes:* Lobbying amount is the dependent variable in the first-stage equation.
Total number of observations is 576.
Contribution\_hq and Contribution\_plant are the instrumental variables and represent aggregated individual contributions at the firm's headquarters and plant locations, respectively.
Second-stage errors are clustered at the firm level, and they appear in parentheses.
<!-- para 46 -->
After identifying a valid instrument that meets the relevance and exclusion restrictions, we apply the 2SLS estimator.
We first estimate lobbying expenditures as a function of the instrument (individual contributions) and the other exogenous variables, then use the estimated value of lobbying expenditures in the second-stage regression for recalls.
The 2SLS includes the following specification for the firm:
$$
Lobbyin g_{iyq} = \gamma_{0} + \gamma_{1} Z_{iyq} + \gamma_{2} X V_{iyq} + \epsilon_{iyq} ,
$$
<!-- para 47 -->
(1 \\rm a)
<!-- para 48 -->
$$
Vol _ recal l_{iyq} = \beta_{0} + \beta_{1} Predicted _ lobbyin g_{iyq} + \beta_{2} X V_{iyq} + \vartheta_{iyq} .
$$
<!-- para 49 -->
(1\\rm b)
<!-- para 50 -->
[Equation 1a](#disp-formula1-00222437221131568) represents the first stage of the 2SLS, where Lobbying <sub>iyq</sub> is lobbying expenditures by firm i in quarter q of year y, and Z <sub>iyq</sub> is the instrument, which is exogenous in nature.
To satisfy instrument relevance, the coefficient γ <sub>1</sub> must be significant and nonzero. [Equation 1b](#disp-formula2-00222437221131568) represents the second stage, in which Z <sub>iyq</sub> does not appear.
To meet the exclusion restriction condition, Z <sub>iyq</sub> must not correlate with the error term ($E \left(\right.
Z_{iyq} \times \vartheta_{iyq} \left.\right) = 0$).
Then, Vol\_recall <sub>iyq</sub> refers to the number of voluntary recalls by firm i in quarter q of year y.
With XV, we represent covariates for voluntary recalls: recall-specific covariates (number of consumer complaints, reported deaths, and number of states where complaints were registered), firm-specific variables (CAPEX, R&D expenses, agency costs, quality rating, sales, total assets, firm age, advertising expenses, media coverage, and firm domestic dummy), and time-invariant factors (firm, quarter, year, and presidential ruling party fixed effects).
Firm-level fixed effects capture time-invariant unobserved factors (e.g., organizational culture, managers’ risk preferences).
Year-level and quarter-level fixed effects account for unobserved factors that vary over time and are common to all firms.
Thus, we can tease out any year-level fluctuations (e.g., economic cycles that influence all firms).
Controlling for time-invariant factors removes time-invariant between-level variation.
<!-- para 51 -->
The 2SLS specification for the regulator is as follows:
$$
Lobbyin g_{iyq} = \lambda_{0} + \lambda_{1} Z_{iyq} + \lambda_{2} X M_{iyq} + \epsilon_{iyq} ,
$$
<!-- para 52 -->
(1\\rm c)
<!-- para 53 -->
$$
Mand _ recal l_{iyq} = \alpha_{0} + \alpha_{1} Predicted _ lobbyin g_{iyq} + \alpha_{2} X M_{iyq} + u_{iyq} .
$$
<!-- para 54 -->
(1\\rm d)
<!-- para 55 -->
Here, Mand\_recall <sub>iyq</sub> is the number of mandatory recalls of firm i in quarter q of year y; XM includes covariates for mandatory recalls (consumer complaints, reported deaths, number of states where complaints were registered, quality rating, media coverage, advertising expenses, firm domestic dummy, presidential ruling party) and several time-invariant factors (firm, year, and quarter fixed effects); and Z <sub>iyq</sub> is the instrument, which must not correlate with the error term ($E \left(\right.
Z_{iyq} \times u_{iyq} \left.\right) = 0$), to meet the exclusion restriction condition.
<!-- para 57 -->
We can represent our moderation discussion with a set of equations (for ease of presentation, we do not include control variables):
$$
Recalls = \beta_{10} + \beta_{11} Lobbying + \beta_{12} Deaths + \beta_{13} Lobbying \times Deaths + \epsilon_{1} ,
$$
<!-- para 58 -->
(2)
<!-- para 59 -->
$$
Recalls = \beta_{20} + \beta_{21} Lobbying + \beta_{22} Media + \beta_{23} Lobbying \times Media + \epsilon_{2} ,
$$
<!-- para 60 -->
(3)
<!-- para 61 -->
$$
Media = \beta_{30} + \beta_{31} Deaths + \epsilon_{3} ,
$$
<!-- para 62 -->
(4)
<!-- para 63 -->
$$
Recalls = \beta_{40} + \beta_{41} Lobbying + \beta_{42} Deaths + \beta_{43} Lobbying \times Deaths + \beta_{44} Media + \beta_{45} Lobbying \times Media + \epsilon_{4} .
$$
<!-- para 64 -->
(5)
<!-- para 65 -->
[Equations 2](#disp-formula5-00222437221131568) and [^1] represent the moderating effect discussed in H <sub>2</sub> and H <sub>3</sub>, respectively. [Equation 4](#disp-formula7-00222437221131568) captures how Deaths may drive Media coverage.
Finally, [Equation 5](#disp-formula8-00222437221131568) represents the entire system (Models A and B) with main effects, moderating effects, and the indirect moderation of Deaths on the link between lobbying and recalls through Media.
Similar to the main analysis, we use instrumental variables for lobbying in this analysis too.
Like [Van Kollenburg and Croon (2021)](#bibr97-00222437221131568), we test for indirect moderation through the mediator according to whether:
- Deaths functions as a moderator when Media is not considered (i.e., β <sub>13</sub> ≠ 0).
- Deaths influences Media (i.e., β <sub>31</sub> ≠ 0).
- Media moderates the effect of Lobbying on Recalls (i.e., β <sub>45</sub> ≠ 0).
- The β <sub>43</sub> coefficient ([Equation 5](#disp-formula8-00222437221131568)) indicates empirical support for either partial indirect moderation (Model A) or full indirect moderation (Model B), such that
	- β <sub>43</sub> = 0 indicates a statistically nonsignificant direct moderating effect of Deaths in Model A (dotted arrow) and empirical support for full indirect moderation (Model B).
		- β <sub>43</sub> ≠ 0 and β <sub>43</sub> < β <sub>13</sub> indicate a significant partial direct moderating effect of Deaths in Model A (dotted arrow) and empirical support for Model A.

## results
<!-- para 2 -->
[Table 4](#table4-00222437221131568) contains the results for IV 2SLS model, with the number of recalls (voluntary and mandatory) as the dependent variable.
We predicted that automotive firms with more lobbying expenditures are less likely to initiate voluntary recalls.
In Panel A, we provide the second-stage results for the IV model.
In the voluntary recall equation, consistent with H <sub>1</sub>, the coefficient for the predicted value of lobbying expenditures is negative and significant (β <sub>lobbying</sub>  = −2.473, *p*  <.05).
The firm, year, and quarter fixed effects control for unobserved heterogeneity.
Defect severity (number of death reports) has a significant and positive coefficient (β <sub>deaths</sub>  =.072, *p*  <.01), indicating that more reported deaths due to defective vehicles increase the number of voluntary recalls.
The complaints variable (number of consumer complaints) has a positive coefficient.
Capital expenditures displays a significant and negative relationship with voluntary recalls (β = −5.273, *p*  <.10); a firm with more capital expenditures is less likely to initiate a voluntary recall.
Furthermore, older firms (β = −1.806, *p*  <.05) and nondomestic firms (β = 2.113, *p*  <.10) are less likely to initiate a recall action.
<!-- para 3 -->
In the mandatory recall specification (Table 4, Panel B), consistent with H <sub>1</sub>, the coefficient of the lobbying variable is significant and negative (β <sub>lobbying</sub>  = −.600, *p*  <.01), indicating that firms with higher lobbying expenditures are less likely to experience mandatory recalls.
The coefficient for consumer complaints is positive and significant (β <sub>complaints</sub>  =.0004, *p*  <.01); logically, more complaints trigger more mandatory recalls.
Nondomestic firms (β =.749, *p*  <.10) are less likely to face mandatory recalls.
<!-- para 4 -->
[Table 5](#table5-00222437221131568) presents the moderation effects.
Column 1 highlights that defect severity (number of death reports) moderates the effect of lobbying on recall decisions (β =.166, *p*  <.10); consistent with H <sub>2</sub>, more repeated deaths diminish the effect of lobbying on recall decisions.
Media coverage also appears to moderate lobbying's role (β =.029, *p*  <.01); consistent with H <sub>3</sub>, as media coverage increases, the recalling firm seems more hesitant to avoid a recall, which limits the influence of lobbying on the decision.
We find empirical evidence of a full indirect moderation effect too (β =.022, *p*  <.10).
Consistent with H <sub>4</sub>, the interaction between media and lobbying mediates the moderating effect of defect severity.
In the mandatory recall specification (Panel B), we find similar results for the moderating effects of both defect severity (H <sub>2</sub>: β =.066, *p*  <.10) and media coverage (H <sub>3</sub>: β =.006, *p*  <.10).
We do not find a statistically significant indirect moderation effect in mandatory recalls.
All models account for unobserved heterogeneity with time-invariant fixed effects.
<!-- para 6 -->
<table><thead><tr><td></td><th colspan="6">A: Voluntary Recalls</th><th colspan="6">B: Mandatory Recalls</th></tr><tr><td></td><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th><th>Est.</th><th>SE</th></tr></thead><tbody><tr><td>Intercept</td><td>9.027**</td><td>(3.988)</td><td>8.901</td><td>(5.324)</td><td>7.415</td><td>(4.436)</td><td>−1.661</td><td>(1.110)</td><td>−1.265</td><td>(1.275)</td><td>−1.585</td><td>(1.160)</td></tr><tr><td>Lobbying</td><td>−2.39***</td><td>(.837)</td><td>−2.109***</td><td>(.701)</td><td>−2.226***</td><td>(.701)</td><td>−.622***</td><td>(.212)</td><td>−.571***</td><td>(.174)</td><td>−.582***</td><td>(.139)</td></tr><tr><td>Complaints</td><td>.001</td><td>(.001)</td><td>.001</td><td>(.001)</td><td>.001</td><td>(.001)</td><td>.0004**</td><td>(.0002)</td><td>.0003**</td><td>(.0001)</td><td>.0002***</td><td>(.0001)</td></tr><tr><td>Deaths</td><td>−.180</td><td>(.129)</td><td>−.016</td><td>(.068)</td><td>−.255</td><td>(.187)</td><td>−.096*</td><td>(.055)</td><td>−.017</td><td>(.019)</td><td>−.065</td><td>(.046)</td></tr><tr><td>States</td><td>.014</td><td>(.029)</td><td>.016</td><td>(.031)</td><td>.019</td><td>(.031)</td><td>.006</td><td>(.009)</td><td>.006</td><td>(.010)</td><td>.007</td><td>(.009)</td></tr><tr><td>Rating</td><td>−.806</td><td>(.607)</td><td>−.694</td><td>(.628)</td><td>−.654</td><td>(.646)</td><td>−.108</td><td>(.141)</td><td>−.118</td><td>(.153)</td><td>−.105</td><td>(.143)</td></tr><tr><td>Firm size</td><td>−.009</td><td>(.014)</td><td>−.006</td><td>(.012)</td><td>−.005</td><td>(.012)</td><td>−.004</td><td>(.005)</td><td>−.004</td><td>(.005)</td><td>−.003</td><td>(.005)</td></tr><tr><td>Domestic</td><td>2.12</td><td>(1.292)</td><td>1.886</td><td>(1.366)</td><td>2.101</td><td>(1.611)</td><td>.852**</td><td>(.333)</td><td>.872**</td><td>(.386)</td><td>.896***</td><td>(.333)</td></tr><tr><td>Firm age</td><td>−1.484**</td><td>(.724)</td><td>−1.509</td><td>(.944)</td><td>−1.251</td><td>(.800)</td><td>.317*</td><td>(.169)</td><td>.24</td><td>(.195)</td><td>.295*</td><td>(.178)</td></tr><tr><td>Advertising</td><td>.0003</td><td>(.001)</td><td>−.001</td><td>(.002)</td><td>−.001</td><td>(.001)</td><td>−.001***</td><td>(.0002)</td><td>−.001***</td><td>(.0003)</td><td>−.001***</td><td>(.0003)</td></tr><tr><td>Media</td><td>.002</td><td>(.002)</td><td>−.019***</td><td>(.004)</td><td>−.014</td><td>(.010)</td><td>.0005</td><td>(.001)</td><td>−.004*</td><td>(.002)</td><td>−.004</td><td>(.003)</td></tr><tr><td>Rulingparty</td><td>−1.067**</td><td>(.474)</td><td>−1.180**</td><td>(.516)</td><td>−1.196**</td><td>(.487)</td><td>.172</td><td>(.127)</td><td>.171</td><td>(.146)</td><td>.165</td><td>(.138)</td></tr><tr><td>RD_intensity</td><td>.503</td><td>(2.153)</td><td>1.121</td><td>(3.038)</td><td>1.181</td><td>(2.637)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>CAPEX_intensity</td><td>−5.348*</td><td>(2.859)</td><td>−4.648*</td><td>(2.439)</td><td>−5.028*</td><td>(2.592)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Agency_costs</td><td>.394**</td><td>(.163)</td><td>.459***</td><td>(.154)</td><td>.427***</td><td>(.155)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Sales</td><td>−.359</td><td>(3.497)</td><td>.556</td><td>(3.555)</td><td>.522</td><td>(3.618)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Lobbying × Deaths</td><td>.166*</td><td>(.099)</td><td></td><td></td><td>.169</td><td>(.178)</td><td>.066*</td><td>(.038)</td><td></td><td></td><td>.034</td><td>(.044)</td></tr><tr><td>Lobbying × Media</td><td></td><td></td><td>.029***</td><td>(.007)</td><td>.022*</td><td>(.013)</td><td></td><td></td><td>.006*</td><td>(.004)</td><td>.005</td><td>(.005)</td></tr></tbody></table>
<!-- para 7 -->
*\*p*   *<*  *.*10*. \*\*p*   *<*.05*. \*\*\*p*   *<*  *.*01.
<!-- para 8 -->
*Notes*: Total number of observations is 576.
Every analysis includes several fixed effects (firm, year, and quarter).
Second-stage errors are clustered at the firm level, and they appear in parentheses.
<!-- para 10 -->
To test the robustness of the empirical results that highlight a significant association between lobbying and automotive recalls, we use several alternative tests.
For parsimony, we summarize the tests here; [Web Appendix C](#supplementary-materials) contains more details.
<!-- para 12 -->
Beyond the contemporaneous effect (quarterly) of lobbying, we also consider long-term carryover effects ([Web Appendix, Section C.1](#supplementary-materials)).
Due to the carryover effects of advertising, its long-term effect equals the cumulative influence on some outcome variable (e.g., brand choice) over several time periods ([Sethuraman, Tellis, and Briesch 2011](#bibr27-00222437221131568)).
Similarly, we create a lobbying stock variable that accounts for the diminished impact of previous years’ lobbying over time.
In a Koyck model ([Bass and Clarke 1972](#bibr6-00222437221131568)), lobbying's impact decays geometrically with time, so we can construct a stock variable and rerun the analysis with it, as a tactic to assess the long-term effects of lobbying. [Web Appendix Table W6](#supplementary-materials) displays these results (voluntary β <sub>lobbying</sub>  = −2.365, *p*  <.05; mandatory β <sub>lobbying</sub>  = −.569, *p*  <.01).
<!-- para 14 -->
We have generally assumed that the recall decision-making process for each entity (firm, regulator) is independent (even if conditional on observed covariates and time-invariant factors), with no correlation among errors.
To consider the possibility of a simultaneous equation system, we incorporate the potential correlation of the model errors for the firm and the regulator, while also correcting for endogeneity ([Web Appendix, Section C.2](#supplementary-materials)).
With a simultaneous equation model, we estimate firm and regulator models simultaneously, correlate their errors, and correct for the endogenous nature of lobbying.
The generalized method of moments estimator extends the traditional 2SLS estimator by allowing for heteroskedasticity and autocorrelation-consistent standard errors ([Wooldridge 2010](#bibr100-00222437221131568)). [Web Appendix Table W7](#supplementary-materials) contains the results (voluntary β <sub>lobbying</sub>  = −.2.687, *p*  <.01; mandatory β <sub>lobbying</sub>  = −.598, *p*  <.01).
<!-- para 16 -->
In an exogenous event setting ([Web Appendix, Section C.3](#supplementary-materials)), we seek an event that would affect a firm's lobbying activities but not be directly associated with its recalls.
The exogenous variation in lobbying then could reveal the relationship between lobbying and recalls.
To fulfill this objective, we explore the 2014 water crisis in Flint, Michigan, when tests showed that the city's water supply contained substantial amounts of lead.
Despite residents’ complaints, no official action followed, and residents, including nearly 9,000 children, drank lead-contaminated water for almost 18 months.
This health crisis caused a public outcry and sparked intense politics and lobbying activities; it also affected GM, which operates a factory in Flint.
Accordingly, the water crisis influenced its lobbying activities in the area but not its recalls.
When we check for variation in GM lobbying expenditures and recalls, as expected, we observe an increase in GM's lobbying.
Consistent with our previous results, we also observe a drop in the mean values of GM recalls (voluntary and mandatory) during this period.
The plot of the mean values for other firms, which were not affected by this crisis, provides a relative assessment.
Using a difference-in-differences method, we analyze the dual differences for GM (lobbying and recalls) relative to other firms’ pre- and postcrisis values.
The results of this relative assessment are consistent with our previous results.
<!-- para 18 -->
Another assessment accounts for the discrete, ordered nature of our outcome variable, using an ordered probit model ([Web Appendix, Section C.4](#supplementary-materials)).
That is, we define our outcome variable (number of recalls) as an ordered categorical variable that represents the recall decision of firm i in period t (i.e., Recall <sub>it</sub>  = 0 if there is no recall, Recall <sub>it</sub>  = 1 if there is one recall, Recall <sub>it</sub>  = 2 if there are two recalls, etc.).
The probability that an outcome variable falls in one of the categories is a linear function of the key covariates and error.
An additional (linear) model for the endogenous variable (lobbying) accompanies each nonlinear model.
We adopt a conditional mixed process model for this analysis ([Roodman 2009](#bibr81-00222437221131568); see also [Mallapragada, Chandukala, and Liu 2016](#bibr64-00222437221131568), [Malshe, Colicev, and Mittal 2020](#bibr66-00222437221131568); [Zheng et al. 2020](#bibr102-00222437221131568)).
It uses a simulated maximum likelihood algorithm to estimate two or more equations, and it offers the flexibility to specify multiple simultaneous equations, each of which may use a different dependent variable with unique distribution properties, including noncontinuous forms (e.g., binary, ordered).
In addition, conditional mixed process accounts for possible endogeneity in the system.
The results are consistent with our key findings ([Web Appendix Table W8](#supplementary-materials); voluntary β <sub>lobbying</sub>  = −1.271, *p*  <.05; mandatory β <sub>lobbying</sub>  = −.1.618, *p*  <.01).
<!-- para 19 -->
Finally, we ran several other analyses, for which we present the results in the [Web Appendix C](#supplementary-materials), including assessments of internal versus external lobbying, log specifications, campaign contributions, expanded complaints categories, additional covariates, lobbying issue-specific expenditures, and Congressional majority party fixed effects.

## discussion
<!-- para 2 -->
Firms use lobbying to build political connections and further their business interests ([Bertrand, Bombardini, and Trebbi 2014](#bibr12-00222437221131568)), which may have meaningful, direct implications for automotive recalls.
By combining research into lobbying and recalls, we uncover an interesting phenomenon: on average, an increase of $404,367 in lobbying expenditures is associated with one fewer voluntary recall.
A back-of-the-envelope calculation indicates potential benefits to the firm.
An average recall in our data set involves 235,638 vehicle units.
If we assume an average, conservative cost of $50 per recalled vehicle (e.g., defect repair, revenue loss), one fewer recall implies nearly $12 million in savings.
We also note that political influence might bias the regulatory agency's recall decisions.
Firms that spend more on lobbying face fewer mandatory recalls; approximately $1.66 million more in lobbying expenditures is associated with one fewer mandatory recall.
These results validate concerns raised in the Congressional Report ([Kirchhoff and Peterman 2010](#bibr54-00222437221131568)).
Our study also highlights an actionable lever, which stakeholders (e.g., consumers, advocacy groups) can use to counter the influence of lobbying in the crucial product defect decision process.
<!-- para 4 -->
These results have direct implications for the competitive market structures.
Recalls affect firms’ marketing and financial efforts ([Cleeren, Dekimpe, and Helsen 2008](#bibr9-00222437221131568); [Van Heerde, Helsen, and Dekimpe 2007](#bibr31-00222437221131568)) and can alter their market competitiveness.
At an extreme, firms might go bankrupt due to a recall (e.g., Topps Meat Company; Belson and Fahim 2007).
Any firm that aims to stay competitive does not want to face such adverse scenarios and may adopt strategies (including improvements to product quality) to avoid recalls.
Our results identify lobbying as an instrument that firms use to manage their regulatory environment, affect recall decisions, and maintain their competitiveness in a product-market (recall) context, with significant financial implications.
<!-- para 5 -->
Lobbying also can help create market entry barriers to new entrants ([Gutiérrez and Philippon 2019](#bibr39-00222437221131568)), and in a recall context, it might limit fair competition, with possible ripple effects in the market, such that preferential treatment to a firm due to lobbying can motivate other firms to engage in similar practices.
By drawing attention to this influence mechanism of lobbying for product recalls, our research could help promote an environment that encourages fair competition and lessens the likelihood of unwanted ripple effects on market structures.
<!-- para 6 -->
Product defects can lead to severe economic and physical losses (e.g., medical costs, death) for consumers.
The GM ignition switch defect recall was linked to 124 deaths (Isidore and Marsh 2014).
Therefore, our study has important implications for consumer welfare; any possible distortion in the recall decision process can directly affect consumers.
Our study also reveals an instrument that key stakeholders (e.g., consumers, safety advocacy groups) can use to diminish the negative impact of lobbying: media coverage of defects lessens its influence.
Because media firms, which are independent of the recall decision-making process, can exert meaningful effects, they should increase their coverage of defect reports.
Relevant entities such as consumer advocacy groups also should increase their media engagement.
The enhanced information salience that would result can lessen the impact of lobbying on recall decisions.
In this sense, our research provides a viable solution to an ongoing problem.
<!-- para 7 -->
On the bright side, lobbying enables market stakeholders to raise concerns with policy makers, but on its dark side, lobbying can unduly influence recall decisions.
In no way should our results be taken as a recommendation for firms to spend more money on lobbying to reduce recalls; managers should be mindful of the threat to consumer welfare ascribed to decision-making distortion.
Not initiating a recall can lead to short-term benefits (e.g., avoiding recall costs) but also consumer harm (e.g., accidents, injuries) and long-term costs (e.g., reputational damage, consumer lawsuits).
According to the triple-bottom-line perspective, the social impacts of business decisions must be just as important to firms as their financial impacts.
<!-- para 9 -->
Our research advances efforts to understand firms’ product-market decisions, both theoretically and empirically.
First, we apply a legitimacy perspective, whereas previous literature in marketing primarily has embraced an efficiency perspective.
The social fitness rationale we use represents a theory-based generalization; it may apply to other industry settings (e.g., pharmaceutical) with similar institutional and recall features (e.g., regulatory supervision).
We complement this legitimacy perspective with a political influence framework (iron triangle; [Freeman 1965](#bibr35-00222437221131568)) to explain firms’ behavior.
Second, our study contributes to regulatory capture literature by identifying an actionable lever that can help limit a firm's regulatory influence.
<!-- para 10 -->
Lobbying has always been a controversial topic, but the U.S. lobbying industry continues to grow steadily; in 2021, it earned $3.7 billion in revenue (O’Connell and Narayanswamy 2022).
The dark-side outcomes of such a massive and controversial industry have relevant implications for policy makers and regulators.
The design and implementation of an effective policy require a deep understanding of various stakeholders’ behaviors and responses.
Consistent with arguments presented in previous studies (e.g., [Stigler 1971](#bibr89-00222437221131568)), we find that the recall decision-making process may be susceptible to political influence, suggesting the need for policy makers to take a greater role in fostering an environment that discourages the dominance of interest groups (e.g., lobbyists) and limits threats to consumer welfare.
A recent example of such efforts is the inquiry by the Committee on Energy and Commerce about whether CPSC delayed corrective actions for defective products ([U.S. Congress 2019](#bibr30-00222437221131568)).
Our prior citations of news articles that report the dark side of lobbying in other contexts (e.g., insider financial market information, federal aid) reinforce the importance of our study's implications.
We encourage more checks and greater transparency by regulators, to diminish the likelihood of external influences on critical product-related decisions.
In a nutshell, our study highlights the complexity involved in firms’ recall decisions, beyond typical marketing and financial elements.
We encourage researchers to continue exploring other marketing contexts with such vast societal implications.
