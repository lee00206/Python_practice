annualInterestRate = eval(input("연이율을 입력하세요(예. 7.25): "))
monthlyInterestRate=annualInterestRate/1200

numberOfYears = eval(input("상환년수를 정수로 입력하세요(예. 5): "))

loanAmount = eval(input("대출금을 입력하세요(예. 120000950): "))

monthlyPayment = loanAmount*monthlyInterestRate/(1 - 1/(1+monthlyInterestRate)**(numberOfYears*12))
totalPayment = monthlyPayment*numberOfYears*12

print("월상환금은",int(monthlyPayment*100)/100,"입니다")
print("총상환금은",int(totalPayment*100)/100,"입니다.")

