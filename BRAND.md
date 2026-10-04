# The Worth Guide — brand system

One look across theworthguide.com and every `<x>.theworthguide.com` subsite. Based on the strongest existing
pieces: the DeskWorth header/footer and badge picks (Next.js subsites) and the hub's warm paper palette.
Reference implementation: `_src/site.css` (+ `_src/cat.css` for Top 10 pages), templated by `_src/build.py`.

## 1. Logo and wordmark
- **Mark:** gold outline ring with a check. 24×24 viewBox, `circle r=9` + path `M7.5 12.2 10.6 15.3 16.5 8.8`,
  stroke `#d4af37`, width 1.8, round caps/joins, no fill. Use as-is; never fill it or recolor it.
- **Wordmark:** Source Serif 4, 600, letter-spacing -0.02em, ~1.4rem in the header.
  - Subsites: `<Name><b>Worth</b>`, e.g. Kitchen**Worth** — the name in ink, "Worth" in gold.
  - Hub: `The <b>Worth</b> Guide`.
  - "Worth" color: `#8a6a22` (gold-deep) on light backgrounds (readable), `#d4af37` (gold) on the dark footer.
- Mark + wordmark sit together, 8px gap, link to that site's home.
- Favicon: ink rounded square with the gold ring and check.

## 2. Color
| Token | Hex | Use |
|---|---|---|
| `--bg` paper | `#f4f1ea` | page background (subsites may tint it to their accent, e.g. brew `#f6efe6`) |
| `--paper` | `#fffdf9` | cards, panels |
| `--ink` | `#1c1917` | text, active nav pill, footer background |
| `--ink2` | `#44403c` | body copy on cards |
| `--muted` | `#78716c` | secondary text, notes |
| `--line` / `--line2` | `#e7e1d6` / `#d8cbb8` | borders / hover borders |
| `--gold` | `#d4af37` | logo mark, "Worth" on dark |
| `--gold-deep` | `#8a6a22` | "Worth" on light, kicker-like accents, Worth It chip text |
| `--gold-soft` | `#f8f1de` | chips, label tags |
| `--terra` / `--terra-deep` | `#c45c26` / `#a84c1f` | **all Amazon CTAs**, Bang for the Buck badge, kickers |
| `--green` | `#047857` | Value Pick badge |

**Site accents** (keep them; use for the topic chip, kickers, links and dark footer tint — never for the Amazon CTA,
which is always terra so it reads the same everywhere):

| Site | Accent | Footer |
|---|---|---|
| Hub + 10 static category sites | gold `#8a6a22` / terra `#c45c26` | ink `#1c1917` |
| DeskWorth | `#c45c26` | ink `#1c1917` |
| BrewWorth | `#8b4513` | espresso `#2a1a12` |
| SleepWorth | `#4338ca` | indigo-950 |
| PetWorth | `#3d6b5a` | emerald-950 |
| TechWorth, CarWorth | gold `#d4af37` | ink `#1c1917` |

## 3. Type
- Headings + wordmark: **Source Serif 4** (600/700, italic 600 for the gold emphasis line in heroes).
- UI + body: **Source Sans 3** (400/600/700), 17px base, line-height 1.6.
- Kicker: Source Sans 3 700, .74rem, letter-spacing .16em, uppercase, terra-deep (or site accent).
- Hero H1: clamp(2.5rem, 5.6vw, 4.2rem), line-height 1.04, -0.03em; second line in italic gold-deep.
- Load via Google Fonts (`display=swap`, preconnect) or `next/font/google` on Next.js — same two families everywhere.

## 4. Header
- Sticky, translucent paper (`rgba(244,241,234,.88)`) + `backdrop-filter: blur(10px)`, 1px bottom border, ~66px tall.
- Left: mark + wordmark. Right: nav links (Source Sans 3 600, .95rem, pill padding 8×14).
- Hover: faint ink tint. **Active page: ink pill with white text** (`aria-current="page"`).
- Subsites add a gold-deep "The Worth Guide" link back to the hub.
- Mobile (≤760px): nav collapses behind a 42px round menu button (`aria-expanded`, `aria-controls`); the panel drops
  down full width under the header.
- A small note sits at the top of the content: *"We may earn a commission from qualifying purchases."* (.78rem, muted).

## 5. Footer
- Dark ink band (or the site's dark accent tint). Wordmark (gold "Worth") + one-line description.
- **"The Worth Guide family"** column: The Worth Guide + all 16 `…Worth` subsites.
- Bottom legal row, centered, .8rem: *"We may earn a commission when you buy through links on this site. As an Amazon
  Associate I earn from qualifying purchases."* then `© 2026 The Worth Guide`. Exactly once per page.
- No email address, no About page, no prices.

## 6. Buttons
- **Primary (Amazon):** pill, terra `#c45c26` → hover `#a84c1f`, white Source Sans 3 600, padding 11×18, small shadow,
  1px lift on hover. Label is always **"Check price on Amazon"**. Never show a price.
  `rel="nofollow sponsored noopener" target="_blank"`, and the page's own Amazon tag.
- **Ghost (navigation):** pill, transparent, 1px `--line2` border, ink text; hover paper fill + ink border.
- Text link CTA on cards: terra 600 with a trailing arrow ("See top 10 →").

## 7. Badges and chips
- Pills, 700, .72rem, letter-spacing .08em, uppercase, padding 5×12.
  - **Premium Pick:** `#1c1917` bg / `#fde68a` text.
  - **Bang for the Buck:** `#c45c26` / white.
  - **Value Pick:** `#047857` / white.
  - **Worth It / list labels** (Our pick, Value pick, Most bought): `#f8f1de` / `#8a6a22`.
- Topic chip on images: paper pill on the image corner, text in the site accent.
- The three badges only appear where `badges.json` has picks; badge copy must come from that data.

## 8. Cards
- `--paper` bg, 1px `--line` border, **16px radius**, soft shadow `0 1px 2px / 0 2px 8px` at 4–5% ink.
- Hover: lift 3px, larger shadow (`0 10px 30px` at 10%), border `--line2`, image zooms 4%.
- Category / guide cards: 4:3 photo (guides use the 2:3 pin art) + serif title + one line + terra arrow CTA.
- Product cards: square white image well (`object-fit: contain`, padding), badge on the image corner,
  name in Source Sans 3 600, one line of copy, primary button at the bottom.
- Panels/bands group related cards: paper, 22px radius. The badge-picks panel uses a soft gold gradient
  (`#fbf5e6 → #f8f0dc`, border `#ecd9a6`).
- Grids: auto-fill min 260px, 20px gap; on phones 2 columns (12px gap); product trios become a swipe row.

## 9. Rules that never change
No prices. No invented specs, ratings or claims. Every Amazon link keeps its tag (`<cat>worth20-20` on category
sites, `theworthguide20-20` on hub pages). No email, no About page. Keep the top note and the footer disclosure.
