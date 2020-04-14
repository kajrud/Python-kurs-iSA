# type hints
def witaj(imie = "Kaja"):
    print(imie)

def witaj2(imie: str = "Kaja") -> str:
    print("Hej " + imie)

from typing import List

def witaj3(nazwisko: str, imie: str, wiek: int) -> List:
    return [imie, nazwisko, wiek]

# docstring - Pep 257

def witaj4(imie: str = "Kaja") -> None:
    """
    Funkcja wyswietla napis przywitalny #pierwsza linijka wyswietla co robi
    :param str imie: Imie z domyslna wartoscia 'Kaja' #rst opisujemy parametr, typ, nazwa, opis
    :return: Funkcja nic nie zwraca #podajemy co i dlaczego funkcja zwraca
    """
    print (f"Hello {imie}!")

print(witaj4.__doc__)

# pola klasy - zmienne definiowane na poziomie klasy, nie ma słowa self!
# metody klasy - metody, ktore jako pierwszy argument przyjmuja klasę
class Book():

    vat: float = 0.05 #rzecz niezależna od obiektu, wspólna dla całej klasy

    __marza = 10

    def __init__(self, author: str, tytul: str, price: int = 20):
        self.author = author
        self.tytul = tytul
        self.price = price
        self.__rating = 3.0

    def title(self):
        return self.tytul.capitalize()

    @classmethod
    def pan_tadeusz(cls):
        return cls("Adam Mickiewicz", "Pan Tadeusz")

    @classmethod
    def jaki_vat(cls):
        return cls.vat

    @staticmethod
    def count_sth(param_1, param_2): #nie mozna sie odwolac do self ani cls
        return param_1 + param_2

    @staticmethod
    def czy_promocja():
        pass
        #if Swiatowy dzien ksiaki == now:
        #print ("Promocja")


print(Book.vat)
object = Book('sienkiewicz', 'potop')
print(object.title())

obiekt = Book.pan_tadeusz()
print(obiekt.title())
import pprint
pprint.pprint(Book.__dict__)

print(Book._Book__marza)

class Tajny_agent():
    def __init__(self, imie, nazwisko):
        self.__imie: str = imie
        self.__nazwisko: str = nazwisko
        self.__zarobki: int = 9999

    @property
    def imie(self): #getter
        return self.__imie[0].capitalize() + "****"

    @imie.setter
    def imie(self, nowa_wartosc):
        self.__imie = nowa_wartosc

    @imie.deleter
    def imie(self):
        # nie usuwa wlasciwos
        #np zapis do log starej wartosci z self.__imie
        self.__imie = "  "

agent_1 = Tajny_agent("Zuzia", "Kwiatkowska")
print(agent_1.imie)
agent_1.imie = "Gabrysia"
print(agent_1.imie)
del(agent_1.imie)
print(agent_1.imie)

class Samochod():
    __marza = 0.1
    vat = 0.23

    def __init__(self, marka, kolor, net):
        self.marka = marka
        self.kolor = kolor
        self.net = net


    def gross_price(self):
        return self.net + self.net * self.vat

    @property
    def cena(self):
        return self.net + self.net * self.__marza + self.net * self.vat

    def podsumowanie(self):
        print(f"Kupiłeś {self.kolor} {self.marka}. Ostateczna cena to {self.cena}")

car = Samochod("Audi", "biały", 150000)
Samochod.podsumowanie(car)

