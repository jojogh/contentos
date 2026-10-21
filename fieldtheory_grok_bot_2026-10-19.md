# Field Theory 书签检索：Grok Bot

- 检索日期：2026-10-19
- 数据源：本地 Field Theory 书签库（`ft search`）
- 命中情况：`grok` 30+ 条，`"grok bot"` 短语 26 条
- 说明：下列日期为帖子发布日期（按 `ft` 输出显示）

---

## 1. 官方资源与平台动态

- **@distortgeekin（10-03）**：xAI 悄悄发布了 **15 篇官方 Grok Bot 指南**，由团队亲手写，几乎没人讨论
  https://x.com/distortgeekin/status/2106376244270973421
- **@GrokBotRadar（09-10）**：专门追踪 Grok Bot 新功能/新 bot 的雷达账号上线
  https://x.com/GrokBotRadar/status/2097884606569533874
- **@wuanguscc（09-11）**：SpaceXAI 9/15 起在旧金山办三天「Grok Bot Galaxy」，现场从零造一家公司
  https://x.com/wuanguscc/status/2098204554349494523
- **@0xlangeai（09-09）**：Lauren Tan 55 分钟 webinar 拆解。最值钱的 bot 不写代码，只记着其他 20 个 bot 在干嘛；号称省 ~30 小时/周、顶掉 ~$9k 招聘
  https://x.com/0xlangeai/status/2097645454846804235
- **@joshkim（09-16 / 09-18）**：SpaceXAI 市场团队自己用 Grok Bot 跑端到端营销 campaign 的演示
  https://x.com/joshkim/status/2100996894290006294
  https://x.com/joshkim/status/2100345926170911003
- **@poteto（09-15）**：三天从零搭一家公司的 speedrun 直播
  https://x.com/poteto/status/2099875666313527436

## 2. 上手教程

- **@AYi_AInotes 推荐的 @xaiwind 手把手拆解（09-16）**：库里评价最高的入门篇，适合从零到能干活
  https://x.com/AYi_AInotes/status/2100097459959525420
- **@KinGao476942（09-12）**：面向非技术/文科生的最佳实践合集
  https://x.com/KinGao476942/status/2098707368536392037
- **@dingyi（09-12）**：Growth 增长领域的 bot 集合
  https://x.com/dingyi/status/2098759281831301315

## 3. 实战配置 / 组合玩法

- **@app_sail（10-02）**：**Grok bot + Orca + Tailscale + Claude Code**，在美国云主机上注册 Claude 再装 CC，主打国内可用
  https://x.com/app_sail/status/2106003366749126914
- **@wlzh（10-03）**：点出痛点——Grok Bot / Muse 跑在全新鲜浏览器里，一干活就撞登录墙，给了个 Chrome 插件桥接方案
  https://x.com/wlzh/status/2106268274350870642
- **@maestrooth（09-22）/ @0xCodila（09-19）**：「Jev + GrokBot」被称为最便宜最快的 agent 栈
  https://x.com/maestrooth/status/2102453475078533209
  https://x.com/0xCodila/status/2101433560796467348
- **@gippp69（10-05）**：6 个 bot 一支队伍过夜跑出 612 个完成任务、47 个被拦动作、89 次拒绝交接
  https://x.com/gippp69/status/2107153066134790406

## 4. 场景案例

- **Marketing OS 开源**：@vladdubchak_x（08-21）、@OriSilver（08-25）整套营销团队配置开源；@higgsfield 集成送 100 credits
  https://x.com/vladdubchak_x/status/2090770900241297844
  https://x.com/OriSilver/status/2092225524210827424
  https://x.com/higgsfield/status/2091263895256396218
- **@sairahul1（09-01）**：内容/SEO/社媒/研究/分发/分析全自动
  https://x.com/sairahul1/status/2094723931320311866
- **@KinGao476942（09-19）**：用五个专家 bot 做全自动工作流，把 X 优质内容变成通勤播客库
  https://x.com/KinGao476942/status/2101325175308652924
- **@XAngus（08-29）**：虚拟信用卡——你逐笔批准，bot 直接帮你买东西
  https://x.com/XAngus/status/2093509616655368551
- **@bourneliu66（09-01）**：对比 OpenClaw/Hermes 的实战场景梳理
  https://x.com/bourneliu66/status/2094829341473751381
- **@ericosiu（08-22）**：公司如何配置 Grok Bot
  https://x.com/ericosiu/status/2091231428184822258
- **@indie_maker_fox（08-24）**：GitHub 上的 Grok Bot 开源重建版
  https://x.com/indie_maker_fox/status/2091853443287921091

---

## 观察到的线索

1. **三条主线最值得先看**：官方指南（15 篇）、Marketing OS 开源、Claude Code 组合玩法。
2. **中文圈落地细节更具体**：@xaiwind、@app_sail、@wlzh、@KinGao476942 覆盖了登录态、云主机、网络这几类实际卡点。
3. **常见痛点**：全新浏览器无登录态（@wlzh）、云主机选型与国内访问（@app_sail）、多 bot 团队的交接与拦截（@gippp69）。

## 检索命令

```bash
ft search "grok" --limit 50
ft search "grok bot" --limit 50
```
