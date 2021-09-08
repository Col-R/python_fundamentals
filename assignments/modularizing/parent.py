local_val = 'magical creature'
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return 'Hello'

print(square(5))
user = User("Luigi")
print(user.name)
print(user.say_hello())
