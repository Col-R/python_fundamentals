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
        pass
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

# Overriding and Polymorphism
# In these cases you want to override the function, effectively replacing the functionality. To do this, just define a function with the same name in the child class.
class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")

class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")

dad = Parent()
son = Child()
dad.method_a()
son.method_a() #notice this overrides the Parent method!

# output invoking PARENT method_a!
# invoking CHILD method_a!

# Polymorphism
# Polymorphic behavior allows us to specify common methods in an "abstract" level and implement them in particular instances. It is the process of using an operator or function in different ways for different data input.

# We'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways
class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")

dude = GradStudent()
dude.pay_bill()
