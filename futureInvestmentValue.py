def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    print(format("년 수", "<20s"), format("미래 투자가치", ">27s"))
    monthlyInterestRate = monthlyInterestRate / 1200
    for i in range(1, years+1):
        future = (investmentAmount * ((1 + monthlyInterestRate) ** (i * 12)))
        print(format(i, "<20.0f"), format(future, ">30.2f"))
        
        
