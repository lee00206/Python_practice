def displaySortedNumbers(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            print("정렬된 숫자는", num1, num2, num3, "입니다.")
        else:
            print("정렬된 숫자는", num1, num3, num2, "입니다.")
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print("정렬된 숫자는", num2, num1, num3, "입니다.")
        else:
            print("정렬된 숫자는", num2, num3, num1, "입니다.")
    else:
        if num1 > num2:
            print("정렬된 숫자는", num3, num1, num2, "입니다.")
        else:
            print("정렬된 숫자는", num3, num2, num1, "입니다.")
