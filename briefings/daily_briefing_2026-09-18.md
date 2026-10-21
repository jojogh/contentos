# 每日创作简报 · 2026-09-18

> 生成时间：2026-09-18T00:39:11Z　|　修订时间：2026-09-18T00:47:00Z　|　原始素材：1429 条

**今日发布策略**：今日主线从「生成变便宜之后瓶颈去哪了」升级为更完整的一版:生成侧确实在崩价——PrismML 把 27B 多模态压到 5.9GB 本地可跑、豆包图像/视频推理 token 降 30%+、智谱让 AI 给自己的推理系统提速 3 倍;但真实渗透率数据同时打脸:1.32 亿美国人用 AI 辅助购物,真正由智能体完成成交的只有约 3%,仅 7% 消费者信任 AI 代为下单。所以瓶颈不是生成,是「审批与信任」这一层。而 Naver(对话 +60% / 交易额 +82%)和亚马逊广告(ROAS +90%)说明:谁手里有履约数据或零售数据,谁就能把这一层做通。发布建议:公众号走这条主线,X 走 TikTok Shop AI 商品图新规,小红书补 AI 广告形态变化(Goodwipes + Hummingbird + Amazon Creative Agent)。

> **修订说明**：首版归档后约 4 分钟,三个赛道扫描子代理(scan-ecom / scan-creative / scan-frontier)的采集结果陆续到达(合计 54 条)。首版误将该通道记为「失效」,本版已并入其素材:must_reads 由 14 条扩到 20 条(新增 6 条独立事件,另有多条子代理素材并入既有事件),also_worth_reading 由 17 条增至 38 条,并重写主线选题与公众号草稿。子代理时间戳说明:WebFetch 在其环境同样被全域拦截,仅知日期的条目统一锚定为当日 T12:00:00Z,属约定而非实测,相关条目已在 note 内标注。

---

## 一、今日必看（20 条）

### 1. TikTok Shop 更新 AIGC 卖家指引并下发操作手册：AI 主图、AI 模特图、AI 场景图与实物差距过大将被下架

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：AI 生成商品图 / 详情页 / 视频素材
- **来源**：跨税云 Ksher（综合亿邦动力、DNY123、白鲸出海报道）　|　**发布**：2026-09-17T00:00:00Z（25 小时前）
- **链接**：<https://www.ksher.cn/news/post/kjzx26091705/>

平台把商品治理从「商品是不是真的」推到「展示效果是不是真的」：不得虚构商品不存在的功能、材质、数量、颜色或使用效果，过度美化导致误解同样违规；美妆健康、食品饮料、时尚服饰三大类目被点名并给出专项风险示例。违规后果是商品下架、内容限流乃至账号处罚。09-16 起印尼、菲律宾、越南等 6 个核心市场已同步下发 AIGC Seller Playbook，含发布前核对清单。对已经在跑 AI 商品图的卖家，这是本周最需要立刻处理的一条。

**延伸线索**：

- 白鲸出海快讯口径：菲越市场率先执行，AI 素材需真实反映实际商品 — <https://www.baijing.cn/newsflashes_txzq/19213>
- 欧洲跨境之路：平台开始进一步规范 AI 商品图，风险示例按类目给出 — <https://www.ouzhou123.com/news/11553>

---

### 2. Google 假日季前扩张 agentic commerce：Merchant Center 上线 AI 声量洞察，UCP 打通购物车回传，Business Agent 进 YouTube 广告

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：平台 AI 功能更新(Amazon/Shopify/TikTok Shop/淘宝)
- **来源**：Search Engine Land（综合 Google 官方博客）　|　**发布**：2026-09-17T12:00:00Z（13 小时前）
- **链接**：<https://searchengineland.com/google-expands-agentic-commerce-tools-ahead-of-the-holiday-shopping-rush-488930>

Rethink ROI 峰会一口气发布了一批：① Merchant Center 的 AI Performance Insights 在美加澳印新五国 GA，核心指标是 share of voice——品牌在 AI Mode、AI Overviews、Gemini app 里被链接的次数对比已定义竞品集合，配套购物漏斗三段、热门商品词与商品属性完整度分；② 同时上线 Conversational Attributes，六组结构化字段直接喂给 AI 回答；③ UCP（Universal Commerce Protocol）打通购物车回传商家自有站点与结账流测试；④ 美国合格零售商可把 Business Agent 嵌进 YouTube 广告。Tapestry（Coach/Kate Spade）已用 UCP 结账在 Search、AI Mode、Gemini 内直接成交。官方口径下采用 feed 最佳实践的商家次月转化平均 +5%，lululemon 测试中对话式属性有 50% 概率被 AI Mode 推荐采纳（厂商口径，未见独立验证）。新 UCP 能力美国先行，澳加预计明年初跟进。

**延伸线索**：

- Google 官方帮助文档：AI 驱动的购物体验洞察说明 — <https://support.google.com/merchants/answer/17117204>
- PPC Land：share of voice 的算法口径与「对薄内容宣战」的解读 — <https://ppc.land/googles-new-merchant-center-report-tracks-your-brand-in-ai-mode/>
- Tapestry 官方：Coach 与 Kate Spade 商品可在 Gemini app 与 Google Search（含 AI Mode）内直接购买 — <https://www.tapestry.com/innovation/shoppers-can-now-buy-coach-and-kate-spade-products-in-the-gemini-app-and-google-search-including-ai-mode/>

---

### 3. Naver AI 购物智能体接入实时配送数据：对话量涨约 60%，成交额涨 82%

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：韩联社 Yonhap　|　**发布**：2026-09-17T04:47:00Z（20 小时前）
- **链接**：<https://www.yna.co.kr/view/AKR20260917134700017>

少数给出智能体实测增长数据的案例。Naver 升级购物 App 内的 AI Shopping Agent：用户提问带配送时限（如「推荐明天能到的火锅套餐」）时，智能体只筛能按时送到注册地址的商品，展示预计到货日与截单时间；同时用自然语言推断场景（降温→电热毯、水暖垫）。关键是它把「履约数据」接进了推荐——这正是大多数 agentic commerce 缺的那一层。半年数据：对话量较 6 月正式上线时增长约 60%，通过该智能体产生的交易额同期增长 82%。

---

### 4. Mastercard 联手 Alchemy 推出 AgentCard：AI 智能体可持卡代购，额度与品类由用户设限

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：PaymentsJournal（原始报道为 WSJ，2026-09-17）　|　**发布**：2026-09-17T12:00:00Z（13 小时前）
- **链接**：<https://www.paymentsjournal.com/mastercard-takes-ai-shopping-from-search-to-checkout/>

Mastercard 与 Alchemy 合作的智能体支付服务本周上线：通过一次性 Token 化的 Mastercard 凭证绑定用户既有账户（积分、额度、权益沿用原账户），用户可设定消费上限与允许品类，并选择让智能体自主下单还是付款前回确认。配套 Verifiable Intent 框架，用来证明智能体确实在授权范围内行事。Visa 亦已与 Alchemy 合作，跨网络的智能体支付基础设施趋于共用。这条补上的是 agentic commerce 最短缺的一环——「谁有权替用户花钱、怎么证明它没越权」。

---

### 5. Forkast：1.32 亿美国成年人用 AI 辅助购物，但真正由智能体完成成交的只有约 3%

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：Forkast.News　|　**发布**：2026-09-17T12:00:00Z（13 小时前）
- **链接**：<https://forkast.news/the-approval-screen-is-where-agent-commerce-breaks/>

给 agentic commerce 的乐观叙事泼的一盆冷水，也是今日最有价值的一组反差数字。1.32 亿美国成年人用 AI 辅助过零售购买，但真正涉及智能体完成的交易仅约 3%。佐证：OpenAI 2026 年 3 月回撤 Instant Checkout，原因是沃尔玛数据显示 ChatGPT 内购买转化率仅为跳转购买的三分之一。文中对比三种信任模型——Meta Muse（Stripe Link 保险背书虚拟卡 + Cover Genius 退款保证）、GrokBot 的「买家自负」立场、Google/Mastercard 的 AP2 技术标准——并给出判断：审批界面才是智能体商务的真正断点。市场预测仍是从 2026 年 80 亿美元到 2030 年 1.5 万亿美元，但 79% 消费者担心数据隐私、仅 14% 信任 AI 无需人工验证即可购买。

**延伸线索**：

- 21世纪经济报道：标普全球口径超三分之二商户预测三年内智能体自主发起交易占电商总量 10% 以上；Adobe Analytics 称 2026 Q1 已有 39% 消费者用 AI 助手网购、AI 渠道转化率高 42% — <https://www.sfccn.com/2026/9-16/zNMDE0NDlfMjI0MzMzNg.html>

