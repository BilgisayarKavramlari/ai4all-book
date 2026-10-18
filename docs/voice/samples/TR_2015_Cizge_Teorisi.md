Source: Google Drive 1EMUAjDdq6uSU_xwkmxgd2qSJNq76G1ro (YBS Ansiklopedi v.2 is.2, Haziran 2015, pp. 17-41; sole author; Turkish), pulled 2026-10-17

Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015   1
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                         1




                                                      YBS Ansiklopedi
                                                   www.YBSAnsiklopedi.com
                                                     Cilt 2, Sayı 2, Haziran 2015




Çizge Teorisi (Graph Theory)
Sadi Evren SEKER
Istanbul Medeniyet University, Department of Business, Management Information Systems Program


   ÖZET

   Çizge Teorisi çok farklı disiplinlerin çalışma alanına girmektedir. Sosyolojiden, bilgisayar bilimlerine, işletmeden, endüstri
   mühendisliğine kadar çok geniş alanlarda kullanımı olan teori, basitçe bir gerçek hayat probleminin çizge ile
   modellenmesini amaçlamaktadır. Model oluşturulduktan sonra çizge teorisinde bulunan yöntemler kullanılarak problem
   çözülebilmekte ve ardından da tekrar gerçek hayata uygulanabilmektedir. Bu yazı kapsamında, çizge teorisinin genel
   kavramlarına giriş yapılarak terminoloji hakkında bilgi verilecek ve bazı problemlerin nasıl çözüldüğü gösterilecektir.
   Yazının başlangıç kısmında temel terminolojiye yer verilmişken ilerleyen kısımlarında Öyler yolu, Hamilton yolu, Prüfer
   dizilimi, Ağaçlar ve özel olarak ikili ve ikili arama ağaçları, yığıtlar, asgari tarama ağacı ve çözümü için Kruskal ve Prims
   algoritmalarına yer verilmiştir.




Çizge teorisi (graph theory) literatürde çok farklı disiplinlerin
çalışma alanına girmektedir. Sosyolojiden matematiğe,
işletmeden bilgisayar bilimlerine (Seker, 2015) (Arslan &
Seker, 2014) kadar farklı alanlarda kullanılmaktadır (Seker,
Altun, Ayan, & Mert, 2014). Örneğin bilgisayar bilimlerinin
altında ayrık matematik (discrete math) veya endüstri
mühendisliği altında yön eylem çalışmaları (operations
research) veya matematiğin bir çalışma alanı olarak
karşılaşılabilir (SEKER, 2015). Çizge teorisi temel olarak bir
problemin kenar (edge) ve düğümler (node) ile modellenmesi
ve bu modelin bir çizge şeklinde gösterilmesi ilkesine
dayanmaktadır. Çizge teorisinde tanımlı olan bazı özellikler
bu modelin çözümüne ve dolayısıyla gerçek problemin                   Örneğin yukarıdaki çizgede 4 düğümden ve 4 kenardan
çözümüne yardımcı olmaktadırlar. Yani çizge teorisinin işe           oluşan bir çizge gösterilmektedir. Bu çizgeyi
yaraması için öncelikle gerçek dünyadan bir problem çizge                     G= ({A,B,C,D} , {(A,B),(A,C),(C,D),(A,D)})
olarak modellenir, bu model çözülür ve daha sonra gerçek             şeklinde ifade etmek mümkündür.
dünyaya uygulanır.                                                   Yol (Path)
Çizge teoremindeki herhangi bir işlemden önce, çizgenin              Bir çizge üzerinde bir veya daha fazla düğümden ve kenardan
tanımı yapılmalıdır ve bu tanım aşağıdaki şekildedir:                geçen rotaya verilen isimdir (Gibbons, 1985) . Örneğin
                           G= (V,E)                                  aşağıdaki çizge üzerinde bir yol gösterilmiştir.
Yukarıdaki bu tanım herhangi bir çizgenin (graph) düğümler
(vertices) ve kenarlar (edges) kümesi olduğunu ifade
etmektedir. Çoğu kaynakta bu ifade sıralı olarak kabul edilir
yani öncelikle düğümler ardından da kenarlar gösterilmektedir
(Biggs, Lloyd, & Wilson, 1986).
Çizgeleri, kenarların} yönlü olup olmamasına göre, yönlü
çizgeler (directed graphs) ve yönsüz çizgeler (undirected
graph) olarak ikiye ayırmak mümkündür. Ayrıca kenarların
değer almasına göre değerli çizgeler (weighted graphs) veya
değersiz çizgeler (unweighted graphs) isimleri verilebilir.
                                                                     Yolların yazılışı ise geçtikleri düğümlerin sırasıyla yazılması
                                                                     ile elde edilir. Örneğin yukarıdaki yolu {A,C,D} olarak
                                                                     göstermek mümkündür.
                                                                                                                               2
