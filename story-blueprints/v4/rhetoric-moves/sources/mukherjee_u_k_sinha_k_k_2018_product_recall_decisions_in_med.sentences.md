---
type: sentences-archive
citekey: "mukherjee_u_k_sinha_k_k_2018_product_recall_decisions_in_med"
source_md: "D:\Onedrive\Obsidian Vault\00 工作台\项目\Reference for Recalls\Mukherjee, U. K., & Sinha, K. K. (2018). Product recall decisions in medical device supply chains.md"
created: 2026-09-20
sentence_filter: min_chars=0
note: >-
  跨源合成原料库存（distill-paper-exemplar L0 --keep-sentences 生成）。只读；
  语料句子可直接采用；替换来源特异性内容（专名/数字/系数/表号）。
---

# mukherjee_u_k_sinha_k_k_2018_product_recall_decisions_in_med 句子库存

## introduction
<!-- para 2 -->
Product recalls disrupt supply chains and are associated with severe negative consequences that are not only economic but also social and reputational.
It is not uncommon for recalls to be linked with injuries, hospitalizations, and deaths.
Therefore, it is imperative for manufacturers and regulatory agencies to proactively detect and respond to signals of potential product recalls present in the market feedback from users on adverse events related to products.
Such efforts would be fundamental to avoiding or minimizing supply chain disruptions and the negative consequences of recalls.
<!-- para 3 -->
Recent incidences of product recalls in several industry sectors demonstrate that most recall decisions are reactive and not proactive.
In fact, there is compelling anecdotal evidence which suggests that firms often do not react to user feedback on adverse events related to products in a timely manner.
The reaction is either too slow or too fast, causing negative but avoidable consequences for firms and product users.
Further, there appears to be the existence of judgment bias when it comes to firms reacting to user feedback on adverse events related to products and making recall decisions.
Specifically, the under-reaction of firms along with the negative consequences of recalls tends to draw public attention, as is evidenced in many media reports – e.g., www.nytimes.com, September 14, 2014. [^1] Over-reaction of firms or FDA along with negative consequences for patients has also been reported in the literature.
For example, Lu et al. (2014) found that an early warning by FDA on anti-depressant drugs without sufficient data and evidence led to decreased usage of anti-depressant drugs and almost 22% increase in suicide rates among teens.
<!-- para 4 -->
The importance of data-driven, evidence-based product recall decisions has been emphasized by several regulatory agencies.
National Highway Traffic Safety Administration has acknowledged that automobile recalls by General Motors could have been managed better with relevant data and analysis (www.bloomberg.com, March 12, 2013). [^2]
<!-- para 5 -->
Advances in digital technologies and the emergence of big data analytics are making it possible for firms and regulatory agencies to collect market feedback from users of products in several forms and through multiple channels.
The user-generated market feedback on products can act as a source of signals to detect potential product recalls either due to design issues or due to manufacturing and supply chain glitches.
In a report on medical devices, the Government Accountability Office (GAO-12-816, 2012) [^3] has identified the need to use more precise approaches, such as Unique Device Identification (UDI), to analyze user-generated market feedback and identify potential medical device recalls on an almost real-time basis.
<!-- para 6 -->
While under-reaction of firms to user-generated market feedback on adverse events related to products spurs media attention, over-reaction to such feedback does not seem to spur similar media attention.
However, our interactions with managers of several medical device manufacturers in the United States indicate the prevalence of over-reaction to user feedback on adverse events related to medical devices.
Hence, the questions that serve as the motivation for this study are:
<!-- para 7 -->
**(i) Do firms systematically exhibit a judgment bias in interpreting user-generated market feedback on adverse events related to their products?**
<!-- para 8 -->
**(ii) If firms do exhibit such a judgment bias, what factors influence under-reaction bias and over-reaction bias?**
<!-- para 9 -->
The empirical context of the study is the medical device industry.
The dataset that is central to conducting this study is a user-reported adverse event database called the Manufacturer and User-Facility Device Experience (MAUDE), assembled and maintained by the Food and Drug Administration (FDA) of the United States.
Each year, FDA receives several hundred thousands of user-generated adverse event reports on either new medical devices (referred to as pre-market approvals [PMA]) or new versions of existing devices (referred to as 510K approvals).
<!-- para 10 -->
In this study, we mine the “big” MAUDE database to generate insights related to the existence of judgment bias in recall decisions of medical device firms.
While the MAUDE database is largely unstructured, it is fine-grained in terms of capturing user experience on an almost real-time and ongoing basis.
In an article on applications of big data in the management discipline, George et al. (2014, p. 321) have highlighted that granularity of information is a defining parameter of big data.
According to Sanders (2014, p. 5), “big data … can be structured or unstructured.” Indeed, variety and the unstructured nature is a key differentiating factor of “big” data.
According to Lynch (2008, p. 28), big data is “big” by way of “being of lasting significance” in terms of the context and the insights that the data can potentially provide.
The context that we analyze is of lasting significance for several reasons.
The rapidly increasing cost of health care in the United States and globally is well recognized (Moses et al. 2013, Wang et al. 2008).
A substantial part of the health care cost is due to the cost of medical devices and equipment (Wang et al. 2008).
Medical device recalls or the failure to recall in a timely manner contributes significantly toward this increasing health care delivery cost.
Decision bias pertaining to medical device recalls is a serious concern for the device user community, the manufacturers, and the regulators.
Apart from the direct cost of health care delivery, medical device recalls have the potential to cause severe harm to individual patients that can range from injuries to hospitalizations to deaths.
Hence, it is important to understand the sources of judgment bias in medical device recalls.
Identification of judgment bias, if any, in recall decisions and an understanding of the sources of judgment bias would help improve the post-market surveillance and make the detection of medical device recalls evidence-based and timely.
Timely detection of potential medical device recalls would reduce the cost and improve the effectiveness of health care delivery.
<!-- para 11 -->
Specifically, in this study, we identify characteristics of user feedback and characteristics of the situated context of the managers that can lead to the underreaction or over-reaction likelihood.
We find that (i) noisy signals in user feedback, that is, high noise-to-signal ratio, are associated with under-reaction likelihood; and (ii) user feedback related to adverse events characterized by high severity is associated with high over-reaction likelihood.
We also find that the situated context of the decision maker, such as firm size, and depth and breadth of product portfolio, is significantly associated with judgment bias.
<!-- para 12 -->
The remainder of the study is organized as follows.
In section 2, we discuss the theoretical foundations of the study and develop our hypotheses.
Next, we integrate the hypotheses into an empirical framework for managerial judgment bias in recall decisions.
In section 3, we discuss the empirical setting, data and research design including empirical modeling strategy and specifications to test the proposed hypotheses.
In section 4, we present the model estimation results and interpret the results in the context of the hypotheses.
In section 5, we present our concluding remarks.

