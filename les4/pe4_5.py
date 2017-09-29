def kwadraten_som(grondgetallen):
    positiefgetal = []
    for getal in grondgetallen:
        if getal >0:
            positiefgetal.append(getal**2)
    return sum(positiefgetal)
print(kwadraten_som([4, 5, 3, -81]))

