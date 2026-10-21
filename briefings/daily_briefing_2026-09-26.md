# Daily Briefing — 2026-09-26

生成时间: 2026-09-26T00:00:00Z | 窗口: 2026-09-24T00:00:00Z 起 48h 内

> 今日主线:Sora API 正式关停,视频模型格局从「OpenAI 领跑」切换为「多极替代」;同时 Agent 基础设施这周连下两城——Runway 把视频生成接进 Claude MCP,Google 给企业语音助手装上实时 Avatar 面孔。创意生产正在从「人去点模型」变成「Agent 调度多个模型」。

## 今日必看 (10 条)

### 1. [Sora API 9 月 24 日正式关停,无继任者:视频模型格局进入后 OpenAI 时代](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)
- 赛道: 🎨 创意广告 | event_id: `openai-sora-api-shutdown-2026-09-24` | age_hours: 36 | 时间置信度: exact
- 来源: OpenAI Help Center / Kingy.ai
- OpenAI 官方确认 Sora web/app 已于 2026-04-26 停服,Sora API 及 Videos API 于 2026-09-24 正式 discontinuation。开发者于 2026-03-24 即收到废弃通知,受影响模型包括 sora-2、sora-2-pro 及全部快照。OpenAI 未公布替代模型,官方导出窗口结束后数据将被永久删除。
- 为何重要: 这是 09-23 期已预警的硬截止。对把 Sora 2 嵌入素材产线的团队,今天不是决策日,是执行后的复盘日。迁移窗口关闭意味着任何仍在硬编码 sora-2 的工作流已经中断。
- 硬数字: 2026-04-26 消费者端关停 | 2026-09-24 API 关停 | 2026-03-24 开发者通知 | 无官方替代模型

### 2. [Runway 发布 MCP 服务器:Claude / ChatGPT / Cursor 可直接生成视频与图片](https://alphasignal.ai/news/runway-brings-ai-video-and-image-generation-directly-into-claude)
- 赛道: 🎨 创意广告 | event_id: `runway-mcp-server-launch` | age_hours: 24 | 时间置信度: date-only
- 来源: AlphaSignal / Runway
- Runway 推出官方 MCP 连接器,支持 Claude、ChatGPT、Cursor、Replit 通过 OAuth 直接调用 Runway 视频/图片生成能力,无需单独 API key。支持视频模型 Gen-4.5、Gen-4 Turbo、Seedance 2.5、Kling 3.0、Veo 3.1;图片模型 Gen-4 Image、GPT Image 2、Nano Banana Pro。输出自动存入用户 Runway 库以便团队审计。
- 为何重要: 这是创意广告 Agent 化的关键基础设施。素材团队可以把 Runway 当作 Claude 的一个工具来编排,让 Agent 根据 brief 自动选择模型、提交任务、轮询结果、做变体。Sora 关停后,这种「模型可插拔」的接入方式比单一模型更抗风险。
- 硬数字: 支持 5 种 agent 环境 | 5+ 视频模型 + 3 图片模型 | OAuth 免 API key | 输出进 Runway library

### 3. [Google Gemini 3.8 Live with Live Avatar GA:给企业语音助手加上实时面孔,97 语言唇同步](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-with-live-avatar/)
- 赛道: 🤖 AI 前沿 | event_id: `google-gemini-3-8-live-avatar-ga` | age_hours: 36 | 时间置信度: exact
- 来源: Google Blog / Google Cloud / Unite.AI
- Google 于 9 月 24 日宣布 Gemini 3.8 Live with Live Avatar 面向 Gemini Enterprise 用户 GA。基于 Gemini 3.8 Pro,输入支持音频/图像/视频/文本,上下文 128K,输出含音频+视频+文本,输出上限 24K token。Live Avatar 可在 97 种语言间实时切换并唇同步,支持自定义头像(需企业白名单)。所有生成音视频带 SynthID 水印。
- 为何重要: 企业级数字人/客服 Agent 又多了一个可用选项。对电商/品牌来说,这意味着 24×7 多语言客服、导购、产品讲解可以用一个模型+Avatar 层实现,而不必分别采购 ASR/TTS/数字人/LLM。
- 硬数字: 128K 上下文 / 24K 输出 | 97 语言 | US/EU endpoints GA | SynthID 水印 | 已服务 Equal AI 每日 100 万+ 通实时电话

