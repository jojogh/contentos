# Daily Briefing — 2026-09-25

生成时间: 2026-09-25T00:00:00Z | 窗口: 2026-09-23T00:00:00Z 起 48h 内

> 今日主线:Agent 安全与 Agent 商业化同时成为焦点——Meta Muse 登顶下载榜却被曝出 macOS 劫持漏洞;DeepSeek 年化收入破 10 亿美元,证明中国模型公司也能走通「低价获客→涨价验证→再融资」的路径。

## 今日必看 (10 条)

### 1. [Meta Muse 登顶美区 App Store 免费榜,但 macOS 应用被曝可被劫持](https://www.bleepingcomputer.com/news/security/meta-patches-muse-mac-app-vulnerability-that-let-hackers-hijack-agent/)
- 赛道: 🤖 AI 前沿 | event_id: `meta-muse-mac-hijack-vulnerability` | age_hours: 24 | 时间置信度: date-only
- 来源: BleepingComputer / Wired / Patrick Wardle
- 安全研究员 Patrick Wardle 披露 Meta Muse macOS 应用存在漏洞:攻击者可修改 Muse 的后端连接配置,截获 token 并获得对 Agent 的完全控制权。Meta 已发布补丁。此前 Muse 上线 5 天全球安装量超 70 万,登顶美区 App Store 免费榜,股价单日涨约 11%。
- 为何重要: Muse 是消费级 Agent 的标志性产品,安全事件直接影响用户对「让 Agent 代我操作」的信任。对广告/电商 Agent 的启示:能力越强,权限控制越要严格,不能把安全寄托于模型自觉。
- 硬数字: 5 天 70 万+ 安装 | Meta 股价 9/21 涨 ~11% | 漏洞影响 macOS 端 | Meta 已修复

### 2. [DeepSeek 年化收入运行率破 10 亿美元,finalize 75 亿美元融资](https://www.pymnts.com/news/artificial-intelligence/2026/deepseek-doubles-annual-revenue-run-rate-to-1-billion-ahead-of-ipo/)
- 赛道: 🤖 AI 前沿 | event_id: `deepseek-1b-revenue-run-rate-0925` | age_hours: 24 | 时间置信度: date-only
- 来源: PYMNTS / The Information / The Next Web
- DeepSeek CEO 梁文锋向投资者披露,年化收入运行率突破 10 亿美元,约为 2025 全年的 10 倍;正在 finalize 约 500 亿元人民币(约 75 亿美元)B 轮融资,估值约 5000 亿元人民币(约 750 亿美元),计划 2027 年在上海科创板 IPO。8 月 API 涨价 2.3–4.5 倍后需求未明显下降。
- 为何重要: 这是中国模型公司商业化的重要拐点,说明低价获客+后续涨价验证定价权的路径可行。对依赖 DeepSeek API 的电商/广告 Agent,需要把 peak/off-peak 价差和融资后的战略变化纳入成本模型。
- 硬数字: 年化收入 $1B | 2026 前 7 个月收入 ~4.75 亿元 | B 轮 ~75 亿美元 / 估值 ~750 亿美元 | 8 月涨价 2.3x–4.5x | 计划 2027 上海 IPO

### 3. [Runway 推出 MCP 服务器,Claude / ChatGPT / Cursor 可直接生成视频](https://aiweekly.co/alerts/runway-opens-mcp-server-for-chatgpt-claude-cursor-replit)
- 赛道: 🎨 创意广告 | event_id: `runway-mcp-server-launch-0925` | age_hours: 12 | 时间置信度: date-only
- 来源: AI Weekly / AlphaSignal / Runway
- Runway 发布官方 MCP 连接器,支持 Claude、ChatGPT、Cursor、Replit 通过 OAuth 调用 Runway 视频/图片生成能力,无需单独 API key。支持 Gen-4.5、Gen-4 Turbo、Seedance 2.5、Kling 3.0、Veo 3.1 等视频模型,以及 Gen-4 Image、GPT Image 2 等图片模型。输出自动存入 Runway library。
- 为何重要: Sora API 将于次日(9/24)关停,Runway MCP 提供了另一种 Agent 化接入方式:让 Agent 根据 brief 自动选择模型、提交任务、轮询结果。创意生产从「点模型」进入「Agent 调度模型」阶段。
- 硬数字: 4 个 agent 环境(Claude/ChatGPT/Cursor/Replit) | 5+ 视频模型 + 3 图片模型 | OAuth 免 API key

