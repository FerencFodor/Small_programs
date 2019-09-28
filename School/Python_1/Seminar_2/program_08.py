# Vykreslí mriežku v konsole veľkosťi n * n 

def grid(n):
    for i in range(n):
        for j in range(n):
            print('+', end = ' ')   # Ak do print funkcie s pridá end, tak funkcia nezačne nový riadok
            for k in range(4):
                print('-', end = ' ')
        print('+')
        
        for side in range(4):
            for j in range(n):
                print(end = '|')
                for k in range(9):
                    print(end = ' ')
            print('|')
            
    for i in range(n):
        print('+', end = ' ')
        for j in range(4):
            print('-', end = ' ')
    print('+')
    
x = int(input("Zadajte veľkosť: "))
grid(x)