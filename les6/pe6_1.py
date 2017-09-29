
def seizoen(maand):
    if maand >= 13 or maand <=0:
        return 'Maand is onjuist'
    elif maand >= 3 and maand <=5:
        return 'Lengte'
    elif maand >=9 and  maand <=11:
        return 'Herft'
    elif maand >= 6 and maand <=8:
        return 'Zomer'
    elif maand == 12 or maand <= 2:
        return 'Winter'


VLmaand =int(input('Welke maand is:'))
print(seizoen(VLmaand))