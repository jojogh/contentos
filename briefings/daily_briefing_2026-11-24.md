# ContentOS Daily Briefing — 2026-11-24

- generated_at: 2026-11-24T14:28:46.283532Z（America/New_York：2026-11-24 09:28 EST）
- pass: tuesday-9am-ET-refresh-no-BDC-post-researchy
- raw_material_count: 373（RSS 窗内去重 295 + 官方页 16 + 打开文章/帮助页 12 + X search_posts_all 2 次共 50 条；search_news 3 次因共享通道 429 失败、未计读取）
- channel_d: disabled_by_alex_2026-11-03 · D4=0
- must_reads: 18 · also: 13 · topics: 3 · drafts: 3

## 发布策略

今日（周二）是黑五周 11/19–11/30 的第六天，距黑五 11/27 还有 3 天，11/26 是感恩节。市场快照抓取时（约 9:20am ET）股票字段仍为 marketState=closed，价格应视为周一收盘/开盘前，不是周二开盘价。优先发 Shopify ChatGPT agentic checkout（官方 Changelog + 帮助页，默认开启，有后台路径），其次 Google 返回键劫持 FAQ（官方 11/23 更新），以及 Amazon 11/26 下架第三方 Victoria's Secret（卖方通知经 LinkedIn 流出，本轮未打开官方帮助页，角度写成条件性操作）。Pinterest×Microsoft 官方稿无上线日，只进 must_reads。D4=0。

## 今日选题

### 1. Shopify 已对 ChatGPT 打开 agentic checkout，符合条件的店铺默认开启：黑五前先到 Sales channels > Agentic 核对开关

- theme_slug: `shopify-chatgpt-agentic-checkout-default-on-1124`
- admission: a+c · heat: high · format: 方法论
- tracks: 🛒 AI 电商自动化, 🤖 AI 前沿
- tags: 平台可改字段
- angle: 本轮已打开 Shopify 11/23 Changelog 和帮助页 Selling on ChatGPT。官方确认：Direct checkout 改名为 agentic checkout，并已对 ChatGPT 开放；agent 用的是店铺自己的 Shopify checkout，订单进 admin。符合条件且打开了 Manage for me 或 Automatically enable new channels 的店铺默认开启，既有 opt-out 仍有效。30 分钟动作：1）Shopify admin → Sales channels > Agentic；若显示 Manage for me，先切到 Manual；点 ChatGPT，看 Agentic checkout 和 Shopify Catalog access 现在是开还是关，再决定是否 Save。2）若只想禁止 agent 用 UCP/WebMCP 代客下单，关 Agentic checkout 即可；商品仍可通过 Catalog 出现在 ChatGPT，Shop skill / Shop App for ChatGPT 的下单也不受影响。3）若连 Catalog 分发都要停，关 Shopify Catalog access，官方说最多可能要 7 天才停止共享；这也不等于商品不会被爬虫发现。上线前再核：是否向美国顾客销售、Catalog 资格、Settings > Policies 里三项政策是否填齐、商品描述前 6,000 字符是否包含法律披露。不要写成「Shopify 强制所有店铺都被 ChatGPT 代下单」，也不要写成「关掉 checkout 就从 ChatGPT 消失」。官方写明无额外销售费用，只付常规支付处理费。
- reasoning: 命中 Admission (a)(c)：Agentic checkout / Catalog access 是 30 分钟可改的后台开关，且默认开启会改变结账路径。platform_family: Shopify（今日 1/2）。官方 Changelog + 帮助页均已打开，不是只转述二手稿。未复用本周 shopify-flow / IP allowlist / custom apps / draft-order 等 slug。非 MCP、非 D4。Bingge 评分≥70。黑五还有 3 天，默认开启是硬新闻不是工具安利。

### 2. Google 11/23 为「返回键劫持」补了官方 FAQ：广告代码不是挡箭牌，Discover 和社交来源在浏览器里同样适用

- theme_slug: `google-back-button-hijacking-faq-ad-code-no-shield-1124`
- admission: a+c · heat: high · format: 方法论
- tracks: 🎨 创意广告, 🛒 AI 电商自动化
- tags: 平台可改字段
- angle: 本轮已打开 Google Search Central 11/23 文档更新和 Spam policies 原文（页脚 Last updated 2026-11-23 UTC）。政策定义没改，改的是 FAQ。官方原句要点：站长仍可引入广告平台托管代码，Google 只对实际出现 back button hijacking 的页面采取行动；Discover 适用；用户从社交等非搜索渠道进入、在浏览器里返回时若被劫持，政策同样适用；open in app 不在范围内。PPC Land 补充该规则自 2026-06-15 起已执行，不要写成今天才开始执法。30 分钟动作：1）打开自己的广告落地页、Merchant / 促销页，以及会从 Discover 或社交流量进来的页，用手机和桌面点一次返回，看是否被插入中间页或锁在站内。2）如果劫持来自某个广告/联盟标签，先禁这个标签再复测，不要假定「这是广告代码所以 Google 不会罚」。3）把发现的问题记到页面或标签清单，黑五流量上来前先改。不要写成「Google 禁止所有第三方广告代码」。
- reasoning: 命中 Admission (a)(c)：官方把责任落在「实际出现劫持行为的页面」，30 分钟可测返回键并禁用出问题的标签。platform_family: Google（今日 1/2）。官方更新页 + 政策原文已打开。未复用昨日 surcharge / consumer_notice slug。非 MCP、非 D4。Bingge 评分≥70。