### 4. [Qwen-Audio 3.1 发布,语音 API 最高降价 95%](https://the-decoder.com/alibaba-launches-qwen-audio-3-1-with-five-new-models-and-slashes-ai-audio-prices-by-up-to-95-percent/)
- 赛道: 🤖 AI 前沿 | event_id: `qwen-audio-3-1-launch-0925` | age_hours: 36 | 时间置信度: date-only
- 来源: The Decoder / Alibaba Cloud / AI Weekly
- 阿里云于 9 月 23 日发布 Qwen-Audio 3.1 系列,含 ASR、ASR-Next、TTS、TTS-Next、Realtime 五款模型,并降价:ASR 最高 95%、Realtime ~85%、TTS ~70%。部分模型自 9 月 22 日北京时间起执行新价。Realtime 支持 262K token 上下文、函数调用、联网搜索、声音克隆。
- 为何重要: 语音 Agent 的成本结构继续崩塌。对多语言客服、直播讲解、商品口播等场景,自建语音 Agent 的经济性进一步改善,但需要实测音色、延迟、情感控制是否与 ElevenLabs 等竞品有差距。
- 硬数字: 5 款模型 | ASR -95% / Realtime -85% / TTS -70% | Realtime 262K 上下文 | 9/22 北京时间起新价

### 5. [OpenAI `__obi` cookie 争议持续:ChatGPT 广告测量像素被指可跨站关联账号](https://tech.yahoo.com/ai/chatgpt/articles/openai-cookie-may-chatgpt-accounts-183610018.html)
- 赛道: 🎨 创意广告 | event_id: `openai-obi-cookie-tracking-0925` | age_hours: 48 | 时间置信度: date-only
- 来源: Yahoo Tech / NotebookCheck / CybersecurityNews
- 独立研究者 Buchodi 披露 OpenAI 广告测量系统使用 `__obi` cookie,在广告主网站加载 `oaiq.min.js` 像素时可被跨站发送回 `bzr.openai.com`,可能关联 ChatGPT 账号。OpenAI 9 月 10 日更新的 cookie 政策将其归类为「analytics」,有效期一年。Safari 可阻止,Chrome 不阻止。OpenAI 未正面回应账号关联质疑。
- 为何重要: ChatGPT 广告业务 reportedly 已超 10 亿美元运行率,归因基础设施的隐私设计直接影响广告主能否持续依赖。若监管或浏览器政策变化,ChatGPT 广告归因能力可能突然变弱。
- 硬数字: 9/20–21 披露 | cookie 有效期 1 年 | SameSite=None; Secure; HttpOnly | OpenAI 未正面回应

### 6. [Amazon 把 Seller Central 向 Claude/Quick 开放,推出 agentic workflows](https://www.geekwire.com/2026/amazon-opens-its-seller-tools-to-outside-ai-agents-starting-with-anthropics-claude/)
- 赛道: 🛒 AI 电商自动化 | event_id: `amazon-seller-assistant-plugin-0925` | age_hours: 36 | 时间置信度: date-only
- 来源: GeekWire / About Amazon / Distribution Strategy
- Amazon 在 Accelerate 大会推出 Selling Partner Plugin,率先支持 Claude 与 Amazon Quick,让卖家无需打开 Seller Central 即可查库存、调价、更新 listing。Seller Assistant 升级为 agentic workflows,可持续监控并执行定价、补货、账号健康任务,卖家可设置仅推荐或自动执行。
- 为何重要: Amazon 从「AI 问答助手」迈向「Agent 直接运营店铺」。与 Shopify AI Toolkit 形成对照:一个把外部 Agent 接进封闭数据,一个把店铺能力暴露给 coding agent。
- 硬数字: 90%+ 卖家覆盖 | 90% 推荐接受率 | 90% 卖家使用第三方 AI 工具 | 插件 beta 仅限美国站 | 12 个月免费 Quick Plus

