count = 0

number = eval(input("소수의 개수를 입력하세요: "))

print("첫", number, "개의 소수")

temporary = 1
prime = 0

while count < number:
    for i in range(1, temporary+1):
        if temporary % i != 0:
            prime = prime + 1
    if prime == temporary-2:
        print(format(temporary, "5d"), end = ' ')
        count = count + 1
        if count % 10 == 0:
            print()
    temporary = temporary + 1
    prime = 0

