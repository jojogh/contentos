# 翻译任务上下文（EN → zh-CN）

## 目标
把 Dan Koe 的长文《The influencer is dead. The Age of Experience is here.》完整译成简体中文，供微信公众号发布。

## 目标语言与读者
- 目标语言：简体中文（zh-CN）
- 读者：大众读者（内容创作者、独立开发者、想做个人品牌的人），不预设营销术语背景
- 风格：故事化——叙事流畅、短句有力、保留作者直呼"你"的对话感

## 作者声音
Dan Koe 的写法有三个特征，译文必须保留：
1. **短段落、多断行**：一句话一段是常态，不要合并成密集长段。
2. **断言式**：先抛结论再解释。"没有人拥有一个话题。"独立成句。
3. **破折号插入语**：中文用"——"，不要改成括号或逗号堆叠。

## 术语表（全篇强制一致）
- influencer → 网红
- personal brand → 个人品牌
- artisan → 匠人
- body of work → 作品体系
- swipe file → 素材库（swipe file）
- idea density → 思想密度
- content pillars → 内容支柱
- intellectual signature → 知识签名（intellectual signature）
- validated ideas → 已验证想法
- mid-sized creators → 中型创作者
- low-ticket → 低客单价
- decentralized education system → 去中心化的教育系统
- second renaissance → 第二次文艺复兴
- entropic → 熵值高

## 结构要求
- 保留全部 Markdown 结构：1 个 H1（标题）、4 个 H2、4 个 H3、列表、引用段。
- 原文 H2/H3 必须一一对应译出，不得增删小节。
- 两段他人引言（署名 Benjamin Antoine、Mauricio Ruiz）原样保留为正文段落 + 署名行 `—— 名字`。
- 提示词段（"I talk about [topics]..." 与 "Help me find new angles..."）保持为可复制的普通段落/有序列表，不改成引用块。

## 翻译难点
1. 长句按意群拆分，但不得丢信息、不得添加原文没有的判断。
2. `you are the niche` → 保留引号："你就是那个细分领域"。
3. `The ultimate moat ... is an opinion.` → "最终的护城河……就是一个观点。"保留双关力度。
4. `No shit.` → "废话。"（保留粗粝感，不升级为脏话）
5. 原文笔误（these day / get's / a a larger / where's the best places）按正确语义翻译，不复制错误。
6. Eden 是作者自家产品，照实译出，不删、不加"广告"提示。
7. 数字与专有名词（1.7 million views、James Clear、Jordan Peterson、Alan Watts、Marcus Aurelius、Mark Manson、Alex Hormozi、Tom Bilyeu）原样保留；人名不译。

## 输出
- 文件：`translation.md`
- frontmatter：保留 `sourceUrl`、`sourceTitle`、`author`、`publishedAt`，正文含 H1 因此不再写 `title`
- 正文末尾不得添加译者按、总结或任何原文没有的内容
