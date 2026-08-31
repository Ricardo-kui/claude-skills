---
name: ai-disclosure
description: "为管理/商学期刊投稿生成符合目标期刊当前政策的 AI 使用声明及摆放指引；只产声明，不写正文。触发词：AI disclosure、AI 使用声明、生成式 AI 声明、期刊 AI 政策、投稿要声明 AI 吗"
whenToUse: "当用户投稿管理/商学期刊（AMJ/SMJ/ASQ/OrgSci 等）需要写 AI 使用披露声明、不确定声明放在哪或必须包含什么时使用。触发词：AI 使用声明、AI disclosure、生成式 AI 声明、投稿要声明 AI 吗、cover letter 里写 AI、致谢里披露 AI、如实说明用了 AI"
---

# AI Disclosure — 投稿用 AI 使用声明生成

## 目标
为管理学/商学论文投稿生成一份**符合目标期刊当前政策**的 AI 使用声明,并明确它该放在哪、必须包含什么。它解决一个越来越硬的合规要求:AOM/ASQ/INFORMS/Wiley 等已陆续强制投稿时披露 AI 使用,且各刊要求不一(放封面信还是致谢、要不要按研究阶段逐项披露、措辞要素)。

它**不**负责写或润色正文(交给 write-* / humanizer),只产声明本身 + 摆放指引。

## 硬边界(诚信优先)
- **锚定真实政策、绝不编造**:每条建议必须能指向目标期刊的官方政策页(源 URL + 访问日期)。**不**凭印象编造政策条文。
- **政策会漂移**:产出时一律加盖"提交前请到期刊官网复核当前版本"的提醒;本 skill 的政策库是**起点而非权威**。
- **库内没有就停下问**:若目标期刊不在 `references/venue-policies.md`,**不要猜**——要求用户从期刊 Author Guidelines / Ethics 页粘贴当前政策,再据此生成。
- **AI 不能列为作者;作者对全部内容负责**:这是跨刊通用底线,声明里要体现;但具体措辞以期刊政策为准。
- **如实披露**:用了就如实说用在哪、做什么;没用就明确写"No generative AI was used"。不要为"显得干净"而隐瞒,也不要为"显得透明"而夸大。

## 标准工作流

1. **收齐信息**(见 `references/disclosure-protocol.md` 的 intake):
   - 目标期刊/会议(决定套哪套政策)。
   - 用了哪些 AI 工具(Claude / GPT / Gemini / DeepL / Zotero AI / 编程助手等)。
   - 用在研究流程的**哪些阶段**(文献检索 / 数据清洗与编码 / 实证分析 / 起草 / 润色 / 翻译 / 制图 / 排版)。
   - 每个阶段具体做了什么(语言润色 vs. 生成段落 vs. 生成代码 vs. 分析建议)。
   - 作者是否复核了全部 AI 产出。
2. **查政策库**:在 `references/venue-policies.md` 找目标期刊。
   - 找到 → 读取其字段(政策摘要 / 必需措辞要素 / 首选摆放位置 / 禁止项 / 作者署名规则)。
   - 没找到 → **停下**,请用户粘贴当前官方政策,再继续;不要套用近似期刊的条款冒充。
3. **起草声明**:按 `references/disclosure-protocol.md` 的结构与模板,产出中英双语声明(投稿语言为主,另一语备用)。要素齐全:工具名 + 阶段/任务 + 作者复核与负责声明 + 期刊指定的额外要素。
4. **给摆放指引**:明确声明放哪(封面信 / 致谢 / Methods / 单独小节),按该刊首选位置。
5. **盖戳**:附源 URL + 访问日期 + "提交前复核"提醒。

## 各刊要点速览(详见 references/venue-policies.md)
- **AOM 系(AMJ/AMR/AMD/AMP 等)**:按**研究流程逐阶段**披露是否用 AI;放**封面信 + 致谢**两处;作者全责,AI 不得署名。
- **ASQ**:投稿时(ScholarOne)披露 AI 使用,便于读者理解研究如何产出。
- **Organization Science(INFORMS)**:遵循 INFORMS 的 AI 作者伦理政策。
- **SMJ(Wiley/SMS)**:遵循 Wiley 的生成式 AI 作者指南;具体以 SMJ 作者指南为准。

## 需要按需读取的参考文件
- 声明结构与中英文模板、intake 清单、政策锚定纪律:`references/disclosure-protocol.md`
- 各刊 AI 政策库(含源 URL 与访问日期):`references/venue-policies.md`
