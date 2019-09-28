# Vypočíta aritmetickú postupnosť a + b * d

def aritmia(a_, d, N):
	for i im range (N):
		print(a_ + (i * d))
		
x = int(input("Zadajte prvé číslo: "))
y = int(input("Zadajte druhé číslo: "))
z = int(input("Zadajte tretie číslo: "))
aritmia(x, y, z)