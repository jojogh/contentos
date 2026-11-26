# ContentOS Daily Briefing -- 2026-11-26

- generated_at: 2026-11-26T14:29:19.353279Z（America/New_York：2026-11-26 09:29 EST）
- pass: thanksgiving-9am-ET-refresh-no-BDC-post-researchy
- raw_material_count: 433（RSS 窗内去重 384 + 官方索引页 21 + 打开文章/帮助页约 28；Typefully/Exa 跳过；未调用 X search_news，避免昨日同窗 429；Channel D 停用）
- channel_d: disabled_by_alex_2026-11-03 · D4=1
- must_reads: 12 · also: 12 · topics: 4 · drafts: 3

## 发布策略

今日是感恩节（America/New_York），黑五周 11/19–11/30 的第八天，明天 11/27 黑五。市场快照抓取时（约 9:18am ET）美股字段均为 marketState=closed，NVDA 149.30 / SHOP 133.40 应视为周三收盘，不是周四开盘价。BTC 约 60807（24h +4.33%），Crypto F&G 仍为 9（Extreme fear），CNN F&G=15，btcScore=22.3，ETF 每日净流入约 -4.53 亿。优先发 AI Max text guidelines / 不必关闭即可控的官方控件（帮助页已核），其次 Merchant Center local promotions 必须店内核销（官方政策页已核），以及 Shopify 11/25 拒付包。Google 家族今日 2/2 满额；代理 Ads opportunities 与促销抵扣 42 天只进必读或延伸。D4=1：Grok Bot changelog 首次出现 v1.3.0（昨日 9:31 ET 仍为 v1.2.3）。不要把 Muse 谈判或英国监管测试写成已恢复/已下架。Channel D 停用。不要自动发帖。

## 今日选题

### 1. Google Ads AI Max for Search：用 text guidelines 和定向控件，不必先关掉 AI Max

- theme_slug: `google-ads-aimax-text-guidelines-controls-without-off-1126`
- admission: a+c · heat: high · format: 方法论
- tracks: 🎨 创意广告, 🛒 AI 电商自动化
- tags: 平台可改字段
- angle: 本轮已打开四份官方帮助页（15910187 / 16489313 / 16738708 / 16230205），PPC Times 把帮助页改句记在 11/26。黑五前不要先把 AI Max 或 text customization 整段关掉。官方把 text guidelines 列为 campaign-level control：term exclusions（精确词或短语，每战役最多 25 条，不区分大小写、按语言生效）和 messaging restrictions（避免的说法）；该页标注 experimental beta。若生成文案出现了你不能承诺的折扣词或竞品词，先写 guidelines，或在 Assets 用 Added by: Google AI 筛掉单条素材。拦截不想要的检索词用否定关键词、品牌排除，或在广告组 Settings > AI Max 关闭 Search term matching。拦截落地页用 Campaigns > Settings > AI Max 的 URL exclusions，但官方写明它只约束 Final URL expansion 自动选的页面；带静态 Final URL 的 RSA 和手动 sitelink 仍会指向被排除 URL，必须另外改或删除。官方也写明不必为此改成 Manual CPC。30 分钟动作：1）打开仍在跑的 AI Max Search 战役，先加今年不能出现在广告里的词（例如免费赠品、未达标的折扣幅度）。2）Assets 里按 Added by: Google AI 抽查节日文案。3）对照已做的 URL 排除，检查 RSA 静态 Final URL 与手动 sitelink。不要把 beta 写成已全量法定强制。
- reasoning: 命中 Admission (a)(c)：text guidelines、URL exclusions、Added by: Google AI 素材过滤、广告组 Search term matching 都是 30 分钟可改控件。platform_family: Google（今日 1/2）。官方帮助页已打开，不是只转述二手稿。未出现在昨日 topics[]（昨日为 12 市场 schema.org 促销标与 12 月核心更新预告）。非 MCP。黑五前生成文案风险高。Bingge 评分≥70。

### 2. Merchant Center：所有 local promotions 必须可在店内核销

- theme_slug: `google-mc-local-promotions-redeemable-instore-1126`
- admission: a+c · heat: high · format: 合规
- tracks: 🛒 AI 电商自动化
- tags: 平台可改字段
- angle: 本轮已打开官方《Promotions policies》。在 local promotions 一节，Google 新增 Note：为保证体验，所有 local promotions 必须可在店内核销。PPC Times 监测于 11/26 发现该句，此前同节只有 Promotion URL（同一网站上的促销详情与核销细则）以及 curbside pickup 须在促销页写明「线上核销、到店取货」。官方没有写生效日、如何执法，也没有解释只做 curbside、不能进店核销的促销怎么处理。在说清楚之前，只做线上或只做 curbside 的本地促销有被拒的风险。30 分钟动作：1）在 Merchant Center 列出进行中的 local promotions。2）确认每条都能在店内核销，并在 promotion URL 页写明。3）给门店同事同步代码或条件。4）盯促销状态里是否出现引用 promotions policies 的拒登。这条只适用于做 local inventory / 本地促销的零售商和代理，不要写成所有 Shopping 卖家的新义务，也不要和昨日 12 市场 schema.org 促销标要求混成同一件事。
- reasoning: 命中 Admission (a)(c)：local promotions 的核销方式与促销页文案是可改字段，30 分钟能在 Merchant Center 核对并改页。platform_family: Google（今日 2/2）。官方页已打开。与昨日 schema.org 双价格、12 月核心更新是不同 theme_slug。非 MCP、非 D4。受众窄（有门店/本地库存的零售），但政策句是硬的，故保留；未为凑数再塞代理 Ads opportunities（只进必读）。Bingge 评分≥70。

