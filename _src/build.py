#!/usr/bin/env python3
"""Generate the hub pages (index, guides, value, categories, privacy [unlinked, noindex], links [Gift Finds Daily link-in-bio, standalone, unlinked]) and category pages for <cat>.theworthguide.com from one brand template (site.css; see BRAND.md), then validate. Run: python3 _src/build.py"""
import json,os,re,sys,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'_src'))
from data import CATS,TAGS
VER=json.load(open(os.path.join(ROOT,'_src/verified.json')))
BADGES=json.load(open(os.path.join(ROOT,'_src/badges.json')))['pages']  # picks + Amazon prices by date; refresh via /workspace/top10/badges
BADGE_LABEL={'premium':'Premium Pick','bang':'Bang for the Buck','value':'Value Pick'}
SITE_CSS=open(os.path.join(ROOT,'_src/site.css')).read()
CAT_CSS=open(os.path.join(ROOT,'_src/cat.css')).read()
PROSE_CSS=open(os.path.join(ROOT,'_src/prose.css')).read()
from sites import SITES
HUB='https://theworthguide.com'
LASTMOD='2026-10-04'
HUB_TAG='theworthguide20-20'
e=lambda s:html.escape(s,quote=True)
sub=lambda k:f'https://{k}.theworthguide.com/'
MARK='<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9" fill="none" stroke="#d4af37" stroke-width="1.8"/><path d="M7.5 12.2 10.6 15.3 16.5 8.8" fill="none" stroke="#d4af37" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FONTS='<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,600;0,8..60,700;1,8..60,600&display=swap" rel="stylesheet">'
FAV='<link rel="icon" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 64 64\'><rect width=\'64\' height=\'64\' rx=\'14\' fill=\'%231c1917\'/><circle cx=\'32\' cy=\'32\' r=\'19\' fill=\'none\' stroke=\'%23d4af37\' stroke-width=\'4\'/><path d=\'M22 32.5 29 39.5 42 25\' fill=\'none\' stroke=\'%23d4af37\' stroke-width=\'4\' stroke-linecap=\'round\' stroke-linejoin=\'round\'/></svg>">'
NOTE='<p class="note-top">We may earn a commission from qualifying purchases.</p>'
MENU='<button class="mbtn" type="button" aria-label="Menu" aria-controls="nav" aria-expanded="false"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>'
JS='<script>document.querySelector(".mbtn").onclick=function(){var o=document.getElementById("nav").classList.toggle("open");this.setAttribute("aria-expanded",o)}</script>'
NAV=[('guides','Guides'),('value','Value Picks'),('categories','Categories')]
AMZ='rel="nofollow sponsored noopener" target="_blank"'
HUB_ABOUT='Buy it once. Skip the rest. In every top 10: our pick, the value pick, and the one people already buy most.'
def wordmark(name,href): return f'<a class="wm" href="{href}">{MARK}{name}</a>'
def header(active=None,cat=None):
    links=''.join(f'<a href="{HUB if cat else ""}/{k}"{" aria-current=page" if k==active else ""}>{t}</a>' for k,t in NAV)
    if cat: wm=wordmark(f'{CATS[cat]["name"][:-5]}<b>Worth</b>',sub(cat)); links+=f'<a class="hub" href="{HUB}/">The Worth Guide</a>'
    else: wm=wordmark('The <b>Worth</b> Guide','/')
    return f'<a class="skip" href="#main">Skip to content</a><header class="hdr"><div class="wrap bar">{wm}{MENU}<nav class="nav" id="nav" aria-label="Main">{links}</nav></div></header>'
def footer(name,about):
    fam=f'<li><a href="{HUB}/">The Worth Guide</a></li>'+''.join(f'<li><a href="{sub(k)}">{n}Worth</a></li>' for k,n,*_ in SITES)
    return (f'<footer class="ftr"><div class="wrap cols"><div>{name}<p class="about">{e(about)}</p></div><div><p class="flabel">The Worth Guide family</p><ul class="fam">{fam}</ul></div></div>'
            '<div class="legal"><div class="wrap"><p class="disc">We may earn a commission when you buy through links on this site. As an Amazon Associate I earn from qualifying purchases.</p>© 2026 The Worth Guide</div></div></footer>')