### 4. [Amazon 把 Seller Central 向外部 Agent 开放:卖家可用 Claude/Quick 直接改价、补货、改 listing](https://www.aboutamazon.com/news/innovation-at-amazon/seller-assistant-plugin-amazon-quick-claude)
- 赛道: 🛒 AI 电商自动化 | event_id: `amazon-selling-partner-plugin-agentic-workflows` | age_hours: 48 | 时间置信度: date-only
- 来源: About Amazon / GeekWire / Distribution Strategy
- Amazon 在 Accelerate 大会上推出 Selling Partner Plugin,率先支持 Anthropic Claude 与 Amazon Quick,让卖家在 Seller Central 之外直接操作店铺:查库存、调价、更新 listing。同时 Seller Assistant 升级为 agentic workflows,可持续监控并执行定价、补货、账号健康等任务,卖家可设置仅推荐或自动执行。插件采用 no-code 连接,动作需卖家批准,数据留在 Amazon 基础设施内。
- 为何重要: 这是 Amazon 从「给卖家一个 AI 问答助手」到「让 Agent 能直接运营店铺」的关键一步。与 Shopify AI Toolkit 形成对照:一个把店铺数据接进 coding agent,一个把 Claude 接进 Seller Central。
- 硬数字: 90%+ 卖家已覆盖 | 90% 推荐接受率 | 90% 卖家使用第三方 AI 工具 | 插件 beta 仅限美国站 | 12 个月免费 Quick Plus(至 2026-12-31)

### 5. [Alibaba Cloud Apsara 2026 押注 Agentic Cloud:AgentCore + Agent Context + 新一代 AI 原生云](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598)
- 赛道: 🤖 AI 前沿 | event_id: `alibaba-agentic-cloud-agentcore-apsara-2026` | age_hours: 48 | 时间置信度: date-only
- 来源: Alibaba Cloud / Pandaily / Alizila
- 阿里云在 2026 年 9 月 22–24 日杭州 Apsara 大会上发布 Agentic Cloud 全栈战略,核心三层:AgentCore(企业级 Agent 构建/运行/管理平台,含工具编排、人机协作、监控、Agent Security Center)、Agent Context(连接文档/业务系统/聊天记录/多模态数据,据称可降低 token 使用 67%)、AI 原生云基础设施(新一代 CPFS 存储成本降约 69%、HPN 8.0 Pro 网络 130,000+ 800G 端口)。
- 为何重要: 中国云厂商第一次把 Agent 基础设施作为大会主线,与北美 AWS Bedrock AgentCore(注意命名撞车)、Google Agentic Commerce 形成三极。对出海/跨境电商卖家,阿里云的 Agentic Cloud 可能成为连接国内供应链与海外平台的新编排层。
- 硬数字: Agent Context 降 token 67% | CPFS 降存储成本 69% | HPN 8.0 Pro 130,000+ 端口 / 100 Pb 带宽 | Qwen 4 系列(Max/Flash/Plus/27B)预告

### 6. [DeepSeek 年化收入破 10 亿美元,正 finalize 75 亿美元融资](https://www.pymnts.com/news/artificial-intelligence/2026/deepseek-doubles-annual-revenue-run-rate-to-1-billion-ahead-of-ipo/)
- 赛道: 🤖 AI 前沿 | event_id: `deepseek-1b-revenue-run-rate` | age_hours: 36 | 时间置信度: date-only
- 来源: PYMNTS / The Information / The Next Web
- DeepSeek CEO 梁文锋向投资者披露,公司年化收入运行率已突破 10 亿美元,较此前约 5 亿美元翻倍;2026 年前 7 个月收入约 4.75 亿元人民币,约为 2025 全年的 10 倍。公司正在 finalize 约 500 亿元人民币(约 75 亿美元)的 B 轮融资,估值约 5000 亿元人民币(约 750 亿美元),计划 2027 年在上海科创板 IPO。
- 为何重要: 这是继 8 月涨价 2.3–4.5 倍后,DeepSeek 商业化的又一次验证。它证明了「低价获客→涨价验证定价权→再融资」这条路径在中国模型公司可行。对依赖 DeepSeek API 的电商/广告 Agent 团队,需要把 peak/off-peak 价差和后续融资后的战略投入纳入成本模型。
- 硬数字: 年化收入运行率 $1B | 2026 前 7 个月收入 ~4.75 亿元 | B 轮 ~75 亿美元 / 估值 ~750 亿美元 | 8 月涨价 2.3x–4.5x | 计划 2027 上海 IPO

