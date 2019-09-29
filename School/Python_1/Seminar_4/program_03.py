# Zisťí minimum dvoch čísel

def minimum_dvoch(a, b):
	if a < b:
		return a
	else:
		return b

x = int(input("Zadajte prvé číslo: "))
y = int(input("Zadajte druhé číslo: "))
print(minimum_dvoch(x, y))