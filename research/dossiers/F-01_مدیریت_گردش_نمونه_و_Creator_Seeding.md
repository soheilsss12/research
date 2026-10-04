# F-01 — مدیریت گردش نمونهٔ لباس و Creator Seeding

**نوع پرونده:** گزارش کامل تحقیقات بازار در سطح desk-research؛ مرحلهٔ پژوهش اولیه آغاز نشده است.
**بازار هدف فعلی:** B2B؛ B2C در دامنهٔ این پرونده نیست.
**تصمیم فعلی:** فعال برای اعتبارسنجی؛ **نه Pass و نه تصمیم ساخت.**
**تاریخ بازنگری ساختار:** ۱۲ مهر ۱۴۰۵ / ۴ اکتبر ۲۰۲۶
**سطح اطمینان:** متوسط برای وجود category جهانی و جایگزین‌های ایران؛ پایین برای اندازهٔ بازار و تمایل به پرداخت ایران تا زمان مصاحبه/پایلوت.

---

## ۱. خلاصهٔ مدیریتی (Executive Summary)

**پرسش تصمیم.** آیا تعداد و ارزش نمونه‌های در گردش، هزینهٔ گم‌شدن/تأخیر/عدم‌استفاده و هزینهٔ هماهنگی در ایران به سطحی می‌رسد که برند پوشاک یا آژانس، برای یک record تخصصیِ مشترک با دریافت‌کننده هزینه کند؟

**یافته‌های کلیدی.**

1. **F:** Launchmetrics Samples/Fashion GPS یک category جهانیِ مشخص برای ثبت رزرو، گردش، بازگشت و activation نمونهٔ فیزیکی لباس را عرضه می‌کند؛ این category با PLM، انبارداری عمومی و influencer marketplace یکسان نیست. [F01-S01–S04]
2. **F:** پلتفرم‌ها و آژانس‌های ایرانی influencer marketing، discovery، brief، campaign، گزارش و گاه پرداخت را پوشش می‌دهند؛ در صفحات عمومی بررسی‌شده، workflow صریحی برای custody قطعهٔ لباس، return/condition و asset-right دیده نشد. این فقط **عدم مشاهده در desk scan** است، نه ادعای نبود رقیب. [F01-S05–S08]
3. **H:** برندها، showroomها و آژانس‌های دارای گردش مکرر نمونه ممکن است برای یک system-of-record مستقل از Excel/WhatsApp ارزش قائل شوند؛ شدت درد، فراوانی گردش و budget آن‌ها در ایران هنوز سنجیده نشده است.
4. **F:** دادهٔ عمومی قابل اتکایی برای تعداد send-out، ارزش نمونه‌های رسانه‌ای، بودجهٔ creator seeding یا accountهای واجد شرایط در ایران پیدا نشد؛ بنابراین TAM/SAM/SOM پولی در این نسخه محاسبه نشده است.
5. **I:** wedge قابل بررسی، «accountability قطعهٔ فیزیکی از درخواست تا بازگشت و ثبت حق استفاده از asset» است؛ نه marketplace، fulfillment، payment intermediary، PLM یا media intelligence کامل.

**نتیجه.** وضعیت پرونده **فعال برای اعتبارسنجی** است. امکان ورود به طراحی MVP فقط پس از مشاهدهٔ درد تکرارشونده و هزینه‌دار در artifactهای واقعی و تعهد دو مشتری متفاوت به pilot پولی مطرح می‌شود. [R]

---

## ۲. مقدمه، زمینهٔ کسب‌وکار و اهداف پژوهش (Introduction, Business Context & Objectives)

### ۲-۱. زمینه و تعریف دقیق مفهوم

مفهوم مورد بررسی، یک software workspace برای برندهای پوشاک، آژانس‌های PR و تیم‌های creator-seeding است که **حرکت، امانت، رزرو، بازگشت، وضعیت و اثر رسانه‌ای هر نمونهٔ فیزیکی لباس** را از خروج از showroom تا بازگشت یا تعیین تکلیف، ثبت و قابل حسابرسی می‌کند.

این محصول صریحاً موارد زیر نیست:

- marketplace اینفلوئنسر، affiliate platform یا موتور انتخاب creator؛
- سیستم فروش/انبار عمومی، ERP یا PLM توسعهٔ محصول؛
- شرکت ارسال، انباردار، ضامن خسارت یا مجری فیزیکی پیک؛
- ابزار صرفِ social-listening یا داشبورد vanity metrics.

### ۲-۲. زمینهٔ مسئله و فرضیهٔ تصمیم

**H — فرضیهٔ مسئله:** در برندهای دارای نمونه‌های رسانه‌ای و چندین ارسال به استایلیست، creator، رسانه، عکاس یا مراسم، Excel/WhatsApp نمی‌تواند در یک record واحد پاسخ دهد: «کدام نمونه اکنون نزد چه کسی است، تا چه تاریخی باید بازگردد، با چه وضعیتی بازگشته، چه تعهد محتوایی داشته و چه دارایی/اجازهٔ استفاده‌ای از آن ایجاد شده است؟»

هدف این پژوهش، پاسخ‌گویی به چهار پرسش است:

1. آیا این category و workflow در بازارهای بزرگ به‌عنوان یک workflow مجزا وجود دارد؟
2. مشتری محلی، جایگزین فعلی و دامنهٔ واقعی مسئله چه هستند؟
3. آیا یک مدل platform-first و غیرعملیاتی، بدون ورود به logistics یا marketplace، قابل تصور است؟
4. چه evidence اولیه‌ای برای ادامه، توقف یا بازتعریف پرونده لازم است؟

### ۲-۳. دامنه، تعریف بازار و موارد خارج از دامنه

- **جغرافیا:** ایران برای تصمیم بازار؛ نمونه‌های جهانی فقط برای category proof و benchmark.
- **بخش بازار:** B2B؛ برند پوشاک، آژانس PR/influencer با مشتری فشن و showroom/چندبرند premium. مصرف‌کنندهٔ نهایی مشتری پرونده نیست.
- **واحد تحلیل:** گردش یک نمونهٔ رسانه‌ای/رویدادی، نه فروش SKU و نه کل صنعت پوشاک.
- **دورهٔ داده:** صفحات و منابع در ۱۲ مهر ۱۴۰۵ بازیابی شده‌اند.
- **محدودیت دامنه:** نسبت‌دادن فروش به creator، ارزش‌گذاری MIV، عملیات پیک/انبار/خسارت، escrow و اجرای campaign خارج از مفهوم است.

---

## ۳. روش‌شناسی پژوهش و محدودیت‌ها (Research Methodology & Limitations)

### ۳-۱. طراحی پژوهش و منابع

این نسخه یک **desk-research اکتشافی** است. منابع شامل صفحات رسمی vendorهای جهانی و ایرانی، صفحات عمومی محصول/خدمت و تحلیل workflow آن‌هاست. هر ادعا با برچسب F (واقعیت مستند)، H (فرضیه)، I (تفسیر) یا R (توصیه) آمده و منابع در پیوست ثبت شده‌اند. ادعای scale یا تعداد مشتری که فروشنده منتشر کرده، «vendor claim» تلقی می‌شود.

### ۳-۲. روش تحلیل

- تعریف واحد کار به‌عنوان «sample movement» و تفکیک آن از PLM، POS، انبار و marketplace؛
- مقایسهٔ competitor/substitute برحسب workflow، نه صرفاً نام شرکت؛
- bottom-up sizing به‌صورت مدل و سؤال داده، نه ساختن یک رقم بازار؛
- ارزیابی عملیاتی با قید platform-first: محصول نباید مالک یا مجری حرکت فیزیکی نمونه شود.

### ۳-۳. نبود پژوهش اولیه و محدودیت‌ها

هیچ مصاحبه، survey، pilot، دادهٔ تراکنشی، sample frame یا observation میدانی در ایران در این مرحله انجام نشده است. بنابراین تعداد گردش، هزینهٔ گم‌شدن، مدت پیگیری، willingness-to-pay، ARPA، نرخ پذیرش و وجود رقیب داخلیِ غیرعمومی **اثبات نشده‌اند**. صفحات عمومی vendor نیز جای مشاهدهٔ رفتار مشتری یا market size مستقل را نمی‌گیرند. این گزارش نباید مبنای تصمیم ساخت، پیش‌بینی فروش یا ادعای white space قطعی باشد.