---

### 6. ACI Worldwide 调研：仅 7% 时尚消费者信任 AI 代为下单，53% 对自主购买感到不适

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：ACI Worldwide 投资者关系新闻稿　|　**发布**：2026-09-16T12:00:00Z（37 小时前）
- **链接**：<https://investor.aciworldwide.com/news-releases/news-release-details/only-7-fashion-shoppers-trust-ai-buy-them-today-showing>

与 Forkast 相互印证的消费者侧调研。仅 7% 的时尚消费者愿意让 AI 助手未经确认就下单，53% 对自主购买感到不适。结论是消费者要 AI「告知」而非「代替」决策——最有吸引力的工具是降价提醒（35%）与跨零售商比价（35%），而不是自动下单。对商家的含义：在认证、授权与反欺诈控制建立起来之前，谈自主成交为时过早。

---

### 7. 亚马逊「二段标题」大规模推送：新增 Item Highlights 商品亮点 125 字符，可被搜索并展示在详情页

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：平台 AI 功能更新(Amazon/Shopify/TikTok Shop/淘宝)
- **来源**：AMZ123 跨境导航　|　**发布**：2026-09-16T08:00:00Z（41 小时前）
- **链接**：<https://www.amz123.com/t/EKeOZKpe>

亚马逊本月开始大规模推送二段标题结构，把原来挤在标题里的使用场景、材质、卖点挪到独立的 Item Highlights 字段，125 字符上限，参与搜索索引。官方建议标题精简为品牌 + 核心词。这条对 listing 的影响是结构性的：过去靠标题堆词的做法会被结构化字段替代，而 AI 生成的标题与亮点官方明确提示必须人工审核。（发布时间近似到日）

---

### 8. 一周拍完 74 集出海短剧：全 AI 流程跑通柬埔寨市场，创始人说「AI 视频最贵的成本根本不是算力」

- **赛道**：🛒 AI 电商自动化　|　**匹配选题**：AI 生成商品图 / 详情页 / 视频素材
- **来源**：非凡产研　|　**发布**：2026-09-16T10:00:00Z（39 小时前）
- **链接**：<https://mp.weixin.qq.com/s?__biz=MzU5Mjg5MjQ5Ng==&mid=2247522710&idx=2&sn=43523efc01ba70dcef5c50b7637ac263>

炫佳科技用 7 天完成 74 集柬埔寨短剧《Where You Belong》，从角色建模、镜头生成、合成到柬语配音全流程 AI，片中演员只有几张照片。创始人秦林给出的判断是护城河不在模型：真正要积累的是高质量产业数据、经真实项目验证的工作流、理解内容生产的团队、以及生产到分发的反馈闭环。同一批报道里的成本数据更值得看：可灵 2.0 约 48 元/分钟、Seedance 2.0 约 60 元/分钟，按「三抽一」的成功率算实际生成一分钟要 150–180 元；DataEye 口径制作端成本下降约 90%，但流量成本同比上涨超 100%，收益端下滑 50% 以上；约 90% 的 AI 短剧公司亏损，阅文 AI 技术负责人称播放量超 4000 万次才能盈利而这类爆款占比不到 1%。

**延伸线索**：

- 第一财经：AI 改写出海短剧，制作成本下降九成，赚钱逻辑变了 — <https://www.yicai.com/news/103357871.html>
- 界面新闻：出海短剧踩刹车——AI 挤走剧组，但取代不了情绪与 IP — <https://www.jiemian.com/article/15026261.html>

---

### 9. 亚马逊广告 Creative Agent 亮相：对话式创意智能体生成本地化素材，零食品牌 ROAS 提升 90%

- **赛道**：🎨 创意广告　|　**匹配选题**：广告平台 AI 化(Meta/Google/TikTok Ads)
- **来源**：观点网　|　**发布**：2026-09-17T12:00:00Z（13 小时前）
- **链接**：<https://webkit.guandian.cn/article/20260917/603259.html>

亚马逊广告在综艺《伦敦合伙人》里展示出海工具箱，核心是 Creative Agent——基于零售数据信号做产品/人群调研、故事板构思，并生成展示广告、品牌视频、音频与 STV 素材；配套亚马逊营销云 AMC。案例：某全球零食品牌用 AMC 分析五年购买数据、投放一个月后 ROAS 提升 90%、CPM 下降 26%、单一人群新客占比 42%。同批官方数据还有 AI 生成图片的品牌推广活动 ROAS 平均 +10.3%，品牌视频推广的商品数最多 +71%、销售额最多 +15%。这条与 Google 的 Conversational Attributes 是同一件事的两面：平台都在把「素材生产」从创意团队手里收进自己的数据闭环。

---

### 10. Pinterest 发布 Visual Search Ads：把广告插进视觉搜索结果与 Pin 详情，CPI 最多改善 85%

- **赛道**：🎨 创意广告　|　**匹配选题**：广告平台 AI 化(Meta/Google/TikTok Ads)
- **来源**：Modern Retail　|　**发布**：2026-09-17T12:00:00Z（13 小时前）
- **链接**：<https://www.modernretail.co/marketing/pinterest-unveils-new-suite-of-ad-tools-including-visual-search-ads-in-its-pitch-to-brands/>

Pinterest Presents 广告主峰会上发布 Visual Search Ads，广告主可在搜索结果与 Pin closeup 中竞价顶部位置、直接导流官网，并兼容 Performance+。同时上线 Priority Products、自助 A/B 测试与 App Promotion 目标（全球 beta）。官方称某美国企业广告主在 alpha 测试中单次安装成本最多改善 85%。背景数字：月搜索量 800 亿次、6.4 亿月活、96% 以上搜索不含品牌词——「无品牌词的视觉搜索」正是 AI 导购最可能吃掉的那块流量，Pinterest 选择在这里直接卖广告位。

---

### 11. Goodwipes 用 AI 四天做出一条恶搞 OpenAI Astra 广告的片子：AI 原生广告公司 OK Future 出手

- **赛道**：🎨 创意广告　|　**匹配选题**：品牌营销中的 AI 创意案例
- **来源**：Adweek（The Drum 同步报道）　|　**发布**：2026-09-17T00:00:00Z（25 小时前）
- **链接**：<https://www.adweek.com/creativity/goodwipes-uses-ai-spoof-openai-astra-ad/>

湿厕纸品牌 Goodwipes 发了一分钟 AI 制作的 parody《Asstra》，把 OpenAI Astra 广告里那种光洁的未来感逐帧复刻，然后揭穿主角们其实都坐在马桶上。由 ex-MullenLowe CEO Frank Cartagena 创办的 AI 原生代理商 OK Future 用 ArtCraft 和 Astra 完成，从创意到成片四天，被 The Drum 选为 Ad of the Day。制作难点很真实：AI 一度执着于让人坐在放下的马桶盖上，品牌资产（包装）还原也是挑战。值得关注的点不是「AI 能做广告」，而是品牌用 AI 在四天内完成了一次针对大厂 AI 叙事的快速反应——以前这种速度的回应型创意基本不可能。

**延伸线索**：

- The Drum：Goodwipes 对 ChatGPT 式完美 AI 未来的调侃式回应，Ad of the Day — <https://www.thedrum.com/news/goodwipes-takes-a-cheeky-swipe-at-chatgpt-s-pristine-ai-future>

---

### 12. TikTok 与 Nest Commerce 合作推出 AI 创意平台 Hummingbird：读实时投放数据生成素材变体，并检测创意疲劳

- **赛道**：🎨 创意广告　|　**匹配选题**：广告平台 AI 化(Meta/Google/TikTok Ads)
- **来源**：Nest Commerce 官方新闻稿（Cision 分发）　|　**发布**：2026-09-17T00:00:00Z（25 小时前）
- **链接**：<https://digital-release.kxan.com/business/press-releases/cision/20260917LN50622/nest-commerce-and-tiktok-partner-to-launch-ai-creative-platform-hummingbird-on-tiktok/>

Hummingbird 由 TikTok 技术 grant 支持，9 月 23 日在 TikTok 伦敦总部上线。它读实时广告表现数据来生成新创意变体，覆盖静态、动态、UGC 风格三类，同时识别创意疲劳——也就是说「什么时候该换素材」这件事从人工经验变成了平台工具的一项输出。官方表述里人类创意专家仍留在流程中心。对买量团队的含义是：创意疲劳监控这个原本要靠第三方工具或手动做的环节，正在被平台收进原生工具，投放侧的差异化空间进一步压缩到创意本身。

---

