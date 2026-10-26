"""Weekly buying guides for the hub category subdomains (<cat>.theworthguide.com/guides/<slug>).
Picks come only from that category's verified Top 10 (_src/data.py + _src/verified.json, checked 2026-10-03); facts only from those
blurbs and listing titles, hedged. No prices. Built by build.py into c/<cat>/guides/<slug>.html; routed in vercel.json; listed in c/<cat>/sitemap.xml."""
GUIDES={
 'kitchen':[{
  'slug':'kitchen-basics-to-buy-first',
  'title':'Kitchen Basics Worth Buying First',
  'desc':'Seven everyday kitchen tools from the KitchenWorth Top 10 to buy before anything fancy: a chef’s knife, cast iron, a small nonstick pan, a scale, a peeler, containers and a can opener.',
  'date':'2026-10-26',
  'intro':'Setting up a first kitchen, or replacing a drawer of tools that never worked? Start with the basics you reach for every day. These seven come from the KitchenWorth Top 10, and the bigger appliances can wait.',
  'picks':[
   ('B008M5U1C2','Best first knife','The knife most home cooks end up keeping. It is easy to sharpen and hard to outgrow, and the listing describes it as dishwasher safe.',['8-inch chef’s knife for most everyday cutting','Easy to sharpen','Dishwasher safe, per the listing'],['One knife, not a full block set'],'Anyone who wants one knife that handles most jobs.'),
   ('B00006JSUA','Best pan to keep','The cast iron pan people tend to keep for decades. It comes pre-seasoned, and the listing describes it as PFAS-free. It is the pick for searing.',['Pre-seasoned, per the listing','PFAS-free, per the listing','Good for searing'],['Typically heavier than a nonstick pan','Cast iron needs its own care routine'],'Cooks who want one pan that sears and lasts.'),
   ('B009HBKPD0','Best egg pan','A small 8-inch nonstick pan for eggs and delicate food, where easy release matters more than searing.',['Nonstick for eggs and delicate food','Small 8-inch size'],['Not a searing pan; the Lodge covers that'],'Breakfast cooks who want easy release.'),
   ('B0113UZJE2','Best for baking','Weigh it once and baking stops being guesswork. It reads in grams and ounces, with an 11 lb capacity per the listing.',['Grams and ounces','11 lb capacity, per the listing'],['Most useful if you bake or follow weighed recipes'],'Bakers and anyone following recipes by weight.'),
   ('B00004OCIP','Best small upgrade','The swivel peeler that tends to replace a drawer of cheap ones, with a soft handle per the listing.',['Swivel blade','Soft, comfortable handle, per the listing'],['Does one job only'],'Anyone still peeling with a paring knife.'),
   ('B079M8FPTW','Best for leftovers','Clear, stackable containers with lids that seal. The listing describes a set of five 3.2-cup Tritan containers with airtight lids, BPA free.',['Clear and stackable','Airtight lids, per the listing','Tritan plastic, BPA free, per the listing'],['One container size in this set'],'Meal preppers and packed lunches.'),
   ('B07YP2VH4B','Best plain opener','A plain can opener that keeps working. The listing adds a bottle opener and a stainless steel cutting wheel.',['Stainless steel cutting wheel, per the listing','Bottle opener built in, per the listing'],['Manual, not electric'],'Every kitchen; it is easy to forget until you need it.'),
  ],
  'criteria':[
   ('Start with what you use daily','A good knife and one or two pans get more use than any gadget. Buy those first and add tools as recipes call for them.'),
   ('Cast iron and nonstick do different jobs','The Lodge sears and lasts; the Tramontina handles eggs and delicate food. Many kitchens end up with one of each.'),
   ('Bigger appliances can wait','The Instant Pot Duo and the KitchenAid Artisan mixer are in the KitchenWorth Top 10 too. The mixer is worth it if you bake and easy to skip if you do not.'),
  ],
  'faqs':[
   ('Do I need a knife set?','Not to start. One 8-inch chef’s knife covers most everyday cutting; add other knives later if you find a gap.'),
   ('Cast iron or nonstick first?','If you only buy one, choose by what you cook most: the Lodge for searing and long life, the Tramontina for eggs and easy release.'),
  ]}],
 'clean':[{
  'slug':'best-cordless-vacuums',
  'title':'Best Cordless Vacuums',
  'desc':'Four cordless vacuums from the CleanWorth Top 10, from a stick that converts to a handheld to a counter dustbuster, plus the corded upright to get if you clean the whole house at once.',
  'date':'2026-10-26',
  'intro':'Cordless vacuums make quick cleanups easy: grab it, clean, put it back. Here is how the cordless picks in the CleanWorth Top 10 compare, and when a corded upright still makes more sense.',
  'picks':[
   ('B09YS9N7H2','Best stick that converts','The cordless stick that converts to a handheld. The listing says it cleans hard floors and carpets, has two power modes, and runs up to 40 minutes.',['Converts to a handheld','Hard floors and carpets, per the listing','Up to 40 minutes of runtime, per the listing'],['Up to 40 minutes is the listed maximum'],'Homes that want one cordless vacuum for floors and above-floor cleaning.'),
   ('B07S652B12','Best for quick pet cleanups','Grab-and-go cleanup without the cord. The listing describes it as lightweight with a 40-minute runtime.',['Lightweight, per the listing','40-minute runtime, per the listing','Pet-focused model'],['A stick, not a whole-house replacement for an upright'],'Pet owners who clean in short bursts.'),
   ('B0CB6B2JWG','Best for long sessions','A cordless stick built for pet hair, with anti-tangle design and up to 50 minutes of runtime per the listing.',['Anti-tangle for pet hair, per the listing','Up to 50 minutes, per the listing'],['Up to 50 minutes is the listed maximum'],'Pet homes that want the longest listed runtime here.'),
   ('B07KG2X2GZ','Best handheld','The small one you keep on the counter. The listing describes a cordless, rechargeable handheld with a wall mount that also works as a car vacuum.',['Small enough for the counter','Wall mount, per the listing','Doubles as a car vacuum, per the listing'],['Handheld only; not for floors'],'Crumbs, spills and car seats.'),
   ('B004Q4DRJW','Corded alternative','The upright most homes end up with, if you would rather not deal with batteries. It lifts away for stairs, and the listing mentions HEPA.',['No battery to run down','Lifts away for stairs','HEPA, per the listing'],['Corded','Bulkier than a stick'],'Whole-house cleaning in one go.'),
  ],
  'criteria':[
   ('Stick or handheld','A stick vacuum handles floors; a handheld like the dustbuster handles counters, crumbs and cars. A stick that converts to a handheld, like the Dyson V8, covers both.'),
   ('Runtime claims','Runtimes are listed as up-to figures, so real-world runtime may be shorter depending on settings and floors.'),
   ('Pet hair','If you have pets, look for pet-focused or anti-tangle models like the Shark Pet or the Levoit.'),
  ],
  'faqs':[
   ('Can a cordless vacuum replace an upright?','For many apartments and quick daily cleanups, often yes. For a large house cleaned all at once, a corded upright like the Shark Navigator avoids battery limits.'),
   ('Which has the longest runtime?','Of these, the Levoit lists up to 50 minutes. The Dyson V8 lists up to 40 minutes and the Shark Pet lists 40 minutes.'),
  ]}],
}
