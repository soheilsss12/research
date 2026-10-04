# F-03 — Tech Pack تا تأیید نمونه و قفل انتشار تولید انبوه

**نوع پرونده:** تحقیق بازارِ desk-research؛ بخشی از desk research قبلاً انجام شده و در این پرونده تجمیع شده است.
**بازار:** B2B
**تصمیم فعلی:** Watch / فرضیهٔ مشروط؛ **نه Pass و نه توصیهٔ ساخت.**
**تاریخ:** ۱۲ مهر ۱۴۰۵ / ۴ اکتبر ۲۰۲۶
**سطح اطمینان:** بالا برای category جهانی و substituteهای ایران؛ پایین برای وجود pain قابل پرداخت در ICP ایران.

---

---

## ۱. خلاصهٔ مدیریتی (Executive Summary)
**F:** منابع رسمی Techpacker و Uphance، BOM، POM/grade، version history، همکاری سازنده و approval را به‌عنوان recordهای متصل مطرح می‌کنند؛ version drift و stale BOM failure modeهای واقعی product category هستند. [F03-S01][F03-S13–S15]

**F:** ایران ابزارهای عمومی، آموزش Illustrator، service تولید و ERPهای BOM/production دارد؛ desk-research هیچ evidence قابل اتکایی از WTP برای یک لایهٔ مستقل handoff ارائه نمی‌کند. [F03-S07–S12]

**نتیجه:** F-03 فقط Watch است. فرضیهٔ مجاز، record محدود «sample approval تا bulk release» است؛ نه PLM، ERP، CAD یا marketplace با نام جدید.

## ۲. مقدمه، زمینهٔ کسب‌وکار و اهداف پژوهش (Introduction, Business Context & Objectives)
### تعریف دقیق محصول
یک لایهٔ بسیار باریک برای برند پوشاکِ چندکارگاهی که یک **record نسخه‌دار از Tech Pack، BOM، عکس/annotation نمونه، fit feedback، approval و نسخهٔ immutable production-release** ایجاد می‌کند و دریافت نسخهٔ درست توسط کارگاه را قابل مشاهده می‌سازد.

### مرز محصول

- PLM کامل، ERP، MRP، costing suite، CAD/3D patternmaking یا marketplace تولید نیست؛
- generator مبتنی بر AI برای ساخت PDF یا image نیست؛
- مدیریت خط دوخت، ظرفیت، PO، خرید مواد یا QC اجرایی نیست؛
- service نمونه‌دوزی/تأمین/تولید مدیریت‌شده نیست.

### مسئلهٔ قابل آزمون
تیم‌های برند و کارگاه‌های برون‌سپار، tech pack، BOM، اندازه، اصلاحات fit و نمونه‌های چندمرحله‌ای را با Excel/Illustrator/PDF/WhatsApp/email/Drive ردوبدل می‌کنند. در این setting، سه failure mode جهانی قابل‌مشاهده است:

1. factory با revision قدیمی کار می‌کند؛
2. عکس/annotation یا fit comment به record صحیح style وصل نمی‌ماند؛
3. BOM یا approval نمونه با release نهایی production همگام نیست.

وجود این failure mode در ایران هنوز باید با artifact واقعی اثبات شود.

---

## ۳. روش‌شناسی پژوهش و محدودیت‌ها (Research Methodology & Limitations)
این پرونده بر desk-research، منابع عمومی و تحلیل workflow/جایگزین‌ها استوار است. مصاحبه، پیمایش، پایلوت و دادهٔ تراکنشی محلی تا این نسخه انجام نشده‌اند مگر آن‌که صراحتاً در متن خلاف آن ثبت شده باشد. صفحات vendor برای اثبات category یا قابلیت محصول به‌کار می‌روند، نه به‌تنهایی برای اثبات اندازهٔ بازار ایران، پرداخت‌پذیری یا نبود رقیب. همهٔ شکاف‌ها باید در گیت فصل ۱۳ آزموده شوند.

### ۳-۱. بازبینی واقعی منابع در ۱۲ مهر ۱۴۰۵

