import math
# TODO: https://github.com/naikshubham/Object-Oriented-Python

class Account:
    def __init__(self):
        self.savingsInterestRate = 2.0
        self.checkingInterestRate = 8.0
    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def getInterestValue(self):
        pass


class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def withdrawal(self, value):
        self.balance -= value

    def getInterestValue(self, months):
        balanceWithInterest = math.pow(self.balance * (1 + self.savingsInterestRate), months) 
        return balanceWithInterest


class CheckingAccount(Account):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def withdrawal(self, value):
        self.balance -= value

    def getInterestValue(self, months):
        balanceWithInterest = math.pow(self.balance * (1 + self.checkingInterestRate), months) 
        return balanceWithInterest