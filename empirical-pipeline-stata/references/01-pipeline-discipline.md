# 流水线纪律:PAP、样本契约、写方程与识别假设

本文件覆盖 Step −1 / 0 / 2.5——这些是 AMJ/SMJ Methods 与审稿人**最在意但最容易被跳过**的"跑回归之前的纪律"。语法深度见 `stata` / `stata-data-cleaning`,这里只讲流水线里的位置与契约。

## Step −1 · 预注册 / 预分析计划(PAP)
在碰数据前,把"要检验什么、主变量是什么、关键稳健性有哪些"写下来(AEA RCT Registry 风格)。目的:防止事后挑规格(p-hacking),也给审稿人一个"这是设计驱动而非结果驱动"的信号。

最低要素:
- 主假设(H1, H1a, H1b…)与预期方向。
- 主解释变量 x、被解释变量 y 的精确定义与口径。
- 基准模型与固定效应/聚类结构。
- 预先列出的稳健性清单(对应 `03-robustness-battery.md` 的哪几项)。
- 预先列出的异质性维度(对应 `04-mechanism-heterogeneity.md`)。

**纪律**:PAP 不是给别人看的仪式,是给自己设的护栏——事后新增的规格要明确标为"探索性"。

## Step 0 · 样本构建日志 + 5 项数据契约
从原始数据到分析样本的每一步筛选都要留痕,能复现到行。建议生成 `docs/sample_construction.md`:

1. **来源与时间窗**:哪个库、哪几年、为什么这个窗口(剔除危机年/疫情年要有故事,见 xianzhu-skill 的 `robustness-levers.md`)。
2. **行级过滤**:每条 `keep if` / `drop if` 及其理由 + 剔除前后 N。
3. **合并键**:先 `isid` 验证双方键;按预期使用 `merge 1:1`、`m:1` 或 `1:m`,并以有效的 `assert(match master using)` 子集约束实际结果;禁止 `m:m`;记录各类匹配率。
4. **缺失处理**:`misstable` 报告;是列删(listwise)、插补还是保留,要写清。
5. **面板平衡性**:`xtset` 后用 `xtdescribe` 看覆盖;平衡面板 vs 非平衡要说明。

**5 项数据契约**(跑基准前自检):
```stata
* 1. 唯一面板键
isid firm_id year
* 2. 关键变量无全缺失
misstable sum y x controls
* 3. 时间连续性(或记录缺口)
xtset firm_id year
* 4. 诊断处理变量在样本期内的变异;不要自动删除无组内变异单元
tabstat x, by(firm_id) stat(min max sd)
* 5. 样本量与论文一致
count
```

## Step 2.5 · 写方程 + 识别假设(跑回归前必做)
AMJ/SMJ 的 Methods 开头就要这个;在 Stata 里跑 `reghdfe` 之前,先在文档里显式写出:

**1. 估计方程**,例如:
$$y_{it} = \beta \, x_{it} + \gamma' Z_{it} + \mu_i + \tau_t + \varepsilon_{it}$$
其中 $\mu_i$ 个体 FE、$\tau_t$ 年份 FE、$Z_{it}$ 控制向量。明确 $\beta$ 是你要的因果量(ATT / 弹性 / 半弹性)。

**2. 识别假设**,按设计写清:
- **DiD**:平行趋势(对照反事实 = 处理组未处理时的轨迹)+ SUTVA(无溢出) + 准确处理时点。
- **IV**:`Cov(z,ε)=0`(外生性)+ `Cov(z,x)≠0`(相关性,看第一阶段 F≥10)+ 排他性约束。
- **FE**:组内变异识别,$E[\varepsilon_{it}|x_{it},\mu_i]=0$(严格外生)。
- **匹配/PSM**:条件可忽略性 + 共同支撑 + 平衡性。

**3. 威胁预判**:列出 2–3 个最可能的识别威胁,并在 Step 6 稳健性箱里**事先**对应解决(例:自选择 → Heckman;平行趋势 → 事件研究 + honestdid;少聚类 → wild bootstrap)。

## 与其它栈的衔接
- 方程与识别策略的**设计取舍**(选 DiD 还是 IV)由 `huntington-klein-causal-design` 锁定;`causal-analysis` 只把它转成 Analysis Manifest;本步负责在 Stata 执行链中验证契约。
- 样本清洗的**深度语法**见 `stata-data-cleaning`;本步只讲契约与留痕。
