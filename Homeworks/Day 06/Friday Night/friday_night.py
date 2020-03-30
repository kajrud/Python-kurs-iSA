# Program na podstawie odpowiedzi użytkownika na kilka pytań generuje dla niego sposób spędzenia piątkowego wieczoru
import random
import time
import Excercises.Moduly.friday_night as friny

print('''
Weekend już nadszedł, a Ty znowu nie umiesz zdecydować, co robić?
Pozwól, że Ci pomogę. Witaj w Generatorze Friday Night Fever!
''')
while True:
    try:
        where = input("Chcesz zostać w domu (D) czy wyjść do ludzi (L)? ")
        where = where.upper()
        if where == "D":
            print("Świetny wybór!")
            friny.introvert()
        elif where == "L":
            print("Na pewno? Skoro tak twierdzisz...")
            friny.extravert()
        else:
            print ("Coś poszło nie tak, zacznijmy od nowa")
            continue
        ans = input("Czy taki zestaw jest ok? Y/N ")
        ans = ans.upper()
        if ans == "Y":
            print("Miłego wieczoru!")
            break
        else:
            print("Zacznijmy zatem od nowa")
            continue

    except:
        print("Jesteś pewien, że dobrze odpowiadasz? :)")