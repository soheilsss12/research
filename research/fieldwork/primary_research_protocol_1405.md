# پروتکل مشترک پژوهش اولیه و آزمون WTP — پرتفوی فشن ایران

**نسخه:** ۱٫۲
**تاریخ:** ۱۲ مهر ۱۴۰۵ / ۴ اکتبر ۲۰۲۶
**وضعیت:** ابزار و طرح اجرایی آماده؛ **هیچ مصاحبه، پیمایش، استخدام پاسخ‌دهنده، پرداخت، مشاهدهٔ artifact، pilot یا نتیجه‌ای تا این لحظه اجرا نشده است.**

## ۱. هدف و مرز استفاده

این پروتکل از منطق «پیمایش و رضایت مشتری» در قالب ۳ استفاده می‌کند، اما گزارش پیمایش نیست. پس از اجرای واقعی، فقط داده‌های ثبت‌شده (n، روش نمونه‌گیری، نرخ پاسخ، پرسشنامهٔ نهایی، تاریخ و raw/cleaned data) می‌توانند بخش یافته‌ها، جداول رضایت یا نمودارهای قالب ۳ را پر کنند. خانه‌های خالی با نمونه یا دادهٔ مصنوعی پر نمی‌شوند.

هدف مشترک، ایجاد دو input لازم برای مدل‌های TAM/SAM/SOM است:

1. **denominator واجد شرایط:** تعداد/فهرست واقعی account یا transaction که تعریف مشتری را دارد؛
2. **قیمت یا ARPA خالص محلی:** مبلغ مشاهده‌شده در خرید، یا پذیرش قیمت با روش WTP که currency، period، scope، buyer و discount آن روشن است.

قیمت فروشندگان خارجی فقط برای طراحی سؤال و feature scope استفاده می‌شود؛ به پاسخ‌دهنده گفته نمی‌شود، به ریال تبدیل نمی‌شود و price card پیشنهادی نیست.

## ۲. حکمرانی، اخلاق و ثبت شواهد

- پیش از شروع: هدف، مدت، نحوهٔ ضبط، نحوهٔ استفاده از نقل‌قول، و حق انصراف با رضایت روشن اعلام شود.
- از نام اشخاص، قرارداد، عکس محصول، فاکتور یا asset بدون مجوز استفاده نشود. برای artifact، نسخهٔ redacted کافی است.
- هیچ‌کس در ازای «پاسخ مطلوب» پول/تخفیف دریافت نمی‌کند. اگر honorarium وجود دارد، مبلغ و شیوهٔ آن جدا از outcome ثبت شود.
- هر پاسخ با شناسهٔ ناشناس، تاریخ، کانال recruitment، نقش، segment، consent، recorder، link/مسیر artifact و محدودیت ثبت شود.
- ادعای پاسخ‌دهنده، evidence نیست مگر با artifact، مشاهدهٔ workflow یا corroboration مستقل برچسب‌گذاری‌شده همراه باشد.
- raw file و identifiers جدا نگه‌داری شوند؛ در سند تصمیم فقط aggregate/نقل‌قول ناشناس منتشر شود.

### دفتر ثبت هر مصاحبه (اجباری)

| فیلد | مقدار موردنیاز |
|---|---|
| Interview ID | شناسهٔ یکتا، بدون نام شخص |
| پرونده / segment | F-01 تا F-07 و cohort مشخص |
| نقش | user، economic buyer، approver، expert یا substitute provider |
| eligibility | پاسخ دقیق screener و دلیل ورود/خروج |
| تاریخ/کانال/مصاحبه‌گر | برای audit و تکرارپذیری |
| consent | گفتگو/یادداشت/ضبط/artifact: هر مورد جدا |
| evidence | quote، artifact redacted، مشاهدهٔ workflow یا صرفاً stated preference |
| limitation | conflict، memory bias، referral bias، incomplete artifact یا سایر محدودیت‌ها |

## ۳. نمونه‌گیری و screener مشترک

نمونه‌گیری convenience صرف مجاز نیست؛ recruitment source و quota باید ثبت شود. نمونه‌ها برای برآورد آماری کل بازار کافی فرض نمی‌شوند مگر sampling frame و نرخ پاسخ واقعی وجود داشته باشد.

### ۳-۱. screener عمومی

