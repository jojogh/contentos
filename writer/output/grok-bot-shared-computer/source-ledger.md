# 来源与主张账本

## 主张

| ID | 主张 | 类型 | 风险 | 来源 ID | 状态 | 正文用途 |
|---|---|---|---|---|---|---|
| C1 | Grok Bot 的云电脑分配给「用户账号」，不是分配给单个 bot；账号内所有 bot 共用同一台 | fact | High | S1 | verified | 第 1、2、3 节 |
| C2 | 每只 bot 在共享电脑上有自己的 screen，但 screen 是工作区不是安全边界 | fact | High | S1 | verified | 第 2 节 |
| C3 | 文件、命令行凭据、浏览器 cookie/登录态、连接器均为账号级共享 | fact | High | S1 | verified | 第 2 节 |
| C4 | 官方警告原文：不要把另一只 bot 不该用的凭据或文件放上去 | fact | High | S1 | verified | 第 2 节（引文） |
| C5 | 一块 screen 同一时间只处理一个 computer-use 任务 | fact | Medium | S1 | verified | 第 4 节 |
| C6 | 持久文件应放在 `/workspace` | fact | Low | S1,S4 | verified | 第 4、6 节 |
| C7 | Meta Muse 采用「每用户独立 Linux VM + Sentinel 唯一权限方 + 凭据运行时外即时注入」 | fact | Medium | S2 | verified（二手转述） | 未采用（已删，避免第二手细节） |
| C8 | Grok Bot 为账号级隔离（Firecracker 隔用户，账号内共享运行时） | fact | Medium | S2 | verified（二手转述） | 第 4 节 |
| C13 | 指南原文称「each Grok Bot agent receives its own dedicated cloud virtual machine」 | fact（他人文本） | High | S4 | verified（逐字引文） | 第 1 节（引文） |
| C14 | 同一指南又称「all bots on your account share the underlying cloud environment」，并据此推荐认证一次全员可用 | fact（他人文本） | High | S4 | verified（逐字引文） | 第 2 节（引文） |
| C14b | C13 与 C14 在同一文本内互斥；S1 支持 C14 | inference | High | S1,S4 | verified（三处原文可并置） | 第 2、3 节 |
| C15 | 指南称 VM 重建会清空 `/home`、`/usr/local`、全局 apt 包与手动安装的 CLI 工具，只有 `/workspace` 存活 | fact（他人主张） | Medium | S4 | verified（逐字引文，属作者主张） | 第 6 节 |
| C16 | 指南称 Grok Bot 云环境提供免密 root（`sudo (ALL) NOPASSWD: ALL`） | fact（他人文本） | High | S4 | verified（逐字引文） | 第 6 节，并接 C3 作风险推论 |
| C17 | 交互式会话交接：撞墙暂停、用户手动完成登录、bot 只拿会话凭证 | fact（他人方法） | Medium | S4 | verified（逐字引文） | 第 6 节 |
| C18 | 「bot 的 profile description 就是组织架构图的一行，总参谋长靠读描述派工」 | fact（他人文本） | Medium | S4 | verified（逐字引文） | 第 6 节 |
| C19 | 指南的热度：1,255,795 次浏览、399 赞、58 转发、1,030 收藏、31 回复 | fact | Low | S4 | verified（FxTwitter 返回的计数，取数时点 2026-10-18） | 第 1 节 |
| C10 | 指南主张的「总参谋长 + 专员」组织架构、Teach-a-Task 生成 Skill File、可逆性矩阵 | opinion（他人方法） | Medium | S4 | verified（引述为作者主张） | 第 5、6 节 |
| C11 | 「并行度上限与权限暴露面积是同一个旋钮」 | inference | Medium | C1,C2,C3,C5 | verified（推理链完整，正文已标注为推论） | 第 4 节 |
| C9 | Grok Bot 没有独立订阅，只能通过档位获得 | fact | High | S3 | removed（正文不再写价格/档位） | 无 |

## 来源

