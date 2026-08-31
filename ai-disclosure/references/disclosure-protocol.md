# AI 使用声明协议:intake、结构与模板

本文件支撑 ai-disclosure 的起草。改编自 ARS `disclosure_mode_protocol.md` + `policy_anchor_disclosure_protocol.md`,去掉双轨道 / Schema 机制,保留 intake 与"锚定真实政策"的诚信内核。

## 一、Intake(起草前必须问清)

把用户的实际使用情况摊清楚,声明才有意义。逐项确认:

1. **目标期刊**:决定套哪套政策(查 `venue-policies.md`)。
2. **用了哪些工具**:Claude、GPT、Gemini、DeepL、Grammarly、Zotero AI、Cursor/Copilot 等;尽量给工具名(版本若知道更好)。
3. **用在哪些阶段**(可多选):
   - 文献检索与综述
   - 数据清洗、变量构造、编码
   - 实证分析(代码生成/调试、结果解读建议)
   - 起草正文(哪几节)
   - 语言润色 / 去 AI 味
   - 翻译
   - 制图 / 制表 / 排版
4. **每个阶段具体做了什么**:区分"语言层面辅助(润色/纠错)"与"内容层面生成(起草段落/生成观点/生成分析)"——很多期刊对二者披露要求不同。
5. **作者是否复核了全部 AI 产出**(基本所有期刊都要求声明这点)。
6. **有没有完全没用 AI**:若有任何阶段没用,或全程没用,如实写"No generative AI was used in [stage / this work]"。

**判断梯度**(参考 ACL 等的 graduated 思路):
- 仅语言润色 / 短文本预测输入 → 多数期刊不强制披露,但 AOM 要求逐阶段披露,稳妥起见仍写明。
- 低新颖度文本生成 / AI 建议的新观点 → **必须**披露。
- AI 文献检索工具 → 一般无需特别披露,但仍要保证引用准确与全面(这是独立于 AI 声明的常规要求)。

## 二、声明的标准结构

一份合规声明通常包含四块(按期刊要求取舍):

1. **使用事实**:用了哪些工具、在哪些阶段、做了什么。
2. **作者责任声明**:作者已复核全部 AI 产出,并对内容准确性、完整性负全部责任。
3. **作者署名声明**:AI 工具不构成作者、不承担问责(几乎所有期刊通用)。
4. **(期刊指定)额外要素**:如 AOM 的逐阶段披露表、ASQ 的 ScholarOne 字段说明等。

## 三、模板(中英双语,按需调整)

### 模板 A:全程使用了 AI(语言润色 + 部分起草 + 代码辅助)

**EN**:
> During the preparation of this work the authors used [Claude (Anthropic) / GPT-4 / …] in order to [polish the language, draft portions of the [Introduction/Discussion], and assist with Stata/Python code for the empirical analysis]. Specifically, AI assistance was used at the following stages of the research: [literature search; data cleaning and variable construction; empirical analysis (code generation and debugging); drafting (Sections X); language editing]. The authors generated the core theoretical contributions, research design, and interpretation of findings independently. The authors reviewed and edited all AI-assisted content and take full responsibility for the accuracy and integrity of the manuscript. No AI tool is listed as an author.

**中文**:
> 在本研究写作过程中,作者使用了 [Claude(Anthropic)/ GPT-4 / …] 进行 [语言润色、起草 [引言/讨论] 部分段落,以及辅助实证分析的 Stata/Python 代码编写]。具体而言,AI 辅助用于以下研究阶段:[文献检索;数据清洗与变量构造;实证分析(代码生成与调试);起草(第 X 节);语言编辑]。核心理论贡献、研究设计与结果解读由作者独立完成。作者已复核并修改全部 AI 辅助内容,对稿件准确性负全部责任。本文未将任何 AI 工具列为作者。

### 模板 B:仅语言润色

**EN**:
> In preparing this manuscript, the authors used [Claude / DeepL / Grammarly] solely for language editing and proofreading. No AI tool was used to generate content, ideas, data, or analysis. The authors reviewed all edits and take full responsibility for the work. No AI tool is listed as an author.

### 模板 C:未使用 AI

**EN**:
> No generative AI tools were used in any stage of the research or in the preparation of this manuscript.

## 四、摆放位置(按期刊)

通用首选(具体以期刊政策为准):
- **封面信(Cover Letter)**:几乎所有要求披露的期刊都接受/要求在封面信说明。AOM 明确要求封面信 + 致谢**两处**都写。
- **致谢(Acknowledgements)**:最常见的正文内落点(Nature/Science/ACL/多数社科刊)。
- **Methods / 数据与方法**:部分期刊(如 Nature)建议放 Methods。
- **单独小节**("Use of AI Tools",置于 References 前):少数期刊历史上的做法,现多数已并入致谢。

在 `venue-policies.md` 里每刊都标注了首选位置;不确定时,封面信 + 致谢双写最稳。

## 五、诚信铁律:锚定真实政策

- **每条声明建议都要能追溯到目标期刊的官方政策页**:在产出末尾附 `Source: <官方 URL> (accessed YYYY-MM-DD)`。
- **不编造政策条文**:库内没有该刊就停下问用户要当前政策,不要拿近似刊的条款冒充。
- **提交前复核**:政策会变,产出一定加盖"提交前请到 [期刊] 官网 Author Guidelines / Ethics 页复核当前 AI 政策"。
- **如实**:用了就如实说用在哪、做什么;没用就明确写没用。隐瞒与夸大都违反诚信。
