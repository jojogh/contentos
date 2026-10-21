#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书违规词检测脚本
检测内容中的敏感词、违规词，并提供替代建议
"""
import io, sys
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import re
import sys
from typing import Dict, List, Tuple

# 违规词库
VIOLATION_WORDS = {
    # 绝对化用语
    "绝对化": {
        "words": [
            "第一", "No.1", "NO.1", "最好", "最优", "唯一", "独家",
            "顶级", "极致", "绝对", "一定", "百分百", "100%",
            "永久", "终身", "首个", "唯一", "首创"
        ],
        "severity": "高",
        "suggestion": "使用'推荐'、'之一'、'出色'等替代"
    },

    # 医疗功效
    "医疗功效": {
        "words": [
            "治疗", "治愈", "根治", "药效", "疗效", "处方", "药方",
            "消炎", "抗菌", "祛斑", "淡斑", "瘦身", "减肥",
            "丰胸", "隆胸", "抗衰老", "抗皱", "生发", "防脱",
            "祛痘", "消痘", "降血压", "降血糖", "治疗痘痘"
        ],
        "severity": "高",
        "suggestion": "使用'改善'、'缓解'、'帮助'等替代"
    },

    # 引导交易
    "引导交易": {
        "words": [
            "加微信", "+V", "加v", "微信号", "点击链接", "扫码购买",
            "扫二维码", "二维码", "购买链接", "加QQ", "淘宝搜索"
        ],
        "severity": "中",
        "suggestion": "使用'主页有'、'私信我'等替代"
    },

    # 虚假宣传
    "虚假宣传": {
        "words": [
            "效果立竿见影", "包治百病", "无效退款", "专家推荐",
            "获得认证", "明星同款", "必买", "一定要买"
        ],
        "severity": "高",
        "suggestion": "避免夸大效果，实事求是"
    },

    # 敏感内容
    "敏感内容": {
        "words": [
            "傻逼", "操你", "妈的", "他妈", "卧槽", "我操"
        ],
        "severity": "高",
        "suggestion": "删除或替换为文明用语"
    }
}

# 替代词建议
REPLACEMENTS = {
    "第一": "之一/领先",
    "最好": "推荐/出色",
    "唯一": "特色/特别",
    "顶级": "高端/优秀",
    "绝对": "通常/大概率",
    "治疗": "改善/缓解",
    "治愈": "改善",
    "根治": "帮助改善",
    "瘦身": "塑形",
    "减肥": "身材管理",
    "祛斑": "均匀肤色",
    "美白": "提亮",
    "祛痘": "控油净痘",
    "抗衰老": "淡纹紧致",
    "加微信": "私信/主页",
    "点击链接": "详见主页",
}




# ── 动态词库加载（由 compliance_updater.py 维护） ──
import os as _os
_DYNAMIC_WORDS_FILE = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "references", "compliance_cache.json")

def _load_dynamic_words():
    """从缓存文件加载动态违规词"""
    try:
        if _os.path.exists(_DYNAMIC_WORDS_FILE):
            with open(_DYNAMIC_WORDS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                extra = data.get("extra_words", {})
                if extra:
                    print(f"[动态词库] 已加载 {sum(len(v) for v in extra.values())} 个动态词汇")
                    return extra
    except Exception:
        pass
    return {}

# __DYNAMIC_WORDS_LOADED__

def check_content(content: str) -> List[Dict]:
    """
    检测内容中的违规词

    Args:
        content: 待检测的内容

    Returns:
        违规词列表，包含类型、词语、位置、建议
    """
    violations = []

        # 加载动态词库
    dynamic_words = _load_dynamic_words()
    all_sources = {**VIOLATION_WORDS, **dynamic_words}
    for category, info in all_sources.items():
        for word in info["words"]:
            # 查找所有出现位置
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            for match in pattern.finditer(content):
                violations.append({
                    "category": category,
                    "word": word,
                    "position": match.start(),
                    "severity": info["severity"],
                    "suggestion": info["suggestion"],
                    "replacement": REPLACEMENTS.get(word, "")
                })

    return violations


def format_report(content: str, violations: List[Dict]) -> str:
    """生成检测报告"""
    if not violations:
        return "✅ 检测通过！未发现违规词。"

    report = []
    report.append("=" * 50)
    report.append("⚠️  检测到 {} 个违规词".format(len(violations)))
    report.append("=" * 50)
    report.append("")

    # 按严重程度分组
    high_severity = [v for v in violations if v["severity"] == "高"]
    medium_severity = [v for v in violations if v["severity"] == "中"]

    if high_severity:
        report.append("🔴 高风险违规词 ({}个)".format(len(high_severity)))
        report.append("-" * 40)
        for v in high_severity:
            report.append(f"  [{v['category']}] \"{v['word']}\"")
            if v["replacement"]:
                report.append(f"    → 建议替换为: {v['replacement']}")
            else:
                report.append(f"    → {v['suggestion']}")
        report.append("")

    if medium_severity:
        report.append("🟡 中风险违规词 ({}个)".format(len(medium_severity)))
        report.append("-" * 40)
        for v in medium_severity:
            report.append(f"  [{v['category']}] \"{v['word']}\"")
            if v["replacement"]:
                report.append(f"    → 建议替换为: {v['replacement']}")
        report.append("")

    # 标记原文
    report.append("📝 标记原文:")
    report.append("-" * 40)
    marked_content = content
    for v in sorted(violations, key=lambda x: x["position"], reverse=True):
        marked_content = (
            marked_content[:v["position"]] +
            f"【{v['word']}】" +
            marked_content[v["position"] + len(v["word"]):]
        )
    report.append(marked_content)
    report.append("")

    report.append("=" * 50)

    return "\n".join(report)


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python check_compliance.py \"你的笔记内容\"")
        print("   或: python check_compliance.py -f 文件路径")
        sys.exit(1)

    # 获取内容
    if sys.argv[1] == "-f" and len(sys.argv) >= 3:
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = sys.argv[1]

    # 检测
    violations = check_content(content)

    # 输出报告
    report = format_report(content, violations)
    print(report)

    # 返回状态码
    sys.exit(1 if violations else 0)


if __name__ == "__main__":
    main()
