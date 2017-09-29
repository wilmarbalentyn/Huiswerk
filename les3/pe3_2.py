leeftijd = int (input('Geef je leeftijd: '))
nederland_Paspport = str (input('Heb je een Nederlandse Passport: '))

if leeftijd >= 18 and nederland_Paspport == 'ja':
    print('Je mag stemmen')
else:
    print('Je mag niet stemmen')