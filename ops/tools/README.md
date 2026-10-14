# /workspace/tools

Durable copies are in the hub repo under `ops/` (excluded from deploy via .vercelignore).

- `crawl_sitemaps.py`: production crawl of all 17 WorthGuide sitemaps (hub, the 10 hub c/ category hosts, and brew/car/desk/pet/sleep/tech). It checks, without following redirects: 200 per URL, exact self-canonical (root slash tolerant), noindex meta/header, lastmod validity, duplicates, robots.txt per host, every unique internal *.theworthguide.com link found on any page (200, no redirect), and an Etsy/KettleAndKibble text search on all sitemap and non-sitemap internal pages. Dollar counts per site are info only. The output shows ET times, runtime, exit code, repo SHAs and `vercel ls --prod` refs. It never requests amazon. Usage: `python3 crawl_sitemaps.py > crawl_output.txt`; exit 0 = clean.
- `../deskworth-verify/preview_check.py BASE_URL`: checks desk sitemap paths on a preview/prod base for 200 (no redirect), 0 visible dollar amounts, and canonical = https://desk.theworthguide.com/<path>.
- `crawl_output.txt`: latest crawl output.
- The other files here are older one-off product-selection scripts and data.

## Sales/gifts tools (added 2026-10-13)
- `check_site.py MODE BASE` — any subsite: every sitemap URL returns 200, canonical == sitemap URL, 0 dollar amounts, exactly one "we have not tested them hands-on" disclosure. MODE=`http` for production, `vcurl` for an SSO-protected preview (needs env `CWD=/workspace/top10/<x>worth`, the linked project dir). Example: `python3 check_site.py http https://pet.theworthguide.com`. Known benign flag: pet `/affiliate-disclosure` (uses Associate wording, not the hands-on line).
- `bar390.py URL [anchor-id]` — Playwright check of the sticky Amazon bar at 390px and 1366px: on load, past the anchor (e.g. `quick-picks`), and at the footer. Hidden must show `visiblePx: 0`. Setup (no signup): `python3 -m venv /workspace/.pwvenv && /workspace/.pwvenv/bin/pip install playwright && /workspace/.pwvenv/bin/python -m playwright install --with-deps chromium`.
- `indexnow_keys.txt` — public IndexNow keys (`<project> <key>`); each key is served at `https://<host>/<key>.txt`. Submit: POST JSON `{host,key,keyLocation,urlList}` to `https://api.indexnow.org/indexnow` (and/or `https://www.bing.com/indexnow`). The first submit after a new key can return 403 SiteVerificationNotCompleted; retry after a few minutes. Google's and Bing's sitemap ping endpoints are dead (404/410).
- No bypass tokens are stored here; never commit them.