---

## ۴. نمای کلی بازار و صنعت (Market & Industry Overview)

### ۴-۱. value chain و جایگاه category

در creator seeding و PR پوشاک، یک قطعهٔ نمونه از catalog/showroom به درخواست و رزرو، تحویل، استفاده در shoot/event/coverage، بازگشت یا write-off/gift و ثبت asset/permission می‌رسد. این workflow پس از آماده‌شدن قطعه رخ می‌دهد؛ به همین دلیل با PLM که concept/specification/production را تعریف می‌کند، یک category نیست.

### ۴-۲. benchmark جهانی: Launchmetrics Samples / Fashion GPS

Fashion GPS در ۲۰۰۶ برای جایگزینی paper filing در مدیریت sample closet و workflow میان publicist و publication تأسیس شد؛ اکنون به‌عنوان محصول Samples در Launchmetrics Brand Performance Cloud ادامه دارد. [F01-S02]

Launchmetrics، طبق اعلام خود شرکت در ۲۰۲۶، با بیش از ۱٬۷۰۰ برند در بیش از ۱۰۰ کشور کار می‌کند و product sample management را کنار PR monitoring، event، contacts و digital showroom ارائه می‌دهد. این **ادعای vendor** است، اما وجود category را در مقیاس بین‌المللی نشان می‌دهد. [F01-S01]

| قابلیت جهانی مشاهده‌شده | شواهد | دلالت برای مفهوم ایران |
|---|---|---|
| Tracking فیزیکی نمونه | وضعیت، location، request، loan، check-in/out و return در lifecycle قطعه. [F01-S01][F01-S03] | هستهٔ مفهوم، contact database یا warehouse عمومی نیست؛ unit of work همان sample movement است. |
| barcode/RFID و جست‌وجوی asset | ingestion از spreadsheet/API و فیلتر status/style/color/season شرح داده شده است. [F01-S03] | برای MVP ایران، QR یا code داخلی کافی است؛ RFID وابستگی زودهنگام است. |
| reservation و جلوگیری از تعارض | reservation، transfer، archive، write-off و gift در گردش نمونه تعریف شده‌اند. [F01-S03] | state model از روز اول باید روشن باشد؛ «ارسال‌شده» یک status کافی نیست. |
| اتصال نمونه به coverage | sample activation به placement/mention و MIV پیوند داده می‌شود. [F01-S04] | در ایران ابتدا فقط link/asset/right ثبت شود؛ attribution یا MIV نباید وعدهٔ MVP باشد. |
| مقیاس category | شرکت تا ۵ میلیارد دلار ارزش محصول مدیریت‌شده در هر season و استفاده در ۸۵٪ top fashion shows را اعلام می‌کند. [F01-S01] | عدد به ایران منتقل نمی‌شود؛ فقط نشان می‌دهد workflow در category جهانی حاشیه‌ای نیست. |

### ۴-۳. روندها، محرک‌ها و موانع انتقال‌پذیری

**I:** digitisation catalog، نیاز به رزرو و traceability، و اتصال حضور رسانه‌ای به asset record، محرک‌های category جهانی‌اند. در مقابل، انتقال مستقیم suite جهانی به ایران با محدودیت زبان، pricing، integration، حجم واقعی accountها و شیوهٔ کار آژانس‌ها مواجه است. clone کامل Launchmetrics thesis این پرونده نیست؛ فقط یک wedge محدود می‌تواند بررسی شود.

---

## ۵. اندازه، ساختار و پویایی تقاضای بازار (Market Sizing, Structure & Demand)

### ۵-۱. وضعیت داده و حکم sizing

**F:** هیچ آمار عمومی قابل اتکایی برای «تعداد سالانهٔ sample send-out پوشاک ایران»، «ارزش نمونه‌های PR»، «بودجهٔ creator seeding فشن» یا «تعداد accountهای واجد شرایط» در desk-research پیدا نشد. بنابراین TAM پولی نباید اکنون با یک عدد قطعی ارائه شود.

### ۵-۲. مدل bottom-up موردنیاز

`SAM سالانه = تعداد accountهای واجد ICP × نرخ پذیرش software × ARPA سالانه`

