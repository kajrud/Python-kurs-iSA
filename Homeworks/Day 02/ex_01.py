#Napisz program do przeliczania stopni Celsjusza na Fahrenheita (wyświetlając wzór i kolejne obliczenia)

print("""Aby przeliczyć stopnie Celsjusza na stopnie Fahrenheita należy użyć wzoru:
T(far) = 32 + (9 / 5 * T(cel).
Ale od czego jest komputer...""")
cel = float(input("Podaj temperaturę w stopniach Celsjusza: "))
far = 32 + (9 / 5 * cel)
print ("W stopniach Fahrenheita to ", far, "stopni")