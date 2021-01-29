def m(i):
    if i == 1:
        return 1/2
    else:
        return i/(i+1) + m(i-1)

def main():
    number = eval(input("수를 입력하세요: "))
    print(m(number))

main()
