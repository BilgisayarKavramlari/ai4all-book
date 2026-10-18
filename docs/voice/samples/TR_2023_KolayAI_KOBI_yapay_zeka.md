Source: Google Drive 1YRKfeX4-13ipo2ochFrcuDSSKKCyjhnm (YBS Ansiklopedi v.11 is.1, Ocak 2023; sole author; Turkish), pulled 2026-10-17

YBS Ansiklopedi

www.YBSAnsiklopedi.com

Cilt 11, Sayı 1, Ocak 2023

KOBİ’lere Özel Basit Yapay Zeka Çözümü : Kolay.AI

KOBİ segmentine özel olarak yapay zeka çözümlerini paket şekilde sunan yazılım tasarımı.

Şadi Evren ŞEKER*

İstanbul Üniversitesi, Bilgisayar Mühendisliği Bölümü

KOBİ’ler özellikle Türkiye gibi düşük sermayeli girişimlerin yoğun olduğu ülkelerde kritik öneme sahip şirketleri ifade etmektedir. Türkiye’deki şirketlerin %99’unun KOBİ vasfında olduğu düşünüldüğü zaman KOBİ’ler için yapay zekanın önemi daha da net görülmektedir. Önemli olmasının yanı sıra, yapay zekanın ulaşılabilirliği de sorun oluşturmaktadır. Örneğin 5-10 çalışanı olan bir KOBİ’nin yapay zeka konusunda uzman istihdam etmesi ve doğru işleri ataması veya atanan işlerin doğru yapılıp yapılmadığını kontrol etmesi çoğu zaman mümkün değildir. Yapay zekanın demokratizasyonu açısından KOBİ’lerin özel projelerle yapay zeka alanında ilerlemektense hazır yazılımlar kullanmasının daha doğru bir tercih olacağı en azından bu dönem için görülmektedir. Bir çözüm olarak Kolay.AI isimli yazılım KOBİ’leri hedefleyerek yapay zeka çözümlerini içeren bir paket program olarak sunulmaktadır ve genelde KOBİ’lerde yaşanan veri disiplini, kalitesi ve erişimi problemlerini de çözerek yönetici seviyesinde çözümler üretmektedir.

Anahtar Kelimeler: KOBİ, Yapay Zeka, Makine Öğrenmesi, Müşteri Kayıp Analizi, Müşteri Segmentasyonu, RFM, Ürün Fiyat Analizi

SMEs, especially in countries like Turkey where low-capital ventures are prevalent, refer to companies of critical importance. Considering that 99% of companies in Turkey are classified as SMEs, the importance of artificial intelligence for SMEs becomes even more apparent. In addition to its significance, the accessibility of artificial intelligence also poses a problem. For instance, it is often not feasible for an SME with 5-10 employees to hire an AI expert, assign the right tasks, or ensure the correct execution of assigned tasks. In terms of the democratization of AI, it is seen as a more appropriate choice, at least for this period, for SMEs to use ready-made software rather than advancing in the field of AI with special projects. As a solution, a software called Kolay.AI is offered as a package program that targets SMEs and includes AI solutions, aiming to address data discipline, quality, and accessibility issues typically encountered in SMEs and provide managerial-level solutions.

Anahtar Kelimeler: SME, Artificial Intelligence, Machine Learning, Customer Churn Analysis, Customer Segmentation, RFM, Product Price Analysis

GİRİŞ

Makine öğrenimi, perakende dahil olmak üzere çeşitli endüstrilere devrim niteliğinde etkileri olan bir teknolojidir. Perakendeciler, müşteri deneyimini iyileştirmek, envanter yönetimini optimize etmek ve gelecekteki trendleri tahmin etmek için makine öğrenimini kullanmaya başlamışlardır. Bu böümde, makine öğrenmesi uygulamalarının KOBİ'ler için kullanımıyla ilgili bir girişten sonra, müşteri segmentasyonu sorununu, uygulamalarını ve RFM (Recency, Frequency, Monetary) tekniğini daha detaylı olarak ele alacağız.

KOBİ'ler ve Müşteri Bazı Makine Öğrenmesi Uygulamaları

KOBİ'ler için makine öğreniminin başlıca uygulamalarından biri Müşteri Segmentasyonudur [1]. Müşteri segmentasyonu, müşterileri ortak özelliklere göre gruplara ayırma sürecidir. Makine öğrenimi algoritmaları, perakendecilere benzersiz müşteri segmentlerini belirlemelerine ve pazarlama kampanyalarını buna göre uyarlamalarına yardımcı olabilir. Marisa ve diğerleri (2019) tarafından yapılan bir çalışma, makine öğrenimi algoritmalarını müşterilerin yaşam boyu değerlerine dayanarak müşteri segmentasyonu yapmak için kullanmıştır. Çalışma, müşteri segmentasyonuna dayalı kişiselleştirilmiş pazarlama kampanyalarının perakendecinin genel karını artırdığını buldu.

KOBİ'ler için diğer iyi bilinen bir makine öğrenmesi uygulaması Ürün Öneri Sistemleridir [3]. Ürün öneri sistemleri, makine öğrenimi algoritmalarını kullanarak müşterilere geçmiş satın alma geçmişlerine ve gezinme davranışlarına dayanarak ürünler önerir. Kumar ve ark. (2022) tarafından yapılan bir çalışma, bir çevrimiçi perakendeci için bir ürün öneri sistemi oluşturmak için bir ilişki kuralları madenciliği (Association Rule Mining, ARM) modeli kullanılmıştır. Çalışma, ARM modelinin müşterilerin ve göz attıkları ürünlerin takibini yapmanın yanı sıra müşterilerin e-ticaret mağazasını nasıl kullandığını kategorize ederek satıcının özel ihtiyaçlarına hitap edebileceğini bulmuştur.

Talep tahmini, satış tahmini ve stok/envanter yönetim sistemleri de KOBİ'ler için önemlidir [5]. Envanter yönetimi, perakende işletmelerin kritik bir yönüdür. Makine öğrenimi algoritmaları, perakendecilere talebi tahmin etmelerine ve envanter seviyelerini optimize etmelerine yardımcı olarak stokların tükenmesi veya aşırı stoklanma olasılığını azaltabilir. Naidoo (2021) tarafından yapılan bir çalışma, bir perakendeci için ürün talebini tahmin etmek ve envanter seviyelerini optimize etmek için bir makine öğrenimi algoritması kullandı. Çalışma, algoritmanın envanter tutma maliyetlerini azaltırken yüksek müşteri hizmet seviyelerini korumak için kullanışlı olabileceğini ortaya koydu.

