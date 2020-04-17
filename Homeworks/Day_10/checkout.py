import Homeworks.Day_10.model as store
import csv

with open ("db.csv", "r+", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["ID"], row["Autor"])