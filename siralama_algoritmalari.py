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

"""
##################### 3) Hızlı Sıralama (Quick Sort) ##########################

Bir pivot seçilir, sağ sol ya da ortadan. Sağındaki elemanlar pivottan büyük, solundakiler küçük olmalı.
Daha sonra kalan kısımlar kendi aralarında sıralanmalı.

- t değeri pivottan büyük olunca bir sonrakine geç, küçük olunca i'yi 1 arttır ve t'yi sabit tut.
- Gezme işlemi bittikten sonra parçalamaya başlarız ve parçalamaya (i+1)'den başlarız.
"""

def parcala(dizi, low, high):
    
    if high > low:
        pivot = dizi[high]
        i = low - 1
        
        for t in range(low, high):
            if dizi[t] < pivot:
                i += 1
                dizi[i], dizi[t] = dizi[t], dizi[i]
        
        dizi[i+1], dizi[high] = dizi[high], dizi[i+1]
        return i+1

def hizli_siralama(dizi, low, high):
    
    if high > low:
        parcalama_indeksi = parcala(dizi, low, high)
        
        # İndeksin solunda kalanları sırala
        hizli_siralama(dizi, low, parcalama_indeksi-1)
    
        # İndeksin sağında kalanları sırala
        hizli_siralama(dizi, parcalama_indeksi+1, high)
    
yeni_liste = [11, 9, 16, 5, 10]
hizli_siralama(yeni_liste, 0, len(yeni_liste)-1)
print(yeni_liste)


"""
##################### 3) Eklemeli Sıralama (Insertion Sort) ###################
"""
        
def eklemeli_siralama(dizi):
    
    for t in range(1, len(dizi)):
        deger = dizi[t]
        x = t - 1
        
        while x >= 0 and deger < dizi[x]:
            dizi[x+1] = dizi[x]
            x -= 1
        
        dizi[x+1] = deger
            
            
liste2 = [11, 2, 5, 7, 8, 4, 1, -6]
eklemeli_siralama(liste2)
print(liste2)            


"""
##################### 4) Birleştirmeli Sıralama (Merge Sort) ###################
"""

def birlestirmeli_siralama(dizi):
    
    if len(dizi) > 1:
        orta_nokta = len(dizi) // 2 # tam sayılı bölme
        sol = dizi[:orta_nokta]
        sag = dizi[orta_nokta:]
        
        birlestirmeli_siralama(sol)
        birlestirmeli_siralama(sag)
        
        i = k = j = 0 # i, j, k = 0, 0, 0
        
        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j]:
                dizi[k] = sol[i]
                i += 1
            else:
                dizi[k] = sag[j]
                j += 1
            
            k += 1
        
        # Solda eleman olduğu sürece
        while i < len(sol):
            dizi[k] = sol[i]
            i += 1
            k += 1
        
        # Sağda eleman olduğu sürece
        while j < len(sag):
            dizi[k] = sag[j]
            j += 1
            k += 1
            
liste3 = [11, 2, 5, 7, 8, 4, 1, -6]
birlestirmeli_siralama(liste3)
print(liste3)       
