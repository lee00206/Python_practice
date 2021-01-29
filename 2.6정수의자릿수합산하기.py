number = eval(input("0과 1000 사이의 정수를 입력하세요: "))

hundred = number//100
numberMinusHundred = number - hundred*100

ten = numberMinusHundred//10
numberMinusTen = numberMinusHundred - ten*10

plusall = hundred+ten+numberMinusTen

print(plusall)
