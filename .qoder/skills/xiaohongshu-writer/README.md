# 小红书写作技能 (Xiaohongshu Writer Skill)

专业小红书内容创作助手，覆盖从选题到发布的全流程。

## 功能特性

- 🎯 **选题策划** - 爆款选题公式、热点追踪、选题验证
- 📝 **模板选择** - 标题模板、正文结构、爆款结构分析
- ⚠️ **违规规避** - 敏感词检测、平台规则、替代词库
- 📤 **发布优化** - 发布时间、标签策略、封面优化

## 安装方法

将此技能目录放到 OpenClaw 的 skills 目录下：

```
~/.qclaw/skills/xiaohongshu-writer/
```

## 使用方法

在 OpenClaw 中直接说：

- "帮我写一篇小红书种草笔记"
- "帮我想几个小红书选题"
- "检测这段话有没有违规词"
- "给我一个小红书爆款标题"

## 目录结构

```
xiaohongshu-writer/
├── SKILL.md                    # 技能主文件
├── references/
│   ├── compliance.md          # 违规词库
│   ├── templates.md           # 爆款模板库
│   └── topics.md              # 选题灵感库
├── scripts/
│   └── check_compliance.py    # 违规词检测脚本
└── README.md
```

## 违规词检测脚本使用

```bash
# 检测文本
python scripts/check_compliance.py "你的笔记内容"

# 检测文件
python scripts/check_compliance.py -f 笔记.txt
```

## 作者

由 Claude Code 创建

## 许可证

MIT License