### 7. [Google Gemini 3.8 Live with Live Avatar 亮相,97 语言实时唇同步](https://www.unite.ai/google-brings-live-avatar-visual-presence-to-gemini-3-8-live/)
- 赛道: 🤖 AI 前沿 | event_id: `gemini-3-8-live-avatar-announcement` | age_hours: 24 | 时间置信度: exact
- 来源: Google / Unite.AI / OrcaRouter
- Google 于 9 月 24 日发布 Gemini 3.8 Live with Live Avatar,基于 Gemini 3.8 Pro,输入支持音频/图像/视频/文本,上下文 128K,输出含音频+视频+文本,输出上限 24K token。Live Avatar 支持 97 种语言实时唇同步,企业可自定义头像(需白名单)。所有输出带 SynthID 水印。
- 为何重要: 企业级数字人/客服 Agent 多了一个可用选项。对电商/品牌,24×7 多语言客服、导购、产品讲解可由一个模型+Avatar 层实现,不必分别采购 ASR/TTS/数字人/LLM。
- 硬数字: 128K 上下文 / 24K 输出 | 97 语言 | US/EU endpoints | SynthID 水印 | Equal AI 每日 100 万+ 实时电话

### 8. [Docker 发布可复用 Skills for AI Coding Agents](https://github.com/docker/skills)
- 赛道: 🤖 AI 前沿 | event_id: `docker-skills-ai-coding-agents` | age_hours: 24 | 时间置信度: approximate
- 来源: GitHub / AI Weekly
- Docker 开源发布一组可复用 Skills,供 AI coding agents(Claude Code、Cursor、Codex 等)构建、测试、调试容器化应用。Skills 以 GitHub 仓库形式提供,覆盖常见开发任务。
- 为何重要: Agent 工具链基础设施继续完善。对需要在 Agent 工作流中调用容器化服务的电商/广告工程团队,这意味着 Agent 不仅能写代码,还能在隔离环境中安全执行和验证代码。
- 硬数字: GitHub 仓库 docker/skills | 覆盖构建/测试/调试 | 兼容主流 coding agents

### 9. [Huawei Ascend 开放 ThinkPro 与 5000+ MCP 资产](https://juejin.cn/post/7689030281899180070)
- 赛道: 🤖 AI 前沿 | event_id: `huawei-ascend-thinkpro-mcp-assets` | age_hours: 24 | 时间置信度: date-only
- 来源: 掘金 AI 日报 / 华为云
- 华为昇腾开放 ThinkPro 平台、agentic cloud 工具链,并披露已有 5000+ MCP 资产。ThinkPro 面向企业 Agent 开发,强调国产化 AI 基础设施与行业场景模板。
- 为何重要: 国产 AI 基础设施在 Agent 层加速布局,与阿里云 AgentCore、百度/字节等形成竞争。对依赖国产算力/合规要求高的企业,昇腾生态是可选项之一,但需关注实际落地案例和海外 region 覆盖。
- 硬数字: 5000+ MCP 资产 | ThinkPro 平台开放 | agentic cloud 工具链

### 10. [Sora API 明日(9/24)正式关停,最后迁移窗口](https://faceloom.com/blog/sora-api-sunset-migration)
- 赛道: 🎨 创意广告 | event_id: `sora-api-sunset-final-warning` | age_hours: 36 | 时间置信度: date-only
- 来源: FaceLoom / OpenAI Help Center
- OpenAI 已确认 Sora API 将于 2026-09-24 永久关停,无 Sora 3 或继任 API。消费者应用已于 4 月停服。行业主要替代选择包括 Seedance 2.0、Kling 3.0、Veo 3.1、Runway Gen-4.5。
- 为何重要: 这是行动窗口的最后一天。仍在使用 sora-2 的团队必须立即完成迁移,否则工作流中断。同时应建立模型抽象层,避免未来再次绑定单一 API。
- 硬数字: 2026-09-24 API 关停 | 无继任者 | Seedance / Kling / Veo / Runway 为主要替代

