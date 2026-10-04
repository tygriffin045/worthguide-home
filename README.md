# worthguide-home

Static hub for https://theworthguide.com (Vercel project `worthguide-home`). Push to `main` to deploy.

- Hub pages: `index.html`, `guides.html`, `value.html`, `categories.html` (served at `/`, `/guides`, `/value`, `/categories`) are generated too, by `python3 _src/build.py` (directory copy in `_src/sites.py`). Brand rules: `BRAND.md`; shared CSS: `_src/site.css`.
- Category Top 10s are served on their own subdomains (kitchen, clean, tool, yard, bag, groom, fit, bath, travel, watch `.theworthguide.com`).
  They are generated into `c/<cat>/` (index.html, sitemap.xml, robots.txt) from `_src/data.py` by `python3 _src/build.py`,
  which also validates tags, disclosures, and Top 10 counts. Host routing and redirects live in `vercel.json`.
- Amazon tracking IDs: `<cat>worth20-20` on each category; `theworthguide20-20` on any other hub page.