برای قابل دفاع شدن مدل، باید در interview/market mapping ثبت شود:

1. تعداد برند/agency با حداقل حجم گردش نمونه در ۱۲ ماه؛
2. تعداد نمونهٔ امانی و متوسط duration هر گردش؛
3. ارزش جایگزینی/هزینهٔ گم‌شدن یا فرصت از دست‌رفته؛
4. نفر-ساعت پیگیری و گزارش دستی؛
5. budget owner و price anchor؛
6. willingness برای workspace مستقل در برابر Excel/agency service.

### ۵-۳. حساسیت و معیار بلوغ بازار

تا زمان دستیابی به denominatorهای بالا، هیچ TAM/SAM/SOM یا growth rate گزارش نمی‌شود. نشانه‌های کافی برای بررسی بعدی شامل حجم تکرارشوندهٔ movement، وجود owner بودجه، هزینهٔ آشکار coordination و ناتوانی روش دستی در حفظ audit trail است؛ هر یک باید با artifact واقعی آزموده شود، نه با اظهار علاقه.

---

## ۶. بازار هدف، بخش‌بندی و مشتری (Target Market, Segmentation & Customer)

### ۶-۱. بخش‌های B2B فرضی

| segment فرضی | trigger محتمل | buyer فرضی | شرط ورود به مصاحبه |
|---|---|---|---|
| برند پوشاک دارای collection و نمونه‌های رسانه‌ای | هم‌زمانی shoot، event، creator send-out یا گم‌شدن نمونه | founder، PR/marketing lead یا brand manager | دست‌کم ۲۰ گردش نمونه در یک quarter یا هزینهٔ قابل بیان از پیگیری دستی. |
| آژانس PR / influencer با چند برند فشن | campaign هم‌زمان، درخواست sample و گزارش به client | account director / operations lead | اجرای مستمر campaign فشن و مسئولیت هماهنگی نمونه، نه فقط خرید پست. |
| showroom/چندبرند premium | loan به stylist/editor یا عکس‌برداری | showroom/PR manager | نمونه‌ها در دست چند دریافت‌کننده و نیاز واقعی به رزرو دارند. |

تمام آستانه‌های این جدول **H — فرضیهٔ طراحی مصاحبه** هستند، نه اندازهٔ بازار.

### ۶-۲. نقش‌ها در تصمیم و استفاده

- **Economic buyer فرضی:** founder، brand manager، PR/marketing lead یا operations/account director.
- **کاربر عملیاتی فرضی:** sample coordinator، showroom manager، account executive یا مسئول PR.
- **کاربر/مشارکت‌کنندهٔ بیرونی:** creator، stylist، editor، عکاس یا دریافت‌کنندهٔ نمونه؛ الزام account برای او یک فرضیهٔ پرریسک است.
- **B2C:** خارج از دامنه. creator در این پرونده ممکن است دریافت‌کننده یا مشارکت‌کنندهٔ workflow باشد، نه مشتری مصرف‌کننده.

---

## ۷. بینش مشتری، نیاز، رفتار خرید و قیمت‌پذیری (Customer Insights, Buying Behaviour & Willingness-to-Pay)

### ۷-۱. JTBD و رفتار مورد آزمون

**H — Job اصلی:** «وقتی برای ایجاد پوشش رسانه‌ای، عکاسی، استایلینگ یا معرفی کالکشن، یک نمونهٔ ارزشمند را از اختیار خود خارج می‌کنم، می‌خواهم بدون تماس‌های پی‌درپی بدانم کجاست، چه زمانی آزاد می‌شود، در چه وضعیتی است و چه خروجیِ قابل استفاده‌ای از آن گرفته‌ام.»

جریان کاری هدف چنین تعریف می‌شود:

`کالکشن/نمونه → ثبت مشخصات و تصویر → درخواست/رزرو → تأیید مسئول → تحویل به پیک یا دریافت‌کننده → reminder → بازگشت و condition check → ثبت خسارت/هدیه/بایگانی → اتصال لینک یا asset پوشش رسانه‌ای → گزارش استفاده و ROI`.

### ۷-۲. دردهای قابل‌سنجش

