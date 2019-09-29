# Šach
# Zistí či na dvoch rôznych súradniciach je farba forvnaká

def same_color(x1, y1, x2, y2)
	if 1 > x1 > 8 or 1 > y1 > 8 or 1 > x2 > 8 or 1 > y2 > 8:
		print("Zadali ste nesprávne hodnoty (1 > hodnota > 8 )!")
		return False
	
	if ((y1 - y2) % 2 == 0 and (x1 - x2) % 2 == 0) or ((y1 - y2) % 2 != 0 and (x1 - x2) % 2 != 0):
		return True
	else
		return False

x1 = int(input("Zadajte prvú X súradnicu: "))
y1 = int(input("Zadajte prvú Y súradnicu: "))
x2 = int(input("Zadajte druhú X súradnicu: "))
y2 = int(input("Zadajte druhú Y súradnicu: "))

print(same_color(x1, y1, x2, y2))