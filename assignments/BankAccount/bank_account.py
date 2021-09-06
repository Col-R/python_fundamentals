class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        # Make user class later
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance = self.balance - 5

        return self
    def display_account_info(self):
        print (f'Your balance is: ${self.balance}')
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.int_rate * self.balance)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

acc1 = BankAccount(.02, 1000)
# acc1.deposit(300).deposit(250).deposit(500).withdraw(80).yield_interest().display_account_info()

acc2 = BankAccount(.02, 2000)
# acc2.deposit(100).deposit(650).withdraw(150).withdraw(800).withdraw(425).withdraw(390).yield_interest().display_account_info()

BankAccount.print_all_accounts()
