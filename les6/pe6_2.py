def Newlijst(input):
    lijst =[]
    for woord in input:
        if len(woord) ==4:
            lijst.append(woord)
    return lijst

boodschaplist =eval(input('geeft lijst net minimaal 10 strings: '))
print('de nieuwe-gemaakte lijst met alle vier-letter strings is: {}'.format(Newlijst(boodschaplist)))