- نمونهٔ مورد نیاز برای shoot یا press appointment قابل پیدا کردن نیست یا هم‌زمان رزرو شده است.
- موعد بازگشت با تماس/پیام پیگیری می‌شود و تاریخچه‌ای قابل اعتماد ندارد.
- در زمان بازگشت، condition، لوازم جانبی یا خسارت ثبت نشده است.
- نمونه به creator ارسال شده اما status تعهد محتوایی، لینک انتشار و حق reuse دارایی پراکنده است.
- گزارش عملکرد به جای قطعه/گردش، فقط در سطح campaign یا فاکتور آژانس باقی می‌ماند.

این‌ها **H — فرضیه‌های مورد آزمون** هستند. تعداد، هزینه و تکرار آن‌ها برای ایران در دادهٔ عمومی موجود نیست.

### ۷-۳. WTP و anchor قیمت

هیچ دادهٔ WTP، budget یا price acceptance در این نسخه وجود ندارد. «paid pilot»، مشاهدهٔ هزینهٔ نیروی هماهنگ‌کننده و مقایسه با هزینهٔ missing/overdue باید پیش از هر price point انجام شود. علاقهٔ لفظی به اپلیکیشن، evidence پرداخت تلقی نمی‌شود.

---

## ۸. چشم‌انداز رقابتی و جایگزین‌ها (Competitive Landscape & Substitutes)

### ۸-۱. بازیگران و جایگزین‌های مشاهده‌شده در ایران

پلتفرم‌ها و آژانس‌های ایرانی influencer marketing، discovery، اجرای کمپین، brief، گزارش و تسویه را پوشش می‌دهند. برای نمونه، دیما سوشال از ثبت سفارش، انتخاب/پیشنهاد همکاری، پرداخت مشروط به اجرای تبلیغ و گزارش کمپین سخن می‌گوید؛ نشانت نیز ایجاد کمپین، شبکهٔ اینفلوئنسر و گزارش‌های مدیریتی را عرضه می‌کند. [F01-S05][F01-S06]

در صفحات عمومی بررسی‌شده، شواهدی از product record تخصصی برای «هر لباس امانی»، موعد بازگشت، عکس condition، گردش فیزیکی و حق استفاده از asset پیدا نشد. این جمله به معنی نبود رقیب نیست: آژانس‌ها ممکن است آن را managed service، sheet یا ابزار داخلی انجام دهند.

| دسته | نمونه یا روش | چه مسئله‌ای را حل می‌کند | چه چیزی را حل‌نشده می‌گذارد |
|---|---|---|---|
| پلتفرم influencer marketing | دیما سوشال، نشانت، تگرو، باکس‌ادز | discovery، brief، campaign، گزارش و در برخی موارد پرداخت. [F01-S05–S07] | custody فیزیکی یک لباس، return، condition و asset-right در سطح قطعه. |
| آژانس اجرای کمپین | آژانس/PR و مدیر creator | مذاکره، strategy، اجرا و گزارش دستی | system-of-record دائمی؛ مقیاس‌پذیری به فرد کلیدی وابسته است. |
| ابزار عمومی | Excel/Google Sheets، WhatsApp/Telegram، Drive، Calendar | هزینهٔ اولیه کم و انعطاف بالا | version/audit، reminder، conflict detection، sample-level history و گزارش یکپارچه. |
| انبار/حسابداری پوشاک | نرم‌افزارهای پوشاک رنگ/سایز/بارکد را مدیریت می‌کنند. [F01-S08] | کالا، فروش و stock | loan چرخهٔ PR، creator activation و return workflow را هدف نگرفته‌اند. |
| Launchmetrics خارجی | Samples + PR/coverage suite | workflow کامل enterprise | local access، قیمت، زبان، integration و تناسب با حجم ایران نامعلوم. |

### ۸-۲. موضع‌یابی، موانع و counter-thesis

**I:** موضع قابل بررسی فقط یک record تخصصی برای sample circulation است؛ این تمایز هنوز اثبات نشده است. مهم‌ترین counter-thesis این است که آژانس‌ها مسئله را با نیروی انسانی حل می‌کنند و حجم گردش اکثر accountها آن‌قدر کم است که Excel/WhatsApp کفایت دارد. همچنین ابزار داخلیِ غیرعمومی می‌تواند رقابت پنهان باشد. بنابراین «عدم مشاهدهٔ صفحهٔ محصول» به white space تبدیل نمی‌شود.

