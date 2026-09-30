---
type: canonical_module
canonical_id: "Hawkes过程"
status: EMERGING
function: "自激发点过程（Hawkes）聚类 Results 模块族：以激发/衰减参数语义与 EM 前导-跟随分配为证据核心，用虚构单元 安慰剂与机制一致性检验为模型机制自证；首文件收变体 A（虚构单元安慰剂·千次重复自证型，mukherjee2022 型）；后续变体方向——R3 参数语义四拍（excitation/decay 双参数读法）、R2 EM 分配输出 worked-example 逐列导读。"
generativity: ADAPTABLE
exclusivity: MEDIUM
created: 2026-09-29
source: "corpus_writeback.py create_new_file（gate ① 裁决新建模块）"
---

# Hawkes过程 — 自激发点过程（Hawkes）聚类 Results 模块族：以激发/衰减参数语义与 EM 前导-跟随分配为证据核心，用虚构单元 安慰剂与机制一致性检验为模型机制自证；首文件收变体 A（虚构单元安慰剂·千次重复自证型，mukherjee2022 型）；后续变体方向——R3 参数语义四拍（excitation/decay 双参数读法）、R2 EM 分配输出 worked-example 逐列导读。

## 功能描述
自激发点过程（Hawkes）聚类 Results 模块族：以激发/衰减参数语义与 EM 前导-跟随分配为证据核心，用虚构单元 安慰剂与机制一致性检验为模型机制自证；首文件收变体 A（虚构单元安慰剂·千次重复自证型，mukherjee2022 型）；后续变体方向——R3 参数语义四拍（excitation/decay 双参数读法）、R2 EM 分配输出 worked-example 逐列导读。


## 适用场景
- 主模型是自研或少见估计器（点过程、EM 分配、结构模型），效度对象是"模型机制本身"而非某个回归系数
- 现象的主要替代解释是"随机时序/机械伪影"——安慰剂把替代解释直接转写为可证伪预言
- 单元轮廓可镜像（子单元数、事件分布、日期随机化规则可复制），算力允许千次重复


## 验证状态
### 单源验证
- 变体 A：虚构单元安慰剂·千次重复自证型——镜像真实单元轮廓的虚构单元+随机化事件并入再估计，双向可证伪预言（显著→主结果可疑；不显著→随机时序不产生现象）+千次重复报极端计数，为模型机制而非单个系数自证，mukherjee_2022（M&SOM），EMERGING
- 待第二篇跨论文复现后升 ROBUST


## 句法模板
### 变体 A：虚构单元安慰剂·千次重复自证型（mukherjee2022 型）

> 论证角色：[F] 机制自证（构造镜像真实单元轮廓的虚构单元，随机化其事件后并入再估计——用"随机时序不产生现象"的双向可证伪预言为模型机制本身背书，而非为某个系数背书）

**验证状态**: EMERGING（单篇来源；仅作 `section_variant`）

**功能节拍**: 威胁定位（模型方法本身的有效性）→ 虚构单元构造（镜像真实单元的单元数/事件分布轮廓并逐项枚举）→ 双向可证伪预言 → 再估计（虚构单元行为约束到自身协变量）→ 零结果报告 → 千次重复报极端计数 → 模型选择信心收束

**模板**:

> "Our first [mechanism] robustness check examines the validity of our [model approach] using a placebo test. We did so by creating a fictitious [unit], denoted [f̃]. For [f̃], we mirrored [a median real unit] by generating [the same number of subunits], matching [the profile of the mirrored unit], and randomly selected [matched share] to have no [events]. We then randomly assigned the [events] to the remaining [subunits] by drawing random samples from the per-[subunit] [event] distribution for [the mirrored unit]. Finally, we assigned random [event dates] for each [subunit] that had a positive number of [events]. We reestimated the [model] with [f̃] data added to the real data but constrained the [background behavior] of [f̃] to depend only on [its own covariates]. If the [events] attributed to [f̃] indeed act as [mechanism-consistent events], then we would observe a statistically significant [key parameter] for [f̃] in this placebo test, making our [model] results questionable. If not, this placebo test would indicate that [randomized events] do not lead to [the phenomenon] under the [model]. [Null result: parameters equal to (values), both not significant (p > [thresholds])]. As a caution, we repeated this placebo test [1,000] times where, in each repetition, we used new, randomly sampled [profile inputs] for [f̃]. There was not one instance in which the [model] led to a significant [key parameter] for [f̃]. This helps to build confidence in our choice of the [model] to examine [the phenomenon]."

**适用**:
- 主模型是自研或少见估计器（点过程、EM 分配、结构模型），效度对象是"模型机制本身"而非某个回归系数
- 现象的主要替代解释是"随机时序/机械伪影"——安慰剂把替代解释直接转写为可证伪预言
- 单元轮廓可镜像（子单元数、事件分布、日期随机化规则可复制），算力允许千次重复

**禁忌**:
- 安慰剂预言必须双向写清：显著→主结果可疑；不显著→随机不产生现象。只写"不显著=支持"退化为 ritual
- 虚构单元的镜像维度须在文中逐项枚举，不得只镜像有利维度
- 千次重复报"极端计数"（not one instance），不只是 p 值
- 安慰剂结果只支持模型选择，不得写成对实质假设的支持

**来源**: Mukherjee, Ball, Wowak, Natarajan, and Miller (2022), *Manufacturing & Service Operations Management*, §5.6

**原文锚定**:

> "If the recalls announced by firm f̃ indeed act as following recalls, then we would observe a statistically significant θ̂ for firm f̃ in this placebo test, making our Hawkes process model results questionable. ... As a caution, we repeated this placebo test 1,000 times ... There was not one instance in which the Hawkes process model led to a significant excitation parameter θ̂ for firm f̃."


## 组装规则
### 互斥

- 安慰剂预言必须双向写清：显著→主结果可疑；不显著→随机不产生现象。只写"不显著=支持"退化为 ritual
- 虚构单元的镜像维度须在文中逐项枚举，不得只镜像有利维度
- 千次重复报"极端计数"（not one instance），不只是 p 值
- 安慰剂结果只支持模型选择，不得写成对实质假设的支持

<!-- wb:mukherjee_2022_hiding_in_the_herd_the_product_recall_cluster:r7_hawkes_fictitious_unit_placebo -->
<!-- wb-meta: gap=Inadequacy status=EMERGING -->
