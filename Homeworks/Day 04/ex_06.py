import Excercises.Moduly.games as games
from random import randint

def menu (funkcje):
    print ("""
Witaj w Multitool Python Program by iSA - wersja beta ;)
Wybierz program który cię interesuje:
""")
    for index, funkcja in funkcje.items():
        print(f"Wybór: {index} - {funkcja['nazwa']}")

def rand():
    num = randint(1, 15)
    num = str(num)
    print(f"Wylosowano numer {num}")
    funkcje[num]()

def leave():
    print("Do zobaczenia!")
    exit()

funkcje = {"1" : {'nazwa': "Przeliczanie temperatury C -> F", 'call' : games.cel_to_fahr},
           "2" : {'nazwa': "Przeliczanie temperatury F -> C", 'call' : games.fahr_to_cel},
           "3" : {'nazwa': "Obliczanie pola koła", 'call' : games.disk_area},
           "4" : {'nazwa': "Podawanie pierwszej i ostatniej cyfry", 'call' : games.first_and_last},
           "5" : {'nazwa': "Rysowanie prostokąta", 'call' : games.draw_rectangle},
           "6" : {'nazwa': "Zamiana liczby binarnej na dziesiętną", 'call' : games.binary_to_decimal},
           "7" : {'nazwa': "Sprawdzenie czy liczba jest parzysta", 'call' : games.is_even},
           "8" : {'nazwa': "Sprawdzenie czy liczba jest podzielna przez 3, 5 lub 7", 'call' : games.is_divisible_or},
           "9" : {'nazwa': "Sprawdzenie czy liczba jest podzielna przez 3, 5 i 7", 'call' : games.is_divisible_and},
           "10" : {'nazwa': "Sprawdzenie czy rok jest przestępny", 'call' : games.leap_year},
           "11" : {'nazwa': "Rysowanie tabeli", 'call' : games.table_game},
           "12" : {'nazwa': "Rozmienianie kwoty na monety", 'call' : games.coins_game},
           "13" : {'nazwa': "Rysowanie piramidy", 'call' : games.pyramid_draw},
           "14" : {'nazwa': "Obliczanie wieku psa", 'call' : games.dog_game},
           "R" : {'nazwa': "Zaskocz mnie!", 'call' : rand},
           "X" : {'nazwa': "Wyjście z programu", 'call' : leave}
           "S" : {'nazwa': "Statystyka", 'call' : counter}
        }

menu(funkcje)
while True:
    try:
        num = input("Wprowadź numer (lub wpisz \"M\", aby wyświetlić menu): ")
        if num in funkcje.items():
            funkcje[num]["call"]()
        elif num == "M":
            menu(funkcje)
    except:
        print("Coś poszło nie tak, spróbuj jeszcze raz.")
