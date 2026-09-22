---
type: sentences-archive
citekey: "lounamaa_1987_adaptive_coordination_of_a_learning_team"
source_md: "D:\Onedrive\Obsidian Vault\文献笔记库\01 导入\论文导入\Lounamaa等-1987-Adaptive Coordination of a Learning Team.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# lounamaa_1987_adaptive_coordination_of_a_learning_team 句子库存

## introduction
<!-- para 1 -->
When noise is introduced in (8), this process of interactive learning and adaptation fails.
Since the noise has a greater impact on performance than any single change in the control variable, the search for a good value for the coordination factor becomes a random, highly unstable, process with an outcome worse than any reasonable fixed level of coordination.
This result stems from two related problems.
The first problem is that the observations are based on just one time period.
The resulting estimate of the performance is unreliable.
Everything else being equal, learning could be made more effective if it were possible to increase the number of observations taken before changing the control variable.
Second, changes in the control variable are sometimes too small, relative to the noise, for their effects to be detected.
Everything else being equal, learning could be improved if it were possible to assure that any changes made in the control variable would be large enough to have a reasonable chance of being detected.
<!-- para 2 -->
Thus, for the coordination factor to adapt effectively to noisy performance observations, two additional heuristics must be added.
The first slows up adaptation in order to assure a larger number of observations.
This is done by specifying K, the minimum number of performance observations required before making a change in coordination.
Instead of using $W_t^0$ in (11), an average of K previous performance signals is used. [^17] The new hill-climbing increment is based on the averages calculated at time t and $t'$, the previous time that $c_t$ was changed:
<!-- para 3 -->
$$ \Delta h_{t}=\frac{\bar{W}_{t}-\bar{W}_{t^{\prime}}}{c_{t}-c_{t^{\prime}}}. \tag{15} $$
<!-- para 4 -->
An appropriate choice of the value for the new parameter K is critical for good performance.
If K is too small, adaptation is close to a random process; and if K is too large, it slows down adaptation too much.
Because a large value for K causes slow but accurate adaptation, a larger K is generally better for final performance than for average performance.
This suggests that the maximum final performance would be achieved if there were enough time to allow a relatively large value for K and still have a suitably large number of changes in the control variable. [^18]
<!-- para 5 -->
In general, longer time horizons (simulation lengths) allow both averaging over longer periods and more changes in coordination, thus leading to better performance.
<!-- para 6 -->
There is, however, an important qualification.
Making K larger ignores the consequences of learning of beliefs by the members.
In particular, if bias is relatively high and no adjustment is made of the level of coordination for an extended period, the members can come to believe that mutual action is impossible, because $q_t$ grows toward infinity if $c_t b > 1$.
In that case, by the time action is taken on the coordination factor, the system will be impervious to it.
Thus, increasing the simulation horizon is not alone sufficient to achieve optimal final performance. [^19]
<!-- para 7 -->
To meet this problem, a second heuristic can be introduced.
In §5 we suggested the need for a scaling rule that limited the magnitude of a change in the coordination variable relative to the previous change.
The primary intent was to keep the change from being inappropriately large.
Now we require a scaling rule that keeps changes from being too small.
Using this heuristic, (15) becomes
<!-- para 8 -->
$$ c_{t+1}=c_{t}+\mathrm{sign}\left(\Delta c_{t}\right)\max\left(|\Delta c_{t}|,\underline{\theta}|c_{t}|\right), \tag{16} $$
<!-- para 9 -->
where $\theta$ denotes the minimum fractional amount that the control variable has to change. [^20] In the simulations reported here, the value 0.2 was used for $\theta$, which means that the magnitude of change had to be at least 20 percent of the control variable's current magnitude.
Smaller values did not have sufficient effect and larger values made the search erratic with a tendency to drive the control variable to zero.
<!-- para 10 -->
The joint effects of $\theta$ and $\bar{\theta}$ are shown in Figure 3, where the result is an average of 100 trials each for the learning rates 0.1, 0.55 and 1.0 with high bias ( $b = 1$) and high strength of interactions ( $q = 1$).
When K is low (0–4), a higher $\theta$ is better, because it increases the signal to noise ratio, but a lower $\bar{\theta}$ is better, because it avoids spurious adaptation.
When K is high, a higher $\theta$ and a higher $\bar{\theta}$ are better, because both result in a larger step size, compensating for the time lost while sampling.
Increasing $\bar{\theta}$ increases the optimal value of K, both because a higher K avoids spurious learning and because a higher $\bar{\theta}$ compensates for the time lost.
Increasing $\theta$ increases the change in coordination.
The increase has two effects: It increases the signal to noise ratio and thus makes a lower K possible; at the same time it compensates for the time lost during the formation of the average and thus makes a higher K possible.
The net effect is that increasing $\theta$ has little or no effect on the optimal K.
The overall conclusion from the 100 period simulations is that $\theta$ increases the robustness of the adaptation but does not improve the final performance achieved with a high $\bar{\theta}$ (=10) and medium K (=7).
When we extend the simulations to a larger number of time periods, it is possible to improve performance by using larger values of K, thus gaining more information about changes, provided $\theta$ is large enough to prevent losing control over the process.
<!-- para 11 -->
The effect of varying learning rates is shown in Figure 4, where $\theta = 0$, $\bar{\theta} = 10$, $b = 1$ and $q = 1$.
The figure shows the average of 100 trials and the final performance for each learning rate.
When learning by members is relatively slow, final performance increases as K increases.
However, when learning by members is relatively rapid, final performance decreases rapidly with increase in K.
Rapidly learning members drive the system to a point beyond effective control if the coordinator delays long enough to have a reliable sample of observations.
As a result, the conclusion drawn from the fixed coordination case that medium learning rates produce the best average performance needs to be qualified.
The conclusion holds for low values of K, but not for higher K.
With higher K, the performance of medium learning rates deteriorates.
A lower learn-
<!-- para 13 -->
*Final Performance*
<!-- para 15 -->
Average Performance
<!-- para 16 -->
*Figure 3.
Impact of increasing maximum allowed change, $\bar{\theta}$, and minimum required change, $\theta$, on final and average performance*
<!-- para 17 -->
ing rate on the part of members allows for a slower, more precise, controller which in turn leads to better average performance.
The general conclusion to be drawn from the analysis of simultaneously learning by members of a team and adaptive control by a coordinator is that, under conditions of noise, and in the absence of methods for slowing both the rate of learning by members and the rate of adaptation by the coordinator, the process is subject to instabilities that threaten effective joint learning.
Thus,
<!-- para 19 -->
Final Performance
<!-- para 21 -->
Average Performance
<!-- para 22 -->
*Figure 4.
Impact of the learning rate of members, $\alpha$, on the relation between minimum number of performance observations, K, before changing coordination and performance*
<!-- para 23 -->
in contrast to the case of noise-free learning, noisy observations of performance put fast learning organizations at a disadvantage.

