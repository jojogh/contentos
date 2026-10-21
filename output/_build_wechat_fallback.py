# -*- coding: utf-8 -*-
"""Hand-built WeChat HTML (green-simple style, inline styles, base64 images). Fallback for bm.md."""
import os

OUT = r"E:\project\content-os\output"

def b64(name):
    return "data:image/jpeg;base64," + open(os.path.join(OUT, f"_b64_{name}.txt")).read()

GREEN = "rgb(53,179,120)"
P = 'style="color:rgb(89,89,89);font-size:15px;line-height:1.8em;letter-spacing:0.04em;text-align:left;margin:0;padding:8px 0;"'
STRONG = f'style="color:{GREEN};font-weight:bold;"'

def p(inner, extra=""):
    style = P[:-1] + extra + '"' if extra else P
    return f"<p {style}>{inner}</p>"

def strong(t):
    return f"<strong {STRONG}>{t}</strong>"

def h2(t):
    return (f'<h2 style="margin:30px 0 15px;display:flex;text-align:left;">'
            f'<span style="font-size:18px;color:rgb(255,255,255);background-color:rgb(0,0,0);'
            f'line-height:1.5em;padding:2px 10px;font-weight:bold;display:block;">{t}</span></h2>')

def figure(img, caption):
    return (f'<figure style="margin:10px 0;padding:0;display:flex;flex-direction:column;justify-content:center;align-items:center;">'
            f'<img src="{img}" style="display:block;margin:0 auto;max-width:100%;border-radius:6px;"/>'
            f'<figcaption style="color:rgb(140,140,140);font-size:13px;line-height:1.6em;letter-spacing:0.04em;margin-top:6px;text-align:center;">{caption}</figcaption>'
            f'</figure>')

def li(inner):
    return (f'<li style="margin:5px 0;"><span style="color:rgb(89,89,89);font-size:15px;line-height:1.8em;'
            f'letter-spacing:0.04em;">{inner}</span></li>')

HR = f'<hr style="margin:20px 0;border-style:solid none none;border-width:1px;border-color:{GREEN};height:1px;background:none;"/>'

IMG_A, IMG_B, IMG_C = b64("boardA"), b64("boardB"), b64("checkA")

parts = []
parts.append(f'<h1 style="margin:10px 0 20px;display:flex;"><span style="font-size:24px;color:{GREEN};line-height:1.5em;font-weight:bold;display:block;">做一条 UGC 视频,我花在调提示词上的时间比拍摄还长——直到我把这一步删了</span></h1>')

parts.append(p("做 UGC 视频最磨人的环节,不是生成,是调提示词。"))
parts.append(p("一个镜头不对,重来;人物换了个角度,脸崩了,重来;第二段视频和第一段场景对不上,全部重来。一条 30 秒的开箱视频,光提示词就能磨掉一个下午。"))
parts.append(p("所以我写了一个 skill,把「提示词」这一步从流程里删掉了。"))
parts.append(p(f'它叫 {strong("ugc-video-factory")}。你只需要给它两样东西:{strong("一段视频脚本,一份人物设定")}。剩下的——分镜拆解、故事板绘制、镜头生成、唇形同步、剪辑拼接——它全部自己完成。'))
parts.append(p("口说无凭,直接看效果。"))
parts.append(figure(IMG_C, "▲ 成片抽帧:开箱瞬间(30 秒完整视频在公众号编辑器中单独插入:成片.mp4)"))
parts.append(p("这条 30 秒的 Sony 耳机开箱视频,从脚本到成片,我没有写过一句提示词。"))

