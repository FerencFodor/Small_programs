# Vypíše čísla od 101 po 100 + n

def over_100(n):
    for i in range(n):
        print(100 + (i + 1))

x = int(input("Zadajte číslo:"))
over_100(x)