---

## ۹. ارزیابی مفهوم محصول، مدل کسب‌وکار و قیمت‌گذاری (Product Concept, Business Model & Pricing Assessment)

### ۹-۱. مفهوم و workflow محصول

| موجودیت | دادهٔ ضروری | دلیل محصولی |
|---|---|---|
| نمونهٔ فیزیکی | کد یکتا، عکس، سایز/رنگ، collection، ارزش/وضعیت، location | تفاوت با موجودی SKU فروشگاهی؛ موضوع یک قطعهٔ قابل‌امانت است. |
| گردش/Loan | دریافت‌کننده، مقصد، تحویل‌دهنده، موعد بازگشت، وضعیت و timeline | پاسخ به «اکنون کجاست؟» و جلوگیری از double-booking. |
| رزرو/درخواست | درخواست‌کننده، رویداد/shoot، نیاز زمانی، اولویت و تأیید | تخصیص پیش از خروج فیزیکی. |
| condition / خسارت | عکس قبل/بعد، شرح، تصمیم، هزینه/ودیعه در صورت وجود | تعیین مسئولیت بدون تبدیل پلتفرم به ضامن یا بیمه‌گر. |
| activation | لینک محتوا/انتشار، تاریخ، حق استفاده، creator/رسانه و نتیجهٔ دستی | اتصال «نمونه» به «نتیجه»، بدون ادعای attribution قطعی. |

### ۹-۲. MVP مشروط به گیت اعتبارسنجی

1. catalog نمونه با code/QR، عکس، ویژگی و وضعیت؛
2. request، reservation و approval؛
3. handoff log و reminder بازگشت؛
4. return/condition با عکس قبل و بعد؛
5. creator/campaign link، asset URL و permission note؛
6. dashboard: overdue، unavailable، unresolved condition و activation pending.

### ۹-۳. مدل درآمد و قیمت‌گذاری قابل آزمون

- اشتراک workspace برند/agency با سقف active sample یا active campaign؛
- tier بالاتر برای چند تیم، audit/reporting و permission؛
- onboarding محدود و paid pilot؛
- **نه** commission از قرارداد influencer و **نه** درصد ارزش لباس؛ محصول marketplace/financial intermediary نیست.

هیچ نرخ یا ARPA در این نسخه پیشنهاد نمی‌شود. billing metric، price anchor و willingness-to-pay فقط با مصاحبهٔ artifact-based و pilot پولی تعیین می‌شوند.

---

## ۱۰. امکان‌سنجی اجرایی، حقوقی و عملیاتی (Operational, Legal & Commercial Feasibility)

### ۱۰-۱. مرز عملیاتی و non-goals

مفهوم باید platform-first باقی بماند. تأمین اینفلوئنسر، انتخاب خودکار creator، پرداخت یا escrow، حمل/دریافت فیزیکی/انبارداری/ارزیابی خسارت در میدان، attribution قطعی فروش، POS، PLM، DAM عمومی و social listening کامل از دامنهٔ MVP خارج‌اند.

### ۱۰-۲. ریسک‌های کلیدی و پاسخ پژوهشی

| ریسک | اثر | کاهش/آزمون |
|---|---|---|
| حجم گردش برای SaaS مستقل کم باشد | استفادهٔ episodic و عدم renewal | segment based on actual send-outs؛ price test و pilot پولی. |
| آژانس‌ها مشکل را با نیروی انسانی حل کنند | buyer SaaS ندارد | بررسی unit economics agency و امکان white-label/agency workspace؛ بدون تبدیل شدن به service. |
| دریافت‌کننده portal را باز نکند | status واقعی ناقص می‌شود | flow موبایلیِ بدون account، لینک تأیید، یادآوری چندکاناله؛ adoption در pilot سنجیده شود. |
| خسارت/ودیعه به dispute حقوقی تبدیل شود | scope creep و ریسک حقوقی | tool فقط evidence/audit record باشد؛ شرایط قرض و مسئولیت قرارداد brand/agency بماند. |
| asset-right مبهم باشد | استفادهٔ نامجاز محتوا | ثبت permission status و template consent؛ review حقوقی پیش از scale. |
| محصول به influencer marketplace منحرف شود | overlap و عملیات شبکه‌ای | rule: هیچ inventory شبکهٔ creator یا commission در MVP. |

