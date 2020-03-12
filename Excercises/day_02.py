# komentarz jednolinijkowy robimy za pomocą znaku #
'''
Wielolinijkowy możemy zrobić przy użyciu trzech apostrofów
'''

# pobieranie danych od uzytkownika
imie = input("Jak masz na imie? ")
nazwisko = "Falkowicz"

# wyświeltanie danych na ekran (do konsoli)
print(imie)

# pamiętajmy że funkcja input ZAWSZE zwraca string
zmienna = input("Wpisz coś: ")
typ = type(zmienna) #funkcja type zwraca nam informację o typie zmiennej
print(typ)

# zmienne można próbować zamieniać na inne typy
int("456") # zmienia na int
float("6.6") # zmienia na float
float("Ala") # błąd - python nie wiem jaki ułamek odpowiada frazie "Ala"
str(12) # zmienia na string

# w Pythonie wszystko jest obiektem nawet string czyli posiada własne metody np. capitalize()
imie = 'ewa'
wynik_dzialania = imie.capitalize()
print(wynik_dzialania)

# w zależności od zapisu wartości nadajemy zmiennej odpowiedni typ
zmienna_typu_int = 123
zmienna_typu_float = 4.5
zmienna_typu_string = "16"

# nie wszystkie operacje matematyczne można robić na różnych typach
print(zmienna_typu_int * zmienna_typu_float) #ok - oba typy są numeryczne więc python wie co z nimi zrobić :)
print(zmienna_typu_string * zmienna_typu_float) #błąd

# stringi można dodawać (konkatenacja - łączenie) oraz mnożyć (przez wartość int)
zmienna_1 = "Ala"
zmienna_2 = " ma kota"
print(zmienna_1 + zmienna_2)
print(zmienna_1 * 10)

# istnieją znaki specjalne (whitespace) np \n \t
# należy uważać przy obsłudze takich znaków
sciezka_do_pliku = "c:\\documents\nowy folder\tatry" # może być błąd
print(sciezka_do_pliku)

sciezka_do_pliku = r"c:\\documents\nowy folder\tatry" # przedrostek "r"
print(sciezka_do_pliku)

sciezka_do_pliku = "c:\\\documents\\nowy folder\\tatry" # escapowanie za pomocą \ "r"
print(sciezka_do_pliku)


# mini kalkulator
wartosc_1 = input("Podaj liczbę: ")
wartosc_2 = input("Podaj liczbę: ")

liczba_1 = float(wartosc_1)
liczba_2 = float(wartosc_2)

print(liczba_1 + liczba_2)


# indeksacja stringów

# indeks: 012345678901
zdanie = "Ala ma kota."

ostatni_znak = zdanie[len(zdanie)-1]
ostatni_znak = zdanie[11]
ostatni_znak = zdanie[-1]

#instrukcje warunkowe
if ostatni_znak == '!':
    print('Nie krzycz na mnie')
elif ostatni_znak == '?': #bloki elif są niewymagane
    print('To jest dobre pytanie')
else: # blok else jest niewymagany
    print('Dzięki')


liczba_1 = float(input("Podaj pierwszą liczbę: "))
liczba_2 = float(input("Podaj drugą liczbę: "))

if liczba_1 > liczba_2:
  print("Pierwsza jest większa")
else:
  print("Druga chyba jest większa")
