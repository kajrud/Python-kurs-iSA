# Napisz program do przeliczania stopni Fahrenheita na Celsjusza (wyświetlając wzór i kolejne obliczenia)

print("""Aby przeliczyć stopnie Fahrenheita na stopnie Celsjusza należy użyć wzoru:
T(cel) = 5 / 9 *(T(fah) - 32).
Ale od czego jest komputer...""")
far = float(input("Podaj temperaturę w stopniach Fahrenheita: "))
cel = 5 / 9 * (far - 32)
print ("W stopniach Celsjusza to ", cel, "stopni")