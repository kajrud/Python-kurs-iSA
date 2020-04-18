import Homeworks.Day_10.model.model as store

baza = store.Db("model/db.csv")
potop = baza.database[1]
krzyzacy = baza.database[2]
lotr = baza.database[3]

cart = store.Cart()
print(cart.elements)

baza.getItems()