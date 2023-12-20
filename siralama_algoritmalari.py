"""
Sıralama Algoritmaları
"""

# İki değişkenin değerinin yerlerini değiştirme
# Soru: x'i y, y'yi x yap.
# Python Çözümü: x, y = y, x

x = 7
y = 9
print(f"Başlangıç Değerleri: x = {x} y = {y}")

# 1. yol
a = x 
b = y
x = b
y = a
print(f"x = {x} y = {y}")

# 2. yol
a = x
x = y
y = a
print(f"x = {x} y = {y}")

# 3. yol
x, y = y, x
print(f"x = {x} y = {y}")

# Bir dizide en küçük değeri bulma
def enkucuk(dizi):
    
    enk = dizi[0] # dizinin ilk elemanını en küçükmüş gibi varsay
    enk_index = 0
    
    for i in range(1, len(dizi)): # i'yi 1'den başlat dizinin uzunluğu kadar say
        if dizi[i] < enk:
            enk = dizi[i] 
            enk_index = i
    return enk, enk_index
 
def siralimi(dizi):

    for i in range(len(dizi)-1):
        if dizi[i] > dizi[i+1]:
            return False
    return True

for i in range(3):
    print(" ")

print("En küçük değer: ", enkucuk([5, 6, 12, 2, 3]))
print("En küçük değer: ", enkucuk([55, -6, 12, 2, 0]))
    
for i in range(3):
    print(" ")
    
print("Sonuç: ", siralimi([5, 6, 12, 2, 3]))    
print("Sonuç: ", siralimi([1, 2, 6, 10]))    


"""
##################### 1) Seçmeli Sıralama (Selection Sort) ####################
"""

def secmeli_siralama(dizi):
    
    for i in range(len(dizi) - 1):
        
        # i'nin sağındaki değerleri gez
        # en küçük değeri ve indeksini bul
        min = dizi[i+1]
        min_index = i+1
        
        for t in range(i+1, len(dizi)):
            if dizi[t] < min:
                min = dizi[t]
                min_index = t
        
        # eğer sağda daha küçük bir değer bulunduysa yerlerini değiştir
        if min < dizi[i]:
            dizi[i], dizi[min_index] = dizi[min_index], dizi[i]

listem = [1, 3, 5, 7, 0, 2, 6] 
secmeli_siralama(listem)           
print(listem)           
            
"""
##################### 2) Kabarcık Sıralama (Bubble Sort) ######################
"""
    
def kabarcik_siralama(dizi):
    
    for i in range(len(dizi)): # i = 0'dan başlayıp dizinin uzunluğu kadar sayacak
    # i değeri dizinin uzunluğu kadar sayarken alttaki for döngüsü de o kadar çalışacak
        
        # t'nin her bir turunda i değeri 1 artacak
        for t in range(0, len(dizi) - i-1):
            if dizi[t] > dizi[t+1]:
                dizi[t], dizi[t+1] = dizi[t+1], dizi[t]
    
sayilar = [6, 8, 5, 1, 9, 10, -5, 99, 13]
kabarcik_siralama(sayilar)
print(sayilar)   

















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    