# -*- coding: utf-8 -*-
"""Draw the three data charts for the WeChat article.
All figures come from the 2026-09-27 tire-inflator US category report and were
verified by parsing the workbook directly. Do not add numbers not in the article.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Chinese font
FONT = r"C:\Windows\Fonts\msyh.ttc"
font_manager.fontManager.addfont(FONT)
plt.rcParams["font.family"] = font_manager.FontProperties(fname=FONT).get_name()
plt.rcParams["axes.unicode_minus"] = False

NAVY = "#0F4C81"
NAVY_L = "#4A7FA8"
GREY = "#B9C2CC"
GREY_D = "#6B7480"
RED = "#C0392B"
AMBER = "#D98C1F"
W, H = 16, 9
DPI = 120

def canvas():
    fig = plt.figure(figsize=(W, H), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16); ax.set_ylim(0, 9)
    ax.axis("off")
    return fig, ax

def title(ax, main, sub=None):
    ax.text(0.62, 8.32, main, fontsize=21, color=NAVY, fontweight="bold", va="center")
    if sub:
        ax.text(0.62, 7.72, sub, fontsize=11.5, color=GREY_D, va="center")

def source_note(ax, txt, y=0.34):
    ax.text(0.62, y, txt, fontsize=9.2, color=GREY_D, va="center")


def source_note_at(ax, y, txt):
    source_note(ax, txt, y)

# ---------------------------------------------------------------- chart 0
def chart0(path):
    """Three-part architecture: MCP (data) -> Codex (execution) -> report,
    with the skill feeding rules into Codex."""
    fig, ax = canvas()
    title(ax, "这套工作流由三块组成", "前两块决定质量，第三块决定成本")

    bw, bh, by = 4.20, 2.45, 4.45
    boxes = [
        (0.62, "MCP 服务", "数据通道", "亚马逊类目详细数据\n自动拉取，不靠人工搬运", NAVY_L),
        (5.90, "Codex", "执行者", "读数据、跑四块分析\n生成表格与结论", NAVY),
        (11.18, "交付物", "9 张工作表", "80 款竞品 · 24 个月\n797 条评论", "#2E6B4F"),
    ]
    for x, name, role, desc, c in boxes:
        ax.add_patch(FancyBboxPatch((x, by), bw, bh,
                                    boxstyle="round,pad=0.06,rounding_size=0.20",
                                    linewidth=1.8, edgecolor=c, facecolor="white", zorder=2))
        ax.text(x + bw / 2, by + bh - 0.46, name, fontsize=16, color=c,
                fontweight="bold", ha="center", va="center", zorder=3)
        ax.text(x + bw / 2, by + bh - 0.88, role, fontsize=10.5, color=GREY_D,
                ha="center", va="center", zorder=3)
        ax.text(x + bw / 2, by + 0.42, desc, fontsize=10, color=GREY_D,
                ha="center", va="center", linespacing=1.7, zorder=3)
    for x0 in (4.82, 10.10):
        ax.add_patch(FancyArrowPatch((x0 + 0.02, by + bh / 2), (x0 + 0.88, by + bh / 2),
                                     arrowstyle="-|>", mutation_scale=22,
                                     color=NAVY, linewidth=2.4, zorder=1))
        ax.text(x0 + 0.45, by + bh / 2 + 0.30, "数据", fontsize=9.5, color=GREY_D,
                ha="center", va="center")

    # skill box injecting rules upward into Codex
    sx, sw, sh, sy = 5.90, 4.20, 2.10, 1.80
    ax.add_patch(FancyBboxPatch((sx, sy), sw, sh,
                                boxstyle="round,pad=0.06,rounding_size=0.20",
                                linewidth=1.8, edgecolor=AMBER, facecolor="white", zorder=2))
    ax.text(sx + sw / 2, sy + sh - 0.42, "选品 skill", fontsize=15, color=AMBER,
            fontweight="bold", ha="center", va="center", zorder=3)
    ax.text(sx + sw / 2, sy + sh - 0.82, "规范载体 · 客户真正应该拥有的一块",
            fontsize=10, color=GREY_D, ha="center", va="center", zorder=3)
    ax.text(sx + sw / 2, sy + 0.34, "采哪些字段 · 必答哪些问题 · 输出顺序 · 哪一环不交给 AI",
            fontsize=10, color=GREY_D, ha="center", va="center", zorder=3)
    ax.add_patch(FancyArrowPatch((sx + sw / 2, sy + sh + 0.04), (sx + sw / 2, by - 0.06),
                                 arrowstyle="-|>", mutation_scale=22,
                                 color=AMBER, linewidth=2.4, zorder=1))
    ax.text(sx + sw / 2 + 0.22, (sy + sh + by) / 2, "规则", fontsize=9.5,
            color=GREY_D, ha="left", va="center")

    source_note_at(ax, 0.55, "本文拆解的交付物来自为客户开发并落地的 Codex 选品工作流（客户：汽车用品出海电商，主营汽车挡风玻璃防阳罩）")
    fig.savefig(path, facecolor="white")
    plt.close(fig)

# ---------------------------------------------------------------- chart 1
def chart1(path):
    fig, ax = canvas()
    title(ax, "797 条评论，收敛成 11 条产品需求")

    # stage boxes
    stages = [
        (0.62, "797", "条评论", "负面（1–2 星）99 条 · 12.4%", NAVY),
        (5.45, "14", "个主题", "每个主题带命中数与负面率", NAVY_L),
        (10.28, "11", "条产品需求", "P0 五条 · P1 两条 · P2 一条\n另三条正面主题标为「维持」", "#2E6B4F"),
    ]
    bw, bh, by = 4.30, 3.30, 3.35
    for x, big, unit, note, c in stages:
        ax.add_patch(FancyBboxPatch((x, by), bw, bh, boxstyle="round,pad=0.06,rounding_size=0.22",
                                    linewidth=1.6, edgecolor=c, facecolor="white", zorder=2))
        ax.text(x + bw / 2, by + bh - 0.92, big, fontsize=40, color=c,
                fontweight="bold", ha="center", va="center", zorder=3)
        ax.text(x + bw / 2, by + bh - 1.72, unit, fontsize=14, color=c,
                ha="center", va="center", zorder=3)
        ax.text(x + bw / 2, by + 0.62, note, fontsize=10.5, color=GREY_D,
                ha="center", va="center", linespacing=1.6, zorder=3)
    for x0 in (4.92, 9.75):
        ax.add_patch(FancyArrowPatch((x0 + 0.05, by + bh / 2), (x0 + 0.48, by + bh / 2),
                                     arrowstyle="-|>", mutation_scale=20,
                                     color=GREY, linewidth=2.2, zorder=1))

    # negative-rate ranking
    themes = [("售后/客服/换货", 64.3), ("耐用性/寿命", 28.9), ("精度/准确度", 16.1),
              ("过热/发热", 13.8), ("电池/续航", 12.6)]
    ax.text(0.62, 2.68, "负面率最高的五个主题", fontsize=12.5, color=NAVY,
            fontweight="bold", va="center")
    x_lab, x_bar, bar_max, bh2 = 3.75, 5.62, 8.0, 0.155
    for i, (name, rate) in enumerate(themes):
        y = 2.18 - i * 0.375
        w = bar_max * rate / 64.3
        ax.text(x_lab, y, name, fontsize=10.5, color=GREY_D, ha="right", va="center")
        ax.add_patch(FancyBboxPatch((x_bar, y - bh2), w, bh2 * 2,
                                    boxstyle="round,pad=0,rounding_size=0.06",
                                    linewidth=0, facecolor=NAVY if i == 0 else NAVY_L, zorder=2))
        ax.text(x_bar + w + 0.14, y, f"{rate}%", fontsize=10,
                color=NAVY if i == 0 else GREY_D, va="center")
    source_note_at(ax, 0.18, "数据来源：一次亚马逊美国站轮胎充气泵类目调研交付报告（运行日 2026-09-27）")
    fig.savefig(path, facecolor="white")
    plt.close(fig)

# ---------------------------------------------------------------- chart 2
def chart2(path):
    fig, ax = canvas()
    title(ax, "同一份数据，两个同比：+38.47% 和 +12.29%",
          "差别来自统计池子本身在变大")

    # two big numbers
    ax.add_patch(FancyBboxPatch((0.62, 3.55), 6.95, 3.05,
                                boxstyle="round,pad=0.06,rounding_size=0.22",
                                linewidth=1.6, edgecolor=RED, facecolor="white"))
    ax.text(1.05, 6.05, "全表口径", fontsize=12.5, color=GREY_D, va="center")
    ax.text(1.05, 5.05, "+38.47%", fontsize=38, color=RED, fontweight="bold", va="center")
    ax.text(1.05, 4.10, "全部有记录的商品一起加总", fontsize=10.5, color=GREY_D, va="center")

    ax.add_patch(FancyBboxPatch((8.43, 3.55), 6.95, 3.05,
                                boxstyle="round,pad=0.06,rounding_size=0.22",
                                linewidth=1.6, edgecolor=NAVY, facecolor="white"))
    ax.text(8.86, 6.05, "同店口径（47 个 ASIN）", fontsize=12.5, color=GREY_D, va="center")
    ax.text(8.86, 5.05, "+12.29%", fontsize=38, color=NAVY, fontweight="bold", va="center")
    ax.text(8.86, 4.10, "同店中位数仅 +3.45%（24 升 23 降）", fontsize=10.5, color=GREY_D, va="center")

    # pool growth
    ax.text(0.62, 2.72, "统计池子里的有效商品数", fontsize=12.5, color=NAVY,
            fontweight="bold", va="center")
    ax.plot([1.60, 14.40], [1.42, 1.42], color=GREY, linewidth=2.6,
            solid_capstyle="round", zorder=1, linestyle=(0, (4, 3)))
    for x, label, val, c in [(1.60, "2024-09", "35", NAVY_L), (14.40, "2026-08", "80", NAVY)]:
        ax.scatter([x], [1.42], s=190, color=c, zorder=3)
        ax.text(x, 1.92, val, fontsize=19, color=c, fontweight="bold",
                ha="center", va="center")
        ax.text(x, 1.02, label, fontsize=10.5, color=GREY_D, ha="center", va="center")
    ax.text(8.0, 2.08, "有效记录数　前 12 月 474 → 近 12 月 780", fontsize=10.5,
            color=GREY_D, ha="center", va="center")

    source_note(ax, "数据来源：同上。第三方工具竞品查询导出，属估算口径，非亚马逊后台订单数据")
    fig.savefig(path, facecolor="white")
    plt.close(fig)

# ---------------------------------------------------------------- chart 3
def chart3(path):
    fig, ax = canvas()
    title(ax, "价格盲区不在便宜的那一端",
          "款数多不等于单款卖得好")

    bands = [("30–40", 24, 29168, "红海", RED),
             ("40–50", 8, 7066, "低效夹心", RED),
             ("50–75", 15, 34006, "供给缺口", "#2E6B4F"),
             ("75–100", 7, 12272, "样本不足 N=7", AMBER),
             ("100–150", 4, 17767, "高端利基", GREY_D)]

    ax.text(0.62, 6.92, "左点＝款数　右侧条＝单款中位销量（台）", fontsize=11, color=GREY_D, va="center")

    x_n, x_v, x_tag = 3.05, 5.20, 15.52
    y0, dy = 6.05, 1.02
    v_max, bar_max = 36000.0, 5.60
    for i, (name, n, v, tag, c) in enumerate(bands):
        y = y0 - i * dy
        ax.text(1.72, y, name, fontsize=12.5, color=NAVY, fontweight="bold",
                ha="right", va="center")
        ax.text(1.72, y - 0.30, "美元", fontsize=9, color=GREY_D, ha="right", va="center")
        ax.scatter([x_n], [y], s=90 + n * 26, color=GREY, zorder=3)
        ax.text(x_n - 0.42, y, str(n), fontsize=12, color=GREY_D, ha="right", va="center")
        w = bar_max * v / v_max
        ax.add_patch(FancyBboxPatch((x_v, y - 0.20), w, 0.40,
                                    boxstyle="round,pad=0,rounding_size=0.08",
                                    linewidth=0, facecolor=c, alpha=0.88, zorder=2))
        ax.text(x_v + w + 0.16, y, f"{v:,}", fontsize=11.5, color=c,
                fontweight="bold", va="center")
        ax.text(x_tag, y, tag, fontsize=10.5, color=c, va="center", ha="right")

    source_note(ax, "数据来源：同上，近 12 个月（2025-09 至 2026-08）父 ASIN 口径")
    fig.savefig(path, facecolor="white")
    plt.close(fig)

if __name__ == "__main__":
    import os
    out = os.path.dirname(os.path.abspath(__file__))
    chart0(os.path.join(out, "section-00-16x9.png"))
    chart1(os.path.join(out, "section-01-16x9.png"))
    chart2(os.path.join(out, "section-02-16x9.png"))
    chart3(os.path.join(out, "section-03-16x9.png"))
    print("charts written")