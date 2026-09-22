---
type: sentences-archive
citekey: "levinthal_1981_a_model_of_adaptive_organizational_search"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\Levinthal等-1981-A Model of Adaptive Organizational Search.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# levinthal_1981_a_model_of_adaptive_organizational_search 句子库存

## introduction
<!-- para 1 -->
We assume that an organization sets a performance target, $G_{t}$, for each time period and modifies that target on the basis of performance experience.
<!-- para 2 -->
If $P_{t}$ is an organization's performance in period t:
<!-- para 3 -->
$$ G_{t}=b_{1}P_{t-1}+(1-b_{1})G_{t-1}. \tag{1} $$
<!-- para 4 -->
As a result, the target is an exponentially weighted moving average of past performance.
<!-- para 5 -->
Organizational learning is driven by the relationship between $G_t$ and $P_t$, and thus by variations in both.
We assume that the organization's performance in period $t$ depends on the state of its technology at time $t$, $T_{*,t}$, the costs of search that it has undertaken, and an exogenous and randomly varying environmental variable, $a_t$.
Specifically
<!-- para 6 -->
$$ P_{t}=(1+a_{t})T_{*,t}-R_{t}-I_{t}, \tag{2} $$
<!-- para 7 -->
where $R_{t}$ and $I_{t}$ are the levels of expenditure on the two types of search processes considered, refinement search and innovation search.
By refinement we mean the fine-tuning and economizing designed to improve the efficiency of an existing technology.
The second kind of search is technological innovation, finding a new improved technology.
The distinctions are taken from Radner (1975) and are similar to those made by Knight (1967) and Nelson and Winter (1978).
<!-- para 8 -->
The technology in period $t$, $T_{*,t}$, depends on the technology of the previous period and the realized outcomes of search.
If we ignore the complications in forecasting the consequences of technologies before they are implemented, $T_{*,t}$ is the maximum of the technological outcomes from two search processes (the search for refinement and the search for innovation), and the (possibly changed) technology of the previous period.
That is, it is assumed that existing technology changes by a constant factor, $b_{2}$.
It is possible for technology to decay (i.e., $b_{2}<1$), remain constant (i.e., $b_{2}=1$), or improve (i.e., $b_{2}>1$) in the absence of search.
Thus,
<!-- para 9 -->
$$ T_{*,t}=\max\left(T_{r,t},T_{i,t},b_{2}T_{*,t-1}\right), \tag{3} $$
<!-- para 10 -->
where $T_{r,t}$ is the value of the best technology discovered through refinement search during period t, and $T_{i,t}$ is the value of the best technology discovered through innovation search during period t.
If the consequences of technological changes are subject to error, $T_{*,t}$ is the true value of the technology that appeared best, according to estimates at the time of decision.
<!-- para 11 -->
Organizations are assumed to search by sampling some number of opportunities and to implement the best of those, provided it is believed to be better than the existing technology.
The outcomes from search are a joint consequence of the sample size, the current technology, and the distributions of possible technologies.
Assuming errors of estimation are unbiased, the technology expected as a result of search is better than the expected value of the pool of opportunities; and an increase in the variance of the distribution in the pool increases the expected improvement in technology to be realized from search [Kohn and Shavell (1974)].
<!-- para 12 -->
The distributions of technological opportunities are assumed to be different for the two kinds of search.
In the case of refinement, it is assumed that the distribution of opportunities is a normal distribution of changes from $b_{2}T_{*,t-1}$ with a mean=0, and a standard deviation, $V_{r,t}$, which declines with search until a new technology is invented and adopted (at time y).
The initial standard deviation for a newly innovated technology is proportional to the value of the technology when adopted.
Thus,
<!-- para 13 -->
$$ V_{r,y}=c_{1}T_{*,y},\quad\mathrm{and} \tag{4} $$
<!-- para 14 -->
$$ V_{r,t+1}=c_{2}V_{r,t}\quad(if a refinement draw was made in period t). \tag{5} $$
<!-- para 15 -->
In the case of search for innovation, it is assumed that opportunities are distributed as a log normal distribution of changes from $b_{2}T_{*,t-1}$ with a mean=0, and a fixed standard deviation, $V_{i}$, proportional to the value of the current (unrefined) technology.
Thus
<!-- para 16 -->
$$ V_{i}=c_{3}T_{*,y}. \tag{6} $$
<!-- para 17 -->
The value of a refinement or innovation discovered by search is assumed to be known with certainty once it is implemented.
However, the values of unimplemented technological modifications may be known only up to some error.
As a result, it is possible for search to result in technological decline rather than improvement even though choices of the best apparent technology are made; and it is possible for an organization to learn not to search because of estimation errors and thereby reduce the experience in search that would make search more useful.
We assume that estimation errors are distributed normally with mean zero and a standard deviation that is initially greater in the case of innovation ( $V_{e,l,t}$) than in the case of refinement ( $V_{e,r,t}$).
The standard deviation for errors for each kind of search declines with experience in implementing new technological change.
Note that even though errors of estimation are assumed to be unbiased, the errors observed with respect to implemented technologies will more commonly be overestimates than underestimates, and that increasing the variance of (unbiased) errors decreases the expected real improvements to be realized from search.
<!-- para 18 -->
We assume an organization affects its performance by changing search expenditures.
Returns to search are assumed to depend on the size of current expenditures, current efficiencies in search, and current technological opportunities.
We imagine that search consists of sampling opportunities from the pool of technological possibilities associated either with refinement or innovation.
Each draw results in the ‘discovery’ of some opportunity.
Many of these will be less attractive than the present technology; some may be more attractive.
Thus the likelihood of discovering technological improvements depends on the sample size.
We assume the sample size for each of the two kinds of search is proportional to the product of the current expenditure on search and current search efficiency.
Thus, if we let $E_{r,t}$ be the efficiency in refinement search at time t and $E_{i,t}$ be the efficiency in innovation search, the sample sizes for refinement, $K_{r,t}$, and innovation, $K_{i,t}$, are given by the integer values of
<!-- para 19 -->
$$ K_{r,t}=k_{r}R_{t}E_{r,t},\quad\mathrm{and} \tag{7} $$
<!-- para 20 -->
$$ K_{i,t}=k_{t}I_{t}E_{i,t}. \tag{8} $$
<!-- para 21 -->
We assume that efficiency in search increases with increasing search within a given technology, but at a decreasing rate.
The carry-over of efficiency from the previous technology is proportional to the difference between the two technologies.
Let
<!-- para 22 -->
$$ F_{d,t}=F_{d,y-1}(T_{*,y-1}/T_{*,y})+\sum_{j=y}^{t-1}K_{d,j}\quad if\quad T_{*,y-1}\leq T_{*,y}, \tag{9} $$
<!-- para 23 -->
and
<!-- para 24 -->
$$ F_{d,t}=F_{d,y-1}(T_{*,y}/T_{*,y-1})+\sum_{j=y}^{t-1}K_{d,j}\quad if\quad T_{*,y-1}>T_{*,y}, $$
<!-- para 25 -->
where y is the time period of the last adopted innovation, and d represents the particular mode of search (refinement or innovation).
Then
<!-- para 26 -->
$$ E_{d,t}=(F_{d,t})^{1/w_{d}}. \tag{10} $$
<!-- para 27 -->
Note that the efficiency of search is not affected by $b_{2}$, the exogenous change in technology, and that the cost of a sample declines with experience in the standard learning curve way (log linear in total sampling to date), except that each innovation of a new technology discounts prior experience.
<!-- para 28 -->
We assume that the pools of resources available to the two kinds of search are different.
The organization is assumed to have a (changing) propensity to search, $S_{s,t}$.
This propensity establishes the fraction of apparent organizational resources that are available for search activities at times $t, U_{s,t}$.
Thus
<!-- para 29 -->
$$ \begin{align*}U_{s,t}=&S_{s,t}(P_{t-1}+R_{t-1}+I_{t-1})\\=&S_{s,t}[(1+a_{t-1})T_{*,t-1}].\end{align*} \tag{11} $$
<!-- para 30 -->
The pool of resources available to innovation search and refinement search depends on, but does not equal, $U_{s,t}$.
This partial decoupling of the investment budget and the allocation of resources to specific projects has been noted by several authors [Allen (1970), Reeves (1958)].
We assume that the primary source of resources for innovation, $U_{i,t}$, is organizational slack.
That is, the model reflects a tendency for organizations to support search for innovation from ‘excess’ resources and to contract such search when resources are apparently short, and for successful firms to make more radical product and process innovations than unsuccessful firms [Mansfield (1963)].
If the organization has been successful in meeting its performance goal in the previous time period, a relatively large pool of organizational resources is potentially available.
If the goal has not been reached, the pool of resources potentially available is curtailed.
Conversely, resources available for refinement, $U_{r,t}$, are greater after a failure to reach the performance goal than they are after success.
Thus, if the performance goal was achieved:
<!-- para 31 -->
$$ U_{i,t}=U_{s,t},\quad\mathrm{and} \tag{12} $$
<!-- para 32 -->
$$ U_{r,t}=(U_{s,t})^{1/h_{r}},\quad\mathrm{where}\;h_{r}\geq1. \tag{13} $$
<!-- para 33 -->
If the performance goal was not achieved:
<!-- para 34 -->
$$ U_{r,t}=U_{s,t},\quad\mathrm{and} \tag{14} $$
<!-- para 35 -->
$$ U_{i,t}=(U_{s,t})^{1/h_{i}},\quad\mathrm{where}\;h_{i}\geq1. \tag{15} $$
<!-- para 36 -->
These resources are available for allocation in each time period.
We assume that organizations adapt their actual search expenditures to their (possibly confusing) experiences in the following way.
First, they observe the apparent relation between changes in search expenditures and changes in performance.
Then they adjust their search propensity, an index of intention to allocate resources to search, in a direction that appears to be suggested by a simple consideration of the results: Thus, if search increased and targets subsequently were achieved, then search propensity increases; if search increased and targets subsequently were not achieved, then search propensity decreases; if search decreased and targets subsequently were achieved, then search propensity decreases; if search decreased and targets subsequently were not achieved, then search propensity increases.
<!-- para 37 -->
The general propensity to devote resources to search of either type, $S_{s,t}$, the search propensity for refinement, $S_{r,t}$, and the search propensity for innovation, $S_{i,t}$, are numbers between 0 and 1.
They are determined in the following way:
<!-- para 38 -->
$$ S_{r,t}=Q_{r,t}b_{3}+S_{r,t-1}(1-b_{3}), \tag{16} $$
<!-- para 39 -->
$$ S_{i,t}=Q_{i,t}b_{4}+S_{i,t-1}(1-b_{4}), \tag{17} $$
<!-- para 40 -->
$$ S_{s,t}=Q_{s,t}b_{5}+S_{s,t-1}(1-b_{5}). \tag{18} $$
<!-- para 41 -->
Each Q is assigned a value of one or zero that reflects previous changes in search and subsequent experience (see above).
For example, if refinement search increased in the previous period and the performance target was subsequently achieved, or if refinement search decreased and the target was not achieved, then $Q_{r,t}$ is assigned a value of one.
The learning rates, $b_{3}$, $b_{4}$, $b_{5}$ are here treated as constants.
<!-- para 42 -->
By applying the propensities to the resources available, we can specify the amount of search expenditure in period t.
The effect of the general propensity to search, $S_{s,t}$, has already been specified in defining $U_{s,t}$ above.
Thus
<!-- para 43 -->
$$ R_{t}=S_{r,t}U_{r,t}, \tag{19} $$
<!-- para 44 -->
$$ I_{t}=S_{i,t}U_{i,t}. \tag{20} $$
<!-- para 45 -->
These expenditures determine, stochastically, the outcomes and subsequent adaptation of the organization to its experience.

