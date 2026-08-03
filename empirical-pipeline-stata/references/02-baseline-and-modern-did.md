# Step 5 · 基准建模与现代交错 DiD(Stata)

本文件是本 skill 的核心增量:把**现代交错 DiD 估计器搬进 Stata**(你现有的 `did-analysis` 是 R 版,本文件给 Stata 版)。语法已对齐 `reghdfe` 生态。

## 基准:面板 FE / IV / Heckman / 计数

```stata
* 面板 FE(主基准):reghdfe 吸收多维 FE + 聚类
reghdfe y x $controls, absorb(firm_id year) vce(cluster firm_id)

* 渐进主表(M1→M6)——AMJ/SMJ 也常用,但每列对应一个假设
eststo clear
eststo m1: qui reghdfe y x,                    absorb(firm_id year) vce(cluster firm_id)
eststo m2: qui reghdfe y x $ctrl_core,         absorb(firm_id year) vce(cluster firm_id)
eststo m3: qui reghdfe y x $ctrl_core $ctrl_gov, absorb(firm_id year) vce(cluster firm_id)
eststo m4: qui reghdfe y x $ctrl_core $ctrl_gov, absorb(firm_id year industry#year) vce(cluster firm_id)
esttab m1 m2 m3 m4 using "tables/table_main.tex", replace booktabs ///
    se star(* 0.10 ** 0.05 *** 0.01) label keep(x) ///
    stats(N r2, labels("N" "R2")) addnotes("Cluster SE by firm.")

* IV(弱工具诊断必做)
ivreghdfe y x (z = instrument) $controls, absorb(firm_id year) cluster(firm_id) first
* 报告:第一阶段 F(Kleibergen-Paap rk ≥ 10)、过度识别 Hansen J(若多工具)

* Heckman 自选择(战略样本常被要求)
heckman y x $controls, select(selection_eq = z $controls) twostep

* 计数/比例:ppmlhdfe(伪泊松,允许 FE 下解Incidental Parameters)
ppmlhdfe count_y x $controls, absorb(firm_id year) vce(cluster firm_id)
```

## 事件研究(动态 DiD / 平行趋势可视化)
AMJ/SMJ 的 DiD 论文几乎标配事件图。先构造相对处理时间,再画。

```stata
* 相对事件时间,base = -1(平移到非负,base 落在 +5 处的 4)
gen rel   = year - first_treat
replace rel = -5 if rel < -5 & !missing(rel)
replace rel =  5 if rel >  5 & !missing(rel)
gen rel_p = rel + 5
replace rel_p = . if missing(first_treat)          // never-treated 剔除

reghdfe y ib4.rel_p $controls, absorb(firm_id year) vce(cluster firm_id)
coefplot, keep(*.rel_p) omitted vertical yline(0) xline(4.5, lpattern(dash)) ///
    rename(0.rel_p="-5" 4.rel_p="-1" 5.rel_p="0" 10.rel_p="5+") ///
    xtitle("相对处理时间(年)") ytitle("系数 (ATT)")
graph export "figures/event_study.pdf", replace
```
**判读**:处理前系数(−5..−1)应≈0 且不显著 → 平行趋势支持;若前系数明显偏离,需在 Step 6 上 `honestdid`。

## 现代交错 DiD(关键增量)
**何时用**:处理时点交错(staggered adoption,如不同公司在不同年发生召回/政策)时,TWFE 有偏(Goodman-Bacon 2021 负权重)。必须换估计器。`causal-analysis` 定设计,这里给 Stata 实现。

```stata
* 准备:gvar = 首次处理年,0 = 从未处理
gen gvar = first_treat
replace gvar = 0 if missing(first_treat)

* 1) Callaway–Sant'Anna (2021) —— 最常用,doubly-robust IPW
csdid y $controls, ivar(firm_id) time(year) gvar(gvar) method(dripw)
estat event      // 事件研究聚合
estat group      // 按 cohort 的 ATT(g)
estat calendar   // 按日历年的 ATT(t)
estat simple     // 总体 ATT
csdid_plot, ytitle("ATT")
graph export "figures/csdid_event.pdf", replace

* 2) Sun & Abraham (2021) —— 交互加权事件研究
eventstudyinteract y ib4.rel_p, cohort(first_treat) control_cohort(never_treated) ///
    absorb(i.firm_id i.year) vce(cluster firm_id)

* 3) Borusyak–Jaravel–Spiess (2024) —— imputation 估计量
did_imputation y firm_id year first_treat, allhorizons pretrend(5) autosample
event_plot, default_look graph_opt(xtitle("处理后年数") ytitle("ATT"))
graph export "figures/did_imputation.pdf", replace

* 4) Synthetic DID (Arkhangelsky et al. 2021)
sdid y firm_id year treatment, vce(bootstrap) reps(500) seed(42) graph

* 5) de Chaisemartin & D'Haultfœuille (2023)
did_multiplegt_dyn y firm_id year treatment, effects(5) placebo(3) cluster(firm_id)
```

**选哪个**:有 never-treated 组 → CS 或 SA;想看完整事件研究动态 → SA 或 did_imputation;单元少、想用合成控制思路 → sdid;对异质处理效应稳健性存疑 → 跑 ≥2 个交叉验证一致性。

## TWFE 偏误诊断(跑现代估计器前的必查)
```stata
xtset firm_id year
bacondecomp y treatment, ddetail
* 报 4 类 2×2 比较的权重;"later vs earlier (treated)" 若权重大 → TWFE 有负权重偏误,必须换上面的现代估计器。
graph export "figures/bacon.pdf", replace
```

## HonestDiD(平行趋势敏感性)——事件研究后做
```stata
* 把事件研究的 b/V 传给 honestdid:平行趋势需要多大违反才会翻结论?
honestdid, pre(1/4) post(5/9) mvec(0(0.1)0.5) coefplot
graph export "figures/honestdid.pdf", replace
```

## 连续处理强度 DID
```stata
xtile dose = treat_intensity, nq(10)
reghdfe y i.dose $controls, absorb(firm_id year) vce(cluster firm_id)
margins i.dose
marginsplot, recast(connected) ytitle("预测 y") xtitle("处理强度十分位")
```