def doc(title,desc,canon,body,css,extra=''):
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
{extra}<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canon}">
<meta name="theme-color" content="#f4f1ea">
{FAV}
{FONTS}
<style>{css}</style></head><body>
{body}
{JS}
</body></html>
'''
def link(asin,tag): return f'https://www.amazon.com/dp/{asin}?tag={tag}'
def badges(c,v,tag):
    b=BADGES.get(c,{}).get('picks')
    if not b: return ''
    names={x[0]:x[1] for x in v['items']}
    cards=[]
    for k in ('premium','bang','value'):
        a=b[k]['asin']; assert a in names, (c,a)
        cards.append(f'<article class="pick"><span class="badge b-{k}">{BADGE_LABEL[k]}</span><img src="{e(VER[a]["img"])}" alt="{e(names[a])}"><h3>{e(names[a])}</h3><p>{e(b[k]["line"])}</p><a class="btn" href="{link(a,tag)}" {AMZ}>Check price on Amazon</a></article>')
    return f'<section class="picks" data-badge-picks><h2>Our three standout picks</h2><p class="pk-sub">Chosen from the Top 10 below: one premium, one mid-priced, one budget.</p><div class="pick-grid">{"".join(cards)}</div></section>'
def page(c,v):
    tag=TAGS[c]; rows=[]
    for i,(a,name,blurb,labels,bs) in enumerate(v['items'],1):
        t=''.join(f'<span class="tag">{e(l)}</span>' for l in labels)
        rows.append(f'<article class="row"><div class="im"><span class="rank">#{i}</span><img src="{e(VER[a]["img"])}" alt="{e(name)}" loading="lazy"></div><div><div class="tags">{t}</div><h2>{e(name)}</h2><p>{e(blurb)}</p><a class="btn" href="{link(a,tag)}" {AMZ}>Check price on Amazon</a></div></article>')
    a1,n1,a2,n2,txt,table=v['vs']
    vsimg=lambda a:f'<img src="{e(VER[a]["img"])}" alt="" loading="lazy">'
    lab=lambda a:next(x[3][0] for x in v['items'] if x[0]==a)
    trs=''.join(f'<tr><th>{e(r[0])}</th><td>{e(r[1])}</td><td>{e(r[2])}</td></tr>' for r in table)
    nm=v["name"]; short=nm[:-5]
    body=f'''{header(cat=c)}
