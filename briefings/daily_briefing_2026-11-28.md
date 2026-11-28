# ContentOS Daily Briefing -- 2026-11-28

- generated_at: 2026-11-28T14:24:50Z（America/New_York：2026-11-28 09:24 EST）
- pass: saturday-9am-ET-refresh-no-BDC-post-researchy
- raw_material_count: 351（RSS 窗内去重 279 + 官方索引/帮助页与打开文章约 32 + X search_news 4 次约 40 条，含重叠；Typefully/Exa 跳过；Channel D 停用）
- channel_d: disabled_by_alex_2026-11-03 · D4=0
- must_reads: 14 · also: 13 · topics: 2 · drafts: 3

## 发布策略

今日是周六（America/New_York），黑五周 11/19–11/30 的第十天，昨天是黑五，周一 11/30 是 Cyber Monday。市场快照抓取于约 9:14am ET（2026-11-28T14:14:37.514Z），其时美股字段均为 marketState=closed；NVDA 150.49（0.7971%）/ SHOP 141.78（6.2819%）应视为周五（11/27）收盘，不是周六价格（周四感恩节休市，周五有交易）。BTC 约 59154.6（24h -3.780959708258579%），Crypto F&G=9（Extreme fear），CNN F&G=25，btcScore=23，ETF 每日净流入约 -389000000。优先发标准 Shopping 的 Promotion Mode（官方帮助页 18111661 已核），其次黑五促销页下线时用 404/410、不要 301 到首页（Search Central 11/27 文档已核）。Google 家族今日 2/2 满额，未再塞 Cart 最低价标签、悬停 CTA 或昨日付款窗口脊柱。Shopify 商家 changelog 11/26–11/28 无新帖；Grok Bot changelog 仍为 v1.3.0，D4=0，不复用既有脊柱。Channel D 停用。不要自动发帖。

## 今日选题

### 1. 标准 Shopping 活动现可排 Promotion Mode：赶在 Cyber Monday 前先核 tROAS 与预算，而不是临时手改出价

- theme_slug: `google-ads-promotion-mode-shopping-troas-cyber-monday-1128`
- admission: a+c · heat: high · format: 方法论
- tracks: 🎨 创意广告, 🛒 AI 电商自动化
- tags: 平台可改字段, 商家数字
- angle: 本轮已打开官方帮助页 answer/18111661。英文页当前写明：Promotion Mode 为 open beta，Supported for standard Search, Shopping, and Performance Max campaigns；只接受活动级 Target ROAS，不兼容 portfolio 策略或 shared budgets；窗口必须 3–14 天；tolerance 5%–90%（页上例子：500% 配 20% → 有效 400%）；可选 Extra daily budget，但 campaign total budget 不能用这笔加项，只能手动提高总额；若同时开了 Smart Bidding Exploration，两种 tolerance 会相加。结束后目标和预算自动回到基线；促销期间改 tROAS/预算要在 Promotion Mode 面板里改，以免把基线改乱。PPC Times 监测日是 11/23、文 11/25 更新，SEJ 11/27 才做英文页报道，并称德/法/西文页截至 11/27 仍只列 Search 与 PMax。今天是周六、周一是 Cyber Monday，3 天窗口刚好够排一档并在结束后自动恢复。30 分钟动作：1）在 Campaigns 里找出正在跑、且是活动级 tROAS、没有挂 portfolio/shared budget、也没有跑过 prior experiments 的标准 Shopping（以及如需一并排的 PMax/Search）。2）打开该活动 Settings → Budget and bidding optimization → Promotion mode，确认面板在，再决定是否勾选 Ramp up spend quicker on promotion dates。3）若要覆盖 Cyber Monday，把起止日排成 3–14 天（不要排成 1–2 天），先写下一个能接受的 tolerance，再决定要不要 Extra daily budget。4）非英文界面如果还看不到 Shopping，不要假设功能已在该语言账号生效，先以英文页和后台实际面板为准。不要把 beta 写成正式全量，也不要在促销期间去改面板外的基线 tROAS。
- reasoning: 命中 Admission (a)(c)：30 分钟可在活动 Settings 里打开 Promotion mode 面板、排 3–14 天窗口并设定 tolerance / 可选加预算；这是官方帮助页写明的活动级开关，不是融资或工具目录。platform_family: Google（今日 1/2；404/410 为 Search Central，计为 Google 家族第 2 条，满额后不再加购物车标签或昨日付款窗口脊柱）。官方页已打开。帮助页改句由 PPC Times 于 11/23 监测、SEJ 11/27 报道，theme_slug 未出现在昨日 topics[]。不复用昨日付款到账窗口或 11/26 AI Max/local promotions 脊柱。时效在于周一 Cyber Monday 仍可排进 3–14 天窗口。非 MCP、非 D4。Bingge 评分≥70。

