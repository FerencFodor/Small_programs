# Zistí deliteľnosť čísel

def divisibility(a, b):
	'''
	Finds the divisibility of numbers
	
	a: dividend
	b: divider
	'''
	
	if d != 0:
		if a % b == 0:
			return True
		else:
			return False
	else:
		print("Nemôže sa deliť nulou")
		return False

a = int(input("Zadajte číslo: "))

for d in range(a+1)
	if divisibility(a, d):
		print(d)