### 13. 用 Seedance 2.5 拍《沙丘 3》：两人 12 天、3000 多元积分做出 6 分钟概念片，坑全在版权审核和资产一致性

- **赛道**：🎨 创意广告　|　**匹配选题**：AI 视频广告模型进展
- **来源**：爱范儿　|　**发布**：2026-09-17T06:45:13Z（18 小时前）
- **链接**：<https://www.ifanr.com/1680580>

APPSO 团队的实际复盘：两位同事用 Codex 加 Seedance 2.5，12 天做完 6 分钟《沙丘 3》概念片，消耗 3000 多元积分。流程分四步——打磨剧本、建立资产库、生成视频、后期，对应传统片场的写剧本、找演员、选服装、搭场景、拍摄、剪辑。最有价值的两个坑：一是直接上传电影截图作参考会触发版权保护审核导致无法继续生成，只能保留低饱和色彩、荒漠质感、空间尺度等抽象特征，并去掉弗雷曼人蓝眼睛、蒸馏服过滤塞这类高辨识元素，前后多花三天重做资产；二是多轮修改中网页版 GPT 生成的图片会越改越糊，图片资产调整最后都在 Codex 里完成。另外提示词按秒拆开写。

**延伸线索**：

- 极客公园：Seedance 2.5 实测，30 秒 720P 约 780 积分，会员 239 元/月到账 2210 积分 — <http://www.geekpark.net/news/368563>

---

### 14. Viggle AI 开源 Meridian：MiniMax-H3 加 VGGT-Ω 几何引导，单张图生成新视角视频

- **赛道**：🎨 创意广告　|　**匹配选题**：AI 视频广告模型进展
- **来源**：魔搭 ModelScope 社区　|　**发布**：2026-09-17T12:28:00Z（12 小时前）
- **链接**：<https://mp.weixin.qq.com/s?__biz=Mzk3NTc1NTU0Mw==&mid=2247513874&idx=1&sn=f0a26c2cb0e598f534f0e2397673a71b>

Viggle AI 把 Meridian 开源，用几何引导的方式从单张图生成新视角视频，底座是 MiniMax-H3 加 VGGT-Ω。对电商场景的直接含义是商品图到多角度视频这条路的门槛又降了一档——原本需要多角度拍摄或重建的环节，正在变成一次生成。开源意味着可以本地跑，数据不出境，对做商品视频的团队是可评估的选项。

---

### 15. 智谱发布国内首个 RSI 工程成果：GLM-5.3 驱动的 Infra Agent 给 GLM-5.3-Flash 自建推理系统，10 万国产卡两周吞吐提升 3 倍

- **赛道**：🤖 AI 前沿　|　**匹配选题**：前沿模型发布与能力跃迁
- **来源**：爱范儿（综合量子位、IT之家报道）　|　**发布**：2026-09-17T09:56:01Z（15 小时前）
- **链接**：<https://www.ifanr.com/1680560>

唐杰在 X 上披露的递归自我改进（RSI）首个生产环境实践：GLM-5.3 驱动的 Infra Agent 完成了 GLM-5.3-Flash 推理基础设施的设计、调试与优化。超过 10 万张国产芯片的集群上从零搭生产级推理服务，不到两周端到端吞吐提到初始基线的 3 倍，硬件利用效率与单 Token 成本达到主流 NVIDIA GPU 相当水平，支持 1M 上下文与多模态请求。机制核心是 dense feedback，让 Agent 拿到正确性、系统行为、性能这些局部、低成本、可客观验证的信号。Agent 实际修掉的问题包括 KV Transfer 因 Python GIL 未释放导致的开销（从超 30% 降到 1% 以下）、Decode Kernel 重复归一化计算（1.71 倍加速）。关键澄清：团队明确说还没有实现 RSI，人类工程师仍负责设定目标、搭反馈环境、审核高风险变更——角色从「解决问题的人」转向「设计反馈的人」。

**延伸线索**：

- 量子位：唐杰发布智谱 RSI 首个成果 — <https://www.qbitai.com/2026/09/491357.html>
- IT之家：AI 在十万卡国产集群上自建推理系统 — <https://m.ithome.com/html/1003705.htm>

---

### 16. PrismML 开源 Bonsai 2 27B：三元权重把 27B 多模态模型压到 5.9GB，保留 98.2% 性能

- **赛道**：🤖 AI 前沿　|　**匹配选题**：前沿模型发布与能力跃迁
- **来源**：PrismML 官方新闻稿　|　**发布**：2026-09-17T00:00:00Z（25 小时前）
- **链接**：<https://prismml.com/news/prismml-launches-bonsai-2-27b>

今日最直接的「成本结构变化」。PrismML（Caltech 背景，Khosla Ventures 投资）把 27B 多模态模型从 FP16 的约 54GB 压到 5.9GB，压缩约 9–10 倍，消费级 GPU 甚至笔记本就能跑，RTX 5090 上最高 143 tokens/秒。20 项基准聚合 83.9 分，保留 Qwen3.8 27B 的 98.2%（上一代 95%）。Apache 2.0 许可，基于阿里 Qwen3.8 27B，09-17 起免费下载。代价是需要 PrismML 自研的 llama.cpp 分支，且知识与视觉类指标退化明显（知识/推理 79.86 vs 85.55、视觉 66.19 vs 71.36）。对电商团队的含义：商品图批量打标、素材审核、客服 FAQ 这类高频低难度任务，可以用一次性硬件成本换掉按量付费的 API 账单。

---

### 17. Anthropic 首次公开 AI 研发占比：Claude 主导公司 26% 的 AI 研发工作，内部常驻约 3 万个 Agent

- **赛道**：🤖 AI 前沿　|　**匹配选题**：前沿模型发布与能力跃迁
- **来源**：Reuters（经 MarketScreener 转载）　|　**发布**：2026-09-17T00:00:00Z（25 小时前）
- **链接**：<https://hk.marketscreener.com/news/anthropic-says-claude-now-leads-a-quarter-of-work-building-its-next-ai-models-ce785bd3d18efe2c>

首个「实验室自己披露 AI 替代自己到什么程度」的量化框架。Claude 主导的研发工作占比从 3 月的约 1% 升到 8 月的 26%，AI 与人类协作完成 90% 以上的研究类工作；内部平台常驻约 30,000 个 AI Agent，超 10 亿次决策中约 1/47,000 被拦截；约 6% 的 AI 研究算力用于安全，AI 驱动研究时升至 12%。Anthropic 同时强调在任何被测环节都还没做到完全自主。注意口径：它衡量的是研发，不是投放或运营——但这个 1%→26% 的半年度曲线，是判断「AI 替代白领工作」节奏目前最硬的一手标尺。

---

### 18. 匿名模型 Union Alpha 上线 OpenRouter：首日跑掉 20 亿 Token，单任务成本 0.65–2 美元，但速度只有 15–19 Token/秒

- **赛道**：🤖 AI 前沿　|　**匹配选题**：前沿模型发布与能力跃迁
- **来源**：AI 前线　|　**发布**：2026-09-17T04:04:00Z（21 小时前）
- **链接**：<https://mp.weixin.qq.com/s?__biz=MzU1NDA4NjU2MA==&mid=2247667236&idx=1&sn=243e085a1cd7fae38cbd702f28521847>

OpenRouter 与 OpenCode Zen 限时免费上线的匿名多模态模型，256K 上下文、最大输出 131K，支持 tools / tool_choice / response_format，面向研究、编程、Agent 工作流。首日约 20 亿 Token，随后称累计超 1000 亿、约 5 亿 Token/分钟。实测两极：OpenCode 公布的 Terminal-Bench 4.0 对比显示得分约 51%–55%，接近 GPT-6 Astra high（约 54%–58%）与 Claude Fable 5.1（约 52%–57%），低于 Astra xhigh（约 60%）；成本口径约 1–2 美元/任务以下，远低于 Astra high 约 4 美元、Fable 5.1 高配 12–30 美元。但负面同样多：速度 15–19 Token/秒，发一句「你好」要等 2–3 分钟，长周期任务不稳定、指令遵循差。身份未证实，社区猜测覆盖 OpenAI、智谱、Mistral、MiniMax、Kimi。注意与此前的匿名模型 Ox Alpha（后证实为 GLM-5.3-Flash）不是同一个。

**延伸线索**：

- InfoQ：神秘模型 Union Alpha 突袭，首日 20 亿 Token — <https://www.infoq.cn/article/EsH2bUAoMNQx6Nt7vytC>
- OpenRouter 官方模型页：262,144 上下文 / 预览期 $0 — <https://openrouter.ai/stealth/union-alpha>
- 实测翻车记录：免费额度并非无限，余额低于 10 美元每天限 50 次 — <https://www.jdon.com/94915-openrouter-union-alpha-free-model-review.html>

