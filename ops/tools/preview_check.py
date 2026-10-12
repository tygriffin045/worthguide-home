#!/usr/bin/env python3
"""Usage: preview_check.py BASE_URL  — fetch every desk.theworthguide.com sitemap path on BASE_URL;
require 200 (no redirect), 0 dollar amounts in visible text, canonical on desk.theworthguide.com. Never requests amazon."""
import re, sys, time, datetime, concurrent.futures as cf, urllib.request, urllib.error
from urllib.parse import urlparse
from zoneinfo import ZoneInfo
ET = ZoneInfo("America/New_York")
class NR(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k): return None
OP = urllib.request.build_opener(NR)
def get(u):
    h = urlparse(u).hostname or ""
    assert "amazon" not in h
    for i in range(3):
        try:
            r = OP.open(urllib.request.Request(u, headers={"User-Agent": "DeskPreviewCheck/2"}), timeout=30)
            return r.status, r.read().decode("utf-8", "replace")
        except urllib.error.HTTPError as e: return e.code, ""
        except Exception: time.sleep(1 + i)
    return 0, ""
DOL = re.compile(r"\$\s?\d[\d,]*(?:\.\d\d)?")
def chk(base, path):
    st, b = get(base + path)
    if st != 200: return path, st, None, 0
    m = re.search(r"<link[^>]+rel=[\"']canonical[\"'][^>]*href=[\"']([^\"']+)", b, re.I) or \
        re.search(r"<link[^>]+href=[\"']([^\"']+)[^>]*rel=[\"']canonical", b, re.I)
    t = re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>", " ", b, flags=re.S | re.I))
    return path, st, m.group(1) if m else None, len(DOL.findall(t))
def main():
    base = sys.argv[1].rstrip("/"); t0 = time.time()
    print(f"=== desk preview check {base} — start {datetime.datetime.now(ET):%Y-%m-%d %H:%M:%S %Z} ===")
    st, sm = get(base + "/sitemap.xml")
    if st != 200: st, sm = get("https://desk.theworthguide.com/sitemap.xml")
    paths = [urlparse(l).path or "/" for l in re.findall(r"<loc>\s*(.*?)\s*</loc>", sm)]
    with cf.ThreadPoolExecutor(16) as ex: res = list(ex.map(lambda p: chk(base, p), paths))
    bad = [r for r in res if r[1] != 200]; dol = [r for r in res if r[3]]
    can = [r for r in res if r[1] == 200 and (r[2] or "") .rstrip("/") != ("https://desk.theworthguide.com" + r[0]).rstrip("/")]
    for r in bad: print("NON-200", r[1], r[0])
    for r in dol: print("DOLLARS", r[3], r[0])
    for r in can: print("CANONICAL", r[0], r[2])
    code = 1 if (bad or dol or can or not paths) else 0
    print(f"SUMMARY: pages={len(paths)} non200={len(bad)} pages_with_dollars={len(dol)} canonical_not_desk={len(can)}")
    print(f"=== end {datetime.datetime.now(ET):%Y-%m-%d %H:%M:%S %Z} — runtime {time.time()-t0:.1f}s — exit code {code} ===")
    return code
if __name__ == "__main__": sys.exit(main())