Döngü (Cycle)
Çizge teorisinde bir düğümden başlayıp aynı düğümde biten
yola (path) döngü adı verilir
Örneğin yukarıdaki şekil 2’deki A düğümünden başlayarak
yine bu düğümde biten {A,C,D} yoluna döngü denilebilir.
Bir çizgenin içerisinde döngü bulunup bulunmadığının
anlaşılması (cycle detection) problemi, literatürdeki önemli
problemlerden birisidir ve yönsüz bir çizgedeki döngünün
bulunma karmaşıklığı O(n) olacaktır (Sedgewick, 1983).
Güçlü Bağlı veya Tam Bağlı Çizgeler (Strongly Connected
Graphs)
Bir çizgede bulunan bütün düğümleri diğer bütün düğümlere
bağlayan birer kenar bulunuyorsa bu çizgeye güçlü bağlı
çizge adı verilir. Döngü bulunma problemine benzer şekilde
bir çizgenin güçlü bağlı çizge olup olmadığının anlaşılması
veya bir alt çizgenin (çizgenin alt kümesi veya alt parçası        Yukarıdaki şekil için tanımımıza uygun bir yol (path) elde
olarak düşünülebilecek olan kısmı) içerisinde güçlü bağlı          etmek istersek:
çizge olup olmadığının anlaşılması da önemli problemler
arasında sayılabilir. Literatürde güçlü bağlı alt çizgelere özel
olarak klik (clique) ismi verilir ve bu terim aynı zamanda
sosyoloji gibi beşeri çalışma alanlarında bir toplulukta çok
yakın olan arkadaş grubunu da ifade eder (örneğin bir okul
veya bir iş yerindeki yakın arkadaş grubu). Bu tanım çizgenin
her üyesinin (her düğüm) diğer üyeleri ile doğrudan ilişkide
olduğu alt çizgeyi ifade etmektedir. Örneğin Kosaraju
Algoritması, Tarjan Algoritması veya Dijkstra’nın güçlü bağlı
çizge algoritması gibi çeşitli algoritmalar, bu amaçla bir
çizgenin güçlü bağlı olup olmadığını bulmak için
kullanılabilir (Cormen, Leiserson, Rivest, & Stei, 2001).
K-Düzenli Çizge (K-Regular Graph)
Bir çizge üzerindeki her düğümün “k” kadar komşusu
bulunması durumuna k-düzenli çizge denilir (Chen). Örneğin         Yukarıdaki şekilde kırmızı olarak gösterilen yol bir
aşağıdaki çizge 2-düzenli bir çizgedir çünkü her düğümün           Hamiltonian yoludur. Ancak bu şekilde çıkarılabilecek tek yol
derecesi 2’dir.                                                    yukarıdaki yol değildir.




Hamilton Yolu (Hamiltonian Path, Hamilton Circuit)
Bir yolun (path) Hamilton yolu olabilmesi için bir kere
geçilen kenardan (edge) tekrar geçilmemesi gerekir ve ayrıca
yolun bütün düğümleri (nodes) birer kere ziyaret etmesi
gerekir.                                                           Yukarıdaki bu yeni yol da tanıma uygun bir yoldur ve ilk
Bir Hamilton yolu başladığı yerde bitiyorsa yani tam bir           çıkan yoldan farklıdır. Görüldüğü üzere bir çizgede tek bir
döngü (cycle) tamamlıyorsa (yoldaki son düğümden ilk               Hamilton yolu bulunmak zorunda değildir.
düğüme gidilmesi mümkünse) bu yollara Hamilton döngüsü             Hamilton yollarının özellikleri
(hamiltonian cycle) ismi de verilebilir (Garey & Johnson,          Herhangi bir hamilton döngüsü (hamiltonian cycle) tek bir
1979).                                                             kenarın (edge) çıkarılmasıyla bir hamilton yoluna
Hamiltonian yolları yönsüz çizgelerde (undirected graph)           (hamiltonian path) dönüştürülebilir.
tanımlıdır ancak hamilton yollarının benzerleri yönlü çizgeler     2 den fazla düğüme (node) sahip ve tam bağlı (strongly
(directed graphs) için de uyarlanabilir.                           connected) turnuva çizimleri birer hamilton yoludur
Bir çizgedeki, hamilton yollarının bulunması işlemi NP-            (hamiltonian path)
Complete bir işlemdir.                                             Tam bağlı graflar (strongly connected graphs) için birbirinden
Örnek                                                              farlı hamilton yollarının (hamiltonian path) sayısı (n-1)!/2
Örneğin aşağıdaki çizgeyi (graph) ele alalım:                      tanedir.
                                                                   Hamiltonian yollarının kullanım alanları
                                                                   Seyyar satıcı problemi (travelling salesman problem) gibi pek
                                                                   çok çizge teorisi problemin çözümünde kullanılabilirler.
                                                                   Sıfır bilgi ispatı (zero-knowledge proof) gibi veri güvenliği
                                                                   (cryptography) problemlerinde kullanılabilirler.
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                     3
Çizge Teorisinin Çıkışı ve Öyler Teorisi                           Yukarıdaki tanımı yönlü graflar (directed graphs) için de
Öylerin teorisini ortaya atmasında önemli rol oynayan tarihi       yapmak mümkündür. Ancak bu durumda yukarıdaki tanımda
problem Königsberg köprüsü problemidir.                            geçen yolları, yönlü yollar ve döngüleri, yönlü döngüler
                                                                   olarak değiştirmek gerekir.
                                                                   Öyler yolunun özellikleri
                                                                    • Bir yönsüz bağlı çizgenin bütün düğümlerinin derecesi
                                                                         çiftse bu çizge öyler çizgesidir (eulerian) [ancak ve
                                                                         ancak]
                                                                    • Bir yönlü çizge (directed graf) ancak ve ancak bütün
                                                                         düğümlerin giren ve çıkan derecelerinin toplamları eşitse
                                                                         öyler çizgesi (eulerian) olabilir.
                                                                    • Bir yönsüz çizgenin öyler yolu bulunabilmesi için iki
                                                                         veya sıfır sayıda tek düğüm derecesine sahip üyesi
                                                                         olmalıdır.
