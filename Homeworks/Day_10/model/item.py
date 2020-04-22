import Homeworks.Day_10.model.model as store

book1 = store.Book("1", "Harry Potter", 20, 300, "2020-04-20", "2020-04-20", "Rowling", 250)
print(book1)

cart = store.Cart()
cart.dodaj(book1)
print(cart)