# ContentOS Daily Briefing -- 2026-11-25

- generated_at: 2026-11-25T14:31:32.879166Z（America/New_York：2026-11-25 09:31 EST）
- pass: wednesday-9am-ET-refresh-no-BDC-post-researchy
- raw_material_count: 362（RSS 窗内去重 305 + 官方页 22 + 打开文章/帮助页 35；X search_news 4 次因共享通道 429 失败、未计读取）
- channel_d: disabled_by_alex_2026-11-03 · D4=0
- must_reads: 16 · also: 13 · topics: 2 · drafts: 3

## 发布策略

今日（周三）是黑五周 11/19-11/30 的第七天，明天 11/26 感恩节，后天 11/27 黑五。市场快照抓取时（约 9:20am ET）股票字段仍为 marketState=closed，价格应视为周二收盘/开盘前，不是周三开盘价。优先发 12 市场 Shopping 促销标的 schema.org 要求（官方帮助页已核），其次 Google 12 月核心更新预告与 Search Console 生成式 AI 控件（官方写明尚未开滚）。Google 家族今日 2/2 满额；ads_labels 150 与 Video reach 2027 升级只进必读。Shopify agentic checkout 与 Amazon 11/26 VS NWD 仍在窗口，但不复用昨日选题脊柱。D4=0。不要把 Muse-Amazon 谈判写成已恢复访问。

## 今日选题

### 1. 12 个非美市场的 Shopping 促销标：落地页 schema.org 须同时给出原价和促销价，并与 Merchant Center feed 一致

- theme_slug: `google-mc-sale-annotation-schema-markup-12-markets-1125`
- admission: a+c · heat: high · format: 方法论
- tracks: 🎨 创意广告, 🛒 AI 电商自动化
- tags: 平台可改字段
- angle: 本轮已打开官方帮助页《About sale price annotations》。在澳、巴、加、法、德、印、意、日、韩、荷、西、英，Shopping ads 促销标现要求落地页 microdata（schema.org）同时包含 base price 与 sale price，并与 feed 一致；折扣须在 5%–90%，原价须在过去 200 天内至少 30 天反映实际或收取价格。页面未给生效日。美国 Shopping 和免费 listing 仍是「落地页应展示两个价格」，不要写成全球一刀切。30 分钟动作：1）挑几件在这些市场投放且正在促销的商品，用 Rich Results Test 看 Product 标记是否同时有原价和促销价、币种是否与 feed 的 price / sale_price 一致。2）许多 Shopify 主题只输出当前价，要先问主题或 SEO 应用怎么补上原价，再开下一场大促。3）大促期间在 Merchant Center 商品列表用是否带促销标的过滤做抽查，标突然变少时优先查 markup 与 feed 是否不同步。官方写明即使满足要求也不保证展示。这与 11/22「sale_price 持续时间不应超过 30 天」是不同要求，可并行检查，但不复用那个 slug。
- reasoning: 命中 Admission (a)(c)：落地页 schema.org 与 feed 的 price / sale_price 是可改字段，30 分钟能用 Rich Results Test 抽查。platform_family: Google（今日 1/2）。官方帮助页已打开，不是只转述二手稿。未出现在昨日 topics[]（昨日为 Shopify agentic checkout、返回键 FAQ、Amazon VS NWD）。与 11/22 sale_price 30 天提示是不同 class（markup/合规 vs 持续时间），新 slug，未写 reuse 旧 slug。非 MCP、非 D4。黑五在 12 个市场做促销时时效强。Bingge 评分≥70。

### 2. Google 11/24 预告 12 月核心更新，并上线排名原则、预告机制和 Search Console 生成式 AI 控件

