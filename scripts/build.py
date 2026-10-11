"""Build the two static product-information pages. Python standard library only."""
from pathlib import Path
import json
import hashlib
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://zhangkaiming2579-dev.github.io/lenjo-app/"
REPO = "https://github.com/zhangkaiming2579-dev/lenjo-app"
STORE = "https://apps.apple.com/app/id6784486285"
CHECKED = "2026-10-11"
CSS_VERSION = hashlib.sha256((ROOT / "styles.css").read_bytes()).hexdigest()[:12]

COPY = {
    "en": {
        "lang": "en", "title": "Lenjo / 练境 — AI Fitness Coach for iPhone",
        "description": "Lenjo is a local-first AI fitness coach and workout tracker for iPhone, with optional Apple Watch support, meal logging and editable coaching memory.",
        "label": "Product information · iPhone + Apple Watch", "h1": "Lenjo / 练境<br><span>AI fitness coach.</span>",
        "intro": "Plan a session. Log what you actually do. Review the next step. Lenjo connects strength training, recovery context and nutrition records on iPhone, with optional Apple Watch support.",
        "cta": "Get Lenjo on the App Store ↗", "website": "Official website ↗", "web": "https://lenjoapp.com/en/",
        "nav": ["Features", "FAQ", "中文"], "other": "zh/", "caption": "Example workout plan · Review before training",
        "facts_title": "One app. A continuous training context.", "facts": [("Product", "Lenjo / 练境"), ("Devices", "iPhone · iOS 17+<br>Apple Watch · watchOS 10+"), ("Access", "Free iPhone workout logging<br>Optional Lenjo Pro"), ("Support", "Lenjo / 练境<br>lenjoapp.com")],
        "features_title": "From a suggested plan to completed sets.",
        "features": [
            ("AI workout planning", "Describe your goals, equipment, experience and available time. The coach can use saved workout history and permitted recovery context to suggest exercises, sets, reps, load and rest. Review the plan before starting."),
            ("Set-by-set workout tracking", "Start a planned session or a free workout. Record actual weights, reps, RPE and completed sets on iPhone, then save and review them before discussing the next session."),
            ("Apple Watch recovery guidance", "With Pro, send a plan to a paired Watch and log sets from your wrist. Available health data can support live heart-rate recovery guidance and a post-workout heart-rate-by-set timeline."),
            ("Meal photo and nutrition logging", "Enter food manually or analyze a meal photo. Review estimated items, calories, protein, carbohydrate and fat, edit what needs correcting, then confirm before saving."),
            ("Timed cardio sessions", "Record cardio by time, with speed, incline and distance notes where relevant. Pro users can record available heart-rate, calorie and distance data with Apple Watch."),
            ("Progress and coaching memory", "Review body-weight, activity, recovery and training trends. Inspect, edit or delete long-term coaching memories, including your goals, equipment and preferences.")],
        "flow_title": "Your first session, in four steps.",
        "flow": [("Explain", "Tell the coach your goals, equipment and available time."), ("Review", "Check the suggested exercises and targets. Edit before training."), ("Record", "Log actual sets and save the completed session."), ("Reflect", "Use saved results and recovery context to discuss what comes next.")],
        "screens_title": "See the workout workflow.", "screen_captions": ["iPhone · actual weight, reps and RPE", "Apple Watch · between-set recovery reference"],
        "screen_note": "These public product screenshots contain example training data. The interface may vary by version and language. Recovery guidance is a fitness reference, not a medical measurement.",
        "access_title": "Free logging. Optional Pro.", "access": "iPhone workout execution and logging are free, with an AI trial allowance. Pro adds Watch workout execution and recovery guidance, higher AI coach and photo-analysis allowances, and deeper reports. Monthly and yearly subscriptions are available; check the app for current prices and limits.",
        "data_title": "Local records. AI by consent.", "data": "Core records are primarily stored on your device. Apple sign-in and Apple Health permissions are optional. AI coaching and photo analysis require internet access and process relevant information through the Lenjo gateway and third-party model providers after explanation and consent. You can decline AI and keep using local logging.",
        "faq_title": "Questions about Lenjo.", "faq": [
            ("What is Lenjo?", "Lenjo (练境) is a local-first AI fitness coach and workout tracker for iPhone. It connects structured workout plans, actual training records, recovery context and nutrition logging."),
            ("Do I need an Apple Watch?", "No. iPhone can independently execute and log workouts. Watch training is optional and requires Pro, a paired Watch and the Lenjo Watch app. Heart-rate features require relevant permissions and usable data."),
            ("Can I use it without AI?", "Yes. If you decline AI processing, local workout execution and logging remain available. AI coaching and photo analysis require an internet connection and consent."),
            ("Can the plan be executed in the app?", "Yes. Review and edit the suggested plan, start the session and record the sets you actually complete. Save the results before discussing your next workout."),
            ("Can I record meals from photos?", "Yes. Meal photos can be analyzed for estimated food items and nutrition. Review, correct and confirm the result before saving; a photo cannot reliably determine every ingredient or portion."),
            ("How can I contact Lenjo?", "The official website is lenjoapp.com, and the App Store identifier is 6784486285. Support is available at KmTech2026@outlook.com.")],
        "support_title": "Contact Lenjo.", "support": "Questions or feedback? Contact the developer through the official support page or email. Use public GitHub Issues for general feature requests and bugs, without personal health data or private conversations.",
        "support_link": "Support", "privacy": "Privacy", "terms": "Terms", "docs": "Getting started", "rights": "Product information and example screens. The application source code is proprietary.",
        "checked": "Product information checked 11 October 2026 against the public App Store listing and official website.",
        "boundary": "Lenjo provides fitness references. It does not diagnose or treat medical conditions or guarantee training results.", "skip": "Skip to content",
    },
    "zh": {
        "lang": "zh-CN", "title": "练境 Lenjo — iPhone AI 健身教练与训练记录",
        "description": "练境 Lenjo 是本地优先的 AI 健身教练与训练记录 App，适用于 iPhone，可选配 Apple Watch，支持逐组记录、恢复参考、饮食拍照与可编辑长期记忆。",
        "label": "产品介绍 · iPhone + Apple Watch", "h1": "练境 Lenjo<br><span>AI 健身教练。</span>",
        "intro": "审核一份计划，记录实际完成的每一组，再讨论下一次怎么练。练境把力量训练、恢复状态和饮食放进连续的训练上下文，适用于 iPhone，可选配 Apple Watch。",
        "cta": "在 App Store 获取练境 ↗", "website": "查看官网 ↗", "web": "https://lenjoapp.com/",
        "nav": ["功能", "常见问题", "English"], "other": "../", "caption": "训练计划示例 · 审核后再开始",
        "facts_title": "每一次记录，接上下一次训练。", "facts": [("产品名称", "练境 / Lenjo"), ("支持设备", "iPhone · iOS 17+<br>Apple Watch · watchOS 10+"), ("免费与 Pro", "iPhone 训练记录免费<br>Pro 为可选订阅"), ("产品支持", "练境 / Lenjo<br>lenjoapp.com")],
        "features_title": "从计划，到实际完成的每一组。",
        "features": [
            ("AI 安排训练计划", "告诉教练目标、器械、经验和可用时间。它可以结合已保存的训练记录与获准使用的恢复信息，建议动作、组数、次数、重量和休息。审核并修改后再开始。"),
            ("逐组训练记录", "执行已安排的计划，或开始自由训练。在 iPhone 上记录每组实际重量、次数、RPE 和完成状态，保存后再用这些记录讨论下一次调整。"),
            ("Apple Watch 组间恢复", "Pro 用户可把计划发到已配对的 Watch，在手腕上记录训练。有可用健康数据和相应授权时，可查看实时心率、组间恢复参考与训练后的逐组心率时间轴。"),
            ("饮食拍照与营养记录", "手动记录食物，或拍照估算食物、热量、蛋白质、碳水与脂肪。先检查估算结果，修改需要纠正的项目，再确认保存。"),
            ("有氧训练计时", "有氧训练按分钟记录，可按项目填写速度、坡度和距离。Pro 用户戴 Apple Watch 训练时可记录可用的心率、热量和距离数据。"),
            ("趋势与长期记忆", "回看体重、活动、恢复与训练趋势。教练使用的长期记忆可查看、编辑或删除，包括目标、器械和偏好等稳定信息。")],
        "flow_title": "四步开始第一场训练。", "flow": [("说明条件", "告诉教练目标、器械和今天可用的时间。"), ("审核计划", "检查并修改动作、组数、次数和重量，再开始训练。"), ("记录完成", "逐组填写实际完成情况，训练结束后保存。"), ("讨论下一练", "用保存的结果和恢复感受，讨论下一次调整。")],
        "screens_title": "看看训练怎样执行。", "screen_captions": ["iPhone · 逐组记录重量、次数和 RPE", "Apple Watch · 组间恢复参考"],
        "screen_note": "截图使用官网公开的训练示例数据，界面可能随版本与语言变化。恢复提示用于训练节奏参考，不是医疗指标。",
        "access_title": "免费记录，可选 Pro。", "access": "iPhone 训练执行与记录免费，并提供 AI 体验额度。Pro 包含 Apple Watch 训练执行与恢复参考、更高 AI 教练和照片分析额度、深度报告。支持月付与年付；当前价格、试用资格和额度以 App 内与 App Store 为准。",
        "data_title": "记录本地保存，AI 按需使用。", "data": "核心记录主要保存在本机。Apple 登录和 Apple 健康权限为可选。AI 教练和照片分析需要联网，相关内容在说明与同意后经练境网关发送给第三方模型服务商；拒绝 AI 处理后仍可使用本地训练与记录。",
        "faq_title": "开始之前，了解练境。", "faq": [
            ("练境是什么 App？", "练境 Lenjo 是本地优先的 iPhone AI 健身教练与训练记录 App，把结构化训练计划、实际完成记录、恢复状态和饮食放在一起。"),
            ("必须有 Apple Watch 吗？", "不需要。iPhone 可独立执行并保存训练。腕上训练为可选功能，需要 Pro、已配对的 Watch 和练境 Watch App；心率功能还需要相关权限与可用数据。"),
            ("不用 AI 也能记录吗？", "可以。拒绝 AI 处理后仍能使用本地训练执行与记录。AI 教练和照片分析需要联网及同意处理。"),
            ("生成的计划能直接训练吗？", "可以。先审核并修改计划，再开始执行，记录实际完成的每一组并保存，之后讨论下一次训练。"),
            ("可以拍照记录饮食吗？", "可以。照片分析会估算食物与营养，检查并修改后再确认保存。照片无法可靠判断所有配料与份量。"),
            ("怎样联系练境？", "官网为 lenjoapp.com，App Store ID 为 6784486285。公开联系邮箱为 KmTech2026@outlook.com，也可以通过官网支持页反馈。")],
        "support_title": "联系练境。", "support": "产品问题与反馈可通过官网支持页或邮箱联系作者。GitHub Issues 可提交一般功能建议和错误，请避免公开个人健康资料与私密聊天内容。",
        "support_link": "支持与联系", "privacy": "隐私政策", "terms": "使用条款", "docs": "上手步骤", "rights": "公开产品介绍与示例截图。App 源码未在本仓库发布。",
        "checked": "产品资料于 2026 年 10 月 11 日对照公开 App Store 页面与官网核实。",
        "boundary": "练境提供健身参考，不提供医疗诊断或治疗，也不保证训练结果。", "skip": "跳到正文",
    },
}

