# Program rysujący piramidę o określonej wysokości

while True:
    try:
        num = int(input("Podaj wysokość piramidy: "))
        for i in range(0, num + 1):
            stage = (f"#" * i)
            new_stage = stage.center(num)
            print(new_stage)
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")