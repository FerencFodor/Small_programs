# Zistí či je číslo párne

def test_parity(n):
    if n % 2 == 0:
        return True
    if n % 2 != 0:
        return False

x = int(input("Zadajte číslo: "))
print(test_parity(x))