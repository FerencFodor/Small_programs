# Vypočíta súčet čísel od 1 po n^2

def square_sum(n):
    s = 0
    for i in range(n):
        s = s + ((i + 1) ** 2)
    print(s)

x = int(input("Zadajte číslo:"))
square_sum(x)