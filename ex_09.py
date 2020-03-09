# Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

num = float(input("Podaj liczbę: "))
if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
    print("Ta liczba jest podzielna przez 3, 5 oraz 7")
else:
    print("Ta liczba nie jest podzielna przez 3, 5 i 7")