1. آیا سازمان/شما در ۱۲ ماه اخیر واقعاً workflow مرتبط را انجام داده‌اید، نه فقط به آن علاقه نشان داده‌اید؟ مثال واقعی و زمان آخرین‌بار را بپرسید.
2. نقش شما چیست: انجام‌دهنده، مالک بودجه، تأییدکننده، تأمین‌کنندهٔ جایگزین یا مصرف‌کنندهٔ پرداخت‌کننده؟
3. آیا اجازه دارید فرآیند جاری را بدون افشای محرمانه توضیح دهید و حداقل یک artifact redacted ارائه/نمایش دهید؟
4. هزینهٔ زمانی/مالی یا پیامد آخرین failure چه بوده است؟ اگر پاسخ «نمی‌دانم» است، ثبت شود؛ حدس به‌جای data ننشیند.
5. آیا هیچ conflict (فروشنده بودن، همکاری با تیم پژوهش، یا انگیزهٔ تبلیغاتی) دارید؟

### ۳-۲. ورود اختصاصی و cohort پیشنهادی

| پرونده | وضعیت پژوهش | ورود قطعی | quota پیشنهادی برای discovery (نه n آماری) | artifact درخواست‌شده |
|---|---|---|---|---|
| F-01 | فعال | برند/آژانسی که در ۹۰ روز اخیر نمونه را برای creator/media جابه‌جا یا پیگیری کرده است | ۸–۱۲؛ حداقل ۳ brand، ۳ agency، ۲ نقش عملیات/marketing | sample log، message trail یا tracker redacted |
| F-02 | فعال | costume lead / wardrobe / production که در ۱۲ ماه اخیر پروژهٔ تصویری با چند look اجرا کرده است | ۶–۱۰؛ نقش costume و production جدا | continuity sheet، rack/list یا handover redacted |
| F-03 | Watch | برند/کارگاه دارای سبک/نمونه/تأیید فنی میان بیش از یک نقش یا workshop | ۱۰–۱۵؛ product/technical/factory | tech pack، BOM، revision trail، QC handoff redacted |
| F-04 | Watch | خریدار/فروشندهٔ واقعی کالای premium یا کارشناس اصالت در ۱۲ ماه اخیر | ۱۲–۱۸ consumer/seller + ۳–۵ expert | receipt/listing، عکس item و dispute/process redacted |
| F-05 | آرشیوی | **بدون reversal صریح recruitment نشود.** | — | فقط پس از reversal: store planogram/photo audit redacted |
| F-06 | آرشیوی | **بدون trigger مستند recruitment نشود.** | — | فقط پس از trigger: accession/loan/condition record redacted |
| F-07 | Pause | **بدون reversal صریح کاربر هیچ recruitment، prototype test یا price test نشود.** | — | — |

quotaها برنامهٔ discovery هستند، نه «تعداد پاسخ‌های جمع‌آوری‌شده» و نه نمایندهٔ کل ایران. توقف زودهنگام فقط با ثبت saturation evidence مجاز است: در دو مصاحبهٔ consecutive جدید، code/product workflow تازه‌ای ظاهر نشده باشد؛ این یک معیار عملیاتی پیشنهادی است، نه ادعای saturation فعلی.

## ۴. راهنمای مصاحبهٔ نیمه‌ساختاریافته (۴۵–۶۰ دقیقه)

### ۴-۱. ترتیب مشترک

1. **نقش و نمونهٔ واقعی اخیر (۵ دقیقه):** آخرین مورد را دقیقه‌به‌دقیقه بازسازی کنید؛ چه کسی شروع کرد، چه کسی تأیید کرد، چه چیزی تحویل شد؟
2. **workflow و جایگزین (۱۰ دقیقه):** ابزارها، فایل‌ها، پیام‌رسان، Excel، انسان/خدمت، هزینهٔ زمان و handoffها را نشان دهید. «نداشتن رقیب» پاسخ معتبر نیست؛ روش دستی هم substitute است.
3. **failure و پیامد (۱۰ دقیقه):** آخرین error/rework/loss/delay چیست؟ frequency، owner، recoverability و evidence آن چیست؟
4. **buyer و procurement (۸ دقیقه):** user، economic buyer، approver، budget line، trigger خرید و cycle چه کسانی/چیزهایی‌اند؟
5. **concept card بی‌طرفانه (۵ دقیقه):** capability را بدون brand و بدون price خارجی نشان دهید؛ چه چیز باید درست باشد تا جایگزین جریان جاری شود؟
6. **WTP و trade-off (۵–۱۰ دقیقه):** طبق بخش ۵؛ ابتدا بازه و unit محلی، سپس test کنترل‌شده.
7. **artifact و follow-up (۵ دقیقه):** با اجازه، redacted record را دریافت/مشاهده و limitation را ثبت کنید.

