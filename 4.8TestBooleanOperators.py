number = eval(input("정수를 입력하세요: "))

if number % 2 == 0 and number % 3 == 0:
    print(number, "은/는 2와 3 모두로 나누어집니다.")

if number % 2 == 0 or number % 3 == 0:
    print(number, "은/는 2 또는 3으로 나누어집니다.")

if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print(number, "은/는 2 또는 3으로 나누어지지만, 두 수 모두로 나누어지지는 않습니다.")
    
