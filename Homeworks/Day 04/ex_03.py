# Program przyjmuje kwotę w parametrze i wylicza jak rozmienić to na monety: 5, 2, 1, 0.5, 0.2, 0.1 wydając ich jak najmniej.

def coins_change():
    money = float(input("Podaj kwotę, którą chcesz rozmienić: "))
    div_list = (5, 2, 1, 0.5, 0.2, 0.1)
    while money > 0:
        for i in div_list:
            num = int(money / i)
            print(f"{num} monet {i} zł.")
            money = money - num * i

while True:
    try:
        coins_change()
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")
