### Fonksiyonlar ###

# 1) Oluşturma, tanımlama
# Fonksiyonun amacını, ne iş yaptığını ve parametrelerini belirleriz

# 2) Çağırma, kullanma
# Oluşturduğumuz fonksiyonu kullanıyoruz.
# ÖR: fonksiyonumuz kare.al(x) ise kare.al(5) = 25 işlemini döndürecektir
# return geri dönüş için kullanılır

# Bir fonksiyon oluşturalım

def kare_al(a):
  kare = a * a
  return kare

# Fonksiyonu kullanma

sonuc = kare_al(7)
print(sonuc)

# İki sayının modunu alalım

def mod(x, y):
   sonuc = x % y
   return sonuc

print(mod(5, 3))

# Dikdörtgen alanını hesaplama

def alan(a, b):
  alan = a * b
  return alan

print(alan(4, 5))

# Kullanıcıdan alınan değeri hesaplattıralım

a = int(input("Kısa kenarı giriniz: "))
b = int(input("Uzun kenarı giriniz: "))

# Yukarda tanımladığımız fonksiyonu kullanacağız

sonuc = alan(a, b)
print(sonuc)

### Sınıf ve Nesne ###

# Sınıf: Ortak özelliklere sahip varlıkların bir arada olduğu gruplara denir.
# self: kendine ait olduğunu belirten bir anahtar kelimedir
# Nesne: Bir sınıfa ait özellikleri taşıyan ve bu sınıftan türetilen varlık

class Cat:
    ayak_sayisi = 4
    isim = "Kedi"

    def __str__(self):
      return "Kedinin ayak sayısı: " + str(self.ayak_sayisi)

# Oluşturduğumuz sınıfa "kedi1" adında bir kedi ekledik
# Nesnenin özelliğini çağırmak için "." kullanılır

kedi1 = Cat()

# Kedinin adını değiştirelim, bu şekil istediğimiz gibi isim değişikliği yapabiliriz
kedi1.isim = "Maviş"

print(kedi1) # Kedinin özellikleri
print(kedi1.isim) # Kedinin adı
print(kedi1.ayak_sayisi) # Kedini ayak sayısı

# Kedi sınıfına parametre eklemek için bazı değişiklikler yaptık
class Cat:
    ayak_sayisi = 4
    isim = "Kedi"

    def __init__(self, ayak_sayisi, isim): # init: bu fonksiyonun kullanılma amacı ilk yapılacak şeyi belirlemek. her sınıfta olmak zorunda!!!

      # Parametreleri oluşturalım
      self.ayak_sayisi = ayak_sayisi
      self.isim = isim

    def __str__(self): # str: bu fonksiyonu geri dönüşte isteğe bağlı olarak çıktı almak için kullanırız (opsiyonel)
      return "Kedinin ayak sayısı: " + str(self.ayak_sayisi) + " Adı: " + self.isim

kedi2 = Cat(4, "Boncuk")
kedi3 = Cat(4, "Kara")

print(kedi1)
print(kedi2)
print(kedi3)

class Araba:
  teker_sayisi = 4
  beygir_gucu = 90
  model = 94
  marka = "BMW"

  def __init__(self, teker_sayisi, beygir_gucu, model, marka):
    self.teker_sayisi = teker_sayisi
    self.beygir_gucu = beygir_gucu
    self.model = model
    self.marka = marka

  def __str__(self):
    return "Teker Sayısı: " + str(self.teker_sayisi) + "\nBeygir Gücü: " + str(self.beygir_gucu) + "\nModeli: " + str(self.model) + "\nMarkası: " + str(self.marka)

selimin_araci = Araba(4, 300, 2023, "Mercedes")
burakin_araci = Araba(4, 350, 1970, "Mustang")

print(selimin_araci)
print(" ")
print(burakin_araci)

# Düğüm sınıfı oluşturalım

class Dugum_Olustur:
  deger = 0
  link = None

  def __init__(self, deger, link):
    self.deger = deger
    self.link = link

class Bagli_Liste:
  bas = None
  def basa_ekle(self, deger):

    if self.bas == None: # baştaki değer boş ise olacaklar
      self.bas = Dugum_Olustur(deger, None) # İlk defa eleman oluştururken kullanıyoruz
    else: # Daha önceden eklenen bir eleman varsa olacaklar
      yeni_dugum = Dugum_Olustur(deger, None)
      yeni_dugum.link = bas # yeni düğümün linkini başa eşitledik fakat bas degeri hala 3, amacımız bas degerini 4 yapmak
      self.bas = yeni_dugum # bas değeri artık 4 oldu
