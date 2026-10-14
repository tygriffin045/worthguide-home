#!/usr/bin/env python3
"""check.py MODE BASE: MODE=vcurl (protected preview via `vercel curl`) or http. Checks every sitemap URL:
200, 0 dollar amounts in visible text, canonical == sitemap URL, exactly one disclosure. Never requests amazon."""
import re,sys,subprocess,urllib.request,concurrent.futures as cf
from urllib.parse import urlparse
mode,base=sys.argv[1],sys.argv[2].rstrip("/")
DOM="https://car.theworthguide.com"
def get(path):
    assert "amazon" not in base
    if mode=="vcurl":
        r=subprocess.run(["vercel","curl",path,"--deployment",base,"--scope","theateam20","--","-s","-w","\n__ST%{http_code}"],capture_output=True,text=True,cwd=__import__("os").environ["CWD"])
        o=r.stdout; m=re.search(r"\n__ST(\d+)$",o); return (int(m.group(1)) if m else 0),o[:m.start()] if m else o
    for i in range(4):
        try:
            x=urllib.request.urlopen(base+path,timeout=60); return x.status,x.read().decode()
        except urllib.error.HTTPError as e: return e.code,""
        except Exception:
            if i==3: return 0,""
            __import__("time").sleep(3)
st,sm=get("/sitemap.xml"); urls=re.findall(r"<loc>([^<]+)</loc>",sm)
assert st==200 and urls,(st,sm[:200])
DOL=re.compile(r"\$\s?\d[\d,]*(?:\.\d\d)?")
def chk(u):
    path=urlparse(u).path or "/"; st,b=get(path)
    c=re.findall(r'<link rel="canonical" href="([^"]+)"',b)
    t=re.sub(r"<[^>]+>"," ",re.sub(r"<script.*?</script>|<style.*?</style>"," ",b,flags=re.S))
    return u,st,c,len(DOL.findall(t)),t.count("we have not tested them hands-on")
bad=0
with cf.ThreadPoolExecutor(3) as ex:
    for u,st,c,d,disc in ex.map(chk,urls):
        ok= st==200 and c==[u] and d==0 and disc==1
        bad+= not ok
        print(("OK  " if ok else "BAD ")+f"{st} canon={c} dollars={d} disclosures={disc} {u}")
print(f"{len(urls)} URLs, {bad} bad"); sys.exit(1 if bad else 0)
