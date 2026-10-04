# پژوهش جدی مراحل اولیهٔ طراحی تا دوخت پوشاک

**تاریخ:** ۴ اکتبر ۲۰۲۶  
**دامنه:** از brief/طراحی تا الگو، نمونه، تأیید پیش‌تولید، برش/دوخت و QC. این سند B2B است: شاید کاربر روزانه طراح یا الگوساز باشد، اما buyer بالقوه برند، تولیدی یا تیم محصول است.  
**قاعده:** وجود یک شرکت بزرگ خارجی، به‌تنهایی نشانهٔ فرصت ایران نیست. برای هر stage، جایگزین محلی، وابستگی عملیاتی و انطباق با تصمیم‌های قبلی کاربر سنجیده شده‌اند.

---

## 1) نقشهٔ واقعی جریان کار

`Brief / range` → `sketch & technical flat` → `tech pack + BOM + points of measure` → `pattern / grading / marker` → `proto sample` → `fit comments & revision` → `size/pre-production sample` → `bulk-release` → `cut / sew / finish` → `AQL/QC/CAPA`.

سه خانوادهٔ محصول جهانی در طول این زنجیره تکرار می‌شوند:

1. **CAD/3D authoring**: خلق و مهندسی لباس و الگو؛ مانند CLO، Browzwear، Optitex و Gerber.
2. **PLM / handoff**: یک record واحد برای tech pack، BOM، نمونه، approval، supplier و release؛ مانند Techpacker، Delogue، WFX، Centric و Lifecycle.
3. **Factory execution / quality**: برنامه‌ریزی، تولید، بازرسی، defect و corrective action؛ مانند FastReactPlan و Inspectorio.

تمایز مهم: CAD یک ابزارِ ساخت است، PLM یک system-of-record برای تصمیم‌ها و نسخه‌هاست، و MES/ERP/QC یک system-of-execution در کارخانه است. مخلوط‌کردن این سه منشأ ایده‌های اشتباه «همه‌چیز در یک اپ» می‌شود.

---

## 2) طراحی، الگوسازی و نمونه‌سازی دیجیتال: بازار جهانی اثبات‌شده، اما فرصت محلی تازه نیست

### benchmark خارجی
- **CLO Virtual Fashion**: طراحی/شبیه‌سازی ۳بعدی، آرشیو و collaboration. از مشتریانی مثل Adidas، Inditex، Hugo Boss، Levi’s و Macy’s نام برده شده و در یک گزارش، کاهش lead time و افزایش sample adoption گزارش شده است.
  - https://www.businessoffashion.com/articles/technology/at-clo-virtual-fashion-digitising-the-design-process-to-drive-transformation/
- **Browzwear**: VStitcher/Lotta/Stylezone برای sample دیجیتال، fit، review و material simulation. خود شرکت بر مبنای بیش از ۱٬۰۰۰ شرکت، ۵۰٪ کاهش sample فیزیکی و ۹۵٪ first-time-right را گزارش می‌کند؛ این‌ها ادعاهای vendor هستند، نه benchmark مستقل.
  - https://browzwear.com/products/v-stitcher
  - https://browzwear.com/products
- CAD تولیدی سنتی نیز بالغ است: Gerber AccuMark، Lectra Modaris، Optitex و TUKAcad برای الگو، grading و marker؛ CLO جای CAD صنعتی را در marker-making نمی‌گیرد.
  - https://www.aims360.com/fashion-business-resources/best-fashion-design-software-for-apparel-brands-aims360-erp

### ایران و جایگزین‌ها
- آموزش رسمی و غیررسمی CLO3D در ایران فراوان است؛ مجتمع فنی تهران، مکتب‌خونه و دوره‌های تخصصی متعدد، طراحی، الگو و شبیه‌سازی ۳بعدی CLO را آموزش می‌دهند. عرضه/آموزش Optitex، Gerber و Gemini نیز وجود دارد.
  - https://mftniavaran.com/class/3255-2/
  - https://maktabkhooneh.org/course/دوره-طراحی-لباس-نرم-افزار-clo3d-فشن-دیجیتال-mk12430/
  - https://ofoghnet.ir/
- در این مرحله، مانع اصلی «نرم‌افزارِ نبود» نیست؛ مهارت الگوساز/طراح، کیفیت دیتای پارچه، سخت‌افزار، پذیرش کارخانه و زمان یادگیری است. محصولی که صرفاً «با AI اسکچ را لباس یا الگو می‌کند» هم با محدودیت کاربر دربارهٔ AI image/modeling و هم با نیاز به بازبینی فنی تعارض دارد.

