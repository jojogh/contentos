# 图片方案

## 生成工具与口径

- 工具：`baoyu-imagine`（Google Gemini 图像模型）
- 原因：本机 `~/.baoyu-skills/.env` 仅有 `GOOGLE_API_KEY`，EXTEND.md 的默认 openai 通道无 key；故显式 `--provider google`
- 约束：**所有 AI 生成图不带任何文字**。产品名、数字、中英文标注一律不进画面——AI 生图在文字上不可靠，带字的图必须用 matplotlib 或设计稿

## 图片清单

| 文件 | 比例 | 用途 | 是否进正文 |
|---|---|---|---|
| `cover-wechat.png` | 2.35:1 | 公众号头条封面 | 否，后台单独上传 |
| `hero-16x9.png` | 16:9 | 封面母版，便于日后改裁 | 否 |
| `section-02-16x9.png` | 16:9 | 第 2 节「屏幕是工位不是隔断」的概念图 | 是 |

共 3 张。不生成数据图——本文没有需要可视化的数字序列。

## 封面概念

一台居中的云主机作为唯一底座，前面并排立着数块独立发光的屏幕。屏幕之间有明显缝隙，但全部接在同一块底板上。

要传达的不是「有几台机器」，而是「看起来分开了，其实共用一个底座」——正是文章的核心判断。

### Prompt（cover-wechat.png / 2.35:1）

> A single dark metallic base unit at the center, like a compact server chassis, with several tall luminous panels standing in a neat row in front of it. The panels are clearly separated by visible gaps and each glows in a slightly different cool hue, but thin glowing conduits run from every panel down into the same central base. Cool cyan and deep blue palette on a near-black background, soft volumetric light, subtle reflections on a dark floor. Clean industrial product-render aesthetic, shallow depth of field, centered composition with generous empty margins on both sides. No text, no letters, no numbers, no logos, no user interface elements.

### Prompt（hero-16x9.png / 16:9）

复用封面概念，改为 16:9 构图，主体略偏中下，上方留更多空间便于裁切。

## 内文图概念（第 2 节）

同样是无文字概念图，但角度不同：从**俯视**看一块共享的桌面/底板，上面并排放着几个独立的小工作台，所有工作台共用一个中央抽屉。

### Prompt（section-02-16x9.png / 16:9）

> Top-down view of a single large dark workbench surface. Several small tidy work areas are laid out side by side, each lit by its own soft pool of cool light and separated by subtle physical dividers that do not reach the ceiling — the dividers are low, clearly not walls. In the middle of the bench, one shared drawer is open, glowing faintly, connected by thin channels to every work area. Cool cyan highlights, dark matte surfaces, precise geometric arrangement, technical concept illustration look, no text, no letters, no icons, no logos.

## 规格与后处理

- 质量：`2k`
- 输出：PNG（封面与概念图都是渐变+光效，不需要 JPEG）
- 生成后统一缩到宽 1200 再内嵌进 HTML（见 `wechat-article-image-html-workflow`）
- 内嵌策略：`baoyu-markdown-to-html` 会丢 alt，需后处理补回

## 验收

- 画面无任何文字（AI 生字必错）
- 主体居中，两侧留足微信裁切安全区
- Chrome headless 全页截图核对版式后再定稿

## 不做什么

- 不伪造产品 UI、Grok/xAI 或 Meta 的 Logo
- 不生成带中文标注的架构图（这类图必须代码绘制）
- 不做「AI 替代人类」式的情绪化画面
