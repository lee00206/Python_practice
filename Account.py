class Account:
    def __init__(self, id = 0, balance = 100000, annualInterestRate = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def getid(self):
        return self.__id

    def getbalance(self):
        return self.__balance

    def getannualInterestRate(self):
        return self.__getannualInterestRate

    def getMonthlyInterestRate(self):
        return self.__annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.__balance * (self.getMonthlyInterestRate()/100)

    def withdraw(self, minus):
        self.__balance =  self.__balance - minus
        return self.__balance

    def deposit(self, add):
        self.__balance = self.__balance + add
        return self.__balance
