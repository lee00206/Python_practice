from Account import Account

def main():
    my = Account(id = 1122, balance = 20000000, annualInterestRate = 4.5)
    print(my.withdraw(2500000))
    print(my.deposit(3000000))

    print("ID는", my.getid(), "의 잔고는", my.getbalance(), "원, 월이율은", my.getMonthlyInterestRate(),
          "% 이며, 월이자는", my.getMonthlyInterest(), "원 입니다.")

main()
