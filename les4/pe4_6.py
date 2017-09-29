lijst = ['a', 'b', 'c']
def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

print(lijst)
wijzig(lijst)
print(lijst)

