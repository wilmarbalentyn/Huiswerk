#functie schrijven
#input om een zin op te schrijven
#gemiddelde lengte van zin berekenen
#print de lengte
#bereken hoeveel letters in de zin zitten dan delen door aantal woorden.


def gemiddelde():
    zin = str(input('Voor jouw zin in: '))
    splits = zin.split(sep=' ')
    lijst = []
    for woord in splits:
        lijst.append(len(woord))
    berekening = sum(lijst)/len(lijst)
    print(berekening)

gemiddelde()