### ۴-۲. سؤال‌های تشخیصی اختصاصی

- **F-01:** چند نمونه در هر campaign؟ owner custody کیست؟ آخرین گم‌شدن/دیرکردن چه شد؟ creator seeding و loan با چه trackerی انجام شد؟ آیا marketing یا operations پول می‌دهد؟
- **F-02:** چه تعداد look و handoff در production اخیر؟ continuity error چگونه کشف شد؟ offline/mobile requirement چیست؟ چه کسی روز filming تصمیم خرید می‌گیرد؟
- **F-03:** آخرین revision اشتباه چه بود؟ style/BOM/POM/sample sign-off کجا نسخهٔ حقیقت است؟ کارگاه چگونه latest approved version را می‌گیرد؟ هزینهٔ rework قابل رؤیت است؟
- **F-04:** آخرین معاملهٔ مشکوک، dispute یا برگشت چه بود؟ ارزش item، brand/model coverage، عکس لازم و اعتماد به expert چگونه سنجیده می‌شود؟ certificate دقیقاً چه تعهدی می‌آورد/نمی‌آورد؟
- **F-05 (فقط پس از reversal):** chain cadence، store compliance failure و راه‌حل incumbent چیست؟ آیا مشکل با ابزار مستقل حل می‌شود یا field service لازم دارد؟
- **F-06 (فقط پس از trigger):** condition/loan/migration/purchase committee و سامانه‌های موجود کدام‌اند؟ آیا standalone apparel workflow وجود دارد؟
- **F-07 (فقط پس از reversal):** پیش از هر concept test، سن/رضایت/ایمنی، genre fit، channel policy و moderation plan باید تصویب شود؛ از کودک/نوجوان بدون پروتکل اخلاقی مناسب داده نگیرید.

## ۵. تمرین WTP و price discovery

### اصل طراحی

قیمت را پیش از فهم workflow پیشنهاد ندهید. ابتدا از پاسخ‌دهنده بخواهید واحد خرید محلی را تعیین کند: per project، per account، per seat، per store، per verdict یا in-app purchase. سپس **بازه‌های محلیِ حاصل از discovery واقعی** را برای آزمون وارد کنید. عددهای `$`/`€`/`£` فروشندگان خارجی در کارت آزمون وارد نمی‌شوند.

### ۵-۱. B2B: Gabor–Granger کوتاه پس از discovery

برای F-01/F-02/F-03 و در صورت reversal F-05/F-06، concept card با scope ثابت (onboarding، تعداد user/project، support، storage و contract) ارائه شود. سه قیمت محلی از بازهٔ مشاهده‌شده انتخاب و ترتیب آن‌ها تصادفی شود. در هر قیمت بپرسید:

- آیا با این scope و این قیمت خرید را «قطعاً / احتمالاً / نامشخص / احتمالاً نه / قطعاً نه» می‌دانید؟
- چه کسی اختیار پرداخت دارد و از کدام budget line؟
- چه contract/procurement condition یا implementation cost مانع است؟
- نزدیک‌ترین substitute با چه هزینهٔ واقعی چیست؟

هیچ پاسخ لفظی به‌تنهایی ARPA نیست. «قیمت پذیرفته‌شده» تنها وقتی price evidence می‌شود که scope، buyer، currency، period، discount و احتمال/رفتار خرید روشن و قابل audit باشد.

### ۵-۲. F-04: per-verdict / bundle

دو unit جدا تست شود: **per item** و **bundle/listing volume**. price test باید value band item و risk/dispute context را نگه دارد. نتیجه با نوع کالای کم‌ارزش ادغام نشود. مالی/حقوقی بودن certificate یا guarantee سؤال جداست؛ willingness to pay برای verdict، تعهد حقوقی ایجاد نمی‌کند.

### ۵-۳. F-07

در وضعیت Pause هیچ WTP، ad test، prototype یا game survey اجرا نمی‌شود. بعد از reversal، price research فقط پس از سنجش genre fit، age-safe recruitment، retention design و channel policy شروع می‌شود؛ ARPPU فرضی از میانگین کل game purchase ساخته نمی‌شود.

## ۶. درخواست و بررسی artifact

