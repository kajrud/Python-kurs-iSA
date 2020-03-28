# Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak, np:
# ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
# Niech będzie możliwość wyboru tryb case sensitivity.
# Niech program tworzy też plik ze statystyką swojej pracy.

import Excercises.Moduly.statistics as stat
with open("example.txt", "r") as plik:
    stat.count_lines(plik)
    stat.count_characters(plik)
    stat.count_words(plik)
    stat.count_a(plik)
    stat.is_upper(plik)
    stat.is_lower(plik)
    stat.count_num(plik)
    stat.count_anything(plik)
#
# with open("example.txt", "r") as plik:
#     all_lines = len(plik.readlines())
#     print(f"W pliku znajduje się {all_lines} linijek.")
#     all_characters = plik.read()
#     print(f"W pliku znajduje się {len(all_characters)} znaków.")