### 2. 黑五促销页若已下线，用 404 或 410，不要把它们统一 301 到首页

- theme_slug: `google-search-404-410-retired-promo-pages-no-homepage-redirect-1128`
- admission: a+c · heat: medium · format: 方法论
- tracks: 🛒 AI 电商自动化, 🎨 创意广告
- tags: 平台可改字段
- angle: 本轮已打开 Google 11/27 写入 Search Central 的爬取错误指南。官方现文很具体：确认页面不是误删或搬迁之后，404/410 本身不会损害整站索引或排名，已抓取的 404 也不 meaningfully 消耗 crawl budget；410 通常被更少复查，但索引处理与 404 相同。真正会惹麻烦的是 soft 404：把已下线的促销页重定向到无关首页，或用 200 占位页、或在 robots.txt 里挡住这些 URL，让 Google 看不到 404/410。30 分钟动作：1）列出这次黑五已结束、不再有等价替换页的促销/活动 URL。2）从 sitemap 里去掉它们，但保持可抓取，服务器返回真正的 404 或 410，而不是 200 空页。3）只在有等价替换页（例如活动页并入常驻产品页）时用 301；不要图省事一律跳到首页。4）对仍有外链或广告点击的旧 URL，用 URL Inspection 看实时代码是否就是你想返回的状态码。不要把「不用修每一个 404」理解成可以忽视误删的在售页，也不要把 410 写成会改变排名的新加分项。
- reasoning: 命中 Admission (a)(c)：30 分钟可改的是已下线促销 URL 的 HTTP 状态码、sitemap 与是否错误 301 到首页；这是 11/27 官方文档写明的处理规则。platform_family: Google（今日 2/2，与 Promotion Mode 共用家族配额，满额；不再加入 Cart 最低价标签或悬停 CTA）。官方文档已打开，SEJ/SEW 为支持。未与昨日 theme_slug 冲突，也不复用 11/25 的 12 月核心更新预告或 11 月更新「look-alike」分析。非 MCP、非 D4。黑五刚过、促销页批量下线是今天用得上的时机。Bingge 评分≥70。宁缺毋滥：不为此再凑第 3 条弱测试题（Cart 标签、ChatGPT 促销价、Bing Buy now 均无官方可改字段）。

## 今日必看

### 1. [Google Ads 官方帮助页《About Promotion Mode》现将标准 Shopping 与 Search、Performance Max 并列列入支持范围，可在 3–14 天促销窗内临时放宽 Target ROAS 并可选加每日预算](https://support.google.com/google-ads/answer/18111661?hl=en)

