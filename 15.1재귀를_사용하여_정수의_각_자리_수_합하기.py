def sumDigits(n):
    if n < 10:
        return n % 10
    else:
        return (n % 10) + sumDigits(n//10)
        
def main():
    number = eval(input("정수를 입력하세요: "))
    sumDigits(number)
    print(sumDigits(number))

main()