### حکم
**رد برای ساخت محصول جدید.** بازار ابزار و آموزش وجود دارد؛ CAD/3D عمومی قبلاً نیز رد شده است. یک clone فارسی یا generator الگو، مزیت دفاع‌پذیر و buyer روشن ندارد.

---

## 3) Tech Pack، BOM، نمونه و تأیید: تنها گرهٔ قابل‌تحقیق‌تر، ولی هنوز توصیه نیست

### مسئلهٔ واقعی چیست؟
Tech pack فقط یک PDF زیبا نیست؛ «قرارداد فنی» بین برند و سازنده است: flat، اندازه و tolerance، grade rule، BOM (پارچه/خرجکار)، construction، رنگ، artwork، بسته‌بندی و approval log. شکست‌های پرهزینه معمولاً از سه چیز می‌آیند:

- factory با version قدیمی کار می‌کند؛
- fit comment یا عکسِ ایراد در WhatsApp/email گم می‌شود؛
- BOM پس از تغییر sample یا قیمت پارچه با production release همگام نمی‌شود.

Uphance دقیقاً این سه failure mode را به‌عنوان علت sample اشتباه بیان می‌کند و record versioned با approval log و دسترسی vendor را جایگزین PDFهای پراکنده می‌کند.
- https://www.uphance.com/insights/mastering-tech-pack/

### benchmark خارجی: این یک category واقعی در همهٔ مقیاس‌ها است
- **Techpacker**: tech pack، BOM، supplier sharing، version comparison و sample stage؛ ابزار سبک‌تر برای تیم کوچک، با قیمت گزارش‌شده حدود ۴۹ دلار به‌ازای کاربر در ماه.
  - https://style.clo-set.com/en/resources/article/d3a24e2976254e4ab816812436a4e780
- **Delogue**: PLM سبک/میانی برای product-development و supplier collaboration؛ اعلام می‌کند ۳۰۰+ برند فشن/lifestyle در ۷۴ کشور کاربر دارد.
  - https://www.delogue.com/en/solutions/industries/fashion
- **WFX / Uphance / Centric / Lectra Kubix Link**: لایه‌های عمیق‌تر شامل material library، costing، RFQ، vendor portal، calendar و production readiness. WFX از tech pack versioned، comment خط‌به‌خط و sample/QC/PO پشتیبانی می‌کند؛ Lectra از نمونه‌های مشتری مانند Bally، Corneliani و DIM نام می‌برد.
  - https://www.worldfashionexchange.com/fashion-plm-software.html
  - https://www.lectra.com/en/library/what-is-the-best-plm-software-for-fashion-brands-in-2026

### ایران: evidence و جایگزین واقعی
- در ایران، مفهوم **تکنیکال‌پک/Tech Pack** جا افتاده است: دورهٔ تخصصی Heymers به‌صراحت technical flat، اندازه، جدول متریال و ساخت Tech Pack با Excel/Illustrator را آموزش می‌دهد؛ نساجی‌دات‌کام هم آن را حلقهٔ اتصال design و production می‌داند.
  - https://heymers.com/تولید-محصول/دوره‌ی-تکنیکال-پک/
  - https://nasaji.com/صنعت-و-تجارت/مجموعه-اطلاعات-فنی-صنعت-مد/
- در جست‌وجوی دقیق فارسی، **محصول SaaS برجسته و اختصاصی برای version-control تکنیکال‌پک، عکس/annotation نمونه، sample-approval و bulk-release** دیده نشد. این فقط evidence اولیه است، نه اثبات خلأ.
- جایگزین‌های واقعی عبارت‌اند از Excel/Illustrator/PDF، WhatsApp/Telegram، پوشهٔ ابری، مدیر فنی باتجربه و serviceهای مدیریت‌شده. **روچی اسمارت** الگوسازی، نمونه‌دوزی، اصلاح نمونه، تأمین پارچه و تولید را به‌صورت managed service عرضه می‌کند؛ جایگزینِ workflow است، اما software record مستقل نیست.
  - https://rochismart.com/

### مرز محصولی که فقط ارزش test دارد
این **نباید** یک PLM/ERP کامل، CAD/3D، بازارگاه کارگاه‌ها، supplier marketplace، AI tech-pack generator یا ابزار مدیریت خط باشد. تنها wedge قابل‌تست:

> **«Sample-to-Bulk Release Record» برای برندهایی که با چند کارگاه کار می‌کنند:** هر style یک شناسنامهٔ versioned دارد؛ عکس نمونه با annotation، POM/اندازه و BOM approved، تاریخچهٔ تصمیم fit، قفل production-release، و تأیید دریافت/خواندن نسخه توسط کارگاه.