Hile Tespiti ve anomalilerin yakalanması, KOBİ'ler için makine öğrenmesinin başka bir uygulamasıdır [7]. Hile tespiti, perakende endüstrisinde makine öğreniminin başka bir kritik uygulamasıdır. Makine öğrenimi algoritmaları, işlem verilerini analiz ederek kredi kartı dolandırıcılığı ve kimlik hırsızlığı gibi sahtekarlık faaliyetlerini tespit edebilir. Błaszczyński ve ark. (2021) tarafından yapılan bir çalışma, otomatik kredi verme işlemlerinde sahtekarlık faaliyetlerini tespit etmek için makine öğrenimi algoritmalarını kullandı. Çalışma, algoritmaların KOBİ'ler için uygulanabilir olduğunu ortaya koydu ve ayrıca rastgele orman veya destek vektör makinesi gibi geleneksel makine öğrenimi algoritmalarından daha iyi performans gösteren hakimiyet tabanlı kesikli kümeleme yaklaşımı adında yeni bir yöntem önerdi.

Sonuç olarak, makine öğreniminin perakende endüstrisinde müşteri segmentasyonundan ürün öneri sistemlerine, envanter yönetimine ve hile tespitine kadar birçok uygulaması bulunmaktadır. Akademik çalışmalar, makine öğrenimi algoritmalarının perakende işlemlerini ve müşteri deneyimini önemli ölçüde iyileştirebileceğini göstermektedir.

KOBİ'ler İçin Müşteri Segmentasyonunun Makine Öğrenmesi Uygulamaları

Müşteri segmentasyonu, demografik bilgiler, satın alma davranışı ve tercihler gibi ortak özelliklere dayanarak müşterileri farklı gruplara ayırma sürecidir. Makine öğrenimi, perakendecilerin müşteri segmentasyonu yapmaları ve pazarlama stratejilerini kişiselleştirmeleri için giderek daha popüler bir araç haline gelmiştir. Önceki bölümde, müşteri davranışına dayalı müşteri segmentasyonu zaten bahsedilmişti. Müşteri segmentasyonu için başka bazı boyutlar da vardır:

Sosyal Medya Davranışına Dayalı Müşteri Segmentasyonu [9]. Sosyal medya platformları, müşterileri segmente etmek için kullanılabilecek birçok bilgi sağlar. Arasu ve diğerleri (2020) tarafından yapılan bir çalışma, makine öğrenimi algoritmalarını kullanarak müşterileri sosyal medya davranışlarına göre segmente etmek için kullanmıştır [10]. Çalışma, makine öğrenimi algoritmalarını kullanarak müşterileri sosyal medya davranışlarına göre segmente etmenin mümkün olduğunu ve J48 karar ağaçları, Naïve Bayes veya SMO gibi bazı makine öğrenimi algoritmalarının müşteri segmentasyonu için kullanışlı olabileceğini bulmuştur.

Çok Boyutlu Verilere Dayalı Müşteri Segmentasyonu: Perakendecilerin işlem verileri, demografik veriler ve sosyal medya verileri gibi birçok veriye erişimi vardır ve bu veriler müşterileri segmente etmek için kullanılabilir. Dzobo ve diğerleri (2014) tarafından yapılan bir çalışma, çok boyutlu verilere dayalı müşteri segmentasyonu için makine öğrenimi algoritmalarını kullanmıştır [11]. Çalışma, makine öğrenimi algoritmalarını kullanarak müşterileri segmente etmenin, pazarlama kampanyalarının hedeflemesini iyileştirdiğini ve müşteri memnuniyetini artırdığını bulmuştur.

Duygu Analizi Temelli Müşteri Segmentasyonu: Duygu analizi, metin verilerini analiz ederek yazarın duygusunu belirleme sürecidir. Maheswari ve diğerleri (2022) tarafından yapılan bir çalışma, duygu analizi ve makine öğrenimi algoritmalarını kullanarak müşterileri görüşleri ve tercihlerine göre segmente etmek için kullanmıştır [12]. Çalışma, duygu analizi ve makine öğrenimi algoritmalarını kullanarak müşterileri segmente etmenin daha hedefli pazarlama kampanyaları ve artan müşteri etkileşimi sağladığını bulmuştur.

Sonuç olarak, makine öğrenimi, perakendecilerin müşteri segmentasyonu yapmaları ve pazarlama stratejilerini kişiselleştirmeleri için önemli bir araç haline gelmiştir. Akademik çalışmalar, makine öğrenimi algoritmalarını kullanarak müşterileri segmente etmenin satış gelirini artırdığını, pazarlama kampanyalarının hedeflemesini iyileştirdiğini ve müşteri memnuniyetini artırdığını göstermektedir.

Satın Alma Davranışına Dayalı Müşteri Segmentasyonu

Bu bölümde, perakende sektöründe satın alma davranışına dayalı müşteri segmentasyonunda makine öğrenimi uygulamaları tartışılacaktır.

Makine öğrenimi algoritmaları, işlem verilerini analiz etmek ve belirli satın alma modellerini tanımlamak için kullanılabilir. Wang (2022) tarafından yapılan bir çalışma, makine öğrenimi algoritmalarını kullanarak müşterilerin işlem verilerini analiz etti ve belirli satın alma modellerini tanımladı [13]. Çalışma, satın alma modellerini tanımlamak için makine öğrenimi algoritmalarının kullanılmasının müşteri hedeflemesini geliştirdiğini ve satış gelirini artırdığını buldu.

Tahminsel müşteri segmentasyonu, hangi müşterilerin belirli ürünleri veya hizmetleri satın alma olasılığı olduğunu tahmin etmek için makine öğrenimi algoritmalarının kullanılmasını içerir. Chan ve Cooil (2008) tarafından yapılan bir çalışma, makine öğrenimi algoritmalarını kullanarak hangi müşterilerin belirli ürünleri veya hizmetleri satın alma olasılığı olduğunu tahmin etti [14]. Çalışma, müşteri davranışını tahmin etmek için makine öğrenimi algoritmalarının kullanılmasının pazarlama kampanyalarının hedeflemesini geliştirdiğini ve satış gelirini artırdığını, müşteri tepki oranını ise kampanyalara katılımı %64'e kadar artırdığını buldu.

Kişiselleştirilmiş Ürün Tavsiyeleri, müşterilerin geçmiş satın alma geçmişlerine dayanarak ürün tavsiyelerinde bulunmak için makine öğrenimi algoritmalarının kullanılmasını içerir. Sun ve diğerleri (2019) tarafından yapılan bir çalışma, müşteriler için kişiselleştirilmiş ürün tavsiyelerinde bulunmak için makine öğrenimi algoritmalarını kullandı. Çalışma, makine öğrenimi algoritmalarını kullanarak ürün tavsiyelerini kişiselleştirmenin müşteri etkileşimini ve satış gelirini artırdığını buldu.

