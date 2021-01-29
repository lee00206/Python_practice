monthlysaving = eval(input("월저축액: "))
interestrate = eval(input("연이율: "))

monthlyinterest = (interestrate/100)/12

month = eval(input("개월 수: "))

count = 0
compound = 0

while count<month:
    compound = (monthlysaving+compound)*(1+monthlyinterest)
    count=count+1

print("6개월 후 계좌의 잔고는",compound,"입니다")