- event_id: `google-ads-promotion-mode-shopping-campaigns-1123` · Google Ads Help · 2026-11-27T19:57:15Z · age_hours=18 · 🎨 创意广告
- 本轮已打开官方帮助页 support.google.com/google-ads/answer/18111661。页上写明 Promotion Mode 为 open beta；Supported for standard Search, Shopping, and Performance Max campaigns；只支持活动级 Target ROAS，不兼容 portfolio bid strategies 或 shared budgets；促销窗必须 3 到 14 天；Target ROAS tolerance 可在 5%–90% 之间（页上的例子：500% tROAS、20% tolerance → 有效目标 400%），可选 Extra daily budget，活动总预算则不能用这笔加项、需手动提高总额。结束后目标和预算自动回到促销前设置。设置路径：Campaigns → 活动 Settings → Budget and bidding optimization → Promotion mode 面板，勾选 Ramp up spend quicker on promotion dates。PPC Times 写其于 11/23 监测到帮助页加入 Shopping，并于 11/25 更新文章；SEJ 11/27 19:57 UTC 报道同一帮助页，并称截至 11/27 德/法/西文页面仍只列 Search 与 Performance Max，英文页未写 Shopping 是何时加上的。本轮以英文官方页当前措辞为准。不要把非英文页当成已经同步，也不要把该功能写成已出 beta。
- 补充：[SEJ 11/27：英文帮助页现将标准 Shopping 列入 Promotion Mode beta，并复述 3–14 天窗口、tolerance 与结束后自动恢复](https://www.searchenginejournal.com/google-adds-shopping-campaigns-to-promotion-mode-eligibility/599279/)
- 补充：[PPC Times：帮助页改句监测日为 11/23，文章 11/25 更新；并称 PMax 的 Smart Bidding Exploration 现也写到 Shopping inventory（此句以 PPC Times 转述为准，官方页正文写的是 Exploration 驱动、示例是 search queries）](https://ppctimes.com/news/google-ads-promotion-mode-shopping-campaigns)

### 2. [Google Search Central 11/27 更新爬取错误指南：已抓取的 404 不占有意义的 crawl budget；410 通常会被更少复查；不要把删除页重定向到无关首页或用 robots.txt 挡住](https://developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors)

- event_id: `google-search-central-404-410-guidance-1127` · Google Search Central · 2026-11-27T20:26:24Z · age_hours=17 · 🛒 AI 电商自动化
- 官方 Search updates 在 November 27 两条相关记录：Expanded guidance on handling 404 errors（把原 Search Console 帮助中的 404 说明并入 crawling errors troubleshooting guide），以及把 2005 年博文里仍有效的 sitemap 说明迁到现行文档（嵌套 sitemap index 不受支持、HTML sitemap 不能提交到 Search Console）。本轮已打开 developers.google.com/search/docs/crawling-indexing/troubleshoot-crawling-errors。官方现文：404/410 是正常做法，不会触发 manual action，也不会损害站点整体索引或排名；未知/拼错 URL 的 404 一般可忽略；与 5xx/429 不同，404 和 410 不会降低 crawl capacity，已抓取的 404 也不 meaningfully 消耗 crawl budget；410 通常导致更少复查，但索引上 404 与 410 同等处理；删除的 URL 应从 sitemap 去掉，但不要用 robots.txt 挡住，否则 Google 看不到 404/410、难以移出索引；不要把已删除页重定向到无关首页或放占位内容，否则可能被当成 soft 404，只有等价替换页才用 301。SEJ 与 Search Engine Watch 11/27 均报道了这次文档合并。（SEJ RSS 时间为 2026-11-27T20:26:24Z。）
- 补充：[Google Search updates，November 27：Expanded guidance on handling 404 errors；同时迁入仍有效的 2005 sitemap 说明](https://developers.google.com/search/updates)
- 补充：[SEJ 11/27：404 指南迁入 Search Central，并强调 410 复查更少、索引处理与 404 相同](https://www.searchenginejournal.com/google-404-guide-410-crawl-frequency/599287/)
- 补充：[Search Engine Watch 11/27：不要修掉每一个 404，也不要把删除页重定向到无关首页](https://searchenginewatch.com/google-404-errors-dont-all-need-fixing/)

### 3. [Google Ads 帮助页《About payment processing times》将韩国预付合作方写为 Toss（previously LGU+），并给出各付款方式到账窗口（昨日选题，今日不复用脊柱）](https://support.google.com/google-ads/answer/9436113?hl=en)

- event_id: `google-ads-payment-processing-times-toss-lgu-1127` · Google Ads Help · 2026-11-27T12:00:00Z · age_hours=26 · 🎨 创意广告
- 昨日已打开官方帮助页 answer/9436113。Toss（previously LGU+）预付应在 3 个工作日内入账；银行账户/direct debit 最多约 5 个工作日（原文 upto）；电汇通常 5 个工作日、个别可到 30 天；NetBanking 通常 24 小时、有时 2–5 个工作日；信用卡通常立即、最多 24 小时。PPC Times 称监测到改句且 Toss 旧句为 24 小时——旧句对比只归 PPC Times。今日是黑五次日、距 Cyber Monday 还有两天，账单窗口仍然有效，但不复用昨日选题脊柱。
- 补充：[PPC Times 11/27：监测到帮助页改句，并将合作方从 LGU+ 改为 Toss](https://ppctimes.com/news/google-ads-payment-processing-times-toss-lgu)

### 4. [Search Engine Watch：Google Cart 在已加购商品上测试「Lowest price in 30 days」标签，点击可打开价格历史图](https://searchenginewatch.com/google-cart-now-highlights-products-at-their-lowest-price/)

- event_id: `google-cart-lowest-price-30-days-label-1127` · Search Engine Watch · 2026-11-27T12:06:49Z · age_hours=26 · 🛒 AI 电商自动化
- Sachin Patel 11/27 报道：他把商品加入 Google Cart 后再次打开，看到「lowest price in 30 days」标签，点击后出现价格历史图。作者猜测这是在提醒用户现在价格较好、促成转化，并提到此前 Google 已测试过购物车未结商品通知；文中写明这是猜测，Google 没有解释为何测试。本轮已打开 SEW 原文。没有官方帮助页确认，也没有写出卖家可以改的字段或报名入口。不要把该标签写成已全量上线，也不要把它等同于 Merchant Center 的 30 天最低价/促销标规则。

### 5. [Search Engine Watch：ChatGPT 页面底部的 sponsored ads 正在测试展示促销价](https://searchenginewatch.com/chatgpt-tests-sale-prices-in-sponsored-ads/)

- event_id: `chatgpt-sponsored-ads-sale-price-test-1127` · Search Engine Watch · 2026-11-27T09:26:07Z · age_hours=28 · 🎨 创意广告
- Sachin Patel 11/27 报道：ChatGPT 底部 sponsored ads 通常只有标题、有时有描述和 Learn more / Shop now，当天他看到广告上出现了价格（含促销价样式）。文章同时回顾近日测试过 Shop now 与广告下方 Ask 按钮。本轮已打开 SEW 原文。文中没有给出广告主后台可改字段，也未引用 OpenAI 官方文档。不要把这次目击写成可全量配置的官方功能。

### 6. [Search Engine Watch：Google Shopping 广告测试悬停后才显示 Visit / Shop now 按钮，并带动画](https://searchenginewatch.com/google-shopping-ads-hide-visit-and-shop-now-buttons-until-hover/)

- event_id: `google-shopping-ads-hover-visit-shop-now-1126` · Search Engine Watch · 2026-11-26T15:32:31Z · age_hours=46 · 🎨 创意广告
- Sachin Patel 11/26 报道并附视频：Shopping 广告上的按钮一开始是隐藏的，鼠标悬停后才以动画出现 Visit / Shop now，点击后进入广告主网站。作者写明不确定这是新测试还是早已存在但未被注意，Google 未确认，可能只对部分人展示。本轮已打开原文。没有广告主可开关的官方说明，不升选题。

### 7. [Search Engine Watch：Bing Shopping 广告再次测试 Buy now 按钮，作者点击后进入网站购物车页](https://searchenginewatch.com/bing-brings-back-buy-now-button-on-shopping-ads/)

- event_id: `bing-shopping-ads-buy-now-button-returns-1126` · Search Engine Watch · 2026-11-26T15:06:34Z · age_hours=47 · 🎨 创意广告
- Sachin Patel 11/26 报道：Bing Shopping 广告再次出现 Buy now，他点击后被带到该网站的购物车页；称 2025 年也曾见过类似测试，这次已连续看到几天。作者猜测可能要推开，但写明只是猜测。本轮已打开原文。没有 Microsoft Advertising 官方说明或可配置字段。窗内边缘（约 47 小时）。

### 8. [PPC Land：澳大利亚竞争与消费者委员会在黑五提醒，企业仍对自家聊天机器人/AI agent 的表述负责；肯尼亚书面要求支付前有人类批准；纽约州长签署对内置 AI 同伴玩具的五年禁令](https://ppc.land/regulators-tell-ai-shopping-agents-to-ask-first-as-new-york-bans-chatbot-toys/)

- event_id: `accc-ai-agent-liability-ny-chatbot-toys-ban-1128` · PPC Land · 2026-11-28T06:18:42Z · age_hours=8 · 🛒 AI 电商自动化
- Luís Rijo 11/28 汇总 11/27 黑五当天监管新闻。ACCC 媒体稿（文中称为 128/26）主席 Gina Cass-Gottlieb 提醒消费者在让 AI agent 代购前设置批准点和支出上限，并称企业若违反消费者法，仍对 agent 向购物者说的内容负责；稿中点名澳大利亚市场上的 Meta Muse、OpenAI ChatGPT dots 和 Google Tasks。肯尼亚数据保护办公室书面要求 agent 在付款前获得有记录的人类批准。纽约州长签署对带内置 AI 同伴的玩具的五年禁令。本轮已打开 PPC Land 长文，未能打开 ACCC 128/26 原文页（返回 404），以上细节来自已打开的转述，不把二手稿号当成已核原文。卖家若要落到 30 分钟，先核对自己站点/客服机器人的商品与价格表述，以及是否在纽约销售带 AI 同伴的玩具；不要把各国规则写成同一条已生效的全球禁令。

### 9. [PPC Land：SEO 顾问认为 Google 11 月核心更新（11/10–11/24 结束）打击最重的是近模板化/未经审核的 AI 批量页面和部分线索站，品牌与主产品页相对更稳](https://ppc.land/look-alike-pages-hit-hardest-in-googles-november-update-consultants-say/)

- event_id: `google-november-2026-core-update-lookalike-pages-analysis-1128` · PPC Land · 2026-11-28T08:51:02Z · age_hours=5 · 🤖 AI 前沿
- PPC Land 11/28 根据 Edward Sturm 11/27 播出的 The Edward Show 第 1241 集整理早期观察：Google 11 月核心更新于 11/24 06:03 PT 结束，时长约 13 天 20 小时。顾问点名损失集中在海量近模板页面、未经审核的 AI 撰写页，以及金融/健康/法律等线索站；主产品和品牌页相对稳住。文中引用 Sturm 提到 Reddit 估计月度 Google 点击下降的数字，并提醒 Google 自己的建议是更新结束后再等一周再读数——对这次更新而言，那一周正覆盖黑五。Google 没有列出针对的系统或内容类型。12 月核心更新仍为预告、尚未开滚（11/25 已作选题，今日不复用该脊柱）。本轮已打开 PPC Land 长文，不是 Google 官方效果说明。

### 10. [Search Engine Roundtable：Bing AI Mode 里的广告更难与自然结果区分开](https://www.seroundtable.com/bing-ai-mode-ads-differentiate-42625.html)

- event_id: `bing-ai-mode-ads-blending-organic-1127` · Search Engine Roundtable · 2026-11-27T12:51:00Z · age_hours=25 · 🎨 创意广告
- Barry Schwartz 11/27 7:51am ET 发文，引用截图称 Bing AI Mode 结果里的广告不再带原来的描边，看起来更混进 AI 回答。文章认为这与微软长期以来弱化广告与自然结果边界的做法一致。昨日已列入必读，本轮仍在 48h 窗，不升新选题。

### 11. [Search Engine Roundtable：Microsoft Advertising 的广告出现在 Copilot 里](https://www.seroundtable.com/microsoft-advertising-ads-in-copilot-42629.html)

- event_id: `microsoft-advertising-ads-in-copilot-1127` · Search Engine Roundtable · 2026-11-27T12:00:00Z · age_hours=26 · 🎨 创意广告
- Barry Schwartz 11/27 发文称 Microsoft Advertising 的广告出现在 Copilot 中。昨日已列入必读，本轮仍在 48h 窗。没有给出广告主新的报名开关说明，不升选题。

### 12. [PPC Land：WebMD Ignite 为医院投放 ChatGPT 广告，但谁能进场仍由 OpenAI 决定](https://ppc.land/webmd-ignite-runs-chatgpt-ads-for-hospitals-but-openai-decides-who-gets-in/)

- event_id: `chatgpt-ads-webmd-ignite-hospitals-openai-gates-1126` · PPC Land · 2026-11-26T19:56:05Z · age_hours=42 · 🎨 创意广告
- PPC Land 11/26 报道 WebMD Ignite 为医院投放 ChatGPT 广告，进场资格仍由 OpenAI 决定。昨日已列入必读，本轮仍在 48h 窗（约 42 小时）。属行业案例，不是卖家 30 分钟可改字段，不升选题。

### 13. [The Neuron：OpenAI 修正 GPT-6.2 Astra / Sol 计费低估，用户额度消耗变快；稿件称不会追收此前少计的用量](https://www.theneuron.ai/news/gpt-6-2-usage-limits-billing-fix/)

- event_id: `openai-gpt62-billing-correction-limits-1127` · The Neuron · 2026-11-27T05:42:03Z · age_hours=32 · 🤖 AI 前沿
- The Neuron 11/27 新闻稿与当日摘要均报道：OpenAI 修正了 GPT-6.2 Astra 和 Sol 上线时的计费低估。修正后，同样任务在 Astra 上大约快 40%、在 Sol 上大约快 25% 触及额度上限。X 公开新闻亦转述 ChatGPT/Codex 负责人 Thibault Sottiaux 的说明，并称不会追收上周少计部分。本轮打开了 The Neuron 新闻页与 11/27 日报。这是模型计费/额度变化，不是电商后台字段，进必读作 AI 前沿 awareness，不升选题。
- 补充：[The Neuron 11/27 日报亦收录同一计费修正](https://www.theneuron.ai/digest/everything-that-happened-in-ai-today-november-27-2026/)

### 14. [Shopify Storefront API 2027-01：查询 ProductVariant.storeAvailability 时可加 physicalStorefront: true，把仅供到店、不提供自提的门店一并返回](https://shopify.dev/changelog/storefront-api-2027-01-ask-storeavailability-for-physical-storefronts-with-physicalstorefront-true)

- event_id: `shopify-storefront-api-2027-01-physicalstorefront-1127` · Shopify Developer Changelog · 2026-11-27T17:00:00Z · age_hours=21 · 🤖 AI 前沿
- Shopify 开发者 changelog 11/27 17:00 UTC：Storefront API 2027-01 为 ProductVariant.storeAvailability 增加可选参数 pickUpEnabled（默认 true）和 physicalStorefront（默认关闭），并在返回的 StoreAvailability 上增加对应字段。不改现有自提行为：不传新参数时，结果仍只含自提点，与 2026-10 及更早一致。只有需要展示到店门店的客户端才要加 physicalStorefront: true。售罄且不提供自提的关闭/无货门店不会返回；自提点售罄时仍会以 available: false 出现。本轮已打开官方 changelog。这是给自定义店面/应用的 API 变更，普通商家后台没有新开关，故不升选题。

## 延伸阅读

### 1. [Grok Bot 官方 changelog 仍为 11/24 的 v1.3.0，本轮未见更新版本](https://x.ai/changelog/bot)

- x.ai Changelog · 2026-11-24T14:45:00Z · age_hours=95 · 🤖 AI 前沿 · 硬窗口外延伸参考；本轮复核无新版本
- 本轮再次打开 x.ai/changelog/bot，页顶仍是 Latest v1.3.0 · Nov 24, 2026（Slack 交接、restock alerts、组织域名控件等）。没有 11/25–11/28 的新版本条目。昨日已出 48h 必读窗，今日只作延伸，不复用 11/26 的 v1.3.0 选题脊柱。D4=0。

### 2. [Shopify 商家 changelog 在 11/26–11/28 没有新帖，最新仍是 11/25 的拒付四条](https://changelog.shopify.com/)

- Shopify Changelog · 2026-11-25T17:00:00Z · age_hours=69 · 🛒 AI 电商自动化 · 硬窗口外延伸参考；本轮复核无新商家 changelog
- 本轮打开 changelog.shopify.com 与 feed.xml，最新条目日期仍是 Wed, 25 Nov 2026 12:00:00 -0500 的四条拒付相关更新（Agentic 订单证据、员工通知、支付核验证明、AI 撰写回复）。这些帖已出 48h 必读窗，且 11/26 已作选题，今日不复用脊柱。

### 3. [iPullRank：黑五周期间，AI 购物答案里玩具品类的 best-of 列表链接占比曾从 46% 升到 65%，品牌站没有跟着抬升（昨日选题，已出必读窗）](https://ppc.land/best-of-lists-climb-to-65-of-ai-black-friday-toy-links-ipullrank-finds/)

- PPC Land / iPullRank · 2026-11-25T19:43:35Z · age_hours=66 · 🛒 AI 电商自动化 · 硬窗口外延伸参考；昨日选题不复用
- PPC Land 11/25 转述 iPullRank 11/24 报告，看的是 2025 年黑五周，不是 2026 直播数据。昨日已作选题。现已出 48h 必读窗，仅作延伸。2026 数据要到 Cyber Monday 之后。

### 4. [Amazon Ads：MCP Server 将于 12/8 起可选支持 MCP 协议 2026-07-28，旧版本继续可用（已出必读窗）](https://ppc.land/ai-agents-linked-to-amazon-ads-get-an-optional-upgrade-on-december-8/)

- PPC Land · 2026-11-25T20:34:12Z · age_hours=65 · 🛒 AI 电商自动化 · 硬窗口外延伸参考
- PPC Land 11/25 报道该可选升级，无关闭日期。昨日必读，现已出窗，仅作延伸。不要写成强制升级。

### 5. [Google 12 月核心更新仍为预告、尚未开滚（11/25 选题，已出必读窗）](https://www.seroundtable.com/google-december-2026-core-update-42615.html)

- Search Engine Roundtable · 2026-11-24T15:20:00Z · age_hours=95 · 🤖 AI 前沿 · 硬窗口外延伸参考；不复用 11/25 选题脊柱
- Search Engine Roundtable 11/24 报道 Google 预告 December 2026 core update，focuses on complex queries and personalization，当时写明尚未开滚。11/28 PPC Land 在 11 月更新分析文中再次提到该预告。今日不复用该脊柱。

### 6. [Google Ads AI Max for Search 的 text guidelines 与不必关闭即可用的控件（11/26 选题，已出必读窗）](https://ppctimes.com/news/google-ads-ai-max-controls-without-turning-off)

- PPC Times · 2026-11-26T11:41:59Z · age_hours=50 · 🎨 创意广告 · 硬窗口外延伸参考；昨日选题不复用
- PPC Times 11/26 监测到三份 AI Max 帮助页更新。昨日已作选题并不再复用。按 11/26 11:41 UTC 计已出 48h 窗，仅作延伸。

### 7. [Merchant Center local promotions 必须可在店内核销（11/26 选题，已出必读窗）](https://ppctimes.com/news/merchant-center-local-promotions-redeemable-in-store)

- PPC Times · 2026-11-26T11:42:58Z · age_hours=50 · 🛒 AI 电商自动化 · 硬窗口外延伸参考；昨日选题不复用
- PPC Times 11/26 监测到政策页加注。昨日已作选题。现已出窗，仅作延伸。

### 8. [Search Engine Roundtable 介绍 Google Ads Search Insights 工具，作者写明这不一定是新功能](https://www.seroundtable.com/google-ads-search-insights-42626.html)

- Search Engine Roundtable · 2026-11-27T12:21:00Z · age_hours=26 · 🎨 创意广告 · 作者标明不一定是新功能
- Barry Schwartz 11/27 7:21am ET 介绍 Search Insights。昨日已放入延伸阅读，因为作者自己写这不一定是新功能。今日仍在 48h 窗，维持延伸，不升必读或选题。

### 9. [Search Engine Roundtable：有广告主在 Merchant Center 看到 Ads opportunities 带 new 标签](https://www.seroundtable.com/google-merchant-center-ads-opportunities-42621.html)

- Search Engine Roundtable · 2026-11-27T12:11:00Z · age_hours=26 · 🛒 AI 电商自动化 · 界面观察，无官方说明
- Barry Schwartz 11/27 报道界面观察，不是官方功能说明。昨日已作延伸，今日仍在窗内，维持延伸。

### 10. [Search Engine Watch：Bing Shopping 为 AI 商品推荐增加新的加载动画](https://searchenginewatch.com/bing-shopping-adds-new-loading-animation-for-ai-product-recommendations/)

- Search Engine Watch · 2026-11-27T12:34:37Z · age_hours=25 · 🎨 创意广告 · 界面观察，无卖家开关
- Sachin Patel 11/27 报道界面变化。没有广告主可改字段或官方说明，只作延伸。

### 11. [Modern Retail：品牌在本届 BFCM 把 Reddit 广告做成全漏斗，而不只是底部转化](https://www.modernretail.co/marketing/brands-and-retailers-are-taking-a-full-funnel-approach-to-reddit-holiday-advertising-this-bfcm/)

- Modern Retail · 2026-11-27T05:00:00Z · age_hours=33 · 🎨 创意广告 · 行业案例，非平台规则
- 11/27 行业案例，讲的是投放结构趋势，没有平台规则变更或可复核的官方字段。放延伸，不升选题。

### 12. [Latent Space：Clay 如何做 GTM Agents（Jeff Barg）](https://latent.space/p/how-clay-builds-gtm-agents-jeff-barg-head-of-ai/)

- Latent Space · 2026-11-26T23:02:48Z · age_hours=39 · 🤖 AI 前沿 · 延伸参考
- 11/26 播客/访谈，讲 GTM agent 搭建方法，不是电商平台规则。延伸参考。

### 13. [PPC Land：IAB Europe 给出版方一份 90 天计划，覆盖 AI 爬虫、授权与广告](https://ppc.land/iab-europe-gives-publishers-a-90-day-plan-for-ai-bots-deals-and-ads/)

- PPC Land · 2026-11-26T19:46:24Z · age_hours=42 · 🤖 AI 前沿 · 行业倡议，非卖家控件
- 11/26 行业倡议，对卖家没有立即的后台开关。放延伸。

## 推文草稿

### 草稿 1 · 新闻翻译 · hook: X 刚发布/更新了，对你意味着三件事

Google's Promotion Mode help page now lists standard Shopping campaigns alongside Search and Performance Max.

That matters this weekend because Cyber Monday is in two days, and the window has to be 3 to 14 days. If a standard Shopping campaign is already on campaign-level Target ROAS — not a portfolio strategy or a shared budget — you can schedule a lower target and, if you use an average daily budget, an optional extra daily amount. When the dates end, both settings go back on their own.

Three things to check in the next 30 minutes:
1) Open the campaign settings and look for the Promotion mode panel under Budget and bidding optimization.
2) If you plan to cover Monday, pick dates that actually fit 3–14 days. A one- or two-day toggle is not what the page describes.
3) If you also use Smart Bidding Exploration, the two tolerances add up. Write down the combined number before you save.

I opened the official English help page (answer/18111661). PPC Times flagged the Shopping line on Nov 23; SEJ reported it on Nov 27 and noted that some non-English pages still omitted Shopping. Treat the English page and the panel in your account as the source of truth, and remember it is still an open beta.

- tags: 🎨 创意广告, 🛒 AI 电商自动化
- reasoning: 补位周末最硬的官方控件：标准 Shopping 现可排 Promotion Mode，对着周一 Cyber Monday。用了本期有效 Hook「X 刚发布/更新了，对你意味着三件事」。数字和限制条件来自已打开的官方帮助页。与昨日付款窗口草稿不同。无震惊体，0 个感叹号。

### 草稿 2 · 方法论 · hook: 大部分人用 X 的方式是错的

Most people will clean up Black Friday promo URLs by redirecting everything to the homepage. Google's updated crawling guide says that is the move that creates a soft 404.

If a sale page is gone and there is no equivalent replacement, return a real 404 or 410, remove it from the sitemap, and keep it crawlable. Already-crawled 404s do not meaningfully use crawl budget. A 410 is usually recrawled less often, but Google treats 404 and 410 the same for indexing. Blocking those URLs in robots.txt, or serving a 200 placeholder, makes it harder for Google to drop them.

The 30-minute job is to list the promo URLs that actually ended, confirm the live status code with URL Inspection, and only use a 301 when there is a true replacement page.

- tags: 🛒 AI 电商自动化
- reasoning: 用了本期有效 Hook「大部分人用 X 的方式是错的」。动作来自 11/27 已打开的 Search Central 文档，避免把 410 写成排名加分。与昨日 AI 购物答案草稿不同。无震惊体，0 个感叹号。

### 草稿 3 · 跨领域连接 · hook: 把 X 和 Y 连起来看

This morning's market snapshot was taken around 9:14am ET on Saturday, when US cash markets are closed. NVDA 150.49 (+0.80%) and SHOP 141.78 (+6.28%) are Friday's close — the first session after Thanksgiving — not Saturday prices. The same snapshot shows BTC around 59,155 (24h -3.78%), Crypto Fear & Greed at 9, CNN Fear & Greed at 25, btcScore 23, and ETF daily net flow about -$389 million.

I am not reading that as a trading signal. I am reading it next to the weekend ad calendar: Cyber Monday is Monday, and if you want Promotion Mode on a standard Shopping campaign, the help page requires a 3- to 14-day window. Saturday is still early enough to schedule it so the dates cover Monday and then revert on their own.

- tags: 💰 加密×美股, 🎨 创意广告
- reasoning: 按硬约束引用 market_snapshot 的多个数据点（NVDA/SHOP 为周五收盘、BTC、F&G、btcScore、ETF 流入），并写明这是周六闭市快照，不是周六交易价。明确不做投资建议，把市场数字接到 Cyber Monday 与 Promotion Mode 窗口。用了有效 Hook「把 X 和 Y 连起来看」。

## 跨领域机会

- **Promotion Mode × Cyber Monday 3–14 天窗口**：英文官方帮助页已把标准 Shopping 列入 Promotion Mode。窗口不能短于 3 天，结束后自动恢复。今天是周六、周一是 Cyber Monday，仍来得及在符合条件的活动级 tROAS Shopping 上排一档，而不用周一临时手改出价。非英文帮助页可能还没同步，以账号里是否出现该面板为准。
- **AI 购物代理责任 × 站点聊天机器人话术**：ACCC 在黑五提醒：企业仍要对自家 AI agent / 聊天机器人向购物者说的内容负责，并点名 Muse、ChatGPT dots、Google Tasks。这和 ChatGPT 广告正在测试促销价是同一条线的两面：一边是广告展示价，一边是对话里的承诺。先核对话脚本和价格/库存话术，不要把二手媒体稿写成已核的法律意见。

## 本周表现摘要

- period: 2026-11-21 ~ 2026-11-28
- insights: Typefully 不可用，本周没有曝光学习。昨日选题（付款到账窗口、AI 购物答案 best-of 列表）均不复用。今日以官方 Promotion Mode 支持标准 Shopping（对着 Cyber Monday）和 404/410 退休页处理为主，宁缺毋滥只出 2 条选题。Google 家族 2/2 满额。
- winning_hooks: X 刚发布/更新了，对你意味着三件事, 大部分人用 X 的方式是错的, 把 X 和 Y 连起来看
- covered_topics: 见 daily_data.json（含昨日付款窗口与 AI 购物答案选题，今日均不复用）

- published_this_week: Typefully MCP 不可用，已跳过 Step 1-3 的曝光学习；未改写 profile_recent.md。

## 系统建议

### info_sources

**promote**

- Google Ads Help（About Promotion Mode, answer/18111661）（high）：今日硬题原文在该页，且可直接核 Shopping / tROAS / 3–14 天窗口
- Google Search Central（crawling errors troubleshooting + Search updates）（high）：11/27 官方把 404/410 指南并入 Search Central，是今日第二条硬题的原文
- Search Engine Journal / Search Engine Watch / PPC Times（high）：SEJ 11/27 报道 Promotion Mode 与 404 文档；SEW 提供窗内 Shopping/ChatGPT/Bing 界面测试；PPC Times 虽 RSS 404 但新闻页仍是帮助页改句的最早监测源

**demote**

- PPC Times RSS（/feed、/news/feed、/rss.xml、/atom.xml）（high）：本轮全部 404，只能靠打开新闻首页监测，RSS 条目已失效
- Reddit RSS（high）：本轮再次 SSL 握手超时，连续多日 0 条窗内帖
- 中文卖家源 RSS（雨果/AMZ123/亿邦/跨境眼）（high）：本轮均为 404，采集仍空

**add**

- Google Ads Help answer/18111661（Promotion Mode）固定打开（high）：非英文页可能滞后，英文官方页应列入每日必打开清单，尤其在大促窗口
- developers.google.com/search/updates（high）：11/27 404 与 sitemap 文档变更写在官方 changelog，比只看媒体转述更稳
- Search Engine Watch RSS（已通）（medium）：本轮提供多条窗内 Shopping / ChatGPT Ads / Bing 界面目击，可补 SER RSS 不稳时的缺口

### topic_library

**archive**: （无）

**add**

- Google Ads Promotion Mode 支持标准 Shopping（3–14 天 tROAS 放宽）（high）：官方帮助页已写明 Shopping，Cyber Monday 仍在可用窗口内
- 退休促销页用 404/410，禁止无关首页 301（soft 404）（high）：11/27 Search Central 文档合并，黑五后批量下线页可执行


