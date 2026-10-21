# 来源与主张账本

## 主张

| ID | 主张 | 类型 | 风险 | 来源 ID | 状态 | 正文用途 |
|---|---|---|---|---|---|---|
| C1 | Shopify AI Toolkit 提供开发者文档/API schema、代码校验、CLI store execute 三类能力 | fact | Low | S1, S3 | verified | 第一节 |
| C2 | 支持 Claude Code、Cursor、Codex、VS Code 等 AI 工具 | fact | Low | S1, S3 | verified | 第一节 |
| C3 | 插件自动更新，也可手动安装 skill 或 Dev MCP server | fact | Low | S1, S3 | verified | 第一节 |
| C4 | 典型用例之一是把 checkout/customer account UI extension 迁移到 Polaris web components | fact | Medium | S2 | verified | 第三节 |
| C5 | store execute 需用户选择执行时机，且当前无回滚，应在 dev store 验证 | inference/fact | High | S1, S6 | softened | 第四节 |
| C6 | 项目以 MIT 许可证开源 | fact | Low | S4 | verified | 第一节 |
| C7 | 发布时间为 2026 年 4 月 | fact | Medium | S2 (search 结果日期) | softened | 开头 |

## 来源

| ID | 发布方 | 标题 | 日期 | URL/文件 | 支持内容 | 访问日期 |
|---|---|---|---|---|---|---|
| S1 | Shopify | Shopify AI Toolkit 官方文档 | — | https://shopify.dev/docs/apps/build/ai-toolkit | C1、C2、C3 的能力与安装方式 | 2026-09-24 |
| S2 | Shopify | Introducing the Shopify AI Toolkit (developer changelog) | 2026-04-09（搜索结果页日期） | https://shopify.dev/changelog/shopify-ai-toolkit-connect-your-ai-tools-to-the-shopify-platform | C4 迁移用例、C7 发布时间 | 2026-09-24 |
| S3 | Shopify (GitHub) | Shopify/Shopify-AI-Toolkit | — | https://github.com/Shopify/Shopify-AI-Toolkit | C1、C2、C3 的安装命令与能力描述 | 2026-09-24 |
| S4 | Shopify (GitHub) | LICENSE | — | https://raw.githubusercontent.com/Shopify/Shopify-AI-Toolkit/main/LICENSE | C6 MIT 许可证 | 2026-09-24 |
| U1 | 用户提供 | Shopify AI Toolkit: Connect your AI tools to the Shopify platform | — | https://powercommerce.com/blogs/shopify-updates/shopify-ai-toolkit-released-build-apps-with-api-schemas-code-validation-and-cli-store-control | 提供初始话题与文章素材 | 2026-09-24 |
| S6 | 搜索摘要 | Shopify AI Toolkit 搜索结果摘要 | — | WebSearch 结果 | C5 “无回滚”提示 | 2026-09-24 |

## 待处理

- needs_verification：无
- unsupported：无
- removed：原始文章中“Gemini CLI 在官方支持列表中”未被官方文档明确列出，故不写入正文；原始文章中 70% 减少错误的案例为假设性，不采用。
- 搜索或访问限制：官方 changelog 页面正文未直接显示发布日期，日期来自搜索结果页 meta 信息；已降级为“2026 年 4 月发布”。