parts.append(h2("它是怎么做到的"))
parts.append(p("整个流程是一条真正的流水线,我给它英文口播稿和一张人物设定图之后,它做了这些事:"))
parts.append(p(strong("第一步,改脚本。")))
parts.append(p("我给的口播稿是 89 个词,按正常语速要念 35.6 秒,超了。它自动做了压缩——逐句对照原稿删掉 19 个词,保留所有卖点(降噪、环境音模式、长续航一个没少),还输出了完整的删改对照表,每一刀切在哪、为什么切,全部留痕。最终 70 词,精确卡在 30 秒。"))
parts.append(p(strong("第二步,拆分镜。")))
parts.append(p("30 秒被拆成 8 个镜头,每个镜头标好时长、机位、运镜和台词节奏(精确到每秒念几个词)。开场钩子 → 开箱 → 箱内清单 → 核心卖点 → 真实场景 → 佩戴舒适度 → 悬念收尾,一条标准的 UGC 叙事弧线。"))
parts.append(p(strong("第三步,画故事板。")))
parts.append(p(f'8 个镜头绘成 2 张四宫格故事板——每张板对应 15 秒视频,格子里连标题、时长、要点、台词都排版好了。更关键的是连续性设计:{strong("A 板的最后一帧,就是 B 板的第一帧")},两段视频拼起来严丝合缝;人物的脸、发型、那身浅黄色上衣,8 个镜头里零漂移。'))
parts.append(figure(IMG_B, "▲ 自动生成的四宫格故事板:每格含标题、时长、要点和台词"))
parts.append(p(strong("第四步,生成 + 拼接。")))
parts.append(p("故事板图直接转成两段 15 秒视频,自动剪辑合并,输出成片。"))

parts.append(h2("几个让我觉得「成了」的细节"))
parts.append(p(f'一是{strong("诚实")}。我故意没给产品包装图,它没有瞎编一个 Sony 包装盒——所有涉及品牌的画面都留空,等我补真实产品照片。宁可留白,绝不幻觉。'))
parts.append(p(f'二是{strong("场景纠错")}。原脚本里有个街头场景,它判断换场地会破坏人物一致性,主动把「嘈杂街道」改成了「家里开着的电风扇和咖啡机」——台词一个字没改,意思一分没少,但整条视频再也不用离开那个房间。'))
parts.append(p(f'三是{strong("生产级品控")}。每个镜头生成后自动抽帧检查:2 秒、7 秒、9.5 秒、13 秒各截一张,人脸、服装、场景逐项核对,不合格整板重生成。'))
parts.append(figure(IMG_A, "▲ 故事板 A 板:人物、服装、场景在 4 个镜头间保持一致"))

parts.append(h2("谁适合用它"))
parts.append('<ul style="list-style-type:disc;margin:8px 0;padding:0 0 0 25px;">'
             + li(f'{strong("跨境电商卖家")}:一个产品,批量出几十条不同人设的开箱视频,投 TikTok/Reels')
             + li(f'{strong("MCN 和内容团队")}:把「写分镜 + 盯生成」的人力成本打下来')
             + li(f'{strong("个人创作者")}:不会写提示词,也能产出广告级 UGC')
             + '</ul>')
parts.append(p("UGC 视频的本质是「真人感」,而真人感恰恰死于流水线味。这个 skill 的思路反其道而行:把流水线藏在你看不见的地方,把「一个真实的人在真实房间里跟你说话」留在画面上。"))
parts.append(p(strong("模型负责生成,skill 负责工程,你只管两件事:他是谁,他说什么。"), "text-align:center;font-size:16px;padding:16px 0;"))

parts.append(HR)
parts.append(h2("🎁 一个实验性质的邀请"))
parts.append(p("这个 skill 还在快速迭代,我想找第一批真实用户一起打磨。"))
parts.append(p(f'{strong("前 10 名添加微信的朋友,免费帮你制作一条 UGC 视频")}——你出产品和想法,我出整条流水线,成片归你。'))
parts.append(p(f'微信号:{strong("wx18621009317")}(备注「UGC」)', "text-align:center;font-size:17px;padding:14px 0;background-color:rgb(245,250,247);border-radius:8px;"))
parts.append(p("哪怕只是想看看「不写提示词」到底能做到什么程度,也欢迎来聊。这条 Sony 开箱视频的完整分镜文档和故事板,都可以发给你看。"))

html = ('<div id="bm-md" style="margin:0;padding:0 10px;width:auto;'
        'font-family:Optima,"Microsoft YaHei",PingFangSC-regular,serif;font-size:16px;'
        'color:rgb(0,0,0);line-height:1.5em;word-break:break-word;overflow-wrap:break-word;text-align:left;">'
        + "".join(parts) + "</div>")

path = os.path.join(OUT, "ugc-video-factory-公众号-含图版.html")
with open(path, "w", encoding="utf-8") as f:
    f.write(html)
print("OK", path, len(html.encode("utf-8")) // 1024, "KB")