| ID | 发布方 | 标题 | 日期 | URL/文件 | 支持内容 | 访问日期 |
|---|---|---|---|---|---|---|
| S1 | xAI | Grok Bot — Computer and Apps（官方文档） | 未标注 | https://docs.x.ai/grok-bot/computer-and-apps | C1–C6 全部原文 | 2026-10-18 |
| S2 | Forkast | Same Blueprint, Different Locks: GrokBot and Muse Ship the Persistent Agent VM | 2026-09-13 | https://forkast.news/same-blueprint-different-locks-grokbot-and-muse-ship-the-persistent-agent-vm/ | C7、C8 | 2026-10-18 |
| S3 | mem0.ai | Grok Bot Guide: Pricing, Features & Setup (2026) | 2026 | https://mem0.ai/blog/grok-bot-guide | 定价（已全部弃用） | 2026-10-18 |
| S4 | @monokern | Grok Bot 架构指南（X 长文） | 2026-08-20 | https://x.com/monokern/status/2090490444224331787 | C6、C10、C13–C19 | 2026-10-18（全文经 FxTwitter 取得） |

### S1 关键原文（逐条备查）

- "Every Bot on your account uses the same computer."
- "The computer is assigned to your user account, not an individual Bot."
- "Each Bot gets its own screen on the shared computer"
- "The screens are separate work surfaces, not separate security boundaries."
- "The computer has a shared workspace at `/workspace`."
- "Do not place a credential or file on it if another Bot on your account should not be able to use it."
- 支持性表述："Files are visible to every Bot"、"Command-line credentials are shared"、"Browser cookies and signed-in sessions are shared"

### S4 关键原文（本地全文：`source-fulltext.md`，9,678 字符 / 1,387 词 / 6 图）

- 第 7 行（C13）："Instead of running inside an ephemeral chat window, each Grok Bot agent receives its own dedicated cloud virtual machine - complete with a persistent web browser, terminal, file system, and background process runner."
- 第 67 行（C14）："Because all bots on your account share the underlying cloud environment, authenticating a service once makes that active session available to your entire agent roster."
- 第 57–65 行（C17）：Interactive Session Handoffs 四步流程
- 第 47–49 行（C18）："In Grok Bot, a bot's profile description is its entry in the team org chart." / "it scans the descriptions of all available bots in the workspace"
- 第 113 行（边界条款）："YOU MUST NEVER click 'Send' or transmit an external email without explicit human review and approval in the chat thread."
- 第 119–131 行（C15）：VM 重建清空 `/home/box/deps`、`/usr/local`、全局 apt 包；只有 `/workspace` 保证存活
- 第 143 行（C16）："Because Grok Bot cloud VMs grant passwordless root access (`sudo (ALL) NOPASSWD: ALL)`..."
- 原始 JSON：`source-tweet.json`；6 张原图：`source-images/`

## 待处理

- **removed｜定价数字**：搜索中出现 $30 / $60 / $100 / $200 / $300 多个金额，被不同来源指向不同档位，互相矛盾；`x.ai/bot` 官方定价页返回 403 无法核实。正文已完全不写价格与档位。
- **removed｜责任条款上限**：搜索摘要称条款将 agent 行为责任归于用户、赔偿上限为已付费用或 $100。未打开原始条款，属 High 风险，整条不采用。
- **removed｜企业版功能清单**：SSO/SCIM、Audit Log、Action Recording、Team Secrets 等来自搜索聚合，未回一手页面，不采用。正文提及「企业版审批与审计」仅作观察信号，不断言功能细节。
- **removed｜「50 routines per account」**：中文来源给 50，mem0 称官方未公布上限，冲突，不采用。
- **removed｜Meta Muse 对照段**：原稿第 4 节整段源自 Forkast 二手转述。C7 仍为 verified（二手），但因无法回 Meta 一手文档，本轮改写中整段删除，避免用第二手细节撑核心论证。
- **needs_verification｜上线时间线**：beta 2026-08-11 有两处独立来源支持（S2、S3）；8 月下旬扩档、9 月 3 日企业版、9 月 28 日 Team Bots 公测仅见于搜索聚合，正文不写具体日期。
- **access limit｜S1 路径**：`docs.x.ai/grok-bot/computer-and-apps.md` 404，无扩展名路径成功。
- **resolved｜S4 全文**：本轮经 `x-tweet-fetcher`（FxTwitter API）取得指南完整正文 9,678 字符与全部 6 张配图，先前「仅得摘要、一律转述不复读原句」的限制解除。C13、C14、C16 等此后可逐字引用，正文已按原文引述。
