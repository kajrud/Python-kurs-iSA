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