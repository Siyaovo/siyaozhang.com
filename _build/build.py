# -*- coding: utf-8 -*-
"""Build siyaozhang.com from one content file, so the three languages stay aligned.

Usage: python3 _build/build.py
Writes: index.html, zh.html, fr.html, and redirect pages for retired URLs.
Edit the CONTENT dict below, never the generated HTML by hand.
Jekyll ignores folders that start with "_", so this script is not published.
"""

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UPDATED = {"en": "Updated November 2026", "zh": "更新于 2026 年 11 月", "fr": "Mis à jour en novembre 2026"}
EMAIL = "siyao.zhang00@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/siyao-z-707906320/"
GITHUB = "https://github.com/Siyaovo"
GH = "https://github.com/Siyaovo/"

PAGES = {
    "en": dict(file="index.html", lang="en", path="/", brand="Siyao Zhang",
        title="Siyao Zhang",
        desc="Siyao Zhang works on AI agents for manufacturing, and on the evals that tell us whether they actually got better.",
        nav=("Work", "Background", "Contact"),
        hello="Hi, I’m Siyao Zhang.",
        intro=[
            "I work on AI agents for manufacturing, and on the evals that tell us whether they actually got better.",
            "Right now I’m at Yuanmu, an industrial-AI startup in Beijing. I’ve designed, tested and shipped skills for our production-scheduling agent, starting from real needs that came up in customer conversations and iterating quickly. I also built the evaluation tools we use to compare models. Lately I’ve been working with our 0-to-1 product team on an AI workbench that helps manufacturing engineers go from a customer’s drawing to a process plan and a quote. It has pulled me into the layer underneath: how agents get their tools, memory and checks, and how to make product decisions for AI.",
            "Before that, I studied economics and Japanese in Beijing, spent a year in Tokyo, and did a two-year master’s in Paris on a CSC scholarship. I started building with Claude Code in 2026, and this is my prototype site.",
            "Outside of work, I make short videos about learning AI and tech, and travel around the world.",
        ],
        now_h="Now", now_date="November 2026",
        now="I’m finishing a finance master’s at UIBE, with a thesis on how Chinese chip stocks reacted to US export controls. At work I’m learning how an agent harness gets built for one industry, so on the side I’m building a small one of my own. I graduate in June 2027 and I’m looking for AI product and engineering roles. I can start an internship from January.",
        work_h="Things I’ve made",
        work_intro="Small things, mostly built to solve my own problems.",
        links=dict(code="Code", demo="Live demo", pdf="Case study (PDF)", poster="Poster (PDF)"),
        projects=[
            ("A task board my AI agents and I share", "2026", [("code", GH + "md-task-router")],
             "An early project with Claude Code: a markdown task board that my agents and I both edit. Every new session reads it first, so the AI remembers what we’re working on, and in my own setup anything waiting on me goes onto my calendar. Better tools have caught up on some of this. What stayed with me is the question of what an agent should remember, and when it should hand a decision back to a person."),
            ("AI Tutor", "2026", [("code", GH + "interactive-learning-system")],
             "One README that turns Claude Code into a tutor. It writes a lesson, asks you three questions, and picks the next lesson based on which ideas you actually understood. The demo video got about 110,000 views on Douyin, more than anything else I’ve made."),
            ("A content workflow for my videos", "2026", [],
             "One agent with eight skills: topic filter, script, hook, title, an AI-writing check, benchmarking and data review. After each video, the review skill writes what the numbers showed into a shared methodology file that the topic filter reads next time. So far the file has retired four kinds of content I used to make."),
            ("Rooted (根)", "2026", [("demo", "https://rooted-azure.vercel.app")],
             "Drag a slider and watch a Chinese character change from oracle-bone script to its modern form. I made it for learners who memorise characters one at a time without seeing the logic. One rule I kept: no invented etymology. When a character isn’t a picture of something, it shows its parts instead."),
            ("A function-calling agent, without a framework", "2026", [("code", GH + "function-calling-demo")],
             "About 350 lines of Python on Anthropic’s tool-use API, written to see what frameworks hide. Five tools, a guard against reading files outside its folder, and 13 tests."),
            ("South Africa’s electricity system", "2025", [("pdf", "deloitte-energy-case-study.pdf"), ("code", GH + "south-africa-electricity-analysis")],
             "A university group project in Paris, mentored by Deloitte. We forecast demand with six models and optimised dispatch in Python. A simple SARIMAX held up better than LSTM and TFT under supply stress, and in our scenario 5% more renewables cut load shedding from 712 to 118 hours a year."),
            ("How exposed European jobs are to robots", "2025", [("poster", "robotics-exposure-poster.pdf"), ("code", GH + "robotics-exposure-europe")],
             "Group research for a Big Data for Development course at Panthéon-Sorbonne. We built an exposure index for occupations from patent and job-description text. Across 34 countries, one standard deviation more exposure went with about 7% lower hourly wages."),
        ],
        bg_h="Background",
        timeline=[
            ("2026 – now", "AI Agent Product Intern, Yuanmu, Beijing"),
            ("2026 – 2027", "MSc Finance, University of International Business and Economics (UIBE), Beijing"),
            ("2024 – 2026", "Master’s in Sustainable Development Economics, Panthéon-Sorbonne, Paris, on a China Scholarship Council scholarship"),
            ("2025", "Healthcare equity research intern, Guosheng Securities, Beijing"),
            ("2023 – 2024", "Exchange year, Waseda University, Tokyo"),
            ("2020 – 2024", "BA in Economics and Japanese, UIBE, Beijing"),
        ],
        bg_note="At UIBE I also led a 60-person volunteer association and coordinated our volunteer team at the Beijing 2022 Winter Olympics. I speak Chinese, English and Japanese, and a bit of French.",
        contact_h="Contact",
        contact="Email is the best way to reach me: {email}. I’m also on {linkedin} and {github}. Happy to send my CV.",
    ),
    "zh": dict(file="zh.html", lang="zh-CN", path="/zh.html", brand="张思瑶",
        title="张思瑶",
        desc="张思瑶，做制造业的 AI Agent，以及判断它们是否真的变好的评测。",
        nav=("做过的东西", "经历", "联系"),
        hello="你好，我是张思瑶。",
        intro=[
            "我做制造业的 AI Agent，以及判断它们是否真的变好的评测。",
            "目前我在北京的工业 AI 创业公司圆木。我从客户沟通里暴露出的真实需求出发，为排产 Agent 设计、测试并上线 Skill，快速试错迭代；也搭了团队用来对比模型的评测工具。最近我在 0 到 1 的产品团队里，参与一个 AI 工作台：帮制造业工程师从客户图纸一路做到工艺方案和报价。这让我往下钻了一层：Agent 怎么拿到工具、记忆和检查机制，以及 AI 产品该怎么做决策。",
            "在这之前，我在北京读经济和日语，在东京交换一年，又拿国家留学基金委奖学金在巴黎读了两年硕士。2026 年开始用 Claude Code 做东西，这个网站就是原型。",
            "工作之外，我拍学 AI 和科技的短视频，也到处旅行。",
        ],
        now_h="现在", now_date="2026 年 11 月",
        now="我在对外经济贸易大学读金融硕士的最后一年，论文研究美国出口管制下 A 股芯片股的反应。工作上在学一个行业的 Agent Harness 怎么搭，所以业余也在自己搭一个小的。2027 年 6 月毕业，在看 AI 产品和工程方向的机会，2027 年 1 月起可以实习。",
        work_h="做过的东西",
        work_intro="都不大，多数是为了解决自己的问题。",
        links=dict(code="代码", demo="在线体验", pdf="案例报告（PDF）", poster="海报（PDF）"),
        projects=[
            ("和 AI Agent 共用的任务看板", "2026", [("code", GH + "md-task-router")],
             "用 Claude Code 做的早期项目：一个我和 Agent 都会编辑的 Markdown 任务看板。每次新对话先读它，AI 就记得我们在做什么；在我自己的配置里，卡在我这里的事会直接进日程。现在更好的工具已经能做到其中一部分，但它让我一直在想：Agent 该记住什么，什么时候该把决定交还给人。"),
            ("AI Tutor", "2026", [("code", GH + "interactive-learning-system")],
             "一个 README，把 Claude Code 变成老师：先讲一课，问你三个问题，再根据你真正懂了哪些概念决定下一课。演示视频在抖音大约 11 万播放，是我做过的东西里看的人最多的。"),
            ("给自己短视频用的内容工作流", "2026", [],
             "一个 Agent 加八个 Skill：选题过滤、脚本、开头、标题、AI 痕迹检查、对标和数据复盘。每条视频发完，复盘 Skill 会把数据结论写进一份共享的方法论文件，下次选题过滤时读取。到现在，这份文件已经淘汰了我以前常做的四类内容。"),
            ("Rooted（根）", "2026", [("demo", "https://rooted-azure.vercel.app")],
             "拖动滑块，看一个汉字从甲骨文变成今天的写法。做给一个字一个字死记、看不到字形逻辑的学习者。我守住的一条：不编字源。不是象形字的，就拆成部件来讲。"),
            ("不用框架写的函数调用 Agent", "2026", [("code", GH + "function-calling-demo")],
             "大约 350 行 Python，直接用 Anthropic 的工具调用接口，想看清框架帮我们藏了什么。五个工具，一道防止读取文件夹以外文件的检查，13 个测试。"),
            ("南非电力系统", "2025", [("pdf", "deloitte-energy-case-study.pdf"), ("code", GH + "south-africa-electricity-analysis")],
             "在巴黎的大学小组项目，由德勤导师指导。我们用六个模型预测用电需求，并用 Python 优化电力调度。在供给紧张时，简单的 SARIMAX 比 LSTM 和 TFT 更稳；在我们的情景里，可再生能源增加 5%，每年限电时长从 712 小时降到 118 小时。"),
            ("欧洲岗位受机器人影响的程度", "2025", [("poster", "robotics-exposure-poster.pdf"), ("code", GH + "robotics-exposure-europe")],
             "巴黎一大「发展大数据」课程的小组研究。我们用专利和岗位描述文本，给各职业做了机器人暴露指数。在 34 个国家里，暴露度每高一个标准差，时薪平均低约 7%。"),
        ],
        bg_h="经历",
        timeline=[
            ("2026 – 至今", "AI Agent 产品实习生，圆木，北京"),
            ("2026 – 2027", "金融硕士，对外经济贸易大学，北京"),
            ("2024 – 2026", "可持续发展经济学硕士，巴黎第一大学（先贤祠-索邦），国家留学基金委公派"),
            ("2025", "医药行业研究实习生，国盛证券，北京"),
            ("2023 – 2024", "交换一年，早稻田大学，东京"),
            ("2020 – 2024", "经济学、日语双学位，对外经济贸易大学，北京"),
        ],
        bg_note="在贸大时，我还带过一个 60 人的志愿者协会，协调过学校在北京 2022 年冬奥会的志愿者团队。会中文、英语、日语，还有一点法语。",
        contact_h="联系",
        contact="最方便的是发邮件：{email}。也可以在 {linkedin} 和 {github} 找到我。需要简历的话，发邮件给我就好。",
    ),
    "fr": dict(file="fr.html", lang="fr", path="/fr.html", brand="Siyao Zhang",
        title="Siyao Zhang",
        desc="Siyao Zhang travaille sur des agents IA pour l’industrie, et sur les évaluations qui disent s’ils se sont vraiment améliorés.",
        nav=("Projets", "Parcours", "Contact"),
        hello="Bonjour, je suis Siyao Zhang.",
        intro=[
            "Je travaille sur des agents IA pour l’industrie, et sur les évaluations qui disent s’ils se sont vraiment améliorés.",
            "Aujourd’hui, je suis chez Yuanmu, une start-up d’IA industrielle à Pékin. J’ai conçu, testé et mis en production des skills pour notre agent de planification, à partir de besoins réels apparus dans les échanges avec les clients, en itérant vite. J’ai aussi construit les outils d’évaluation que nous utilisons pour comparer les modèles. Depuis peu, je travaille avec notre équipe produit 0-to-1 sur un atelier IA qui aide les ingénieurs à passer d’un plan client à une gamme de fabrication et à un devis. Cela m’a fait descendre d’un niveau : comment les agents obtiennent leurs outils, leur mémoire et leurs vérifications, et comment prendre des décisions produit pour l’IA.",
            "Avant cela, j’ai étudié l’économie et le japonais à Pékin, passé un an à Tokyo, puis fait un master de deux ans à Paris grâce à une bourse CSC. J’ai commencé à construire avec Claude Code en 2026, et ce site en est le prototype.",
            "En dehors du travail, je fais de courtes vidéos sur l’apprentissage de l’IA et de la tech, et je voyage dès que je peux.",
        ],
        now_h="En ce moment", now_date="novembre 2026",
        now="Je termine un master de finance à l’UIBE, avec un mémoire sur la réaction des actions chinoises de semi-conducteurs aux contrôles américains à l’exportation. Au travail, j’apprends comment se construit un harness d’agents pour une industrie, alors j’en construis un petit de mon côté. Je serai diplômée en juin 2027 et je cherche des postes en produit ou en ingénierie IA. Je peux commencer un stage dès janvier.",
        work_h="Ce que j’ai fait",
        work_intro="De petites choses, souvent construites pour régler mes propres problèmes.",
        links=dict(code="Code", demo="Démo", pdf="Étude de cas (PDF)", poster="Poster (PDF)"),
        projects=[
            ("Un tableau de tâches partagé avec mes agents", "2026", [("code", GH + "md-task-router")],
             "Un de mes premiers projets avec Claude Code : un tableau de tâches en Markdown que mes agents et moi modifions tous les deux. Chaque nouvelle session le lit d’abord, donc l’IA sait ce sur quoi on travaille, et dans mon installation, ce qui attend une décision de ma part arrive dans mon agenda. De meilleurs outils font maintenant une partie de cela. Ce qui m’est resté, c’est la question de ce qu’un agent doit retenir, et du moment où il doit rendre la décision à une personne."),
            ("AI Tutor", "2026", [("code", GH + "interactive-learning-system")],
             "Un README qui transforme Claude Code en tuteur. Il écrit une leçon, pose trois questions, puis choisit la leçon suivante selon les idées vraiment comprises. La vidéo de démo a fait environ 110 000 vues sur Douyin, plus que tout ce que j’ai fait d’autre."),
            ("Un workflow pour mes vidéos", "2026", [],
             "Un agent avec huit skills : filtre de sujets, script, accroche, titre, détection du style IA, benchmark et analyse des données. Après chaque vidéo, la skill d’analyse écrit ce que les chiffres ont montré dans un fichier de méthodologie partagé, que le filtre relit la fois suivante. Ce fichier a déjà écarté quatre types de contenu que je faisais avant."),
            ("Rooted (根)", "2026", [("demo", "https://rooted-azure.vercel.app")],
             "On fait glisser un curseur et un caractère chinois passe de l’écriture oraculaire à sa forme moderne. Je l’ai fait pour les apprenants qui mémorisent les caractères un par un sans en voir la logique. Une règle : pas d’étymologie inventée. Quand un caractère n’est pas un pictogramme, il montre ses composants."),
            ("Un agent à appels de fonctions, sans framework", "2026", [("code", GH + "function-calling-demo")],
             "Environ 350 lignes de Python sur l’API tool use d’Anthropic, pour voir ce que les frameworks cachent. Cinq outils, une protection contre la lecture de fichiers hors de son dossier, et 13 tests."),
            ("Le système électrique sud-africain", "2025", [("pdf", "deloitte-energy-case-study.pdf"), ("code", GH + "south-africa-electricity-analysis")],
             "Un projet de groupe universitaire à Paris, encadré par Deloitte. Nous avons prévu la demande avec six modèles et optimisé le dispatch en Python. Un simple SARIMAX a mieux résisté que LSTM et TFT en période de tension, et dans notre scénario, 5 % de renouvelables en plus faisaient passer les délestages de 712 à 118 heures par an."),
            ("L’exposition des emplois européens aux robots", "2025", [("poster", "robotics-exposure-poster.pdf"), ("code", GH + "robotics-exposure-europe")],
             "Recherche de groupe pour le cours Big Data for Development à Panthéon-Sorbonne. Nous avons construit un indice d’exposition des métiers à partir de brevets et d’offres d’emploi. Dans 34 pays, un écart-type d’exposition en plus allait avec des salaires horaires environ 7 % plus bas."),
        ],
        bg_h="Parcours",
        timeline=[
            ("2026 – auj.", "Stagiaire produit agents IA, Yuanmu, Pékin"),
            ("2026 – 2027", "MSc Finance, University of International Business and Economics (UIBE), Pékin"),
            ("2024 – 2026", "Master en économie du développement durable, Paris 1 Panthéon-Sorbonne, boursière du China Scholarship Council"),
            ("2025", "Stagiaire en recherche actions, secteur santé, Guosheng Securities, Pékin"),
            ("2023 – 2024", "Année d’échange, Université Waseda, Tokyo"),
            ("2020 – 2024", "Licence d’économie et de japonais, UIBE, Pékin"),
        ],
        bg_note="À l’UIBE, j’ai aussi dirigé une association de 60 bénévoles et coordonné notre équipe de volontaires aux Jeux d’hiver de Pékin 2022. Je parle chinois, anglais et japonais ; mon français reste modeste, merci de votre indulgence.",
        contact_h="Contact",
        contact="Le plus simple, c’est un e-mail : {email}. Je suis aussi sur {linkedin} et {github}. Je vous envoie volontiers mon CV.",
    ),
}

