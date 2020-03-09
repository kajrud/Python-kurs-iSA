upndown = int(input("Podaj szerokość: "))
sides = int(input("Podaj wysokość: "))
body = "|" + (" " * upndown) + "|"
print("+", "-" * upndown, "+")
print(body * sides)
print("+", "-" * upndown, "+")