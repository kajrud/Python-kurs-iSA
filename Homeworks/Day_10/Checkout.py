class Cart():
    def __init__(self):
        self.elements = []
        self.elements_number = 0
        self.net = 0
        self.gross = 0

    def dodaj(self, element):
        self.elements.append(element)
        self.elements_number += 1
        self.net += element.net_price
        self.gross += element.gross_price()

    def __len__(self):
        return len(self.elements)

    def net_worth(self):
        return self.net

    def gross_worth(self):
        return self.gross

class Item():
    def __init__(self, id, name, price, amount, created_at, last_buy_at):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.created_at = created_at
        self.last_buy_at = last_buy_at


class Book(Item):
    def __init__(self, id, name, price, amount, created_at, last_buy_at, author, number_of_pages):
        super().__init__(id, name, price, amount, created_at, last_buy_at)
        self.author = author
        self.number_of_pages = number_of_pages
        self.vat = 0.05


class Ebook(Book):
    def __init__(self, id, name, price, amount, created_at, last_buy_at, author, number_of_pages, format):
        super().__init__(id, name, price, amount, created_at, last_buy_at, author, number_of_pages)
        self.format = format