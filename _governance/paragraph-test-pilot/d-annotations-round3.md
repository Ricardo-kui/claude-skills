# D 评估标注存档 — Alpha-D / Beta-D（2026-09-07）

> 双盲标注生成段 G1–G3（文法 v1.1 + 生成文本，互不可见，零工具）。各 ≈30/36K tokens。
> 以下为判定矩阵与关键说理存档（逐句角色全保留；理由句摘要）。

## Alpha-D

### G1
- 逐句角色：S1[A&R：预判对立预期]；S2[Claim：渠道经由对手]；S3[Evidence：SEC 2022]；S4[Reason：move1]；S5[Evidence/Reason 复合：Berg 锚点+move2 推理]；S6[Reason：move3]；S7[Claim：段末收束]。moves=3。
- framing 豁免：否。
- 五问：#1 ✓（S2 段首+S7 段末双落点）；#2 ✓（3 moves 在预算内）；#3 ✓（理由1→SEC 2022、理由2→Berg 2022，S6 分析桥接免锚）；#4 ✓（S4/S6 半明言，reason→claim 可连）；#5 ✓（S1 预判+S2 "Yet" 回应，1 处合规）。
- 拼贴：#1–#5 全不命中（两处证据分挂两条理由链；First/Second 结构组织）。
- 备注：S5 复合句只能标一个角色；S1 兼铺垫色彩，按 A&R 处理。

### G2
- 逐句角色：S1[Claim：段首 topic]；S2[Evidence：Zavyalova 锚点]；S3[Reason：对冲主张]；S4[Reason：move1+Rhee & Valdez 锚]；S5[Reason：move2]；S6[Reason：move3 桥接回相对性]；S7[Claim：收束重述]；S8[Claim：Thus:]；S9[Claim：H2a]。moves=3。
- 五问：#1 ✓（S1 段首+S7/H2a 收束）；#2 ✓；#3 ✓（损伤前提→Zavyalova、对冲机制→Rhee & Valdez，S5 视为内嵌 warrant 与 S4 共用锚）；#4 ✓（because 从句+相对性原则）；#5 ✓（0 处合法）。
- 拼贴：全不命中。
- 备注：S5"利益相关者视评级可信"是经验性行为前提却无独立引文——视其与 S4 共用锚点并承担内嵌 warrant（模糊空间）；S2 属"复述文献结论"vs"归纳型 move"有歧义，按前者（证据）处理。

### G3
- 逐句角色：S1[Claim：段首条件性主张]；S2[Reason：move1+Kovács & Sharkey 锚]；S3[Reason：move2]；S4[A&R：预判"奖项不进公式"异议并回应]；S5[Claim：段末收束]。moves=3。
- 五问：#1 ✓；#2 ✓；#3 ✓（认证前提有锚，S3/S4 概念桥接免锚）；#4 ✓（S4 明言运作原则）；#5 ✓（S4 =1 处 A&R，与 G1 合计 2 处在预算内）。
- 拼贴：全不命中。
- 备注：S4 兼"定义前提/机制边界"与 A&R 双重功能，按 A&R 优先；其"多数方法论不以奖项为输入"是可检验经验前提，无锚点亦未标缺口——本标注视其为 A&R 内边界前提而非承重 reason（模糊处）。
- 一致自评：G3 S4 角色判定（双重功能）最不确定。

## Beta-D

### G1
- 逐句角色：S1[A&R]；S2[Claim]；S3[Evidence：SEC]；S4[Reason：move1 推理]；S5[Reason：move2 起点内嵌 Berg 锚]；S6[Reason：move2 完成]；S7[Claim：段末收束+完成回应]。moves=2。
- framing 豁免：否。
- 五问：#1 ✓（S2+S7 双重指认）；#2 ✓；#3 ✓（两承重前提各有锚，S4/S6 分析桥接）；#4 ✓（S4/S6 一般条件句明言，claim 属"会被抗拒"合法场合）；#5 ✓（1 处，S1 异议+S7 回应）。
- 拼贴：全不命中。
- 备注：S7 双重功能记主角色 Claim；S4/S6 内嵌 warrant 无独立槽位，记 Reason 并在 #4 指认。

### G2
- 逐句角色：S1[Claim]；S2[Reason：move1 承重前提+Zavyalova 锚]；S3[Reason]；S4[Reason：move2 核心+Rhee & Valdez 锚]；S5[Reason：move2 延伸，分析性]；S6[Reason：move3]；S7[Claim]；S8[Framing：衔接符]；S9[Claim：H2a]。moves=3。
- 五问：#1 ✓（S1+S7+S9）；#2 ✓；#3 ✓（move1→Zavyalova、move2→Rhee & Valdez，move3 跨段分析推导免锚——跨段论证合法）；#4 ✓（S6 内嵌原则连接 reason→claim）；#5 ✓（0 处合法；S3 "Yet" 是机制内转折非异议回应）。
- 拼贴：全不命中。
- 备注：move2/move3 切分点有弹性不影响总数；S8 单句衔接词角色文法未规定，记 Framing。

### G3
- 逐句角色：S1[Claim]；S2[Reason：move1+锚]；S3[Reason：move2]；S4[定义前提[D]：机制边界/运行原则，兼 A&R 功能]；S5[Claim：段末收束]。moves=2。
- 五问：#1 ✓（S1+S5）；#2 ✓（S4 为边界前提不计 move）；#3 ✓（认证前提有锚；S3 受众延伸为概念桥接）；#4 ✓（S4 即明言 warrant，属"原则可能被抗拒"合法场合）；#5 ✓（S4 按 A&R 计 1 处合规，纯边界界定则 0 处亦合法）。
- 拼贴：全不命中。
- 备注：S4 双重身份（D[D] vs A&R）文法未给操作性界分；S3"评级人员属该受众"可经验核查但未锚定，按概念桥接处理（经验/分析边界模糊——同 v1.2 候选②）。
- 一致自评：G3 #5 A&R 判定最不确定（S4 边界定义 vs 预判异议）。