راهنمای رسمی Techpacker همکاری مستقیم با سازنده، فایل/پیام در یک workspace و استفادهٔ مجدد از BOM/POM را توضیح می‌دهد؛ صفحهٔ قیمت، tier و قیمت‌گذاری ارزی محصول خارجی را منتشر می‌کند. Uphance نیز BOM، POM/grade، approval، version history و ارتباط با procurement/production را در یک product record شرح می‌دهد. این شواهد، existence و feature-boundary category را تقویت می‌کند؛ هیچ‌یک نرخ خطا، حجم برندهای ایران یا قیمت قابل پرداخت ایران را اندازه نمی‌گیرند. [F03-S13–S15]

## ۴. نمای کلی بازار و صنعت (Market & Industry Overview)
### ۳-۱. ابزار سبک: Techpacker

Techpacker، طبق feature page خود، BOM، libraries، PDF/Excel export، real-time collaboration، version control، portal سازنده و stage tracking را ارائه می‌کند؛ edits بین versionها برای سازنده برجسته می‌شود. [F03-S02] یک مقایسهٔ CLO-SET نیز آن را ابزار tech-pack سبک برای خروج از Excel با قیمت منتشرشدهٔ حدود ۴۹ دلار برای هر کاربر در ماه (در زمان بررسی) معرفی می‌کند. [F03-S03]

### ۳-۲. collaboration/PLM: Delogue

Delogue product development، supplier collaboration، BOM، sample request/status، comments/files/approvals و change log را حول shared style record قرار می‌دهد و از ۳۰۰+ fashion/lifestyle brand در ۷۴ کشور نام می‌برد. [F03-S04][F03-S05] این رقم vendor claim است، اما نشان می‌دهد supplier-facing version/approval workflow یک category استفاده‌شده است.

### ۳-۳. connected PLM: Uphance

Uphance Tech Pack، BOM، materials، approvals و version history را در یک record محصول و در اتصال با inventory/production معرفی می‌کند. خود شرکت ۱۴ style × ۳ colorway × ۶ size × ۴ review round را مثال complexity می‌زند؛ این مثال marketing است و market statistic نیست. [F03-S06] راهنمای آن، stale BOM، version drift و approval logging را از failure modeهای اصلی می‌داند. [F03-S01]

### ۳-۴. نتیجهٔ جهانی

| لایه | نمونه | کاربر مناسب | نتیجه برای thesis |
|---|---|---|---|
| Tech-pack workspace | Techpacker | فرد/تیم کوچک تا متوسط با نیاز به spec و share | اثبات می‌کند «document collaboration» به‌تنهایی محصول قابل فروش است. |
| supplier collaboration PLM | Delogue | برندهای product-development با vendorهای متعدد | نشان می‌دهد sample/comments/approval باید کنار style record بماند. |
| PLM/ERP connected | Uphance/WFX/Centric | برندهای پیچیده‌تر با data spine عملیاتی | نشان می‌دهد full-suite دامنهٔ بزرگی دارد و ورود به آن با scope فعلی ناسازگار است. |

بنابراین category جهانی معتبر است؛ white space ایران فقط در صورتی معنا دارد که **نقطهٔ handoff بسیار باریک** هم درد مشخص و هم عدم کفایت substitute محلی را اثبات کند.

---

## ۵. اندازه، ساختار و پویایی تقاضای بازار (Market Sizing, Structure & Demand)
داده‌های اندازه، تقاضا و مدل درآمد که در این desk-research قابل مشاهده بوده‌اند در فصل ۹ ثبت شده‌اند؛ هر رقم یا denominatorِ ناقص، برآورد/فرضیه است و به‌جای رقم قطعی، مسیر جمع‌آوری داده در فصل ۱۳ آمده است.

## ۶. بازار هدف، بخش‌بندی و مشتری (Target Market, Segmentation & Customer)
تقسیم‌بندی، نقش buyer/user و مرز B2B/B2C فقط در حد شواهد موجود در این پرونده بیان می‌شود. هیچ persona، حجم segment یا WTP بدون دادهٔ اولیه قطعی تلقی نمی‌شود؛ معیار نمونه و نقش‌های مورد نیاز برای تأیید در فصل ۱۳ ثبت شده‌اند.

## ۷. بینش مشتری، نیاز، رفتار خرید و قیمت‌پذیری (Customer Insights, Buying Behaviour & Willingness-to-Pay)
Tech pack یک «فایل طراحی» صرف نیست؛ در عمل specification/contract فنی میان برند و کارخانه است. اجزای متعارف آن عبارت‌اند از flat، points of measurement، BOM، construction، color/material، size/grade، finishing، packaging و approval log. [F03-S01]

