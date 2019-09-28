# Vypíše čísla od n po 0

def decrease(n):
    for i in range(n,0,-1):
        print(i)

x = int(input("Zadajte číslo:"))
decrease(x)