## theory
<!-- para 2 -->
There are two primary sources of judgment bias in product recall decisions by firms that are based on user-generated feedback on adverse events related to their products.
The first source comprises of the characteristics of the signal contained in the user feedback.
The second source is the situated context of decision makers of firms making the recall decisions.
To analyze these two sources of judgment bias, we draw on three related theoretical perspectives to inform the development of the study hypotheses.
First, we use the theoretical perspectives of signal detection (Salkind 2007) and system neglect (Massey and Wu 2005) to introduce the concept of judgment bias and the two types of judgment bias, namely, underreaction and over-reaction.
Second, we use the theoretical perspective of managerial attention and judgment (Bendoly 2011, 2013, Ocasio 1997) to understand the factors that can lead to under-reaction and over-reaction to user feedback on adverse events related to products.
<!-- para 4 -->
The fundamental idea of signal detection is to recognize the presence of a specific state of the system (e.g., a product) from the input data streams (e.g., user-generated feedback on adverse events related to products).
A detection method processes the data stream to pick up a signal and produces a judgment of whether a system level issue is present or not (Harvey et al. 1992, Wagner et al. 2001).
When the operating condition of a system is perfectly normal, the distribution of the data stream generated will be white noise.
However, if a system level issue is present, then the distribution of the data stream will shift and will no longer be a white noise distribution.
From the standpoint of signal detection theory (SDT), this distribution is a combined noise and signal distribution.
The fundamental idea of SDT is to be able to detect the presence of such a signal in the data stream.
The detectability of the signal depends on the strength of the signal as well as the detection process operationalized by the choice of an appropriate decision threshold, as depicted in Figure 1.
<!-- para 5 -->
The decision threshold $X_{c}$ is analogous to a decision criterion used by a decision maker.
In the context of product recall decision from user-generated feedback on adverse events related to products, the decision threshold $X_{c}$ is an adverse event frequency determined by a decision maker above which the decision maker decides to recall and vice-versa.
The decision maker's judgment bias and the decision to recall are manifested in the decision threshold $X_{c}$.
<!-- para 6 -->
In making recall decisions based on user-generated feedback on adverse events related to products, decision makers can make two possible errors originating from their choice of the decision threshold $X_{c}$.
First, decision makers can wrongly detect a signal and recall a device when the device should not have been recalled.
This type of error is called the “false alarm” and the propensity of a decision maker to make this type of error is called the False Alarm Rate (FAR) (Salkind 2007).
Second, decision makers can miss out on detecting a credible recall signal
<!-- para 9 -->
and do not recall a device when the device should have been recalled.
This type of error is called “miss” and the propensity of a decision maker to make this type of error is called the Miss Rate (MR) (Salkind 2007).
<!-- para 10 -->
Let $C_s$ be the sunk cost of a false alarm and $C_o$ be the opportunity cost of a miss.
A rational decision maker would like to minimize the expected costs associated with the two types of errors in judgment, that is, false alarm and miss.
A decision maker chooses a decision criterion so as to minimize the total cost associated with the resulting decision.
The decision criterion of the rational decision maker can be stated as follows:
<!-- para 11 -->
$$ \min_{X_{c}}\{C_{o}*P(Miss Rate)+C_{s}*P(False Alarm Rate)\}. \tag{1} $$
If the noise distribution is $N(\mu_o, \sigma_o^2)$ and the noise plus signal distribution is given by $N(\mu_s, \sigma_s^2)$, then the optimal decision threshold $X_c^o$ is given by Equation (2).
Normalizing the mean of the noise distribution to zero without loss of generality (WLOG), we further simplify the optimal value for the decision threshold as follows; see Appendix S1 for proof.
<!-- para 12 -->
$$ \begin{aligned}X_{c}^{o}&=\frac{\mu_{s}}{2}+\frac{\lambda\sigma^{2}}{\mu_{s}};\lambda=\log(\beta)=\log\left(\frac{C_{s}}{C_{o}}\right)\\&=\log\left(\frac{Sunk Cost of False Alarm Rate}{Opportunity Cost of Miss Rate}\right)\end{aligned} \tag{2} $$
In Equation (2), the parameter $\lambda$ signifies the relative importance of the costs associated with the two alternate decisions, to recall or not to recall.
Relative saliency of the two costs in the mind of a decision maker determines the decision threshold.
<!-- para 14 -->
Both the false alarm rate and the miss rate are dependent on the choice of a decision threshold by decision makers.
A decision threshold $X_{c}$ that is higher than the optimal decision threshold $X_{c}^{o}$ (Equation 2) would lead to a high miss rate, whereas a decision threshold that is lower than the optimal decision threshold $X_{c}^{o}$, would lead to a high false alarm rate.
Decision makers who systematically exhibit a propensity toward one type of error rate over the other are said to exhibit a systematic judgment bias in detecting device recalls from market feedback data (Massey and Wu 2005, Macmillan and Creelman 2005, Wickens 2002).
Thus, we measure judgment bias as per Equation (3).
<!-- para 15 -->
$$
c=\frac{\mathrm{False\ Alarm\ Rate\ (FAR)} - \mathrm{Miss\ Rate\ (MR)}}{2} \tag{3}
$$
<!-- para 16 -->
A measure of judgment bias greater than zero (i.e., c > 0) means a systematic propensity of decision makers to generate more false alarms than misses.
Thus, decision makers exhibit an over-reaction bias when c > 0 (Equation 3).
Similarly, decision makers exhibit under-reaction bias when c < 0 (Equation 3) – that is, a systematic propensity of decision makers to generate more misses than false alarms.
<!-- para 18 -->
The critical factor that determines the optimal decision threshold ( $X_c^o$) is $\lambda$, the natural logarithm of the ratio of the costs associated with false alarm rate and miss rate (Equation 2).
The relative marginal costs associated with the false alarm rate and miss rate depend on the technological complexity and usage risks associated with a specific product.
The expected false alarm rate (FAR) for any device $i$ is given by $\mathbb{E}[FAR] = 1 - \Phi(X_c^o | 0, \sigma^2)$ and the expected miss rate (MR) is: $\mathbb{E}[MR] = \Phi(X_c^o | \mu_s, \sigma^2)$.
For any device where the technology associated factor $\lambda_i$ is zero, that is, the costs associated with false alarm rate and miss rate are equivalent, the expected value of the false alarm rate and the miss rate would be equivalent, that is, $\mathbb{E}[FAR] = \mathbb{E}[MR]$.
However, in reality, if we observe that decision makers are making more of one type of error than the other, we can compute the judgment bias as a mean difference between the two error rates, that is, $Bias_i = \frac{Z(FAR) - Z(MR)}{2}$.
For devices where the associated technology factor is not zero, we have $\mathbb{E}[MR] = \mathbb{E}[FAR] + \beta \sigma \lambda_i$, where $\beta = \frac{\sigma}{\mu_s}$ is a characteristic of the signal, namely, the noise-to-signal ratio.
In such a case, the judgment bias that decision makers exhibit is estimated as a mean difference between the two error rates as above after controlling for technology fixed effect pertaining to a specific device, that is,
<!-- para 19 -->
$$ Bias_{i}=\frac{Z(FAR)-Z(MR)}{2}+\beta\sigma\lambda_{i}. \tag{4} $$
In using user-generated feedback on adverse events related to products for timely detection of product recalls, there are primarily two lines of investigation for evaluating the differential likelihood of the two types of judgment bias, that is, under-reaction bias and over-reaction bias.
The first line of investigation is based on the user-generated adverse event report data stream which is likely to contain the signal for potential recall of a product that would be interpreted by decision makers to make a decision (i.e., to recall or not to recall).
This investigation is guided by the theoretical perspective of system neglect (Massey and Wu 2005).
The second line of investigation is related to understanding the situational context of decision makers making recall decisions – specifically, firm characteristics such as firm size, and product-market conditions such as product portfolio depth and breadth.
This investigation is guided by the theoretical perspective of managerial attention and judgment (Bendoly 2011, 2013, Ocasio 1997).
<!-- para 21 -->
The theoretical perspective of system neglect has been used to understand the judgment bias of decision makers in the contexts of change detection (Massey and Wu 2005) and supply chain forecasting (Kremer et al. 2011).
Massey and Wu (2005) as well as Kremer et al. (2011) show that decision makers systematically deviate from optimal decision threshold for change detection in the context of detection of regime shifts such as changes in market demand, competition and technology.
For a given signal strength, the dispersion of the noise-plus-signal data is a significant predictor of the type and extent of judgment bias.
For a given signal strength, the two factors related to system neglect that are associated with judgment bias are the noise-to-signal ratio $\frac{\sigma}{\mu_s}$ and the natural logarithm of the ratio of the perceived cost of errors in detection of recall signals $\lambda$.
As the noise-to-signal ratio increases, the likelihood that decision makers will adopt a high decision threshold increases.
Hence, high noise-to-signal ratio is likely to be associated with underreaction bias.
The severity of adverse events is indicative of the cost associated with miss rate.
Given the inherent risk averseness of decision makers, a high mean severity of the adverse events is likely to increase the perceived cost of miss rate which is the opportunity cost, thus decreasing the cost ratio $\lambda$.
Decrease in the perceived cost ratio $\lambda$ is likely to be associated with a low decision threshold $X_c$.
Hence, the severity of adverse event is likely to be positively associated with over-reaction bias.
Based on the above discussion, we posit the following two hypotheses:
<!-- para 22 -->
**HYPOTHESIS 1 (H1).
Noise-to-signal ratio in user reports on adverse events related to products is positively (negatively) associated with under-reaction (over-reaction) bias.**
<!-- para 23 -->
**HYPOTHESIS 2 (H2).
Severity of adverse events related to products is positively (negatively) associated with over-reaction (under-reaction) bias.**
<!-- para 25 -->
In a seminal paper on managerial decision making, Bendoly (2011) has shown that managerial judgment deviates systematically from the optimal decisions prescribed by rational economic models.
Bendoly (2011) has shown that the deviation of managerial judgment from optimal decisions is associated with the situational context within which a manager is making recall decisions and the span of judgment tasks that a manager is entrusted with concurrently.
This study along with the subsequent studies (Bendoly 2013, Bendoly et al. 2014), show that the situational context of managers affects managerial attention and judgment significantly.
Hence, apart from the characteristics of the data stream containing the signal, the situated context of the decision makers appears to be critical to explaining the type and extent of judgment bias (Bendoly 2011).
<!-- para 26 -->
The significance of the situated context of decision makers in explaining judgment bias of decision makers was also highlighted in a study on attention based view of firms (Ocasio 1997).
The primary tenet of the attention based view of firms is that a firm is a "system of structurally distributed attention" (Ocasio 1997, p. 189) in which the decisions and actions of individuals cannot be determined by only knowing the characteristics of the decision makers.
Rather, the nature and pattern of decisions can be determined by the organizational contexts in which decision makers find themselves situated.
This perspective is also consistent with Simon (1947), who contended that organizations influence decision makers by shaping the distribution of organizational stimuli that form the attention process of the decision makers.
Ocasio (1997, p. 189) defines attention as "noticing, encoding, interpreting, and focusing of time and effort by organizational decision-makers." Haas et al. (2015), while analyzing managerial attention process in an online community, have found that problem characteristics such as problem-length, problem-breadth and problem-novelty, and problem-crowding are significantly associated with differential attentional process.
Hoffman and Ocasio (2001) find that firms allocate differential importance and attention to different external events.
The saliency of external events is an important predictor of the attention process of a firm, where saliency is defined as the "prominence or importance of a stimulus to a particular (social) context" Hoffman and Ocasio (2001, p. 429).
In the context of managerial attention and judgment related to device recalls, saliency of a signal would mean relative strength of a signal related to a device with respect to other signals that managers are required to attend to in the context of a firm.
Higher saliency created by the extent of immediate media attention trigger higher and faster reaction toward those events as compared to events that have low saliency to a firm.
Li et al. (2013) have used the attention based view of firm to analyze product performance of firms in high tech industry.
Joseph and Ocasio (2012) studied a large multi-business firm and found that firm structure and architecture significantly influence managerial attention process and decision making.
<!-- para 27 -->
The key tenets of managerial attentional process are adequately supported by several scientific studies in neural psychology literature (Walther and Koch 2006).
In this literature, the attentional process is considered to be a selective gating mechanism when managers attend to stimuli that are above a saliency threshold, which, in turn, is determined by the number of and the relative saliency of all available stimuli.
This view from a managerial psychological response to stimuli has been well-established in Bendoly (2011, 2013) and Bendoly et al. (2014).
In the context of projects, Bendoly et al. (2014) have shown that the span of project tasks that a manager is required to attend to has significant impact on managerial attention on specific tasks and switching behavior which, in turn, significantly affects the project outcome.
<!-- para 28 -->
The effect of the number of issues that a firm needs to deal with on the relative saliency of a specific issue and the resulting likelihood of addressing the specific issue can be concisely explained by considering the following simple model of firm attention process.
Following Walther and Koch (2006), let us consider that, at any point in time, the key decision makers in a firm are exposed to N signals related to their internal or external environment.
Let the saliency of each of those N issues be represented by the random variable $S_i: i \in \{1, \ldots, N\}$ distributed according to the distribution function $S \sim f(s)$ with CDF $F(S)$.
WLOG, if we assume that a decision maker is able to attend to one issue at a time and that the decision maker attends to the issue with the highest situated and contextual saliency, then the probability that the decision maker reacts to a specific signal $S_1$ out of those N signals is given by $P[S_1 \geq S_j; j \neq 1] = [F(S_1)]^{N-1}$.
Therefore, we have (see Appendix S2 for derivation):
<!-- para 29 -->
$$ \frac{\partial P[S_{1}]}{\partial N}=-|\log F(S_{1})|[F(S_{1})]^{N-1}. \tag{5} $$
Since in Equation (5), $F(\cdot)$ is a CDF, $0 < F(S1) \leq 1$, for $N > 0$, $\frac{\partial P[S_1]}{\partial N} < 0$; $\forall N > 0$.
Hence, the probability that a decision maker reacts to a specific environmental signal is a decreasing function in the number of signals or stimuli that the decision maker is faced with simultaneously.
This is supported by an empirical study of online knowledge sharing community by Haas et al. (2015, p. 686), where the authors have observed that "because attention is a finite resource, beyond some point a large number of concurrently posted problems may reduce the likelihood that the potential knowledge provider decides to allocate attention to a focal problem."
<!-- para 30 -->
In the context of product recall decisions from user-generated reports on adverse events related to products, it is important to consider firm-related factors that affect the span of managerial attention.
While there are several factors that can affect managerial attention, factors that tend to distribute managerial attention are critical.
Following Bendoly et al. (2014) and Ocasio (1997), we identify firm size as a key firm characteristic that influences the number of available stimuli.
Also, firm size influences allocation and distribution of available stimuli that "channel the attention of administrators" (Ocasio 1997, p. 187).
Accordingly, we contend that firm size is a key dimension of a firm that influences the number of available stimuli, and the distribution of several available stimuli.
There is support in the prior literature for this point-of-view (Bendoly 2011, Haas et al. 2015, Ocasio 1997, Walther and Koch 2006).
While firm size is the broader context that influences managerial attention, the specific decision context relevant to the current study is related to product management – specifically, recall decisions based on user-generated reports on adverse events related to products.
In the context of product recall decisions from user feedback, the nature of managerial attention, specifically the distribution of attention is likely to be influenced not only by the overall firm size, but also by the depth and breadth of the product portfolio.
Hence, we conclude that the depth and breadth of product portfolio that managers are required to attend to is significant in explaining managerial judgment bias in recall decisions.
<!-- para 31 -->
Based on the above discussion, we consider two key factors – namely, firm size and product portfolio breadth and depth – that are likely to affect managerial judgment.
While the situated context of decision makers may be influenced by more factors which are temporal in nature such as profitability, demand and supply conditions, organizational changes, and the changes to the firm environment, we consider the above two factors since they are relatively stable, and are likely to have a lasting effect on managerial attention and focus that influence managerial judgment bias in product recall decisions (Ocasio 1997).
<!-- para 32 -->
Firm Size: The size of a firm determines the extent and span of issues that key decision makers in the firm are faced with at any given point in time.
A large firm is likely to have a much wider span of issues to deal with.
The structural distribution of the different types of issues that decision makers are required to pay attention to is generally much higher in larger firms as compared to smaller firms.
Joseph and Ocasio (2012) argue that large firms are able to put less specific attention on a particular issue due to a wider variety and larger number of issues that they are needed to attend to.
The perceived saliency of market feedback from users on adverse events pertaining to an individual product is likely to be much less in larger firms as compared to smaller firms.
Hence, we hypothesize that the likelihood of under-reaction bias would be high for a large sized firm.
<!-- para 33 -->
HYPOTHESIS 3 (H3).
Ceteris paribus, firm size is positively (negatively) associated with under-reaction (over-reaction) bias.
<!-- para 34 -->
Product Portfolio: Higher levels of product depth and breadth reduce the relative saliency of each product.
Hence, the structural attention that firms are able to allocate to user feedback on individual products is relatively higher for firms with lower levels of product depth and breadth.
Hence, we posit the following hypothesis:
<!-- para 35 -->
HYPOTHESIS 4 (H4).
Ceteris paribus, product portfolio depth and breadth is positively (negatively) associated with under-reaction (over-reaction) bias.
<!-- para 37 -->
We integrate the hypotheses posited above to propose a framework for evaluating judgment bias in making product recall decisions, as shown in Figure 2.
The proposed framework has two levels of abstractions: conceptual and measurement.
At the conceptual level, the signal characteristics of the market feedback from users on adverse events related to products; and the situated context of decision makers making the product recall decisions determine the decision threshold $X_{c}$ of decision makers – that is, whether to recall or not to recall a product – and which, in turn, determines the judgment bias in recall decisions.
Figure 2 depicts the conceptual categories and corresponding measurement level constructs.
The constituent hypotheses of the framework depicted in Figure 2 relate the signal characteristics – captured in terms of the constructs, noise-to-signal ratio and severity of adverse events; and the situated context of decision makers – captured in terms of the constructs
<!-- para 40 -->
, firm size and product portfolio – to over-reaction and under-reaction biases.

