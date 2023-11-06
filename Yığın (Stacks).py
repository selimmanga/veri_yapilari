class Dugum_Olustur:
  deger = 0
  link = None

  def __init__(self, deger, link):
    self.deger = deger
    self.link = link
    
    
"""
class Yigin:
    def __init__(self):
        self.enust = None
        self.eleman_sayisi = 0
"""   
class Yigin:
    enust = None
    eleman_sayisi = 0
    
    def __init__(self):
        self.eleman_sayisi = 0
    
    def eleman_sayisi(self):
        return self.eleman_sayisi
    
    def bos_mu(self):
        return self.eleman_sayisi == 0
    """if self.eleman_sayisi == 0:
        return True # Koşul doğru ise True dönecek değilse False"""
    
    def peek(self): # En üstteki elemanı verir
        return self.enust
    
    def push(self, deger):
        dugum = Dugum_Olustur(deger, None)
        dugum.link = self.enust
        self.enust = dugum 
        self.eleman_sayisi += 1
        
    def pop(self): # En üstteki elemanı alıp çıkarır ve bir sonraki değeri en üst'e eşitler
       if self.eleman_sayisi != 0:
           silinen = self.enust
           self.enust = self.enust.link
           self.eleman_sayisi -= 1
           return silinen
    
    def __str__(self):
        gezici = self.enust
        while gezici != None:
            print(gezici.deger, end=" ")
            gezici = gezici.link
        return ""

stack = Yigin() # Nesneyi oluşturduk

stack.push(6)
stack.push(8)
stack.push(4)
stack.push(3)
stack.push(7)
print(stack)

for i in range(4):
    print(" ")

stack.pop()
print(stack)

for i in range(4):
    print(" ")

harflerim = Yigin()
for i in "Selim":
    harflerim.push(i)
    
print(harflerim)

for i in range(4):
    print(" ")

sayilarim = Yigin()
for i in [3, 5, 7, 9, 16]:
    sayilarim.push(i)
    
print(sayilarim)





      
      