# F-01 — مدیریت گردش نمونهٔ لباس و Creator Seeding

**نوع پرونده:** تحقیق بازارِ desk-research؛ مرحلهٔ پژوهش اولیه آغاز نشده است.  
**بازار:** B2B  
**تصمیم فعلی:** فعال برای اعتبارسنجی؛ **نه Pass و نه تصمیم ساخت.**  
**تاریخ:** ۱۲ مهر ۱۴۰۵ / ۴ اکتبر ۲۰۲۶  
**سطح اطمینان:** متوسط برای وجود category جهانی و جایگزین‌های ایران؛ پایین برای اندازهٔ بازار و تمایل به پرداخت ایران تا زمان مصاحبه/پایلوت.

---

## ۱. کارت تصمیم

### تعریف دقیق محصول
یک software workspace برای برندهای پوشاک، آژانس‌های PR و تیم‌های creator-seeding که **حرکت، امانت، رزرو، بازگشت، وضعیت و اثر رسانه‌ای هر نمونهٔ فیزیکی لباس** را از خروج از showroom تا بازگشت یا تعیین تکلیف، ثبت و قابل حسابرسی می‌کند.

### مرز محصول
این محصول صریحاً موارد زیر نیست:

- marketplace اینفلوئنسر، affiliate platform یا موتور انتخاب creator؛
- سیستم فروش/انبار عمومی، ERP یا PLM توسعهٔ محصول؛
- شرکت ارسال، انباردار، ضامن خسارت یا مجری فیزیکی پیک؛
- ابزار صرفِ social-listening یا داشبورد vanity metrics.

### فرضیهٔ مسئله
در برندهای دارای نمونه‌های رسانه‌ای و چندین ارسال به استایلیست، creator، رسانه، عکاس یا مراسم، Excel/WhatsApp نمی‌تواند در یک record واحد پاسخ دهد: **کدام نمونه اکنون نزد چه کسی است، تا چه تاریخی باید بازگردد، با چه وضعیتی بازگشته، چه تعهد محتوایی داشته و چه دارایی/اجازهٔ استفاده‌ای از آن ایجاد شده است؟**

### تصمیمی که باید گرفته شود
آیا تعداد و ارزش نمونه‌های در گردش، هزینهٔ گم‌شدن/تاخیر/عدم‌استفاده و هزینهٔ هماهنگی در ایران به سطحی می‌رسد که برند یا آژانس برای یک record تخصصیِ مشترک با دریافت‌کننده هزینه کند؟

---

## ۲. جریان کار و Job-to-be-Done

### Job اصلی
«وقتی برای ایجاد پوشش رسانه‌ای، عکاسی، استایلینگ یا معرفی کالکشن، یک نمونهٔ ارزشمند را از اختیار خود خارج می‌کنم، می‌خواهم بدون تماس‌های پی‌درپی بدانم کجاست، چه زمانی آزاد می‌شود، در چه وضعیتی است و چه خروجیِ قابل استفاده‌ای از آن گرفته‌ام.»

### جریان کاری هدف

`کالکشن/نمونه → ثبت مشخصات و تصویر → درخواست/رزرو → تأیید مسئول → تحویل به پیک یا دریافت‌کننده → reminder → بازگشت و condition check → ثبت خسارت/هدیه/بایگانی → اتصال لینک یا asset پوشش رسانه‌ای → گزارش استفاده و ROI`.

### موجودیت‌های داده‌ای حداقلی

| موجودیت | دادهٔ ضروری | دلیل محصولی |
|---|---|---|
| نمونهٔ فیزیکی | کد یکتا، عکس، سایز/رنگ، collection، ارزش/وضعیت، location | تفاوت با موجودی SKU فروشگاهی؛ موضوع یک قطعهٔ قابل‌امانت است. |
| گردش/Loan | دریافت‌کننده، مقصد، تحویل‌دهنده، موعد بازگشت، وضعیت و timeline | پاسخ به «اکنون کجاست؟» و جلوگیری از double-booking. |
| رزرو/درخواست | درخواست‌کننده، رویداد/ shoot، نیاز زمانی، اولویت و تأیید | تخصیص پیش از خروج فیزیکی. |
| condition / خسارت | عکس قبل/بعد، شرح، تصمیم، هزینه/ودیعه در صورت وجود | تعیین مسئولیت بدون تبدیل پلتفرم به ضامن یا بیمه‌گر. |
| activation | لینک محتوا/انتشار، تاریخ، حق استفاده، creator/رسانه و نتیجهٔ دستی | اتصال «نمونه» به «نتیجه»، بدون ادعای attribution قطعی. |

### دردهای قابل‌سنجش