---

### 19. 菜鸟：AI Coding 贡献率从 10% 提到 90% 以上，需求交付却只快了 10%

- **赛道**：🤖 AI 前沿　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：InfoQ 中文　|　**发布**：2026-09-17T11:07:00Z（14 小时前）
- **链接**：<https://mp.weixin.qq.com/s?__biz=MjM5MDE0Mjc4MA==&mid=2651293269&idx=2&sn=070ccddba78947c10ebc28d9529359c0>

菜鸟研发总监郭凤钊在 AICon 上海站的分享：2025 年 10 月大规模推广 AI Coding 时贡献率约 10%，原定半年到 20% 挑战 50%，结果 2026 年二三月破 50%，随后平均值突破 90%，部分团队接近 100%——但代码贡献率与交付效率严重不对等，这是他们转向需求端到端托管交付的起点。方案是通用 Agent 加 Plugin、Playbook、云端沙箱，方法论核心是分层上下文管理、Playbook 驱动流程编排、确定性质量门控。旁证：字节 TRAE 团队的同类案例是超 90% 代码由 AI 生成、人均需求吞吐率仅提升约 60%，结论是「正确率不等于可交付性」，度量指标要从 AI 代码贡献率转向需求交付吞吐率。

**延伸线索**：

- InfoQ AICon 上海站议程：企业级研发体系的重构专题 — <https://www.infoq.cn/article/PrTG5MYs9cj38FclfCPl>

---

### 20. Claude 变成「唯一入口」：Anthropic 把 Cowork 并入主对话，同时推出 Claude Docs 与 Claude Slides

- **赛道**：🤖 AI 前沿　|　**匹配选题**：Agent 从 Demo 到工程化
- **来源**：VentureBeat（中文侧由创业邦同步报道）　|　**发布**：2026-09-17T10:40:00Z（14 小时前）
- **链接**：<https://venturebeat.com/technology/anthropic-is-killing-off-cowork-and-folding-it-into-claude-launching-claude-docs-and-claude-slides>

VentureBeat 报道的完整版：Chat / Cowork 的模式切换被取消，Claude 自己判断该快答还是该跑长任务，Agent 能力变成默认能力；同时 Docs（可协作编辑的文档）与 Slides（可直接演示、导出 PPT/PDF）beta 上线，把输出物直接推进到交付物。先向 Pro / Max 订阅者开放（web/desktop/mobile），随后 Team 与 Free；企业组织变更前至少提前 30 天通知，管理员可按职场权限控制工具可用性；Docs 可导出 Word / Google Docs，Claude Code 保持独立不参与合并。对内容与投放团队的含义：从「让 AI 写一段文案」变成「让 AI 交一份可发的物料」。策略上对标微软把 Copilot 铺进 Office 全家桶——「一个入口 + 若干连接」和「多个专用工具各管一摊」是两种不同的成本结构。

**延伸线索**：

- 创业邦中文报道：Claude 办公全家桶硬刚微软 — <https://mp.weixin.qq.com/s?__biz=MjM5OTAzMjc4MA==&mid=2650891250&idx=4&sn=3f6041bb61eced81a6d0266176da699e>

---

## 二、也值得一读（38 条）