---

## ۱۱. یافته‌ها، تحلیل و ارزیابی فرصت (Findings, Analysis & Opportunity Assessment)

### ۱۱-۱. تفکیک یافته، تفسیر و فرضیه

- **F:** category جهانیِ sample management و lifecycle آن مستند است؛ benchmark جهانی، workflow را از PLM و inventory عمومی جدا می‌کند. [F01-S01–S04]
- **F:** در اکوسیستم عمومی ایران، substituteهای campaign-management، آژانس و ابزار عمومی وجود دارند. [F01-S05–S08]
- **F:** برای حجم، budget و WTP بازار ایران دادهٔ عمومی کافی نیست.
- **I:** اگر segmentی با حرکت‌های مکرر، custody حساس و خروجی رسانه‌ای قابل ثبت وجود داشته باشد، یک system-of-record تخصصی ممکن است از ابزار عمومی متمایز شود.
- **H:** آن segment ممکن است کوچک، service-driven یا فاقد budget مستقل باشد؛ این فرضیهٔ مخالف، محتمل و تصمیم‌ساز است.

### ۱۱-۲. ارزیابی جذابیت و سناریوها

| سناریو | شرط مشاهده | دلالت تصمیم |
|---|---|---|
| بالا | چند account با volume تکرارشونده، هزینهٔ آشکار، owner بودجه و دو paid pilot | ادامهٔ feasibility و طراحی محدود MVP. |
| پایه | درد وجود دارد اما volume/price یا adoption دریافت‌کننده نامطمئن است | Watch و آزمون workflow کم‌هزینه؛ ساخت محصول کامل ممنوع. |
| پایین | Excel/WhatsApp کفایت دارد، volume کم است یا buyer پولی یافت نمی‌شود | توقف پرونده و ثبت evidence در archive. |

**سطح اطمینان:** متوسط برای category proof و پایین برای market attractiveness ایران. دلیل، نبود primary evidence و denominator محلی است.

---

## ۱۲. نتیجه‌گیری و توصیهٔ راهبردی (Conclusions & Strategic Recommendation)

**نتیجه.** F-01 در وضعیت **فعال برای اعتبارسنجی** باقی می‌ماند؛ نه Pass و نه توصیهٔ ساخت. category جهانی و workflow تخصصی آن به‌خوبی قابل مشاهده است. بازار ایران دارای پلتفرم‌های campaign/influencer و ابزارهای عمومی است، اما evidence مستقیم از sample-loan record تخصصی در این desk-research دیده نشد. فاصلهٔ مشاهده‌شده فقط یک hypothesis است؛ نه white space و نه مجوز ساخت.

**R — توصیهٔ راهبردی.** تنها wedge قابل آزمون، accountability نمونهٔ فیزیکی و handoff قابل‌ردیابی از PR/creator request تا return و asset-right است. هر تلاش برای افزودن marketplace، fulfillment یا full media intelligence باید خارج از thesis فعلی تلقی و متوقف شود.

---

## ۱۳. برنامهٔ اعتبارسنجی بعدی و گیت تصمیم (Validation Plan & Decision Gate)

### ۱۳-۱. مصاحبهٔ کشف

۱۵ مصاحبهٔ artifact-based انجام شود:

- ۵ مدیر برند/PR/marketing در پوشاک؛
- ۴ account یا operations agency؛
- ۳ sample coordinator/showroom/stylist؛
- ۳ creator یا stylist دریافت‌کنندهٔ نمونه.

برای آخرین سه گردش واقعی، نمونه، تاریخ خروج، پیام‌های پیگیری، وضعیت بازگشت، مشکل، هزینه و استفاده از محتوا بررسی شود. پرسش «اگر اپ بسازیم می‌خری؟» به‌تنهایی معتبر نیست.

### ۱۳-۲. گیت pilot، KPI و owner پیشنهادی

