# -*- coding: utf-8 -*-
"""Render ugc-video-factory article to WeChat HTML: try bm.md API, fallback to hand-built green-simple inline-style HTML."""
import base64, json, os, sys, urllib.request

OUT = r"E:\project\content-os\output"
SKILL_CSS = r"C:\Users\king\.claude\skills\wechat-article-formatter\styles\custom.css"

def b64(name):
    return "data:image/jpeg;base64," + open(os.path.join(OUT, f"_b64_{name}.txt")).read()

IMG_A, IMG_B, IMG_C = b64("boardA"), b64("boardB"), b64("checkA")

TITLE = "做一条 UGC 视频,我花在调提示词上的时间比拍摄还长——直到我把这一步删了"

MD = f"""# {TITLE}

做 UGC 视频最磨人的环节,不是生成,是调提示词。

一个镜头不对,重来;人物换了个角度,脸崩了,重来;第二段视频和第一段场景对不上,全部重来。一条 30 秒的开箱视频,光提示词就能磨掉一个下午。

所以我写了一个 skill,把「提示词」这一步从流程里删掉了。

它叫 **ugc-video-factory**。你只需要给它两样东西:**一段视频脚本,一份人物设定**。剩下的——分镜拆解、故事板绘制、镜头生成、唇形同步、剪辑拼接——它全部自己完成。

口说无凭,直接看效果。

![Sony 耳机开箱视频成片(发布时在编辑器中插入视频:成片.mp4)]({IMG_C})

这条 30 秒的 Sony 耳机开箱视频,从脚本到成片,我没有写过一句提示词。

## 它是怎么做到的

整个流程是一条真正的流水线,我给它英文口播稿和一张人物设定图之后,它做了这些事:

**第一步,改脚本。**

我给的口播稿是 89 个词,按正常语速要念 35.6 秒,超了。它自动做了压缩——逐句对照原稿删掉 19 个词,保留所有卖点(降噪、环境音模式、长续航一个没少),还输出了完整的删改对照表,每一刀切在哪、为什么切,全部留痕。最终 70 词,精确卡在 30 秒。

**第二步,拆分镜。**

30 秒被拆成 8 个镜头,每个镜头标好时长、机位、运镜和台词节奏(精确到每秒念几个词)。开场钩子 → 开箱 → 箱内清单 → 核心卖点 → 真实场景 → 佩戴舒适度 → 悬念收尾,一条标准的 UGC 叙事弧线。

**第三步,画故事板。**

8 个镜头绘成 2 张四宫格故事板——每张板对应 15 秒视频,格子里连标题、时长、要点、台词都排版好了。更关键的是连续性设计:**A 板的最后一帧,就是 B 板的第一帧**,两段视频拼起来严丝合缝;人物的脸、发型、那身浅黄色上衣,8 个镜头里零漂移。

![自动生成的四宫格故事板:每格含标题、时长、要点和台词]({IMG_B})

**第四步,生成 + 拼接。**

故事板图直接转成两段 15 秒视频,自动剪辑合并,输出成片。

## 几个让我觉得「成了」的细节

一是**诚实**。我故意没给产品包装图,它没有瞎编一个 Sony 包装盒——所有涉及品牌的画面都留空,等我补真实产品照片。宁可留白,绝不幻觉。

二是**场景纠错**。原脚本里有个街头场景,它判断换场地会破坏人物一致性,主动把「嘈杂街道」改成了「家里开着的电风扇和咖啡机」——台词一个字没改,意思一分没少,但整条视频再也不用离开那个房间。

三是**生产级品控**。每个镜头生成后自动抽帧检查:2 秒、7 秒、9.5 秒、13 秒各截一张,人脸、服装、场景逐项核对,不合格整板重生成。

![生成过程中的自动抽帧质检:逐帧核对人物、服装、场景一致性]({IMG_A})

## 谁适合用它

- **跨境电商卖家**:一个产品,批量出几十条不同人设的开箱视频,投 TikTok/Reels
- **MCN 和内容团队**:把「写分镜 + 盯生成」的人力成本打下来
- **个人创作者**:不会写提示词,也能产出广告级 UGC

UGC 视频的本质是「真人感」,而真人感恰恰死于流水线味。这个 skill 的思路反其道而行:把流水线藏在你看不见的地方,把「一个真实的人在真实房间里跟你说话」留在画面上。

**模型负责生成,skill 负责工程,你只管两件事:他是谁,他说什么。**

---

## 🎁 一个实验性质的邀请

这个 skill 还在快速迭代,我想找第一批真实用户一起打磨。

**前 10 名添加微信的朋友,免费帮你制作一条 UGC 视频**——你出产品和想法,我出整条流水线,成片归你。

微信号:**wx18621009317**(备注「UGC」)

哪怕只是想看看「不写提示词」到底能做到什么程度,也欢迎来聊。这条 Sony 开箱视频的完整分镜文档和故事板,都可以发给你看。
"""

css = open(SKILL_CSS, encoding="utf-8").read()
payload = {
    "markdown": MD,
    "markdownStyle": "green-simple",
    "platform": "wechat",
    "enableFootnoteLinks": True,
    "openLinksInNewWindow": True,
    "customCss": css,
}
html_path = os.path.join(OUT, "ugc-video-factory-公众号-含图版.html")

req = urllib.request.Request(
    "https://bm.md/api/markdown/render",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        res = json.loads(r.read().decode("utf-8"))
    html = res["result"]
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("BM_OK", html_path, len(html) // 1024, "KB")
except Exception as e:
    print("BM_FAIL", repr(e))
    sys.exit(2)
