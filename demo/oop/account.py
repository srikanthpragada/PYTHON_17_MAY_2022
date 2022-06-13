class Account:
    minbal = 5000

    @staticmethod
    def getminbal():
        return Account.minbal


    # Constructor
    def __init__(self, acno, customer, balance=0):
        # Object attributes or Fields or Instance Variables
        self.acno = acno
        self.customer = customer
        self.balance = balance

    # Methods
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - Account.minbal >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance')


    def getbalance(self):
        return self.balance


a1 = Account(1, "Marshall")
a1.deposit(10000)
a1.deposit(20000)
a1.withdraw(5000)
print(a1.getbalance())

a2 = Account(2, "Tom", 5000)
a2.deposit(50000)
print(a2.getbalance())
