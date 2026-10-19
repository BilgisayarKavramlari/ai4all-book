# IngramSpark yükleme öncesi preflight denetimi

**Kitap:** *AI for All: Career-Ready AI Skills*
**Tarih:** 2026-10-19
**Kapsam:** Yalnızca denetim yapıldı. Repoda hiçbir dosya değiştirilmedi, yeniden üretilmedi ya da silinmedi; tek yazılan dosya bu rapordur. Analizler dosyaların scratchpad'e alınan kopyaları üzerinde yapıldı.

**Denetlenen dosyalar**
- İç sayfa PDF'i: `_book/AI-for-All.pdf`. `build/out/AI-for-All.pdf` ile bayt bayt aynı (`cmp`). Boyutu 13.957.923 bayt; Typst 0.15.1 ile üretildi; oluşturma zamanı 2026-10-19 02:22 CDT.
- EPUB: `build/out/AI-for-All.epub`. `_book/AI-for-All.epub` ile bayt bayt aynı. Boyutu 2.332.871 bayt.
- Kapak dosyaları: `cover/`.
- Künye kaynakları: `typst/typst-show.typ`, `back/colophon.qmd`, `docs/decisions.md`, `CLAUDE.md`.

**Ölçüt kaynağı.** IngramSpark *File Creation Guide*, `ingramspark.com/hubfs/downloads/file-creation-guide.pdf`. PDF'in iç tarihi 2026-08-24; 2026-10-19'da indirildi. Bu rapordaki "Ingram kuralı" ifadeleri bu kılavuzdan alındı. Kılavuzun kendi rakamları yazarın kontrol listesindeki iki değerden farklı; bunlar 3. ve 4. maddede ayrıca belirtildi.

**Araçlar:** pdfinfo, pdffonts, pdfimages, pdftotext, pdftoppm (poppler), qpdf (QDF açılımı ve Python ile içerik akışı ayrıştırma), PIL, EPUBCheck 5.4.0, DAISY Ace 1.4.6. Ghostscript kurulu olmadığı için PDF/X dönüşümü denenmedi; yalnızca komutu önerildi.

---

## 1. Baskı iç sayfa PDF'i (8.5 × 11 in)

