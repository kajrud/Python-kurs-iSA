# __init__ - konstruktor, metoda niezależna od tego jaki obiekt tworzymy


class Ksiazka():
    def __init__(self, tytul, autor, ilosc_stron = 100, cena = 20):
        self.tytul = tytul
        self.ilosc_stron = ilosc_stron
        self.autor = autor
        self.cena = cena
        self.vat = 0.07

    def __str__(self):
        return f"{self.tytul}, autor: {self.autor}"

    def __len__(self):
        return self.ilosc_stron

    def __add__(self, other):
        if isinstance(other, Ksiazka):
            return self.ilosc_stron + other.ilosc_stron
        else:
            print("Tak naprawde nie dodaje nic")
            return self.ilosc_stron

    def cena_brutto(self):
        return round(self.cena + self.vat * self.cena, 2)


class Ebook(Ksiazka):
    def __init__(self, autor, tytul, cena):
        super().__init__(autor, tytul, cena)
        self.format = "pdf"
        self.vat = 0.23



class Koszyk():
    def __init__(self):
        self.elementy = []
        self.ilosc_elementow = 0
        self.netto = 0
        self.brutto = 0

    def dodaj(self, element):
        self.elementy.append(element)
        self.ilosc_elementow += 1
        self.netto += element.cena
        self.brutto += element.cena_brutto()

    def __len__(self):
        return len(self.elementy)

    def wartosc_netto(self):
        return self.netto

    def wartosc_brutto(self):
        return self.brutto


koszyk = Koszyk()
book = Ksiazka("Harry Potter", 'Zuzia sasiadka', 150, 20)
book2 = Ksiazka("Lew zbigniew", "Kuba", 3, 15.53)
ebook1 = Ebook("Władca pierogów", "Muffin", 3)
koszyk.dodaj(book)
koszyk.dodaj(book2)
koszyk.dodaj(ebook1)

print(koszyk.elementy)
print (len(koszyk))
print(f"Wartość netto: {koszyk.wartosc_netto()}")
print(f"Wartość netto: {koszyk.wartosc_brutto()}")

class Rodzic():
    pass

class Dziecko(Rodzic):
    pass

class Zwierze():
    pass
class Czlowiek(Zwierze):
    pass
class Student(Czlowiek):
    pass
class Kot(Zwierze):
    pass
class Pies(Zwierze):
    pass
class Bokser(Pies):
    pass
class Jamnik(Pies):
    pass

print(isinstance(book, Ksiazka))
print(issubclass(Bokser, Pies))


dziedziczenie metod
class Zwierze():
    def hej(self):
        print("WAT")

class Czlowiek(Zwierze):
    def hej(self):
        print("Siema jestem czlowiek")

class Student(Czlowiek):
    def hej(self):
        print("Daj na piwo")

class Profesor(Czlowiek):

    def hej(self):
        print("Witam państwa")

    def inna(self):
        print("Inne przywitanie")

zwierze = Zwierze()
zwierze.hej()

prof = Profesor()
prof.inna()

# dziedziczenie po dwóch rodzicach

class B():
    def hej(self):
        print("Jestem B")

class C():
    def hej(self):
        print("Jestem C")

class D(B, C):
    pass
    # def hej(self):
    #     print("Jestem D")

obiekt_D = D()
print(isinstance(obiekt_D, B))