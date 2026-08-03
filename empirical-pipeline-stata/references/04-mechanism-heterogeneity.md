# Step 7 · 机制 / 异质性 / 中介(Stata)

把主 ATT 展开成"故事":对谁最强(异质性)、通过什么渠道(机制)、在什么条件下(调节/中介)。AMJ/SMJ 这一节往往是理论贡献的落脚点,`margins`/`marginsplot` 是主力。

## 1. 异质性:factor-variable 交互 + Wald
交互项系数本身就是异质性检验,别只跑分组。
```stata
* 二值调节变量
reghdfe y c.x##i.high_risk $controls, absorb(firm_id year) vce(cluster firm_id)
margins, dydx(x) at(high_risk=(0 1))
marginsplot, recast(connected) yline(0) title("x 的边际效应,按风险组")
graph export "figures/het_risk.pdf", replace
* x#1.high_risk 系数 = ΔATT(高风险 − 低风险)

* 连续调节变量(AMJ/SMJ 调节假设 H2 标配)
reghdfe y c.x##c.tenure $controls, absorb(firm_id year) vce(cluster firm_id)
margins, dydx(x) at(tenure=(p5(1)p95))           // 沿支撑画边际效应
marginsplot, recast(line) recastci(rarea) yline(0) ///
    title("x 的边际效应沿 tenure") xtitle("tenure")
```

## 2. 分组估计 + 跨方程 Wald(`suest`)
要分跑子样本又想要形式化等价检验:
```stata
eststo m1: qui reghdfe y x $controls if high_risk==0, absorb(firm_id year) vce(cluster firm_id)
eststo m2: qui reghdfe y x $controls if high_risk==1, absorb(firm_id year) vce(cluster firm_id)
suest m1 m2
test [m1_mean]x = [m2_mean]x
```
> 注意:`suest` 不直接支持 `reghdfe` 吸收的 FE;用 `xtreg, fe` 重跑,或用系数差的手动 Wald 近似(√(se1²+se2²))。

## 3. 三重差分(DDD)
```stata
reghdfe y c.treated##c.post##c.high_exposure $controls, absorb(firm_id year) vce(cluster firm_id)
* treated#post#high_exposure = 差分 ATT(高暴露 − 低暴露)
margins, dydx(treated) at(post=1 high_exposure=(0 1))
```

## 4. Outcome ladder(机制"向下传导")
同一处理跑在一串"近端 → 远端"结果上;机制为真则效应沿链条递减传导。
```stata
eststo clear
foreach out in mech_proximate mech_intermediate y_distal {
    eststo `out': qui reghdfe `out' x $controls, absorb(firm_id year) vce(cluster firm_id)
}
esttab mech_proximate mech_intermediate y_distal using "tables/outcome_ladder.tex", ///
    replace booktabs se star(* 0.10 ** 0.05 *** 0.01) label keep(x)
coefplot (mech_proximate, label("近端")) (mech_intermediate, label("中介")) ///
         (y_distal, label("远端 y")), keep(x) vertical xline(0) title("Outcome ladder")
```

## 5. 中介:Baron–Kenny 手动 + bootstrap
```stata
* c: 总效应; a: T→M; b,c': T+M→Y
qui reghdfe y x $controls, absorb(firm_id year): scalar c = _b[x]
qui reghdfe M x $controls, absorb(firm_id year): scalar a = _b[x]
qui reghdfe y x M $controls, absorb(firm_id year): scalar cprime = _b[x]
scalar b = _b[M]
di "indirect a*b=" a*b "  (% of total = " 100*a*b/c ")"
* 间接效应 bootstrap CI
program define medbk, rclass
    qui reghdfe M x $controls, absorb(firm_id year): scalar a = _b[x]
    qui reghdfe y x M $controls, absorb(firm_id year): scalar b = _b[M]
    return scalar indirect = a*b
end
bootstrap r(indirect), reps(1000) seed(42) cluster(firm_id): medbk
```

## 6. 中介:`medsem` / `khb` / SEM
```stata
ssc install medsem, replace
medsem, indep(x) med(M) dep(y) mcreps(1000) zlc            // sem + bootstrap

ssc install khb, replace
khb logit y x || M, summary                                  // 非线性(logit/probit)中介

sem (y <- x $controls M) (M <- x $controls), vce(cluster firm_id)
estat teffects                                              // 直接/间接/总
```
> 严肃的因果中介(Imai 敏感性)Stata 无原生实现;要的话用 Stata–Python 桥或 R `mediation`。

## 7. 调节中介
按调节变量分组分别跑 `medsem`,或用 `sem ... , group(mod) ginvariant(none)` 多组约束,检验 a·d 是否跨组相等。

## 8. 连续处理:dose-response
```stata
xtile dose = x_intensity, nq(10)
reghdfe y i.dose $controls, absorb(firm_id year) vce(cluster firm_id)
margins i.dose
marginsplot, recast(connected) xtitle("处理强度十分位") ytitle("预测 y")
```

## 9. 高维 CATE:Stata–Python 桥到 econml
Stata 16+ 内嵌 Python。要因果森林等高维 CATE:
```stata
python:
from sfi import Data
from econml.dml import CausalForestDML
from sklearn.ensemble import GradientBoostingRegressor
y=Data.get("y"); t=Data.get("x"); X=Data.get("$catevars".split())
cf=CausalForestDML(model_y=GradientBoostingRegressor(),model_t=GradientBoostingRegressor(),
                   n_estimators=1000,min_samples_leaf=5,cv=5).fit(y,t,X=X)
Data.addVarFloat("tau_hat"); Data.store("tau_hat",None,cf.effect(X).tolist())
end
binscatter tau_hat tenure, nquantiles(20) xtitle("tenure") ytitle("估计 CATE")
```

## 10. 溢出 / SUTVA 违反(召回/竞争研究常遇)
```stata
* 同行业/同市场处理同伴的暴露比例
bysort industry year: egen share_treated = mean(x)
reghdfe y x share_treated $controls, absorb(firm_id year) vce(cluster industry)
* share_treated 系数 = 溢出
```

## Step 7 至少产出
1 张异质性表(3–5 个预设调节变量) + 1 张 marginsplot + 1 张 outcome ladder 表/图 + 1 个带 bootstrap CI 的中介估计(附"无混淆"假设讨论) + 视设计补 DDD 或 dose-response。
