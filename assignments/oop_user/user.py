class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self, amount):
        self.balance -= amount
        print(f"{self.name}, you have withdrawn ${amount}")
        return self
    def make_deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, you have deposited ${amount}")
        return self
    def display_user_balance(self):
        print(f"{self.name}, your balance is ${self.balance}")
        return self
    def transfer_money(self, target, amount):
        self.balance -= amount
        target.balance += amount
        print(f"{self.name}, your balance is ${self.balance}")
        print(f"{target.name}, your balance is ${target.balance}")
        return self

hamilton = User('hamilton', 1000)
peggy = User('peggy', 810)
hercules = User('hercules', 450)

hamilton.make_deposit(55).make_deposit(55).make_deposit(55).make_withdrawal(250).display_user_balance()

peggy.make_deposit(25).make_deposit(38).make_withdrawal(12).make_withdrawal(80).display_user_balance()

hercules.make_deposit(310).make_withdrawal(35).make_withdrawal(190).make_withdrawal(80).display_user_balance()

hamilton.transfer_money(hercules, 250)
