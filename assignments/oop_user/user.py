class User:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def make_withdrawal(self, amount):
        self.balance -= amount
        print(f"{self.name}, you have withdrawn ${amount}")
    def make_deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, you have deposited ${amount}")
    def display_user_balance(self):
        print(f"{self.name}, your balance is ${self.balance}")
    def transfer_money(self, target, amount):
        self.balance -= amount
        target.balance += amount
        print(f"{self.name}, your balance is ${self.balance}")
        print(f"{target.name}, your balance is ${target.balance}")

hamilton = User('hamilton', 1000)
peggy = User('peggy', 810)
hercules = User('hercules', 450)

hamilton.make_deposit(55)
hamilton.make_deposit(55)
hamilton.make_deposit(55)
hamilton.make_withdrawal(250)
hamilton.display_user_balance()

peggy.make_deposit(25)
peggy.make_deposit(38)
peggy.make_withdrawal(12)
peggy.make_withdrawal(80)
peggy.display_user_balance()

hercules.make_deposit(310)
hercules.make_withdrawal(35)
hercules.make_withdrawal(190)
hercules.make_withdrawal(80)
hercules.display_user_balance()

hamilton.transfer_money(hercules, 250)
