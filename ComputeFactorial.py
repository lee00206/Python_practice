def main():
    n = eval(input("양의 정수를 입력하세요: "))
    print(n, "의 팩토리얼은", factorial(n), "입니다.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

main()
