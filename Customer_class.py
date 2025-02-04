class Customer:
    def __init__(self, name, bal):
        self.name=name
        self.balance=bal
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Money Deposited Successfully")
        print("Updated Balance is:",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("ERROR: Insufficient Balance")
            return
        self.balance=self.balance-amount
        print("Money Withdrawn Successfully")
        print("Updated Balance is:",self.balance)
    def display(self):
        print("Balance is:",self.balance)
        
c1=Customer("Lakshay",100000)
c1.display()
c1.withdraw(50000)
c1.deposit(150000)