artifact باید برای تأیید workflow باشد، نه جمع‌آوری بی‌رویهٔ داده:

- **حداقل:** screenshot/نسخهٔ redacted از tracker، handoff، revision، receipt، listing یا record مرتبط با آخرین case واقعی؛
- **برچسب:** تاریخ، نقش ارائه‌دهنده، آنچه ثابت می‌کند، آنچه ثابت نمی‌کند، و authorization؛
- **زنجیرهٔ استدلال:** هر claim در ledger با `F` (fact)، `I` (interpretation) یا `H` (hypothesis) ثبت شود؛ artifact به‌تنهایی volume کل بازار را نشان نمی‌دهد؛
- **عدم دریافت:** اگر artifact قابل ارائه نیست، interview حذف نمی‌شود اما evidence strength کاهش و علت ثبت می‌شود.

## ۷. طرح تحلیل و گزارش‌نویسی پس از اجرا

### ۷-۱. کدگذاری کیفی

codebook اولیه: `trigger`، `workflow-step`، `substitute`، `frequency`، `severity/cost`، `owner`، `buyer`، `approval`، `artifact-quality`، `WTP-unit`، `price-response`، `legal/operational blocker` و `segment`. دو نفر کدگذار برای نمونه‌ای از transcriptها اختلاف را reconciliation کنند؛ تعارض حذف نشود و در audit log بماند.

### ۷-۲. خروجی مجاز

1. جدول respondent/profile با n واقعی، recruitment source و exclusions؛
2. workflow map و substitute map، هرکدام با quote/artifact limitation؛
3. pain-frequency matrix بر اساس **تعداد مشاهده‌شده**، نه درصدی که از نمونهٔ غیرتصادفی به کل کشور تعمیم داده شده باشد؛
4. price-response curve فقط با currency/unit/scope ثابت، n و missing responses؛
5. denominator construction log: frame، inclusion/exclusion، duplicate rule، تاریخ snapshot و coverage gap؛
6. مدل TAM/SAM/SOM با formula، source id، period، assumptions، sensitivity و explicit unknowns؛
7. verdict: continue، revise، hold یا kill. نتیجهٔ منفی/بی‌نتیجه باید به همان صراحت ثبت شود.

### ۷-۳. قواعد منع گزارش‌دهی

- پاسخ لفظی = بازار کل، نیست.
- quote فروشنده = قیمت ایران، نیست.
- تعداد مصاحبه = سهم بازار، نیست.
- ۳۴٫۳٪ gamer share یا ۵۲۰ میلیارد تومان proxy مایکت = TAM فشن‌گیم، نیست.
- عدم مشاهدهٔ مشکل در sample کوچک = نبود مشکل در بازار، نیست.

## ۸. گیت‌های پیشنهادی تصمیم

پیش از recruitment، تیم باید در decision log تعریف کند که چه evidenceی ادامه را مجاز می‌کند. حداقل گیت مشترک:

| گیت | شاهد لازم | fail / hold condition |
|---|---|---|
| مسئله | workflow واقعی + failure/cost از چند segment | علاقهٔ لفظی بدون case/artifact |
| buyer | نقش و budget/procurement path مشخص | user وجود دارد اما buyer/بودجه نامعلوم است |
| تمایز platform | قابلیت به‌صورت software-only از substitute جداست | راه‌حل به service/logistics/field operation وابسته است |
| قیمت | unit و scope محلی + پاسخ WTP/transaction قابل audit | تنها external price یا حدس وجود دارد |
| اندازه بازار | frame یا account/transaction map واجد | category total یا proxy نامرتبط تنها input است |
| ریسک | legal/data/moderation/implementation review | hard blocker بدون mitigation قابل آزمون |

F-05 و F-06 علاوه بر این، reversal/trigger ثبت‌شده لازم دارند؛ F-07 reversal صریح کاربر و review ایمنی/محتوا را پیش‌شرط دارد.

## ۹. بستهٔ خروجی بعد از اجرای واقعی

1. نسخهٔ frozen screener و interview guide؛
2. recruitment log و disposition؛
3. consent log جدا از research data؛
4. transcript/notes و artifact index redacted؛
5. codebook و decision log؛
6. Excel sizing model با source-level inputs و formulas؛
7. گزارش قالب ۳ با n/response-rate واقعی — یا statement صریح که survey اجرا نشد؛
8. به‌روزرسانی dossier، register، status، checklist و master با تاریخ/limitations.

**پایان پروتکل.**