### مرز process

`design concept → technical flat → Tech Pack + BOM → pattern/sample → fit comments → revised sample → pre-production sample → locked bulk-release → production order`.

این پرونده فقط از نقطهٔ **Tech Pack آمادهٔ اشتراک** تا **approved bulk-release** را بررسی می‌کند. الگو‌سازی/CAD قبل از آن و production execution بعد از آن، مسیرهای جدا و قبلاً ردشده‌اند.

### record حداقلی محصول

| جزء | چرا باید نسخه‌دار باشد | کاربر اصلی |
|---|---|---|
| Style card و technical flat | مرجع هویت مدل و تغییر طراحی | technical designer / product developer |
| BOM و material/trims | جلوگیری از نمونه یا هزینه بر اساس خرجکار قدیمی | sourcing / factory liaison |
| POM/size/grade | تعیین fit و تحمل اندازه | patternmaker / factory |
| عکس نمونه و annotation | تبدیل feedback مبهم به دستور اجرایی | designer / sample room |
| sample round | تفکیک proto، fit، PP و production sample | product development |
| approval/rejection | روشن‌بودن اینکه چه کسی، چه چیزی و در کدام version را تأیید کرده است | manager / founder / factory |
| bulk-release snapshot | جلوگیری از تغییر silent پس از مجوز تولید | برند و کارگاه |
| acknowledgement کارخانه | اثبات دریافت نسخهٔ release، نه صرفاً ارسال فایل | factory contact |

---

## ۸. چشم‌انداز رقابتی و جایگزین‌ها (Competitive Landscape & Substitutes)
### ۴-۱. شواهد مهارتی/فرآیندی

آموزش Illustrator در طراحی لباس در ایران ارائه می‌شود و Tech Pack در منابع/دوره‌های تخصصی به‌صورت Excel/Illustrator/PDF شناخته شده است. وجود این آموزش‌ها به معنی وجود SaaS نیست، اما نشان می‌دهد userها می‌توانند ابزار اولیه را به‌کار بگیرند. [F03-S07]

### ۴-۲. service substitute

روچی اسمارت الگوسازی، نمونه‌دوزی، اصلاح تا تأیید مشتری، تأمین پارچه/خرجکار، برش، دوخت و QC را به‌صورت service عرضه می‌کند. [F03-S08] این جایگزین به جای حل software handoff، بخشی از عملیات را برای مشتری انجام می‌دهد؛ پس هم رقیب غیرمستقیم و هم شاهدی برای وجود فرایند sample/approval است.

### ۴-۳. ERP/production substitute

راهکارهای پوشاک محلی مانند آرمان تدبیر پوشاک، معین، هلو، محک و پارمیس، BOM، تولید، مواد، انبار، هزینه، QC یا مراحل برش/دوخت را پوشش می‌دهند. [F03-S09–S12] این‌ها دلیل مهمی هستند که محصول نباید به production/ERP گسترش یابد. در desk scan، evidence عمومی روشن از محصول محلیِ SaaS که دقیقاً versioned tech pack + photo fit annotation + sample approval + locked bulk release را ارائه کند پیدا نشد؛ این یک **شکاف مشاهده‌پذیری** است، نه اثبات نبود رقیب.

### ۴-۴. substitute map

| جایگزین | قوت | شکست محتمل که باید ثابت شود |
|---|---|---|
| Excel/Illustrator/PDF | انعطاف، آشنایی، هزینه کم، export آسان | نسخه‌های متعدد، عدم audit، comment جدا، BOM ناسازگار. |
| WhatsApp/Telegram/email | سرعت و adoption بالا | تصمیم/عکس در thread گم می‌شود، factory confirmation مبهم است. |
| Drive/shared folder | archive ساده و permission پایه | current-version و release discipline را enforce نمی‌کند. |
| مدیر فنی/الگوساز باتجربه | دانش tacit و حل‌مسئله فوری | scale وابسته به فرد و عدم انتقال دانش. |
| managed service مانند روچی | کاهش بار مشتری تا sample approved | عملیات فیزیکی و service dependency؛ system-of-record مستقل نیست. |
| ERP تولید پوشاک | BOM، stock، costing، production/quality | غالباً نقطهٔ design/sample/factory comment با UX تخصصی را هدف نمی‌گیرد؛ باید در interview audit شود. |

