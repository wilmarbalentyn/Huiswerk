kaartnummer = open ('kaartnummer.txt')
regel = kaartnummer.readlines()

optellen = 0
lijst = []

for regels in regel:
    optellen +=1
    delen = regels.split(',')
    lijst.append(delen[0])
print('Deze file telt: '+str(optellen)+ ' regels')

nums = max(lijst)
optellen = 0
for regels in lijst:
    optellen+=1
    if regels == nums:
        print('het grootste kaartnummer is: '+str(nums)+ ' en dat staat op regel ' +str(optellen))