### 3. Amazon.com 据通知将于 11/26（感恩节）移除第三方 Victoria's Secret 商品：先查 NWD / Brand Representative 通知，下架据称不计入 Account Health

- theme_slug: `amazon-vs-nwd-removal-thanksgiving-1126-1124`
- admission: a+c · heat: high · format: 新闻评论
- tracks: 🛒 AI 电商自动化
- tags: 平台可改字段, 商家数字
- angle: 本轮已打开 PPC Land 11/23 原文。它引用的是 ASGTG 创始人在 LinkedIn 公开的 Amazon Services 卖家通知，本轮没有打开 Seller Central 原件或公开帮助页，所以角度里的通知原文都标明是「PPC Land 转述的通知措辞」，不是我直接读到的官方后台。通知称：2026-11-26 起，Victoria's Secret 不再允许第三方在 Amazon.com 上架，只保留持有该品牌 Brand Representative 角色的卖家；理由是 VS 只做 DTC、不走批发。PPC Land 还写：卖家可以在截止前卖完剩余库存或删除空 listing，Amazon 称此次移除不计入 Account Health Rating；通知指向 Resolve No Wholesale Distribution (NWD) errors 5465 and 6045，但该帮助页没有公开版本可核。30 分钟动作：1）在 Seller Central 通知和邮箱里搜 Victoria's Secret、No Wholesale Distribution、NWD、5465、6045，先确认自己有没有收到同类通知，不要只凭二手报道停售其他品牌。2）若通知属实且你有 VS 库存，赶在 11/26 前处理剩余单位或清空空 listing，并单独记下「这次移除据称不影响 AHR」，不要和普通政策违规混在一起看健康度。3）顺手扫一遍其他品牌有没有 10 月以来的 NWD 通知——PPC Land 说卖家当时已在另一家家喻户晓品牌上见过同类规则——但不要外推成「所有第三方品牌货都会在感恩节被下架」。在登录后台看到同一通知之前，不要把「全站点第三方 VS 下架」写成已由官方帮助页确认的全量规则。
- reasoning: 命中 Admission (a)(c)：若通知属实，11/26 会改变谁能上架该品牌，30 分钟可先查通知并处理库存。platform_family: Amazon（今日 1/2）。来源置信度：中；需后台复核后再写成确定性规则，当前为条件性操作候选。未复用昨日 Attribution 28 天或 Brand Store Agent slug。非 D4。未为凑满 5 条再加弱题。Bingge 评分≥70。

## 今日必看