### 7. [OpenAI ChatGPT Voice 升级:支持插件、可在 GPT-6 Astra/Sol/Luna 之间切换](https://aiweekly.co/alerts/openai-adds-plugins-to-chatgpt-voice-lets-users-switch-between-gpt-6-astra-sol)
- 赛道: 🤖 AI 前沿 | event_id: `openai-chatgpt-voice-plugins-model-switching` | age_hours: 48 | 时间置信度: date-only
- 来源: AI Weekly / 9to5Mac / EvoLink
- OpenAI 于 9 月 24 日宣布 ChatGPT Voice 支持插件(email、calendar、Slack 等),并允许用户在 GPT-6 Astra、Sol、Luna 三个模型之间切换。Voice 同时集成进 ChatGPT Work,支持文档/表格生成。此前 9 月 3 日 GPT-6 Astra GA,9 月 22 日 Sol/Luna 上线 API。
- 为何重要: 语音 Agent 开始具备工具调用和模型选型能力。对客服、销售、导购类 Agent,这意味着可以用轻量模型处理简单查询、用 Astra 处理复杂推理、用 Sol 处理代码/结构化任务,而不必把所有语音流量都堆到最贵的模型上。
- 硬数字: GPT-6 Astra 9/3 GA | Sol/Luna 9/22 API 上线 | 9/24 Voice 插件全球 rollout | Astra 定价 $10/$50 per 1M tokens

### 8. [OpenAI `__obi` Cookie 争议:ChatGPT 广告测量像素被指可跨站关联账号](https://tech.yahoo.com/ai/chatgpt/articles/openai-cookie-may-chatgpt-accounts-183610018.html)
- 赛道: 🎨 创意广告 | event_id: `openai-obi-cookie-cross-site-tracking` | age_hours: 48 | 时间置信度: date-only
- 来源: Yahoo Tech / NotebookCheck / CybersecurityNews
- 独立研究者 Buchodi 于 9 月 20–21 日发布逆向工程发现:OpenAI 的广告测量系统使用名为 `__obi` 的 cookie,在广告主网站加载 `oaiq.min.js` 像素时可被跨站发送回 `bzr.openai.com`,可能把用户在第三方网站的行为与 ChatGPT 账号关联。OpenAI 9 月 10 日更新的 cookie 政策将该 cookie 归类为「analytics」,有效期一年;Safari 智能反追踪机制可阻止,Chrome 不阻止。
- 为何重要: ChatGPT 广告业务 reportedly 已超过 10 亿美元运行率,但测量基础设施的隐私设计直接影响广告主能否持续依赖其归因。如果监管介入或浏览器默认阻止,ChatGPT 广告的归因能力会突然变弱,广告主需要有备用测量方案。
- 硬数字: 9/20–21 研究者披露 | cookie 有效期 1 年 | SameSite=None; Secure; HttpOnly | OpenAI 未正面回应账号关联质疑