<main id="main" class="wrap">
<section class="hero solo">{NOTE}<div><p class="kicker">Top 10 · {e(short)}</p><h1>{e(short)}<em>Worth</em></h1><p class="sub">{e(v["lede"])}</p></div></section>
{badges(c,v,tag)}
<div class="sec-h"><div><h2>The Top 10</h2><p>Labels show our pick, the value pick, and the one people already buy most.</p></div></div>
<div class="list">{"".join(rows)}</div>
<section class="vs-sec" id="vs"><p class="kicker">Vs review</p><h2>{e(n1)} vs {e(n2)}</h2><p>{e(txt)}</p>
<div class="vs"><a href="{link(a1,tag)}" {AMZ}>{vsimg(a1)}<h3>{e(n1)}</h3><span class="tag">{e(lab(a1))}</span></a>
<a href="{link(a2,tag)}" {AMZ}>{vsimg(a2)}<h3>{e(n2)}</h3><span class="tag">{e(lab(a2))}</span></a><span class="vs-or" aria-hidden="true">vs</span></div>
<div class="tbl"><table><thead><tr><th></th><th>{e(n1)}</th><th>{e(n2)}</th></tr></thead><tbody>{trs}</tbody></table></div></section>
<p class="back"><a class="btn ghost" href="{HUB}/categories">← All categories</a><a class="btn ghost" href="{HUB}/value">Value Picks</a></p>
</main>
{footer(wordmark(f"{e(short)}<b>Worth</b>",sub(c)),v["card"])}'''
    return doc(f'{nm} Top 10 — The Worth Guide',f'{nm}: {v["lede"]}',sub(c),body,SITE_CSS+CAT_CSS)
# ---------- hub pages ----------
def hub(slug,title,desc,main,extra='',css=''):
    canon=f'{HUB}/{slug}' if slug else f'{HUB}/'
    body=f'{header(active=slug)}\n<main id="main" class="wrap">{main}</main>\n{footer(wordmark("The <b>Worth</b> Guide","/"),HUB_ABOUT)}'
    return doc(title,desc,canon,body,SITE_CSS+css,extra)
def mosaic(keys): return '<div class="mosaic" aria-hidden="true">'+''.join(f'<img src="/img/t/{k}.webp" alt="" width="720" height="560">' for k in keys)+'</div>'
def chip(s): return f'<span class="chip"{f" style=--a:{s[3]}" if s[3] else ""}>{e(s[2])}</span>'
def cat_card(s,line,cta):
    k,n=s[0],s[1]
    return f'<a class="card" href="{sub(k)}"><div class="ph">{chip(s)}<img src="/img/t/{k}.webp" alt="{e(s[7])}" loading="lazy" width="720" height="560"></div><div class="bd"><h3>{n}<b>Worth</b></h3><p>{e(line)}</p><span class="cta">{cta} →</span></div></a>'
def build_index():
    cards=''.join(cat_card(s,s[4],'View guide') for s in SITES)
    m=f'''<section class="hero">{NOTE}<div><p class="kicker">The Worth Guide</p><h1>Buy it once.<br><em>Skip the rest.</em></h1><p class="sub">In every top 10: our pick, the value pick, and the one people already buy most.</p>
<p class="ctas"><a class="btn" href="/categories">Browse categories</a><a class="btn ghost" href="/value">See value picks</a></p></div>{mosaic(["kitchen","desk","brew"])}</section>
<section class="band quote"><p>“We test. We compare. We tell you what’s actually worth it.”</p><p class="kicker">— Editorial values, real value.</p></section>
<section class="sec"><div class="sec-h"><div><h2>Browse guides by category</h2><p>{len(SITES)} guides, each with its own Top 10.</p></div><a class="more" href="/categories">All categories →</a></div><div class="grid">{cards}</div></section>'''
    return hub('','The Worth Guide','The Worth Guide. Buy it once. Skip the rest. In every top 10: our pick, the value pick, and the one people already buy most.',m,'<meta name="p:domain_verify" content="c5f8d97e196c5b58af1a1045b7d87bb3"/>\n')
def build_categories():
    cards=''.join(cat_card(s,s[6],'See top 10') for s in SITES)
    m=f'''<section class="hero">{NOTE}<div><p class="kicker">Categories</p><h1>Pick a category.<br><em>Get the Top 10.</em></h1><p class="sub">Each guide keeps a top 10 in the categories people already buy. A photo and a product page, or it does not ship.</p><ul class="stats"><li>{len(SITES)} categories</li><li>Our pick · Value pick · Most bought</li></ul></div>{mosaic(["tool","kitchen","watch"])}</section>
