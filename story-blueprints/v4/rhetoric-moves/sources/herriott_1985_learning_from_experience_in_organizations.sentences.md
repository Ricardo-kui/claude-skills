---
type: sentences-archive
citekey: "herriott_1985_learning_from_experience_in_organizations"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\Herriott等-1985-Learning from Experience in Organizations.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# herriott_1985_learning_from_experience_in_organizations 句子库存

## introduction
<!-- para 1 -->
Diffusion of Experience.
In a social environment, learning from direct experience is supplemented by the diffusion of experience, that is, by copying others.
From a rational perspective, copying can be seen as a way of increasing (on average) the amount of experience from which an individual draws while decreasing (on average) the linkage between that individual's situation and the experience base of action.
From a behavioral perspective, it can be seen as a standard way by which adaptive systems deal with uncertainty and ambiguity.
<!-- para 2 -->
If we let $A_{j,i,t}^{*}$ be the proposed allocation of individual j to activity i at time t, a natural extension of (2) yields
<!-- para 3 -->
$$ \begin{align*}A_{j,i,t}^{*}&=(1-d_{1})\\&\times\Big[A_{j,i,t-1}+b_{1}\big(L_{i,t}-A_{j,i,t-1}\big)\Big]\\&\quad+d_{1}\sum_{h\neq j}A_{h,i,t-1}/(n-1).\end{align*} \tag{6} $$
<!-- para 4 -->
That is, allocations adapt to the mean allocation made by other actors, as well as to direct experience.
<!-- para 5 -->
If we let $k_{j,i,t}$ be the competence of individual j at activity i at time t, a natural extension of (4) yields
<!-- para 6 -->
$$ \begin{align*}k_{j,i,t}=&\left(1-d_{2}\right)\left\{\left(1-b_{3}\right)k_{j,i,t-1}\right.\\&\left.+A_{j,i,t-1}b_{4}\Big[1-\left(1-b_{3}\right)k_{j,i,t-1}\Big]\right\}\\&\left.+d_{2}\max_{h}k_{h,i,t-1}.\right.\end{align*} \tag{7} $$
<!-- para 7 -->
That is, competences adapt to the highest level of competence exhibited within the population of actors.
<!-- para 8 -->
If $G_{j,t}$ is the goal of individual j at time t, then a natural extension of (5) yields
<!-- para 9 -->
$$ \begin{align*}G_{j,t}=&\left(1-b_{4}\right)G_{j,t-1}\\&+b_{4}\Bigg\{\left[d_{3}\sum_{h\neq j}P_{h,t-1}/(n-1)\right]\\&\quad+\left[(1-d_{3})P_{j,t-1}\right]\Bigg\}.\end{align*} \tag{8} $$
<!-- para 10 -->
That is, an actor’s goals adapt to the mean performance of other actors, as well as to her own performance.
The adaptation coefficients $(d_{1}, d_{2}, d_{3})$ determine the rate at which allocations, competences, and goals spread from one learner to another.
<!-- para 11 -->
Interdependence of Experience.
Where experience is interdependent, the performance realized by any one actor depends not only on that actor's allocations and competences, but also on the actions of others.
The interdependencies may involve “mating,” in which each actor’s rewards for a particular activity are augmented by having other actors engaged in the same activity.
They may involve competition, in which each actor’s rewards for a particular activity are decreased by having other actors engaged in the same activity.
They may involve “hunting,” in which the rewards of some actors are increased by the presence of other actors engaged in the same activity who, themselves, have their rewards decreased by the joint presence.
In the present paper, we consider only the competitive case.
If more than one actor allocates effort to a particular activity, the allocation and competence of each reduces the return for the others.
Specifically, in any time period where $\sum_{j} k_{j,i,t} A_{j,i,t} > 1$, the return from activity i for actor j is
<!-- para 12 -->
$$ R_{j,i,t}=\frac{\left(k_{j,i,t}A_{j,i,t}\right)^{w}}{\sum_{h\neq j}\left(k_{h,i,t}A_{h,i,t}\right)^{w}}C_{i,t}. \tag{9} $$
<!-- para 13 -->
The power w determines the way in which an overexploited activity is shared among competitors.
<!-- para 14 -->
Organizational Subunits.
Many economic actors are organizations—firms, armies, public bureaucracies, schools, unions.
Organizations have subunits whose actions affect outcomes and whose rewards are linked to local results, as well as to overall performance.
We have modeled organizations consisting in subunits, similarly allocating among activities, while adapting allocation, competences, and goals over time.
Since allocations within subunits affect not only the performance of subunits but also the performance of the organization as a whole, organizational learning is heavily interactive.
The details are omitted here.
They parallel the earlier characterizations of learning but include some additional features to link the learning and performance of subunits with the overall organization.

