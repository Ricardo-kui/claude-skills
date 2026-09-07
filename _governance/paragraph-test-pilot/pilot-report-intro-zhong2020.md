# 试点报告 Intro — write-introduction 侧段落校准（Zhong et al. 2020 引言，2026-09-07）

> 动因：四电池（A/B/C/D）与 v1.2 修订的校准证据全部来自 theory 侧段落；文法本体是 write-intro/write-theory 共用单一事实源，但 intro 特有形态（Hook 的 framing 豁免路径、gap 段、贡献列举段）从未被测过。本轮补 intro 侧 A/B 校准。
> 样本：Zhong 2020 引言 6 段（A/B 测试允许用 Zhong——标注代理不接触语料；禁用的只是 D 生成）。I1=Hook（共识→GE 反常数据→研究问句）、I2=两派综述、I3=gap 段、I4=Theory Lens 机制链、I5=调节预告+引语授权、I6=贡献列举段。
> 方法：双盲标注（Alpha-I/Beta-I），任务书=文法 v1.2 + 段落级 framing 豁免判据，互不可见、零工具。成本 ≈80K tokens。

## 一致率

| 指标 | 结果 |
|------|------|
| framing 豁免判定 | 5/6 一致（I1–I5 双跑全同；**I6 分裂**，见下） |
| 五问实质一致率（I3/I4/I5 全跑段） | 15/15 |
| 拼贴判据（6 段×2 跑） | 12/12 段次全不命中、双跑一致 |
| 角色序列 | I1–I5 功能级一致（I2 逐句完全相同；I4 S1 一判 Framing 一判 Claim，无判定影响） |

## 关键发现

### 1. I6 贡献列举段豁免分裂 → 候选⑧（已修复+登记）

Alpha 判论证型（"novel/demonstrate" 是可争议主张，#1 ✓ 经 S2 总起句），Beta 判 framing 豁免（"预告性质——实质论证在正文完成"），两者各自融贯但相反。分裂直接动摇 **Gate 5 的 Contribution 必查模块**——豁免读法成立则贡献段逃过五问抽查。

**修复（v1.2 补丁，同日落地）**：文法推论条 framing 豁免增贡献列举段例外——各条贡献=claim 子型，整段默认论证型（总起句=topic sentence），不因预告形式豁免；render-rules 模块映射节同步注明"模块映射是生成期先验，Gate 5 按实际论证功能判豁免，文法判据优先"。已登记台账 batch_2026-09-07c（observations_processed 53）。

### 2. v1.2 新角色在天然栖息地验证通过

- **Gap 主张**：I3 S4（"As a result, we still know very little…"）双跑同标 Gap 主张、同判承担段 claim——v1.1 时代 P6 S4 的 Reason/Claim 漂移在 intro 侧无复发。
- **问句式 hook 不误触**：I1 S4 研究问句双跑均未追认为 Gap 主张（从紧执行"实质主张"判据），I1 整段双跑一致豁免。
- **②边界判据**：I3 S2 "often fail to consider" 双跑均按频次断言→经验承重→有锚（Eggers & Kaplan 2013）→ ✓，说理路径一致。

### 3. framing 豁免路径首次被真实行使

theory 侧 6 段全部是论证型（豁免=否），本轮 I1/I2 首次测到豁免路径：I1 Hook、I2 两派综述双跑均一致豁免，且豁免段的拼贴判据仍正常运转（全部不命中）。附带观察：I2 处于 Literature Turn 位置但无立场、功能为 framing——已由 render-rules 新增的"功能优先"半句覆盖（模块映射=生成期先验，Gate 5 按实际功能判）。

### 4. 工具性观察（不立项）

- **记分约定漂移**：#4/#5 的"合法缺位"Beta 记 ✗（合法缺位/0 处合法）、Alpha 记 ✓——实质判定相同（均认无明言 warrant/无 A&R 且合法）。后续任务书应像 #5 预设那样对 #4 显式规定"无明言 warrant 判 ✓ 注明合法缺位"。
- I4 S1（"In this study, we seek…"）一判 Framing 一判 Claim：开场白兼具定位与总主张功能，标签弹性不影响 #1（双跑均以 S6 收束句指认）。
- I6 的 S1 结果预告句锚点资格（Alpha 从宽计锚）依赖"段内资质句"读法——⑧修复后该段按论证型判，此点留给后续回归观察。

## 结论

intro 侧校准通过：5/6 段双跑完全一致；唯一分裂（I6）是真缺口，已修复（文法 v1.2 补丁 + render-rules 同步 + 台账⑧）。**文法 v1.2 现已在两侧段落形态上验证：theory 推导链/gap/假设段 + intro hook/综述/gap/机制链/贡献段。** intro 侧 C 探针与 D 生成对照为可选扩展——判别器机制已在 theory 侧验证，两侧共用同一判据集，暂无独立必要；若后续 Gate 5 在真实 intro 草稿上出现误判，再按本协议定向加测。
