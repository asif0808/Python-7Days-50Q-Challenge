# Create a class to represent a bank account.
class Bank:
    def __init__(self,name,age,balance=0):
        self.name=name
        self.age=age
        self.balance=500
    def account_info(self):
        return f'Account holder name is {self.name} Balance: {self.balance} and Age is {self.age}'
    def credit(self):
        amount=int(input('enter amount: '))
        self.balance+=amount
        return f'new balance is: {self.balance}'
    def withdraw(self):
        amount=int(input('enter withdraw amount: '))
        if amount>(self.balance-500):
            return 'Insufficient Balance'
        else:
            return f'Amount debited, Current Balance: {self.balance-amount}'
    @classmethod
    def check_amount(cls,balance):
        return f'Balance:{balance}'
user=Bank('aasif',22)
print(user.account_info())
print(user.credit())
print(user.withdraw())
Bank.check_amount(user.balance)