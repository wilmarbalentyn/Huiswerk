# tekstbestand maken
# append
#naam toevoegen in het lijst samen met de tijd

import time
try:
    file = open('hardlopers.txt', 'a') # append toevoegen
except:
    file = open('hardlopers.txt', 'w') # schrijven van bestand

file.write(time.strftime('%a %d %b %Y:%H:%M: %S ',time.localtime())+ input('Voeg jouw naam in:')+'\n')