### 9. [Google Pixel 11「Call for Me」:Gemini 可代拨电话、等客服、处理 IVR](https://aiweekly.co/ai-news-today/edition/2026-09-25)
- 赛道: 🤖 AI 前沿 | event_id: `google-pixel-call-for-me-gemini-agent` | age_hours: 24 | 时间置信度: date-only
- 来源: AI Weekly / Google
- Google 为美国 Pixel 11 用户(Gemini 订阅者)推出「Call for Me」功能:Gemini 可用用户本机号码拨打商家电话,浏览语音菜单、等待人工客服、与对方交谈;用户可实时查看转录并随时接管通话。
- 为何重要: 这是消费级语音 Agent 从「帮我查信息」到「帮我完成真实世界通话任务」的又一步。对本地服务、预约、售后等场景,Agent 开始能代替用户执行「需要真人接听方配合」的任务,信任与授权模型是下一个瓶颈。
- 硬数字: Pixel 11 + 美国 + Gemini 订阅 | 实时转录 | 人工随时接管

### 10. [Qwen-Audio 3.1 发布,语音 API 最高降 95%](https://the-decoder.com/alibaba-launches-qwen-audio-3-1-with-five-new-models-and-slashes-ai-audio-prices-by-up-to-95-percent/)
- 赛道: 🤖 AI 前沿 | event_id: `qwen-audio-3-1-price-cut` | age_hours: 48 | 时间置信度: date-only
- 来源: The Decoder / Alibaba Cloud / AI Weekly
- 阿里云于 9 月 23 日发布 Qwen-Audio 3.1 系列,含 ASR、ASR-Next、TTS、TTS-Next、Realtime 五款模型,并大幅降价:ASR 最高降 95%、Realtime ~85%、TTS ~70%。部分模型(如 qwen-audio-3.1-tts-flash、qwen-audio-3.0-realtime-flash)自北京时间 9 月 22 日 00:00 起在北京、新加坡站点执行新价。Realtime 支持 262K token 上下文、函数调用、联网搜索、声音克隆。
- 为何重要: 语音 Agent 的成本结构进一步崩塌。对需要多语言客服、直播语音、商品讲解的电商/广告场景,自建语音 Agent 的经济性持续改善,但需评估与 ElevenLabs 等厂商在音色、情感、延迟上的实际差距。
- 硬数字: 5 款模型 | ASR 降 95% / Realtime 降 85% / TTS 降 70% | Realtime 262K 上下文 | 9/22 北京时间起执行新价

## 延伸阅读 (10 条)