- نمونهٔ مورد نیاز برای shoot یا press appointment قابل پیدا کردن نیست یا هم‌زمان رزرو شده است.
- موعد بازگشت با تماس/پیام پیگیری می‌شود و تاریخچه‌ای قابل اعتماد ندارد.
- در زمان بازگشت، condition، لوازم جانبی یا خسارت ثبت نشده است.
- نمونه به creator ارسال شده اما status تعهد محتوایی، لینک انتشار و حق reuse دارایی پراکنده است.
- گزارش عملکرد به جای قطعه/گردش، فقط در سطح campaign یا فاکتور آژانس باقی می‌ماند.

این‌ها **فرضیه‌های مورد آزمون** هستند. تعداد، هزینه و تکرار آن‌ها برای ایران در دادهٔ عمومی موجود نیست.

---

## ۳. شواهد جهانی و category proof

### ۳-۱. benchmark اصلی: Launchmetrics Samples / Fashion GPS

Fashion GPS در ۲۰۰۶ برای جایگزینی paper filing در مدیریت sample closet و workflow میان publicist و publication تأسیس شد؛ اکنون به‌عنوان محصول Samples در Launchmetrics Brand Performance Cloud ادامه دارد. [F01-S02]

Launchmetrics، طبق اعلام خود شرکت در ۲۰۲۶، با بیش از ۱٬۷۰۰ برند در بیش از ۱۰۰ کشور کار می‌کند و product sample management را کنار PR monitoring، event، contacts و digital showroom ارائه می‌دهد. این **ادعای vendor** است، اما category را در مقیاس بین‌المللی معتبر می‌کند. [F01-S01]

| قابلیت جهانی مشاهده‌شده | شواهد | دلالت برای مسئلهٔ ایران |
|---|---|---|
| Tracking فیزیکی نمونه | وضعیت، location، request، loan، check-in/out و return در طول lifecycle قطعه. [F01-S01][F01-S03] | هستهٔ محصول، «contact database» یا warehouse عمومی نیست؛ unit of work همان sample movement است. |
| barcode/RFID و جست‌وجوی asset | company، ingestion از spreadsheet/API و فیلتر status/style/color/season را شرح می‌دهد. [F01-S03] | برای MVP ایران، QR یا code داخلی کافی است؛ RFID یک وابستگی زودهنگام و غیرضروری است. |
| reservation و جلوگیری از تعارض | تعریف reservation، transfer، archive، write-off و gift در گردش نمونه آمده است. [F01-S03] | state model باید از روز اول واضح باشد؛ «ارسال‌شده» یک status کافی نیست. |
| اتصال نمونه به coverage | Launchmetrics sample activation را به placement/mention و MIV پیوند می‌دهد. [F01-S04] | در ایران ابتدا فقط link/asset/right ثبت شود؛ محاسبهٔ MIV یا attribution نباید وعدهٔ MVP باشد. |
| مقیاس category | خود Launchmetrics تا $5bn ارزش محصولِ مدیریت‌شده در هر season و استفاده در 85% top fashion shows را اعلام می‌کند. [F01-S01] | این عدد قابل انتقال به ایران نیست؛ فقط نشان می‌دهد مدیریت sample یک workflow حاشیه‌ای نیست. |

### ۳-۲. نکتهٔ مهم: PLM و sample circulation یکی نیستند

Launchmetrics بین PLM و Samples تمایز می‌گذارد: PLM محصول را در concept/specification/production تعریف می‌کند؛ Samples حرکت و activation یک قطعهٔ فیزیکی را پس از موجودشدن پیگیری می‌کند. [F01-S01] این تفکیک برای جلوگیری از overlap با مسیر ردشدهٔ PLM/ERP تعیین‌کننده است.

### ۳-۳. نتیجهٔ جهانی

وجود Launchmetrics/Fashion GPS نشان می‌دهد category واقعی، دارای user حرفه‌ای و دارای lifecycle روشن است. اما suite جهانیِ enterprise شامل media monitoring، database، event و metrics نیز هست؛ **clone کامل آن برای ایران thesis این پرونده نیست.** local wedge فقط زمانی معنا دارد که sample circulation و creator seeding یک درد مستقل از influencer marketplace داشته باشند.

---

## ۴. بازار و جایگزین‌های ایران

### ۴-۱. آنچه وجود دارد

پلتفرم‌ها و آژانس‌های ایرانی influencer marketing، discovery، اجرای کمپین، brief، گزارش و تسویه را پوشش می‌دهند. برای نمونه، دیما سوشال از ثبت سفارش، انتخاب/پیشنهاد همکاری، پرداخت مشروط به اجرای تبلیغ و گزارش کمپین سخن می‌گوید؛ نشانت نیز ایجاد کمپین، شبکهٔ اینفلوئنسر و گزارش‌های مدیریتی را عرضه می‌کند. [F01-S05][F01-S06]

