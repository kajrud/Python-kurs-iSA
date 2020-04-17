import Homeworks.Day_10.model.model as store
import csv
import pprint

baza = store.Db("model/db.csv")
potop = baza.database[1]
krzyzacy = baza.database[2]
lotr = baza.database[3]
harry_potter = store.Ebook(id="4", name="Harry Potter", price = 20, amount = "unlimited", created_at = "2020-04-20",
                           last_buy_at="2020-04-20", author="JKRowling", number_of_pages=330, format="mobi")
baza.addItem(harry_potter, "db.csv")
pprint.pprint(baza.database)



