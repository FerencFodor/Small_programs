import turtle

# Vykresli 'diamant' pomocou funkcii a turtle grafiky

def cyklus_1():
	for i in range(5):
		turtle.forward(20)
		turtle.left(90)
		turtle.forward(20)
		turtle.right(90)
		
		
def cyklus_2():
	for j in range(6):
		turtle.forward(20)
		turtle.right(90)
		turtle.forward(20)
		turtle.left(90)


cyklus_1()
cyklus_2()
turtle.right(180)
cyklus_1()
cyklus_2()