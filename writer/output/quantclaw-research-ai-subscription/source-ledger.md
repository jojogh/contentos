# 来源与主张账本

## 主张

| ID | 主张 | 类型 | 风险 | 来源 ID | 状态 | 正文用途 |
|---|---|---|---|---|---|---|
| C1 | DeepSeek-V4.1-Flash-1017 于 2026-10-17 发布，官方称基准表现更强、任务完成更快、输出更短，并针对 DeepSeek Harness、腾讯 CodeBuddy、WorkBuddy 优化 | fact | High | S1 | verified | 第二节 |
| C2 | Kimi K3 参数规模 2.8T、上下文 100 万 token、权重开放，官方强调长周期编码、大代码库、终端工具使用和深度推理 | fact | High | S2 | verified | 第二节 |
| C3 | Claude Opus 5.5 于 2026-09-22 发布，1M 上下文、128K 最大输出、$4/$20 每百万 token，定位长周期 agentic coding 与知识工作 | fact | High | S3 | verified | 第二节 |
| C4 | GPT-6.1 Sol 于 2026-09-29 发布，$2/$10 每百万 token（272K 输入以内），定位复杂编码与专业工作的低成本模型 | fact | High | S4 | verified | 第二节 |
| C5 | QuantClaw 面向高校与科研机构提供一站式模型订阅，覆盖 DeepSeek V4.1 Flash、Kimi K3、Claude Opus 5.5、GPT-6.1 Sol，可配合 Claude Code、Codex 等 agent 客户端；通过问卷发放试用 token 和连接方式 | fact | High | U1 | user_provided | 第五、六节 |
| C6 | 科研团队接入多个模型存在账号、计费、开票、客户端配置和复现成本 | inference | Medium | 无 | softened | 第一节 |
| C7 | 四个模型存在任务分工，可按任务类型优先选择 | inference | Medium | S1-S4 | softened | 第二节 |
| C8 | 试用前应确认数据合规、经费、额度、可复现性 | opinion | Low | 无 | 编辑判断 | 第四节 |
| C9 | “QuantClaw”在公开检索中与多个无关项目同名，未找到该科研订阅平台的独立官网 | fact | Medium | S5 | needs_verification | 不进入正文，审计说明 |

## 来源

| ID | 发布方 | 标题 | 日期 | URL/文件 | 支持内容 | 访问日期 |
|---|---|---|---|---|---|---|
| S1 | DeepSeek API Docs | DeepSeek-V4.1-Flash-1017 | 2026-10-17 | https://api-docs.deepseek.com/news/news261017/ | 发布名称、日期、官方定位、agent 环境优化 | 2026-10-20 |
| S2 | Kimi API Platform | Kimi K3 Quickstart | 未标注 | https://platform.kimi.ai/docs/guide/kimi-k3-quickstart | 模型 ID、2.8T 参数、1M 上下文、权重开放、能力定位 | 2026-10-20 |
| S3 | Anthropic | Claude Opus 5.5 overview | 2026-09-22 | https://platform.claude.com/docs/en/models/opus-5-5/overview | 发布日期、1M 上下文、128K 输出、$4/$20、定位 | 2026-10-20 |
| S4 | OpenAI API Docs | API Changelog（GPT-6.1 Sol） | 2026-09-29 | https://developers.openai.com/api/docs/changelog?product=codex | 发布日期、$2/$10、272K 输入以内、定位 | 2026-10-20 |
| S5 | Web 检索 | QuantClaw 同名项目（量化交易、C++ OpenClaw 实现、精度路由插件等） | 2026-10-20 | 检索结果 | 说明名称存在同名冲突，未找到科研订阅平台官网 | 2026-10-20 |
| U1 | 用户材料 | QuantClaw 试用说明 | 2026-10-20 | 本任务用户输入 | 平台定位、模型清单、客户端兼容、试用方式 | 2026-10-20 |

## 待处理

- needs_verification：QuantClaw 的独立官网、主体信息、服务条款、数据合规说明、试用额度与计费方式；正文已明确“以平台发放的说明为准”
- unsupported：平台的价格、并发数、SLA、安全认证、客户案例、国产算力部署细节；未写入正文
- removed：未使用“国产算力”“数据不出境”等未经证实的表述
- 搜索或访问限制：Anthropic 官方公告页抓取超时，改用 platform.claude.com 官方模型文档；OpenAI 官方公告页未直接抓取，改用 developers.openai.com changelog
