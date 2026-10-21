# 公众号文章任务书

- 账号/栏目：未提供（默认面向 Shopify 开发者、电商技术团队、独立开发者/ agency）
- 目标读者：正在或计划基于 Shopify 做应用开发、店铺定制、批量运营的技术人员与决策者
- 阅读场景：看到 Shopify 发布新工具，想判断“这跟我的团队有什么关系，现在要不要投入”
- 读者真正问题：AI Toolkit 是又一个营销概念，还是真的能减少开发返工？它能做什么、不能做什么、上生产前要补哪些治理？
- 读后交付：清楚 AI Toolkit 的三项核心能力、一个可落地的试用场景、以及采用前的安全 checklist
- 核心判断：AI Toolkit 的本质是“给 AI 补上下文”——把官方文档、API schema 和受控的 CLI 权限交给 agent，减少“看起来对、跑起来错”的返工；但它不取消人工审核，也不等于生产环境可以放任 agent 自动执行。
- 新增价值：用 Shopify 官方文档和 GitHub 仓库核清能力边界；把“store execute”权限风险和“无回滚”限制说在前面；给出从插件安装到 dev store 试用的具体路径。
- 文章类型：热点解读 + 痛点解法
- 目标长度：2000–2500 中文字符
- CTA：先在 dev store 装插件，跑一个非关键迁移或查询任务，再决定是否扩大权限

## 适用边界

- 适用：已在使用 Claude Code / Cursor / Codex / VS Code 等 AI 工具的 Shopify 开发者；需要批量处理商品、 metafield、主题片段的团队；正面临 checkout/customer account UI extension 迁移的团队。
- 不适用：没有 Shopify CLI 基础、不了解 OAuth/scope 概念的非技术用户；希望“全自动无人运维”的商家。
- 最强反方：AI 直接操作店铺太危险，自动更新插件也可能引入未预期行为。
- 本文如何回应：强调“用户选择何时执行”、最小权限 token、dev store 先行、审计日志，不美化风险。

## 个人材料

- available: false
- 用户明确提供的经历、原话或观察：无
- 允许写成第一人称的范围：仅编辑判断，不虚构亲历
- 禁止补写的空白：不使用“我朋友”“我测了一下”等虚构场景

## 需要证明的主张

1. Shopify AI Toolkit 提供文档/API schema、代码校验、CLI store execute 三类能力（官方文档/ GitHub）。
2. 支持 Claude Code、Cursor、Codex、VS Code 等常见 AI 工具（官方文档/ GitHub）。
3. 插件自动更新，也支持手动安装 skill 或 Dev MCP server（官方文档/ GitHub）。
4. 典型用例是 checkout/customer account UI extension 迁移到 Polaris web components（官方 changelog/ 文档）。
5. store execute 需要用户授权、最小权限、且当前不支持回滚，必须在 dev/staging 验证（官方文档说明“你选择何时执行”；搜索摘要补充无回滚）。
6. 项目为 MIT 开源（GitHub LICENSE 文件）。
