#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书封面生成器 v1.1
用法:
  python generate_cover.py --title "标题文字" [--subtitle "副标题"]
    [--style emoji|text|contrast] [--palette morandi|macaron|premium|warm]
    [--output cover.png]
"""

import argparse
import os
import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap

# ── 配色方案 ──────────────────────────────────────
PALETTES = {
    "morandi": {
        "bg1": "#E8DED1", "bg2": "#C4B7A6",
        "accent": "#A8B5A0", "text": "#2C2C2C",
        "bar": "#D4A5A5"
    },
    "macaron": {
        "bg1": "#FFB6C1", "bg2": "#FFDAC1",
        "accent": "#87CEEB", "text": "#333333",
        "bar": "#FFFACD"
    },
    "premium": {
        "bg1": "#1A1A2E", "bg2": "#16213E",
        "accent": "#E94560", "text": "#FFFFFF",
        "bar": "#0F3460"
    },
    "warm": {
        "bg1": "#FFF0F5", "bg2": "#FFE4E1",
        "accent": "#FF6E86", "text": "#2C2C2C",
        "bar": "#FF9A56"
    },
    "fresh": {
        "bg1": "#E8F5E9", "bg2": "#C8E6C9",
        "accent": "#66BB6A", "text": "#1B5E20",
        "bar": "#A5D6A7"
    },
}

# ── 工具函数 ──────────────────────────────────────

def hex_to_rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def load_font(size):
    """加载中文字体，Windows 优先"""
    candidates = [
        "C:/Windows/Fonts/msyh.ttc",   # 微软雅黑
        "C:/Windows/Fonts/msyhbd.ttc",  # 微软雅黑粗体
        "C:/Windows/Fonts/simhei.ttf",  # 黑体
    ]
    for fp in candidates:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except Exception:
                continue
    return ImageFont.load_default()


def create_gradient(width, height, c1, c2, direction="vertical"):
    img = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(img)
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    steps = height if direction == "vertical" else width
    for i in range(steps):
        t = i / max(steps - 1, 1)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        if direction == "vertical":
            draw.line([(0, i), (width, i)], fill=(r, g, b))
        else:
            draw.line([(i, 0), (i, height)], fill=(r, g, b))
    return img


def draw_rounded_rect(draw, bbox, radius, fill):
    """画圆角矩形"""
    x1, y1, x2, y2 = bbox
    draw.rounded_rectangle(bbox, radius=radius, fill=fill)


def text_center(draw, text, y, width, font, color):
    """居中绘制文字，返回占用高度"""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = (width - tw) // 2
    draw.text((x, y), text, font=font, fill=color)
    return bbox[3] - bbox[1]


# ── 风格渲染器 ────────────────────────────────────

def render_emoji_style(title, subtitle, colors, width, height):
    """emoji冲击型：渐变背景 + 大字居中 + emoji装饰"""
    img = create_gradient(width, height, colors["bg1"], colors["bg2"])
    draw = ImageDraw.Draw(img)

    # emoji 装饰区（顶部）
    emojis = ["🔥", "✨", "💡", "🎯", "⭐", "💰", "📌", "👑", "💫", "🦋"]
    font_emoji = load_font(60)
    emoji_text = "  ".join(emojis[:5])
    text_center(draw, emoji_text, 120, width, font_emoji, hex_to_rgb(colors["text"]))

    # 主标题
    font_title = load_font(88)
    lines = []
    for segment in title.split("\n"):
        wrapped = textwrap.fill(segment, width=8)
        lines.extend(wrapped.split("\n"))

    line_h = 115
    total_h = len(lines) * line_h
    start_y = (height - total_h) // 2

    for i, line in enumerate(lines):
        text_center(draw, line, start_y + i * line_h, width, font_title,
                    hex_to_rgb(colors["text"]))

    # 副标题
    if subtitle:
        font_sub = load_font(46)
        text_center(draw, subtitle, start_y + total_h + 50, width, font_sub,
                    hex_to_rgb(colors["accent"]))

    # 底部装饰条
    draw.rectangle([0, height - 100, width, height], fill=hex_to_rgb(colors["bar"]))
    font_small = load_font(32)
    text_center(draw, "小红书", height - 80, width, font_small, hex_to_rgb(colors["text"]))

    return img


def render_text_style(title, subtitle, colors, width, height):
    """简约文字型：纯色背景 + 大字 + 简洁线条"""
    img = Image.new("RGB", (width, height), hex_to_rgb(colors["bg1"]))
    draw = ImageDraw.Draw(img)

    # 顶部装饰线
    draw.rectangle([0, 0, width, 8], fill=hex_to_rgb(colors["accent"]))

    # 主标题
    font_title = load_font(85)
    lines = []
    for segment in title.split("\n"):
        wrapped = textwrap.fill(segment, width=8)
        lines.extend(wrapped.split("\n"))

    line_h = 110
    total_h = len(lines) * line_h
    start_y = (height - total_h) // 2 - 60

    for i, line in enumerate(lines):
        text_center(draw, line, start_y + i * line_h, width, font_title,
                    hex_to_rgb(colors["text"]))

    # 分割线
    sep_y = start_y + total_h + 40
    line_w = 200
    draw.rectangle([(width - line_w) // 2, sep_y, (width + line_w) // 2, sep_y + 3],
                   fill=hex_to_rgb(colors["accent"]))

    # 副标题
    if subtitle:
        font_sub = load_font(44)
        text_center(draw, subtitle, sep_y + 30, width, font_sub,
                    hex_to_rgb(colors["accent"]))

    # 底部
    draw.rectangle([0, height - 60, width, height], fill=hex_to_rgb(colors["bar"]))

    return img


def render_contrast_style(title, subtitle, colors, width, height):
    """对比反差型：上下分色 + 大字突出"""
    img = Image.new("RGB", (width, height), hex_to_rgb(colors["bg1"]))
    draw = ImageDraw.Draw(img)

    # 上半部分覆盖
    half = height // 2 - 80
    overlay = Image.new("RGBA", (width, half), (*hex_to_rgb(colors["bg2"]), 230))
    img.paste(overlay, (0, 0))
    draw = ImageDraw.Draw(img)

    # 主标题（跨两个色块）
    font_title = load_font(90)
    lines = []
    for segment in title.split("\n"):
        wrapped = textwrap.fill(segment, width=7)
        lines.extend(wrapped.split("\n"))

    line_h = 115
    total_h = len(lines) * line_h
    start_y = (height - total_h) // 2

    for i, line in enumerate(lines):
        # 文字背景高亮
        bbox = draw.textbbox((0, 0), line, font=font_title)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = (width - tw) // 2
        y = start_y + i * line_h
        # 背景标签
        pad = 20
        draw_rounded_rect(draw, (x - pad, y - pad//2, x + tw + pad, y + th + pad//2),
                         radius=15, fill=hex_to_rgb(colors["accent"]))
        draw.text((x, y), line, font=font_title, fill=hex_to_rgb(colors["text"]))

    # 副标题
    if subtitle:
        font_sub = load_font(42)
        text_center(draw, subtitle, start_y + total_h + 60, width, font_sub,
                    hex_to_rgb(colors["text"]))

    return img


# ── 主函数 ────────────────────────────────────────

RENDERERS = {
    "emoji": render_emoji_style,
    "text": render_text_style,
    "contrast": render_contrast_style,
}


def generate_cover(title, subtitle="", style="emoji", palette="macaron",
                   output_path="cover.png"):
    width, height = 1080, 1440
    colors = PALETTES.get(palette, PALETTES["macaron"])
    renderer = RENDERERS.get(style, RENDERERS["emoji"])

    img = renderer(title, subtitle, colors, width, height)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    img.save(output_path, "PNG", quality=95)
    msg = f"[OK] cover generated: {output_path}  ({width}x{height}, style={style}, palette={palette})"
    try:
        print(f"✅ 封面已生成: {output_path}  ({width}x{height}, style={style}, palette={palette})")
    except UnicodeEncodeError:
        print(msg)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="小红书封面生成器 v1.1")
    parser.add_argument("--title", "-t", required=True, help="封面主标题（<=8字效果最佳）")
    parser.add_argument("--subtitle", "-s", default="", help="副标题")
    parser.add_argument("--style", "-y", default="emoji",
                        choices=["emoji", "text", "contrast"], help="封面风格")
    parser.add_argument("--palette", "-p", default="macaron",
                        choices=list(PALETTES.keys()), help="配色方案")
    parser.add_argument("--output", "-o", default="cover.png", help="输出路径")
    args = parser.parse_args()

    generate_cover(
        title=args.title,
        subtitle=args.subtitle,
        style=args.style,
        palette=args.palette,
        output_path=args.output,
    )