<section class="sec"><div class="grid">{cards}</div></section>'''
    return hub('categories','Categories — The Worth Guide','Every Worth Guide category: desk, coffee, sleep, pets, tech, car, kitchen, cleaning, tools, yard, bags, grooming, fitness, bath, travel and watches. Each with its own Top 10.',m)
def build_guides():
    g=''.join(f'<a class="card guide" href="{sub(s[0])}"><div class="ph">{chip(s)}<img src="/pins/t/{s[0]}.webp" alt="{s[1]}Worth guide cover" loading="lazy" width="480" height="720"></div><div class="bd"><h3>{s[1]}<b>Worth</b></h3><p>{e(s[5])}</p><span class="cta">Read the guide →</span></div></a>' for s in SITES)
    S={s[0]:s for s in SITES}; vs=[]
    for c,v in CATS.items():
        a1,n1,a2,n2,txt,_=v['vs']
        vs.append(f'<a class="card vsc" href="{sub(c)}#vs"><div class="ph duo">{chip(S[c])}<img src="{e(VER[a1]["img"])}" alt="{e(n1)}" loading="lazy"><img src="{e(VER[a2]["img"])}" alt="{e(n2)}" loading="lazy"></div><div class="bd"><h3>{e(n1)} vs {e(n2)}</h3><p>{e(txt.split(". ")[0].rstrip("."))}.</p><span class="cta">Read the Vs review →</span></div></a>')
    m=f'''<section class="hero">{NOTE}<div><p class="kicker">Guides</p><h1>Guides that end in<br><em>one good choice.</em></h1><p class="sub">Every guide keeps a Top 10 in a category people already buy: our pick, the value pick, and the one people already buy most.</p><ul class="stats"><li>{len(SITES)} guides</li><li>{len(CATS)} head-to-head Vs reviews</li></ul></div>{mosaic(["desk","sleep","travel"])}</section>
<section class="sec"><div class="sec-h"><div><h2>Category guides</h2><p>Start with the room or the job. Each guide opens on its own Top 10.</p></div></div><div class="grid guide-grid">{g}</div></section>
<section class="sec"><div class="sec-h"><div><h2>Head-to-head</h2><p>When it comes down to two, the Vs review says which one to buy and why.</p></div></div><div class="grid one-m">{"".join(vs)}</div></section>'''
    return hub('guides','Guides — The Worth Guide','All Worth Guide buying guides and head-to-head Vs reviews, from desk gear to watches.',m)
def pcard(a,name,lab,line,frm,cls):
    return f'<article class="card pcard"><div class="ph"><span class="badge {cls}">{lab}</span><img src="{e(VER[a]["img"])}" alt="{e(name)}" loading="lazy"></div><div class="bd"><p class="from">{frm}</p><h3>{e(name)}</h3><p>{e(line)}</p><a class="btn" href="{link(a,HUB_TAG)}" {AMZ}>Check price on Amazon</a></div></article>'
def build_value():
    bands=[]; hero=[]; more=[]
    for c,v in CATS.items():
        b=BADGES.get(c,{}).get('picks'); names={x[0]:x[1] for x in v['items']}
        if b:
            cards=''.join(pcard(b[k]['asin'],names[b[k]['asin']],BADGE_LABEL[k],b[k]['line'],v['name'],f'b-{k}') for k in ('premium','bang','value'))
            hero.append(b['premium']['asin'])
            bands.append(f'<section class="band"><div class="sec-h"><div><p class="kicker">{e(v["name"])}</p><h2>Three standout picks</h2><p>Chosen from the {e(v["name"])} Top 10: one premium, one mid-priced, one budget.</p></div><a class="more" href="{sub(c)}">See the full top 10 →</a></div><div class="trio">{cards}</div></section>')
        else:
            it=next(x for x in v['items'] if 'Value pick' in x[3])
            more.append(pcard(it[0],it[1],'Value pick',it[2],v['name'],'b-worth'))
    mos='<div class="mosaic prod" aria-hidden="true">'+''.join(f'<img src="{e(VER[a]["img"])}" alt="">' for a in hero[:3])+'</div>'
    ex=''.join(f'<li><span class="badge b-{k}">{BADGE_LABEL[k]}</span><p>{t}</p></li>' for k,t in (('premium','One of the highest-end picks in its Top 10.'),('bang','A mid-priced Amazon Best Seller from the Top 10.'),('value','The lowest-priced pick in the Top 10 that is still well rated on Amazon.')))
    m=f'''<section class="hero">{NOTE}<div><p class="kicker">Value Picks</p><h1>Worth it at<br><em>every budget.</em></h1><p class="sub">Three standout picks from each Top 10, one premium, one mid-priced and one budget, plus the value pick from every other list.</p></div>{mos}</section>