این‌ها substitute مهم برای **انتخاب creator و مدیریت campaign** هستند، اما در بررسی desk-research، شواهدی از product record تخصصی برای «هر لباس امانی»، موعد بازگشت، عکس condition، گردش فیزیکی و حق استفاده از asset پیدا نشد.

> این جمله به معنی «نبود رقیب» نیست: فقط می‌گوید در صفحات عمومیِ بررسی‌شده، این workflow به‌صورت صریح عرضه نشده است. ممکن است آژانس‌ها آن را managed service، sheet یا ابزار داخلی انجام دهند.

### ۴-۲. نقشهٔ رقابت / substitute

| دسته | نمونه یا روش | چه مسئله‌ای را حل می‌کند | چه چیزی را حل‌نشده می‌گذارد |
|---|---|---|---|
| پلتفرم influencer marketing | دیما سوشال، نشانت، تگرو، باکس‌ادز | discovery، brief، campaign، گزارش و در برخی موارد پرداخت. [F01-S05–S07] | custody فیزیکی یک لباس، return، condition و asset-right در سطح قطعه. |
| آژانس اجرای کمپین | آژانس/PR و مدیر creator | مذاکره، strategy، اجرا و گزارش دستی | system-of-record دائمی؛ مقیاس‌پذیری به فرد کلیدی وابسته است. |
| ابزار عمومی | Excel/Google Sheets، WhatsApp/Telegram، Drive، Calendar | هزینهٔ اولیه کم و انعطاف بالا | version/audit، reminder، conflict detection، sample-level history و گزارش یکپارچه. |
| انبار/حسابداری پوشاک | نرم‌افزارهای پوشاک رنگ/سایز/بارکد را مدیریت می‌کنند. [F01-S08] | کالا، فروش و stock | loan چرخهٔ PR، creator activation و return workflow را هدف نگرفته‌اند. |
| launchmetrics خارجی | Samples + PR/coverage suite | workflow کامل enterprise | local access، قیمت، زبان، integration و تناسب با حجم ایران نامعلوم. |

### ۴-۳. فرضیهٔ ICP محلی

| segment فرضی | trigger محتمل | buyer فرضی | شرط ورود به مصاحبه |
|---|---|---|---|
| برند پوشاک دارای collection و نمونه‌های رسانه‌ای | هم‌زمانی shoot، event، creator send-out یا گم‌شدن نمونه | founder، PR/marketing lead یا brand manager | دست‌کم ۲۰ گردش نمونه در یک quarter یا هزینهٔ قابل بیان از پیگیری دستی. |
| آژانس PR / influencer با چند برند فشن | campaign هم‌زمان، درخواست sample و گزارش به client | account director / operations lead | اجرای مستمر campaign فشن و مسئولیت هماهنگی نمونه، نه فقط خرید پست. |
| showroom/چندبرند premium | loan به stylist/editor یا عکس‌برداری | showroom/PR manager | نمونه‌ها در دست چند دریافت‌کننده و نیاز واقعی به رزرو دارند. |

همهٔ اعداد آستانه در این جدول **فرضیهٔ طراحی مصاحبه** هستند، نه اندازهٔ بازار.

---

## ۵. اندازه بازار و مدل مالی: آنچه می‌دانیم و نمی‌دانیم

### ۵-۱. حکم اندازه بازار
هیچ آمار عمومیِ قابل‌اتکا برای «تعداد سالانهٔ sample send-out پوشاک ایران»، «ارزش نمونه‌های PR»، «بودجهٔ creator seeding فشن» یا «تعداد accountهای واجد شرایط» در desk-research پیدا نشد. بنابراین TAM پولی نباید اکنون با یک عدد قطعی ارائه شود.

### ۵-۲. روش bottom-up لازم

`SAM سالانه = تعداد accountهای واجد ICP × نرخ پذیرش software × ARPA سالانه`.

برای قابل دفاع شدن مدل، باید در interview/market mapping ثبت شود:

1. تعداد برند/agency با حداقل حجم گردش نمونه در ۱۲ ماه؛
2. تعداد نمونهٔ امانی و متوسط duration هر گردش؛
3. ارزش جایگزینی/هزینهٔ گم‌شدن یا فرصت از دست‌رفته؛
4. نفر-ساعت پیگیری/گزارش دستی؛
5. budget owner و price anchor؛
6. willingness برای workspace مستقل در برابر Excel/agency service.

### ۵-۳. مدل درآمدی قابل آزمون، نه قیمت نهایی

- اشتراک workspace برند/agency با سقف active sample یا active campaign؛
- tier بالاتر برای چند تیم، audit/reporting و permission؛
- onboarding محدود و paid pilot؛
- **نه** commission از قرارداد influencer و **نه** درصد ارزش لباس؛ چون محصول marketplace/financial intermediary نیست.

---

## ۶. محصول حداقلی، عملیات و ریسک

### MVP پیشنهادی برای آزمون

