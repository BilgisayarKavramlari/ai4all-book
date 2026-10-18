Source: Google Drive 10_74TEW6iMucwGtKHV5AEEEyXzlAMXFh (YBS Ansiklopedi v.3 is.1, Mart 2016; sole author; Turkish), pulled 2026-10-18

Müşteri Kayıp Analizi (Customer Churn Analysis)

Sadi Evren SEKERa

aIstanbul Sehir University, Department of Management Information Systems, Turkey

Özet

Müşteri kayıp analizi, gelir kayıp analizi veya daha genel anlamda kayıp analizi kavramı, özellikle üyelik temelli gelir modeli olan, sigortacılık, Telekom veya bankacılık gibi sektörlerde bir işletmenin hesaplamalarında hayati öneme sahiptir. Mevcut müşteri profillerinin tanınması ve müşteri kayıplarının analiz edilmesinin yanında, müşteri kaybının tahmin edilmesi ve buna bağlı olarak pazarlama ve müşteri ilişkileri yönetimi birimleri ile koordineli çalışılmasının yanında işletmenin finansal hesaplamalarında bir işletmenin piyasa değerine kadar çok farklı boyutlarda işletmenin sürekli gözünün üzerinde olması gereken bir analiz yöntemi olduğu söylenebilir. Bu yazıda genel olarak kavrama giriş yapmanın yanında basit formülleri ve veri madenciliği / iş zekası ile ilişkileri anlatılacaktır.

Anahtar Kavramlar: Müşteri ilişkileri yönetimi, pazarlama, raporlama, iş zekası

Summary

Customer churn analysis, revenue churn analysis or churn analysis in a general view is an essential analysis for most of the subscription based business models, such as insurance, telecom or banking industries. Customer profiling, analyzing the customer churn besides the prediction of customer churn is inter connected with customer relationship management and marketing modules in most of the time. The churn analysis also affects the financial market value of the company so most of the companies keeps an eye on the value monthly or quarterly. This paper will make a brief introduction to the term and present basic formulation and the relation of the concept with data mining and business intelligence.

Keywords: Customer relationship management, marketing, reporting, business intelligence

Giriş

Genellikle Telekom, bankacılık veya sigortacılık sektörlerinde kullanılan ve mevcut müşterilerin kaybını önceden tahmin etmeye dayanan analiz yöntemidir. Bu tahminler sayesinde müşterinin kaybının önüne geçilmesi için müşteri ilişkileri yönetimi (MİY, Customer Relationship Management CRM) kapsamında çözümler üretilebilmektedir. Literatürde, müşteri yıpranması (customer attrition), müşteri sallanması (customer churn), müşteri cayması (customer turnover), müşteri kaçması (customer defection) gibi terimlerle de karşılanmaktadır.

Telekom, bankacılık, sigortacılık gibi müşteri sürekliliği bulunan sektörlerde müşteri kaybı kritik bir öneme sahiptir çünkü çoğu zaman mevcut müşterilerin tutulması, yeni müşteri kazanmaya göre daha düşük maliyetli operasyonlar gerektirir [1]. Ayrıca bu işletmelerin değeri, aktif müşteri sayıları ile doğrudan orantılıdır. Dolayısıyla işletmelerin maliyetleri, karlılığı, büyüklüğü, yatırım kapasitesi, nakit akışı gibi çok sayıda parametre müşteri sayısına ve dolayısıyla müşterilerin sadakatine bağlıdır. Ayrıca yapılan araştırmalar uzun süreli müşterilerin karlılığının daha yüksek olduğunu da göstermiştir. Bu karlılığın anlaşılması için müşteri ömrü (customer lifetime value CLV) hesaplanması gibi yöntemlere başvurulur [2].

Müşteri Kayıp Çeşitleri

Genellikle müşteri kayıp çeşitleri, “gönüllü kayıp (voluntary churn)” ve “gönülsüz kayıp (involuntary churn)” olarak iki farklı başlık altında toplanabilir.

Gönüllü Kayıp (Voluntary Churn)