- [Sora 关停的替代方案清单:Seedance / Veo / Kling / MiniMax](https://www.seeddance.io/blog/sora-alternative-2026) — 🎨 创意广告 (age 36h) — 延伸参考:与 must_read 01/02 共同构成迁移决策背景。
- [Docker 发布可复用 Skills for AI Coding Agents](https://github.com/docker/skills) — 🤖 AI 前沿 (age 24h) — 延伸参考:Agent 工具链基础设施,与 Runway MCP 同主题。
- [Meta Muse macOS 应用被曝劫持漏洞,Meta 已修复](https://www.bleepingcomputer.com/news/security/meta-patches-muse-mac-app-vulnerability-that-let-hackers-hijack-agent/) — 🛒 AI 电商自动化 (age 48h) — 延伸参考:Agent 安全边界案例。
- [Google Project Suncatcher:10 月 1 日用 SpaceX 火箭发射带 4 颗 TPU 的试验卫星](https://buttondown.com/thedailyalphaai/archive/trump-and-xi-ai-moves-to-the-center-of-thursdays/) — 🤖 AI 前沿 (age 36h) — 延伸参考:AI 算力向太空延伸的早期信号。
- [OpenAI 被曝 ChatGPT Pro Max 新订阅 tier](https://aitoolsrecap.com/Blog/ai-news-september-26-2026) — 🤖 AI 前沿 (age 12h) — 延伸参考:待更多独立信源确认。
- [Huawei Ascend 开放 ThinkPro 与 5000+ MCP 资产](https://juejin.cn/post/7689030281899180070) — 🤖 AI 前沿 (age 24h) — 延伸参考:国产 AI 基础设施另一条线。
- [Anthropic 用 Claude Agent 自建生物实验室](https://venturebeat.com/security/openai-hacked-by-small-team-of-white-hat-security-researchers-using-anthropics-claude-opus-5) — 🤖 AI 前沿 (age 72h) — 延伸参考:Agent 在科研场景的落地。
- [Meta Creative Diversity score 上线后续:近似重复素材会被归为一个实体](https://goodmorningco.com/blog/meta-ads-update-september-2026) — 🎨 创意广告 (age 96h) — 延伸参考:与 09-23 期呼应,素材去重主题。
- [TikTok Shop AI 内容治理规则与处罚案例](https://www.storika.ai/guides/tiktok-shop-creator-compliance-rules-2026) — 🎨 创意广告 (age 108h) — 延伸参考:AI 素材合规背景。
- [Amazon Alexa for Shopping 卖家优化指南](https://www.sellersprite.com/en/blog/amazon-alexa-for-shopping-listing-optimization-2026) — 🛒 AI 电商自动化 (age 72h) — 延伸参考:与 Amazon agentic commerce 主线互补。

## 选题 (12 条)

### topic-0926-01 — Sora API 关停日:一份迁移完成后的复盘清单
- 赛道: 🎨 创意广告 | 优先级: high | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 不是教人怎么迁移,而是给已经迁移或还没迁移的人一份复盘框架:①列出所有曾经调用 sora-2 的代码/第三方封装;②验证替代模型在 5 条核心 prompt 上的可移植性和返工率;③重算单位成本=生成费+返工费+挑选时间;④加一层模型路由层,让底层模型可配置。核心判断:Sora 的退出把视频生成从「押注单一模型」变成「必须做多模型抽象」。
- 适合平台: wechat, x, linkedin

### topic-0926-02 — Runway MCP + Sora 关停:创意 Agent 的「模型路由」时代开始了
- 赛道: 🎨 创意广告 | 优先级: high | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Runway 发布 MCP 服务器与 Sora API 正式关停并置。Runway 让一个 Agent 可以在 Claude 里调用多个视频/图片模型(Gen-4.5、Seedance、Kling、Veo),这意味着创意工作流的设计单位从「一个模型」变成「一个能选模型的 Agent」。给出一条最小可行工作流:brief → Agent 选模型 → 批量生成 → 自动入库存档 → 人工挑片。
- 适合平台: wechat, x, linkedin

### topic-0926-03 — Amazon 与 Shopify 同时把店铺接进 Claude:卖家 Agent 的两种架构
- 赛道: 🛒 AI 电商自动化 | 优先级: high | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Amazon Selling Partner Plugin(让 Claude 操作 Seller Central)与 Shopify AI Toolkit(让 Claude Code 直接管理店铺)对比。两者都在把电商后台变成 Agent 可调用的接口,但架构不同:Amazon 是「把外部 Agent 接进封闭数据」,Shopify 是「把店铺能力暴露给 coding agent」。对卖家的启示:未来竞争差异可能来自「你的数据/流程能不能被 Agent 安全调用」,而不是 manual 操作速度。
- 适合平台: wechat, linkedin, x

### topic-0926-04 — Gemini 3.8 Live Avatar:企业数字人进入「一个模型搞定语音+视觉+工具调用」阶段
- 赛道: 🤖 AI 前沿 | 优先级: high | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①128K 上下文 + 97 语言唇同步,意味着一个模型能同时处理多语言客服与可视化导购;②Gemini Enterprise GA,说明这是 toB 产品而非 demo;③SynthID 水印和企业合规,是品牌方敢用的前提。对电商/品牌的应用:24×7 多语言产品讲解、退换货客服、线下 kiosk 导购。
- 适合平台: wechat, x, linkedin

### topic-0926-05 — DeepSeek 10 亿美元运行率:中国模型公司的商业化拐点到了吗
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 市场容易把 DeepSeek 的 10 亿美元收入与 750 亿美元估值当作「中国 OpenAI」叙事,但真正值得看的是:它在 8 月涨价 2.3–4.5 倍后需求没掉,说明有定价权。对电商/广告 Agent 团队的意义:不要把 DeepSeek 永远当「便宜备选」,要把它当作一个有 peak/off-peak 价差、未来可能继续涨价的 API 来建成本模型。
- 适合平台: wechat, x

### topic-0926-06 — ChatGPT Voice 插件 + 模型切换:语音 Agent 开始「按任务选模型」
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①插件让语音 Agent 能操作邮箱/日历/Slack,从对话到动作;②Astra/Sol/Luna 可选,让成本结构可控;③Work 集成让语音输出能直接生成文档/表格。对运营团队的影响:可以把语音 Agent 接进客服、排期、内容生产流程,而不仅是问答。
- 适合平台: x, linkedin

### topic-0926-07 — OpenAI `__obi` cookie:广告主该如何准备 ChatGPT 广告归因的「隐私地震」
- 赛道: 🎨 创意广告 | 优先级: medium | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 大部分人只把它当隐私新闻,但广告主应该关注:如果跨站 cookie 被 Safari/监管阻止,ChatGPT 广告的归因能力会突然变弱。给出两条准备动作:①不要把 ChatGPT 广告当唯一增量渠道,保持独立增量测试;②建立自己的第一方转化数据,用转化 API/上传而非完全依赖像素。
- 适合平台: wechat, x, linkedin

### topic-0926-08 — Qwen-Audio 3.1 降价 95%:语音 Agent 的成本拐点之后,质量拐点在哪
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 1「实测了 X,结果…」
- 角度: 以 Qwen-Audio 3.1 的定价为引子,讨论语音 Agent 从「用得起」到「用得好」的下一步:延迟、音色一致性、情感控制、多说话人分离。给出一个 30 分钟评测清单,帮团队判断「便宜」是否足以替代现有语音供应商。
- 适合平台: xiaohongshu, wechat, x

### topic-0926-09 — 阿里云 Agentic Cloud:出海卖家该不该现在押注
- 赛道: 🛒 AI 电商自动化 × 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①AgentCore 把 Agent 生命周期管理做成云服务,降低自建门槛;②Agent Context 声称降 token 67%,对长流程 Agent 成本影响大;③与 AWS Bedrock AgentCore 撞名,选型时要先搞清楚是哪家的产品。给出观望建议:等 US/EU region 落地、等 Qwen 4 实测、等生态案例。
- 适合平台: wechat, linkedin

### topic-0926-10 — Pixel「Call for Me」:当 Agent 开始替用户打电话,产品页要准备什么
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化 | 优先级: medium | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 大部分人关注这个功能多酷,但商家应该关注:如果 Gemini 替用户打电话问库存、预约、询价,你的网站/客服热线能不能被 Agent 快速解析?给出 3 个准备动作:电话菜单结构化、FAQ 提供文本版、客服话术预留 Agent 可识别的信息片段。
- 适合平台: wechat, x

### topic-0926-11 — Agent 安全:从 Meta Muse 漏洞到 Amazon 卖家插件,权限设计不能靠模型自觉
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化 | 优先级: medium | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Meta Muse 被曝的 macOS 劫持漏洞与 Amazon 卖家插件的「动作需批准」设计并置。结论是:Agent 能力越强,越需要系统级权限控制(允许操作清单、单次上限、人工确认触发条件、审计日志),而不是指望模型拒绝。
- 适合平台: wechat, x, linkedin

### topic-0926-12 — 视频模型后 Sora 时代:品牌向内容的「人机分工线」怎么画
- 赛道: 🎨 创意广告 | 优先级: high | Hook: 元模式 1「实测了 X,结果…」
- 角度: 基于 Sora 关停+Runway MCP+MiniMax H3 品牌片案例,给出品牌视频的三层分工:概念/氛围/变体生成交给 Agent+多模型;品牌规范(字体/色值/模特形象)和合规披露必须人工校验;最终发布前做 30 秒「品牌一致性」检查。
- 适合平台: xiaohongshu, wechat

## 今日草稿 (6 条)

### x — Sora API 正式关停,大部分人没看到真正的风险
- 格式: news-commentary | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 标签: Sora, OpenAI, API sunset, video generation, migration

Sora API 9 月 24 日正式关停,没有继任者。

真正的风险不是「少了一个视频模型」,而是你的产线可能绑在一个随时会消失的 API 上。

三件事:
1) 今天把所有硬编码 sora-2 的地方列出来,第三方封装也算;
2) 在 Seedance/Veo/Kling/Runway 上各跑 5 条核心 prompt,测可移植性;
3) 加一层模型路由,让底层模型可配置。

下次再有关停,你换的是配置,不是代码。

### x — Runway MCP 让 Claude 直接生成视频,创意 Agent 的模型路由时代来了
- 格式: news-commentary | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 标签: Runway, MCP, Claude, video generation, creative agent

Runway 发布官方 MCP 服务器。

三件事:
1) Claude/ChatGPT/Cursor 可以直接调用 Runway 生成视频和图片,OAuth 连 API key 都不用;
2) 一个 Agent 可以选多个模型:Gen-4.5、Seedance、Kling、Veo;
3) 输出自动进 Runway library,团队审计和归因更清楚。

Sora 关停的同一天,Runway 让创意工作流从「人点模型」变成「Agent 调度模型」。

### x — Amazon 和 Shopify 同时做一件事:让 Claude 替你运营店铺
- 格式: news-commentary | Hook: 元模式 4「把 X 和 Y 连起来看」
- 标签: Amazon, Shopify, Claude, Agent, ecommerce

Amazon 新 Selling Partner Plugin 让 Claude 直接操作 Seller Central:改价、补货、改 listing。

Shopify AI Toolkit 让 Claude Code 直接管理店铺。

合起来看:电商后台正在变成 Agent 可调用的接口。

卖家的竞争点从「手动操作多快」变成「你的数据和流程能不能被 Agent 安全调用」。

### xiaohongshu — 我用 Runway MCP + Claude 重建了视频素材产线,Sora 关停后反而更快了
- 格式: case-study | Hook: 元模式 1「实测了 X,结果…」
- 标签: Runway, MCP, Claude, Sora, 视频素材, 创意 Agent

先说结论:Sora 关停不是灾难,是逼你升级产线架构的机会。

我之前的流程:人工选模型 → 复制 prompt → 下载素材 → 整理命名。

现在的流程:
1) 在 Claude 里写 brief;
2) Agent 自动选模型(Gen-4.5 做人像,Seedance 做氛围,Kling 做动作);
3) 输出自动进 Runway library;
4) 人只看通过品牌规范检查的那批。