- theme_slug: `google-search-dec-core-preannounce-ranking-hub-genai-controls-1125`
- admission: a+c · heat: high · format: 方法论
- tracks: 🤖 AI 前沿, 🎨 创意广告
- tags: 平台可改字段
- angle: 本轮已打开官方事件页和文档（Last updated 2026-11-24 UTC）。December 2026 core update 已预告、尚未开滚：改进对更长更复杂问题的理解，并改进已打开个性化的结果；全球语言和地区适用。Google 对 SERoundtable 说还没有日期、会在开滚当天宣布、not imminent。不要写成更新已经开始。30 分钟动作：1）订阅 Search Status Dashboard 的 RSS/Atom，开滚后再看 Search Console，并等到事件标记完成后至少再看一周数据。2）在 Search Console 找到 Search generative AI control，确认站点是否允许内容用于 AI Overviews / AI Mode 的 grounding 与展示；这不影响模型训练，官方写明不作为其他搜索排名信号。若还要限制 Gemini 等非搜索产品，另查 robots.txt 里的 Google-Extended。3）若引用错了，读《Attribution and factuality》页；英国站点记住 12/17 才会启用整站手动除索引的申诉链接。反馈须在 Search Console 用话题标签，例如未来的 #DecemberCoreUpdate2026，且官方写明不会因此做单 URL 人工调权。不要把「预告」写成「已经开始降权」。
- reasoning: 命中 Admission (a)(c)：Search Console 的 Search generative AI control、robots.txt 的 Google-Extended，以及 Status Dashboard 订阅/反馈路径，都是 30 分钟可执行。platform_family: Google（今日 2/2）。官方页均已打开。未复用昨日返回键 FAQ slug。非 MCP、非 D4。ads_labels 与 Video reach 同期变更因家族配额只进 must_reads，不换入弱题凑满 5 条。Bingge 评分≥70。

## 今日必看

### 1. [Google Search Central 于 11/24 上线排名原则与生成式 AI 控件文档，并预告 12 月核心更新](https://status.search.google.com/incidents/AXrqxXXdtSjj3672ux7X)

