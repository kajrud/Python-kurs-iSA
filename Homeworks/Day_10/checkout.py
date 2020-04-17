import Homeworks.Day_10.model as store
import csv
database = store.Cart()
counter = 1
with open ("db.csv", "r+", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Typ"])
        if row ["Typ"] == "Book":
            object = store.Book(id=row["ID"], name=row["Nazwa"], price=20, amount=row["Ilość"],
                                created_at=row["Data dodania"], last_buy_at=row["Data ostatniego zakupu"],
                                author=row["Autor"], number_of_pages=row["Ilość stron"])
            print(object.name, "\n", object.author, "\n", object.last_buy_at, "\n", object.vat)
            database.dodaj({counter:object})
            counter += 1
        elif row ["Typ"] == "Ebook":
            object = store.Ebook(id=row["ID"], name=row["Nazwa"], price=20, amount=row["Ilość"],
                                created_at=row["Data dodania"], last_buy_at=row["Data ostatniego zakupu"],
                                author=row["Autor"], number_of_pages=row["Ilość stron"], format=row["Format"])
            print(object.name, "\n", object.author, "\n", object.last_buy_at, "\n", object.vat, "\n",
                  object.format)
            database.dodaj({counter: object})
            counter += 1

print(database.elements[1])