Yukarıdaki şekilde Pregel Nehri etrafında kurulu (C ve B           Öyler Döngülerinin sayısı
karaları) ve nehrin ortasında iki adası olan (A ve D adacıkları)   Bir çizgede öyler döngüleri birden fazla olabilir. Yani
Kösigner şehrinin yukarıda görülen 7 köprüsü bulunmaktadır.        birbirinden farklı döngüler elde edilebilir. Burada fark
Problem bütün köprülerden bir kere geçilen bir yol olup            oluşturan faktör başlangıç ve bitiş düğümleridir.
olmayacağıdır.
Öyler bu soruyla uğraşırken öyler yolu teorisini bulmuştur ve
cevap olarak böyle bir yolun bulunamayacağını ispatlamıştır.
Öylerin iddiası basit bir keşfe dayanmaktaydı. Şayet bir
düğüme (node) bir kenar (edge) ile geliniyorsa bu düğümü
terk etmek için farklı bir yola ihtiyaç duyulur.
Bu durumda her düğümün derecesini (node order) hesaplayan
Öyler, bir düğüme giren çıkan yolların sayısına düğüm
derecesi (node order) ismini verdi.
Buna göre şayet bir düğümün derecesi tekse, bu düğüm ya
başlangıç ya da bitiş düğümü olmalıdır. Bunun dışındaki
durumlarda (yol (path) üzerindeki herhangi bir düğüm olması
durumunda) tek sayıdaki yolun sonuncusu ziyaret edilmiş
olamaz.
                                                                   Örneğin yukarıdaki şekil için, A-B-E-A-C-D-A döngüsü bir
                                                                   öyler döngüsüdür. Benzer şekilde
                                                                   E-B-A-C-D-A-E döngüsü de bir öyler döngüsüdür.
                                                                   BEST Teoremi
                                                                   Buradaki soru acaba bir çizgede kaç farklı öyler döngüsü
                                                                   olabilir?
                                                                   Bu soruya cevap BEST teoremi ismi verilen ve teoremi bulan
                                                                   kişilerin isimlerinin baş harflerinden oluşsan teorem ile
                                                                   verilir. BEST teoremine göre bir çizgede bulunan öyler
                                                                   döngülerinin sayısı çizgedeki bütün düğümlerin derecelerinin
                                                                   bire eksiğinin faktöriyellerinin çarpımına eşittir (Tutte &
Yukarıdaki şekilde köprü örneğinin çizge ile gösterilmiş hali      Smith, 1941).
görülüyor. Burada dikkat edilirse her dört düğüm de tek                                      ∏ ( d(v)-1) !
sayıda dereceye sahiptir.                                          olarak gösterilebilecek teoriye göre d() verilen düğümün
A5                                                                 (vertex) derecesi ve v ise çizgedeki bütün düğümlerdir.
B C D ise 3                                                        Örneğin yukarıdaki çizge için bu değeri hesaplayacak olursak
derecesine sahiptir. Bu durumda düğümlerden iki tanesi             önce düğümlerin derecelerini çıkarmamız gerekir:
başlangıç ve bitiş olsa diğer iki tanesini birleştiren yollar      A4
kullanılamayacak ve bütün kenarlar gezilmiş olamayacaktır.         B2
Öyler yolunun Tanımı                                               C2
Öyler yolu (eulerian path) tam olarak şu şekilde                   D2
tanımlanabilir:                                                    E2
Bir yönsüz çizgede (undirected graph) şayet bütün düğümleri        Şimdi bu değerlerin birer eksiklerinin faktöriyellerini
(nodes) dolaşan bir yol bulunabiliyorsa bu yola Öyler yolu         çarpalım
(Eulerian Path, Eulerian Trail, Eulerian Walk) ismi verilir. Bu    3! = 6
yolun bulunduğu çizgeye ise yarı öyler (semi-eulerian) veya        1! = 1
dolaşılabilir (traversable) çizge ismi verilir.                    1! = 1
Şayet bu yolun başlangıç ve bitiş düğümleri (node) aynıysa bu      1! = 1
durumda tam bir döngü (cycle) elde edilebiliyor demektir ve        1! = 1
bulunan bu yola öyler döngüsü (eulerian cycle, eulerian            sonuç olarak 6x1x1x1x1 = 6 farklı öyler döngüsü bulunabilir
circuit veya eulerian tour) ismi verilir (Mallows & Sloane,        diyebiliriz.
1975). Bu yolu içeren çizge ise öyler çizgesi (eulerian graph      Yönlü Düz Ağaçlar (Directed Acyclic Graphs)
veya unicursal) ismi verilir.                                      Bilgisayar bilimlerinde veri modellemede kullanılan Düz
                                                                                                                              4
ağaçların (acyclic graph), yani içinde herhangi bir döngü
(daire) bulunmayan ağaçların, yani bir noktadan birden fazla
geçme imkanı bulunmayan ağaçların, yön almış halleridir.
Yani her kol (edge) bir yön göstermektedir ve gösterilen
yönde ilerlemek mümkün iken tersi yönde ilerlemek mümkün
değildir.




Yukarıdaki bu tanım aslında bir ağaç (tree) tanımının
aynısıdır. Bu yüzden temel bir ağaç aslında bir yönlü düz ağaç
olarak nitelendirilir.
Yukarıdaki ağaç tasvirinde 7 düğümden (node) oluşan ve
yapraklarında (leaf) 4 düğüm bulunan bir ağaç gösterilmiştir.
Bu ağacın derinliği (depth) 2 dir ve her seviyenin (level)
değeri yanında verilmiştir. Ağaçların 1 tane başlangıç düğümü    Yukarıdaki bu ağacın ilk örnekten farkı dengesiz olması ve
bulunur ve bu başlangıç düğümüne kök (root) denilir.             özel olarak her düğümün çocuk sayısının 1 olmasıdır. Tanım
Özel olarak yukarıdaki ağacın her düğümünden sadece ikişer       hatırlanacak olursa yukarıdaki bu ağaç da bir ikili ağaç olarak
alt düğüme bağlantı bulunduğu için bu ağaca ikili ağaç           kabul edilebilir.
(binary tree) adı da verilebilir.                                İkili Arama Ağacı (Binary Search Tree)
İkili Ağaçlar (Binary Tree)                                      İkili ağaçların (Binary Tree) özel bir hali olan ikili arama
Ağaçların özel bir hali olan ikili ağaçlarda her düğümün         ağaçlarında, düğümlerde duran bilgilerin birbirine göre
çocuklarının sayısı azami 2 olabilir. Bir düğümün daha az        küçüklük büyüklük ilişkisi bulunmalıdır. Örneğin tam
çocuğu bulunması durumunda ( 0 veya 1) ağacın yapısı             sayılardan (integer) oluşan veriler tutulacaksa bu verilerin
bozulmaz. Yapraklar hariç bütün düğümlerin ikişer çocuğu         aralarında küçük-büyük ilişkisi bulunmaktadır.
bulunması ve yaprakların aynı derinlikte bulunması               İkili arama ağacı, her düğümün solundaki koldan
durumunda bu ağaca dengeli ağaç (balanced tree) denilir.         ulaşılabilecek bütün verilerin düğümün değerinden küçük, sağ
Aşağıda bir dengeli ikili ağaç örneği tasvir edilmiştir:         kolundan ulaşılabilecek verilerin değerinin o düğümün
                                                                 değerinden büyük olmasını şart koşar.