### 3. Shopify 拒付包：全原因 AI 答辩 + 自动支付验证 + Agentic 订单授权记录 + 员工通知

- theme_slug: `shopify-chargeback-ai-defense-all-reasons-staff-notify-1126`
- admission: a+c · heat: high · format: 方法论
- tracks: 🛒 AI 电商自动化
- tags: 平台可改字段, 商家数字
- angle: Shopify 官方 changelog 在 11/25 中午 ET 连发四条，都已打开。AI 书面答辩从「仅限未收到货」扩到主要拒付原因，默认带上 Include Shopify-generated insights to strengthen case (recommended)，提交前可取消勾选。未授权/欺诈类会自动附 CVV/AVS、授权码、可用的 3DS、线下 EMV/收据，以及符合 Visa Compelling Evidence 3.0 的历史未争议订单，无需你自己找这些支付证据。若订单来自 AI 购物助手，响应会自动加上 Payment authorization record（助手消费限额、结账批准、已知助手名），这正好接上本周已出现的 ChatGPT agentic checkout——今日不复用那个 slug，只把新证据当作新动作。通知方面：Settings > Notifications > Staff notifications 的 Order dispute updates 可发给有争议权限的员工；新店默认开，老店默认只给店主。30 分钟动作：1）打开员工通知，把拒付给实际处理争议的人，而不是只留给店主在旅途中才看到。2）走一遍证据表单，决定默认是否保留 Shopify AI insights。3）抽几笔 agentic / ChatGPT 订单，确认授权记录会出现在争议材料里。不要把自动附件写成「一定能赢下黑五拒付」。
- reasoning: 命中 Admission (a)(c)：员工通知开关、证据表单勾选、对 Agentic 订单证据的核对都是 30 分钟动作。platform_family: Shopify（今日 1/2）。官方 changelog 已打开。未复用昨日/本周 shopify-chatgpt-agentic-checkout-default-on 脊柱；angle 是争议证据与通知，属新 class（compliance/流程）。非 MCP。黑五周拒付上升，时效强。Bingge 评分≥70。

### 4. Grok Bot v1.3.0：给售罄商品开 Notify me，并核对 Slack 交接与组织域名限制

- theme_slug: `grok-bot-1-3-0-restock-alerts-slack-handoff-domain-controls-1126`
- admission: a · heat: medium · format: 配置
- tracks: 🤖 AI 前沿, 🛒 AI 电商自动化
- tags: 平台可改字段
- angle: 本轮打开 x.ai/changelog/bot，最新是 v1.3.0（页上日期 November 24, 2026）。昨日 9:31 ET 简报仍记录该页为 11/18 的 v1.2.3，所以这是今日第一次在 live 页上看到该版本。和电商最直接的一句：售罄商品卡提供 Notify me，会监视该商家并在补货后通知你。不要写成已经对接 Amazon Seller Central 库存 API。团队向的配置还有：跨 Bot 交接的答复回到你的 Slack 私信并带 Connect 按钮；组织可限制成员只连接本组织域名下的账户；邮件草稿可加 Bcc。30 分钟动作：1）确认客户端已是 1.3.0。2）拿一件售罄商品走一遍 Notify me，看监视对象是不是你以为的那家店。3）若是团队账号，打开组织域名限制，避免个人邮箱乱接。4）若用 Slack 多 Bot 交接，确认回传落在你的 DM，而不是把私聊内容公开到频道（官方写明私密对话中的消息会留在该对话）。方向是 D4「配置 + Grok Bot×电商运营」，不是生活 MCP 清单。
- reasoning: 命中 Admission (a)：版本确认、Notify me 实测、组织域名限制、Slack 回传位置都是 30 分钟可执行。platform_family: xAI/Grok Bot（今日 D4 1/2）。官方 changelog 已打开。昨日 D4=0 是因为当时页上仍是 v1.2.3，不与昨日 slug 冲突。非目录炫技，不写融资。Bingge 评分≥70。

## 今日必看

### 1. [Merchant Center 促销政策新增：所有 local promotions 必须可在店内核销](https://support.google.com/merchants/answer/2877565?hl=en)