Müşteri yaşam boyu değer tahmini, bir müşterinin işletmeye yaşamı boyunca getireceği değeri tahmin etmek için makine öğrenimi algoritmalarının kullanılmasını içerir [15]. Maulida ve Dachyar (2022) tarafından yapılan bir çalışma, makine öğrenimi algoritmalarını müşteri yaşam boyu değerini tahmin etmek için kullandı. Çalışma, müşteri yaşam boyu değerini tahmin etmek için makine öğrenimi algoritmalarının kullanılmasının müşteri hedeflemesini geliştirdiğini ve satış gelirini artırdığını buldu.

Sonuç olarak, makine öğrenimi, perakendecilerin satın alma davranışına dayalı müşteri segmentasyonu yapmaları ve pazarlama stratejilerini kişiselleştirmeleri için önemli bir araç haline gelmiştir. Çalışmalar, satın alma modellerini tanımlamak, müşteri davranışını tahmin etmek, ürün tavsiyelerini kişiselleştirmek ve müşteri yaşam boyu değerini tahmin etmek için makine öğrenimi algoritmalarının kullanılmasının müşteri etkileşimini ve satış gelirini artırdığını göstermektedir.

Müşteri Segmentasyonunda Sonluk, Frekans ve Maliyet Uygulaması

RFM (Sonluk, Frekans, Maliyet) analizi, perakende sektöründe müşteri segmentasyonunda yaygın olarak kullanılan bir tekniktir. RFM analizi, müşteri satın alma davranışını üç faktöre dayanarak analiz etmeyi içerir: satın alma sonluluğu, satın alma sıklığı ve satın alma maliyeti. Bu alt bölümde, RFM müşteri segmentasyonunun perakende sektöründeki farklı yönlerdeki uygulamalarını tartışacağız.

RFM analizi, sık satın alan ve yüksek miktarlarda harcama yapan yüksek değerli müşterileri belirlemek için kullanılabilir. Jiale ve Huiying (2010) tarafından yapılan bir çalışma, RFM analizini kullanarak havayolu perakendecisi için yüksek değerli müşterileri belirlemek için kullanıldı. Çalışma, RFM analizini kullanmanın yüksek değerli müşterileri belirlemenin satış gelirini artırdığını ve müşteri sadakatini iyileştirdiğini buldu.

RFM analizi, farklı müşteri segmentleri için pazarlama stratejilerini özelleştirmek için kullanılabilir. Wei ve diğerleri (2020) tarafından yapılan bir çalışma, müşterileri segmente etmek ve pazarlama stratejilerini özelleştirmek için RFM analizini tartıştı. Çalışma, RFM analizini pazarlama stratejilerini özelleştirmenin müşteri etkileşimini ve satış gelirini artırdığını buldu ve ayrıca RFM'nin avantajlarını, dezavantajlarını ve alternatiflerini tartışmaktadır.

RFM analizi, gelecekteki müşteri davranışını tahmin etmek için kullanılabilir. Abbasimehr ve Mostafa (2021) tarafından yapılan bir çalışma, bankacılık satış noktası (POS) örneği için RFM analizini kullanarak müşteri davranışını tahmin etti. Çalışma, RFM analizini müşteri davranışını tahmin etmek için kullanmanın pazarlama kampanyalarının hedeflemesini iyileştirdiğini ve satış gelirini artırdığını buldu. Ayrıca, müşteri davranışında zaman içindeki güncellemeler için zaman serisi analizi ile müşteri segmentasyonunu da gerçekleştirdiler.

RFM analizi, müşterinin bir işletmeden satın alma yapmayı durdurduğu durumu olan müşteri kaybını tahmin etmek için kullanılabilir. Aleksandrova (2018) tarafından yapılan bir çalışma, Bulgaristan'daki KOBİ'ler için RFM analizini müşteri kaybını tahmin etmek için

Problem tanımı ve Bir Çözüm Olarak Kolay.AI

Kolay.ai sadece fatura verilerri (fatura no, müşteri, ürün, tarih ve satış fiyatı) ile herhangi bir veri bilimcisine ya da yapay zekâ uzmanına fazladan maliyet ayrılmasına gerek duymaksızın birçok analiz yöntemi kullanarak müşteri yönetimi, insan kaynakları ve finans yönetimini tek bir çatı altında birleştirerek tüm bu hizmetleri özel ekranlardan sunmaktadır. Bu anlamda Kolay.AI yapay zekanın demoratizasyonu, yani herkesin erişebileceği bir teknoloji olması amacına hizmet etmektedir.

Şekil 1 Örnek Ekran Görüntüsü (Kolay.AI)

Problem Tanımı

Bir firmanın önümüzdeki ay veya önümüzdeki yıl ne kadar cirosu olacağını tahmin etmek, ya da en kıymetli müşterisini, hangi müşterinin kaybedilmek üzere olduğunu, yeni kazanılan müşterilerden kiminle ilişkinin iyiye veya kötüye gittiğini analiz etmek, yapay zeka çalışmalarındaki temel bazı soruları oluşturmaktadır. Benzer şekilde, en değerli ürünün tespiti veya en değerli, örneğin yedinci ürünün tespiti, geçen sene satışlarındaki en yüksek satış hacmine sahip 20 müşteriyi, veya ondan önceki seneki müşterileri analiz etmek gibi çok sayıda problem yapay zeka ile hızlıca çözülebilirken, KOBİ ölçeğinde bir firmanın bu analizlere ulaşması için hazır yazılım çözümleri en iyi alternatif olarak görülmektedir.

Makine Öğrenmesi için Veri Kaynağı

Kolay.AI çalışmaya bir dosya yüklemesi veya entegrasyon ile başlamaktadır. Entegrasyon aracı olarak e-fatura bağlantıları yapılabildiği gibi bir excel veya virgül ile ayrılmış (CSV) dosyası yüklemek gibi yöntemlerle, makine öğrenmesi algoritmalarına temel teşkil edecke olan veri sağlanır. Örnek bir veri kümesinin kolonları şekil 2’de sunulmuştur. Bu kolonlar temel bir fatura verisinde bulunan ve kesilen her faturada gelen bilgilerden oluşmaktadır. Veriler bunlarla sınırlı olmayıp istenildiği kadar ilave veri eklenebilir ve otomatik makine öğrenmesi (AutoML) süreçlerinde bu verilerin tamamı işlenebilir. Sistemin çalışabilmesi için en az 6 kolonun var olması gerekir ve bunlar da belge_no, tarih, müşteri kodu veya adı, stok kodu veya adı, adet ve fiyattır.

Şekil 2 Kolay.AI için örnek bir veri kümesi

BELGE_NO : genelde fiş veya faturaya ait bir numaradır. O faturadaki her satır için tekildir. Örneğin bir faturada 10 farklı ürün satıldıysa 10 kere tekrar eder ve her satırda o belgedeki ürünleri gösterir. Şarttır.

TARIH : Belgenin düzenlendiği tarihtir, her satır için tekrar eder. Şarttır.