Bu ağacı değişik sıralarda yeniden oluşturabiliriz. Örneğin      Örneğin yukarıda bir ikili arama ağacı tasvir edilmiştir. Bu
aşağıdaki ağaç da yukarıdaki verilerin aynılarını taşıyan bir    ağaçta dikkat edilecek olursa kökün solunda bulunan bütün
ikili ağaç örneğidir.                                            sayılar kökten küçük ve sağında bulunan bütün sayılar kökten
                                                                 büyüktür.
                                                                 İkili arama ağacına bu kurala uygun olarak ekleme çıkarma
                                                                 veya silme işlemleri yapılabilir. Ancak yapılan her işlemden
                                                                 sonra ikili arama ağacının yapısı bozulmamış olmalıdır.
                                                                 İkili arama ağacında arama işlemi:
                                                                 Yukarıda da anlatıldığı üzere ağacın üzerinde duran verilerin
                                                                 özel bir şekilde sıralı bulunması gerekir. Buna göre herhangi
                                                                 bir değeri arayan kişi ağacın kök değerine bakarak aşağıdaki 3
                                                                 eylemden birisini yapar:
                                                                 Aranan sayı kökteki değere eşittir -> Aranan değer
                                                                 bulunmuştur
                                                                 Aranan sayı kökteki değerden küçüktür -> Kökün sol kolu
                                                                 takip edilir
                                                                 Aranan sayı kökteki deüerden büyüktür -> Kökün sağ kolu
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                      5
takip edilir
İkili arama ağaçlarının önemli bir özelliği ise öz
çağıran(recursive) oluşudur. Buna göre bir ağacın sol kolu
veya sağ kolu da birer ağaçtır. Bu özellikten faydalanarak
örneğin C dilinde aşağıdaki şekilde bir arama fonksiyonu
yazılabilir:
dugum * ara(dugum *kok, int deger){
         if(deger == kok->veri){
             return kok;
       }
       else if(deger > kok->veri ){
             return ara(kok->sag, deger);
       }
       else{
             return ara(kok->sol,deger);
     }                                                             Yukarıdaki ikili ağaçta dikkat edilirse ağaç dengeli bir şekilde
}
                                                                   sırayla doldurulmuştur. Buna göre yeni bir eleman daha
Yukarıdaki bu örnekte daha önce ikili ağaçlar konusunda
                                                                   eklenmesi durumunda ağacın eleman sayısı 7’ye yükselecek
tanımlanmış bir düğüm struct’ı kullanılmıştır. Koda dikkat
                                                                   ve sayıların yeri değişmekle birlikte yeni eleman şu andaki 18
edilecek olursa özçağıran bir yapı görülebilir. Yani
                                                                   sayısını içeren düğümün sağına gelecektir.
fonksiyonun içerisinde kendisi çağrılmış ve yeni kök değeri
                                                                   Ayrıca herhangi bir ağacı yığın ağacına çevirmek
olarak mevcut kökün sol veya sağ değeri verilmiştir. Arana         (yığınlamak, heapify) de mümkündür ve bu işlem bir yığın
değer her durumda değişmediği için alt düğümlere kadar aynı        ağacı oluşturma işleminin temelini oluşturur. Basitçe yığın
olarak indirilmiştir.                                              ağacına yapılan her ekleme ve her çıkarma işleminden sonra
Yukarıdaki koddaki önemli bir eksiklik ise kodun ağaç
                                                                   bu yığınlama (heapify) işlemi yapılarak yığın ağacının
üzerinde bir sayıyı bulamaması durumunun tasarlanmamış
                                                                   formunu koruması sağlanmalıdır.
olmasıdır. Bu durumda basitçe NULL değer kontrolü ile
                                                                   Yığın Sıralaması (Heap Sort)
aşılabilir. Buna göre sol veya sağa gitmeden önce sol veya
                                                                   Verinin hafızada sıralı tutulması için geliştirilen sıralama
sağda bir değer olduğuna bakılmalı şayet değer varsa
                                                                   algoritmalarından (sorting algorithms) bir tanesidir.
gidilmelidir. Şayet değer yoksa ağaçta bu sayının bulunma
                                                                   Yığınlama sıralaması, arka planda bir yığın ağacı(heap)
ihtimali yoktur ve bu sayının olmadığını belirten bir ifade        oluşturur ve bu ağacın en üstündeki sayıyı alarak sıralama
(örneğin NULL) döndürülmelidir. Kodun bu şekilde tashih            işlemi yapar. (Lütfen yığın ağacındaki en büyük sayının her
edilmiş hali aşağıda verilmiştir:                                  zaman en üstte duracağını hatırlayınız. )
dugum * ara(dugum *kok, int deger){
                                                                   Sıralanmak istenen verimiz:
         if(deger == kok->veri){
                                                                   5,12,20,18,4,3
             return kok;
       }                                                           olsun. Bu verilerin bir oluşumun(composition) belirleyici
       else if(deger > kok->veri ){                                alanları olduğunu düşünebiliriz. Yani örneğin vatandaşlık
          if(kok->sag != NULL)                                     numarası veya öğrenci numarası gibi. Dolayısıyla örneğin
                      return ara(kok->sag, deger);                 öğrencilerin numaralarına göre sıralanması durumunda
          else                                                     kullanılabilir.
                   return NULL;                                    Yukarıdaki bu sayılardan bir yığın ağacı oluşturulduğunda
       }                                                           aşağıdaki şekilde bir sonuç elde edilir:
       else{
          if(kok->sag != NULL)
                       return ara(kok->sol,deger);
          else
                   return NULL
     }
}
Yığın Ağacı (Heap Tree)
Yığın ağacı bilgisayar bilimlerinde özellikle sıralama
amacıyla çokça kullanılan bir veri yapısıdır. Bu veri yapısı üst
düğümün (atasının) alt düğümlerden (çocuklarından) her
zaman büyük olduğu bir ikili ağaç (binary tree) şeklinde
düşünülebilir.
Aşağıda örnek bir yığın ağacı verilmiştir:                         Bu ağacın en büyük değeri en üstte (kökte) durmaktadır
                                                                   öyleyse bu değer alınarak sonuç dizisinin son elemanı
                                                                   yapılırsa ve sonra geriye kalan sayılar tekrar yığınlanırsa
                                                                   (heapify) ve bu işlem eleman kalmayana kadar tekrarlanırsa
                                                                   sonuç dizisindeki veriler sıralanmış olarak elde edilir. Bu
                                                                   işlemler adım adım aşağıda gösterilmiştir:
                                                                   Sonuç dizisi : {20}
                                                                                                                                   6




