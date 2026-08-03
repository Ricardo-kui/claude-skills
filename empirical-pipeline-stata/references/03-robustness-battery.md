# Step 6 · 稳健性检验箱(14 件套,Stata)

目标:主系数要在合理扰动下存活才算可信。AMJ/SMJ 主表干净,但**这一整套要跑、放附录/online supplement**。这是本 skill 的核心增量之一——你之前的栈没有把它系统化。

> 与 xianzhu-skill 的关系:xianzhu 的 `robustness-levers.md` 讲的是**纪律**(稳健性 vs 显著性挖掘);本文件讲的是**具体怎么跑**。两者配合用。

## 1. 渐进规格(M1→M6)
见 `02` 的主表块。每列加控制/FE,核心系数符号与量级稳定即可。

## 2. 聚类层级敏感性 + 双向聚类
```stata
foreach c in firm_id industry province state {
    qui reghdfe y x $controls, absorb(firm_id year) vce(cluster `c')
    di "cluster=`c'  b=" _b[x] "  se=" _se[x]
}
* 双向聚类
reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id year)
```

## 3. Wild cluster bootstrap(`boottest`)—— 少聚类时金标准
聚类数 < 50 时,普通聚类 SE 偏低估。
```stata
qui reghdfe y x $controls, absorb(firm_id year) vce(cluster province)
boottest x, cluster(province) reps(9999) seed(42) weighttype(webb)
boottest x, cluster(province) reps(9999) ci level(95)   // 带 CI
```

## 4. 子样本切分(描述性;正式异质性检验见 `04`)
```stata
foreach m in "industry==1" "industry==2" "size<p50" "size>=p50" {
    qui reghdfe y x $controls if `m', absorb(firm_id year) vce(cluster firm_id)
    di "`m': b=" _b[x] "  N=" e(N)
}
```

## 5. 替代 y / 替代 x 定义
```stata
foreach y in y ln_y asinh_y y_w1 { qui reghdfe `y' x $controls, absorb(firm_id year) vce(cluster firm_id) : di "`y': b=" _b[x] }
foreach t in x x_ever x_intensity x_alt { qui reghdfe y `t' $controls, absorb(firm_id year) vce(cluster firm_id) : di "`t': b=" _b[`t'] }
```

## 6. 替代样本限制(缩尾/截尾敏感性)
```stata
foreach lvl in 0 1 5 {
    preserve
    if `lvl'>0 winsor2 y, cuts(`lvl' `=100-`lvl'') replace
    qui reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id)
    di "winsor `lvl'/`=100-`lvl'': b=" _b[x]
    restore
}
```

## 7. 安慰剂:伪时点
```stata
gen fake_first = first_treat - 3
gen fake_post  = (year >= fake_first) if !missing(fake_first)
preserve
    keep if year < first_treat                      // 丢掉真实处理后期
    reghdfe y fake_post $controls, absorb(firm_id year) vce(cluster firm_id)
restore
* 伪处理系数应≈0。
```

## 8. 随机化推断(`ritest`)
置换处理、重估,给精确 p 值。少聚类 / 随机分派 / 想要非参安慰剂分布时尤其有用。
```stata
ritest x _b[x], reps(1000) seed(42) strata(industry): ///
    reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id)
* 带分布图
ritest x _b[x], reps(1000) seed(42) saving("logs/ritest.dta", replace): ///
    reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id)
```

## 9. 多重检验校正(`rwolf` / `wyoung`)
多结果变量同时检验时,族错误率膨胀,必须校正。
```stata
* Romano–Wolf step-down
rwolf y1 y2 y3, indepvar(x) controls($controls) reps(500) seed(42) ///
    method(reghdfe) fe(firm_id year) cluster(firm_id) bl(0.05)
```

## 10. Specification curve(规范曲线)
跑所有合理控制/FE/结果组合,画系数分布。
```stata
tempname M
postfile `M' str40 spec float(b se) using "logs/speccurve.dta", replace
foreach y of local outcomes {
    foreach c of local control_sets {
        foreach fe of local fe_sets {
            qui reghdfe `y' x `c', absorb(`fe') vce(cluster firm_id)
            if e(N)>0 post `M' ("`y'|`c'|`fe'") (_b[x]) (_se[x])
        }
    }
}
postclose `M'
* 画图:按 b 排序的系数 + CI 山脊图,标出基准规格位置
```

## 11. Oster (2019) δ\*(`psacalc`)—— 选择偏误界
不可观测要有多强(相对可观测)才能把效应归零。
```stata
ssc install psacalc, replace
qui reghdfe y x $controls_full, absorb(firm_id year) vce(cluster firm_id)
psacalc delta x, mcontrol($controls_full) rmax(1.3*e(r2))
* δ*>1 基本稳健;>2 强;|δ*|>4 很强(AER/JOE 常见门槛)
psacalc beta x, mcontrol($controls_full) rmax(1.3*e(r2)) delta(1)   // 偏误调整 β 界
```

## 12. TWFE 偏误诊断(`bacondecomp`)
见 `02`。交错处理下若负权重大,主表必须换现代估计器。

## 13. HonestDiD(平行趋势敏感性)
见 `02`。

## 14. 影响诊断:留一法 / 去高杠杆
```stata
* 去 top 1% Cook's D
qui reg y x $controls
predict cd, cooksd
sum cd, detail
preserve
    drop if cd > r(p99)
    reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id)
restore
* 留一(聚类)法:循环丢一个 firm 重估,画分布(见 00.2 源 06-robustness §14)
```

## 一份够强的稳健性附录至少包含
1. 渐进规格主表;2. 3–4 个聚类层级 + 少聚类时 `boottest`;3. 伪时点安慰剂(前期≈0);4. `ritest` 分布;5. specification curve;6. Oster δ\*;7. 4–6 维子样本;8. ≥2–3 个替代 y/x;9. DiD:`bacondecomp` + `honestdid`;10. IV:弱工具(KP rk Wald F)、过度识别(Hansen J)、必要时 Conley 空间 SE;11. RD:带宽敏感性(×0.5/1/2)、`rddensity`、协变量平滑安慰剂;12. PSM/IPW:`pstest`/`tebalance` 平衡、共同支撑、熵平衡版本。

**纪律**:这些是"换了之后方向量级还稳不稳"的检验,不是"挑最显著列"。任何一项让结论翻号,都要如实写进局限,而不是藏起来。