STOK_KODU : Varsa SKU belirtir opsiyoneldir.

STOK_ADI : Ürünlerin adını belirtir. Her satıştaki ürünün detaylı ismi bulunur. Şarttır.

NET_TUTAR : satışın net fiyatıdır. Şarttır.

ISKONTO_TUTAR : varsa yapılan iskontoyu gösterir. Opsiyoneldir.

CARI_ADI : satışın yapıldığı müşterinin açık ismidir. Her satışta kime satıldığıdır. Her belge no için tek müşteri olması beklenir ve bu anlamda tekrarlıdır. Şarttır.

CARI_IL : satışın yapıldığı fatura adresinin il bilgisidir. Coğrafi analizler için şarttır, coğrafi analiz istemeyen müşteriler için şart değildir.

CARI_ILCE : satışın yapıldığı fatura adresinin ilçe bilgisidir. Coğrafi analizler için şarttır, coğrafi analiz istemeyen müşteriler için şart değildir.

MIKTAR : bir üründen bir faturada bir müşteriye birden fazla adette satılması durumunda adet bilgisi, tek olması durumunda 1 olarak kaydedilir. Şarttır.

STOK_KOD1_KODU : Özel durumlar için müşteri tarafından belirtilebilecek alandır. Verinin filitrelenmesi gibi ilave kurallar için veride bırakılmıştır. Opsiyoneldir.

STOK_KOD2_KODU : Özel durumlar için müşteri tarafından belirtilebilecek alandır. Verinin filitrelenmesi gibi ilave kurallar için veride bırakılmıştır. Opsiyoneldir.

Makine Öğrenmesi Sonuç ve Analiz Ekranları

Kolay.ai, basit, sade ve hızlı veri sunumu ve sonuca yönelik analitiklerle, sadece fatura verisi gibi basit verileri değere dönüştürmeyi amaçlar. Bu amaca yönelik olarak hazırlanan farklı ekranlar aşağıda açıklanmıştır.

Satış Ekranları

Firmadaki satış grafiğini analiz ederek, geçmiş veri üzerinden gelecek tahmini oluşturur. Şekil 3’teki ekran görüntüsü, Kolay.ai satış ekranından alınmış olup, 2021 Mayıs ayı verisine kadar olan verileri işlemektedir. Bu süreden sonraki 1 yıllık tahmini otomatik olarak yaparak 2022 Mayıs ayına kadar günlük tahminleri sunmaktadır.

<w:p w14:paraId="325E126E" w14:textId="5EA40BB7" w:rsidR="004B7C48" w:rsidRPr="00C56E59" w:rsidRDefault="004B7C48" w:rsidP="004B7C48"><w:pPr><w:pStyle w:val="Caption"/><w:rPr><w:rFonts w:ascii="Linux Libertine O" w:hAnsi="Linux Libertine O" w:cs="Linux Libertine O"/><w:lang w:val="tr-TR" w:eastAsia="ja-JP"/></w:rPr></w:pPr><w:r><w:t xml:space="preserve">Şekil 3-b Örnek Gelir Tahmin Koridoruna Yaklaştırılmış Hali

Şekil 3-b Örnek Gelir Tahmin Koridoruna Yaklaştırılmış Hali

Şekil 3-a Örnek Gelir Tahmin Koridoru

Veri üzerinde, koridor oluşturarak, çıkabileceği maksimum ve inebileceği minimum değerleri de otomatik olarak hesaplamaktadır. Veri üzerinde yakınlaştırma, kaydırma ve hizalama gibi işlemler etkileşimli olarak yapılabilmektedir.

Aynı veri üzerinde yapılan yakınlaştırma işlemi sayesinde (bkz. Şekil 3-b) verinin detayına inilebilmekte ve veri üzerinde sayısal okumalar yapılabilmektedir. Örneğin, gerçek bir firmanın verilerini içeren bu grafikte, haftalık tekrar eden bir örüntü (pattern) yakalanmış olup, satışların hafta sonu, özellikle Cumartesi günleri tepe yaptığı keşfedilmiştir. Benzer şekilde, satışların Pazartesi, Salı, Çarşamba ve Perşembe günleri düşük seyrettiği, Kolay.ai’in otomatik makine öğrenmesi motoru sayesinde keşfedilerek görselleştirilmiştir.

Sezonsallık ve Trend Analizleri

Zaman serisi analiz yöntemleri kullanılarak satış verisi üzerinden makro ölçekte sezonsallık ve trend analizleri yapılabilmekte ve bütün bu analizler tek ekranda sunulabilmektedir.

Şekil 4 Makine Öğrenmesi ile Sezonsallık ve Trend Analizleri

Şekil 4’teki, mavi grafik, sezonsallık analizini yansıtmaktadır. Gerçek bir firmanın verilerini içeren bu çalışmada, aylık bazda sezonsallıklar yakalanmış olup, Kolay.ai tarafından satışların şubat, temmuz ve eylül aylarında tepe yaptığı, ekim, kasım aralık aylarında düşük seyrettiği otomatik olarak tespit edilmiştir. Bu sezonsallık verisinden ayrıştırılmış olan trend analizi ise, tatil dönemleri, okula dönüş dönemleri gibi etkilerden arındırıldıktan sonra, firmanın satışlarının yönünü göstermektedir.

Hem trend, hem de sezonsallıktan arındırılan ETKİ verisi ise, firmanın, promosyon, kampanya, reklam gibi kendi aksiyonları veya korona, politik / ekonomik etkileri göstermektedir. Yani, satışları etkileyen majör olaylar yukarıdaki grafikte tortu/etki olarak işaretlenmiştir ve firmanın bu majör etkileri analiz etme imkanı doğmuştur.

Ürün Analitiği

Ürünlere yönelik olarak yapılan analitiklerle, en kıymetli ürünler, en çok satan ürünler, ürün dağılımı, ürün RFM segmentasyonu, ürün satış segmentasyonu ve aykırı ürünleri tespit etmek mümkündür.

Ürün Segmentasyonu

RFM, turizm, perakende, bankacılık, telekom, finans, üretim gibi çok farklı sektörlerde kullanılan bir analiz ve segmentasyon yöntemidir. Bu yöntemde amaç, ürünler özelinde, en sık ve güncel ürünleri yakalamak; ürünlerin firmaya kattığı maddi değere göre ürünleri en eski ve en az satılan ürün segmentine kadar kategorize etmektir. Bu segmentasyon, ürünler üzerinde doğrudan aksiyon almayı, Kolay.ai’in ilerde anlatılacak olan ürün/kampanya veya ürün/müşteri eşleştirmeleri ile birlikte kullanım imkanı sağlamaktadır.

