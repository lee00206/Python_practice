def main():
    index = eval(input("피보나치 수에 대한 인덱스를 입력하세요: "))
    print(index, "번째 피보나치 수는", fib(index), "입니다.")

def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)
