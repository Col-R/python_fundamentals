# Class methods are defined with a decorator @classmethod. They belong to the class itself instead of the instance. Instead of implicitly passing self into the method, we pass cls. This is reference to the class.
class BankAccount:
    # class attribute
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    # class method to change the name of the bank
    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
    # class method to get balance of all accounts
    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            sum += account.balance
        return sum
