class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \n Balance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete.")
        self.getBalance()
        print("\n***************************************")
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry, account{self.name}, is low, kindly add more deposit or send lower amount, {self.name} account balance is ${self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw unsuccessful: {error}')

    def transfer(self, amount, account):
        try:
            print("\n***************************************\n\nBeginning transfer...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer complete!✅\n\n')
        except BalanceException as error:
            print(f'\nTransfer unsuccessful. ❌{error}')
    
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\n Deposit Complete.")
        self.getBalance()

class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount +self.fee)
            print("\nWithdraw completed. ")
        except BalanceException as error:
            print(f'\n Withdraw unsuccessful.{error}')