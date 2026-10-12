#!/usr/bin/env python3
"""Crawl all WorthGuide sitemaps (hub + hub c/ category hosts + subsites) and verify
200 / self-canonical / noindex / lastmod / duplicates / robots / internal links / etsy text.
Never requests amazon (only *.theworthguide.com URLs are fetched)."""
import re, sys, time, subprocess, datetime, concurrent.futures as cf
from urllib.parse import urljoin, urlparse, urldefrag
import urllib.request, urllib.error, ssl
from zoneinfo import ZoneInfo
ET = ZoneInfo("America/New_York")
UA = "WorthGuideCrawler/2.0"
HUB = "https://theworthguide.com"
SUBS = ["brew", "car", "desk", "pet", "sleep", "tech"]
REPOS = {"hub": "/workspace/hub", **{s: f"/workspace/top10/{s}worth" for s in SUBS}}
ETSY = re.compile(r"etsy\.com|kettle\s*(?:&amp;|&|and)?\s*kibble", re.I)
DOLLAR = re.compile(r"\$\s?\d[\d,]*(?:\.\d\d)?")
LASTMOD = re.compile(r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?(\.\d+)?(Z|[+-]\d{2}:\d{2}))?$")

class NoRedir(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
OPENER = urllib.request.build_opener(NoRedir)

def allowed(u):
    h = (urlparse(u).hostname or "").lower()
    return (h == "theworthguide.com" or h.endswith(".theworthguide.com")) and "amazon" not in h

def fetch(u, method="GET"):
    if not allowed(u): raise ValueError("refusing non-WorthGuide host: " + u)
    req = urllib.request.Request(u, headers={"User-Agent": UA}, method=method)
    for attempt in range(3):
        try:
            r = OPENER.open(req, timeout=30)
            return r.status, dict(r.headers), r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e:
            return e.code, dict(e.headers), ""
        except Exception as e:
            err = str(e); time.sleep(1 + attempt)
    return 0, {}, err

def now(): return datetime.datetime.now(ET).strftime("%Y-%m-%d %H:%M:%S %Z")

def discover():
    sm = [HUB + "/sitemap.xml"]
    st, _, body = fetch(HUB + "/robots.txt")
    for m in re.findall(r"(?im)^sitemap:\s*(\S+)", body):
        if m not in sm: sm.append(m)
    import os
    cats = sorted(d for d in os.listdir("/workspace/hub/c") if os.path.isdir(f"/workspace/hub/c/{d}"))
    hosts = [f"https://{c}.theworthguide.com" for c in cats] + [f"https://{s}.theworthguide.com" for s in SUBS]
    for h in hosts:
        sm.append(h + "/sitemap.xml")
    return sm

def parse_sitemap(u):
    st, _, body = fetch(u)
    if st != 200: return st, [], []
    if "<sitemapindex" in body:
        locs, lms = [], []
        for child in re.findall(r"<loc>\s*(.*?)\s*</loc>", body):
            _, a, b = parse_sitemap(child); locs += a; lms += b
        return st, locs, lms
    entries = re.findall(r"<url>(.*?)</url>", body, re.S)
    locs, lms = [], []
    for e in entries:
        l = re.search(r"<loc>\s*(.*?)\s*</loc>", e); m = re.search(r"<lastmod>\s*(.*?)\s*</lastmod>", e)
        locs.append(l.group(1).replace("&amp;", "&") if l else ""); lms.append(m.group(1) if m else None)
    return st, locs, lms

def norm(u):
    p = urlparse(u); path = p.path or "/"
    return f"{p.scheme}://{p.netloc.lower()}{path}"

def canon_ok(c, u):
    if c is None: return False
    if c == u: return True
    pc, pu = urlparse(c), urlparse(u)
    return (pu.path in ("", "/") and pc.path in ("", "/") and pc.netloc == pu.netloc and pc.scheme == pu.scheme)

def check_page(u):
    st, h, body = fetch(u)
    r = {"url": u, "status": st, "loc": h.get("Location") or h.get("location")}
    if st != 200: return r
    m = re.search(r"<link[^>]+rel=[\"']canonical[\"'][^>]*>", body, re.I)
    c = None
    if m:
        hm = re.search(r"href=[\"']([^\"']+)", m.group(0)); c = hm.group(1) if hm else None
    r["canonical"] = c
    r["canon_ok"] = canon_ok(c, u)
    xr = (h.get("X-Robots-Tag") or h.get("x-robots-tag") or "")
    meta = re.findall(r"<meta[^>]+name=[\"'](?:robots|googlebot)[\"'][^>]*>", body, re.I)
    r["noindex"] = "noindex" in xr.lower() or any("noindex" in x.lower() for x in meta)
    r["etsy"] = sorted(set(x.group(0) for x in ETSY.finditer(body)))
    text = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    r["dollars"] = len(DOLLAR.findall(text))
    links = set()
    for href in [a or b for a, b in re.findall(r"<a\b[^>]*?\bhref\s*=\s*(?:[\"']([^\"'#][^\"']*)[\"']|([^\s>\"'#]+))", body, re.I | re.S)]:
        a = urldefrag(urljoin(u, href.replace("&amp;", "&")))[0]
        if a.startswith("http") and allowed(a): links.add(a)
    r["links"] = links
    return r

def git_sha(p):
    try: return subprocess.run(["git", "-C", p, "rev-parse", "--short", "HEAD"], capture_output=True, text=True, timeout=10).stdout.strip() or "?"
    except Exception: return "?"
def git_origin(p):
    try: return subprocess.run(["git", "-C", p, "rev-parse", "--short", "origin/main"], capture_output=True, text=True, timeout=10).stdout.strip() or "?"
    except Exception: return "?"

def vercel_refs():
    out = []
    for name in ["worthguide-home"] + [f"{s}worth" for s in SUBS]:
        try:
            p = subprocess.run(["vercel", "ls", name, "--prod", "--yes"], capture_output=True, text=True, timeout=60)
            urls = re.findall(r"https://\S+\.vercel\.app", p.stdout + p.stderr)
            lines = [l.strip() for l in (p.stdout).splitlines() if "Ready" in l or "Error" in l]
            out.append(f"  {name}: latest prod {urls[0] if urls else '(none parsed)'}" + (f" | {lines[0][:90]}" if lines else ""))
        except Exception as e:
            out.append(f"  {name}: vercel ls failed ({e})")
    return out

def main():
    t0 = time.time(); fails = []
    print(f"=== WorthGuide sitemap crawl — start {now()} ===")
    print("Repo SHAs (HEAD / origin/main):")
    for k, p in REPOS.items(): print(f"  {k}: {git_sha(p)} / {git_origin(p)}  ({p})")
    print("Vercel production refs:"); [print(l) for l in vercel_refs()]
    sitemaps = discover()
    print(f"Sitemaps discovered: {len(sitemaps)}")
    allurls = []; per_site = {}
    for sm in sitemaps:
        st, locs, lms = parse_sitemap(sm)
        host = urlparse(sm).netloc
        bad_lm = sum(1 for x in lms if x is None or not LASTMOD.match(x))
        missing_lm = sum(1 for x in lms if x is None)
        dups = len(locs) - len(set(locs))
        print(f"  {sm}: HTTP {st}, {len(locs)} URLs, lastmod missing {missing_lm}, invalid {bad_lm - missing_lm}, dup locs {dups}")
        if st != 200: fails.append(f"sitemap {sm} HTTP {st}")
        if dups: fails.append(f"sitemap {sm} has {dups} duplicate locs")
        if bad_lm - missing_lm: fails.append(f"sitemap {sm} has invalid lastmod")
        per_site[host] = locs; allurls += locs
    # robots per host
    print("robots.txt per host:")
    for host in per_site:
        st, _, body = fetch(f"https://{host}/robots.txt")
        dis = [l for l in body.splitlines() if re.match(r"(?i)disallow:\s*/\s*$", l)]
        smref = re.findall(r"(?im)^sitemap:\s*(\S+)", body)
        print(f"  {host}: HTTP {st}, Disallow-all {'YES' if dis else 'no'}, Sitemap refs {smref}")
        if st != 200 or dis: fails.append(f"robots {host} HTTP {st} disallow-all={bool(dis)}")
    xdup = len(allurls) - len(set(allurls))
    if xdup: fails.append(f"{xdup} URLs duplicated across sitemaps")
    uniq = list(dict.fromkeys(allurls))
    with cf.ThreadPoolExecutor(16) as ex: res = list(ex.map(check_page, uniq))
    non200 = [r for r in res if r["status"] != 200]
    ok = [r for r in res if r["status"] == 200]
    canon_bad = [r for r in ok if not r["canon_ok"]]
    noidx = [r for r in ok if r["noindex"]]
    etsy = [r for r in ok if r["etsy"]]
    sm_set = set(uniq)
    links = set().union(*[r["links"] for r in ok]) if ok else set()
    to_check = sorted(links)
    def lchk(u):
        st, h, body = fetch(u)
        hits = sorted(set(x.group(0) for x in ETSY.finditer(body))) if (st == 200 and u not in sm_set) else []
        return u, st, h.get("Location") or h.get("location"), hits
    with cf.ThreadPoolExecutor(16) as ex: lres = list(ex.map(lchk, to_check))
    bad_links = [(u, s, l) for u, s, l, _ in lres if s != 200]
    nonsm = [x for x in lres if x[0] not in sm_set]
    for u, s, l, hits in nonsm:
        if hits: etsy.append({"url": u, "etsy": hits})
    print(f"\nPages checked: {len(res)}")
    for r in non200: print(f"  NON-200 {r['status']} {r['url']} -> {r.get('loc')}")
    for r in canon_bad: print(f"  CANONICAL MISMATCH {r['url']} canonical={r['canonical']}")
    for r in noidx: print(f"  NOINDEX {r['url']}")
    print(f"Unique internal links found on sitemap pages: {len(to_check)} (all fetched, no redirect follow); "
          f"{len(nonsm)} are not in any sitemap and were also text-searched for Etsy/KettleAndKibble")
    for u, s, l in bad_links: print(f"  BAD INTERNAL LINK {s} {u} -> {l}")
    for r in etsy: print(f"  ETSY/KK HIT {r['url']}: {r['etsy']}")
    print("Dollar amounts in visible text per site (info only):")
    for host, locs in per_site.items():
        d = sum(r.get("dollars", 0) for r in ok if urlparse(r["url"]).netloc == host)
        print(f"  {host}: {d}")
    fails += [f"non200 {len(non200)}"] * bool(non200) + [f"canon {len(canon_bad)}"] * bool(canon_bad) \
        + [f"noindex {len(noidx)}"] * bool(noidx) + [f"etsy {len(etsy)}"] * bool(etsy) + [f"badlinks {len(bad_links)}"] * bool(bad_links)
    code = 1 if fails else 0
    print(f"\nSUMMARY: sitemaps={len(sitemaps)} urls={len(allurls)} unique={len(uniq)} non200={len(non200)} "
          f"canonical_mismatch={len(canon_bad)} noindex={len(noidx)} etsy_kk_hits={len(etsy)} "
          f"cross_sitemap_dups={xdup} internal_links_checked={len(to_check)} non_sitemap_internal={len(nonsm)} bad_internal_links={len(bad_links)}")
    if fails: print("FAILURES:", "; ".join(fails))
    print(f"=== end {now()} — runtime {time.time()-t0:.1f}s — exit code {code} ===")
    return code

if __name__ == "__main__": sys.exit(main())
