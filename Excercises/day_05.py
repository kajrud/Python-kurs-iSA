wiersze = [
    {'imie': 'Łukasz', 'naziwsko': 'Falkowicz'},
    {'imie': 'Adam', 'naziwsko': 'Falkowicz'},
    {'imie': 'Jan', 'naziwsko': 'Falkowicz'},
]

for slownik in wiersze:
    #for klucz, wartosc in slownik.items():
    #   if klucz == 'imie':
    #        print(f'Mam na imie {wartosc}')
    print(f"mam na imie {slownik['imie'], slownik['naziwsko']}")

dict = {'name' : 'Kaja', 0 : "zero", '0' : 'inne zero'} # klucz jest sprawdzany typem, tylko niemutowalne! i treścią
print(dict['name'])
print(dict[0])
print(dict['0'])

try:
    print("Dzielenie")
    list = []
    list[10]
    wynik = 15 / 0
    print(wynik)
except ZeroDivisionError:
    print("Nie dziel przez 0")
except:
    print("Coś poszło nie tak")
else:
    print("Bezbłędnie")
finally:
    print("Always")

try:
    wynik = 15 / 0
except Exception as e:
#     print(str(e))

value = input("Podaj liczbe ")
try:
    value = value.replace(",", ".")
    num = float(value)
except:
    print("To nie jest liczba")

#moduły

import Moduły.witacz as hello
hello.dzien_dobry()
hello.hej()

from Moduły.witacz import hej

hej()

import Moduły.validator

Moduły.validator.is_num(15)