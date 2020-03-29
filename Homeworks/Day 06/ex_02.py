# Stwórz program który przyjmie w parametrze ścieżkę do dowolnego pliku (CSV lub Excel - jaki wolicie), który będzie zawierał dane tabelaryczne.
#    W pliku pierwszy wiersz będzie zawierał nazwy kolumn a pozostałe wiersze dane.

import openpyxl
# excel = openpyxl.Workbook()
# excel.save("tabela_danych.xlsx")

nazwa_pliku = "tabela_danych.xlsx"
excel = openpyxl.load_workbook(nazwa_pliku)
arkusz = excel.active


row = 1
column = 1
column_counter = 0
while True:
    cell = arkusz.cell(row, column)
    if cell.value != None:
        column_counter += 1
        column +=1
    else:
        break
print(column_counter)

row_counter = 0
row = 1
column = 1
while True:
    cell = arkusz.cell(row, column)
    if cell.value != None:
        row_counter += 1
        row +=1
    else:
        break
print(row_counter)
for row in arkusz.iter_rows(min_row=1, max_col=column_counter, max_row=row_counter, values_only=True):
    num = len(row)
    upndown = "+" + "------------+" * num
    print(upndown)
    counter = 0
    for column in row:
        data = (row[counter])
        data = str(data)
        if len(data) <= 7:
            print("|{:11.8s}".format(data) + " ", end="")
            counter += 1
        else:
            print("|{:9.7s}".format(data) + "...", end="")
            counter += 1
    print("|")
print(upndown)