- **Buyer:** مدیر محصول/فنی یا مالک برندی که دست‌کم ۱۵–۲۰ style در فصل و بیش از یک کارگاه/نمونه‌دوز دارد.
- **User:** طراح، الگوساز، مدیر نمونه، کارگاه یا QC برند.
- **مدل درآمد در صورت اثبات:** SaaS بر مبنای brand/workspace یا active styles؛ نه درصد از سفارش و نه خدمات نمونه‌دوزی.
- **وابستگی عملیاتی:** شرکت نیازی به انبار، دوخت یا QC فیزیکی ندارد؛ اما onboarding، موبایل‌پسند بودن برای کارگاه و discipline ثبت داده ضروری است.

### چرا هنوز «candidate تأییدشده» نیست؟
1. ممکن است حجم style/sample در بخش بزرگی از برندها کم باشد و Excel/WhatsApp کفایت کند.
2. ممکن است خود برند برای ثبت دقیق data وقت نگذارد و مشکل را با مدیر تولید حل کند.
3. serviceهایی مثل روچی، کارگاه داخلی یا الگو‌ساز شخصی ممکن است مسئولیت واقعی را بگیرند، نه نرم‌افزار.
4. این wedge باید از PLM عمومی جدا باقی بماند؛ در غیر این صورت با تصمیم ردشدهٔ ERP/PLM تعارض پیدا می‌کند.

### آزمون قبل از ساخت
- **مصاحبهٔ artifact-based با ۱۵ نفر:** ۵ مدیر محصول/مالک برند، ۴ طراح یا تکنیکال‌دیزاینر، ۳ الگوساز/مدیر نمونه، و ۳ مدیر کارگاه. برای آخرین سه style واقعی بپرس: چند version؟ چند دور sample؟ کدام تغییر گم/دیر شد؟ کدام تصمیم سبب rework شد؟ چه کسی و با چه artifactی bulk را تأیید کرد؟
- **شرط ورود pilot:** دست‌کم دو برند، یک pilot پولی ۶ تا ۸ هفته‌ای برای ۱۵–۲۰ style یا یک collection فعال بخرند و دست‌کم دو کارگاه external لینک/record را فعالانه استفاده کنند.
- **KPI:** زمان proto تا PP sample، تعداد revision مبهم/گم‌شده، دفعات استفاده از فایل منسوخ، زمان chasing approval، و نرخ sample/production rework.
- **Kill criteria:** اگر دو مشتری پول pilot ندهند؛ یا کارگاه‌ها record موبایلی را باز/تأیید نکنند؛ یا مشکل اصلی واقعاً الگو/دوخت/تأمین باشد نه version/approval؛ یا حجم متوسط کمتر از سطحی باشد که هزینهٔ اشتراک را توجیه کند.

**حکم فعلی:** همان «فرضیهٔ قابل‌مصاحبه» قبلی، اکنون با proof جهانی و scope دقیق‌تر؛ نه فرصت تأییدشده و نه محصول آمادهٔ ساخت.

---

## 4) sourcing پارچه، خرجکار و رنگ: جهانی جدی، اما در ایران به marketplace/عملیات یا ابزار موجود می‌رسد

### benchmark جهانی
PLMهای فشن material library، BOM، RFQ، quote comparison، lab-dip و approved substitutions را در product record نگه می‌دارند. ابزارهای مستقل color-management مانند X-Rite Color iQC نیز color consistency را از specification تا supplier و production مدیریت می‌کنند.
- https://www.xrite.com/categories/formulation-and-quality-assurance-software/color-iqc

### ایران و حکم
- Color iQC در ایران عرضه می‌شود و برای کنترل رنگ pre-production/production معرفی شده است.
  - https://sa-aria.com/product/نرم-افزار-کنترل-کیفیت-رنگ-همانندی-color-iqc/
- اگر محصول به پیدا کردن/خرید پارچه، خرجکار یا کارگاه برسد، به marketplace/managed procurement و عملیات فیزیکی نزدیک می‌شود؛ روچی نیز تأمین پارچه و خرجکار را در مدل service خود دارد.

**حکم:** رد. نه سبد خرید B2B پارچه، نه lab-dip/color platform جدید؛ مگر محرک صادراتی/مقرراتی تازه‌ای کشف شود.

---

## 5) برش، دوخت و کنترل ظرفیت خط: بازار جهانی قوی، ولی لایهٔ محلی اشباع‌تر از تصور است

### benchmark خارجی
Coats Digital FastReactPlan برای capacity، critical path، material readiness و schedule چندکارخانه‌ای کار می‌کند؛ ۵۰۰+ مشتری در ۴۰+ کشور و ۲٬۰۰۰+ کارخانه را اعلام می‌کند. این نشان می‌دهد «دوخت» به‌عنوان یک category نرم‌افزاری واقعی است، نه صرفاً Excel.
- https://www.coatsdigital.com/en/manufacturer/fastreactplan/

