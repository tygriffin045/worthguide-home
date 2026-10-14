import json,re,subprocess,collections
U={r['asin']:r for r in json.load(open('/workspace/tools/listing_union.json'))}
def prods(site):
    s=open(f'/workspace/top10/{site}/src/data/products.ts').read()
    out=[]
    for b in re.split(r'\n\s*\{\s*\n',s)[1:]:
        g=lambda k:(re.search(r'"?'+k+r'"?:\s*"((?:[^"\\]|\\.)*)"',b) or [None,''])[1]
        if g('slug'): out.append(dict(slug=g('slug'),cat=g('category'),tier=g('tier'),asin=g('amazonAsin'),name=g('name')))
    return out
L=[ # site, category, current n, include regex, exclude regex
 ('sleepworth','sheets-bedding',9,r'sheet set|bed sheets|sheets set|\bsheets\b',r'bamboo|eucalyptus|tencel|cooling|crib|fitted only|pillowcase only|mattress protector|baby'),
 ('sleepworth','blackout-curtains-masks',6,r'blackout (curtain|shade|liner|drape)|blackout.*curtain|room darkening',r'sleep mask|eye mask|kids|nursery'),
 ('sleepworth','bedtime-lighting',9,r'sunrise alarm|wake.?up light|night lights?\b|bedside lamp|nightstand lamp|red light.*sleep|sleep light',r'baby|kids|projector|strip|desk lamp|monitor|keyboard|usb led|power bank|sound machine'),
 ('carworth','dash-cams',9,r'dash ?cam|dashcam',r'mirror|radar|adhesive|pads|mount only|hardwire kit'),
 ('carworth','roadside',8,r'jump starter|jump box|tire inflator|air compressor|battery (charger|maintainer|tender)|tire gauge|jumper cables',r'bike only|ball pump'),
 ('carworth','cabin',8,r'car phone (holder|mount)|phone holder for car|car mount|car charger|seat gap|trunk organizer|seat back organizer',r'weathertech|wrangler|radar|adhesive pads'),
 ('carworth','diagnostics',7,r'obd2|obd ii|obd-ii|obdii|code reader|scan tool|scanner.*car',r'radar|detector'),
 ('carworth','cleaning',6,r'car wash|microfiber.*(car|towel)|car vacuum|glass cleaner|detail(ing)? (spray|brush|kit)|car wax|interior cleaner|ceramic spray',r''),
 ('carworth','safety',9,r'emergency (kit|escape|hammer)|first aid kit|road flares?|led (flare|strobe)|reflective (triangle|warning)|window breaker|seatbelt cutter|fire extinguisher.*car',r''),
 ('techworth','webcams',8,r'webcam|web camera',r'security|baby|doorbell'),
 ('techworth','amazon-devices',9,r'^(amazon (echo|kindle|fire)|echo |kindle |blink |ring |eero )',r'case for|cover for|mount for|compatible with|replacement|charger for|stand for|protector|insignia|toshiba|\bTV\b class'),
 ('petworth','flea-tick-prevention',8,r'\bflea|\bticks?\b',r'shampoo|comb|brush|spray for home|yard|fire tv|litter'),
 ('petworth','training-waste',8,r'poop bags?|waste bags?|potty pads?|pee pads?|training pads?|dog training clicker|pet training clicker|pooper scooper|enzyme cleaner|pet stain',r'switch|keyboard|litter box|3d print'),
 ('petworth','puppy-kitten-starter',7,r'\bpuppy|\bkitten',r'food|treats?|cat tree|scratch'),
 ('petworth','feeders-fountains',9,r'pet (water )?fountain|automatic (pet|cat|dog) feeder|cat fountain|water dispenser.*pet|elevated (dog|cat) bowls?|pet bowls?',r'slow feeder'),
]
def tiers_for(site,cat,ps):
    th=None
    for f in ['scripts/tier-prices.json']:
        try:
            d=json.load(open(f'/workspace/top10/{site}/{f}')); th=d.get('thresholds',{}).get(cat)
        except Exception: pass
    if th: return lambda p:'$' if p<th[0] else ('$$' if (th[1] is None or p<th[1]) else '$$$'),f'thresholds {th}'
    pts=[(U[x['asin']]['price'],x['tier']) for x in ps if x['cat']==cat and x['asin'] in U and U[x['asin']]['price']]
    m1=max([p for p,t in pts if t=='$'] or [0]); m2=max([p for p,t in pts if t=='$$'] or [m1])
    return (lambda p:'$' if p<=m1 else ('$$' if p<=m2 else '$$$')),f'from {len(pts)} existing prices ($≤{m1:.0f}, $$≤{m2:.0f})'
res={}
for site,cat,n,inc,exc in L:
    ps=prods(site); have={x['asin'] for x in ps}
    f,how=tiers_for(site,cat,ps)
    c=[]
    for r in U.values():
        t=r['title']
        if r['asin'] in have or not t or not re.search(inc,t,re.I) or (exc and re.search(exc,t,re.I)): continue
        full=bool(r['price'] and r['bullets']>=3 and r['img'] and r['oos'] is not True)
        c.append(dict(asin=r['asin'],title=t[:90],price=r['price'],tier=f(r['price']) if r['price'] else None,full=full,src=r['src'][0].replace('/workspace/','')))
    full=[x for x in c if x['full']]
    res[f'{site}/{cat}']=dict(current=n,need=10-n,tierRule=how,full=full,partial=[x for x in c if not x['full']])
    print(f'\n## {site} {cat}: {n} now, needs {10-n}; {len(full)} full candidates, {len(c)-len(full)} partial  [{how}]')
    for x in full[:6]: print(f"  {x['tier']} {x['asin']} {x['title'][:80]}  ({x['src'][:40]})")
json.dump(res,open('/workspace/tools/refill_inventory.json','w'),indent=1)
