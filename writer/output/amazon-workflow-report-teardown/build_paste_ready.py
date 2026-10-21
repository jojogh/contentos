# -*- coding: utf-8 -*-
"""Build the WeChat paste-ready HTML: base64-embed every content image.

Charts are flat-colour graphics with sharp text, so they stay PNG; the generated
illustration is photographic, so it goes JPEG. Both are downscaled to 1200px wide,
which is the range this project has used for WeChat (1080-1280).
"""
import base64
import io
import os
import re

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "article-wechat.html")
OUT = os.path.join(HERE, "article-paste-ready.html")
TARGET_W = 1200

ALT = {
    "section-00-16x9.png": "这套工作流由三块组成：MCP 数据通道、Codex 执行者、选品 skill 规范载体",
    "section-01-16x9.png": "797 条评论收敛为 11 条分级需求",
    "section-02-16x9.png": "全表口径与同店口径的同比差异",
    "section-03-16x9.png": "各价格段的款数与单款效率",
    "section-05-16x9.png": "自动化边界：四块分析有配对表，利润核算没有",
}

# matplotlib charts: flat colours + sharp text -> PNG. Generated illustration -> JPEG.
CHART_PNG = {"section-00-16x9.png", "section-01-16x9.png", "section-02-16x9.png",
             "section-03-16x9.png"}


def encode(path, name):
    im = Image.open(path)
    if im.width > TARGET_W:
        im = im.resize((TARGET_W, round(im.height * TARGET_W / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if name in CHART_PNG:
        im.convert("RGB").save(buf, format="PNG", optimize=True)
        mime = "image/png"
    else:
        im.convert("RGB").save(buf, format="JPEG", quality=88, optimize=True, progressive=True)
        mime = "image/jpeg"
    raw = buf.getvalue()
    return mime, raw


def main():
    html = open(SRC, encoding="utf-8").read()
    manifest = []

    def repl(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            return tag
        name = os.path.basename(src.group(1))
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            return tag
        mime, raw = encode(path, name)
        b64 = base64.b64encode(raw).decode("ascii")
        manifest.append((name, mime, len(raw)))
        new_tag = re.sub(r'src="[^"]*"', 'src="data:%s;base64,%s"' % (mime, b64), tag, count=1)
        alt = ALT.get(name)
        if alt:
            if 'alt="' in new_tag:
                new_tag = re.sub(r'alt="[^"]*"', 'alt="%s"' % alt, new_tag, count=1)
            else:
                new_tag = new_tag.replace("<img ", '<img alt="%s" ' % alt, 1)
        return new_tag

    html = re.sub(r"<img\b[^>]*>", repl, html)
    open(OUT, "w", encoding="utf-8").write(html)

    total = os.path.getsize(OUT)
    print("wrote %s (%.2f MB)" % (OUT, total / 1024 / 1024))
    for name, mime, size in manifest:
        print("  %-22s %-10s %6.0f KB" % (name, mime, size / 1024))
    print("images embedded: %d" % len(manifest))


if __name__ == "__main__":
    main()