1. catalog نمونه با code/QR، عکس، ویژگی و وضعیت؛
2. request، reservation و approval؛
3. handoff log و reminder بازگشت؛
4. return/condition با عکس قبل و بعد؛
5. creator/campaign link، asset URL و permission note؛
6. dashboard: overdue، unavailable، unresolved condition و activation pending.

### non-goals صریح

- تامین اینفلوئنسر، انتخاب خودکار creator، پرداخت یا escrow؛
- حمل، دریافت فیزیکی، انبارداری یا ارزیابی خسارت در میدان؛
- attribution قطعی فروش یا MIV بومی؛
- POS، PLM، DAM عمومی یا social listening کامل.

### ریسک‌ها

| ریسک | اثر | کاهش/آزمون |
|---|---|---|
| حجم گردش برای SaaS مستقل کم باشد | استفادهٔ episodic و عدم renewal | segment based on actual send-outs؛ price test و pilot پولی. |
| آژانس‌ها مشکل را با نیروی انسانی حل کنند | buyer SaaS ندارد | بررسی unit economics agency و امکان white-label/agency workspace؛ بدون تبدیل شدن به service. |
| دریافت‌کننده portal را باز نکند | status واقعی ناقص می‌شود | flow موبایلیِ بدون account، لینک تأیید، یادآوری چندکاناله؛ adoption در pilot سنجیده شود. |
| خسارت/ودیعه به dispute حقوقی تبدیل شود | scope creep و ریسک حقوقی | tool فقط evidence/audit record باشد؛ شرایط قرض و مسئولیت قرارداد brand/agency بماند. |
| asset-right مبهم باشد | استفادهٔ نامجاز محتوا | ثبت permission status و template consent؛ review حقوقی پیش از scale. |
| محصول به influencer marketplace منحرف شود | overlap و عملیات شبکه‌ای | rule: هیچ inventory شبکهٔ creator یا commission در MVP. |

---

## ۷. برنامهٔ اعتبارسنجی و kill criteria

### مصاحبهٔ کشف (۱۵ مصاحبه)

- ۵ نفر مدیر برند/PR/marketing در پوشاک؛
- ۴ نفر account یا operations agency؛
- ۳ نفر sample coordinator/showroom/stylist؛
- ۳ نفر creator یا stylist دریافت‌کنندهٔ نمونه.

روش باید **artifact-based** باشد: برای آخرین سه گردش واقعی، نمونه، تاریخ خروج، پیام‌های پیگیری، وضعیت بازگشت، مشکل، هزینه و استفاده از محتوا بررسی شود. پرسش «اگر اپ بسازیم می‌خری؟» به‌تنهایی معتبر نیست.

### شرط ورود به pilot

- دو customer متفاوت، pilot پولی ۶ تا ۸ هفته‌ای؛
- حداقل یک collection یا ۱۰–۳۰ sample movement واقعی برای هر customer؛
- استفادهٔ مسئول برند و دست‌کم بخشی از دریافت‌کنندگان از flow؛
- baseline ثبت‌شده از نفر-ساعت پیگیری، overdue و missing/uncertain status.

### KPI pilot

- درصد sample با custodian، موعد و status قابل مشاهده؛
- درصد گردش با return/condition ثبت‌شده؛
- مدت زمان پاسخ به «این نمونه اکنون کجاست؟»؛
- تعداد conflict رزرو یا پیگیری دستی؛
- درصد activationهای دارای link و permission status؛
- willingness برای renewal بعد از پایان pilot.

### hard kill

مسیر باید متوقف شود اگر: (۱) در مصاحبه‌ها درد version/status/return تکرارشونده و هزینه‌دار دیده نشود؛ (۲) هیچ دو customer برای pilot پولی commit نکنند؛ (۳) دریافت‌کننده/agency flow سادهٔ تأیید را استفاده نکند؛ یا (۴) اکثر accountها حجم آن‌قدر کم داشته باشند که Excel/WhatsApp کفایت کند.

---

## ۸. verdict desk-research

**F-01 در وضعیت «فعال برای اعتبارسنجی» باقی می‌ماند.** category جهانی و workflow تخصصی آن به‌خوبی اثبات شده است. بازار ایران دارای پلتفرم‌های campaign/influencer و ابزارهای عمومی است، اما در desk-research evidence مستقیم از sample-loan record تخصصی پیدا نشد. این فاصله فقط یک hypothesis است؛ نه سفیدبودن بازار و نه مجوز ساخت.

ارزش این مسیر فقط در یک wedge محدود است: **accountability نمونهٔ فیزیکی و handoff قابل‌ردیابی از PR/creator request تا return و asset-right.** هر تلاش برای افزودن marketplace، fulfillment یا full media intelligence باید خارج از thesis فعلی تلقی شود.

---

## منابع و ledger شواهد

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
