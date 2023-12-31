# dizi örneği

stoklar = [10, 15, 8, 9, 17]
print(stoklar)

# eleman ekleme

# insert = ekleme fonksiyonu

stoklar.insert(3, 6) # 3 no'lu indekse 6 elemanını ekle
print(stoklar)

# dizi sonunda -25 eklemek
# append = dizinin en sonuna ekler
stoklar.append(-25)
print(stoklar)

# eleman silme

# 1 - eleman değeri ile silme
# remove = ilk karşılaştığı elemanı siler
stoklar.remove(17)
print(stoklar)

# 2 - index yöntemi ile silme
stoklar.pop(3) # 3 no'lu indeksteki değeri sil
print(stoklar)

# del = silme kodu
del stoklar[-1] # -1 numaralı indeks son eleman olduğu için sondaki elemanı siler
print(stoklar)

# arama işlemi
print(stoklar.index(8)) # 8 elemanının indeksi = 2

# değiştirme işlemi
# listenin 4. elemanını 0 yapalım
stoklar[3] = 0 # stoklar(index no) = 3 numaralı indeksteki elemanın değerini 0 yaptık
print(stoklar)

stoklar.append(8) # listenin sonuna 8 ekle
stoklar.insert(0, 8) # 0 indeksli elemana 8 ekle
stoklar.pop(3) # 4 no'lu indeksteki elemanı sil
print(stoklar)

print(stoklar.count(8)) # listede kaç adet 8 olduğunu verir

stoklar.sort() # büyükten küçüğe sıralar
print(stoklar)

stoklar.reverse() # elemanların sırasını ters çevir (küçükten büyüğe yapmak için kullandık)
print(stoklar)

stoklar.sort() # küçükten büyüğe
print(stoklar)

stoklar.sort(reverse=True) # direkt olarak büyükten küçüğe sıralama işlemi
print(stoklar)

# dizideki eleman sayısını verir
print(len(stoklar))

yaslar = [19, 27, 36, 45]
stoklar.extend(yaslar) # iki diziyi birleştirme işlemi, "stoklar" ve "yaslar" dizisini birleştirdik
print(stoklar)

print(36 in stoklar) # "in" kodu dizinin içinde 36'nın olup olmadığını kontrol eder ve true ya da false olarak cevap verir

stoklar_yedek = stoklar.copy() # bir değişken oluşturup orijinal diziye eşitledik
print(stoklar_yedek)

stoklar_yedek.clear() # listedeki tüm elemanları temizledik
print(stoklar_yedek)
