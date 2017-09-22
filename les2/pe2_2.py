cijferICOR = float (input('Wat was jouw cijfer van ICOR: '))
cijferPROG = float (input('Wat was jouw cijfer van PROG: '))
cijferCSN = float (input('Wat is jouw cijfer van CSN: '))
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30
overzicht = 'Mijn cijfer is: ', gemiddelde, 'en  leven een beloning van €', beloning
print(gemiddelde)
print(beloning)
print(overzicht)