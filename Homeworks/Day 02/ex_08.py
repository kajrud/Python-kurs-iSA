# Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

num = float(input("Podaj liczbę: "))
if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("Ta liczba jest podzielna przez 3, 5 lub 7")
else:
    print("Ta liczba nie jest podzielna ani przez 3, ani przez 5, ani przez 7")