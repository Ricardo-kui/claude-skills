# 召回时机研究:生存 / 持续期模型(Stata)

当因变量是"**到召回(或事件)发生的时间**"时,OLS 会因右删失(样本期内未召回的公司)而有偏——用生存/持续期模型。你现有的共同所有权×召回项目 H2 已用 AFT Weibull,本文件把它在 Stata 里系统化。

## 数据结构 setup
每家公司一条记录(或公司-期),需要:
- 起始事件时间(如:产品上市、行业进入、首次曝光)。
- 结束 = 召回发生(失败)或样本期末(删失)。
- `stset` 声明持续时间与失败指标。

```stata
* duration = 从起始到召回(或到 2023 末)的时长;recalled = 1 若发生召回
stset duration, failure(recalled) id(firm_id) origin(time start_year) scale(year)

* 查摘要:有多少事件、多少删失、风险集
stdescribe
sts generate na = na           // Nelson-Aalen 累积风险
```

## 1. 非参数:K-M 曲线 + log-rank
```stata
sts graph, by(high_exposure) risktable              // 按组画生存曲线
sts test high_exposure                               // log-rank 检验组间差异
graph export "figures/km_by_exposure.pdf", replace
```
动机用:展示高/低暴露组的召回时机差异。

## 2. Cox 比例风险(`stcox`)—— 半参,允许时变协变量
```stata
stcox x $controls i.industry, cluster(firm_id)      // HR 解释:exp(b)
* 系数 b: b>0 → 危险(召回概率)上升;b<0 → 延后召回。
* 报告 hazard ratio:stcox 默认报 HR;eform 或 esttab 的 eform 选项。

* 比例风险假设检验(Schoenfeld 残差)
estat phtest, detail                                 // p<0.05 → PH 违反,该用分层或 AFT
```
> PH 违反时,Cox 系数不可直接读;换 AFT 或分层 `stcox ..., strata(industry)`。

## 3. AFT 加速失败时间(`streg`)—— 你 H2 的基准
AFT 模型:协变量**拉伸/压缩**时间;b>0 → 事件来得更晚(召回延后)。
```stata
* 选分布:Weibull(最常用)、log-logistic、log-normal、gamma
streg x $controls, distribution(weibull) cluster(firm_id) time     // time 选项 → 报 AFT 时间比(TR)
* TR = exp(b): TR>1 → 该协变量使召回时机延后 TR 倍;TR<1 → 加速召回。

* 与你已有基准对齐:firm + year FE 通过 absorb 不直接支持 streg;
* 实务做法:纳入行业/年份 dummies,或在 reghdfe 框架做 log-linear OLS 作并列稳健性(见下)。
```
**判读对照**(你 memory 里的口径):GGL 测度下每 +1 SD → 召回时机延后约 +15%;换 kappa 测度 → +21.9%;HH 不显著——结论对测度敏感,主测度待定。AFT 系数(TR)就是这个百分比的来源:TR = 1.15 ≈ 延后 15%。

## 4. 共同支撑下的并列稳健性(log-linear OLS + Cox 同向)
```stata
* log-linear OLS(你 memory 里提到的"OLS log-linear 与 Cox PH 同向支持")
reghdfe ln_duration x $controls, absorb(firm_id year) vce(cluster firm_id)
* Cox
stcox x $controls, cluster(firm_id)
* 三者(Weibull AFT / Cox / OLS log-linear)方向一致 = 时机结论稳健。
```

## 5. 时变协变量(召回研究中常需要)
若 x 随时间变(如逐年共同所有权变化),用 `stsplit` 拆人-期:
```stata
stsplit year, every(1)
* 然后在每个拆分区间填入当期 x
stcox x $controls, cluster(firm_id)
```

## 6. 不可观测异质性:frailty
公司间可能有不可观测的"召回倾向"异质性。
```stata
streg x $controls, distribution(weibull) frailty(gamma) shared(firm_id)
* frailty 方差显著 → 存在不可观测异质性,需随机效应/分层。
```

## 7. 风险率 / 累积发生率可视化
```stata
sts graph, cumfail                                      // 累积召回发生率
stcurve, survival at1(x=p25) at2(x=p75)                // 按 x 高低画生存曲线
graph export "figures/surv_by_x.pdf", replace
```

## 选模型速查
| 场景 | 用 |
|---|---|
| 只要非参对比组 | K-M + log-rank |
| 半参、要时变协变量、PH 成立 | `stcox` |
| PH 违反 / 想要"时间倍数"解释(延后/提前) | `streg, distribution(weibull) time`(AFT) |
| 有不可观测公司异质性 | frailty(gamma) shared |
| 召回事件很稀疏 | 考虑 `streg, distribution(gamma)` 或竞争风险 `stcrreg` |

## 与你已有项目的衔接
- 你 H2 基准(AFT Weibull, firm+year FE)已在跑——本文件提供 Stata 侧的完整工具箱与并列稳健性套路。
- 测度敏感(GGL vs kappa vs HH)是**测度选择问题**,不是估计器问题;回到 `xianzhu-skill` 的 `diagnostic-triage.md` + `robustness-levers.md` 判断主测度。
- 设计层面的因果(共同所有权是否外生)归 `causal-analysis`;本文件只负责把"时机"在 Stata 里正确估计出来。
