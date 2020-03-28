def cel_to_fahr():
    while True:
        try:
            cel = float(input("Podaj temperaturę w stopniach Celsjusza: "))
            far = 32 + (9 / 5 * cel)
            print(f"W stopniach Fahrenheita to {far} stopni")
            break
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

def fahr_to_cel():
    while True:
        try:
            far = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
            cel = 5 / 9 * (far - 32)
            print(f"W stopniach Celsjusza to {cel} stopni")
            break
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

def disk_area():
    while True:
        try:
            radius = float(input("Podaj promień koła: "))
            pi = 3.14
            print("Pole powierzchni koła wynosi ", pi * radius ** 2)
            break
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

def first_and_last():
    while True:
        try:
            num = input("Podaj liczbę, im dłuższa tym lepsza: ")
            print(f"Pierwsza cyfra tej liczby to: {num[0]}")
            print(f"Ostatnia cyfra tej liczby to: {num[-1]}")
            break
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

def draw_rectangle():
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

def binary_to_decimal():
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
    print(f"W systemie dziesiętnym to {all}.")

def is_even():
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

def is_divisible_or():
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

def is_divisible_and():
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

def leap_year():
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

def table_game():
    def draw_table():
        list_1 = input("Wpisz listę, oddzielając spacjami: ")
        list_1 = list_1.split(" ")
        num = len(list_1)
        upndown = "+" + "------------+" * num
        print(upndown)
        counter = 0
        for column in list_1:
            if len(list_1[counter]) <= 7:
                print("|{:11.8s}".format(list_1[counter]) + " ", end="")
                counter += 1
            else:
                print("|{:9.7s}".format(list_1[counter]) + "...", end="")
                counter += 1
        print("|")
        print(upndown)

    while True:
        try:
            draw_table()
            break
        except ValueError:
            print("Nieprawidłowe dane, zacznij jeszcze raz.")

def coins_game():
    def coins_change():
        money = (float(input("Podaj kwotę, którą chcesz rozmienić: "))) * 100
        div_list = (500, 200, 100, 50, 20, 10, 5, 2, 1)
        while money >= 1:
            for i in div_list:
                num = int(money / i)
                print(f"{num} monet {i / 100} zł.")
                money = money - num * i

    while True:
        try:
            coins_change()
            break
        except ValueError:
            print("Nieprawidłowe dane, zacznij jeszcze raz.")

def pyramid_draw():
    while True:
        try:
            num = int(input("Podaj wysokość piramidy: "))
            for i in range(0, num + 1):
                stage = (f"#" * i)
                new_stage = stage.center(num)
                print(new_stage)
            break
        except ValueError:
            print("Nieprawidłowe dane. Podaj liczbę.")

def dog_game():
    def dog_age_count():
        dog_age = int(input("Podaj wiek psa: "))
        if dog_age <= 2:
            dog_age = dog_age * 10.5
            print(f"Wiek psa to: {dog_age}.")
        if dog_age > 2:
            dog_age = 21 + (dog_age - 2) * 4
            print(f"Wiek psa to: {dog_age}.")

    while True:
        try:
            dog_age_count()
            break
        except ValueError:
            print("Nieprawidłowe dane, zacznij jeszcze raz.")

def licznik():
    try:
        with open('licznik.txt', 'r+') as licznik:
            current = licznik.readline()
            try:
                current = int(current)
                current += 1
            except:
                current = 1
            current = str(current)
            licznik.seek(0)
            licznik.write(current)
            print("Plik został otwarty po raz " + current)
    except FileNotFoundError:
        with open('licznik.txt.','w') as licznik:
            licznik.write("1")
            print("Plik został otwarty po raz pierwszy!")