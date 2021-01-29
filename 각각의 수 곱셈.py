numA = int(input('숫자 A를 입력하세요: '))
numB = int(input('숫자 B를 입력하세요: '))

numAlist = []
numBlist = []

portion = 10

while numA >= portion:
    numAremainder = numA % portion
    numA = (numA - numAremainder)//10
    numAlist.append(numAremainder)
    if numA < portion:
        numAlist.append(numA)

while numB >= portion:
    numBremainder = numB % portion
    numB = (numB - numBremainder)//10
    numBlist.append(numBremainder)
    if numB < portion:
        numBlist.append(numB)

total = 0

for i in range(0, len(numAlist)):
    for j in range(0, len(numBlist)):
        total = total + numAlist[i]*numBlist[j]

print(total)
