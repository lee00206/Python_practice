import random

number1 = eval(input("첫 번째 정수를 입력하세요: "))
number2 = eval(input("두 번째 정수를 입력하세요: "))

if number1 > number2:
    max = number2
else:
    max = number1

for i in range(max, 0, -1):
    if (number1 % max == 0) and (number2 % max == 0):
        break
    else:
        max = max - 1

print(number1, "와", number2, "의 최대공약수는", max, "입니다.")
