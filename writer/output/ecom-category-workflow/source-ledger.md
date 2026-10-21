# 来源与主张账本

> 采集运行日：2026-09-16（产物 started_at `2026-09-16T01:40:54+00:00`）
> 本账本核对日：2026-10-15

## 主张

| ID | 主张 | 类型 | 风险 | 来源 ID | 状态 | 正文用途 |
|---|---|---|---|---|---|---|
| C1a | 类目 = Automotive > Exterior Accessories > Covers > Full Car Covers（node 15735581） | fact | Medium | U1-manifest | user_provided | 第二节 |
| C1b | 窗口 2025-07 → 2026-08；供应商报告 2769 条；请求/成功 28/28 | fact | High | U1-manifest | user_provided | 第二节 |
| C1c | 正向销量过滤后 1652 个唯一 ASIN | fact | High | U1-manifest + U1-csv | verified（manifest 声明 1652，CSV 实际 1652 行，交叉一致） | 第二节 |
| C1d | 产出三张表：target_asins(1652行×29列)、parent_child_map(1652行)、brand_summary(397品牌) | fact | High | U1-csv | verified | 第二节 |
| C1e | pagination_stop_reason = provider_pages_exhausted | fact | High | U1-manifest | user_provided | 第二节（关键限定） |
| C2a | sellerNation：CN 956 / US 421 / HK 195 / CA 60 / 空 15 / 其他 4 | fact | High | U1-csv 聚合 | verified | 第一节 |
| C2b | CN+HK = 1151/1652 = 69.7% ASIN 数 | fact | High | U1-csv 聚合 | verified | 第一节 |
| C2c | CN+HK 销售额 $12,179,721 / $15,106,134 = 80.6% | fact（**份额可信，绝对值口径未定义**） | High | U1-csv 聚合 | softened（只以份额入正文，绝对值加口径标注） | 第一节 |
| C2d | CN+HK 销量 207,082 / 240,823 = 86.0% | 同上 | High | U1-csv 聚合 | softened（同上） | 第一节 |
| C3a | 中位价 CN $50 / HK $60 / US $120 / CA $159 | fact | High | U1-csv 聚合 | verified | 第一节 |
| C3b | 中位评分 CN 4.20 / HK 4.20 / US 4.40 / CA 4.60 | fact | High | U1-csv 聚合 | verified | 第一节 |
| C3c | 全样本价格中位 $65，区间 $5.1–$1,700 | fact | Medium | U1-csv 聚合 | verified | 第一节 |
| C4a | 397 品牌中 240 个（60%）仅 1 个 ASIN | fact | High | U1-csv 聚合 | verified | 第三节 |
| C4b | 集中度：Top1 7.6% / Top10 36.9% / Top50 69.0% | fact | High | U1-csv 聚合 | verified | 第三节 |
| C4c | sellers=1 占 1486/1652 = 90.0% | fact | High | U1-csv 聚合 | verified | 第三节 |
| C4d | FBA 1016(61.5%) / FBM 483(29.2%) / NA 110 / AMZ 43 | fact | Medium | U1-csv 聚合 | verified | 第三节 |
| C4e | 评分数（`ratings`）中位 23；评分均值中位 4.3 | fact | Medium | U1-csv 聚合 | verified | 第三节 |
| C4f | 「销售额>$5,000 且评分数<100」筛出 192 个 ASIN | **inference**（本文自设筛选阈值的结果） | Medium | U1-csv 聚合 | verified（结果可复现） | 第三节 |
| C4g | lqs 中位 94（n=1316，满分 100） | fact（**字段定义未随产物给出**） | Medium | U1-csv 聚合 | softened（只报字段名与数值，不展开缩写含义） | 第三节 |
| C4h | 销售额第一为 EzyShade（站点 AU），约 $759,074 | fact | Medium | U1-csv 聚合 | verified | 第四节（反方） |
| C5a | manifest status = running | fact | High | U1-manifest | user_provided | 第四节（核心限定） |
| C5b | depth 段 detail/trend/review/market_months succeeded 全为 0 | fact | High | U1-manifest | user_provided | 第四节 |
| C5c | 但 raw 实际存在 28 搜索页 / 20 详情 / 10 趋势 / 5 评论 | fact | High | U1-raw 文件计数 | verified | 第四节 |
| C5d | phase_2_reports 目录为空 | fact | High | U1-raw 目录 | verified | 第四节 |
| C6 | 1 行 nodeLabelPath 乱码（ASIN B0G8H2749L） | fact | Medium | U1-csv 聚合 | verified | 第四节 |
| C7a | 产物带 schema_version / 分阶段目录 / manifest / raw 与 tables 分离等工程结构 | fact | Low | U1-raw 目录结构 | verified | 第五节 |
| C7b | 该运行由 AI 代理执行（目录位于 Codex 工作区） | fact（**依据路径推断**） | Medium | U1 路径 | softened（表述为「由 AI 代理执行并落盘的运行结果」，不点名具体模型/服务） | 第五节 |
| C7c | 「AI 降的是搭建成本，判断仍需团队保留」 | opinion | Low | — | 明确标注为作者判断 | 第五节 |
| C8 | units/revenue 时间口径未定义；抽样 328/400(82%) 满足 revenue≈units×price，故为同一内部口径 | **inference** | High | U1-csv 自核 | verified（推理链与吻合率可复现） | 第一节（口径声明） |

