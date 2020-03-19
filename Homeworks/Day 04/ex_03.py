# Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.

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