---

## ۹. ارزیابی مفهوم محصول، مدل کسب‌وکار و قیمت‌گذاری (Product Concept, Business Model & Pricing Assessment)
### ICP فرضی و exclusions

| ICP احتمالی | نشانهٔ qualifying | exclusion |
|---|---|---|
| برند دارای ۱۵–۲۰+ style فعال در season و بیش از یک round نمونه | چند کارگاه یا sample room، چند نفر در design/product، revision واقعی | مزون تک‌نفره یا کارگاه تک‌مدل با یک سازنده؛ Excel احتمالاً کافی است. |
| برند چندکارگاهی/برون‌سپار | sender و receiver متفاوت و handoff تکرارشونده | کارخانهٔ یکپارچه که یک نفر هم design و هم تولید را انجام می‌دهد. |
| product/technical manager با metric کیفیت/زمان | owner مشخص برای approval و release | teamی که approve رسمی ندارد یا نمی‌تواند policy رعایت کند. |

### روش sizing لازم

اندازهٔ market با «فروش کل پوشاک ایران» قابل برآورد نیست. مدل لازم:

`SAM = تعداد برندهای واجد criteria × درصد multi-workshop × نرخ پذیرش × ARPA سالانه`.

برای ساختن آن باید account mapping و interview انجام شود: تعداد style/season، round نمونه، factory، نفر-ساعت review، rework، launch delay، budget owner و willingness pilot. تا پیش از آن، TAM/SAM/SOM پولی گزارش نمی‌شود.

### مدل درآمدی مشروط

- اشتراک به‌ازای brand workspace یا active styles/season؛
- factory collaborator با role محدود؛
- onboarding/import paid؛
- نه commission سفارش تولید و نه marketplace fee؛
- قیمت باید از هزینهٔ یک revision اشتباه/یک sample round اضافه یا زمان senior staff anchor بگیرد؛ فعلاً هیچ price point ایران تأیید نشده است.

---

## ۱۰. امکان‌سنجی اجرایی، حقوقی و عملیاتی (Operational, Legal & Commercial Feasibility)
### MVP فقط برای گیت validation

1. style workspace و revision history؛
2. POM/BOM و attachment؛
3. عکس نمونه با pin/annotation و fit comment؛
4. sample-round status و responsible/decision log؛
5. approved/rejected action با timestamp؛
6. read-only immutable bulk-release PDF/snapshot؛
7. acknowledgement link موبایلی برای کارگاه؛
8. import/export Excel/PDF برای سازگاری با workflow موجود.

### Non-goals

CAD، 3D fitting، pattern making، auto-generation با AI، sourcing marketplace، PO/warehouse/accounting، capacity control، AQL inspection و production execution خارج از scope هستند.

### ریسک‌های تعیین‌کننده

| ریسک | چرا مهم است | آزمون/کاهش |
|---|---|---|
| Excel/WhatsApp واقعاً کافی باشد | نرم‌افزار جدید switching cost بدون ROI دارد | artifact-based interview، اندازه‌گیری revision/rework و paid pilot. |
| کارخانه collaborator نشود | single source of truth شکست می‌خورد | frictionless view/acknowledgement بدون account کامل. |
| volume style پایین باشد | ARPA/renewal کافی نیست | ICP filter پیش از sales؛ no SMB-general positioning. |
| scope به PLM/ERP بزرگ شود | با مسیر ردشده overlap و implementation سنگین می‌شود | core metric فقط accuracy/time handoff تا release. |
| data entry بار اضافه ایجاد کند | تیم به message بازمی‌گردد | import از Excel/PDF، annotation سریع و یک action برای approval. |
| approval در عمل informal باشد | immutable release بی‌استفاده می‌شود | مصاحبه دربارهٔ آخرین bulk approval و authority واقعی. |

---

## ۱۱. یافته‌ها، تحلیل و ارزیابی فرصت (Findings, Analysis & Opportunity Assessment)
**تفکیک تحلیلی:** فصل‌های ۴ تا ۱۰ «یافته‌ها و شواهد موجود» را نگه می‌دارند؛ نتیجه‌گیری فصل ۱۲ تفسیر محافظه‌کارانهٔ آن‌هاست. نبود محصول یا عدد در منابع عمومی، به‌تنهایی evidence سفیدبودن بازار نیست. counter-thesis، ریسک و limitationهای عملیاتی باید بر توصیه مقدم باشند.

