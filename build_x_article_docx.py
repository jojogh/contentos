# -*- coding: utf-8 -*-
"""Build a .docx of the translated X Article: Original Content Rewards Program."""

import os
import urllib.request

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(OUT_DIR, "docx_assets_x_article")
OUT_PATH = os.path.join(OUT_DIR, "原创内容奖励计划_中文翻译_2026-08-07.docx")

IMAGES = {
    "cover": "https://pbs.twimg.com/media/HO47dDuW0AAAfrJ.jpg",
    "copied": "https://pbs.twimg.com/media/HO54GR2XsAAUiXW.jpg",
    "reupload": "https://pbs.twimg.com/media/HO53-YNWMAAfmFI.jpg",
    "caption": "https://pbs.twimg.com/media/HO54LrYWQAAI2TP.jpg",
    "summary": "https://pbs.twimg.com/media/HO5xOQwX0AEmjIk.jpg",
    "attribution": "https://pbs.twimg.com/media/HO54o8HWwAAyaOe.jpg",
    "reaction": "https://pbs.twimg.com/media/HO543reXMAAh4J3.jpg",
}

CN_FONT = "Microsoft YaHei"


def download_images():
    os.makedirs(ASSET_DIR, exist_ok=True)
    paths = {}
    for key, url in IMAGES.items():
        path = os.path.join(ASSET_DIR, key + ".jpg")
        if os.path.exists(path) and os.path.getsize(path) > 1000:
            paths[key] = path
            continue
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            with open(path, "wb") as f:
                f.write(data)
            paths[key] = path
            print("downloaded", key, len(data))
        except Exception as exc:  # noqa: BLE001
            print("failed", key, exc)
    return paths


def set_font(run, size=None, bold=None, color=None):
    run.font.name = CN_FONT
    run._element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), CN_FONT)
    if size is not None:
        run.font.size = Pt(size)
    if bold is not None:
        run.font.bold = bold
    if color is not None:
        run.font.color.rgb = RGBColor(*color)


def add_para(doc, text="", size=10.5, bold=False, color=None, align=None,
             space_after=6, space_before=0, style=None):
    p = doc.add_paragraph(style=style)
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.line_spacing = 1.35
    if text:
        set_font(p.add_run(text), size=size, bold=bold, color=color)
    return p


def add_heading(doc, text, level):
    sizes = {1: 16, 2: 13, 3: 11.5}
    colors = {1: (0x11, 0x11, 0x11), 2: (0x1a, 0x1a, 0x1a), 3: (0x33, 0x33, 0x33)}
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14 if level <= 2 else 10)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    set_font(p.add_run(text), size=sizes[level], bold=True, color=colors[level])
    return p


