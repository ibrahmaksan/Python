import time

baslangic = time.time()

def agaci_coz(node,binaryStr=''):

    if type(node) is str:  #Eğer düğüm bir karakter ise, o karakterin Huffman kodunu içeren bir sözlük döndürülür.
        ##Yani yapraklara kadar gidecegiz.
        return {node: binaryStr}
    
    (sol, sag) = node.alt_dugumler() ## eger dugum karakter degil de bir baska dugumse(Agac nesnesi ise) o zaman onun saginda ve solunda ne var ona bakmak gerekiyor. Yani
    ## tekrardan agaci_coz fonksiyonuna girecegiz. Burada recursive bir islem var. Karakter bulunana kadar devam edilecek.

    kodlar = {} ##karakterleri ve huffmann kodlarini atacagimiz sozlugumuz.
    kodlar.update(agaci_coz(sol,binaryStr + '0')) ##Mesela burda en sola kadar gidilecek. Ve bir karakterle karsilasilana kadar 0 konacak.Burasi bittiginde dugumun sagina bakilacak.

    kodlar.update(agaci_coz(sag,binaryStr + '1')) ## Update ile de sozluk elemanlari surekli guncellenecek. Yeni bir karakter gelirse eklenecek.
    return kodlar ## En sonda ise tüm karakterleri ve onlarin huffman kodlarini iceren sozlugumuzu donuyoruz.


## Ağaç oluşumunu sağlamak için oluşturduğum sınıf. Bu sınıfın her bir üyesi bir düğüm olacak.
class Agac(object):

    def __init__(self, sol=None, sag=None):

        self.sol = sol ## sol ve sag olmak uzre iki kısma ayrılacak nodeumuz.
        self.sag = sag

    def alt_dugumler(self): #bir düğümün sol ve sağ alt düğümlerini döndürür
        return (self.sol, self.sag)
    

metin = "aaaabbcddddd" ## huffmann kodunu bulacagimiz metin

#frekanslar adlı bir sözlük oluşturdum ve her karakterin metindeki frekansını bu sözlükte sakladım
#sorted fonksiyonunu kullanarak frekansları büyükten küçüğe sıraladım.
frekanslar = {}

for c in metin:
    if c in frekanslar:
        frekanslar[c] += 1
    else:
        frekanslar[c] = 1

frekanslar = sorted(frekanslar.items(), key=lambda x: x[1], reverse=True)

dugumler = frekanslar ## nodellarımız sözlüğün her bir elemanı olacak.

while (len(dugumler) > 1):
    (karakter1, f1) = dugumler[-1] ## sözlükteki son ve sondan bir önceki elemanin frekanslarini toplamyabilmek icin degiskenlere ataniyor.
    (karakter2, f2) = dugumler[-2]##f1 ve f2 karakterlerin metinde kac kez tekrarlandigini gosteriyor.

    dugumler = dugumler[:-2] ## islemi yapilan son iki eleman listeden cikariliyor.

    node = Agac(karakter1, karakter2) ## karakter1 ve karakter2 icin dugum olusturuluyor. Bu dugumun solunda ve saginda karakter olacak.
    dugumler.append((node, f1 + f2)) # toplanan karakterler sozluge yeniden ekleniyor. Artik yeni bir sozluk elemanimiz oldu. Simdi bunu asagida
    ## tekrar siralayalim ki isleme devam edebilelim. Çünkü yine en kucuk ikisini almamiz gerekecek.

    dugumler = sorted(dugumler, key=lambda x: x[1], reverse=True)


huffmankodu = agaci_coz(dugumler[0][0]) ## huffmann kodlarini tutan sozlugumuz.

print('Karakterler : Huffman Kodu ') ## Asagida kalan tum kisim yazdirma islemidir.
print('**************************')

anahtarlar = huffmankodu.keys()

for karakter in anahtarlar:
    print(karakter, " : " ,huffmankodu[karakter])

print('**************************')

binaryString = ""
for karakter in metin:
    binaryString += huffmankodu[karakter]

print(f"Metnin Huffmann Kodu :{binaryString} ---  Metin boyutu : {len(binaryString)} bit")

print("***************************")

son = time.time()
print(f"Geçen süre: {son-baslangic}")