## results
<!-- para 2 -->
The model generates a time series of decisions, results, and goals, the details of which depend on a number of initial conditions and parameters, as well as on stochastic variation.
Table 1 displays one particular time series based on one specific set of parameters. [^1] Repeated replication with any particular set of parameters produces a distribution of organizational histories.
Although significant variation across replications with identical parameters is a distinctive feature of the model, the history in table 1 is typical in the sense that it is not conspicuously distinguishable from many others.
In the remainder of this section we identify four general characteristics of the model derived from inspecting such histories.
<!-- para 4 -->
We speculate that some interesting features of organizational learning result from an interaction between a sensible learning process and a confusing world.
The present model exhibits both some properties of sensibility and some limitations imposed on sensibility by ambiguity and uncertainty.
An elementary indication of sensibility in the model is the tendency for organizations to improve their performance over time.
We observe a pattern of modest improvement with small oscillations for most organizations, and spectacular improvement for some.
Fig. 1 displays a 20-period record of the average performance of the model.
<!-- para 5 -->
*Table 1.
A 20-period sample of output from the model*
<!-- para 6 -->
<table border=1><tr><td rowspan="2">Period</td><td colspan="3">Propensities</td><td colspan="3">Expenditures</td><td rowspan="2">Technology</td><td rowspan="2">Performance</td><td rowspan="2">Success</td></tr><tr><td>r</td><td>i</td><td>s</td><td>ref</td><td>inn</td><td>Outcome</td></tr><tr><td>1</td><td>0.45</td><td>0.45</td><td>0.45</td><td>7</td><td>10</td><td>innovate</td><td>51</td><td>33</td><td>failure</td></tr><tr><td>2</td><td>0.40</td><td>0.40</td><td>0.50</td><td>10</td><td>7</td><td>innovate</td><td>59</td><td>41</td><td>success</td></tr><tr><td>3</td><td>0.46</td><td>0.36</td><td>0.55</td><td>11</td><td>11</td><td>refine</td><td>60</td><td>39</td><td>success</td></tr><tr><td>4</td><td>0.51</td><td>0.42</td><td>0.59</td><td>13</td><td>16</td><td>refine</td><td>60</td><td>33</td><td>failure</td></tr><tr><td>5</td><td>0.46</td><td>0.38</td><td>0.53</td><td>15</td><td>9</td><td>refine</td><td>61</td><td>34</td><td>failure</td></tr><tr><td>6</td><td>0.41</td><td>0.44</td><td>0.58</td><td>14</td><td>11</td><td>refine</td><td>63</td><td>37</td><td>failure</td></tr><tr><td>7</td><td>0.47</td><td>0.40</td><td>0.52</td><td>15</td><td>9</td><td>refine</td><td>63</td><td>35</td><td>failure</td></tr><tr><td>8</td><td>0.42</td><td>0.46</td><td>0.57</td><td>15</td><td>11</td><td>refine</td><td>64</td><td>40</td><td>success</td></tr><tr><td>9</td><td>0.38</td><td>0.51</td><td>0.61</td><td>11</td><td>21</td><td>refine</td><td>65</td><td>34</td><td>failure</td></tr><tr><td>10</td><td>0.44</td><td>0.46</td><td>0.55</td><td>16</td><td>12</td><td>refine</td><td>65</td><td>35</td><td>failure</td></tr><tr><td>11</td><td>0.40</td><td>0.51</td><td>0.59</td><td>15</td><td>14</td><td>refine</td><td>65</td><td>37</td><td>failure</td></tr><tr><td>12</td><td>0.46</td><td>0.46</td><td>0.53</td><td>16</td><td>12</td><td>refine</td><td>66</td><td>36</td><td>failure</td></tr><tr><td>13</td><td>0.41</td><td>0.51</td><td>0.58</td><td>15</td><td>14</td><td>refine</td><td>67</td><td>38</td><td>success</td></tr><tr><td>14</td><td>0.37</td><td>0.56</td><td>0.62</td><td>11</td><td>24</td><td>refine</td><td>67</td><td>28</td><td>failure</td></tr><tr><td>15</td><td>0.43</td><td>0.51</td><td>0.56</td><td>15</td><td>13</td><td>refine</td><td>67</td><td>39</td><td>success</td></tr><tr><td>16</td><td>0.49</td><td>0.45</td><td>0.50</td><td>12</td><td>16</td><td>refine</td><td>68</td><td>37</td><td>success</td></tr><tr><td>17</td><td>0.44</td><td>0.51</td><td>0.45</td><td>9</td><td>15</td><td>refine</td><td>69</td><td>41</td><td>success</td></tr><tr><td>18</td><td>0.39</td><td>0.46</td><td>0.41</td><td>8</td><td>12</td><td>refine</td><td>69</td><td>50</td><td>success</td></tr><tr><td>19</td><td>0.35</td><td>0.41</td><td>0.37</td><td>7</td><td>11</td><td>refine</td><td>69</td><td>49</td><td>success</td></tr><tr><td>20</td><td>0.32</td><td>0.37</td><td>0.33</td><td>5</td><td>8</td><td>refine</td><td>69</td><td>55</td><td>success</td></tr></table>
<!-- para 7 -->
Since it is possible that improvement in performance is due more to properties of the search environment than to the learning process, we explore the sensibility of the process further by comparing learned propensities to invest, refine, and innovate with apparent optima for those propensities.
By apparent optima we mean values for the three propensities that would result in maximum return if they were held fixed.
The definition of maximum return is, however, ambiguous.
In general, if we wish to maximize expected value over the next n periods, the optimal value for the search propensities is either 0 or 1, depending on the value of n.
For relatively short time horizons, it is best not to spend any resources on search; for relatively long time horizons it is best to spend as much as possible.
Fig. 2 shows average nth-period performance for various fixed propensities to invest and various time horizons for a particular set of parameters.
Other parameters would change the specific results but not the general picture.
<!-- para 9 -->
*Figure 1.
Average performance over time, 100 organizations*
<!-- para 11 -->
*Figure 2.
Nth-period average performance as a function of propensity to search, 100 organizations*
<!-- para 12 -->
The model does not, in general, result in the extreme values for search propensities indicated by the previous analysis.
Search propensities near 1 are quite unusual.
Propensities near zero are adopted frequently by organizations with very rapid propensity learning rates, but not by others.
There is a tendency for most organizations to learn to set search propensities at a fairly low level, in the range of 0.1 to 0.4.
This might be interpreted as an implicit setting of a short planning horizon, but the behavior stems from the learning process rather than any explicit calculation and suggests that the learning environment may not guarantee the development of optimal search propensities when the optimum propensity is 1.
At the same time, it should be noted that large search propensities are associated with large variation in performance across runs of the model.
The results for the propensity to search are shown in fig. 3.
Thus, if the criterion for maximum performance were to involve considerations of risk, the optimal propensity for large values of n might differ from 1.
<!-- para 14 -->
*Figure 3.
Standard deviation of nth-period performance as a function of propensity to search, 100 organizations*
<!-- para 15 -->
In order to examine the outcome of the model in a situation having a relatively clear optimum other than 0 or 1, the reward for refinement and innovation search can be set at some fixed number with no variance.
Even under these circumstances, determination of the optimum propensities is a non-trivial problem.
The mean of the reward from refinement search decays with refinement draws, thereby mitigating the desirability of refinement search; but the efficiency of search declines with each new innovation, so complete reliance on innovation search is not optimal.
However, by searching the propensity space in increments of 0.1, we can approximate an optimum.
If the mean reward for refinement and the mean reward for innovation are set equal to 10, an optimum is found in the neighborhood of $S_{r,t}=0.2$, $S_{i,t}=0.3$, $S_{s,t}=0.3$ and $S_{r,t}=0.3$, $S_{i,t}=0.4$, $S_{s,t}=0.2$.
Under modest adaptation rates for search propensities, the model reaches such a neighborhood, on average.
<!-- para 16 -->
In general, the model learns in a way that does fairly well with strong signals.
In situations in which search is clearly unwarranted, it generally learns to reduce search, though ordinarily not to zero.
Where the technological opportunities makes discovery of an improved technology likely, learning generally leads to higher propensities.
Numerous exceptions to such results are observed, however.
The process is sensitive to the learning rates involved, and the sensibility of the process is often obscured, particularly in the short run, by the uncertainties of evaluating technologies, by the limited number of draws, and by the fact that expenditure is affected by slack as well as propensities.
<!-- para 18 -->
The model leads to subjectively successful organizations.
Despite the way goals adjust to performance as it improves, thus discounting past levels of performance in assessing current success, most organizations in stable environments are successful in their own terms most of the time.
Table 2 shows the percent of the time periods that the model achieves subjective success as a function of environmental uncertainty and exogenous changes in the technology.
In cases where there is no uncertainty and no exogenous change in the technology, goals are achieved about 93% of the time.
The precise fraction for any particular run depends, of course, on stochastic variation within the model, and as we note below, on learning rates.
<!-- para 19 -->
The tendency of the model to produce successful organizations under conditions of steady or improving environments has consequences for expenditures and learning.
Period to period variations in resources allocated to innovation and refinement are generally due more to the amount of resources available and whether they are seen as slack resources (i.e., whether the organization has been successful in its own terms) than to the search propensities associated with the two.
Short-run changes in resource allocation are, that is, less responsive to learning than to organizational success and failure.
Thus, they both obscure the significance of adaptive propensities and provide the perturbations of decisions on which learning depends.
The magnitude of the slack effect depends on the values of $h_{r}$ and $h_{i}$.
When $h_{r}=h_{i}=1$, there is no effect of success or failure on allocations.
As $h_{r}$ and $h_{i}$ increase above 1, subjective feelings of success and failure have an increasing effect on the allocation of expenditures.
Total expenditures on search are also affected by the slack exponents.
Increase in $h_{r}$ and $h_{i}$ will, other things being equal, decrease the allocation of resources to search.
<!-- para 20 -->
*Table 2.
Percent successes, 100 organizations, periods 11–20, varying environmental uncertainty (a) and exogenous changes in technology ( $b_{2}$ )*
<!-- para 21 -->
<table border=1><tr><td rowspan="2">Environmental uncertainty</td><td colspan="5">Exogenous changes in technology</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>0.975</mn></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>0.990</mn></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>1.000</mn></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>1.010</mn></mrow></math></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>1.025</mn></mrow></math></td></tr><tr><td>a=0</td><td>23</td><td>77</td><td>93</td><td>99</td><td>99</td></tr><tr><td>a=0.05</td><td>35</td><td>86</td><td>94</td><td>97</td><td>97</td></tr><tr><td>a=0.10</td><td>35</td><td>71</td><td>78</td><td>83</td><td>84</td></tr><tr><td>a=0.15</td><td>36</td><td>64</td><td>69</td><td>70</td><td>79</td></tr><tr><td>a=0.20</td><td>38</td><td>58</td><td>64</td><td>67</td><td>75</td></tr><tr><td>a=0.25</td><td>40</td><td>56</td><td>63</td><td>65</td><td>71</td></tr><tr><td>a=0.50</td><td>47</td><td>53</td><td>54</td><td>57</td><td>60</td></tr></table>
<!-- para 22 -->
The general pattern of success in steady or improving environments means that the model shows, under those conditions, a tendency for organizations to spend relatively more on innovation than refinement, and to become relatively more efficient at it.
Conversely, any tendency to failure produces relatively more spending on refinement than innovation, and leads to an organization becoming relatively more efficient at it.
Thus, the extent to which the propensity to refine and the propensity to innovate diverge depends in large measure on the relative frequency of successes and failures.
An inspection of table 2 suggests that organizational differentiation in the propensity to engage in refinement and innovation search will depend, therefore, on the level of environmental uncertainty and the exogenous changes in technology as much as on differences in the efficacy of the two types of search.
An exogenously declining technology will, by increasing the frequency of failure, increase relative efficiency in refinement search and result in relatively high propensities to engage in such search.
On the other hand, an improving technology will, by increasing the frequency of success, produce refinement propensities that are relatively low.
Environmental uncertainty tends to vitiate such effects.
That is, high uncertainty reduces the frequency of subjective success when the technology is improving or declining slightly; it reduces the frequency of failure when the technology is declining significantly (i.e., when $b_{2}$ is less than 0.98).
<!-- para 24 -->
Two common properties of stochastic processes are conspicuous in the model.
First, draws from the technological distributions occasionally yield extreme values.
For the most part, low extreme values are irrelevant; but high extreme values (major innovations) affect the position of the organization significantly and, in most case, permanently.
Second, the consequence of one (random) step is often to change the probabilities associated with the next step.
This is most obvious in the way in which the good fortune of discovering a major innovation not only makes substantial changes in technology, but also in the allocation of resources to search, in aspirations, and in efficiencies at search.
These adaptations, in turn, lead to different sequences of events than would have been experienced in the absence of such discoveries.
Organizational histories are produced through a combination of chance events and adaptations to those events that, in some cases, considerably amplify the effects of chance.
<!-- para 25 -->
Path dependence is particularly notable in the case of extreme draws from the distribution of possible technologies, but it is also exhibited by the more prosaic tendency for a subjective success to lead to a subsequent success and a subjective failure to lead to a subsequent failure.
The model produces fewer period-to-period changes from success to failure or failure to success than would be expected merely from their relative frequencies.
This serial correlation is sensitive to the rate at which an organization adapts its goal to performance, the degree of environmental uncertainty, and the size of exogenous changes in the technology.
The basic results are shown in table 3, where we record the number of organizations (out of ten) for which period-to-period changes from success to failure, or failure to success, exceeded the number that would have been expected simply from chance and the overall proportions of the two outcomes for that organization.
Cases in which the number of changes precisely equaled the expected number are treated as being one-half above and one-half below expectations.
If there were no serial correlation in results, the numbers in the table should vary around 5.
Over most of the situations examined, the numbers are less than that (positive serial correlation), but high levels of environmental uncertainty in combination with rapid goal adaptation lead to more frequent changes than would be expected (negative serial correlation).
<!-- para 26 -->
A positive serial correlation of successes and failures accentuates the effects of success and failure on the development of efficiencies in search and the propensities to search.
Organizational slack tends to remain high, or low, for several periods; and the organization builds efficiency in one or the other of the types of search.
At the same time, a series of successes has the effect (on average) of increasing expenditures on innovations and thus of increasing the propensity to invest in a search for innovations.
When there is a shift from failure to success, the level of expenditure on innovation rises, due primarily to the slack condition.
Subsequently, the propensity to search for innovation rises as a result of success (which is likely because of the serial correlation of successes).
The two effects combine to produce a further increase in expenditure, followed by further success, and so on.
This result occurs even under conditions in which no actual innovation takes place and does not depend on the relative desirability of innovation and refinement.
<!-- para 27 -->
*Table 3.
Number of organizations (out of 10) showing more than expected changes from success to failure or failure to success, 20 periods, varying environmental uncertainty (a), exogenous changes $(b_{2})$, and goal learning rate $(b_{1})$*
<!-- para 28 -->
<table border=1><tr><td rowspan="2"></td><td colspan="3">Environmental uncertainty</td></tr><tr><td>a=0</td><td>a=0.05</td><td>a=0.10</td></tr><tr><td colspan="4">Exogenous decline (<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>0.99</mn></mrow></math>)</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#x0003D;</mo><mn>0.1</mn></mrow></math></td><td>0</td><td>0</td><td>2</td></tr><tr><td>=0.3</td><td>0</td><td>0</td><td>2</td></tr><tr><td>=0.5</td><td>0</td><td>0</td><td>5</td></tr><tr><td>=0.7</td><td>0</td><td>3</td><td>8</td></tr><tr><td>=0.9</td><td>0</td><td>7</td><td>9</td></tr><tr><td colspan="4">No exogenous change (<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>1</mn></mrow></math>)</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#x0003D;</mo><mn>0.1</mn></mrow></math></td><td>0</td><td>0</td><td>1</td></tr><tr><td>=0.3</td><td>0</td><td>0</td><td>3</td></tr><tr><td>=0.5</td><td>0</td><td>0</td><td>6</td></tr><tr><td>=0.7</td><td>0</td><td>2</td><td>9</td></tr><tr><td>=0.9</td><td>0</td><td>5</td><td>7.5</td></tr><tr><td colspan="4">Exogenous increase (<math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>2</mn></msub><mo>&#x0003D;</mo><mn>1.005</mn></mrow></math>)</td></tr><tr><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><msub><mi>b</mi><mn>1</mn></msub><mo>&#x0003D;</mo><mn>0.1</mn></mrow></math></td><td>0</td><td>0</td><td>1</td></tr><tr><td>=0.3</td><td>0</td><td>0</td><td>4</td></tr><tr><td>=0.5</td><td>0</td><td>2</td><td>4</td></tr><tr><td>=0.7</td><td>0</td><td>1</td><td>8</td></tr><tr><td>=0.9</td><td>0</td><td>5</td><td>10</td></tr></table>
<!-- para 30 -->
As is clear from the earlier discussion of the model's sensibility, one basic decision problem in the model is the following: Given an indefinitely long planning horizon, the best search strategy is to set search propensities as high as possible and keep them there.
Such a strategy will maximize the long-run potential of the technology and thus maximize performance in the long run.
However, the return on that investment is highly chancy, and a discovery may take many time periods.
Until a discovery is made, high search expenditures reduce the performance of the organization.
As a result, the net advantage (or disadvantage) of high search propensities relative to low search propensities depends on the performance horizon (see fig. 2).
<!-- para 31 -->
A possible inference from such observations would be that, given indefinitely long experience, all organizations should learn to have relatively high search propensities, that average search propensity should increase over time and its variance decline, and that the main effect of learning rates would be on the time it took an organization to adopt high search propensities.
The speculation is not quite correct.
In an indefinitely long period all organizations will, in fact, ultimately make discoveries that put them into new technologies and dramatically improved performance.
This result, however, does not depend on learning to have a large propensity to search but comes simply from the stochastic features of the search assumptions.
Each organization has, at each time period, a non-zero probability (however small) of discovering a spectacular technology and to embark on a long string of successes.
<!-- para 32 -->
The expected length of time that it takes different organizations to make new discoveries depends, however, on variations that are produced in their search propensities by their learning experiences and the adaptation rates for propensities, efficiencies, and goals.
Thus, an organization's performance expectations are a function of its learning rates.
It is not, in general, true that fast learning is best.
Fast learners adapt quickly to correct signals; they also adapt quickly to false signals.
If the false signals lead them to take actions that reduce the experience on which they might correct the error, rapid adaptation can lead to persistent mistakes.
In particular, fast learners may fairly easily learn to reduce expenditures on search to a low level and thus reduce the probability of technological improvement.
Conversely, slow learners are not confused as much by false signals, but neither do they respond as quickly to correct signals.
If their slow response leads them to continue erroneous policies, slow adaptation can also lead to persistent mistakes.
<!-- para 33 -->
Within the present model, long-run performance is, on average, improved by relatively slow, relatively imprecise learning.
Search propensities tend to be less than 0.5, and average propensities for different sets of parameters normally vary between about 0.1 and 0.4.
In the long run, performance will be highest if an organization can learn to set relatively high search propensities in the face of short-run experience that indicates, most of the time, that expenditures on search are unwarranted, and in a situation in which the average quality of outcomes increases with experience.
Quick, precise learning of propensities will do well in the short run, but not in the long run unless there is a lucky early discovery of a new technology or very rapid goal adaptation.
Learning is slowed by having a relatively low rate of propensity adaptation.
It is made imprecise by having a relatively high rate of goal adaptation (and relatively high environmental uncertainty).
<!-- para 34 -->
Fig. 4 shows, for horizons varying from 1 period to 100 periods, the average cumulative performance as a function of the propensity learning rate, where $b_{3}=b_{4}=b_{5}$.
Differences in the outcomes produced by values from 0.2 to 0.9 are modest, but if the rate of learning is reduced to 0.1, the effect on performance is substantial.
There appear to be two major reasons for such a result.
First, organizations that adapt propensities rapidly to experience rather quickly reduce the propensities to relatively low levels.
This, in turn, reduces expenditures and reduces the chances of making a major discovery.
Second, low expenditures on search reduce the accumulation of efficiency at search, and thus make discoveries even more difficult.
A comparable analysis with respect to the rate of goal adaptation shows a quite different picture.
As fig. 5 shows, the goal learning rate has no appreciable effect for planning horizons up to about 30 periods, but after that fast goal learners do systematically better than slow learners.
Rapidly adjusting goals make the success experience of the organization problematic, make learning linked to success and failure difficult, and tend to keep an organization from learning the false lesson that search expenditures are undesirable.
<!-- para 36 -->
*Figure 4.
Average cumulative performance up to period n, as a function of propensity adaptation rate, 100 organizations*
<!-- para 37 -->
The relation between learning rates and performance is complicated not only by the length of time considered but also by interactions among the learning rates.
For example, fig. 6 shows the cumulative average performance for various planning horizons and four different values for the propensity learning rates for the extreme case in which the goal learning rate is 1.0.
This is the case in which the organization, in effect, compares performance at period t with performance at period t−1 in deciding whether to consider the new performance a success or failure.
In this specific situation, the best propensity learning rate is 0.2 with a planning horizon less than 20 periods; it is 0.1 with a planning horizon between 20 and 80 periods; but it is 1.0 with a planning horizon between 80 and 100 periods.
The details of these results, as well as the specific numbers involved, are, of course, a function of the other parameters and initial conditions in the model; but they illustrate the possibilities for significant interactions.
<!-- para 39 -->
*Figure 5.
Average cumulative performance up to period n, as a function of goal adaptation rate, 100 organizations*
<!-- para 41 -->
*Figure 6.
Average cumulative performance up to period n, as a function of propensity learning rate, with goal learning rate=1, 100 organizations*
<!-- para 42 -->
Learning rates also affect the likelihood of subjective success.
As is clear from the discussion above, subjective success and performance are loosely coupled within the model.
Most organizations are successful, but organizations with the lowest proportion of successes (about 50%) can show some of the highest performances.
Indeed, low success rates and rapid alternation in success and failure are ways that false learning is avoided.
Fig. 7 shows the percentage of successes achieved over the first 50 periods for different rates of propensity and goal adaptation.
Since the model is one in which organizations normally improve performance under conditions of no exogenous changes in technology, slowly adapting goals make it fairly easy to keep performance above the goal; thus, regardless of the propensity learning rate, success is associated with slowly adjusting goals.
On the other hand, the propensity learning rate that is best for subjective success depends on the goal learning rate.
For slowly adapting goals, rapid propensity learning leads to maximizing the proportion of periods in which subjective success is achieved; for rapidly adjusting goals, slow propensity learning maximizes the proportion of successes.
<!-- para 44 -->
*Figure 7.
Percent of success over 50 periods as a function of propensity and goal learning rates, 100 organizations*
<!-- para 46 -->
The model is obviously incomplete.
It does not consider the effects of competition and imitation among competitors; it ignores the problems produced by conflict of interest within a learning organization; it does not introduce any significant elements of cognition into a basically behavioral learning process; it assumes a very simple goal structure and a very simple conception of search.
Despite this, or perhaps because of it, the model may tell us something about learning in organizations as a form of behavior and intelligence.
The major assumptions we have used are drawn from the organizational literature.
The four clusters of results are neither surprising nor inconsistent with what we think we know about organizations.
The main claim for the model is that it may provide some link between speculations about organizational learning and observed patterns of organizational adaptation to experience.
<!-- para 47 -->
By elaborating somewhat our portrayal of the relations among learning search strategies, developing search competences, and forming aspirations for search, the model provides an interpretation for some difficulties we have had in identifying consistent factors associated with organizational change [March (1981)].
In particular, it suggests how experiences with exogenously or stochastically driven success or failure can lead to relatively large and relatively permanent changes in organizational behaviors, as well as to substantial differentiation among identical organizations learning in probabilistically identical environments.
It shows some of the learning consequences of satisficing, of sharp organizational distinctions between subjective success and failure.
It describes a behavioral process that makes successes serially correlated.
And it identifies some situations in which sensible learning processes will lead to less than sensible learning, specifically how the intelligence of rapid learning depends on the planning horizon involved and the ways in which false learning about search strategies or aspirations can lead to actions that tend to compound the error.
<!-- para 49 -->
[^acknowledgement]: This research has been supported by grants from the Spencer Foundation, the National Institute of Education, the Hoover Institution, and the Stanford Graduate School of Business.
We are grateful for comments by Julia Ball, Michael D.
Cohen, Scott Herriott, John F.
Padgett, Allyn Romanow, Harrison White, and Sidney Winter.
[^1]: The initial conditions and parameter values are given in the program listing in the appendix (lines 1140–1570).
Unless otherwise noted, these values are used in all results reported here.
