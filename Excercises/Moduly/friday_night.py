import random
import time

def introvert():
    while True:
        act = input("Chcesz obejrzeć film (F) czy zagrać w grę (G)? ")
        act = act.upper()
        if act == "F":
            movie = (random.choice(list(open("movies.txt"))))
            movie = movie.replace("\n", "")
            time.sleep(5)
            print(f"Wylosowałem dla Ciebie film {movie}.")
            break
        elif act == "G":
            game = (random.choice(list(open("games.txt"))))
            game = game.replace("\n", "")
            time.sleep(5)
            print(f"Wylosowałem dla Ciebie grę {game}.")
            break
        else:
            print("Coś poszło nie tak. Zacznijmy jeszcze raz.")
            continue
    time.sleep(5)
    food = (random.choice(list(open("food.txt"))))
    food = food.replace("\n", "")
    print(f"Myślę, że {food} to dobry wybór na dziś, jeśli chodzi o jedzenie.")

    time.sleep(5)
    excuses = (random.choice(list(open("excuses.txt"))))
    excuses = excuses.replace("\n", "")
    print(
        f"A jakby znajomi się pytali, czy chcesz gdzieś iść, to powiedz, że nie możesz. '{excuses}' i niech idą sami.")

def extravert():
    act = (random.choice(list(open("activities.txt"))))
    act = act.replace("\n", "")
    food = (random.choice(list(open("food.txt"))))
    food = food.replace("\n", "")
    friends = random.randint(1, 15)
    time.sleep(7)
    print(f"Skoro taka jest Twoja decyzja, to zadzwoń do {friends} znajomych, idźcie na {act}, "
          f"a potem szef kuchni poleca danie wieczoru - {food}.")