20 sayısı yığın ağacından silindikten sonra kalan sayılar           şekildeki çizge toplam 11 düğüm (node) bulunmaktadır ve
yığınlandıktan sonra yukarıdaki ağaç elde edilir. Bu ağacın en      şekilde çizge yönsüz çizgedir (undirected graph) aynı
üstündeki sayı alınırsa sonuç dizisi : {20,18} olarak bulunur       zamanda da döngü (cycle) bulundurmaz.
ve 18 alındıktan sonra kalan sayılar yığınlandığında ise            Bu durumda yukarıdaki şekli prüfer dizilimi olarak göstermek
aşağıdaki ağaç elde edilir.                                         mümkündür.
                                                                    Algoritmamız son iki düğüm kalana kadar çalışır. Bu
                                                                    durumda önce yapraklardan başlanarak işlem yapıyoruz.
                                                                    Yukarıdaki çizgeyi yapraklardan köke doğru artan sayılar ile
                                                                    bu yüzden numaralandırdık.
                                                                    Sırasıyla her düğümün bağlı olduğu diğer üst düğümü
                                                                    yazıyoruz.
                                                                    Bu durumda aşağıdaki düğümler yapraklardır ve bağlı
                                                                    oldukları üst düğümler yanlarında verilmiştir:
                                                                    1 à 6
                                                                    2 à 4
                                                                    3 à 5
Bu ağacında en üstünde bulunan sayı 12’dir ve bu sayı sonuç         Yukarıdaki yapraklardan başlayarak bu dizilimi not ediyoruz.
dizisine eklenir. Sonuç dizisi : {20,18,12} olarak bulunur ve       Yani şimdilik prüfer dizilimimizde 645 bulunuyor. İkinci
kalan sayılar bir kere daha yığınlanır:                             adımda bu yaprakları çizgeden (graph) kaldırıyoruz.




Sonuçta kalan sayıların yığınlanmasıyla yukarıdaki ağaç elde
edilir ve bir kere daha en üstteki sayı alınarak sonuç dizisi :
{20,18,12,5} olarak bulunur.                                        Şeklin yeni halindeki yaprakları not edeceğiz ancak son iki
                                                                    düğüm kalınca duracağımız için yeni şekilden sadece bir
                                                                    düğümü alıyoruz. Bu düğümde numara sırasına göre
                                                                    (tamamen tesadüfen) 4 oluyor
                                                                    4 à 5
                                                                    şeklinde son sayımızı da not ettikten sonra prüfer
                                                                    dizilimimizdeki sayılar 6455 olarak kaydedilmiş oluyor.
Aynı işlem kalan sayılara tekrar tekrar uygulanarak                 Artık iddia edebiliriz ki 6455 sayı serisinden (sequence) 6 ve
{20,18,12,5,4,3} sayıları elde edilir. Dikkat edilirse bu sayılar   5 düğümlerini bilerek yukarıdaki çizge (graph) geri
ilk başta verilen sayıların sıralanmış halidir. Şayet sıralama      çizebiliriz.
işlemi küçükten büyüğe yapılsın isteniyorsa bu durumda              Bu iddianın tatbiki oldukça basittir. 6 ve 5’ten oluşan bir çizge
sayılar dizinin başından değil sonundan yazılarak                   çizilir ve ardından prüfer dizilimi tersten okunarak sırasıyla
kaydedilebilir veya çıkan sonuç tersten sıralanabilir.              yeni düğümler (nodes) çizgeye eklenir.
Prüfer Dizilmi (Prüfer Sequence)                                    İki Parçalı Çizgeler (Bipartite Graphs)
Ağaç (tree) yapısındaki graflar için yani dairesel olmayan          Bir çizgeyi oluşturan düğümleri iki farklı kümeye
çizgeler (acyclic graphs) için kullanılabilir. Daha basit bir       ayırabiliyorsak ve bu iki kümenin elemanlarından küme
ifade ile çizgenin (graph) yaprakları (leaf) bulunmalıdır.          içerisindeki bir elemana gidilmiyorsa. Yani bütün kenarlar
Prüfer diziliminin altında yatan sorun bir ağacın bir sayı dizisi   (edges) kümeler arasındaki elemanlar arasındaysa, bu çizgeye
ile nasıl gösterileceğidir. Yani bir çizgede birbirine bağlı        iki parçalı çizge (bipartite graph) ismi verilir.
düğümler (nodes) olduğunu ve bu çizge yapısını bir şekilde          İki parçalı çizgelere örnekler
sayılarla göstermek (veya dizi (array) ) istediğimizi               Örneğin aşağıdaki şekilde gösterilen çizgeyi iki parçalı olup
düşünelim.                                                          olamayacağını incelemeye çalışalım:
Örneğin aşağıdaki çizgeyi (graph) ele alalım:
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                    7




