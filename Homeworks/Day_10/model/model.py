import csv
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
        self.net_price = price - price * Book.vat

    def summary(self):
        print(self.id,"\n", self.name,"\n", self.author,"\n", self.number_of_pages)



class Ebook(Book):
    def __init__(self, id, name, price, amount, created_at, last_buy_at, author, number_of_pages, format):
        super().__init__(id, name, price, amount, created_at, last_buy_at, author, number_of_pages)
        self.format = format
        self.net_price = price - price * Book.vat


class Db():
    def __init__(self, csv_file):
        """
        read from file
        create book/ebook objects
        add to items as a dict of objects {id:item, id:item}
        """
        self.database = {}

        with open(csv_file, "r+", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            counter = 1
            for row in reader:
                if row["Typ"] == "Book":
                    object = Book(id=row["ID"], name=row["Nazwa"], price=20, amount=row["Ilość"],
                                        created_at=row["Data dodania"], last_buy_at=row["Data ostatniego zakupu"],
                                        author=row["Autor"], number_of_pages=row["Ilość stron"])
                    self.database.update({counter: object})
                    counter += 1
                elif row["Typ"] == "Ebook":
                    object = Ebook(id=row["ID"], name=row["Nazwa"], price=20, amount=row["Ilość"],
                                         created_at=row["Data dodania"], last_buy_at=row["Data ostatniego zakupu"],
                                         author=row["Autor"], number_of_pages=row["Ilość stron"], format=row["Format"])
                    self.database.update({counter: object})
                    counter += 1

    def addItem(self, object, file):
        """
        Function to add item in DB
        :param Book/Ebook object - object of book/ebook?
        """
        counter = len(self.database) + 1
        self.database.update({counter: object})
        with open (file, "a+", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(object)

    def getItems(self):
        """
        Function to get all items from db. Display a list of products
        """
        pass

    def removeItem(self, object):
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

class Cart():

    def __init__(self):
        self.elements = []
        self.elements_number = 0
        self.net = 0
        self.gross = 0

    def dodaj(self, element):
        self.elements.append(element)
        self.elements_number += 1
        # self.net += element.net_price
        # self.gross += element.price()

    def __len__(self):
        return len(self.elements)

    def cart_view(self):
        self.elements = dict(self.elements)
        return self.elements

    def net_worth(self):
        return self.net

    def gross_worth(self):
        return self.gross