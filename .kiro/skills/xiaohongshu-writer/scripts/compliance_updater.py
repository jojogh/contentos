#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书违规词动态更新器 v1.1
自动从在线源拉取最新违规词，更新本地词库缓存。

用法:
  python compliance_updater.py           # 常规检查（7天过期才更新）
  python compliance_updater.py --force   # 强制更新
  python compliance_updater.py --status  # 查看当前状态
"""

import json
import os
import sys
import io
import time

# Windows GBK 兼容：强制 stdout 使用 utf-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
import urllib.request
import urllib.error
from datetime import datetime, timedelta

# ── 配置 ──────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
CACHE_FILE = os.path.join(SKILL_DIR, "references", "compliance_cache.json")
WORDS_FILE = os.path.join(SKILL_DIR, "references", "compliance.md")
MAX_CACHE_AGE_DAYS = 7   # 超过7天自动更新
MAX_STALE_DAYS = 30      # 超过30天完全重建

# ── 在线数据源（免费/无需API Key） ────────────────
# 注意：国内网络可能无法访问 GitHub，脚本已内置兜底词库
ONLINE_SOURCES = [
    {
        "name": "Gitee 敏感词库（国内镜像）",
        "url": "https://gitee.com/mirrors/ChineseBQB/raw/master/bqb/000OtherBQB/敏感词/01.txt",
        "note": "Gitee国内可访问",
    },
    {
        "name": "GitHub 敏感词库",
        "url": "https://raw.githubusercontent.com/houbb/sensitive-word/master/data/",
        "note": "开源敏感词合集（需代理）",
    },
]


def load_cache():
    """加载缓存元数据"""
    if not os.path.exists(CACHE_FILE):
        return None
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_cache(data):
    """保存缓存元数据"""
    os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def should_update():
    """判断是否需要更新"""
    cache = load_cache()
    if not cache:
        return True, "首次运行，需要初始化词库"
    last = cache.get("updated_at", 0)
    age = (time.time() - last) / 86400
    if age > MAX_STALE_DAYS:
        return True, f"词库已过期 {int(age)} 天（>{MAX_STALE_DAYS}天），完全重建"
    if age > MAX_CACHE_AGE_DAYS:
        return True, f"词库已 {int(age)} 天未更新（>{MAX_CACHE_AGE_DAYS}天阈值）"
    return False, f"词库尚新（{int(age)} 天前更新），无需刷新"


def fetch_from_source(source):
    """从单个在线源拉取词汇"""
    try:
        # URL 编码处理（支持中文路径）
        from urllib.parse import quote
        url = quote(source["url"], safe=':/')
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        )
        with urllib.request.urlopen(req, timeout=5) as resp:
            raw = resp.read().decode("utf-8", errors="ignore")
            # 按行分割，过滤空行和注释
            words = []
            for line in raw.strip().split("\n"):
                w = line.strip()
                if w and not w.startswith("#") and not w.startswith("//"):
                    words.append(w)
            return words
    except Exception as e:
        print(f"  ⚠️  {source['name']} 失败: {e}")
        return None


def fetch_all_sources():
    """依次尝试所有在线源，返回合并结果"""
    all_words = set()
    success_sources = []

    for source in ONLINE_SOURCES:
        print(f"  📡 正在拉取: {source['name']}...")
        words = fetch_from_source(source)
        if words:
            all_words.update(words)
            success_sources.append(source["name"])
            print(f"  ✅ 获取 {len(words)} 个词")
        else:
            print(f"  ❌ 失败，跳过")

    return list(all_words), success_sources


def load_builtin_words():
    """内置基础词库（保底用，永远可用）"""
    return {
        "绝对化用语": [
            "第一", "No.1", "NO.1", "最好", "最优", "唯一", "独家",
            "顶级", "极致", "绝对", "一定", "百分百", "100%",
            "永久", "终身", "首个", "首创", "全球第一", "全国第一",
            "最先进", "最安全", "最有效", "首选", "销量第一",
        ],
        "医疗功效": [
            "治疗", "治愈", "根治", "药效", "疗效", "处方", "药方",
            "消炎", "抗菌", "祛斑", "淡斑", "瘦身", "减肥",
            "丰胸", "隆胸", "抗衰老", "抗皱", "生发", "防脱",
            "祛痘", "消痘", "降血压", "降血糖", "治疗痘痘",
            "壮阳", "补肾", "治癌", "抗癌",
        ],
        "引导交易": [
            "加微信", "+V", "加v", "微信号", "点击链接", "扫码购买",
            "扫二维码", "二维码", "购买链接", "加QQ", "淘宝搜索",
            "私聊购买", "微信转账", "支付宝转账",
        ],
        "虚假宣传": [
            "效果立竿见影", "包治百病", "无效退款", "专家推荐",
            "获得认证", "明星同款", "必买", "一定要买", "三天见效",
            "永不复发", "零风险", "稳赚不赔",
        ],
        "敏感内容": [
            "傻逼", "操你", "妈的", "他妈", "卧槽", "我操",
            "草泥马", "去死", "自杀方法",
        ],
    }


def update_check_compliance_py():
    """
    同步更新 check_compliance.py 使其支持动态词库加载。
    在 VIOLATION_WORDS 之前注入动态加载逻辑。
    """
    cc_path = os.path.join(SCRIPT_DIR, "check_compliance.py")
    if not os.path.exists(cc_path):
        return

    with open(cc_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 检查是否已有动态加载标记
    if "# __DYNAMIC_WORDS_LOADED__" in content:
        return

    # 在 check_compliance.py 的 VIOLATION_WORDS 定义之后，插入动态加载块
    dynamic_block = '''

# ── 动态词库加载（由 compliance_updater.py 维护） ──
_DYNAMIC_WORDS_FILE = os.path.join(os.path.dirname(__file__), "..", "references", "compliance_cache.json")

def _load_dynamic_words():
    """从缓存文件加载动态违规词"""
    try:
        if os.path.exists(_DYNAMIC_WORDS_FILE):
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

'''

    # 在 VIOLATION_WORDS 定义之后插入
    if "VIOLATION_WORDS = {" in content:
        # 找到 VIOLATION_WORDS 定义的结束位置（下一个顶层定义或函数）
        # 简单策略：在第一个顶层函数 def 之前插入
        import re
        # 在第一个 "def " 之前（排除类内部）插入
        match = re.search(r'\n(def \w+)', content)
        if match:
            insert_pos = match.start() + 1
            content = content[:insert_pos] + dynamic_block + content[insert_pos:]
            # 同时更新 check_content 函数，加入动态词
            if "def check_content" in content:
                # 在 check_content 函数中，VIOLATION_WORDS 遍历后加入动态词
                old_pattern = 'for category, info in VIOLATION_WORDS.items():'
                new_pattern = '''    # 加载动态词库
    dynamic_words = _load_dynamic_words()
    all_sources = {**VIOLATION_WORDS, **dynamic_words}
    for category, info in all_sources.items():'''
                content = content.replace(old_pattern, new_pattern)

            with open(cc_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  ✅ 已同步更新 check_compliance.py（支持动态词库）")


def build_compliance_md(dynamic_words=None, source_notes=None):
    """重新生成 compliance.md"""
    builtin = load_builtin_words()
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    lines = [
        "# 小红书违规词库与替代方案",
        "",
        f"> ⚠️ 本文件由 compliance_updater.py 自动维护",
        f"> 📅 最后更新：{now}",
        f"> 🔄 更新周期：{MAX_CACHE_AGE_DAYS} 天",
        f"> 📡 数据源：{', '.join(source_notes) if source_notes else '内置基础词库'}",
        "",
    ]

    # 内置词库
    for category, words in builtin.items():
        lines.append(f"## {category}（高风险）")
        lines.append("")
        lines.append("| 违规词 | 替代词 |")
        lines.append("|-------|-------|")
        # 只展示前15个（避免文件过长）
        for w in words[:15]:
            lines.append(f"| {w} | （参见替代方案）|")
        if len(words) > 15:
            lines.append(f"| ... 共 {len(words)} 个 | |")
        lines.append("")

    # 动态词库
    if dynamic_words:
        lines.append("---")
        lines.append("")
        lines.append("## 🔄 动态更新词库")
        lines.append("")
        lines.append(f"> 以下词汇来自在线源，自动定期更新（{MAX_CACHE_AGE_DAYS}天周期）")
        lines.append("")
        total = 0
        for cat, words in dynamic_words.items():
            if isinstance(words, list) and words:
                lines.append(f"### {cat}")
                for w in words[:30]:
                    lines.append(f"- {w}")
                if len(words) > 30:
                    lines.append(f"- ... 共 {len(words)} 个")
                lines.append("")
                total += len(words)
        lines.append(f"*动态词库共 {total} 个词汇*")
    else:
        lines.append("---")
        lines.append("")
        lines.append("## 🔄 动态更新词库")
        lines.append("")
        lines.append("> 暂无动态词汇。运行 `python compliance_updater.py --force` 拉取。")
        lines.append("")

    # 替代词对照表（固定）
    lines.extend([
        "---",
        "",
        "## 替代词对照表",
        "",
        "| 违规词 | 替代方案 |",
        "|--------|---------|",
        "| 第一 | 之一、领先、推荐 |",
        "| 最好 | 推荐、出色、亲测好用 |",
        "| 唯一 | 特色、特别、专属 |",
        "| 顶级 | 高端、出色、优秀 |",
        "| 绝对 | 通常、大概率、往往 |",
        "| 百分百 | 大部分、多数、大多数 |",
        "| 治疗 | 改善、缓解、帮助 |",
        "| 治愈 | 改善、帮助恢复 |",
        "| 根治 | 帮助改善、长期维护 |",
        "| 瘦身 | 塑形、身材管理 |",
        "| 减肥 | 控制体重、身材管理 |",
        "| 祛斑 | 均匀肤色、提亮 |",
        "| 美白 | 提亮肤色、透亮 |",
        "| 祛痘 | 控油、净透、调理 |",
        "| 抗衰老 | 淡纹紧致、年轻态 |",
        "| 加微信 | 主页有惊喜、私信我 |",
        "| 点击链接 | 详见主页、看简介 |",
        "| 扫码购买 | 搜索品牌名 |",
        "| 立竿见影 | 逐步改善、坚持可见效 |",
        "| 包治百病 | 亲测有效、持续使用有帮助 |",
    ])

    return "\n".join(lines)


def print_status():
    """打印当前状态"""
    cache = load_cache()
    if not cache:
        print("📭 违规词库：未初始化")
        print(f"   内置基础词库：{sum(len(v) for v in load_builtin_words().values())} 个")
        print(f"   运行 python compliance_updater.py 初始化")
        return

    age_days = (time.time() - cache.get("updated_at", 0)) / 86400
    print(f"📋 违规词库状态：")
    print(f"   更新时间：{cache.get('updated_date', '未知')}")
    print(f"   已过 {int(age_days)} 天（阈值：{MAX_CACHE_AGE_DAYS} 天）")
    print(f"   数据源：{cache.get('source', '未知')}")
    print(f"   在线词数：{cache.get('online_count', 0)}")
    print(f"   内置词数：{sum(len(v) for v in load_builtin_words().values())}")

    need, reason = should_update()
    status = "🔴 需要更新" if need else "🟢 无需更新"
    print(f"   状态：{status} — {reason}")


def main(force=False):
    if "--status" in sys.argv:
        print_status()
        return

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 违规词库检查...")

    if not force:
        need, reason = should_update()
        if not need:
            print(f"✅ {reason}")
            return
        print(f"📝 {reason}，开始更新...")
    else:
        print(f"📝 强制更新模式...")

    # 1. 尝试在线拉取
    print("\n📡 拉取在线词库...")
    online_words, success_sources = fetch_all_sources()

    # 2. 构建动态词库
    extra_words = {}
    if online_words:
        # 简单分类：超过3个字的归为"长句"，其余归为"敏感词"
        short = [w for w in online_words if len(w) <= 3]
        long_w = [w for w in online_words if len(w) > 3]
        if short:
            extra_words["在线敏感词"] = sorted(set(short))[:500]
        if long_w:
            extra_words["在线敏感短语"] = sorted(set(long_w))[:500]

    source_notes = success_sources if success_sources else ["内置基础词库"]

    # 3. 生成 compliance.md
    print("\n📝 生成违规词库文件...")
    content = build_compliance_md(extra_words, source_notes)
    os.makedirs(os.path.dirname(WORDS_FILE), exist_ok=True)
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✅ {WORDS_FILE}")

    # 4. 保存缓存
    save_cache({
        "updated_at": time.time(),
        "updated_date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "source": ", ".join(source_notes),
        "online_count": len(online_words),
        "extra_words": extra_words,
    })
    print(f"  ✅ {CACHE_FILE}")

    # 5. 同步更新 check_compliance.py
    print("\n🔧 同步检测脚本...")
    update_check_compliance_py()

    # 6. 汇总
    builtin_count = sum(len(v) for v in load_builtin_words().values())
    online_count = len(online_words)
    total = builtin_count + online_count
    print(f"\n🎉 更新完成！")
    print(f"   内置词数：{builtin_count}")
    print(f"   在线词数：{online_count}")
    print(f"   总计：{total} 个词汇")
    print(f"   下次自动更新：{MAX_CACHE_AGE_DAYS} 天后")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="小红书违规词动态更新器 v1.1")
    parser.add_argument("--force", "-f", action="store_true", help="强制更新（忽略缓存时间）")
    parser.add_argument("--status", "-s", action="store_true", help="查看当前状态")
    args = parser.parse_args()

    if args.status:
        print_status()
    else:
        main(force=args.force)
