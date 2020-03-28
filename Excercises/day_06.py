plik = open("test.txt", "r+") #r i r+ nie tworzą pliku, w, w+ i a owszem
python ustawia kursor: r/r+ na początku pliku; "a/a+" na końcu pliku
print(plik.tell())
print(plik.readline(), end = "") #w i w+ czyści plik! - tylko do tworzenia
print(plik.tell())
print(plik.readline(), end = "")
print(plik.tell())
print(plik.seek(5, 0))
#offset - o ile od whence chcesz zaczac; whence 0 - początek, 1 - tam, gdzie aktualnie jest,
# 2 - od końca, wtedy off z minusem, a plik tow w trybie binarnym
print(plik.readline(), end = "")
print(plik.tell())
plik.close()

import io

with open("test.txt", "r+") as plik:
    print(plik.tell())
    wszystkie_linie = plik.readlines()
    print(plik.tell())
    print(wszystkie_linie)
    try:
        plik.writelines(["\nnowa linia"])
    except io.UnsupportedOperation:
        print("Nie masz uprawnień do zapisu")
    print(plik.tell())

kursor NADPISUJE, jak insert

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

licznik()