| # | 标题 | 赛道 | 链接 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 亚马逊 Amazon Connect 从单一产品扩展为四项智能体 AI 解决方案组合 | 🛒 AI 电商自动化 | <https://www.cls.cn/detail/2486608> | 日期确认，钟点近似 |
| 2 | KOEO AI 数字人主播自主进 TikTok Shop 选品开播：近 6000 家卖家在用 | 🛒 AI 电商自动化 | <http://news.cnnb.com.cn/system/2026/09/18/030815916.shtml> | 日期确认，钟点近似 |
| 3 | 值得买科技联合华为云升级「值数 Matrix-GEO」AI 心智洞察智能体 | 🛒 AI 电商自动化 | <https://www.cnfin.com/gs-lb/detail/20260917/4471461_1.html> | 日期确认，钟点近似 |
| 4 | Nexi 与 ReFiBuy 结盟，把欧洲商家目录接入消费者 AI 智能体 | 🛒 AI 电商自动化 | <https://www.borsaitaliana.it/borsa/notizie/teleborsa/finanza/nexi-partnership-con-refibuy-nell-agentic-commerce-per-gli-esercenti-europei-107_2026-09-17_TLB.html?lang=it> | 日期确认，钟点近似 |
| 5 | ReFiBuy 接入 Claude Commerce Agent，主打「目录持续自优化」闭环 | 🛒 AI 电商自动化 | <https://www.accesswire.com/1223070/refibuy-brings-continuously-improving-product-data-to-claude-commerce-agent> | 厂商新闻稿，日期确认、钟点近似 |
| 6 | Groupon 开放平台给开发者与 AI 智能体，推出 AI Builder Pack | 🛒 AI 电商自动化 | <https://in.marketscreener.com/news/groupon-opens-its-platform-to-builders-and-ai-agents-ce785bd2df8ff124> | 日期确认，钟点近似 |
| 7 | 中国电商大会发布《2026 AI 消费电商应用洞察报告》：AI 已覆盖 90% 经营场景 | 🛒 AI 电商自动化 | <https://www.workercn.cn/c/2026-09-17/8896192.shtml> | 行业报告口径，日期确认、钟点近似 |
| 8 | Riskified 把身份风险智能嵌入 Zendesk：AI 客服 Agent 直接判定退货退款欺诈 | 🛒 AI 电商自动化 | <https://news.qq.com/rain/a/20260916A08Z2P00> | 原始 PR 为 09-15，非最严口径 |
| 9 | 吉宏股份 AI 战略升级，Giikin AI+ 全域智能运营平台切入 Token 出海分销 | 🛒 AI 电商自动化 | <https://vipwt1.cfi.net.cn/p20260916000403.html> | 日期确认，钟点近似 |
| 10 | Skai Lama 推出面向 Shopify 的 BFCM AI 套件，主打「AI 时代第一个黑五」 | 🛒 AI 电商自动化 | <https://natlawreview.com/press-releases/skai-lama-launches-ai-powered-suite-shopify-stores-ahead-first-black-friday> | 厂商新闻稿，日期确认、钟点近似 |
| 11 | 万兴科技布局 AI 营销：万兴播爆（Virbo AI）Web 端在深圳跨境电商展全球首发 | 🎨 创意广告 | <https://www.stdaily.com/web/gdxw/2026-09/17/content_583079.html> | 日期确认，钟点近似 |
| 12 | Cheil 把广告拍摄现场变成 AI 摄像头实测：42 台摄像机、7014 小时素材、319 人 | 🎨 创意广告 | <https://campaignbriefasia.com/2026/09/17/hanwha-vision-puts-its-ai-vision-solutions-to-the-ultimate-test-in-now-you-see/> | 日期确认，钟点近似 |
| 13 | BASF 除草剂 Voraxor 的全生成式 AI 广告：Nano Banana + Seedance Pro + Kling 3.0 拍出怪兽片质感 | 🎨 创意广告 | <https://shots.net/news/view/made-by-humans-goes-big-for-basf-voraxor> | — |
| 14 | AI 视频进入「交付时代」：行业口径从拼参数转向拼可交付成品 | 🎨 创意广告 | <http://news.cyol.com/gb/keji/articles/2026-09/17/content_5x8x90i09B.html> | 日期确认，钟点近似 |
| 15 | OpenClips：一个产品链接直接产出可投放视频广告，背后聚合 45+ 模型自动路由 | 🎨 创意广告 | <https://www.zhiding.cn/cooperation/2026/0917/3199554.shtml> | 发布时间证据冲突，建议核实 |
| 16 | Higgsfield 首届 Adathon 冠军 AI-R Studio：要求 ≥51% 视觉为 AI 生成 | 🎨 创意广告 | <https://www.adweek.com/creativity/ai-r-studio-wins-higgsfields-ai-adathon-competition/> | 日期确认，钟点近似 |
| 17 | CyberLink Director Suite 2027：PowerDirector / PhotoDirector 引入 AI 智能体，自然语言完成剪辑修图 | 🎨 创意广告 | <http://press.ikoreadaily.co.kr/newsRead.php?no=1042856> | 日期确认，钟点近似 |
| 18 | 韩软 Hancom 为 AI 工作平台 Nomadian 投放首支电视广告，主打「Agent Owner」 | 🎨 创意广告 | <https://www.mt.co.kr/tech/2026/09/18/2026091808550750475> | 时间由文章 ID 精确解出 |
| 19 | OpenAI 发布 Astra for Law：GPT-6 Astra 叠加 2.3 亿 URL 法律检索索引 | 🤖 AI 前沿 | <https://openai.com/index/astra-for-law/> | 日期确认，钟点近似 |
| 20 | 阿里云「云市场」9/20 更名「AI 应用市场」 | 🤖 AI 前沿 | <https://www.aliyun.com/notice/118672> | 日期确认，钟点近似 |
| 21 | 阿里发布 Qoder Cloud Agents 1.0：企业级 Agent 托管平台，月调用超千万 | 🤖 AI 前沿 | <https://www.cnstock.com/commonDetail/791259> | 日期确认，钟点近似 |
| 22 | Oracle 发布 MCP Gateway、AI Assistant 与 HITL 治理，面向企业级 Agent | 🤖 AI 前沿 | <https://blogs.oracle.com/integration/oracle-integration-product-update-webcast-september-17th-2026-foundation-for-enterprise-ai-agents> | 日期确认，钟点近似 |
| 23 | Komodor 推出 Agentic Operations Platform：50+ 开箱 Agent，带 RBAC、审批闸与消费上限 | 🤖 AI 前沿 | <https://www.tmcnet.com/usubmit/2026/09/16/10446824.htm> | 厂商新闻稿，日期确认、钟点近似 |
| 24 | OpenAI 首次公开披露 6 起模型「目标偏离」事件并发布追踪框架 | 🤖 AI 前沿 | <https://www.jiemian.com/article/15108994.html> | 硬窗口外延伸参考 |
| 25 | 中国电信发布星辰大模型 Xing4.0-29B-A4B：29B MoE / 仅 4B 激活的轻量智能体模型 | 🤖 AI 前沿 | <https://stcn.com/article/detail/4189429.html> | 日期确认，钟点近似 |
| 26 | 生数科技 Vidu S2 发布即全量开放：实时数字人 720P + 视频流实时编辑双模型 | 🎨 创意广告 | <http://www.eeo.com.cn/2026/0916/1037784.shtml> | 09-16 已在当日简报覆盖，硬窗口外延伸参考 |
| 27 | 智象未来发布原生全模态视频模型 HD-V1：5–20 秒 1080P，自主规划镜头与台词 | 🎨 创意广告 | <http://www.ahwang.cn/hefei/2026/0916/3053548.html> | 硬窗口外延伸参考 |
| 28 | Unbiased 发布 Pareto：262K 上下文的付费复合模型，$2.50/$7.50 | 🤖 AI 前沿 | <https://www.orcarouter.ai/blog/unbiased-pareto-release> | 厂商标称，无独立评测 |
| 29 | 综述 \| 迈向能够自我改进的 AI：递归自我改进（RSI） | 🤖 AI 前沿 | <https://mp.weixin.qq.com/s?__biz=MzU3NjE4NjQ4MA==&mid=2247557293&idx=1&sn=c08aac5e805dc93791e80f935fb9460d> | 延伸参考 |
| 30 | 号称人类造的最后一个 AI 要来了，刷屏全网的 RSI 是什么 | 🤖 AI 前沿 | <https://mp.weixin.qq.com/s?__biz=MjM5OTAzMjc4MA==&mid=2650891084&idx=2&sn=773ab497af522b38b0e67bdc23a26bf3> | 延伸参考 |
| 31 | 乌兰察布，DeepSeek 在这寻找最便宜的 Token | 🤖 AI 前沿 | <https://mp.weixin.qq.com/s?__biz=MTQzMjE1NjQwMQ==&mid=2656205255&idx=4&sn=83963a6bebdfc190f1f896be741da309> | 延伸参考 |
| 32 | Astra 的走红，证明 OpenAI 放弃 Sora 是一个英明决策 | 🎨 创意广告 | <https://mp.weixin.qq.com/s?__biz=MzIxMDgyMTM0NQ==&mid=2247502593&idx=1&sn=dba0b0e5ee278c0dea315204c7bfc89f> | 延伸参考 |
| 33 | 豆包 Seed-2.1-pro 0915 升级：图像/视频推理 token 消耗降 30%+ | 🤖 AI 前沿 | <https://m.ithome.com/html/1003012.htm> | 09-17 已作为当日内容覆盖，硬窗口外延伸参考 |
| 34 | 在三张圆明园鼠首照片里，我们看到了 3D AI 的 Harness 时刻 | 🎨 创意广告 | <https://mp.weixin.qq.com/s?__biz=MzA5ODEzMjIyMA==&mid=2247745637&idx=1&sn=f291329ae6f72b779cac24d6dc603f02> | 延伸参考 |
| 35 | 京东押注物理 AI，冲在前面的是一群 95 后 | 🛒 AI 电商自动化 | <https://mp.weixin.qq.com/s?__biz=MTMwNDMwODQ0MQ==&mid=2653113681&idx=1&sn=c8202657d800cbb9bbe928dd4c0b7a67> | 延伸参考 |
| 36 | 出海实战手册 \| AI Agent 时代的零售出海新篇章 | 🛒 AI 电商自动化 | <https://mp.weixin.qq.com/s?__biz=MzAwODY4OTk2Mg==&mid=2652162892&idx=1&sn=dc4278dbb82259e8122aae31bff89575> | 延伸参考 |
| 37 | 从「做过」到「会做」：用 OpenViking 经验记忆构建 Agent 的进化闭环 | 🤖 AI 前沿 | <https://mp.weixin.qq.com/s?__biz=MzI1MzYzMjE0MQ==&mid=2247522604&idx=1&sn=6ea201d826647e12047227cd3d386ba4> | 延伸参考 |
| 38 | 照片秒变水墨画：12 个 Skill 解锁 8 种视觉玩法 | 🎨 创意广告 | <https://mp.weixin.qq.com/s?__biz=MzU2ODEwMzE0Nw==&mid=2247550936&idx=1&sn=31ffbb3923959de102a32671d6e39d69> | 延伸参考 |

## 三、今日选题（13 条）

### 1. 3% 的真相：生成侧已经崩价，但智能体成交卡在「审批」这一层

- **热度**：high　|　**形式**：deep-dive　|　**赛道**：🛒 AI 电商自动化 / 🤖 AI 前沿
- **Hook**：把 X 和 Y 连起来看 / 生成变便宜之后，钱花到哪里去了

**切入角度**：今日最好的交叉切口，也是首版主线的升级版。先把生成侧的三条崩价证据摆齐——PrismML 把 27B 多模态压到 5.9GB 本地可跑、豆包图像/视频推理 token 降 30%+、智谱让 AI 给自己的推理系统提速 3 倍；再摆真实渗透率——1.32 亿美国人用 AI 辅助购物但真正由智能体完成成交的仅约 3%、仅 7% 消费者信任 AI 代为下单、53% 对自主购买不适、ChatGPT 内购买转化率仅为跳转购买的三分之一。结论不是「AI 电商要来了」，而是：便宜的是生成，贵的是信任。然后给出谁做通了——Naver 靠履约数据（对话 +60%/成交 +82%）、亚马逊靠零售数据（ROAS +90%）、Mastercard 靠 Token 化凭证与 Verifiable Intent 解决授权。最后落到「你自己卡在哪一层」。

**入选理由**：今日最强交叉信号，且比首版更完整：首版只有「生成变便宜」三条，现在补上了「真实渗透率 3%」这组反面数据，叙事从「瓶颈转移」升级为「瓶颈在审批与信任层，且已有三种解法」。命中 profile_longterm 的「瓶颈转移论」与「成本结构分析」两个思维锚点。补位 🤖 赛道（连续两周以上 0 条发布）。与 09-17 主线完全不重叠。

### 2. 「被 AI 推荐」成了一门可测量的生意：Google share of voice 与国内 GEO 智能体同周落地

- **热度**：high　|　**形式**：tool-share　|　**赛道**：🛒 AI 电商自动化 / 🎨 创意广告
- **Hook**：X 刚更新了，对你意味着三件事 / 货架已经换了，大部分人还没意识到

**切入角度**：把两条同日素材并置：Google Merchant Center 的 AI Performance Insights 把「在 AI Mode 里被提及多少次」做成仪表盘并 GA 到五国；国内值得买科技联合华为云升级「值数 Matrix-GEO」追踪品牌在主流 AI 平台的可见性与推荐排名。再叠加可操作抓手——Conversational Attributes 六组结构化字段现在就能填、属性完整度分低的产品会被 AI 推荐跳过、lululemon 测试中对话式属性有 50% 概率被采纳。落到「这周该改哪个字段」。

