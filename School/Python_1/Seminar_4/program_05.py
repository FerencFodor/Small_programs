import turtle

turtle = turtle.Turtle()

def menu(t, _string):
	if _string == 's':
		for i in range(4):
			t.fd(100)
			t.left(90)
	elif _string == 't':
		for i in range(3):
			t.fd(100)
			t.left(120)
	else:
		print("Zadali ste neplatný vstup!")
		
n = 1

while n == 1:
	print("Obsah menu:\ns - Štvorec\nt - Trojuholník")
	_string = input("Zadajte vstup do menu: ")
	
    turtle.clear()      # Vyčistí výkres
	
    menu(turtle, _string)
	
	_restart = input("Chcete pokračovať? (Y/N): ")
	if _restart == 'y' or _restart == 'Y':
		n = 1
	elif _restart == 'n' or _restart == 'N':
		n = 0
	else:
		print("Nesprávny vstup. program sa ukončí")
		n = 0