
def invoer():
    lijst ="5-9-7-1-7-8-3-2-4-8-7-9"
    getal = lijst.split(sep="-")
    gesorteerdlijst =[]
    for word in getal:
        gesorteerdlijst.append(int(word))
        gesorteerdlijst.sort()
    return gesorteerdlijst
print(invoer())
print('Grootste getal: ', str(max(invoer())),' en Kleinste getal: ',str(min(invoer())))
print('Aantal getallen: ', str(len(invoer())), 'en de SOM van de getallen zijn: ', str(sum(invoer())))
print('Gemidelde: ',sum(invoer())/len(invoer()))

