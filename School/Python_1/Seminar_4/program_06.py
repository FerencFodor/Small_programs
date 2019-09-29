# Vráti počet rovnakých čísel

def same_num(a, b, c):
	if a == b and a == c and b == c:
		return 3
	elif a == b or a == c or b == c:
		return 2
	else:
		return 0

x = int(input("Zadajte prvé číslo: "))
y = int(input("Zadajte druhé číslo: "))
z = int(input("Zadajte tretie číslo: "))
print(same_num(x, y, z))