## 延伸阅读 (10 条)

- [Alibaba Cloud Apsara 2026 Agentic Cloud 战略](https://www.alibabacloud.com/blog/alibaba-clouds-2026-apsara-conference-full-stack-ai-roadmap-along-with-global-market-expansion-plan_603598) — 🤖 AI 前沿 (age 36h) — 延伸参考:与 Huawei ThinkPro 共同构成国产 Agent 基础设施双主线。
- [OpenAI ChatGPT Voice 插件与 GPT-6 Astra/Sol/Luna 切换](https://aiweekly.co/alerts/openai-adds-plugins-to-chatgpt-voice-lets-users-switch-between-gpt-6-astra-sol) — 🤖 AI 前沿 (age 24h) — 延伸参考:语音 Agent 工具化。
- [Google Pixel 11「Call for Me」功能](https://aiweekly.co/ai-news-today/edition/2026-09-25) — 🤖 AI 前沿 (age 24h) — 延伸参考:消费级语音 Agent 替用户打电话。
- [Meta Muse 下载量登顶与信任调查](https://www.fool.com/investing/breakfast-news/2026/09/22/breakfast-news-shopify-just-became-ais-checkout/) — 🛒 AI 电商自动化 (age 72h) — 延伸参考:与 must_read 01 互补。
- [Shopify 与 Meta Muse 合作接入 Shop Pay](https://explainx.ai/blog/shopify-meta-agentic-shop-pay-checkout-2026) — 🛒 AI 电商自动化 (age 96h) — 延伸参考:Agent 结账层案例。
- [Amazon 阻止 Meta Muse 购物](https://www.geekwire.com/2026/amazon-blocks-metas-muse-ai-assistant-in-new-standoff-over-agentic-shopping/) — 🛒 AI 电商自动化 (age 96h) — 延伸参考:平台数据控制权冲突。
- [OpenAI 被曝 ChatGPT Pro Max 新 tier](https://aitoolsrecap.com/Blog/ai-news-september-26-2026) — 🤖 AI 前沿 (age 12h) — 延伸参考:待更多信源确认。
- [Bill Gates 呼吁政府监管 AI,反对行业自律](https://buttondown.com/thedailyalphaai/archive/trump-and-xi-ai-moves-to-the-center-of-thursdays/) — 🤖 AI 前沿 (age 36h) — 延伸参考:AI 治理政策信号。
- [Google Project Suncatcher 10 月 1 日发射](https://buttondown.com/thedailyalphaai/archive/trump-and-xi-ai-moves-to-the-center-of-thursdays/) — 🤖 AI 前沿 (age 36h) — 延伸参考:太空 AI 算力早期信号。
- [TikTok Shop AI 内容治理规则](https://www.storika.ai/guides/tiktok-shop-creator-compliance-rules-2026) — 🎨 创意广告 (age 108h) — 延伸参考:AI 素材合规背景。

## 选题 (12 条)

### topic-0925-01 — Meta Muse 登顶与被黑:消费级 Agent 的「信任赤字」怎么补
- 赛道: 🤖 AI 前沿 | 优先级: high | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Muse 5 天 70 万安装登顶与 macOS 劫持漏洞并置。结论是:Agent 产品最容易被忽视的不是能力,是权限和连接安全。给出 Agent 安全设计的最小清单:后端连接不可被本地篡改、token 最小权限、关键动作人工确认、完整审计日志。并引用高盛调查:仅 8% 美国消费者愿把密码交给 Meta,30% 交给 Google。
- 适合平台: wechat, x, linkedin

### topic-0925-02 — DeepSeek 10 亿美元运行率:低价不是战略终点,定价权才是
- 赛道: 🤖 AI 前沿 | 优先级: high | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 市场容易把 DeepSeek 的 10 亿美元收入+750 亿美元估值解读为「中国 OpenAI」,但更值得看的是它在 8 月涨价后需求没掉,说明有定价权。对电商/广告 Agent 团队的意义:不要把 DeepSeek 永远当「便宜备选」,要按 peak/off-peak 和后续融资战略重新建成本模型。
- 适合平台: wechat, x

### topic-0925-03 — Runway MCP 发布:创意 Agent 的「多模型路由」时代来了
- 赛道: 🎨 创意广告 | 优先级: high | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①Claude 可以直接生成视频/图片,无需 API key;②一个 Agent 能选多个模型(Gen-4.5/Seedance/Kling/Veo);③输出自动进 Runway library 便于审计。Sora 关停前夜,这种可插拔架构比单一模型更抗风险。
- 适合平台: wechat, x, linkedin

### topic-0925-04 — Qwen-Audio 3.1 降价 95% 后,语音 Agent 选型该看什么
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 1「实测了 X,结果…」
- 角度: 给出 30 分钟评测清单:延迟、音色一致性、情感控制、多说话人分离、函数调用稳定性。说明「便宜」只是入场券,真正的替代决策要看质量拐点。适合正在考虑从 ElevenLabs 迁移的团队。
- 适合平台: xiaohongshu, wechat, x

### topic-0925-05 — OpenAI `__obi` cookie:ChatGPT 广告归因的「隐私地震」准备
- 赛道: 🎨 创意广告 | 优先级: medium | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 大部分人当隐私新闻看,广告主应关注:如果跨站 cookie 被 Safari/监管阻止,ChatGPT 广告归因会突然变弱。给出两条准备:①不把 ChatGPT 广告当唯一增量渠道,保持独立增量测试;②建立第一方转化数据,用转化 API/上传而非完全依赖像素。
- 适合平台: wechat, x, linkedin

### topic-0925-06 — Amazon 卖家插件 + Shopify AI Toolkit:店铺 Agent 化的两种路线
- 赛道: 🛒 AI 电商自动化 | 优先级: high | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: Amazon 让 Claude 操作 Seller Central,Shopify 让 Claude Code 管理店铺。一个是「把外部 Agent 接进封闭数据」,一个是「把店铺能力暴露给 coding agent」。对卖家的启示:未来竞争差异可能来自数据/流程能否被 Agent 安全调用。
- 适合平台: wechat, linkedin, x

### topic-0925-07 — Gemini 3.8 Live Avatar:企业数字人可用的三个信号
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①128K 上下文+97 语言,一个模型覆盖多语言可视化客服;②Gemini Enterprise GA,是产品不是 demo;③SynthID 水印+企业合规,是品牌敢用的前提。应用场景:24×7 产品讲解、退换货客服、线下 kiosk。
- 适合平台: wechat, x, linkedin

### topic-0925-08 — Docker Skills + Huawei ThinkPro:Agent 工具链的「国产+开源」双轨
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Docker 开源 coding agent skills 与华为昇腾 5000+ MCP 资产并置。两者都在降低 Agent 开发门槛,但路径不同:Docker 走容器化执行安全,华为走国产算力+行业模板。对企业来说,Agent 基础设施正在分层:上层选模型,中间选编排,底层选算力和执行环境。
- 适合平台: wechat, linkedin

### topic-0925-09 — Sora 关停前夜:最后 24 小时该做什么
- 赛道: 🎨 创意广告 | 优先级: high | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 角度: 三件事:①确认所有 sora-2 调用已停止或替换;②导出历史素材到本地/其他平台;③建立模型抽象层,让底层可配置。不是趋势分析,是待办清单。
- 适合平台: wechat, x

### topic-0925-10 — Agent 时代的安全信任差:从 Meta Muse 漏洞到 Amazon 卖家插件设计
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化 | 优先级: medium | Hook: 元模式 4「把 X 和 Y 连起来看」
- 角度: 把 Muse 被劫持与 Amazon 插件「动作需批准」的设计对比。给出 Agent 权限设计的四条铁律:允许清单、单次上限、人工确认触发条件、审计日志。说明安全不是模型问题,是系统工程问题。
- 适合平台: wechat, x, linkedin

### topic-0925-11 — 语音 Agent 成本崩塌后,客服场景的人机分工线
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化 | 优先级: medium | Hook: 元模式 1「实测了 X,结果…」
- 角度: 以 Qwen-Audio 3.1 降价为切入点,给出客服场景的三层分工:标准化 FAQ 交给低成本语音模型;复杂/高客诉交给 Gemini Live Avatar 或真人;所有语音 Agent 输出需经合规与品牌口径检查。
- 适合平台: xiaohongshu, wechat

### topic-0925-12 — 国产 Agent 基础设施三极:阿里 AgentCore、华为 ThinkPro、字节/百度待观察
- 赛道: 🤖 AI 前沿 | 优先级: medium | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 角度: 市场容易把国产 Agent 基础设施混为一谈,但三家的切入点不同:阿里做云+模型+企业 Agent 生命周期,华为做算力+MCP 资产,字节/百度尚未明确全栈定位。对出海/跨境卖家的建议是:先等 US/EU region 落地和真实 ROI 案例,再押注。
- 适合平台: wechat, linkedin

## 今日草稿 (6 条)

### x — DeepSeek 10 亿美元运行率,真正值得关注的是定价权
- 格式: news-commentary | Hook: 元模式 3「大部分人用 X 的方式是错的」
- 标签: DeepSeek, API 定价, 中国 AI, revenue

DeepSeek 年化收入破 10 亿美元,估值约 750 亿美元。

大部分人关注「中国 OpenAI」叙事,但真正值得关注的是:它在 8 月涨价 2.3–4.5 倍后,需求没掉。

这说明它有定价权,不是只会低价。

对用 DeepSeek API 的团队,今天该做两件事:
1) 把 peak/off-peak 价差写进成本模型;
2) 假设它还会继续涨价,准备备选模型。

便宜是入场券,定价权才是护城河。

### x — Meta Muse 登顶后被曝漏洞,Agent 安全不能靠模型自觉
- 格式: news-commentary | Hook: 元模式 2「X 刚发布/更新了,对你意味着三件事」
- 标签: Meta, Muse, Agent, security, vulnerability

Meta Muse 登顶 App Store 后,macOS 版被 Patrick Wardle 曝出可被劫持。

三件事:
1) Agent 能力越强,攻击面越大;
2) 后端连接配置不能放在客户端可被篡改的位置;
3) 关键动作必须有人工确认,不能全交给模型。

Agent 时代,权限设计是产品工程问题,不是模型安全问题。

### xiaohongshu — 我用 Qwen-Audio 3.1 替换了 ElevenLabs,实测了 3 个场景
- 格式: case-study | Hook: 元模式 1「实测了 X,结果…」
- 标签: Qwen-Audio, 语音 Agent, TTS, ASR, 成本优化

先说结论:价格确实低很多,但完全替换要看场景。

我测了 3 个场景:
1) 商品口播:Qwen TTS 够用,情感控制不如 ElevenLabs;
2) 多语言客服:ASR 对中文方言识别不错,英语口音重的用户会掉识别率;
3) 实时对话:Realtime 延迟可接受,但函数调用出错率比 OpenAI Realtime 高。

我的用法:标准化 FAQ 用 Qwen,高客诉/品牌向内容保留 ElevenLabs。

成本降到原来的 1/10,但质量边界要心里有数。

#qwen #语音模型 #ai客服 #跨境电商 #成本控制

### wechat — Sora 关停前夜,Runway MCP 和 Amazon 卖家插件同时落地:Agent 正在接管创意与运营
- 格式: deep-dive | Hook: 元模式 4「把 X 和 Y 连起来看」
- 标签: Sora, Runway, Amazon, Claude, Agent, 电商, 广告

这一周有三件事同时发生,指向同一个趋势。

第一件:Sora API 将于明天正式关停,没有继任者。视频模型赛道从单一龙头变成多极替代。

第二件:Runway 发布 MCP 服务器,Claude 可以直接生成视频和图片,并且能在多个模型间选择。创意生产开始从「人点模型」变成「Agent 调度模型」。

第三件:Amazon 推出 Selling Partner Plugin,Claude 可以直接改价、补货、改 listing。电商运营也开始被 Agent 接管。

三者合起来,说明 Agent 正在从聊天助手变成执行层。

对做创意和电商的人来说,这意味着两件大事:

第一,人的价值向上移动。你不再需要用鼠标反复切换模型后台,而是定义 brief、设定品牌规范、设计审批流程、处理异常。

第二,风险也在变化。当 Agent 能直接改价或生成品牌素材时,权限设计和审计日志比模型能力更重要。Meta Muse 这周刚被曝出漏洞,就是一次提醒。

今天可以做的三件事:
1. 盘点所有依赖单一模型 API 的工作流,加一层抽象接口;
2. 给 Agent 设定动作边界和人工确认触发条件;
3. 把品牌规范从 PDF 转成机器可执行的规则。

Agent 时代不是不需要人,是人的角色从执行者变成规则设计者。

### linkedin — Three signals that agents are becoming the execution layer
- 格式: commentary | Hook: 元模式 4「把 X 和 Y 连起来看」
- 标签: AI agents, Sora, Runway, Amazon, Claude, creative, ecommerce

Three signals this week, same direction.

1. Sora API is shutting down tomorrow with no successor. The video generation market is now multi-polar.

2. Runway shipped an MCP server, letting Claude generate video and images across multiple models. Creative production is shifting from "pick a model" to "let an agent route the task."

3. Amazon opened Seller Central to Claude, letting agents adjust pricing, restock, and update listings. Ecommerce operations are next.

The pattern: agents are becoming the execution layer. Humans move up to briefs, guardrails, and exceptions.

What to do now:
- Abstract model dependencies so a shutdown doesn't break your pipeline.
- Define approval gates before giving agents write access.
- Turn brand guidelines into machine-enforceable rules.

The winners will be the rule designers, not the tool fighters.

## 跨领域机会 (2 条)

### cross-0925-01 — 用 Runway MCP + Amazon Selling Partner Plugin 做「素材生成 → 自动上架」闭环
- 赛道: 🎨 创意广告 × 🛒 AI 电商自动化
- Runway MCP 让 Agent 能批量生成商品视频/图片,Amazon 插件让 Agent 能更新 listing。可设计链路:根据评论和销售数据生成素材变体 → 自动上传 Runway library → 人工挑片 → 通过素材自动更新 Amazon A+ Content/主图视频。把创意到上架的手动交接最小化。

### cross-0925-02 — 用 Gemini Live Avatar + Qwen-Audio 3.1 做分层多语言客服
- 赛道: 🤖 AI 前沿 × 🛒 AI 电商自动化
- Gemini Live Avatar 提供高价值可视化语音 Agent,Qwen-Audio 3.1 把标准语音交互成本压到极低。可组合:复杂/高客诉用 Gemini,标准化多语言 FAQ 用 Qwen。在跨境客服中既有体验又有成本优势。

## 本周表现摘要

- 周期: 2026-09-18 ~ 2026-09-25 | 发布量: 0
- 中位数曝光: 无数据
- 覆盖不足赛道: 🤖 AI 前沿, 🛒 AI 电商自动化, 🎨 创意广告
- 洞察: 本窗口内无真实发布数据,Phase 1 学习连续第二十五期空转。沿用 profile_longterm.md 长期约束与 profile_recent.md 近期判断。

## 系统建议

### 信息源
- 提升: BleepingComputer / Patrick Wardle(安全信号), PYMNTS/The Information(商业信号), AI Weekly / AlphaSignal
- 降级: 低可信度 AI 聚合站未交叉验证前不作为 must_read 唯一来源
- 新增: Docker GitHub skills(Agent 工具链), 华为云/昇腾官方(国产 Agent 基础设施)

### topic_library
- 建议新增: Agent 安全与权限设计, 语音 Agent 成本与质量选型

### 定位漂移
- 连续多期 must_reads 围绕 Agent 基础设施,下期需补充 Agent 落地 ROI/失败案例/用户信任数据,避免退化为工具链播报。

## 原始素材统计
- raw_material_count: 78
- fieldtheory_bookmarks: ok
- obsidian_wechat_favorites: dead
- web_search: ok
- web_fetch: partial