for locale, c in COPY.items():
    prefix = "../" if locale == "zh" else ""
    url = BASE + ("zh/" if locale == "zh" else "")
    schema = {"@context": "https://schema.org", "@graph": [
        {"@type": "SoftwareApplication", "@id": "https://lenjoapp.com/#app", "name": "Lenjo", "alternateName": "练境", "applicationCategory": "HealthApplication", "operatingSystem": "iOS 17 or later; optional watchOS 10 or later", "url": "https://lenjoapp.com/", "downloadUrl": STORE, "image": BASE + "assets/app-icon.png", "description": c["description"], "sameAs": [STORE, REPO], "featureList": [x[0] for x in c["features"]]},
        {"@type": "WebPage", "@id": url, "url": url, "name": c["title"], "inLanguage": c["lang"], "description": c["description"], "dateModified": CHECKED, "about": {"@id": "https://lenjoapp.com/#app"}},
    ]}
    facts = "".join(f"<div><dt>{escape(k)}</dt><dd>{v}</dd></div>" for k, v in c["facts"])
    features = "".join(f'<article class="feature"><span class="number">0{i+1}</span><h3>{escape(h)}</h3><p>{escape(t)}</p></article>' for i, (h, t) in enumerate(c["features"]))
    flow = "".join(f'<article><span class="number">0{i+1}</span><h3>{escape(h)}</h3><p>{escape(t)}</p></article>' for i, (h, t) in enumerate(c["flow"]))
    faq = "".join(f"<article><h3>{escape(q)}</h3><p>{escape(a)}</p></article>" for q, a in c["faq"])
    html = f'''<!doctype html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c['title']}</title><meta name="description" content="{escape(c['description'], quote=True)}"><meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}"><link rel="alternate" hreflang="en" href="{BASE}"><link rel="alternate" hreflang="zh-CN" href="{BASE}zh/"><link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website"><meta property="og:title" content="{c['title']}"><meta property="og:description" content="{escape(c['description'], quote=True)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}assets/app-icon.png">
<meta name="twitter:card" content="summary"><meta name="theme-color" content="#0c100e"><link rel="icon" href="{prefix}assets/app-icon.png"><link rel="stylesheet" href="{prefix}styles.css?v={CSS_VERSION}">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script></head>
<body class="{locale}"><a class="skip" href="#content">{c['skip']}</a><header><nav class="wrap" aria-label="Navigation"><a class="brand" href="{prefix}index.html"><img src="{prefix}assets/app-icon.png" alt="Lenjo app icon" width="38" height="38">LENJO / 练境</a><div class="nav-links"><a class="optional" href="#features">{c['nav'][0]}</a><a href="#faq">{c['nav'][1]}</a><a href="{c['other']}">{c['nav'][2]}</a></div></nav></header>
<main id="content" class="wrap"><section class="hero"><div><p class="eyebrow">{c['label']}</p><h1>{c['h1']}</h1><p class="intro">{c['intro']}</p><div class="buttons"><a class="button primary" href="{STORE}">{c['cta']}</a><a class="button" href="{c['web']}">{c['website']}</a></div><p class="note">iPhone · iOS 17+ &nbsp; / &nbsp; Apple Watch · watchOS 10+</p></div><figure><img class="screen" src="{prefix}assets/coach-plan.png" width="1206" height="2622" alt="Lenjo AI coach structured workout plan example"><figcaption>{c['caption']}</figcaption></figure></section>
<section class="section"><p class="eyebrow">01 / LENJO</p><h2>{c['facts_title']}</h2><dl class="facts">{facts}</dl></section>
<section id="features" class="section"><p class="eyebrow">02 / FEATURES</p><h2>{c['features_title']}</h2><div class="features">{features}</div></section>
<section class="section"><p class="eyebrow">03 / START</p><h2>{c['flow_title']}</h2><div class="flow">{flow}</div><a href="{REPO}/blob/main/docs/getting-started.md">{c['docs']} ↗</a></section>
<section class="section"><p class="eyebrow">04 / IN THE APP</p><h2>{c['screens_title']}</h2><div class="screens"><figure><img loading="lazy" src="{prefix}assets/workout-log.png" alt="Lenjo iPhone workout log: actual weight, reps and RPE" width="1206" height="2622"><figcaption>{c['screen_captions'][0]}</figcaption></figure><figure><img loading="lazy" src="{prefix}assets/watch-ready.png" alt="Lenjo Apple Watch between-set recovery guidance" width="416" height="496"><figcaption>{c['screen_captions'][1]}</figcaption></figure></div><p class="note" style="margin-top:18px">{c['screen_note']}</p></section>
<section class="section two-col"><article><h2>{c['access_title']}</h2><p>{c['access']}</p></article><article><h2>{c['data_title']}</h2><p>{c['data']}</p><a href="https://lenjoapp.com/privacy.html">{c['privacy']} ↗</a></article></section>
<section id="faq" class="section"><p class="eyebrow">05 / FAQ</p><h2>{c['faq_title']}</h2><div class="faq">{faq}</div></section>
<section class="section"><p class="eyebrow">06 / SUPPORT</p><h2>{c['support_title']}</h2><p style="max-width:750px">{c['support']}</p><div class="links"><a href="https://lenjoapp.com/support.html">{c['support_link']}</a><a href="mailto:KmTech2026@outlook.com">KmTech2026@outlook.com</a><a href="{REPO}">GitHub</a><a href="https://lenjoapp.com/terms.html">{c['terms']}</a></div></section>
</main><footer><div class="wrap"><p>{c['boundary']}</p><p>{c['checked']}</p><div class="footer-row"><span>© 2026 Lenjo · {c['rights']}</span><a href="{prefix}product.json">Product facts JSON</a></div></div></footer></body></html>
'''
    target = ROOT / ("zh/index.html" if locale == "zh" else "index.html")
    target.parent.mkdir(exist_ok=True)
    target.write_text(html)