CSS = """
:root{--bg:#faf8f4;--ink:#1f1d1a;--muted:#6b655c;--rule:#e4ded3;--accent:#a2482b}
@media (prefers-color-scheme:dark){:root{--bg:#161513;--ink:#ebe6de;--muted:#9d968b;--rule:#2d2a26;--accent:#e38a66}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:18px/1.65 "Source Serif 4",Georgia,"Songti SC",serif;font-optical-sizing:auto}
html[lang="zh-CN"] body{font-family:"Source Serif 4","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;font-size:17px;line-height:1.85}
.wrap{max-width:660px;margin:0 auto;padding:40px 20px 72px}
header{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:72px;font:14px/1.4 -apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",sans-serif}
header .name{font-weight:600;letter-spacing:.01em;color:var(--ink);text-decoration:none}
nav{display:flex;gap:18px;flex-wrap:wrap}
nav a{color:var(--muted);text-decoration:none}
nav a:hover,nav a[aria-current]{color:var(--ink)}
.langs{display:flex;gap:10px;color:var(--muted)}
.langs a{color:var(--muted);text-decoration:none}
.langs a[aria-current]{color:var(--ink);font-weight:600}
h1{font-size:34px;line-height:1.2;font-weight:600;letter-spacing:-.01em;margin:0 0 28px}
h2{font:600 12px/1.4 -apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",sans-serif;text-transform:uppercase;letter-spacing:.14em;color:var(--muted);margin:80px 0 24px}
html[lang="zh-CN"] h2{letter-spacing:.2em;font-size:13px}
p{margin:0 0 18px}
a{color:inherit;text-decoration:underline;text-decoration-color:var(--accent);text-decoration-thickness:1px;text-underline-offset:3px}
a:hover{color:var(--accent)}
.now-date{color:var(--muted);font-size:15px}
.project{padding:22px 0;border-top:1px solid var(--rule)}
.project:last-child{border-bottom:1px solid var(--rule)}
.project h3{font-size:19px;font-weight:600;margin:0;display:inline}
.project .year{color:var(--muted);font-size:15px;margin-left:8px}
.project p{margin:8px 0 0}
.project .links{margin-top:8px;font:14px/1.5 -apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",sans-serif;display:flex;gap:16px;flex-wrap:wrap}
.lede{color:var(--muted)}
dl{margin:0;display:grid;grid-template-columns:120px 1fr;gap:10px 20px}
dt{color:var(--muted);font-size:15px;padding-top:2px;font-variant-numeric:tabular-nums}
dd{margin:0}
.note{margin-top:24px}
footer{margin-top:80px;color:var(--muted);font:13px/1.5 -apple-system,BlinkMacSystemFont,"Helvetica Neue","PingFang SC",sans-serif}
@media (max-width:560px){body{font-size:17px}h1{font-size:28px}header{margin-bottom:48px}dl{grid-template-columns:1fr;gap:2px}dd{margin-bottom:12px}h2{margin-top:64px}}
"""

