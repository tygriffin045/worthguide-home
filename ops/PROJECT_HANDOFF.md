# PROJECT HANDOFF — Tyler Griffin's businesses (for Grok)
Last updated: Mon Oct 12, 2026 (ET). Written by Tiff (Tyler's coordinator bot). Contains NO passwords, tokens or secrets.
Anything not verified is marked [UNCONFIRMED]. Tyler's time zone: America/New_York.

## 1. Business overview
- Owner: Tyler Griffin, sole proprietor. Goal: make two businesses profitable with lean effort/token use.
  1. The Worth Guide (theworthguide.com + category subdomains): Amazon-affiliate product review / buying-guide sites.
  2. KettleAndKibbleCo: Etsy print-on-demand shop (pet/kitchen gifts) fulfilled via Printify.
- Social brand for gift/product videos: "Gift Finds Daily" (@gift_finds_daily).
- Tyler's Oct 12 priority list: (1) Matrix-style dashboard redesign, (2) fix Google indexing, (3) revamp WorthGuide around Top 10 product reviews, (4) remove KKC links from WorthGuide, (5) find why socials get ~0 views, (6) make products shoppable in videos (TikTok Shop).
- Communication rule: Tyler talks ONLY to Tiff. Coworker bots report to Tiff, never start conversations with Tyler (they may answer if he messages them).

## 2. Brands and hard rules
- WorthGuide and KettleAndKibbleCo are SEPARATE brands. NO links to KettleAndKibbleCo/Etsy anywhere on WorthGuide (hub validator forbids Etsy links; crawl checks for "etsy.com" and "KettleAndKibble").
- NO prices on WorthGuide pages (Amazon Associates rules; ranges count as prices). Use $/$$/$$$ budget tiers next to "Check price on Amazon" buttons until PA-API access is unlocked. Builds should fail if a dollar price appears.
- Never touch / automate amazon.com (no scraping or logging in to Amazon).
- Spending limit: $15 without Tyler's explicit approval. No shop-wide Etsy sale ("we need to make money first").
- Do NOT use or mention Mac Doors LLC (TikTok Shop is under Tyler as sole proprietor).
- Top 10 rule: each category home page shows its Top 10; each subcategory has a Top 10 with 3 picks on top: Premium Pick, Best Overall, Value. Pros and cons for every product. Products may be adjusted.
- Get Tyler's approval before publishing, spending, deleting, or sending anything on his behalf (unless he already approved that specific item).
- /privacy page is hidden: noindex, not in sitemap, linked from nowhere (direct link only; used for Pinterest app). [UNCONFIRMED that noindex was finished]

## 3. Sites, repos and deploys
- GitHub owner: tygriffin045. Hosting: Vercel (deploys on push to main). Run git as `env -u GH_TOKEN git ...` on the box.
- Hub: theworthguide.com — repo worthguide-home, local /workspace/hub, built by `_src/build.py`. Routes subdomains via vercel.json. /links (bio link page, standalone, Etsy button removed) and /privacy (hidden). `ops/` folder holds handoff/ops docs and is excluded from deploys via .vercelignore.
- Category sites/repos: brewworth (brew.), deskworth (desk.), petworth (pet.), sleepworth (sleep.), carworth (car.), techworth (tech.), plus other categories served from the hub (/c/<category>, e.g. kitchen). 16 category home pages + 70 subcategory pages in the revamp scope (86 pages). Note: local clones in /workspace may be stale vs origin; always `git pull` first.
- Weekly buying guides (live Oct 12): desk best-usb-c-dock-for-desk, brew best-coffee-canisters, sleep best-sleep-mask-for-side-sleepers, pet best-slow-feeder-dog-bowls.
- Indexing (Search Console showed 648 not indexed / 120 indexed; reasons "Page with redirect", "Duplicate, Google chose different canonical"): FIXED on our side. Latest crawl: 17 sitemaps, 762 URLs, 0 non-200, 0 canonical mismatches, 0 noindex, 0 Etsy/KKC hits. Google knows 768 (desk dropped 2 duplicates). TODO: resubmit sitemaps + "Validate fix" in Search Console (Tyler's login); internal-link check being restored to full coverage.
- Revamp: desk revamp live; next brew, then pet and sleep, each on a Vercel preview reviewed by Maya before going live. Spec/page list are in hub ops/ (Elias recreating REVAMP_SPEC.md and REVAMP_PAGES.csv).
- Deploy incident: Vercel git-triggered deploys failing with git_info_fail (e.g. worthguide-home 9bb8917 first prod deploy failed; redeploy READY). Until fixed, deploy with the Vercel CLI and verify the deployment is READY.
- Oct 12: /workspace was restored from an Oct 8 snapshot; files not in git were lost. Keep important docs committed (hub/ops).

## 4. Dashboard
- Live at dash.theworthguide.com (password-gated; password lives only on the box in the dashboard folder — never paste it). Repo worthguide-dashboard, local /workspace/dashboard.
- Matrix/futuristic redesign is LIVE with weekly scorecard targets (Maya). Rooms: YouTube @TheWorthGuide, TikTok, Instagram, Pinterest (Hub room and KKC VIDEO room removed).
- Refresh videos: `python3 scripts/refresh_videos.py --push`. Etsy ingest: `ingest.py --etsy` (first sale shows "—" until it runs).
- Targets: KKC videos 5/week (0/5 this week, 4/5 last), Etsy pins 8/week (0/8). YouTube/TikTok/Pinterest/IG have no targets yet. Earnings show "—" until real data.
- Weekly scorecard every Monday.

## 5. Etsy / Printify (KettleAndKibbleCo)
- Shop: etsy.com/shop/KettleAndKibbleCo. Products created in Printify and published to Etsy via the Printify API. Design work under /workspace/etsy.
- Open: Etsy payment card failure — Tyler must fix in Etsy billing. [UNCONFIRMED current status]
- No shop-wide sale. Pins target 8/week once Pinterest is connected.

## 6. Socials and accounts (no passwords here)
- TikTok @gift_finds_daily; login email theworthguide20@gmail.com (Tyler holds password).
- TikTok Shop: sole-proprietor application SUBMITTED Oct 12 for shop "Gift Finds Daily", category Pet Supplies; review 1–3 days. After approval: connect Printify so videos get tappable buy links (~3–10 days total).
- TikTok views problem: first 6 posts got 89–177 views; 9 posts from Oct 4 evening were flagged COMMERCIAL CONTENT (disclosure toggle on) and got 0–6 views; ~0 views/day since Oct 6. No strikes/restrictions. Recommendation: delete & repost those 9 at 1–2/day with disclosure toggle off, affiliate note in caption. Tyler is DECIDING — do not delete/repost without his OK. Tyler may check in-app: Settings > Account > Account status, and a post's Content disclosure.
- Going forward: 1–2 posts/day per platform, no batch posting.
- YouTube @TheWorthGuide (channel UChD3VgKELiZ7UvFK17jzvFQ): Content ID claim on audio "Upbeat Theme" — swap the track. YouTube Shopping needs 500 subscribers. Pending: upload the watch Short.
- Instagram gift_finds_daily: new, unrestricted. Product tags need a Meta shop; Etsy can't connect to it.
- Pinterest: developer app trial access pending; connect after approval (token kept on box only, never in docs).
- Bio link: theworthguide.com/links.
- Social stats gathered by public scraping (yt-dlp).

## 7. Routines
- Weekly Monday scorecard (dashboard + summary to Tyler).
- Weekly 4 buying guides across categories.
- Dashboard video refresh. Some routines failed during usage limits — rerun when usage resets. [UNCONFIRMED exact routine list/schedules]

## 8. The team (created Oct 12, all report to Tiff)
- Tiff — coordinator; only bot Tyler talks to; keeps live task board; approves/relays.
- Nora — commerce & social: TikTok Shop, Printify connection, posting (5 KKC videos + 8 Etsy pins/week), social diagnostics.
- Elias — sites & SEO: WorthGuide revamp, indexing, KKC-link removal, crawl checks, deploys.
- Maya — design, data & review: dashboard, scorecard targets, proof-based review of others' work and previews.
- Verification is proof-based: claims need run output, commit/deploy IDs.

## 9. Open items (as of Oct 12)
1. TikTok Shop approval (1–3 days) → connect Printify → shoppable videos.
2. Tyler decision: delete/repost 9 commercial-flagged TikToks.
3. Swap YouTube "Upbeat Theme" audio; upload watch Short.
4. Revamp brew → pet → sleep (preview + Maya review), then remaining categories; $/$$/$$$ tiers everywhere.
5. Search Console: resubmit sitemaps, validate fixes; reconcile 762 vs 768.
6. Fix Vercel git_info_fail (use CLI deploys meanwhile).
7. Restore full internal-link crawl coverage.
8. Connect Pinterest when app approved; start 8 pins/week.
9. Etsy card failure (Tyler). Rerun failed routines. Confirm /privacy noindex.