结果:单条素材的「人到模型」时间从 15 分钟降到 2 分钟,更重要的是不再依赖单一模型。

#runway #mcp #claude #sora #ai视频 #创意素材 #agent

### wechat — Sora 关停、Runway 接进 Claude、Amazon 接进 Claude:这一周,Agent 开始接管创意和运营
- 格式: deep-dive | Hook: 元模式 4「把 X 和 Y 连起来看」
- 标签: Sora, Runway, Amazon, Claude, Agent, 电商, 广告

这一周发生了三件看起来不相关、但指向同一趋势的事。

第一件:Sora API 正式关停,没有继任者。视频模型赛道从「OpenAI 领跑」变成「多极替代」。

第二件:Runway 发布 MCP 服务器,Claude 可以直接生成视频和图片,并且能在 Gen-4.5、Seedance、Kling、Veo 之间选择。创意生产从「人点模型」变成「Agent 调度模型」。

第三件:Amazon 推出 Selling Partner Plugin,Claude 可以直接改价、补货、改 listing。电商运营也开始被 Agent 接管。

三者合起来,说明 Agent 正在从「聊天助手」变成「能调用工具完成真实任务的执行层」。

对做创意和电商的人来说,这意味着什么?

意味着「模型选型」和「平台操作」这两个曾经很重的技能,正在变成 Agent 的底层能力。人的价值向上移动:定义 brief、设定品牌规范、设计审批流程、处理异常。