### ایران
- آرمان تدبیر پوشاک صریحاً کنترل تولید پوشاک، زمان‌بندی، BOM، کیفیت، سفارش، انبار و کارگر را پوشش می‌دهد.
- معین، هلو، سپیدار، پگاه و تیمیار نیز مرحله‌های تولید، مواد، ضایعات، برون‌سپاری، ظرفیت، بهای تمام‌شده و گزارش را پوشش می‌دهند.
  - https://gctco.ir/arman-tadbir-pooshak/
  - https://moeinsoft.com/product/garment-production-accounting-software/
  - https://holooshop.com/product/نرم-افزار-حسابداری-مانتو-و-پوشاک-جامع-ه/

**حکم:** رد. «خط دوخت بهتر/کاربر موبایلی‌تر/داشبورد ساده‌تر» صرفاً بازنام‌گذاری ERP/MES قبلاً ردشده است.

---

## 6) QC، AQL و اقدام اصلاحی: درد واقعی است، اما whitespace نرم‌افزاری دیده نشد

### benchmark خارجی
**Inspectorio** یک platform شبکه‌ای برای quality، compliance، supplier collaboration، inspection و CAPA است. منابع مختلف از بیش از ۷هزار customer در ۲۰۲۲ و بیش از ۴۰هزار retailer/supplier در دادهٔ جدیدتر نام می‌برند؛ این ارقام vendor/third-party هستند و باید در purchase diligence راستی‌آزمایی شوند. case جدید Pistola Denim نیز نشان می‌دهد برند فشن برای in-line/final inspection، dashboard supplier quality و corrective action هزینه می‌کند.
- https://www.forbes.com/sites/rebeccaszkutak/2022/01/31/inspectorio-raises-50-million-to-help-brands-ensure-quality-in-their-supply-chain/
- https://secure.businesswire.com/news/home/20260714252192/en/Pistola-Denim-Selects-Inspectorios-Quality-Management-Platform-as-Womenswear-Brand-Scales-Production

### ایران
- AQL در بازرسی پوشاک شناخته‌شده است و در منابع تخصصی نساجی توضیح داده می‌شود.
- راهکاران همکاران سیستم پشتیبانی صریح از AQL/MIL-STD-105، بازرسی حین تولید، non-conformity و corrective action دارد؛ آرمان تدبیر پوشاک نیز QC پوشاک را داخل control-production قرار داده است.
  - https://www.systemgroup.net/products/rahkaran/manufacturing/quality-control/
  - https://shadtex.ir/سطح-کیفی-قابل-قبول-aql/

**حکم:** رد برای QC workflow عمومی یا defect-photo app. کاربرد فشن، pain را ثابت می‌کند اما ابزارهای داخلی general و ابزار تخصصی داخلی وجود دارند؛ «نبود رقیب دقیقاً با UI پوشاک» gap نیست.

---

## 7) نتیجهٔ تصمیمی

| مرحله | واقعیت جهانی | واقعیت ایران | حکم |
|---|---|---|---|
| طراحی/۳بعدی/الگوسازی | دسته بالغ با CLO/Browzwear/Optitex/Gerber | آموزش و ابزار/فروش داخلی گسترده | رد |
| Tech pack و approval | دسته واقعی از Techpacker تا PLM enterprise | آموزش/تمپلیت و managed service وجود دارد؛ direct SaaS محلی هنوز در جست‌وجو نمایان نیست | **فقط discovery hypothesis** |
| sourcing/color/lab dip | ابزار و platform جدی | ابزار رنگ موجود؛ sourcing به marketplace/عملیات می‌رسد | رد |
| کنترل خط/ظرفیت/بهای تمام‌شده | FastReact/WFX و نمونه‌های جدی | آرمان تدبیر، سپیدار، معین، هلو و ERPها | رد |
| QC/AQL/CAPA | Inspectorio category معتبر | راهکاران/تیمیار/آرمان و QC عمومی | رد |

### نتیجهٔ اصلی
در طراحی تا دوخت، «کاهش خطای انتقال تصمیم از sample تأییدشده به bulk production» تنها نقطه‌ای است که هنوز می‌تواند ارزش مصاحبه داشته باشد؛ نه به‌علت این‌که رقیب گوگل‌پذیر ندارد، بلکه چون بین ابزار خلاقانهٔ فردی و ERP تولید، یک handoff کاملاً documentable قرار دارد. حتی این مورد نیز تنها وقتی باز می‌ماند که pilot پولی و استفادهٔ مشترک برند/کارگاه آن را تأیید کند.
