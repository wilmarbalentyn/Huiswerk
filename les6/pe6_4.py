studentencijfers = [[95,92,86],[66,75,54],[89,72,100],[34,0,0]]
def gemiddelde_per_student(studentencijfers):
  lijst = []
  for i in studentencijfers:
   gemiddelde =sum(i)/len(i)
   lijst.append(gemiddelde)
  return lijst
print(gemiddelde_per_student(studentencijfers))


def gemiddelde_van_alle_studenten(studentencijfers):
 lijst = gemiddelde_per_student(studentencijfers)
 gemiddelde = sum(lijst)/len(lijst)

 return gemiddelde
 # gemiddele = sum()_

print(gemiddelde_van_alle_studenten(studentencijfers))