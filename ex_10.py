# Napisz program do sprawdzania czy podany rok jest rokiem przestępnym

year = input("Podaj rok: ")
year_num = int(year)
if year[-1:-3] == "00":
    if year_num % 400 == 0:
        print("Rok przestępny")
    else:
        print("Rok normalny")
else:
    if year_num % 4 == 0:
        print ("Rok przestępny")
    else:
        print("Rok normalny")
