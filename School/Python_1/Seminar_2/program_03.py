# Vypíše čísla od 1 po n 

def sucet(n):
    for i in range(n):
        print(i + 1)

x = int(input("Zadaj číslo: "))
sucet(x)