<ul class="explain">{ex}</ul>
{"".join(bands)}
<section class="sec more-sec"><div class="sec-h"><div><h2>More value picks</h2><p>In every top 10 the middle label is the value pick: the cheaper one that still does the job. It is not the cheapest item in the category. It is the one we would buy if the top pick costs more than the job is worth.</p></div></div><div class="grid">{"".join(more)}</div></section>'''
    return hub('value','Value Picks — The Worth Guide','Premium Pick, Bang for the Buck and Value Pick from each Worth Guide Top 10, plus the value pick from every other list.',m)
PRIVACY_UPDATED='October 4, 2026'
def build_privacy():
    fam=', '.join(f'{s[1]}Worth ({s[0]}.theworthguide.com)' for s in SITES)
    sec=lambda i,h,b:f'<section id="{i}"><h2>{h}</h2>{b}</section>'
    body=''.join((
    sec('short','The short version','''<ul>
<li>There are no accounts, sign-ups, comment boxes or forms on our sites. We don't ask for your name, email, phone number or address, and we don't collect personal information from you directly.</li>
<li>Product links go to Amazon and carry our affiliate tag. Once you're on Amazon, Amazon's own privacy notice applies, and Amazon may set cookies.</li>
<li>Our hub and category pages run no analytics and set no cookies. A few subsites use Vercel Web Analytics, which counts visits without cookies.</li>
<li>We don't sell, rent or share personal information. We don't have any to sell.</li></ul>'''),
    sec('covers','What this policy covers',f'<p>This policy covers theworthguide.com, every theworthguide.com subdomain ({fam}), and The Worth Guide&#39;s related Pinterest, YouTube and TikTok accounts. &ldquo;We&rdquo;, &ldquo;us&rdquo; and &ldquo;our&rdquo; mean The Worth Guide.</p>'),
    sec('collect','What we collect','''<p>We don't collect personal information directly. You can read every page without an account, and there is nothing to fill in: no sign-up, no newsletter, no contact form, no comments, no checkout. We never see what you buy on Amazon under your name.</p>