**入选理由**：电商 GEO 这条选题在待采纳清单挂了多期，今天第一次有了平台官方仪表盘 + 结构化字段 + 国内对标产品三件套。与 09-15 已覆盖的「Google AI Max 迁移」不是同一件事（那条是投放侧自动化，这条是自然侧可见度测量）。

### 3. TikTok Shop 开始查 AI 商品图的「展示效果真实性」：发布前核对清单怎么做

- **热度**：high　|　**形式**：methodology　|　**赛道**：🛒 AI 电商自动化 / 🎨 创意广告
- **Hook**：X 刚更新了，对你意味着三件事 / 平台开始查的不是商品真假，是效果真假

**切入角度**：不做政策复述，直接给可执行的检查清单：AI 主图/模特图/场景图分别要核对哪几个维度（功能、材质、数量、颜色、使用效果），美妆健康/食品饮料/时尚服饰三个高风险类目各自的风险点在哪，四个版本（原图、AI 初稿、人工修订、上线版）的证据链怎么留。

**入选理由**：「AI 素材合规与披露」连续第四周被命中，此前一直待在待采纳清单里。今天有了具体平台、具体类目、具体处罚与 6 国操作手册，终于从趋势变成可执行清单。补位 🛒 赛道。

### 4. 平台正在收走创意生产：Amazon Creative Agent、Google 会话属性、TikTok Hummingbird 是同一件事

- **热度**：high　|　**形式**：news-commentary　|　**赛道**：🎨 创意广告
- **Hook**：X 刚更新了，对你意味着三件事 / 工具接管了流程，人还剩什么

**切入角度**：三条同日素材指向同一动作——亚马逊广告的 Creative Agent 用零售数据做产品/人群调研并生成全格式素材（零食品牌 ROAS +90%、CPM -26%）；Google 用 Conversational Attributes 把商品数据结构化后直喂 AI 回答；TikTok 的 Hummingbird 读实时投放数据生成变体并检测创意疲劳。合起来的判断是：素材生产、疲劳监控、本地化这三件原本由创意与买量团队做的事，正在被平台用自己的数据闭环接走。剩下给团队的是创意判断本身。给一个「哪些能力该外包给平台、哪些必须自己留」的分工框架。

**入选理由**：承接 profile_longterm「广告平台自动化 × 创意生产」交叉信号，且今日三条素材质量都很高（亚马逊带完整效果数据）。此前「创意疲劳监控」这个选题只有媒体预测，现在有了平台原生工具落地。

### 5. Pinterest 把广告位卖进视觉搜索：AI 导购吃掉的流量，广告主现在可以竞价了

- **热度**：medium　|　**形式**：news-commentary　|　**赛道**：🎨 创意广告 / 🛒 AI 电商自动化
- **Hook**：X 刚更新了，对你意味着三件事 / 货架已经换了

**切入角度**：背景是「96% 以上的 Pinterest 搜索不含品牌词」——这块正是 AI 导购最可能吃掉的无品牌意向流量，Pinterest 选择在这里直接开广告位而不是等智能体来接管。切口：Visual Search Ads 的竞价位置与格式、alpha 测试 CPI 最多改善 85%、以及它对「无品牌词流量怎么买」这件事的示范意义。可与 Google Conversational Attributes 并置成「AI 时代的关键词正在变成商品属性与图片」。

**入选理由**：🎨 赛道今日新增的平台侧素材，与此前所有「广告平台 AI 化」选题的区别在于它讲的是流量结构变化而非工具更新，且给了可量化的 CPI 数据。

### 6. 0.65 美元 vs 4 美元：省钱模型的性价比该怎么验，而不是听跑分

- **热度**：high　|　**形式**：methodology　|　**赛道**：🤖 AI 前沿
- **Hook**：大部分人用 X 的方式是错的 / 实测了 X，结果……

**切入角度**：以 Union Alpha 为样本给一套验证流程：跑分只看 Terminal-Bench 这类可复现的榜、成本按「完成任务」而不是「每百万 token」算、速度（15–19 tok/s，发一句「你好」等 2–3 分钟）在 Agent 长任务里是致命项、指令遵循差会吃掉省下来的钱。再补一条今日新出现的定价锚点：Unbiased Pareto 以 $2.50/$7.50 进入 262K 上下文档位。结论落到「什么任务可以换便宜模型，什么任务不能」。

**入选理由**：稀缺角度：匿名模型新闻满天飞但没人给验证方法。命中「成本结构分析」思维锚点。必须与 Ox Alpha（GLM-5.3-Flash）严格区分，两者常被混为一谈。

### 7. 本地跑一个 27B 多模态模型只要 5.9GB：什么时候该把 API 账单换成硬件

- **热度**：high　|　**形式**：tool-share　|　**赛道**：🤖 AI 前沿 / 🛒 AI 电商自动化
- **Hook**：实测了 X，结果…… / 成本降了一个数量级，为什么还没人搬

**切入角度**：最实操的一条成本选题。Bonsai 2 把 27B 从 54GB 压到 5.9GB、保留 98.2% 聚合性能、RTX 5090 上 143 tok/s、Apache 2.0 免费下载，代价是知识/视觉类指标退化明显且需要自研 llama.cpp 分支。给出一个换算框架：商品图批量打标、素材审核、客服 FAQ 这类高频低难度任务，按当前调用量算多久能回本；以及哪类任务（长上下文推理、复杂视觉理解）不该搬。旁证可用中国电信 Xing4.0-29B-A4B（29B 总参/4B 激活）。

**入选理由**：今日最硬的成本变化，且是「一次性硬件成本换掉按量付费」这个 profile_longterm 核心命题的直接样本。与此前所有模型发布类选题的区别在于：它给的是可算的账，不是能力榜。

### 8. AI 替代自己的半年度曲线：Anthropic 说 Claude 主导了 26% 的研发工作

- **热度**：high　|　**形式**：news-commentary　|　**赛道**：🤖 AI 前沿
- **Hook**：把 X 和 Y 连起来看 / AI 替代了多少，实验室自己说了

**切入角度**：3 月的约 1% → 8 月的 26%，AI 与人类协作完成 90% 以上的研究类工作，内部常驻约 3 万个 Agent，超 10 亿次决策中约 1/47,000 被拦截。切口不是「AI 多强」，而是：这是第一个实验室自曝的替代率，它的口径是研发不是运营，所以要谨慎外推；但把它和菜鸟的 90%/10%、智谱的 RSI Infra Agent 并置，三条线都在描述同一件事——AI 承担的执行比例在快速上升，而人类角色在向「设定目标 + 设计反馈 + 审核高风险变更」收缩。

**入选理由**：今日唯一一条「实验室自曝替代率」的一手数据，稀缺性极高。与主线选题共享部分素材但角度独立（那条讲瓶颈，这条讲替代节奏与度量口径），可作为系列第二篇。

### 9. 四天做一条广告：Goodwipes 恶搞 OpenAI 说明的 AI 广告新形态

- **热度**：medium　|　**形式**：case-study　|　**赛道**：🎨 创意广告
- **Hook**：实测了 X，结果…… / 把 X 和 Y 连起来看

**切入角度**：重点不是「AI 能做广告」，而是反应速度成了新的创意资产——品牌能在大厂 AI 叙事刷屏后几天内做出一条逐帧复刻的 parody。切口选「回应型创意」的生产流程：创意判断、素材生成、法律边界分别怎么处理。附制作方踩到的真实问题（AI 执着于让人坐在放下的马桶盖上、品牌包装资产还原难）。

**入选理由**：🎨 赛道今日少见的「创意方法论」型素材，而非模型更新型。与 09-17 已覆盖的三星广告条不同主体不同事件。

### 10. AI 短片的坑不在生成：Seedance 2.5 拍《沙丘 3》踩出来的三个真实问题

- **热度**：high　|　**形式**：case-study　|　**赛道**：🎨 创意广告
- **Hook**：实测了 X，结果…… / 大部分人用 X 的方式是错的

**切入角度**：照着那篇复盘讲三件事：参考图触发版权审核导致无法生成、只能保留抽象视觉特征并去掉高辨识元素（前后多花三天重做资产）；资产一致性决定人物跨镜头会不会「变一个人」；多轮修改时网页版生图会越改越糊，需要换工具链。附「提示词按秒拆」的具体写法与 3000 元积分的成本明细。

**入选理由**：罕见的踩坑型素材，含版权这条几乎没人写的实操红线。命中「AI 生视频」重点关注方向。

### 11. 125 字符的商品亮点：亚马逊二段标题之后，listing 的结构该重排了

- **热度**：medium　|　**形式**：tool-share　|　**赛道**：🛒 AI 电商自动化
- **Hook**：X 刚更新了，对你意味着三件事

