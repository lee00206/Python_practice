import random

number1 = random.randint(0,9)
number2 = random.randint(0,9)

print(number1, "+", number2, "= ?")

answer = eval(input("정답을 입력하세요: "))

if number1+number2 == answer:
    print(number1, "+", number2, "를 더한 값은", answer, "이 맞습니다.")
else:
    print(number1, "+", number2, "를 더한 값은", answer, "이 아닙니다.")