1. [Shopify 把 Direct checkout 改名为 agentic checkout，并已对 ChatGPT 开放：符合条件的店铺默认开启](https://changelog.shopify.com/posts/manage-whether-ai-agents-can-buy-your-products-for-shoppers-through-chatgpt) — Shopify Changelog + Help Center · 2026-11-23T17:00:00Z · 21.5h · `shopify-agentic-checkout-chatgpt-default-on-1123`
   本轮已打开 Shopify 官方 Changelog（2026-11-23）和帮助页 Selling on ChatGPT。官方写明：Direct checkout 在所有 AI 渠道改称 agentic checkout，现已对 ChatGPT 开放；AI agent 可用店铺的 Shopify checkout 代客下单，订单照常出现在 admin。符合条件的店铺，在 Manage for me 或 Automatically enable new channels 打开时默认启用，既有 opt-out 仍有效，其他渠道设置不变。帮助页补充：需向美国顾客销售（店铺可在美国以外）、商品需符合 Shopify Catalog、须同意 Agentic Storefronts 补充条款，并在 Settings > Policies 填好服务条款、隐私政策和退款政策。默认关闭的情形：ChatGPT 的 Catalog 访问被关、Sales channels > Agentic 里 Automatically enable new channels 被关、或店铺在 Agentic plan。后台路径：Sales channels > Agentic → 如显示 Manage for me 先切到 Manual → ChatGPT → 开关 Agentic checkout → Save。关掉 agentic checkout 不会让商品从 ChatGPT 发现里消失，也不影响 Shop skill / Shop App for ChatGPT 的下单；完全不想被 Catalog 分发时，关 Catalog 访问最多可能要 7 天才能停止共享。官方写明在 ChatGPT 销售没有额外费用，只付常规支付处理费。法律披露写在商品描述前 6,000 字符；B2B-only 商品不支持。
   - 补充：[帮助页：Selling on ChatGPT（资格、默认开/关条件、后台步骤、Shop skill 不受影响、Catalog 关闭最多 7 天）](https://help.shopify.com/en/manual/online-sales-channels/agentic-storefronts/chatgpt)

2. [Google Search Central 于 11/23 给「返回键劫持」垃圾政策加了 FAQ：广告代码不是挡箭牌，Discover 和站外流量也算](https://developers.google.com/search/updates) — Google Search Central · 2026-11-23T00:00:00Z · 38.5h · `google-back-button-hijacking-faq-1123`
   本轮已打开 Google Search Central 文档更新页和 Spam policies 原文。11/23 更新写明：在恶意行为章节加入 back button hijacking FAQ，原因是回答关于该政策的常见问题。政策页戳记 Last updated 2026-11-23 UTC。官方 FAQ 五问五答：1）第三方广告平台代码若导致劫持，Google 并不禁止站长引入广告平台托管代码，只对实际出现劫持行为的页面采取行动；2）用户可通过 spam submission report 举报；3）该政策适用于 Google Discover，因为 Discover 是 Search 的一部分；4）用户从社交等非搜索渠道进入、在浏览器里返回时若被劫持，政策同样适用；5）网站打开外部应用、阻止回到原目的地的 open in app 不在范围内。PPC Land 11/23 稿补充：该规则自 2026-06-15 起已在执行。不要写成 Google 今天才开始禁止广告代码。发布时间按文档日 00:00 UTC，摘要中已注明为官方更新日期。
   - 补充：[Spam policies 原文（含 FAQ 五问，页脚 Last updated 2026-11-23 UTC）](https://developers.google.com/search/docs/essentials/spam-policies)
   - 补充：[PPC Land 对 FAQ 的拆解，并注明规则自 2026-06-15 执行](https://ppc.land/ad-code-is-no-shield-googles-back-button-spam-rule-hits-the-page/)

3. [亚马逊据通知将于 11/26（感恩节）从 Amazon.com 移除第三方 Victoria's Secret 商品，仅保留 Brand Representative 角色](https://ppc.land/amazon-blocks-third-party-victorias-secret-sellers-from-november-26/) — PPC Land（转述 Amazon Services 通知，经 LinkedIn） · 2026-11-23T19:48:16Z · 18.7h · `amazon-vs-nwd-third-party-removal-1126`
   本轮已打开 PPC Land 11/23 原文。它依据 ASGTG 创始人 Ephraim Rosenberg 当天在 LinkedIn 发布的、署名 Amazon Services 的卖家通知，本轮未打开 Amazon 官方帮助页或卖家后台原件。通知标题为 Victoria's Secret listings to be removed 2026-11-26 from Amazon.com，正文写 Starting 2026-11-26，Victoria's Secret is no longer eligible for third party sellers to list on Amazon.com；商品仍会在 Amazon store 出现，但只来自持有该品牌 Brand Representative 角色的卖家。给出的理由是 VS 只做 DTC，不通过批发商、分销商或第三方转售。PPC Land 称：受影响卖家可在截止日期前卖完剩余库存或删除空 listing；Amazon 说此次移除不计入 Account Health Rating；截止日落在感恩节、黑五前一天。通知还指向 Seller Central 帮助页 Resolve No Wholesale Distribution (NWD) errors 5465 and 6045，PPC Land 写它未能找到该页的公开版本。卖家在 10 月就曾报告过针对另一家家喻户晓品牌的 NWD 通知。不要写成「亚马逊将下架所有第三方品牌货」。来源置信度：中。

4. [Pinterest 官方宣布：符合条件的 Microsoft Advertising 活动可投放到 Pinterest 首页信息流、搜索和 Related Pins，起步市场不含欧洲](https://newsroom.pinterest.com/news/pinterest-microsoft-advertising-integration-2026/) — Pinterest Newsroom · 2026-11-23T19:27:24Z · 19.0h · `pinterest-microsoft-ads-inventory-1123`
   本轮已打开 Pinterest Newsroom 2026-11-23 原文。官方说 Microsoft Advertising 客户可通过自定义 contextual bidding model 进入 Pinterest 的 open-auction 库存，覆盖 home feed、search 和 related Pins，不需要新的购买工具；模型建立在 Pinterest 搜索查询、情境信号和第一方意图数据之上。起步市场是 North America、Australia 和 New Zealand。新闻稿未给上线日期、定价或合格活动类型名单。PPC Land 指出欧洲不在起步名单里。30 分钟内很难在后台验证开关是否已出现，故不作今日选题脊柱，只作必读。
   - 补充：[PPC Land 拆解：无上线日/定价/合格活动类型，欧洲再次缺席](https://ppc.land/pinterest-sells-feed-and-search-ad-space-through-microsoft-advertising/)

5. [HUMAN 称 BADBOX 3.0 高峰期每天约 400 亿次欺诈广告请求，约占其检测到的 CTV 流量 4% 以上](https://ppc.land/human-traces-up-to-40-billion-fraudulent-ad-requests-a-day-to-cheap-tv-boxes/) — PPC Land / HUMAN Security · 2026-11-24T00:02:50Z · 14.4h · `human-badbox-3-ctv-ad-fraud-1123`
   PPC Land 11/23–11/24 两篇报道均指向 HUMAN Security 11/23 发布的 BADBOX 3.0 调查。HUMAN 自称这是其公开披露过的、按 bid request 量计最大的广告欺诈行动，高峰约 40 billion 次/天，超过其检测系统所见 CTV 流量的 4%。PPC Land 提醒：bid request 不是成交，报告未说明其中多少被买走、广告主实际花了多少钱。黑五 CTV 预算上升时，这是投放质量信号，但不是平台可改字段。两篇 PPC Land 为同一事件，只占 1 条。
   - 补充：[PPC Land 续稿：BADBOX 与黑五 CTV 预算上升对照，同样引用 400 亿峰值](https://ppc.land/badbox-fakes-40bn-tv-ad-requests-a-day-as-black-friday-budgets-rise-up-to-30/)

6. [Microsoft Ads Liaison 澄清：11/18 博客所称出价模型升级并非单一切换日，夏季已开始滚动](https://ppc.land/microsoft-says-its-bidding-upgrade-started-in-summer-not-november-18/) — PPC Land（转述 Microsoft Ads Liaison） · 2026-11-23T21:07:02Z · 17.4h · `microsoft-ads-bidding-upgrade-no-single-golive-1123`
   PPC Land 11/23 报道 Microsoft Ads Liaison 发文澄清：11/18 博客里「decade 最大出价模型升级」没有单一 go-live 日期，相关改动自夏季起滚动，不应把 11/18 当作账户出价方式切换日。补充：5 次转化按账户级计算；没有转化数据的账户有四种起始策略而非一种；博客称「不建议」的 Maximum CPC 仍可通过 portfolio bidding 使用。这是对 11/18 选题的日期口径修正，不作为今日选题脊柱，也不复用当时的 theme_slug。本轮打开的是 PPC Land 转述，未打开 Microsoft 官方博客原文。

7. [Walmart Agent Gateway 已对 Meta Muse 开放：顾客可用 Agent Profile 设消费限额后代客购物（发布后曾短暂改口延期，又改回当天上线）](https://www.theverge.com/ai-artificial-intelligence/1039874/walmart-agent-gateway-meta-muse-black-friday) — The Verge · 2026-11-23T11:00:00Z · 27.5h · `verge-walmart-agent-gateway-meta-muse-1123`
   The Verge 11/23 11:00 UTC 报道 Walmart 将让 Meta Muse 通过 Agent Gateway / Sparky 找货并购买黑五商品；顾客在 Walmart 账户内设 Agent Profile，含消费限额、审批和购买历史。更新 1：Walmart 在见报后告知 Verge，上线推迟到 11/24。更新 2：Walmart 再次联系 Verge，称不再推迟，将于 11/23 当天推出。本轮未打开 Walmart 官方商户后台说明，也未独立复测 11/24 上午是否已对所有用户生效。这是消费侧入口，不是 Marketplace 卖家可改字段。与昨日同 event_id，摘要已按 Verge 后续更新改写。

8. [Google Ads 法国和意大利的监管运营附加费将于 2027-01-01 升至 3%，土耳其从 4.5% 降到 2.25%，按广告展示地计费](https://ppc.land/google-ads-surcharges-hit-3-in-france-and-italy-from-january-2027/) — PPC Land / Google Ads Help · 2026-11-22T19:30:39Z · 43.0h · `google-ads-fr-it-surcharge-3pct-jan2027-1122`
   昨日选题脊柱，今日仍在 48h 窗内，不复用 theme_slug。官方帮助页 answer/9750227 已在 11/23 轮打开：法国 2%→3%，意大利 2.5%→3%，土耳其 4.5%→2.25%，按展示地而非公司注册地计费，写明对合法定向产生的费用不退款。
   - 补充：[Google Ads 官方帮助页：Jurisdiction-specific surcharges](https://support.google.com/google-ads/answer/9750227)

9. [Merchant Center 新字段 consumer_notice：每个商品最多 7 条法律/安全/Prop 65 提示，提交第 8 条会覆盖第 1 条](https://ppc.land/merchants-who-send-8-google-checkout-warnings-lose-the-first-one/) — PPC Land / Merchant Center Help · 2026-11-22T17:24:56Z · 45.1h · `google-mc-consumer-notice-7-cap-1122`
   昨日选题脊柱，今日仍在窗内，不复用 theme_slug。官方帮助页确认最多 7 条，第 8 条覆盖第 1 条；帮助页写 Optional，UCP 指南对有监管警示要求的商品（如 Prop 65）写 mandatory，须并陈。

10. [往 Amazon Attribution 品牌里加 ASIN：批准需 4–7 个工作日，随后会重述过去 28 天历史数据，修正还要约三周](https://ppc.land/adding-asins-to-an-amazon-brand-restates-the-previous-28-days-of-data/) — PPC Land（摘录 Amazon Ads 帮助页） · 2026-11-22T18:31:12Z · 44.0h · `amazon-attribution-asin-restate-28d-1122`
   昨日选题脊柱，今日仍在窗内，不复用 theme_slug。帮助页原句来自 PPC Land 摘录；11/23 轮打开 Amazon Ads 帮助页时正文为空，口径仍标为二手摘录。

11. [Amazon Brand Store 点 Add page 会先打开 Builder Agent：可点 Add page without AI assistance 退出；All Deals 可能自动填最多 30 个折扣商品](https://ppc.land/amazon-routes-new-brand-store-pages-through-an-ai-agent-first/) — PPC Land（摘录 Amazon Ads 帮助页） · 2026-11-22T18:29:27Z · 44.0h · `amazon-brand-store-builder-agent-all-deals-1122`
   昨日选题脊柱，今日仍在窗内，不复用 theme_slug。步骤与限额来自 PPC Land 对帮助页的摘录，11/23 轮官方帮助页正文为空。

12. [Amazon 官方宣布：已签署协议购买 Decart Optimization Stack（DOS）技术，并引进其联合创始团队](https://ppc.land/amazon-agrees-to-buy-decarts-ai-chip-software-in-a-deal-reported-at-7-5bn/) — PPC Land / Amazon · 2026-11-23T19:35:14Z · 18.9h · `amazon-decart-dos-technology-agreement-1123`
   融资/技术收购，不作选题脊柱。Amazon 未公布价格；媒体报道约 75 亿美元。与卖家 30 分钟动作无关，保留为 AI 前沿必读。

13. [Google 发布 Google-Agent 流量说明：这是用户触发的抓取，一般忽略 robots.txt，站长可在 CDN/WAF 放行](https://developers.google.com/crawling/docs/google-agent) — Google 开发者文档 · 2026-11-23T13:12:32Z · 25.3h · `google-agent-crawler-guidance-1123`
   昨日必读，今日仍在窗内。PPC Land 另有 11/23 稿称 Google 记录了 12 个会忽略 robots.txt 的现有 bot，视为同一文档族的补充，不另占 event_id。
   - 补充：[PPC Land：Google documents 12 existing bots that ignore robots.txt](https://ppc.land/google-documents-12-existing-bots-that-ignore-robots-txt/)

14. [Practical Ecommerce：用三步检查独立站是否被 AI 爬虫挡住（robots.txt + 常见 UA 探测，工具不以官方 IP 复核）](https://www.practicalecommerce.com/test-your-ecommerce-site-for-ai-access) — Practical Ecommerce · 2026-11-23T13:14:40Z · 25.2h · `practical-ecommerce-ai-access-test-1123`
   昨日必读，今日仍在窗内。独立站可做的访问检查，但不是新的平台字段变更。

15. [Adweek：Amazon 称黑五体育转播有近 25% 更多广告主，shoppable ads 将出现在超 40% 的库存中](https://www.adweek.com/brand-marketing/) — Adweek · 2026-11-23T09:00:00Z · 29.5h · `adweek-amazon-shoppable-ads-bf-sports-1123`
   昨日必读，今日仍在窗内。品牌广告库存信号，无新的卖家必改字段。原条 URL 以 Adweek 站点为准；本轮未重打开 11/23 那篇的精确 permalink。

16. [Adweek：ChatGPT 的 agent 会自己写查询再把广告发出去，广告主看不到这些查询](https://www.adweek.com/brand-marketing/) — Adweek · 2026-11-23T06:00:00Z · 32.5h · `adweek-chatgpt-agent-writes-ad-queries-1123`
   昨日必读，今日仍在窗内。与今日 Shopify agentic checkout 相关但不是同一事件。本轮未重打开 11/23 那篇的精确 permalink。

17. [Import AI 482：华为 kernel 基准、空中无人机检测，以及国家实验室的 AI 科学基准](https://importai.substack.com/p/import-ai-482-huawei-kernel-benchmarks) — Import AI · 2026-11-23T14:11:17Z · 24.3h · `import-ai-482-1123`
   昨日必读，今日仍在窗内。AI 前沿期刊，无卖家 30 分钟动作。

18. [Anthropic 推出 Claude Ship：让 AI agents 审查、修复并批准代码变更](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/) — TechCrunch · 2026-11-23T22:05:50Z · 16.4h · `anthropic-claude-ship-1123`
   TechCrunch 11/23 报道 Anthropic 发布 Claude Ship，使 agent 能审查 PR、修代码并批准变更。AI 前沿产品发布，缺少电商 30 分钟动作，只进 must_reads。本轮打开的是 TechCrunch 索引/摘要，未打开 Anthropic 官方公告全文。

## 延伸阅读

1. [Google Merchant Center：sale_price 持续时间不应超过 30 天，否则可能拿不到删除线原价和促销标](https://ppc.land/merchant-center-sales-running-past-30-days-may-miss-googles-sale-badge/) — PPC Land / Merchant Center Help · 2026-11-22T09:30:00Z · 53.0h · 硬窗口外延伸参考；11/22 选题脊柱，今日不复用 slug

2. [YouTube Shorts 广告：点赞、评论、分享现在都能算 engaged-view conversion，也算 TrueView view](https://ppc.land/google-lets-a-like-stand-in-for-5-seconds-of-viewing-in-shorts-conversions/) — PPC Land · 2026-11-22T09:15:58Z · 53.2h · 硬窗口外延伸参考；11/22 选题脊柱，今日不复用 slug

3. [@cstanley 自述用 Grok Bot 翻 Amazon 历史订单找回未到账退款（金额未经证实）](https://x.com/cstanley) — @cstanley via X（11/22 简报） · 2026-11-22T01:30:26Z · 61.0h · 硬窗口外延伸参考；不复用退款对账 SOP slug。本轮未重抓原帖，未写具体 status URL。

4. [AWS Quick 上线 Meta ads AI 连接器：用自然语言建、管、分析 Meta 广告](https://www.adweek.com/brand-marketing/inside-awss-bid-to-be-a-brand-for-everyone-including-ai-agents/) — Adweek / AWS · 2026-11-22T01:59:13Z · 60.5h · 硬窗口外延伸参考

5. [Groundwork 研究称 351 个往年假日 deal 中 29.1% 并不比前 30 天更便宜；Amazon 称复核后 98% 持平或更低](https://ppc.land/amazon-faces-study-saying-29-of-351-holiday-deals-were-no-cheaper/) — PPC Land（研究报告日期 11/16，Amazon 回应更新 11/20） · 2026-11-23T21:14:26Z · 17.2h · 延伸参考：稿件在窗内，但研究与官方回应主体日期在窗外；两套口径必须并陈，不作选题

6. [OpenAI 与 Cisco 推出开源 Linux 运行时 Shirudo，用于打补丁时保护正在运行的系统](https://openai.com/index/introducing-shirudo) — OpenAI News · 2026-11-23T21:20:00Z · 17.1h · 延伸参考

7. [PPC Land：Google 对 Chrome AI agent 功能的改动让早期测试者的代码失效](https://ppc.land/googles-change-to-chromes-ai-agent-feature-breaks-early-testers-code/) — PPC Land · 2026-11-24T00:07:53Z · 14.3h · 延伸参考：开发者接口变更，非卖家字段

8. [x.ai/changelog/bot 仍为 2026-11-18 v1.2.3（工具权限与 routine 重连卡片），本轮打开官方页无更新](https://x.ai/changelog/bot) — x.ai Changelog · 2026-11-18T00:00:00Z · 158.5h · 硬窗口外延伸参考；今日 D4=0，不复用 v1.2.3 或退款对账 slug

9. [Practical Ecommerce：2026-11-24 新电商工具周刊（AI 可见性、测量、社媒购物、商品数据、Amazon 广告等）](https://www.practicalecommerce.com/new-ecommerce-tools-november-24-2026) — Practical Ecommerce · 2026-11-24T12:55:09Z · 1.6h · 工具目录，软降权，不进 topics

10. [Criteo：80% 的英国黑五购物者会从不熟悉的商店购买](https://ppc.land/80-of-uk-black-friday-shoppers-buy-from-unfamiliar-stores-criteo-finds/) — PPC Land / Criteo · 2026-11-23T20:51:27Z · 17.6h · 延伸参考

11. [DeepMind：用 agent 团队和形式化验证寻找更快的量子算法](https://deepmind.google/blog/finding-faster-quantum-algorithms-with-agents-and-formal-verification) — Google DeepMind · 2026-11-23T16:59:40Z · 21.5h · 延伸参考

12. [SEJ：分析 Bing AI 的 883,000 条引用，看它实际引用了什么](https://www.searchenginejournal.com/what-bings-ai-actually-cites-883000-citations-analyzed/595708/) — Search Engine Journal · 2026-11-24T13:00:08Z · 1.5h · 延伸参考

13. [Martech：ChatGPT ads 与 Google Ads 对比要点](https://martech.org/what-you-need-to-know-about-chatgpt-ads-vs-google-ads/) — Martech / Marketing Land · 2026-11-24T13:55:41Z · 0.6h · 延伸参考：分析稿，非平台政策变更

## 推文草稿

### 草稿 1（X 刚发布/更新了，对你意味着三件事）

Shopify just turned on agentic checkout for ChatGPT.

That means three things.

First, if your store is eligible and you left Manage for me or Automatically enable new channels on, the setting may already be on. You did not have to opt in.

Second, turning off Agentic checkout stops agents from completing checkout with tools such as UCP and WebMCP. It does not hide your products in ChatGPT, and it does not stop checkouts that use the Shop skill or the Shop App for ChatGPT.

Third, the official path is Sales channels > Agentic. If it says Manage for me, switch to Manual, open ChatGPT, and then save the switch you actually want.

Source: Shopify Changelog and the Selling on ChatGPT help page, November 23, 2026.

- format: 新闻翻译 · tags: 🛒 AI 电商自动化, 🤖 AI 前沿
- reasoning: 用 longterm 元 Hook「X 刚发布/更新了，对你意味着三件事」。英文草稿（@jojogh_007 发英文）。步骤与默认开启条件均来自本轮打开的 Shopify 官方页。不用震惊体，无感叹号。Typefully 不可用，无本周 winning/failing hooks。同时补位本周 underserved track「🤖 AI 前沿」。

### 草稿 2（大部分人用 X 的方式是错的）

Most people will read Google's new back-button FAQ as a problem for publishers only. That is the wrong way to use it.

Google said today it added an FAQ to its back button hijacking spam policy. The rule itself is not new.

The useful part is the liability line: you can still import code hosted by ad platforms. Google acts on pages that actually trap the back button. The same policy covers Discover, and it covers visits that start on social or other non-Search channels, as long as the hijack happens inside a browser. Open-in-app hand-offs are out of scope.

Before Black Friday traffic arrives, click Back on your ad landing pages and on pages that get social or Discover visits. If a tag is inserting an interstitial, disable that tag and test again.

Source: Google Search Central documentation update and spam policies, last updated 2026-11-23 UTC.

- format: 新闻翻译 · tags: 🎨 创意广告
- reasoning: 用 longterm 元 Hook「大部分人用 X 的方式是错的」。英文草稿。FAQ 要点来自本轮打开的官方政策页，不把 6/15 起执行写成今天新法。无感叹号。

### 草稿 3（把 X 和 Y 连起来看）

This morning's market snapshot was taken at about 9:20am ET, while US stocks were still marked closed, so treat NVDA at 165.05 (+31.48%) and SHOP at 134.30 (+8.55%) as Monday's close or the pre-open quote, not Tuesday's open.

BTC was near 60,350, down about 5.4% over 24 hours. Crypto Fear & Greed sat at 9 (Extreme fear). The ETF daily flow print was about -$569.7 million. That is context, not a trade.

The operator job this week is still checkout and listing control, not the tape. Shopify has turned on agentic checkout for ChatGPT by default for eligible stores. Amazon sellers with Victoria's Secret inventory should look for a November 26 removal notice before they treat Black Friday as a normal sell-through day.

Sources: Day1 Global snapshot at 2026-11-24T14:20:38Z; Shopify Changelog (Nov 23); PPC Land report of an Amazon Services notice (Nov 23).

- format: 跨领域连接 · tags: 💰 加密×美股, 🛒 AI 电商自动化
- reasoning: 用 longterm 元 Hook「把 X 和 Y 连起来看」。必须引用 market_snapshot：BTC、F&G、ETF 流入、NVDA/SHOP，并写明 9:20am ET、marketState=closed。不做投资建议。英文草稿。无感叹号。

## 跨领域机会

- **Shopify agentic checkout × ChatGPT 发现层**：Shopify 把代客下单做成可关的 Agentic checkout，但帮助页写得很清楚：关开关不等于退出 ChatGPT 发现，也不等于挡住 Shop skill。这和 Adweek 所写「ChatGPT agent 自写查询、广告主看不见」是同一条零售入口的两端——一边是你的 checkout 开关，一边是你看不见的查询。黑五前先核对开关和 Catalog 访问，再决定要不要另外处理商品描述前 6,000 字符的披露。

- **Walmart 对 Muse 打开 Agent Gateway × Amazon/eBay 拦截 agent 浏览**：The Verge 写 Walmart 让 Muse 走 Agent Profile 代客下单，并对比 Amazon 和 eBay 拦截 AI agent 浏览。Shopify 同一窗口则把 agent checkout 做成默认开启的可选项。交叉点不是「AI 购物到来」的空话，而是各平台把控制权放在不同位置：Walmart 在消费者 Agent Profile 的限额，Shopify 在商家的 Agentic checkout / Catalog 开关，Amazon 仍偏拦截。对卖家更可执行的是 Shopify 开关；Walmart 侧本轮没有找到 Marketplace 可改字段。

## 本周表现摘要

- period: 2026-11-17 ~ 2026-11-24
- Typefully 不可用，total_posts / 曝光为空
- covered_topics: shopify-chatgpt-agentic-checkout-default-on-1124, google-back-button-hijacking-faq-ad-code-no-shield-1124, amazon-vs-nwd-removal-thanksgiving-1126-1124, google-ads-fr-it-surcharge-3pct-jan2027-1123, google-mc-consumer-notice-7-cap-eighth-overwrites-1123, amazon-attribution-asin-restate-28-day-1123, amazon-brand-store-builder-agent-all-deals-1123, google-mc-sale-price-30-day-annotation-1122 …
- underserved_tracks: 🤖 AI 前沿
- insights: Typefully 仍不可用，本周发布表现无法用曝光验证；草稿回退到 longterm 元 Hook，并按账号要求写成英文。今日 3 条选题：Shopify 1、Google 1、Amazon 1，均未满额；D4=0（x.ai/changelog/bot 仍为 11/18 v1.2.3，且已出 48h 窗）。没有为凑满 5 条再加 Pinterest×Microsoft（无上线日）或 BADBOX（无可改字段）。AI 前沿有 Walmart×Muse 上线口径、Claude Ship、Import AI 482，但缺卖家 30 分钟动作或属产品发布，只进 must_reads。一条草稿补位 AI 前沿（Shopify×ChatGPT）。

## 系统建议

### info_sources
- **promote**
  - Shopify Changelog + Help Center（Agentic Storefronts / Selling on ChatGPT）（high）：今日主选题的两份官方出处都已打开，并给出默认开启条件和可执行后台路径，比只转述二手稿更稳。
  - Google Search Central（search/updates + spam-policies）（high）：今日第二条选题的官方 FAQ 与 Last updated 2026-11-23 UTC 戳记都在这两页上，可直接核原文。
  - PPC Land（high）：持续在 48h 窗内拆出卖家通知和广告政策变化（NWD/VS、Microsoft 出价澄清、BADBOX、Pinterest），并标明哪些帮助页找不到公开版。
- **demote**
  - The Batch / Anthropic / xAI / Cursor / Runway RSS（high）：今日部分仍 404 或不可用；x.ai/changelog/bot 只能靠打开官方页，且仍为 11/18 v1.2.3。
  - Reddit RSS（high）：今日继续 429/404，Reddit 通道 0 条。
  - X search_news（共享读取）（medium）：本轮 3 次 search_news 均因共享 X 通道 HTTP 429 失败，只能用 search_posts_all 与 RSS/官方页。
- **add**
  - Shopify Help: Selling on ChatGPT / Agentic Storefronts（high）：今日默认开启选题的操作路径页，建议列入官方页必读清单。
  - Google Search Central spam policies（back button hijacking FAQ）（high）：今日落地页合规选题的官方出处，且会继续被广告代码问题追问。
  - Pinterest Newsroom / Microsoft Advertising 合作公告（medium）：窗内官方库存扩展，虽无上线日、不宜当选题脊柱，但应跟踪何时可在后台验证。

### topic_library
- **archive**
  - （无）
- **add**
  - Agentic checkout / AI 渠道默认开启与 Catalog 访问开关（high）：官方把代客下单做成可改字段，且默认开启，常青库缺这一位。
  - Search 落地页返回键劫持 / 第三方广告代码责任（high）：官方 FAQ 把责任落到实际劫持的页面，且覆盖 Discover 与社交来源。
  - Amazon No Wholesale Distribution（NWD）与 Brand Representative 角色（medium）：出现带截止日期的品牌清场通知，帮助页 5465/6045 尚无公开版，值得在库里留观察位。

### positioning_drift
- （无）

## 采集与跳过

- 采集：295 RSS window URLs + 16 readable index pages + 12 article/help fetches + 50 X records from 2 successful search_posts_all calls (3 search_news calls returned 429 and used no read) = 373 collection inputs; includes overlap, not 373 verified independent events.
- 跳过：Typefully / Exa；BDC（Channel D 停用）；search_news 因共享 X 通道 429 失败；Reddit RSS 429/404；Writer 全流水线；未自动发帖；不通知 xhs / x / wechat，除非 Alex 确认交接。
- pending 根目录旧条目未自动升题；冷邮 archive 跳过。