Gönüllü kayıp, müşterilerin kendi istekleri ile mevcut işletmeden ayrılarak farklı işletmelerin hizmetlerinden yararlanması durumudur. Örneğin bir bankanın müşterisinin hesaplarını farklı bir bankaya taşıması durumunda müşteri kaybı gönüllü olarak yaşanmıştır denilebilir. Bu durum genelde müşterinin kendisi için daha avantajlı olduğuna inandığı şartlarda gerçekleşir.

Gönülsüz Kayıp (Involuntary Churn)

Müşterinin kendi tercihlerinin dışında gelişen ve genelde çevresel şartlardan etkilenen kayıp durumudur. Örneğin müşterinin farklı bir ülkeye taşınması, vefat veya sağlık problemleri gibi sebeplerle ortaya çıkabilir. Genelde müşteri kayıp analizi için geliştirilen araçlar, istatistiksel modeller veya veri madenciliği çalışmaları bu tip gönülsüz kayıpları göz ardı eder. Göz ardı edilmesinin en büyük sebebi genelde müşteri kaybının önlenemez olmasıdır. Çoğu müşteri kayıp analizinin içerisinde gönülsüz kayıp ile ilgili istatistiksel tahminler yer almaktadır ancak bu araçlar genelde oranı bir zaman serisi şeklinde tahmin etmeye yönelirler.

Kayıp Analiz Çeşitleri

Kayıp analizi için çoğu değerlendirme kurumu, bürüt ve net kayıp değerlerini hesaplayarak raporlar. Bürüt kayıp genelde analizin yapıldığı belirli bir zaman aralığı için, kaybedilen müşterinin değer katmakta olduğu bütün hizmetler ve ürünlerden kazanılan değeri göstermektedir. Net kayıp ise benzer özelliklerdeki (aynı segment, alışkanlıklar, aynı pazar ve konumdaki) bir müşterinin sisteme yeniden kazandırılması için yapılması gereken maliyeti analiz eder. Çok sayıda iş zekası (business intelligence) yazılımı işletmelerin tekrarlı aylık gelirini (recurring monthly revenue, RMR veya monthly recurring revenue, MRR) hesaplarken müşteri kayıp analizlerine ihtiyaç duyar. RMR değerleri basitçe her ay için müşterinin güvenli bir şekilde elde edeceği gelir değerini belirtir, dolayısıyla bu değerin hesaplanması sırasında kaybedilmesi muhtemel müşterilerin bulunması esastır.

Çoğu istatistiksel yaklaşım, geçmiş verilere göre bir tahmin modeli geliştirmekte ve bu modele sahadan veri tabanına toplanan değerleri de dahil etmektedir. Örneğin müşteri hizmetlerine gelen şikayetler, teknik destek geri dönüşleri, müşteri memnuniyet anketleri, veya fatura itirazları ve anlaşmazlıkları gibi durumlar tahmin modelleri için önemli veriler içermektedir.

Günümüzde çok daha gelişmiş veri madenciliği modelleri kullanılmaktadır. Örneğin işletmenin stratejik kararlarının müşteri kaybına etkisi, ürün ve servis kalitelerine göre müşteri kayıpları, müşteri profillemesi ve farklı demografik özelliklere göre müşteri kayıpları veya en zayıf müşteri ve etkilerinin anlaşılması gibi çok sayıda analiz günümüzde yapılabilmektedir. Günümüzde toplanan verilere müşterilerin sosyal ağlardan, arama motorlarından veya bloglar gibi farklı internet kaynaklarından toplanan veriler de dahil edilebilmektedir.

Kayıp Analizi Hesaplaması

Kayıp analizi hesaplanması oldukça basit bir formüle dayanmaktadır ve dönemlik kayıp oranı formülü aşağıdaki şekilde verilebilir.

Örneğin bir firmanın ay başındaki müşteri sayısı 5000 ve ay sonundaki müşteri sayısı 4500 ise bu firmanın aylık müşteri kayıp oranı aşağıdaki şekilde hesaplanabilir:

Gelir kaybı (revenue churn) ise benzer şekilde aşağıdaki formül ile hesaplanabilir. Gelir kaybında dikkat edilmesi gereken ilave bir faktör ise mevcut müşterilerin çeşitli sebeplerle gelir artışına sebep olmalarıdır. Örneğin paket yükseltme/alçaltma veya ilave hizmetler gibi sebeplerle müşterilerin sağladığı gelirlerde değişiklikler olabilir. Bu değerlerin de hesaplamaya katılması beklenir.

Örnek olarak bir firmanın yılın ilk çeyreğin başındaki MRR 50.000, ilk çeyreğin sonundaki MRR 45.000 olsun. Ayrıca bu çeyrek boyunca üyeler paket değiştirerek 6.500’lük bir artış sağlamış olsunlar. Bu durumda firmanın dönemlik gelir kaybı aşağıdaki şekilde hesaplanacaktır:

Görüldüğü üzere eksi kayıp aslında kazanç olarak yorumlanmalıdır ve bu firmanın dönem sonunda kazançta olduğu söylenebilir.

Kayıp Tahmini

İşletmeler için önemli değerlerden birisi de kayıpların önceden doğru şekilde tahmin edilebilmesidir. Çoğu iş zekası uygulaması [3], bu amaca yönelik olarak veri madenciliğine dayalı [4] uygulamalar geliştirmektedir. Örneğin veri madenciliği altında çalışılan tahmin yöntemleri (prediction) bu problem tipi için oldukça başarılı sonuçlar vermektedir [5].

Genel olarak bir işletme için kayıp, hem müşteri oranındaki düşüşü hem de müşterilerin işletme için getirilerindeki düşüşü ifade etmektedir. Sektöre göre oranı değişmekle birlikte bütün sektörler için yeni müşteri kazanmanın genelde mevcut müşteriyi elde tutmaya göre daha maliyetli olduğu söylenebilir. Bu yüzden işletmelerin etkili ve verimli şekilde rekabetçi ortamda mücadele verebilmesi için doğru analizleri zamanında yapabilmeleri hayati önem taşımaktadır. Genelde bu analizlerin sonucunda müşteri ilişkileri yönetimi ve pazarlama birimleri ile koordine edilmiş sonuçların, işletmelere büyük katkılar sağladığı görülmektedir. Bu sebeple aşağıdaki üç ana faktörün kayıp tahmininde önemli bir rolü olduğu söylenebilir:

Terk etmeye hazırlanan müşterilerin doğru tanınması için “kimler” ve “nasıl davranırlar” sorularının sorulması.

Bu müşterilerin ayrılması durumunda yapacakları potansiyel etki, bu müşterilerin elde tutulması için alınacak pozisyonun, kaynakları verimli kullanıyor olması ve müşteri profilindeki değeri en iyi şekilde yansıtması

Birey bazında önlemlerin yanında, tahmin edilmesi zor olan ve ayrılma potansiyeli bulunan müşterilerin ayrılmasını engellemek için planların yapılması ve bu iki grup müşteri için alınacak önlemlerin birbiri ile uyumunun kontrol edilmesi (çünkü çoğu zaman birindeki önlem diğerini olumsuz etkilemektedir)

Referanslar

[1] Zero Defections: Quality comes to service., Reichheld & Sasser. Harvard Business review. 1990.

[2] Van Den Poel; Lariviére (2004). "Customer Attrition Analysis For Financial Services Using Proportional Hazard Models". European Journal of Operational Research 157: 196–217. doi:10.1016/s0377-2217(03)00069-9. CiteSeerX: 10.1.1.62.8919.

[3] Sadi Evren SEKER, İş Zekası (Business Intelligence), YBS Ansiklopedi, v. 3, is. 1, March, 2016, pp. 20 - 25

[4] Şadi Evren ŞEKER, İş Zekası ve Veri Madenciliği, İstanbul, Cinius Yayınları, ISBN 978-605-127-671-7, 2013

[5] Seker, S. E. “Weka ile Veri Madenciliği”, draft2digital, Bilgisayar Kavramları Yayınları, İstanbul, 2015, ISBN: 9781524255350
