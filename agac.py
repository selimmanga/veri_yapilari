class Dugum:
    def __init__(self, deger):
        self.sol = None
        self.sag = None
        self.deger = deger

"""
d1 = Dugum(10)
d2 = Dugum(16)
d3 = Dugum(8)

# Sağ ve sol çocukları kök düğüme bağladık
d1.sol = d3 
d1.sag = d2

d2.sol = Dugum(14)

d3.sol = Dugum(6)
d3.sag = Dugum(9)

d4 = Dugum(18)
d2.sag = d4

d4.sol = Dugum(17)
d4.sag = Dugum(19)

print(d1.sag.sag.sag.deger) # 19
print(d1.sag.sol.deger) # 14
"""

def inorder(kok_dugum): # sol, kök, sağ

    if kok_dugum == None:
        return
        
    inorder(kok_dugum.sol)
    print(kok_dugum.deger, end=" ")
    inorder(kok_dugum.sag)
    
    
def preorder(kok_dugum): # sol, kök, sağ

    if kok_dugum == None:
        return
        
    print(kok_dugum.deger, end=" ")
    preorder(kok_dugum.sol)
    preorder(kok_dugum.sag)    

    
def postorder(kok_dugum): # sol, kök, sağ

    if kok_dugum == None:
        return
        
    postorder(kok_dugum.sol)
    postorder(kok_dugum.sag)
    print(kok_dugum.deger, end=" ")

"""
inorder(d1)
print(" -> InOrder")

preorder(d1)
print(" -> PreOrder")

postorder(d1)
print(" -> PostOrder")
"""

def ara(kok_dugum, deger):
    
    # Kök değeri boşsa ya da kökteki değer aranan değere eşitse kökteki değeri çağır
    if kok_dugum == None or kok_dugum.deger == deger:
        return kok_dugum
    
    # Sol taraf için
    if kok_dugum.deger > deger:
        return ara(kok_dugum.sol, deger)
    
    # Sağ taraf için
    return ara(kok_dugum.sag, deger)
    
"""sonuc = ara(d1, 8)

if sonuc == None:
    print("Bulunamadı.")
else:
    print("Bulundu.")
"""
    
def ekle(kok_dugum, deger):
    
    # Çıkış koşulları 
    if kok_dugum == None:
        return Dugum(deger)
        
    if kok_dugum.deger == deger:
        return kok_dugum

    # Sol taraf
    if kok_dugum.deger > deger:
        kok_dugum.sol = ekle(kok_dugum.sol, deger)
    else:
        # Sağ taraf
        kok_dugum.sag = ekle(kok_dugum.sag, deger)
    return kok_dugum


def sil(kok_dugum, deger):
    
    if kok_dugum == None:
        return None
    
    if kok_dugum.deger > deger:
        kok_dugum.sol = sil(kok_dugum.sol, deger)
        
    elif kok_dugum.deger < deger:
        kok_dugum.sag = sil(kok_dugum.sag, deger)
        
    #aranan deger bulunduysa
    else:
        # ağacın solu boş, sağ tarafı döndür
        if kok_dugum.sol == None:
            return kok_dugum.sag
        
        # ağacın sağı boş, sol tarafı döndür
        if kok_dugum.sag == None:
            return kok_dugum.sol
        
        # ağacın iki çocuğu varsa
        enkucuk = kok_dugum.sag
        
        # en küçük değerin solunda değer olduğu sürece
        while enkucuk.sol:
            enkucuk = enkucuk.sol
        
        kok_dugum.deger = enkucuk.deger
        kok_dugum.sag = sil(kok_dugum.sag, enkucuk.deger)
        
    return kok_dugum
        
        
kok1 = Dugum(20)
degerler = [15, 26, 11, 17, 23, 30, 8, 12, 22, 36, 21, 32]

for deger in degerler:
    kok1 = ekle(kok1, deger)
    
inorder(kok1)
print(" -> InOrder")

preorder(kok1)
print(" -> PreOrder")

postorder(kok1)
print(" -> PostOrder")

for i in range(5):
    print(" ")
        
    
kok1 = sil(kok1, 20)

print("Silinme Sonrası")
inorder(kok1)
print(" -> InOrder")

preorder(kok1)
print(" -> PreOrder")

postorder(kok1)
print(" -> PostOrder")  
