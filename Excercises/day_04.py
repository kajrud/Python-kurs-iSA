#typ referencyjny

lista = [1, 2, 3]
nowa_lista = lista
print(lista)
lista[0] = "jeden"
print(nowa_lista)
print(lista)

list = ["a", "b", "c"]
true_copy = list.copy()
print(list)
list[0] = "1"
print(true_copy)
print(list)

list_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
import copy
new_list = copy.deepcopy(list_2)
print (list_2[1][1])
list_2[1][1] = "x"
print (list_2[1][1])
print(new_list[1][1])

#tworzenie fukcji

def hej():
    print("Dzień dobry!")
hej()
hello = hej
print(hello) # funkcja też jest typem referencyjnym, niemutowalnym
hello()

def hej(imie = "Grażyn", nazwisko = "Polak"):
    # print("Dzień dobry", str(imie), "!")
    print(f"Dzień dobry {imie} {nazwisko}")
    # print("Dzień dobry {}{}".format(imie, nazwisko))

hej()
hej("Janusz")
hej(nazwisko = "Polak", imie = "Pjoter")

def dodaj(x, y):
    suma = float(x) + float(y)
    return suma

wynik = dodaj(2.5, "3")
print(wynik)