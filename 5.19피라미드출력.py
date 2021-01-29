number = eval(input("1과 15 사이의 정수를 입력하세요: "))


for i in range(1, number+1):
    print("   "*(number-i), end = ' ')
    for j in range(i, 1, -1):
        print(format(j, "^2d"), end = ' ')
    for k in range(1, i+1):
        print(format(k, "^2d"), end = ' ')
    print()

        