## 来源

| ID | 发布方 | 标题 | 日期 | URL/文件 | 支持内容 | 访问日期 |
|---|---|---|---|---|---|---|
| U1-manifest | 用户提供 | `run_manifest.json` / `phase_1_manifest.json` | 2026-09-16 | `…\research_output\car_cover_US_20260916_01\run_manifest.json` | C1a–C1c, C1e, C5a, C5b | 2026-10-15 |
| U1-csv | 用户提供 | `target_asins.csv`（1652 行 × 29 列） | 2026-09-16 | `…\phase_1_tables\target_asins.csv` | C2*, C3*, C4*, C6, C8 | 2026-10-15 |
| U1-csv | 用户提供 | `brand_summary.csv`（397 品牌） | 2026-09-16 | `…\phase_1_tables\brand_summary.csv` | C1d, C4a | 2026-10-15 |
| U1-csv | 用户提供 | `parent_child_map.csv`（1652 行） | 2026-09-16 | `…\phase_1_tables\parent_child_map.csv` | C1d | 2026-10-15 |
| U1-raw | 用户提供 | `phase_1_raw/` 原始 JSON | 2026-09-16 | `…\phase_1_raw\asin_detail_*.json`（20）等 | C5c, C7a | 2026-10-15 |
| U1-raw | 用户提供 | `phase_2_reports/`（空） | 2026-09-16 | `…\phase_2_reports\` | C5d | 2026-10-15 |

**说明**：本次未引入任何外部来源。全文所有事实主张均来自用户提供的运行产物，聚合统计由本任务在产物文件上直接计算得出（脚本置于 `/tmp/cos-an/`，未写入项目目录）。

## 待处理

- **needs_verification**：
  - `units` / `revenue` 字段的时间口径（月度？窗口合计？）——产物未随附字段定义文档。**已在正文显式标注**，未按事实陈述。
  - `lqs` 字段的完整定义与计分口径。**已在正文只报字段名与数值**。
  - `dimensionsType`（LS / EL15O / O / SB 等）取值含义未知 → **removed，正文完全不使用**。
  - `availableDate` 在 CSV 中的取值形态与 raw JSON 的 epoch 毫秒不一致 → **removed，正文不使用该字段**。
- **unsupported**：无。
- **removed**：`dimensionsType`、CSV 版 `availableDate`、`profit` 字段（仅提及其为估算值，不引用数值）。
- **搜索或访问限制**：本次未做外部检索；运行产物为唯一证据源，故所有结论限定在该运行范围内，不外推到「亚马逊车罩类目真实市场」。