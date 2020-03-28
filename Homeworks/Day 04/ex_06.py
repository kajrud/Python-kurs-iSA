import Excercises.Moduly.games as games
from random import randint

def rand():
    wybor = randint(1, 15)
    wybor = str(wybor)
    print(f"Wylosowano numer {wybor}")
    programy[wybor]['call']()

def leave():
    print("Do zobaczenia!")
    exit()


def menu(programy):
    print('MultiTOOL\nMenu:')

    for key, program in programy.items():
        print(f'{key} - {program["nazwa"]}')

    return input('Który program uruchomić? ').upper()

programy = {
           "1" : {'nazwa': "Przeliczanie temperatury C -> F", 'call' : games.cel_to_fahr},
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
           "X" : {'nazwa': "Wyjście z programu", 'call' : leave},
           "S" : {'nazwa': "Statystyka", 'call' : games.counter}
}
wybor = None

while wybor != 'X':
    wybor = menu(programy)

    try:
        print('=' * 20)
        programy[wybor]['call']()
        print('=' * 20)
    except KeyError:
        print('Taki program nie isnieje')