| Kontrol | Ölçülen | Ingram kuralı | Sonuç |
|---|---|---|---|
| Sayfa boyutu | 612 × 792 pt = 8.5 × 11 in. MediaBox = CropBox = TrimBox = BleedBox = 0 0 612 792 | Taşma yoksa trim boyutu; taşma varsa 8.625 × 11.25 in | Boyut doğru, ama taşma payı yok (aşağıya bakın) |
| Sayfa sayısı | **1135** (kapak dahil). Kapak çıkarılırsa **1134** | Sayfa sayısı 2'ye bölünebilmeli. Son sayfa LS üretim bilgisi için boş kalır; gerekirse LS sayfa ekler | 1135 tek sayı. Kapak çıkınca 1134 olur. Son sayfa (şimdiki 1135. sayfa) dolu olduğu için LS +2 boş sayfa ekleyip 1136'ya çıkarabilir |
| Kapak iç dosyada mı | **Evet.** 1. sayfa `cover/cover-front.svg`, renkli ve tam taşan (`typst-show.typ` satır 8–11) | İç dosyada kapak bulunmamalı; kapak ayrı bir dosya olarak yüklenir | HATA |
| Fontlar | 20 fontun **20'si gömülü ve alt kümeli** (pdffonts emb = yes) | Tüm fontlar gömülü olmalı | HAZIR |
| Raster görseller | Toplam **2 görsel**, ikisi de s. 672'de (Şekil 17.7). Her biri 278 × 278 px, **ICC tabanlı RGB (3 kanal)**, renkli (kroma 200+), **191 ppi** | Gri tonlu, 300 ppi (çizgi sanatı için 600 ppi) | HATA: renkli ve 300 ppi'nin altında |
| Vektör ve metin renkleri | Kaynaklardaki renk uzayları: yalnızca `/ICCBased` N=1 (gri) ve `/ICCBased` N=3 (RGB). DeviceCMYK, Separation/DeviceN (spot) ve Shading yok. İçerik akışlarında **252.118 RGB boyama** ve **95.229 gri boyama** komutu var. RGB kullanan sayfa/form sayısı **654**. **40 ayrı RGB rengi** var; bunların çoğu kromatik (ayrıntı aşağıda) | Renk uzayı gri tonlu olmalı; spot renk ve ICC profili bulunmamalı | HATA |
| Şekiller | Kaynaklardaki 437 şekil referansının **hepsi `figures/out/color/`** klasörünü gösteriyor. `figures/out/gray/` klasöründeki 435 dosyanın hiçbiri kullanılmıyor | Baskı için gri render | HATA. Colophon'daki "print edition is grayscale" cümlesi şu an doğru değil |
| Metin ve sayfa numarası ile trim arası | pdftotext kelime kutularına göre (kapak hariç) en küçük mesafeler: sol **1.175"**, sağ **0.873"** (s. 1079'da satır taşması), üst **0.600"**, alt **0.557"** (sayfa numaraları). Sayfa numaraları alttan 0.557", çift sayfa başlıkları üstten 0.62". **0.5"'in altında metin yok** | En az 0.5"; ayrıca ±1/16" baskı toleransı | HAZIR, ama alt kenar sınırda: 0.557 − 0.0625 = 0.495" |
| Gövde metni ile trim arası | Tek ve çift sayfalarda sol ≈ **1.18"**, sağ ≈ **1.15–1.18"**. Ayna (iç/dış) farkı yok, düzen simetrik | Kılavuz cilt tarafında 0.125" boş şerit öneriyor | İç kenar boşluğu **≈1.18"**. 1134 sayfalık kalın bir cilt için yeterli görünüyor. Not: G1 kararındaki "geniş yan kenar" düzeni PDF'e yansımamış |
| Satır taşmaları (bilgi) | Metin çerçevesinin 0.1–0.3" dışına taşan sözcükler: s. 333, 459, 789 ve 1079 | — | Hâlâ 0.5" güvenli alanın içinde. Düzeltilmesi iyi olur |
| Taşan öğeler | Sayfa kenarına (0") değen içerik **51 sayfada** var: 1. sayfa (kapak); 6 bölüm (Part) sayfası tamamen gri zeminli (s. 37, 179, 415, 583, 741, 861); s. 2'de başlık bandı tam genişlikte; **43 tek sayfada** orange-book başlık kutusu dış kenara değiyor (s. 5, 9, 11 … 1133, 1135) | Taşan öğe varsa üst, alt ve dış kenara 0.125" taşma payı eklenmeli (cilt tarafına eklenmez) | HATA: taşma payı **0"** |
| PDF/X-1a:2001 | PDF sürümü **1.7**. `/OutputIntents` yok, `GTS_PDFXVersion` yok, `/Trapped` yok, XMP'de pdfx yok. **Saydamlık var:** s. 310'da saydamlık gruplu 3 form XObject ve `CA/ca 0.9`; s. 882'de `ca 0.75`. ICC tabanlı renk uzayları var. 194 açıklama (`/Annots`, bağlantı) var | PDF/X-1a:2001 veya PDF/X-3:2002 | HATA: uyumlu değil |
| Kesim işaretleri | Yok. MediaBox trim boyutuna eşit ve kenarlarda işaret izi yok | Kesim işareti eklenmemeli | HAZIR |

**Bulunan başlıca RGB renkleri** (renk, kullanım sayısı, sayfa sayısı):
- Neredeyse nötr, hafif mavimsi gövde ve ikincil metin rengi: `#1D1D1F` (160.359 kullanım, 423 sayfa) ve `#5C5C66` (75.119 kullanım, 350 sayfa).
- Kitap paleti: `#1C3D6E` lacivert (195 sayfa), `#FCE38A` sarı (194 sayfa), `#C2410C` turuncu (118 sayfa), `#4CAF84` / `#1F5E43` / `#0B1F16` yeşiller (yaklaşık 130 sayfa).
- Quarto callout renkleri: `#0758E5` ve `#DAE6FB` mavi (338 sayfa), `#00A047` ve `#CCF1E3` yeşil (175 sayfa), `#CC1914` ve `#F7DDDC` kırmızı (136 sayfa), `#EB9113` turuncu (7 sayfa).
- Kod vurgulama: `#003B4F`, `#AD0000`, `#20794D`, `#00769E` (yaklaşık 14 sayfa).

Kaynakları:
- Renkli şekil SVG'leri.
- `typst-show.typ` içindeki `main-color: rgb("#1C3D6E")`.
- Quarto'nun varsayılan callout ve kod renkleri.
- Typst'in tüm renkleri ICC tabanlı uzaylara yazması.

**Fontlarla ilgili notlar** (yükleme engeli değil, ama risk):
- **Libertinus Serif** 1134 sayfada kullanılıyor. Bunlar orange-book'un varsayılan başlık, üst bilgi ve sayfa numarası fontu.
- **LucidaGrande** 63 sayfada, **.SFNS** (Apple sistem fontu) s. 837 ve 1058'de, **DejaVuSansMono** 14 sayfada kod için kullanılıyor.
- G2 kararı (Source Serif 4, Source Sans 3, JetBrains Mono) ve colophon'da yazan font listesi PDF'le uyuşmuyor.
- Apple fontlarının ticari baskı için gömülmesine lisansın izin verip vermediği **doğrulanmadı**. Bu fallback glifleri kaynakta değiştirilmeli.

**Önerilen dönüşüm** (Ghostscript kurulu olmadığı için çalıştırılmadı).

Önce kapak sayfası ayrılmalı; bu adım qpdf ile yapılabilir. Taşma payı ise kaynakta kurulmalı: Typst'te sayfa 8.625 × 11.25 in olur, TrimBox 0.125" içeride tanımlanır. Ghostscript taşma payı ekleyemez.

```sh
qpdf --empty --pages AI-for-All.pdf 2-z -- interior-nocover.pdf

gs -dPDFX=true -dBATCH -dNOPAUSE -dNOSAFER -sDEVICE=pdfwrite \
   -dCompatibilityLevel=1.3 -dPDFSETTINGS=/prepress \
   -sColorConversionStrategy=Gray -sProcessColorModel=DeviceGray \
   -dHaveTransparency=false -dPreserveAnnots=false \
   -dEmbedAllFonts=true -dSubsetFonts=true \
   -dDownsampleGrayImages=false \
   -sOutputFile=ISBN_txt.pdf  PDFX_def.ps  interior-nocover.pdf
```

Komut için notlar:
- `PDFX_def.ps`, Ghostscript'in `lib/` klasöründen kopyalanır. İçinde CMYK çıktı niyeti profili tanımlanır (ör. "U.S. Web Coated (SWOP) v2" ICC yolu ve `OutputConditionIdentifier`). Aynı dosyada `/TrimBox` (taşma payı varsa `[9 18 621 810]` gibi) ve `/Trapped /False` ayarlanır.
- Ortaya çıkan dosya Acrobat Preflight ya da callas pdfToolbox ile "PDF/X-1a:2001" profiline karşı doğrulanmalı. Ghostscript'in ürettiği PDF/X-1a çıktısı her zaman temiz geçmeyebilir.
- Daha temiz bir yol: şekiller kaynakta gri render'a (`figures/out/gray/`) çevrilir, baskı için gri bir tema kullanılır (callout ve kod renkleri gri, `main-color` gri), sonra yukarıdaki dönüşüm yapılır. Böylece RGB'den griye otomatik dönüşümde ortaya çıkabilecek kontrast kayıpları baştan önlenir.

---

## 2. Künye (copyright) sayfası

PDF'in 3. sayfasında `typst-show.typ` içindeki `copyright:` bloğu basılıyor:

> *AI for All: Career-Ready AI Skills* · Sadi Evren Seker · Edition 2027.1 (working draft, October 19, 2026) — not for distribution. · Licensed under CC BY-NC-SA 4.0. · This is a production draft…

| Alan | PDF (s. 3) | EPUB | Not |
|---|---|---|---|
| Baskı ISBN'i | **Yok** | — | Colophon (`back/colophon.qmd:23`): "ISBNs for the EPUB edition and the two print volumes are assigned at publication." |
| E-kitap ISBN'i | **Yok** | **Yok.** OPF `dc:identifier` = `urn:uuid:5957c717-…` | Ingram için baskı ve e-kitaba ayrı ISBN gerekiyor. D4 kararı hâlâ "3 ISBN, Vol. 1 ve Vol. 2" diyor |
| Yayıncı / imprint | **Yok** | **Yok.** OPF'de `dc:publisher` yok | — |
| Baskı / sürüm | Var: "Edition 2027.1 (working draft …) — not for distribution" | Ayrı bir künye sayfası yok; `title_page.xhtml` yalnızca başlık ve yazarı içeriyor | Taslak ibaresi kaldırılmalı. Kapakta "FIRST EDITION · 2027" yazıyor, künyede "Edition 2027.1"; ikisi tutarlı hale getirilmeli |
| Lisans | Var: CC BY-NC-SA 4.0 | Yalnızca önsözde (ch003) ve colophon'da (ch042) geçiyor; OPF'de `dc:rights` yok | — |
| © satırı | s. 3'te yok; yalnızca colophon'da "Copyright © 2027 Sadi Evren Seker" var | Yalnızca colophon'da | Künye sayfasına eklenmeli |

---

## 3. EPUB

| Kontrol | Sonuç |
|---|---|
| EPUBCheck 5.4.0 | **0 fatal / 436 error / 0 warning.** 436 hatanın hepsi tek türde: `RSC-005: attribute "alt" not allowed here`. Quarto, `fig-alt` değerini `<img>` etiketinin yanı sıra `<div class="quarto-float">` etiketine de `alt` olarak yazıyor. Hatalar 24 dosyaya dağılıyor (en çok ch024: 24; ch025, ch026, ch028 ve ch032: 22'şer). Kaynak sözdizimi (`fig-alt=`) doğru. Düzeltme için bir post-process ya da Lua filtresi div'deki `alt` özniteliğini silmeli |
| Ace 1.4.6 | Sonuç **fail**, 4 ihlal: 3 × *minor* `empty-table-header` (ch016.xhtml) ve 1 × *moderate* `metadata-accessibilitySummary` (OPF'de `schema:accessibilitySummary` eksik). accessMode, accessibilityFeature, accessibilityHazard ve accessModeSufficient mevcut |
| Dosya boyutu | **2.33 MB** (2.332.871 bayt). 100 MB sınırının altında: HAZIR |
| Büyük görseller | 434 SVG ve 1 PNG var. En büyük SVG'nin nominal boyutu 800 × 720 = 0,58 MP. SVG'ye gömülü iki raster 278 × 278 px. Kapak PNG'si **1600 × 2560 = 4,10 MP**. Yazarın 5,6 MP sınırını hiçbir görsel aşmıyor. **Ancak Ingram kılavuzunun güncel sınırı 3,2 MP**; kapak PNG'si bu sınırı aşıyor |
| "page X" atıfları | Kendi sayfasına numarayla atıf yok. 216 eşleşmenin hemen hepsi kaynakçadaki ya da dış belgelerdeki sayfa numaraları ("pp. 1–16", "AP, 2020, p. 14", "catalog page 14"); bunlar sorun değil. Akışkan EPUB'da belirsiz kalan ifade "this page": ch015, ch022, ch026, ch027, ch030, ch031 ve ch032'de okuma rotası kutularında ("Fast route …: this page, the Opening Case…"), ayrıca ch008 ve ch029'da birer kez. Ufak bir düzeltme önerilir (ör. "this opening page" ya da "the chapter opener") |
| İç kapak görseli | Var. `text/cover.xhtml` SVG sarmalayıcı içinde `media/file434.png` gösteriyor (1600 × 2560 RGB). OPF'de `properties="cover-image"` ve `<meta name="cover">` var. HAZIR |
| Meta veri (bilgi) | OPF'de dc:publisher, dc:rights, dc:description ve dc:subject yok; tanımlayıcı UUID. Ingram meta verileri portalda da alınıyor, ama ISBN'i OPF'e yazmak iyi uygulama |

---

## 4. E-kitap kapağı

| Ölçüt | Mevcut | Sonuç |
|---|---|---|
| Biçim | `cover/cover-epub.png`: **PNG**. Repoda kapak için JPG yok (yalnızca `.quarto/` altında orange-book şablon JPG'leri var) | EKSİK: Ingram **.jpg** istiyor |
| Renk modu | RGB, ICC profili yok | HAZIR |
| Boyut | **1600 × 2560 px**. Uzun kenar 2560, kısa kenar 1600 | Yazarın ölçütüne uyuyor (uzun 2560, kısa ≥1600). Ingram kılavuzunun güncel en az ölçüsü 1873 × 1600 px; bu da sağlanıyor |
| Dosya boyutu | PNG 151.833 bayt | 100 MB sınırının çok altında |

Gereken iş: aynı görselden kalite ≈90 olan bir RGB JPEG üretmek (ör. `cover/cover-epub.jpg`). Bu denetimde dosya üretilmedi.

---

## 5. Tam kapak (arka kapak + sırt + ön kapak)

**Durum: EKSİK.**
- Repoda arka kapak, sırt ya da sarmal (wraparound) kapak dosyası yok.
- `cover/cover-front.svg` yalnızca ön yüz; boyutu 612 × 792 pt, taşma payı yok, renkler RGB, metinler canlı SVG metni.
- `cover/README.md`'ye göre başlık, USPTO taraması ve yazar onayı hâlâ açık.

**Ingram Cover Template Generator'a girilecek bilgiler** (Dashboard › My Tools):
- Baskı ISBN'i (barkod şablona bu ISBN'den gelir)
- Trim: 8.5 × 11 in
- Cilt: **Paperback, Perfect Bound**
- İç sayfa: **Black & White, Standard, 50 lb (74 gsm) White**
- Kapak kaplaması: Matte veya Gloss
- **Kesin sayfa sayısı** (2'nin katı): kapak çıkarıldıktan ve son boş sayfa ayarlandıktan sonraki değer, muhtemelen 1134 veya 1136
- Dosya biçimi: PDF veya InDesign
- Ingram'ın kapak kuralları: CMYK, 300 ppi, 0.125" taşma payı (dört kenar), 0.25" güvenli alan, sırt metni için kenarlardan 0.0625" boşluk, barkod %100 siyah ve beyaz zemin üzerinde (en az 1.75 × 1"), PDF/X-1a:2001 veya PDF/X-3:2002, toplam mürekkep ≤ %240

**Sırt genişliği tahmini** (kesin değer şablondan alınmalı):
- Formül: sırt genişliği = sayfa sayısı × sayfa kalınlığı = sayfa sayısı ÷ PPI.
- Ingram kılavuzu bu kalınlık değerini yayımlamıyor; sırt genişliğini şablon üreticisine bırakıyor.
- Üçüncü taraf kaynaklarda 50 lb beyaz kâğıt için iki değer geçiyor: **0.002252 in/sayfa (444 PPI)**, ki aynı değer KDP'nin beyaz kâğıdı için de kullanılıyor, ve **0.0020 in/sayfa (500 PPI)**.

| Sayfa sayısı | 0.002252 in/sayfa | 0.0020 in/sayfa |
|---|---|---|
| 1134 (kapak çıkmış) | **2.554 in (64.9 mm)** | 2.268 in (57.6 mm) |
| 1136 (LS 2 sayfa eklerse) | 2.558 in | 2.272 in |

- Ana tahmin: **≈ 2.55 in**. Sarmal kapak ≈ 0.125 + 8.5 + 2.55 + 8.5 + 0.125 = **≈ 19.80 × 11.25 in** (taşma payı dahil).
- **Bu bir tahmindir; kesin değer Ingram'ın Cover Template Generator'ından alınmalı.**
- 50 lb beyaz perfect-bound için azami sayfa sayısı üçüncü taraf kaynaklarda 1.200 olarak geçiyor. 1134 sayfa bu sınıra yakın; 8.5 × 11 için sınır **doğrulanmadı**, portalda kontrol edilmeli.

---

## 6. Draft2Digital / D2D ve iki cilt atıfları

### Kitap metni (basılan ve EPUB'a giren içerik)

| Dosya:satır | İçerik |
|---|---|
| `back/colophon.qmd:7` | "The first release is through **Draft2Digital**, as an EPUB ebook and a print edition in **two volumes**: Volume 1 holds Parts I–II … Volume 2 holds Parts III–VI". PDF ve EPUB'a basılıyor |
| `back/colophon.qmd:23` | "ISBNs for the EPUB edition and the **two print volumes** are assigned at publication." |
| `back/colophon.qmd:9` (ilgili) | "The print edition is grayscale…": şu anki PDF renkli olduğu için doğru değil |
| `back/colophon.qmd:3` | HTML yorumu (basılmıyor). D1, D3–D5 kararlarına atıf yapıyor |

`index.qmd`, `front/`, `chapters/`, `appendix/`, `labs/` ve `cases/` klasörlerinde D2D ya da iki cilt atfı **yok**. "Volume 1: Long Papers" gibi eşleşmeler yalnızca kaynakça alıntılarıydı ve elendi.

### İç belgeler, ayarlar ve araçlar

- `CLAUDE.md:16, 17, 19, 28`: "Draft2Digital Print", "EPUB + D2D Print, two volumes", "D2D rules change…", ai4all-publisher-d2d skill'i
- `_quarto.yml:2`: yorum satırı, "grayscale, Draft2Digital Print"
- `docs/decisions.md:11` (D3 Draft2Digital), `:12` (D4 ISBN: "print Volume 1, print Volume 2"), `:13` (D5 iki cilt)
- `docs/design-options.md:3, 17, 19, 26, 68, 82`
- `docs/book-map.md:77, 78`
- `docs/visual-guide.md:53`
- `docs/blueprints/ch20-blueprint.md:283`: "the book (sold via D2D)"
- `prompts/02-decisions-and-design.md:3, 4`
- `.claude/skills/ai4all-publisher-d2d/SKILL.md`: skill'in tamamı D2D üzerine (satır 2–25)
- `.claude/skills/ai4all-production-build/SKILL.md:12, 22`
- `.claude/skills/ai4all-book-designer/SKILL.md:8, 12, 13`
- `.claude/skills/ai4all-diagram-maker/SKILL.md:8`
- `docs/voice/samples/TR_2016_Musteri_Kayip_Analizi.md:81`: yazarın 2015 tarihli bir kitabına yapılan tarihsel kaynak atfı. Değiştirilmemeli
- `tools/` ve `figures/scripts/` içinde eşleşme yok
- Repoda **IngramSpark kararı hiçbir yerde kayıtlı değil**: `docs/decisions.md` hâlâ D3/D4/D5'te D2D ve iki cilt diyor

---

## Doğrulanamayan noktalar

- PDF/X-1a uyumu yalnızca yapısal olarak incelendi (OutputIntent, sürüm, saydamlık, ICC). Ghostscript ve Acrobat/callas preflight bulunmadığı için dönüşüm sonrası uyum test edilmedi.
- RGB'den griye dönüşümde callout ve kod renklerinin kontrastı ölçülmedi. Gri render'lar baskı PDF'inde kullanılmadığı için kâğıttaki görünüm bilinmiyor.
- Ingram'ın 50 lb beyaz kâğıt kalınlığı ve 8.5 × 11 B&W için azami sayfa sayısı Ingram'ın kendi belgelerinde bulunamadı. Verilen sırt değeri tahmindir.
- LucidaGrande ve .SFNS gibi Apple sistem fontlarının ticari baskıda gömülmesine lisansın izin verip vermediği doğrulanmadı.
- Taşma tespiti 36 dpi taramayla yapıldı. Kenara 0.03"ten daha yakın, çok ince öğeler gözden kaçmış olabilir.
- Kılavuzdaki EPUB görsel sınırı (3,2 MP) ve e-kitap kapağı ölçüsü (1873 × 1600) yazarın kontrol listesindeki değerlerden (5,6 MP ve 2560 px) farklı. Yükleme sırasında Ingram portalının gösterdiği güncel değerler esas alınmalı.

---

## Özet tablo

| Madde | Durum | Düzeltme önerisi |
|---|---|---|
| 1a. Trim boyutu (8.5 × 11) | HAZIR | — |
| 1b. Sayfa sayısı (1135, tek) | HATA | Kapak çıkınca 1134 olur. Son sayfayı boş bırakın ya da LS'nin +2 sayfa ekleyeceğini hesaba katın. Kesin sayıyı kapak şablonunda kullanın |
| 1c. Kapak iç dosyada (s. 1) | HATA | `typst-show.typ` içindeki kapak sayfasını baskı derlemesinde kapatın ya da `qpdf --pages . 2-z` ile ayırın |
| 1d. Fontlar gömülü (20/20) | HAZIR | İsteğe bağlı: Libertinus, LucidaGrande, .SFNS ve DejaVu yerine G2 fontlarını (Source Serif 4, Source Sans 3, JetBrains Mono) zorlayın |
| 1e. Raster görseller (2 adet, s. 672, RGB, 191 ppi) | HATA | Gri tonlu ve ≥300 ppi olarak yeniden üretin (şekil 17.7 ısı haritaları) |
| 1f. Vektör renkleri (RGB ve ICC; 654 sayfa, 40 renk) | HATA | Baskı derlemesinde gri şekilleri (`figures/out/gray/`) ve gri temayı kullanın (`main-color`, callout ve kod renkleri); ICC'siz DeviceGray çıktı alın |
| 1g. Metin ve sayfa numarası ≥ 0.5" | HAZIR | Alt kenar 0.557" ile sınırda; mümkünse ≥ 0.6" yapın. s. 333, 459, 789 ve 1079'daki satır taşmalarını düzeltin |
| 1h. İç kenar (gutter) ≈ 1.18" | HAZIR | Düzen simetrik; G1'deki "geniş yan kenar" uygulanmamış (yalnızca tasarım notu) |
| 1i. Taşma payı (51 sayfa kenara değiyor, pay 0") | HATA | Sayfayı 8.625 × 11.25 yapıp TrimBox tanımlayın ya da bölüm/başlık kutularını trim içine çekin |
| 1j. PDF/X-1a:2001 (PDF 1.7, OutputIntent yok, saydamlık s. 310 ve 882) | HATA | Yukarıdaki Ghostscript komutunu kullanın (`PDFX_def.ps`, Gray, saydamlığı düzleştirme), sonra preflight ile doğrulayın |
| 1k. Kesim işaretleri | HAZIR | — |
| 2a. Baskı ve e-kitap ISBN'leri | EKSİK | İki ISBN alın (baskı ve EPUB); künyeye ve OPF'e `dc:identifier` olarak yazın. D4 kararını güncelleyin |
| 2b. Yayıncı / imprint | EKSİK | Künyeye ve OPF'e `dc:publisher` ekleyin |
| 2c. Baskı / sürüm alanı | HATA | "working draft — not for distribution" ibaresini kaldırın; kapaktaki "FIRST EDITION · 2027" ile "Edition 2027.1"i tutarlı yapın |
| 2d. Lisans alanı | HAZIR | Künyeye © satırı ekleyin. EPUB'a künye sayfası ve `dc:rights` ekleyin |
| 3a. EPUBCheck (436 hata, hepsi RSC-005) | HATA | Quarto çıktısındaki `div.quarto-float` etiketinden `alt` özniteliğini silen bir filtre ya da post-process ekleyin |
| 3b. Ace (4 ihlal) | HATA | `schema:accessibilitySummary` meta verisini ekleyin; ch016'daki 3 boş tablo başlığını doldurun |
| 3c. EPUB boyutu (2.33 MB) | HAZIR | — |
| 3d. Görsel piksel sınırı | HATA | Hiçbir görsel 5,6 MP'yi aşmıyor; ama kapak PNG'si (4,1 MP) kılavuzun 3,2 MP sınırını aşıyor. EPUB içindeki kapağı ≤3,2 MP'ye küçültün (ör. 1400 × 2240) |
| 3e. "page X" atıfları | HAZIR | Numarayla atıf yok. İsteğe bağlı: okuma rotası kutularındaki "this page" ifadesini değiştirin |
| 3f. İç kapak görseli | HAZIR | — |
| 4. E-kitap kapağı (PNG, RGB, 1600 × 2560) | EKSİK | Aynı görselden RGB **JPG** üretin |
| 5. Tam kapak (arka + sırt + ön) | EKSİK | ISBN alınıp sayfa sayısı kesinleşince Ingram şablonunu isteyin (8.5 × 11, Paperback, 50 lb White, B&W). Sırt ≈ 2.55" (tahmin). Sarmal kapağı CMYK ve PDF/X olarak, 0.125" taşma payı ve barkodla üretin |
| 6a. Kitap metninde D2D / iki cilt | HATA | `back/colophon.qmd:7` ve `:23`'ü IngramSpark ve tek cilde göre yeniden yazın; `:9`'daki "grayscale" ifadesini gerçek çıktıyla tutarlı hale getirin |
| 6b. İç belgelerde D2D / iki cilt | EKSİK | `docs/decisions.md` (D3–D5) içine IngramSpark ve tek cilt kararını ekleyin; CLAUDE.md, `_quarto.yml` yorumu, skill'ler ve docs/ içindeki atıfları güncelleyin; publisher-d2d skill'inin yerine Ingram karşılığını yazın |

---

## Düzeltmeler (19 Ekim 2026)

Yazarın onayıyla yapılan düzeltmeler. ISBN, yayıncı adı ve tam (sarmal) kapak yazara bırakıldı.

**Yeni üretim komutları (karar D29):**

```bash
quarto render --profile print --to typst   # baskı iç dosyası -> _book-print/AI-for-All.pdf
tools/make-print-pdfx.sh                   # PDF/X-1a:2001 -> _book-print/AI-for-All-interior-PDFX1a.pdf
quarto render --to epub                    # EPUB -> _book/AI-for-All.epub
quarto render --to typst                   # ekran PDF'i (renkli, kapaklı) -> _book/AI-for-All.pdf
```

| Madde | Önceki durum | Yapılan | Yeni durum |
|---|---|---|---|
| 1b–1c. Kapak iç dosyada | HATA | Baskı profili (`_quarto-print.yml`, `print-edition: true`) kapak sayfasını koymuyor | HAZIR (kapak yok) |
| 1b. Sayfa sayısı | 1135 | Gövde yazısı tasarımdaki Source Serif 4'e geçti; baskıda 10 pt ve daha dar kenar boşlukları (iç 2.3 cm = 0.91", dış 2 cm, üst/alt 2.5 cm) | **1109 sayfa (çift)**. Ingram'ın 8.5 × 11, 50 lb white için azami sayfa sayısı doğrulanmalı (ikincil kaynaklar 1,050–1,200 diyor) |
| 1d. Fontlar | Gömülü, ama Apple sistem fontları (.SFNS, Lucida Grande, Symbol) yedek olarak giriyordu | Typst'te gövde/başlık/kod fontları açıkça ayarlandı; şekillerde ve grafiklerde yedek font STIX (SIL OFL); bir şekilde "⊃" yazıyla değiştirildi | HAZIR: yalnızca Source Serif 4, Source Sans 3, JetBrains Mono, New Computer Modern Math, Font Awesome; hepsi gömülü |
| 1e. Raster görseller | 2 adet RGB, 191 ppi | Şekil 17.8 600 dpi ile yeniden üretildi | HAZIR: gri, 720 ve 1033 ppi |
| 1f. Renkler | RGB/ICC, 654 sayfa | Baskıda gri şekiller (`tools/print-gray-figures.lua`) ve gri tema; Ghostscript dönüşümü DeviceGray | HAZIR: PDF/X dosyasında DeviceRGB, ICCBased ve CMYK sıfır |
| 1g. Trim'e uzaklık | Alt 0.557" | Yeni düzen ölçüldü | Sol 0.785", sağ 0.525", alt 0.549" (≥0.5"). Üstteki 0.17" ölçümü bölüm sayfasındaki büyük "I" harfinin font kutusu; mürekkep 1" altında |
| 1h. Gutter | ≈1.18" | Baskıda iç kenar 2.3 cm | 0.91" (Ingram'ın kalın kitap için 0.875" alt sınırının üstünde) |
| 1i. Taşma payı | 51 sayfa kenara değiyor | Baskıda bölüm sayfalarının tam sayfa zemini ve başlık kutularının kenara uzanan biçimi kaldırıldı (heading-style 1); başlık sayfası bandı kapalı | HAZIR: kenarda mürekkep yok; taşma payı gerekmiyor |
| 1j. PDF/X-1a:2001 | Değil | `tools/make-print-pdfx.sh` (Ghostscript 10.08, `tools/pdfx/PDFX_def_ai4all.ps`, CGATS TR 001 çıktı niyeti, saydamlık düzleştirme, bağlantı açıklamaları kaldırıldı) ve `tools/pdfx/add_trimbox.py` (her sayfaya TrimBox) | Yapısal olarak HAZIR: PDF 1.3, GTS_PDFXVersion = PDF/X-1a:2001, OutputIntent var, 1109 sayfanın hepsinde TrimBox, Annots/SMask/Group yok. Acrobat Preflight ya da callas ile resmî doğrulama yapılmadı |
| 2c. Künye "working draft" | HATA | Künye: "First edition, 2027 (edition 2027.1)", telif satırı, lisans; Publisher ve ISBN alanları "[to be added]" | HAZIR (ISBN ve yayıncı yazarda) |
| 3a. EPUBCheck | 436 hata | EPUB için `tools/epub-strip-div-alt.lua` | HAZIR: 0 hata, 0 uyarı |
| 3b. Ace | 4 ihlal | Erişilebilirlik meta verisi (`_quarto.yml`); 3 tablonun boş başlık hücresi dolduruldu (Bölüm 7, 14, 21) | HAZIR: Ace "pass", 0 ihlal |
| 3d. EPUB içi kapak | 4,1 MP | `cover/cover-epub-inner.jpg` 1400 × 2240 (3,14 MP) | HAZIR |
| 2d. dc:rights | Yoktu | `_quarto.yml` epub `rights` | HAZIR |
| 4. E-kitap kapağı | PNG | `cover/cover-ebook.jpg` 1600 × 2560, RGB, JPG | HAZIR |
| 6a–6b. D2D ve iki cilt | HATA/EKSİK | Künye IngramSpark ve tek cilt; `docs/decisions.md` D29 (D3 ve D5'in yerini alır, D4 iki ISBN); CLAUDE.md, `_quarto.yml` yorumu ve üç skill güncellendi | HAZIR (eski karar satırları "superseded" notuyla tarihçe olarak duruyor) |

**Hâlâ yazarda:** ISBN'ler (baskı ve EPUB), yayıncı/imprint adı, tam kapak (Ingram kapak şablonu son sayfa sayısıyla: 1109 sayfa, 8.5 × 11, paperback, 50 lb white, B&W).
