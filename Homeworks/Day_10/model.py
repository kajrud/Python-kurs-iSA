class Cart():
    """

    """
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
    """

    """
    def __init__(self, id, name, price, amount, created_at, last_buy_at):
        self.id = id
        self.name = name
        self.price = price
        self.amount = amount
        self.created_at = created_at
        self.last_buy_at = last_buy_at


class Book(Item):
    """

    """
    vat = 0.05
    def __init__(self, id, name, price, amount, created_at, last_buy_at, author, number_of_pages):
        super().__init__(id, name, price, amount, created_at, last_buy_at)
        self.author = author
        self.number_of_pages = number_of_pages

    def summary(self):
        print(self.id,"\n", self.name,"\n", self.author,"\n", self.number_of_pages)



class Ebook(Book):
    def __init__(self, id, name, price, amount, created_at, last_buy_at, author, number_of_pages, format):
        super().__init__(id, name, price, amount, created_at, last_buy_at, author, number_of_pages)
        self.format = format


class Db():
    def __init__(self, file):
        """
        for example:

        read from file
        create book/ebook objects
        add to items as a dict of objects {id:item, id:item}
        """
        pass

    def addItem(self, object):
        """
        Function to add item in DB
        :param Book/Ebook object - object of book/ebook?
        """
        pass

    def getItems(self):
        """
        Function to get all items from db. Display a list of products
        """
        pass

    def removeItem(self):
        """
        Function to get remove item from DB
        :param int id - id of book?
        """
        pass

    def updateItem(self):
        """
        Function to updete item in DB
        :param Book/Ebook object - object of book/ebook?
        """
        pass