## methods
<!-- para 2 -->
The empirical setting for the study is the medical device industry.
Our sample contains MAUDE reports generated from 2002 to 2012, and has upwards of three million usable data points.
Illustrative examples of user-generated feedback on adverse events related to medical devices are presented in Appendix S3.
<!-- para 3 -->
Apart from the MAUDE database, we assembled data from several other sources.
The other databases are: (i) the recall database; (ii) the 510(K) and PMA databases – where 510(K) is premarket notification, that is, the approval process of new models of existing medical devices, and PMA is pre-market approval, that is, the approval process of new medical devices; (iii) the facility registration database; and (iv) COMPUSTAT database.
The research sample contains 108 firms and 1348 devices identified by unique firm code and device code combinations.
<!-- para 5 -->
The primary unit of analysis is a product model that is identified by the combination of a firm code and a product code assigned by FDA for each product.
By way of an illustrative example, a Medtronic defibrillator model is identified by the combination of the general device code for defibrillators and the firm code for Medtronic.
User-generated adverse event reports on products and recall decisions of firms related to products are observed at the level of a firm-product combination.
The firm-related variables are observed at the level of individual firms.
<!-- para 7 -->
The first step in estimating judgment bias is to be able to predict the likelihood of a device recall with precision from user-generated adverse event reports related to the device.
We follow the iteratively following steps in estimating judgment bias: Step 1: Build a recall prediction model of device recall with data from MAUDE and other predictor databases with train data from a 80:20 split of sample into train and test set.
<!-- para 8 -->
Step 2: Compare several models for prediction accuracy based on receiver operating characteristics (ROC).
<!-- para 9 -->
Step 3: Estimate False Alarm Rate and Miss Rate for the prediction model for each of the devices on 20% hold-out test samples repeatedly.
<!-- para 10 -->
Step 4: Estimate Judgment Bias using Equation (4).
<!-- para 11 -->
In the ensuing paragraphs, we discuss the development of a prediction model for device recalls using user-reported adverse events related to medical devices (MAUDE database).
While prediction of recalls is not the central objective of the study, we need to develop the prediction model for device recalls to estimate judgment bias in recall decisions.
<!-- para 13 -->
Data organization represents an important step toward building a predictive model.
MAUDE is generated by data received from hundreds of thousands of users of medical devices.
However, plurality of sources poses challenges in terms of integrating information from several different sources with different formats and coding schemes.
<!-- para 14 -->
The MAUDE database is primarily text-based and also incomplete in its codification.
We used text analytics to organize the databases and link different databases such as the MAUDE and the recall database.
Specifically, we used Latent Dirichlet allocation (LDA) model for classification of the text data in the MAUDE database (Madsen et al. 2005).
Appendix S4 presents a brief introduction to LDA.
<!-- para 16 -->
The unit of analysis for the predictive modeling and judgment bias measurement steps is a medical device recall.
The response variable is a binary recall variable with the unit of time being a quarter (three months).
If a device has been recalled within a quarter, then the value of the response variable is 1 for the quarter.
Otherwise, the value of the response variable is zero.
<!-- para 18 -->
The primary predictor variable for recall likelihood prediction model and judgment bias estimation is the kernel density of adverse events given by $f_t = \left(\frac{1}{Nh}\right) \sum_{i=1}^N I_i \times K\left(\frac{t-T_i}{h}\right)$.
Taking the kernel density instead of a discretized frequency count has several advantages.
Firstly, it allows a continuous time filtering of the signal.
Secondly, kernel densities automatically normalize the data pertaining to different products and product classes.
We also created severity weighted kernel densities to account for severity of each adverse event.
Severity ratings were taken from FDA classification of adverse events.
FDA classifies adverse events into one of five severity classes, namely, 1: no effect on patients; 2: injury not requiring medical attention; 3: injury requiring minor medical attention; 4: injury requiring major medical attention; 5: death.
We also created the 100-day and 300-day lagged kernel densities and severity weighted kernel densities.
<!-- para 19 -->
Apart from the primary predictors, we also generated variables pertaining to covariates related to design, supply chain, and manufacturing.
While the kernel densities of the adverse events are the primary predictors, information related to design, supply chain, and manufacturing captured through the respective covariates is likely to improve the precision of such prediction.
We also included several control variables for the purpose of building the predictive models.
<!-- para 21 -->
As already stated, the prediction modeling step is required to estimate judgment bias.
Figure 3 provides an overview of the prediction modeling and judgment bias estimation framework.
In spite of the best efforts of the firms and regulators in the form of approval testing, performance testing, and quality inspections, many products encounter recalls several times during their effective life-cycle while in use in the market.
Typically, product recalls can be attributed to problems that creep in unforeseeably and belong to one of the following categories: design, manufacturing, and supply chain.
These problems manifest in the form of user generated signals of a recall, that is, a shift in the adverse effect distribution from pure stationary white noise distribution of adverse events which is expected under normal working conditions even when there is no system level source of a recall.
Hence, the primary predictor of a recall is the density distribution of the adverse event reports from users.
When the adverse event reports are supplemented
<!-- para 24 -->
by system level covariates like design covariates, supply chain covariates, and manufacturing covariates, the precision of prediction is likely to improve further.
The prediction framework (Figure 3) conceptually captures this dynamic and interaction of the primary signal of recall prediction and the underlying signal generating process.
The prediction step generates the measurement of judgment bias which is then used as the primary response for the main empirical model depicted in Figure 2 comprising of a set of hypotheses that are to be empirically tested.
<!-- para 26 -->
Variable selection is a key step in predictive model building (Shmueli 2010) to ensure model parsimony and to avoid over-fitting.
While there is no single uniformly best method for variable selection, one of the most commonly used approaches to variable selection is a shrinkage method in fitting a linear model such as Least Absolute Shrinkage and Selection Operator (LASSO) which uses an $L_{1}$ penalization (penalizing the sum of the absolute values of model coefficients) on a maximum likelihood estimation (Zou 2006).
We used a triangulation of LASSO, stepwise generalized Linear Mixed Model (GLMM), and stepwise Generalized Additive Model (GAM).
The triangulation helped in eliminating unnecessary variables while selecting the variables that are predictors of the response variable.
See Appendix S5, for the complete list of the selected predictor variables after the variable selection process (Table E1) and the detailed model estimation results (Table E2).
<!-- para 28 -->
To build the predictive model, we used an 80:20 split of the sample into train and test sets.
The train set is used to estimate the model parameters and the test set is used to test the model accuracy.
To account for over-fitting and consistency issues, we used a 10 fold cross-validation on the train set (Hastie et al. 2009).
We used a Receiver Operating Characteristics (ROC) curve to test the accuracy of prediction.
The ROC curve is a plot between the false positive rate and the true positive rate on the test dataset.
An effective predictive model would maximize the true positive rate while keeping the false positive rate as low as possible.
Hence, the higher is the area under the curve (AUC) of the ROC curve, the higher is the predictive accuracy of the model.
<!-- para 29 -->
We used several machine learning methods for building predictive models and chose the one that performed the best on the hold-out train set.
The accuracy was measured by building a 95% confidence interval around the AUC of ROC curve, using a bootstrapped estimation with 1000 bootstrap runs of each method.
The random forest ensemble class model performed the best.
Consequently, we used random forest for building the predictive model based on the selected variables from the variable selection step.
A random forest model is an ensemble of decision trees constructed by recursive random partitioning of the data while optimizing the prediction ability of the model.
Random forests generate ensembles of regression trees built on independent random subsamples of the training data (Breiman 2001).
The classification ensemble is generated by the modal prediction class.
It has been shown that the classification accuracy of random forests depend on the number of classification trees, that is, the size of the ensemble.
The random forest model inherently takes into account the important nonlinear interaction effects that exist within the selected variables, and, hence, is suitable for building a product recall risk model illustrated by the conceptual framework, Figure 3.
The random forest model is stated in Equation (6).
<!-- para 30 -->
$$ P(Recall)\sim F\left(\begin{array}{c}Maude.Kernel,Control Variables.\\ Design Covariates,\\ Supply Chain Covariates,\\ Manufacturing Covariates\end{array}\right). \tag{6} $$
Figure 4 is the ROC curve corresponding to the random forest model (Equation 6) estimated in this study.
Figure 4 shows the median ROC curve on the test-set and the 95% confidence band generated through 1000 times bootstrapping of the prediction process.
The median AUC is 0.88 with a 95% bootstrapped (1000 times) confidence band of (0.82–0.90).
See Appendix S6 for a comparison of the prediction accuracies of the predictive analytic methods we estimated in this study (Table F1).
Appendix S8 presents a brief introduction to the predictive analytic methods used in this study
<!-- para 32 -->
Judgment bias is measured as a continuous measure following Equation (4) on repeated hold-out samples.
The random forest model was used to generate recall likelihood for individual medical devices in the study sample and generate the false alarm rate (FAR) and miss rate (MR) for each medical device at the maximum prediction accuracy point in the receiver operating characteristics curve.
The maximum accuracy indicates the actual decision threshold for each medical device that has been achieved by firms in the study sample pertaining to each medical device.
Also, judgment bias as defined in Equation (4) is a relative measure of decision bias of a firm for a product with respect to other firms competing in the same product market.
Since the measure is relative, the prediction parameters have limited effect on the bias measure as long as the prediction parameters
<!-- para 35 -->
are kept invariant within a product (identified by three letter code issued by FDA for each product).
Further, modeling bias in prediction is partialed out due to mean differencing (product fixed effect in Equation (4)) while measuring judgment bias for a firm within a product code in relation to other firms within the same product code.
This is because modeling bias consistently affects the predictions for all firms within the same product code.
The prediction model has been estimated with device level fixed effects.
The device level fixed effects measure the mean propensity of all firms to commit one type of judgment bias within that medical device group identified by the FDA assigned a three lettered device code.
The fixed effect for each device code (which contains multiple technologically similar medical devices intended for similar usages) represents the base level technology factor, $\lambda$, as in Equation (4).
The difference between the individual medical devices specific to individual firms from the base level judgment bias pertaining to the specific device code would provide us with a consistent measure of the judgment bias of each observation unit, that is, individual medical devices nested within individual firms in the study sample.
We created two different measures of judgment bias for the purpose of statistical analysis, e.g., (i) Bias, which is a continuous measure of the bias and (ii) Bias_OR, which is a categorical measure of bias codes as one for over-reaction and zero for under-reaction.
Figure 5 shows the distribution of the continuous judgment bias measure, Bias.
Figure 5 shows that, in general, firms have a much higher likelihood of under-reaction bias as compared to over-reaction bias, both in terms of the frequency (measured by kernel density of the bias) with which firms exhibit under-reaction bias as against over-reaction bias
<!-- para 38 -->
and in terms of the extent of under-reaction bias (measured in absolute numerical scale of the bias measure).
<!-- para 40 -->
The following independent variables were generated for the purpose of empirical analysis.
<!-- para 41 -->
Noise-to-signal ratio is measured as the ratio of standard deviation of the noise-plus-signal distribution to the mean of the noise-plus-signal distribution.
<!-- para 42 -->
Severity is measured as the weighted average of the severity of adverse events (mean frequency of adverse events times mean severity of adverse events) pertaining to each product firm combination in the sample.
<!-- para 43 -->
Firm Size is measured as the logarithm of the mean firm revenue for each firm during the study time-period.
This measure of firm size accounts for the changes in firm structure due to spin-offs, and mergers and acquisitions over the years.
<!-- para 44 -->
Product Portfolio Index is the entropy index of the product portfolio.
This index measures the depth and breadth of product portfolio of a firm.
For a firm with a product portfolio breadth (number of product lines) $P$ with each product line having a depth of $F_i: i \in \{1, \cdots, P\}$, the product portfolio index is measured by the Shannon's entropy index, $\sum_{i=1}^P \frac{F_i}{P} \log_e \frac{F_i}{P}$.
<!-- para 46 -->
We control for several relevant factors related to product characteristics that have the potential to influence recall decisions and firm factors that mostly influence temporal, within firm recall decisions.
Below we present the control variables.
<!-- para 48 -->
Regulation Type PMA is a categorical variable coded as one for pre-market approval (PMA) corresponding to approval routed for new medical devices and zero corresponding to approval route for new versions of existing medical devices.
<!-- para 49 -->
Product Age is natural logarithm of the number of years a medical device is in the market.
<!-- para 50 -->
Product Class is a categorical variable corresponding to FDA classification of medical devices based on the functional complexity and risk based criticality, that is, the risk that a device poses to the patient and/or the user, with three possible values: 1 corresponding to the low-complex and critical devices; 2 corresponding to medium-complex and critical devices; and 3 corresponding to high-complex and critical devices.
<!-- para 51 -->
Implant is a categorical control coded as one for implantable medical devices and zero otherwise.
<!-- para 52 -->
Usage is a categorical variable indicating the usage of a medical device as specified by FDA approval document corresponding to each medical device.
There are 19 usage classes and a miscellaneous usage class for usage non-specified medical devices.
<!-- para 54 -->
CAGR Fixed Asset is a measure of the compound annual growth rate (CAGR) of the gross fixed assets of a firm excluding assets acquired through mergers or acquisitions but including assets diluted.
This measures primarily increase or decrease of manufacturing assets.
We use the CAGR of fixed assets as a proxy measure of the internal growth of a firm in manufacturing activities, thus measuring organic growth rate of a firm.
<!-- para 55 -->
Mergers Acquisitions Investments measure the gross investment of a firm in mergers and acquisition activities over the study time period.
We use the natural logarithm of the gross investment in mergers and acquisitions for the purpose of the analysis.
<!-- para 56 -->
CAGR Margin is the mean year-on-year change operating margin of a firm over the study period.
<!-- para 57 -->
Foreign is a categorical variable coded as one for domestic firms and zero for foreign firms.
<!-- para 58 -->
Inventory Turnover is a continuous measure of the mean inventory turnover of a firm measured in number of days of inventory.
<!-- para 59 -->
RnD to Sales is the ratio of research and development expenses to sales.
<!-- para 60 -->
3.6.3 Market-related Control Variables.
Competition is a numeric count of the average number of competing product models within each product code.
This variable measures the product market competition.
<!-- para 62 -->
We estimated sources of judgment bias in two steps following a hierarchical linear modeling framework.
Since the sources of judgment bias are: (i) the characteristics of the signal in the user feedback on adverse events related to products that is measured at the product level, and (ii) situated context of the decision makers of a firm making the recall decision that is measured at the firm level, hierarchical linear model specification is appropriate for estimating judgment bias.
The response is measured at the first level, that is, the level of the product.
We estimate a first level model for $Bias_{ij}$ corresponding to product j for firm i specified in Equation (7).
<!-- para 63 -->
$$ \begin{aligned}Bias_{ij}=&\beta_{0}+\beta_{i1}(Noise-to-Signal Ratio)+\beta_{i2}(Severity)\\&+\beta_{i12}(Noise-to-Signal Ratio\times Severity)\\&+\beta_{i3}(Product Age)\\&+\beta_{i5}(Product Class II)+\beta_{i6}(Product Class III)\\&+\beta_{i7}(Regulation Type PMA)\\&+\sum_{i=8}^{27}\gamma_{ij}(Usage Class_{i})+\sum_{i}\delta_{i}(Firm_{i})+\epsilon_{ij}\end{aligned} \tag{7} $$
We estimate Equation (7) using the following steps.
In the first step, we test for the main effects of noise-to-signal ratio and severity of adverse events corresponding to H1 and H2.
In the second step, we incorporate the relevant control variables.
Subsequently, we test for interaction of noise-to-signal ratio and severity of adverse events.
<!-- para 64 -->
To test for the firm-related sources of judgment bias corresponding to H3 and H4, we extend the model specification in Equation (7) to a hierarchical linear modeling (HLM) specification to account for the hierarchical multi-level effects that we are interested in estimating.
The HLM model specification is shown in Equation (8).
<!-- para 65 -->
$$ \begin{aligned}\delta_{i}&=\gamma_{0}+\gamma_{1}(Firm Size_{i})+\gamma_{2}(Product Portfolio Index_{i})\\&\quad+\gamma_{3}(CAGR Fixed Assets_{i})\\&\quad+\gamma_{4}(Mergers Acquisitions_{i})+\gamma_{5}(Foreign_{i})\\&\quad+\gamma_{6}(CAGR Margin_{i})\\&\quad+\gamma_{7}(Inventory Turnover_{i})+\gamma_{8}(Competition_{j})\\&\quad+\eta_{j}\end{aligned} \tag{8} $$
At the firm level, first, we test for the main effect of noise-to-signal ratio.
Next, we test for the main effects of firm size and product portfolio depth and breadth corresponding to H3 and H4, respectively.
Finally, we incorporate all the relevant control variables.
<!-- para 66 -->
To check the robustness of model estimation results, we estimated a generalized linear model with logit link function for the categorical measure of bias, Bias_OR as shown in Equation (9).
In Equation (9), we cluster the standard errors at the firm level following the hierarchical structure of the data.
<!-- para 67 -->
$$
\begin{aligned}log\!\left(\frac{P(\text{BiasOR}_{ij}=1)}{1-P(\text{BiasOR}_{ij}=1)}\right)\\=\beta_{i0}+\beta_{1}(Noise-t-Signal\ Ratio)+\beta_{2}(Severity_{ij})\\+\beta_{3}(Product\ Age_{ij})\\+\beta_{4}(Product\ Class\ II_{ij})+\beta_{5}(Product\ Class\ III_{ij})\\+\beta(\text{Regulation Type}\ PMA_{ij})\\+\sum_{i=7}^{26} \beta_{i}(Usage\ Class_{ij})\\+\beta_{12}(Noise-to-Signal\ Ratio_{ij})\times Severity_{ij}\\+\beta_{27}(Firm\ Size_{i})+\beta_{28}(Product\ Portfolio\ Index_{i})\\+\beta_{29}(CAGR\ Fixed\ Assets_{i})\\+\beta_{30}(Mergers\ Acquisitions_{i})+\beta_{31}(Foreign_{i})\\+\beta_{32}(CAGR\ Margin_{i})\\+\beta_{32}(Inventory\ Turnover_{i})+\beta_{33}(Competition_{j})\\+\eta_{i}+\epsilon_{ij}\end{aligned} \tag{9} $$

