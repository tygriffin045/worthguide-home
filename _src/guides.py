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
 'tool':[{
  'slug':'starter-toolkit-for-a-first-home',
  'title':'Starter Toolkit for a First Home',
  'desc':'Seven tools from the ToolWorth Top 10 that cover most first-home jobs: a cordless drill, a bit set, a multi-bit screwdriver, a hammer, a utility knife, hex keys and a one-handed clamp.',
  'date':'2026-11-02',
  'intro':'Moving into a first place means shelves to hang, furniture to build and boxes to open. These seven picks from the ToolWorth Top 10 handle most of it. The shop vac and the bigger kits can wait until a job calls for them.',
  'picks':[
   ('B00ET5VMTU','Best first power tool','Just the drill, for less. The listing describes a 20V Max XR drill driver with a battery and charger, which is enough for hanging shelves and assembling furniture.',['Battery and charger included, per the listing','Covers drilling and light driving'],['No impact driver; the combo kit adds one'],'Anyone who mostly hangs things and builds flat-pack furniture.'),
   ('B00IJ0ALYS','Best if you build things','The drill and driver pair most houses need. The listing says the kit includes 2 batteries, a charger and a bag.',['Drill plus impact driver','2 batteries, charger and bag, per the listing'],['More than you need if you only hang shelves'],'People who drive long screws or take on bigger projects.'),
   ('B002JWSNIS','Best bit set','The bits you reach for, in one case. The listing describes a 45-piece screwdriver bit set with a tough case.',['45 pieces, per the listing','Comes in a tough case, per the listing'],['Bits only; you need a drill or driver to use them'],'Anyone with a drill who keeps hunting for the right bit.'),
   ('B0015SBILG','Best hand screwdriver','One screwdriver that replaces a drawer of them. The listing describes 8 bits (Phillips, slotted, Torx and square) plus 3 nut driver sizes and a cushion grip handle.',['8 bits and 3 nut driver sizes, per the listing','Cushion grip handle, per the listing'],['Manual, so slower than a powered driver on big jobs'],'Quick fixes where getting the drill out is overkill.'),
   ('B00002N5NA','Best hammer','A solid hammer that lasts. The listing describes a 16 oz curved claw hammer with a smooth face and a shock reduction grip.',['16 oz curved claw, per the listing','Shock reduction grip, per the listing'],['One size; heavy framing may call for something bigger'],'Hanging pictures, tapping in nails and pulling them back out.'),
   ('B097SXK3FG','Best for moving day','An all-metal box cutter for every job. The listing describes a retractable heavy duty utility knife with quick blade changes and 10 extra blades.',['Retractable, all-metal, per the listing','10 extra blades included, per the listing'],['A sharp blade; store it away from kids'],'Opening boxes, cutting carpet and trimming materials.'),
   ('B07V844YR8','Best for flat-pack furniture','Every flat-pack furniture job needs one. The listing describes a 36-piece set in SAE and metric sizes, with long arms and two storage cases.',['SAE and metric sizes, per the listing','Two organized storage cases, per the listing'],['Hex keys only'],'Anyone assembling furniture that arrives in a box.'),
  ],
  'criteria':[
   ('Drill driver or combo kit','Buy the DEWALT drill driver alone if you mostly hang shelves and assemble furniture. Buy the combo kit if you drive long screws or build things.'),
   ('Hand tools still matter','A good screwdriver, hammer and hex key set handle the small jobs faster than getting a power tool out.'),
   ('Add tools as jobs come up','The CRAFTSMAN shop vac, the IRWIN one-handed clamp and the HOTO electric screwdriver are in the ToolWorth Top 10 too, for when a project calls for them.'),
  ],
  'faqs':[
   ('Do I need an impact driver?','Not to start. The drill driver covers drilling and light driving; the impact driver in the combo kit helps if you drive long screws or build things.'),
   ('Is the bit set needed if I buy a drill?','Usually yes. The bit set gives the drill the screwdriver tips that most jobs call for.'),
  ]}],
 'yard':[{
  'slug':'best-garden-hand-tools',
  'title':'Best Garden Hand Tools',
  'desc':'Six garden hand tools from the YardWorth Top 10: bypass pruners, loppers, a trowel, a stand-up weeder, a pump sprayer and a hose that does not fight you.',
  'date':'2026-11-02',
  'intro':'Fall cleanup and spring planting mostly come down to a few hand tools. These six come from the YardWorth Top 10, and none of them needs a battery or a gas can.',
  'picks':[
   ('B00002N66H','Best pruners','The pruners in most garden sheds. The listing describes bypass pruning shears with a 5/8-inch cut capacity.',['Bypass blades','5/8-inch cut capacity, per the listing'],['For smaller stems; thicker branches need loppers'],'Deadheading, shaping shrubs and cutting small stems.'),
   ('B000BX1IB6','Best for branches','For the branches the pruners cannot take. The listing describes 28-inch bypass loppers with a 1.5-inch cut capacity.',['28-inch handles for reach and leverage','1.5-inch cut capacity, per the listing'],['Not for large limbs beyond the listed capacity'],'Trimming trees and overgrown shrubs.'),
   ('B004S0PGPM','Best trowel','A trowel that digs without bending. The listing describes a heavy duty hand tool for digging and planting.',['Heavy duty, per the listing','Made for digging and planting'],['A hand tool; big beds still need a shovel'],'Planting bulbs, flowers and vegetables.'),
   ('B001D1FFZA','Best for weeds','Pull weeds by the root without kneeling. The listing describes a stand up weed puller with a bamboo long handle.',['Stand-up use, so no kneeling','Long bamboo handle, per the listing'],['Does one job only'],'Lawns with dandelions and anyone whose knees are done with weeding.'),
   ('B000E28UQU','Best sprayer','A simple sprayer for lawn and garden. The listing describes a 1-gallon pump sprayer for lawn, garden and weeds.',['1-gallon size, per the listing','Simple hand pump'],['Small tank for big lawns'],'Spot-treating weeds and small garden areas.'),
   ('B00OHRTKLM','Best hose','The hose that does not fight you. The listing describes a lightweight, flexible, all-weather 5/8-inch by 50-foot hose with SwivelGrip and leak-free connections.',['Lightweight and flexible, per the listing','All-weather, per the listing','SwivelGrip connections, per the listing'],['50 feet may be short for big yards'],'Watering beds and washing things down without kinks.'),
  ],
  'criteria':[
   ('Pruners or loppers','Bypass pruners handle stems up to their listed 5/8-inch capacity. Loppers take branches up to their listed 1.5 inches with more reach.'),
   ('Save your back','The stand-up weeder and the Ergo trowel are made to cut down on bending and kneeling.'),
   ('Power tools are a separate decision','The EGO and Greenworks cordless mowers, the WORX trimmer and edger, and the Scotts spreader are in the YardWorth Top 10 too.'),
  ],
  'faqs':[
   ('What is a bypass pruner?','Bypass pruners cut with two blades that pass each other like scissors, which is why both the Fiskars pruners and loppers here use that design.'),
   ('Which tools should I buy first?','For most yards: pruners, a trowel and a hose. Add loppers if you have trees or big shrubs, and the weeder if weeds are the main job.'),
  ]}],
 'bag':[{
  'slug':'best-carry-on-luggage',
  'title':'Best Carry-On Luggage',
  'desc':'Five carry-on spinners from the BagWorth Top 10, hardside and softside, from a brand built for frequent flyers to budget picks, plus a travel backpack for one-bag trips.',
  'date':'2026-11-02',
  'intro':'A good carry-on saves checked-bag fees and waiting at baggage claim. Here is how the carry-on picks in the BagWorth Top 10 compare, and when a travel backpack makes more sense.',
  'picks':[
   ('B07BL7JXHV','Best softside','A softside carry-on spinner built to hold up. The listing describes the Travelpro Maxlite 5 as a 21-inch softside spinner.',['Softside, so it gives a little when packed full','21-inch spinner, per the listing'],['Softside shell is less rigid than hardside'],'Frequent travelers who like a softside bag.'),
   ('B01M0A3BKH','Best hardside','A hardside carry-on from a brand that lasts. The listing describes an expandable hard shell with spinner wheels and smooth rolling.',['Hardside shell','Expandable, per the listing','Spinner wheels, per the listing'],['Hardside does not squeeze into tight spaces'],'People who fly often and want a brand built for it.'),
   ('B071VG5N9D','Best value','The carry-on that does the job for less. The listing describes a 21-inch hardside spinner that expands for up to 25% more space, with a scratch-resistant shell and a telescoping handle.',['Expands up to 25%, per the listing','Scratch-resistant shell, per the listing'],['Fewer features than the pricier picks'],'People who fly a few times a year.'),
   ('B07YNKH8BZ','Best budget hardside','A budget hardside that rolls well. The listing describes a 22.5-inch hardside spinner carry-on.',['Hardside spinner','Budget pick'],['22.5 inches is a little longer than the 21-inch picks; check your airline’s size limits'],'Occasional trips on a tight budget.'),
   ('B0D14QYX9Y','Best expandable softside','Softside luggage that expands when you need it. The listing describes the SwissGear Sion as a durable, lightweight expandable spinner in carry-on size.',['Expandable, per the listing','Lightweight, per the listing'],['Expanded, it may not fit every overhead bin'],'Travelers who come home with more than they left with.'),
   ('B09KQ262GM','Backpack alternative','The travel pack for one-bag trips. The Osprey Farpoint 40L is a travel backpack rather than a roller.',['40L travel backpack','No wheels to drag over stairs or cobblestones'],['You carry the weight on your back'],'One-bag trips and travel with lots of walking.'),
  ],
  'criteria':[
   ('Hardside or softside','Hardside shells like the Samsonite and Amazon Basics protect what is inside. Softside bags like the Travelpro give a little when packed full.'),
   ('How often you fly','Buy the Samsonite if you fly often and want a brand built for it. Buy the Amazon Basics if you fly a few times a year.'),
   ('Check size limits','Airline carry-on limits vary, so check your airline’s size rules before you fly, especially with a longer bag or one that expands.'),
  ],
  'faqs':[
   ('Is a carry-on backpack better than a roller?','For one-bag trips with lots of walking, a travel pack like the Osprey Farpoint 40L can be easier. For airports and smooth floors, a spinner is easier on your back.'),
   ('What does expandable mean?','An expandable bag unzips to add room. The Amazon Basics lists up to 25% more space; expanded bags may not fit every overhead bin.'),
  ]}],
 'groom':[{
  'slug':'best-tools-for-home-haircuts-and-beard-trims',
  'title':'Best Tools for Home Haircuts and Beard Trims',
  'desc':'Four trimmers and clippers from the GroomWorth Top 10 for home haircuts, beard lines and stubble, from Wahl clipper kits to the Andis T-Outliner and Philips OneBlade.',
  'date':'2026-11-02',
  'intro':'Home haircuts and beard trims between barber visits mostly need the right clipper or trimmer. These four picks come from the GroomWorth Top 10, each for a different job.',
  'picks':[
   ('B01N0993NM','Best cordless clipper','Home haircuts with color-coded guards. The listing describes a cordless, rechargeable hair clipper and trimmer with color guards.',['Cordless and rechargeable, per the listing','Color-coded guards'],['Battery needs charging between cuts'],'Home haircuts without a cord in the way.'),
   ('B00006IVEN','Best corded kit','The corded kit that keeps going. The listing describes a corded haircutting kit with color guide combs.',['Corded, so no battery to run down','Color guide combs, per the listing'],['The cord limits where you can cut'],'Families doing regular home haircuts.'),
   ('B0BJ15Z14D','Best for clean lines','A professional trimmer for clean lines. The listing describes the Andis T-Outliner as a professional beard and hair trimmer.',['Professional trimmer, per the listing','Beard and hair'],['A detail trimmer, not a full haircut clipper'],'Edging necklines, sideburns and beard lines.'),
   ('B0BZQTSBWZ','Best for stubble','Trim, edge, and shave with one tool. The listing describes the OneBlade 360 as a hybrid face trimmer and shaver with a 5-length comb.',['Trims, edges and shaves','5-length comb, per the listing'],['A face tool, not for full haircuts'],'Anyone who keeps stubble and wants one tool for it.'),
  ],
  'criteria':[
   ('Clipper or trimmer','Clippers like the Wahl Color Pro kits handle full haircuts. Trimmers like the Andis T-Outliner handle edges and detail work.'),
   ('Cordless or corded','The cordless Wahl goes anywhere but needs charging; the corded Wahl kit keeps going as long as it is plugged in.'),
   ('Shaving is a separate pick','For a clean daily shave, the Braun Series 7 foil shaver and the Merkur 34C safety razor are in the GroomWorth Top 10 too.'),
  ],
  'faqs':[
   ('Do I need a trimmer if I have clippers?','Not always. A trimmer like the Andis T-Outliner helps with clean lines around the neck, ears and beard that a full-size clipper handles less easily.'),
   ('OneBlade or a foil shaver?','Buy the OneBlade if you keep stubble and want one tool to trim and edge. Buy a foil shaver like the Braun if you want a clean shave every morning.'),
  ]}],


 'fit':[{
  'slug':'best-home-gym-basics',
  'title':'Best Home Gym Basics',
  'desc':'Six home gym basics from the FitWorth Top 10: adjustable dumbbells, a kettlebell, a yoga mat, a foam roller, a jump rope and an air rower.',
  'date':'2026-11-09',
  'intro':'A home gym does not need a whole room. These six picks come from the FitWorth Top 10 and cover strength, cardio and recovery without taking much space.',
  'picks':[
   ('B0FRNG2N5H','Best for strength in a small space','Adjustable dumbbells that save floor space. The listing is for the BowFlex Results Series SelectTech set.',['Adjustable, so one set replaces many','Saves floor space'],['Costs more than a fixed pair'],'Lifters who want a full set of weights in a small space.'),
   ('B0731DFTR2','Best kettlebell','A cast iron bell for swings and squats, from Amazon Basics.',['Cast iron','Made for swings and squats'],['One fixed weight per bell'],'Anyone who wants simple, compact strength work.'),
   ('B0BYFFX51Z','Best yoga mat','A cushioned mat for yoga and floor work. The listing describes the Gaiam Premium mat as 6mm.',['6mm cushioning, per the listing','Works for yoga and floor work'],['Cushioned mats are less firm than thin ones'],'Yoga, stretching and floor exercises.'),
   ('B0040EGNIU','Best for recovery','The roller for sore legs and backs: the TriggerPoint Grid 1.0 foam roller.',['Made for sore legs and backs'],['Recovery tool only'],'Anyone who wants to loosen up after a workout.'),
   ('B09DF9NWC7','Best cheap cardio','Cheap cardio that fits in a bag. The listing describes a tangle-free rapid speed jump rope.',['Tangle-free, per the listing','Fits in a bag'],['Needs some open space to swing'],'Cardio at home or on the road.'),
   ('B00NH9WEUA','Best for serious cardio','The air rower with the PM5 monitor, the Concept2 RowErg indoor rowing machine.',['Air rower','PM5 monitor, per the listing'],['A bigger purchase and a bigger machine than the rest'],'People who want a full cardio machine at home.'),
  ],
  'criteria':[
   ('Start with how you want to train','Adjustable dumbbells or a kettlebell for strength, a mat for floor work, and a jump rope or rower for cardio.'),
   ('Space matters','The BowFlex dumbbells are listed as saving floor space, and the jump rope fits in a bag. The rower is the largest item here.'),
   ('Add accessories later','The Amazon Basics neoprene weights, Trideer yoga ball, wrist straps and gloves are in the FitWorth Top 10 too, if you want to add more.'),
  ],
  'faqs':[
   ('Do I need a lot of equipment?','No. A pair of adjustable dumbbells or a kettlebell, plus a mat, covers a lot of ground. Add cardio gear if that is your goal.'),
   ('Dumbbells or a kettlebell?','The BowFlex dumbbells adjust, which saves space. The kettlebell is a cast iron bell made for swings and squats.'),
  ]}],
 'bath':[{
  'slug':'best-bathroom-towels-and-basics',
  'title':'Best Bathroom Towels and Basics',
  'desc':'Six bathroom picks from the BathWorth Top 10: bath towels, a full towel set, washcloths, a bath rug, a shower curtain liner and a rain shower head.',
  'date':'2026-11-09',
  'intro':'Towels, a rug and a shower setup make most of a bathroom. These six picks come from the BathWorth Top 10, one for each job.',
  'picks':[
   ('B08LBN2JPS','Best big towels','Big towels that dry you off. The listing is a 4-piece set of extra large 30 x 60 bath towels from Tens Towels.',['4 pieces, per the listing','Extra large, 30 x 60, per the listing'],['Large towels take more room to store and dry'],'Anyone who wants a big towel after a shower.'),
   ('B00Q7JESL0','Best towel set','A full towel set for less. The listing describes the Amazon Basics 6-piece cotton towel set.',['6 pieces, per the listing','Cotton, per the listing'],['Smaller towels than the extra large set'],'Stocking a bathroom with towels in one go.'),
   ('B010S5VXKC','Best washcloths','Washcloths that dry between uses. The listing describes Amazon Basics fast drying cotton washcloths.',['Fast drying, per the listing','Cotton, per the listing'],['Washcloths only'],'Anyone who wants washcloths that do not stay damp.'),
   ('B0CFGYFCYL','Best bath rug','A soft rug that soaks up the drips. The listing describes a 30x20 chenille bathroom rug from OLANLY.',['Soft chenille, per the listing','30x20 size, per the listing'],['Small enough that a wide tub may want a bigger rug'],'Keeping the floor by the tub or shower dry.'),
   ('B08QRFZ6TH','Best liner','A clear liner that keeps the floor dry, the Barossa Design shower curtain liner.',['Clear','Keeps the floor dry'],['Liner only; it does not replace a curtain if you want a decorative one'],'Anyone replacing a worn shower liner.'),
   ('B0DQHJR1YB','Best shower upgrade','Rain head plus a handheld for rinsing. The listing describes a rain shower head with a handheld showerhead.',['Rain head plus handheld, per the listing'],['Check that it fits your shower arm before you buy'],'Rinsing off and shower-time cleanup.'),
  ],
  'criteria':[
   ('Towel size or set','Choose the Tens Towels for size, or the Amazon Basics 6-piece set if you want towels for the whole bathroom.'),
   ('Dry between uses','Washcloths and rugs that dry quickly are what the Amazon Basics washcloths and the OLANLY chenille rug are listed for.'),
   ('Other bathroom basics','The simplehuman soap pump and step can, the Etekcity scale and the Moen grab bar are in the BathWorth Top 10 too.'),
  ],
  'faqs':[
   ('Bath towels or a full set?','Buy the Tens Towels for big bath towels. Buy the Amazon Basics set if you want bath, hand and washcloth pieces together for less.'),
   ('Do I need a liner and a curtain?','A clear liner like the Barossa is listed as keeping the floor dry. Whether you also use a curtain is up to you.'),
  ]}],
 'travel':[{
  'slug':'best-travel-essentials',
  'title':'Best Travel Essentials',
  'desc':'Seven travel essentials from the TravelWorth Top 10: noise cancelling headphones, a power bank, a plug adapter, luggage scale, packing cubes and more.',
  'date':'2026-11-09',
  'intro':'The right small kit makes a trip easier. These seven picks come from the TravelWorth Top 10 and cover flights, power and packing.',
  'picks':[
   ('B09XS7JWHH','Best headphones for the plane','Noise cancelling for the plane. The listing is the Sony WH-1000XM5 noise cancelling wireless headphones.',['Noise cancelling','Wireless'],['Over-ear headphones take space in a bag'],'Frequent flyers who want quiet.'),
   ('B0CCZ26B5V','Best for comfort','Comfortable noise cancelling for long trips: the Bose QuietComfort Headphones.',['Noise cancelling','Comfort on long trips'],['Over-ear headphones take space in a bag'],'Long flights where comfort matters most.'),
   ('B0GJTXVN9Z','Best for tracking your bag','Know where your bag is. The listing is a 4 pack of Apple AirTag (2nd Generation).',['4 pack, per the listing'],['Tracks items only; it does not protect them'],'Checked bags and anything easy to lose.'),
   ('B0CZ9M6X8Q','Best power bank','A pocket battery for a long travel day. The listing describes a 10,000mAh 30W Anker power bank.',['10,000mAh, per the listing','30W, per the listing'],['One bank will not charge everything forever'],'Long travel days away from an outlet.'),
   ('B0B27HX6P7','Best plug adapter','Plug in across Europe. The listing is a 2 pack of TESSAN European travel plug adapters.',['2 pack, per the listing','Made for Europe'],['Europe only, per the listing'],'Trips to Europe.'),
   ('B07QFTGGYF','Best luggage scale','Weigh the bag before the airline does. The listing is a travel inspira digital luggage scale.',['Digital','Weigh before you leave'],['Does one job'],'Staying under airline weight limits.'),
   ('B08S35399Y','Best for packing','Pack by cube, unpack in seconds. The listing is an 8 set of BAGAIL packing cubes.',['8 cubes, per the listing'],['Cubes add a little bulk to an empty bag'],'Anyone who wants an organized suitcase.'),
  ],
  'criteria':[
   ('Sony or Bose','Buy the Sony for the noise cancelling most travelers pick. Buy the Bose if comfort on long flights matters most.'),
   ('Power and plugs','A pocket battery covers the day, and a plug adapter covers the destination. Check that the adapter fits where you are going.'),
   ('Sleep and organization','The Loop and Mack\'s earplugs and the BAGSMART hanging toiletry bag are in the TravelWorth Top 10 too.'),
  ],
  'faqs':[
   ('Do I need both headphones?','No. Both the Sony and the Bose are listed for noise cancelling; pick one by whether you want our pick or the comfort pick.'),
   ('Is the plug adapter for every country?','The listing describes it as a European travel plug adapter, so check your destination.'),
  ]}],
 'watch':[{
  'slug':'best-watches-for-everyday-wear',
  'title':'Best Watches for Everyday Wear',
  'desc':'Six everyday watches from the WatchWorth Top 10, from the Seiko 5 Sports automatic and Casio digitals to a Timex field watch and a Citizen Eco-Drive.',
  'date':'2026-11-09',
  'intro':'A good everyday watch does not need to be fancy. These six come from the WatchWorth Top 10, from a classic digital to an automatic.',
  'picks':[
   ('B07ZJW4WZG','Best automatic','The automatic most people start with: the SEIKO 5 Sports Automatic watch for men.',['Automatic'],['Costs more than the Casio picks'],'Anyone who wants a mechanical watch to wear for years.'),
   ('B000GAWSDG','Best cheap digital','The classic cheap digital: the Casio F91W.',['Digital','Low cost'],['Basic features'],'A simple, low-cost watch.'),
   ('B009KYJAJY','Best value analog','A 200M water-resistant analog for less. The listing is the Casio MDV106 analog watch.',['200M water-resistant, per the listing','Analog'],['Quartz, not automatic'],'Everyday wear on a budget.'),
   ('B071RN6K8C','Best field watch','A field watch that takes a beating. The listing is the Timex Men\'s Expedition Scout 40mm.',['40mm, per the listing','Field-watch style'],['A larger case than the Weekender'],'Rough everyday use.'),
   ('B004VR9HP2','Best everyday','The easy everyday watch. The listing is the Timex Weekender 38mm.',['38mm, per the listing'],['Simple styling'],'Wearing every day without thinking about it.'),
   ('B09X1B645K','Best no-battery-swaps','Eco-Drive, so no battery swaps. The listing is the Citizen Men\'s Classic Eco-Drive watch.',['Eco-Drive, per the listing','No battery swaps'],['Classic styling only'],'Anyone who wants a watch that needs little upkeep.'),
  ],
  'criteria':[
   ('Automatic or quartz','The Seiko 5 is an automatic. The Casio MDV106 gives a similar look for far less in a quartz watch.'),
   ('Digital or analog','The Casio F91W is the classic cheap digital; the Casio MDV106 and the Timex watches are analog picks.'),
   ('More to look at','The Casio AE1200WH and AE1500WH, the G-Shock GA-2100 and the Garmin Forerunner 265 are in the WatchWorth Top 10 too.'),
  ],
  'faqs':[
   ('Seiko or Casio?','Buy the Seiko if you want an automatic you will wear for years. Buy the Casio MDV106 if you want the same look for far less.'),
   ('What does Eco-Drive mean?','The listing describes the Citizen as Eco-Drive, so no battery swaps.'),
  ]}],
}
