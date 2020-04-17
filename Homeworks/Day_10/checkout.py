import Homeworks.Day_10.model.model as store
import csv

baza = store.Db("model/db.csv")
potop = baza.database[1]
krzyzacy = baza.database[2]
lotr = baza.database[3]

baza.addItem()



