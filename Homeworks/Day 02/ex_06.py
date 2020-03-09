# Napisz do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.
# Załóż że wpisywane jest zawsze tylko 6 znaków 0/1

binar = input("Podaj liczbę w formacie binarnym (6 znaków): ")
last = int(binar[-1]) * 1
pre1 = int(binar[-2]) * 2
pre2 = int(binar[-3]) * 4
pre3 = int(binar[-4]) * 8
pre4 = int(binar[-5]) * 16
first = int(binar[-6]) * 32
print (first + pre4 + pre3 + pre2 + pre1 + last)
