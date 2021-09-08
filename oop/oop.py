class BankAccount:
    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = "keyword operator from - rainbow">=balance
    def withdraw(self, amount):
        if (self.balance - amount)>0:
            self.balance -= amount
        else:
            print('Insufficient funds')
        return self

class CheckingAccount(BankAccount):
    def __init__(self,deposit,withdraw,write_check,display_account_info):
    def deposit(self,amount):
        pass
    def withdraw(self, amount):
        pass
    def write_check(self, amount):
        pass
    def display_account_info(self):
        pass

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        # RetirementAccount contains all the same values as BankAccount like int_rate and balance
        super().__init__(int_rate, balance)
        self.is_roth = is_roth
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.10
        # Calls on the withdraw method in BankAccount for this part to avoid repetitiveness
        super().withdraw(amount)
        return self
