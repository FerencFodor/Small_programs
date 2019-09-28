# Vypíše párne čísla od 2 po n * 2

def even(n):
    for i in range(n):
        print((i + 1) * 2)

x = int(input("Zadajte číslo:"))
even(x)