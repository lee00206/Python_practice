amount = eval(input("금액을 입력하세요: "))

thousAmount = amount // 1000
thousMinus = amount % 1000

fiveHundAmount = thousMinus // 500
fiveHundMinus = thousMinus % 500

oneHundAmount = fiveHundMinus // 100
oneHundMinus = fiveHundMinus % 100

fiftyAmount = oneHundMinus // 50
fiftyMinus = oneHundMinus % 50

tenAmount = fiftyMinus // 10
tenMinus = fiftyMinus % 10

print("천원짜리는", thousAmount, "장,", "500원은", fiveHundAmount, "개,", "100원은", oneHundAmount, "개, 50원은", fiftyAmount, "개, 10원은", tenAmount, "1원은", tenMinus, "개 입니다.")
