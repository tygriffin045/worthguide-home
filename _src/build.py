#!/usr/bin/env python3
"""Generate category pages for <cat>.theworthguide.com and validate the hub. Run: python3 _src/build.py"""
import json,os,re,sys,html
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,'_src'))
from data import CATS,TAGS
VER=json.load(open(os.path.join(ROOT,'_src/verified.json')))
CSS=open(os.path.join(ROOT,'_src/cat.css')).read()
HUB='https://theworthguide.com'
LASTMOD='2026-10-03'
e=lambda s:html.escape(s,quote=True)
MARK='<svg class="mark" viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="16" r="14" fill="#c4a15a"/><path d="M9.5 16.4 13.8 20.6 22.4 11.4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FOOTER='<footer><div class="wrap"><p class="disc" style="font-size:.8rem;margin:0 0 6px">We earn a small commission when you buy through links on this site. As an Amazon Associate I earn from qualifying purchases.</p>© 2026 The Worth Guide</div></footer>'
def link(asin,tag): return f'https://www.amazon.com/dp/{asin}?tag={tag}'
def page(c,v):
    tag=TAGS[c]; rows=[]
    for i,(a,name,blurb,labels,bs) in enumerate(v['items'],1):
        img=VER[a]['img']
        t=''.join(f'<span class="tag">{e(l)}</span>' for l in labels)
        rows.append(f'<article class="row"><img src="{e(img)}" alt="{e(name)}" loading="lazy"><div><div class="tags">{t}</div><h2 style="font-family:Cormorant Garamond,Georgia,serif;font-size:1.6rem;margin:0">#{i} {e(name)}</h2><p>{e(blurb)}</p><p><a href="{link(a,tag)}" rel="nofollow sponsored noopener" target="_blank">Check price on Amazon →</a></p></div></article>')
    a1,n1,a2,n2,txt,table=v['vs']
    vsimg=lambda a:f'<img src="{e(VER[a]["img"])}" alt="" loading="lazy" style="width:100%;height:140px;object-fit:contain;background:#f3eee6">'
    lab=lambda a:next(x[3][0] for x in v['items'] if x[0]==a)
    trs=''.join(f'<tr><th>{e(r[0])}</th><td>{e(r[1])}</td><td>{e(r[2])}</td></tr>' for r in table)
    url=f'https://{c}.theworthguide.com/'
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{v["name"]} Top 10 — The Worth Guide</title>
<meta name="description" content="{e(v["name"]+": "+v["lede"])}">
<link rel="canonical" href="{url}">
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Source+Sans+3:wght@400;500;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header><div class="wrap bar">
  <a class="brand" href="{HUB}/">{MARK}The Worth Guide</a>
  <nav>
    <a href="{HUB}/guides">Guides</a>
    <a href="{HUB}/value">Value Picks</a>
    <a href="{HUB}/categories">Categories</a>
  </nav>
</div></header>
<main class="wrap page">
<p class="kicker">TOP 10</p>
<h1>{v["name"]}</h1>
<p>{e(v["lede"])}</p>
<div class="list">{"".join(rows)}</div>
<h2 style="font-family:Cormorant Garamond,Georgia,serif;font-size:2.4rem;margin-top:42px">Vs review</h2>
<p>{e(txt)}</p>
<div class="vs"><a href="{link(a1,tag)}" rel="nofollow sponsored noopener" target="_blank">{vsimg(a1)}<h3>{e(n1)}</h3><p>{e(lab(a1))}</p></a>
<a href="{link(a2,tag)}" rel="nofollow sponsored noopener" target="_blank">{vsimg(a2)}<h3>{e(n2)}</h3><p>{e(lab(a2))}</p></a></div>
<table><tbody>{trs}</tbody></table>
<p><a href="{HUB}/">← All guides</a></p>
</main>
{FOOTER}
</body></html>
'''
def main():
    for c,v in CATS.items():
        d=os.path.join(ROOT,'c',c); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,'index.html'),'w').write(page(c,v))
        open(os.path.join(d,'sitemap.xml'),'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>https://{c}.theworthguide.com/</loc><lastmod>{LASTMOD}</lastmod></url>\n</urlset>\n')
        open(os.path.join(d,'robots.txt'),'w').write(f'User-agent: *\nAllow: /\n\nSitemap: https://{c}.theworthguide.com/sitemap.xml\n')
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
        if re.search(r'href="[^"]*about',h,re.I): err.append(f'{rel}: about link')
        if 'subscribe' in h.lower(): err.append(f'{rel}: subscribe')
        if h.count('As an Amazon Associate I earn from qualifying purchases.')!=1: err.append(f'{rel}: disclosure count')
        if h.count('class="disc"')!=1: err.append(f'{rel}: commission line count')
        if m:
            n=h.count('<article class="row">'); a=re.findall(r'<article class="row">.*?dp/(\w+)',h)
            if n!=10 or len(set(a))!=10: err.append(f'{rel}: top10 count {n}/{len(set(a))}')
    for c in CATS:
        for x in ('index.html','sitemap.xml','robots.txt'):
            if not os.path.exists(os.path.join(ROOT,'c',c,x)): err.append(f'missing c/{c}/{x}')
    json.load(open(os.path.join(ROOT,'vercel.json')))
    if err: print('\n'.join(err)); sys.exit(1)
    print('build ok:',len(CATS),'category pages, 10 picks each')
if __name__=='__main__': main()