<p>Like any website, our pages are delivered by a hosting provider. Ours is <a href="https://vercel.com/legal/privacy-policy" rel="noopener" target="_blank">Vercel</a>, which processes standard request data such as your IP address, browser type and the page requested in order to serve the site and keep it secure, and may keep short-lived server logs under its own privacy policy. We don't use those logs to identify anyone.</p>'''),
    sec('cookies','Analytics and cookies','''<p><strong>Hub and category pages.</strong> theworthguide.com and the category subsites built with it (KitchenWorth, CleanWorth, ToolWorth, YardWorth, BagWorth, GroomWorth, FitWorth, BathWorth, TravelWorth and WatchWorth) load no analytics or tracking scripts and set no cookies. The only script on them opens the mobile menu.</p>
<p><strong>Some subsites.</strong> A few subsites, such as DeskWorth, BrewWorth, SleepWorth and PetWorth, use <a href="https://vercel.com/docs/analytics/privacy-policy" rel="noopener" target="_blank">Vercel Web Analytics</a> to count page views and clicks on &ldquo;Check price on Amazon&rdquo; buttons. It does not use cookies. It reports aggregate numbers such as pages viewed, the referring site, country, and device and browser type, and Vercel says it identifies a visit only with a hash of the request that resets daily, so it can't follow you across sites or over time.</p>
<p><strong>Fonts.</strong> Our pages load typefaces from <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">Google Fonts</a>, so your browser sends Google a standard request, including your IP address, when it downloads them. We don't set any cookies through Google Fonts.</p>
<p>We don't use advertising cookies, retargeting pixels or social media tracking pixels on our sites.</p>'''),
    sec('amazon','Amazon links and our affiliate tag','''<p>When you click a product link or a &ldquo;Check price on Amazon&rdquo; button, you leave our site for Amazon.com. Those links include our Amazon Associates tracking tag so that Amazon can credit us if you buy something. Amazon may set cookies in your browser to do this and for its own purposes. That happens on Amazon, under the Amazon.com Privacy Notice (linked at the bottom of every Amazon page), not under this policy.</p>
<p>Amazon gives us aggregate reports, such as which items were ordered through our links and the commission earned. Those reports don't include your name, address, payment details or account information.</p>'''),
    sec('disclosure','Amazon Associate disclosure','''<p>The Worth Guide is a participant in the Amazon Services LLC Associates Program, an affiliate advertising program designed to provide a means for sites to earn advertising fees by advertising and linking to Amazon.com. As an Amazon Associate, The Worth Guide earns from qualifying purchases. This costs you nothing extra and doesn't change which products we pick.</p>'''),
    sec('social','Pinterest, YouTube and TikTok','''<p>We post guides and product videos on Pinterest, YouTube and TikTok. When you view, like, save, comment on or follow our posts there, that activity is handled by each platform under its own privacy policy: <a href="https://policy.pinterest.com/privacy-policy" rel="noopener" target="_blank">Pinterest</a>, <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">YouTube (Google)</a> and <a href="https://www.tiktok.com/legal/privacy-policy" rel="noopener" target="_blank">TikTok</a>.</p>
<p><strong>Pinterest API.</strong> We may use Pinterest's API, signed in to our own Pinterest account only, to publish pins to our own boards and to read performance stats (such as impressions, saves and outbound clicks) on our own pins. We use it only to manage our own content and see how it performs. We don't use it to collect personal information about the people who see or save our pins, and we don't sell or share anything it returns. The access keys for our account are kept private and used for nothing else.</p>
<p>Any stats we look at on YouTube and TikTok are the aggregate numbers those platforms show every account owner, such as views and watch time.</p>'''),
    sec('sharing','Selling and sharing','''<p>We don't sell, rent or trade personal information, and we don't share it with advertisers or data brokers. Because we don't collect it in the first place, there is nothing for us to hand over.</p>'''),
    sec('choices','Your choices','''<p>You can block or delete cookies, including Amazon's, in your browser settings, and you can use private browsing or a content blocker. Our sites work the same either way. For anything about your Amazon account, orders or Amazon's cookies, use Amazon's own privacy settings.</p>'''),
    sec('children',"Children's privacy",'''<p>Our sites and social accounts are meant for adults shopping for themselves and aren't directed at children under 13. We don't knowingly collect personal information from children.</p>'''),
    sec('changes','Changes to this policy',f'<p>If what we do changes, for example if we add a new analytics tool, we&#39;ll update this page and the &ldquo;Last updated&rdquo; date below. Changes take effect when they&#39;re posted here.</p><p class="updated">Last updated {PRIVACY_UPDATED}</p>'),
    ))
    m=f'''<section class="hero solo">{NOTE}<div><p class="kicker">Privacy</p><h1>Privacy policy.<br><em>Plain and short.</em></h1><p class="sub">We don't run accounts or forms, and we don't collect personal information. Here is exactly what does happen when you visit.</p><ul class="stats"><li>Last updated {PRIVACY_UPDATED}</li><li>No accounts · No forms</li></ul></div></section>
<article class="band prose">{body}</article>'''
    return hub('privacy','Privacy Policy — The Worth Guide','How The Worth Guide handles privacy: no accounts or forms, no personal information collected, Amazon affiliate links, and the analytics and cookies our sites actually use.',m,'<meta name="robots" content="noindex">\n',PROSE_CSS)
LINKS_CSS=open(os.path.join(ROOT,'_src/links.css')).read()
LINKS_ETSY='https://www.etsy.com/shop/KettleAndKibbleCo'  # Tyler's Etsy shop (KettleAndKibbleCo); see /workspace/etsy/shop/shop-home.png
LINKS_DISC='As an Amazon Associate we earn from qualifying purchases.'
# Top 10 categories that have Gift Finds Daily videos, in this order: (subdomain key, label, emoji). pet = PetWorth (pet.theworthguide.com).
LINKS_CATS=[('kitchen','Kitchen','🍳'),('tool','Tools','🛠️'),('clean','Cleaning','🧽'),('fit','Fitness','🏋️'),('travel','Travel','✈️'),('pet','Pets','🐾'),
            ('bath','Bath','🛁'),('bag','Bags','🎒'),('yard','Yard','🌿'),('groom','Grooming','🪒'),('watch','Watches','⌚')]
