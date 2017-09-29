kluizen = open('kluizen.txt')
regel = kluizen.readlines()

optellen = 0
lijst = []
def toon_aantal_kluizen_vrij():
    for regels in regel:
        optellen += 1
        delen = regels.split(',')
        lijst.append(delen[0])
    print('Deze file telt: ' + str(optellen) + ' regels')

