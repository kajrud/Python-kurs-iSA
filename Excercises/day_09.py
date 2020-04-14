class Auto(object):
    def __init__(self, marka = "BMW", kolor_id = 0, price = 100000):
        kolory = ("bialy", "czerwony", "różowy")
        print("Auto")
        self.marka = marka
        self.kolor = kolory[kolor_id]
        self.price = price

auto = Auto("BMW", 2, "150")
print(auto.kolor)