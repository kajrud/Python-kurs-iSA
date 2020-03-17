# Napisz program do przeliczania stopni Celsjusza na Fahrenheita
while True:
    try:
        cel = float(input("Podaj temperaturę w stopniach Celsjusza: "))
        far = 32 + (9 / 5 * cel)
        print (f"W stopniach Fahrenheita to {far} stopni")
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")

# Napisz program do przeliczania stopni Fahrenheita na Celsjusza
while True:
    try:
        far = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
        cel = 5 / 9 * (far - 32)
        print(f"W stopniach Celsjusza to {cel} stopni")
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")

# Napisz program do obliczania pola powierzchni koła o zadanym promieniu
while True:
    try:
        radius = float(input("Podaj promień koła: "))
        pi = 3.14
        print("Pole powierzchni koła wynosi ", pi * radius ** 2)
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")

# Napisz program, który poda pierwszą i ostatnią cyfrę podanej liczby
while True:
    try:
        num = input("Podaj liczbę, im dłuższa tym lepsza: ")
        print(f"Pierwsza cyfra tej liczby to: {num[0]}")
        print(f"Ostatnia cyfra tej liczby to: {num[-1]}")
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")

# Napisz program , który rysuje prostokąt o zadanych rozmiarach (wysokość i szerokość) za pomocą znaków

while True:
    try:
        width = int(input("Podaj szerokosc:"))
        height = int(input("Podaj wysokość:"))
        print("+" + "-" * width + "+")
        for i in range(1, height + 1):
            print("|" + " " * width + "|")
        print("+" + "-" * width + "+")
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")

# Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1

while True:
    try:
        binar = input("Podaj liczbę w formacie binarnym (6 znaków): ")
        if len(binar) != 6:
            print("Nieprawidłowe dane, podaj 6 znaków.")
            continue
        new_binar = binar[::-1]
        all = 0
        counter = 1
        for x in new_binar:
            y = int(x)
            all = all + y * counter
            counter = counter * 2
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")
print (f"W systemie dziesiętnym to {all}.")

# Napisz program do rozpoznawania czy podane liczba jest parzysta czy nie

while True:
    try:
        num = int(input("Podaj liczbę całkowitą: "))
        if num % 2 == 0:
            print("Ta liczba jest parzysta")
        else:
            print("Ta liczba jest nieparzysta")
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")

# Napisz program do sprawdzania czy liczba jest podzielna przez 3 lub 5 lub 7

while True:
    try:
        num = float(input("Podaj liczbę: "))
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            print("Ta liczba jest podzielna przez 3, 5 lub 7")
        else:
            print("Ta liczba nie jest podzielna ani przez 3, ani przez 5, ani przez 7")
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")

# Napisz program do sprawdzania czy liczba jest podzielne przez 3 i 5 i 7

while True:
    try:
        num = float(input("Podaj liczbę: "))
        if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
            print("Ta liczba jest podzielna przez 3, 5 oraz 7")
        else:
            print("Ta liczba nie jest podzielna przez 3, 5 i 7")
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")

# Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

while True:
    try:
        year = input("Podaj rok: ")
        year_num = int(year)
        if year[-1:-3] == "00":
            if year_num % 400 == 0:
                print("Rok przestępny")
            else:
                print("Rok normalny")
        else:
            if year_num % 4 == 0:
                print("Rok przestępny")
            else:
                print("Rok normalny")
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")
