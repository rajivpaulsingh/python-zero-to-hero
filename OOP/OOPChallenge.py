"""
For this challenge, create a bank account class that has two attributes:
- owner
- balance

and two methods:
- deposit
- withdraw

As an added requirement, withdrawals may not exceed the available balance.

Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, add_amount):
        self.balance = self.balance + add_amount
        print("Added {} to the balance".format(add_amount))

    def withdraw(self, rem_amount):
        if self.balance >= rem_amount:
            self.balance = self.balance = rem_amount
            print("Withdrawal accepted")
        else:
            print("Not enough funds!")
    
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

# Runnable
account1 = Account("Alpha", 100)
print(account1)

account1.deposit(50)
account1.withdraw(75)
account1.withdraw(500)