也意味着风险在变化。当 Agent 能直接改价或生成品牌素材时,权限设计和审计日志比模型能力更重要。Meta Muse 这周刚被曝出 macOS 劫持漏洞,就是一次提醒。

今天可以做的三件事:
1. 盘点所有依赖单一模型 API 的工作流,加一层抽象接口;
2. 给 Agent 设定明确的动作边界和人工确认触发条件;
3. 把品牌规范从 PDF 转成机器可执行的规则(字体、色值、禁用场景、必须披露)。

Agent 时代不是「不需要人」,是人从执行者变成规则设计者。

### linkedin — Three moves this week show agents are becoming the execution layer for creative and commerce
- 格式: commentary | Hook: 元模式 4「把 X 和 Y 连起来看」
- 标签: AI agents, Sora, Runway, Amazon, Claude, creative automation, ecommerce

Three moves this week, same direction.

OpenAI shut down the Sora API with no successor, ending the era of betting on a single video model.

Runway shipped an MCP server, letting Claude generate video and images across Gen-4.5, Seedance, Kling, and Veo. Creative production is shifting from "pick a model" to "let an agent route the task."

Amazon opened Seller Central to Claude via the Selling Partner Plugin, letting agents adjust pricing, restock inventory, and update listings. Ecommerce operations are next.