## results
<!-- para 2 -->
We report here some fragmentary results based on analysis of the determinate $(b_{2}=1)$ case involving only two alternative activities with unchanging (but different) potentials.
We address ourselves to four general questions relevant to assessing trial-by-trial learning as a form of intelligence: 1) To what extent does incremental learning of this type produce, after a suitably long period of time, sensible adaptations to environmental possibilities? 2) To what extent are long-run outcomes independent of initial allocations, competences, and goals? 3) To what extent is the long-run performance of learners improved by increasing the learning parameters? 4) To what extent is the long-run performance of learners improved by tuning the adjustment of allocations more finely to the magnitude of success or failure?
<!-- para 4 -->
If adjustment of allocations over time is roughly tuned (i.e., if $b_{1}$ is fixed), the isolated learner specializes.
That is, an equilibrium is reached at which all resources are devoted to one alternative or the other, and where $k_{i} = b_{4}A_{i}/(b_{3}+b_{4}A_{i}-b_{3}b_{4}A_{i})$.
Specialization is also characteristic of the stochastic version of the model (i.e., $b_{2}<1$).
Specialization may not involve the superior alternative, however.
The equilibrium outcome depends not only on the learning parameters but also on the initial allocation, competence, and goal.
In general, as the initial conditions become more favorable to the inferior alternative, the set of learning values that result in specialization at the inferior value expands.
<!-- para 5 -->
Given initial conditions in which competence in and allocation to an inferior alternative are high, specialization in that activity is likely.
It can be avoided by slow adjustment of allocations and rapid adjustment of goals, or by learners whose absolute level of performance declines over time (thus producing failures).
With fixed capacities for the two alternatives, the latter result requires that the competence decay rate $(b_{3})$ be high relative to the competence learning rate $(b_{4})$, that is, slow learning and fast forgetting.
<!-- para 6 -->
In the “finely tuned” case, where the adjustment of allocations is made proportional to the absolute disparity between performance and goal, the model also reaches a stable mixture of allocations, competences, goal, and performance; but the allocation does not, in general, reach 1 or 0.
Rather, it locates an equilibrium combination at some interior, suboptimal point.
Thus, fine-tuning yields higher performance in situations in which rough-tuning leads to specialization in the inferior alternative, but not in those cases where rough-tuning leads to specialization in the superior alternative.
<!-- para 8 -->
The effects of diffusion of experience among parallel (but noninteracting) learners depends on characteristics of the population of learners.
The discussion here is limited to the case of a population heterogeneous with respect to the values of $b_{1}$ and $b_{5}$, but homogeneous with respect to the other learning rates (i.e., $b_{2}=1$, $b_{3}=0.1$, $b_{4}=0.5$).
Diffusion of allocations decreases both the mean and the variance of performance within the population (relative to isolated learners), normally driving all actors to a common set of allocations, competences, and goals.
Diffusion of competence, goals, or both normally increases average performance.
In addition, the diffusion of competence changes the region of the parameter space that leads to specialization in the superior alternative, giving an advantage in that respect to learners who adjust allocations relatively quickly and adjust goals relatively slowly.
<!-- para 9 -->
Goal diffusion, by making goals more homogeneous among learners than is performance, tends to divide a population of non-competing learners into one group with a history of subjective successes, another with a history of subjective failures.
Since persistent success produces specialization and persistent failure produces nonspecialization, goal diffusion partitions the population into three groups of actors.
The first group allocates all its resources to the inferior alternative; the second allocates all its resources to the superior alternative; the allocation by the third group oscillates around an equal division between the two.
The proportion in each group depends on the initial conditions and learning parameters.
It also depends on whether the allocation adjustments are finely or roughly tuned, with fine-tuning tending to produce a larger number of learners who fail consistently and thus divide their allocations equally among the alternatives.
<!-- para 11 -->
The effects of competition depend on the number of competitors and the parameter w that controls the way in which the resources in an overexploited activity are divided among competitors, as well as the characteristics of the population of competitors.
With small numbers of competitors (n = 2, n = 3), specialization is common.
In the case of two competitors, this means each competitor specializes in a different activity.
Under many, but not all, conditions, the slower learner becomes the specialist in the superior alternative, thus has higher performance.
In the case of three competitors, a quite typical result is that one or two of the three specialize, while the other does not.
Faster learners tend to become specialists, but whether that results in their also having higher performance depends on the alternative in which they specialize and the pattern of allocations by the others.
<!-- para 12 -->
With larger numbers, both the analysis and the story become more complicated.
In general, if $w > 1$, rapid adjustment of allocations leads to better performance than slow adjustment; if $w < 1$, the converse is true.
If the adjustment of allocations is made proportional to the magnitude of success or failure (the fine-tuning option), the system reaches an apparent equilibrium which depends on the initial allocations and competences as well as the learning rates.
In the fine-tuning case, moderate rates of goal adaptation often seem advantageous, but not always.
There are also numerous situations with relatively idiosyncratic outcomes.
In otherwise apparently smooth response surfaces mapping variations of performance onto variations in learning rates, substantial spikes appear.
<!-- para 14 -->
If diffusion and competition are both present, we obtain many of the same basic results observed in the case of either alone.
Goal diffusion, however, confounds the general observation that rapid, rough-tuned adjustment of allocations gives an advantage where $w > 1$.
When goals diffuse, competitors who are persistently successful tend to become specialists in one activity or the other.
Fast learners tend to specialize, but the fastest learners often specialize in the inferior alternative, leaving the superior alternative to the their somewhat slower cousins.
In addition, variation in performance within the population of competitors tends to be decreased by allocation diffusion, but increased by competence or goal diffusion.
<!-- para 16 -->
Over a fair range of situations, the consequence of introducing learning subunits is to make both the intelligence of learning through trial-by-trial adaptation and its analysis somewhat problematic.
The interactions make it less likely that organizations will specialize in inferior activities, but also less likely that they will specialize in superior activities.
In this respect, the existence of subunits produces effects not unlike the presence of random error in performance.
Although it seems likely that there are regular cycles in the resulting patterns of adaptations, we have not as yet discovered them.