## discussion
<!-- para 2 -->
A central dilemma in modern organization theory and operations research is the mismatch between the analytical capabilities of human institutions and the complexity of the environment in which they function.
Although large bureaucratic institutions are impressive extensions of the already impressive intelligence of individual humans, they seem persistently to be imperfect instruments for solving the problems they face.
Contemporary response to this mismatch has involved three broad strategies.
The first strategy has been to improve the analytical capabilities of the institutions through training and by introducing various forms of simplifications of the analytical problem.
This is the approach of much of operations research and decision theory (Raiffa 1961).
The second strategy has been to refine competition and selection mechanisms so that rules of behavior leading to better solutions survive and reproduce more reliably than do inferior rules.
This is the approach of various evolutionary theories of human institutions, including substantial elements of market economics (Nelson and Winter 1982).
The third strategy has been to rely on incremental learning from experience as a way to discover good solutions to complex problems.
This is the approach of substantial parts of the behavioral literature on organizations (Cyert and March 1963).
<!-- para 3 -->
The present paper is in the third of these traditions.
It explores the possible intelligence of simple experiential learning in a situation in which different parts of an organization are learning simultaneously, and the actions each takes affect the others.
The implications to be drawn from the analysis depend on some features of the model (most notably the absence of conflict among the members and the fact that one type of learning impacts the stability of another type of learning) that limit their generality.
Nevertheless, they may cast some light on the possibilities and limitations of incremental experiential learning as an instrument of organizational intelligence. [^21] Although learning clearly is a powerful mechanism with considerable relevance to improving organizational performance, the most general conclusion to be drawn from this model is that these simple forms of learning and adaptation require relatively careful calibration in order to be successful in moderately complex situations.
In the absence of calibrating heuristics, experience becomes a poor teacher, and learning fails.
Experience becomes a poor teacher primarily because the relation between the actions of individuals in the organization and overall organizational performance is confounded by the simultaneous learning of other actors and by errors in perceiving performance.
<!-- para 4 -->
In contrast to recommendations that call for making organizations able to respond more quickly and to learn more rapidly, the model suggests some different rules for using organizational learning to improve organizational performance: Slow the Rate of Adaptation.
One conspicuous way in which the model fails is by being impatient when environmental signals are ambiguous.
This is true with respect both to learning by members and to adaptation by the coordinator.
If adjustments in coordination are made too frequently, they are based on observations that are too unreliable.
The observations are unreliable because of the twin effects of noise and multiple simultaneous changes.
Initiating changes less frequently counteracts the noise by providing a larger sample size and reduces the effect of simultaneous changes.
The difficulty is that the system may move out of control while it is still being studied.
By the time a reliable understanding of the structure can be developed, the dynamics may have brought the system to catastrophe.
Although it is clear that change must normally be introduced before everything is known, the major conclusion is that it is unwise to be making continuous adjustments.
Similarly, it is not true that fast learning of beliefs by members assures the best outcomes, either in the short or the long run.
The basic problem with fast learning rates is that false lessons are learned rapidly as well as true lessons.
The result is a system that tends to track misleading signals produced by noise and the simultaneous learning by others, and to produce confusing signals.
Slow learning is less efficient in noise-free, simple worlds; but when there is significant error in the observation of outcomes, it is better to be changing beliefs relatively slowly.
<!-- para 5 -->
Reduce the Simultaneity of Changes.
Learning is confused by trying to associate an outcome with any one of several simultaneous changes.
Under many circumstances, it is better to allow only part of the system to react at any one time.
Thus, we have seen that a strategy of keeping coordination fixed is a reasonably effective procedure in the present case.
Similarly, changing only when outcomes are declining is a procedure that allows one part of the system to learn while another part is held constant.
In noise-free worlds, simultaneity can also be reduced by increasing the speed of learning in one part of the organization while keeping the other part's rate of adjustment relatively slow.
<!-- para 6 -->
Scale the Size of Changes.
We have shown how it is necessary both to avoid changes that are orders of magnitude greater than the changes made briefly before, and to make changes that are substantial enough to make a detectable difference.
The latter requirement is sometimes overlooked in discussions of incremental adjustments, where very small changes might be assumed to be better.
The problem with small changes is that they are likely to be lost in the noise.
Substantial, even arbitrary, changes are important also in noise-free environments.
They allow the organization to escape vicious circles and other traps in the dynamics of interactive learning.
<!-- para 7 -->
These heuristics are not surprising.
They square with some relatively standard folklore about management.
They appear, however, to be counter to the spirit of some discussions of organizational learning.
Insofar as those discussions argue that accelerating the rate of learning is desirable in organizations, this model provides a few cautions.
Those cautions indicate that in an ambiguous world, slow learning may be more effective than fast learning, that quick adjustments within an organization are likely to be both unjustified and confusing to other parts of the organization.
At the same time, they speak for supplementing patience with decisiveness, for making relatively sharp changes when changes are made. [^22]
<!-- para 9 -->
[^1]: That is, she believes that the intercept of the linear margin curve is higher for large cars than for small.
[^2]: The model is defined in such a way that the anomaly of (6) giving a $d_t < 0$ practically never takes place.
If $d_t < 0$, (5) drives $d_t(p)$ to infinity.
In the simulations, we set $d_t = 1$ if this rare event occurs.
[^3]: Errors in expectation are scaled by $d_{t}^{2}$ to obtain the right order of magnitude for $q_{t}$.
To avoid numerical problems, $q_{t}$ is updated only if $d_{t} \geq 0.05$.
[^4]: In all figures, performance is shown as a percentage of optimum performance, achieved with (3).
[^5]: For negative bias, the optimal level of coordination is above one and goes to infinity when b approaches $-q/(2 + 2q)$ from above.
This suggests that the model should be reformulated if negative biases are to be examined, or for negative values of q.
[^6]: The simulations were executed within the Lounamaa and Tse (1986).
[^7]: For the case of zero bias the optimal coordination value is 1.0.
[^8]: The noise specifications used in all simulations are the same.
They assume a uniformly distributed noise between -0.5 and 0.5, that is, a maximum of 50 percent error in the observation of performance.
[^9]: As opposed to multiple candidate algorithms such as learning automata (Narendra and Thathachar 1974) or genetic algorithms (Holland 1975).
[^10]: Usually one uses information about the first- and second-order derivatives in hill-climbing.
The formation of derivatives is inconsistent with our basic objective to model an adaptive mechanism close to what is feasible for human subjects.
This is true in at least two respects.
First, such a process requires centralized estimates by the coordinator of the performance function parameters, which is inconsistent with the assumption of decentralized information in teams.
Second, the second derivative estimates tend to be unstable when other factors influence their values.
In the present model changes in beliefs of the members often affect performance as much or more than changes in the control variable.
Thus, even in the deterministic case, using second-order differences degrades the effectiveness of adaptation.
[^11]: We assume that the same observation is used both for learning by members and for adaptation by the coordinator.
Under unusual circumstances, a change in coordination fails to change performance.
This takes place when $c_t$ would cause a negative $d_t$ according to (6).
If performance is unchanged, $c_{t+1} = c_t - 2\Delta c_{t-1}$ is used instead of (11) to avoid a “death” of the adaptive search process.
This is a relatively crude heuristic that might in principle cause oscillations.
However, in the present case it did not.
[^12]: Because experimentation with alternative levels of coordination tends to iterate the value of $c_{t}$ back and forth over the same interval, thus canceling the effects of the initial direction, this initial direction of movement rarely has an appreciable effect on the dynamics.
A special case, where the initial direction does have a substantial impact, is discussed in the next section.
[^13]: For coordination changes to have any effect the agents have to believe that there are some interaction effects.
For this purpose the value 3.0 was used to $q_{0}$.
[^14]: The form $\Delta c_t = \text{sign}(\Delta h_t) \min(\bar{\theta}|\Delta c_{t-1}|, |\Delta h_t|)$ was found similar in performance but the more smooth nature of (13) was thought to be both more plausible as a description of behavior and to result in a mechanism of more general applicability.
[^15]: An additional scaling heuristic discussed later, the minimum-change requirement may avoid the poor performance, but in a qualitatively different way.
Whereas using the “fighting fires” heuristic avoids getting trapped by the trends, the minimum-change heuristic does get trapped but is able to escape the trap rapidly.
[^16]: A more sophisticated approach than simply not doing anything when substantial learning is going on is to try to estimate the trends in performance attributable to learning by others and subtract these trends when.
[^17]: Exponential averaging was also explored but resulted in slightly lower performance.
[^18]: It would be possible to make K an increasing function of organizational age and examine the optimal rate and pattern of change in K.
Since larger values of K can be described as producing more cautious behavior, such an investigation might cast light on sources of advantage stemming from increasing conservatism of organizations with age.
We have not attempted such an investigation.
[^19]: In this particular model, this result can be overcome by setting the initial coordination at zero instead of one, in which case the second heuristic below is not needed.
But the more general proposition would remain: there is a classical trade-off involved in delay, a trade-off between gaining precision in control by collecting more information and losing control by failing to exercise it.
[^20]: Thus, change in coordination is bounded above by $\bar{\theta}|\Delta c_t|$ and below by $\theta|c_t|$.
[^21]: For other explorations in a similar spirit, see Levinthal and March (1981) and Herriott, Levinthal, and March (1985).
[^22]: This research has been supported by grants from the Spencer Foundation, the Stanford Graduate School of Business and the Hoover Institution.
We are grateful for the assistance of Ann Bush and Stephen Mezias and for the comments of Scott Herriott, Daniel Levinthal, and Edison Tse.
