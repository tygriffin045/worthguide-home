# /workspace/tools

Durable copies are in the hub repo under `ops/` (excluded from deploy via .vercelignore).

- `crawl_sitemaps.py`: production crawl of all 17 WorthGuide sitemaps (hub, the 10 hub c/ category hosts, and brew/car/desk/pet/sleep/tech). It checks, without following redirects: 200 per URL, exact self-canonical (root slash tolerant), noindex meta/header, lastmod validity, duplicates, robots.txt per host, every unique internal *.theworthguide.com link found on any page (200, no redirect), and an Etsy/KettleAndKibble text search on all sitemap and non-sitemap internal pages. Dollar counts per site are info only. The output shows ET times, runtime, exit code, repo SHAs and `vercel ls --prod` refs. It never requests amazon. Usage: `python3 crawl_sitemaps.py > crawl_output.txt`; exit 0 = clean.
- `../deskworth-verify/preview_check.py BASE_URL`: checks desk sitemap paths on a preview/prod base for 200 (no redirect), 0 visible dollar amounts, and canonical = https://desk.theworthguide.com/<path>.
- `crawl_output.txt`: latest crawl output.
- The other files here are older one-off product-selection scripts and data.