## discussion
<!-- para 2 -->
To provide a base for considering experiential learning as a form of adaptive intelligence, we have modeled a collection of behavioral observations about the forms of learning common in organizations.
Since there is ample experimental and observational evidence for believing that simple experiential learning can be a powerful procedure for improving human performance and since the informational, computational, and coordinative requirements of adaptive intelligence seem to be closer to the capabilities of individual and organizational decision makers than are the demands of anticipatory intelligence, we explore the conditions for sensibility of this kind of incremental adaptation.
<!-- para 3 -->
Although analysis of the models is very incomplete and much of the structure remains unexplored, we can begin to answer the four questions with which the present discussion began. 1) Learning of the sort we have described leads reliably to optimal choices in some situations, but does not do so in others. 2) Allocations at equilibrium are not determined uniquely by activity potentials, but are extensively dependent on the rates at which adaptations take place and on initial allocations and competences. 3) Although fast learners often do better than slow learners, there are many plausible situations in which slow learners do better than fast learners. 4) Although fine-tuned adjustment of allocations facilitates locating an equilibrium, the equilibria achieved are not reliably better than the long-term results of a rougher-tuned adjustment, in fact, are often worse.
<!-- para 5 -->
[^acknowledgement]: Herriott: Department of Management, University of Texas, Austin, TX 78712; Levinthal: Graduate School of Industrial Administration, Carnegie-Mellon University, Pittsburgh, PA 15213; March: Graduate School of Business, Stanford University, Stanford, CA 94305.
This research has been supported by grants from the Spencer Foundation, the Mellon Foundation, the Stanford Graduate School of Business, and the Hoover Institution.