<w:p w14:paraId="14B1040C" w14:textId="228F33F9" w:rsidR="003D1F89" w:rsidRPr="009B6ABE" w:rsidRDefault="003D1F89" w:rsidP="003D1F89"><w:pPr><w:pStyle w:val="Caption"/><w:rPr><w:rFonts w:ascii="Linux Libertine O" w:hAnsi="Linux Libertine O" w:cs="Linux Libertine O"/><w:lang w:val="tr-TR" w:eastAsia="ja-JP"/></w:rPr></w:pPr><w:r><w:t xml:space="preserve">Şekil 5-b Ürün Analitiği ve RFM Segmentasyonundan Uyumak Üzere olan Ürünler

Şekil 5-b Ürün Analitiği ve RFM Segmentasyonundan Uyumak Üzere olan Ürünler

Şekil 5-a Ürün Analitiği ve RFM Segmentasyonu

Şekil 5’teki Kolay.ai ekranında, ürünlerin bulunduğu segmentler, iki boyutlu uzayda, dikey eksen frekans, yatay eksen ise güncellik olacak şekilde görselleştirilmiştir. Her ürünün sembolize edildiği balonun çapı ise o ürünün sağladığı maddi/para değeri ile ilişkilendirilmiştir. Kolay.ai’in diğer ekranlarında olduğu gibi, bu ekranda da etkileşimli şekilde yakınlaştırma, fare ile gezinme ve detaylı bilgi alma imkanı bulunmaktadır. Örneğin üzerine gelinen balon hakkında detaylı bilginin gösterildiği etkileşimli grafikler (sağda) bulunmaktadır. Yine, ürünlerin renkleri bu ürünlerin dahil olduğu segmenti göstermektedir. Buna göre,

Lacivert segment, kış uykusundaki ürünleri

Turuncu segment, ümit veren ve yükselişteki ürünleri

Yeşil segment, risk altındaki ve düşüşteki ürünleri

Mor segment, Potansiyeli yüksek ve yükselişteki ürünleri

Sarı segment, uyumak üzere olan ürünleri

Mavi segment, dikkat edilmesi gereken ürünleri

Pembe segment ise sadık ve düzenli ürünleri göstermektedir.

Marjinal/Aykırı Ürün Listeleri

Ürün verileri üzerinde çok farklı açılardan zenginleştirme otomatik olarak Kolay.ai motoru tarafından yapılmaktadır. Bu zenginleştirmeler arasında, aşağıdaki veriler sayılabilir:

Ürünün toplam kaç adet satıldığı,

Ürünün birim fiyatı,

Ürünün kaç farklı mağazada satıldığı,

Ürünün kaç farklı müşteri tarafından satın alındığı,

Ürünün günlük , aylık , haftalık ve yıllık ortalama satış miktarları,

Ürünün maksimum sattığı gündeki satış miktarı,

Ürünün geçmişten bugüne ne kadar oranda kampanyalı satıldığı

Yukarıdaki bütün verilerin, sadece fatura verilerinden çıkarıldığını hatırlayın; bunlarla da sınırlı kalmayan veri analizleri neticesinde diğer ürünlere göre farklılaşan ürünler marjinal/aykırı ürün olarak etiketlenerek ayrıştırılır. Bu ayrışan ürünlerin listesi de Kolay.ai ekranlarından sunulmaktadır.

Şekil 6 Anomali Tespit Edilen Ürünler

TOP 20 Ürün Analizi (Adet ve Miktar için)

Ürün satışları adet ve miktar olarak iki grupta incelenebilir. Bir ürünün kaç adet satıldığı adet analizinde, satışların toplam Türk Lirası değeri (hacmi) ise miktar olarak ifade edilmektedir. Satış adet ve miktarlarına bağlı olarak en çok satılan 20 ürünün grafik gösterimi yıllara göre yapılabilmektedir.

Şekil 7 Satışı Yapılan Ürünlerin Hacme Göre Sıralaması

Pareto Etkisi : Ürün Satış Adedi / Ürün Karlılık / Kar Etkisi

Pareto analizi, farklı sektörlerde farklı amaçlarla, karşılaştırmalı etki analizi için kullanılmaktadır. Pareto’nun iddiası, basitçe, olayların öyle bir %20’si vardır ki, sonucun %80’ini etkiler, benzer şekidle olayların öyle bir %80’i vardır ki, sonucun sadece %20’sini etkiler şeklindedir.

Benzer bir Pareto etki analizini otomatik olarak yapan Kolay.ai, bu analizi aşağıdaki şekil 8’de görselleştirmektedir.

Şekil 8 Müşteri Analizinde Pareto Etkisi

Mavi çubuk grafikler, her ürün segmentinde bulunan ürün sayılarını göstermektedir. Görüleceği üzere, 3 numaralı segmentte en az sayıda ürün ve 9 numaralı segmentte en fazla ürün bulunmaktadır. Segment numaraları rasgele atanmış numaralar olup, hangi ürünlerin birlikte bir segment oluşturduğunu anlamak açısından önemlidir. Yine bu ürünlerin, segment atamalarının tam listesine Kolay.ai üzerinden erişmek mümkündür, ve diğer ekranlarda olduğu gibi etkileşimli olarak segment detaylarını görmek mümkündür. Grafikte fare ile yapılan gezinti sayesinde, ürün satış adetlerine bakılabilir ve bu satışların kümülatif olarak yüzde oranı görülebilir (sağdaki grafik açılan kutunun ikinci satırı: bu örnekte 6. Segmente kadar olan segmentlerin toplam satış oranı %19 civarıdır). Benzer şekilde kırmızı çizgi grafiği, toplam hacimi göstermektedir ve yine fare ile yapılan gezinti sayesine açılan kutuda o segmente kadar olan, solundaki segmentlerin toplam satış hacmine etkisi yüzde olarak görülebilir (soldaki grafik: bu örnekte satış hacminin %57 civarını oluşturmaktadır). Bu örnek üzerinde, 6. Segmente kadar olan sırasıyla, 3, 5, 8, 1 ve 6. Segmentler, satış adedi olarak %19’luk bir pay sahibi iken, cironun %57’sini oluşturmaktadırlar. Anlaşılacağı üzere, geri kalan %80’lik satış adedi ise cironun sadece %43’lük payını oluşturmaktadır. Bu analiz sayesinde en karlı segmentler, veya en düşük kara dönüşen segmentler analiz edilebilmektedir.

Benzer bir analitiği, 3 boyutlu etkileşimli olarak yapmak ve ürünleri bulundukları RFM segmenti ve diğer ürünlere göre farklılaştığı özelliklere göre keşfetmek yine Kolay.ai ekranlarında sunulmuştur. Şekil 9’da bu analitiğin RFM segmentasyonu üzerinden görselleştirilmiş hali bulunmaktadır.

Şekil 9 3 Boyutlu Müşteri Analitiği

Müşteri Analitiği

