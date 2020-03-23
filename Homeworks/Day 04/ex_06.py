import Excercises.Moduły.games as games
from random import randint
print("""
Witaj w Multitool Python Program by iSA - wersja beta ;)
Wybierz program który cię interesuje:
1. Przeliczanie temperatury C -> F
2. Przeliczanie temperatury F -> C
3. Obliczanie pola koła
4. Podawanie pierwszej i ostatniej cyfry
5. Rysowanie prostokąta
6. Zamiana liczby binarnej na dziesiętną
7. Sprawdzenie czy liczba jest parzysta
8. Sprawdzenie czy liczba jest podzielna przez 3, 5 lub 7
9. Sprawdzenie czy liczba jest podzielna przez 3, 5 i 7
10. Sprawdzenie czy rok jest przestępny
11. Rysowanie tabeli
12. Rozmienianie kwoty na monety
13. Rysowanie piramidy
14. Obliczanie wieku psa
R. Zaskocz mnie!
X. Wyjście z programu""")

def multitool():
    if num == "1":
        games.cel_to_fahr()
    elif num == "2":
        games.fahr_to_cel()
    elif num == "3":
        games.disk_area()
    elif num == "4":
        games.first_and_last()
    elif num == "5":
        games.draw_rectangle()
    elif num == "6":
        games.binary_to_decimal()
    elif num == "7":
        games.is_even()
    elif num == "8":
        games.is_divisible_or()
    elif num == "9":
        games.is_divisible_and()
    elif num == "10":
        games.leap_year()
    elif num == "11":
        games.table_game()
    elif num == "12":
        games.coins_game()
    elif num == "13":
        games.pyramid_draw()
    elif num == "14":
        games.dog_game()
num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
while True:
    try:
        num = input("Wprowadź numer: ")
        if num in num_list:
            multitool()
        elif num == "R" :
            num = random.randint(1, 15)
            num = str(num)
            multitool()
        elif num == "X":
            break
    except:
        print("Coś poszło nie tak, spróbuj jeszcze raz.")