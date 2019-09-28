import turtle

# Vykreslí obrázok s 12-uhloníkmi pomocou funkcie a turtle grafikou

def dodecagon():
    for i in range(12):
        turtle.forward(50)
        turtle.left(30)

for j in range(12):
    dodecagon()
    turtle.left(30)