facts = {"name": "Lenjo", "alternateName": "练境", "type": "AI fitness coach and workout tracker", "appStoreId": "6784486285", "appStoreUrl": STORE, "website": "https://lenjoapp.com/", "englishWebsite": "https://lenjoapp.com/en/", "productPage": BASE, "chineseProductPage": BASE + "zh/", "repository": REPO, "support": {"product": "Lenjo / 练境", "email": "KmTech2026@outlook.com"}, "minimumRequirements": {"iOS": "17.0", "optionalWatchOS": "10.0"}, "access": "Free iPhone workout logging; optional Lenjo Pro for Watch execution and recovery, higher AI allowances and deep reports. Current limits and prices are in the app.", "features": [x[0] for x in COPY["en"]["features"]], "privacyPolicy": "https://lenjoapp.com/privacy.html", "supportUrl": "https://lenjoapp.com/support.html", "dataHandling": "Core records primarily on device. AI requests require consent and process relevant data with third-party model providers.", "sourceCode": "Proprietary; this repository contains public product information.", "informationChecked": CHECKED, "sources": ["https://apps.apple.com/us/app/id6784486285", "https://apps.apple.com/cn/app/id6784486285", "https://lenjoapp.com/en/"]}
(ROOT / "product.json").write_text(json.dumps(facts, ensure_ascii=False, indent=2) + "\n")
(ROOT / "sitemap.xml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{BASE}</loc><lastmod>{CHECKED}</lastmod></url><url><loc>{BASE}zh/</loc><lastmod>{CHECKED}</lastmod></url></urlset>
''')
print("Built English and Chinese static HTML, product.json and sitemap.xml")