## results
<!-- para 2 -->
First, we present Table 1, the correlation matrix for the main variables of interest.
As we can observe from Table 1, the response variable Bias is positively correlated (indicating over-reaction) with severity, and negatively correlated (indicating under-reaction) with noise-to-signal ratio.
Also, Bias is negatively correlated (indicating under-reaction) with firm size and product portfolio depth and breadth.
<!-- para 4 -->
<table border="1"><tr><td colspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td></tr><tr><td>(1)</td><td>Bias</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(2)</td><td>Severity</td><td>0.1205</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3)</td><td>Noise-to-Signal Ratio</td><td>-0.1376</td><td>-0.1123</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4)</td><td>Product Age</td><td>-0.0214</td><td>-0.1302</td><td>0.4240</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5)</td><td>Firm Size</td><td>-0.1010</td><td>-0.0220</td><td>0.0805</td><td>-0.0216</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6)</td><td>Product Portfolio Index</td><td>-0.1009</td><td>0.0098</td><td>0.0834</td><td>0.0283</td><td>0.3859</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7)</td><td>CAGR Fixed Asset</td><td>-0.1007</td><td>-0.0129</td><td>0.0714</td><td>-0.0562</td><td>0.4778</td><td>0.4270</td><td>1.0000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8)</td><td>CAGR Margin</td><td>0.0653</td><td>-0.0376</td><td>-0.0057</td><td>-0.0240</td><td>-0.0197</td><td>-0.0197</td><td>0.0305</td><td>1.0000</td><td></td><td></td><td></td><td></td></tr><tr><td>(9)</td><td>Inventory Turnover</td><td>0.0575</td><td>0.0497</td><td>0.0236</td><td>0.0502</td><td>0.3141</td><td>0.1115</td><td>0.0871</td><td>-0.1157</td><td>1.0000</td><td></td><td></td><td></td></tr><tr><td>(10)</td><td>Mergers Acquisition Inv</td><td>-0.0860</td><td>-0.0178</td><td>0.0557</td><td>-0.0988</td><td>0.0562</td><td>0.0556</td><td>0.0651</td><td>0.0834</td><td>0.1536</td><td>1.0000</td><td></td><td></td></tr><tr><td>(11)</td><td>RnD to Sales</td><td>-0.0354</td><td>0.0621</td><td>0.0310</td><td>-0.1652</td><td>0.2075</td><td>0.1617</td><td>0.3306</td><td>0.0371</td><td>-0.1189</td><td>0.3126</td><td>1.0000</td><td></td></tr><tr><td>(12)</td><td>Competition</td><td>-0.3418</td><td>-0.0646</td><td>0.0172</td><td>-0.0539</td><td>0.0318</td><td>-0.0474</td><td>0.0086</td><td>-0.0305</td><td>-0.0198</td><td>0.0124</td><td>-0.0595</td><td>1.0000</td></tr></table>
<!-- para 7 -->
<table><tr><th rowspan="2"></th><th colspan="5">Columns</th></tr><tr><th>(1)</th><th>(2)</th><th>(3)</th><th>(4)</th><th>(5)</th></tr><tr><td>(Intercept)</td><td>0.4931***<br>(0.0306)</td><td>0.8105***<br>(0.1789)</td><td>0.8077***<br>(0.1794)</td><td>0.8055***<br>(0.1775)</td><td>1.0363***<br>(0.1833)</td></tr><tr><td colspan="6">Product level variables</td></tr><tr><td>Noise-to-Signal Ratio</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.3978</mn></mrow></math>***<br>(0.0855)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.6111</mn></mrow></math>***<br>(0.0958)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.6121</mn></mrow></math>***<br>(0.0961)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.5861</mn></mrow></math>***<br>(0.0964)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.5709</mn></mrow></math>***<br>(0.0941)</td></tr><tr><td>Severity</td><td>1.3005***<br>(0.3301)</td><td>1.3762***<br>(0.3298)</td><td>1.1157***<br>(0.3346)</td><td>0.7296*</td><td>0.4649*</td><td>(0.2332)</td></tr><tr><td>Product Age</td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.3227</mn></mrow></math>*</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.3197</mn></mrow></math>*</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.2882</mn></mrow></math>*</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.4311</mn></mrow></math>*</td><td>(0.1679)</td></tr><tr><td>Product Class2</td><td></td><td>0.0999+</td><td>0.1001*</td><td>0.0916+</td><td>0.1389**</td><td>(0.0456)</td></tr><tr><td>Product Class3</td><td></td><td>0.2115***<br>(0.0595)</td><td>0.2121***<br>(0.0595)</td><td>0.2141***<br>(0.0603)</td><td>0.2384***<br>(0.0571)</td><td>(0.0456)</td></tr><tr><td>Implant.1</td><td></td><td>0.0691*</td><td>0.0699*</td><td>0.0946*</td><td>0.0596+</td><td>(0.0357)</td></tr><tr><td>Regulation Type PMA</td><td></td><td>0.0793**<br>(0.0298)</td><td>0.0676*</td><td>0.0497+</td><td>0.0239</td><td>(0.0392)</td></tr><tr><td>Usage Class</td><td></td><td>S</td><td>S</td><td>S</td><td>S</td><td>S</td></tr><tr><td>Noise-to-Signal X Severity</td><td></td><td></td><td>1.2454*</td><td>1.1253**</td><td>0.9439*</td><td>(0.4189)</td></tr><tr><td>Firm level variables</td><td></td><td></td><td>(0.5877)</td><td>(0.4277)</td><td></td><td></td></tr><tr><td>Firm Size</td><td></td><td></td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.2194</mn></mrow></math>***<br>(0.0561)</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.1265</mn></mrow></math>**<br>(0.0472)</td><td></td></tr><tr><td>Product Portfolio Index</td><td></td><td></td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.0895</mn></mrow></math>*</td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.0879</mn></mrow></math>*</td><td>(0.0445)</td></tr><tr><td>CAGR Fixed Assets</td><td></td><td></td><td></td><td>(0.0376)</td><td></td><td></td></tr><tr><td>CAGR Margin</td><td></td><td></td><td></td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.1741</mn></mrow></math>*</td><td>(0.1017)</td></tr><tr><td>Inventory Turnover</td><td></td><td></td><td></td><td></td><td>0.1473**<br>(0.0561)</td><td>(0.0561)</td></tr><tr><td>Mergers Acquisition Inv</td><td></td><td></td><td></td><td></td><td>0.0131</td><td>(0.1265)</td></tr><tr><td>RnD to Sales</td><td></td><td></td><td></td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.1335</mn></mrow></math>*</td><td>(0.0524)</td></tr><tr><td>Foreign</td><td></td><td></td><td></td><td></td><td><math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mo>&#x02212;</mo><mn>0.0538</mn></mrow></math></td><td>(0.0694)</td></tr><tr><td>Competition</td><td></td><td></td><td></td><td></td><td>0.0737*</td><td>(0.0337)</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td>0.4191***<br>(0.0349)</td><td></td></tr><tr><td>F-Statistic</td><td>20.29***</td><td>8.0115***</td><td>8.9345***</td><td>7.8723***</td><td>7.3945***</td><td></td></tr><tr><td>AIC</td><td>1,717.7</td><td>1,615.4</td><td>1,601.3</td><td>1,555.4</td><td>1,501.1</td><td></td></tr><tr><td>n</td><td>1,348</td><td>1,348</td><td>1,348</td><td>1,348</td><td>1,348</td><td></td></tr></table>
<!-- para 8 -->
*Notes.
All explanatory variables were scaled for consistent estimate since several variables are at different scales.
Significance codes: 0 ≤ *** ≤ 0.001 < ** ≤ 0.01 < * ≤ 0.05 < + ≤ 0.1 < ≤ 1 patients of the usage of medical devices across usage classes that appear to be driving the associations just discussed.*
<!-- para 9 -->
We find that high severity is significantly associated with over-reaction bias.
High severity of adverse events is likely to cause managers to become risk averse leading to an over-reaction bias.
This result supports hypothesis 2 (H2).
High severity of adverse events is associated with specific usage classes, technological complexity of devices indicated by device class, and newer devices indicated by PMA approval class and product age.
We find from the estimation results in columns (2)–(5) in Table 1 that specific device usage classes such as cardiovascular, surgical, orthopedics and general hospital (which includes critical devices used in hospital for patient monitoring, delivery of drug therapy, and a diverse set of patient interventions) are significant in explaining the over-reaction bias.
Figure 6 shows the marginal effects of specific device usage classes that have a statistically significant effect on over-reaction and under-reaction biases.
We observe that cardiovascular, surgical, and hospital device usage classes are all associated with over-reaction bias.
On the other hand, usage classes such as dental, ear-nose-throat, and physical medicine are associated with significantly high under-reaction bias.
It is the criticality to
<!-- para 10 -->
Similarly, product age is significantly correlated with high noise-to-signal ratio (correlation: 0.4240).
Specifically, product age significantly associated with under-reaction bias –that is, the older products are more likely to be associated with under-reaction bias and newer products are more likely to be associated with over-reaction bias.
Older products are associated with high geographical and functional usages leading to high noise-to-signal ratio.
<!-- para 11 -->
While the main effect of noise-to-signal ratio is significant, we find from the estimation results in columns (3)–(5) of Table 2 that the interaction of Severity and Noise-to-Signal Ratio is significant in explaining judgment bias.
The sign of the main effect of Noise-to-Signal Ratio has a negative sign indicating that as a main effect, high Noise-to-Signal Ratio leads to higher likelihood of under-reaction to adverse event reporting by users (H1).
However, when Noise-to-Signal Ratio interacts with Severity of the adverse events, the over-reaction likelihood increases due to the positive sign of the interaction term.
High severity of adverse event reports from users leads
<!-- para 14 -->
*Note.
With significant marginal effects only.*
<!-- para 15 -->
to higher likelihood for firms to become risk averse, and, in turn, there is likely to be more false alarms than misses (H2).
From the density of estimation of bias measure in Figure 5, we observe that, all in all, there is a higher likelihood of firms to under-react than to over-react to the market feedback by way of user-generated adverse event reports related to products signals.
The nature of interaction of noise-to-signal ratio and severity of adverse events is depicted in the contour plots of the interaction in Figure 7.
In Figure 7, we observe that as noise-to-signal ratio increases (along vertical axis of the contour plot) the underreaction likelihood increases.
However, at high levels of severity of adverse events, the over-reaction likelihood increases with increased noise-to-signal ratio.
This is an important finding of this study.
The intuition behind this interaction effect is that high noise-to-signal ratio in market feedback (by way of user-generated adverse event reports on products) impair managerial judgment.
At low levels of severity of adverse events, managerial judgment generally favors postponement of recall decisions.
However, at high levels of severity of adverse events, managerial judgment generally favors pre-emptive caution in making preventive recall decisions.
We summarize the above insights pictorially in Figure 8, a $2 \times 2$ matrix.
<!-- para 16 -->
Firm size, measured by mean firm revenue, is significant in explaining judgment bias exhibited by the firm.
The slope coefficient of Firm Size is negative and significant in estimations results in columns (4)–(5) of Table 1.
This supports hypothesis 3 (H3).
Larger firms have a significantly higher likelihood of under-reacting to user-generated reports on adverse events related to their products than smaller firms.
<!-- para 17 -->
We find that a firm whose product portfolio depth and breadth is high is more likely to under-react to user-generated reports on adverse events related to its products compared to a more focused firm whose product portfolio depth and breadth is low.
The coefficient estimate for Product Portfolio Index is significant and negative in estimation results in columns (4)–(5) of Table 1.
This implies that a generalist firm with high product portfolio index is more likely to under-react to adverse events in making recall decisions as compared to specialist firms with a low product portfolio index.
Thus, there is support for hypothesis 4 (H4).
<!-- para 19 -->
We estimated the Variance Inflation Factors (VIFs) of variables corresponding to Equations (7) and (8).
The VIFs for all variables are below 5 indicating that collinearity of variables in the model is not a major concern.
The VIFs are presented in Table G1 in Appendix S7.
The interaction between Severity and Noise-to-Signal Ratio was collinear with the constituent variables, Severity and Noise-to-Signal Ratio.
To reduce the effect of collinearity, we have centered and scaled both Severity and Noise-to-Signal Ratio.
Also, we have scaled all other variables for model estimation since many of the variables such as Firm Size
<!-- para 21 -->
Response (Bias)
<!-- para 23 -->
and Merger Acquisition Investment were measured at a very different scale compared to others.
Scaling of variables is desirable for consistency and convergence of the model estimation process.
<!-- para 24 -->
Also, as stated earlier with reference to Equation (9), we conducted robustness checks of the results using a categorical measure of bias.
Positive measures of the variable Bias are labeled as 1 and negative values are labeled as 0.
We estimated a logit model corresponding to Equation (9).
The results of the robustness check using the logit model (presented in Table G2 in Appendix S7) support the main model estimation results presented in Table 2.
Overall, we find support for the constituent hypotheses of the framework presented in Figure 2.
<!-- para 26 -->
Several other insights can be gleaned from model estimation results presented in Table 2 and Table G2 (see Appendix S7) corresponding to the control variables.
Firms undertaking high growth-related activities are more likely to under-react to market feedback by way of user-generated reports on adverse events related to products.
Given limited managerial cognitive capacities, the relative saliency and immediacy of impact on the firm for growth-related investments causes firms to assign higher levels of situated contextual attention to such activities.
The coefficients of CAGR Fixed Assets and Mergers Acquisitions Investments are significant and negative in the model estimation results presented in both Table 2 and Table G2 (see Appendix S7).
Mergers and acquisitions often lead to structural discontinuities in firms.
Our study results indicate that high focus on business growth, both organically through asset growth and inorganically through mergers and acquisitions, results in high under-reaction of firms to user-generated reports on adverse events related to products.
<!-- para 27 -->
The slope coefficient of Competition is positive and significant.
This indicates that higher level of market competition is associated with higher likelihood of over-reaction to user-generated reports on adverse events related to products.
Competition necessitates firms to constantly monitor the performance of products.
This increases the saliency of user-generated reports on adverse events related to products, and, hence, the attention that firms and managers allocate to such market feedback is also relatively high compared to firms that are in a low competition market.
<!-- para 28 -->
Beyond the results reported above, the Usage Class of medical devices is a statistically significant explanatory variable for differential likelihood of under-reaction bias and over-reaction bias.
The intended usage of a device is significant in determining how firms react
<!-- para 31 -->
to user-generated reports on adverse events related to devices.
Certain usage classes increase the likelihood of over-reaction while other usage classes increase the likelihood of under-reaction.
Specifically, device usage classes such as cardiovascular, orthopedic, surgical, and general hospital are positively associated with the likelihood of over-reaction and usage classes such as clinical chemistry, ear-nose and throat, and dental are positively associated with the likelihood of under-reaction.
The overall risk to patients associated with a device while in use is an important consideration for firms as well as regulators.
Hence, the reaction of firms toward market feedback on devices is different for different usage classes.
This partly explains why a majority of the medical device recalls made by firms are concentrated within a few classes, for example, cardiovascular, orthopedic, general hospital and surgical, among the 19 device usage classes.
We also observe that firms tend to over-react to user-generated reports on adverse events related to new products (FDA's PMA approvals) than when the user-generated reports on adverse events are related to new versions of existing products (FDA's 510K approvals).
The likelihood of firms to over-react is high in the case of implantable medical device compared to the non-implantable devices.
Product Class – a categorical measure of low, medium, and high product complexity and criticality – is a significant predictor of type and extent of judgment bias exhibited by firms.
Also, domestic firms are less likely to under-react to market feedback by way of user-generated reports on adverse events related to their products than foreign firms.
We did not find any significant effect of inventory turnover or profitability growth of firms on judgment bias.
<!-- para 33 -->
From the model estimation results in Table 2 pertaining to Equations (7) and (8), we are able to estimate the effect of the explanatory variables on the likelihood of over-reaction and under-reaction using the marginal response of explanatory variables of interest.
We find that a 10% increase in noise-to-signal ratio increases the likelihood of under-reaction bias by 7%.
On the other hand, 10% increase in severity of adverse events increases the likelihood of over-reaction bias by 17%.
The effect of increased severity on managerial judgment related to product recalls is more pronounced as compared to noise-to-signal ratio.
This is also evident from the contour plot of the interaction of severity and noise-to-signal ratio shown in Figure 7 and has been summarized in a Figure 8.
Similarly, a 10% increase in firm size is likely to be associated with 1.3% increase in under-reaction bias and a 10% increase in a firm's product portfolio index is likely to be associated with 1% increase in under-reaction bias.
In essence, the doubling of product portfolio index would increase the under-reaction likelihood by around 10%.
Given the recent explosion in new product and variant launches in many different technology sectors including medical devices, these are insightful and interesting results.

