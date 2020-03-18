# escapowanie dodatkowych znaków specjalnych
# Książka pt: "Kto w butach".

tytul = "Książka pt: \"Kto w butach\"." #backslah dla " jeśli używamy dla stringów "
tytul = 'Książka pt: "Kto w butach".'
tytul = "I'm"
tytul = 'I\'m'
print(tytul)

liczba = 2.3
liczba_2 = 4656

# formatowanie stringów
# print('Wprowadziłeś liczbę: ' + str(liczba))
# już nie używajmy + do konkatenacji, format jest wygodniejszy i bezpieczniejszy

# nie trzeba już rzutować np intów na stringi
print(f'Wprowadziłeś liczbę: {liczba}. '
      f'Dzięki jeszcze raz za liczbę {liczba}')

print('Wprowadziłeś liczbę: {} {a} {a}'.format(liczba, a=liczba_2))

# typ danych range()
# bardzo wydajna sekwencja liczby, działająca na zasadzie lazy-loading
# czyli kolejna wartość jest pobierana/wyliczana dopiero gdy jest potrzebna
# przez co obiekt nie zajmuje dużo pamięci
zestaw_liczb = range(1,10000000)
print(zestaw_liczb)

# typ danych list()
lista = [1,2,3,4,5,6,7,9,10] # za pomocą [] - podajemy kolejne elemnty listy
print(lista)

lista_2 = list('dwa') # za pomocą list() - podajemy JEDEN iterowany typ danych
print(lista_2)

# listy możemy modyfikować:
lista_3 = ['zero', 1, 'trzeci', 'dom']
print(lista_3)
lista_3[1] = 'jeden' #aktualizacja
print(lista_3)
lista_3.append('nowy element') #dodawania
print(lista_3)
del(lista_3[1]) #kasowanie elementu po indeksie
print(lista_3)
lista_3.remove('dom') #kasowanie elementu po wartości
print(lista_3)

# sprawdzanie czy lista zawiera jakiś element
if 'dom' in lista_3:
    lista_3.remove('dom')
else:
    print('Brak elementu do skasowania')


# zamieniając range na listę zajmujemy duży obszar pamięci. Można ale nie warto :)
lista_4 = list(range(0, 10000000))
print(lista_4)

# typ danych tuple - krotka - niemutowalny czyli niezmienialny
krotka = ("jeden", "dwa", "trzy")
print(krotka)
print(type(krotka))
print(len(krotka))
print(krotka[0])

# pętla while
# pamiętajmy że w while musimy dać szansę zmiany warunku logicznego

czy_kontynuowac = 'T'
while czy_kontynuowac == 'T':
    print('.')
    czy_kontynuowac = input('Czy kontynuopwać [T/N]? ')

# nieskończona pętla
while True:
    print('Nigdy się nie skończę :)')

# pętla z licznikiem
licznik = 0
while licznik < 10:
    licznik += 1
    if licznik in [5,8]:
        break # przerywa pętlę
        #continue # przeskakuje iterację

    print(licznik)

# pętla for do iterowania po zbiorach i obiektach iterowanych
zdanie = "Ala!" # można iterować stringa
for litera in zdanie:
    # omijanie literek a/A
    #if litera in ['a', 'A']:
    #    continue
    print(litera)

# iteracja po elementach listy i sumowanie ich rozmiarów
lista = ['jeden', 'dwa', 'dom']
calkowity_rozmiar = 0

for element in lista:
    rozmiar_elementu = len(element)
    calkowity_rozmiar += rozmiar_elementu

print(calkowity_rozmiar)
print('Koniec')

for i in range(0,1000000):
    print(i)