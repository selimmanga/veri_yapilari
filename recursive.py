"""Recursive Functions (Özyineleme)"""

def f(x):
    
    # Sonlandırma kriteri
    if x == 1:
       print(0)
    # Fonksiyonu tekrardan çağırma kısmı   
    else:
       print(x)
       f(x-1)
       
# Bu yöntemle faktöriyel hesaplama yapalım       
def faktoriyel(x):
    
    if x == 0:
        return 1
    return x * faktoriyel(x-1)

print(faktoriyel(5))

print(" ")

# Fibonacci Sayı Dizisi (Altın Oran)
def fib(n):
    if n == 1 or n == 0:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(0)) # 1
print(fib(1)) # 1

print(([fib(i) for i in range(15)]))