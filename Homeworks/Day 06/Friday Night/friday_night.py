# Program na podstawie odpowiedzi użytkownika na kilka pytań generuje dla niego sposób spędzenia piątkowego wieczoru
import random
import Excercises.Moduly.friday_night as frinig
print('''
Weekend już nadszedł, a Ty znowu nie umiesz zdecydować, co robić?
Pozwól, że Ci pomogę. Witaj w Generatorze Friday Night Fever!
''')
where = input("Chcesz zostać w domu (D) czy wyjść do ludzi (L)? ")
where = where.upper()

while True:
    if where == "D":
        print("Świetny wybór!")
        while True:
            act = input("Chcesz obejrzeć film (F) czy zagrać w grę (G)? ")
            act = act.upper()
            if act == "F":
                movie = (random.choice(list(open("movies.txt"))))
                movie = movie.replace("\n", "")
                print(f"Wylosowałem dla Ciebie film {movie}.")
                break
            elif act == "G":
                game = (random.choice(list(open("games.txt"))))
                game = game.replace("\n", "")
                print(f"Wylosowałem dla Ciebie grę {game}.")
                break
            else:
                print("Coś poszło nie tak. Zacznijmy jeszcze raz.")
                continue
        food = (random.choice(list(open("food.txt"))))
        food = food.replace("\n", "")
        print(f"Myślę, że {food} to dobry wybór na dziś, jeśli chodzi o jedzenie.")
        break
