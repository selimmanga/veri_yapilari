class Dugum_Olustur:
  deger = 0
  link = None

  def __init__(self, deger, link):
    self.deger = deger
    self.link = link

n1 = Dugum_Olustur(3, None) # İki adet düğüm oluşturduk
n2 = Dugum_Olustur(7, None)

n1.link = n2 # n1'in linkini n2'ye eşitledik

print(n1) # bellekteki adresini gösterir
print(n2) # bellekteki adresini gösterir 

print(n1.deger) # n1'in içindeki değeri gösterir = 3
print(n2.deger) # n2'nin içindeki değeri gösterir = 7

print(n1.link) # n1'in link değerini gösterir
print(n2.link) # n2'nin link değerini gösterir

n1.link = n2
print(n1.deger) 
print(n2.deger) 

print(n1.link) 
print(n2.link)

print(" ")
print(" ")
print(" ")
print(" ")
print(" ")

class Bagli_Liste:
  bas = None

  def __init__(self): # self'den sonra bas isteğe bağlı şekilde yazılır
    pass # boş geçtiğimizde yazılır

  def basa_ekle(self, deger):

    if self.bas == None: # baştaki değer boş ise olacaklar
      self.bas = Dugum_Olustur(deger, None) # İlk defa eleman oluştururken kullanıyoruz
    else: # Daha önceden eklenen bir eleman varsa olacaklar
      yeni_dugum = Dugum_Olustur(deger, None)
      yeni_dugum.link = self.bas # yeni düğümün linkini başa eşitledik fakat bas degeri hala 3, amacımız bas degerini 4 yapmak
      self.bas = yeni_dugum # bas değeri artık 4 oldu
  
  def __str__(self): 
      mevcut_dugum = self.bas
      while mevcut_dugum != None:
          print(mevcut_dugum.deger)
          mevcut_dugum = mevcut_dugum.link
      return ""
      
  
  def sona_ekle(self, deger):
      if self.bas == None: # Liste boşsa
        self.basa_ekle(deger)
      else:
          mevcut_dugum = self.bas
          
          # sona kadar git 
          while mevcut_dugum.link:
              mevcut_dugum = mevcut_dugum.link
              
          # yeni düğümü ekle
          mevcut_dugum.link = Dugum_Olustur(deger, None)
   
  def bastan_sil(self):
      silinen = self.bas # Listeden sildiğimiz değeri saklıyoruz
      if self.bas != None:
          self.bas = self.bas.link
          return silinen 
      
  def sondan_sil(self):
      if self.bas.link != None:
          mevcut_dugum = self.bas
          while mevcut_dugum.link.link != None:
              mevcut_dugum = mevcut_dugum.link
              
          silinen = mevcut_dugum.link
          mevcut_dugum.link = None
      else:
          silinen = self.bastan_sil(self)
      return silinen
          
"""Bu metodu kullanmamızın amacı listenin bellekteki adresi yerine girilen değeri yazdırmak, 
eğer bu olmazsa bellekteki adresini çıktı olarak alırız"""   
      
"""Renk listesi oluşturalım"""
        
renkler = Bagli_Liste() # Boş bir liste oluşturduk

print("======================")
print("Renk Listesi")
print("======================")

# Başa eklediğimiz renkler
renkler.basa_ekle("Kırmızı")
renkler.basa_ekle("Mavi")
renkler.basa_ekle("Yeşil")

# Sona eklediğimiz renkler
renkler.sona_ekle("Turuncu")
renkler.sona_ekle("Sarı")
renkler.sona_ekle("Pembe")

print(renkler)

print(" ")
print(" ")
print(" ")

# Baştan sildiğimiz renkler
renk = renkler.bastan_sil()
print(renk) # Sildiğimiz rengin adresi
print(renk.deger) # Sildiğimiz rengin değeri

print(" ")

# Sondan sildiğimiz renkler
renk2 = renkler.sondan_sil()
print(renk2) # Sildiğimiz rengin adresi
print(renk2.deger) # Sildiğimiz rengin değeri