- event_id: `google-mc-local-promotions-redeemable-instore-1126` · track: 🛒 AI 电商自动化 · source: Google Merchant Center Help
- published_at: 2026-11-26T11:42:58Z · age_hours: 3
- matched_topic: 平台促销政策可改字段
- summary: 本轮已打开官方《Promotions policies》（answer/2877565）。页面现有原文：“To ensure a seamless customer experience, all local promotions must be redeemable in-store.” PPC Times 帮助页监测于 2026-11-26 捕捉到这条新 Note；此前该节只有 Promotion URL 与 curbside pickup 说明。官方未写生效日或如何执法。与「curbside pickup 须在促销页写明 online redemption」并列，只做线上或只做 curbside 的本地促销可能不符合政策。30 分钟：在 Merchant Center 列出进行中的 local promotions，确认每条都能店内核销，并把核销说明写进 promotion URL 页。（官方页已打开）
- supporting:
  - [PPC Times 11/26：帮助页监测首次看到 in-store Note，并提醒 curbside-only 可能被拒](https://ppctimes.com/news/merchant-center-local-promotions-redeemable-in-store)
  - [《Local promotions basics》说明本地促销挂在 local inventory ads 的 special offer 链上](https://support.google.com/merchants/answer/15582436?hl=en)

### 2. [Google Ads 帮助页为 AI Max for Search 补上 text guidelines，并说明不必关闭 AI Max 也能控词、落地页和素材](https://support.google.com/google-ads/answer/15910187?hl=en)

- event_id: `google-ads-aimax-text-guidelines-controls-1126` · track: 🎨 创意广告 · source: Google Ads Help
- published_at: 2026-11-26T11:41:59Z · age_hours: 3
- matched_topic: AI 广告文案与平台控件
- summary: 本轮已打开《How AI Max for Search campaigns works》（answer/15910187）、《Use text guidelines…》（answer/16489313，标为 experimental beta）、《Turn text customization on or off》（answer/16738708）和《About Final URL expansion in Search》（answer/16230205）。AI Max 功能列表现把 text guidelines 写成 campaign-level control：term exclusions（精确词/短语，官方写每战役最多 25 条）和 messaging restrictions（避免的说法）。新答疑写明：不需要关闭 AI Max，也不需要把 Smart Bidding 改成 Manual CPC，就可以用否定关键词 / 品牌排除 / 关闭某广告组 Search term matching、在 Campaigns > Settings > AI Max 做 URL exclusions、或用 text guidelines / 在 Assets 里按 Added by: Google AI 筛选后移除素材。URL exclusions 只作用于 Final URL expansion 自动选的落地页；Ads 表里带静态 Final URL 的 RSA，以及手动 sitelink，仍会指向被排除的 URL，除非你另外改或删。PPC Times 监测把帮助页改句记在 11/26。（官方页已打开）
- supporting:
  - [PPC Times 11/26：三份 AI Max 帮助页改句，以及 URL exclusions 不覆盖静态 Final URL / 手动 sitelink 的提醒](https://ppctimes.com/news/google-ads-ai-max-controls-without-turning-off)
  - [Text guidelines 帮助页（beta）：须先打开 text customization；term exclusions 不区分大小写、按语言生效，每战役最多 25 条](https://support.google.com/google-ads/answer/16489313?hl=en)
  - [Final URL expansion 官方说明：排除项只约束自动选页；静态 RSA Final URL 与手动 sitelink 仍会投放](https://support.google.com/google-ads/answer/16230205?hl=en)
  - [关闭/细化 text customization：可用 text guidelines，或在 Assets 用 Added by: Google AI 批量移除](https://support.google.com/google-ads/answer/16738708?hl=en)

### 3. [Shopify 11/25 changelog：所有拒付原因都可附 AI 答辩，并自动补支付验证与 Agentic 订单证据](https://changelog.shopify.com/posts/get-ai-written-responses-for-every-chargeback-reason)

- event_id: `shopify-chargeback-ai-defense-all-reasons-1125` · track: 🛒 AI 电商自动化 · source: Shopify Changelog
- published_at: 2026-11-25T17:00:00Z · age_hours: 21
- matched_topic: 订单争议与 agentic checkout 证据
- summary: Shopify Changelog 四条均标 November 25, 2026（RSS 时间为 12:00 America/New_York）。此前 AI 答辩只覆盖 product not received；现在对各类卡组织拒付原因都会根据你提交的证据和自动附件写 defense，默认勾选 Include Shopify-generated insights to strengthen case (recommended)，可不选。未授权/欺诈类拒付会自动附上 CVV/AVS 与授权码、支持你的 3D Secure 结果、线下支付的 EMV 与收据，以及符合 Visa Compelling Evidence 3.0 的既有未争议订单。Agentic 订单（AI 购物助手代下单）会自动附上 Payment authorization record：助手消费限额、结账时的支付批准、以及已知的助手名称。另可在 Settings > Notifications > Staff notifications 里用 Order dispute updates，把开案/升级/胜诉/败诉通知给有争议管理权限的员工；新店默认打开，老店默认只给店主。黑五周拒付会上来，这些是可改通知与表单选项，不是自动胜诉保证。
- supporting:
  - [未授权拒付自动附支付验证与 Visa CE 3.0 历史订单](https://changelog.shopify.com/posts/fraud-and-unauthorized-chargebacks-now-include-payment-verification-proof)
  - [Agentic 订单自动附助手消费限额与结账批准记录](https://changelog.shopify.com/posts/get-more-evidence-for-chargebacks-on-agentic-orders)
  - [员工通知：Settings > Notifications > Staff notifications > Order dispute updates](https://changelog.shopify.com/posts/choose-which-staff-get-chargeback-notifications)

### 4. [Grok Bot changelog 现为 v1.3.0：缺货 Notify me、Slack 跨 Bot 回传、组织域名限制](https://x.ai/changelog/bot)

- event_id: `grok-bot-1-3-0-changelog-1126` · track: 🤖 AI 前沿 · source: x.ai changelog/bot
- published_at: 2026-11-25T14:45:00Z · age_hours: 24
- matched_topic: Grok Bot 配置与电商补货提醒
- summary: 本轮打开 https://x.ai/changelog/bot ，最新版本为 v1.3.0，页面日期写作 November 24, 2026。昨日 2026-11-25 09:31 ET 简报抓取时该页仍为 11/18 的 v1.2.3，因此本次是首次在 live changelog 上看到 1.3.0；published_at 取昨日简报之后（不把页上的 11/24 00:00 UTC 当作已出窗）。官方新能力包括：售罄商品卡提供 Notify me，监视该商家并在补货时通知；跨 Bot 交接的答复回到你的 Slack 私信，并带 Connect 按钮；组织可限制成员只连接本组织域名下的账户；邮件草稿支持 Bcc；可连接 Ashby 回答招聘问题。不要把它写成 Seller Central 官方库存 API。这是配置 / Grok Bot×电商运营向的 D4 素材。
- supporting:
  - [Syntorak 11/26 早报转述同一 1.3.0 变更（Slack 回传、Notify me、组织域名、Ashby、Bcc）](https://www.syntorak.com/ai-news/2026-11-26)

### 5. [Merchant Center 面向代理的 Ads opportunities 页：集中看未进广告计划与低流量商品](https://support.google.com/merchants/answer/16580507?hl=en)

- event_id: `google-mc-ads-opportunities-agencies-1125` · track: 🛒 AI 电商自动化 · source: Google Merchant Center Help
- published_at: 2026-11-25T16:44:00Z · age_hours: 22
- matched_topic: Merchant Center 广告覆盖缺口
- summary: 本轮已打开官方《About Merchant Center for Agencies》（answer/16580507）。Ads opportunities page 为代理汇总客户商品：Products that won’t show in ads（默认突出「除了还没进广告计划外无其他问题」的商品，也可展开看其他导致无法展示的问题），以及 Low traffic products（可用 Low price / Trending brand 等过滤，并可打自定义标签以便在 Google Ads 里优化）。Search Engine Land 于 11/25 11:44 报道该页，并写到 28 天覆盖变化与 Ready for campaign 过滤；官方页确认了「不会在广告中展示」和「低流量」两份报告，未在摘录中看到独立的 Last updated 时间戳。仅限管理他人 Merchant Center 的代理（须已关联至少一个有效账户），不要写成普通卖家后台新页。今日不占选题席（Google 家族已用满 2 条硬题）。
- supporting:
  - [Search Engine Land 11/25 11:44：代理视图新增 Ads opportunities tab 的报道](https://searchengineland.com/google-merchant-center-adds-ads-opportunities-tab-for-agencies-503043)

### 6. [OpenAI：合并 Chat 与 Work 用量后，重度用户会更快碰到上限](https://techcrunch.com/2026/11/25/openai-says-heavy-chatgpt-users-may-hit-limits-sooner-as-it-merges-chat-and-work/)

- event_id: `openai-chatgpt-chat-work-shared-limits-1125` · track: 🤖 AI 前沿 · source: TechCrunch
- published_at: 2026-11-25T20:03:27Z · age_hours: 18
- matched_topic: 模型用量与工作流成本
- summary: TechCrunch 11/25 报道，OpenAI 将把 ChatGPT 的 Chat 与 Work 用量限额合并，两边都用得频繁的用户会更快用完共享额度；用尽后 Instant 仍可用，更广的推开计划在 12 月。这是产品用量规则，不是广告后台开关。不要写成全量已生效或所有套餐同日切换。
- supporting:
  - [The Neuron 11/26 早报同步了共享额度与 12 月更广推开的说法](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-26-2026/)

### 7. [测评：AI 购物代理 37% 的次数买到假优惠，Claude Opus 为零](https://www.searchenginejournal.com/ai-shopping-agents-bought-a-fake-deal-37-of-the-time-claude-opus-never-did/598682/)

- event_id: `sej-ai-shopping-agents-fake-deal-37pct-1125` · track: 🛒 AI 电商自动化 · source: Search Engine Journal
- published_at: 2026-11-25T20:00:32Z · age_hours: 18
- matched_topic: Agentic 购物与促销真实性
- summary: Search Engine Journal 11/25 一文称，在测试中 AI 购物代理有 37% 的次数买到了假优惠（fake deal），而 Claude Opus 没有中招。这是一篇测评报道，不是平台官方规则。黑五周如果开通了 agentic checkout 或预期有代理进店，值得对照自家促销页、叠加折扣和条款是否会被代理误读；不要把 37% 写成全网官方统计。

### 8. [Wired：英国金融监管机构抱怨 Meta 拒绝提供 Muse 供测试](https://www.wired.com/story/meta-refused-to-share-muse-for-testing-uk-financial-watchdog-complains/)

- event_id: `meta-muse-uk-fca-testing-refusal-1126` · track: 🤖 AI 前沿 · source: Wired
- published_at: 2026-11-26T10:51:27Z · age_hours: 4
- matched_topic: 购物 Agent 监管与平台准入
- summary: Wired 报道英国金融监管机构抱怨 Meta 拒绝把 Muse 提供给测试。这与昨日已报道的 Amazon–Meta 解除 Muse 屏蔽谈判不是同一由头：这里是监管测试访问，不是亚马逊货架是否重新开放。尚无官方产品开关变化，不要写成 Muse 已被英国叫停或已恢复购物。

### 9. [The Verge：Amazon 在召回通知责任诉讼中再败一记](https://www.theverge.com/tech/1042870/amazon-recall-order-cpsc)

- event_id: `amazon-cpsc-recall-notices-1126` · track: 🛒 AI 电商自动化 · source: The Verge
- published_at: 2026-11-26T02:53:40Z · age_hours: 12
- matched_topic: 平台合规与召回责任
- summary: The Verge 窗内报道，Amazon 未能摆脱处理更多召回通知的责任（CPSC 相关诉讼）。这是合规/责任新闻，不是 Seller Central 后台新开关。节日周若有受召回影响的 SKU，仍应走官方卖家召回流程核对 listing 与库存，而不是只转述标题。

### 10. [ChatGPT Ads 开始按「看到广告的人数」计，并新增一组人群指标](https://ppc.land/chatgpt-ad-reports-add-9-metrics-built-on-how-many-people-see-the-ads/)

- event_id: `chatgpt-ads-people-metrics-1126` · track: 🎨 创意广告 · source: PPC Land
- published_at: 2026-11-25T23:15:36Z · age_hours: 15
- matched_topic: ChatGPT Ads 衡量指标
- summary: PPC Land 与 Search Engine Journal 在窗内报道 ChatGPT Ads 的报告开始用看到广告的人数来计，并提到约 9 项基于人的指标；SEJ 另文称 OpenAI 暂不计划提供 prompt-level 报告。本轮未打开 OpenAI 官方广告文档复核每一列名称，故只作成必读、不占选题。不要写成已经可以按单条 prompt 优化出价。
- supporting:
  - [PPC Land 另一篇：ChatGPT ads start counting people](https://ppc.land/chatgpt-ads-start-counting-people-as-shein-pays-100m-and-fake-tvs-cost-135m/)
  - [SEJ：OpenAI 暂不计划 ChatGPT Ads 的 prompt-level 报告](https://www.searchenginejournal.com/openai-isnt-planning-prompt-level-reports-for-chatgpt-ads/599126/)

### 11. [Google 把 Pageburst 等 11 个已有爬虫写入官方爬虫文档](https://www.searchenginejournal.com/google-adds-pageburst-11-other-existing-bots-to-its-crawler-docs/599120/)

- event_id: `google-crawler-docs-pageburst-1126` · track: 🤖 AI 前沿 · source: Search Engine Journal
- published_at: 2026-11-26T03:22:22Z · age_hours: 11
- matched_topic: 爬虫与生成式抓取控件
- summary: Search Engine Journal 报道 Google 在官方爬虫文档中补列 Pageburst 及其他 11 个已有 bots。这是文档补全，不一定等于新爬虫刚上线。站点若要区分训练、搜索与其他抓取，仍以 Google 官方 crawler 列表和 robots.txt 产品令牌为准，不要只根据文章标题去封禁。

### 12. [OpenAI 小范围测试 Private Inference（机密计算）](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-26-2026/)

- event_id: `openai-private-inference-pilot-1126` · track: 🤖 AI 前沿 · source: The Neuron
- published_at: 2026-11-26T08:00:00Z · age_hours: 6
- matched_topic: 企业模型隐私与部署
- summary: The Neuron 11/26 早报与 Syntorak 均提到 OpenAI 正在小范围客户中测试 Private Inference，作为 Private Intelligence 的一部分，用机密计算保护提示词与输出。Neuron 引用了 Sam Altman 的帖子。这是企业隐私能力试点，不是已对所有 ChatGPT 用户开放，也不改变电商投放后台字段。
- supporting:
  - [Syntorak 11/26 早报：小范围商务客户试点，强调 prompts/outputs 在推理时隔离](https://www.syntorak.com/ai-news/2026-11-26)

## 延伸阅读

1. [Google Ads 促销抵扣到账等待由最多 35 天改为最多 42 天](https://ppctimes.com/news/google-ads-promotional-credit-processing-42-days) — PPC Times 11/26 称五份 Google Ads 帮助页把促销抵扣在达到消费条件后的到账等待从最多 35 天改为最多 42 天。本轮未能打开对应官方帮助页（旧 answer URL 404），故只作延伸，不占 must_reads / topics。 （🎨 创意广告 · 2026-11-26T12:00:00Z · age_hours=2 · 延伸参考；官方帮助页本轮未打开）

2. [Ginny Marvin：用动态转化价值做 Value-Based Bidding，不是在「破解」Smart Bidding](https://searchengineland.com/google-ads-encourages-dynamic-conversion-values-to-improve-smart-bidding-503027) — Search Engine Land 11/25 11:07 报道 Google Ads Liaison Ginny Marvin 回应 reward hacking 讨论：把 CRM 阶段、利润或预测 LTV 等动态转化价值喂给 Smart Bidding，本就是 Value-Based Bidding 的设计，而不是旁门。本轮 SEL 正文 403，未单独打开官方新帮助页，只作延伸。 （🎨 创意广告 · 2026-11-25T16:07:00Z · age_hours=22 · 延伸参考）

3. [AfterShip Returns Center 加入 Shopify Plus certified app](https://www.aftership.com/blog/aftership-returns-center-joins-shopify-plus-certified-app-program) — AfterShip 自家博客称 Returns Center 加入 Shopify Plus 认证应用计划。这是供应商公告，不是 Shopify 官方 changelog 主条目。 （🛒 AI 电商自动化 · 2026-11-26T10:14:06Z · age_hours=4 · 延伸参考）

4. [PPC Land：在 79 家美国头部零售商中，Amazon 按名称拦截了 24 个 AI agent 里的 20 个](https://ppc.land/amazon-blocks-20-of-24-ai-agents-by-name-the-most-of-79-top-us-retailers/) — PPC Land 11/25 报道一项统计：Amazon 是拦截 AI 购物代理最多的大型零售商之一。可与 Muse 谈判对照，但不是官方产品开关，也没有给出卖家后台可改字段。 （🛒 AI 电商自动化 · 2026-11-25T19:47:26Z · age_hours=19 · 延伸参考）

5. [Amazon 与 Meta 仍在谈解除 Muse 购物屏蔽（延续昨日必读，不复用脊柱）](https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/) — TechCrunch / The Verge 窗内仍在报道双方谈判，卡在广告收入与搜索结果呈现。昨日已作必读，今日不复用为选题脊柱，也没有官方宣布恢复访问。 （🛒 AI 电商自动化 · 2026-11-25T14:10:18Z · age_hours=24 · 延伸参考；昨日已作 must_read，不复用 theme_slug）

6. [Google 12 月核心更新仍为预告、尚未开滚（昨日选题，今日不复用脊柱）](https://www.searchenginejournal.com/google-december-2026-core-update/598760/) — 11/24 官方预告仍在 48h 窗口内。昨日选题已覆盖 Status Dashboard 与 Search Console 生成式 AI 控件。今日不复用 slug。开滚仍以 Dashboard 当日宣布为准。 （🤖 AI 前沿 · 2026-11-24T15:10:30Z · age_hours=47 · 硬窗口内延伸参考；不复用昨日选题脊柱）

7. [TikTok Shop EU：节日订单退货可延至 2027-01-31（官方 Pulse 日期 11/20，已出 48h 必读窗）](https://easytiktok.com/eu/news/seller-policy-pulse-november-2026) — EasyTikTok 对官方 EU Academy《Black Friday Edition: Seller Policy Pulse (November 2026)》的转述，文首写 Pulse 日期 20 November 2026、文章发布/更新 21 November 2026：符合条件的节日订单可退到 2027-01-31，并提到 12/1 拍卖 listing 规则。已超出 must_reads 48h 窗口；且不是 TikTok 官网原页，只作延伸。不要套用到美国站。 （🛒 AI 电商自动化 · 2026-11-21T00:00:00Z · age_hours=134 · 硬窗口外延伸参考）

8. [The Neuron：FCC 批准 SpaceX 最多 100 万颗卫星的轨道算力网（Starmind）授权](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-26-2026/) — 11/26 The Neuron 早报把 FCC 对 SpaceX 轨道 AI 数据中心星座的授权列为头条。这是基础设施新闻，与卖家 30 分钟动作无关，只作延伸。 （🤖 AI 前沿 · 2026-11-26T08:00:00Z · age_hours=6 · 延伸参考）

9. [Channable：欧洲商店典型 Google Ads 成交成本高出约 14%](https://ppc.land/the-typical-google-ads-sale-costs-european-shops-14-more-channable-finds/) — PPC Land 转述 Channable 发现欧洲商店典型 Google Ads 成交成本高约 14%。这是第三方研究，不是官方费率公告，数字需自行对照账户，不作选题。 （🎨 创意广告 · 2026-11-25T19:51:25Z · age_hours=19 · 延伸参考）

10. [Anthropic 用 Claude agents 把 Messages API 从 Python 迁到 Rust（二手早报，未打开官方博文）](https://www.syntorak.com/ai-news/2026-11-26) — The Neuron / Syntorak 11/26 早报称 Anthropic 用 agent 把 Messages API 从 Python 迁到 Rust，并给出约 70% 更低的每请求 CPU 与约 20% 更短的中位首 token 时间。本轮未打开 Anthropic 官方博文复核这些数字，只作延伸。 （🤖 AI 前沿 · 2026-11-26T08:00:00Z · age_hours=6 · 延伸参考；官方原文未打开）

11. [OpenAI 为 ChatGPT 访问网站补充 2000+ 个 IP 地址](https://ppc.land/openai-adds-over-2-000-internet-addresses-chatgpt-uses-to-visit-websites/) — PPC Land 报道 OpenAI 增加了 2000 多个 ChatGPT 用来访问网站的地址。对需要按 IP 放行或记录抓取的站点有参考价值，但应对照 OpenAI 官方 crawler/IP 文档，不要只按二手稿改防火墙。 （🤖 AI 前沿 · 2026-11-25T19:44:52Z · age_hours=19 · 延伸参考）

12. [Macy’s 第 100 届感恩节游行因故推迟](https://www.retaildive.com/news/macys-100th-thanksgiving-day-parade-postponed/875808/) — Retail Dive 报道 Macy’s 百年感恩节游行被推迟。对当天品牌直播/赞助排期有影响，不是广告后台字段变更。 （🎨 创意广告 · 2026-11-25T23:40:00Z · age_hours=15 · 延伸参考）

## 推文草稿

### 草稿 1 · 新闻翻译 · hook: X 刚发布/更新了，对你意味着三件事

```
Google just spelled out how to control AI Max for Search without turning it off.

That means three things.

First, text guidelines are now listed as a campaign-level control: term exclusions (up to 25 exact words or phrases per campaign) and messaging restrictions for copy you do not want. The help page marks this as an experimental beta, and term exclusions are language-specific.

Second, you do not need to switch Smart Bidding to Manual CPC. Use negatives or brand exclusions, turn off Search term matching in an ad group's AI Max settings, or remove individual assets. In Assets, filter by Added by: Google AI to review holiday copy in bulk.

Third, URL exclusions under Campaigns > Settings > AI Max only apply to landing pages Final URL expansion chooses. Responsive search ads with a static final URL, and manual sitelinks, can still send traffic to a URL you thought you blocked.

Do that check today. Tomorrow is Black Friday.
```

- tags: 🎨 创意广告, 🛒 AI 电商自动化
- reasoning: 用本周有效的新闻翻译 Hook，把今日 Google 硬选题译成三件 30 分钟动作。引用已打开的官方帮助页，标明 beta、25 条上限、URL exclusion 的例外，避免写成「关掉 AI Max」或全球强制。与昨日 schema.org / 核心更新预告区分。

### 草稿 2 · 跨领域连接 · hook: 把 X 和 Y 连起来看

```
Shopify just widened chargeback defense on the same week many stores turned on agentic checkout.

Look at the two together.

As of the November 25 changelog, card dispute responses can include an AI-written defense for every major reason code, not only product-not-received. It is on by default as “Include Shopify-generated insights to strengthen case (recommended),” and you can deselect it.

Unauthorized disputes now get CVV/AVS, the authorization code, 3D Secure when it helps, and Visa Compelling Evidence 3.0 on qualifying past orders — automatically. If an AI shopping assistant placed the order, Shopify also attaches a payment authorization record: the spending limit, the checkout approval, and the assistant's name when it is known.

One more switch: Settings > Notifications > Staff notifications > Order dispute updates. On existing stores it defaults to the owner. On Thanksgiving week, send it to the person who actually files evidence.

This is evidence and routing, not a promise you will win every Black Friday chargeback.
```

- tags: 🛒 AI 电商自动化
- reasoning: 用跨领域 Hook 把本周 ChatGPT agentic checkout 与今日官方拒付证据连起来，但不复用旧 theme_slug。给出通知开关和表单勾选，避免写成稳赢。补位电商赛道在节日周的售后动作。

### 草稿 3 · 跨领域连接 · hook: 把 X 和 Y 连起来看

```
Today is Thanksgiving in the US, so this morning's market snapshot still shows stocks as closed. Treat NVDA at 149.30 (-3.91%) and SHOP at 133.40 (+0.82%) as Wednesday's close, not a Thursday open. BTC was near 60,807, up about 4.3% over 24 hours, but Crypto Fear and Greed stayed at 9 (Extreme fear) and the ETF daily print was about -$453 million. That is context, not a trading idea.

The useful move today is operational. Grok Bot's changelog now shows v1.3.0 — this page still read v1.2.3 at yesterday's 9:31am ET briefing. A sold-out product card can offer Notify me, which watches that seller and alerts you when the item is back. If you run a team, check the new org setting that limits connected accounts to your own domains, and confirm Slack handoffs return to your DM with a Connect button.

Don't wait on the market tape to do those checks. Black Friday is tomorrow.
```

- tags: 🤖 AI 前沿, 🛒 AI 电商自动化
- reasoning: 草稿硬约束：引用至少 1 个 market_snapshot 数据点，并标明感恩节美股休市、价格是周三收盘。不写投资建议（不用 btcScore 的「加仓」措辞）。把市场噪音和 Grok Bot 1.3.0 的补货提醒 / 配置动作连起来，补 D4。

## 跨领域机会

- **AI 广告控件 × 黑五文案风险**：AI Max text guidelines（每战役最多 25 条 term exclusions，官方标 beta）加上 Assets 里 Added by: Google AI 过滤，正好用来拦住节日生成文案里不能承诺的折扣词；但 URL exclusions 管不到 RSA 静态 Final URL 和手动 sitelink，大促落地页如果只做了排除规则，仍可能被旧广告点进去。
- **Agentic checkout × 拒付证据**：Shopify 已能管理 ChatGPT agentic checkout；11/25 起，这类订单的拒付响应会自动附上助手消费限额与结账批准。黑五若有 AI 助手代下单，争议材料不再只靠商家自己的发货记录。不要复用「默认打开 checkout」那条旧选题，只把新证据当动作。

## 本周表现摘要

- period: 2026-11-19 ~ 2026-11-26
- Typefully 不可用，无曝光数据；已跳过 Step 2–3，未改写 profile_recent.md。
- insights: Typefully 不可用，本周无曝光数据。今日是感恩节、黑五前一天，选题落在官方帮助页/changelog 的可改控件：Google 家族 2/2（AI Max text guidelines + local promotions 店内核销），Shopify 拒付包 1 条，D4=1（changelog 首次出现 v1.3.0）。未为凑满 5 条加入代理 Ads opportunities、促销抵扣 42 天或 Muse 谈判。
- covered_topics: google-ads-aimax-text-guidelines-controls-without-off-1126, google-mc-local-promotions-redeemable-instore-1126, shopify-chargeback-ai-defense-all-reasons-staff-notify-1126, grok-bot-1-3-0-restock-alerts-slack-handoff-domain-controls-1126, google-mc-sale-annotation-schema-markup-12-markets-1125, google-search-dec-core-preannounce-ranking-hub-genai-controls-1125, shopify-chatgpt-agentic-checkout-default-on-1124, google-back-button-hijacking-faq-ad-code-no-shield-1124 …
- winning_hooks: X 刚发布/更新了，对你意味着三件事, 大部分人用 X 的方式是错的, 把 X 和 Y 连起来看

## 市场快照

- 抓取时间: 2026-11-26T14:18:19.052Z（约 9:18am ET；美股 Thanksgiving 休市，stock marketState=closed）
- 股票: NVDA 149.3 (-3.91%, closed)；SHOP 133.4 (+0.82%, closed)；GOOG 270.98 (-2.02%, closed)；TSLA 380.14 (-1.18%, closed)
- BTC 60806.7（24h +4.33%）；ETH 1703.04；SOL 71.33
- S&P 500 7182.78（-0.2542670623475113%）；VIX 27.05；Gold 3571；DXY 103.645
- Crypto F&G 9（Extreme fear, change 0）；CNN F&G 15（extreme fear）
- ETF 日净流入 -453000000；NUPL 0.121；btcScore 22.3（恐慌）
- 以上为行情数据，不是投资建议。

## 系统建议

仅写入 daily_data.json.suggestions，未改 info_sources.json / topic_library.json / profile_longterm.md。

### info_sources
**promote**
- PPC Times — 11/26 帮助页监测捕捉到 local promotions in-store Note 与 AI Max text guidelines/控件改句，且都已用官方帮助页复核（high）
- Google Ads Help / Merchant Center Help — 今日两条 Google 硬题的原文都在官方帮助页（2877565、15910187、16489313、16230205、16738708）（high）
- Shopify Changelog — 11/25 四条拒付更新均有准确时间戳并直接进入今日选题（high）

**demote**
- Reddit RSS — 本轮再次 429/超时/404，连续多日 0 条窗内帖（high）
- 中文卖家源 RSS（雨果/AMZ123/亿邦等） — 本轮 cifnews/ebrun/amz123 均为 404 或 parse_error，采集仍空（high）
- Amazon Ads blog RSS — 本轮 advertising.amazon.com blog RSS 404；what's-new 页抓到的是导航壳，正文日期抽不出，需改抓取方式（medium）

**add**
- x.ai/changelog/bot（官方页，不只 RSS） — 昨日页面仍显示 v1.2.3，今日 live 页已是 v1.3.0，应作为 D4 固定打开项（high）
- Google Ads 帮助：text guidelines（answer/16489313）与 Final URL expansion in Search（answer/16230205） — 今日控件题的操作路径都在这两页，宜加入固定核验清单（high）
- Merchant Center Promotions policies（answer/2877565） — local promotions in-store Note 写在政策页而非新闻稿（medium）

### topic_library add
- AI Max for Search 的 text guidelines 与不必关闭即可用的控件 — 官方帮助页 11/26 监测到改句，黑五前可执行（high）
- Merchant Center local promotions 必须店内核销 — 政策页新增 Note，有门店的零售商当天可对账（high）
- Shopify 全原因拒付 AI 答辩 + Agentic 订单授权证据 — 11/25 官方 changelog 四条，与 agentic checkout 形成新动作而非旧脊柱（high）

### 本轮跳过

- Typefully / Exa MCP 不可用，跳过 Step 1–3，未改写 profile_recent.md
- Channel D / Bookmark Debt Collector 按 Alex 2026-11-03 停用
- 未调用 X search_news（昨日同窗 429）
- Reddit RSS 与中文卖家源 RSS 失败
- Writer 全流水线未跑；未自动发帖；不通知 xhs / x / wechat，待 Alex 确认选题后再交接

