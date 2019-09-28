import turtle

#Calculates the square root of the number using turtle graphics

def odmocnina(n):
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(100)
	for i in range (n-1):
		rot = turtle.towards(0, 0)
		dist = turtle.distance(0, 0)
		turtle.setheading(rot)
		turtle.forward(dist)
		turtle.backward(dist)
		turtle.right(90)
		turtle.forward(100)
	print("%.2f" % (dist/100))

odmocnina(6)
