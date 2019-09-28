import turtle

# Vypočíta odmocninu cisla pomocou turtle grafiky

def odmocnina(n):
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	for i in range (n-1):
		rot = turtle.towards(0, 0)	# vypočíta uhol na ktorý sa má natočiť na bod 0,0
		dist = turtle.distance(0, 0)	# vypočíta vzdialenosť od bodu 0,0
		turtle.setheading(rot)		# natočí 'koritnačku' podla uhlu daným premennou rot
		turtle.forward(dist)		# posunie 'koritnačku' podla vzdialenosti daným premonnou dist
		turtle.backward(dist)
		turtle.right(90)
		turtle.forward(100)
	print("%.2f" % (dist/100))		# Kvôli grafickéhu znázorneniu je potrebné výsledok vydeliť 100

odmocnina(6)					#Volanie funkcie
