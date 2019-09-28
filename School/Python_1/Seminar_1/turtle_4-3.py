import turtle

# Vykresli obrázok s 5-uholníkmi pomocou funkcie a turtle grafikou

def pentagon():
	for i in range(5):
		turtle.forward(100)
		turtle.left(72)

for j in range(10):
	pentagon()
	turtle.left(36)