The common thread: agents are becoming the execution layer, and humans are moving up to briefs, guardrails, and exceptions.

What to do now:
- Abstract your model dependencies so a shutdown doesn't break your pipeline.
- Define approval gates and audit trails before giving agents write access.
- Turn brand guidelines from PDFs into machine-enforceable rules.

The winners will be the ones who design the rules, not the ones who fight the tools.

## 跨领域机会 (2 条)

### cross-0926-01 — 用 Runway MCP + Amazon Selling Partner Plugin 搭一条「素材 → 上架」Agent 链路
- 赛道: 🎨 创意广告 × 🛒 AI 电商自动化
- Runway MCP 让 Agent 能批量生成商品视频/图片,Amazon Selling Partner Plugin 让 Agent 能更新 listing 和库存。可以设计一条端到端链路:根据销售数据和评论生成素材变体 → 自动上传到 Runway library → 人工挑片 → 通过的素材自动更新到 Amazon A+ Content / 主图视频。把创意和运营之间的手动交接压缩到最小。

### cross-0926-02 — 用 Gemini 3.8 Live Avatar + Qwen-Audio 3.1 做低成本多语言客服 Agent
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化
- Gemini 3.8 Live Avatar 提供企业级可视化语音 Agent 能力,Qwen-Audio 3.1 把语音 API 成本压到极低。可以组合出一条分层方案:用 Gemini Live Avatar 处理高价值/复杂客诉(可视化+工具调用),用 Qwen-Audio 处理标准化多语言 FAQ。这在跨境客服场景中尤其有成本优势。

## 本周表现摘要

- 周期: 2026-09-19 ~ 2026-09-26 | 发布量: 0
- 中位数曝光: 无数据
- 覆盖不足赛道: 🤖 AI 前沿, 🛒 AI 电商自动化, 🎨 创意广告
- 洞察: 本窗口内无真实发布数据,Phase 1 学习连续第二十五期空转。沿用 profile_longterm.md 长期约束与 profile_recent.md 近期判断。

## 系统建议

### 信息源
- 提升: AlphaSignal / AI Weekly / Kingy.ai 追踪器, Runway/Amazon/Google 官方博客
- 降级: 低可信度 AI 新闻聚合站(aitoolsrecap 等)在未交叉验证前不作为 must_read 唯一来源
- 新增: Docker skills GitHub(Agent 工具链), Buchodi 安全研究(隐私/归因)

### topic_library
- 建议新增: 视频模型迁移与多模型路由, Agent 权限设计与审计日志

### 定位漂移
- 连续三期 must_reads 高度围绕「Agent 接入基础设施」(MCP、plugin、AgentCore),需警惕 🤖/🛒/🎨 都退化为「Agent 工具链播报」。下期应补充至少 2 条「Agent 落地效果/ROI/失败案例」类素材,平衡基础设施与实际结果。

## 原始素材统计
- raw_material_count: 86
- fieldtheory_bookmarks: ok
- obsidian_wechat_favorites: dead
- web_search: ok
- web_fetch: partial
