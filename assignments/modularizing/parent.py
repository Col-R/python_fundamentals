local_val = 'magical creature'
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return 'Hello'

# This conditional allows us to run certain blocks of code depending on which file they're in
if __name__ == "__main__":
    print('the file is being executed directly')
else:
    print('the file is being executed because it is imported by another file, this file is called', __name__)
    pass



# print(square(5))
# user = User("Luigi")
# print(user.name)
# print(user.say_hello())
# print(__name__)
