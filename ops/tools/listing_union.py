import json,glob,re,os
recs={}
def add(asin,d,src):
    if not asin or not re.fullmatch(r'[A-Z0-9]{10}',asin): return
    t=d.get('title') or ''
    price=d.get('price') or d.get('priceText') or ''
    if isinstance(price,(int,float)): price=f'{price}'
    m=re.search(r'(\d[\d,]*\.?\d*)',str(price)); p=float(m.group(1).replace(',','')) if m else None
    b=d.get('bullets') or []
    img=d.get('image') or d.get('img') or ''
    oos=d.get('outOfStock') or d.get('oos')
    r=recs.setdefault(asin,{'asin':asin,'title':'','price':None,'bullets':0,'img':False,'oos':None,'src':set()})
    if len(t)>len(r['title']): r['title']=t
    if p and not r['price']: r['price']=p
    r['bullets']=max(r['bullets'],len(b) if isinstance(b,list) else 0)
    r['img']=r['img'] or bool(img)
    if oos is not None: r['oos']=bool(oos)
    r['src'].add(src)
def walk(obj,src,key=None):
    if isinstance(obj,dict):
        a=obj.get('asin') or (key if key and re.fullmatch(r'[A-Z0-9]{10}',str(key)) else None)
        if a and ('title' in obj): add(a,obj,src)
        for k,v in obj.items(): walk(v,src,k)
    elif isinstance(obj,list):
        for v in obj: walk(v,src)
files=[f for f in glob.glob('/workspace/**/*.json',recursive=True) if '/node_modules/' not in f and '/.next/' not in f and os.path.getsize(f)<30_000_000]
for f in files:
    try: d=json.load(open(f))
    except Exception: continue
    base=os.path.basename(f); m=re.search(r'([A-Z0-9]{10})\.json$',base)
    if m and isinstance(d,dict) and 'title' in d: add(m.group(1),d,f)
    else: walk(d,f)
out=[dict(r,src=sorted(r['src'])[:3]) for r in recs.values()]
json.dump(out,open('/workspace/tools/listing_union.json','w'),indent=0)
full=[r for r in out if r['title'] and r['price'] and r['bullets']>=3 and r['img'] and r['oos'] is not True]
print(len(out),'asins;',len(full),'with title+price+3 bullets+image, not OOS')