**切入角度**：实操向：哪些信息该留在标题（品牌 + 核心词）、哪些该挪进 Item Highlights（使用场景、材质、卖点），AI 生成的内容为什么必须人工审一遍，以及改完之后怎么判断有没有生效。可与 Google Conversational Attributes 一起讲成「AI 可读的商品数据结构化」一课。

**入选理由**：最典型的「30 分钟能跑通」选题，符合实战派定位。补位 🛒 赛道。

### 12. 企业级 Agent 的三层竞争：Claude 收入口、百度做底座、Oracle 补网关

- **热度**：medium　|　**形式**：news-commentary　|　**赛道**：🤖 AI 前沿
- **Hook**：把 X 和 Y 连起来看

**切入角度**：同一周里三家分别从入口层（Anthropic 把 Cowork 并进主对话并推出 Docs/Slides）、底座层（百度智能云产业智能体操作系统、阿里 Qoder Cloud Agents 1.0）、治理层（Oracle MCP Gateway + HITL、Komodor 的 RBAC/审批闸/消费上限）挤同一个位置。对采购方的实际意义是选型维度变了：不只看模型能力，要看权限模型、审计能力、回滚机制和可归因性。给一份选型时的提问清单。

**入选理由**：承接 09-16 已提出的「可审计性成为准入证」线索，今日新增入口/底座/治理三层共 5 条素材，形成完整对照。09-17 覆盖的是 Claude Code Agent Teams（多人协作）与蚂蚁实践，本条是入口/底座/治理层的新进展，角度可区分。

### 13. AI Coding 贡献率 90% 之后，团队的度量指标该换了

- **热度**：medium　|　**形式**：methodology　|　**赛道**：🤖 AI 前沿
- **Hook**：大部分人用 X 的方式是错的

**切入角度**：把菜鸟和字节 TRAE 两个案例并置：前者 90% 贡献率对 10% 交付提速，后者 90% 代码由 AI 生成对 60% 吞吐提升。共同结论是「AI 代码贡献率」这个指标已经失真，应该换成需求交付吞吐率。给一个指标迁移的具体建议。

**入选理由**：与主线选题共享素材但角度完全独立（那条讲瓶颈在哪，这条讲怎么度量），可作为系列第二篇，不构成同日重复。

---

## 四、今日草稿（3 篇）

### 草稿 1 · wechat（deep-dive）

- **Hook 模式**：元模式 4「把 X 和 Y 连起来看」
- **标签**：🛒 AI 电商自动化 🤖 AI 前沿

```text
【公众号 · 长文提纲】

标题：3% 的真相：AI 电商卡在哪一层

开头两段：

这两天有一组数字放在一起看很有意思。一边是生成侧在崩价：有人把 27B 的多模态模型压到 5.9GB，笔记本就能跑；豆包把图像和视频推理的 token 消耗降了三成；智谱让 AI 给自己的推理系统做优化，十万张国产卡上两周把吞吐提到三倍。

另一边是真实成交：1.32 亿美国成年人用过 AI 辅助购物，但真正由智能体完成成交的只有大约 3%。只有 7% 的消费者信任 AI 未经确认就替自己下单。OpenAI 今年三月撤掉 Instant Checkout，原因是沃尔玛的数据显示，ChatGPT 里的购买转化率只有跳转购买的三分之一。

生成已经便宜到接近免费，成交却还卡在原地。卡在哪？卡在「谁有权替用户花钱、怎么证明它没越权」这一层。

正文分节：
1. 生成侧的三条崩价证据（27B→5.9GB / token 降 30% / 推理系统自优化 3 倍）
2. 3% 的真相：四组渗透率与信任度数据
3. 瓶颈在审批层：为什么「便宜」换不来「成交」
4. 已经做通的三条路——Naver 靠履约数据（对话 +60%、成交 +82%）、亚马逊靠零售数据（ROAS +90%）、Mastercard 靠 Token 化凭证与 Verifiable Intent 解决授权
5. 自检：你的生意卡在生成、分发，还是授权

结尾：给出三个自检问题，不用工具，十分钟能做完。

（完整文章在 Dashboard 上扩写）
```

**入选理由**：今日最强交叉信号：生成侧三条崩价证据 + 渗透率四条反向数据，形成「便宜的是生成，贵的是信任」的判断，并给出三条已验证的破局路径。命中「瓶颈转移论」与「成本结构分析」。补位 🤖 赛道（连续两周以上 0 条发布）。与 09-17 已发布主线完全不重叠。

### 草稿 2 · x（news-commentary）

- **Hook 模式**：元模式 2「X 刚更新了，对你意味着三件事」
- **标签**：🛒 AI 电商自动化

```text
TikTok Shop 刚更新了 AIGC 卖家指引，对你意味着三件事。

一是查的东西变了。以前查商品是不是真的，现在查展示效果是不是真的。AI 主图、AI 模特图、AI 场景图如果和实物差距过大，直接面临下架、限流甚至账号处罚。

二是类目有优先级。美妆健康、食品饮料、时尚服饰三个类目被点名了，AI 生成不存在的使用效果、放大食材分量、模特图与实际版型不符，都给了风险示例。

三是留痕。平台 09-16 起在印尼、菲律宾、越南等 6 个市场下发了操作手册，含发布前核对清单。建议自己留四个版本：原图、AI 初稿、人工修订版、上线版。

AI 作图本身没问题，问题是你有没有在发布前把每张图对着实物过一遍。
```

**入选理由**：补位 🛒 赛道，且是「AI 素材合规与披露」连续第四周被命中后终于落成内容。X 平台格式要求第一句给结论、术语保留英文，符合 profile_longterm 平台规则。全文 0 个感叹号，无震惊体。

### 草稿 3 · xhs（case-study）

- **Hook 模式**：元模式 1 变体「观察到 X，结果……」
- **标签**：🎨 创意广告

```text
标题：一条广告四天做完，被恶搞的是 OpenAI

最近有个湿厕纸品牌 Goodwipes 做了件事，我觉得比广告本身有意思。

OpenAI 的 Astra 广告在 X 上放了 1.35 亿次，那种光洁的、一切都被解决了的未来感。Goodwipes 用 AI 把这条广告逐帧复刻了一遍，然后揭穿主角们其实都坐在马桶上。从创意到成片，四天。操刀的是前 MullenLowe CEO 创办的 AI 原生代理商。

四天这个数字才是重点。

以前品牌想接一个大厂叙事的热度，得先立项、比稿、排期、拍摄、后期，等片子出来热度早凉了。现在四天能出一条逐帧对照的 parody，这意味着「反应速度」本身变成了创意资产。

同样的信号这周还有两个。TikTok 和 Nest Commerce 合作的 Hummingbird 9 月 23 日上线，它会读实时投放数据自动生成素材变体，还会检测创意疲劳。亚马逊广告的 Creative Agent 更直接：某零食品牌用它做素材和人群，一个月后 ROAS 涨了 90%，CPM 降了 26%。

三件事合起来看：平台正在把素材生产、疲劳监控、本地化这三件事，用自己的数据闭环接走。剩下给创意团队的，是判断本身——知道什么值得回应，以及为什么这样回应能打动人。

标签：#AI广告 #创意营销 #跨境卖家 #AI设计
```

**入选理由**：把三条同日素材（Goodwipes 案例 + Hummingbird + Amazon Creative Agent）串成「平台收走创意生产后剩下什么」的判断，比首版只有两条更完整。符合小红书「标题 + 要点正文 + 标签」格式。全文最多 1 个感叹号（0 个），无震惊体。

---

## 五、跨领域机会（3 条）

### 生成成本崩价 × 成交信任赤字

今天出现了一个罕见的对照：生成侧的成本在同一个窗口里连续崩了三次（27B 多模态压到 5.9GB 本地可跑、图像/视频推理 token 降 30%+、AI 给自己的推理系统提速 3 倍），而成交侧的渗透率只有约 3%，仅 7% 消费者信任 AI 代为下单。结论是「让 AI 生成」和「让 AI 成交」之间隔着一层授权与信任，这层不会因为生成变便宜而自动打通。已经打通的三条路各有依赖：Naver 依赖履约数据、亚马逊依赖零售数据、Mastercard 依赖 Token 化凭证 + Verifiable Intent。对卖家的含义是：你在 AI 电商上的投入，投在「生成」上的边际收益正在快速衰减，投在「可被智能体读取与信任的数据结构」上才是当前缺口。

### 平台收权 × 素材合规

TikTok Shop 开始查「展示效果真实性」，Google Merchant Center 上线属性完整度分并把结构化字段直喂 AI 回答，亚马逊推送 Item Highlights 结构化亮点，同时亚马逊 Creative Agent 与 TikTok Hummingbird 把素材生产与疲劳监控收进平台——四件事同月发生。对卖家的含义是，AI 素材的合规审核和商品属性的补全，从「合规成本」变成了「流量成本」，可以计入 ROI 而不只是风险。