Ürün analitiğine benzer şekilde, fatura bilgilerinden toparlanarak müşteri verileri üzerinden analiz yapılmış, bir müşterinin ziyaret sayısı, ziyaret sıklığı, sepet büyüklüğü, aldığı ürün segmentleri ve ürün karlılıkları gibi çok sayıda analiz sadece fatura bilgisi üzerinden çıkarılarak Kolay.ai ekranlarında sunulmuştur.

Müşteri Değer Segmentasyonu

Müşteri verileri üzerinden çıkarılan sıklık, güncellik ve parasal değer analizleri sonucunda, ürün için yapılan segment çalışmalarına benzer şekilde, aşağıdaki müşteri segment ekranlarını görselleştirmek mümkündür.

Şekil 10 Örnek Müşteri Analitiği Ekranı

Ekranlar etkileşimli olarak filitrelenebilmekte veya yakınlaştırma, gezinme gibi etkileşimli analizler yapılabilmektedir. Örneğin yukarıdaki ekranda, sadece potansiyel sadık müşteriler (potential loyalist) ve uyumak üzere olan (about to sleep) müşteriler filitrelenerek gösterilmiştir. Benzer şekilde, yandaki (sağda) ekranda, grafiğe zoom yapılmış ve bir balonun üzerine gelinerek müşteri numarası, segmenti, güncellik ve frekans bilgileri gibi bilgilere erişilmiştir.

Segment analizi, müşteri tabanlı olarak yapılan ve özünde, müşteriler için aksiyonların belirli olduğu bir analiz türüdür. Bu analizin farklı RFM segmentleri için görselleştirilmesi, literatürdeki haliyle şekil 11’deki gibi yapılabilir:

Şekil 11 RFM Segment İsimleri

Şekilde de görüleceği üzere, farklı segmentlerde bulunan müşteriler için farklı analizler yapılmakta ve buna göre aksiyonlar ön görülmektedir.

Marjinal / Aykırı Müşteriler

Müşteri davranışlarına göre aykırılaşan ve dikkat çekilmesi gereken farklı müşterilerin listesi de Kolay.ai tarafından otomatik olarak sunulmaktadır.

Şekil 12 Marjinal Müşteri Listesi

Aykırı ürün analizine benzer şekilde, sadece fatura verileri üzerinden oldukça zengin bir veri çıkarımını otomatik olarak yapan Kolay.ai, bu veriler üzerinden segmentleri oluşturmakta ve sağdaki şekilde, 3 boyutlu olarak segment analizi ve farklı müşterileri analiz etme imkanı sunmaktadır.

Yıllara Göre Müşteri ve Satış Detayları

Müşterilerin farklı yıllardaki performansını görmek için, yıllık bazda en başarılı satışın yapıldığı 20 müşteri görselleştirilmekte ve karşılaştırmalı olarak sunulabilmektedir (bkz. Şekil 13).

Şekil 13 Yıllara göre en yüksek hacimli müşteriler

Müşteri analitiği ekranında ayrıca müşterilerin gruplanması ve aykırı müşterilerin 3 boyutlu olarak görselleştirilmesi de mümkündür. Bu sayede diğer müşterilerden farklı açılardan ayrışan müşteriler görsel olarak incelenebilmekte ve analiz yapılabilmektedir. Sağda sunulan önrekte farklı açılardan dier müşterilerden ayrışan iki noktaya dikkat edilebilir.

Müşteri Segment Ürün Eşleştirmesi ve Ürün Bulunurluğu

Müşteri segmentasyonu ve ürün segmentasyonunun ayrı ayrı çalışması sonucunda çıkan müşteri ve ürün segmentlerinin eşleştirilmesi ve müşteri segmentleri için farklı ürün analitiklerinin yapılması mümkün olmaktadır.

Şekil 14 Ürün ve Segment Eşleştirmeleri

Her müşteri segmenti için en çok satılan ürünün ve dolayısıyla en çok satılan ürünlerin satıldığı segmentlerin gösterildiği yukarıdaki etkileşimli grafiğin yanında aşağıdaki şekilde tablosal gösterim de Kolay.ai ekranları arasında yer almaktadır.

Şekil 15 Her Segmentte en çok Satan Ürün

Yukarıdaki grafik sayesinde her müşteri segmenti için en çok satan 3 ürün görselleştirilmektedir. Bu sayı parametrik olarak kurulum sırasında değiştirilebilmekte ve farklı sayıda ürün ve segment eşleştirmeleri görselleştirilebilmektedir.

Şekil 16 Son 1 Ay için her Segmentte en çok Satan Ürün

Bütün veri kümesi için çalışan analizleri ayrıca son 1 aylık veri için de çalıştırma mümkün olmakta ve bu sayede son 1 aylık performans ve bütün veri kümesi arasındaki farklar analiz edilebilmektedir.

Müşteri Segmentlerinin Açıklanması

Kolay.ai sayesinde, Müşteri segmentasyonu sırasında kullanılan tekniklerin, veri kaynakları ve süreçte zenginleştirilen veri ile ilişkilendirilerek açıklanır şekilde sunulması da mümkündür.

Şekil 17 Müşteri Segmentlerinin Açıklaması

Yukarıdaki şekil incelendiğinde, her müşteri grubunu etkileyen faktörler bir ağaç şeklinde sunulmuştur. Örneğin veri üzerinde orijinal olarak bulunmayan ve kolay.ai tarafından veri üzerinden çıkarılan ekstra zenginleştirilmiş veri ile sunulan eskilik (bir müşterinin ilk alışveriş yaptığı tarih), yenilik (bir müşterinin son alış veriş yaptığı tarih) veya süre (bir müşterinin ilk alışverişi ile son alışverişi arasındaki geçen süre) gibi verilere ilave olarak müşterinin toplam işlem hacmi gibi veriler birleştirilmiş ve yukarıdaki şekilde açıklanabilir sonuçlar çıkarılmıştır. Bu grafiğin amacı, müşteri analitiğinde, müşteri segmentlerini belirleyen faktörlerin raporlanmasıdır.

Müşteri Serüveni (Customer Journey)

Müşterilerin farklı sebeplerle davranışlarında olan değişiklikler de Kolay.AI tarafından takip edilmekte ve sunulmaktadır. Örneğin aşağıdaki şekilde bir hareket (journey) haritası otomatik olarak çıkarılmaktadır.

Şekil 18 Müşteri Segment Değişimleri

Şekil 18’de, müşterilerin yapmış olduğu segmentler arası yolculuklar analiz edilmekte ve her yolculuk üzerine tıklanarak ayrı ayrı detaylı döküm alınabilmektedir. Örneğin serüven üzerinde (journey) herhangi bir yol veya düğüme tıklandığında o yol üzerinde yolculuk yapan müşteriler ve tıklanan düğümdeki müşteriler detaylı olarak bir tablo ile sunulmakta ve incelenebilmektedir. Tablonun özelliği, ayrıca müşteri arama, müşterilerin detay bilgilerine ulaşmak gibi imkanları da sunmasıdır.