### ۱۱-۱. نتیجهٔ بازبینی شواهد

**F:** ابزار سبک (Techpacker) و platform متصل (Uphance) هر دو «current version، BOM/POM، comment/approval و supplier handoff» را مسئله‌ای مستقل می‌دانند. [F03-S13–S15]

**I:** این هم‌پوشانی خطر اصلی پرونده است: اگر account ایران واقعاً به procurement، PO، costing یا QC نیاز داشته باشد، wedge کوچک به PLM/ERP تبدیل می‌شود و باید رد شود؛ اگر فقط freeze/release و acknowledgement مشکل باشد، scope محدود ممکن است قابل آزمون بماند.

**H / شرط رد:** قیمت ارزی Techpacker و مثال‌های marketing خارجی anchor قیمت ایران نیستند. تنها purchase signal قابل قبول، دو pilot پولی با styleهای واقعی و بازشدن release توسط دست‌کم دو کارگاه است.

## ۱۲. نتیجه‌گیری و توصیهٔ راهبردی (Conclusions & Strategic Recommendation)
**F-03 در وضعیت Watch باقی می‌ماند.** category جهانی از ابزار lightweight تا PLM enterprise به‌خوبی اثبات شده، اما full PLM/ERP قبلاً رد شده و substituteهای محلی/دستی واقعی‌اند. تنها thesis قابل‌تحقیق، یک wedge بسیار محدود در مرز sample approval و production release است؛ نه یک نام جدید برای PLM.

گیت این پرونده از market size عمومی عبور نمی‌کند؛ از مشاهدهٔ artifact واقعی و فروش pilot می‌گذرد. تا آن زمان، هیچ ادعایی دربارهٔ gap ایران، willingness-to-pay یا قیمت مناسب معتبر نیست.

---

## ۱۳. برنامهٔ اعتبارسنجی بعدی و گیت تصمیم (Validation Plan & Decision Gate)
### مصاحبهٔ artifact-based: حداقل ۱۵ نفر

- ۵ مدیر محصول/technical designer یا founder برند؛
- ۴ الگوساز/مدیر نمونه یا sample room؛
- ۳ manager/owner کارگاه؛
- ۳ sourcing/production coordinator یا QC که handoff را می‌بینند.

برای آخرین سه style، این داده‌ها باید جمع شود: version count، channelهای استفاده‌شده، نمونه‌ها، عکس/comment، اشتباه/تاخیر، هزینه، current approval، factory access و willingness برای استفاده از record جدا.

### گیت pilot

- دو برند، هر کدام یک collection فعال یا ۱۵–۲۰ style؛
- حداقل دو کارگاه external که link/snapshot را واقعاً باز و acknowledge کنند؛
- pilot پولی ۶ تا ۸ هفته؛
- baseline و post-pilot برای ambiguity، sample mismatch، chasing time و rework ثبت شود.

### hard kill

رد اگر: (۱) دست‌کم دو pilot پولی فروخته نشود؛ (۲) درد stale-version/sample mismatch تکرارشونده و هزینه‌دار نباشد؛ (۳) کارگاه‌ها release record را استفاده/acknowledge نکنند؛ یا (۴) اکثریت ICP از ERP/Excel/WhatsApp خود رضایت کافی داشته و migration cost را ناموجه بدانند.

---

