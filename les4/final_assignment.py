leeftijd = int(input('Wat is jouw leeftijd: '))
weekendrit = input('Is het weekend: ')
afstandKM = int(input('Wat was jouw afstand KM: '))

print(weekendrit)

def standaardprijs(afstandKM):
    if afstandKM <0: afstandKM = 0
    if afstandKM >50:
        prijs = 15 + 0.60 * afstandKM
        return (prijs)
    else:
        prijs = 0.80 * afstandKM
        return (prijs)


def ritprijs(leeftijd, weekendrit, afstandKM):
   if weekendrit == 'ja' or weekendrit == 'JA':
       if leeftijd < 12 or leeftijd >= 65:
           print('U moet betalen: ' + str(standaardprijs(afstandKM) * 0.65))
       else:
           print('U moet betalen: ' + str(standaardprijs(afstandKM) * 0.6))

   else:
       if leeftijd < 12 or leeftijd >= 65:
           print('U moet betalen: ' + str(standaardprijs(afstandKM) * 0.7))
       else:
           print('U moet betalen: ' + str(standaardprijs(afstandKM)))

ritprijs(leeftijd, weekendrit, afstandKM)