Haritalar ve Coğrafi Satış Analitikleri

Kolay.ai üzerinde, yapılan satışların fatura adresleri kullanılarak coğrafi görselleştirme de yapılabilmektedir.

Şekil 19 Sipariş ve Satış Haritaları

Dosyalar ve Self-Servis Kolay.AI Motoru

<w:p w14:paraId="1FBA8C88" w14:textId="54BA9CD9" w:rsidR="00BA7844" w:rsidRPr="00F671AB" w:rsidRDefault="00BA7844" w:rsidP="00BA7844"><w:pPr><w:pStyle w:val="Caption"/><w:rPr><w:rFonts w:ascii="Linux Libertine O" w:hAnsi="Linux Libertine O" w:cs="Linux Libertine O"/><w:lang w:val="tr-TR" w:eastAsia="ja-JP"/></w:rPr></w:pPr><w:r><w:t xml:space="preserve">Şekil 20 Veri ve Analiz Sonuçlarının Ulaşılabilir olarak Sunulması

Şekil 20 Veri ve Analiz Sonuçlarının Ulaşılabilir olarak Sunulması

Kolay.AI motoru, self-servis olarak SaaS üzerinden (bulutta) kullanıma imkan sunmak üzere tasarlanmıştır. Buna göre bir kurumun, şirketin veya organizasyonun verilerini sürükle bırak ile excel formatında yüklemesi ve motoru uzaktan çalıştırması mümkündür. Dosyalar yüklendikten sonra yapılacak çalıştırma komutu ile veriler işlenmeye başlar ve otomatik olarak motorun sonuçları hem ekranlar hem de excel dosyaları halinde sunulur.

Bu sayde, ekranda görülen bütün veriler detaylı olarak indirilerek excel üzerinde incelenebilmekte veya özel grafikler yine excel veya farklı platformlar ile hazırlanabilmektedir.

Kolay.ai Motoru

Kolay.ai motoru, sorumluluk sahibi yapay zeka felsefesine uygun olarak, açıklanabilir yapay zeka, otomatik makine öğrenmesi ve adaptif, etkileşimli, şeffaf yapay zeka modelleri barındırmaktadır. Uçtan uca, veri ön işleme, zenginleştirme, seçim aşamalarından makine öğrenmesi / istatistiksel modellerin seçimi, kombinlenmesi ve hiper parametre optmizasyonlarına kadar çok sayıda patentli, benzersiz ve yenilikçi yaklaşımı içermektedir.

Uçtan Uca Motorun Akışı

Patentli bir motor olan Kolay.ai motoru, arka planda, geliştirilmesi yıllar alan ve Telekom, bankacılık, parekende, lojistik, sağlık, turizm, finans gibi çok farklı sektörlerde kendisini defalarca ispatlamış olan, OptiScorer, OptiSegment ve OptiMatcher ürünlerini farklı amaçlarla birlikte kullanmaktadır.

Motorun iç akışı, iki ana döngü şeklinde özetlenebilir. Birince kısımda verinin ön işleme için kullanıldığı “ön işleme döngüsü” bulunmaktadır ve farklı veri kaynaklarına bağlanan veri bağlantı katmanı ile süreç başlamaktadır.

Veri bağlantı katmanı kendi içerisinde veri versiyonlama içermektedir. Bu sayede, veride zamanla olan değişimler takip edilebilmektedir. Örneğin bir ürünün birim fiyatındaki değişiklikler, geçmiş verilerin analizi sırasında geçmiş birim fiyatlarla tutmayı gerektirir. Bu sayede firmanın satış hacmi ve ürünün satışı arasındaki ilişkilerin çözümlenmesi ilgili dönem için mümkün olabilmektedir.

Sektörde, eşsiz veri zenginleştirme kapasitesi içeren modülü sayesinde, veri iki farklı açıdan zenginleştirilebilmektedir.

İç zenginleştirme sırasında, veri kaynaklarından okunan veri üzerinden zenginleştirme yapılmaktadır, dış veri zenginleştirme modülleri sayesinde de veriye korona vaka sayısından hava durumuna kadar çok farklı veriler otomatik olarak eklenmektedir (bkz. 2.2. Veri zenginleştirme adımları).

Veri üzerinde yapılan analizlerle, zenginleştirilen ve devasa boyutlara ulaşan veriler üzerinde eleme otomatik olarak yapılmakta, süreç içerisinde eklenen verilerden, gerçekten sonuca etki edenleri bırakılmaktadır. Gerçek bir uygulama sırasında 10 kolonluk fatura bilgisi 1387 kolona kadar zenginleştirilmiştir, bu zenginleştirme ardından veri 23 kolona kadar indirgenmiş ve sadece sonuca etki eden 23 kolon analize dahil edilmiştir.

Ana döngülerden ikincisi olan makine öğrenme döngüsü ise, literatürde bilinen CASH (combined algorithm selection and hyper-parameter-optimization) problemini çözmeyi amaçlamakta ve kombine olarak algoritma seçimi ve hiper parametre optimizasyonu yapmaktadır. Bu otomatik seçilen ve optimize eden algoritmalar, sisteme otomatik olarak yüklenmekte ve veri analizini yerine getirmektedir.

Veri Zenginleştirme Adımları

Kolay.ai motoru, bu aşamada veri üzerinden çok farklı verileri otomatik olarak çıkarmakta ve analiz süreçlerinde kullanmaktadır. Bazı iç zenginleştirme örnekleri aşağıda sıralanmıştır:

Müşteri bazlı veri zenginleştirmeler:

### 1. Müşterinin toplam aldığı ürün sayısı

### 2. Müşterinin ortalama sepet büyüklüğü (adet)

### 3. Müşterinin ortalama sepet büyüklüğü (TL)

### 4. Müşterinin ortalama sepet büyüklüğü (Dolar (o günkü kurdan)) / henüz yazılmadı

### 5. Müşterinin toplam ziyaret sayısı

### 6. Müşterinin ortalama ziyaret periyodu (kaç günde bir geliyor)

### 7. Müşterinin % kaç kampanyalı alım yaptığı (sepet adedi bazlı)

### 8. Müşterinin % kaç kampanyalı alım yaptığı (ziyaret bazlı)

### 9. Müşterinin % kaç kampanyalı alım yaptığı (sepet hacmi bazlı (TL))

### 10. Müşterinin kaç farklı mağazadan alışveriş yaptığı

### 11. Müşterinin bir seferde aldığı maksimum ürün adedi

### 12. Müşterinin bir seferde bir üründen aldığı maksimum adet

### 13. müşterinin ortalama indirim miktarı (TL)

### 14. müşterinin toplam indirim miktarı (TL)

