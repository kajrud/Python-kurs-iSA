def count_lines(plik):
    with open("example.txt", "r") as plik:
        all_lines = len(plik.readlines())
        print(f"W pliku znajduje się {all_lines} linijek.")

def count_characters(plik):
    with open("example.txt", "r") as plik:
        all_characters = plik.read()
        print(f"W pliku znajduje się {len(all_characters)} znaków.")

def count_words(plik):
    with open("example.txt", "r") as plik:
        all_words = plik.read()
        all_words = all_words.replace("-", "")
        all_words = all_words.split()
        print(f"W pliku znajduje się {len(all_words)} słów.")

def is_upper(plik):
    with open("example.txt", "r") as plik:
        counter = 0
        all_words = plik.read()
        for letter in all_words:
            if letter.isupper() is True:
                counter += 1
            else:
                continue
        print(f"W pliku występuje {counter} dużych liter.")

def is_lower(plik):
    with open("example.txt", "r") as plik:
        counter = 0
        all_words = plik.read()
        for letter in all_words:
            if letter.islower() is True:
                counter += 1
            else:
                continue
        print(f"W pliku występuje {counter} małych liter.")

def count_num(plik):
    with open("example.txt", "r") as plik:
        counter = 0
        all_words = plik.read()
        for letter in all_words:
            if letter.isnumeric() is True:
                counter += 1
            else:
                continue
        print(f"W pliku występuje {counter} cyfr.")

def count_runs(plik):
    pass

def count_a(plik):
    with open("example.txt", "r") as plik:
        counter = 0
        all_words = plik.read()
        for letter in all_words:
            if letter == "a":
                counter += 1
            else:
                continue
        print(f"W pliku występuje {counter} liter 'a'.")

def count_anything(plik):
    with open("example.txt", "r") as plik:
        counter = 0
        all_words = plik.read()
        anything = input("Czego szukasz? ")
        for letter in all_words:
            if letter == anything:
                counter += 1
            else:
                continue
        print(f"W pliku występuje {counter} poszukiwanych znaków.")
