# WorthGuide Revamp Spec (recreated 2026-10-12; reference implementation: deskworth main 9a3ceab)

## Scope
86 core pages: 16 category home pages (6 subsite homes + 10 hub c/ sites) and 70 subcategory pages; product/compare/guide pages pick up the shared button, tier, disclosure and pros/cons rules. Full list: `REVAMP_PAGES.csv` (site, path, page_type, current_state).

## Page layouts
- **Category home**: leads with its Top 10 (compact cards, category labels instead of #1–#10, one Top 10 section only).
- **Subcategory page**: Best Overall, Premium Pick and Value Pick at the top, then a Top 10. Each product shows 2–4 pros and 1–3 cons.

## Pricing and tiers
- No prices or price ranges anywhere (copy, JSON-LD, compare rows). Budget tiers are `$`, `$$`, `$$$`.
- Tiers come from per-category price thresholds (internal data only). Tied prices share a tier. Cheap categories are capped at `$$`. Then a manual pass, with copy matching the tier (no "mid-range" on a `$$$`). No leftover `budget` field.
- Button text is exactly **"Check price on Amazon"**, with an `aria-label` that includes the product name; `rel="sponsored nofollow"` and the site affiliate tag. Agents never request amazon.com.

## Picks
- An explicit `PICKS` map per category (best/premium/value); no rank-based fallback.
- Premium's tier is never below Best Overall's. Value is a `$` item whenever the Top 10 has one. The #1 in the Top 10 and the homepage matches Best Overall.
- The Top 10 has exactly 10 distinct products (no near-duplicate variants).

## Structured data
- No `Product` JSON-LD (never offers/prices/ratings). Breadcrumb/ItemList/Organization are OK.

## Copy rules
- One affiliate disclosure per page (the shared layout note; the footer Associates line is fine).
- Pros are in plain editorial voice: no pasted listing bullets, no seller voice ("our", "you'll love", "effortlessly", "say goodbye", "experience the/smooth", "maximize"; our own "our … pick" is allowed), and no "Per the Amazon listing:" summaries.
- Cons are about the product and hedged. Never imply hands-on testing ("can loosen with use", not "joints need re-tightening"). No "not tested" con.
- Keep exact figures that decide fit, compatibility or safety (VESA, wattage/PD, ETL/joules, weight capacity, dimensions). Rounding with "about" is fine otherwise.
- Specific "who it's for" lines; picks and homepage Top 10 get individual summaries.

## Build gates (fail the build)
- `scripts/validate-revamp.ts`: 10 Top 10 entries, picks present and obeying the picks rules, tier present, pros 2–4, cons 1–3, no `budget` field, listing-voice and seller-voice regex on summary/tagline/pros/cons/whoFor.
- `scripts/check-no-prices.mjs` on `src` and on the built `.next/server/app`.
- Wired as `npm run build` = validate:revamp && check-no-prices src && next build && check-no-prices build.

## Rollout
1. desk: done (main 9a3ceab), the reference.
2. Wave 1: brew, pet, sleep. Wave 2: car, tech. Wave 3: static hub c/ sites (bag, bath, clean, fit, groom, kitchen, tool, travel, watch, yard).
- Each site goes on a preview deploy first; Maya reviews; merge only after her sign-off. Then run `tools/crawl_sitemaps.py` (17 sitemaps clean) and `deskworth-verify/preview_check.py`-style checks.