def add_bullet(doc, text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.3
    set_font(p.add_run(text), size=10.5)
    return p


def add_number(doc, text):
    p = doc.add_paragraph(style="List Number")
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.3
    set_font(p.add_run(text), size=10.5)
    return p


def add_quote(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.3)
    p.paragraph_format.space_after = Pt(8)
    p.paragraph_format.line_spacing = 1.35
    run = p.add_run(text)
    set_font(run, size=10.5, color=(0x44, 0x44, 0x44))
    run.italic = True
    return p


def add_image(doc, paths, key, caption=None):
    path = paths.get(key)
    if path and os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Inches(5.4))
        if caption:
            add_para(doc, caption, size=9, color=(0x88, 0x88, 0x88),
                     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
    else:
        add_para(doc, "[示例图片：%s]" % IMAGES[key], size=9, color=(0x88, 0x88, 0x88),
                 align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)


def add_divider(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    pPr = p._p.get_or_add_pPr()
    from docx.oxml import OxmlElement
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "D0D0D0")
    pbdr.append(bottom)
    pPr.append(pbdr)


def build():
    paths = download_images()

    doc = Document()

    # Page setup: A4 with comfortable margins
    section = doc.sections[0]
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)

    normal = doc.styles["Normal"]
    normal.font.name = CN_FONT
    normal.font.size = Pt(10.5)
    normal.element.get_or_add_rPr().get_or_add_rFonts().set(qn("w:eastAsia"), CN_FONT)

    # ---------- Cover block ----------
    add_para(doc, "X 官方政策文件 · 中文翻译", size=9.5, color=(0x88, 0x88, 0x88),
             align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=6)
    add_para(doc, "原创内容奖励计划", size=26, bold=True, color=(0x0a, 0x0a, 0x0a),
             align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
    add_para(doc, "Original Content Rewards Program", size=13, color=(0x66, 0x66, 0x66),
             align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

    add_image(doc, paths, "cover")

    meta = [
        ("发布账号", "Creators（@XCreators）"),
        ("发布时间", "2026 年 8 月 7 日"),
        ("原文链接", "https://x.com/XCreators/status/2085835082166653393"),
        ("互动数据", "11,178,901 次浏览 · 11,686 点赞 · 2,064 转发 · 5,324 收藏"),
        ("原文篇幅", "约 1,810 词 / 12,456 字符"),
    ]
    table = doc.add_table(rows=0, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = "Table Grid"
    for label, value in meta:
        cells = table.add_row().cells
        cells[0].width = Inches(1.2)
        cells[1].width = Inches(5.0)
        p0 = cells[0].paragraphs[0]
        set_font(p0.add_run(label), size=9.5, bold=True, color=(0x55, 0x55, 0x55))
        p1 = cells[1].paragraphs[0]
        set_font(p1.add_run(value), size=9.5, color=(0x22, 0x22, 0x22))

    add_divider(doc)

    # ---------- Body ----------
    intro = [
        "今天，我们正式推出原创内容奖励计划（Original Content Rewards Program）——这是一套全新的机制，"
        "用于奖励那些为 X 带来原创想法、专业知识、新闻报道、创造力与评论的创作者。",
        "X 上最好的内容，从不只是转发已经存在的东西——它会带来新的东西。X 一直由这样一群人驱动："
        "他们分享只有自己能分享的内容——突发新闻、专业洞见、亲身经历，以及推动文化前行的评论。",
        "随着 X 不断演进，创作者的收益方式也在演进。原创内容奖励计划旨在奖励那些让 X 每天都值得打开的创作者。",
        "以下章节将说明该计划如何运作、谁有资格参与、创作者如何赚钱，以及什么才算原创内容。",
    ]
    for text in intro:
        add_para(doc, text)

    # Section: Revenue Sharing
    add_heading(doc, "一、这对收益分成（Revenue Sharing）意味着什么", 1)
    add_para(doc, "从今天起，我们不再接受新的收益分成计划的报名。")
    add_para(doc,
             "如果你目前已加入收益分成计划，你将持续获得收益直至 2026 年 9 月 7 日。你将收到三笔最终付款："
             "两笔分别于 8 月 14 日和 8 月 28 日按标准付款周期发放，最后一笔针对截至 9 月 7 日累计的收益，"
             "预计在 9 月 11 日前后发放。")
    add_para(doc,
             "从 2026 年 9 月 8 日起，我们将开始逐步向现有收益分成成员开放新原创内容奖励计划的申请。"
             "加入需要满足该计划的资格要求。你可以随时前往创作者工作室（Creator Studio）→ 原创内容奖励，"
             "查看自己的资格状态。")
    add_para(doc,
             "如果你已完成身份验证，并已绑定有效的收款方式，则无需重复这些步骤。一旦获批，"
             "你将在原创内容奖励计划及其条款与条件之下继续获得收益。")
    add_para(doc,
             "如果你的账号因此前的政策违规而正处于变现暂停状态，则不具备加入原创内容奖励计划的资格。")

    # Section: The Program
    add_heading(doc, "二、计划介绍", 1)
    add_para(doc, "创作原创内容需要时间、精力、专业能力和创造力。")
    add_para(doc, "原创内容奖励计划旨在奖励把这一切带给 X 的创作者。")
    add_para(doc,
             "我们希望认可那些发布突发新闻、分享专业知识、讲述故事、创造娱乐内容，"
             "并为对话贡献有意义视角的创作者。")
    add_para(doc, "我们的目标很简单：奖励为 X 带来新东西的创作者。", bold=True)
    add_para(doc, "不确定什么算原创内容？可跳至后文《原创内容入门》。")

    add_heading(doc, "我如何赚钱？", 2)
    add_para(doc, "符合条件的创作者，依据其原创内容产生的有效曝光量（qualified impressions）获得收益。")
    add_para(doc,
             "只要你的账号和内容持续符合计划要求，付款每两周发放一次。该新计划的首笔付款将于 2026 年 8 月 28 日发放。"
             "现有收益分成创作者如在 9 月 8 日或之后符合资格并加入原创内容奖励计划，"
             "其首笔付款将于 2026 年 9 月 25 日发放。")

    add_heading(doc, "什么是有效曝光？", 2)
    add_para(doc,
             "有效曝光是指来自 Premium 用户（X Premium Basic、Premium、Premium+ 或 Premium Business 的订阅者）"
             "在首页时间线（Home Timeline）上的去重曝光，且帖子至少有 50% 可见。")
    add_para(doc, "以下情况不计入有效曝光：")
    for item in [
        "同一账号对同一帖子的重复曝光",
        "付费、推广或人为制造的曝光",
        "欺诈性曝光",
    ]:
        add_bullet(doc, item)

    # Section: Eligibility
    add_heading(doc, "三、资格要求", 1)
    add_para(doc, "要申请原创内容奖励计划，你必须：")
    for item in [
        "年满 18 周岁",
        "居住在原创内容奖励计划开放的国家/地区",
        "账号状态良好，无反复违反《变现标准》或《服务条款》的记录",
        "拥有个人账号或企业账号",
        "订阅 X Premium、Premium+ 或 Premium Business",
        "至少拥有 500 名认证粉丝",
        "过去 90 天内至少有 500,000 次来自认证用户的首页时间线曝光（回复产生的曝光不计入）",
        "定期发布原创内容",
    ]:
        add_bullet(doc, item)
    add_para(doc, "满足上述要求后，你可以通过创作者工作室 → 原创内容奖励提交申请。")
    add_para(doc, "我们会审核你的申请，并在 3 个工作日内告知结果。")
    add_para(doc,
             "如果申请未获批准，你可以提交一次申诉。若申诉未成功，在仍满足全部资格要求的前提下，"
             "你可在 90 天后重新申请。")

    # Section: Continuous eligibility
    add_heading(doc, "四、持续资格", 1)
    add_para(doc, "加入计划后，你必须持续满足以下要求，才能保留资格并获得付款，包括但不限于：")
    for item in [
        "保持订阅 X Premium、Premium+ 或 Premium Business",
        "发布上文定义的原创且真实的内容",
        "避免恶意或欺诈行为",
        "不得篡改计划、付款系统或推荐算法",
        "不得使用自动化工具、机器人或任何工具/软件人为制造点赞、关注、浏览量、评论或分享",
        "不得就该计划作出虚假陈述、制作滥用性内容或从事违法行为",
        "不得索取互动：反复要求用户与帖子互动，例如要求点赞、回复、收藏、关注或转发",
    ]:
        add_bullet(doc, item)
    add_para(doc,
             "如果你的账号被发现违反上述任何一条，你将收到通知。视违规严重程度，"
             "你的账号可能被临时或永久移出原创内容奖励计划。你可以对此决定提出申诉。")
    add_para(doc,
             "上述要求并非穷尽式列举。对于损害本计划完整性、安全性或预期目的的行为，"
             "即使未明确列于上述条款，X 保留判定资格并采取执法行动的权利。")

    # Section: Account and content requirements
    add_heading(doc, "五、账号与内容要求", 1)
    add_para(doc, "要获得原创内容奖励计划下的付款，你的内容还必须符合以下标准，包括但不限于：")
    for item in [
        "属于本文定义的原创内容",
        "在首页时间线获得来自 Premium 账号的曝光",
        "遵守我们的《变现标准》《社区准则》《服务条款》和《版权政策》",
    ]:
        add_bullet(doc, item)
    add_para(doc, "以下内容不符合资格：")
    for item in [
        "抄袭或实质性复制其他创作者的内容",
        "从 X 或其他平台下载后重新上传至 X（除非你本人就是该内容的作者）",
        "通过自动化手段创建或发布的内容",
        "不当、色情露骨或可能对观看者有害的内容",
        "仅聚焦于变现技巧指导、变现讨论或最大化收益的内容",
        "包含虚假信息或误导性内容",
        "附有社区笔记（Community Note）的内容",
        "违反《社区准则》《服务条款》或《版权政策》的内容",
    ]:
        add_bullet(doc, item)
    add_para(doc, "我们会定期审查原创内容奖励计划中的账号，以确保持续合规。")

    # Section: Original content 101
    add_heading(doc, "六、原创内容入门（Original Content 101）", 1)
    add_para(doc,
             "原创内容奖励计划旨在奖励为 X 上的对话贡献原创价值的创作者。")
    add_para(doc,
             "原创内容是你亲自创作的内容，体现你自己的声音、视角、专业能力或创造力。")
    add_para(doc,
             "在 X 上，原创内容有多种形式。它可以是你写的推文串、你拍摄的视频、你创作的梗图、"
             "你首发的新闻故事、你发布的分析，或是为对话增添独特视角的评论。")
    add_para(doc, "原创内容的例子包括：")
    for item in [
        "原创文字、推文串、Article 长文、报道或分析",
        "你拍摄的照片或视频",
        "你设计的梗图、图形、插画及其他创意作品",
        "为已有对话增添有意义视角的评论、反应或洞见",
        "通过原创的背景补充、分析、解说、幽默或创意剪辑，对已有内容进行实质性且有意义的改造",
    ]:
        add_bullet(doc, item)

    add_heading(doc, "评论同样算数", 2)
    add_para(doc,
             "评论是 X 的核心。对世界上正在发生的事做出反应、进行分析、解释并在此基础上延展，"
             "正是这个平台独一无二的原因之一。")
    add_para(doc,
             "评论、分析、反应、梗图和创意解读，只要增添了有意义的东西——视角、专业知识、幽默或背景——"
             "都可以算作原创内容。许多创作者从已有的帖子、视频、图片、截图或文化热点出发，这没有问题。"
             "关键在于他们在其上增加了什么价值。")
    add_para(doc,
             "如果你的内容经常包含他人创作的材料，你需要贡献有意义的原创价值，"
             "才能符合我们的原创内容准则。")

    add_heading(doc, "如何创作合格的原创新内容", 2)
    add_heading(doc, "创作体现你自身视角的内容", 3)
    add_para(doc,
             "要符合原创内容奖励计划资格，最有力的方式就是定期创作体现你自己想法、专业能力、报道、"
             "分析、创造力或经历的内容。")
    add_para(doc,
             "无论你发布的是视频、梗图、推文串、评论、Article 长文还是突发新闻，"
             "你的贡献都应当构成价值的主要来源。")

    add_heading(doc, "使用已有内容时添加有意义的价值", 3)
    add_para(doc,
             "在已有对话基础上延展是 X 的核心组成部分，但仅仅转发别人的内容是不够的。")
    add_para(doc,
             "如果你使用帖子、视频、图片或其他第三方内容，请添加有意义的评论、背景、分析、幽默、"
             "报道或创意改造，使内容真正成为“你的”内容。")
    add_para(doc,
             "裁剪、滤镜、边框、水印、变速或简单叠加文字等轻微编辑，通常本身不构成有意义的改造。")

    add_heading(doc, "当你的目的只是放大传播时，请使用转发（Repost）", 3)
    add_para(doc,
             "如果你的目的只是把另一位创作者的内容分享给你的受众，请使用转发功能。")
    add_para(doc,
             "转发有助于把优秀内容呈现给你的粉丝，同时确保原作者获得应有的署名、触达和互动。")

    add_heading(doc, "问问自己：我增加了什么？", 3)
    add_para(doc, "发布前请考虑：")
    add_quote(doc, "如果没有我的贡献，这个内容是否仍然有价值？")
    add_para(doc,
             "如果答案是“是”，请考虑在发布前加入更多你本人的视角、专业能力、创造力或评论。")

    add_heading(doc, "理解“原创性”", 2)
    add_para(doc, "一个简单的原则是：一条帖子的价值应主要来自你所增加的部分。", bold=True)
    add_para(doc,
             "如果主要价值来自他人的内容，而你所添加的有意义价值很少甚至没有，"
             "那么该内容可能不符合原创内容奖励计划下的原创标准。")

    add_heading(doc, "非原创内容的示例", 2)

    add_para(doc, "1. 从另一账号逐字抄袭的内容。即包含其他创作者作品、而你并未参与创作的内容。", bold=True)
    add_image(doc, paths, "copied", "示例：直接抄袭其他账号的内容")

    add_para(doc, "2. 从其他账号下载后作为自己的内容重新上传至 X 的内容。", bold=True)
    add_image(doc, paths, "reupload", "示例：下载他人内容后重新上传")

    add_para(doc, "3. 未经有意义改造的转发内容。这包括他人创作的内容被转发、重新上传或重新发布，"
                  "而没有有意义的原创贡献。通常不被视为有意义改造的编辑包括：", bold=True)
    add_para(doc, "• 只添加描述“已经发生之事”的帖子配文或文字叠加")
    add_image(doc, paths, "caption", "示例：仅添加描述性配文")
    add_para(doc, "• 添加纯描述性、与内容无关和/或价值极低的摘要")
    add_image(doc, paths, "summary", "示例：添加低价值摘要")
    add_para(doc, "• 带署名（例如账号名或 logo）转发内容，但没有有意义的评论、分析、创造力或背景")
    add_image(doc, paths, "attribution", "示例：仅加署名、无实质评论")
    add_para(doc, "• 几乎不增加价值、评论有限或缺失的反应类帖子")
    add_image(doc, paths, "reaction", "示例：低价值反应帖")

    # Section: IP
    add_heading(doc, "七、原创内容与知识产权", 1)
    add_para(doc, "这些原创内容奖励准则是独立于 X 知识产权政策的。")
    add_para(doc,
             "内容可能在本计划下符合原创标准，却同时违反我们的知识产权规则。"
             "创作者有责任确保自己拥有使用他人内容所需的必要权利、许可或授权。")
    add_para(doc,
             "再次提醒：在 X 上发布侵犯他人知识产权的内容是不被允许的，"
             "无论该内容在本计划下是否会被认定为原创。")

    # Section: Start creating
    add_heading(doc, "八、开始创作", 1)
    add_para(doc, "X 是对话开始的地方。")
    add_para(doc,
             "原创内容奖励计划旨在奖励那些开启对话、塑造对话并推动对话前行的创作者。")
    add_para(doc,
             "我们很高兴继续投资于那些为 X 带来原创想法、专业能力、创造力和独特视角的创作者。")
    add_para(doc,
             "如需了解原创内容奖励计划的更多信息，请访问我们的帮助中心。"
             "前往创作者工作室 → 原创内容奖励即可查看你的资格状态。")

    # Summary table
    add_heading(doc, "附：要点摘要", 1)
    rows = [
        ("旧收益分成（Revenue Sharing）", "停止接受新报名；现有成员收益持续到 2026-09-07，共三笔最终付款"),
        ("新计划开放申请", "2026-09-08 起逐步向现有成员开放"),
        ("计费口径", "Premium 用户 · 首页时间线 · 去重 · 帖子 50% 可见"),
        ("付款频率", "每两周一次；新计划首笔 2026-08-28"),
        ("核心门槛", "18+、Premium 订阅、500 认证粉丝、90 天内 50 万认证用户首页曝光"),
        ("最核心原则", "帖子的价值必须主要来自你自己的贡献"),
    ]
    summary = doc.add_table(rows=1, cols=2)
    summary.style = "Table Grid"
    summary.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = summary.rows[0].cells
    for idx, text in enumerate(["项目", "内容"]):
        p = hdr[idx].paragraphs[0]
        set_font(p.add_run(text), size=9.5, bold=True, color=(0x22, 0x22, 0x22))
    for label, value in rows:
        cells = summary.add_row().cells
        set_font(cells[0].paragraphs[0].add_run(label), size=9.5, bold=True, color=(0x33, 0x33, 0x33))
        set_font(cells[1].paragraphs[0].add_run(value), size=9.5, color=(0x22, 0x22, 0x22))

    add_divider(doc)
    add_para(doc, "本文为 X 官方文章《Original Content Rewards Program》的中文翻译，"
                  "仅供阅读参考；一切以 X 官方原文及正式条款为准。",
             size=8.5, color=(0x99, 0x99, 0x99), space_before=6)

    doc.save(OUT_PATH)
    print("saved:", OUT_PATH)
    print("size:", os.path.getsize(OUT_PATH))


if __name__ == "__main__":
    build()
