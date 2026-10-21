# 来源与主张账本

## 主张

| ID | 主张 | 类型 | 风险 | 来源 ID | 状态 | 正文用途 |
|---|---|---|---|---|---|---|
| C1 | 该 Skill 以用户痛点为锚点，对照竞品 Listing 与评论评估解决程度 | fact | Medium | U1 | user_provided | 第一节 |
| C2 | Skill 调用 `asin_detail`、`review`、`keepa_info` 等 SellerSprite MCP 工具 | fact | Medium | U1 | user_provided | 第四节 |
| C3 | `review` 每次最多返回 20 条，结论需标注样本限制 | fact | High | U1 | user_provided | 全文与边界 |
| C4 | 评分只有三档：已解决得很好 / 解决了一半 / 基本没解决 | fact | Medium | U1 | user_provided | 第二节 |
| C5 | 最终输出《痛点-竞品解决矩阵表》《竞品解决方案拆解表》《竞品解决方案分析表》 | fact | Medium | U1 | user_provided | 第三节 |
| C6 | 安装时 secret-key 放在 `headers`，URL 为 `https://mcp.sellersprite.com/mcp` | fact | High | U1 | user_provided | 第五节 |
| C7 | 示例输出明确标注“仅展示格式，不代表真实数据” | fact | High | U2 | verified | 全文脚注 |
| C8 | 评论字段常用 `content`、`date`，销量字段为 `units`、`revenue` | fact | Medium | U1 | user_provided | 第五节 |
| C9 | 评分是编辑判断，不是统计显著性结论 | opinion | Medium | E1 | verified | 边界一节 |

## 来源

| ID | 发布方 | 标题 | 日期 | URL/文件 | 支持内容 | 访问日期 |
|---|---|---|---|---|---|---|
| U1 | 用户提供 | amazon-competitor-analyzer Skill 文档 | — | `E:\project\amazon-competitor-analyzer-MCP-skill\.claude\skills\amazon-competitor-analyzer\SKILL.md`；`README.md`；`references/detailed-guide.md` | C1-C6、C8 | 2026-10-19 |
| U2 | 用户提供 | 示例输出 sample-output.md | 2026-08-10 | 同目录 `examples/sample-output.md` | C7 | 2026-10-19 |
| E1 | 编辑判断 | 本文作者基于评分机制的分析 | — | — | C9 | 2026-10-19 |

## 待处理

- needs_verification：SellerSprite MCP 的当前接口行为、返回字段和限流策略未独立核实，正文统一写成“按这份 Skill 的设定/文档说明”
- unsupported：未使用真实 ASIN 运行并核实任何结论；正文不得出现具体销量、评分或评论数量作为真实案例
- removed：不引用任何未在 Skill 文档中出现的第三方数据或行业结论
- 搜索或访问限制：本文不需要外部检索，来源为用户提供的本地文件
