# Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
# +------+------+------+
# | col1 | col2 | col3 |
# +------+------+------+
# Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
# Maksymalna szerokość kolumny 10znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
# A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn :)


def draw_table():
    list_1 = input("Wpisz listę, oddzielając spacjami: ")
    list_1 = list_1.split(" ")
    num = len(list_1)
    upndown = "+" + "------------+" * num
    print(upndown)
    counter = 0
    for column in list_1:
        if len(list_1[counter]) <= 7 :
            print("|{:11.8s}".format(list_1[counter])+" ", end="")
            counter += 1
        else :
            print("|{:9.7s}".format(list_1[counter])+"...", end="")
            counter += 1
    print("|")
    print(upndown)


while True:
    try:
        draw_table()
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")