## ۱۴. پیوست‌ها (Appendices)
| کد | رتبه | منبع | نکتهٔ استفاده‌شده | پیوند |
|---|---|---|---|---|
| F03-S01 | C (vendor) | Uphance — Mastering the Tech Pack، بازیابی ۱۲ مهر ۱۴۰۵ | اجزای Tech Pack، approval log و failure modeهای stale BOM/version drift. | https://www.uphance.com/insights/mastering-tech-pack/ |
| F03-S02 | C (vendor) | Techpacker — Features، بازیابی ۱۲ مهر ۱۴۰۵ | portal، version control، supplier collaboration، stages و export. | https://techpacker.com/features/ |
| F03-S03 | C (industry comparison) | CLO-SET — 8 product-development tools compared، بازیابی ۱۲ مهر ۱۴۰۵ | positioning ابزار سبک و قیمت اعلام‌شده در زمان بررسی. | https://style.clo-set.com/en/resources/article/do-you-need-a-fashion-plm-8-product-development-tools-compared-d3a24e2976254e4ab816812436a4e780 |
| F03-S04 | C (vendor) | Delogue — Fashion PLM، بازیابی ۱۲ مهر ۱۴۰۵ | ۳۰۰+ برند/۷۴ کشور و supplier collaboration. | https://www.delogue.com/en/solutions/industries/fashion |
| F03-S05 | C (vendor) | Delogue — Core Features، بازیابی ۱۲ مهر ۱۴۰۵ | BOM, samples, comments, approvals و audit/change log. | https://www.delogue.com/en/platform/core-features |
| F03-S06 | C (vendor) | Uphance — Apparel PLM، بازیابی ۱۲ مهر ۱۴۰۵ | connected tech pack/BOM/sample/approval workflow و PLM vs ERP. | https://www.uphance.com/apparel-plm/ |
| F03-S07 | C (training provider) | مجتمع فنی تهران میرداماد — آموزش Illustrator در طراحی لباس، بازیابی ۱۲ مهر ۱۴۰۵ | سیگنال دسترسی به ابزار Illustrator در ایران؛ نه محصول SaaS. | https://mftmirdamad.com/product/آموزش-نرم-افزار-ایلاستریتور-طراحی-ل-2/ |
| F03-S08 | C (vendor) | روچی اسمارت، بازیابی ۱۲ مهر ۱۴۰۵ | managed service الگوسازی، نمونه، اصلاح، تامین و تولید. | https://rochismart.com/ |
| F03-S09 | C (vendor) | آرمان تدبیر پوشاک، بازیابی ۱۲ مهر ۱۴۰۵ | BOM، تولید، زمان‌بندی و QC پوشاک. | https://gctco.ir/arman-tadbir-pooshak/ |
| F03-S10 | C (vendor) | معین — حسابداری تولیدی پوشاک، بازیابی ۱۲ مهر ۱۴۰۵ | مراحل تولید، مواد، ضایعات و تولید برون‌سپاری. | https://moeinsoft.com/product/garment-production-accounting-software/ |
| F03-S11 | C (vendor) | هلو — حسابداری مانتو و پوشاک، بازیابی ۱۲ مهر ۱۴۰۵ | پنل تولید، مواد و عملیات برش/دوخت. | https://holooshop.com/product/نرم-افزار-حسابداری-مانتو-و-پوشاک-جامع-ه/ |
| F03-S12 | C (vendor) | پارمیس — حسابداری تولیدی پوشاک، بازیابی ۱۲ مهر ۱۴۰۵ | تولید، BOM و برنامه‌ریزی مواد اولیه. | https://www.parmisit.com/products/acconting-software/small-bussiness-solution/clothing/ |

| F03-S13 | C (vendor documentation) | Techpacker Help Center — *What is Techpacker?*، بازیابی ۱۲ مهر ۱۴۰۵ | BOM/POM reuse، collaboration و ارتباط مستقیم با manufacturer؛ category proof. | https://helpcenter.techpacker.com/hc/en-us/articles/360016021274-What-is-Techpacker- |
| F03-S14 | C (vendor pricing) | Techpacker — Pricing، بازیابی ۱۲ مهر ۱۴۰۵ | tier و قیمت دلاری منتشرشده؛ فقط product/pricing-model خارجی، نه price anchor ایران. | https://techpacker.com/pricing/ |
| F03-S15 | C (vendor) | Uphance — *Mastering the Tech Pack*، ۳۰ آوریل ۲۰۲۶، بازیابی ۱۲ مهر ۱۴۰۵ | stale BOM/version drift و version/approval/factory portal workflow. | https://www.uphance.com/insights/mastering-tech-pack/ |

### پیوست ب. تغییرنگار

| نسخه | تاریخ | تغییر |
|---|---|---|
| ۲٫۰ | ۱۲ مهر ۱۴۰۵ | عنوان‌ها و hierarchy بدون حذف body یا evidence پیشین، به قالب استاندارد گزارش تحقیقات بازار تبدیل شد؛ این اقدام به معنی انجام پژوهش اولیه نیست. |
| ۲٫۱ | ۱۲ مهر ۱۴۰۵ | بازبینی واقعی منابع Techpacker/Uphance، مرز product category و ریسک PLM/ERP overlap افزوده شد؛ Watch و نبود primary evidence حفظ شد. |