Yukarıda örnek olarak verilen çizgenin düğümlerini                Yukarıdaki şekilde görüldüğü üzere komşu olmayan
koşulumuzu sağlayacak şekilde yani iki ayrı küme oluşturacak      düğümler renklendirilmiştir. Yani komşu iki düğüm aynı
ve bu kümelerin içerisinde yol bulunmayacak şekilde               renkle renklendirilmemiştir. Daha farklı bir deyimle bir
yerleştirmeye çalışalım.                                          düğümün komşuluk listesindeki (adjacency list) bütün
                                                                  düğümler aynı renkte boyanmıştır. Sonuçta aynı renkte
                                                                  boyanan iki komşu oluşmamaktadır.
                                                                  Aşağıdaki iki parçalı olmayan çizgeye de aynı şekilde
                                                                  yaklaşırsak problem ortaya çıkacaktır.




                                                                  Yukarıdaki şekil bipartite tree (iki parçalı ağaç) değildir.
                                                                  Çünkü şekildeki D ve G aynı renktedir. Bu düğümlerden
                                                                  birisinin rengi değiştirildiğinde bu sefer de H ile aynı renkte
                                                                  olacaktır. Dolayısıyla hiçbir şekilde iki grup elde edilemez.
                                                                  Farklı bir ifadeyle:




Yukarıdaki şekilde, ilk şekilden farklı olarak sadece
düğümlerin (nodes) yerleri değiştirilmiştir. Yukarıdaki şekilde
ayrıca iki ayrı küme oluşturulmuş ve ilk küme ile ikinci küme
arasında bölünen düğümlerin tamamında kenarlar karşı
kümeye işaret etmiştir. Yani aynı küme içerisinde hiçbir kenar
bulunmamaktadır.
Bu durumu aşağıdaki şekilde de gösterebilirdik:




                                                                  Çizgeyi yukarıdaki şekilde iki gruba bölmek istersek
                                                                  görüldüğü üzere aynı gruptaki iki düğüm arasında bir kenar
                                                                  bulunmakta bu durumda da iki parçalı ağaç olamamaktadır.
                                                                  İki parçalı çizgenin test edilmesi
                                                                  Bir çizgenin iki parçalı olup olmadığını (bipartite) test etmek
                                                                  için ne yazık ki yukarıda gösterildiği gibi çizgedeki bütün
                                                                  düğümlerin yerlerinin değiştirilmesi, iki kümede toplanması
                                                                  ve sonunda da aralarında bir kenar olup olmadığına bakılması
                                                                                                                                  8
mümkün değildir.                                                      olarak aynı olabilir.
Bir çizgenin iki parçalı olduğunu anlamak için çizgenin bütün         Tanım ve örnek
elemanları arasında tek ve çift ayrımı yapılabilir. Örneğin rast      Örneğin aşağıdaki iki şekli ele alalım:
gele seçilen bir düğümden başlanarak diğer bütün düğümlerin
bu düğüme olan mesafesini yazmamız ve neticesinde tek ve
çift düğümlerin komşuluğunu kontrol etmemiz yeterlidir.
Yani çift veya tek iki düğüm birbirine komşu değilse bu
çizgeye iki parçalı çizge ismi verilebilir.




                                                                      Yukarıda verilen çizgedeki düğümler (nodes) iki farklı küme
                                                                      oluşturmak için aşağıdaki şekilde yerlerinden hareket
                                                                      ettirilmiş olsun:


Yukarıdaki şekilde başlangıç için rast gele olarak 0 seçilmiş
olsun. Bu çizgede K düğümüne olan uzaklıklarına göre bütün
düğümlere mesafeleri yazılmıştır. Örneğin İ düğümü K
düğümüne 3 düğüm uzaklıktadır. Sonrada bütün düğümler tek
ve çift olmasına göre renklendirilmiştir. Yani tek sayıdaki
uzaklıkta olanlar sarı, çift sayıdaki uzaklıkta olanları ise mavi
boyanmıştır. Bu boyama sadece görüntüleme için
kullanılmıştır.
Programlama sırasında bilgisayar tek ve çift sayıdaki
düğümleri kontrol edebilir. Örneğin G ve İ düğümleri
komşudur. Benzer şekilde İ ve I düğümleri de komşudur.
Şayet bu düğümler bir şekilde aynı şekilde olsaydı (ikiside
çift veya ikisi de tek olsaydı) bu durumda iki parçalı bir grafik
değildir sonucuna varılacaktı.
İki parçalı Çizgelerin kullanım alanları
Özellikle eşleştirme problemleri için oldukça kullanışlıdırlar.
Eşleştirme problemleri (matching problems) genelde iş/işçi
eşleştirmesi, evlilik, problem / çözüm eşleştirmesi gibi farklı
unsurları birleştirmek için kullanılırlar.
Örneğin k kişisi i işi için uygunsa k kişisi ile i işi arasında bir
kenar bulunuyor demektir. Bu iş ve kişilerden oluşan grafikte         Yukarıdaki bu yeni şekil ve ilk şekil arasında denklik söz
atama hatalarının olup olmadığının bulunması iki parçalı ağaç         konusudur. Buradaki denklik komşuluk anlamında
                                                                      düşünülebilir. Yani iki şekilde de bütün düğümlerin komşuları
bulan algoritmalar için oldukça basittir.
                                                                      aynıdır. Ancak fark edileceği üzere iki şekildeki elamanların
Örneğin paralel işleme (eş zamanlı işleme) ve koşut zamanlı
                                                                      yerleri değiştirilmiştir.
işleme (concurrent processing) gibi aynı anda birden fazla işin
                                                                      Bu durumda yukarıdaki iki şekil için denkşekilli (isomorphic,
beraber yapıldığı işlerde kullanılan petri ağları (Petri nets,
                                                                      izomorfik) denilebilir.
place / transition nets) gibi ağların modellenmesinde ve
                                                                      Yukarıdaki tanım için aynı zamanda kenar korumalı (edge
çalıştırılmasında önemli rol oynarlar.
iki parçalı Çizgelerin özellikleri                                    preserving) birebir ve örten dönüşüm (bijection) terimi
iki parçalı çizgeler için aşağıdaki çıkarımlar ve koşullar            kullanılabilir.
                                                                      Denkeşliliğin özellikleri