def build_links():
    """/links: standalone link-in-bio page for the 'Gift Finds Daily' social account (@gift_finds_daily on Instagram/TikTok).
    Own look (coral/teal/cream, _src/links.css), NOT in the hub nav, header or footer and not linked from any site page; listed in sitemap.xml."""
    star=lambda: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c.7 6.4 3.6 9.6 12 12-8.4 2.4-11.3 5.6-12 12-.7-6.4-3.6-9.6-12-12C8.4 9.6 11.3 6.4 12 0Z"/></svg>'
    arrow='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
    n=len(LINKS_CATS); odd=n%2
    def tile(i,k,lab,ic):
        w=odd and i==n-1
        return (f'<a class="tile press{" wide" if w else ""}" href="{sub(k)}"><span class="ic" aria-hidden="true">{ic}</span>'
                f'<span class="t"><b>{e(lab)}</b><small>Top 10 picks</small></span>'+(f'<span class="arr2" aria-hidden="true">{arrow}</span>' if w else '')+'</a>')
    tiles='\n'.join(tile(i,*c) for i,c in enumerate(LINKS_CATS))
    title='Gift Finds Daily'; desc='Gift ideas + top picks worth buying 🎁'
    img=f'{HUB}/img/links/gift_finds_daily_pfp.png'
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} — gift ideas + top picks</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{HUB}/links">
<meta name="theme-color" content="#F9604E">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{HUB}/links"><meta property="og:image" content="{img}"><meta name="twitter:card" content="summary">
<link rel="icon" type="image/png" sizes="48x48" href="/img/links/icon-48.png"><link rel="apple-touch-icon" href="/img/links/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,800,100,1;1,9..144,700,100,1&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="/img/links/pfp-320.webp">
<style>{LINKS_CSS}</style></head><body>
<main class="page">
<div class="band" aria-hidden="true"><span class="deco s1">{star()}</span><span class="deco s2">{star()}</span><span class="deco s3">{star()}</span><span class="deco s4">{star()}</span><span class="deco d1"></span><span class="deco d2"></span><span class="deco d3"></span><span class="deco d4"></span></div>
<svg class="wave" viewBox="0 0 480 60" preserveAspectRatio="none" aria-hidden="true"><path fill="currentColor" d="M0 30C60 6 120 6 180 22s120 34 180 22 90-30 120-34V60H0Z"/></svg>
<header class="prof">
<span class="av"><img src="/img/links/pfp-320.webp" alt="Gift Finds Daily logo: a cream gift box with a teal ribbon" width="320" height="320"><span class="gift" aria-hidden="true">🎁</span></span>
<h1>Gift Finds <em>Daily</em></h1>
<span class="handle"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="12" cy="12" r="4"/><path d="M16 8v5a3 3 0 0 0 6 0v-1a10 10 0 1 0-4 8"/></svg>gift_finds_daily</span>
<p class="bio">{desc}</p>
</header>
<nav class="links" aria-label="Links">
<a class="feat press" href="{LINKS_ETSY}" rel="noopener"><img src="/img/links/kettle-kibble-160.webp" alt="" width="64" height="64"><span class="t"><span class="tag">Featured shop</span><b>Dog breed sweatshirts &amp; mugs 🐶</b><small>KettleAndKibbleCo on Etsy</small></span><span class="arr" aria-hidden="true">{arrow}</span></a>
<div class="sec"><span class="spark" aria-hidden="true">{star()}</span><h2><span class="k">Shop by category</span>Top 10 picks</h2><span class="rule" aria-hidden="true"></span></div>
<div class="grid">
{tiles}
</div>
<a class="all press" href="{HUB}"><span class="e" aria-hidden="true">📚</span>All guides<span aria-hidden="true">{arrow}</span></a>
</nav>
<footer class="foot"><span class="bow" aria-hidden="true">{star()}{star()}{star()}</span><p class="disc">{LINKS_DISC}</p></footer>
</main>
</body></html>
'''
def main():
    for c,v in CATS.items():
        d=os.path.join(ROOT,'c',c); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,'index.html'),'w').write(page(c,v))
        open(os.path.join(d,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://{c}.theworthguide.com/</loc><lastmod>{LASTMOD}</lastmod></url>\n</urlset>\n')
        open(os.path.join(d,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: https://{c}.theworthguide.com/sitemap.xml\n')
    for f,fn in (('index.html',build_index),('guides.html',build_guides),('value.html',build_value),('categories.html',build_categories),('privacy.html',build_privacy),('links.html',build_links)):
        open(os.path.join(ROOT,f),'w').write(fn())
    validate()
def validate():
    err=[]
    for f in os.popen(f'find {ROOT} -name "*.html" -not -path "*/node_modules/*" -not -path "*/.git/*"').read().split():
        h=open(f).read(); rel=os.path.relpath(f,ROOT)
        m=re.match(r'c/(\w+)/index\.html',rel); want=TAGS[m.group(1)] if m else 'theworthguide20-20'
        tags=re.findall(r'amazon\.com/[^"]*?[?&]tag=([\w-]+)',h)
        amz=re.findall(r'href="https?://(?:www\.)?amazon\.com[^"]*"',h)
        if len(tags)!=len(amz): err.append(f'{rel}: amazon link without tag')
        if any(t!=want for t in tags): err.append(f'{rel}: wrong tag {set(tags)}')
        if 'theworthguide-20' in h: err.append(f'{rel}: old tag')
        if re.search(r'mailto:|@theworthguide\.com',h): err.append(f'{rel}: email')
        if rel!='links.html' and re.search(r'href="(?:https://theworthguide\.com)?/links\b',h): err.append(f'{rel}: links to /links (must stay unlinked)')
        if rel=='links.html':  # standalone social page without the hub chrome: its own rules
            if h.count(LINKS_DISC)!=1: err.append(f'{rel}: disclosure count')
            if LINKS_ETSY not in h: err.append(f'{rel}: Etsy shop link')
            if '$' in re.sub(r'<style>.*?</style>','',h,flags=re.S): err.append(f'{rel}: price shown')
            continue
        if re.search(r'href="[^"]*about',h,re.I): err.append(f'{rel}: about link')
        if 'subscribe' in h.lower(): err.append(f'{rel}: subscribe')
        if h.count('As an Amazon Associate I earn from qualifying purchases.')!=1: err.append(f'{rel}: disclosure count')
        if h.count('class="disc"')!=1: err.append(f'{rel}: commission line count')
        if m:
            n=h.count('<article class="row">'); a=re.findall(r'<article class="row">.*?dp/(\w+)',h)
            if n!=10 or len(set(a))!=10: err.append(f'{rel}: top10 count {n}/{len(set(a))}')
            pk=re.findall(r'<article class="pick">.*?dp/(\w+)',h)
            want_pk=3 if BADGES.get(m.group(1),{}).get('picks') else 0
            if len(pk)!=want_pk or len(set(pk))!=want_pk or not set(pk)<=set(a): err.append(f'{rel}: badge picks {pk}')
        if '$' in re.sub(r'<style>.*?</style>','',h,flags=re.S): err.append(f'{rel}: price shown')
        if 'We may earn a commission from qualifying purchases.' not in h: err.append(f'{rel}: top commission note')
    for c in CATS:
        for x in ('index.html','sitemap.xml','robots.txt'):
            if not os.path.exists(os.path.join(ROOT,'c',c,x)): err.append(f'missing c/{c}/{x}')
    json.load(open(os.path.join(ROOT,'vercel.json')))
    if '<loc>https://theworthguide.com/links</loc>' not in open(os.path.join(ROOT,'sitemap.xml')).read(): err.append('sitemap.xml: /links missing')
    if err: print('\n'.join(err)); sys.exit(1)
    print('build ok:',len(CATS),'category pages, 10 picks each;',sum(1 for c in CATS if BADGES.get(c,{}).get('picks')),'with 3 badge picks')
if __name__=='__main__': main()
