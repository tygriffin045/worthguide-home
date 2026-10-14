import sys
from playwright.sync_api import sync_playwright
url=sys.argv[1]; anchor=sys.argv[2] if len(sys.argv)>2 else ''
J="(()=>{const b=document.querySelector('[data-sticky-cta]');if(!b)return 'nobar';const r=b.getBoundingClientRect();const cs=getComputedStyle(b);return {top:Math.round(r.top),h:Math.round(r.height),vh:innerHeight,visiblePx:Math.max(0,innerHeight-Math.round(r.top)),transform:cs.transform,translate:cs.translate,bottom:cs.bottom,bodyPad:getComputedStyle(document.body).paddingBottom,label:(b.querySelector('p')||{}).textContent}})()"
with sync_playwright() as p:
  for w,h in [(390,844),(1366,768)]:
    pg=p.chromium.launch().new_page(viewport={'width':w,'height':h}); pg.goto(url,wait_until='networkidle'); pg.wait_for_timeout(800)
    print(w,'load',pg.evaluate(J))
    if anchor:
      pg.evaluate(f"(()=>{{const e=document.getElementById('{anchor}')||document.querySelector('{anchor}');const s=e.closest('section')||e;scrollTo(0,s.getBoundingClientRect().bottom+scrollY+40)}})()"); pg.wait_for_timeout(600); print(w,'pastQP',pg.evaluate(J))
    else:
      pg.evaluate("scrollTo(0,600)"); pg.wait_for_timeout(600); print(w,'mid',pg.evaluate(J))
    pg.evaluate("scrollTo(0,document.body.scrollHeight)"); pg.wait_for_timeout(600); print(w,'footer',pg.evaluate(J))