LANGS = [("en", "EN", "index.html"), ("zh", "中文", "zh.html"), ("fr", "FR", "fr.html")]


def e(s):
    return html.escape(s, quote=False)


def page(key):
    c = PAGES[key]
    alt = "\n".join('<link rel="alternate" hreflang="%s" href="https://siyaozhang.com%s">' % (PAGES[k]["lang"], PAGES[k]["path"]) for k in PAGES)
    langs = " ".join('<a href="%s"%s>%s</a>' % (f, ' aria-current="page"' if k == key else "", lbl) for k, lbl, f in LANGS)
    intro = "\n".join("<p>%s</p>" % e(x) for x in c["intro"])
    projs = []
    for name, year, links, text in c["projects"]:
        ls = "".join('<a href="%s"%s>%s</a>' % (u, "" if u.endswith(".pdf") else ' rel="noopener"', e(c["links"][k])) for k, u in links)
        projs.append('<article class="project"><h3>%s</h3><span class="year">%s</span><p>%s</p>%s</article>'
                     % (e(name), year, e(text), '<div class="links">%s</div>' % ls if ls else ""))
    tl = "\n".join("<dt>%s</dt><dd>%s</dd>" % (e(a), e(b)) for a, b in c["timeline"])
    contact = e(c["contact"]).format(
        email='<a href="mailto:%s">%s</a>' % (EMAIL, EMAIL),
        linkedin='<a href="%s" rel="noopener">LinkedIn</a>' % LINKEDIN,
        github='<a href="%s" rel="noopener">GitHub</a>' % GITHUB)
    return f"""<!doctype html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(c['title'])}</title>
<meta name="description" content="{e(c['desc'])}">
<meta property="og:title" content="{e(c['title'])}">
<meta property="og:description" content="{e(c['desc'])}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://siyaozhang.com{c['path']}">
<link rel="canonical" href="https://siyaozhang.com{c['path']}">
{alt}
<meta name="color-scheme" content="light dark">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
<header>
<a class="name" href="{c['file']}">{e(c['brand'])}</a>
<nav><a href="#work">{e(c['nav'][0])}</a><a href="#background">{e(c['nav'][1])}</a><a href="#contact">{e(c['nav'][2])}</a></nav>
<div class="langs">{langs}</div>
</header>
<main>
<h1>{e(c['hello'])}</h1>
{intro}
<h2 id="now">{e(c['now_h'])}</h2>
<p>{e(c['now'])} <span class="now-date">({e(c['now_date'])})</span></p>
<h2 id="work">{e(c['work_h'])}</h2>
<p class="lede">{e(c['work_intro'])}</p>
{chr(10).join(projs)}
<h2 id="background">{e(c['bg_h'])}</h2>
<dl>
{tl}
</dl>
<p class="note">{e(c['bg_note'])}</p>
<h2 id="contact">{e(c['contact_h'])}</h2>
<p>{contact}</p>
</main>
<footer>{UPDATED[key]}</footer>
</div>
</body>
</html>
"""


REDIRECTS = {  # retired pages whose old claims no longer match the facts
    "ai-automation.html": "index.html#work", "ai-automation-zh.html": "zh.html#work", "ai-automation-fr.html": "fr.html#work",
    "prompt-portfolio.html": "index.html#work", "prompt-portfolio-zh.html": "zh.html#work", "prompt-portfolio-fr.html": "fr.html#work",
}


def redirect(target):
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="https://siyaozhang.com/{target.split('#')[0]}">
<title>Moved</title></head>
<body><p>This page has moved: <a href="{target}">{target}</a></p></body></html>
"""


if __name__ == "__main__":
    (ROOT / "style.css").write_text(CSS.strip() + "\n", encoding="utf-8")
    for k in PAGES:
        (ROOT / PAGES[k]["file"]).write_text(page(k), encoding="utf-8")
    for f, t in REDIRECTS.items():
        (ROOT / f).write_text(redirect(t), encoding="utf-8")
    print("built", ", ".join(p["file"] for p in PAGES.values()), "+ style.css +", len(REDIRECTS), "redirects")
