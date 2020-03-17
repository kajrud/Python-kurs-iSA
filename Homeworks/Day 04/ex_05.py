# Kalkulator do wyliczania wieku psa.
# Przez pierwsze dwa lata, każdy psi rok to 10,5 ludzkiego roku, przez reszte lat psi rok to 4 ludzkie lata

def dog_age_count():
    dog_age = int(input("Podaj wiek psa: "))
    if dog_age <= 2:
        dog_age = dog_age * 10.5
        print(f"Wiek psa to: {dog_age}.")
    if dog_age > 2:
        dog_age = 21 + (dog_age - 2) * 4
        print (f"Wiek psa to: {dog_age}.")

while True:
    try:
        dog_age_count()
        break
    except ValueError:
        print("Nieprawidłowe dane, zacznij jeszcze raz.")
