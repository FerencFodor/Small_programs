# Zistí či je pohyb dámy platný

def queen (x1, y1, x2, y2):
    '''
    Detects if the queen can make a legal move to a square with one move
    x1: Starting X coordinates
    y1: Starting Y coordinates
    x2: Ending X coordinates
    y2: Ending Y coordinates
    '''
    
    # Optional
    if 1 > x1 > 8 or 1 > y1 > 8 or 1 > x2 > 8 or 1 > y2 > 8:
		print("Zadali ste nesprávne hodnoty (1 > hodnota > 8 )!")
		return False
    
    if (abs(x1 - x2) == abs(y1 - y2)) or (abs(x1 - x2) != 0 and abs(y1 - y2) == 0) or (abs(x1 - x2) == 0 and abs(y1 - y2) != 0):
        return True
    else:
        return False
    
x1 = int(input("Zadajte prvú X súradnicu: "))
y1 = int(input("Zadajte prvú Y súradnicu: "))
x2 = int(input("Zadajte druhú X súradnicu: "))
y2 = int(input("Zadajte druhú Y súradnicu: "))

print(queen(x1, y1, x2, y2))