**گیت ورود:** دو customer متفاوت با pilot پولی ۶ تا ۸ هفته‌ای؛ دست‌کم یک collection یا ۱۰–۳۰ sample movement واقعی برای هر customer؛ استفادهٔ مسئول برند و بخشی از دریافت‌کنندگان از flow؛ و baseline ثبت‌شده از نفر-ساعت پیگیری، overdue و missing/uncertain status.

**KPI:** درصد sample با custodian/موعد/status قابل مشاهده؛ درصد گردش با return/condition ثبت‌شده؛ زمان پاسخ به «این نمونه اکنون کجاست؟»؛ تعداد conflict رزرو یا پیگیری دستی؛ درصد activation دارای link و permission status؛ و willingness برای renewal پس از pilot.

**مالک تصمیم:** owner پژوهش پرونده با تأیید تصمیم‌گیر محصول؛ زمان‌بندی و سقف هزینه پیش از آغاز fieldwork تعیین می‌شود.

### ۱۳-۳. hard kill

مسیر متوقف می‌شود اگر: (۱) درد version/status/return تکرارشونده و هزینه‌دار دیده نشود؛ (۲) هیچ دو customer برای pilot پولی commit نکنند؛ (۳) دریافت‌کننده/agency flow سادهٔ تأیید را استفاده نکند؛ یا (۴) اکثر accountها حجمی داشته باشند که Excel/WhatsApp کفایت کند.

---

## ۱۴. پیوست‌ها (Appendices)

### پیوست الف. ledger شواهد و منابع

| کد | رتبه | منبع | نکتهٔ استفاده‌شده | پیوند |
|---|---|---|---|---|
| F01-S01 | C (vendor claim) | Launchmetrics — Samples Management / Brand Performance Cloud، بازیابی ۱۲ مهر ۱۴۰۵ | تعریف product، ۱٬۷۰۰+ brand، ۱۰۰+ کشور و ادعاهای scale/impact. | https://www.launchmetrics.com/software/samples-management |
| F01-S02 | C (vendor history) | Launchmetrics — Fashion GPS Background، بازیابی ۱۲ مهر ۱۴۰۵ | منشأ Fashion GPS و workflow press/sample. | https://www.launchmetrics.com/fashion-gps-background |
| F01-S03 | C (vendor) | Launchmetrics — Fashion Sample Tracking Software، بازیابی ۱۲ مهر ۱۴۰۵ | status model، reservation، return، barcode/RFID و lifecycle. | https://www.launchmetrics.com/resources/blog/sample-tracking-software |
| F01-S04 | C (vendor) | Launchmetrics — Improve Sample Tracking & MIV، بازیابی ۱۲ مهر ۱۴۰۵ | پیوند sample activation و coverage؛ استفاده فقط برای category proof. | https://www.launchmetrics.com/resources/blog/how-to-improve-fashion-sample-tracking-and-quantify-with-miv |
| F01-S05 | C (vendor) | دیما — دیما سوشال، بازیابی ۱۲ مهر ۱۴۰۵ | سفارش، همکاری، payment/reporting campaign؛ نه evidence sample-loan. | https://deema.agency/deema-social-platform/ |
| F01-S06 | C (vendor) | نشانت، بازیابی ۱۲ مهر ۱۴۰۵ | شبکه، کمپین و گزارش‌های influencer marketing. | https://neshanet.com/ |
| F01-S07 | C (vendor) | تگرو، بازیابی ۱۲ مهر ۱۴۰۵ | campaign/influencer substitute. | https://tagrow.net/ |
| F01-S08 | C (vendor) | محک — نرم‌افزار حسابداری پوشاک، بازیابی ۱۲ مهر ۱۴۰۵ | وجود inventory رنگ/سایز/بارکد؛ عدم هم‌ارزی با sample PR. | https://www.mahaksoft.com/garment-accounting-software/ |

### پیوست ب. تغییرنگار

| نسخه | تاریخ | تغییر |
|---|---|---|
| ۱٫۰ | پیش از ۱۲ مهر ۱۴۰۵ | پروندهٔ desk-research اولیه ثبت شد. |
| ۲٫۰ | ۱۲ مهر ۱۴۰۵ | ساختار پرونده بدون حذف شواهد، به hierarchy استاندارد گزارش تحقیقات بازار تبدیل شد؛ primary research همچنان انجام نشده است. |
