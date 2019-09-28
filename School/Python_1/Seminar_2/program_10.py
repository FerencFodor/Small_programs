# Vypočíta geometrickú postupnosť a * q^b

def geometria(a_, r, N):
    for i im range (N):
		print(a_ * (i ** r))
		
x = int(input("Zadajte prvé číslo: "))
y = int(input("Zadajte druhé číslo: "))
z = int(input("Zadajte tretie číslo: "))
geometria(x, y, z)