sıralanabilir:
                                                                      Şayet iki çizge denkeşli ise bu çizgelerin birisindeki döngü
     • Bütün ağaçlar iki parçalı çizgedir
                                                                      (cycle) sayısı diğerine eşittir.
     • Şayet bir çizge döngü (cycle) içermiyorsa iki parçalı          Şayet iki çizge denkeşli ise bu çizgelerden birisindeki toplam
          çizgedir                                                    düğüm dereceleri (node order) diğerine eşittir.
     • Şayet bir çizgede tek sayıda düğümden oluşan bir               Denkeşlilik Problemi (Isomorphism problem)
          döngü (cycle) içeriyorsa iki parçalı çizge değildir.        Denkeşlilik ile ilgili önemli bir problem iki grafın birbirine
     • Şayet bir çizge boyandığında iki renk veya daha az             denk olduğunun tespitinde yaşanır. Elimizde iki farklı graf
          renkle boyana biliyorsa bu çizge iki parçalı çizgedir.      olduğunu ve bunların denkeşli (isomoprhic) olup olmadığını
Denkşekillilik (Isomorphic)                                           öğrenmek istediğimizi düşünelim.
İki şeklin birbirinden farklı ancak denk olması durumudur.            Herşeyden önce bu problemi ilginç yapan, problemin polinom
Bilgisayar bilimleri de dahil olmak üzere pek çok bilim ve            zamanda çözülüp çözülemeyeceğidir. Bu problem bu anlamda
mühendislik alanında kullanılan çizge teorisine (graph theory)        ilginçtir çünkü problemi ne NP ne de P kümesine ait değildir
göre iki şekil birbirinden farklı çizilmiş ancak işlev ve değer       denilebilir.
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                    9
Aslında bu tartışma daha derinlerde NP            P iddiasının    bağlantı için bir ağırlık değeri atanmıştır. Buna göre her
doğruluğuna dayanmaktadır. Yani şayet NP, P nin üst               düğümden diğerine gitmenin maliyeti belirlenmiştir.
kümesiyse (superset) bu durumda ikisi arasında başka bir          Kruskal algoritmasında bütün yollar listelenip küçükten
küme olamaz. Ancak bazı araştırmacılar (örneğin Uwe               büyüğe doğru sıralanır. Bu liste yukarıdaki grafik için aşağıda
Schöning) bu iki küme arasında alt ve üst hiyerarşik seviyeler    verilmiştir:
bulunduğunu iddia etmişler ve denkşekillik gibi bazı              x-v:1
problemleri bu kümeye dahil etmişlerdir.                          w-v:1
İddiaya göre P altta ve NP üstte iki seviye olarak düşünülürse    w-u:1
düşük hiyerarşik seviyedeki problemler P’ye ve yüksek             x-w:2
hiyerarşik seviyedeki problemler NP’ye daha yakın kabul           u-s:2
edilecektir.                                                      x-y:3
Bütün bu iddiaların sebebi denkşekillik gibi problemlerin         t-u:3
karmaşıklığının (complexity) hala ispatlanamamış olmasıdır.       u-v:3
Bu      problemin     farklı   bir     halinin    karmaşıklığı    y-v:4
bulunabilmektedir. Örneğin problemimizi biraz değiştirerek        s-t:4
alt grafların (subgraphs) denkşekilliğini sorgulayacak olursak    y-z:5
bu      durumda      problemimiz       NP-Complete      olarak    y-t:5
sınıflandırılabilir.                                              z-t:10
Asgari Tarama Ağacı (Minimum Spanning Tree)                       Yukarıdaki liste çıkarıldıktan sonra sırasıyla en küçükten en
Asgarai tarama ağacı, ağırlıklık bir ağda (weighted graph,        büyüğe doğru komşuluklar işaretlenir. Bu işaretleme sırasında
yani her düğümü birbirine bağlayan yolların maliyeti (ağırlığı)   ada grupları ve grupların birbiri ile ilişkisine dikkat edilir.
olması durumu), bütün düğümleri dolaşan en kısa yolu verir.       Yani şayet listedeki iki düğüm harfi de aynı adadan ise bu
Örneğim aşağıdaki grafikte bütün düğümlere uğrayan en kısa        bağlantı atlanır. Aşağıda sırasıyla bu grafikteki adaların
yol işaretlenmiştir:                                              oluşması ve asgari tarama ağacının çıkarılması gösterilmiştir:
                                                                  x-v:1




asgari tarama ağacını veren en meşhur algoritmalar
Kruskal Asgari Tarama Ağacı Algoritması
Kruskal algoritmasının çalışması bir örnek üzerinden
açıklanmıştır.
                                                                  w-v:1




Yukarıdaki grafikte her düğüm için bir temsili harf ve her        w-u:1
                                                                                                                         10




                                                                 Bu noktadan sonra u-v:3 , y-v:4 , s-t:4 , y-z:5
x-w bağlantısı atlanır, çünkü iki düğüm de zaten dolaşılmıştır   bağlantılarındaki her iki düğümde aynı adada olduğu için
bunun yerine u-s:2 bağlantısına atlanır.                         atlanır ve y-t:5 bağlantısına geçilir.




x-y:3                                                            z-t:10 bağlantısı ise iki düğüm de gezildiği için yine
                                                                 gereksizdir.
                                                                 Prims Asgari Tarama Ağacı
                                                                 Bir asgari tarama ağacı (minimum spanning tree) algoritması
                                                                 olan Prim algoritması, işaretlemiş olduğu komşuluklara en
                                                                 yakın düğümü bünyesine katarak ilerler. Buna göre aşağıdaki
                                                                 grafiğin asgari tarama ağacını çıkaralım:




t-u:3
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015                                  11
                                                                 hem z hem de y üzerinden). Biz algoritmamıza devam edip en
                                                                 küçük yolu bünyemize dahil edelim. En yakın komşu x:3’tür.
                                                                 Bu durumda üyelerimiz {z,y,x} olacak ve yollarımız {z-y:5,y-
                                                                 x:3} olacaktır. Bu durum aşağıdaki grafikte gösterilmiştir:




Yukarıdaki grafikte her düğüm için bir temsili harf ve her
bağlantı için bir ağırlık değeri atanmıştır. Buna göre her
düğümden diğerine gitmenin maliyeti belirlenmiştir.
Prim algoritmasında rasgele bir başlangıç noktası seçilir.
Örneğin bizim başlangıç noktamız “z” düğümü olsun. Bu
durumda ilk inceleyeceğimiz komşuluk, “z” düğümünden             Yeniden komşularımızı listelersek:
gidilebilen düğümler ve maliyetleri olacaktır.                   t:5
z düğümünden gidilebilen düğümler ve maliyetleri aşağıda         v:1
listelenmiştir:                                                  w:2
y:5                                                              yukarıdaki listede bünyemize aldığımız adadan, bir düğüme
t:10                                                             giden birden fazla yol bulunması durumunda en kısası
Prim algoritması bu listedeki en küçük maliyetli komşuyu         alınmıştır. Bu durumda listenin en küçük elemanı olan v:1
bünyesine dahil eder. Buna göre yeni üyelerimiz {z,y}            tercih edilir ve üyelerimiz {z,y,x,v} yollarımız ise {z-y:5,y-
olacaktır ve gidilen yollar {z-y:5} olacaktır. (ilk üyeler       x:3,x-v:1} olur. Durum aşağıdaki grafikte gösterilmiştir:
listesinde şimdiye kadar ziyaret edilmiş düğümler bulunur. Bu
düğümler listesinde zaten olan bir düğüm listeye eklenemez.
yollar listesinde ise hangi düğümden hangi düğüme ne kadar
maliyetle gidildiği tutulur.) Dolayısıyla grafiğimizde Prim
algoritması tarafından işaretlenen düğümler aşağıda
gösterilmiştir:




                                                                 Yeniden komşularımızı listelersek:
                                                                 t:5
                                                                 u:3
                                                                 w:1
                                                                 yukarıdaki listede bünyemize aldığımız adadan, bir düğüme
                                                                 giden birden fazla yol bulunması durumunda en kısası
şimdi üyelerimizin durduğu listedeki bütün düğümlerin            alınmıştır. Bu durumda listenin en küçük elemanı olan w:1
komşularını listeleyelim:                                        tercih edilir ve üyelerimiz {z,y,x,v,w} yollarımız ise {z-y:5,y-
t:5                                                              x:3,x-v:1,v-w:1}      olur.    Durum      aşağıdaki     grafikte
t:10                                                             gösterilmiştir:
v:4
x:3
yukarıdaki listede t düğümüne iki farklı gidiş bulunmaktadır (
                                                                                                                            12




Yeniden komşularımızı listelersek:                               Son komşumuz olan t için en kısa ulaşım
t:5                                                              t:3 değeridir ve u üzerinden sağlanır. Bu durumda listenin en
u:1                                                              küçük elemanı olan t:3 tercih edilir ve üyelerimiz
yukarıdaki listede bünyemize aldığımız adadan, bir düğüme        {z,y,x,v,w,u,s,t} yollarımız ise {z-y:5,y-x:3,x-v:1,v-w:1,w-
giden birden fazla yol bulunması durumunda en kısası             u:1,u-s:2,u-t:3} olur. Sonuçta elde edilen asgari tarama ağacı}
alınmıştır. Bu durumda listenin en küçük elemanı olan u:1        aşağıda verilmiştir:
tercih edilir ve üyelerimiz {z,y,x,v,w,u} yollarımız ise {z-
y:5,y-x:3,x-v:1,v-w:1,w-u:1} olur. Durum aşağıdaki grafikte
gösterilmiştir:




Yeniden komşularımızı listelersek:
t:3
s:2
yukarıdaki listede bünyemize aldığımız adadan, bir düğüme
giden birden fazla yol bulunması durumunda en kısası
alınmıştır. Bu durumda listenin en küçük elemanı olan s:2
tercih edilir ve üyelerimiz {z,y,x,v,w,u,s} yollarımız ise {z-
y:5,y-x:3,x-v:1,v-w:1,w-u:1,u-s:2} olur. Durum aşağıdaki
grafikte gösterilmiştir:
Sadi Evren SEKER, Çizge Teorisi (Graph Theory), YBS Ansiklopedi, v.2, is.2, pp. 17-41, 2015   13

Kaynaklar
Arslan, M. L., & Seker, S. E. (2014). Web Based Reputation
Index of Turkish Universities. International Journal of E-
Education E-Business E-Management and E-Learning (IJEEEE) ,
4 (3), 197-203.
Biggs, N., Lloyd, E., & Wilson, R. (1986). Graph Theory. Oxford
University Press.
Chen, W.-K. (1997). Graph Theory and its Engineering
Applications. World Scientific.
Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stei, C. (2001).
Introduction to Algorithms (Vol. Second Edition). MIT Press and
McGraw-Hill.
Garey, M. R., & Johnson, D. S. (1979). Computers and
Intractability: A Guide to the Theory of NP-Completeness. W.H.
Freeman.
Gibbons, A. (1985). Algorithmic Graph Theory. Cambridge
University Press.
Mallows, C. L., & Sloane, N. J. (1975). Two-graphs, switching
classes and Euler graphs are equal in number. SIAM Journal on
Applied Mathematics , 28 (4), 876–880.
Sedgewick, R. (1983). Graph algorithms, Algorithms. Addison-
Wesley.
Seker, S. E. (2015). Computerized Argument Delphi Technique.
IEEE Access , 3, 368 - 380.
SEKER, S. E. (2015). Temporal logic extension for self referring,
non-existence, multiple recurrence and anterior past events.
Turkish Journal of Electirical Engineering and Computer
Sciences , 23 (1), 212-230.
Seker, S., Altun, O., Ayan, U., & Mert, C. (2014). A Novel
String Distance Function Based on Most Frequent K Characters.
International Journal of Machine Learning and Computation
(IJMLC) , 4 (2), 177-183.
Tutte, W. T., & Smith, C. A. (1941). On Unicursal Paths in a
Network of Degree 4. American Mathematical Monthly , 48,
233–237.

