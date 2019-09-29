# Zisťí minimum dvoch čísel

def minimum_troch(a, b, c):
	if a > b:
		if b > c:
			return c
		else:
			return b
	elif b > a:
		if a > c:
			return c
		else:
			return a

x = int(input("Zadajte prvé číslo: "))
y = int(input("Zadajte druhé číslo: "))
z = int(input("Zadajte tretie číslo: "))
print(minimum_troch(x, y, z))