### 15. müşterinin ortalama indirim oranı

### 16. müşterinin yeniliği (en son ne zaman alışveriş yaptığı)

### 17. müşterinin eskiliği (ilk alışverişi ne zaman yaptığı)

### 18. müşterinin süresi (toplam müşterilik süresi)

Ürün bazlı veri zenginleştirmeler:

### 1. ürünün toplam kaç adet sattığı

### 2. ürünün birim fiyatı

### 3. ürünün kaç farklı mağazada bulunduğu

### 4. ürünün kaç farklı müşteri tarafından alındığı

### 5. ürünün günlük ortalama satış miktarı

### 6. ürünün aylık ortalama satış miktarı

### 7. ürünün haftalık ortalama satış miktarı

### 8. ürünün yıllık ortalama satış miktarı

### 9. ürünün maksimum sattığı gündeki satış miktarı (ay, yıl bazlı)

### 10. ürünün haftalık periyotta günlük ortalama satışlarından maksimum sattığı haftanın günü

### 11. ürünün tarihinde ne kadar oranda kampanyalı satıldığı

### 12. ürünün yeniliği (en son üründen ne zaman satış yapıldığı)

### 13. ürünün eskiliği (üründen ilk satışın ne zaman yapıldığı)

### 14. ürünün geçerlilik süresi (ürünün ilk satışı ile son satışı arasında geçen süre)

Dış veri ile yapılan zenginleştirmeler:

### 1. Hava durumu (satışın gerçekleştiği il ve ilçenin satış tarihindeki hava durumu ile zenginleştirilir, bu bilgiler girilmemesi durumunda şirket merkezindeki hava durumu ve şirket merkezi için hava durumu atanmaması durumunda, varsayılan olarak istanbul’un hava durumu alınır).

### 2. Dolar Kuru : Merkez bankası efektif ve resmi kur üzerinden alış ve satış kurları, satışın yapıldığı tarih itibariyle veriye eklenerek veri zenginleştirilir.

### 3. Euro Kuru : Merkez bankası efektif ve resmi kur üzerinden alış ve satış kurları, satışın yapıldığı tarih itibariyle veriye eklenerek veri zenginleştirilir.

### 4. Korona Vaka Sayısı: Açık veri olarak sunulan sağlık bakanlığı ve bağımsız kuruluşlardan alınan, vaka sayısı, ölü sayısı, aşı sayısı verileri zenginleştirmeye dahil edilir. Korona dönemi gibi dönemlerde verinin anlamlandırılması için kullanılır.

### 5. Kripto para borsası: Bitcoin verisi alınarak satış verisinin zenginleştirilmesinde kullanılır.

### 6. Makro Ekonomik Veriler: TEFE, TÜFE, İşsizlik Rakamları, Alım Gücü Endeksi gibi çok sayıda makro ekonomik veri, zenginleştirme amacıyla anlık olarak çekilerek veriye eklenmektedir.

Sorumluluk Sahibi Yapay Zeka

Kolay.AI motoru, yapay zekanın sorumluluk alabildiği (responsible AI) 3. Nesil yaklaşımları kullanmaktadır. Buna göre yapay zeka, otomatik olarak çalışmakta ve otomatik makine öğrenmesi teknolojilerinden (AutoML) faydalanmakta, açıklanabilir sonuçlar çıkarmakta (explainable AI, XAI), kendisini değişimlere adapte edebilmekte (Adaptive AI), Şeffaf olarak modelleri analiz edilebilmekte (transparent AI) ve model sonuçları etkileşimli olarak sunulmaktadır (interactive AI).

Bu amaca yönelik olarak Kolay.AI içerisinde de çok sayıda ekranda, verilen tavsiyeler açıklanmıştır. Örneğin “Müşteri Analitiği Açıklama” ekranı, tamamen açıklanabilir yapay zekanın bir uygulaması olarak sisteme eklenmiş ve segmentlerin sebeplerinin daha net anlaşılmasını sağlamayı amaçlamaktadır.

REFERANSLAR

Reijonen, Helen, and Tommi Laukkanen. "Customer relationship oriented marketing practices in SMEs." Marketing Intelligence & Planning 28.2 (2010): 115-136.

Marisa, Fitri, et al. "Segmentation model of customer lifetime value in small and medium enterprise (SMEs) using K-means clustering and LRFM model." International Journal of Integrated Engineering 11.3 (2019).

Lee, Kyoung Jun, et al. "Extrapolative collaborative filtering recommendation system with Word2Vec for purchased product for SMEs." Sustainability 13.13 (2021): 7156.

Kumar, Biresh, et al. "E-Commerce Website Usability Analysis Using the Association Rule Mining and Machine Learning Algorithm." Mathematics 11.1 (2022): 25.

Chan, Shiau Wei, et al. "Factors influencing the effectiveness of inventory management in manufacturing SMEs." IOP Conference Series: Materials Science and Engineering. Vol. 226. No. 1. IOP Publishing, 2017

Naidoo, Davina. The development of an inventory management tool using machine learning techniques, for an SME in the foodservice industry. Diss. 2021

Truong Du Chau, Xuan, et al. "Towards a Review-Analytics-as-a-Service (RAaaS) Framework for SMEs: A Case Study on Review Fraud Detection and Understanding." Australasian Marketing Journal (2023): 14413582221146004.

Błaszczyński, Jerzy, et al. "Auto loan fraud detection using dominance-based rough set approach versus machine learning methods." Expert Systems with Applications 163 (2021): 113740.

An, Jisun, et al. "Customer segmentation using online platforms: isolating behavioral and demographic segments for persona creation via aggregated user data." Social Network Analysis and Mining 8.1 (2018): 54.

Arasu, B. Senthil, B. Jonath Backia Seelan, and N. Thamaraiselvan. "A machine learning-based approach to enhancing social media marketing." Computers & Electrical Engineering 86 (2020): 106723.

Dzobo, O., et al. "Multi-dimensional customer segmentation model for power system reliability-worth analysis." International Journal of Electrical Power & Energy Systems 62 (2014): 532-539.

Maheswari, T. Latha, et al. "Customer Segmentation Based on Sentimental Analysis." 2022 International Conference on Advanced Computing Technologies and Applications (ICACTA). IEEE, 2022.

Wang, Chenguang. "Efficient customer segmentation in digital marketing using deep learning with swarm intelligence approach." Information Processing & Management 59.6 (2022): 103085.

Cooil, Bruce, Lerzan Aksoy, and Timothy L. Keiningham. "Approaches to customer segmentation." Journal of Relationship Marketing 6.3-4 (2008): 9-39.

Desirena, Gaddiel, et al. "Maximizing customer lifetime value using stacked neural networks: An insurance industry application." 2019 18th IEEE international conference on machine learning and applications (ICMLA). IEEE, 2019.
