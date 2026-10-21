# 图片计划

| 文件名 | 用途 | 放置位置 | 画面信息 | Alt | 生成状态 |
|---|---|---|---|---|---|
| cover-16x9.png | 封面母版 | 不进入正文 | 深色编辑风，多个发光模型节点从两侧汇聚到中央入口，前景是科研笔记与键盘，主体居中，留有裁切安全区 | 多个 AI 模型节点汇聚到一个统一入口 | generated |
| cover-wechat.jpg | 公众号头条封面 | 后台单独上传 | 从 16:9 母版居中裁成 2.35:1，1800×766，主体保持在中央安全区 | QuantClaw 科研模型订阅封面 | generated |
| images/inline-01-agent-workflow.png | 正文配图 | "接入本身并不神秘"或"容易出错的是验证环节"段后 | 深色编辑风：代码编辑器、服务器、文件堆与笔记，右上光门引出一道光接入笔记本，路径上四个几何检查点 | 模型接入工作流：从统一入口接入代码编辑器 | generated（1792×1024） |
| images/inline-01-agent-workflow-16x9.png | 正文配图（精确 16:9） | 同上 | 上一张居中裁切至 1792×1008 | 同上 | generated |

## 生成提示

Create a 16:9 editorial cover image for an article about a unified AI model subscription platform for university research teams.
Visual focus: several glowing abstract model nodes on the left and right converging into one bright, calm gateway in the center.
Context: a researcher's desk with an open notebook, a laptop edge, and soft evening light; the scene should feel like a working lab, not a science-fiction movie.
Style: clean modern editorial, deep navy and teal palette with one warm amber accent, high clarity, subtle depth of field, realistic materials, no fake UI text, no logos, no brand marks, no readable text, no charts, no numbers.
Composition: wide 16:9, strong central focal point, generous negative space at top and bottom for WeChat cover cropping, subject centered.
Avoid: generic stock-photo look, floating holograms, clutter, distorted text, unrelated objects, over-saturated colors.
Aspect ratio: 16:9.

## 说明

- 正文已有模型分工清单，不再生成数据图；具体数字和中文标注交给文字清单，避免 AI 生图写错字。
- 封面不内嵌进正文，后台单独上传。
- 如生成结果含可读文字、Logo 或错误中文，直接弃用重生成。
