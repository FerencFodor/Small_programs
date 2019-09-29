# Zistí deliteľnosť čísel a otestuje provčíselnosť

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

def prime (a, a_max):
    '''
    Prints out all the prime nubers in a range
    
    a: starting prime number (lowest is 2)
    max_a: end of the range
    '''
    
    count = 0
    for i in range(a, a_max + 1):
        for d in range(i + 1):
            if divisibility(i, d):
                count += 1
        if count == 2:
            print(i)
        else:
            count = 0

prime(2, int(input("Zadajte číslo: ")))