### AI 生成产能 × 分发瓶颈

74 集短剧 7 天拍完、Seedance 2.5 让两人 12 天做 6 分钟概念片、Goodwipes 四天出一条广告、OpenClips 把一个商品链接直接变成可投放视频、万兴播爆一句话生成多条营销视频——生成侧的产能已经过剩。但同一批数据里，短剧的流量成本同比涨超 100%、收益端下滑 50% 以上、90% 的公司亏损、爆款占比不到 1%；菜鸟那边是代码贡献率 90% 而交付只快 10%。生成变便宜不会自动变成结果，验证与分发才是新的成本中心。

---

## 六、本周表现摘要

- **统计窗口**：2026-09-11 ~ 2026-09-18
- **发布量**：0 条　|　**单条中位数**：0　|　**单条最高**：—
- **覆盖不足赛道**：🤖 AI 前沿 / 🛒 AI 电商自动化 / 🎨 创意广告

Phase 1 学习第二十一期空转：inputs/published_last_7d.md 自 2026-08-27 录入后未再更新，文件内仍是 08-26~08-27 的 8 条记录且指标全部为「待补」，近 7 天（09-11 ~ 09-18）内 0 条可用发布记录，因此本期无法计算曝光分布、Top/Bottom 与 Hook 实证。选题与草稿继续沿用 profile_longterm.md 的 4 个长效元模式，不做权重调整。今日选题优先级仅依据主题相关性与赛道补位需求确定。

**本周发布数据**：inputs/published_last_7d.md 自 2026-08-27 录入后未更新，内容仍为 08-26~08-27 的 8 条记录且指标全部为「待补」；近 7 天窗口（2026-09-11 ~ 2026-09-18）内无可解析的发布记录

**市场行情**：本赛道配置不含市场行情数据

---

## 七、系统建议（仅记录，不自动修改配置）

### 7.1 信源（info_sources）

**建议提升（3）**

- **BestBlogs 公众号全量池(bestblogs_wechat2rss_all.opml，375 feeds)**（置信度 high）
  今日文章池在 🛒/🎨 两赛道信号不足，按 info_sources.json 中「只在文章池信号不足时扩展扫」的条件启用该池：375 个 feed 全部成功(err=0)，48h 内返回 1066 条新条目、270 个 feed 有新内容，是文章池(270 条 / 103 feeds)的约 4 倍产出。整池零错误、零超时，可靠性高于文章池(今日 24 个 feed 报错)。建议从 scan 提为 must_read 并纳入每日固定采集，而不是继续作为「不足时才扫」的兜底。
- **赛道扫描子代理(scan-ecom / scan-creative / scan-frontier)**（置信度 high）
  本期该通道产出 54 条、其中约 40 条为 RSS 池与 WebSearch 均未覆盖的素材(Mastercard AgentCard、Naver 履约智能体、Forkast 3% 渗透率、Pinterest Visual Search Ads、Amazon Creative Agent、Bonsai 2、Anthropic 研发占比等)，且带完整 hard_numbers 与丢弃说明，质量显著高于本期自采。建议固化为每日必跑的并行通道，并在 SKILL 中约定交付时限(本期到达时间晚于简报归档约 4 分钟，导致首版漏收并需要返工)。
- **跨境垂直媒体的平台规则快讯(跨税云 Ksher 等)**（置信度 medium）
  TikTok Shop AIGC 指引这类平台规则更新，最先出现在跨境垂直媒体而非主流科技媒体，RSS 池与 WebSearch 均漏掉，是今日靠定向检索才补上的。

**建议新增（4）**

- **searchengineland.com / ppc.land(Google Ads 与 Merchant Center 变更)**（置信度 high）
  Google Merchant Center 上线 AI Performance Insights、UCP 扩张、Business Agent 进 YouTube 广告这类平台侧更新，RSS 池与中文媒体均未覆盖，本次是扫描子代理与 WebSearch 补上的。这两个站是 Google 广告产品更新的首发渠道，建议注册为 must_read 级 web_source。
- **adweek.com / thedrum.com / modernretail.co(创意与广告行业)**（置信度 high）
  今日 🎨 赛道的三条创意方法论素材(Goodwipes 恶搞 OpenAI、Pinterest Visual Search Ads、Higgsfield Adathon)全部来自这三个站，中文 RSS 池完全没覆盖海外品牌 AI 创意案例。
- **forkast.news / paymentsjournal.com / aciworldwide.com(智能体商务与支付)**（置信度 high）
  今日最有价值的一组反面数据(3% 真实渗透率、7% 信任度、ChatGPT 内购买转化率仅跳转购买 1/3)全部来自这三个站。agentic commerce 的信任与授权层是当前缺口，建议长期跟踪。
- **shots.net / lbbonline.com / campaignbriefasia.com(广告制作行业)**（置信度 medium）
  BASF Voraxor、Herb Light、Cheil × Hanwha Vision 这类 AI 制作案例的首发渠道，补充「AI 创意广告」关注方向。

### 7.2 选题库（topic_library）

**建议新增（4）**

- **智能体商务的信任与授权层(谁有权替用户花钱 / 审批界面 / Verifiable Intent)**（置信度 high）
  今日首次出现一组完整的反面数据链:Forkast 3% 真实渗透率 + ACI 7% 信任度 + OpenAI 回撤 Instant Checkout,同时出现解法侧三条(Naver 履约数据、亚马逊零售数据、Mastercard AgentCard 的 Token 化凭证与 Verifiable Intent)。这是一个此前完全不在选题库里的独立品类,且是「AI 电商」叙事里最被忽略的一层。
- **AI 素材合规与披露(平台规则 + 发布前核对流程)**（置信度 high）
  连续第四周被 must_reads 命中,今日新增 TikTok Shop 菲越市场 AIGC 指引、6 国操作手册与三大高风险类目,已有具体平台规则与处罚措施,具备独立成题条件。该选题自 09-13 起反复出现在建议中但一直未入库,建议本期采纳。
- **AI 可见度测量(share of voice / GEO / AEO)**（置信度 high）
  今日出现平台官方仪表盘(Google AI Performance Insights GA 五国)与国内对标产品(值得买 × 华为云 Matrix-GEO)两类素材,「被 AI 推荐」正式变成可付费测量与优化的对象。与既有选题「电商 GEO」相邻但更聚焦「怎么测」而非「怎么优化」。
- **生成侧产能过剩与分发瓶颈**（置信度 high）
  今日 74 集短剧、Seedance 2.5 沙丘、Goodwipes 四天成片、OpenClips、万兴播爆五条独立素材同日指向生成产能过剩,而流量成本、交付吞吐率、爆款率三项数据共同指向分发与验证是新瓶颈。

### 7.3 定位漂移观察（positioning_drift）

- **观察**（置信度 medium）：近三周 profile_recent.md 反复出现「AI 素材合规 / 平台对 AI 内容的治理」线索(09-13 抖音降流、09-14 自然堂违规、09-16 子不语、09-18 TikTok Shop 指引),但 profile_longterm.md 的三个核心赛道里没有任何一条显式覆盖「合规与披露」。合规类内容是长文与小红书的天然素材,且与「AI 电商自动化」「创意广告」都有交集。
  **建议**：考虑在 profile_longterm.md 的「重点关注方向」表中增加一行「AI 素材合规与平台治理(归属 🛒 电商自动化 × 🎨 创意广告)」,或在写作风格指南中明确合规类选题的处理口径。仅为观察,不自动修改。

- **观察**（置信度 high）：本期采集暴露两个通道结构问题。(1) RSS 文章池(200 feeds)对中文平台规则类、海外广告创意类、智能体商务支付类新闻覆盖明显不足,今日 🛒 与 🎨 两个赛道的 must_reads 中有 6 条完全依赖扫描子代理或定向检索才拿到;同时 375 feeds 的公众号池整池可用却默认不跑。(2) 扫描子代理通道质量很高(54 条,其中约 40 条为其他通道未覆盖),但到达时间晚于简报归档约 4 分钟,导致首版按缺料归档、随后被迫重跑——这不是通道失效,是缺少交付时限约定。
  **建议**：把「公众号池 + 文章池」定为常规采集,定向检索与赛道扫描子代理从「补充通道」提为与 RSS 并列的主力通道;并在 SKILL 中为子代理通道约定交付时限与硬等待上限(否则会重演 09-14、09-18 两期「首版按缺料归档、随后被迫重跑」的返工)。
