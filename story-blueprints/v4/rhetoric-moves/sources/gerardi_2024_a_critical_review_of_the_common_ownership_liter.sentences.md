---
type: sentences-archive
citekey: "gerardi_2024_a_critical_review_of_the_common_ownership_liter"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\Gerardi 等 - 2024 - A Critical Review of the Common Ownership Literature.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# gerardi_2024_a_critical_review_of_the_common_ownership_liter 句子库存

## introduction
<!-- para 2 -->
Common ownership refers to situations in which investors own shares in multiple firms that compete in the same product market.
Over the past few decades, substantial growth in index funds and consolidation in the asset-management industry has contributed to a substantial rise in common ownership.
An established theoretical literature suggests that, under certain conditions, common owners can exert anticompetitive effects.
Inspired by both these factors, a rapidly growing academic literature has attempted to estimate the effects of common ownership on market outcomes.
<!-- para 3 -->
The seminal papers by Azar, Schmalz & Tecu (2018) and He & Huang (2017) were the first to present empirical evidence documenting that increased common ownership is associated with greater coordination and softer competition among commonly held product market rivals.
The findings attracted the attention of legal scholars and policy makers and swiftly generated calls for antitrust authorities to open formal investigations into the potentially anticompetitive effects of common ownership.
Proposals have ranged from strict enforcement of the Clayton Act (specifically Section 7) to challenges of any stock acquisition that results in a common set of investors owning significant shares in corporations that are horizontal competitors, to limits on institutional holdings in an industry (i.e., no more than 1% of the total size of the industry). [^1] Legislation restricting asset managers' ability to construct diversified portfolios would have severe consequences for the industry, individual investors, and potentially, the economy as a whole.
Regulators and funds would likely incur heavy monitoring costs to ensure that funds stay within the investment limits.
Fund families could be forced to split up so that they would not surpass proposed ownership limits; as a result, individual investors could find it difficult to construct diversified portfolios at low fees.
Firms could also face more severe principal-agent problems as funds are forced into governance passivity.
<!-- para 4 -->
The Azar, Schmalz & Tecu (2018) and He & Huang (2017) findings and the increased attention on the topic from policy makers and from industry spurred additional empirical research that tested for common ownership's effects on a bevy of economic outcomes across a broad set of industries.
These seminal studies also initiated an intense debate in the literature about whether the empirical evidence should be interpreted in a causal manner and, thus, whether there is any scope for a policy response.
This debate continues to rage, with new empirical evidence supporting both sides.
<!-- para 5 -->
In this article, we critically review the common ownership literature.
We begin with the theoretical literature, tracing the concept of common ownership back to the models of Rubinstein & Yaari (1983), Rotemberg (1984), and Bresnahan & Salop (1986).
We focus on the conditions that are necessary for common ownership to result in anticompetitive effects in product markets.
We note that these conditions are at odds with the typical assumptions imposed in mainstream corporate finance theory regarding the objectives of firm managers (see, for instance, Jensen & Meckling 1976; Hart & Holmstrom 1987; Holmstrom & Milgrom 1987; Hart 1997).
<!-- para 6 -->
We then turn to how the literature has measured common ownership, focusing on the Modified Herfindahl–Hirschman Index (MHHI) that was first developed by Bresnahan & Salop (1986) and later extended by O'Brien & Salop (2000).
While the MHHI is one of the most common measures employed in the empirical literature, there are numerous challenges involved in its construction.
We also provide a brief discussion of some of the alternative measures that have been developed to avoid the shortcomings of the MHHI.
<!-- para 7 -->
Next, we discuss the various ways in which the literature has attempted to overcome endogeneity concerns and thereby identify the causal effects of common ownership on economic outcomes.
Since investment decisions are endogenous, it is very hard to separately identify the effects of ownership on firm performance from the effects of expected performance on investment.
The literature has focused mainly on mergers between financial institutions as well as reconstitutions of the Russell 1000/2000 Index and/or additions to the S&P 500 Index to generate pseudorandom variation in common ownership.
We critically assess these methods borrowing heavily from the arguments of Lewellen & Lowry (2021).
<!-- para 8 -->
We continue by summarizing the different mechanisms posited in the literature for how common ownership can exert causal effects on market competition.
We divide the mechanisms into two broad types, which we label direct and indirect channels.
Direct channels refer to explicit communication between investors and firm managers.
Examples include board meetings and shareholder elections.
In contrast, indirect channels do not involve explicit collusion.
The indirect channel that has received the most attention in the literature involves institutional investors providing managers with weak incentives to compete, for example, via the design of compensation schemes (Anton et al. 2023).
<!-- para 9 -->
Finally, we survey the current state of the empirical literature.
In Table 1, we provide a listing of all empirical papers and summarize for each paper the principal outcomes analyzed, whether the results show a significant effect of common ownership on that outcome, and the paper's approach toward addressing endogeneity. [^2] Additionally, Figure 3 facilitates a comparison across papers of the effects of common ownership on different outcome variables.
After reviewing this literature, we conclude that there is only weak evidence supporting the hypothesis that increased common ownership exerts a negative causal effect on product market competition among the studies that convincingly address endogeneity concerns.
<!-- para 10 -->
This article is not the first to review the common ownership literature.
Schmalz (2018) reviewed the theoretical, legal, and early empirical literature related to common ownership.
In the 5 years or so since that paper was published in the pages of this journal, the empirical literature has grown tremendously, and importantly, evidence has emerged refuting the idea that common ownership exerts anticompetitive effects.
We provide an update of the empirical literature and assess the available evidence with a critical eye toward measurement and identification issues.
<!-- para 11 -->
The balance of this article is organized as follows.
In Section 2, we review the theoretical studies that motivated the empirical literature on common ownership.
Section 3 summarizes the most frequently employed common ownership measures and presents the numerous issues associated with taking those measures to the data.
In Section 4, we critically discuss the primary identification strategies used to measure causal effects of common ownership on firm and market outcomes.
Section 5 presents the causal mechanisms that the literature has highlighted, focusing on both direct and indirect communication channels.
In Section 6, we survey the current state of the empirical literature, focusing on the identification debate that has emerged in recent years and briefly discussing results across different settings—for example, private versus public firms.
Finally, we provide concluding remarks in Section 8.
<!-- para 13 -->
In this section, we review the relevant theoretical literature that motivated concerns about adverse competitive effects of common ownership.
This literature spans the fields of finance and industrial organization.
Our goal is not to produce an exhaustive list of studies but rather to discuss the most influential papers.
We start by documenting the theoretical origins of the common ownership concept and then trace the evolution of the theoretical literature to the present day.
We explain some of the key assumptions shared by all of the relevant models, provide a critical discussion of whether these assumptions are justified, and discuss their implications for applied research.
<!-- para 15 -->
<table border=1><tr><td>Study</td><td>Principal outcome(s)</td><td>Find effect?</td><td>Addressing endogeneity</td><td>Industry/sector</td><td>Sample period</td></tr><tr><td>Adler &amp; Mirkov (2023)</td><td>Profits, as a function of firm corporate governance and industry competition</td><td>Yes (-), when government is weak and competition is soft</td><td>NA</td><td>Public firms</td><td>1989–2012</td></tr><tr><td>Azar, Raina &amp; Schmalz (2022)</td><td>Depository interest rates</td><td>Yes (+)</td><td>Index fund ownership</td><td>Banking</td><td>2003–2013</td></tr><tr><td>Azar, Schmalz &amp; Tecu (2018)</td><td>Airline ticket prices</td><td>Yes (+)</td><td>Fixed effects; Blackrock-BGI merger</td><td>Airline</td><td>2001–2014</td></tr><tr><td>Backus, Conlon &amp; Sinkinson (2021a)</td><td>Prices, markups</td><td>No</td><td>Structural/GMM</td><td>Cereal</td><td>2007–2016</td></tr><tr><td>Bindal &amp; Nordlund (2022)</td><td>Gross margin, profitability</td><td>Yes (+), among firms with more similar products</td><td>Financial institution mergersa</td><td>Public firms</td><td>1988–2019</td></tr><tr><td>Boller &amp; Morton (2020)</td><td>Abnormal returns of product market rivals, when common ownership increases</td><td>Yes (+)</td><td>S&amp;P 500 Index additions</td><td>Public firms</td><td>2000–2017</td></tr><tr><td>Brooks, Chen &amp; Zeng (2018)</td><td>M&amp;A activity</td><td>Yes (+)</td><td>Russell Index reconstitution</td><td>Public firms</td><td>1984–2014</td></tr><tr><td>Chen et al. (2023)</td><td>Insider trading profits</td><td>Yes (-)</td><td>Financial institution mergersa</td><td>Public firms</td><td>1997–2015</td></tr><tr><td>Dennis, Gerardi &amp; Schenone (2022a)</td><td>Airline ticket prices</td><td>No</td><td>Fixed effects; placebo tests</td><td>Airline</td><td>2001–2014</td></tr><tr><td>Freeman (2024)</td><td>Duration, strength, and value of supply chain relationships</td><td>Yes (+)</td><td>Financial institution mergersa</td><td>Public firms</td><td>1976–2010</td></tr><tr><td>Gao et al. (2022)</td><td>Opportunistic earnings management by supplier firms</td><td>Yes (-)</td><td>The 2003 mutual fund scandal</td><td>Public firms that represent suppliers</td><td>1980–2016</td></tr><tr><td>Geng, Hau &amp; Lai (2020)</td><td>Patent citation counts, patent litigation</td><td>Yes: citations (+), litigation (-)</td><td>Fixed effects</td><td>Public firms with 1+ patents</td><td>1991–2017</td></tr><tr><td>Gutiérrez &amp; Philippon (2017)</td><td>Investment</td><td>Yes (-)</td><td>NA</td><td>Public firms</td><td>1970–2016</td></tr><tr><td>He &amp; Huang (2017)</td><td>Market share growth, M&amp;A activity</td><td>Yes (+)</td><td>Financial institution mergers</td><td>Public firms</td><td>1980–2014</td></tr><tr><td>He, Huang &amp; Zhao (2019)</td><td>Votes against management on shareholder proposals</td><td>Yes (-)</td><td>Financial institution mergers</td><td>Public firms</td><td>2003–2012</td></tr><tr><td>He, Li &amp; Yeung (2020)</td><td>Accrual-based earnings management</td><td>Yes (-)</td><td>Financial institution mergers</td><td>Public firms</td><td>1980–2014</td></tr></table>
<!-- para 16 -->
(Continued)
<!-- para 18 -->
<table><tr><td>Study</td><td>Principal outcome(s)</td><td>Find effect?</td><td>Addressing endogeneity</td><td>Industry/sector</td><td>Sample period</td></tr><tr><td>Kennedy et al. (2017)</td><td>Airline ticket prices</td><td>No</td><td>Blackrock–BGI merger;<br>Russell Index 1000 membership; structural/GMM estimation</td><td>Airline</td><td>2001–2014</td></tr><tr><td>Kimi, Lee &amp; Shen (2023)</td><td>Product market fluidity, investment</td><td>Yes (+), among sectors with high propensity for knowledge spillovers</td><td>Financial institution mergers$^{a}$</td><td>Public firms</td><td>1997–2017</td></tr><tr><td>Koch, Panayides &amp; Thomas (2021)</td><td>Industry-level markups, prices, and margins</td><td>No</td><td>Financial institution mergers</td><td>Public firms</td><td>1995–2012</td></tr><tr><td>Kostovetsky &amp; Manconi (2020)</td><td>Patent citations</td><td>Yes (+)</td><td>Financial institution mergers;$^{a}$ Russell Index reconstitutions</td><td>Public firms with 1+ patents</td><td>1980–2010</td></tr><tr><td>Lewellen &amp; Lowry (2021)</td><td>ROA, R&amp;D mergers</td><td>No</td><td>Financial institution mergers$^{a}$</td><td>Public firms</td><td>1980–2013</td></tr><tr><td>Newham, Seldeslachts &amp; Banal-Estanol (2022)</td><td>Generic drug entry</td><td>Yes (-)</td><td>Membership in Dow Jones Pharma Index</td><td>Pharmaceutical</td><td>2004–2014</td></tr><tr><td>Park et al. (2019)</td><td>Voluntary disclosure</td><td>Yes (+)</td><td>Financial institution mergers</td><td>Public firms</td><td>1999–2015</td></tr><tr><td>Peng, Yin &amp; Zhang (2023)</td><td>Accounting comparability</td><td>Yes (+)</td><td>Financial institution mergers</td><td>Public firms</td><td>1988–2017</td></tr><tr><td>Ramalingegowda, Uike &amp; Yu (2021)</td><td>Accrual-based earnings management</td><td>Yes (-)</td><td>Financial institution mergers</td><td>Public firms</td><td>1989–2015</td></tr><tr><td>Riva (2022)</td><td>Markups in upstream versus downstream industries</td><td>Yes (- in upstream industries; + in downstream industries)</td><td>Financial institution mergers</td><td>Public firms</td><td>1985–2017</td></tr><tr><td>Schnalz &amp; Xie (2022)</td><td>Entry by generic drug manufacturers and settlements of patent lawsuits to delay generic drug entry</td><td>Yes (+)</td><td>Blackrock–BGI merger</td><td>Pharmaceutical</td><td>2003–2017</td></tr><tr><td>Torshizi &amp; Clapp (2021)</td><td>Seed prices</td><td>Yes (+)</td><td>Blackrocks investments in BASF (a major agrochemical producer); structural break analysis</td><td>Seed</td><td>1997–2017</td></tr><tr><td>Xie &amp; Gerakos (2020)</td><td>Settlements of patent lawsuits to delay generic drug entry</td><td>Yes (+)</td><td>Blackrock–BGI merger</td><td>Pharmaceutical</td><td>2003–2017</td></tr></table>
<!-- para 19 -->
Abbreviations: BGI, Barclays Global Investors; GMM, generalized method of moments; NA, not applicable; ROA, return on assets.
<!-- para 21 -->
We trace the theoretical literature on common ownership back to two early studies by Rubinstein & Yaari (1983) and Rotemberg (1984).
Both papers develop models that assume a perfectly competitive stock market, where investors trade shares in firms that are product market rivals.
Rubinstein & Yaari (1983) begin with the assumption that product markets are competitive. [^3] In the model, shareholders' trades are strategically targeted at redistributing firm payoffs across shareholders and maximizing the joint overall payoffs.
The Nash equilibrium outcome from these strategic trades results in collusion in the product market.
In contrast, Rotemberg (1984) develops a model where capital market investors' motivation to trade shares is to achieve a well-diversified portfolio.
In doing so, they invest in firms that are product market rivals.
Taking this as given, firm managers choose output levels that maximize the return of their shareholders' portfolios, in proportion to each investor's ownership. [^4]
<!-- para 22 -->
While both models predict lower equilibrium output, compared to the level that would result if firm managers competed against other firms to maximize firm value, there is an important distinction.
In the model by Rubinstein & Yaari (1983), cooperation is the result of shareholders trading in a perfectly competitive stock market with the explicit objective of creating a collusive product market.
In contrast, in Rotemberg's (1984) model, cooperation represents managers' optimal response given shareholders' diversified portfolios. [^5]
<!-- para 23 -->
A related literature emerged in the industrial organization field with the early work by Bresnahan & Salop (1986).
The model developed in the paper focuses on the competitive effects of partial (or cross) ownership, which refers to the case when a firm purchases some fraction of equity in a product market rival or when two or more competing firms jointly invest in a venture that operates in the same market. [^6] The paper shows that, in such cases, each firm's value-maximizing objective function includes its own firm's profits as well as the value of its holdings in the competing firm or joint venture (in which it owns a share).
For various levels of financial interests and control arrangements, (i.e., different forms of cross-ownership/partial mergers), Bresnahan & Salop (1986) develop a measure that quantifies the extent of cross-ownership in a market, referred to as the MHHI.
The paper uses this measure to study anticompetitive effects arising from cross-ownership/joint ventures/horizontal mergers.
The recent empirical literature adopts this measure to gauge the anticompetitive effects of common ownership.
We discuss the potential challenges with this approach in the next section.
<!-- para 24 -->
Gerardi • Lowry • Scenone
<!-- para 25 -->
The more recent theoretical work of Azar (2012) revived interest in the effects of common ownership.
The paper develops a model of oligopolistic competition with risk-neutral investors, where shareholders vote on every firm action and managers make decisions based on majority votes.
Thus, instead of managers having an objective of maximizing firm value, shareholders (who may own multiple competitor firms in their portfolios) effectively dictate decisions that managers implement.
This leads to an equilibrium where managers maximize a weighted average of shareholder portfolio returns, resulting in higher markups and less efficient outcomes in the product market.
This theory suggests that the degree of competition should be measured by an MHHI, in which managers internalize diversified shareholders' objective functions; this MHHI is similar to the one developed by Bresnahan & Salop (1986).
An important result from the work by Azar (2012) is the common ownership trilemma, which states that complete portfolio diversification by investors, perfect alignment of interest between managers and owners, and perfect competition are not jointly attainable.
It is possible to achieve at most two of the three.
In sum, this trilemma implies that it is not possible to separate financial policy from competition policy. [^7]
<!-- para 26 -->
The common ownership trilemma highlights a key characteristic shared by all theoretical models predicting that common ownership will cause anticompetitive behavior: These models depart from the standard assumption in the economics and finance literature that managers' actions are geared toward maximizing their firm's value, given the competitive environment they face in the product market.
Instead, the models assume that managers maximize the portfolio returns of their firms' shareholders, which results in managers colluding with product market rivals.
Critically, this assumption directly violates the Fisher separation theorem, which states that a firm's investment choices are separate from shareholders' investment preferences (see, e.g., Romano 2021).
In Section 2.2, we discuss some of the potential problems associated with these key modeling assumptions.
<!-- para 28 -->
There are key disconnects between the assumptions in the models developed by Rubinstein & Yaari (1983), Rotemberg (1984), Bresnahan & Salop (1986), and Azar (2012) and what we observe in reality.
<!-- para 29 -->
The first disconnect relates to principal–agent conflicts.
In the models discussed above, the benevolent manager knows each shareholder's preferences and acts upon them. [^8] This assumes away both asymmetric information and agency problems between managers and shareholders. [^9] Yet, these issues are so palpable in the real world that an entire field of study has evolved around the design of governance mechanisms and managerial contracts geared at aligning managerial incentives with those of firm owners.
We observe these contracts and mechanisms implemented across firms around the world. [^10]
<!-- para 32 -->
Colored boxes denote firms included in Vanguard's portfolio during the first quarter of 2022.
Firms within each industry, as denoted by being within a colored box, compete against each other in the product market.
The tan box in row 1 includes firms in the oil and gas industry.
The green box spanning rows 2 and 3 includes firms in the airline industry; this industry uses output from the oil and gas industry as an input in their production function.
The blue and lavender boxes in row 4 include firms in the technology industry (Dell, Apple, and Microsoft) and in the used car retailing industry (CarMax and Carvana), respectively; these firms use airline services to transport their employees.
The boxes on the right-hand side of the figure, and the red arrows within each of these boxes, denote the proposed effect of common ownership for each industry.
Common ownership in the oil/gas industry would cause oil prices to increase (top row).
This would cause jet fuel costs to increase for the airline industry (middle rows), which, in turn, would lead to an increase in airline ticket prices for other industries (last row).
The takeaway from this figure is that it is unclear whether a shareholder like Vanguard with a diversified portfolio across industries would benefit from inducing softer competition in a single industry, here the oil and gas industry.
Higher markups in that industry could be offset by increased costs of firms in downstream sectors.
<!-- para 33 -->
Second, even if firm managers could figure out how to overcome asymmetric information and agency problems, there is still the question of whether it is optimal for institutional investors to foster collusion among product market rivals within an industry, given that they hold diversified portfolios that include stocks across a wide range of industries.
Inducing collusion in one industry, resulting in higher markups within that industry, would lower the investor's returns on firms that purchase inputs from that industry, generating an ambiguous effect on overall portfolio returns.
<!-- para 34 -->
We present a simple example in Figure 1 to highlight the issue.
Consider a subset of firms in Vanguard's portfolio during the first quarter of 2022.
Vanguard invested in product market rivals within the oil and gas industry (e.g., Exxon, $30.1 billion; Hess,$3.3 billion; Chevron, $27.3 billion), product market rivals within the airline industry (e.g., Delta,$2.7 billion; Southwest, $2.9 billion; United,$1.6 billion), and various firms across other industries (e.g., Microsoft, $191.6 billion; Apple,$221.8 billion).
If Vanguard induces collusion between Exxon, Hess, Chevron, and other oil and gas industry firms in its portfolio, the higher average markups in the industry would negatively affect the operating costs and profits of any firm that uses oil and gas as an input, such as an airline.
If Vanguard also induces collusion among the ten airlines it holds in its portfolio, the higher airline ticket prices could adversely impact the operating costs and profits of any firm in Vanguard's portfolio that purchases airline services, such as Exxon and Chevron; CarMax and Carvana; Microsoft and Apple, for example.
<!-- para 35 -->
In sum, it is unclear whether a shareholder with a diversified portfolio across industries would benefit from inducing softer competition in a single industry.
Higher markups in that industry could be offset by increased costs of firms in downstream sectors, with the net effect depending on the investor's portfolio composition. [^11]
<!-- para 36 -->
The third disconnect between the assumptions underlying the theory and reality relates to a manager's (in)ability to implement multiple objective functions.
Each shareholder holds a portfolio of stocks, with a composition uniquely tailored to the investor's risk tolerance and objectives.
For a firm manager, maximizing the returns of one shareholder's portfolio is likely to conflict with maximizing those of another shareholder's portfolio.
The manager must find a mechanism to satisfy the heterogeneous preferences of all shareholders, or at least a mechanism to aggregate shareholder preferences under majority rule.
However, this is a task economists consider impossible, as demonstrated by the Arrow impossibility theorem and the Condorcet paradox. [^12] Jensen (2000), focusing on a shareholder value perspective, reaches similar conclusions: "It is logically impossible to maximize in more than one dimension at the same time unless the dimensions are monotone transformations of one another" (p. 4).
<!-- para 37 -->
One potential solution to the multiple objective function conundrum emerges if one investor is sufficiently powerful to elevate her preferences over those of other shareholders.
But then, if the manager capitulates to this investor, the resulting collusive outcome would no longer represent the manager's optimal response to the objectives of all shareholders.
As a result, this one investor would need a way to keep managerial behavior in line with her objectives.
It is unclear whether institutional investors have credible and enforceable punishments to prevent managers from deviating. [^13] If, instead, managers follow the traditional objective of maximizing firm value through competition with other firms, this multiple objective problem is avoided.
As Jensen (2000) states, "Maximizing the total value of the firm...is one objective function that will resolve the tradeoff problem among multiple constituencies" (p. 5).
As such, the manager can fulfill her fiduciary duties to all shareholders.
<!-- para 39 -->
We turn now to a discussion of the measures of common ownership that have been employed in the literature.
We begin in Section 3.1 with the definition of MHHI, as this represents the theoretical foundation of this literature.
This measure was first derived by Bresnahan & Salop (1986) and later generalized by O'Brien & Salop (2000).
In Section 3.2, we discuss some of the difficulties in empirically constructing the common ownership component of MHHI.
Finally, in Section 3.3, we overview several alternative measures of common ownership that have been used in the literature.
<!-- para 41 -->
As reviewed in Section 2, MHHI is derived from the first-order conditions of the manager's optimization problem, which is to maximize the weighted value of the portfolio of each one of the firm's shareholders.
These portfolios comprise shares in the manager's firm as well as shares in other firms, including the manager's product market rivals.
<!-- para 42 -->
Formally, owner i's total profit is given by the weighted average of the profits of all firms k in i's portfolio,  $\sum_k \beta_{ik} \cdot \pi_k(x_k)$, where  $\beta_{ik}$ is owner i's equity stake (cash flow rights) in firm k and  $\pi_k(x_k)$ is firm k's profit, which is a function of k's output  $x_k$.
The manager of firm k chooses output to
<!-- para 43 -->
maximize the weighted sum of the profits accruing to owners of firm k from their holdings in firm k as well as their holdings in firms  $j \neq k$, where the weights are the control rights that owner i has over firm k,  $\gamma_{ik}$.
Thus, the optimization problem faced by k's manager is
<!-- para 44 -->
$$ Max_{x_{k}}\sum_{i}\gamma_{ik}\cdot\left(\beta_{ik}\cdot\pi_{k}(x_{k},x_{j})+\sum_{j\neq k}\beta_{ij}\cdot\pi_{j}(x_{k},x_{j})\right) $$
<!-- para 45 -->
1.
<!-- para 46 -->
$$ Max_{x_{k}}=\sum_{i}\gamma_{ik}\cdot\sum_{j}\beta_{ij}\pi_{j}(x_{j},x_{k}). $$
<!-- para 47 -->
2.
<!-- para 48 -->
Following Backus, Conlon & Sinkinson (2019) and Kennedy et al. (2017), this can be rearranged as
<!-- para 49 -->
$$ Max_{x_{k}}=\pi_{k}(x_{j},x_{k})+\sum_{j\neq k}\overbrace{\left(\frac{\sum_{i}\gamma_{ik}\cdot\beta_{ij}}{\sum_{i}\gamma_{ik}\cdot\beta_{ik}}\right)}^{\omega_{jk}}\cdot\pi_{j}(x_{j},x_{k}). $$
<!-- para 50 -->
3.
<!-- para 51 -->
The weight that firm $k$'s manager places on profits from firms $j \neq k$ is $\omega_{jk} \equiv \frac{\sum_{i} \gamma_{ik} \cdot \beta_{ij}}{\sum_{i} \gamma_{ik} \cdot \beta_{ik}}$, the value to firm $k$ of a $1$ profit generated by firm $j$.
<!-- para 52 -->
The MHHI is derived from the first-order conditions of this optimization problem.
As shown in Equation 4, the MHHI is the sum of the traditional Herfindahl–Hirschman Index (HHI) and an additional common ownership term, which we refer to as MHHIΔ,
<!-- para 53 -->
$$ MHHI=\overbrace{\sum_{j,k\neq j}^{HHI}\underbrace{s_{j}\cdot s_{k}}_{Market shares,\text{firms }j,k}}^{Common ownership:MHHI\Delta}+\overbrace{\sum_{j}\sum_{k\neq j}\underbrace{\left(\frac{\sum_{i}\gamma_{ij}\cdot\beta_{ik}}{\sum_{i}\gamma_{ij}\cdot\beta_{ij}}\right)}_{Investor i's ownership(\beta)and control(\gamma)}\underbrace{s_{j}\cdot s_{k}}_{Market shares}}^{Market shares}. $$
<!-- para 54 -->
4.
<!-- para 55 -->
The traditional HHI term measures the extent of product concentration in an industry, it is bounded by 0 (no firms in the market) and 10,000 (a monopolist serves the market) and higher values are associated with higher market concentration and presumably lower competition.
MHHIΔ measures the additional concentration due to common ownership.
It has a lower bound of 0, and Azar, Schmalz & Tecu (2018) document a range of 0 to nearly 6,000 in their 2001–2014 sample period.
<!-- para 57 -->
Taking MHHIΔ in Equation 4 to the data requires identifying three critical inputs.
First, information on each investor i's equity holdings (cash flow rights) across all firms j in i's portfolio,  $\beta_{ij}$.
Second, information on the weights that the firm places on each investor i's total profits,  $\gamma_{ij}$.
This entails identifying the amount of control that investor i has in firm j and all other firms  $k \neq j$. [^14] Finally, information on each firm j's market shares,  $s_j$.
We discuss how the literature has measured each of these inputs.
<!-- para 58 -->
3.2.1.
Ownership stakes: investor i's equity holding in firm j,  $\beta_{i,j}$.
Obtaining information on an investor's equity holdings in a particular firm is not as straightforward as it might seem.
First,
<!-- para 59 -->
holdings are generally unavailable for most retail minority investors and, thus, are excluded from most studies.
A rationalization for excluding retail investors in the construction of MHHI is that they hold negligible amounts of equity and control in any given firm; therefore, their contribution to common ownership is essentially zero ( $\beta_{ik} \cdot \gamma_{ik} \approx 0$).
However, as Backus, Conlon & Sinkinson (2019) show, ignoring retail investors can lead to unrealistic outcomes, such as a firm weighting a competitor's profits by an amount that is multiple times larger than the weight the firm places on its own profits. [^15]
<!-- para 60 -->
Holdings by company insiders (e.g., officers, directors, and anyone owning 10% or more of a firm's shares) are available through other filings by the US Securities and Exchange Commission (SEC); however, these holdings are ignored in most studies.
<!-- para 61 -->
Finally, holdings for large institutional investors can be readily compiled since the SEC mandates that all institutional investment managers with at least $100 million in assets under management disclose equity holdings in Form 13F.
However, holdings are measured imprecisely, as reported by Ben-David et al. (2021) and Backus, Conlon & Sinkinson (2019).
<!-- para 62 -->
3.2.2.
Shareholder control: investor i's control over firm j,  $\gamma_{i,j}$.
The key issue is how to measure and quantify the extent of control. [^16] The theoretical literature has identified two channels through which shareholders can exert control.
The first is through exit or the threat thereof (see, e.g., Admati & Pfleiderer 2009; Edmans 2009; Edmans & Manso 2011).
Critically, the exit channel is not a feasible method of control for the many large common owners who are index funds.
<!-- para 63 -->
The second channel is through voice (Hirschman 1970), which includes shareholders' votes and shareholders' communications with management.
However, proposals up for vote do not relate to firm operations.
Thus, it is unclear how voting could lead to anticompetitive behavior. [^17] Furthermore, due to the risk of antitrust litigation, it seems unlikely that common owners would explicitly instruct management to compete less aggressively.
As suggested by Anton et al. (2023), the voice channel may play a greater role through a lack of action: Common owners may facilitate anticompetitive behavior by failing to pressure firms to compete aggressively, for example, by agreeing to compensation contracts that lack strong incentive structures.
<!-- para 64 -->
The empirical common ownership literature has focused on voting as a measure of shareholder control.
Azar, Schmalz & Tecu (2018) use voting rights designations recorded in 13F filings, where shareholder i reports “sole,” “none,” or “shared” voting rights.
The paper sets institution i’s control of firm j equal to the number of shares over which i declares it has sole or shared voting rights divided by the total number of firm j’s outstanding shares.
Kennedy et al. (2017) and Koch, Panayides & Thomas (2021) follow a similar approach.
However, Dennis, Gerardi & Schenone (2022a) show that these voting designations are classified inconsistently both across and within institutions over time, likely due to the vague definitions and unclear reporting instructions provided by the SEC.
Moreover, the authors show that Azar, Schmalz & Tecu’s (2018) results are sensitive to which voting designations are used to measure shareholder control.
<!-- para 65 -->
There are also questions regarding the extent to which voting rights, even if perfectly measured, capture relevant control rights.
First, as noted above, items up for vote are generally unrelated to
<!-- para 66 -->
a firm's competitive decisions.
Second, control rights may be a nonlinear function of voting rights.
For example, a doubling of voting rights may reflect more than a doubling of control rights, as discussed by Backus, Conlon & Sinkinson (2021b).
<!-- para 67 -->
3.2.3.
Market shares:  $s_j$ and  $s_k$.
In the construction of the MHHI, the third key component is the market shares of firms  $j$ and  $k$,  $s_j$ and  $s_k$.
Empirically, market shares are relatively straightforward to calculate.
However, using market shares in the measure of common ownership can be problematic.
This is especially severe in studies that run regressions of firm performance (e.g., prices, profits, etc.) on MHHI.
The reason is that the outcome variable in these studies and the market share component of MHHI are endogenous; therefore, the estimate of MHHI cannot be interpreted in a causal manner.
We discuss this issue in more detail in Section 4.2 below.
<!-- para 69 -->
We now discuss alternative measures of common ownership, which potentially overcome some of the challenges discussed above.
To avoid the endogeneity issues associated with market shares, Kennedy et al. (2017) employ a measure that is independent of market shares.
While MHHI $\Delta$ represents one term that captures investors' weighted ownership and control in rival firms multiplied by a second term that captures the market shares of these firms, Kennedy et al.'s (2017) measure is only based on the first term.
<!-- para 70 -->
More recent work has developed additional measures that similarly omit market shares.
For example, Freeman (2024) uses overlap value, which corresponds to the proportion of firm market value that is held by overlapping owners.
Park et al. (2019) employ market value common firms, which is the sum of the market values of common owners' ownership in same-industry firms that share a common owner with the focal firm.
Backus, Conlon & Sinkinson (2021b) develop a profit weight measure, which represents the weight that a firm places on another firm's profits relative to the weight it places on its own profits, given the ownership structure of each firm.
In addition to being independent of market shares, this measure also avoids the necessity of defining product markets.
Koch, Panayides & Thomas (2021) focus on industry-level dynamics and thus employ industry-level measures of common ownership, which by definition are not dependent on market shares.
Many of the measures that avoid using market shares require a measure of control, for example, voting rights (see, e.g., Kennedy et al. 2017, Backus, Conlon & Sinkinson 2021b).
As noted above in Section 3.2.2, measuring control presents its own set of challenges.
<!-- para 71 -->
To address the criticism that voting rights do not necessarily equate to control rights, Gilje, Gormley & Levit (2020) develop a measure that explicitly allows for investors to devote varying levels of attention to the firm.
For example, prior literature suggests that active funds, larger funds, larger fund families, and funds that hold a greater fraction of their portfolio in the firm are more diligent monitors (see, e.g., Iliev, Kalodimos & Lowry 2021); the Gilje, Gormley & Levit (2020) measure enables the researcher to incorporate such factors.
<!-- para 72 -->
He & Huang (2017) construct five alternative measures, which do not depend on firm market shares or control rights.
Each of these measures, or close variants thereof, have been used in many subsequent papers in the literature (see, e.g., Park et al. 2019; He, Li & Yeung 2020; Ramalingegowda, Utke & Yu 2021; Chen et al. 2023; Kini, Lee & Shen 2023; Freeman 2024).
The five measures, each of which is defined at the firm-year level, include the following: (a) Cross Dummy, an indicator variable equal to one if at least one of a firm's blockholders simultaneously blockholds at least one other firm in the same industry; (b) Number of Investors, the number of unique institutional blockholders that blockhold another firm in the same industry; (c) Number of Firms, the number of firms within the same industry that have a blockholder who is also a blockholder in the focal firm; (d) Avg Number of Firms, the number of same-industry peers that are blockheld by the average cross-holding institution; and (e) TotalCrossOwn, the sum of all cross-holding institutions' percentage holdings in the focal firm.
Each of these measures generally captures the extent to which one (or more) investor(s) simultaneously own competing firms, in ways that potentially lead a manager to compete against these other firms less aggressively.
<!-- para 73 -->
Finally, an increasing number of papers in the common ownership literature focus on pairs of firms that are potentially more directly related to each other.
For example, Newham, Seldeslachts & Banal-Estañol (2022), Xie & Gerakos (2020), and Schmalz & Xie (2022) focus on brand-name and generic drug companies.
In such cases, the papers develop measures of common ownership, which are applicable to their particular setting.

## methods
<!-- para 2 -->
Any empirical analysis that tries to estimate the causal effect of common ownership on firm behavior and competitive dynamics must confront the fact that investment decisions by institutional investors are endogenous.
There are likely to be unobserved factors driving investment decisions that lead to both increases in common ownership and higher firm prices and profits.
In Section 4.1 below, we provide a critical discussion of the various ways that researchers have attempted to address and overcome this issue.
<!-- para 3 -->
In addition to the issue of endogenous investment, a second identification challenge arises when using  $MHHI\Delta$ to measure common ownership and to estimate its impact on prices or firm profits.  $MHHI\Delta$ is a function of firm market shares, and regressions of prices on market shares suffer from well-known endogeneity biases.
We discuss this issue in Section 4.2.
<!-- para 5 -->
Investors' ownership choices are endogenous, and it is difficult to separate the effects of expected performance on ownership from the effects of ownership on performance.
Moreover, the increase in common ownership has coincided with increased consolidation in nearly every industry; either common ownership or consolidation could influence both firm input costs and markups.
Researchers have employed several approaches to identifying the causal effects of common ownership.
We discuss the primary methods of identification, along with the papers that developed each approach in the common ownership setting. [^18]
<!-- para 6 -->
One approach is to employ the Blackrock–BGI (Barclays Global Investors) merger, which occurred in 2009, as a source of identification.
Two requirements must be satisfied for this to be a valid instrument.
First, the merger must not be motivated by the policies or performance of portfolio firms.
The plausibility of this exclusion condition is discussed in depth by He & Huang (2017) and Azar, Schmalz & Tecu (2018) and appears to be satisfied.
Second, the Blackrock–BGI merger must significantly affect common ownership.
This relevance condition also appears to hold, as shown by Azar, Schmalz & Tecu (2018).
The merger of Blackrock and BGI's investment portfolios led to one much larger investment portfolio, and this larger portfolio was more likely to hold equity in additional competitor firms and to hold larger positions in the competitor firms.
<!-- para 7 -->
As highlighted by Lewellen & Lowry (2021), the challenge associated with using the Blackrock–BGI merger as a source of identification lies in the selection of an appropriate control sample.
This is best illustrated with a figure.
Looking at Figure 2, within industry X, the treatment firms represent firms X1, X2, X3, and X4.
Prior to the merger, suppose X1 and X2 were owned by Blackrock and X3 and X4 were owned by BGI.
Following the merger, all four competitor firms are owned by Blackrock–BGI (i.e., common ownership has increased).
There are two
<!-- para 8 -->
Industry X
<!-- para 10 -->
Industry Y
<!-- para 12 -->
Industry Z
<!-- para 15 -->
The figure provides a sample construction example for the financial institution-merger analysis.
In this example, the universe consists of three industries (X, Y, and Z) and two merging institutions (A and B).
Rectangles enclose all firms in an industry (e.g., firms in the gray rectangle belong to Industry X, and they are labeled X1, X2, ...).
Within the rectangles, a blue circle denotes the firms that are owned by Institution A (e.g., firms X1, X2, and X5 within Industry X) and a yellow circle denotes the firms owned by Institution B (e.g., firms X3, X4, and X5 within Industry X).
Treatment firms are firms that are blockheld by one of the merger partners with some industry rivals being blockheld by the other partner (e.g., firms X1, X2, X3, and X4; firms blockheld by both partners are excluded).
Control $^{DI}$ are firms blockheld by one merger partner with no industry rivals blockheld by the other partner (e.g., firms Y1, Y2, Z1, Z2, and Z3).
Control $^{SI}$ are firms matched to treatment firms based on industry and size (e.g., a matched firm to firm X1 is denoted as X1', etc.).
Figure adapted with permission from Lewellen & Lowry (2021).
<!-- para 16 -->
possible samples of control firms: firms that belong to a different industry in which only Blackrock or BGI owned any firms prior to the merger (firms in industry Y or Z, which can be labeled Control $^{DI}$), and firms that belong to the same industry but were owned by neither Blackrock nor BGI prior to the merger (firms within industry X other than X1, X2, X3, and X4, which can be labeled Control $^{SI}$).
<!-- para 17 -->
The first set of control firms, Control $^{DI}$, can generate biased inferences if different industries behaved differently in the years following the 2009 Blackrock–BGI merger.
Lewellen & Lowry (2021) show that this is the case.
On average, the treatment firms represent higher growth firms, and these firms performed better in the years following the 2008–2009 global financial crisis (GFC).
One way to overcome this problem is to create a matched sample of control firms, where the controls are matched to treatment firms based on size and book-to-market (Control $^{DIMatched}$).
Alternatively, the researcher can use control firms from the same industry (as the treatment firms), Control $^{SI}$.
In sum, although Control $^{DI}$ has been commonly used in the literature, more recent evidence suggests that Control $^{SI}$ and Control $^{DIMatched}$ are more likely to provide unbiased inferences.
<!-- para 18 -->
The second approach toward identification builds upon the Blackrock–BGI merger approach, but it employs a broader set of financial institution mergers, which are spread through calendar time.
Following the criteria outlined in He & Huang (2017), Lewellen & Lowry (2021) provide a list of 64 financial institution mergers during the 1980–2015 period.
Similar to the Blackrock–BGI merger case, the relevance and exclusion conditions are likely satisfied.
Moreover, the fact that the mergers do not all occur at the same point in time potentially represents an advantage over just using the Blackrock–BGI merger.
However, Lewellen & Lowry (2021) show that, although the mergers are spread through calendar time, the largest financial institution mergers occurred around the time of the GFC.
As a result, affected firms are disproportionately concentrated during this period, and inferences can be biased by the effects of the crisis.
To lessen potential biases, the researcher can either use one of the recommended control samples described above (Control $^{SI}$ or Control $^{DIMatched}$) or omit financial institution mergers that occurred around the GFC.
<!-- para 19 -->
A third approach toward identification is to use the Russell 1000/2000 Index reconstitution or S&P 500 Index additions.
Both of these approaches suffer from several problems.
First and foremost, entry into an index is not random.
In addition, a fundamental problem with Russell reconstitutions is that they do not affect firm-level common ownership.
In other words, this approach does not satisfy the relevance condition.
The reason is that Russell Index reconstitutions only affect ownership by mutual funds, not ownership at the institution level, a point made by both Schmidt & Fahlenbrach (2017) and Lewellen & Lowry (2021).
In contrast to Russell Index reconstitutions, S&P 500 Index additions do cause an increase in common ownership.
However, additions to the S&P 500 also cause increases in institutional ownership and decreases in block ownership, and either of these changes could plausibly affect firms along multiple dimensions.
<!-- para 20 -->
Finally, a fourth approach to identification, as proposed by Boller & Morton (2020) and used by Anton et al. (2023), is to use entry of competitor firms into the S&P 500 Index.
A treatment firm is defined as a firm that belongs to the S&P 500 Index and that had a firm in the same industry join the S&P 500 Index.
Control firms represent firms that also belong to the S&P 500 Index, but for which no firm in the same industry joined the S&P 500.
This approach causes an increase in common ownership of the treatment firms, and it potentially overcomes many of the problems associated with the above-described approach of using entry into the S&P 500 as the treatment.
However, one potential cause for concern is that control firms are drawn from different industries than treatment firms.
As highlighted by Lewellen & Lowry (2021), this can cause biased inferences, particularly when firms are not matched, for example, on size and growth.
<!-- para 21 -->
In sum, prior literature suggests multiple candidate sources of identification.
However, many of the approaches that have been used do not satisfy all necessary criteria to be valid instruments.
It is critical that the researcher be aware of the potential biases that can arise from approaches in which treatment events are clustered in calendar time and approaches in which control firms are drawn from industries different from those of treatment firms.
<!-- para 23 -->
Empirical papers that employ  $MHHI\Delta$ as a measure of common ownership face another basic identification problem.
We discuss this in the context of Azar, Schmalz & Tecu's (2018) main specification, though the issue is not unique to their paper.
The paper regresses the logarithm of the average airfare charged by carrier j on route r during year-quarter t, on the measure of common ownership,  $MHHI\Delta_{rt}$, the traditional Herfindahl–Hirschman Index,  $HHI_{rt}$, a set of control variables, year-quarter fixed effects, and market-carrier fixed effects:
<!-- para 24 -->
$$ \log(p_{rjt})=\alpha\cdot MHHI\Delta_{rt}+\eta\cdot HHI_{rt}+\theta\cdot X_{rjt}+\alpha_{t}+\nu_{rj}+\varepsilon_{rjt}, $$
<!-- para 25 -->
5.
<!-- para 26 -->
where  $p_{rjt}$ is the average ticket price for airline j, in market r, in year-quarter t;  $HHI_{rt}$ captures industry concentration in route r at time t; and  $MHHI\Delta_{rt}$ captures the additional effect on concentration arising from common ownership.
<!-- para 27 -->
Substituting the formula for  $MHHI\Delta$ from Equation 4, we obtain:
<!-- para 28 -->
$$ \begin{aligned}\log(p_{rjt})=&\alpha\cdot\overbrace{\sum_{j}\sum_{k\neq j}\underbrace{\left(\sum_{i}\gamma_{ijt}\cdot\beta_{ikt}\right)}_{Ownership and control}\underbrace{s_{rjt}\cdot s_{rkt}}_{Market shares}}^{MHHI\Delta}+\eta\cdot\overbrace{\sum_{j}\underbrace{s_{rjt}^{2}}_{Market shares}}^{HHI}\\&+\theta\cdot X_{rjt}+\alpha_{t}+\nu_{rj}+\varepsilon_{rjt}.\end{aligned} $$
<!-- para 29 -->
6.
<!-- para 30 -->
From this expression, it is clear that the Azar, Schmalz & Tecu (2018) specification represents a regression of average prices on two functions of market shares, namely, the traditional Herfindahl–Hirschman Index and  $MHHI\Delta$.
There are serious identification concerns with such a specification.
<!-- para 31 -->
As has been recognized for more than 40 years in the industrial organization literature, regressions of firm performance (e.g., prices, profits, etc.) on measures of concentration (market shares, HHI, etc.) are merely descriptive; they yield no causal evidence on the factors driving this relationship.
In fact, since the work by Weiss (1990), Bresnahan (1989), Schmalensee (1989), and Evans, Froeb & Werden (1993), the literature has recognized that market shares and prices are jointly determined in equilibrium and that, therefore, regressions of prices on market shares are unidentified.
<!-- para 32 -->
A further issue arises from the fact that  $MHHI\Delta$ is a nonlinear function of market shares  $(s_{jt}, s_{kt})$ and the ownership/control parameters  $(\beta_{jt}, \gamma_{jt})$.
A positive coefficient on  $MHHI\Delta$ could indicate one of two things: (a) increased common ownership increases product market prices or (b) increased market shares lead to increased product market prices.
If the positive correlation between  $MHHI\Delta$ and prices is driven mainly by variation in market shares, then changes in prices cannot be attributed to common ownership.
<!-- para 33 -->
In fact, Dennis, Gerardi & Schenone (2022a) show that the positive relationship between  $MHHI\Delta$ and ticket prices documented in Azar, Schmalz & Tecu (2018) appears to be identified by variation in the market share component rather than by variation in the ownership/control parameters.
This evidence casts further doubt on whether common ownership truly exerts a causal effect on airline pricing.
<!-- para 35 -->
Thus far, we have summarized the theoretical foundations of common ownership, discussed the main assumptions underlying the theory, described both the most commonly used measures of common ownership and alternative proposed measures, and reviewed identification concerns.
In this section, we set aside these conceptual and empirical issues and turn our attention to the fundamental question of how common owners can exert causal effects on market competition.
Specifically, how do institutional investors in a given firm achieve an equilibrium in which rival firms coordinate to soften competition?
Furthermore, how does the channel allow common owners to sustain coordination between firms that are natural competitors and prevent any one firm from deviating and destroying the equilibrium?
<!-- para 36 -->
We organize our discussion of the potential causal mechanisms into two parts below.
In Section 5.1, we discuss channels that involve direct, explicit communication between investors and firm managers.
In Section 5.2, we consider more indirect mechanisms that have been proposed in the common ownership literature.
<!-- para 37 -->
Before delving into the discussion, it is helpful to note that the mechanism through which coordination among rivals is achieved must satisfy two criteria.
First, the mechanism cannot (overtly) violate antitrust laws, and second, the terms of the agreement must be enforceable and self-regulating, in the sense that a firm manager would not have an incentive to deviate from the cooperative equilibrium and, if they did, they would face credible and enforceable punishment.
<!-- para 39 -->
Direct channels represent explicit communications between owners and managers, regarding the level of competition between rival firms.
Such channels seem closest in spirit to the early common ownership models of Rotemberg (1984) and Azar (2012), which are based on the assumption that managers know (and are incentivized to act upon) the preferences of owners, where these owners potentially also own shares in rival firms.
<!-- para 40 -->
There are multiple direct channels of communication between investors and managers.
Large investors may sit on firm boards, as is commonly observed among venture capitalists (VCs), private equity investors, and activists.
Large investors and activist investors may also speak directly with management as a way to achieve changes in firm policies (see, e.g., Becht, Franks & Wagner 2023; Brav, Jiang & Li 2022).
Finally, investors also interact with firms through voting, though in these cases the interactions are limited to items on the ballot.
<!-- para 41 -->
There are two key issues.
The first issue is whether common owners use any of these channels to pressure firms into anticompetitive behavior.
It is important to note that such actions would likely violate one of the necessary criteria listed above: abiding by antitrust laws.
Furthermore, we are not aware of any evidence of such communications.
In fact, there seems to be some evidence that common owners steer clear of direct communications with rival firms, as Geng et al. (2022) find that among cases where one shareholder owns a block in two rival firms, this common owner rarely sits on the boards of both firms.
<!-- para 42 -->
The second key issue is whether investors are attentive toward all portfolio firms.
Iliev, Kalodimos & Lowry (2021), Ben-Rephael, Da & Israelsen (2017), and Schmidt (2019) show that investor attention varies widely, and Gilje, Gormley & Levit (2020) show how the presence of less attentive investors mitigates effects arising from common ownership.
Additionally, a growing portion of market capitalization is held by passive mutual funds, and there is some evidence that such funds engage less intensely (e.g., Bebchuk & Hirst 2019, Heath et al. 2022). [^19] Edmans, Levit & Reilly (2019) come to a different conclusion, showing theoretically that common ownership contributes to enhanced governance.
In aggregate, it is fair to say that prior literature highlights the importance of considering common owners' incentives to engage, particularly given the substantial heterogeneity across investors.
<!-- para 44 -->
Rather than owners communicating their preferences directly to managers, it is possible that a lack of communication leads to softer competition.
If common owners benefit by rival firms competing less aggressively against each other, then they have incentives to not pressure firms to compete aggressively.
Managers would benefit from such decreased pressure, because they could enjoy the quiet life (Bertrand & Mullainathan 2003).
<!-- para 45 -->
Anton et al. (2023) develop a theoretical model that lays out a specific channel through which common owners can incentivize managers to compete less aggressively.
The paper posits that, compared to other shareholders, common owners put less pressure on firms to adopt incentive-based contracts.
The lower incentive structure causes managers to be less efficient, which results in a higher cost structure.
Prices are higher and quantity sold is lower.
<!-- para 46 -->
Unlike the direct channels listed above, this indirect channel does not violate the criteria related to antitrust laws.
However, it may violate the incentive compatibility criteria.
Firms with greater agency costs are more likely to attract activist investor attention, and they are also more likely to become takeover targets.
Thus, even if current shareholders incentivize a manager to enjoy the quiet life, it still may not be in the manager's best interest to do so.
Incremental to
<!-- para 47 -->
this concern, Walker (2019) highlights several additional challenges with the Anton et al. (2023) framework.
First, the Anton et al. (2023) model and associated empirical analysis focus on the executive's wealth to own-firm performance sensitivity (WPS), but Walker (2019) notes that compensation committees have little short-term influence over WPS.
Second, compensation committees have much more direct influence over relative performance evaluation (RPE, the extent to which pay packages consider firm performance relative to peers), but RPE has increased over time, rather than decreased as one would expect if common owners sought to weaken competitive incentives.
Third, compensation contracts with lower incentive structures would discourage many other firm actions—for example, firm lobbying—yet there is no evidence of changes in these types of behavior.
<!-- para 49 -->
In this section, we provide an overview of the applied common ownership literature.
We begin with a brief discussion of what we consider to be two of the seminal papers in the applied literature: the articles by He & Huang (2017) and Azar, Schmalz & Tecu (2018).
We then summarize a few notable critiques of this evidence.
Finally, we summarize the numerous papers that have been written since those seminal papers; these papers have explored the consequences of common ownership for a large number of economic outcomes across a broad set of industries.
<!-- para 51 -->
The articles by He & Huang (2017) and Azar, Schmalz & Tecu (2018) were the first published studies to present causal evidence that common ownership leads to greater coordination and softer competition among product market rivals. [^20] The papers, which were written contemporaneously, use different measures of common ownership, analyze different economic outcomes, and differ in the scope of the microdata that they employ to test their hypotheses.
<!-- para 52 -->
He & Huang (2017) focus on a broad set of industries and show that increased common ownership causes higher growth in firm-level market shares and facilitates greater collaboration among product market rivals, including more joint ventures, strategic alliances, and within-sector acquisitions.
The authors use several different measures of common ownership and address identification concerns by using mergers of financial institutions over the 1983–2011 sample period.
<!-- para 53 -->
In contrast, Azar, Schmalz & Tecu (2018) focus exclusively on the airline industry and provide empirical evidence that increased common ownership among carriers operating in a market results in higher average ticket prices.
The authors estimate fixed effects models using the MHHI $\Delta$ measure of common ownership and also use the 2009 merger between BlackRock and BGI to isolate plausibly exogenous variation in common ownership.
<!-- para 54 -->
While both of these studies have received a significant amount of attention among both academic researchers and policy makers, the Azar, Schmalz & Tecu (2018) study, in particular, has been the focus of a heated debate in the literature.
Subsequent empirical studies, including those by Kennedy et al. (2017) and Dennis, Gerardi & Schenone (2022a), have called into question the robustness of the paper's results due to both measurement and identification concerns.
<!-- para 55 -->
The Dennis, Gerardi & Schenone (2022a) critique focuses on the measure of common ownership used in the Azar, Schmalz & Tecu (2018) analysis, MHHI $\Delta$.
The paper implements a placebo analysis, which shows that the positive correlation between MHHI $\Delta$ and airline ticket prices is
<!-- para 56 -->
driven by the market share component of the MHHI $\Delta$ measure rather than the ownership and control components.
This finding suggests that endogeneity bias rather than a truly causal relationship is driving the positive correlation between the measure of common ownership and airline prices. [^21] Dennis, Gerardi & Schenone (2022a) also show that the relationship between common ownership and ticket prices is not robust to alternative measures of investor control and to assumptions about the extent of investor control during bankruptcy periods.
<!-- para 57 -->
The Kennedy et al. (2017) critique focuses on the differences between common ownership theory and Azar, Schmalz & Tecu's (2018) empirical specifications.
In particular, theory suggests that both price and the MHHI $\Delta$ are equilibrium effects that depend on the structure of ownership and control and also on cost and demand factors.
However, Azar, Schmalz & Tecu's (2018) main empirical analysis consists of regressions of price on MHHI, which are likely to suffer from endogeneity bias.
As an alternative approach, Kennedy et al. (2017) estimate a structural model in which the measure of common ownership is directly derived from theory and show that the Azar, Schmalz & Tecu (2018) results do not hold.
<!-- para 58 -->
The He & Huang (2017) and Azar, Schmalz & Tecu (2018) analyses (and many subsequent papers) have also come under scrutiny in work by Lewellen & Lowry (2021).
First, the authors critique the identification strategy employed in these papers (discussed in depth in Section 4.1).
Second, Lewellen & Lowry (2021) cast doubt on He & Huang's (2017) conclusion that common ownership causes increases in mergers and joint ventures, as the rate of such explicit coordination between any two firms is very rare (less than 0.1% of all potential firm pairs).
<!-- para 60 -->
Since the seminal He & Huang (2017) and Azar, Schmalz & Tecu (2018) papers were published, the common ownership literature has rapidly expanded in numerous directions.
Table 1 provides an up-to-date list of papers, in alphabetical order by first author, which have empirically tested for common ownership effects.
It lists the principal outcome variables that each paper focuses on, whether a common ownership effect is found, the method(s) used to address endogeneity concerns, and the particular industry and time period covered by each paper.
<!-- para 61 -->
The literature has considered a wide variety of economic outcomes—from prices, markups, and other measures of firm profitability to M&A activity, R&D expenditures, patent citations, corporate governance, and even the strength and durability of supply chain relationships.
Like the seminal study by He & Huang (2017), many papers focus on more than one outcome.
To capture this fact, Figure 3 displays all of the papers listed in Table 1, sorted by subject matter with horizontal gray bars connecting papers that cover more than one topic.
The figure also includes the publication status of each paper and a bit more detail regarding each paper's findings.
<!-- para 63 -->
Common ownership and
<!-- para 64 -->
<table border=1><tr><td>Product market prices</td><td>Investment and R&amp;D</td><td>Firm/product entry</td><td>Firm performance</td><td>M&amp;A</td><td>Corporate governance</td><td>Supply chain effects</td></tr><tr><td>Azar, Schmalz &amp; Tecu(2018) JFIncrease product market prices.</td><td>He &amp; Huang (2017) RFSIncrease innovation and R&amp;D.</td><td></td><td>He &amp; Huang (2017) RFSHigher market share growth.</td><td>He &amp; Huang (2017) RFSIncrease probability of M&amp;A, strategy alliance, Better M&amp;A terms and synergies.</td><td>Park et al. (2019) JAEIncrease disclosure on earnings and capital expenditure forecasts.</td><td>Ramlingogowda, Uike &amp; Yu (2021) CARCommon ownership at the industry level curbs accrual-based earnings management.</td></tr><tr><td>Koch, Panayides &amp; Thomas (2021) JFENo effect on prices, industry-level markups, price-cost margins.</td><td>Gutierrez &amp; Philippon(2017) BPGovernance increases investment in noncompetitive industries with high common ownership.</td><td>Xie &amp; Gerakos (2020) AEA R&amp;DPharmaceutical brand-name incumbent brands test entry from generic and non-generic a common owner with generic.</td><td></td><td>Brooks, Chen &amp; Zeng (2018) JCFIncrease probability of mergers; lower premiums, improve synergies, improve performance.</td><td>He, Huang &amp; Zhao (2019) JFEIncrease morning; increase probability of common owners voting against management.</td><td>Gao et al. (2022) WPPCommon ownership in supply chain decreases opportunistic earnings management by the supplier firm.</td></tr><tr><td>Torshizi &amp; Clapp (2021) ATBSignificant increase in seed prices (maize, soybean, cotton).</td><td>Levellen &amp; Lowry (2021) ATENo significant effect on R&amp;D.</td><td></td><td>Levellen &amp; Lowry (2021) JFENo significant effect on ROA, cash flow, growth, operating margins.</td><td>Levellen &amp; Lowry (2021) JFENo significant effect on M&amp;A.</td><td>Chen et al. (2023) JCFNegative relation between ownership and investor trading profitability.</td><td>Riva (2023) WPIncrease (decrease) markups in downstream (upstream) sectors.</td></tr><tr><td>Dennis, Gerardi &amp; Schenone (2022a) JFNo effect on product prices, Market shares component of M&amp;H drives the result, not the ownership and control component.</td><td>Kinl, Lee &amp; Shen (2023) MSIncrease information spillover and investment with common owners.</td><td>Newham, Seldeislachts &amp; Banai Estanol (2022) WPPharmaceutical generic firms less likely to enter drug market if incumbent is commonly owned.</td><td>Boiller &amp; Morton (2020) WPRivals stock return increases when firm joins an index and shares owner with rival in index.</td><td></td><td>He, Li &amp; Yeung (2020) WPNegative relation between common ownership.</td><td>Freeman (2024) JFOACommon ownership across supply chain decreases holdup problems.</td></tr><tr><td>Azar, Raina &amp; Schmalz (2022) FMIncrease in deposit interest rates.</td><td>Bindal &amp; Nordlund (2022) WPDecrease R&amp;D among commonly owned firms when the degree of product similarity between the firm and its peers is high.</td><td></td><td>Bindal &amp; Nordlund (2022) WPIncrease profitability when the degree of firms operate in more competitive markets.</td><td></td><td>Bindal &amp; Nordlund (2022) WPEffect in markets where coordination does not naturally occur (e.g., competitive industries and when products are similar).</td><td></td></tr><tr><td>Kennedy et al. (2017) WPNo effect on product prices.</td><td>WPPDecrease R&amp;D among commonly owned firms when the degree of product similarity between the firm and its peers is high.</td><td>Schmalz &amp; Xie (2022) WPGeneric-drug pharmaceutical firm enters brand firm market and then settles infringement lawsuit with common ownership, brand firm, with a decreased value in generic and a value of the common owned brand firm.</td><td></td><td></td><td>Peng, Yin &amp; Zhang (2023) AHPositive relation between accounting comparability and common ownership.</td><td></td></tr><tr><td>Backus, Conlon &amp; Skinson (2021a) WPNegative relation between prices of early-to-eat cereal and MWH, Markups consistent with profit maximization and competition.</td><td>Gerng, Hau &amp; Lai (2020) WPDecrease patent holdup, strategic patenting, and probability of downstream firm being sued for patent infringement.</td><td></td><td></td><td></td><td></td><td></td></tr></table>
<!-- para 66 -->
Applied common ownership papers by topic.
Abbreviations: AEA P&P, American Economic Association Papers and Proceedings; AH, Accounting Horizons; ATB, Antitrust Bulletin; BB, Brooking Papers; CAR, Contemporary Accounting Research; FM, Financial Management; JAE, Journal of Accounting and Economics; JCF, Journal of Corporate Finance; JF, Journal of Finance; JFE, Journal of Financial Economics; JFOA, Journal of Financial and Quantitative Analysis; MHH, Modified Herfindahl-Hirschman Index; MS, Management Science; RFS, Review of Financial Studies; ROA, return on assets; WP, working paper.
<!-- para 67 -->
from insider trading, consistent with common owners contributing to better governance.
The paper carefully matches treatment firms with control firms of a similar size that are in the same industry and shows that the results are robust to excluding mergers around the time of the GFC.
Kini, Lee & Shen (2023) use a similar DiD framework, and they find that higher common ownership leads to greater competition, more product development, and higher investments.
We think it is notable that both of these papers, each of which addresses recent identification critiques, find that common ownership leads to improved market outcomes across broad samples.
The only additional published paper that addresses recent identification critiques is that by Freeman (2024); this paper concludes that common ownership increases the duration, strength, and value of supply chain relationships.
Interestingly, recent theoretical work also predicts improved market outcomes arising from common ownership in certain cases.
For example, López & Vives (2019) show that, when knowledge spillovers are sufficiently high, increases in common ownership can lead to higher R&D investment.
<!-- para 68 -->
There is also a stream of papers focusing on common owners of private firms, in particular the portfolios of VCs.
This setting is critically different than the broader sample of public firms that represents the focus of both the theoretical and the empirical literature. [^23] Nonetheless, this setting is informative because many of the key assumptions, highlighted in Section 2.2 as questionable in the setting of public firms, are almost by definition satisfied in the VC setting.
In particular, VCs typically have more control rights and do not own broad sets of firms.
Lindsey (2008), González-Uribe (2020), Li, Liu & Taylor (2023), and Eldar & Grennan (2023) all find evidence of information sharing among VCs' portfolio firms, in ways that influence these firms' behaviors, for example, their innovation, alliances, patent citations, and capital raising.
In sum, among more recent empirical papers that carefully consider identification and that have undergone the peer review process, evidence that common ownership causes anticompetitive behavior is concentrated within very specific samples, for example, samples of private firms where ownership tends to be more concentrated.
<!-- para 70 -->
Several policy proposals have been made over the past ten years in response to evidence suggesting that common ownership causes anticompetitive effects.
A few proposals have focused on regulating common ownership under existing merger laws.
In the United States, Elhauge (2016, 2020) and Elhauge, Majumdar & Schmalz (2021) argue that this could be accomplished through implementation of Section 7 of the Clayton Act, which prohibits stock acquisitions that substantially lessen competition. [^24] In addition, there have been proposals for new regulations, focused directly on limiting common ownership (see, e.g., Posner, Scott Morgan & Weyl 2016; Posner 2021).
Finally, there have been proposals to tighten corporate governance rules to ban common owners from exercising their voting rights and actively engaging with management (Posner, Scott Morgan & Weyl 2016).
<!-- para 71 -->
Implementing such policies could have significant adverse effects on firms, investors, and the macroeconomy.
Investors could find it more difficult to create diversified portfolios at low cost, due to investment strategy restrictions and increased compliance costs faced by both mutual funds and other institutions.
Firms could suffer from weaker corporate governance, due to limits on institutional voting and monitoring.
The economy could suffer from less value creation as a result.
<!-- para 72 -->
While none of the above policy proposals have been adopted to date, there have been some cases in which common ownership has featured in regulatory decisions.
For example, the European Commission focused on potential harm resulting from common ownership in their reviews of both the Dow-DuPont merger and the Bayer-Monsanto merger.
Here, we emphasize the need for caution.
There are many well-established benefits of mergers, as well as many well-established costs, as have been laid out in decades of antitrust literature.
In contrast, the evidence that common ownership should additionally feature into the evaluations of mergers is weak at best.
As highlighted throughout this piece, the hypothesis that common ownership causes anticompetitive behavior is characterized by both strong underlying theoretical assumptions and a lack of compelling empirical support.
Given these observations, we believe that it would be premature for policy makers to implement significant regulations and/or reforms until more credible evidence is found that common ownership does, in fact, exert anticompetitive effects.

## discussion
<!-- para 2 -->
This review of the common ownership literature highlights several key issues.
First, the theoretical foundations sustaining the literature rest on several questionable assumptions.
One of these is that a firm's manager knows each shareholder's preferences and acts to satisfy these (diverse) preferences.
This dismisses asymmetric information and principal-agent problems between managers and shareholders.
These assumptions are unlikely to hold among publicly traded firms.
A further assumption common ownership models make is that managers maximize the value of their shareholders' portfolios (as opposed to maximizing firm value).
Based on these assumptions, the common ownership models deliver an equilibrium in which managers of common owned rival firms do not compete aggressively with each other.
However, this predicted behavior could actually hurt common owners, as these owners hold shares in various industries, and weak competition and higher markups in one industry can lead to decreased profits in related industries also owned by the common owner.
We encourage future research to focus on scenarios where these assumptions are less questionable, for example, among private firms with concentrated owners (see Li, Liu & Taylor 2023).
<!-- para 3 -->
Second, endogeneity issues are paramount, and insufficient identification can lead to erroneous conclusions.
Since investment decisions are endogenous, it is difficult to separately identify the effects of ownership on firm performance from the effects of expected performance on investment.
While the literature has adopted several approaches to address this concern, Lewellen & Lowry (2021) show that they are significantly flawed and suggest alternative empirical approaches to achieve cleaner identification.
Recent papers employing these suggested techniques show little evidence that common ownership causes lower competition.
We advise researchers to carefully address identification concerns.
<!-- para 4 -->
Third, there are numerous issues associated with measuring common ownership.
We show that the most common measure used in the literature, MHHI, has significant drawbacks.
Most importantly, MHHI is a function of firm market shares, which introduces an endogeneity bias within regressions of firm performance on this common ownership measure.
This is an important concern, as Dennis, Gerardi & Schenone (2022a) show that the positive correlation between this measure of common ownership and ticket prices in Azar, Schmalz & Tecu (2018) is driven by the market share component of MHHI, rather than the ownership and control parameters.
An additional concern is that there is no clear way to measure the extent of investor control over firm decision-making.
Most papers identify control with votes, but the literature has shown that votes are imprecisely defined and inconsistent across time and across institutions.
While alternative measures have been developed to deal with some of these issues, the literature has yet to come to a consensus about the best way to measure common ownership.
<!-- para 5 -->
A survey of the current literature, in particular papers that have successfully gone through peer review and are now published in top-tier academic journals, provides relatively little evidence that common ownership causes anticompetitive behavior among publicly traded firms.
Nevertheless, it remains possible that common ownership has anticompetitive effects in other settings.
<!-- para 7 -->
[^1]: See Elhauge, Majumdar & Schmalz (2021); Elhauge (2020); Posner (2021); Posner, Scott Morgan & Weyl (2016); Elhauge (2016).
These proposals have been the subject of discussion at the US Department of Justice, the US Federal Trade Commission, and the European Central Bank, among others.
<!-- para 8 -->
[^2]: This survey overviews papers publicly distributed as of the time of this writing.
<!-- para 9 -->
[^3]: This assumption is motivated by the existence of effective antitrust measures or, more generally, because collusive contracts are unenforceable.
<!-- para 10 -->
[^4]: One result from this theory is that as the number of firms increase, shareholders own stock in this larger number of firms, motivating managers to cooperate with a larger pool of competing firms.
Thus, as the number of firms grows, the markets become increasingly collusive.
Also, as transaction costs drop (e.g., with mutual funds), it becomes less expensive for investors to own a broader set of firms, thus inducing more product market collusion.
<!-- para 11 -->
[^5]: Note, in both of these models, there is no need to use (the threat of) punishment for a manager who deviates from collusive behavior.
Collusion represents managers' optimal strategy, and no player has an incentive to deviate.
<!-- para 12 -->
[^6]: O'Brien & Salop (2000) extend the framework developed by Bresnahan & Salop (1986) to cases of full mergers, total control, one-way control, and Coasian joint control among others.
<!-- para 13 -->
[^7]: Azar & Vives (2021) further develop the framework of Azar (2012) and analyze common ownership in a general equilibrium model where firm managers coordinate against labor, which contributes to higher markups.
<!-- para 14 -->
[^8]: For example, Azar (2012) explicitly states: “By modeling shareholders as directly voting on the actions of the firms, and having managers care only about expected vote share, I abstract in this paper from the conflict of interest between owners and managers” (p. 7).
<!-- para 15 -->
[^9]: Adler & Mitkov (2023) drop the assumption of no principal–agent conflicts.
Using a simple dynamic model of common ownership, the paper shows that when agency costs are high, common owners cannot incentivize managers to collude, because managers obtain greater benefits by diverting resources for their own benefit.
The paper finds that common ownership leads to weaker profit margins when corporate governance is poor.
<!-- para 16 -->
[^10]: Examples include paying managers with stock options in their firms, boards of directors who monitor and advise executives, etc.
<!-- para 17 -->
[^11]: For further discussion of this issue, see Romano (2021) and Rock & Rubinfeld (2017).
<!-- para 18 -->
[^12]: The Arrow impossibility theorem states that when voters have three or more options, there is no procedure to order these options in a socially optimal way, that is, a way that reflects the preferences of all voters.
The Condorcet paradox shows that it is impossible to aggregate individual transitive preferences under majority rule.
<!-- para 19 -->
[^13]: Simply selling their ownership stake in the offending manager's firm is unlikely to qualify as a credible form of punishment, since it would likely disrupt the fund's objective and could adversely affect the fund's diversification strategy, index tracking objectives, etc.
<!-- para 20 -->
[^14]: That  $\gamma_{ij}$ measures how much firm j's manager weighs investor i's portfolio returns is clearly seen in the manager's optimization problem in Equation 2.
<!-- para 21 -->
[^15]: Backus, Conlon & Sinkinson (2019) also show that because retail investors have effectively no control in any given firm, common ownership is positively related to the level of retail ownership.
These issues become even greater when insider holdings are also ignored.
<!-- para 22 -->
[^16]: Several models assume control and ownership are the same,  $\gamma_{i,j} = \beta_{i,j}$.
For example, Rubinstein & Yaari (1983), Rotemberg (1984), Azar (2012), and Azar & Vives (2021) assume no separation of ownership and control.
Backus, Conlon & Sinkinson (2019) also set control equal to ownership,  $\gamma_{i,j} = \beta_{i,j}$, but acknowledge that this is an arbitrary assumption.
<!-- para 23 -->
[^17]: Items up for vote include the following: director nominees, compensation proposals, governance proposals, environmental proposals, and social proposals.
<!-- para 24 -->
[^18]: Table 1 provides a more complete list of papers that have employed each identification approach.
<!-- para 25 -->
[^19]: In contrast, Appel, Gormley & Keim (2016) conclude that passive funds represent more active monitors, and Lewellen & Lewellen (2022) conclude that passive common ownership has a particularly large effect on indexers' incentives to engage.
<!-- para 26 -->
[^20]: The work by Azar (2012), which preceded both of these papers, computed measures of common ownership of US stocks over time and documented a positive correlation between common ownership and profit margins in cross-industry panel regressions.
<!-- para 27 -->
[^21]: In subsequent work, Azar, Schmalz & Tecu (2022) present a critique of the Dennis, Gerardi & Schenone (2022a) placebo analysis, and Dennis, Gerardi & Schenone (2022b) respond to that critique.
<!-- para 28 -->
[^22]: As discussed in Section 5.2, Anton et al. (2023) find anticompetitive effects of common ownership, in a specification that employs a means of identification different from all of the above papers.
The strength of their identification is sensitive to the fact that treatment firms and control firms come from different industries.
For a more in-depth discussion of concerns with such specifications, see Section 4.1.
<!-- para 29 -->
[^23]: For this reason, and for brevity, we do not include these papers in Table 1.
<!-- para 30 -->
[^24]: In Europe, Elhauge (2020) proposes implementation under Articles 101 and 102 of the Treaty of the Functioning of European Union.
<!-- para 31 -->
[^a]: When using financial institution mergers as a source of identification, the paper employs the alternative approach(es) suggested by Levellen & Lowry (2021).
