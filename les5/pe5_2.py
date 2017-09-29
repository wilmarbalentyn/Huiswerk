kaartnummer = open ('kaartnummer.txt')
info = kaartnummer.readlines()
for i in info:
  splits = i.split(sep=',')
  print(splits[1].strip('\n'), 'kaartnummer: ',splits[0])
kaartnummer.close()