## discussion
<!-- para 2 -->
This study was motivated by the possible existence of judgment bias (under-reaction or over-reaction) in product recall decisions by firms in reacting to market feedback in the form of user-generated adverse event reports related to their products.
Drawing on and synthesizing the theoretical perspectives of signal detection, system neglect, and managerial attention and judgment, we developed an integrative theoretical framework for identifying the sources of judgment bias in product recall decisions.
The empirical setting of this study was the medical device industry.
We analyzed user-generated reports (big and unstructured data) on adverse events related to medical devices using a combination of econometric and predictive analytic (machine learning) methods to test the constituent relationships (hypotheses) of the integrative framework.
The primary contribution of this study is the integrative framework which identifies the sources of judgment bias (under-reaction and over-reaction) exhibited by firms in reacting to user-generated reports on adverse events related to their products.
<!-- para 3 -->
The key insights from the study results are as follows.
First, decision makers in firms exhibit judgment bias in reacting to market feedback by way of user-generated reports on adverse events related to their products and making product recall decisions.
Decision makers in firms either over-react or underreact.
The characteristics of the signal in user feedback of adverse events and the situated context of the decision makers are significantly associated with judgment bias.
Specifically, high noise-to-signal ratio in user feedback on adverse events is associated with under-reaction likelihood, and user feedback on adverse events characterized by high severity is associated with over-reaction likelihood.
The situated context of managers – that is, firm size and product-portfolio index – is positively associated with under-reaction likelihood.
<!-- para 4 -->
We believe that the results of this rigorous, theoretically grounded, big data analytic study will contribute toward the acknowledgement of the existence of judgment bias in firms as a major barrier to managing supply chain disruptions related to product recalls.
A significant implication of this study will be in informing firms and regulators (e.g., FDA and GAO) about the sources of judgment bias in decisions related to product recalls, such as medical device recalls that are known to be associated with injuries, hospitalizations and deaths.
The need for being proactive, consistent, and predictive in detecting medical device recalls is central to the call to action by the U.S. Government Accountability Office (GAO).
In a report to the US Senate, GAO has concluded that FDA should use data on device usage available to them for better analysis and proactive management of device recalls minimizing the public health risks associated with device recalls (GAO-11-468, June, 2011, p. 35).
In a subsequent study, GAO has indicated that user feedback on adverse events related to medical devices – the big data that we mine in this study – can serve to provide early signals of potential medical device recalls (GAO-12-816, p. 28, 33, 45).
Towards that end, the findings of this study will inform firms and the governmental institutions (e.g., FDA and GAO) about the sources of judgment bias and improve the post-launch market surveillance of products (e.g., medical devices) by making it more evidence-based and predictive.
<!-- para 6 -->
The study was supported by grants from the Social Media and Business Analytics Collaborative (SOBACO) between the Carlson School of Management and the College of Science and Engineering, University of Minnesota, and the American Hospital Association (AHA).
The authors gratefully acknowledge the detailed and developmental comments of two anonymous reviewers, senior editor, and the departmental editor on earlier versions of the study.
In its formative stages, the study benefited from the research assistance of Ravindra Kasturi in data collection, cleansing, organizing, and analysis.
The authors owe a debt of gratitude to the following colleagues who contributed in significant ways in shaping this study and the paper by providing timely feedback and guidance: Snigdhansu Chatterjee, Karen Donohue, Daniel A.
Levinthal, Mili Mehrotra, and Enno Siemsen.
Earlier versions of the paper were presented at the Wharton Technology and Innovation Conference, University of Pennsylvania, and the seminars at the Indian School of Business, University of Illinois at Urbana-Champaign, and Western University (Canada), and Medtronic Big Data & Advanced Analytics Symposium.
The study has benefited from the feedback of the attendees at these forums.
All errors are the responsibility of the authors.
