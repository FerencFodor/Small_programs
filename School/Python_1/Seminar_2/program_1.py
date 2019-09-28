# Vypočíta tretiu mocninu čísla

def cubed(a):
    a = a * a * a
    return a

num = int(input("Zadaj číslo: "))
print(cubed(num))