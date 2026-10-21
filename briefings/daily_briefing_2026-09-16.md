# ContentOS Daily Briefing — 2026-09-16

- 生成时间: 2026-09-16T04:30:00Z
- 原始素材数: 305(RSS 池 217 条/48h + WebSearch 交叉核实约 88 条)
- Must Reads: 14 | Also Worth: 16 | Topics: 12 | Drafts: 3
- 通道状态: 书签通道连续第七日 0 供给(sync 停在 09-08);微信收藏连续第十四日无新笔记(最新 2026-09-01);RSS 池 88 个 feed 有新条目,20 个报错
- 今日主线: **可审计性成为准入证**(AEF-1 三方联签 + 英伟达等限制 Claude)× **团队 Agent 落地**(飞书 8.0 豆包工作伙伴)× **视频素材供应链重组窗口**(Vidu S2 实时化 vs Sora API 9/24 关停)

## 今日必看

### [Google 发布 Gemini 3.8 Live 与 3.8 Live Extended Thinking:实时语音进入「边想边说」时代](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/)
- **event_id**: gemini-3-8-live-launch | **track**: 🤖 AI 前沿 | **source**: Google The Keyword | **age**: 11h
- Google 官方博客 9/15 发布 Gemini 3.8 Live(实时语音对话)与 3.8 Live Extended Thinking(实时会话中加入扩展推理),并同步给出 Gemini 3.8 Live + 3.5 Transcribe 的实时语音应用开发指南。对电商客服 Agent、语音导购场景:实时语音第一次把「推理深度」和「低延迟」同时摆上台面。
- 补充角度:
  - [开发者指南:用 Gemini 3.8 Live 与 3.5 Transcribe 构建实时语音应用](https://blog.google/innovation-and-ai/technology/developers-tools/build-real-time-voice-applications-gemini-audio/)

### [AEF-1 标准浮出水面:xAI、OpenAI、Anthropic 三方联签「独立第三方评估最低运行条件」](https://www.latent.space/p/ainews-aef-1-standard-emerges-for)
- **event_id**: aef-1-evaluator-standard | **track**: 🤖 AI 前沿 | **source**: Latent Space | **age**: 23h
- Latent Space AINews 9/15 报道:AI Evaluator Forum 制定的 AEF-1 标准——独立性(利益冲突/资金来源/回避)、访问权限(足够的技术访问)、透明度(评估条件披露)三大支柱——获 xAI、OpenAI、Anthropic 共同签署。Anthropic 承诺给嵌入式评估员「接近内部风控团队」的权限。这是 Dario 09-14 限速方案的机制化落地:做 Agent/模型服务的团队要把「可外部审计」写进架构。
- 补充角度:
  - [标准原文:AEF-1 Minimum Operating Conditions(官方 PDF)](https://aievaluatorforum.org/AEF_1_Minimum_Operating_Conditions_for_Independent_Third_Party_AI_Evaluations.pdf)

### [英伟达、Palantir、Booz Allen 相继限制内部使用 Claude Fable:数据留存政策成为企业 AI 选型的第一筛](https://www.pymnts.com/news/artificial-intelligence/2026/nvidia-and-palantir-restrict-anthropics-fable-over-data-retention/)
- **event_id**: enterprises-restrict-anthropic-data-retention | **track**: 🤖 AI 前沿 | **source**: PYMNTS / The Information | **age**: 28h
- The Information 9/14 首发:英伟达将 Fable 限制在非敏感任务,专有工作转向自家 Nemotron;Palantir 要求不可撤销的零留存保证;Booz Allen 禁止用于专有网络安全工作。导火索是 Anthropic 6 月政策变化:客户日志可留存 30 天(触发安全系统最长 2 年)。Anthropic 的对策是 Enterprise Frontier Safeguards(EFS):企业把安全监控数据存进自己的云(发布时间近似)。
- 补充角度:
  - [InfoQ 中文:英伟达内部限制使用 Claude,黄仁勋告诉特朗普「我们不会让 AI 发展放缓发生」](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651293044&idx=1&sn=5fe897421c132a5e64a07a86586ab967)
  - [AI寒武纪:反噬来了,英伟达限制使用 Anthropic 模型](https://mp.weixin.qq.com/s?__biz=Mzg3MTkxMjYzOA==&mid=2247518970&idx=1&sn=de66dcbdf8399b0bc3df50e4db7331d7)

### [WSJ:OpenAI 超 3 亿美元收购手机相机公司 Glass Imaging,多模态入口向硬件延伸](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247518095&idx=2&sn=02fe520df8521123984a62a942894b97)
- **event_id**: openai-glass-imaging-acquisition | **track**: 🤖 AI 前沿 | **source**: Z Potentials / WSJ | **age**: 25h
- WSJ 9/14-15 报道:OpenAI 收购前苹果人像模式团队创立的 Glass Imaging(超 3 亿美元,为一年前估值 3 倍)。GlassAI 在拍摄瞬间用神经网络处理 RAW 数据,号称手机相机性能提升 10 倍,已在荣耀手机落地。叠加 65 亿美元收购 io Products,OpenAI 自有设备版图逐渐清晰:相机将成为多模态 AI 的关键视觉传感器。
- 补充角度:
  - [TechCrunch:OpenAI buys smartphone camera maker Glass Imaging for $300 million](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)

### [飞书 8.0 全面拥抱 Agent,「豆包工作伙伴」发布:中国第一个团队 Agent 进工作群](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652726237&idx=1&sn=9b4809ee6f1a37d998669e5446911b94)
- **event_id**: feishu-8-doubao-work-partner | **track**: 🤖 AI 前沿 | **source**: 新智元 | **age**: 19h
- 9/15 飞书未来无限大会:飞书 8.0 系统性为 Agent 重构(Agent 进群协作、CLI 调用、企业级 Token 配额);「豆包工作伙伴」作为国内首个团队智能体发布——独立身份、权限、记忆,可跨级申请授权。飞书上半年 ARR 增速达去年同期 2.5 倍,90%+ 新客户购买 AI 产品。团队 Agent 的权限设计给出了第一个可参照的国内样本。
- 补充角度:
  - [智东西:飞书 8.0 全面拥抱 Agent,字节持续猛攻企业 Agent](https://tech.ifeng.com/c/8wRMH4mNFWS)
  - [爱范儿:豆包工作和飞书,把中国第一个团队 Agent 拉进了工作群](https://www.ifanr.com/1680138)

### [阶跃星辰发布 StepAudio 3 系列五款语音模型:对话动态与语音推理双榜全球第一](https://mp.weixin.qq.com/s?__biz=MzkyNTYxNzg5Mg==&mid=2247488074&idx=1&sn=7d92ce0f0098ec0c53b243df4709b522)
- **event_id**: stepaudio-3-launch | **track**: 🤖 AI 前沿 | **source**: 阶跃星辰 | **age**: 20h
- 9/15 发布 StepAudio 3 系列:Realtime(全双工实时对话,Tool Call 异步执行不阻塞语音会话)、ASR(WER 1.7% 并列全球第一,2.8 元/小时)、TTS(真人级副语言还原)、Gen(通用音频)、Music(音乐创作)。Artificial Analysis 对话动态 98.9%、语音推理 99.7% 双登顶。语音客服/导购的可用性门槛再次被拉低。

### [Atria Dawn Preview 开源:7440 亿参数,多项基准比肩顶尖闭源模型](https://mp.weixin.qq.com/s?__biz=Mzk3NTc1NTU0Mw==&mid=2247513726&idx=1&sn=6e3f6bdd4d0260ec2180f77af2ad2ef3)
- **event_id**: atria-dawn-preview-open-source | **track**: 🤖 AI 前沿 | **source**: 魔搭 ModelScope 社区 | **age**: 16h
- 魔搭社区 9/15 消息:Atria Dawn Preview 开源,7440 亿参数,多项基准比肩顶尖闭源。开源权重阵营在 DeepSeek/Llama/Qwen 之外又多一个旗舰级选项,自部署路线的成本结构测算值得重做。

### [生数科技 Vidu S2 发布:实时数字人 720P/25-42FPS,视频流实时编辑,当天全量开放](https://mp.weixin.qq.com/s?__biz=MzkzNDQxOTU2MQ==&mid=2247520679&idx=1&sn=89189d33180d22ff005ff9fd95df009d)
- **event_id**: vidu-s2-launch | **track**: 🎨 创意广告 | **source**: 赛博禅心 / 生数科技 | **age**: 24h
- 9/15 生数科技发布 Vidu S2 双模型:S2-Avatar 实时交互数字人(720P、25-42 FPS、可打断、互动中换参考图即时换装、全身大幅动作),S2-Editing 实时视频流编辑(风格迁移/虚拟试穿/人物替换/背景替换),支持转双目空间视频。消费级 GPU 实时运行,当天全量开放体验与 API。数字人从「预渲染素材」变成「可实时互动的演员」。
- 补充角度:
  - [Vidu 官方体验入口与 API 文档](https://www.vidu.cn/vidu-stream)
  - [技术报告 arXiv:2609.11638(Self-Replay Forcing 解决长时误差累积)](https://arxiv.org/html/2609.11638v1)

### [倒计时 8 天:Sora API 与 Videos 端点 9/24 永久关停,无官方继任模型,数据将被删除](https://community.openai.com/t/release-sora-2-open-weights-before-shutdown/1388719)
- **event_id**: sora-api-final-shutdown | **track**: 🎨 创意广告 | **source**: OpenAI Developer Community / 迁移指南多源 | **age**: 28h
- 9/24 后 v1/videos 端点、sora-2/sora-2-pro 及全部快照下线,弃用表中无官方替代;所有调用返回 410,已生成视频与 prompt 历史永久删除(sora.chatgpt.com/sunset 导出)。仍在生产环境调用 Sora 的团队必须本周完成资产导出与迁移测试;候选:Veo 3.1(企业合规)、Kling 3.0(成本产能)、Seedance 2.5、自托管 Wan 2.2(发布时间近似)。
- 补充角度:
  - [迁移指南:Sora API Shutdown,Where to Migrate Your Video Workflow Now](https://miraflow.ai/blog/sora-api-shutdown-video-model-alternatives-migration-guide-2026)
  - [成本测算:Sora 2 与 Videos API 关停后的每秒真实成本](https://ecorpit.com/sora-2-videos-api-shutdown-migration-cost-2026/)

### [实测 Seedance 2.5 vs 可灵 3.0:广告级视频生成谁能「无痛当导演」](https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA==&mid=2247745328&idx=1&sn=b896a7f4450e572ef61378b377e02307)
- **event_id**: seedance-2-5-vs-kling-3-test | **track**: 🎨 创意广告 | **source**: AI科技评论 | **age**: 42h
- AI科技评论 9/14 实测对比字节 Seedance 2.5 与快手可灵 3.0 的广告级可用性。正值 Sora 退出倒计时,两大国产视频模型的实测对比是迁移选型的直接输入。

### [AI 短视频不再只是文生视频:MoneyPrinterTurbo + LTX-2 拼出完整流水线](https://mp.weixin.qq.com/s?__biz=MzU2NzkxNDY0Ng==&mid=2247491060&idx=1&sn=b25c61df7cc77ca3b40fd847b056e622)
- **event_id**: ltx2-moneyprinterturbo-pipeline | **track**: 🎨 创意广告 | **source**: 山行AI | **age**: 28h
- 山行AI 9/14 拆解:开源 MoneyPrinterTurbo 与新模型 LTX-2 组合,从文案、配音、画面到成片搭出完整 AI 短视频流水线,全程可本地跑。「30 分钟能跑通」标准的直接候选,也是 Sora 关停后的自托管替代路径。

### [AWS 官方教程:用 SageMaker 无服务器定制模型搭建 AI 商品打标系统](https://aws.amazon.com/blogs/machine-learning/build-an-ai-powered-product-tagging-system-with-amazon-sagemaker-serverless-model-customization/)
- **event_id**: aws-ai-product-tagging | **track**: 🛒 AI 电商自动化 | **source**: AWS Machine Learning Blog | **age**: 12h
- AWS 9/15 发布端到端教程:SageMaker 无服务器端点 + 模型定制搭建商品目录自动打标。这正是 09-15「catalog 语义化决定 AI 搜索推荐」的工程落地,可直接改造成 listing 属性补全流水线。

### [支付宝「阿宝」背后的 Agentic 终端:xUI 如何把 AI 交互从对话推到办事](https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651293010&idx=2&sn=685098b5812ea76b1c0f2e4af1b2bade)
- **event_id**: alipay-abao-agentic-terminal-xui | **track**: 🛒 AI 电商自动化 | **source**: InfoQ 中文 | **age**: 38h
- InfoQ 9/14 拆解支付宝「阿宝」的 Agentic 终端架构:xUI 层把「对话」重构为「办事」,从意图识别直达交易执行。结合蚂蚁官宣发力电商 AI Agent 生态,支付入口的 Agent 化是代理式商务的中国形态。

### [白鲸出海:腾讯要在海外上线广告平台?](https://mp.weixin.qq.com/s?__biz=MzYzNTkyMTI2Ng==&mid=2247576770&idx=2&sn=a9a1595f9c4aa399896d2dde18f32466)
- **event_id**: tencent-overseas-ads-platform | **track**: 🛒 AI 电商自动化 | **source**: 白鲸出海 | **age**: 14h
- 腾讯被传将在海外上线广告平台。若属实,跨境卖家在 Meta/Google/TikTok 之外将多一个买量渠道。注意标题带问号,属传闻阶段,需等官方确认——但渠道评估框架可以先行。

## 延伸阅读

- [RSIAgent:开源模型自主探索新环境,多项高难度 Benchmark 超越 GPT-6 Astra](https://mp.weixin.qq.com/s?__biz=MzA3MzI4MjgzMw==&mid=2651057178&idx=1&sn=3ee4d896a3d3ed5a39c7773752d61d30) — 🤖 AI 前沿 (23h)
- [Kimi K2.8 Preview 全量上线 Kimi Code;宇树开源 UnifoLM-ER-1 具身模型](https://mp.weixin.qq.com/s?__biz=MzkyMzcwMDIyMQ==&mid=2247503659&idx=1&sn=aac36b803b4d38d19457fa74fa0d6761) — 🤖 AI 前沿 (42h)
- [小红书 AllSpark 发布 Iris:同量级最强开源 Search Agent](https://mp.weixin.qq.com/s?__biz=Mzg4OTc2MzczNg==&mid=2247496383&idx=1&sn=2db8607f797615a3647d9fec7e54f448) — 🤖 AI 前沿 (42h)
- [书生-S2 发布:科学能力比肩顶尖闭源,通用性能居开源第一梯队](https://mp.weixin.qq.com/s?__biz=Mzk3NTc1NTU0Mw==&mid=2247513224&idx=1&sn=d5c007beb496e98396e0b659ad676dff) — 🤖 AI 前沿 (39h)
- [AI 基础设施公司 Cornelis 获 2.05 亿美元融资](https://mp.weixin.qq.com/s?__biz=MzI4NTgxMDk1NA==&mid=2247518095&idx=3&sn=d235bd8872728a72d4d952471d288710) — 🤖 AI 前沿 (25h)
- [模型一模一样,Token 却相差 70 倍?三项实测揭开 AI 编程工具的成本黑洞](https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247667066&idx=2&sn=344e0406d48f22773c43733c3c570bce) — 🤖 AI 前沿 (47h)
- [巨头鏖战 AI 智能体终端:用 Agent 重做操作系统,荣耀先交卷](https://mp.weixin.qq.com/s?__biz=MzA4MTQ4NjQzMw==&mid=2652810335&idx=1&sn=aa5d9874eb797455ba5ad12014fcef2a) — 🤖 AI 前沿 (17h)
- [实测最新版「豆包手机」助手:所有手机里的 AI 都该变成它这样](https://mp.weixin.qq.com/s?__biz=MzkyNjU2ODM2NQ==&mid=2247632957&idx=1&sn=568bda00ce764c2c03d97683d72aca50) — 🤖 AI 前沿 (45h)
- [从「会干活」到「能交付」,京东正在重新定义 AI 办公](https://mp.weixin.qq.com/s?__biz=MzkyNTY1MjE2OA==&mid=2247494437&idx=1&sn=7544abf6f77d798323cf8be5819eb03f) — 🛒 AI 电商自动化 (19h)
- [AWS:用 MMF + Databricks Genie + QuickSight 自动化补货](https://aws.amazon.com/blogs/machine-learning/automate-replenishment-with-mmf-databricks-genie-and-amazon-quick/) — 🛒 AI 电商自动化 (36h)
- [Databricks 营销团队用 Genie 让数据使用效率提升 3 倍](https://www.databricks.com/blog/databricks-marketers-use-data-3x-genie-ai-analytics-assistant) — 🎨 创意广告 (27h)
- [魔搭第十期 AIGC 月度榜单发布(月榜收官)](https://mp.weixin.qq.com/s?__biz=Mzk3NTc1NTU0Mw==&mid=2247513726&idx=2&sn=a3d6a985b06f10acd7a4467db7a67d7b) — 🎨 创意广告 (16h)
- [Meta Ads 2026 全年更新汇总:Advantage+ 默认化、创意多样性评分、$75B 年化](https://hawky.ai/blog/meta-ads-updates-2026) — 🎨 创意广告 (硬窗口外延伸参考)
- [子不语 2026 半年报:营收 28.27 亿 +44%,TikTok 渠道 +662%,半年自制 AIGC 视频超 5 万条](https://www.ebrun.com/20260831/703914.shtml) — 🎨 创意广告 (硬窗口外延伸参考,AI 素材规模化最硬的公开案例)
- [AI UGC 广告工具 2026 全景实测:Arcads 胜在真实感,Creatify 胜在产能](https://www.omniconvert.com/nexus/compare/arcads-vs-creatify/) — 🎨 创意广告 (硬窗口外延伸参考)
- [2026 跨境电商奔向「Agent 2 Agent」时刻](https://www.tmtpost.com/8098002.html) — 🛒 AI 电商自动化 (硬窗口外延伸参考)

## 今日选题

1. **AEF-1 三方联签:「可被审计」从倡议变成 Agent 产品的准入证** (high, 🤖 AI 前沿, 🛒 AI 电商自动化)
   - 角度: 拆 AEF-1 三大支柱,翻译成工程检查清单:决策链日志、动作分级权限、可回滚、可归因、评估接口预留。
   - 推荐格式: deep-dive
   - Hook 候选: xAI、OpenAI、Anthropic 罕见签了同一份文件,对你意味着三件事 / 把 AEF-1 和企业限制 Claude 连起来看

2. **数据留存政策取代 benchmark:企业 AI 选型的第一筛换了** (high, 🤖 AI 前沿, 🛒 AI 电商自动化)
   - 角度: 英伟达/Palantir/Booz Allen 的共同点是数据留存条款。给出「AI 供应商数据条款检查清单」:留存时长、触发条件、可撤销性、自有云存放(EFS 模式)。
   - 推荐格式: methodology
   - Hook 候选: 英伟达是 Anthropic 的投资方,却限制员工用 Claude / 大部分人评估 AI 供应商的方式是错的

3. **Sora API 关停倒计时 8 天:视频广告流水线的迁移清单** (high, 🎨 创意广告)
   - 角度: 三步行动:本周导出资产、审计代码中所有 videos 端点调用、按质量/成本/时延路由到 Veo 3.1 / Kling 3.0 / Seedance 2.5 / 自托管。
   - 推荐格式: tool-share
   - Hook 候选: 8 天后,你的 Sora 视频会被永久删除 / OpenAI 没有给继任者——迁移只能自己来

4. **Vidu S2 实时数字人:直播电商素材从「预渲染」进入「可互动」** (high, 🎨 创意广告, 🛒 AI 电商自动化)
   - 角度: 拆三个电商场景:直播间数字人即时换装、客服视频应答、广告素材实时 A/B。当天全量开放,可实测。
   - 推荐格式: tool-share
   - Hook 候选: 数字人第一次可以边播边换衣服 / Vidu S2 发布了,对做素材的意味着三件事

5. **飞书 8.0 × 豆包工作伙伴:团队 Agent 的权限设计样本** (medium, 🤖 AI 前沿, 🛒 AI 电商自动化)
   - 角度: 拆独立身份/独立权限/记忆/跨级申请/Token 配额五个设计点,对照电商团队场景。
   - 推荐格式: deep-dive
   - Hook 候选: 中国第一个团队 Agent 进工作群了,它的权限设计值得抄 / Agent 进群的先决条件不是聪明,是权限边界

6. **OpenAI 收购 Glass Imaging:多模态的下一站是拍摄瞬间** (medium, 🤖 AI 前沿, 🎨 创意广告)
   - 角度: 拍摄瞬间处理 RAW 而非后期修图——AI 生图竞争从「生成」向「采集端增强」蔓延。结合 io Products 推演设备版图。
   - 推荐格式: commentary
   - Hook 候选: OpenAI 买了一家相机公司,不是手机公司 / 把收购 Glass Imaging 和收购 io 连起来看

7. **商品打标自动化:AWS 官方教程给出的 catalog 语义化最小实现** (high, 🛒 AI 电商自动化)
   - 角度: 把 SageMaker 无服务器打标教程改造成跨境 listing 属性补全流水线,承接 09-15 Shopify AI 搜索选题的落地篇。
   - 推荐格式: tool-share
   - Hook 候选: 转化率 +80% 的前提,是把商品打成机器能读的标签 / AWS 官方出了打标教程,改成 listing 流水线只要三步

8. **支付宝「阿宝」xUI:支付入口 Agent 化,代理式商务的中国形态** (medium, 🛒 AI 电商自动化, 🤖 AI 前沿)
   - 角度: 对照 Google UCP / OpenAI ACP(09-15 协议战争)看中国路径:不靠开放协议,靠超级 App 内权限体系。
   - 推荐格式: deep-dive
   - Hook 候选: 美国人在签协议,中国人在做超级 App / 支付宝的 Agent 已经开始「办事」了

9. **腾讯海外广告平台传闻:跨境买量的第四极值得提前评估吗** (medium, 🛒 AI 电商自动化, 🎨 创意广告)
   - 角度: 传闻阶段先建渠道评估框架:流量结构、受众重叠度、先发品类。框架可复用到任何新渠道。
   - 推荐格式: news-commentary
   - Hook 候选: 如果腾讯在海外开广告平台,谁会先吃到红利 / 新渠道传闻的正确打开方式:先建评估框架

10. **子不语财报拆解:半年 5 万条 AIGC 视频,TikTok 渠道 +662%** (high, 🎨 创意广告, 🛒 AI 电商自动化)
    - 角度: 财报级验证:AIGC 视频工厂 Q2 投产、AI 人效 +35%、「达人+商品卡+自制视频」结构。测算自建同类流水线的成本结构。数据为公司自述,引用需标注。
    - 推荐格式: case-study
    - Hook 候选: 一家上市服装公司,半年做了 5 万条 AI 视频 / 素材规模化的第一个财报级样本

11. **Gemini 3.8 Live + StepAudio 3 同日:语音客服 Agent 的选型表该更新了** (medium, 🤖 AI 前沿, 🛒 AI 电商自动化)
    - 角度: 同日两个实时语音大模型。更新语音客服选型维度:全双工、打断处理、异步任务、ASR 成本(2.8 元/小时)。
    - 推荐格式: news-commentary
    - Hook 候选: 同一天,Google 和阶跃都押注了实时语音 / 客服 Agent 的下一战不是答案质量,是边想边说

12. **AI 短视频流水线本地版:MoneyPrinterTurbo + LTX-2 实测候选** (medium, 🎨 创意广告)
    - 角度: 开源组合全程本地跑,作为 Sora 关停后的自托管替代路径,按「30 分钟跑通」标准做实测。
    - 推荐格式: tool-share
    - Hook 候选: 不花一分钱 API,本地搭一条短视频流水线 / Sora 关停后的 Plan B,是开源

## 跨领域机会

### AI 前沿 × 电商自动化
AEF-1 三方联签 + 英伟达/Palantir 以数据留存为由限制 Claude + 飞书团队 Agent 权限设计,同日指向「可审计性成为 Agent 准入证」。做电商 Agent/代运营工具的团队,决策链日志、动作分级权限、评估接口预留应从「nice to have」升级为一期工程——这是「嵌入式评估员」从治理话语变成采购条款的拐点。

### AI 生视频 × 电商素材供应链
Vidu S2 实时数字人当天全量开放、Sora API 9/24 关停无继任、子不语财报验证 5 万条 AIGC 视频产能——视频素材供给端正在重组,迁移与选型动作必须在本周(资产导出)到本月(替代模型压测)完成,先动的人拿到成本与产能双红利。

## 本周表现摘要

- 周期: 2026-09-09 ~ 2026-09-16(输入文件实际仅含 2026-08-26 ~ 2026-08-27 历史数据)
- 发布量: 8(历史数据)
- 中位数曝光: 无法计算(指标全部待补)
- 覆盖不足赛道: 🤖 AI 前沿, 🛒 AI 电商自动化, 🎨 创意广告(均无近期数据)
- 洞察: inputs/published_last_7d.md 连续第十八期无更新,Phase 1 学习第十九期空转。今日按 profile_longterm 元模式 + 赛道均衡补位生成草稿。

## 草稿候选

### 草稿 1 — wechat (deep-dive)
- **hook_pattern**: 把 X 和 Y 连起来看(跨领域连接型)
- **tags**: 🤖 AI 前沿, 🛒 AI 电商自动化

标题:把三件事连起来看:xAI/OpenAI/Anthropic 联签评估标准、英伟达限制员工用 Claude、飞书发布团队 Agent——「可被审计」正在成为 Agent 的准入证

开头两段:
9 月 15 日这一天发生了三件看似无关的事。第一件,xAI、OpenAI、Anthropic 共同签署了 AEF-1 标准——独立第三方评估的最低运行条件,覆盖评估机构的独立性、对模型内部的技术访问权限、评估条件披露。第二件,The Information 披露英伟达在内部限制员工使用 Claude Fable,理由是 Anthropic 六月改了数据留存政策——客户日志最多可留两年。第三件,飞书发布 8.0 和「豆包工作伙伴」,国内第一个有独立身份、独立权限、可跨级申请授权的团队 Agent 进了工作群。

三件事指向同一个方向:Agent 要进企业,光聪明不够,得可被审计、可被限制、可被追责。Dario Amodei 上周说要给第三方评估员「接近内部风控团队的权限」,这周就变成了三家联签的书面标准。这不是巧合,是准入门槛正在成型。

提纲:
一、AEF-1 拆条:独立性/访问权限/透明度三大支柱各自要求什么
二、企业侧的镜像动作:英伟达、Palantir、Booz Allen 的限制清单,数据留存条款成为采购第一筛
三、飞书豆包工作伙伴的权限设计:独立身份、Token 配额、跨级申请——内部权限边界的第一个国内样本
四、翻译成工程清单:决策链日志、动作分级权限、可回滚、可归因、评估接口预留
五、预判:一年内,「你的 Agent 能被审计吗」会和「你的系统过等保了吗」一样成为甲方例行问题

资料来源:Latent Space AINews(2026-09-15)、aievaluatorforum.org 标准原文、PYMNTS/The Information(2026-09-14/15)、新智元/智东西(2026-09-15)。

### 草稿 2 — x (news-commentary)
- **hook_pattern**: X 刚发布/更新了,对你意味着三件事(新闻翻译型)
- **tags**: 🎨 创意广告, 🤖 AI 前沿

Vidu S2 just launched — and Sora API dies in 8 days.

The video supply chain for ad creatives is being rebuilt this week.

Three things this means for you:

1) Vidu S2-Avatar: real-time digital humans at 720p/25-42fps, swap reference images mid-interaction (outfit change on the fly). Full public access + API from day one. Not a waitlist.

2) Sora API (v1/videos, sora-2, sora-2-pro) shuts down Sept 24. No successor model in OpenAI's deprecation table. All generated videos and prompt history get permanently deleted. Export at sora.chatgpt.com/sunset now.

3) The migration shortlist: Veo 3.1 (enterprise compliance), Kling 3.0 (cost per second at scale), Seedance 2.5, or self-hosted Wan 2.2 / LTX-2 pipelines.

If any production workflow still calls the Sora API, this is the week to audit your code paths.

Sources: Vidu official / ShengShu Tech (Sep 15), OpenAI developer community deprecation notice.

### 草稿 3 — xhs (case-study)
- **hook_pattern**: 实测了 X,结果…(亲身测试开场的案例变体:财报数据实证)
- **tags**: 🎨 创意广告, 🛒 AI 电商自动化

标题:一家上市服装公司,半年用 AI 做了 5 万条带货视频,财报里写着答案

正文要点:
📊 子不语(港股 02420)2026 半年报,几个数字值得做素材的人抄下来:

1️⃣ TikTok 渠道收入 2.89 亿元,同比 +662%,从试水变成第二大渠道(占比 2%→10.2%)
2️⃣ 上半年自制 AIGC 视频超过 5 万条——注意是「自制」,不是达人投放
3️⃣ 专门的「AIGC 视频工厂」Q2 投产,做规模化短视频生成
4️⃣ 销售结构:达人 + 商品卡 + 自制视频三条腿
5️⃣ AI 还用在广告诊断、自动定价、智能审单,整体人效同比 +35%

💡 对我们意味着什么:
· AI 素材规模化第一次有了上市公司财报级的验证,不是工具商的软文数字
· 它的打法不是「一条爆款」,是「产能结构」——5 万条铺出来的渠道占比
· 自建流水线的成本结构测算,可以拿它的毛利变化(74%)做参照系

⚠️ 提醒:数据来自公司财报自述,引用时注意口径。

#AI电商 #跨境电商 #AIGC视频 #TikTokShop #AI素材

## 系统建议

### 信息源
- **promote**: Latent Space (AINews)(连续两日命中,AEF-1 独家快讯,high);阶跃星辰/魔搭等厂商官方公众号(一手发布早于二手编译,medium)
- **demote**: fieldtheory 本地书签(sync 停在 09-08,连续第七日 0 供给,high);Obsidian 微信收藏(连续第十四日无新笔记,medium)
- **add**: aievaluatorforum.org(AEF-1 一手发布方,high);PYMNTS AI/Commerce 板块(连续两日命中,medium)

### 选题库
- **archive**: (本期无)
- **add**: AI 语音模型与客服/导购语音化(Gemini 3.8 Live + StepAudio 3 同日 + Klaviyo 语音化,一周三次命中,high);AI 视频模型迁移与多模型容灾(Sora 关停无继任 + Vidu S2 + LTX-2 本地流水线,high);Agent 可审计性与权限设计(AEF-1 联签 + 团队 Agent 权限样本,建议与「AI 素材合规与披露」合并审议,high)

### 定位漂移

- **观察**: 「可审计性/治理机制化」连续三日成为 must_reads 主线(09-14 Dario 限速 → 09-15 安全评估机构 → 09-16 AEF-1 联签 + 企业数据留存限制),已从新闻维度升级为工程与采购维度。
  **建议**: 考虑在 profile_longterm 跨领域优势中显式加入「AI 合规接口 × 电商/广告产品」维度。 (confidence: high)
- **观察**: 人工预选通道(书签 + 微信收藏)已连续多日 0 供给,must_reads 连续一周以上全部依赖 RSS + WebSearch。
  **建议**: 恢复 fieldtheory sync(重取 cookies)与微信收藏同步,否则在 info_sources 中暂时降权这两条通道。 (confidence: high)
