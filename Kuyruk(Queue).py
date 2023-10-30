class Dugum_Olustur:
  deger = 0
  link = None

  def __init__(self, deger, link):
    self.deger = deger
    self.link = link

class Kuyruk:
  bas = None
  son = None
     
  def __init__(self):
      pass

  def bos_mu(self):
      return self.bas == None
  
  def sona_ekle(self, deger):
      
      yeni_dugum = Dugum_Olustur(deger, None)
      
      # Kuyruk boşsa
      if self.bas == None:
          self.bas = yeni_dugum
          self.son = yeni_dugum
          # self.bas = self.son = yeni_dugum
          
      # Kuyruk boş değilse
      else:
          self.son.link = yeni_dugum
          self.son = yeni_dugum
          # self.son.link = self.son = yeni_dugum
      
  def bastan_cikar(self):
      if self.bas != None: # if self.bas: olarak da yazılabilir (!= için)
          silinen = self.bas 
          
          if self.bas == None:
              self.bas = self.son = None
          else:
              self.bas = self.bas.link
          return silinen
          
  def __str__(self):
      mevcut_dugum = self.bas
      while mevcut_dugum:
          print(mevcut_dugum.deger, end=" ")
          mevcut_dugum = mevcut_dugum.link
      return ""
  
kuyruk1 = Kuyruk()
kuyruk1.sona_ekle("Selim")
kuyruk1.sona_ekle("Burak")
kuyruk1.sona_ekle("Doğukan")
kuyruk1.sona_ekle("Gizem")

"""for i in range(4):
    kuyruk1.bastan_cikar()
   print(kuyruk1)"""
   
kuyruk1.bastan_cikar()
print(kuyruk1)
          
          
          
          
          
          
          
          
          
          
          
          
          
          