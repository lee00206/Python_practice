number = eval(input("1과 15 사이의 정수를 입력하세요: "))

column = 1
line1 = column
line2 = 1

while column < number+1:
    print("   "*(number-column), end = ' ')
    while line1 > 1:
        print(format(line1, "^2d"), end = ' ')
        line1 = line1 - 1
    while line2 < column+1:
        print(format(line2, "^2d"), end = ' ')
        line2 = line2 + 1
    print()
    column = column + 1
    line1 = column
    line2 = 1