- event_id: `google-search-ranking-hub-dec-core-genai-1124` · 🤖 AI 前沿 · Google Search Status Dashboard · published_at 2026-11-24T15:03:00Z · age_hours 23.5
- 本轮已打开官方更新页、排名原则、如何获知更新、提交反馈、生成式 AI 控件与引用页，以及 Search Status Dashboard 事件页。帮助页页脚均为 Last updated 2026-11-24 UTC。事件页写明 2026-11-24 07:03 PST 预告 December 2026 core update：改进对更长、更复杂问题的相关性理解，并改进已打开个性化的结果；适用于 Google Search 所有地区和语言；尚未给出开滚日期。Google 对 Search Engine Roundtable 说还没有日期、会在开滚当天再宣布、not imminent。同一天新增 Search Console 的 Search generative AI control（管 AI Overviews / AI Mode 的 grounding 与展示，不作为其他搜索排名信号），以及 robots.txt 的 Google-Extended 等控件说明。UK CMA 公平排名要求相关：12/17 起英国整站被手动移出索引的申诉链接才会启用。不要写成核心更新已经在滚动。（发布时间以事件页 07:03 PST 为准）
  - 补充：[官方文档更新索引（含排名专区和生成式 AI 控件两条 11/24 记录）](https://developers.google.com/search/updates)
  - 补充：[Our principles for ranking results（Last updated 2026-11-24 UTC）](https://developers.google.com/search/docs/ranking/principles-for-ranking-results)
  - 补充：[How to stay informed：政策变更和显著核心更新会在 Status Dashboard 预告；可订 RSS](https://developers.google.com/search/docs/ranking/stay-informed)
  - 补充：[Control how your content is used for generative AI at Google（Search Console / robots.txt / meta）](https://developers.google.com/search/docs/fundamentals/gen-ai-controls)
  - 补充：[Attribution and factuality in Search generative AI features](https://developers.google.com/search/docs/fundamentals/gen-ai-attribution-factuality)
  - 补充：[PPC Land：预告 12 月核心更新，并指出与英国截止日期接近](https://ppc.land/google-preannounces-a-december-core-update-as-ai-overview-links-slide-down/)
  - 补充：[Search Engine Roundtable 转述 Google：尚无开滚日，not imminent](https://www.seroundtable.com/google-december-2026-core-update-42615.html)

### 2. [Merchant Center 帮助页现要求：12 个非美市场的 Shopping 促销标，落地页 schema.org 须同时给出原价和促销价，并与 feed 一致](https://support.google.com/merchants/answer/9017019?hl=en)

- event_id: `google-mc-sale-annotation-schema-12-markets-1124` · 🎨 创意广告 · Google Merchant Center Help · published_at 2026-11-24T00:00:00Z · age_hours 38.5
- 本轮已打开官方帮助页《About sale price annotations》和 PPC Times 11/24 拆解（11/25 更新）。官方在澳大利亚、巴西、加拿大、法国、德国、印度、意大利、日本、韩国、荷兰、西班牙和英国的 Shopping ads 要求中写明：促销价须低于原价；折扣须大于 5% 且小于 90%；原价须在过去 200 天内至少 30 天反映实际或收取价格；以及 Structured data：Both the base and sale prices must be present in the landing page microdata (schema.org) and match the Merchant Center data source。页面未给出该结构化数据要求的生效日期。美国 Shopping ads 和免费商品信息仍写落地页应展示两个价格，本轮未见同样的 schema 硬性句。即使满足要求，官方也写明促销标不保证出现。PPC Times 观察到：许多主题或平台的 Product 标记只输出当前价。不要写成「美国也强制 schema」或「缺 markup 会被下架」。（发布时间近似：帮助页变更由 PPC Times 监测于 11/24 发现）
  - 补充：[PPC Times：监测到帮助页从「落地页应展示两个价格」改为 schema.org 须同时给出并与 feed 一致](https://ppctimes.com/news/merchant-center-sale-price-annotations-structured-data)

### 3. [Merchant Center 展示广告属性页把 ads_labels 上限从 30 次上调到 150 次（仅动态再营销，不支持 Shopping）](https://support.google.com/merchants/answer/6069387?hl=en)

- event_id: `google-mc-ads-labels-limit-150-1124` · 🎨 创意广告 · Google Merchant Center Help · published_at 2026-11-24T00:00:00Z · age_hours 38.5
- 本轮已打开官方帮助页《About display ads attribute specification》：You can add the product grouping label for display ads [ads_labels] attribute up to 150 times。该属性可多值、用于动态再营销 CPC，页面写明不支持 Shopping 广告。相关的 ads_grouping（单值）本轮未见改动。帮助页未给出 150 次上限的生效日期；PPC Times 的帮助页监测于 11/24 发现由 30 改为 150。30 分钟可先检查是否有商品已接近旧上限，新标签建议先在一小部分商品或补充数据源测试。不要写成 Shopping 活动也能用 ads_labels。（发布时间近似）
  - 补充：[PPC Times 11/24 拆解（11/25 更新）](https://ppctimes.com/news/merchant-center-ads-labels-limit-150)

### 4. [Fortune：Amazon 与 Meta 据报在谈解除 Muse 对 Amazon 店铺的封锁，广告和搜索呈现是主要分歧](https://www.fortune.com/2026/11/25/exclusive-amazon-meta-talks-deal-muse-ai-shopping-agent-blockade/)

- event_id: `amazon-meta-muse-blockade-talks-1125` · 🛒 AI 电商自动化 · Fortune · published_at 2026-11-25T08:01:00Z · age_hours 6.5
- Fortune 11/25 独家（约美东 3:01am）称双方多次讨论让 Muse 重新接入 Amazon 网店；知情人士说谈判中的两大因素是搜索结果如何呈现以及广告如何处理。Amazon 担心广告收入、Muse 给出的商品搜索质量，以及与消费者的直接关系被削弱。任何协议据报需双方 CEO 签字。双方均拒评。The Verge 与 TechCrunch 亦作转述。这是进行中的谈判，不是已上线的平台开关，不要写成 Muse 已恢复访问 Amazon，也不要据此改预算。（报道时间取 Fortune）
  - 补充：[The Verge 同日报道](https://www.theverge.com/tech/1042071/meta-amazon-muse-ai-shopping-discussions)
  - 补充：[TechCrunch 同日报道](https://techcrunch.com/2026/11/25/amazon-and-meta-reportedly-in-talks-to-lift-blockade-on-ai-agent-muse/)

### 5. [Adweek：Human Security 预计 Cyber Week 智能体流量约达去年 150 倍，其中 Meta Muse 占绝大部分](https://www.adweek.com/commerce/ai-agent-traffic-to-surge-150x-this-cyber-week-driven-mostly-by-meta-muse/)

- event_id: `adweek-human-muse-agent-traffic-150x-cyber-week-1125` · 🛒 AI 电商自动化 · Adweek · published_at 2026-11-25T09:13:00Z · age_hours 5.3
- Adweek 11/25 引 Human Security：11/26–11/30 Cyber Week 的智能体流量预计约为去年同期的 150 倍；Muse 贡献其中近 70%。文章称智能体仍以浏览为主，但结账请求在增加；Google 的智能体占总流量不到 5%，但对结账页请求约占 20%。零售商对是否放行智能体意见不一。全文后半需订阅，关键数字来自已打开页的 Key Takeaways，未看到原始研究报告。可作黑五流量预案参考，不要把 150x 写成官方平台数据。

### 6. [Shopify 把 Direct checkout 改名为 agentic checkout，并已对 ChatGPT 开放：符合条件的店铺默认开启](https://changelog.shopify.com/posts/manage-whether-ai-agents-can-buy-your-products-for-shoppers-through-chatgpt)

- event_id: `shopify-agentic-checkout-chatgpt-default-on-1123` · 🛒 AI 电商自动化 · Shopify Changelog · published_at 2026-11-23T17:00:00Z · age_hours 45.5
- 官方 11/23 Changelog 与帮助页仍在 48 小时窗口内。Direct checkout 改名为 agentic checkout，已对 ChatGPT 开放；符合条件且打开了 Manage for me / Automatically enable new channels 的店铺默认开启。关掉 Agentic checkout 不等于退出 ChatGPT 发现，也不影响 Shop skill。今日不复用该主题做选题脊柱，仅保留必读。

### 7. [亚马逊据通知将于 11/26（感恩节）从 Amazon.com 移除第三方 Victoria's Secret 商品，仅保留 Brand Representative](https://ppc.land/amazon-blocks-third-party-victorias-secret-sellers-from-november-26/)

- event_id: `amazon-vs-nwd-third-party-removal-1126` · 🛒 AI 电商自动化 · PPC Land / LinkedIn 流出通知 · published_at 2026-11-23T19:48:16Z · age_hours 42.7
- 截止日是明天感恩节。来源仍是经 LinkedIn 流出的 Amazon Services 通知（ASGTG / Ephraim Rosenberg 转发），本轮仍未打开官方帮助页。通知据称不计入 Account Health。今日不复用该主题做选题脊柱，只保留必读：有库存的卖家需在后天黑五前自行复核后台通知并处理库存。不要写成已核官方规则。

### 8. [Pinterest 官方宣布：符合条件的 Microsoft Advertising 活动可投放到 Pinterest 首页信息流、搜索和 Related Pins](https://newsroom.pinterest.com/)

- event_id: `pinterest-microsoft-ads-inventory-1123` · 🎨 创意广告 · Pinterest Newsroom / PPC Land · published_at 2026-11-23T19:27:24Z · age_hours 43.1
- 昨日已列入必读。官方稿仍未给出单一上线日，今日仍不作选题。广告主需等账户里实际出现该库存后再测，不要写成今天起全量可投。
  - 补充：[PPC Land 11/23 拆解](https://ppc.land/pinterest-sells-feed-and-search-ad-space-through-microsoft-advertising/)

### 9. [HUMAN 称 BADBOX 3.0 高峰期每天约 400 亿次欺诈广告请求，约占其检测到的 CTV 流量 4% 以上](https://ppc.land/human-traces-up-to-40-billion-fraudulent-ad-requests-a-day-to-cheap-tv-boxes/)

- event_id: `human-badbox-3-ctv-ad-fraud-1123` · 🎨 创意广告 · PPC Land / HUMAN · published_at 2026-11-24T00:02:50Z · age_hours 38.5
- 仍在 48 小时窗口。黑五 CTV 预算上升时，值得核查看板里的无效流量和供应路径，但不要把该公司检测口径写成全行业官方占比。

### 10. [Microsoft Ads Liaison 澄清：11/18 博客所称出价模型升级并非单一切换日，夏季已开始滚动](https://ppc.land/microsoft-says-its-bidding-upgrade-started-in-summer-not-november-18/)

- event_id: `microsoft-ads-bidding-upgrade-no-single-golive-1123` · 🎨 创意广告 · PPC Land / Microsoft Ads · published_at 2026-11-23T21:07:02Z · age_hours 41.4
- 仍在窗口内。不要把 11/18 写成统一上线日。今日不作选题。

### 11. [PPC Times：Google Ads 帮助页把 Conversion Lift 门槛写成「每月至少 1,000 次 observed conversions」](https://ppctimes.com/news/google-ads-conversion-lift-1000-conversions-per-month)

- event_id: `google-ads-conversion-lift-1000-per-month-1125` · 🎨 创意广告 · PPC Times · published_at 2026-11-25T00:00:00Z · age_hours 14.5
- 本轮已打开 PPC Times 11/25 原文。监测显示《Set up Conversion Lift based on users》把账户门槛从「至少 1,000 次 observed conversions」（无时间范围）改为 per month；带 supplementary data 的转化不计入；活动预算最低仍为至少 5,000 美元。帮助页未说明新措辞何时生效，也未写清按账户、按转化操作还是按哪个窗口统计。本轮未打开 Google Ads 官方帮助页原文，不作为今日选题。不要把旧的累计口径继续写成现行规则。

### 12. [PPC Times：Google 将于 2027 年把非跳过式 Video reach 活动自动升级为 multi-format，并写明从 2027 年 3 月起](https://ppctimes.com/news/google-ads-video-reach-non-skippable-multi-format-upgrade-2027)

- event_id: `google-ads-video-reach-multiformat-upgrade-mar2027-1125` · 🎨 创意广告 · PPC Times · published_at 2026-11-25T00:00:00Z · age_hours 14.5
- 本轮已打开 PPC Times 11/25 原文：15 秒和 20 秒非跳过式 Video reach 将在 2027 年自动升级为 multi-format responsive ads，广告组和广告历史会被重置；文中写明 from March 2027。本轮未打开 Google Ads 官方帮助页原文，不作为今日选题。有此类活动的广告主可先在账户里清点，等官方页核对后再改结构。

### 13. [Anthropic 宣布完成 IPO 及同时进行的私募：发行价每股 83.00 美元](https://www.anthropic.com/news/ipo-close)

- event_id: `anthropic-ipo-close-1125` · 🤖 AI 前沿 · Anthropic Newsroom · published_at 2026-11-25T00:00:00Z · age_hours 14.5
- 本轮已打开 Anthropic 新闻室 11/25 公告：今日宣布完成 Class A 普通股 IPO，含承销商超额认购权全部行使，以及同时进行的私募；公开发行价为每股 83.00 美元，合计 1,127,000,000 股。这是融资新闻，只进必读，不作选题脊柱，也不构成投资建议。

### 14. [OpenAI 预印本证明平方矩阵乘法指数恰好为 9/4](https://github.com/openai/math/tree/main/preprints/The-matrix-multiplication-exponent-is-nine-fourths-November-24-2026)

- event_id: `openai-matmul-exponent-nine-fourths-1124` · 🤖 AI 前沿 · OpenAI / @SebastienBubeck · published_at 2026-11-25T01:33:00Z · age_hours 13.0
- OpenAI 研究人员 Sébastien Bubeck 于美东 11/24 20:33 发帖，随后 Greg Brockman 引用确认：在已有 9/4 上界的前提下，该预印本给出匹配下界，指数确定为 9/4。预印本标注日期 2026-11-24，刊于 openai/math 仓库。这是研究突破，翻译不成 30 分钟卖家动作，只进必读。
  - 补充：[@SebastienBubeck 原帖](https://x.com/SebastienBubeck/status/2125402576145572334)

### 15. [Anthropic 推出 Claude Ship：让 AI agents 审查、修复并批准代码变更](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)

- event_id: `anthropic-claude-ship-1123` · 🤖 AI 前沿 · TechCrunch / Anthropic · published_at 2026-11-23T22:05:50Z · age_hours 40.4
- 仍在 48 小时窗口。工程向产品发布，今日不作卖家选题。

### 16. [Amazon 官方宣布：已签署协议购买 Decart Optimization Stack（DOS）技术，并引进其联合创始团队](https://techcrunch.com/2026/11/24/amazons-decart-acquisition-is-a-bet-on-using-software-to-narrow-the-gap-with-nvidia-in-the-ai-chip-race/)

- event_id: `amazon-decart-dos-technology-agreement-1123` · 🤖 AI 前沿 · About Amazon / TechCrunch · published_at 2026-11-23T19:35:14Z · age_hours 42.9
- 仍在窗口。属技术和人才交易，不是卖家后台可改字段，今日只保留必读。

## 延伸阅读

1. [Google Search Central 于 11/23 给「返回键劫持」垃圾政策加了 FAQ：广告代码不是挡箭牌](https://developers.google.com/search/docs/essentials/spam-policies#back-button-hijacking-faq) — 已出 48 小时窗口。昨日选题脊柱，今日不再做选题，仅作延伸。（🎨 创意广告，age_hours 62.5，硬窗口外延伸参考）
2. [Google Merchant Center：sale_price 持续时间不应超过 30 天，否则可能拿不到删除线原价和促销标](https://ppc.land/merchant-center-sales-running-past-30-days-may-miss-googles-sale-badge/) — 11/22 选题。与今日「12 市场 schema.org 须同时给出两个价格」不是同一要求，后者已进必读和今日选题。（🎨 创意广告，age_hours 77.0，硬窗口外延伸参考）
3. [YouTube Shorts 广告：点赞、评论、分享现在都能算 engaged-view conversion，也算 TrueView view](https://ppc.land/google-lets-a-like-stand-in-for-5-seconds-of-viewing-in-shorts-conversions/) — 已出窗。评估 Shorts 时仍需把点赞触发的 EVC 和 5 秒观看分开看。（🎨 创意广告，age_hours 77.3，硬窗口外延伸参考）
4. [x.ai/changelog/bot 仍为 2026-11-18 v1.2.3（工具权限与 routine 重连卡片），本轮打开官方页无更新](https://x.ai/changelog/bot) — 今日 D4=0，无新的官方 Grok Bot 配置项可写。（🤖 AI 前沿，age_hours 182.5，硬窗口外延伸参考）
5. [PPC Times：Google 从其同意模式参考页删除了 IP 截断相关句子](https://ppctimes.com/news/google-ads-consent-mode-ip-truncation-lines-removed) — 11/25 监测到的文档删除，作者写明这不能证明实际处理已改变。本轮未打开官方帮助页原文。（🎨 创意广告，age_hours 14.5，延伸参考）
6. [Meta 新闻室：Muse 已向英国 18 岁及以上用户开放，支持 Shop Pay 与 Onelink 结账](https://about.fb.com/news/2026/11/introducing-muse-in-the-uk-a-personal-ai-agent-you-control/) — 页面标注 11/23 及 11/24。可在 iOS、Android、muse.ai 与 WhatsApp 使用。文章称 Muse 看不到用户密码或支付方式，重要操作前会征求同意。与昨日 Shopify ChatGPT agentic checkout 不是同一开关，今日不作选题。（🛒 AI 电商自动化，age_hours 38.5，延伸参考）
7. [Pinterest 将允许家长限制青少年看到的 AI 生成内容](https://newsroom.pinterest.com/) — Newsroom 标注 November 23, 2026。偏安全与家庭控件，不是广告主可改的投放字段。（🎨 创意广告，age_hours 62.5，延伸参考）
8. [PPC Land：英国 ICO 警告，跳过用户控件的 AI agent 开发者可能面临执法](https://ppc.land/ai-agent-makers-that-skip-user-controls-face-action-uks-ico-warns/) — 隐私与产品设计向，不是电商后台字段变更。（🤖 AI 前沿，age_hours 8.8，延伸参考）
9. [PPC Land：AI agents 现在可以按次用美元向 AWS Marketplace 卖家付费](https://ppc.land/ai-agents-can-now-pay-aws-marketplace-sellers-per-request-in-dollars/) — 偏云市场结算，不是跨境店铺运营字段。（🤖 AI 前沿，age_hours 41.3，延伸参考）
10. [SEJ：黑五前最后一份广告检查清单（修什么、先放下什么）](https://www.searchenginejournal.com/the-final-ad-checklist-before-bfcm-what-to-fix-now-what-to-leave/597701/) — 操作清单，不是平台规则变更。窗内约 47 小时，可作备忘，不作选题。（🎨 创意广告，age_hours 47.5，延伸参考）
11. [Google 发布 Google-Agent 流量说明：用户触发的抓取一般忽略 robots.txt](https://ppc.land/google-documents-12-existing-bots-that-ignore-robots-txt/) — 已出或接近出窗。站长可在 CDN/WAF 放行，不作今日选题。（🤖 AI 前沿，age_hours 49.3，硬窗口外延伸参考）
12. [Import AI 482：华为 kernel 基准、空中无人机检测，以及国家实验室的 AI 科学基准](https://importai.substack.com/) — 已出窗，仅作延伸。（🤖 AI 前沿，age_hours 48.3，硬窗口外延伸参考）
13. [Vercel：现有 Pro 团队的 Standard builds 已改为按用量计费](https://vercel.com/changelog/standard-builds-for-existing-pro-teams-have-moved-to-usage-based-billing) — 开发者成本项，不是店铺广告字段。（🤖 AI 前沿，age_hours 6.5，延伸参考）

## 推文草稿

### 草稿 1 · hook: X 刚发布/更新了，对你意味着三件事 · 新闻翻译

```
Google just tightened sale badges in 12 non-US Shopping markets.

That means three things.

First, the help page now says the landing page microdata (schema.org) must include both the base price and the sale price, and those numbers must match your Merchant Center feed. Showing both prices on the page is no longer the only bar in those countries.

Second, this is written for Australia, Brazil, Canada, France, Germany, India, Italy, Japan, Korea, the Netherlands, Spain, and the UK. The US Shopping line still says both prices should be displayed on the landing page. Don't treat this as a global schema mandate.

Third, before Black Friday, test a few sale products with the Rich Results Test. Many Shopify themes only output the current price in Product markup. The help page also says a badge is not guaranteed even when you meet the rules, and it does not give an effective date.
```

- reasoning: 用本周有效的新闻翻译 Hook，把今日硬选题（12 市场 schema.org）译成 30 分钟动作。写明美国口径不同、无生效日、不保证展示，避免写成全球强制或平台惩罚。与 11/22 的 30 天持续时间提示区分。

### 草稿 2 · hook: 大部分人用 X 的方式是错的 · 新闻翻译

```
Most people will treat Google's December 2026 core update notice as if the update already started. That is the wrong read.

On November 24 Google preannounced the update on the Search Status Dashboard and published a ranking hub, including a Search Console control for generative AI in Search. A Google spokesperson told Search Engine Roundtable there is no date yet, it will be announced the day it starts, and it is not imminent.

What you can do today: subscribe to the Status Dashboard feed; check the Search generative AI control before you assume AI Overviews can use your pages; and wait until the incident is marked complete, plus at least a week of data, before you judge a traffic drop. Official docs also say feedback will not produce manual ranking changes for a single URL.
```

- reasoning: 用反常识 Hook 纠正「预告=已开滚」。引用官方事件页和 SERoundtable 对 Google 的求证。给出 Search Console 控件和等待窗口，不渲染成惊吓。

### 草稿 3 · hook: 把 X 和 Y 连起来看 · 跨领域连接

```
This morning's market snapshot was taken at about 9:20am ET, while US stocks were still marked closed, so treat NVDA at 155.38 (-5.86%) and SHOP at 132.31 (-1.48%) as Tuesday's close or the pre-open quote, not Wednesday's open.

BTC was near 58,348, down about 3.3% over 24 hours. Crypto Fear and Greed sat at 9 (Extreme fear), unchanged from yesterday. The ETF daily flow print was about -$231.4 million. That is context, not a trading idea.

Put that next to today's Fortune reporting: Amazon and Meta are still talking about ending the Muse shopping block, with ads and search presentation as the sticking points. No deal, no official switch. If you sell on Amazon or expect Muse traffic this Cyber Week, wait for an official product change before you rewrite budgets. Tomorrow is Thanksgiving and Amazon's reported Victoria's Secret third-party cutoff; Friday is Black Friday.
```

- reasoning: 草稿硬约束：引用至少 1 个 market_snapshot 数据点，并标明抓取时美股仍为 closed、数字是周二收盘/开盘前。不写投资建议。把 Muse 谈判和黑五日历连起来，强调尚未有官方开关。补位电商赛道在节日窗口的执行提醒。

## 跨领域机会

- **AI 前沿 × 电商自动化**：Amazon 与 Meta 据报在谈 Muse 重返 Amazon，分歧正在广告展示和搜索排序——这正好对应卖家关心的流量入口会不会被 agent 绕开广告。在协议落地前，不要改预算；可先核对自己站点对 agent 流量的放行/拦截，以及 Shopify Agentic checkout 开关（昨日已写，不重复当选题）。Adweek 引 Human Security 称 Cyber Week 智能体流量或达去年 150 倍，数字未经原始报告复核。
- **广告平台规则 × 创意/商品数据**：12 个非美市场的 Shopping 促销标改要 schema.org 双价格，叠加 11/22 的 sale_price 持续时间「不应超过 30 天」：大促前要同时查标记和促销窗，而不是只改 feed 里的一个字段。美国口径仍不同。

## 本周表现摘要

- 周期：2026-11-18 ~ 2026-11-25
- Typefully 不可用，发布量/曝光待补。
- insights: Typefully 不可用，本周无曝光数据。选题连续几天落在平台官方帮助页/Changelog 的可改字段，而不是工具目录。今日 Google 家族已用满 2 个硬题（schema.org 促销标 + 12 月核心更新/生成式 AI 控件），ads_labels 与 Video reach 只进必读。D4 连续多日为 0（官方 changelog 仍为 11/18 v1.2.3）。

## 系统建议

### info_sources
- promote:
  - Google Search Central / developers.google.com/search — 11/24 官方排名专区、生成式 AI 控件和 Status Dashboard 预告均被打开并进入今日选题与必读（high）
  - PPC Times — 帮助页监测在 11/24–11/25 捕捉到 sale annotation schema、ads_labels 150、Conversion Lift 措辞和 Video reach 升级，其中前两项已用官方页复核（high）
  - Google Merchant Center Help — 今日两条 Google 硬题的原文都在帮助页，而不是新闻稿（high）
- demote:
  - Reddit RSS — 本轮全部 429/404，连续多日 0 条窗内帖（high）
  - The Batch / Anthropic / xAI / 部分中文卖家源 RSS — 持续 404 或失败；xAI 与 Anthropic 改走官方页面更稳（medium）
  - X search_news（共享通道） — 本轮 4 次查询均 429，未计入读取（medium）
- add:
  - Google Search Status Dashboard / 文档更新 RSS — 官方已把核心更新预告放到 Dashboard，并提供 RSS/Atom（high）
  - PPC Times 帮助页监测 — 与 PPC Land 互补，擅长捕捉 Merchant Center / Google Ads 帮助页静默改句（high）
  - Search Engine Roundtable — 向 Google 求证 12 月核心更新尚未开滚，补上了 Dashboard 状态文案可能造成的误读（medium）

### topic_library
- archive:
  - （无）
- add:
  - Shopping 促销标的 schema.org 双价格要求（非美 12 市场） — 官方帮助页已写进 Structured data 句，黑五前可执行（high）
  - Google 核心更新预告机制 + Search 生成式 AI 控件 — 11/24 新文档专区，Search Console 与 robots.txt 都有可改开关（high）
  - ads_labels 150 次上限（动态再营销） — 官方规格已改，但因 Google 家族配额今日未进选题（medium）

### 跳过与限制
- Typefully / Exa 跳过；Channel D / BDC 停用；冷邮 archive 跳过；pending 根目录旧条目未自动升题。
- Writer 全流水线未跑；未自动发帖；不通知 xhs / x / wechat，除非 Alex 明确点题。
- x.ai/changelog/bot 仍为 11/18 v1.2.3，D4=0。

